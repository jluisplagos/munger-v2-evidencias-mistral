"""2 · Ahold: qué lleva cada pieza del motor con A2_propio (alquiler una vez), retornos por perímetro y punto neutro del ROIC terminal.
Uso: 02_perimetro_ahold.py CARPETA_EXPEDIENTE"""
import json, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from motor import *

EXP = sys.argv[1]
L = leer(os.path.join(EXP, "recalc", "Ahold_v63_evaluada.xlsx"), RANGOS)
base, pal = base_del_libro(L), palancas_del_libro(L)
anios = [int(L[f"Historia!{c}5"]) for c in COLS_HIST]
H = lambda fila: dict(zip(anios, [L.get(f"Historia!{c}{fila}") for c in COLS_HIST]))
V, EBIT, DA, t, CFO, capex, dwc, intf, arr, sbc = (H(n) for n in (6, 7, 8, 10, 11, 12, 14, 16, 17, 18))
pat, deuda, pasivo_arr, caja, cap_inv, roic33 = (H(n) for n in (21, 22, 23, 24, 32, 33))
rou, ppa = H(86), H(87)
w = anios[-3:]
med = lambda d, ys=w: sum(d[y] for y in ys) / len(ys)

# Cifras publicadas que no están en la Historia (archivo y página del expediente, texto con marcas [PDF PAGE n]):
INT_ARR = {2021: 337, 2022: 356, 2023: 382, 2024: 422, 2025: 465}   # «Interest accretion to lease liability»: AR2022 p.251 · AR2023 p.262 · AR2024 p.321 · AR2025 p.272
IMP_PAGADO = {2023: 200, 2024: 470, 2025: 499}                      # «Income taxes paid – net»: AR2024 p.263 · AR2025 p.216
ROU_ACTIVO = {2024: 9649, 2025: 9488}                               # «Right-of-use assets» (balance): AR2025 p.214
COBROS = {"intereses": {2023: 160, 2024: 196, 2025: 130}, "subarriendos": {2023: 117, 2024: 125, 2025: 138}, "dividendos_nc": {2023: 22, 2024: 22, 2025: 28}}

print("=" * 110)
print("A · QUÉ LLEVA f CON A2_propio (ventana 2023–2025, medias anuales en mm) — el alquiler entra una vez")
S = med(V)
nopat = med({y: EBIT[y] * (1 - t[y]) for y in w})
dx = {y: DA[y] - rou[y] - ppa[y] for y in w}
reinv = med({y: capex[y] - dx[y] + dwc[y] for y in w})
C70 = L["Historia!C70"]
print(f"NOPAT medio {nopat:.3f} − reinversión propia media {reinv:.3f} − FCF base {C70:.3f} = f·V̄ = {nopat - reinv - C70:.3f} → f = {(nopat - reinv - C70) / S:.12f} (libro C58 = {L['Historia!C58']:.12f})")
c46, c47, c48, c49, c50 = (L[f"Análisis!C{n}"] for n in (46, 47, 48, 49, 50))
print(f"FCF base = C46 {c46:.3f} − C47 {c47:.3f} − C48 {c48:.3f} − C49 {c49:.3f} − C50 {c50:.3f} = {c46 - c47 - c48 - c49 - c50:.3f}")
pagos_brutos, amort_rou = med(arr), med(rou)
otros_cfo = med(CFO) - (med(EBIT) + med(DA) - med(dwc) - med(IMP_PAGADO))
partes = [("alquiler pagado por encima de la amortización de derechos de uso: pagos netos de subarriendos C49 − amortización ROU", c49 - amort_rou),
          ("intereses financieros netos (C48, regla espejo)", c48),
          ("SBC (C50)", c50),
          ("− amortización PPA (no es caja; D_X no la devuelve y f sí)", -med(ppa)),
          ("− dividendos de negocios conjuntos sumados en C46", -(c46 - med(CFO))),
          ("impuestos pagados − τ_año·EBIT (escudo fiscal de los intereses y devolución belga de 2023)", med(IMP_PAGADO) - med({y: EBIT[y] * t[y] for y in w})),
          ("− partidas del CFO que no son EBIT + D&A − circulante − impuestos (cargos no monetarios, SBC…)", -otros_cfo)]
for n, x in partes:
    print(f"   {x:+10.3f}  {n}")
print(f"   {sum(x for _, x in partes):+10.3f}  = f·V̄ (cuadra con {nopat - reinv - C70:.3f})")
print(f"   El alquiler de caja (fila 17, principal e intereses en una línea: AR2025 p.260) medio es {pagos_brutos:.1f}: {amort_rou:.1f} van en el margen (amortización ROU)")
print(f"   y {pagos_brutos - amort_rou:.1f} en f (brutos; {c49 - amort_rou:.1f} netos de subarriendos). Intereses de arrendamiento publicados, media: {med(INT_ARR):.1f}.")
print(f"   Sin las compensaciones, f sería {(c49 - amort_rou + c48 + c50 - med(ppa) - (c46 - med(CFO))) / S:.5f}; es {L['Historia!C58']:.5f} porque impuestos y partidas no monetarias restan {(med(IMP_PAGADO) - med({y: EBIT[y] * t[y] for y in w}) - otros_cfo):.1f}.")
F0 = base["V0"] * (base["m0"] * (1 - base["tau"]) - base["f"])
print(f"Flujo sin crecimiento del motor: V0·[m0(1−τ) − f] = {F0:.3f} (capa F1: 2769.835) · NOPAT 2025 al τ de 5 años = {base['V0'] * base['m0'] * (1 - base['tau']):.3f}")

print("=" * 110)
print("B · RETORNO HISTÓRICO POR PERÍMETRO (2021–2025)")
h5 = anios[-5:]
filas = []
for y in h5:
    k_tot = cap_inv[y]; k_own = cap_inv[y] - pasivo_arr[y]
    n16 = EBIT[y] * (1 - t[y]); nar = (EBIT[y] - INT_ARR[y]) * (1 - t[y])
    l_med = (pasivo_arr[y] + pasivo_arr[y - 1]) / 2
    i_arr = INT_ARR[y] / l_med
    liston_tot = (k_own * base["r"] + pasivo_arr[y] * i_arr * (1 - t[y])) / k_tot
    filas.append(dict(y=y, tot=n16 / k_tot, mixto=n16 / k_own, tras=nar / k_own, s2c_tot=V[y] / k_tot, s2c_own=V[y] / k_own, peso=pasivo_arr[y] / k_tot,
                      factor=k_tot / k_own, i_arr=i_arr, liston_tot=liston_tot))
    print(f"{y}: todo el capital {n16 / k_tot:6.2%} (fila 33 {roic33[y]:6.2%}) · NOPAT NIIF16 ÷ capital propio {n16 / k_own:6.2%} · (EBIT − intereses arrend.)(1−t) ÷ capital propio {nar / k_own:6.2%}"
          f" · S2C medio {V[y] / k_tot:4.2f} → {V[y] / k_own:4.2f} · arrend. {pasivo_arr[y] / k_tot:5.1%} del capital · coste arrend. {i_arr:5.2%} · listón todo el capital {liston_tot:5.2%}")
m5 = lambda k: sum(f_[k] for f_ in filas) / 5
print(f"MEDIA: todo el capital {m5('tot'):.4%} (C55 = {L['Historia!C55']:.4%}) · NIIF16 ÷ propio {m5('mixto'):.4%} · tras alquiler ÷ propio {m5('tras'):.4%} · factor capital total ÷ propio {m5('factor'):.3f}"
      f" · listón coherente de todo el capital {m5('liston_tot'):.2%}")
print(f"   Exceso sobre su listón, mismo perímetro: todo el capital {m5('tot') - m5('liston_tot'):+.2%} · capital propio tras alquiler {m5('tras') - base['r']:+.2%} (frente a r = {base['r']:.0%})")
print(f"   Lo que comparó la fase A: {m5('tot'):.2%} (todo el capital) frente a r = {base['r']:.0%} (listón del flujo del accionista): {m5('tot') - base['r']:+.2%} — cruce de perímetros")
# variante calculable solo con filas del libro V6.3.1 F1 (7, 10, 17, 23, 32 y 86): todo el alquiler de caja, sin dato nuevo
caja = {y: (EBIT[y] - (arr[y] - rou[y])) * (1 - t[y]) / (cap_inv[y] - pasivo_arr[y]) for y in h5}
print("   Con el alquiler de caja (EBIT − (pagos fila 17 − amortización ROU fila 86)): " + " · ".join(f"{y} {caja[y]:.2%}" for y in h5) + f" · media {sum(caja.values()) / 5:.2%}")
k25 = cap_inv[2025]
print(f"   2025 con el ACTIVO por derecho de uso ({ROU_ACTIVO[2025]}) en lugar del pasivo ({pasivo_arr[2025]:.0f}): capital sin ROU {k25 - ROU_ACTIVO[2025]:.0f} → S2C medio {V[2025] / (k25 - ROU_ACTIVO[2025]):.2f}"
      f" (con el pasivo {V[2025] / (k25 - pasivo_arr[2025]):.2f}; ancla marginal A1 de la capa F1: 5,10)")

print("=" * 110)
print("C · EL ROIC TERMINAL EN EL MOTOR: unidades y punto neutro")
r, tau, f = base["r"], base["tau"], base["f"]
for e in ESC:
    pv = pal[e]
    N = pv["mobj"] * (1 - tau)
    neutro = r * N / (N - f)
    print(f"{e}: N = m_obj(1−τ) = {N:.5f} · ROIC neutro (el crecimiento perpetuo ni crea ni destruye valor) = r·N/(N − f) = {neutro:.4%}")
    for roic in (0.08, 0.09, neutro, 0.12, 0.13, 0.15):
        s2c_t = roic / N
        vt_rel = (N * (1 - pv["ginf"] / roic) - f) / (r - pv["ginf"]) / ((N - f) / r)
        print(f"      B18 = {roic:7.4f} → S2C implícito del terminal {s2c_t:5.2f} · reinversión {pv['ginf'] * N / roic:7.4%} de las ventas · valor terminal ÷ el de crecimiento cero = {vt_rel:6.4f}"
              f" · retorno del accionista sobre el capital nuevo (N − f)·S2C_t = {(N - f) * s2c_t:6.2%}")
# comprobación numérica con la réplica: con el ROIC neutro, el terminal vale lo mismo que una perpetuidad sin crecimiento del flujo del año 11
pv = pal["NORMAL"]; N = pv["mobj"] * (1 - tau)
mo = motor(**base, **{**pv, "roic": r * N / (N - f)})
vt = mo["flujo_11"] / (r - pv["ginf"]); vt0 = mo["V11"] * (N - f) / r
print(f"Comprobación (NORMAL): valor terminal con B18 neutro {vt:.6f} = V11·(N − f)/r {vt0:.6f} (dif {vt - vt0:+.2e})")
