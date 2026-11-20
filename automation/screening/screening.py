#!/usr/bin/env python3
"""Cribado por tandas del universo de etapa 1 (tareas A5/A6 del plan).

Una llamada por empresa, en secuencia y sin reintentos. El paquete de cada empresa sale
de la Release del universo (ZIP con huella fija): la respuesta de etapa 1 y las hojas del
Excel evaluado pasadas a CSV en solo lectura. El control de gasto no se reimplementa: por
cada empresa se configura y ejecuta critical_review.run de AUTO1 (tope acumulado, reserva
create-only, una sola llamada, estados de coste, publicación en la rama de registro). Aquí
se añaden el máximo de la tanda, la parada al tope y el informe de la tanda.
"""
import argparse
import base64
import contextlib
import csv
import datetime
from decimal import Decimal, InvalidOperation
import hashlib
import io
import json
import math
import os
from pathlib import Path, PurePosixPath
import re
import subprocess
import sys
import time
import xml.etree.ElementTree as ET
import zipfile

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / 'automation/direct_analysis'))
import direct_analysis as da  # noqa: E402  (importa critical_review y pilot de AUTO1)

cr, pilot = da.cr, da.pilot

ENCARGO_PATH = 'automation/screening/ENCARGO_CRIBADO.md'
EXCEPTIONS_PATH = 'automation/screening/excepciones_ceguera.json'
CODE_PATHS = ('automation/screening/screening.py', ENCARGO_PATH, EXCEPTIONS_PATH) + tuple(da.CODE_PATHS)

# --- Release del universo (subida por la persona responsable el 18-nov-2026) -----------
RELEASE = {'tag': 'universo-etapa1-20261118', 'asset': 'universo_etapa1.zip.zip',
           'sha256': '4d30f7352948fe7e7fe3b133386eabedbddcc71d997e972a1c6db7964d58b0a9',
           'bytes': 9222746, 'empresas': 117}
ZIP_ROOT = 'EMPRESAS_LOTES_COMPLETOS'
COMPANY = re.compile(r'[A-Za-z0-9][A-Za-z0-9_-]{0,39}')
# Lista blanca: solo estos nombres dentro de la carpeta de cada empresa. Cualquier otro
# archivo invalida la Release entera (no se elige a mano qué se manda).
KINDS = {'_evaluada.xlsx': 'libro', '_respuesta.md': 'respuesta', '_cambios_v2.md': 'cambios_v2'}
REQUIRED = ('libro', 'respuesta')
# Hojas del Excel que se vuelcan. «Guía Simply Wall St» (instrucciones genéricas de la
# plantilla) y «Opciones» (listas desplegables) no llevan datos de la empresa.
SHEETS = {'Análisis': 'hoja_analisis', 'Control maestro': 'hoja_control_maestro'}
MAX_RELEASE_BYTES = 50_000_000
MAX_MD_BYTES = 1_000_000
MAX_XLSX_BYTES = 10_000_000
MAX_XML_BYTES = 30_000_000
NO_VALUE = '#SIN_VALOR_CALCULADO'

# --- Límites de gasto (techos del código; los valores los pone la persona) -------------
HARD_MAX_COMPANY_USD = Decimal('2')
HARD_MAX_BATCH_USD = Decimal('30')
MAX_COMPANIES = 20
TASA = '9 % (provisional, decisión de la persona responsable)'
# Decisión C-ARR de la persona responsable (ronda 2): los arrendamientos se cuentan una sola
# vez, en el flujo. Va en cada paquete y la escribe el código en cada resultado.
CONVENCION_ARRENDAMIENTOS = ('C-ARR (decisión de la persona responsable): los arrendamientos se cuentan una sola '
                             'vez, en el flujo. El alquiler se resta de la caja libre; la deuda, deuda/EBITDA y '
                             'deuda/caja libre se miden sin arrendamientos; el pasivo por arrendamientos se muestra '
                             'aparte, como dato.')
CONDICIONES = ('Cifras de la etapa 1 tal como las guardó la hoja, a su fecha de análisis; sin las decisiones '
               'posteriores (P-O1, P-O2, F1-A/F1-B, D-US1/2, D-WM) ni verificación contra la fuente oficial.')
# Decisión C-EX de la persona responsable (ronda 2): las seis empresas del examen quedan
# fuera del cribado hasta después del 23-nov-2026. Lista cerrada: quitarla es un cambio
# de código que se revisa.
EXCLUIDAS = ('Ahold', 'Jumbo', 'Zoetis', 'Elis', 'Vinci', 'WasteManagement')
EXCLUIDA = 'EMPRESA_DEL_EXAMEN_EXCLUIDA_HASTA_DESPUES_DEL_23_NOV'
OK_STATES = ('PREPARADO_SIN_API', 'AUDITORIA_DOCUMENTAL_PENDIENTE_ACEPTACION')
# Fallos antes de reservar que solo afectan a esa empresa: se registra y se sigue.
COMPANY_ONLY = ('COSTE_MAXIMO_INSUFICIENTE_NO_SE_RECORTA', 'PAQUETE_SUPERA_CONTEXTO_DEL_MODELO_NO_SE_RECORTA',
                'RESERVA_SUPERA_2_USD', 'CONTEO_INVALIDO')
# Plazo de la tanda: no se empieza una empresa si no cabe su peor caso (stream de AUTO1 +
# socket + publicación) antes del timeout del job.
PER_CALL_WORST_SECONDS = cr.STREAM_DEADLINE_SECONDS + 60 + 120
# Salida máxima del cribado: la de AUTO1 (32 768), no la del análisis directo (65 536, solo
# en su `configured`); el plazo del stream sigue siendo el de AUTO1 (720 s), que la tanda
# usa arriba para no empezar una empresa que no quepa en el timeout del job.
MAX_OUTPUT = 32768
# Supuesto para el coste orientativo del dry-run (no es la cota): la ejecución real del
# análisis directo con Opus 5.5 high (unos 388 000 tokens de entrada, 1,9 USD) gastó unos
# 17 000 tokens de salida; el cribado devuelve un JSON mucho más corto.
ROUGH_OUTPUT_TOKENS = 15_000
ROUGH_BYTES_PER_TOKEN = 3.5


def digest(raw):
    return pilot.digest(raw)


# --- Lectura de la Release -------------------------------------------------------------
class Release:
    def __init__(self, zf, companies, sha256):
        self.zip, self.companies, self.sha256 = zf, companies, sha256


def slug(name):
    return name.lower().replace('_', '-')


def open_release(path, expected=RELEASE):
    """ZIP con la huella y el tamaño fijados; inventario estricto por lista blanca."""
    path = Path(path)
    if not path.is_file() or path.is_symlink() or path.stat().st_size > MAX_RELEASE_BYTES:
        raise pilot.PilotError('RELEASE_NO_ENCONTRADA_O_DEMASIADO_GRANDE')
    raw = path.read_bytes()
    if len(raw) != expected['bytes'] or digest(raw) != expected['sha256']:
        raise pilot.PilotError('RELEASE_HUELLA_DISTINTA_DE_LA_FIJADA')
    try:
        zf = zipfile.ZipFile(io.BytesIO(raw))
        infos = zf.infolist()
    except zipfile.BadZipFile:
        raise pilot.PilotError('RELEASE_NO_ES_ZIP') from None
    companies, slugs = {}, {}
    for info in infos:
        name = info.filename
        parts = name.split('/')
        if ('\\' in name or '\0' in name or PurePosixPath(name).is_absolute() or parts[0] != ZIP_ROOT
                or any(p in ('.', '..') for p in parts) or info.flag_bits & 1
                or (info.external_attr >> 16) & 0o170000 == 0o120000):
            raise pilot.PilotError('RELEASE_CON_RUTA_NO_PERMITIDA:' + name[:120])
        if name == ZIP_ROOT + '/':
            continue
        if len(parts) != 3 or not COMPANY.fullmatch(parts[1]):
            raise pilot.PilotError('RELEASE_CON_RUTA_NO_PERMITIDA:' + name[:120])
        emp, fname = parts[1], parts[2]
        if slugs.setdefault(slug(emp), emp) != emp:
            raise pilot.PilotError('RELEASE_CON_EMPRESAS_DE_NOMBRE_AMBIGUO:' + emp)
        files = companies.setdefault(emp, {})
        if fname == '':
            if not info.is_dir():
                raise pilot.PilotError('RELEASE_CON_RUTA_NO_PERMITIDA:' + name[:120])
            continue
        kind = next((k for suffix, k in KINDS.items() if fname == emp + suffix), None)
        if kind is None or kind in files or info.is_dir():
            raise pilot.PilotError('ARCHIVO_NO_PERMITIDO_EN_LA_RELEASE:' + name[:120])
        files[kind] = info
    for emp, files in companies.items():
        if any(k not in files for k in REQUIRED):
            raise pilot.PilotError('EMPRESA_INCOMPLETA_EN_LA_RELEASE:' + emp)
    if len(companies) != expected['empresas']:
        raise pilot.PilotError('RELEASE_CON_OTRO_NUMERO_DE_EMPRESAS')
    return Release(zf, companies, digest(raw))


def _member(zf, info, limit):
    if info.file_size > limit:
        raise pilot.PilotError('ARCHIVO_DEMASIADO_GRANDE_NO_SE_RECORTA:' + info.filename[:120])
    with zf.open(info) as fh:
        raw = fh.read(limit + 1)
    if len(raw) > limit:
        raise pilot.PilotError('ARCHIVO_DEMASIADO_GRANDE_NO_SE_RECORTA:' + info.filename[:120])
    return raw


def _text(raw, where):
    if b'\0' in raw:
        raise pilot.PilotError('ARCHIVO_NO_ES_TEXTO:' + where)
    try:
        return raw.decode('utf-8')
    except UnicodeDecodeError:
        raise pilot.PilotError('ARCHIVO_NO_ES_TEXTO:' + where) from None


# --- XLSX en solo lectura, solo con la biblioteca estándar ------------------------------
NS = '{http://schemas.openxmlformats.org/spreadsheetml/2006/main}'
NS_REL = '{http://schemas.openxmlformats.org/officeDocument/2006/relationships}'
NS_PKG = '{http://schemas.openxmlformats.org/package/2006/relationships}'
DATE_FORMATS = {14, 15, 16, 17, 18, 19, 20, 21, 22, 45, 46, 47}
CELL_REF = re.compile(r'([A-Z]{1,3})([0-9]{1,7})')


def _xml(book, name, required=True):
    """XML de un miembro del libro; sin DTD ni entidades (nunca se resuelven)."""
    try:
        info = book.getinfo(name)
    except KeyError:
        if required:
            raise pilot.PilotError('LIBRO_INCOMPLETO:' + name) from None
        return None
    raw = _member(book, info, MAX_XML_BYTES)
    if b'<!DOCTYPE' in raw or b'<!ENTITY' in raw or b'\0' in raw:
        raise pilot.PilotError('LIBRO_XML_NO_ADMITIDO:' + name)
    try:
        return ET.fromstring(raw)
    except ET.ParseError:
        raise pilot.PilotError('LIBRO_XML_INVALIDO:' + name) from None


def _all_text(node):
    """Texto de un <si> o <is>: sus <t> directos y los de cada <r>, sin la fonética (<rPh>)."""
    parts = [t.text or '' for t in node.findall(NS + 't')]
    parts += [t.text or '' for r in node.findall(NS + 'r') for t in r.findall(NS + 't')]
    return ''.join(parts)


def _date_styles(book):
    root = _xml(book, 'xl/styles.xml', required=False)
    if root is None:
        return set()
    custom = {}
    fmts = root.find(NS + 'numFmts')
    for f in (fmts if fmts is not None else []):
        code = re.sub(r'"[^"]*"|\[[^\]]*\]|\\.', '', f.get('formatCode', ''))
        custom[int(f.get('numFmtId', '-1'))] = bool(re.search(r'[dy]', code, re.I))
    xfs = root.find(NS + 'cellXfs')
    out = set()
    for i, xf in enumerate(xfs if xfs is not None else []):
        fid = int(xf.get('numFmtId', '0'))
        if fid in DATE_FORMATS or custom.get(fid):
            out.add(i)
    return out


def col_index(letters):
    n = 0
    for ch in letters:
        n = n * 26 + ord(ch) - 64
    return n


def col_letters(n):
    out = ''
    while n:
        n, r = divmod(n - 1, 26)
        out = chr(65 + r) + out
    return out


def _excel_date(value):
    try:
        days = float(value)
    except ValueError:
        return value
    if not math.isfinite(days) or not 0 < days < 2958466:
        return value
    moment = datetime.datetime(1899, 12, 30) + datetime.timedelta(days=days)
    return moment.date().isoformat() if days == int(days) else moment.isoformat(timespec='minutes')


def read_xlsx(raw):
    """{nombre de hoja: (CSV, celdas con fórmula sin valor calculado)} de los valores guardados.

    No calcula nada ni ejecuta macros: lee los valores que guardó la hoja. Una fórmula sin
    valor guardado se marca como #SIN_VALOR_CALCULADO. Las cifras se copian tal cual, sin
    redondear; solo las celdas con formato de fecha se pasan a fecha ISO.
    """
    try:
        book = zipfile.ZipFile(io.BytesIO(raw))
        names = book.namelist()
    except zipfile.BadZipFile:
        raise pilot.PilotError('LIBRO_NO_ES_XLSX') from None
    if any('vbaproject' in n.lower() or n.lower().endswith('.bin') for n in names):
        raise pilot.PilotError('LIBRO_CON_MACROS_O_BINARIOS')
    shared = []
    sst = _xml(book, 'xl/sharedStrings.xml', required=False)
    if sst is not None:
        shared = [_all_text(si) for si in sst.findall(NS + 'si')]
    dates = _date_styles(book)
    rels = {r.get('Id'): r.get('Target', '') for r in _xml(book, 'xl/_rels/workbook.xml.rels').findall(NS_PKG + 'Relationship')}
    sheets = _xml(book, 'xl/workbook.xml').find(NS + 'sheets')
    out = {}
    for sheet in (sheets if sheets is not None else []):
        target = rels.get(sheet.get(NS_REL + 'id'), '')
        target = target[1:] if target.startswith('/') else 'xl/' + target
        if not re.fullmatch(r'xl/worksheets/sheet[0-9]{1,3}\.xml', target):
            raise pilot.PilotError('LIBRO_CON_HOJA_NO_ADMITIDA')
        out[sheet.get('name')] = _sheet_csv(_xml(book, target), shared, dates)
    return out


def _sheet_csv(root, shared, dates):
    cells, missing = {}, 0
    data = root.find(NS + 'sheetData')
    for row in (data if data is not None else []):
        for c in row.findall(NS + 'c'):
            m = CELL_REF.fullmatch(c.get('r', ''))
            if not m:
                raise pilot.PilotError('LIBRO_CON_CELDA_SIN_REFERENCIA')
            kind, v, f = c.get('t', 'n'), c.find(NS + 'v'), c.find(NS + 'f')
            if kind == 'inlineStr':
                node = c.find(NS + 'is')
                value = _all_text(node) if node is not None else ''
            elif v is None:
                value = NO_VALUE if f is not None else ''
                missing += f is not None
            elif kind == 's':
                try:
                    value = shared[int(v.text)]
                except (ValueError, IndexError, TypeError):
                    raise pilot.PilotError('LIBRO_CON_TEXTO_COMPARTIDO_INVALIDO') from None
            elif kind == 'b':
                value = {'1': 'TRUE', '0': 'FALSE'}.get(v.text or '', v.text or '')
            else:
                value = v.text or ''
                if kind == 'n' and value and int(c.get('s', '0')) in dates:
                    value = _excel_date(value)
            if value != '':
                cells[(int(m.group(2)), col_index(m.group(1)))] = value
    width = max((col for _, col in cells), default=0)
    buf = io.StringIO()
    w = csv.writer(buf, lineterminator='\n')
    w.writerow(['fila'] + [col_letters(i) for i in range(1, width + 1)])
    for r in sorted({row for row, _ in cells}):
        w.writerow([r] + [cells.get((r, i), '') for i in range(1, width + 1)])
    return buf.getvalue(), missing


def csv_cells(text):
    """Mapa {('C', 46): valor} de un CSV de read_xlsx (para las comprobaciones mecánicas)."""
    rows = list(csv.reader(io.StringIO(text)))
    if not rows or rows[0][:1] != ['fila']:
        return {}
    header, out = rows[0], {}
    for row in rows[1:]:
        for letters, value in zip(header[1:], row[1:]):
            if value != '':
                out[(letters, int(row[0]))] = value
    return out


# --- Paquete por empresa -----------------------------------------------------------------
def blind_codes(source, blind):
    """Las capas de ceguera del análisis directo sobre el texto ya preparado: todos los fallos."""
    blobs, chunks = blind
    raw = source['text'].encode('utf-8')
    codes = []
    blob = hashlib.sha1(b'blob %d\0' % len(raw) + raw).hexdigest()
    if blob in blobs:
        codes.append('COPIA_DE_MATERIAL_CIEGO:' + blobs[blob])
    squashed = da.squash(source['text'])
    for marker in da.CONTENT_MARKERS:
        if marker in squashed:
            codes.append(f"CONTENIDO_PROHIBIDO_EN_EL_PAQUETE:{source['id']}:{marker}")
    hits = overlap_all(squashed, chunks)
    if hits:
        codes.append(f"SOLAPE_CON_MATERIAL_CIEGO:{source['id']}:" + '|'.join(hits))
    return codes


def overlap_all(squashed, chunks):
    """Todas las rutas ciegas con las que el texto (ya normalizado) comparte un fragmento.

    da.overlap se para en la primera; una excepción ligada a esa ruta taparía otra.
    """
    if not chunks:
        return []
    n = da.OVERLAP_CHARS
    return sorted({chunks[s] for s in (squashed[i:i + n] for i in range(len(squashed) - n + 1)) if s in chunks})


def load_exceptions(text):
    """{(empresa, archivo, sha256, código): motivo} del archivo versionado de excepciones."""
    try:
        doc = json.loads(text, object_pairs_hook=da._sin_duplicadas)
        out = {}
        for e in doc['excepciones']:
            if set(e) != {'empresa', 'archivo', 'sha256', 'codigo', 'motivo'} or not all(isinstance(v, str) and v for v in e.values()):
                raise ValueError
            if not re.fullmatch(r'[0-9a-f]{64}', e['sha256']):
                raise ValueError
            out[(e['empresa'], e['archivo'], e['sha256'], e['codigo'])] = e['motivo']
        return out
    except (ValueError, KeyError, TypeError):
        raise pilot.PilotError('EXCEPCIONES_DE_CEGUERA_INVALIDAS') from None


def load_company(release, empresa, blind, exceptions=None):
    """(paquete, excepciones aplicadas). Las excepciones no se envían al modelo."""
    if empresa not in release.companies:
        raise pilot.PilotError('EMPRESA_NO_ESTA_EN_LA_RELEASE')
    if empresa in EXCLUIDAS:
        raise pilot.PilotError(EXCLUIDA)
    files = release.companies[empresa]
    sources = []
    for kind in ('respuesta', 'cambios_v2'):
        if kind in files:
            raw = _member(release.zip, files[kind], MAX_MD_BYTES)
            sources.append({'id': kind, 'path': files[kind].filename, 'sha256': digest(raw), 'bytes': len(raw),
                            'text': _text(raw, kind)})
    raw = _member(release.zip, files['libro'], MAX_XLSX_BYTES)
    book_sha = digest(raw)
    sheets = read_xlsx(raw)
    for name, sid in SHEETS.items():
        if name not in sheets:
            raise pilot.PilotError('HOJA_AUSENTE_EN_EL_LIBRO:' + sid)
        text, missing = sheets[name]
        sources.append({'id': sid, 'path': f"{files['libro'].filename}#{name}", 'origen_sha256': book_sha,
                        'sha256': digest(text.encode('utf-8')), 'bytes': len(text.encode('utf-8')),
                        'formulas_sin_valor_calculado': missing, 'text': text})
    applied = []
    for s in sources:
        for code in blind_codes(s, blind):
            motivo = (exceptions or {}).get((empresa, s['id'], s['sha256'], code))
            if motivo is None:
                raise pilot.PilotError(code)
            applied.append({'archivo': s['id'], 'sha256': s['sha256'], 'codigo': code, 'motivo': motivo})
    return ({'empresa': empresa, 'tarea': 'cribado', 'tasa_descuento': TASA,
             'convencion_arrendamientos': CONVENCION_ARRENDAMIENTOS,
             'fecha_hoja': sheet_date(sources), 'release_sha256': release.sha256, 'libro_sha256': book_sha,
             'hojas_omitidas': sorted(set(sheets) - set(SHEETS)), 'sources': sources}, applied)


def sheet_date(sources):
    """La «Fecha de análisis» de la hoja, tal como está (ISO o texto); None si no se encuentra."""
    for s in sources:
        if s['id'] == 'hoja_analisis':
            cells = csv_cells(s['text'])
            for (col, row), value in cells.items():
                if da.squash(value) == 'fechadeanalisis':
                    return cells.get((col_letters(col_index(col) + 1), row))
    return None


def build_bundle(package, encargo, task_id, code_sha):
    return da.build_bundle(package, encargo, task_id, code_sha)


def verify_code(root, code_sha):
    """El código y el encargo que se ejecutan son los bytes del SHA observado."""
    if not re.fullmatch(r'[0-9a-f]{40}', code_sha or ''):
        raise pilot.PilotError('SHA_INVALIDO')
    if da.git(root, 'rev-parse', 'HEAD').decode().strip() != code_sha:
        raise pilot.PilotError('SHA_NO_ES_EL_OBSERVADO')
    for path in CODE_PATHS:
        if (Path(root) / path).read_bytes() != da.git(root, 'show', f'{code_sha}:{path}'):
            raise pilot.PilotError('CODIGO_LOCAL_DISTINTO_DEL_SHA')
    return (da.git(root, 'show', f'{code_sha}:{ENCARGO_PATH}').decode('utf-8'),
            load_exceptions(da.git(root, 'show', f'{code_sha}:{EXCEPTIONS_PATH}').decode('utf-8')))


# --- Esquema pequeño de salida ------------------------------------------------------------
STR, ARR = {'type': 'string'}, {'type': 'array', 'items': {'type': 'string'}}
FILTROS = ('calidad', 'caja', 'balance', 'precio', 'encaje')
RESULTADOS = ['pasa', 'no_pasa', 'dudoso', 'no_aplica']
VEREDICTOS = ['estudiar_a_fondo', 'vigilar', 'descartar', 'demasiado_dificil', 'faltan_datos']
DCF = ['si', 'no', 'dudoso']
_FILTRO = da._obj({'resultado': da._enum(RESULTADOS), 'motivo': STR, 'dato_clave': STR})
SCHEMA = da._obj({
    'empresa': STR,
    'tipo_negocio': STR,
    'dcf_plantilla_aplica': da._enum(DCF),
    'motor_adecuado': STR,
    'filtros': da._obj({f: _FILTRO for f in FILTROS}),
    'pasivo_arrendamientos': STR,
    'veredicto_cribado': da._enum(VEREDICTOS),
    'que_lo_cambiaria': ARR,
    'que_falta': ARR,
})
SHEET_OF = {'analisis': 'hoja_analisis', 'controlmaestro': 'hoja_control_maestro'}
SHEET_REF = re.compile(r"'?(An[aá]lisis|Control maestro)'?!\$?([A-Z]{1,3})\$?([0-9]{1,7})", re.I)
FIGURE = re.compile(r'[0-9]')


def mechanical_checks(doc, bundle):
    """Avisos para la revisión humana; no aceptan ni rechazan el cribado."""
    notes = []
    if da.squash(doc['empresa']) != da.squash(bundle['empresa']):
        notes.append('El campo empresa no coincide con la carpeta del paquete.')
    f = doc['filtros']
    for name in FILTROS:
        x = f[name]
        if x['resultado'] in ('pasa', 'no_pasa') and not (FIGURE.search(x['motivo']) or FIGURE.search(x['dato_clave'])):
            notes.append(f'Filtro {name}: {x["resultado"]} sin ninguna cifra en motivo ni dato_clave.')
        if len(x['motivo']) > 400:
            notes.append(f'Filtro {name}: motivo de más de 400 caracteres.')
    cells = {s['id']: csv_cells(s['text']) for s in bundle['sources'] if s['id'] in SHEET_OF.values()}
    for name in FILTROS:
        for sheet, col, row in SHEET_REF.findall(f[name]['dato_clave']):
            sid = SHEET_OF[da.squash(sheet)]
            if (col.upper(), int(row)) not in cells.get(sid, {}):
                notes.append(f'Filtro {name}: dato_clave cita {sheet}!{col}{row}, celda vacía o inexistente en el paquete.')
    first = [f[k]['resultado'] for k in ('calidad', 'caja', 'balance')]
    v = doc['veredicto_cribado']
    if v in ('estudiar_a_fondo', 'vigilar') and 'no_pasa' in first:
        notes.append(f'Veredicto {v} con calidad, caja o balance en no_pasa.')
    if v == 'estudiar_a_fondo' and f['precio']['resultado'] == 'no_pasa':
        notes.append('Veredicto estudiar_a_fondo con el precio en no_pasa (¿vigilar?).')
    if v == 'descartar' and 'no_pasa' not in first + [f['precio']['resultado']]:
        notes.append('Veredicto descartar sin ningún filtro en no_pasa.')
    if f['encaje']['resultado'] == 'no_pasa' and v == 'descartar' and 'no_pasa' not in first + [f['precio']['resultado']]:
        notes.append('El encaje no elimina en este cribado.')
    if v == 'faltan_datos' and not doc['que_falta']:
        notes.append('Veredicto faltan_datos sin que_falta.')
    for key in ('que_lo_cambiaria', 'que_falta'):
        if len(doc[key]) > 3:
            notes.append(f'{key} con más de 3 elementos.')
    if not doc['pasivo_arrendamientos'].strip():
        notes.append('Pasivo por arrendamientos vacío (C-ARR: se da aparte, o «no consta en la hoja»).')
    free = da.fold(json.dumps(doc, ensure_ascii=False))
    if re.search(r'tamano de (la )?posicion|% de (la )?cartera|porcentaje de (la )?cartera', free):
        notes.append('Un texto menciona un tamaño de posición o un porcentaje de cartera.')
    return {'avisos': notes, 'nota': 'Comprobaciones mecánicas informativas: no acreditan la calidad económica.'}


def safe_checks(doc, bundle):
    try:
        return mechanical_checks(doc, bundle)
    except Exception as err:  # noqa: BLE001 - por diseño: nunca deja sin aceptar lo pagado
        return {'avisos': ['Comprobación mecánica no completada: ' + type(err).__name__],
                'nota': 'Comprobaciones mecánicas informativas: no acreditan la calidad económica.'}


def validate(response, bundle):
    if response.get('stop_reason') != 'end_turn':
        raise pilot.PilotError('RESPUESTA_INCOMPLETA')
    raw = ''.join(x.get('text', '') for x in response.get('content', [])
                  if isinstance(x, dict) and x.get('type') == 'text').strip()
    notes = []
    doc = da.leer_respuesta(raw, notes)
    doc = da.check_schema(da.normalize_enums(doc, SCHEMA, notes), SCHEMA)
    return {'cribado': doc, 'package_sha256': bundle['package_sha256'], 'normalizaciones': notes,
            'comprobaciones_mecanicas': safe_checks(doc, bundle)}


SCHEMA_EN_ENCARGO = ('\n\n## Esquema de la respuesta\n\nResponde solo con un objeto JSON que cumpla '
                     'exactamente este JSON Schema (todas las claves son obligatorias; sin texto antes ni '
                     'después). No añadas claves ni repitas ninguna; no uses null; dentro de los textos escapa '
                     'las comillas dobles como \\" y los saltos de línea como \\n. Un único objeto, en un único '
                     'bloque.\n\n')


def system_con_esquema(encargo):
    return encargo + SCHEMA_EN_ENCARGO + json.dumps(SCHEMA, ensure_ascii=False, sort_keys=True)


# --- Presentación --------------------------------------------------------------------------
def render(report, bundle, holder):
    out = ['# Cribado · ' + bundle['empresa'], '', 'Estado de la ejecución: `' + report['state'] + '`', '',
           'Cribado pendiente de revisión humana. No es una recomendación de compra, ni aceptación, '
           'ni aptitud para dinero real. Tasa 9 % provisional.', '',
           CONVENCION_ARRENDAMIENTOS, '', CONDICIONES, '',
           '| Campo | Valor |', '|---|---|',
           f"| Fecha de la hoja | {bundle.get('fecha_hoja') or '—'} |",
           f"| Tarea | {report['task_id']} |", f"| SHA del código | {report['code_sha']} |",
           f"| Huella del paquete (package_sha256) | {bundle['package_sha256']} |",
           f"| Huella del envío (bundle_sha256) | {report['bundle_sha256']} |",
           f"| Huella del encargo | {bundle['encargo_sha256']} |",
           f"| Huella de la Release | {bundle['release_sha256']} |",
           f"| Huella del libro | {bundle['libro_sha256']} |",
           f"| Modelo pedido / devuelto | {report['model_requested']} / {report.get('model_returned', '—')} |",
           f"| Esfuerzo | {report['effort_requested']} |", f"| Gramática del servidor | {holder.get('gramatica')} |",
           f"| Mensajes enviados | {report['api_messages_sent']} |",
           f"| Cota de entrada antes de llamar | {holder.get('input_tokens_upper_bound')} tokens |",
           f"| Reserva estimada antes de llamar | USD {holder.get('reserve_upper_bound_usd')} |"]
    if isinstance(report.get('usage'), dict):
        out.append(f"| Uso de tokens | entrada {report['usage'].get('input_tokens')}, salida {report['usage'].get('output_tokens')} |")
    if 'cost_status' in report:
        out.append(f"| Coste | {report['cost_status']}; estimado USD {report['estimated_cost_usd']};"
                   f" cota {report.get('cost_upper_bound_usd', report['estimated_cost_usd'])} |")
    out += ['', '| id | ruta | sha256 | bytes |', '|---|---|---|---|']
    out += [f"| {s['id']} | {s['path']} | {s['sha256']} | {s['bytes']} |" for s in bundle['sources']]
    if 'error' in report:
        out += ['', 'Error: `' + report['error'] + '`']
    if isinstance(report.get('api_error'), dict):
        out += ['', 'Error de la API: `' + json.dumps(report['api_error'], ensure_ascii=False).replace('`', "'") + '`']
    review = report.get('review')
    if review:
        c = review['cribado']
        out += ['', '## Salida del modelo (datos, sin acciones ejecutables)', '',
                f"Veredicto `{c['veredicto_cribado']}` · DCF de la plantilla aplica: `{c['dcf_plantilla_aplica']}`", '',
                '| Filtro | Resultado |', '|---|---|']
        out += [f"| {k} | {c['filtros'][k]['resultado']} |" for k in FILTROS]
        out += ['', '### Pasivo por arrendamientos (dato aparte)', ''] + da._block(c['pasivo_arrendamientos'])
        out += ['', '### Tipo de negocio y motor', ''] + da._block(c['tipo_negocio'] + '\n' + c['motor_adecuado'])
        for k in FILTROS:
            out += ['### ' + k, ''] + da._block(c['filtros'][k]['motivo'] + '\nDato clave: ' + c['filtros'][k]['dato_clave'])
        out += ['### Qué lo cambiaría', ''] + da._block('\n'.join('- ' + x for x in c['que_lo_cambiaria']))
        out += ['### Qué falta', ''] + da._block('\n'.join('- ' + x for x in c['que_falta']))
        out += ['### Comprobaciones mecánicas y normalizaciones', ''] + da._block(json.dumps(
            {'comprobaciones': review['comprobaciones_mecanicas'], 'normalizaciones': review['normalizaciones']},
            ensure_ascii=False, indent=2))
    return '\n'.join(out) + '\n'


def make_writer(bundle, holder):
    def write(output, report):
        output = Path(output)
        output.mkdir(parents=True, exist_ok=True)
        (output / 'report.json').write_bytes(pilot.canonical(report))
        try:
            text = render(report, bundle, holder)
        except Exception as err:  # noqa: BLE001 - la presentación nunca impide publicar lo pagado
            text = f"# Cribado\n\nEstado: `{report.get('state')}`\n\nPresentación no completada ({type(err).__name__}).\n"
        (output / 'report.md').write_text(text, encoding='utf-8')
    return write


# --- Configuración de AUTO1 por empresa -------------------------------------------------------
def parse_usd(raw, ceiling, code):
    if not isinstance(raw, str) or not re.fullmatch(r'[0-9]{1,3}(\.[0-9]{1,6})?', raw.strip()):
        raise pilot.PilotError(code + '_INVALIDO')
    value = Decimal(raw.strip())
    if not 0 < value <= ceiling:
        raise pilot.PilotError(code + '_FUERA_DEL_TECHO_DEL_CODIGO')
    return value


@contextlib.contextmanager
def configured(task_id, model, effort, max_usd, bundle, encargo, gramatica=False, holder=None, cache=None):
    if model not in da.MODELS:
        raise pilot.PilotError('MODELO_NO_AUTORIZADO')
    if effort not in da.EFFORTS:
        raise pilot.PilotError('ESFUERZO_INVALIDO')
    info, original_budget = da.MODELS[model], cr.budget
    system = system_con_esquema(encargo)

    def budget(b, count):
        if type(count) is int and count + MAX_OUTPUT > info['context']:
            raise pilot.PilotError('PAQUETE_SUPERA_CONTEXTO_DEL_MODELO_NO_SE_RECORTA')
        return original_budget(b, count)

    def payload(b):
        config = {'effort': cr.EFFORT}
        if gramatica:  # salidas estructuradas: solo si la persona lo pide (ver README)
            config['format'] = {'type': 'json_schema', 'schema': SCHEMA}
        return {'model': cr.MODEL, 'system': cr.SYSTEM,
                'messages': [{'role': 'user', 'content': pilot.canonical(b).decode()}],
                'thinking': {'type': 'adaptive'}, 'output_config': config}

    holder = {} if holder is None else holder
    holder.update(system_sha256=digest(system.encode('utf-8')), gramatica=bool(gramatica))
    values = dict(TASK=task_id, MODEL=model, EFFORT=effort, MAX_OUTPUT=MAX_OUTPUT, MAX_USD=max_usd,
                  INPUT_PRICE=info['input'], OUTPUT_PRICE=info['output'], SYSTEM=system, SCHEMA=SCHEMA,
                  payload=payload, validate=validate, write=make_writer(bundle, holder), budget=budget,
                  Register=cached_register({} if cache is None else cache))
    saved = {k: getattr(cr, k) for k in values}
    try:
        for k, v in values.items():
            setattr(cr, k, v)
        yield holder
    finally:
        for k, v in saved.items():
            setattr(cr, k, v)


def cached_register(cache):
    """cr.Register que relee una carpeta solo si cambia su SHA de árbol (H1).

    El listado de la API de contenidos trae el SHA de cada carpeta, que depende de su
    contenido: si no cambia, su reservation.json tampoco. Sin SHA en el listado se lee
    siempre, como AUTO1. Una reserva ilegible o sin cota sigue bloqueando.
    """
    class CachedRegister(cr.Register):
        def committed(self):
            total, entries = Decimal('0'), []
            for root in cr.REGISTER_ROOTS:
                listing = self._get(root)
                if listing is None:
                    continue
                if not isinstance(listing, list):
                    raise pilot.PilotError('REGISTRO_RESERVAS_NO_VERIFICABLE')
                for item in listing:
                    if not isinstance(item, dict) or item.get('type') != 'dir':
                        continue
                    name, sha = item.get('name'), item.get('sha')
                    if not isinstance(name, str) or not re.fullmatch(r'[A-Za-z0-9][A-Za-z0-9._-]{0,80}', name):
                        raise pilot.PilotError('REGISTRO_RESERVAS_NO_VERIFICABLE')
                    key = (root, name, sha) if isinstance(sha, str) and re.fullmatch(r'[0-9a-f]{40}', sha) else None
                    if key is not None and key in cache:
                        amount = cache[key]
                    else:
                        data = self._get(f'{root}/{name}/reservation.json')
                        if data is None:
                            amount = None
                        else:
                            try:
                                record = json.loads(base64.b64decode(''.join(data['content'].split()), validate=True))
                            except (KeyError, TypeError, AttributeError, ValueError, RecursionError):
                                raise pilot.PilotError('REGISTRO_RESERVAS_NO_VERIFICABLE') from None
                            amount = cr.exposure(record)
                        if key is not None:
                            cache[key] = amount
                    if amount is not None:
                        total += amount
                        entries.append({'path': f'{root}/{name}', 'usd': str(amount)})
            return total, entries
    return CachedRegister


class TrackingReceipt(cr.Receipt):
    """El recibo de AUTO1 con la tarea explícita; anota si llegó a intentar la reserva."""
    def __init__(self, http, sha, task):
        super().__init__(http, sha)
        self.base = f'/repos/{pilot.REPO}/contents/automation/coordination/reviews/{task}'
        self.reserve_attempted = False

    def put(self, name, content, create_only=False):
        if create_only:
            self.reserve_attempted = True
        return super().put(name, content, create_only)


class BatchLedger(pilot.Ledger):
    """Publica el informe de la tanda en una carpeta sin reservation.json (no cuenta como gasto)."""
    def __init__(self, http, sha, folder):
        super().__init__(http, sha)
        self.base = f'/repos/{pilot.REPO}/contents/automation/coordination/reviews/{folder}'


def task_id_for(run_id, empresa):
    return f'cribado-{run_id}-{slug(empresa)}'


def parse_companies(raw, release):
    if not isinstance(raw, str):
        raise pilot.PilotError('LISTA_DE_EMPRESAS_INVALIDA')
    names = [x for x in re.split(r'[\s,;]+', raw.strip()) if x]
    if not 1 <= len(names) <= MAX_COMPANIES:
        raise pilot.PilotError('LISTA_DE_EMPRESAS_DE_1_A_20')
    if len(set(names)) != len(names):
        raise pilot.PilotError('EMPRESA_REPETIDA_EN_LA_LISTA')
    for n in names:
        if not COMPANY.fullmatch(n) or n not in release.companies:
            raise pilot.PilotError('EMPRESA_NO_ESTA_EN_LA_RELEASE:' + n[:40])
    return names


def exposure_of(report, max_usd):
    """Lo que esta empresa compromete en la tanda: coste estimado si se conoce; si no, la cota."""
    status = report.get('cost_status')
    try:
        if status == 'CONOCIDO_ESTIMADO':
            return Decimal(report['estimated_cost_usd'])
        if status == 'INCIERTO' and report.get('cost_upper_bound_usd') is not None:
            return Decimal(report['cost_upper_bound_usd'])
    except (InvalidOperation, TypeError, KeyError):
        return max_usd
    return max_usd if report.get('api_messages_sent') else Decimal('0')


def register_exposure(http, run_id, cache=None):
    """Comprometido en la rama de registro por las tareas de esta tanda (todos sus intentos)."""
    _, entries = cached_register({} if cache is None else cache)(http).committed()
    prefix = f'automation/coordination/reviews/cribado-{run_id}-'
    return sum((Decimal(e['usd']) for e in entries if e['path'].startswith(prefix)), Decimal('0'))


# --- Preparación y tanda ------------------------------------------------------------------------
def prepare(release, names, encargo, run_id, code_sha, model, effort, max_usd, blind, exceptions=None, gramatica=False):
    """Paquetes y comprobación previa de cada empresa, sin red. Un fallo deja fuera solo a esa empresa."""
    rows = []
    for emp in names:
        task = task_id_for(run_id, emp)
        row = {'empresa': emp, 'task_id': task}
        try:
            package, row['excepciones_ceguera'] = load_company(release, emp, blind, exceptions)
            bundle = build_bundle(package, encargo, task, code_sha)
            row['bundle'] = bundle
            with configured(task, model, effort, max_usd, bundle, encargo, gramatica) as holder:
                try:
                    da.preflight(bundle, holder)
                finally:
                    row['preflight'] = dict(holder)
            row['estado'] = 'PREPARADA'
        except pilot.PilotError as err:
            row['estado'] = 'NO_PREPARADA:' + str(err)
        rows.append(row)
    return rows


def mark_previous(http, rows):
    """H8: avisa de las empresas que ya tienen un cribado en la rama de registro (una lectura)."""
    try:
        listing = http.call('github', 'GET', f'/repos/{pilot.REPO}/contents/automation/coordination/reviews'
                            f'?ref={pilot.LEDGER_BRANCH}')
    except pilot.PilotError as err:
        return 'REGISTRO_NO_CONSULTADO:' + str(err)
    names = [i.get('name') for i in listing if isinstance(i, dict) and isinstance(i.get('name'), str)] \
        if isinstance(listing, list) else []
    for row in rows:
        row['cribados_anteriores'] = sorted(n for n in names if re.fullmatch(r'cribado-[0-9]+-' + re.escape(slug(row['empresa'])), n))
    return None


def run_batch(http, rows, encargo, model, effort, max_usd, max_batch, run_id, output, live=False,
              gramatica=False, deadline_seconds=None, clock=time.monotonic):
    """Una llamada por empresa, en secuencia, sin reintentos; para al primer tope alcanzado."""
    output = Path(output)
    start, local, consecutive, rejected, stop = clock(), Decimal('0'), 0, 0, None
    cache, prior = {}, None
    for row in rows:
        if not row['estado'].startswith('PREPARADA'):
            continue
        if stop is not None:
            row['estado'] = 'NO_LLAMADA_TANDA_PARADA'
            continue
        if not live:
            with configured(row['task_id'], model, effort, max_usd, row['bundle'], encargo, gramatica, dict(row['preflight'])):
                cr.run(http, row['bundle'], output / slug(row['empresa']), execute=False)
            row['estado'] = 'PREPARADO_SIN_API'
            continue
        if deadline_seconds is not None and clock() - start + PER_CALL_WORST_SECONDS > deadline_seconds:
            stop = 'PLAZO_DE_LA_TANDA_AGOTADO'
            row['estado'] = 'NO_LLAMADA_TANDA_PARADA'
            continue
        try:
            if prior is None:
                # Una sola lectura: lo comprometido por intentos anteriores de esta ejecución.
                prior = register_exposure(http, run_id, cache)
            committed = prior + local
        except pilot.PilotError as err:
            stop = 'REGISTRO_NO_VERIFICABLE:' + str(err)
            row['estado'] = 'NO_LLAMADA_TANDA_PARADA'
            continue
        row['tanda_comprometido_antes_usd'] = str(committed)
        if committed + max_usd > max_batch:
            stop = 'MAXIMO_DE_LA_TANDA_ALCANZADO'
            row['estado'] = 'NO_LLAMADA_TANDA_PARADA'
            continue
        receipt = TrackingReceipt(http, row['bundle']['code_sha'], row['task_id'])
        try:
            with configured(row['task_id'], model, effort, max_usd, row['bundle'], encargo, gramatica,
                            dict(row['preflight']), cache) as holder:
                da.preflight(row['bundle'], holder)
                report = cr.run(http, row['bundle'], output / slug(row['empresa']), receipt=receipt, execute=True)
        except Exception as err:  # noqa: BLE001 - se registra; nunca se repite la llamada
            code = str(err) if isinstance(err, pilot.PilotError) else 'ERROR_INESPERADO_' + type(err).__name__
            if receipt.reserve_attempted:
                # Pudo haber reserva (y llamada): cuenta el máximo y se para la tanda.
                row.update(estado='FALLO_TRAS_RESERVAR:' + code, exposicion_usd=str(max_usd))
                local += max_usd
                stop = 'FALLO_TRAS_RESERVAR'
            elif code in COMPANY_ONLY:
                row['estado'] = 'NO_LLAMADA:' + code
            else:
                row['estado'] = 'NO_LLAMADA:' + code
                stop = code
            continue
        exposure = exposure_of(report, max_usd)
        local += exposure
        row.update(estado=report['state'], exposicion_usd=str(exposure), report=report)
        if report['state'] == cr.UNCERTAIN:
            consecutive += 1
            status = (report.get('api_error') or {}).get('http_status')
            if report.get('cost_status') == 'INCIERTO_SIN_COTA':
                stop = 'COSTE_SIN_COTA_RECONCILIAR_EN_CONSOLE'
            elif isinstance(status, int) and 400 <= status < 500:
                stop = f'ERROR_HTTP_{status}_DE_LA_API_SE_PARA_LA_TANDA'
            elif consecutive >= 2:
                stop = 'DOS_FALLOS_SEGUIDOS_TRAS_ENVIAR'
        else:
            consecutive = 0
        if report['state'] == cr.REJECTED:
            # H4: dos respuestas pagadas e inválidas seguidas apuntan a un fallo sistemático.
            rejected += 1
            if rejected >= 2:
                stop = 'DOS_RESPUESTAS_PAGADAS_INVALIDAS_SEGUIDAS'
        elif report['state'] != 'YA_RESERVADO_SIN_NUEVA_LLAMADA':
            rejected = 0
    return {'parada': stop, 'comprometido_local_usd': str(local)}


def batch_summary(rows, result, meta):
    out = {'tanda': meta, 'parada': result['parada'], 'empresas': []}
    total = Decimal('0')
    for row in rows:
        rep = row.get('report') or {}
        review = rep.get('review') or {}
        item = {'empresa': row['empresa'], 'task_id': row['task_id'], 'estado': row['estado'],
                'veredicto_cribado': (review.get('cribado') or {}).get('veredicto_cribado'),
                'avisos': len((review.get('comprobaciones_mecanicas') or {}).get('avisos', [])),
                'api_messages_sent': rep.get('api_messages_sent', 0), 'cost_status': rep.get('cost_status'),
                'estimated_cost_usd': rep.get('estimated_cost_usd'),
                'cost_upper_bound_usd': rep.get('cost_upper_bound_usd'),
                'exposicion_usd': row.get('exposicion_usd', '0'),
                'reserva_estimada_usd': (row.get('preflight') or {}).get('reserve_upper_bound_usd'),
                'package_sha256': (row.get('bundle') or {}).get('package_sha256'),
                'fecha_hoja': (row.get('bundle') or {}).get('fecha_hoja'),
                'cribados_anteriores': row.get('cribados_anteriores', []),
                'excepciones_ceguera': row.get('excepciones_ceguera', [])}
        if rep.get('error'):
            item['error'] = rep['error']
        total += Decimal(item['exposicion_usd'])
        out['empresas'].append(item)
    out['comprometido_tanda_usd'] = str(total)
    out['llamadas'] = sum(i['api_messages_sent'] for i in out['empresas'])
    return out


def render_batch(summary):
    m = summary['tanda']
    out = ['# Tanda de cribado', '',
           'Cribado pendiente de revisión humana. No es una recomendación de compra ni aptitud para dinero real.', '',
           CONVENCION_ARRENDAMIENTOS, '', CONDICIONES, '',
           '| Campo | Valor |', '|---|---|']
    out += [f'| {k} | {v} |' for k, v in m.items()]
    out += [f"| Llamadas a la API | {summary['llamadas']} |",
            f"| Comprometido por la tanda (USD, coste conocido o cota) | {summary['comprometido_tanda_usd']} |",
            f"| Parada | {summary['parada'] or '—'} |", '',
            '| Empresa | Veredicto | Estado | Coste USD | Cota USD | Reserva previa USD | Avisos | Fecha de la hoja |',
            '|---|---|---|---|---|---|---|---|']
    for i in summary['empresas']:
        out.append(f"| {i['empresa']} | {i['veredicto_cribado'] or '—'} | {i['estado']} | {i['estimated_cost_usd'] or '—'} |"
                   f" {i['cost_upper_bound_usd'] or '—'} | {i['reserva_estimada_usd'] or '—'} | {i['avisos']} |"
                   f" {i['fecha_hoja'] or '—'} |")
    prev = [(i['empresa'], i['cribados_anteriores']) for i in summary['empresas'] if i['cribados_anteriores']]
    if prev:
        out += ['', 'Ya cribadas en la rama de registro (otra ejecución las volvería a pagar):', '']
        out += [f"- {emp}: {', '.join(dirs)}" for emp, dirs in prev]
    exc = [(i['empresa'], e) for i in summary['empresas'] for e in i['excepciones_ceguera']]
    if exc:
        out += ['', 'Excepciones de ceguera aplicadas (excepciones_ceguera.json, pendientes de revisión):', '']
        out += [f"- {emp} · {e['archivo']} · `{e['codigo']}`" for emp, e in exc]
    return '\n'.join(out) + '\n'


def write_batch(output, summary):
    output = Path(output)
    output.mkdir(parents=True, exist_ok=True)
    (output / 'tanda.json').write_bytes(pilot.canonical(summary))
    (output / 'tanda.md').write_text(render_batch(summary), encoding='utf-8')


def publish_batch(http, code_sha, folder, output):
    ledger = BatchLedger(http, code_sha, folder)
    ledger.put('report.json', (Path(output) / 'tanda.json').read_bytes())
    ledger.put('report.md', (Path(output) / 'tanda.md').read_bytes())


# --- Dry-run del universo: cotas sin API ----------------------------------------------------------
def cotas(release, encargo, code_sha, model, effort, blind, exceptions=None, max_usd=HARD_MAX_COMPANY_USD, size=20):
    names = sorted((n for n in release.companies if n not in EXCLUIDAS), key=str.lower)
    rows = prepare(release, names, encargo, '0', code_sha, model, effort, max_usd, blind, exceptions)
    info = da.MODELS[model]
    table = []
    for r in rows:
        p = r.get('preflight', {})
        b = p.get('payload_bytes')
        rough = None
        if b is not None:
            rough = (Decimal(math.ceil(b / ROUGH_BYTES_PER_TOKEN)) * info['input']
                     + Decimal(ROUGH_OUTPUT_TOKENS) * info['output']) / 1_000_000
        srcs = (r.get('bundle') or {}).get('sources', [])
        table.append({'empresa': r['empresa'], 'estado': r['estado'], 'archivos': ' '.join(s['id'] for s in srcs),
                      'bytes_paquete': b, 'cota_tokens_entrada': p.get('input_tokens_upper_bound'),
                      'tokens_entrada_aprox': p.get('input_tokens_rough_estimate'),
                      'tokens_salida_max': p.get('max_output_tokens'),
                      'reserva_cota_usd': p.get('reserve_upper_bound_usd'),
                      'coste_orientativo_usd': None if rough is None else str(rough.quantize(Decimal('0.0001'))),
                      'formulas_sin_valor': sum(s.get('formulas_sin_valor_calculado', 0) for s in srcs),
                      'excepciones_ceguera': [e['codigo'] for e in r.get('excepciones_ceguera', [])]})
    ok = [t for t in table if t['estado'] == 'PREPARADA']
    batches = []
    for i in range(0, len(ok), size):
        part = ok[i:i + size]
        batches.append({'tanda': len(batches) + 1, 'empresas': [t['empresa'] for t in part],
                        'reserva_cota_usd': str(sum(Decimal(t['reserva_cota_usd']) for t in part)),
                        'coste_orientativo_usd': str(sum(Decimal(t['coste_orientativo_usd']) for t in part)),
                        'reserva_maxima_empresa_usd': str(max(Decimal(t['reserva_cota_usd']) for t in part))})
    return {'modelo': model, 'esfuerzo': effort, 'tarifas_usd_mtok': {'entrada': str(info['input']), 'salida': str(info['output'])},
            'tarifas_consultadas': da.PRICES_CHECKED, 'supuesto_orientativo': {
                'bytes_por_token': ROUGH_BYTES_PER_TOKEN, 'tokens_salida': ROUGH_OUTPUT_TOKENS},
            'empresas': table, 'tandas': batches,
            'total_reserva_cota_usd': str(sum((Decimal(t['reserva_cota_usd']) for t in ok), Decimal('0'))),
            'total_coste_orientativo_usd': str(sum((Decimal(t['coste_orientativo_usd']) for t in ok), Decimal('0'))),
            'preparadas': len(ok), 'no_preparadas': [t for t in table if t['estado'] != 'PREPARADA'],
            'excluidas': [n for n in EXCLUIDAS if n in release.companies], 'motivo_exclusion': EXCLUIDA}


# --- Línea de órdenes ---------------------------------------------------------------------------------
def main(argv=None):
    p = argparse.ArgumentParser(description=__doc__)
    sub = p.add_subparsers(dest='orden', required=True)
    t = sub.add_parser('tanda', help='prepara (sin API) o ejecuta (--execute-api) una tanda')
    t.add_argument('--release', type=Path, required=True)
    t.add_argument('--empresas', required=True)
    t.add_argument('--model', default=da.DEFAULT_MODEL)
    t.add_argument('--effort', default='high')
    t.add_argument('--max-usd-empresa', required=True)
    t.add_argument('--max-usd-tanda', required=True)
    t.add_argument('--gramatica', choices=('no', 'si'), default='no')
    t.add_argument('--run-id', required=True)
    t.add_argument('--run-attempt', default='1')
    t.add_argument('--code-sha', required=True)
    t.add_argument('--output', type=Path, required=True)
    t.add_argument('--deadline-seconds', type=int, default=None)
    t.add_argument('--execute-api', action='store_true')
    c = sub.add_parser('cotas', help='dry-run del universo entero, sin API')
    c.add_argument('--release', type=Path, required=True)
    c.add_argument('--model', default=da.DEFAULT_MODEL)
    c.add_argument('--effort', default='high')
    c.add_argument('--code-sha', required=True)
    c.add_argument('--output', type=Path, required=True)
    a = p.parse_args(argv)
    try:
        encargo, exceptions = verify_code(ROOT, a.code_sha)
        release = open_release(a.release)
        blind = da.blind_material(ROOT, [a.code_sha])
        if a.orden == 'cotas':
            result = cotas(release, encargo, a.code_sha, a.model, a.effort, blind, exceptions)
            write_cotas(a.output, result)
            print(json.dumps({k: result[k] for k in ('preparadas', 'total_reserva_cota_usd', 'total_coste_orientativo_usd')}))
            return 0
        if not re.fullmatch(r'[0-9]{1,20}', a.run_id) or not re.fullmatch(r'[0-9]{1,4}', a.run_attempt):
            raise pilot.PilotError('RUN_ID_INVALIDO')
        max_usd = parse_usd(a.max_usd_empresa, HARD_MAX_COMPANY_USD, 'COSTE_MAXIMO_POR_EMPRESA')
        max_batch = parse_usd(a.max_usd_tanda, HARD_MAX_BATCH_USD, 'COSTE_MAXIMO_DE_LA_TANDA')
        if max_usd > max_batch:
            raise pilot.PilotError('COSTE_MAXIMO_POR_EMPRESA_SUPERA_EL_DE_LA_TANDA')
        names = parse_companies(a.empresas, release)
        gram = a.gramatica == 'si'
        rows = prepare(release, names, encargo, a.run_id, a.code_sha, a.model, a.effort, max_usd, blind, exceptions, gram)
        http = da.DirectHTTP(os.getenv('GH_TOKEN', ''), os.getenv('ANTHROPIC_API_KEY', ''), model=a.model)
        if a.execute_api and (not http.api_key or not http.github_token):
            raise pilot.PilotError('FALTA_CREDENCIAL')
        if a.execute_api:
            previous = 'NO_SE_CONSULTA_EN_LA_EJECUCION (la reserva create-only impide repetir la misma tarea)'
        else:
            previous = mark_previous(http, rows) if http.github_token else 'SIN_TOKEN_NO_CONSULTADO'
        result = run_batch(http, rows, encargo, a.model, a.effort, max_usd, max_batch, a.run_id, a.output,
                           live=a.execute_api, gramatica=gram, deadline_seconds=a.deadline_seconds)
        reserves = [Decimal(r['preflight']['reserve_upper_bound_usd']) for r in rows if 'reserve_upper_bound_usd' in r.get('preflight', {})]
        meta = {'modo': 'ejecución' if a.execute_api else 'preparación sin API', 'run_id': a.run_id,
                'intento': a.run_attempt, 'code_sha': a.code_sha, 'release': f"{RELEASE['tag']}/{RELEASE['asset']}",
                'release_sha256': release.sha256, 'encargo_sha256': digest(encargo.encode('utf-8')),
                'modelo': a.model, 'esfuerzo': a.effort, 'gramatica': a.gramatica,
                'coste_maximo_por_empresa_usd': str(max_usd), 'coste_maximo_tanda_usd': str(max_batch),
                'tope_acumulado': 'variable ' + cr.CAP_ENV + ' del environment (se comprueba antes de cada empresa)',
                'suma_de_reservas_previas_usd': str(sum(reserves, Decimal('0'))),
                'consulta_de_cribados_anteriores': previous or 'hecha', 'excluidas': ', '.join(EXCLUIDAS)}
        summary = batch_summary(rows, result, meta)
        write_batch(a.output, summary)
        if a.execute_api:
            publish_batch(http, a.code_sha, f'cribado-{a.run_id}-tanda-{a.run_attempt}', a.output)
        print(json.dumps({'parada': summary['parada'], 'llamadas': summary['llamadas'],
                          'comprometido_tanda_usd': summary['comprometido_tanda_usd']}))
        if not a.execute_api:
            # Preparación: las empresas no preparadas quedan a la vista en el resumen y la
            # persona decide al aprobar; sin ninguna preparada no hay nada que aprobar.
            return 0 if any(i['estado'] == 'PREPARADO_SIN_API' for i in summary['empresas']) else 1
        ok = all(i['estado'] in OK_STATES for i in summary['empresas']) and summary['parada'] is None
        return 0 if ok else 1
    except (pilot.PilotError, subprocess.CalledProcessError, OSError) as err:
        print(str(err) if isinstance(err, pilot.PilotError) else 'GIT_O_ARCHIVO_NO_VERIFICABLE', file=sys.stderr)
        return 2


def write_cotas(output, result):
    output = Path(output)
    output.mkdir(parents=True, exist_ok=True)
    (output / 'cotas.json').write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding='utf-8')
    cols = ('empresa', 'estado', 'archivos', 'bytes_paquete', 'cota_tokens_entrada', 'tokens_entrada_aprox',
            'tokens_salida_max', 'reserva_cota_usd', 'coste_orientativo_usd', 'formulas_sin_valor')
    with open(output / 'cotas.tsv', 'w', encoding='utf-8', newline='') as fh:
        w = csv.writer(fh, delimiter='\t', lineterminator='\n')
        w.writerow(cols)
        for row in result['empresas']:
            w.writerow(['' if row[k] is None else row[k] for k in cols])
    lines = [f"# Cotas del cribado · {result['modelo']} · esfuerzo {result['esfuerzo']}", '',
             'Dry-run sin API. La **cota** es la reserva de AUTO1: un token por byte del envío + 4 096 de margen'
             f" y la salida máxima ({MAX_OUTPUT} tokens), a {result['tarifas_usd_mtok']['entrada']} / "
             f"{result['tarifas_usd_mtok']['salida']} USD por millón (tarifas del {result['tarifas_consultadas']}). "
             f"El **orientativo** supone {ROUGH_BYTES_PER_TOKEN} bytes por token y {ROUGH_OUTPUT_TOKENS} tokens de salida.", '',
             f"- Empresas preparadas: {result['preparadas']}; no preparadas: {len(result['no_preparadas'])}; "
             f"excluidas ({result['motivo_exclusion']}): {', '.join(result['excluidas'])}.",
             f"- Total de cotas: USD {result['total_reserva_cota_usd']}.",
             f"- Total orientativo: USD {result['total_coste_orientativo_usd']}.", '',
             '| Tanda | Empresas | Suma de cotas USD | Mayor cota USD | Orientativo USD |', '|---|---|---|---|---|']
    for b in result['tandas']:
        lines.append(f"| {b['tanda']} | {len(b['empresas'])} | {b['reserva_cota_usd']} | {b['reserva_maxima_empresa_usd']} |"
                     f" {b['coste_orientativo_usd']} |")
    lines += ['']
    for b in result['tandas']:
        lines += [f"Tanda {b['tanda']}: " + ', '.join(b['empresas']), '']
    if result['no_preparadas']:
        lines += ['No preparadas:', ''] + [f"- {t['empresa']}: {t['estado']}" for t in result['no_preparadas']] + ['']
    lines += ['| Empresa | Archivos | Bytes | Cota tokens entrada | Cota USD | Orientativo USD |', '|---|---|---|---|---|---|']
    for t in result['empresas']:
        lines.append(f"| {t['empresa']} | {t['archivos']} | {t['bytes_paquete']} | {t['cota_tokens_entrada']} |"
                     f" {t['reserva_cota_usd']} | {t['coste_orientativo_usd']} |")
    (output / 'cotas.md').write_text('\n'.join(lines) + '\n', encoding='utf-8')


if __name__ == '__main__':
    sys.exit(main())
