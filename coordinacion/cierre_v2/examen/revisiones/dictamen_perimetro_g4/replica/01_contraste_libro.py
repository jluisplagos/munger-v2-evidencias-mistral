"""1 · La réplica reproduce el libro recalculado (primera pasada de la fase B) y precio.json. Uso: 01_contraste_libro.py CARPETA_EXPEDIENTE"""
import json, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from motor import *

EXP = sys.argv[1]
L = leer(os.path.join(EXP, "recalc", os.path.basename(EXP) + "_v63_evaluada.xlsx"), RANGOS)
base, pal = base_del_libro(L), palancas_del_libro(L)
print("base:", base)
for e in ESC:
    print(" ", e, pal[e])
dif = 0.0
vals = []
for e, fila in zip(ESC, (6, 7, 8)):
    mo = motor(**base, **pal[e])
    for t, c in enumerate(["AU", "AV", "AW", "AX", "AY", "AZ", "BA", "BB", "BC", "BD"]):
        dif = max(dif, abs(mo["flujos"][t] - L[f"Motor!{c}{fila}"]))
    dif = max(dif, abs(mo["flujo_11"] - L[f"Motor!BF{fila}"]), abs(mo["total"] - L[f"Motor!BI{fila}"]))
    vals.append(mo["por_accion"])
    print(f"{e}: réplica {mo['por_accion']:.10f} · libro Motor!BK{fila} {L[f'Motor!BK{fila}']:.10f} · dif {mo['por_accion'] - L[f'Motor!BK{fila}']:+.2e}"
          f" · rent. marginal {mo['rent_marginal']:.6f} (libro BQ {L[f'Motor!BQ{fila}']:.6f}) · % terminal {mo['peso_terminal']:.4f}")
print(f"desviación máxima en 33 flujos y 3 totales: {dif:.2e} mm")
sc = sin_crecimiento(**base)
print(f"sin crecimiento: réplica {sc:.10f} · libro Motor!BO7 {L['Motor!BO7']:.10f}")
pj = json.load(open(os.path.join(EXP, "precio.json"), encoding="utf-8"))
esc = escalera(vals, pj["p"], pj["precio"], pj["k"])
print(f"escalera: precio de Sí {esc['precio_si']:.10f} (precio.json {pj['precio_si']:.10f}) · ponderado {esc['ponderado']:.10f} ({pj['ponderado']:.10f}) · zona {esc['zona']} ({pj['zona']})")
assert dif < 1e-8 and abs(esc["precio_si"] - pj["precio_si"]) < 1e-9 and abs(esc["ponderado"] - pj["ponderado"]) < 1e-9 and esc["zona"] == pj["zona"]
print("RÉPLICA CONFORME con el libro y con precio.json")
