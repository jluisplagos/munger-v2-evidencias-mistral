"""Cálculo independiente (revisor) de f, C53 y flujos 1–11 de Elis con A1/A2, desde la Historia del libro V6.3 de Elis y las series del frente E."""
import json, sys, openpyxl
from fractions import Fraction as Fr
libro, cifras = sys.argv[1], sys.argv[2]
wb = openpyxl.load_workbook(libro, data_only=True); h = wb["Historia"]; m = wb["Motor"]
C = "CDEFGHIJKL"
row = lambda r: {h[f"{c}5"].value: (None if h[f"{c}{r}"].value is None else Fr(str(h[f"{c}{r}"].value))) for c in C}
V, EB, DA, TAU, CAP, ADQ, DWC = (row(r) for r in (6, 7, 8, 10, 12, 13, 14))
yrs = [h[f"{c}5"].value for c in C]
n = int(h["C57"].value); fcf = Fr(str(h["C70"].value)); win = yrs[-n:]; hor = yrs[-5:]; G = yrs[-6]
d = json.load(open(cifras))
ser = {k: {int(y): -Fr(str(e["valor_publicado"])) for y, e in d["series"][k].items()} for k in ("da_rou", "da_ppa")}
E9 = d["referencia_E9"]
def DX(p, y):
    if p == "A0": return DA[y]
    if p == "A1": return DA[y] - ser["da_rou"][y]
    return DA[y] - ser["da_rou"][y] - ser["da_ppa"][y]
out = {}
fA0 = None
for p in ("A0", "A1", "A2"):
    nopat = sum(EB[y] * (1 - TAU[y]) for y in win) / n
    reinv = sum(CAP[y] - DX(p, y) + DWC[y] for y in win) / n
    f = (nopat - reinv - fcf) / (sum(V[y] for y in win) / n)
    c53 = (V[yrs[-1]] - V[G]) / sum(CAP[y] - DX(p, y) + DWC[y] + ADQ[y] for y in hor)
    out[p] = {"f": f, "C53": c53, "reinv": reinv}
    if p == "A0": fA0 = f
# flujos A1/A2 = flujos del libro A0 + V_t·(f_A0 − f_p) (años 1–10) y V10·(1+g)·(f_A0 − f_p) (año 11)
cols = ["AA","AB","AC","AD","AE","AF","AG","AH","AI","AJ"]; fc = ["AU","AV","AW","AX","AY","AZ","BA","BB","BC","BD"]
for p in ("A1", "A2"):
    dev = 0; y11 = []
    for esc, fila in (("MALO", 6), ("NORMAL", 7), ("BUENO", 8)):
        df = fA0 - out[p]["f"]
        for t in range(10):
            v = Fr(str(m[f"{fc[t]}{fila}"].value)) + Fr(str(m[f"{cols[t]}{fila}"].value)) * df
            dev = max(dev, abs(float(v) - E9["A1_A2_flujos_palancas_actuales"][p][esc][t]))
        v11 = Fr(str(m[f"BF{fila}"].value)) + Fr(str(m[f"AJ{fila}"].value)) * (1 + Fr(str(m[f"H{fila}"].value))) * df
        y11.append(float(v11)); dev = max(dev, abs(float(v11) - E9["A1_A2_flujos_palancas_actuales"][p][esc][10]))
    out[p]["anio11"] = y11; out[p]["dev_flujos_vs_E9"] = dev
for p in ("A0", "A1", "A2"):
    r = E9["perimetros"][p]
    print(p, "f", repr(float(out[p]["f"])), "E9", r["f"], "Δ", float(out[p]["f"]) - r["f"], "| C53", repr(float(out[p]["C53"])), "E9", r["S2C_C53"], "Δ", float(out[p]["C53"]) - r["S2C_C53"],
          "| reinv", float(out[p]["reinv"]), r["reinversion_media"], ("| año 11 " + str(out[p]["anio11"]) + f" dev máx flujos {out[p]['dev_flujos_vs_E9']:.2e}") if p != "A0" else "")
print("año 11 A1 − A0 (NORMAL):", out["A1"]["anio11"][1] - float(m["BF7"].value))
json.dump({p: {k: (float(v) if isinstance(v, Fr) else v) for k, v in out[p].items()} for p in out}, open(sys.argv[3], "w"), indent=1)
