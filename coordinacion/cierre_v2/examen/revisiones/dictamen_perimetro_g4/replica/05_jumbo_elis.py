"""5 · ¿Afecta igual a Jumbo y a Elis? Peso de los arrendamientos en el capital invertido y efecto en las anclas que usan la gramática
y las referencias (Historia!C55 frente a NOPAT NIIF 16 ÷ capital sin arrendamientos). Solo lectura de los libros recalculados.
Uso: 05_jumbo_elis.py LIBRO_AHOLD LIBRO_JUMBO LIBRO_ELIS"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from motor import leer, COLS_HIST

RANGOS = [("Historia", "A5:L90"), ("Análisis", "B14:D80"), ("Palancas", "B5:I24")]
for nombre, ruta in zip(("Ahold", "Jumbo", "Elis"), sys.argv[1:4]):
    L = leer(ruta, RANGOS)
    anios = [int(L[f"Historia!{c}5"]) for c in COLS_HIST]
    H = lambda fila: dict(zip(anios, [L.get(f"Historia!{c}{fila}") for c in COLS_HIST]))
    V, EBIT, t, arr, cap = H(6), H(7), H(10), H(23), H(32)
    h5 = anios[-5:]
    tot = sum(EBIT[y] * (1 - t[y]) / cap[y] for y in h5) / 5
    prop = sum(EBIT[y] * (1 - t[y]) / (cap[y] - arr[y]) for y in h5) / 5
    peso = arr[anios[-1]] / cap[anios[-1]]
    factor = cap[anios[-1]] / (cap[anios[-1]] - arr[anios[-1]])
    r = L.get("Análisis!C56")
    print(f"{nombre}: perímetro del libro {L.get('Historia!C89')!r} · arrendamientos {arr[anios[-1]]:.1f} = {peso:.1%} del capital invertido ({cap[anios[-1]]:.1f}) · factor capital total ÷ propio {factor:.3f}")
    print(f"   ROIC 5 años con todo el capital {tot:.2%} (Historia!C55 = {L.get('Historia!C55'):.2%}) · NOPAT NIIF 16 ÷ capital sin arrendamientos {prop:.2%} ({prop - tot:+.2%}; ×{prop / tot:.3f})")
    print(f"   umbral de G7: 2 × C55 = {2 * tot:.2%} · en el perímetro del S2C = {2 * prop:.2%} · r = {r} · C55 − r = {tot - r:+.2%} · C18 del libro = {L.get('Análisis!C18')!r}"
          f" · ancla S2C del perímetro (Historia!C53) = {L.get('Historia!C53')!r} · S2C medio C54 = {L.get('Historia!C54'):.2f} → sin arrendamientos {V[anios[-1]] / (cap[anios[-1]] - arr[anios[-1]]):.2f}")
