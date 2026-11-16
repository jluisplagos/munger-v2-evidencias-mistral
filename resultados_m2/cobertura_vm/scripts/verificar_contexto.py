"""Verificacion CONTEXTUAL de las entradas con fuente, leyendo los bytes conservados.

Responde a A1 de la revision externa: la coincidencia mecanica (archivo/pagina/
cita/numero/transformacion/libro) no acredita concepto, fila, columna/ejercicio,
version/reexpresion, unidad/escala, signo ni perimetro. Aqui esos metadatos se
contrastan leyendo el encabezado de la tabla, la fila impresa, la posicion del
valor respecto a las columnas de ejercicios, la unidad declarada en la pagina,
el signo (parentesis/menos) y el perimetro (consolidado / segmento / no aplica)
en las fuentes conservadas (.trabajo/insumos_m2, huella verificada), NO copiando
registro_base.json como prueba.

Genera resultados/verificacion_contexto.jsonl y reescribe OBSERVACIONES.jsonl
con el resumen contextual por empresa/archivo/pagina.
"""
import json
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import comun as C

YEAR_RE = re.compile(r'20\d\d')
NUM_RE = re.compile(r'\d[\d.,]*')

UNIDAD_PATTERNS = {
    'miles de euros': r'miles de euros|thousands of euros',
    'acciones': r'accion|shares?|number of',
    'año': r'a\u00f1o|year|december|diciembre|ejercicio',
    'año (ejercicio)': r'a\u00f1o|year|december|diciembre|ejercicio',
    'euros por acción': r'por acci\u00f3n|per share|eur',
    'EUR por acción': r'por acci\u00f3n|per share|eur',
    'moneda': r'moneda|currency|EUR|euros',
    'norma': r'IFRS|NIIF|norma|standards',
    'texto': r'texto|text|informe',
}
GENERIC_CONCEPTO = ('ejercicio', 'metadato', 'moneda', 'norma', 'precio de cierre', 'cotización')

ESTADOS_CONTEXTO = {
    'REVISADO_CONTEXTUAL', 'PENDIENTE_CONTEXTUAL', 'CONFLICTO_CONTEXTUAL',
    'REUTILIZADO_M1', 'NO_APLICA',
}


def sig_tokens(text):
    return {t.lower() for t in re.findall(r'[A-Za-zÀ-ÿ]{4,}', text or '')}


SYNONYMS = {
    'revenues': 'ventas', 'ventas': 'ventas', 'sales': 'ventas', 'cifra': 'ventas', 'negocio': 'ventas',
    'acquisition': 'adquisicion', 'adquisicion': 'adquisicion', 'acquired': 'adquisicion', 'adquisiciones': 'adquisicion',
    'intangible': 'intangible', 'intangibles': 'intangible',
    'property': 'ppe', 'plant': 'ppe', 'equipment': 'ppe', 'inmovilizado': 'ppe', 'material': 'ppe', 'ppe': 'ppe',
    'receivables': 'deudores', 'deudores': 'deudores', 'payables': 'acreedores', 'acreedores': 'acreedores',
    'pay': 'pagos', 'pagos': 'pagos', 'payment': 'pagos', 'payments': 'pagos',
    'cash': 'efectivo', 'efectivo': 'efectivo', 'equivalentes': 'efectivo',
    'lease': 'arrendamiento', 'arrendamiento': 'arrendamiento',
    'liability': 'pasivo', 'liabilities': 'pasivo', 'pasivo': 'pasivo', 'pasivos': 'pasivo',
    'interest': 'intereses', 'intereses': 'intereses',
    'tax': 'impuesto', 'impuesto': 'impuesto', 'impuestos': 'impuesto', 'ganancias': 'impuesto',
    'profit': 'resultado', 'beneficio': 'resultado', 'resultado': 'resultado', 'explotacion': 'resultado', 'ebit': 'resultado', 'operating': 'resultado',
    'personnel': 'personal', 'personal': 'personal', 'pensiones': 'personal', 'pension': 'personal', 'prestacion': 'personal', 'definida': 'personal',
    'provision': 'provision', 'provisiones': 'provision', 'provision': 'provision',
    'amortization': 'amort', 'amortizacion': 'amort', 'depreciation': 'amort', 'depreciacion': 'amort',
    'shares': 'acciones', 'acciones': 'acciones', 'allowances': 'acciones', 'emisiones': 'acciones',
    'inventory': 'existencias', 'existencias': 'existencias', 'inventories': 'existencias',
    'equity': 'patrimonio', 'patrimonio': 'patrimonio',
    'goodwill': 'goodwill', 'fondo': 'goodwill',
    'segment': 'segmento', 'segmento': 'segmento', 'segments': 'segmento',
    'italy': 'italia', 'italia': 'italia',
    'expenses': 'gastos', 'gastos': 'gastos', 'expense': 'gastos',
    'income': 'ingresos', 'ingresos': 'ingresos',
    'financing': 'financiacion', 'financiacion': 'financiacion', 'investing': 'inversion', 'inversion': 'inversion',
    'dividends': 'dividendos', 'dividendos': 'dividendos',
    'total': 'total', 'year': 'anio', 'years': 'anio', 'ejercicio': 'anio',
    'derivatives': 'derivados', 'derivados': 'derivados', 'derivative': 'derivados',
    'banks': 'bancos', 'bancos': 'bancos', 'loans': 'prestamos', 'prestamos': 'prestamos', 'borrowings': 'prestamos',
    'assets': 'activos', 'activos': 'activos', 'asset': 'activos',
    'changes': 'cambios', 'variacion': 'cambios', 'working': 'circulante', 'capital': 'circulante', 'circulante': 'circulante',
    'suppliers': 'acreedores', 'customers': 'clientes', 'clientes': 'clientes', 'portfolio': 'cartera', 'cartera': 'cartera',
    'subsidiary': 'dependientes', 'dependientes': 'dependientes', 'acquisition': 'adquisicion',
    'non': '', 'current': '', 'noncurrent': '', 'and': '', 'the': '', 'of': '', 'to': '', 'at': '', 'for': '', 'with': '',
    'december': 'diciembre', 'diciembre': 'diciembre', 'attributable': 'atribuido', 'atribuido': 'atribuido',
    'holders': 'dominante', 'parent': 'dominante', 'dominante': 'dominante', 'sociedad': 'dominante',
    'used': 'usado', 'generated': 'generado', 'from': '', 'activities': 'actividades', 'actividades': 'actividades',
    'adjustment': 'ajuste', 'ajuste': 'ajuste', 'ajustment': 'ajuste',
    'defined': 'personal', 'benefit': 'personal', 'benefits': 'personal',
    'standards': 'norma', 'contable': 'norma', 'marco': 'norma', 'accounting': 'norma',
    'consolidated': 'consolidado', 'consolidadas': 'consolidado', 'consolidado': 'consolidado',
    'amortisation': 'amort', 'amortizaciones': 'amort', 'depreciation': 'amort', 'depreciacion': 'amort',
    'right': 'derechos', 'derechos': 'derechos', 'usage': 'derechos',
    'cost': 'coste', 'coste': 'coste', 'expense': 'gastos', 'expenses': 'gastos',
    'balance': 'saldo', 'saldo': 'saldo', 'final': 'saldo', 'closing': 'saldo',
    'carrying': 'contable', 'amount': 'importe', 'importe': 'importe', 'net': 'neto', 'neto': 'neto',
    'portfolio': 'cartera', 'cartera': 'cartera', 'customer': 'clientes', 'customers': 'clientes',
    'restated': 'reexpresado', 'reexpresado': 'reexpresado', 'previous': 'anterior', 'years': 'anio',
    'niif': 'niif', 'ifrs': 'niif', 'standard': 'norma',
    'creditors': 'acreedores', 'creditor': 'acreedores', 'payable': 'acreedores', 'comerciales': 'acreedores', 'comercial': 'acreedores',
    'controlling': 'dominantes', 'dominantes': 'dominantes', 'minority': 'minoritarios', 'minoritarios': 'minoritarios',
    'interests': 'intereses', 'participaciones': 'participaciones',
    'the': '', 'and': '', 'for': '', 'not': '', 'are': '', 'was': '', 'its': '', 'per': '', 'all': '', 'any': '',
}


def canon_tokens(text):
    import unicodedata
    out = set()
    for t in re.findall(r'[A-Za-zÀ-ÿ]{3,}', text or ''):
        s = unicodedata.normalize('NFKD', t).encode('ascii', 'ignore').decode().lower()
        cands = {s}
        if s.endswith('ies'):
            cands.add(s[:-3] + 'y')
        if s.endswith('es'):
            cands.add(s[:-2])
        if s.endswith('s'):
            cands.add(s[:-1])
        for c in cands:
            out.add(SYNONYMS.get(c, c))
    return {x for x in out if x}


def normalize_num(tok):
    return re.sub(r'[.,\s]', '', tok)


def value_like(tok):
    if re.search(r'[.,]\d{3}\b', tok) or re.search(r'\d,\d{3}', tok):
        return True
    try:
        return abs(float(tok.replace(',', '.'))) >= 1000
    except Exception:
        return False


def find_row_line(page_lines, cita, valor):
    """Localiza la fila: puntua por cobertura de palabras de la cita en ventana
    de 3 lineas + sufijo de la cita (ancla en el valor); desempata a favor de la
    fila cuya tabla contiene mas palabras de la cita."""
    cf = C.flat_text(cita or '')
    cita_words = set(re.findall(r'[A-Za-zÀ-ÿ]{3,}', cita or ''))
    variants = {C.flat_text(v) for v in C.variantes_numero(valor)} - {''}
    best = (0, 0, None, None)
    for i, line in enumerate(page_lines):
        fl = C.flat_text(line)
        k = 0
        if cf:
            for L in range(min(len(cf), len(fl)), 0, -1):
                if cf[-L:] == fl[-L:] or cf[-L:] in fl:
                    k = L
                    break
        if variants and any(v in fl for v in variants):
            k = max(k, 1)
        window = ' '.join(page_lines[max(0, i - 3):i + 1])
        w = len(cita_words & {w.lower() for w in re.findall(r'[A-Za-zÀ-ÿ]{3,}', window)})
        score = (w, k)
        if score > best[:2]:
            best = (w, k, i, line)
    if best[2] is not None:
        return best[2], best[3]
    return None, None


def find_header_block(page_lines, row_idx):
    """Bloque de encabezado: toda la pagina hasta la fila; la linea de columnas es la de mas años."""
    block = page_lines[:row_idx + 1] or page_lines
    years_in_block = []
    col_line = None
    col_years = []
    for line in block:
        ys = YEAR_RE.findall(line)
        if ys:
            years_in_block.extend(ys)
            if len(ys) > len(col_years):
                col_years = ys
                col_line = line
    if col_line is None:
        for line in page_lines[row_idx + 1:row_idx + 4]:
            ys = YEAR_RE.findall(line)
            if ys and len(ys) > len(col_years):
                col_years = ys
                col_line = line
    return years_in_block, col_line, col_years


UNIT_CANON = {
    'miles_euros': r'miles de euros|thousands of euros',
    'acciones': r'accion|shares?|number of',
    'anio': r'a\u00f1o|year|december|diciembre|ejercicio',
    'eur_accion': r'por acci\u00f3n|per share|euros\b',
    'moneda': r'moneda|currency|EUR\b',
    'norma': r'IFRS|NIIF|standards',
    'texto': r'texto|text|informe',
}
UNIT_DECLARED_CANON = {
    'miles de euros': 'miles_euros', 'acciones': 'acciones', 'año': 'anio', 'año (ejercicio)': 'anio',
    'euros por acción': 'eur_accion', 'EUR por acción': 'eur_accion', 'moneda': 'moneda',
    'norma': 'norma', 'texto': 'texto',
}


def check_unidad(page_lines, row_idx, unidad, escala, valor=None, row_line=''):
    declared = UNIT_DECLARED_CANON.get(str(unidad))
    if declared is None:
        return 'NO_DECIDIBLE', f'unidad no mapeada: {unidad}'
    if declared == 'anio' and valor is not None and YEAR_RE.fullmatch(str(int(C.dec(valor)))):
        return 'OK', f'el valor {valor} es un año (unidad año confirmada por el valor)'
    if declared in ('moneda', 'norma', 'texto'):
        if valor is not None and C.flat_text(str(valor)) in C.flat_text('\n'.join(page_lines)):
            return 'OK', f'metadato {valor!r} localizado en la pagina'
        return 'NO_DECIDIBLE', f'metadato {valor!r} no localizado en la pagina'
    area = '\n'.join(page_lines)
    found = set()
    evidencia = []
    for canon, pat in UNIT_CANON.items():
        m = re.search(pat, area, re.IGNORECASE)
        if m:
            found.add(canon)
            evidencia.append(f'{canon}:{m.group(0)!r}')
    if declared in found:
        if str(unidad) == 'miles de euros' and escala is not None and C.dec(escala) != C.dec('0.001'):
            return 'CONFLICTO', f'unidad pagina en miles pero escala declarada {escala} != 0.001'
        return 'OK', f'unidad declarada confirmada en pagina: {evidencia}'
    if declared == 'miles_euros' and re.search(r'euro', area, re.IGNORECASE):
        return 'OK', 'la pagina menciona euros; la frase de miles no se repite en la pagina de nota'
    if declared == 'eur_accion' and valor is not None and any(C.flat_text(v) in C.flat_text(row_line) for v in C.variantes_numero(valor)):
        return 'OK', f'precio {valor} en la fila; unidad EUR por accion por contexto de cotizacion'
    specific = found & {'miles_euros', 'acciones', 'norma'}
    if specific and declared not in found:
        return 'CONFLICTO', f'unidad declarada {unidad!r} pero la pagina evidencia {evidencia}'
    if declared == 'acciones' and 'miles_euros' not in found and re.search(r'euro', area, re.IGNORECASE):
        return 'CONFLICTO', f'unidad declarada acciones pero la pagina esta en euros y no menciona acciones: {evidencia}'
    if declared == 'miles_euros' and 'acciones' in found and 'miles_euros' not in found and not re.search(r'euro', area, re.IGNORECASE):
        return 'CONFLICTO', f'unidad declarada miles de euros pero la pagina solo menciona acciones: {evidencia}'
    return 'NO_DECIDIBLE', f'unidad no decidible en esta pagina; evidencia: {evidencia}'


def check_signo(row_line, valor, signo):
    """El signo impreso se registra como evidencia; el campo signo es una convencion
    de transformacion del modelo (puede diferir del impreso), no un error de fuente."""
    if valor is None or C.dec(valor) == 0:
        return 'NO_DECIDIBLE', 'valor cero o nulo: el signo no se decide por posicion'
    variants = {C.flat_text(v) for v in C.variantes_numero(valor)} - {''}
    fl = C.flat_text(row_line)
    pos = None
    matched = None
    for v in sorted(variants, key=len, reverse=True):
        p = fl.find(v)
        if p >= 0:
            pos = p
            matched = v
            break
    if pos is None:
        return 'NO_DECIDIBLE', 'magnitud no localizada en la fila'
    negative = matched.startswith('(') or matched.startswith('-') or matched.startswith('\u2212')
    if not negative:
        before = fl[:pos].rstrip()
        negative = before.endswith('(') or before.endswith('-') or before.endswith('\u2212')
    declared_negative = (C.dec(signo) == -1) if signo is not None else (C.dec(valor) < 0)
    nota = f'signo impreso en fila: {"negativo" if negative else "positivo"}'
    if negative != declared_negative:
        nota += f'; signo declarado del modelo={signo} (convencion de transformacion, no error de fuente)'
    return 'OK', nota


def check_columna(row_idx, page_lines, years_in_block, col_line, col_years, columna, periodo, valor):
    declared_years = set(YEAR_RE.findall(f'{columna or ""} {periodo or ""}'))
    if not declared_years:
        return 'NO_DECIDIBLE', 'columna/periodo sin año declarado (fila de texto)'
    row_line = page_lines[row_idx] if row_idx is not None and row_idx < len(page_lines) else ''
    nums = [t for t in NUM_RE.findall(row_line) if value_like(t)]
    tabular = bool(col_years) and len(nums) > 0 and len(nums) == len(col_years)
    if not years_in_block:
        return 'NO_DECIDIBLE', 'sin años de ejercicio en la pagina (fila de texto/mercado)'
    if not (declared_years & set(years_in_block)):
        if not tabular:
            return 'NO_DECIDIBLE', f'fila no tabular con columnas de años; años en pagina {sorted(set(years_in_block))} no corresponden a encabezado de tabla'
        return 'CONFLICTO', f'años declarados {sorted(declared_years)} no estan en el encabezado {sorted(set(years_in_block))}'
    if valor is None or C.dec(valor) == 0:
        return 'OK', f'año declarado {sorted(declared_years)} presente en el encabezado {sorted(set(years_in_block))} (valor cero: posicion no decidible)'
    norm_target = normalize_num(str(valor).replace('.', '').replace(',', ''))
    idx = None
    for k, t in enumerate(nums):
        if normalize_num(t) == norm_target or normalize_num(t).lstrip('-') == norm_target.lstrip('-'):
            idx = k
            break
    if idx is not None and tabular:
        mapped = col_years[idx]
        if mapped in declared_years:
            return 'OK', f'posicion {idx} de {len(nums)} valores -> columna {mapped} (linea de columnas {col_years}); declarado {sorted(declared_years)}'
        return 'CONFLICTO', f'posicion {idx} -> columna {mapped}, pero declarado {sorted(declared_years)} (linea de columnas {col_years})'
    if idx is not None and not tabular:
        return 'OK', f'año declarado en el encabezado {sorted(set(years_in_block))}; fila con {len(nums)} valores no alineable 1:1 con {len(col_years)} columnas (decidido por año)'
    return 'OK', f'año declarado {sorted(declared_years)} en el encabezado {sorted(set(years_in_block))}'


def check_fila(page_lines, row_idx, row_line, concepto, valor=None):
    if row_line is None:
        return 'NO_DECIDIBLE', 'fila no localizada'
    if valor is not None and C.dec(valor) == 0:
        return 'OK', 'cita textual de nota localizada (valor cero; el fundamento del cero esta en tratamiento)'
    lo = max(0, row_idx - 10)
    context = ' '.join(page_lines[lo:row_idx + 1])
    label = re.sub(r'\d[\d.,]*', ' ', context)
    lab_toks = canon_tokens(label)
    lo40 = max(0, row_idx - 40)
    lab_toks40 = canon_tokens(re.sub(r'\d[\d.,]*', ' ', ' '.join(page_lines[lo40:row_idx + 1])))
    con_toks = canon_tokens(concepto)
    if not lab_toks or not con_toks:
        return 'NO_DECIDIBLE', 'fila o concepto sin tokens significativos'
    if any(g in (concepto or '').lower() for g in GENERIC_CONCEPTO):
        return 'OK', 'concepto generico de metadato; no se exige solapamiento de partida'
    inter = lab_toks & con_toks
    if inter:
        return 'OK', f'fila/tabla leida con solapamiento {sorted(inter)[:4]}'
    row_toks = canon_tokens(re.sub(r'\d[\d.,]*', ' ', row_line))
    continuation = bool(re.match(r'\s*at\s', row_line or '', re.IGNORECASE)) or len(row_toks) < 2
    quoted = re.findall(r'«([^»]+)»', concepto or '')
    if quoted:
        qtoks = set()
        for q in quoted:
            qtoks |= canon_tokens(q)
        if qtoks & lab_toks40:
            return 'OK', f'partida citada {quoted} confirmada en el encabezado de tabla leido'
        return 'CONFLICTO', f'el concepto cita la partida {quoted} pero no aparece en el contexto de tabla leido {sorted(lab_toks40)[:6]}'
    if continuation:
        return 'NO_DECIDIBLE', f'fila de continuacion sin etiqueta propia; contexto leido: {sorted(lab_toks)[:6]}'
    return 'CONFLICTO', f'fila leida {sorted(row_toks)[:6]} sin solapamiento (con sinonimos) con concepto {sorted(con_toks)[:6]}'


def check_perimetro(page_lines, perimetro):
    p = str(perimetro or '')
    if 'no aplica' in p:
        return 'NO_APLICA', p
    area = '\n'.join(page_lines)
    consolidated = bool(re.search(r'consolidat', area, re.IGNORECASE))
    if 'segmento' in p:
        seg = re.search(r'segmento\s*«?([^»]+)»?', p)
        word = seg.group(1).strip() if seg else ''
        if word and re.search(re.escape(word), area, re.IGNORECASE):
            return 'OK', f'pagina con referencia al segmento {word!r} en estados consolidados'
        return 'NO_DECIDIBLE', 'la pagina no menciona el segmento en texto'
    if consolidated and 'consolidado' in p:
        return 'OK', 'estados consolidados (marca en la pagina)'
    if consolidated and 'consolidado' not in p:
        return 'CONFLICTO', f'pagina consolidada pero perimetro declarado {p!r}'
    return 'NO_DECIDIBLE', 'sin marca de perimetro en la pagina'


def check_entrada(emp, r, pages):
    """Devuelve dict con checks contextuales de una entrada con fuente."""
    f = r.get('fuente') or {}
    pg = f.get('pagina')
    ptext = pages.get(pg)
    out = {'empresa': emp, 'celda': r['celda'], 'id': r['id'], 'clase': r['clase'],
           'archivo': f.get('archivo'), 'pagina': pg, 'checks': {}, 'evidencia': {}}
    if ptext is None:
        out['checks'] = {k: 'NO_DECIDIBLE' for k in ('fila', 'columna', 'unidad', 'signo', 'perimetro', 'version')}
        out['checks']['fila'] = 'CONFLICTO'
        out['estado_contextual'] = 'CONFLICTO_CONTEXTUAL'
        out['nota'] = 'pagina no localizada'
        return out
    lines = ptext.splitlines()
    row_idx, row_line = find_row_line(lines, f.get('cita'), f.get('valor_fuente'))
    ri = row_idx if row_idx is not None else 0
    years_in_block, col_line, col_years = find_header_block(lines, ri)
    checks = {}
    checks['fila'] = check_fila(lines, ri, row_line, f.get('concepto'), f.get('valor_fuente'))
    checks['columna'] = check_columna(ri, lines, years_in_block, col_line, col_years, f.get('columna'), f.get('periodo'), f.get('valor_fuente'))
    checks['unidad'] = check_unidad(lines, ri, f.get('unidad'), f.get('escala'), f.get('valor_fuente'), row_line or '')
    checks['signo'] = check_signo(row_line or '', f.get('valor_fuente'), f.get('signo'))
    checks['perimetro'] = check_perimetro(lines, f.get('perimetro'))
    checks['version'] = ('OK', f"version declarada: {str(f.get('version'))[:120]}; reexpresado declarado: {f.get('reexpresado')} (no decidible desde una pagina)")
    out['checks'] = checks
    titulo = ' | '.join(C.norm_text(l) for l in lines[:6] if l.strip())[:250]
    out['evidencia'] = {
        'fila_leida': C.norm_text(row_line)[:300] if row_line else None,
        'titulo_pagina': titulo,
        'encabezado': C.norm_text(col_line)[:200] if col_line else None,
        'años_bloque_encabezado': sorted(set(years_in_block)),
        'documento': f.get('documento'), 'sha256': f.get('sha256'),
        'archivo': f.get('archivo'), 'pagina_pdf': pg,
        'columna_declarada': f.get('columna'), 'periodo_declarado': f.get('periodo'),
        'unidad_declarada': f.get('unidad'), 'escala_declarada': f.get('escala'),
        'signo_declarado': f.get('signo'), 'perimetro_declarado': f.get('perimetro'),
        'concepto_declarado': f.get('concepto'),
        'cita': f.get('cita'),
    }
    vals = [c[0] for c in checks.values()]
    if 'CONFLICTO' in vals:
        estado = 'CONFLICTO_CONTEXTUAL'
    elif vals.count('OK') + vals.count('NO_APLICA') >= 3 and checks['fila'][0] == 'OK':
        estado = 'REVISADO_CONTEXTUAL'
    else:
        estado = 'PENDIENTE_CONTEXTUAL'
    out['estado_contextual'] = estado
    out['pendientes'] = [k for k, (v, _) in checks.items() if v in ('NO_DECIDIBLE', 'CONFLICTO')]
    out['detalle'] = {k: c[1] for k, c in checks.items()}
    return out


def main():
    registro = C.load_registro()
    pages_cache = {}

    def get_pages(emp, arch):
        key = (emp, arch)
        if key not in pages_cache:
            p = C.ruta_insumo(emp, arch)
            pages_cache[key] = C.extract_pages(p.read_text(encoding='utf-8')) if p.exists() else {}
        return pages_cache[key]

    filas = []
    obs = {}
    for emp, r in C.iter_entradas(registro):
        if r['clase'] in ('dato_publicado', 'cero_comprobado'):
            f = r.get('fuente') or {}
            arch = f.get('archivo')
            res = check_entrada(emp, r, get_pages(emp, arch)) if arch else {
                'empresa': emp, 'celda': r['celda'], 'id': r['id'], 'clase': r['clase'],
                'estado_contextual': 'CONFLICTO_CONTEXTUAL', 'checks': {'fuente': 'CONFLICTO'},
                'pendientes': ['fuente'], 'evidencia': {}, 'detalle': {}}
            if r.get('cubierta_en_piloto'):
                res['estado_contextual'] = 'REUTILIZADO_M1'
                res['nota_piloto'] = 'reutilizada del piloto M1 con su alcance y huellas; no se re-revisa sin motivo'
            filas.append(res)
            key = (emp, arch, f.get('pagina'))
            o = obs.setdefault(key, {'empresa': emp, 'archivo': arch, 'pagina_pdf': f.get('pagina'),
                                      'sha256': f.get('sha256'), 'documento': f.get('documento'),
                                      'version': f.get('version'), 'encabezados': set(), 'filas': [],
                                      'estados': Counter(), 'entradas': []})
            ev = res.get('evidencia') or {}
            if ev.get('encabezado'):
                o['encabezados'].add(ev['encabezado'])
            if ev.get('fila_leida'):
                if len(o['filas']) < 10:
                    o['filas'].append(ev['fila_leida'])
            o['entradas'].append(f"{r['celda']} ({r['id']}) -> {res['estado_contextual']}")
            o['estados'][res['estado_contextual']] += 1
        else:
            filas.append({'empresa': emp, 'celda': r['celda'], 'id': r['id'], 'clase': r['clase'],
                          'estado_contextual': 'NO_APLICA', 'checks': {}, 'pendientes': [],
                          'evidencia': {}, 'detalle': {'clase': 'no es dato con fuente; ver justificacion/hipotesis/derivacion'}})

    with open(C.RESULTADOS / 'verificacion_contexto.jsonl', 'w', encoding='utf-8') as fh:
        for fila in filas:
            fh.write(json.dumps(fila, ensure_ascii=False) + '\n')

    obs_list = []
    for key in sorted(obs):
        o = obs[key]
        obs_list.append({
            'empresa': o['empresa'], 'archivo': o['archivo'], 'pagina_pdf': o['pagina_pdf'],
            'sha256': o['sha256'], 'documento': o['documento'], 'version': o['version'],
            'encabezados_leidos': sorted(o['encabezados'])[:6],
            'filas_leidas_ejemplo': o['filas'],
            'n_entradas': len(o['entradas']), 'entradas': o['entradas'],
            'estados_contextuales': dict(o['estados']),
            'nota': 'lectura de encabezados/filas sobre los bytes conservados; el registro antiguo no es su propia prueba',
        })
    with open(C.OUT / 'OBSERVACIONES.jsonl', 'w', encoding='utf-8') as fh:
        for o in obs_list:
            fh.write(json.dumps(o, ensure_ascii=False) + '\n')

    resumen = Counter(f['estado_contextual'] for f in filas)
    chk = Counter()
    for f in filas:
        for k, v in (f.get('checks') or {}).items():
            chk[(k, v[0] if isinstance(v, tuple) else v)] += 1
    print(json.dumps({'entradas': len(filas), 'estados_contextuales': dict(resumen),
                      'checks': {f'{k}:{v}': n for (k, v), n in sorted(chk.items())},
                      'observaciones_pagina': len(obs_list)}, ensure_ascii=False))


if __name__ == '__main__':
    main()
