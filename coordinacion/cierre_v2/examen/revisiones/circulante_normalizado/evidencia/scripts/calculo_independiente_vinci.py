"""Revisor: f, flujo sin crecimiento y ancla de S2C de VINCI (A2_propio) en fracciones, leyendo solo valores de la Historia del libro de datos
recalculado del expediente (sin motor_a_f1). Ventana 2023–2025 (C57 = 3); τ de proyección = media de 2021–2025; m0 = Historia C48 (EBIT ÷ ventas
de 2025); D_X = fila 88 (D&A − ROU − PPA); ancla = (V_2025 − V_2020) ÷ Σ_2021–2025 (capex − D_X + circulante + adquisiciones).
Uso: calculo_independiente_vinci.py LIBRO_DATOS_RECALCULADO.xlsx"""
import sys
from fractions import Fraction as Fr
import openpyxl
ws = openpyxl.load_workbook(sys.argv[1], data_only=True, read_only=True)["Historia"]
A = list(range(2016, 2026)); COL = dict(zip(A, "CDEFGHIJKL"))
def fila(r): return {y: Fr(str(ws[f"{COL[y]}{r}"].value)) for y in A if ws[f"{COL[y]}{r}"].value is not None}
V, EBIT, TAU, CAPEX, ADQ, WC, DX = fila(6), fila(7), fila(10), fila(12), fila(13), fila(14), fila(88)
C70 = Fr(str(ws["C70"].value)); C48 = Fr(str(ws["C48"].value)); n = int(ws["C57"].value)
ventana = A[-n:]; horiz = A[-5:]
def media(xs): xs = list(xs); return sum(xs, Fr(0)) / len(xs)
def calc(wc):
    S = media(V[y] for y in ventana); nopat = media(EBIT[y] * (1 - TAU[y]) for y in ventana)
    reinv = media(CAPEX[y] - DX[y] + wc[y] for y in ventana); f = (nopat - reinv - C70) / S
    tau5 = media(TAU[y] for y in horiz); F0 = V[A[-1]] * (C48 * (1 - tau5) - f)
    den = sum(CAPEX[y] - DX[y] + wc[y] + ADQ.get(y, Fr(0)) for y in horiz); anc = (V[A[-1]] - V[A[-6]]) / den
    return reinv, f, F0, anc, den
print(f"libro {sys.argv[1]}\nC57 {n} · ventana {ventana} · C70 {float(C70)} · C48 {float(C48)} · fila 14 {[int(WC[y]) for y in A]}")
for et, wc in (("fila 14 tal cual (estado actual)", WC), ("circulante a cero en 2021–2025 (V-CIRC a)", {y: (Fr(0) if y >= 2021 else WC[y]) for y in A})):
    r, f, F0, anc, den = calc(wc)
    print(f"{et}: reinversión media {float(r):.3f} · f {float(f) * 100:.4f} % · flujo sin crecimiento {float(F0):.3f} · ancla {float(anc):.4f} (Σ denominador 2021–2025 {float(den):.1f})")
print("libro: C58", ws["C58"].value, "· C53", ws["C53"].value, "· C76", ws["C76"].value)
