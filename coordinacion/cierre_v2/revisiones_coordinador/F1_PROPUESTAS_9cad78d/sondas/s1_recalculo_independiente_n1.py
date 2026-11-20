"""Sonda 1 del revisor · recálculo independiente de las cifras de N1 (alcance y actualización de México).

No importa `contraste_f1.py` ni el script del autor: lee el CSV verificado y el libro por su cuenta y rehace las cuentas
con otra disposición (fórmulas cerradas de la variación, además del motor completo). Solo lectura.

Uso: python3 -I s1_recalculo_independiente_n1.py <cifras_fuente.csv> <Elis_v63_evaluada.xlsx>
"""
import csv
import sys
from fractions import Fraction as Fr

import openpyxl

CSV, LIBRO = sys.argv[1], sys.argv[2]
v = {}
for r in csv.DictReader(open(CSV, encoding="utf-8"), delimiter=";"):
    if r["tipo"] == "tabla":
        v[r["id"]] = (Fr(r["valor_publicado"]), r["edicion"], r["doc"], r["pagina"], r["literal"])


def x(i):
    val, ed, *_ = v[i]
    assert ed == "vigente", (i, ed)
    return val


wb = openpyxl.load_workbook(LIBRO, data_only=True, read_only=True)
H, P, A, M = wb["Historia"], wb["Palancas"], wb["Análisis"], wb["Motor"]
fr = lambda c: Fr(str(c))  # noqa: E731
pal = {n: dict(g15=fr(P[f"{c}14"].value), m_obj=fr(P[f"{c}15"].value), s2c=fr(P[f"{c}16"].value), roic=fr(P[f"{c}18"].value),
               g_inf=fr(A[f"{c}68"].value)) for n, c in (("MALO", "B"), ("NORMAL", "C"), ("BUENO", "D"))}
libro = dict(tau5=fr(H["C52"].value), f=Fr(H["C58"].value), fcf=Fr(H["C70"].value),
             f11={n: Fr(M[f"BF{k}"].value) for n, k in (("MALO", 6), ("NORMAL", 7), ("BUENO", 8))})

# --- entradas (edición vigente de cada ejercicio)
S = {2021: "_U22_2021", 2022: "_U23_2022", 2023: "_FR_2023", 2024: "_2024", 2025: "_2025"}
bai = {y: x("IS_BAI" + s) for y, s in S.items()}
imp = {y: -x("IS_IMP" + s) for y, s in S.items()}
fin = {y: -x("IS_FIN" + s) for y, s in S.items()}
earn = {2021: x("OOIE_EARN_U22_2021"), 2022: x("OOIE_EARN_U23_2022"), 2023: x("OOIE_EARN_FR_2023"), 2024: x("OOIE_EARN_2024"), 2025: x("OOIE_EARN_2025")}
act = {2023: x("FIN_ACTMEX_FR_2023"), 2024: x("FIN_ACTMEX_2024"), 2025: x("FIN_ACTMEX_2025")}
VENT, HOR = (2023, 2024, 2025), (2021, 2022, 2023, 2024, 2025)
ventas = {y: x("IS_VENTAS" + S[y]) for y in VENT}
V0, S_avg = ventas[2025], sum(ventas.values()) / 3
ebit = {y: bai[y] + fin[y] for y in HOR}                      # EBIT de la Historia = BAI + resultado financiero


def r4(q):
    """Fila 10 de la Historia: tipo con 4 decimales (redondeo al más cercano, como el libro)."""
    return Fr(round(q, 4)).limit_denominator(10 ** 4)


def tipos(n1=(), act_fuera=(), t_efecto=None, exacto=False):
    """n1: años con el ajuste de earnout fuera del BAI; act_fuera: años con la actualización fuera del BAI;
    t_efecto: {año: tipo} si el ajuste lleva su impuesto. Devuelve tipo por año."""
    t_efecto = t_efecto or {}
    out = {}
    for y in HOR:
        b, t = bai[y], imp[y]
        if y in n1:
            b -= earn[y]                                      # cargo (negativo) fuera: el BAI sube
            if y in t_efecto:
                t -= t_efecto[y] * earn[y]                    # y su impuesto, si lo lleva
        if y in act_fuera:
            b += act[y]
        q = t / b
        out[y] = q if exacto else r4(q)
    return out


def motor(tau_y, n1=(), exacto_f=False):
    """Flujo sin crecimiento y año 11 con la f de A0 recalculada. f = f_libro + (NOPAT' − NOPAT_libro)/S_avg."""
    t0 = tipos()
    nopat0 = sum(ebit[y] * (1 - t0[y]) for y in VENT) / 3
    e1 = {y: ebit[y] - (earn[y] if y in n1 else 0) for y in HOR}
    nopat1 = sum(e1[y] * (1 - tau_y[y]) for y in VENT) / 3
    f = libro["f"] + (nopat1 - nopat0) / S_avg
    tau5 = sum(tau_y.values()) / 5
    m0 = e1[2025] / V0
    res = {"tau5": tau5, "m0": m0, "f": f, "F0": V0 * (m0 * (1 - tau5) - f), "f11": {}}
    for n, p in pal.items():
        V = V0
        for t in range(1, 11):
            g = p["g15"] if t <= 5 else p["g15"] - (p["g15"] - p["g_inf"]) * Fr(t - 5, 5)
            V *= 1 + g
        res["f11"][n] = V * (1 + p["g_inf"]) * (p["m_obj"] * (1 - tau5) * (1 - p["g_inf"] / p["roic"]) - f)
        res.setdefault("V10", {})[n] = V
    return res


def d(a, b):
    return float(a["F0"] - b["F0"]), {n: float(a["f11"][n] - b["f11"][n]) for n in pal}


fmt = lambda t: " / ".join(f"{float(t[y]):.4f}" for y in HOR)  # noqa: E731
base = motor(tipos())
print("== 0. Libro")
print(" tipos:", fmt(tipos()), "| τ5 =", float(base["tau5"]), "(libro", float(libro["tau5"]), ")")
print(" F0 =", round(float(base["F0"]), 6), "| año 11:", {n: round(float(q), 4) for n, q in base["f11"].items()},
      "| libro BF6..8:", {n: round(float(q), 4) for n, q in libro["f11"].items()})
assert abs(base["tau5"] - libro["tau5"]) < Fr(1, 10 ** 9)
assert all(abs(base["f11"][n] - libro["f11"][n]) < Fr(1, 10 ** 6) for n in pal), "el año 11 del libro no se reproduce"

t21, t22 = Fr("28.41") / 100, Fr("25.83") / 100
esc = {
    "C · N1 2023–25": dict(n1=VENT),
    "B · N1 2022–25": dict(n1=(2022,) + VENT),
    "A′ · N1 2021–25, 2021 gravado al 28,41 %": dict(n1=HOR, t_efecto={2021: t21}),
    "A · N1 2021–25, sin efecto fiscal": dict(n1=HOR),
    "desc. · 2023–25 + 2021 sin efecto fiscal": dict(n1=(2021,) + VENT),
    "sens. B · 2022 tributa lo que la línea 0,5 no cubre": dict(n1=(2022,) + VENT, t_efecto={2022: (t22 * earn[2022] - Fr("0.5")) / earn[2022]}),
    "C + actualización": dict(n1=VENT, act_fuera=VENT),
    "B + actualización": dict(n1=(2022,) + VENT, act_fuera=VENT),
}
R = {k: motor(tipos(**kw), n1=kw["n1"]) for k, kw in esc.items()}
C = R["C · N1 2023–25"]
print("\n== 1. Escenarios (τ redondeado a 4 decimales, como la fila 10)")
for k, kw in esc.items():
    r = R[k]
    a0, a11 = d(r, base)
    c0, c11 = d(r, C)
    print(f" {k}\n   tipos {fmt(tipos(**kw))} | τ5 {float(r['tau5']):.5f} | f {float(r['f']):.9f} | m0 {float(r['m0']):.6f}")
    print(f"   frente al libro: {a0:+.3f} · " + " / ".join(f"{a11[n]:+.3f}" for n in pal) +
          f"   | frente a C: {c0:+.3f} · " + " / ".join(f"{c11[n]:+.3f}" for n in pal))

print("\n== 2. Fórmula cerrada de la variación de alcance (solo cambia τ5): ΔF0 = −V0·m0·Δτ5; Δaño11 = −V10(1+g∞)·m_obj·(1−g∞/ROIC)·Δτ5")
for k in ("B · N1 2022–25", "A′ · N1 2021–25, 2021 gravado al 28,41 %", "A · N1 2021–25, sin efecto fiscal"):
    dt = R[k]["tau5"] - C["tau5"]
    f0 = -V0 * C["m0"] * dt
    p = pal["NORMAL"]
    f11 = -C["V10"]["NORMAL"] * (1 + p["g_inf"]) * p["m_obj"] * (1 - p["g_inf"] / p["roic"]) * dt
    print(f" {k}: Δτ5 = {float(dt):+.6f} → ΔF0 = {float(f0):+.3f}; Δaño 11 NORMAL = {float(f11):+.3f}")
    assert R[k]["f"] == C["f"] and R[k]["m0"] == C["m0"]

print("\n== 3. Las cifras que pide comprobar el encargo")
chk = [("B frente al libro, flujo sin crecimiento", d(R["B · N1 2022–25"], base)[0], -11.908),
       ("B frente al libro, año 11 NORMAL", d(R["B · N1 2022–25"], base)[1]["NORMAL"], -18.948),
       ("B frente a C, flujo sin crecimiento", d(R["B · N1 2022–25"], C)[0], -0.302),
       ("B frente a C, año 11 NORMAL", d(R["B · N1 2022–25"], C)[1]["NORMAL"], -0.339),
       ("A frente al libro, flujo sin crecimiento", d(R["A · N1 2021–25, sin efecto fiscal"], base)[0], -11.190),
       ("A frente al libro, año 11 NORMAL", d(R["A · N1 2021–25, sin efecto fiscal"], base)[1]["NORMAL"], -18.142),
       ("A frente a C, flujo", d(R["A · N1 2021–25, sin efecto fiscal"], C)[0], 0.416),
       ("A frente a C, año 11 NORMAL", d(R["A · N1 2021–25, sin efecto fiscal"], C)[1]["NORMAL"], 0.466),
       ("A′ frente a C, flujo", d(R["A′ · N1 2021–25, 2021 gravado al 28,41 %"], C)[0], -0.202),
       ("A′ frente a C, año 11 NORMAL", d(R["A′ · N1 2021–25, 2021 gravado al 28,41 %"], C)[1]["NORMAL"], -0.226),
       ("C frente al libro, flujo", d(C, base)[0], -11.605), ("C frente al libro, año 11 NORMAL", d(C, base)[1]["NORMAL"], -18.609),
       ("actualización (C+act − C), flujo", d(R["C + actualización"], C)[0], -0.790),
       ("actualización (C+act − C), año 11 NORMAL", d(R["C + actualización"], C)[1]["NORMAL"], -1.661),
       ("C + actualización frente al libro, flujo", d(R["C + actualización"], base)[0], -12.396),
       ("C + actualización frente al libro, año 11 NORMAL", d(R["C + actualización"], base)[1]["NORMAL"], -20.270),
       ("B + actualización frente al libro, flujo", d(R["B + actualización"], base)[0], -12.698),
       ("B + actualización frente al libro, año 11 NORMAL", d(R["B + actualización"], base)[1]["NORMAL"], -20.609)]
mal = 0
for n, calc, ref in chk:
    ok = abs(calc - ref) < 0.0006
    mal += not ok
    print(f" {'OK ' if ok else 'MAL'} {n}: {calc:+.4f} (documento {ref:+.3f})")

print("\n== 4. Sensibilidad al redondeo de la fila 10 (tipo exacto en lugar de 4 decimales)")
bx = motor(tipos(exacto=True))
Rx = {k: motor(tipos(exacto=True, **kw), n1=kw["n1"]) for k, kw in esc.items()}
for k in ("B · N1 2022–25", "A′ · N1 2021–25, 2021 gravado al 28,41 %", "A · N1 2021–25, sin efecto fiscal", "C + actualización"):
    c0, c11 = d(Rx[k], Rx["C · N1 2023–25"])
    print(f" {k}: frente a C con tipos exactos {c0:+.3f} · año 11 NORMAL {c11['NORMAL']:+.3f}")

print("\n== 5. Tamaño relativo (sobre el FCF base 307,933)")
for k in ("B · N1 2022–25", "A′ · N1 2021–25, 2021 gravado al 28,41 %", "A · N1 2021–25, sin efecto fiscal", "C + actualización"):
    c0, _ = d(R[k], C)
    print(f" {k}: {100 * abs(c0) / float(libro['fcf']):.3f} % del FCF base")
print(" B frente a A (lo que de verdad separa a las opciones: el tratamiento fiscal de 2021):",
      f"{d(R['B · N1 2022–25'], R['A · N1 2021–25, sin efecto fiscal'])[0]:+.3f}",
      f"= {100 * abs(d(R['B · N1 2022–25'], R['A · N1 2021–25, sin efecto fiscal'])[0]) / float(libro['fcf']):.3f} % del FCF base")
print(" B frente a A′:", f"{d(R['B · N1 2022–25'], R['A′ · N1 2021–25, 2021 gravado al 28,41 %'])[0]:+.3f}")

print("\n== 6. Invariantes conservados")
print(" FCF base del libro (Historia!C70) =", float(libro["fcf"]), "| C48 =", A["C48"].value, "| C49 =", A["C49"].value, "| C52 =", A["C52"].value)
print("\nRESULTADO:", "todas las cifras reproducidas" if not mal else f"{mal} cifras NO reproducidas")
sys.exit(1 if mal else 0)
