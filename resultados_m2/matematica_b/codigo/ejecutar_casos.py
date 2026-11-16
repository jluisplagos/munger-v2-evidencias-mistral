#!/usr/bin/env python3
"""Ejecuta los 56 casos fijados con el oráculo propio (ambas soluciones) y la batería de
propiedades ejecutables (T1–T12) sobre cada caso. Escribe `../resultados_casos.json`.

No usa el código del producto: los valores esperados son solo del oráculo propio.
Uso: python3 ejecutar_casos.py
"""
import json
import os
import random
import sys
from fractions import Fraction

AQUI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, AQUI)
import oraculo_precio_si as O

K_GRID = ["1", "3/2", "2", "5/2", "3", "4", "5", "10"]


def propiedades(V, p, k, vn, precio):
    """Batería ejecutable de propiedades sobre un caso. Devuelve dict de resultados."""
    out = {}
    Vf, pf, kf = O.validar(V, p, k)
    Ps = O.p_estrella_trazos(Vf, pf, kf)
    pond = O.ponderado(Vf, pf)
    out["residuo_F_exacto_cero"] = (O.F(Vf, pf, kf, Ps) == 0)
    out["P_en_[minV_maxV]"] = (min(Vf) <= Ps <= max(Vf))
    if kf >= 1:
        out["P_le_ponderado_k_ge_1"] = (Ps <= pond)
    out["k1_da_ponderado"] = (O.p_estrella_trazos(Vf, pf, Fraction(1)) == pond)
    rng = random.Random(1234)
    ok_perm = True
    for _ in range(5):
        idx = list(range(len(Vf)))
        rng.shuffle(idx)
        if O.p_estrella_trazos([Vf[i] for i in idx], [pf[i] for i in idx], kf) != Ps:
            ok_perm = False
    out["invariante_permutacion"] = ok_perm
    out["traslacion_+7"] = (O.p_estrella_trazos([v + 7 for v in Vf], pf, kf) == Ps + 7)
    out["escala_x2"] = (O.p_estrella_trazos([2 * v for v in Vf], pf, kf) == 2 * Ps)
    grid = [O.p_estrella_trazos(Vf, pf, Fraction(x)) for x in K_GRID]
    out["monotona_decreciente_en_k"] = all(grid[i + 1] <= grid[i] for i in range(len(grid) - 1))
    Pb, res = O.p_estrella_biseccion(Vf, pf, kf)
    out["biseccion_coincide_1e-9"] = abs(float(Ps) - Pb) <= 1e-9
    out["residuo_biseccion"] = res
    if vn is not None and precio is not None:
        psi, _ = O.precio_de_si(Vf, pf, kf, Fraction(str(vn)))
        malo = O.precio_escenario_malo(Vf)
        out["zona"] = O.zona(Fraction(str(precio)), malo, psi, pond)
        out["precio_si_en_[minV_vN]"] = (min(Vf) <= psi <= Fraction(str(vn)))
    return out


def main():
    with open(os.path.join(AQUI, "..", "casos_fijados.json"), encoding="utf-8") as f:
        casos = json.load(f)
    filas = []
    n_error_dominio = 0
    for grupo in ("anexo_c", "sinteticos", "historicos"):
        for c in casos[grupo]:
            fila = {"grupo": grupo, "id": c["id"], "V": c["V"], "p": c["p"], "k": c["k"]}
            if c.get("espera_dominio_error"):
                try:
                    O.p_estrella_trazos(c["V"], c["p"], c["k"])
                    fila["error"] = "NO se lanzó DominioError (inesperado)"
                except O.DominioError as e:
                    fila["dominio_error"] = str(e)
                    n_error_dominio += 1
            else:
                r = O.resumen_caso(c["V"], c["p"], c["k"], v_normal=c.get("v_normal"), precio=c.get("precio"))
                fila.update(r)
                fila["propiedades"] = propiedades(c["V"], c["p"], c["k"], c.get("v_normal"), c.get("precio"))
                fila["guardas_producto"] = O.guardas_producto(c["V"], c["p"], c["k"], c.get("precio"))
                if c.get("precio_si_publicado") is not None:
                    fila["precio_si_publicado_paquete"] = c["precio_si_publicado"]
                    fila["residuo_vs_publicado"] = abs(r["precio_si_float"] - float(c["precio_si_publicado"]))
                if c.get("P_estrella_publicado") is not None:
                    fila["P_estrella_publicado_paquete"] = c["P_estrella_publicado"]
                    fila["residuo_P_vs_publicado"] = abs(r["P_estrella_trazos_float"] - float(c["P_estrella_publicado"]))
            filas.append(fila)
    for g in casos["variantes"]:
        for v in g["filas"]:
            if not v.get("V") or not v.get("p"):
                continue
            V = [repr(x) for x in v["V"]]
            p = [repr(x) for x in v["p"]]
            k = repr(v["k"] if v["k"] is not None else g["k"])
            vn = repr(v["V"][1])
            fila = {"grupo": g["grupo"], "id": v["clave"], "V": V, "p": p, "k": k}
            r = O.resumen_caso(V, p, k, v_normal=vn, precio=repr(g["precio"]) if g.get("precio") else None)
            fila.update(r)
            fila["precio_si_publicado_paquete"] = v.get("precio_si_publicado")
            if v.get("precio_si_publicado") is not None:
                fila["residuo_vs_publicado"] = abs(r["precio_si_float"] - float(v["precio_si_publicado"]))
            fila["zona_publicada"] = v.get("zona_publicada")
            filas.append(fila)
    # resumen de propiedades
    checks = {}
    for f in filas:
        pr = f.get("propiedades")
        if not pr:
            continue
        for k2, val in pr.items():
            if isinstance(val, bool):
                checks.setdefault(k2, True)
                checks[k2] = checks[k2] and val
    destino = os.path.join(AQUI, "..", "resultados_casos.json")
    with open(destino, "w", encoding="utf-8") as f:
        json.dump({"n_casos": len(filas), "n_dominio_error_esperados": n_error_dominio,
                   "propiedades_globales": {k: bool(v) for k, v in checks.items()}, "filas": filas},
                  f, ensure_ascii=False, indent=1)
    max_res_pub = max((f.get("residuo_vs_publicado") or 0) for f in filas)
    max_res_Ppub = max((f.get("residuo_P_vs_publicado") or 0) for f in filas)
    print(json.dumps({"n_casos": len(filas), "dominio_error_esperados": n_error_dominio,
                      "propiedades_globales": {k: bool(v) for k, v in checks.items()},
                      "max_residuo_precio_si_vs_publicado_paquete": max_res_pub,
                      "max_residuo_P_vs_publicado_paquete": max_res_Ppub,
                      "destino": os.path.normpath(destino)}, ensure_ascii=False, indent=1))
    return 0 if all(checks.values()) else 1


if __name__ == "__main__":
    sys.exit(main())
