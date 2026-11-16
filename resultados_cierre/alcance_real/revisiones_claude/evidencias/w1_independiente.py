"""Verificacion independiente (Mistral C/F, sesion distinta del autor Claude) del bloque W1
de controles_sinteticos_f1.py @ d519eb0, reconstruido desde cero con Fraction.

Modelo (g = 0, declarado como limite: con g > 0 el flujo base crece y esta caja simplificada
no lo modela; el script del autor cubre g = 2 % internamente):
  N = 10 anos explicititos, r = 10 %, caja sostenible base 68, coste temporal X = 7
  hasta el ano H inclusive, g = 0.
  caja(H)      = sum_{t=1..10} 68/1.1^t + (68/r)/1.1^10 - sum_{t=1..H} 7/1.1^t
  anterior(H)  = sum_{t=1..10} fl_t/1.1^t + fl_11/r/1.1^10,  fl_t = 68 - 7 si t <= H
  propuesta(H) = sum_{t=1..10} fl'_t/1.1^t + (68/r)/1.1^10 - sum_{t=11..H} 7/1.1^t,
                 fl'_t = 68 - 7 si t <= min(H, 10)  (X = 0 desde el ano 11 en el motor)
Con g = 0 las tres reglas son formas cerradas exactas en Fraction.
"""
import json
from fractions import Fraction as Fr

N = 10
r = Fr(1, 10)
BASE = Fr(68)
X = Fr(7)

def caja(H):
    base = sum(BASE / (1 + r) ** t for t in range(1, N + 1)) + BASE / r / (1 + r) ** N
    return base - sum(X / (1 + r) ** t for t in range(1, H + 1))

def anterior(H):
    fl = [BASE - X if t <= H else BASE for t in range(1, N + 1)]
    term = BASE - X if H >= N + 1 else BASE
    return sum(f / (1 + r) ** t for t, f in enumerate(fl, start=1)) + term / r / (1 + r) ** N

def propuesta(H):
    fl = [BASE - X if t <= min(H, N) else BASE for t in range(1, N + 1)]
    vp = sum(f / (1 + r) ** t for t, f in enumerate(fl, start=1)) + BASE / r / (1 + r) ** N
    pend = sum(X / (1 + r) ** t for t in range(N + 1, H + 1))
    return vp - pend

pub = json.load(open("controles_sinteticos_f1.json"))["W1_coste_temporal_despues_del_año_10"]
pub_g0 = [c for c in pub if c["g"] == 0]
print(f"{'H':>3} {'caja(exacta)':>22} {'anterior(exacta)':>22} {'propuesta(exacta)':>22} "
      f"{'|pub caja':>12} {'|pub ant':>12} {'|pub prop':>12} ok")
allok = True
for H in (5, 10, 11, 12):
    cj, an, pr = caja(H), anterior(H), propuesta(H)
    p = next(c for c in pub_g0 if c["H"] == H)
    d1 = abs(float(cj) - p["vp_caja_del_escenario"])
    d2 = abs(float(an) - p["vp_regla_anterior"])
    d3 = abs(float(pr) - p["vp_regla_propuesta"])
    ok = d1 < 1e-9 and d2 < 1e-9 and d3 < 1e-9 and (an == cj) == (H <= N) and pr == cj
    allok &= ok
    print(f"{H:>3} {float(cj):>22.13f} {float(an):>22.13f} {float(pr):>22.13f} "
          f"{d1:>12.2e} {d2:>12.2e} {d3:>12.2e} {ok}")
print("anterior(H=11) == 610 exacto:", anterior(11) == Fr(610), "| anterior(H=12) == 610:", anterior(12) == Fr(610))
print("identidad propuesta == caja (g=0, todo H):", all(propuesta(H) == caja(H) for H in (5, 10, 11, 12)))
print("RESULTADO:", "COINCIDE CON LO PUBLICADO" if allok else "DIFIERENCIA")
