"""Extraccion independiente (Mistral C/F) de las altas PP&E y de intangibles de Vidrala desde los
textos conservados CF_20YY.txt (hash-verificados contra el ZIP base-4.14), sin usar regex/ventanas
del autor. Metodo: nota por titulo; slot de 'Additions' en la linea de cabecera del anio (split en
2+ espacios); fila total de Coste = primera fila puramente numerica despues de 'Work in progress'
(sin etiqueta: slot = hdr_idx - 1). Intangibles: fila 'Additions', total = ultimo token,
goodwill = penultimo, emission = tercer token ('-' = 0).
"""
import re, os

import sys; TXT = sys.argv[1]  # unica linea cambiada por el revisor: ruta como argumento

PPE_ESPERADO = {2017: 101154, 2018: 93148, 2019: 108645, 2020: 134263, 2021: 105877,
                2022: 158234, 2023: 134472, 2024: 171185, 2025: 177848}
INT_ESPERADO = {2017: (156743, 3237, 150657), 2018: (18623, 14645, 0), 2019: (25694, 22147, 0),
                2020: (28666, 26558, 0), 2021: (44810, 37359, 0), 2022: (93759, 90780, 0),
                2023: (100655, 93306, 0), 2024: (48326, 40135, 0), 2025: (45173, 37661, 0)}


def parts(ln):
    return [p for p in re.split(r'\s{2,}', ln.strip()) if p]


def lineas(y):
    return open(os.path.join(TXT, f'CF_{y}.txt'), encoding='utf-8').read().splitlines()


def ventana_nota(ls, patron, max_lin=160):
    for i, ln in enumerate(ls):
        if re.search(patron, ln, re.I):
            return ls[i:i + max_lin], i
    return None, None


def es_fila_numerica(ln):
    return bool(re.match(r'^\s*\(?[\d][\d,\.]*\)?(\s+\(?[\d\-,\.\(\)]+\)?)+\s*$', ln))


def a_num(tok):
    if tok is None or tok == '-':
        return 0.0
    neg = tok.startswith('(')
    v = float(tok.strip('()').replace(',', ''))
    return -v if neg else v


def extraer_ppe(anio, archivo):
    ls = lineas(archivo)
    win, ini = ventana_nota(ls, r'\d+\.\s*Property,\s*Plant\s*and\s*Equipment')
    assert win, f'nota PP&E no encontrada en CF_{archivo}'
    hdr_line = None
    for j, ln in enumerate(win):
        p = parts(ln)
        if p and p[0].startswith(str(anio)):
            hdr_line = j
            break
    assert hdr_line is not None, f'cabecera {anio} no encontrada en CF_{archivo}'
    # fila total de Coste: primera fila numerica despues de la linea 'Work in progress' de ese anio
    wip = next((j for j in range(hdr_line, len(win)) if 'Work in progress' in win[j]), None)
    assert wip is not None, f'Work in progress no encontrada (CF_{archivo} anio {anio})'
    total = next((ln for ln in win[wip + 1:] if es_fila_numerica(ln)), None)
    assert total, f'fila total no encontrada (CF_{archivo} anio {anio})'
    tp = parts(total)
    # en la fila total (sin etiqueta) el slot 1 es siempre la columna Additions
    return a_num(tp[1]), ini + 1


def extraer_intangibles(anio):
    ls = lineas(anio)
    win, ini = ventana_nota(ls, r'\d+\.\s*Intangible\s*Assets')
    assert win, f'nota Intangibles no encontrada en CF_{anio}'
    add = next(ln for ln in win if re.match(r'\s*Additions\b', ln, re.I))
    ap = parts(add)
    return a_num(ap[-1]), a_num(ap[2]), a_num(ap[-2]), ini + 1  # total, emission, goodwill


print('== PP&E Additions (nota PP&E, total Coste tras "Work in progress", columna Additions) ==')
ok = True
for y, esp in PPE_ESPERADO.items():
    got, ini = extraer_ppe(y, y)
    m = got == esp
    ok &= m
    print(f'  CF_{y}: extraido={got:.0f} esperado={esp} {"OK" if m else "MAL"} (nota desde l{ini})')
print('== Comparativos en el CF del ejercicio siguiente (misma columna del anio anterior) ==')
for y in range(2017, 2025):
    esp = PPE_ESPERADO[y]
    got, ini = extraer_ppe(y, y + 1)
    m = got == esp
    ok &= m
    print(f'  CF_{y+1} anio {y}: extraido={got:.0f} esperado={esp} {"OK" if m else "MAL"}')
print('== Intangibles Additions: total / emission allowances / goodwill ==')
for y, (et, ee, eg) in INT_ESPERADO.items():
    t, em, gw, ini = extraer_intangibles(y)
    m = (t == et and em == ee and gw == eg)
    ok &= m
    print(f'  CF_{y}: total={t:.0f} emission={em:.0f} goodwill={gw:.0f} esperado=({et},{ee},{eg}) {"OK" if m else "MAL"}')
print()
print('RESULTADO:', 'TODO COINCIDE' if ok else 'HAY DIFERENCIAS')
