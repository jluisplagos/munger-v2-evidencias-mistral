#!/usr/bin/env python3
"""Sensibilidad FINITA y preanunciada (anunciada en INVENTARIO_Y_PLAN.md §4 ANTES de ver
resultados) de k y de las probabilidades, sobre los vectores fijos de los casos A1, H1, H2.

Rejilla fija:
  - k ∈ {1, 1,5, 2, 2,5, 3, 4, 5, 10}  (dominio de la guarda del producto k ≥ 1)
  - p = (δ, 1−2δ, δ) con δ ∈ {0,05, 0,10, 0,15, 0,20, 0,25, 0,30}
    más los dos vectores históricos asimétricos y su espejo:
    (0,25, 0,60, 0,15) y (0,15, 0,60, 0,25)

No se simula ninguna distribución nueva como si estuviera calibrada: son variaciones
aritméticas de los vectores publicados. Los importes históricos se usan solo para
contraste (zona con el precio publicado), nunca como objetivo vigente.

Escribe `../SENSIBILIDAD_FINITA.csv`. Oráculo propio.
Uso: python3 sensibilidad_finita.py
"""
import csv
import json
import os
import sys
from fractions import Fraction

AQUI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, AQUI)
import oraculo_precio_si as O

K_GRID = ["1", "3/2", "2", "5/2", "3", "4", "5", "10"]
DELTAS = ["1/20", "1/10", "3/20", "1/5", "1/4", "3/10"]          # 0,05 … 0,30
P_HIST = [["1/4", "3/5", "3/20"], ["3/20", "3/5", "1/4"]]          # 0,25/0,60/0,15 y espejo


def p_simetrica(delta):
    d = Fraction(delta)
    return [str(d), str(1 - 2 * d), str(d)]


def main():
    with open(os.path.join(AQUI, "..", "casos_fijados.json"), encoding="utf-8") as f:
        casos = json.load(f)
    sel = {c["id"]: c for g in ("anexo_c", "historicos") for c in casos[g]}
    filas = []
    for cid in ("A1", "H1", "H2"):
        c = sel[cid]
        V, vn, precio = c["V"], c.get("v_normal"), c.get("precio")
        p_grid = [(f"simetrica d={d}", p_simetrica(d)) for d in DELTAS]
        p_grid += [(f"historico {p}", p) for p in P_HIST]
        for k in K_GRID:
            for etiqueta_p, p in p_grid:
                r = O.resumen_caso(V, p, k, v_normal=vn, precio=precio)
                filas.append({
                    "caso": cid, "V": ";".join(V), "v_normal": vn, "precio": precio,
                    "k": k, "p": ";".join(p), "p_grid": etiqueta_p,
                    "P_estrella": r["P_estrella_trazos"], "P_estrella_float": f"{r['P_estrella_trazos_float']:.6f}",
                    "G_en_P": f"{float(Fraction(r['G_en_P'])):.6f}", "L_en_P": f"{float(Fraction(r['L_en_P'])):.6f}",
                    "residuo_F": r["residuo_F_trazos"],
                    "precio_si": f"{r['precio_si_float']:.6f}",
                    "tope_normal_aplicado": r["tope_normal_aplicado"],
                    "ponderado": f"{r['ponderado_float']:.6f}", "zona": r.get("zona", ""),
                    "hipotesis": "rejilla anunciada en INVENTARIO_Y_PLAN.md §4; V y precio fijos del caso; sin distribuciones nuevas",
                })
    destino = os.path.join(AQUI, "..", "SENSIBILIDAD_FINITA.csv")
    with open(destino, "w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(filas[0].keys()))
        w.writeheader()
        w.writerows(filas)
    # resumen por caso: rango de precio_si en la rejilla
    resumen = {}
    for cid in ("A1", "H1", "H2"):
        vals = [float(f["precio_si"]) for f in filas if f["caso"] == cid]
        resumen[cid] = {"min": min(vals), "max": max(vals), "n": len(vals)}
    print(json.dumps({"filas": len(filas), "rango_precio_si_por_caso": resumen,
                      "destino": os.path.normpath(destino)}, ensure_ascii=False, indent=1))


if __name__ == "__main__":
    main()
