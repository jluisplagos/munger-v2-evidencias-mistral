#!/usr/bin/env python3
"""Reproducción INDEPENDIENTE (revisor) de las cifras F1 de Elis, desde el libro d2593777 y el CSV verificado del frente E.
No importa motor_a_f1.py ni ningún script del autor. Uso: repro_independiente.py LIBRO CSV VERIFICACION_JSON"""
import csv, hashlib, json, sys
from fractions import Fraction as F
import openpyxl

libro, pcsv, pver = sys.argv[1:4]
print("libro sha256:", hashlib.sha256(open(libro, "rb").read()).hexdigest())
ver = json.load(open(pver, encoding="utf-8"))
assert ver["huellas"]["datos"] == hashlib.sha256(open(pcsv, "rb").read()).hexdigest(), "la verificación no es de este CSV"
estado = {c["id"]: c["estado"] for c in ver["cifras"]}
filas = {r["id"]: r for r in csv.DictReader(open(pcsv, encoding="utf-8"), delimiter=";")}

def cifra(i):
    r = filas[i]
    assert estado[i] == "OK" and r["edicion"] == "vigente", (i, estado[i], r["edicion"])
    return F(r["valor_publicado"])

wb = openpyxl.load_workbook(libro, data_only=True)
H, A, P, M, D = wb["Historia"], wb["Análisis"], wb["Palancas"], wb["Motor"], wb["Diagnóstico V6"]
def q(x):
    return F(repr(x)) if isinstance(x, float) else F(x)
cols = "CDEFGHIJKL"
anios = [int(H[f"{c}5"].value) for c in cols]
def fila(n):
    return {y: q(H[f"{c}{n}"].value) for y, c in zip(anios, cols)}
V, EBIT, DA, TAU, CAPEX, ADQ, DWC = (fila(n) for n in (6, 7, 8, 10, 12, 13, 14))
n = int(H["C57"].value); w = anios[-n:]; h5 = anios[-5:]
C70, C58, C52, C53, V0 = (q(H[c].value) for c in ("C70", "C58", "C52", "C53", "C44"))
print("ventana", w, "C70", float(C70), "C58", float(C58), "C52", float(C52), "C53", float(C53), "V0", float(V0))
print("Análisis C46..C52:", [A[f"C{i}"].value for i in range(46, 53)])
ROU = {2021: cifra("DA_ROU_U22_2021"), 2022: cifra("DA_ROU_U23_2022"), 2023: cifra("DA_ROU_FR_2023"), 2024: cifra("DA_ROU_2024"), 2025: cifra("DA_ROU_2025")}
PPA = {2021: cifra("DA_PPA_U22_2021"), 2022: cifra("DA_PPA_U23_2022"), 2023: cifra("DA_PPA_FR_2023"), 2024: cifra("DA_PPA_2024"), 2025: cifra("DA_PPA_2025")}
PAG = {2023: cifra("CF_LEASE_FR_2023"), 2024: cifra("CF_LEASE_2024"), 2025: cifra("CF_LEASE_2025")}
BAI = {2021: cifra("IS_BAI_U22_2021"), 2022: cifra("IS_BAI_U23_2022"), 2023: cifra("IS_BAI_FR_2023"), 2024: cifra("IS_BAI_2024"), 2025: cifra("IS_BAI_2025")}
IMP = {2021: cifra("IS_IMP_U22_2021"), 2022: cifra("IS_IMP_U23_2022"), 2023: cifra("IS_IMP_FR_2023"), 2024: cifra("IS_IMP_2024"), 2025: cifra("IS_IMP_2025")}
EARN = {2021: cifra("OOIE_EARN_U22_2021"), 2022: cifra("OOIE_EARN_U23_2022"), 2023: cifra("OOIE_EARN_FR_2023"), 2024: cifra("OOIE_EARN_2024"), 2025: cifra("OOIE_EARN_2025")}
ACT = {2023: cifra("FIN_ACTMEX_FR_2023"), 2024: cifra("FIN_ACTMEX_2024"), 2025: cifra("FIN_ACTMEX_2025")}
rou = {y: -v for y, v in ROU.items()}; ppa = {y: -v for y, v in PPA.items()}; pag = {y: -v for y, v in PAG.items()}
imp = {y: -v for y, v in IMP.items()}
mean = lambda xs: sum(xs, F(0)) / len(list(xs)) if not isinstance(xs, list) else sum(xs, F(0)) / len(xs)
def med(d, ys): return sum((d[y] for y in ys), F(0)) / len(ys)
S = med(V, w)
def calib(dx, ebit=None, tau=None):
    ebit = ebit or EBIT; tau = tau or TAU
    nopat = sum((ebit[y] * (1 - tau[y]) for y in w), F(0)) / n
    reinv = sum((CAPEX[y] - dx[y] + DWC[y] for y in w), F(0)) / n
    f = (nopat - reinv - C70) / S
    tau5 = med(tau, h5)
    m0 = ebit[anios[-1]] / V0
    F0 = V0 * (m0 * (1 - tau5) - f)
    return dict(f=f, nopat=nopat, reinv=reinv, tau5=tau5, m0=m0, F0=F0)
dxA0 = {y: DA[y] for y in anios}
dxA1 = {y: DA[y] - rou[y] for y in h5}
dxA2 = {y: DA[y] - rou[y] - ppa[y] for y in h5}
dxB = {y: CAPEX[y] for y in anios}
R = {k: calib(d) for k, d in (("A0", dxA0), ("A1", dxA1), ("A2", dxA2), ("B", dxB))}
for k, r in R.items():
    print(f"{k}: f={float(r['f']):.15f} F0={float(r['F0']):.9f} nopat={float(r['nopat']):.6f} reinv={float(r['reinv']):.6f}")
print("réplica f A0 − C58:", float(R["A0"]["f"] - C58), "· τ5 − C52:", float(R["A0"]["tau5"] - C52))
print("A1 − A0 =", f"{float(R['A1']['F0'] - R['A0']['F0']):+.6f}", " (= V0·ROU media ÷ S =", f"{float(V0 * med(rou, w) / S):.6f})")
print("A2 − A1 =", f"{float(R['A2']['F0'] - R['A1']['F0']):+.6f}", " (PPA media a escala 2025)")
# ancla S2C
def ancla(dx):
    den = sum((CAPEX[y] - dx[y] + DWC[y] + ADQ[y] for y in h5), F(0))
    return (V[anios[-1]] - V[anios[-6]]) / den
print("anclas S2C: A0", float(ancla(dxA0)), "A1", float(ancla(dxA1)), "A2", float(ancla(dxA2)), "B", float(ancla(dxB)))
# (1b)
w_m = med(pag, w) / S; w_L = pag[2025] / V0
sp = -V0 * (w_L - w_m)
sr = rou[2025] - med(rou, w) / S * V0
print(f"(1b) pagos media {float(100*w_m):.4f}% · 2025 {float(100*w_L):.4f}% · sens. pagos {float(sp):+.3f} · ROU {float(sr):+.3f} · total {float(sp+sr):+.3f}")
print(f"     pesos pagos por año: " + " ".join(f"{y}:{float(100*pag[y]/V[y]):.2f}%" for y in w))
# escala PPA / ROU
print(f"escala PPA (A2): {float(med(ppa, w)/S*V0 - ppa[2025]):+.3f} · proporciones f {float(100*med(ppa,w)/S):.4f}% m0 {float(100*ppa[2025]/V0):.4f}% · PPA media a escala 2025 {float(med(ppa,w)/S*V0):.3f}")
print(f"escala ROU (A1,A2): {float(med(rou, w)/S*V0 - rou[2025]):+.3f} · proporciones f {float(100*med(rou,w)/S):.4f}% m0 {float(100*rou[2025]/V0):.4f}%")
print(f"las dos en A2: {float(med(ppa, w)/S*V0 - ppa[2025] + med(rou, w)/S*V0 - rou[2025]):+.3f}")
# motor
def motor(V0, m0, tau, f, g15, m_obj, s2c, g_inf, roic):
    Vp = V0; fl = []; Vs = []
    for t in range(1, 11):
        g = g15 if t <= 5 else g15 - (g15 - g_inf) * F(t - 5, 5)
        Vt = Vp * (1 + g); mt = m0 + (m_obj - m0) * F(min(t, 5), 5)
        fl.append(Vt * (mt * (1 - tau) - f) - (Vt - Vp) / s2c); Vs.append(Vt); Vp = Vt
    t11 = Vs[-1] * (1 + g_inf) * (m_obj * (1 - tau) * (1 - g_inf / roic) - f)
    return fl, t11
pal = {}
for esc, c in (("MALO", "B"), ("NORMAL", "C"), ("BUENO", "D")):
    pal[esc] = dict(g15=q(P[f"{c}14"].value), m_obj=q(P[f"{c}15"].value), s2c=q(P[f"{c}16"].value), roic=q(P[f"{c}18"].value), g_inf=q(A[f"{c}68"].value))
# réplica de los flujos del libro (Motor AU:BD, BF, filas 6-8)
mx = F(0)
for (esc, fila_) in (("MALO", 6), ("NORMAL", 7), ("BUENO", 8)):
    fl, t11 = motor(V0, R["A0"]["m0"], R["A0"]["tau5"], R["A0"]["f"], **pal[esc])
    for t, c in enumerate(["AU", "AV", "AW", "AX", "AY", "AZ", "BA", "BB", "BC", "BD"]):
        mx = max(mx, abs(fl[t] - q(M[f"{c}{fila_}"].value)))
    mx = max(mx, abs(t11 - q(M[f"BF{fila_}"].value)))
print("réplica independiente de los 33 flujos del Motor (A0): desviación máxima", float(mx))
# T16 · N1 solo en la ventana
def n1(con_fuera=False, con_act=False, perim=dxA0):
    ebit = dict(EBIT); tau = dict(TAU)
    for y in h5:
        en_v = y in w
        if not (en_v or con_fuera):
            continue
        aj = EARN[y]
        dB = ACT.get(y, F(0)) if con_act else F(0)   # la actualización es un gasto financiero (positivo publicado): fuera del BAI → BAI sube
        if en_v:
            ebit[y] = EBIT[y] - aj
        t = imp[y] / (BAI[y] - aj + dB)
        tau[y] = F(round(t, 4)).limit_denominator(10**4)
    return calib(perim, ebit, tau), tau, ebit
r16, tau16, ebit16 = n1()
print("T16 τ ventana:", {y: float(tau16[y]) for y in w}, "τ5", float(r16["tau5"]), "m0", f"{float(r16['m0']):.6f}", "f", f"{float(r16['f']):.9f}", "F0", f"{float(r16['F0']):.3f}",
      "ΔF0", f"{float(r16['F0'] - R['A0']['F0']):+.3f}")
_, t11_n = motor(V0, r16["m0"], r16["tau5"], r16["f"], **pal["NORMAL"]); _, t11_0 = motor(V0, R["A0"]["m0"], R["A0"]["tau5"], R["A0"]["f"], **pal["NORMAL"])
print("T16 Δ año 11 NORMAL:", f"{float(t11_n - t11_0):+.3f}")
for nombre, kw in (("también 2021–22", dict(con_fuera=True)), ("con actualización", dict(con_act=True)), ("las dos", dict(con_fuera=True, con_act=True))):
    rr, _, _ = n1(**kw)
    _, t11_v = motor(V0, rr["m0"], rr["tau5"], rr["f"], **pal["NORMAL"])
    print(f"  variante {nombre}: ΔF0 {float(rr['F0'] - R['A0']['F0']):+.3f} · Δ año 11 NORMAL {float(t11_v - t11_0):+.3f}")
for nombre, dx in (("A1", dxA1), ("A2", dxA2)):
    rr, _, _ = n1(perim=dx)
    print(f"  N1 en {nombre}: ΔF0 {float(rr['F0'] - R[nombre]['F0']):+.3f}")
# τ de la ventana (convención alternativa, solo informativo)
# K3 A0: puente
r0 = R["A0"]; Eb = med(EBIT, w)
l1 = C70
l2 = (EBIT[2025] - Eb) * (1 - r0["tau5"])
l3 = Eb * (1 - r0["tau5"]) - r0["nopat"]
l4 = -r0["f"] * (V0 - S)
da_own = {y: DA[y] - rou[y] - ppa[y] for y in w}
l5 = sum((CAPEX[y] - da_own[y] + DWC[y] for y in w), F(0)) / n
l6 = -med(rou, w); l7 = -med(ppa, w)
print("K3 A0:", " ".join(f"{float(x):+.3f}" for x in (l1, l2, l3, l4, l5, l6, l7)), "= suma", f"{float(l1+l2+l3+l4+l5+l6+l7):.6f}", "· F0", f"{float(r0['F0']):.6f}",
      "· residuo", float(l1+l2+l3+l4+l5+l6+l7 - r0["F0"]))
print("K3 doble cómputo a escala 2025:", f"{float(med(rou, w) * V0 / S):.6f}", "· PPA", f"{float(med(ppa, w) * V0 / S):.6f}")
# valores por acción del libro (para el contexto del F1-LIBRO)
print("Análisis B78:D78 (valor por acción A0 del libro):", [A[f"{c}78"].value for c in "BCD"], "· C43", A["C43"].value, "· precio (Análisis C?)")
