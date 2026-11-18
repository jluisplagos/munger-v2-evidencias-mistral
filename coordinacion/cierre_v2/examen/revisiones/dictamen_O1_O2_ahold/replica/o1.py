import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from motor import *

# Ventana 2023-2025 (Historia C57 = 3)
ventas = [88734, 89356, 92352]
ebit = [2846, 2784, 3542]
tipo = [0.1983, 0.2165, 0.2242]
reinv = [198, -46, 85]              # Historia fila 30 (A2_propio)
fcf_acc = [1938, 1910, 2150]        # Historia fila 35
int_cob = [160, 196, 130]           # AR2024 p.263, AR2025 p.216
sub = [117, 125, 138]
jv = [22, 22, 28]
int_pag = [226, 230, 261]
nopat = [e * (1 - t) for e, t in zip(ebit, tipo)]
S = sum(ventas)
num0 = sum(nopat) - sum(reinv) - sum(fcf_acc)
print("suma NOPAT", sum(nopat), "reinv", sum(reinv), "FCF", sum(fcf_acc), "ventas", S)
print("f libro", num0 / S, " (C58 = 0.0036081074685145)")

def f_con(extra):
    return (num0 - extra) / S

print()
base = resumen("Libro")
casos = [
    ("O1 · los tres cobros (938 en 3 años)", sum(int_cob) + sum(sub) + sum(jv)),
    ("   solo intereses cobrados (486)", sum(int_cob)),
    ("   solo cobros de subarriendos (380)", sum(sub)),
    ("   solo dividendos de negocios conjuntos (72)", sum(jv)),
    ("   subarriendos + dividendos NC (452), sin intereses", sum(sub) + sum(jv)),
]
for n, x in casos:
    f = f_con(x)
    V, pond, ps = resumen(f"{n}  f={f:.6f}", f=f)
    print(f"      Δ precio de Sí {ps - base[2]:+.2f}  Δ ponderado {pond - base[1]:+.2f}   por año {x/3:.1f} mm = {x/3/1999.334:.1%} del FCF base")

print()
print("Solo 2025 (ventana de un año), como el suelo del contradictor:")
f25 = (nopat[2] - reinv[2] - fcf_acc[2]) / ventas[2]
resumen(f"   2025 sin cobros f={f25:.6f}", f=f25)
f25c = (nopat[2] - reinv[2] - fcf_acc[2] - int_cob[2] - sub[2] - jv[2]) / ventas[2]
resumen(f"   2025 con cobros f={f25c:.6f}", f=f25c)
print()
print("Devolución fiscal belga 2023 (367) fuera, con y sin cobros:")
resumen(f"   sin devolución, sin cobros f={(num0+367)/S:.6f}", f=(num0 + 367) / S)
resumen(f"   sin devolución, con cobros f={(num0+367-938)/S:.6f}", f=(num0 + 367 - 938) / S)

# Valor de capitalizar cada corriente en el NORMAL (por acción y total)
print()
V0n = tres()[1]
for n, x in casos:
    Vn = tres(f=f_con(x))[1]
    print(f"NORMAL: {n.strip():<55} +{(Vn - V0n):.2f} €/acc = {(Vn - V0n)*905:,.0f} mm de valor (corriente media {x/3:.0f}/año → múltiplo {(Vn - V0n)*905/(x/3):.1f}x)")
print("Caja al cierre 2025: 3.605 mm = %.2f €/acc; deuda financiera 6.429; arrendamientos 11.974" % (3605 / 905))
print("Intereses pagados medios 239/año; valor de esa fuga en el NORMAL:")
Vsin = tres(f=(num0 + sum(int_pag)) / S)[1]  # si NO se restaran intereses pagados
print("   %.2f €/acc = %.0f mm frente a deuda financiera de 6.429 mm" % (Vsin - V0n, (Vsin - V0n) * 905))
