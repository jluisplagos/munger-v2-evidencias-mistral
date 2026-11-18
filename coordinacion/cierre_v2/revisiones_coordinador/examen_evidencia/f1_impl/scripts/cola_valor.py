#!/usr/bin/env python3
"""Réplica independiente (revisor) de la cola de valoración del motor A del libro V6.3 (descuento, terminal, caja, acciones, quiebra) a partir
de los flujos; contraste con Análisis B71:D78 en A0 y, como DIAGNÓSTICO (no es una valoración), los valores con los flujos A1 y A2 y las
palancas actuales (que no están ancladas en esos perímetros: V-F1g). Uso: cola_valor.py LIBRO resultado_F1.json"""
import json, sys
from fractions import Fraction as F
import openpyxl
libro, pres = sys.argv[1:3]
wb = openpyxl.load_workbook(libro, data_only=True)
A, P, Mo = wb["Análisis"], wb["Palancas"], wb["Motor"]
q = lambda x: F(repr(x)) if isinstance(x, float) else F(x)
r = q(A["C56"].value); acc = q(A["C55"].value); caja = q(A["C76"].value or 0); pq = q(P["C22"].value or 0); rec = q(P["C23"].value or 0)
res = json.load(open(pres, encoding="utf-8"))
def valor(fl, f11, g):
    vp = sum((q(x) / (1 + r) ** (t + 1) for t, x in enumerate(fl)), F(0))
    vt = q(f11) / (r - g) / (1 + r) ** 10
    tot = vp + vt + caja
    return vp, vt, tot, ((1 - pq) * tot + pq * rec) / acc
print(f"r {float(r)} · acciones {float(acc)} · exceso de caja {float(caja)} · p quiebra {float(pq)}")
for per in ("A0_total", "A1_sin_ROU", "A2_propio"):
    d = res["diagnostico_por_perimetro"][per]
    out = []
    for esc, col in (("MALO", "B"), ("NORMAL", "C"), ("BUENO", "D")):
        g = q(A[f"{col}68"].value)
        vp, vt, tot, pa = valor(d["escenarios"][esc]["anios_1_10"], d["escenarios"][esc]["anio_11"], g)
        out.append((esc, float(vp), float(vt), float(tot), float(pa)))
        if per == "A0_total":
            dif = max(abs(float(vp) - A[f"{col}72"].value), abs(float(vt) - A[f"{col}73"].value), abs(float(tot) - A[f"{col}77"].value), abs(float(pa) - A[f"{col}78"].value))
            print(f"  A0 {esc}: réplica VP {float(vp):.6f} VT {float(vt):.6f} total {float(tot):.6f} por acción {float(pa):.6f} · libro {A[f'{col}72'].value:.6f} {A[f'{col}73'].value:.6f} {A[f'{col}77'].value:.6f} {A[f'{col}78'].value:.6f} · dif máx {dif:.2e}")
    probs = [q(A[f"{c}69"].value) for c in "BCD"]
    pond = sum(p * F(repr(o[4])) for p, o in zip(probs, out))
    print(f"{per}: valor por acción MALO/NORMAL/BUENO = " + " / ".join(f"{o[4]:.2f}" for o in out) + f" · ponderado {float(pond):.2f}")
print("precio actual (Análisis C37?):", A["C37"].value, "· C43 (ponderado libro):", A["C43"].value)
