import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from motor import *

ventas = [88734, 89356, 92352]; ebit = [2846, 2784, 3542]; tipo = [0.1983, 0.2165, 0.2242]
reinv = [198, -46, 85]; fcf = [1938, 1910, 2150]
int_cob = [160, 196, 130]; sub = [117, 125, 138]; jv = [22, 22, 28]
S = sum(ventas); num0 = sum(e * (1 - t) for e, t in zip(ebit, tipo)) - sum(reinv) - sum(fcf)
FB = 0.0036081074685145

def zona(precio, malo, ps, pond):
    return "bajo_malo" if precio <= malo else "cumple_regla_k" if precio <= ps else "vigilar" if precio <= pond else "caro"

o1 = [("O1-A · sin cambio (decisión de la etapa 1)", 0.0),
      ("O1-C · + subarriendos y dividendos NC (452)", sum(sub) + sum(jv)),
      ("O1-C' · + solo subarriendos (380)", sum(sub)),
      ("O1-B · + los tres cobros (938)", sum(int_cob) + sum(sub) + sum(jv))]
o2 = [("905 (libro: media diluida 2025)", 905.0), ("890,9 (cierre 2025 + 4 condicionales)", 886.877259 + 4), ("886,877 (cierre 2025, criterio D3/E6)", 886.877259),
      ("881 (etapa 1: media diluida 2T26)", 881.0), ("867,2 (27-sep-2026 + dilución)", 867.2), ("865,174 (27-sep-2026, básicas)", 865.173863)]
precio = 36.05
for n1, x in o1:
    f = FB if x == 0 else (num0 - x) / S
    print(f"\n{n1}   f = {f:.6f}")
    for n2, N in o2:
        V = tres(f=f, acciones=N)
        pond = sum(pi * v for pi, v in zip(P, V)); ps = min(precio_si(V), V[1])
        print(f"   {n2:<42} MALO {V[0]:6.2f} NORMAL {V[1]:6.2f} BUENO {V[2]:6.2f} · pond {pond:6.2f} · P_Sí {ps:6.2f} ({ps-27.735943834595208:+.2f}) · precio/P_Sí {precio/ps-1:+.1%} · zona {zona(precio, V[0], ps, pond)}")

# Avance coherente a 27-sep-2026 (información): E_t = E0·(1+r)^t − repartos capitalizados
print("\nAvance coherente a 27-sep-2026 (solo O2, f del libro):")
r = 0.09; t = 39 / 52
for nombre, i in (("MALO", 0), ("NORMAL", 1), ("BUENO", 2)):
    E0 = tres()[i] * 905
    div_abr = 0.73 * 880.0; div_ago = 0.51 * 868.0   # acciones aproximadas en cada fecha de pago
    rec = 23.847837 * 35.41
    Et = E0 * (1 + r) ** t - div_abr * (1 + r) ** (t - 0.315) - div_ago * (1 + r) ** (t - 0.66) - rec * (1 + r) ** (t / 2)
    print(f"   {nombre}: E0 {E0:,.0f} → E_t {Et:,.0f}; por acción básica {Et/865.173863:.2f} · diluida {Et/867.2:.2f} · libro {tres()[i]:.2f} · E0/886,877 = {E0/886.877259:.2f} · E0/867,2 = {E0/867.2:.2f}")
print("   repartos 2026 hasta 27-sep: dividendos ≈ %.0f + %.0f; recompras %.0f" % (0.73 * 880.0, 0.51 * 868.0, 23.847837 * 35.41))
