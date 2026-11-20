#!/usr/bin/env python3
"""Comprobación SIN LibreOffice (motor A o B de un libro V6.3): con los flujos del libro evaluado oficial (que no dependen de la tasa),
valor por acción = [Σ F_t/(1+r)^t + F_11/((r−g)(1+r)^10) + ajuste]·(1−q) + q·rec) / acciones, con r = C56 (motor A) o la r operativa
(motor B: (C56·E + kd·(1−t)·D)/(E+D)). Compara con hoja_resumen.json."""
import json, sys, glob, openpyxl
sys.path.insert(0, '/tmp/claude-0/revision_hoja/herr')
from indep import p_estrella_biseccion, zona
exp = sys.argv[1]
libro = glob.glob(exp + '/*_v63_evaluada.xlsx')[0]
wb = openpyxl.load_workbook(libro, data_only=True)
A, D, M, H = wb['Análisis'], wb['Diagnóstico V6'], wb['Motor'], wb['Historia']
motor = D['C5'].value
t = json.load(open(exp + '/hoja_resumen.json', encoding='utf-8'))
p = [A['B69'].value, A['C69'].value, A['D69'].value]
precio = A['C37'].value
mx = 0.0
for fila in t['sensibilidad']['filas']:
    r = fila['r']
    if motor == 'B':
        E, Dd, kd, tt = A['C41'].value, H['C64'].value, H['C63'].value, D['C11'].value
        rr = (r * E + kd * (1 - tt) * Dd) / (E + Dd)
    else:
        rr = r
    V = []
    for f in (6, 7, 8):
        fl = [M.cell(f, c).value for c in range(47, 57)]
        f11, g, aj, q, rec, acc = M.cell(f, 58).value, M.cell(f, 8).value, M.cell(f, 13).value, M.cell(f, 14).value, M.cell(f, 15).value, M.cell(f, 16).value
        tot = sum(x / (1 + rr) ** (i + 1) for i, x in enumerate(fl)) + f11 / (rr - g) / (1 + rr) ** 10 + aj
        V.append(((1 - q) * tot + q * rec) / acc)
    P = p_estrella_biseccion(V, p, t['sensibilidad']['k'])
    psi = min(P, V[1]); pond = sum(v * w for v, w in zip(V, p))
    d = max(abs(a - b) / abs(b) for a, b in zip(V + [psi, pond], fila['V'] + [fila['precio_si'], fila['ponderado']]))
    mx = max(mx, d)
    print(f"  r={r:.2f} (descuento {rr:.5f}) V puro={[round(x,4) for x in V]} psi puro={psi:.6f} hoja={fila['precio_si']:.6f} zona puro={zona(precio,V[0],psi,pond)} hoja={fila['zona']} dif rel máx={d:.2e}")
print(f"{exp.split('/')[-1]}: motor {motor} · diferencia relativa máxima {mx:.2e}")
