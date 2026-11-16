"""Utilidades comunes del frente A (cobertura integral M2).

Solo lectura sobre el producto: los insumos viven en .trabajo/insumos_m2
(seleccion parcial verificada por herramientas/preparar_insumos.py) y los
registros de entrada en docs/programa_mistral_m2/entrada. Este paquete no
ejecuta el pipeline ni modifica ningun archivo del producto.
"""
import csv
import hashlib
import json
import re
import unicodedata
from decimal import Decimal
from pathlib import Path

REPO = Path(__file__).resolve().parents[3]
TAREA = REPO / 'docs' / 'programa_mistral_m2'
ENTRADA = TAREA / 'entrada'
INSUMOS = REPO / '.trabajo' / 'insumos_m2'
OUT = REPO / 'resultados_m2' / 'cobertura_vm'
RESULTADOS = OUT / 'resultados'

EMPRESAS = ('Vidrala', 'Viscofan')
CARPETA_EMPRESA = {
    'Vidrala': 'personaje_v2/empresas_v2_correcciones/2026-11_Vidrala_ensayo_4_14/vidrala_decisiones/Vidrala',
    'Viscofan': 'personaje_v2/empresas_v2_correcciones/2026-11_Vidrala_ensayo_4_14/viscofan_decisiones/Viscofan',
}
XLSX = {
    'Vidrala': 'Vidrala_v63_evaluada.xlsx',
    'Viscofan': 'Viscofan_v63_evaluada.xlsx',
}
REGISTRO_OFICIAL = 'verificacion_entradas.json'

ESTADOS_PERMITIDOS = {
    'COINCIDE_PROPUESTO', 'DIFERENCIA', 'NO_ACREDITADO', 'HIPOTESIS',
    'CONVENCION', 'DATO_AUSENTE', 'NO_APLICABLE',
}
CLASE_A_ESTADO = {
    'hipotesis': 'HIPOTESIS',
    'convencion': 'CONVENCION',
    'dato_ausente': 'DATO_AUSENTE',
    'no_aplicable': 'NO_APLICABLE',
}
TOL = Decimal('0.0005')  # redondeo del libro a 3 decimales (mm)

PAGE_RE = re.compile(r'^\[PDF PAGE (\d+)\]\s*$')


def sha256_file(path):
    h = hashlib.sha256()
    with open(path, 'rb') as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b''):
            h.update(chunk)
    return h.hexdigest()


def load_json(path):
    with open(path, encoding='utf-8') as f:
        return json.load(f)


def dump_json(obj, path):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(obj, f, ensure_ascii=False, indent=2, sort_keys=False)
        f.write('\n')


def load_registro():
    return load_json(ENTRADA / 'registro_base.json')


def load_indice():
    return load_json(ENTRADA / 'indice_fuentes.json')


def load_catalogo():
    with open(ENTRADA / 'catalogo_entradas.csv', encoding='utf-8') as f:
        return list(csv.DictReader(f))


def load_configuracion():
    return load_json(ENTRADA / 'configuracion.json')


def iter_entradas(registro):
    for empresa in EMPRESAS:
        for row in registro[empresa]['entradas']:
            yield empresa, row


def ruta_insumo(empresa, archivo):
    """Ruta dentro de .trabajo/insumos_m2 para el archivo declarado de una empresa."""
    return INSUMOS / CARPETA_EMPRESA[empresa] / archivo


def indice_por_ruta(indice):
    return {a['ruta']: a for a in indice['archivos']}


def norm_text(s):
    if s is None:
        return ''
    s = unicodedata.normalize('NFKC', str(s))
    s = s.replace('\u2212', '-').replace('\u2013', '-').replace('\u2014', '-')
    s = s.replace('\u00a0', ' ')
    return re.sub(r'\s+', ' ', s).strip()


def flat_text(s):
    return re.sub(r'\s+', '', norm_text(s))


def extract_pages(text):
    """Separa un .txt extraido con marcadores [PDF PAGE n] en {pagina: texto}."""
    pages = {}
    current = 0
    buf = []
    for line in text.splitlines():
        m = PAGE_RE.match(line)
        if m:
            pages[current] = '\n'.join(buf)
            current = int(m.group(1))
            buf = []
        else:
            buf.append(line)
    pages[current] = '\n'.join(buf)
    return pages


def variantes_numero(valor):
    """Variantes de formato de un numero (ES y EN) para buscar en el texto."""
    if valor is None:
        return set()
    try:
        d = Decimal(str(valor))
    except Exception:
        return set()
    sign = '-' if d < 0 else ''
    mag = -d if d < 0 else d
    s = format(mag, 'f')
    if '.' in s:
        intpart, decpart = s.split('.')
        decpart = decpart.rstrip('0')
    else:
        intpart, decpart = s, ''

    def group3(ip, sep):
        parts = []
        while len(ip) > 3:
            parts.insert(0, ip[-3:])
            ip = ip[:-3]
        parts.insert(0, ip)
        return sep.join(parts)

    ints = {intpart}
    for sep in (',', '.', ' '):
        ints.add(group3(intpart, sep))
    out = set()
    for ip in ints:
        if decpart:
            out.add(sign + ip + '.' + decpart)
            out.add(sign + ip + ',' + decpart)
        else:
            out.add(sign + ip)
            if sign:
                out.add('(' + ip + ')')
    out.add(sign + ip + ('.' + decpart if decpart else ''))
    return {v for v in out if v}


def buscar_valor_en_pagina(page_text, valor):
    """True si alguna variante del numero aparece en la pagina (texto plano)."""
    if valor is None or page_text is None:
        return False
    flat = flat_text(page_text)
    norm = norm_text(page_text)
    for v in variantes_numero(valor):
        vf = flat_text(v)
        if vf and (vf in flat or vf in flat_text(norm)):
            return True
        if norm and v in norm:
            return True
    return False


def buscar_cita_en_pagina(page_text, cita):
    if not cita or page_text is None:
        return False
    c_norm = norm_text(cita)
    c_flat = flat_text(cita)
    p_norm = norm_text(page_text)
    p_flat = flat_text(page_text)
    return (c_norm and c_norm in p_norm) or (c_flat and c_flat in p_flat)


def dec(v):
    if v is None:
        return None
    try:
        return Decimal(str(v))
    except Exception:
        return None


def diff_ok(a, b, tol=TOL):
    """True si coinciden (numerico dentro de tol, o texto igual normalizado)."""
    da, db = dec(a), dec(b)
    if da is not None and db is not None:
        return abs(da - db) <= tol
    if a is None or b is None:
        return None
    return norm_text(a) == norm_text(b)


def leer_xlsx_celdas(empresa):
    """Valores cacheados del libro (solo lectura) para las hojas del registro."""
    import openpyxl
    path = INSUMOS / CARPETA_EMPRESA[empresa] / XLSX[empresa]
    wb = openpyxl.load_workbook(path, read_only=True, data_only=True)
    celdas = {}
    for sheet in wb.sheetnames:
        ws = wb[sheet]
        for row in ws.iter_rows():
            for c in row:
                if c.value is not None:
                    celdas[f'{sheet}!{c.coordinate}'] = c.value
    wb.close()
    return celdas


def leer_registro_oficial(empresa):
    path = INSUMOS / CARPETA_EMPRESA[empresa] / REGISTRO_OFICIAL
    data = load_json(path)
    return {e['celda']: e for e in data['entradas']}


def snippet_pagina(page_text, cita, ventana=2, max_chars=600):
    """Fragmento acotado de la pagina alrededor de la cita (para revision)."""
    if not page_text:
        return ''
    lines = page_text.splitlines()
    norm_c = flat_text(cita or '')
    idx = None
    for i, line in enumerate(lines):
        if norm_c and norm_c and flat_text(line) and (flat_text(cita) in flat_text(line) or flat_text(line) in flat_text(cita)):
            idx = i
            break
    if idx is None:
        for i, line in enumerate(lines):
            if norm_c and flat_text(norm_c[:40]) and flat_text(norm_c[:40]) in flat_text(line):
                idx = i
                break
    if idx is None:
        return norm_text(page_text)[:max_chars]
    lo = max(0, idx - ventana)
    hi = min(len(lines), idx + ventana + 1)
    return norm_text('\n'.join(lines[lo:hi]))[:max_chars]
