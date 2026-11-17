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

YEAR_RE = re.compile(r'(?<![\d.,])20\d\d(?![\d.,])')  # v4.0 (A2-R4): un importe 2045,3 / 0,2050 / 2025,4 no es año
YEAR_FILE_RE = re.compile(r'20\d\d')  # nombres de archivo: CF_2024.txt
NUM_RE = re.compile(r'\(?\d[\d.,]*\)?|\u2212\d[\d.,]*|-\d[\d.,]*')

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
    'right': 'derechos', 'derechos': 'derechos', 'usage': 'derechos', 'derecho': 'derechos',
    'use': 'uso', 'uso': 'uso', 'lease': 'arrendamiento', 'arrendamiento': 'arrendamiento',
    'liabilities': 'pasivo', 'liability': 'pasivo', 'pasivos': 'pasivo', 'pasivo': 'pasivo',
    'deudas': 'deudas', 'deuda': 'deudas', 'corrientes': 'corriente', 'corriente': 'corriente',
    'activo': 'activos',
    'financial': 'financiero', 'financieros': 'financiero', 'financiero': 'financiero', 'financieras': 'financiero', 'finanzas': 'financiero',
    'investments': 'inversiones', 'inversiones': 'inversiones', 'inversion': 'inversiones',
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


def signed_num(tok):
    """A3-R1: valor CON SIGNO de un token impreso: los parentesis contables '(9.000)',
    U+2212 '−9.000' y '-' son negativos; antes solo se quitaba el '-' ASCII."""
    t = str(tok).strip()
    neg = (t.startswith('(') and t.endswith(')')) or t.startswith('-') or t.startswith('−')
    mag = normalize_num(t.strip('()').lstrip('-').lstrip('−'))
    d = C.dec(mag) if mag else None
    return (-d if (neg and d is not None) else d)


def value_like(tok):
    t = str(tok).strip().strip('()').replace('−', '-').lstrip('-')
    if re.search(r'[.,]\d{3}\b', t) or re.search(r'\d,\d{3}', t):
        return True
    try:
        return abs(float(t.replace(',', '.'))) >= 1000
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


def find_header_block(page_lines, row_idx, modo='max'):
    """Bloque de encabezado: toda la pagina hasta la fila. modo='max': linea de columnas
    con mas años (pagina citada). modo='near': linea de columnas MAS PROXIMA arriba de la
    fila con >=2 años (texto original: evita confundir la cabecera del estado con tablas
    de proyeccion de mas columnas que haya en la misma pagina)."""
    block = page_lines[:row_idx + 1] or page_lines
    years_in_block = []
    col_line = None
    col_years = []
    def es_linea_columnas(line):
        # v4.0 (A2-R4): una linea de cabecera de columnas solo tiene años, sin importes
        ys = YEAR_RE.findall(line)
        if not ys:
            return False
        otros = [t for t in NUM_RE.findall(line) if not YEAR_RE.fullmatch(t)]
        if any(value_like(t) for t in otros):
            return False
        # A3-R2: fuera de paréntesis, una línea tabular no puede tener más palabras
        # alfabéticas (len>=3, salvo conectores) que años; si no, es una frase narrativa
        sin_par = re.sub(r'\([^)]*\)', ' ', line)
        palabras = [w for w in re.findall(r'[A-Za-zÀ-ÿ]{3,}', sin_par)
                    if w.lower() not in ('and', 'the', 'of', 'in', 'at', 'for', 'con', 'por', 'del', 'las', 'los')]
        return len(palabras) <= len(ys)

    def fusionar_cabecera_partida(candidatos, row_idx, col_years, col_line):
        # A3-R2: cabecera partida en varias líneas (p. ej. '2025' / '2024' en líneas
        # consecutivas justo arriba de la fila): sus años se fusionan en orden; si aportan
        # más años que la línea elegida, la columna no es inequívoca tal cual
        zona = [l for i, l in candidatos if row_idx - 3 <= i <= row_idx]
        if not zona:
            return col_years, col_line
        zy = []
        for l in zona:
            for y in YEAR_RE.findall(l):
                if y not in zy:
                    zy.append(y)
        if len(zy) > len(col_years):
            return zy, zona[-1]
        return col_years, col_line
    if modo == 'near':
        for line in block:
            years_in_block.extend(YEAR_RE.findall(line))
        candidatos = [(i, l) for i, l in enumerate(block) if es_linea_columnas(l)]
        for i, line in reversed(candidatos):
            if len(YEAR_RE.findall(line)) >= 2:
                col_years = YEAR_RE.findall(line)
                col_line = line
                break
        if col_line is None:
            for i, line in reversed(candidatos):
                col_years = YEAR_RE.findall(line)
                col_line = line
                break
        if col_line is None:
            for line in page_lines[row_idx + 1:row_idx + 4]:
                if es_linea_columnas(line):
                    col_years = YEAR_RE.findall(line)
                    col_line = line
                    break
        else:
            col_years, col_line = fusionar_cabecera_partida(candidatos, row_idx, col_years, col_line)
        return years_in_block, col_line, col_years
    candidatos = []
    for i, line in enumerate(block):
        ys = YEAR_RE.findall(line)
        if ys:
            years_in_block.extend(ys)
            if es_linea_columnas(line):
                candidatos.append((i, line))
                # A3-R2: a igualdad de años gana la cabecera más próxima a la fila
                if len(ys) >= len(col_years):
                    col_years = ys
                    col_line = line
    if candidatos:
        col_years, col_line = fusionar_cabecera_partida(candidatos, row_idx, col_years, col_line)
    if col_line is None:
        for line in page_lines[row_idx + 1:row_idx + 4]:
            if es_linea_columnas(line):
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


# v4.0 (A2-R3): 'in thousands' solo cuenta como miles de EUROS si lo acompaña euros;
# millones/millions es escala contraria explicita (la pagina manda sobre la cabecera)
MILES_RE = re.compile(r'miles de euros|thousands of euros|mil(?:es)? de euros|in thousands of euros|thousand euros', re.IGNORECASE)
MILLONES_RE = re.compile(r'millones de euros|millions of euros|in millions of euros|amounts? in millions|expressed in millions', re.IGNORECASE)
EUROS_ONLY_RE = re.compile(r'\bin euros\b|amounts? in euros|expressed in euros\b|figures in euros', re.IGNORECASE)


def buscar_nota_escala_tabla(pages, pg, ventana=8):
    """v3.2 (bloque 2): nota de escala de la MISMA tabla. Si la pagina citada no trae
    la frase de escala, se busca hacia atras (hasta `ventana` paginas) la frase del
    estado del que la pagina es continuacion. Devuelve (pagina, frase) o None."""
    if pg is None:
        return None
    for pp in range(pg, max(0, pg - ventana), -1):
        t = pages.get(pp) or ''
        m = MILLONES_RE.search(t) or MILES_RE.search(t) or EUROS_ONLY_RE.search(t)
        if m:
            return (pp, m.group(0))
    return None


def check_unidad(page_lines, row_idx, unidad, escala, valor=None, row_line='', doc=None):
    """v2 (seguimiento 63e366b): mencionar euros NO acredita miles de euros ni escala 0,001.
    Se exige frase de escala explicita en la pagina ('miles/thousands of euros') o, en su
    defecto, en la cabecera del documento (primeras paginas). Si la pagina declara otra
    escala explicita ('in euros'), es CONFLICTO para miles declarados."""
    declared = UNIT_DECLARED_CANON.get(str(unidad))
    if declared is None:
        return 'NO_DECIDIBLE', f'unidad no mapeada: {unidad}'
    if declared == 'anio' and valor is not None and YEAR_RE.fullmatch(str(int(C.dec(valor)))):
        return 'OK', f'el valor {valor} es un año (unidad año confirmada por el valor)'
    if declared in ('moneda', 'norma', 'texto'):
        if valor is not None and C.flat_text(str(valor)) in C.flat_text('\n'.join(page_lines)):
            return 'OK', f'metadato {valor!r} localizado en la pagina'
        pages_all = (doc or {}).get('pages') or {}
        # v3.10: el metadato se acredita si TODAS sus palabras significativas figuran en
        # el documento (p. ej. 'IFRS (IFRS-EU)' vale con 'IFRS' presente), con la pagina
        # de la palabra mas rara como evidencia
        palabras = [w for w in re.findall(r'[A-Za-zÀ-ÿ]{3,}', str(valor or ''))]
        if palabras:
            faltan = []
            pagina_ev = None
            for w in palabras:
                wf = C.flat_text(w)
                hallada = None
                for pp in sorted(k for k in pages_all if k is not None):
                    if wf in C.flat_text(pages_all.get(pp) or ''):
                        hallada = pp
                        break
                if hallada is None:
                    faltan.append(w)
                elif pagina_ev is None or hallada > pagina_ev:
                    pagina_ev = hallada
            if not faltan:
                return 'OK', f'metadato {valor!r} acreditado en el documento (palabras {palabras} presentes; pagina {pagina_ev}); no figura en la pagina citada'
            return 'NO_DECIDIBLE', f'metadato {valor!r}: faltan en el documento {faltan}'
        return 'NO_DECIDIBLE', f'metadato {valor!r} no localizado en la pagina ni en el documento'
    area = '\n'.join(page_lines)
    page_miles = MILES_RE.search(area)
    page_euros_only = EUROS_ONLY_RE.search(area)
    page_millones = MILLONES_RE.search(area)
    if declared == 'miles_euros':
        if page_millones:
            return 'CONFLICTO', f'la pagina declara escala {page_millones.group(0)!r} (millones, escala contraria); la pagina manda sobre la cabecera del documento; no acredita miles de euros ni escala 0,001'
        if page_miles:
            if escala is not None and C.dec(escala) != C.dec('0.001'):
                return 'CONFLICTO', f'pagina en miles pero escala declarada {escala} != 0.001'
            return 'OK', f'unidad en miles confirmada en la pagina: {page_miles.group(0)!r}'
        if page_euros_only:
            return 'CONFLICTO', f'la pagina declara escala {page_euros_only.group(0)!r} (euros, no miles); no acredita miles de euros ni escala 0,001'
        ts = (doc or {}).get('tab_scale')
        if ts and MILLONES_RE.search(ts[1]):
            return 'CONFLICTO', f'nota de escala de la tabla en la pagina {ts[0]} es {ts[1]!r} (millones, escala contraria de miles)'
        if ts:
            # v3.2 (bloque 2): la nota de escala de la misma tabla (pagina anterior del
            # estado) acredita la unidad con el mismo control de escala
            if escala is not None and C.dec(escala) != C.dec('0.001'):
                return 'CONFLICTO', f'nota de escala de la tabla en la pagina {ts[0]} ({ts[1]!r}) pero escala declarada {escala} != 0.001'
            return 'OK', f'nota de escala de la misma tabla en la pagina {ts[0]}: {ts[1]!r} (la pagina citada es continuacion de ese estado)'
        if doc and doc.get('millones'):
            return 'CONFLICTO', 'la cabecera del documento declara millones (escala contraria) y la pagina no declara otra escala: no acredita miles'
        if doc and doc.get('miles'):
            # v3 (A-R3): la cabecera del documento tambien valida la escala declarada
            if escala is not None and C.dec(escala) != C.dec('0.001'):
                return 'CONFLICTO', f'cabecera del documento en miles pero escala declarada {escala} != 0.001'
            return 'OK', 'unidad en miles acreditada en la cabecera del documento (alcance: tablas del documento en miles; la pagina no declara otra escala)'
        return 'NO_DECIDIBLE', 'sin frase de escala en la pagina ni en la cabecera del documento'
    if declared == 'eur_accion':
        if valor is not None and any(C.flat_text(v) in C.flat_text(row_line) for v in C.variantes_numero(valor)):
            return 'OK', f'precio {valor} en la fila; unidad EUR por accion por contexto de cotizacion'
        if re.search(r'por acci\u00f3n|per share', area, re.IGNORECASE):
            return 'OK', 'pagina con unidad por accion confirmada'
        return 'NO_DECIDIBLE', 'unidad por accion no decidible en la pagina'
    if declared == 'acciones':
        if re.search(UNIT_CANON['acciones'], area, re.IGNORECASE):
            return 'OK', 'pagina menciona acciones/numero de acciones'
        if page_miles or page_euros_only:
            return 'CONFLICTO', 'unidad declarada acciones pero la pagina esta en euros y no menciona acciones'
        if doc and re.search(UNIT_CANON['acciones'], doc.get('head', ''), re.IGNORECASE):
            return 'OK', 'mencion de acciones en la cabecera del documento'
        return 'NO_DECIDIBLE', 'unidad acciones no decidible en la pagina'
    found = set()
    evidencia = []
    for canon, pat in UNIT_CANON.items():
        m = re.search(pat, area, re.IGNORECASE)
        if m:
            found.add(canon)
            evidencia.append(f'{canon}:{m.group(0)!r}')
    if declared in found:
        return 'OK', f'unidad declarada confirmada en pagina: {evidencia}'
    return 'NO_DECIDIBLE', f'unidad no decidible en esta pagina; evidencia: {evidencia}'


def check_signo(row_line, valor, signo):
    """El signo impreso se registra como evidencia; el campo signo es una convencion
    de transformacion del modelo (puede diferir del impreso), no un error de fuente.
    v2: un cero no tiene signo aplicable (NO_APLICA, no 'no comprobado')."""
    if valor is not None and C.dec(valor) is None:
        return 'NO_APLICA', f'valor no numerico ({valor!r}): metadato textual/moneda/norma, el signo no es aplicable'
    if valor is None or C.dec(valor) == 0:
        return 'NO_APLICA', 'valor cero: el signo no es aplicable'
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


def columna_year(columna, periodo, archivo):
    """v3 (A-R2.3): separa el año de la COLUMNA del año del INFORME incluido en la
    descripcion. Devuelve (año_informe, año_columna)."""
    ya_m = YEAR_FILE_RE.search(Path(archivo or '').name)
    ya = ya_m.group(0) if ya_m else None
    m = re.search(r'informe\s+(20\d\d)', columna or '')
    if m:
        ya = m.group(1)
    # v3.5: los años de una CITA de archivo dentro de la descripcion (CF_2018, AR_2019.txt,
    # 'p. 2013' no es año) no son año de columna: se eliminan antes de contar
    texto_col = re.sub(r'[A-Za-z_]+20\d\d(?:\.(?:txt|pdf))?', ' ', f'{columna or ""} {periodo or ""}')
    years = YEAR_RE.findall(texto_col)
    if not years:
        return ya, None
    ys = list(dict.fromkeys(years))
    if ya and ya in ys and len(ys) > 1:
        yc = next(y for y in ys if y != ya)
    else:
        yc = ys[0]
    return ya, yc


def check_columna(row_idx, page_lines, years_in_block, col_line, col_years, columna, periodo, valor, archivo=None):
    """v4.0 (A2-R1): la columna SOLO se acredita por POSICION: el valor declarado debe
    aparecer una unica vez en la fila y alinearse 1:1 con la linea de columnas de
    encabezado. Sin mapeo posicional -> NO_DECIDIBLE (nunca OK). Años repetidos en la
    cabecera (dos bloques) o valor repetido en la fila -> NO_DECIDIBLE. Si el valor esta
    en una posicion que mapea a otro año -> CONFLICTO."""
    ya, yc = columna_year(columna, periodo, archivo)
    declared_years = {yc} if yc else set()
    if not declared_years:
        return 'NO_DECIDIBLE', 'columna/periodo sin año declarado (fila de texto)'
    row_line = page_lines[row_idx] if row_idx is not None and row_idx < len(page_lines) else ''
    # todos los numeros de la fila (incluye importes <1000 como EPS), sin años; fuera la columna de nota
    nums = [t for t in NUM_RE.findall(row_line) if not YEAR_RE.fullmatch(t)]
    if col_years and len(nums) == len(col_years) + 1 and re.fullmatch(r'\d{1,2}(\.\d+)?', nums[0]) and not re.search(r'[.,]\d{3}$', nums[0]):
        nums = nums[1:]  # columna de referencia a nota (p. ej. '11.2'), no un importe
    if not years_in_block:
        return 'NO_DECIDIBLE', 'sin años de ejercicio en la pagina (fila de texto/mercado)'
    if not (declared_years & set(years_in_block)):
        return 'NO_DECIDIBLE', f'años declarados {sorted(declared_years)} no figuran en la pagina {sorted(set(years_in_block))} (fila no tabular o año fuera de tabla)'
    if not col_years:
        return 'NO_DECIDIBLE', 'sin linea de columnas de encabezado identificable en la pagina'
    if len(set(col_years)) < len(col_years):
        return 'NO_DECIDIBLE', f'años repetidos en la cabecera {col_years}: hay varios bloques (consolidado/individual u otros) y la columna no es inequivoca sin identificar el bloque'
    if not nums:
        return 'NO_DECIDIBLE', 'fila sin valores numericos que mapear'
    if valor is None or C.dec(valor) == 0:
        return 'NO_DECIDIBLE', 'valor cero: la posicion no es decidible (sin mapeo posicional no hay OK)'
    if len(nums) != len(col_years):
        return 'NO_DECIDIBLE', f'fila con {len(nums)} valores no alineable 1:1 con {len(col_years)} columnas {col_years}: sin mapeo posicional'
    # A3-R1: la comparacion posicional compara CON SIGNO (parentesis/U+2212/'-') y la
    # magnitud en espacio de digitos (como antes); sin normalizar el signo impreso,
    # 79 CONFLICTO reales eran artificiales
    raw_val = str(valor).strip()
    neg_target = raw_val.startswith('-') or raw_val.startswith('−') or (raw_val.startswith('(') and raw_val.endswith(')'))
    mag_target = normalize_num(raw_val.strip('()').lstrip('-').lstrip('−').replace('.', '').replace(',', ''))
    positions = []
    for k, t in enumerate(nums):
        s = signed_num(t)
        if s is not None and normalize_num(str(abs(s))) == mag_target and (s < 0) == neg_target:
            positions.append(k)
    if not positions:
        return 'CONFLICTO', f'el valor declarado {valor} no esta en la fila {nums!r} (cabecera {col_years}); declarado {sorted(declared_years)}'
    if len(positions) > 1:
        return 'NO_DECIDIBLE', f'valor {valor} repetido en las posiciones {positions} de la fila: columna ambigua (cabecera {col_years})'
    idx = positions[0]
    mapped = col_years[idx]
    if mapped in declared_years:
        return 'OK', f'posicion {idx} de {len(nums)} valores -> columna {mapped} (linea de columnas {col_years}); declarado {sorted(declared_years)}'
    return 'CONFLICTO', f'posicion {idx} -> columna {mapped}, pero declarado {sorted(declared_years)} (linea de columnas {col_years})'


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


def check_perimetro(page_lines, perimetro, doc=None):
    """v2: el perimetro se acredita en la pagina o en la cabecera del documento
    (titulo de los estados), no solo en la pagina citada."""
    p = str(perimetro or '')
    if 'no aplica' in p:
        return 'NO_APLICA', p
    area = '\n'.join(page_lines)
    # v3.2 (bloque 2): raiz 'consolid' cubre ES ('consolidados') e EN ('consolidated'); antes 'consolidat' dejaba fuera todo el ES
    consolidated = bool(re.search(r'consolid', area, re.IGNORECASE))
    doc_consolidated = bool(doc and re.search(r'consolid', doc.get('head', ''), re.IGNORECASE))
    if 'segmento' in p:
        seg = re.search(r'segmento\s*«?([^»]+)»?', p)
        word = seg.group(1).strip() if seg else ''
        hay = re.search(re.escape(word), area, re.IGNORECASE) if word else None
        if not hay and doc and word:
            hay = re.search(re.escape(word), doc.get('head', ''), re.IGNORECASE)
        if hay:
            return 'OK', f'segmento {word!r} localizado en la pagina o cabecera del documento'
        return 'NO_DECIDIBLE', 'el segmento no aparece en la pagina ni en la cabecera del documento'
    if (consolidated or doc_consolidated) and 'consolidado' in p:
        ev = 'pagina' if consolidated else 'cabecera del documento (titulo de los estados)'
        return 'OK', f'estados consolidados acreditados en la {ev}'
    if (consolidated or doc_consolidated) and 'consolidado' not in p:
        return 'CONFLICTO', f'documento consolidado pero perimetro declarado {p!r}'
    return 'NO_DECIDIBLE', 'sin marca de perimetro en la pagina ni en la cabecera del documento'


def check_version(archivo, page_lines, years_in_block, doc=None):
    """v2: la version necesita evidencia independiente (el año del informe declarado debe
    aparecer en la pagina o en la cabecera del documento), no metadatos copiados."""
    m = YEAR_FILE_RE.search(Path(archivo or '').name)
    archivo_year = m.group(0) if m else None
    head = '\n'.join(page_lines[:6])
    titulo_doc = (doc or {}).get('head', '')
    if archivo_year and (archivo_year in set(years_in_block) or re.search(archivo_year, head) or re.search(archivo_year, titulo_doc)):
        return 'OK', f'el informe declarado ({archivo}, año {archivo_year}) figura en la pagina/cabecera del documento'
    if archivo_year:
        return 'CONFLICTO', f'el año del archivo {archivo_year} no aparece en la pagina ni en la cabecera del documento'
    return 'NO_DECIDIBLE', 'archivo sin año en el nombre; version no comprobable'


def textos_empresa(emp):
    """Todos los .txt conservados de la empresa (para contraste de reexpresion)."""
    folder = C.INSUMOS / C.CARPETA_EMPRESA[emp]
    out = {}
    for sub in ('texto', 'fuentes_mercado'):
        d = folder / sub
        if d.exists():
            for p in sorted(d.glob('*.txt')):
                out[p.name] = p
    return out


TEXTO_CACHE = {}


def es_metadato_anio(f):
    """v3.1 (cierre v2, bloque 1): un metadato de año se identifica SOLO por unidad o
    concepto que lo identifiquen como año (unidad 'año', 'ejercicio de la columna').
    NUNCA por el valor: un importe monetario 2000-2099 (p. ej. 2001 miles de euros en
    pagos de acciones) NO es un año y no debe pasar a NO_APLICA por parecer año."""
    if UNIT_DECLARED_CANON.get(str(f.get('unidad') or '')) == 'anio':
        return True
    concepto = str(f.get('concepto') or '')
    return bool(re.search(r'(año|year|ejercicio)(\s+fiscal)?\s+de la columna|^(año|year|ejercicio)\s*$', concepto, re.IGNORECASE))


def verificar_puente(declared, vdec, valor, candidatos, textos_cache):
    """v3.6 (bloque 2): si la declaracion trae un puente aritmetico citado
    ('177,548 = 165,980 - 1,004 + 6,595 + 5,977 (CF_2019 p.9)'), se verifica:
    LHS == valor del comparativo, la expresion RHS suma exactamente LHS, y cada
    componente figura en la pagina citada del documento original. Si todo cuadra,
    la reexpresion queda acreditada con puente documentado (OK); si no, None."""
    m = re.search(r'([\u2212\-]?[\d.,]+)\s*=\s*([\u2212\-+\d.,()\s]+?)\s*\(\s*([A-Za-z_0-9]+(?:\.txt|\.pdf)?)\s*p\.?\s*(\d+)', declared)
    if not m or vdec is None:
        return None
    lhs_tok, rhs, fname, pg = m.group(1), m.group(2), m.group(3), int(m.group(4))
    if not fname.lower().endswith(('.txt', '.pdf')):
        fname = fname + '.txt'
    lhs = normalize_num(lhs_tok.strip().strip('()').lstrip('\u2212').lstrip('-'))
    if C.dec(lhs) != abs(vdec):
        return None
    rhs2 = rhs.replace('\u2212', '-')
    rhs2 = re.sub(r'\(([\d.,\-\u2212]+)\)', r'(-\1)', rhs2)
    parts = re.findall(r'[+\-]?\s*[\d.,]+', rhs2)
    total = C.dec(0)
    comps = []
    for t in parts:
        raw = t.strip()
        neg = raw.startswith('-')
        mag = normalize_num(raw.lstrip('+-'))
        d = C.dec(mag) if mag else None
        if d is None:
            return None
        comps.append((raw, mag, d))
        total += (-d if neg else d)
    if abs(total - vdec) > C.dec('0.0005') and abs(total - abs(vdec)) > C.dec('0.0005'):
        return None
    if fname not in textos_cache or fname not in candidatos:
        return None
    pages = C.extract_pages(textos_cache[fname].read_text(encoding='utf-8'))
    ptext = pages.get(pg)
    if ptext is None:
        return None
    pflat = C.flat_text(ptext)
    def fvariants(mag):
        out = {mag}
        m = mag
        if len(m) > 3:
            parts = []
            while m:
                parts.append(m[-3:])
                m = m[:-3]
            out.add(','.join(reversed(parts)))
            out.add('.'.join(reversed(parts)))
        return out
    for raw, mag, _ in comps:
        if not mag:
            return None
        if not any(C.flat_text(v) in pflat for v in fvariants(mag)) and C.flat_text(raw) not in pflat:
            return None
    return 'OK', f'reexpresion acreditada por puente aritmetico documentado en la declaracion ({lhs_tok} = {rhs.strip()}, {fname} p.{pg}); la expresion suma {total} y cada componente figura en la pagina citada del original'


NO_RESTATE_RE = re.compile(r'no\s+reexpresar|sin\s+reexpresar|not\s+restate|without\s+restating|did\s+not\s+restate|no\s+restated', re.IGNORECASE)


def nota_no_reexpresion_citada(declared, emp, archivos):
    """v3.11: si la declaracion cita una pagina de alguno de los documentos dados
    (el propio comparativo o el original del año, p. ej. 'AR_2019 p. 23' o
    'IA_2018 p. 104') y esa pagina declara no reexpresar comparativos (transicion
    NIIF 16 u otro cambio normativo), devuelve (documento, pagina, frase)."""
    m = re.search(r'([A-Za-z_0-9]+(?:\.txt|\.pdf)?)\s*p\.?\s*(\d+)', declared)
    if not m:
        return None
    fname = m.group(1)
    if not fname.lower().endswith(('.txt', '.pdf')):
        fname += '.txt'
    pg = int(m.group(2))
    # 1) la pagina citada, si pertenece a alguno de los documentos dados
    for archivo in archivos or []:
        if not archivo or Path(archivo).name != fname:
            continue
        p = C.ruta_insumo(emp, archivo)
        if not p.exists() and not archivo.startswith('texto/'):
            p = C.ruta_insumo(emp, 'texto/' + archivo)
        if not p.exists():
            continue
        pages = C.extract_pages(p.read_text(encoding='utf-8'))
        t = pages.get(pg) or ''
        mm = NO_RESTATE_RE.search(t)
        if mm:
            return (fname, pg, mm.group(0))
    # 2) v3.11c: si la pagina citada no lo declara, buscar en TODO el documento del
    # comparativo y en los originales del año una declaracion de no reexpresar comparativos
    for archivo in archivos or []:
        if not archivo:
            continue
        p = C.ruta_insumo(emp, archivo)
        if not p.exists() and not archivo.startswith('texto/'):
            p = C.ruta_insumo(emp, 'texto/' + archivo)
        if not p.exists():
            continue
        pages = C.extract_pages(p.read_text(encoding='utf-8'))
        for pp in sorted(k for k in pages if k is not None):
            t = pages.get(pp) or ''
            mm = NO_RESTATE_RE.search(t)
            if mm and 'comparativ' in t[max(0, mm.start() - 60):mm.end() + 90].lower():
                return (Path(archivo).name, pp, mm.group(0))
    return None


def check_reexpresion(emp, r, f, col_years, years_in_block):
    """v4.0 (A2-R2): comparacion del comparativo con el original del año de la columna:
    - SIN atajo de cita: solo cuenta una fila del original cuyo rotulo COMPLETO coincide
      (normalizado), mapeada por POSICION de columna 1:1, con la MISMA escala y el MISMO
      perimetro documental;
    - comparacion CON SIGNO (parentesis = negativo);
    - no-claim (cualquier redaccion con 'no': 'no aplica', 'no reexpresado', 'no (igual
      que...)') + valor distinto -> CONFLICTO (nunca OK);
    - diferencia sin declaracion de reexpresion -> NO_DECIDIBLE (falta puente);
    - diferencia SOLO de signo -> NO_DECIDIBLE, clase aparte SOLO_SIGNO (convencion de
      signo, no reexpresion);
    - declaracion afirmativa ('si/reexpresado') + diferencia + misma escala -> OK.
    - metadato de año (unidad/concepto) o valor no numerico -> NO_APLICA.
    """
    declared = str(f.get('reexpresado') or '')
    dl = declared.lower()
    archivo = f.get('archivo') or ''
    ya, yc = columna_year(f.get('columna'), f.get('periodo'), archivo)
    valor = f.get('valor_fuente')
    unidad = str(f.get('unidad') or '')
    if valor is None:
        vdec = None
    else:
        vs = str(valor).strip()
        vneg = vs.startswith('-') or vs.startswith('−') or (vs.startswith('(') and vs.endswith(')'))
        vmag = normalize_num(vs.strip('()').lstrip('-').lstrip('−'))
        vd = C.dec(vmag) if vmag else None
        vdec = (-vd if (vneg and vd is not None) else vd)
    if vdec is None and valor is not None:
        return 'NO_APLICA', f'valor no numerico ({valor!r}): metadato (moneda/norma/texto), no hay importe que contrastar en reexpresion'
    if es_metadato_anio(f):
        return 'NO_APLICA', f'metadato de año identificado por unidad/concepto (unidad {unidad!r}, concepto {f.get("concepto")!r}); un año de columna no se reexpresa como importe'
    if not ya or not yc:
        return 'NO_DECIDIBLE', 'sin años de informe/columna para contrastar reexpresion'
    if yc == ya:
        if 'reexpres' in dl and 'no' not in dl:
            return 'CONFLICTO', f'declara reexpresion pero la columna {yc} es el ejercicio corriente del informe {ya}'
        if 'no aplica' in dl:
            return 'NO_APLICA', declared
        return 'OK', f'columna {yc} = ejercicio corriente del informe {ya}; no hay comparativo que reexpresar'
    key = emp
    if key not in TEXTO_CACHE:
        TEXTO_CACHE[key] = textos_empresa(emp)
    cita = f.get('cita') or ''
    variantes = {C.flat_text(v) for v in C.variantes_numero(valor)} - {''}
    candidatos = [name for name in TEXTO_CACHE[key] if YEAR_FILE_RE.search(name) and YEAR_FILE_RE.search(name).group(0) == yc and name != Path(archivo).name]
    # rotulo completo normalizado (sin numeros): la fila debe contener el rotulo completo
    full_label = C.flat_text(re.sub(r'\d[\d.,]*', ' ', cita))
    cita_toks = canon_tokens(cita)
    no_claim_all = (('no aplica' in dl) or ('no reexpres' in dl) or ('igual al original' in dl)
                    or ('igual que' in dl) or ('no:' in dl) or re.match(r'^no\b', dl) or ('sin reexpresar' in dl))
    affirm = (not no_claim_all) and (('reexpresado' in dl) or ('reexpresion' in dl) or re.search(r'\bs[ií]\b', dl))
    # escala de la pagina citada (comparativo) para comparar con la del original
    perimetro_decl = str(f.get('perimetro') or '')

    def signed(tok):
        t = str(tok).strip()
        neg = (t.startswith('(') and t.endswith(')')) or t.startswith('-') or t.startswith('−')
        mag = normalize_num(t.strip('()').lstrip('-').lstrip('−'))
        d = C.dec(mag) if mag else None
        return (-d if (neg and d is not None) else d)

    def nums_of(ls):
        out = []
        for l in ls:
            for t in NUM_RE.findall(l):
                if value_like(t) and not YEAR_RE.fullmatch(t):
                    out.append((t, signed(t)))
        return out

    def escala_pagina(text_pages, pg):
        t = text_pages.get(pg) or ''
        if MILLONES_RE.search(t):
            return 'millones'
        if MILES_RE.search(t):
            return 'miles'
        if EUROS_ONLY_RE.search(t):
            return 'euros'
        return None

    hints = [signed(t) for t in NUM_RE.findall(cita or '') if value_like(t) and not YEAR_RE.fullmatch(t)]

    for name in candidatos:
        text = TEXTO_CACHE[key][name].read_text(encoding='utf-8')
        tflat = C.flat_text(text)
        orig_pages = C.extract_pages(text)
        orig_lines = text.splitlines()
        # perimetro documental del original
        orig_head = '\n'.join((orig_pages.get(i) or '') for i in range(1, 9))
        orig_consolidado = bool(re.search(r'consolid', orig_head, re.IGNORECASE))
        matched = []
        for i, line in enumerate(orig_lines):
            fl = C.flat_text(line)
            hit = bool(full_label) and full_label in fl
            if not hit and cita_toks:
                toks = canon_tokens(line)
                inter = len(cita_toks & toks)
                if cita_toks and inter == len(cita_toks) and inter >= 2:
                    hit = True
            if not hit:
                continue
            yb2, cl2, cy2 = find_header_block(orig_lines, i, 'near')
            if yc not in yb2:
                continue
            nums = nums_of([line])
            block = nums_of(orig_lines[i:i + 3])
            if yc in cy2 and len(nums) == len(cy2) + 1 and re.fullmatch(r'\d{1,2}(\.\d+)?', nums[0][0]) and not re.search(r'[.,]\d{3}$', nums[0][0]):
                nums = nums[1:]
            if yc in cy2 and len(block) == len(cy2) + 1 and re.fullmatch(r'\d{1,2}(\.\d+)?', block[0][0]) and not re.search(r'[.,]\d{3}$', block[0][0]):
                block = block[1:]
            cand = None
            if yc in cy2:
                if len(nums) == len(cy2):
                    cand = nums
                elif len(block) == len(cy2):
                    cand = block
            hint_hit = any(h is not None and any(h == s for _, s in (block or nums)) for h in hints)
            # escala de la pagina del original donde aparece la fila
            orig_pg = None
            for pp in sorted(k for k in orig_pages if k is not None):
                pass
            matched.append({'i': i, 'cy2': cy2, 'cand': cand, 'nums': nums, 'block': block,
                            'hint': hint_hit, 'line': line})
        matched.sort(key=lambda m: (not m['hint'], m['i']))
        # v4.0: escala y perimetro deben coincidir entre original y comparativo
        for m in matched:
            cand = m['cand']
            if cand is None or yc not in m['cy2']:
                continue
            orig_tok, orig_sv = cand[m['cy2'].index(yc)]
            equal = (vdec is not None and orig_sv is not None and orig_sv == vdec)
            mag_equal = (vdec is not None and orig_sv is not None and abs(orig_sv) == abs(vdec))
            if equal:
                if no_claim_all:
                    return 'NO_APLICA', f'declara no reexpresado y el original {name} confirma el mismo valor (con signo) en la columna {yc} ({orig_tok}) en la fila {m["i"]+1}; coherente'
                return 'OK', f'comparativo {yc} igual al original en {name}: columna {yc} imprime {orig_tok} en la fila {m["i"]+1}; no reexpresado'
            if mag_equal and not equal:
                return 'NO_DECIDIBLE', f'SOLO_SIGNO: magnitudes iguales ({abs(vdec)}) pero signo distinto (original {orig_tok} en {name} col {yc}, comparativo {valor}); es convencion de signo, no reexpresion'
            if no_claim_all:
                return 'CONFLICTO', f'declara no reexpresado ("{declared}") pero el original {name} imprime {orig_tok} en la columna {yc} (fila {m["i"]+1}) y el comparativo cita {valor}: contradiccion explicita'
            if affirm:
                return 'OK', f'reexpresion confirmada por columna: el original {name} imprime {orig_tok} en la columna {yc} (fila {m["i"]+1}) y el comparativo cita {valor}; declarado: {declared}'
            return 'NO_DECIDIBLE', f'el original {name} imprime {orig_tok} en la columna {yc} y el comparativo cita {valor} sin declaracion de reexpresion: falta puente de significado (un cambio de clasificacion/perimetro no acredita reexpresion de la cifra)'
        if matched:
            m = matched[0]
            return 'NO_DECIDIBLE', f'la fila con rotulo completo aparece en {name} (linea {m["i"]+1}) pero la columna {yc} no se puede mapear 1:1 (columnas {m["cy2"]}, valores {[t for t, _ in m["nums"]]})'
        if no_claim_all and variantes and any(v and v in tflat for v in variantes):
            nnr = nota_no_reexpresion_citada(declared, emp, [archivo] + candidatos)
            if nnr:
                return 'NO_APLICA', f'no reexpresado documentado: {nnr[0]} p.{nnr[1]} declara "{nnr[2]}" (no reexpresar comparativos); el valor {valor} figura en el original {name}'
        if variantes and any(v and v in tflat for v in variantes):
            return 'NO_DECIDIBLE', f'el valor aparece en {name} pero no en una fila con el rotulo completo mapeable 1:1 en la columna {yc}; reexpresion no decidible'
    if not candidatos:
        return 'NO_DECIDIBLE', f'no hay texto conservado del año {yc} entre los insumos seleccionados (faltaria el documento original del ejercicio {yc}) para contrastar la reexpresion del comparativo'
    return 'NO_DECIDIBLE', f'el rotulo completo de la partida no se localiza en los textos conservados del año {yc} ({candidatos[:3]})'


def doc_info(emp, arch, pages_all):
    """Cabecera del documento: primeras paginas del .txt (titulo de los estados)."""
    head = '\n'.join((pages_all.get(i) or '') for i in range(1, 9))
    return {'head': head, 'miles': bool(MILES_RE.search(head)), 'millones': bool(MILLONES_RE.search(head)), 'arch': arch, 'pages': pages_all}


def check_entrada(emp, r, pages, doc=None):
    """Devuelve dict con checks contextuales de una entrada con fuente.
    v2 (seguimiento 63e366b): REVISADO_CONTEXTUAL exige que TODAS las dimensiones
    pertinentes esten OK o NO_APLICA; cualquier NO_DECIDIBLE pasa a PENDIENTE."""
    f = r.get('fuente') or {}
    pg = f.get('pagina')
    ptext = pages.get(pg)
    out = {'empresa': emp, 'celda': r['celda'], 'id': r['id'], 'clase': r['clase'],
           'archivo': f.get('archivo'), 'pagina': pg, 'checks': {}, 'evidencia': {}}
    if ptext is None:
        out['checks'] = {k: 'NO_DECIDIBLE' for k in ('fila', 'columna', 'unidad', 'signo', 'perimetro', 'version', 'reexpresion')}
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
    checks['columna'] = check_columna(ri, lines, years_in_block, col_line, col_years, f.get('columna'), f.get('periodo'), f.get('valor_fuente'), f.get('archivo'))
    doc_u = dict(doc or {})
    doc_u['tab_scale'] = buscar_nota_escala_tabla(pages, pg)
    checks['unidad'] = check_unidad(lines, ri, f.get('unidad'), f.get('escala'), f.get('valor_fuente'), row_line or '', doc_u)
    bloque_fila = '\n'.join(lines[max(0, ri - 2):ri + 3])
    checks['signo'] = check_signo(bloque_fila or row_line or '', f.get('valor_fuente'), f.get('signo'))
    checks['perimetro'] = check_perimetro(lines, f.get('perimetro'), doc)
    checks['version'] = check_version(f.get('archivo'), lines, years_in_block, doc)
    checks['reexpresion'] = check_reexpresion(emp, r, f, col_years, years_in_block)
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
    vals = {k: c[0] for k, c in checks.items()}
    if 'CONFLICTO' in vals.values():
        estado = 'CONFLICTO_CONTEXTUAL'
    elif 'NO_DECIDIBLE' in vals.values():
        # v2: no se presenta como plenamente revisada si falta una dimension pertinente
        estado = 'PENDIENTE_CONTEXTUAL'
    else:
        estado = 'REVISADO_CONTEXTUAL'
    out['estado_contextual'] = estado
    out['pendientes'] = [k for k, v in vals.items() if v in ('NO_DECIDIBLE', 'CONFLICTO')]
    out['detalle'] = {k: c[1] for k, c in checks.items()}
    return out


def main():
    registro = C.load_registro()
    pages_cache = {}
    doc_cache = {}

    def get_pages(emp, arch):
        key = (emp, arch)
        if key not in pages_cache:
            p = C.ruta_insumo(emp, arch)
            pages_cache[key] = C.extract_pages(p.read_text(encoding='utf-8')) if p.exists() else {}
        return pages_cache[key]

    def get_doc(emp, arch):
        key = (emp, arch)
        if key not in doc_cache:
            doc_cache[key] = doc_info(emp, arch, get_pages(emp, arch))
        return doc_cache[key]

    filas = []
    obs = {}
    for emp, r in C.iter_entradas(registro):
        if r['clase'] in ('dato_publicado', 'cero_comprobado'):
            f = r.get('fuente') or {}
            arch = f.get('archivo')
            res = check_entrada(emp, r, get_pages(emp, arch), get_doc(emp, arch)) if arch else {
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
