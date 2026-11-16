"""Sonda 4: contrasta CONTRATO_C_PROPUESTA.md y MAPA_ENTRADAS.jsonl (52fb120) con lo que el producto
4.14 define para el motor C (solo lectura de fuentes; no se ejecuta LibreOffice ni el pipeline).
Uso: python3 -I sonda4_contrato_c_vs_motor.py <base414> <contrato.md> <mapa.jsonl>
"""
import json, re, sys
from fractions import Fraction as F

BASE, CON, MAPA = sys.argv[1:4]
rel = open(BASE + '/v6/scripts/relacion_entradas_materiales.py', encoding='utf-8').read()
bld = open(BASE + '/v6/scripts/V6.1/build_v6.py', encoding='utf-8').read()
tf = open(BASE + '/v6/scripts/V6.1/test_fill.py', encoding='utf-8').read()
con = open(CON, encoding='utf-8').read()
mapa = [json.loads(l) for l in open(MAPA, encoding='utf-8') if l.strip()]

print('== Producto: significado de Palancas 14/15/18 en el motor C ==')
for celda in ('14', '15', '16', '18'):
    m = re.search(r'id=f"(\w+)_\{esc\}", celda=f"Palancas!\{col\}%s".*?cond="([^"]*)".*?periodo="([^"]*)"' % celda, rel, re.S)
    print(f'  Palancas!X{celda}: id={m.group(1)!r} cond={m.group(2)!r} periodo={m.group(3)!r}' if m else f'  X{celda}: no hallado')
print('  build_v6.py fila 15 (R_MARG) en C:', re.search(r'"ROE objetivo \(se alcanza en el año 5\)"', bld) is not None)
print('  build_v6.py fila 18 (R_ROIC) en C:', re.search(r'"ROE a largo plazo \(tras el año 10\)"', bld) is not None)
print('  Historia fila 34:', re.search(r"\(34, '([^']*)'", bld).group(1))
print('  Historia fila 9 / 21:', re.search(r"\(9, '([^']*)', 'Cuenta", bld).group(1), '/', re.search(r"\(21, '([^']*)'", bld).group(1))
print('  test_fill: ROE0 = beneficio L9 / patrimonio L21 de cierre:', 'ROE0 = rows[2025][21], rows[2025][9] / rows[2025][21]' in tf.replace('B0, ROE0 = ', 'ROE0 = '))
print('  test_fill: flujo C = B(t-1)*ROE - (B(t)-B(t-1)):', 'flows.append(L[t - 1] * m - (L[t] - L[t - 1]))' in tf)
print('  test_fill: terminal C = B10*(ROE_lp - g_inf)/(r - g_inf):', 'f11 = L[10] * (roic - ginf)' in tf)
print('  g_inf en Analisis B68:D68 (no en Palancas B14):', "A['B68'] = 0.02" in tf)

print('== Contrato / mapa propuestos ==')
for pat in (r'g∞ del patrimonio \(B14\)', r'payout \(B15\)', r'BAI / patrimonio medio', r'BAI \+ OCI \+ dividendos',
            r'múltiplos', r'valor liquidativo'):
    print(f'  contrato contiene {pat!r}:', re.search(pat, con) is not None)
for r_ in mapa:
    if 'B14' in r_['entrada'] or 'ROE' in r_['entrada']:
        print('  mapa:', r_['entrada'])

print('== Contraejemplo minimo del puente de patrimonio propuesto ==')
E0, BN, impuesto, div, OCI, recompras, ampl = F(1000), F(100), F(30), F(40), F(0), F(0), F(0)
BAI = BN + impuesto
real = E0 + BN + OCI - div - recompras + ampl
propuesto = E0 + BAI + OCI + div - recompras + ampl
print(f'  E0=1000, beneficio neto=100, impuesto=30 (BAI=130), dividendos=40: E1 real={real}; '
      f'puente del contrato={propuesto}; diferencia que "otros movimientos" tendria que absorber={real - propuesto}')
roe_prod = BN / real
roe_con = BAI / ((E0 + real) / 2)
print(f'  ROE producto (L9/L21)={float(roe_prod):.6f}; ROE contrato (BAI/patrimonio medio)={float(roe_con):.6f}')

print('== Efecto de leer B15 como payout (replica de la formula del motor C de test_fill.py, valores ilustrativos) ==')
def valor_c(B0, ROE0, g1, roe_obj, ginf, roe_lp, r):
    L = [B0]; flows = []
    for t in range(1, 11):
        g = g1 if t <= 5 else g1 - (g1 - ginf) * (t - 5) / 5
        L.append(L[-1] * (1 + g))
        m = ROE0 + (roe_obj - ROE0) * min(t, 5) / 5
        flows.append(L[t - 1] * m - (L[t] - L[t - 1]))
    pv = sum(x / (1 + r) ** t for t, x in enumerate(flows, 1))
    tv = L[10] * (roe_lp - ginf) / (r - ginf) / (1 + r) ** 10
    return pv + tv
# parametros ilustrativos, NO propuestos para ningun caso: B0=100, ROE0=10 %, g1=3 %, g_inf=2 %, ROE_lp=10 %, r=9 %
v_ok = valor_c(100, 0.10, 0.03, 0.10, 0.02, 0.10, 0.09)
v_mal = valor_c(100, 0.10, 0.03, 0.40, 0.02, 0.10, 0.09)
print(f'  B15 = ROE objetivo 10 %: valor = {v_ok:.2f}; B15 rellenado con un payout de 40 % (se lee como ROE objetivo 40 %): valor = {v_mal:.2f} (x{v_mal / v_ok:.2f})')
