"""Sonda 3b del revisor · ¿qué implementaciones en coma flotante detecta de verdad el caso F10 (y F07, F21, F16)?
Compara la regla exacta (fracciones) con variantes en coma flotante: suma secuencial con «+», sum() del intérprete
(compensada desde Python 3.12), math.fsum, forma con división y forma sin división."""
import math
import sys
from fractions import Fraction as Fr

print("Python", sys.version.split()[0])
casos = {"F07": (["0.3", "0.3", "0.3"], "300"), "F10": (["0.1", "0.2", "0.3"], "200"), "F21": (["300", "300", "300"], "300000"),
         "F14 (1 %)": (["1", "1", "1"], "100"), "F29": (["0.05", "0.05", "0.05"], "79.94"),
         "R7 igualdad con decimales no binarios: 0,7 + 0,1 + 0,1 y FCF 300": (["0.7", "0.1", "0.1"], "300"),
         "R8 igualdad: 0,1 × 3 y FCF 100": (["0.1", "0.1", "0.1"], "100")}
u = {"F14 (1 %)": "0.01"}
def sec(xs):
    s = 0.0
    for x in xs:
        s = s + x
    return s
print(f"{'caso':<62} exacto | '+' ÷ | sum() ÷ | fsum ÷ | '+' sin ÷ | sum() sin ÷")
for k, (rou, fcf) in casos.items():
    uu = u.get(k, "0.001")
    ex = sum(Fr(x) for x in rou) <= Fr(uu) * len(rou) * Fr(fcf)
    fl = [float(x) for x in rou]
    f, n, U = float(fcf), len(rou), float(uu)
    r = [sec(fl) / n / f <= U, sum(fl) / n / f <= U, math.fsum(fl) / n / f <= U, sec(fl) <= U * n * f, sum(fl) <= U * n * f]
    t = lambda b: "AVISO  " if b else "BLOQUEA"   # noqa: E731
    print(f"{k:<62} {t(ex)}| {t(r[0])}| {t(r[1])} | {t(r[2])}| {t(r[3])}   | {t(r[4])}")
print("\nLectura: una implementación en coma flotante coincide o no con la exacta según cómo sume y si divide;")
print("F10 solo detecta la suma secuencial con «+» y división. La hoja de cálculo del motor trabaja en coma flotante.")
