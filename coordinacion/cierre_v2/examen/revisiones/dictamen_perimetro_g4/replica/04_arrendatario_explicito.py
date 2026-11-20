"""4 · Demostración «sin doble cuenta y sin omisión»: un arrendatario sintético con las proporciones de Ahold, cuentas explícitas año a año
(ventas, EBIT NIIF 16, amortización propia y de derechos de uso, intereses de arrendamiento, impuestos, capex, altas de arrendamientos,
pagos), valorado de dos maneras:
  (1) DESCUENTO EXPLÍCITO de la caja del accionista (CFO − capex − pagos de arrendamiento), sin motor;
  (2) MOTOR A (réplica), con f calibrada como la calibra el libro (Historia C58, ventana de 3 años) y las palancas en cada perímetro.
Si el perímetro de las palancas es coherente con el de f, (2) = (1). Importes ficticios; ninguno es un dato de Ahold.
Uso: 04_arrendatario_explicito.py"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from motor import motor


def cuentas(V_prev, V, p):
    """Un ejercicio. Capital propio K = V/s_own y activo arrendado A = V/s_arr al cierre; pasivo por arrendamiento = activo."""
    K0, K1 = V_prev / p["s_own"], V / p["s_own"]
    A0, A1 = V_prev / p["s_arr"], V / p["s_arr"]
    ebit = p["m"] * V                               # EBIT NIIF 16: ya lleva la amortización propia y la de derechos de uso
    da_own, da_rou = p["d_own"] * K0, p["d_rou"] * A0
    interes = p["i"] * A0                           # intereses del pasivo por arrendamiento (fuera del EBIT)
    impuesto = p["tau"] * (ebit - interes)          # el interés es deducible
    capex = da_own + (K1 - K0)                      # reposición propia + crecimiento propio
    altas = da_rou + (A1 - A0)                      # altas de derechos de uso (sin caja: las financia el arrendador)
    principal = da_rou                              # el pasivo sigue al activo
    cfo = ebit + da_own + da_rou - impuesto         # NIIF: los pagos de arrendamiento van en financiación
    pagos = principal + interes                     # una sola línea, como «Repayment of lease liabilities»
    return dict(V=V, ebit=ebit, da=da_own + da_rou, da_rou=da_rou, interes=interes, impuesto=impuesto, capex=capex, altas=altas, cfo=cfo, pagos=pagos,
                fcfe=cfo - capex - pagos, K=K1, A=A1)


def valor_explicito(p, V0, g5, ginf, r):
    """Valor de la caja del accionista: 10 años explícitos + perpetuidad creciente desde el año 11 (cuentas explícitas del año 11)."""
    V_prev, vp, flujos = V0, 0.0, []
    for t in range(1, 11):
        g = g5 if t <= 5 else g5 - (g5 - ginf) * (t - 5) / 5
        c = cuentas(V_prev, V_prev * (1 + g), p)
        flujos.append(c["fcfe"])
        vp += c["fcfe"] / (1 + r) ** t
        V_prev = c["V"]
    c11 = cuentas(V_prev, V_prev * (1 + ginf), p)
    return vp + c11["fcfe"] / (r - ginf) / (1 + r) ** 10, flujos, c11


def calibrar_f(hist, perimetro):
    """f del libro (Historia C58) sobre la ventana: (NOPAT medio − (capex − D_X + circulante) medio − FCF base) ÷ ventas medias."""
    n = len(hist)
    S = sum(c["V"] for c in hist) / n
    nopat = sum(c["ebit"] * (1 - c["tau_ef"]) for c in hist) / n
    dx = lambda c: c["da"] if perimetro == "A0_total" else c["da"] - c["da_rou"]
    reinv = sum(c["capex"] - dx(c) for c in hist) / n
    fcf = sum(c["fcfe"] for c in hist) / n
    return (nopat - reinv - fcf) / S


def demo(nombre, p, g_hist, g5, ginf, r=0.09, V0=1000.0):
    print("=" * 118)
    print(nombre)
    # historia: 3 ejercicios con crecimiento g_hist que terminan en V0
    Vs = [V0 / (1 + g_hist) ** k for k in (3, 2, 1, 0)]
    hist = []
    for a, b in zip(Vs, Vs[1:]):
        c = cuentas(a, b, p)
        c["tau_ef"] = p["tau"]      # tipo efectivo de la cuenta de resultados (impuesto ÷ BAI): el legal, sin partidas raras
        hist.append(c)
    u = hist[-1]
    N = p["m"] * (1 - p["tau"])
    s_tot = 1 / (1 / p["s_own"] + 1 / p["s_arr"])
    f_A2, f_A0 = calibrar_f(hist, "A2_propio"), calibrar_f(hist, "A0_total")
    f_L = sum((1 - p["tau"]) * c["interes"] for c in hist) / sum(c["V"] for c in hist)
    print(f"Último ejercicio: ventas {u['V']:.1f} · EBIT NIIF 16 {u['ebit']:.2f} · amort. ROU {u['da_rou']:.2f} · intereses arrend. {u['interes']:.2f} · pagos arrend. {u['pagos']:.2f}"
          f" · capital propio {u['K']:.1f} · activo arrendado {u['A']:.1f} · caja del accionista {u['fcfe']:.2f}")
    roic_tot = u["ebit"] * (1 - p["tau"]) / (u["K"] + u["A"])
    roic_mixto = u["ebit"] * (1 - p["tau"]) / u["K"]
    roic_tras = (u["ebit"] - u["interes"]) * (1 - p["tau"]) / u["K"]
    wacc_tot = (u["K"] * r + u["A"] * p["i"] * (1 - p["tau"])) / (u["K"] + u["A"])
    print(f"Retorno: todo el capital {roic_tot:.2%} (listón coherente {wacc_tot:.2%}) · NOPAT NIIF 16 ÷ capital propio {roic_mixto:.2%} · tras todo el alquiler ÷ capital propio {roic_tras:.2%} (listón r = {r:.0%})")
    print(f"f calibrada como el libro: A2_propio {f_A2:.6f} (= intereses de arrendamiento después de impuestos ÷ ventas {f_L:.6f}) · A0_total {f_A0:.6f}")
    ve, flujos, c11 = valor_explicito(p, V0, g5, ginf, r)
    print(f"(1) Descuento explícito de la caja del accionista: {ve:.4f}")
    base = dict(V0=V0, m0=p["m"], tau=p["tau"], r=r, g5=g5, mobj=p["m"], ginf=ginf)
    casos = [("A2 coherente: f A2 · S2C propio · ROIC LP = (1+g∞)·N·S2C propio", f_A2, p["s_own"], (1 + ginf) * N * p["s_own"]),
             ("palancas con TODO el capital (1.ª pasada): f A2 · S2C total · ROIC LP = ROIC total", f_A2, s_tot, N * s_tot),
             ("S2C propio y ROIC LP = r (referencia mecánica)", f_A2, p["s_own"], r),
             ("S2C propio y ROIC LP neutro r·N/(N − f)", f_A2, p["s_own"], r * N / (N - f_A2)),
             ("A0 (V6.3): f A0 · S2C propio · ROIC LP coherente", f_A0, p["s_own"], (1 + ginf) * N * p["s_own"]),
             ("omisión: f = 0 (sin el interés) · S2C propio · ROIC LP coherente", 0.0, p["s_own"], (1 + ginf) * N * p["s_own"])]
    for n_, f, s2c, roic in casos:
        mo = motor(f=f, s2c=s2c, roic=roic, **base)
        print(f"(2) {n_:<82} ROIC LP {roic:7.4f} → {mo['total']:10.4f} ({mo['total'] / ve - 1:+8.3%} frente a (1))")
    mo0 = motor(f=f_A2, s2c=p["s_own"], roic=r * N / (N - f_A2), **dict(base, g5=0.0, ginf=0.0))
    print(f"    valor sin crecimiento (g = 0): {mo0['total']:.4f} · el crecimiento vale {ve - mo0['total']:+.4f} en (1)")
    print(f"    ROIC LP neutro en unidades del motor: {r * N / (N - f_A2):.4%} · umbral de G4 (r + 3): {r + 0.03:.2%} · ROIC LP coherente con la historia: {(1 + ginf) * N * p['s_own']:.2%}")
    return ve


# Proporciones de Ahold 2025 (redondeadas): S2C propio 5,4; ventas ÷ pasivo por arrendamiento 7,7; coste del arrendamiento 3,84 %; τ 21,436 %
AHOLD = dict(m=0.04, tau=0.21436, s_own=5.4, s_arr=7.7, i=0.0384, d_own=0.136, d_rou=0.117)
demo("A · Arrendatario con las proporciones de Ahold, crecimiento constante del 2 % (identidad exacta)", AHOLD, g_hist=0.02, g5=0.02, ginf=0.02)
demo("B · El mismo, con la senda del NORMAL de Ahold (2,5 % cinco años y bajada al 2 %)", AHOLD, g_hist=0.025, g5=0.025, ginf=0.02)
# C · arrendatario SIN retorno en exceso: el margen que deja el retorno del capital propio, después de todo el alquiler, en r
N_eq = 0.09 / AHOLD["s_own"] + (1 - AHOLD["tau"]) * AHOLD["i"] / AHOLD["s_arr"] / 1.02
demo("C · Arrendatario sin retorno en exceso: el capital propio rinde r después de todo el alquiler (y todo el capital, su listón mezclado)",
     dict(AHOLD, m=N_eq / (1 - AHOLD["tau"])), g_hist=0.02, g5=0.02, ginf=0.02)
print("    (en C queda un valor del crecimiento de un 2,5 %: es la convención temporal del motor, en la que la inversión del año ya rinde ese año)")
print("    Lectura: sin exceso en un perímetro ⇔ sin exceso en el otro; en unidades del motor ese caso neutro es NOPAT NIIF 16 ÷ capital propio = 11,1 %,")
print("    no 9 %, porque f lleva el interés del arrendamiento; aun así queda por debajo del umbral de G4 (12 %).")
u = cuentas(1000 / 1.02, 1000.0, AHOLD)
print("=" * 118)
print("D · ¿Qué EBIT corresponde a A2? EBIT NIIF 16 − intereses de arrendamiento = EBITDA − alquiler de caja − amortización propia (todo el alquiler, una vez)")
print(f"   sintético: {u['ebit']:.2f} − {u['interes']:.2f} = {u['ebit'] - u['interes']:.2f} · {u['ebit'] + u['da']:.2f} − {u['pagos']:.2f} − {u['da'] - u['da_rou']:.2f} = {u['ebit'] + u['da'] - u['pagos'] - (u['da'] - u['da_rou']):.2f}")
print(f"   Ahold 2025 (Historia y AR2025 p.272): 3.542 − 465 = {3542 - 465} · EBITDA 7.275 − pagos 1.944 − amortización propia y PPA (3.733 − 1.400) = {7275 - 1944 - (3733 - 1400)}"
      f" (la diferencia, {3542 - 465 - (7275 - 1944 - (3733 - 1400))}, es el principal pagado por encima de la amortización del derecho de uso)")
