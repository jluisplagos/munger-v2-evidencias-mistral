#!/usr/bin/env python3
"""Análisis directo en una sola pasada sobre un paquete de entrada declarado.

Personaje frente a análisis directo (REORIENTACION_UNIVERSO §10). El control de gasto
no se reimplementa: se configura y ejecuta critical_review.run de AUTO1 (tope
acumulado, reserva previa create-only, una sola llamada sin reintentos, estados de
coste y publicación en la rama de registro). Aquí solo se arma el paquete, se
comprueba su tamaño antes de llamar y se valida y presenta la salida.
"""
import argparse
import contextlib
import datetime
from decimal import Decimal
import json
import math
import os
from pathlib import Path, PurePosixPath
import re
import subprocess
import sys
import unicodedata

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / 'automation/coordination'))
import critical_review as cr  # noqa: E402  (importa también automation/claude_review/pilot.py)

pilot = cr.pilot

ENCARGO_PATH = 'automation/direct_analysis/ENCARGO_ANALISIS_DIRECTO.md'
CODE_PATHS = ('automation/direct_analysis/direct_analysis.py', ENCARGO_PATH,
              'automation/coordination/critical_review.py', 'automation/claude_review/pilot.py')
# Tarifas USD/MTok de la API de Anthropic (tabla de modelos consultada el 17-nov-2026;
# Fable 5.2 y Sonnet 5.5 coinciden con las ya registradas en AUTO1). Contexto: 1M.
MODELS = {
    'claude-opus-5-5': {'input': Decimal('4'), 'output': Decimal('20'), 'context': 1_000_000},
    'claude-fable-5-2': {'input': Decimal('8'), 'output': Decimal('40'), 'context': 1_000_000},
    'claude-sonnet-5-5': {'input': Decimal('2'), 'output': Decimal('10'), 'context': 1_000_000},
}
DEFAULT_MODEL = 'claude-opus-5-5'
EFFORTS = ('low', 'medium', 'high', 'xhigh', 'max')
PRICES_CHECKED = '2026-11-17'
# Salida máxima (pensamiento + respuesta). Igual que AUTO1, para caber en su plazo de
# stream de 720 s; agotarla deja un resultado pagado y no aceptado.
MAX_OUTPUT = 32768
HARD_MAX_USD = Decimal('5')  # techo del código; el tope acumulado lo fija la persona
MARGIN_TOKENS = 4096          # el mismo margen que critical_review.budget
MAX_FILE_BYTES = 1_500_000
MAX_FILES = 40
TASA = '9 %'
PROBABILIDADES = {'malo': '0,2', 'normal': '0,6', 'bueno': '0,2'}
OK_STATES = ('PREPARADO_SIN_API', 'AUDITORIA_DOCUMENTAL_PENDIENTE_ACEPTACION')


# --- Ceguera (revisión H3): lista blanca de raíces + listas negras + huellas + solape ---
# Única raíz admitida para los datos del paquete: datos_analisis_directo/<empresa>/...
DATA_ROOT = 'datos_analisis_directo'
FIXED_DATA = {'datos_v63.md', 'datos_v63.json', 'fase1_v63.json', 'extracto_v63.md'}
# etapa1/: la misma etapa 1 que recibe el personaje (Excel evaluado en texto y respuesta),
# decisión L2 de la persona responsable, 18-nov-2026.
DATA_DIRS = ('fuentes', 'historia', 'registro_entradas', 'etapa1')
DATA_FILE = re.compile(r'(?:%s)/(?:[\w. -]+/)*[\w. -]+\.(?:txt|md|csv|json)' % '|'.join(DATA_DIRS))
# Segundo filtro (sin tildes, en minúsculas) sobre la parte de la ruta bajo la raíz.
FORBIDDEN_SEGMENTS = {'examen', 'universo', 'traspaso', 'pruebas_candidata', 'automation', '.github',
                      'resultados_qwen', 'prompts_generados', 'revisiones_coordinador', 'revision_externa'}
FORBIDDEN_SUBSTRINGS = ('rubrica', 'critic', 'lectura_informe', 'contradictor', 'mecanismo', 'prompt',
                        'analisis_directo', 'analisis-directo', 'veredicto', 'dictamen', 'respuesta',
                        'salida', 'fase', 'phase', 'audit', 'ficha', 'objetivo', 'escalera', 'material',
                        'solicitud', 'celdas', 'gramatica', 'diagnostico', 'estado_pipeline', 'relevo')
FORBIDDEN_STEMS = re.compile(r'^(informe|precio)(_v\d+)?$')
# Fuera de registro_entradas/ tampoco se admite «verificacion» (p. ej. prompts de verificación).
OUTSIDE_REGISTRY = ('verificacion',)
# En etapa1/ el Excel evaluado y la respuesta llevan nombres de salida («respuesta», hojas
# «Diagnóstico», «precio», «ficha»…): allí solo valen los nombres de material ciego.
ETAPA1_SUBSTRINGS = ('rubrica', 'critic', 'lectura_informe', 'contradictor', 'mecanismo', 'prompt',
                     'analisis_directo', 'analisis-directo', 'relevo', 'audit')
# Carpetas cuyo contenido el análisis directo no puede ver, ni copiado ni retocado.
BLIND_SEGMENTS = {'examen', 'universo', 'traspaso', 'pruebas_candidata'}
# Únicas copias admitidas de una carpeta ciega: el registro de entradas (REORIENTACION §10),
# solo bajo registro_entradas/. Tampoco cuentan para el solape (el registro relleno
# comparte la estructura de su plantilla).
ALLOWED_COPIES = {'lista_entradas.csv', 'verificacion_entradas.plantilla.json'}
CONTENT_MARKERS = ('rubrica', 'informecritico')
META_MARKERS = CONTENT_MARKERS + ('examen', 'munger', 'personaje', 'contradictor')
OVERLAP_CHARS = 200
PATH_CHARS = re.compile(r'[\w./ -]+')
META_CHARS = re.compile(r'[\w.,;:()%/ -]+')
# Los manifiestos viven en un único sitio conocido; no se envían en bruto al modelo.
MANIFEST = re.compile(r'automation/direct_analysis/paquetes/[a-z0-9][a-z0-9_-]{0,60}\.json')


def fold(text):
    return ''.join(c for c in unicodedata.normalize('NFKD', text) if not unicodedata.combining(c)).lower()


def squash(text):
    """Solo letras y cifras, sin tildes: anula espacios dobles, guiones y caracteres de formato."""
    return ''.join(c for c in fold(text) if c.isalnum())


def check_path(path, empresa):
    """Ruta bajo datos_analisis_directo/<empresa>/ y de una clase de datos declarada."""
    if (not isinstance(path, str) or not path or len(path) > 300 or not PATH_CHARS.fullmatch(path)
            or PurePosixPath(path).is_absolute() or any(x in ('', '.', '..') for x in path.split('/'))):
        raise pilot.PilotError('RUTA_INVALIDA')
    prefix = f'{DATA_ROOT}/{empresa}/'
    if not path.startswith(prefix):
        raise pilot.PilotError('RUTA_FUERA_DE_LOS_DATOS_DECLARADOS')
    rel = path[len(prefix):]
    if rel in FIXED_DATA:
        return path
    if not DATA_FILE.fullmatch(rel):
        raise pilot.PilotError('RUTA_FUERA_DE_LOS_DATOS_DECLARADOS')
    folded = fold(rel)
    parts = folded.split('/')
    stem = parts[-1].split('.')[0]
    if parts[0] == 'etapa1':
        if set(parts) & FORBIDDEN_SEGMENTS or any(s in folded for s in ETAPA1_SUBSTRINGS):
            raise pilot.PilotError('RUTA_PROHIBIDA_EN_EL_PAQUETE')
        return path
    if (set(parts) & FORBIDDEN_SEGMENTS or any(s in folded for s in FORBIDDEN_SUBSTRINGS)
            or FORBIDDEN_STEMS.search(stem)
            or (parts[0] != 'registro_entradas' and any(s in folded for s in OUTSIDE_REGISTRY))):
        raise pilot.PilotError('RUTA_PROHIBIDA_EN_EL_PAQUETE')
    return path


def git(root, *args):
    return subprocess.run(['git', *args], cwd=root, capture_output=True, check=True).stdout


def verify_code(root, code_sha):
    """El código y el encargo que se ejecutan son los bytes del SHA observado."""
    if not re.fullmatch(r'[0-9a-f]{40}', code_sha or ''):
        raise pilot.PilotError('SHA_INVALIDO')
    if git(root, 'rev-parse', 'HEAD').decode().strip() != code_sha:
        raise pilot.PilotError('SHA_NO_ES_EL_OBSERVADO')
    for path in CODE_PATHS:
        if (Path(root) / path).read_bytes() != git(root, 'show', f'{code_sha}:{path}'):
            raise pilot.PilotError('CODIGO_LOCAL_DISTINTO_DEL_SHA')
    return git(root, 'show', f'{code_sha}:{ENCARGO_PATH}').decode('utf-8')


def read_blob(root, commit, path):
    """Archivo regular de texto UTF-8 de un commit fijado; nunca enlaces ni submódulos."""
    if not re.fullmatch(r'[0-9a-f]{40}', commit):
        raise pilot.PilotError('COMMIT_NO_FIJADO')
    try:
        if git(root, 'cat-file', '-t', commit).strip() != b'commit':
            raise pilot.PilotError('COMMIT_NO_FIJADO')
        entry = git(root, 'ls-tree', '-z', commit, '--', path).split(b'\0')[0]
    except subprocess.CalledProcessError:
        raise pilot.PilotError('COMMIT_O_ARCHIVO_NO_ENCONTRADO') from None
    meta, _, name = entry.partition(b'\t')
    fields = meta.split()
    if name.decode('utf-8', 'replace') != path or len(fields) != 3:
        raise pilot.PilotError('ARCHIVO_NO_ENCONTRADO')
    if fields[0] not in (b'100644', b'100755') or fields[1] != b'blob':
        raise pilot.PilotError('NO_ES_ARCHIVO_REGULAR')
    if int(git(root, 'cat-file', '-s', fields[2].decode())) > MAX_FILE_BYTES:
        raise pilot.PilotError('ARCHIVO_DEMASIADO_GRANDE_NO_SE_RECORTA')
    raw = git(root, 'cat-file', 'blob', fields[2].decode())
    if b'\0' in raw:
        raise pilot.PilotError('ARCHIVO_NO_ES_TEXTO')
    try:
        return fields[2].decode(), raw, raw.decode('utf-8')
    except UnicodeDecodeError:
        raise pilot.PilotError('ARCHIVO_NO_ES_TEXTO') from None


def blind_material(root, commits):
    """Blobs bajo carpetas ciegas en el código, en cada commit declarado y en todas las refs.

    Devuelve {blob: ruta} para rechazar copias exactas y los fragmentos normalizados de
    OVERLAP_CHARS caracteres de esos textos para rechazar copias retocadas.
    """
    refs = git(root, 'for-each-ref', '--format=%(objectname)', 'refs/heads', 'refs/remotes').decode().split()
    blobs = {}
    for commit in dict.fromkeys(list(commits) + refs):
        for entry in git(root, 'ls-tree', '-r', '-z', commit).split(b'\0'):
            meta, _, name = entry.partition(b'\t')
            fields = meta.split()
            path = name.decode('utf-8', 'replace')
            if len(fields) == 3 and fields[1] == b'blob' and set(fold(path).split('/')[:-1]) & BLIND_SEGMENTS:
                blobs.setdefault(fields[2].decode(), path)
    chunks = {}
    for blob, path in blobs.items():
        if fold(PurePosixPath(path).name) in ALLOWED_COPIES:
            continue
        if int(git(root, 'cat-file', '-s', blob)) > MAX_FILE_BYTES:
            continue
        try:
            text = squash(git(root, 'cat-file', 'blob', blob).decode('utf-8'))
        except UnicodeDecodeError:
            continue  # binarios: solo cuentan por su huella exacta
        for i in range(0, len(text) - OVERLAP_CHARS + 1, OVERLAP_CHARS):
            chunks.setdefault(text[i:i + OVERLAP_CHARS], path)
    return blobs, chunks


def overlap(text, chunks):
    """Ruta ciega de la que el texto copia al menos 2·OVERLAP_CHARS caracteres seguidos."""
    s = squash(text)
    for i in range(len(s) - OVERLAP_CHARS + 1):
        hit = chunks.get(s[i:i + OVERLAP_CHARS])
        if hit is not None:
            return hit
    return None


def _slug(value, code):
    if not isinstance(value, str) or not re.fullmatch(r'[a-z0-9][a-z0-9-]{0,29}', value):
        raise pilot.PilotError(code)
    return value


def _meta_text(value, limit):
    if (not isinstance(value, str) or not 1 <= len(value) <= limit or not META_CHARS.fullmatch(value)
            or any(m in squash(value) for m in META_MARKERS)):
        raise pilot.PilotError('TEXTO_DEL_MANIFIESTO_INVALIDO')
    return value


def load_package(root, code_sha, manifest_path, empresa):
    """Lee el manifiesto versionado y cada archivo declarado, con su huella."""
    _slug(empresa, 'EMPRESA_INVALIDA')
    if not isinstance(manifest_path, str) or not MANIFEST.fullmatch(manifest_path):
        raise pilot.PilotError('MANIFIESTO_FUERA_DE_PAQUETES')
    _, raw_manifest, text = read_blob(root, code_sha, manifest_path)
    try:
        m = json.loads(text)
    except ValueError:
        raise pilot.PilotError('MANIFIESTO_JSON_INVALIDO') from None
    if not isinstance(m, dict) or set(m) != {'empresa', 'caso', 'fecha_corte', 'archivos'}:
        raise pilot.PilotError('MANIFIESTO_INVALIDO')
    if _slug(m['empresa'], 'MANIFIESTO_INVALIDO') != empresa:
        raise pilot.PilotError('MANIFIESTO_DE_OTRA_EMPRESA')
    _meta_text(m['caso'], 100)
    try:
        datetime.date.fromisoformat(m['fecha_corte'])
        if not re.fullmatch(r'\d{4}-\d{2}-\d{2}', m['fecha_corte']):
            raise ValueError
    except (TypeError, ValueError):
        raise pilot.PilotError('FECHA_CORTE_INVALIDA') from None
    files = m['archivos']
    if not isinstance(files, list) or not 1 <= len(files) <= MAX_FILES:
        raise pilot.PilotError('MANIFIESTO_INVALIDO')
    declared, ids = [], set()
    for f in files:
        if isinstance(f, dict) and 'sha256' not in f:
            raise pilot.PilotError('PAQUETE_SIN_HUELLA_DECLARADA')
        if not isinstance(f, dict) or not {'id', 'ruta', 'sha256', 'descripcion'} <= set(f) \
                or set(f) - {'id', 'ruta', 'sha256', 'descripcion', 'commit'}:
            raise pilot.PilotError('ARCHIVO_DECLARADO_INVALIDO')
        if not isinstance(f['id'], str) or not re.fullmatch(r'[a-z][a-z0-9_]{0,40}', f['id']) or f['id'] in ids:
            raise pilot.PilotError('ID_ARCHIVO_INVALIDO')
        ids.add(f['id'])
        _meta_text(f['descripcion'], 300)
        if not isinstance(f['sha256'], str) or not re.fullmatch(r'[0-9a-f]{64}', f['sha256']):
            raise pilot.PilotError('PAQUETE_SIN_HUELLA_DECLARADA')
        commit = f.get('commit', code_sha)
        if not isinstance(commit, str):
            raise pilot.PilotError('COMMIT_NO_FIJADO')
        check_path(f['ruta'], empresa)
        declared.append((f, commit, read_blob(root, commit, f['ruta'])))
    blobs, chunks = blind_material(root, [code_sha] + [c for _, c, _ in declared])
    sources = []
    for f, commit, (blob, raw, body) in declared:
        if pilot.digest(raw) != f['sha256']:
            raise pilot.PilotError('HUELLA_DISTINTA_DE_LA_DECLARADA')
        if blob in blobs and not (fold(PurePosixPath(blobs[blob]).name) in ALLOWED_COPIES
                                  and f['ruta'].startswith(f'{DATA_ROOT}/{empresa}/registro_entradas/')):
            raise pilot.PilotError('COPIA_DE_MATERIAL_CIEGO:' + blobs[blob])
        if any(marker in squash(body) for marker in CONTENT_MARKERS):
            raise pilot.PilotError('CONTENIDO_PROHIBIDO_EN_EL_PAQUETE')
        hit = overlap(body, chunks)
        if hit is not None:
            raise pilot.PilotError('SOLAPE_CON_MATERIAL_CIEGO:' + hit)
        sources.append({'id': f['id'], 'path': f['ruta'], 'commit': commit, 'sha256': f['sha256'],
                        'bytes': len(raw), 'descripcion': f['descripcion'], 'text': body})
    return {'empresa': empresa, 'caso': m['caso'], 'fecha_corte': m['fecha_corte'],
            'tasa_descuento': TASA, 'probabilidades_partida': PROBABILIDADES,
            'manifiesto': {'ruta': manifest_path, 'sha256': pilot.digest(raw_manifest)},
            'sources': sources}


def build_bundle(package, encargo, task_id, code_sha):
    """La huella del paquete no depende del SHA del código ni de la tarea.

    No se envía el nombre del repositorio (revisión H3.5); queda en el registro.
    """
    package = {**package, 'encargo_sha256': pilot.digest(encargo.encode('utf-8'))}
    return {**package, 'package_sha256': pilot.digest(pilot.canonical(package)),
            'task_id': task_id, 'code_sha': code_sha}


# --- Esquema de salida (revisión H2, H4, H5) -----------------------------------------
# Sin anyOf: cada cifra es obligatoria y lleva su indicador `disponible` (límite de la API:
# 16 parámetros con unión). Enumeraciones sin espacios ni mayúsculas. Ningún campo pide
# «razonamiento»: solo explicaciones breves de supuestos y cifras.
STR = {'type': 'string'}
NUM = {'type': 'number'}
BOOL = {'type': 'boolean'}
ESTADOS = ['concluido', 'pendiente_de_investigacion', 'pendiente_de_datos', 'modelo_no_aplicable', 'no_entregable']
CUBOS = ['si', 'vigilar', 'no', 'demasiado_dificil']
CUBO_TEXTO = {'si': 'Sí', 'vigilar': 'Vigilar', 'no': 'No', 'demasiado_dificil': 'Demasiado difícil'}
ACCIONES = ['comprar', 'esperar', 'descartar', 'demasiado_dificil', 'ninguna']
ZONAS = ['bajo_malo', 'cumple_regla_k', 'vigilar', 'caro', 'sin_zona']
TASAS = ('tasa_7', 'tasa_8', 'tasa_9', 'tasa_10', 'tasa_11')
ESCENARIOS = ('malo', 'normal', 'bueno')


def _obj(props):
    return {'type': 'object', 'additionalProperties': False, 'properties': props, 'required': list(props)}


def _enum(values):
    return {'type': 'string', 'enum': values}


_ESC = _obj({'disponible': BOOL, 'valor_por_accion': NUM, 'probabilidad': NUM, 'supuestos_y_cifras': STR})
_TASA = _obj({'disponible': BOOL, 'precio_si': NUM, 'ponderado': NUM, 'zona': _enum(ZONAS), 'comentario': STR})
SCHEMA = _obj({
    'resumen': STR,
    'estado': _enum(ESTADOS),
    'cubo': _enum(CUBOS),
    'accion': _enum(ACCIONES),
    'moneda': STR,
    'precio_actual': _obj({'disponible': BOOL, 'valor': NUM, 'fecha': STR, 'archivo_id': STR}),
    'escenarios': _obj({k: _ESC for k in ESCENARIOS}),
    'motivo_probabilidades': STR,
    'escalera': _obj({'disponible': BOOL, 'precio_escenario_malo_disponible': BOOL, 'precio_escenario_malo': NUM,
                      'p_estrella': NUM, 'precio_si': NUM, 'ponderado': NUM, 'zona': _enum(ZONAS),
                      'formula_aplicada': STR}),
    'crecimiento_implicito': _obj({'disponible': BOOL, 'al_precio_actual_pct': NUM,
                                   'del_escenario_normal_pct': NUM, 'explicacion_breve': STR}),
    'sensibilidad_tasa': _obj({t: _TASA for t in TASAS}),
    'justificacion_breve': STR,
    'que_la_haria_falsa': {'type': 'array', 'items': STR},
    'lo_que_no_se': {'type': 'array', 'items': STR},
    'citas': {'type': 'array', 'items': _obj({'archivo_id': STR, 'cita': STR, 'sostiene': STR})},
})


def _canon(text):
    return re.sub(r'[\s-]+', '_', fold(text).strip())


def normalize_enums(value, schema, notes, where='$'):
    """La API no garantiza mayúsculas en los enum: se canoniza y se registra el original."""
    if isinstance(value, str) and 'enum' in schema and value not in schema['enum']:
        match = {_canon(e): e for e in schema['enum']}.get(_canon(value))
        if match is not None:
            notes.append({'campo': where, 'original': value, 'canonico': match})
            return match
    if isinstance(value, dict) and schema.get('type') == 'object':
        return {k: normalize_enums(v, schema['properties'][k], notes, f'{where}.{k}')
                if k in schema['properties'] else v for k, v in value.items()}
    if isinstance(value, list) and schema.get('type') == 'array':
        return [normalize_enums(v, schema['items'], notes, f'{where}[{i}]') for i, v in enumerate(value)]
    return value


def check_schema(value, schema, where='$'):
    """Validador del subconjunto de JSON Schema usado arriba; no confía en el proveedor."""
    kind = schema['type']
    ok = {'object': isinstance(value, dict), 'array': isinstance(value, list),
          'string': isinstance(value, str), 'boolean': isinstance(value, bool),
          'number': isinstance(value, (int, float)) and not isinstance(value, bool)
          and math.isfinite(value)}[kind]
    if not ok or ('enum' in schema and value not in schema['enum']):
        raise pilot.PilotError('ESQUEMA_INVALIDO:' + where)
    if kind == 'object':
        if set(value) != set(schema['required']):
            raise pilot.PilotError('ESQUEMA_INVALIDO:' + where)
        for key, sub in schema['properties'].items():
            check_schema(value[key], sub, f'{where}.{key}')
    elif kind == 'array':
        for i, item in enumerate(value):
            check_schema(item, schema['items'], f'{where}[{i}]')
    return value


def escalera(values, probs, k=3):
    """Anexo C (§C.2–C.4), forma cerrada. Lectura aritmética de control, no decide nada.

    Devuelve None si faltan valores o las probabilidades no suman 1, y
    {'error': 'valores_desordenados'} si no se cumple malo <= normal <= bueno.
    """
    if len(values) != 3 or any(isinstance(v, bool) or not isinstance(v, (int, float)) for v in values + probs):
        return None
    if any(p < 0 for p in probs) or abs(sum(probs) - 1) > 1e-3:
        return None
    if not values[0] <= values[1] <= values[2]:
        return {'error': 'valores_desordenados'}
    s = sorted(zip(values, probs))
    p_star = None
    for j in (1, 2):
        low, high = s[:j], s[j:]
        num = sum(p * v for v, p in high) + k * sum(p * v for v, p in low)
        den = sum(p for _, p in high) + k * sum(p for _, p in low)
        P = num / den
        tol = 1e-9 * max(1.0, abs(s[j - 1][0]), abs(s[j][0]))  # relativa (revisión R2-1)
        if s[j - 1][0] - tol <= P <= s[j][0] + tol:
            p_star = min(max(P, s[0][0]), s[2][0])
            break
    if p_star is None:  # redondeo: bisección de G − k·L, decreciente, en [V(1), V(3)]
        lo, hi = s[0][0], s[2][0]
        for _ in range(200):
            mid = (lo + hi) / 2
            gain = sum(p * max(v - mid, 0) for v, p in s)
            loss = sum(p * max(mid - v, 0) for v, p in s)
            lo, hi = (mid, hi) if gain >= k * loss else (lo, mid)
        p_star = lo
    return {'p_estrella': p_star, 'precio_si': min(p_star, values[1]),
            'ponderado': sum(p * v for v, p in zip(values, probs)),
            'precio_escenario_malo': values[0] if values[0] > 0 else None}


def zona(precio, e):
    """Anexo C §C.4.4. La zona no es la conclusión."""
    if e['precio_escenario_malo'] is not None and precio <= e['precio_escenario_malo']:
        return 'bajo_malo'
    if precio <= e['precio_si']:
        return 'cumple_regla_k'
    return 'vigilar' if precio <= e['ponderado'] else 'caro'


def _far(a, b):
    return abs(a - b) > 0.01 * max(abs(b), 1e-9)


def mechanical_checks(doc, bundle):
    """Avisos para la revisión humana; no aceptan ni rechazan el análisis."""
    notes = []
    esc = [doc['escenarios'][k] for k in ESCENARIOS]
    probs = [e['probabilidad'] for e in esc]
    if abs(sum(probs) - 1) > 1e-3:
        notes.append('Las probabilidades no suman 1.')
    if probs != [0.2, 0.6, 0.2] and not doc['motivo_probabilidades'].strip():
        notes.append('Probabilidades distintas de 0,2/0,6/0,2 sin motivo.')
    ladder = doc['escalera']
    recalculated = None
    if all(e['disponible'] for e in esc):
        recalculated = escalera([e['valor_por_accion'] for e in esc], probs)
        if recalculated and 'error' in recalculated:
            notes.append('Valores desordenados (malo <= normal <= bueno no se cumple): sin escalera (Anexo C, regla 0).')
        elif recalculated and not ladder['disponible']:
            notes.append('Hay tres escenarios pero no se entrega escalera.')
        elif recalculated:
            for key in ('p_estrella', 'precio_si', 'ponderado'):
                if _far(ladder[key], recalculated[key]):
                    notes.append(f'{key} declarado difiere más de un 1 % del recalculado (Anexo C).')
            if (recalculated['precio_escenario_malo'] is None) == ladder['precio_escenario_malo_disponible']:
                notes.append('Disponibilidad del precio del escenario malo incoherente con su valor.')
            if doc['precio_actual']['disponible'] and ladder['zona'] != zona(doc['precio_actual']['valor'], recalculated):
                notes.append('La zona declarada no es la que resulta del precio actual y la escalera.')
            t9 = doc['sensibilidad_tasa']['tasa_9']
            if t9['disponible'] and _far(t9['precio_si'], recalculated['precio_si']):
                notes.append('El precio de Sí al 9 % de la sensibilidad no coincide con el de la escalera.')
    elif ladder['disponible']:
        notes.append('Escalera entregada sin los tres escenarios disponibles.')
    if doc['cubo'] == 'si' and (doc['estado'] != 'concluido' or doc['accion'] != 'comprar'):
        notes.append('Cubo «Sí» sin estado concluido y acción comprar.')
    texts = {s['id']: s['text'] for s in bundle['sources']}
    bad = [i for i, c in enumerate(doc['citas']) if c['archivo_id'] not in texts or not c['cita']
           or c['cita'] not in texts[c['archivo_id']]]
    if bad:
        notes.append(f'Citas no literales o de archivo inexistente: {bad}.')
    if doc['precio_actual']['disponible'] and doc['precio_actual']['archivo_id'] not in texts:
        notes.append('El precio actual no remite a un archivo del paquete.')
    return {'escalera_recalculada_anexo_c': recalculated, 'citas_total': len(doc['citas']),
            'citas_literales': len(doc['citas']) - len(bad), 'avisos': notes,
            'nota': 'Comprobaciones mecánicas informativas: no acreditan la calidad económica.'}


def _sin_duplicadas(pairs):
    keys = [k for k, _ in pairs]
    if len(keys) != len(set(keys)):
        raise ValueError('clave duplicada')
    return dict(pairs)


def nulos_no_disponibles(value, schema, notes, where='$'):
    """Un null en una cifra de un objeto con `disponible` = false se lee como 0 y se anota.

    Solo ahí: un null en cualquier otro sitio sigue siendo ESQUEMA_INVALIDO.
    """
    if isinstance(value, dict) and schema.get('type') == 'object':
        props = schema.get('properties', {})
        libre = value.get('disponible') is False
        out = {}
        for k, v in value.items():
            sub = props.get(k, {})
            if v is None and libre and sub.get('type') == 'number':
                notes.append({'campo': f'{where}.{k}', 'original': None, 'canonico': 0,
                              'motivo': 'disponible=false'})
                out[k] = 0
            else:
                out[k] = nulos_no_disponibles(v, sub, notes, f'{where}.{k}') if sub else v
        return out
    if isinstance(value, list) and schema.get('type') == 'array':
        return [nulos_no_disponibles(v, schema['items'], notes, f'{where}[{i}]') for i, v in enumerate(value)]
    return value


def validate(response, bundle):
    if response.get('stop_reason') != 'end_turn':
        raise pilot.PilotError('RESPUESTA_INCOMPLETA')
    raw = ''.join(x.get('text', '') for x in response.get('content', [])
                  if isinstance(x, dict) and x.get('type') == 'text').strip()
    notes = []
    doc = leer_respuesta(raw, notes)
    doc = check_schema(normalize_enums(nulos_no_disponibles(doc, SCHEMA, notes), SCHEMA, notes), SCHEMA)
    return {'analisis': doc, 'package_sha256': bundle['package_sha256'], 'normalizaciones_enum': notes,
            'comprobaciones_mecanicas': safe_checks(doc, bundle)}


def leer_respuesta(raw, notes):
    """Objeto JSON de la respuesta, sin aflojar el contenido (check_schema va después).

    Admite: el objeto solo; un bloque ```json; varios bloques ```json **sin texto entre ellos**
    cuyas claves no se repiten (ejecución 44290314915: el modelo partió el objeto en dos
    bloques), que se unen y se anota; o un único objeto rodeado de texto, que se anota.
    """
    raw = raw.strip()
    fenced = re.fullmatch(r'```json\r?\n([\s\S]*)\r?\n```', raw)
    try:
        return json.loads(fenced.group(1) if fenced else raw, object_pairs_hook=_sin_duplicadas)
    except (ValueError, RecursionError):
        pass
    blocks = re.findall(r'```json\r?\n([\s\S]*?)\r?\n```', raw)
    outside = re.sub(r'```json\r?\n[\s\S]*?\r?\n```', '', raw).strip()
    if len(blocks) > 1 and not outside:
        merged = {}
        try:
            for b in blocks:
                part = json.loads(b, object_pairs_hook=_sin_duplicadas)
                if not isinstance(part, dict) or set(part) & set(merged):
                    raise ValueError
                merged.update(part)
        except (ValueError, RecursionError):
            raise pilot.PilotError('JSON_INVALIDO') from None
        notes.append('objeto_json_partido_en_%d_bloques_unido' % len(blocks))
        return merged
    # Sin gramática del servidor: si hay texto alrededor de un único objeto, se toma el
    # objeto y se anota. El contenido pasa después por check_schema completo.
    i, j = raw.find('{'), raw.rfind('}')
    try:
        if i < 0 or j <= i:
            raise ValueError
        doc = json.loads(raw[i:j + 1], object_pairs_hook=_sin_duplicadas)
    except (ValueError, RecursionError):
        raise pilot.PilotError('JSON_INVALIDO') from None
    notes.append('texto_fuera_del_objeto_json_descartado: %d caracteres' % (len(raw) - (j + 1 - i)))
    return doc


def safe_checks(doc, bundle):
    """Un fallo de una comprobación informativa es un aviso, nunca deja sin aceptar lo pagado."""
    try:
        return mechanical_checks(doc, bundle)
    except Exception as err:  # noqa: BLE001 - por diseño: ninguna excepción sale de aquí
        return {'escalera_recalculada_anexo_c': None, 'citas_total': len(doc.get('citas', [])),
                'citas_literales': None, 'avisos': ['Comprobación mecánica no completada: ' + type(err).__name__],
                'nota': 'Comprobaciones mecánicas informativas: no acreditan la calidad económica.'}


# --- Presentación ---------------------------------------------------------------------
def _block(text):
    """Texto del modelo como bloque de código indentado: nunca Markdown interpretable."""
    return ['    ' + line for line in str(text).splitlines() or ['']] + ['']


def _n(value, available=True):
    if not available or value is None:
        return '—'
    return f'{value:.4f}'.rstrip('0').rstrip('.') if isinstance(value, float) else str(value)


def render(report, bundle, preflight):
    out = ['# Análisis directo · ' + bundle['caso'], '',
           'Estado de la ejecución: `' + report['state'] + '`', '',
           'Revisión a ciegas pendiente. No es aceptación, ni integración, ni aptitud para dinero real.', '',
           '| Campo | Valor |', '|---|---|',
           f"| Empresa | {bundle['empresa']} |", f"| Fecha de corte | {bundle['fecha_corte']} |",
           f"| Tasa | {bundle['tasa_descuento']} |", f"| Tarea | {report['task_id']} |",
           f"| SHA del código | {report['code_sha']} |",
           f"| Huella del paquete (package_sha256) | {bundle['package_sha256']} |",
           f"| Huella del envío (bundle_sha256) | {report['bundle_sha256']} |",
           f"| Huella del encargo | {bundle['encargo_sha256']} |",
           f"| Modelo pedido / devuelto | {report['model_requested']} / {report.get('model_returned', '—')} |",
           f"| Esfuerzo | {report['effort_requested']} |",
           f"| Mensajes enviados | {report['api_messages_sent']} |",
           f"| Cota de entrada estimada antes de llamar | {preflight['input_tokens_upper_bound']} tokens |",
           f"| Reserva estimada antes de llamar | USD {preflight['reserve_upper_bound_usd']} (máximo de la ejecución USD {preflight['max_usd']}) |"]
    if 'budget' in report:
        out.append(f"| Reserva registrada | USD {report['budget']['reserved_usd']} |")
    usage = report.get('usage')
    if isinstance(usage, dict):
        out.append(f"| Uso de tokens | entrada {usage.get('input_tokens')}, salida {usage.get('output_tokens')} |")
    if 'cost_status' in report:
        out.append(f"| Coste | {report['cost_status']}; estimado USD {report['estimated_cost_usd']};"
                   f" cota {report.get('cost_upper_bound_usd', report['estimated_cost_usd'])} |")
    out += ['', '## Paquete de entrada', '', '| id | ruta | commit | sha256 | bytes |', '|---|---|---|---|---|']
    out += [f"| {s['id']} | {s['path']} | {s['commit'][:12]} | {s['sha256']} | {s['bytes']} |" for s in bundle['sources']]
    if 'error' in report:
        out += ['', 'Error: `' + report['error'] + '`']
    if isinstance(report.get('api_error'), dict):
        out += ['', 'Error de la API (tipo y mensaje de Anthropic): `'
                + json.dumps(report['api_error'], ensure_ascii=False).replace('`', "'") + '`']
    review = report.get('review')
    if review:
        a, lad, g = review['analisis'], review['analisis']['escalera'], review['analisis']['crecimiento_implicito']
        rec = review['comprobaciones_mecanicas']['escalera_recalculada_anexo_c'] or {}
        out += ['', '## Salida del modelo (datos, sin acciones ejecutables)', '',
                f"Estado `{a['estado']}` · cubo «{CUBO_TEXTO[a['cubo']]}» · acción `{a['accion']}` · zona `{lad['zona']}`", '',
                '| Escenario | Valor por acción | Probabilidad |', '|---|---|---|']
        out += [f"| {k} | {_n(a['escenarios'][k]['valor_por_accion'], a['escenarios'][k]['disponible'])} |"
                f" {_n(a['escenarios'][k]['probabilidad'])} |" for k in ESCENARIOS]
        out += ['', '| Escalera (k = 3) | Declarado | Recalculado (Anexo C) |', '|---|---|---|',
                f"| Precio actual | {_n(a['precio_actual']['valor'], a['precio_actual']['disponible'])} | |",
                f"| Precio del escenario malo | {_n(lad['precio_escenario_malo'], lad['disponible'] and lad['precio_escenario_malo_disponible'])} | {_n(rec.get('precio_escenario_malo'))} |"]
        out += [f"| {label} | {_n(lad[key], lad['disponible'])} | {_n(rec.get(key))} |"
                for label, key in (('P*', 'p_estrella'), ('Precio de Sí = mín(P*, V_normal)', 'precio_si'),
                                   ('Ponderado', 'ponderado'))]
        out += [f"| Crecimiento implícito al precio actual / del normal (%) | {_n(g['al_precio_actual_pct'], g['disponible'])}"
                f" / {_n(g['del_escenario_normal_pct'], g['disponible'])} | |",
                '', '| Tasa | Precio de Sí | Ponderado | Zona |', '|---|---|---|---|']
        out += [f"| {t[5:]} % | {_n(a['sensibilidad_tasa'][t]['precio_si'], a['sensibilidad_tasa'][t]['disponible'])} |"
                f" {_n(a['sensibilidad_tasa'][t]['ponderado'], a['sensibilidad_tasa'][t]['disponible'])} |"
                f" {a['sensibilidad_tasa'][t]['zona']} |" for t in TASAS]
        for title, text in (('Resumen', a['resumen']), ('Moneda', a['moneda']), ('Justificación', a['justificacion_breve']),
                            ('Probabilidades', a['motivo_probabilidades']), ('Fórmula aplicada', lad['formula_aplicada']),
                            ('Crecimiento implícito', g['explicacion_breve'])):
            out += ['', '### ' + title, ''] + _block(text)
        for k in ESCENARIOS:
            out += ['### Escenario ' + k, ''] + _block(a['escenarios'][k]['supuestos_y_cifras'])
        out += ['### Sensibilidad (comentarios)', ''] + _block('\n'.join(
            f"{t[5:]} %: {a['sensibilidad_tasa'][t]['comentario']}" for t in TASAS))
        out += ['### Qué haría falsa la conclusión', ''] + _block('\n'.join('- ' + x for x in a['que_la_haria_falsa']))
        out += ['### Lo que no sabe', ''] + _block('\n'.join('- ' + x for x in a['lo_que_no_se']))
        out += ['### Citas', ''] + _block('\n'.join(f"[{c['archivo_id']}] «{c['cita']}» → {c['sostiene']}" for c in a['citas']))
        out += ['### Comprobaciones mecánicas y normalizaciones', ''] + _block(json.dumps(
            {'comprobaciones': review['comprobaciones_mecanicas'], 'normalizaciones_enum': review['normalizaciones_enum']},
            ensure_ascii=False, indent=2))
    return '\n'.join(out) + '\n'


def make_writer(bundle, preflight):
    def write(output, report):
        output = Path(output)
        output.mkdir(parents=True, exist_ok=True)
        (output / 'report.json').write_bytes(pilot.canonical(report))
        try:
            text = render(report, bundle, preflight)
        except Exception as err:  # noqa: BLE001 - la presentación nunca impide publicar lo pagado
            text = (f"# Análisis directo\n\nEstado de la ejecución: `{report.get('state')}`\n\n"
                    f"Presentación no completada ({type(err).__name__}); ver report.json.\n")
        (output / 'report.md').write_text(text, encoding='utf-8')
    return write


# --- Configuración de AUTO1 y comprobación previa del tamaño -------------------------
def parse_max_usd(raw):
    if not isinstance(raw, str) or not re.fullmatch(r'[0-9]{1,3}(\.[0-9]{1,6})?', raw.strip()):
        raise pilot.PilotError('COSTE_MAXIMO_INVALIDO')
    value = Decimal(raw.strip())
    if not 0 < value <= HARD_MAX_USD:
        raise pilot.PilotError('COSTE_MAXIMO_FUERA_DEL_TECHO_DEL_CODIGO')
    return value




SCHEMA_EN_ENCARGO = ('\n\n## Esquema de la respuesta\n\nResponde solo con un objeto JSON que cumpla '
                     'exactamente este JSON Schema (todas las claves son obligatorias; sin texto antes ni '
                     'después). Reglas de forma: no añadas claves que no estén en el esquema ni repitas '
                     'ninguna; no uses null (si una cifra no está disponible, pon su indicador `disponible` '
                     'en false y la cifra a 0); los números van como números, sin comillas, sin separador '
                     'de miles y con punto decimal; dentro de los textos escapa las comillas dobles como '
                     '\\" y los saltos de línea como \\n; las citas pueden acortarse con «…» para evitar '
                     'caracteres problemáticos, sin cambiar su sentido. Un único objeto, en un único bloque: '
                     'no lo partas aunque sea largo.\n\n')


def system_con_esquema(encargo):
    return encargo + SCHEMA_EN_ENCARGO + json.dumps(SCHEMA, ensure_ascii=False, sort_keys=True)


def payload_sin_gramatica(bundle):
    """Como critical_review.payload, sin `output_config.format`.

    Ejecución 44288081039: con este esquema la API respondió 400 «The compiled grammar is
    too large». El esquema va en el encargo y la respuesta se valida aquí (check_schema).
    """
    return {'model': cr.MODEL, 'system': cr.SYSTEM,
            'messages': [{'role': 'user', 'content': pilot.canonical(bundle).decode()}],
            'thinking': {'type': 'adaptive'},
            'output_config': {'effort': cr.EFFORT}}


@contextlib.contextmanager
def configured(task_id, model, effort, max_usd, bundle, encargo, preflight=None):
    """Configura critical_review como hace qwen_peer_review.configure y lo restaura al salir."""
    if model not in MODELS:
        raise pilot.PilotError('MODELO_NO_AUTORIZADO')
    if effort not in EFFORTS:
        raise pilot.PilotError('ESFUERZO_INVALIDO')
    info, original_budget = MODELS[model], cr.budget

    def budget(b, count):
        # Tras count_tokens y antes de reservar: el conteo real también cabe en el contexto.
        if type(count) is int and count + MAX_OUTPUT > info['context']:
            raise pilot.PilotError('PAQUETE_SUPERA_CONTEXTO_DEL_MODELO_NO_SE_RECORTA')
        return original_budget(b, count)

    holder = preflight if preflight is not None else {}
    holder['system_sha256'] = pilot.digest(system_con_esquema(encargo).encode('utf-8'))
    values = dict(TASK=task_id, MODEL=model, EFFORT=effort, MAX_OUTPUT=MAX_OUTPUT, MAX_USD=max_usd,
                  INPUT_PRICE=info['input'], OUTPUT_PRICE=info['output'], SYSTEM=system_con_esquema(encargo), SCHEMA=SCHEMA,
                  payload=payload_sin_gramatica,
                  validate=validate, write=make_writer(bundle, holder), budget=budget)
    saved = {k: getattr(cr, k) for k in values}
    try:
        for k, v in values.items():
            setattr(cr, k, v)
        yield holder
    finally:
        for k, v in saved.items():
            setattr(cr, k, v)


def preflight(bundle, holder=None):
    """Antes de cualquier llamada: cota de tokens por bytes (un token ocupa al menos un byte).

    Aborta si el paquete no cabe en el contexto o si la reserva supera el máximo de la
    ejecución. Nunca recorta el paquete. Usa la configuración activa de critical_review.
    """
    info = MODELS[cr.MODEL]
    payload_bytes = len(pilot.canonical(cr.payload(bundle)))
    bound = payload_bytes + MARGIN_TOKENS
    reserve = (Decimal(bound) * cr.INPUT_PRICE + Decimal(MAX_OUTPUT) * cr.OUTPUT_PRICE) / 1_000_000
    result = {'payload_bytes': payload_bytes, 'input_tokens_upper_bound': bound,
              'input_tokens_rough_estimate': math.ceil(payload_bytes / 3.5),
              'max_output_tokens': MAX_OUTPUT, 'context_tokens': info['context'],
              'reserve_upper_bound_usd': str(reserve), 'max_usd': str(cr.MAX_USD),
              'usd_per_mtok_input': str(cr.INPUT_PRICE), 'usd_per_mtok_output': str(cr.OUTPUT_PRICE),
              'prices_checked': PRICES_CHECKED}
    if holder is not None:
        holder.update(result)
    if bound + MAX_OUTPUT > info['context']:
        raise pilot.PilotError('PAQUETE_SUPERA_CONTEXTO_DEL_MODELO_NO_SE_RECORTA')
    if reserve > cr.MAX_USD:
        raise pilot.PilotError('COSTE_MAXIMO_INSUFICIENTE_NO_SE_RECORTA')
    return result


class DirectHTTP(cr.StreamingHTTP):
    """El transporte SSE de AUTO1 sin cambios; solo amplía la lista de modelos autorizados.

    pilot.HTTP.__init__ admite únicamente Sonnet 5.5 y Fable 5.2; aquí se valida contra
    MODELS (con sus tarifas). El cuerpo de cada llamada sigue ligado a self.model.
    """
    def __init__(self, github_token='', api_key='', model=DEFAULT_MODEL):
        if model not in MODELS:
            raise pilot.PilotError('MODELO_NO_AUTORIZADO')
        self.github_token, self.api_key, self.model = github_token, api_key, model


def task_id_for(empresa, run_id):
    if not isinstance(run_id, str) or not re.fullmatch(r'[0-9]{1,20}', run_id):
        raise pilot.PilotError('RUN_ID_INVALIDO')
    return f'analisis-directo-{_slug(empresa, "EMPRESA_INVALIDA")}-{run_id}'


def execute(http, bundle, encargo, model, effort, max_usd, output, live=False, receipt=None):
    """Comprobación previa y, solo si pasa, critical_review.run (una llamada como máximo)."""
    with configured(bundle['task_id'], model, effort, max_usd, bundle, encargo) as holder:
        try:
            preflight(bundle, holder)
        except pilot.PilotError as err:
            write_abort(output, bundle, holder, str(err))
            raise
        return cr.run(http, bundle, output, receipt=receipt, execute=live)


def write_abort(output, bundle, holder, code):
    output = Path(output)
    output.mkdir(parents=True, exist_ok=True)
    lines = ['# Análisis directo · ' + bundle['caso'], '', 'Abortado antes de llamar: `' + code + '`', '',
             'Ninguna llamada a Anthropic, ninguna reserva. El paquete no se recorta.', '']
    lines += [f'- {k}: {v}' for k, v in holder.items()]
    (output / 'report.md').write_text('\n'.join(lines) + '\n', encoding='utf-8')
    (output / 'preflight.json').write_bytes(pilot.canonical({'error': code, **holder}))


def main(argv=None):
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--empresa', required=True)
    p.add_argument('--package', required=True, help='manifiesto JSON versionado en el repo')
    p.add_argument('--model', default=DEFAULT_MODEL)
    p.add_argument('--effort', default='high')
    p.add_argument('--max-usd', required=True)
    p.add_argument('--run-id', required=True)
    p.add_argument('--code-sha', required=True)
    p.add_argument('--output', type=Path, required=True)
    p.add_argument('--execute-api', action='store_true')
    a = p.parse_args(argv)
    try:
        max_usd = parse_max_usd(a.max_usd)
        task_id = task_id_for(a.empresa, a.run_id)
        encargo = verify_code(ROOT, a.code_sha)
        bundle = build_bundle(load_package(ROOT, a.code_sha, a.package, a.empresa), encargo, task_id, a.code_sha)
        http = DirectHTTP(os.getenv('GH_TOKEN', ''), os.getenv('ANTHROPIC_API_KEY', ''), model=a.model)
        report = execute(http, bundle, encargo, a.model, a.effort, max_usd, a.output, live=a.execute_api)
        print(json.dumps({k: report.get(k) for k in ('task_id', 'state', 'api_messages_sent', 'estimated_cost_usd', 'error', 'api_error')}))
        # YA_RESERVADO_SIN_NUEVA_LLAMADA (p. ej. «Re-run» de la misma ejecución) sale con 1:
        # no hay análisis nuevo y no debe parecer un éxito.
        return 0 if report['state'] in OK_STATES else 1
    except (pilot.PilotError, subprocess.CalledProcessError, OSError) as err:
        print(str(err) if isinstance(err, pilot.PilotError) else 'GIT_O_ARCHIVO_NO_VERIFICABLE', file=sys.stderr)
        return 2


if __name__ == '__main__':
    sys.exit(main())
