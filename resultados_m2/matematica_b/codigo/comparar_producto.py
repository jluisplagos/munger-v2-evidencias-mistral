#!/usr/bin/env python3
"""Comparación con el producto, DESPUÉS de derivar y fijar los casos (encargo frente C).

El esperado de cada fila es SIEMPRE el oráculo propio (`oraculo_precio_si`). El producto
(`personaje_v2/scripts/precio_de_si.py`, leído de `.trabajo/insumos_m2/` en solo lectura,
sin modificarlo ni ejecutarlo como pipeline) solo rellena las columnas `*_producto`.

Escribe `../COMPARACION_IMPLEMENTACION.csv` con: esperado (traza exacta + bisección),
residuos, obtenido del producto (p_estrella y, con n=3 ordenado, calcular() completo),
residuo oráculo-vs-producto, y la versión exacta comparada (sha256 del archivo + commit).

Uso: python3 comparar_producto.py
"""
import csv
import hashlib
import importlib.util
import json
import os
import sys

AQUI = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.abspath(os.path.join(AQUI, "..", "..", ".."))
sys.path.insert(0, AQUI)
import oraculo_precio_si as O

PRODUCTO_REL = "personaje_v2/scripts/precio_de_si.py"
PRODUCTO = os.path.join(REPO, ".trabajo", "insumos_m2", PRODUCTO_REL)
COMMIT = "059f4f68dca7acf465b5f5b21de2dede84c885ff"

# Valores publicados en la tabla del Anexo C §C.5 (documento, no código) para contraste.
ANEXO_PUB = {"A1": (265 / 3, 265 / 3), "A2": (1330 / 13, 100.0), "A3": (100.0, 100.0),
             "A4": (380 / 7, 380 / 7), "A5": (1005 / 13, 70.0)}


def cargar_producto():
    with open(PRODUCTO, "rb") as f:
        sha = hashlib.sha256(f.read()).hexdigest()
    spec = importlib.util.spec_from_file_location("precio_de_si_producto", PRODUCTO)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod, sha


def producto_p_estrella(mod, V, p, k):
    try:
        return mod.p_estrella(list(V), list(p), float(k)), None
    except Exception as e:  # el producto puede negarse o fallar (n ≠ 3, k < 1...)
        return None, f"{type(e).__name__}: {e}"


def producto_calcular(mod, V, p, k, precio):
    """calcular() del producto con un resultados.json mínimo (solo lectura del módulo)."""
    if len(V) != 3:
        return None, "n ≠ 3: calcular() del producto exige 3 escenarios"
    res = {"valores": {"B78": float(V[0]), "C78": float(V[1]), "D78": float(V[2]),
                       "C37": float(precio), "C83": sum(float(v) * float(q) for v, q in zip(V, p))},
           "probabilidades": [float(x) for x in p],
           "estados": {"estado_tecnico_B255": "COMPLETO Y VÁLIDO", "bloqueo_valor_B252": False,
                       "comparable_B253": True}}
    try:
        out, code = mod.calcular(res, k=float(k))
        return out, f"code={code}"
    except Exception as e:
        return None, f"{type(e).__name__}: {e}"


def main():
    with open(os.path.join(AQUI, "..", "casos_fijados.json"), encoding="utf-8") as f:
        casos = json.load(f)
    mod, sha = cargar_producto()
    filas = []

    def fila_base(grupo, c):
        from fractions import Fraction
        V = [float(Fraction(x)) for x in c["V"]]
        p = [float(Fraction(x)) for x in c["p"]]
        k = float(Fraction(str(c["k"])))
        r = O.resumen_caso(c["V"], c["p"], c["k"], v_normal=c.get("v_normal"), precio=c.get("precio"))
        Pp, err_p = producto_p_estrella(mod, V, p, k)
        calc, err_c = (None, None)
        if c.get("precio") is not None:
            calc, err_c = producto_calcular(mod, V, p, k, float(c["precio"]))
        fila = {
            "grupo": grupo, "caso": c["id"], "V": c["V"], "p": c["p"], "k": c["k"],
            "v_normal": c.get("v_normal"), "precio": c.get("precio"),
            "P_estrella_esperado_trazos_exacto": r["P_estrella_trazos"],
            "P_estrella_esperado_float": f"{r['P_estrella_trazos_float']:.12f}",
            "P_estrella_biseccion": f"{r['P_estrella_biseccion']:.12f}",
            "residuo_F_trazos": r["residuo_F_trazos"], "residuo_F_biseccion": f"{r['residuo_F_biseccion']:.3e}",
            "ponderado": f"{r['ponderado_float']:.12f}",
            "precio_si_oraculo": f"{r['precio_si_float']:.12f}",
            "zona_oraculo": r.get("zona", ""),
            "P_estrella_producto": (f"{Pp:.12f}" if Pp is not None else ""),
            "error_p_estrella_producto": err_p or "",
            "residuo_oraculo_vs_producto": (f"{abs(r['P_estrella_trazos_float'] - Pp):.3e}" if Pp is not None else ""),
            "precio_si_producto": (f"{calc['precio_si']:.12f}" if calc and "precio_si" in calc else ""),
            "zona_producto": (calc.get("zona", "") if calc else ""),
            "salida_calcular_producto": ("sin_lectura: " + calc["sin_lectura"] if calc and "sin_lectura" in calc
                                         else ("sin_escalera G19" if calc and "sin_escalera" in calc
                                               else (err_c or ""))),
            "precio_si_publicado_paquete": c.get("precio_si_publicado", ""),
            "P_estrella_publicado_anexo": (f"{ANEXO_PUB[c['id']][0]:.6f}" if c["id"] in ANEXO_PUB else ""),
            "precio_si_publicado_anexo": (f"{ANEXO_PUB[c['id']][1]:.6f}" if c["id"] in ANEXO_PUB else ""),
            "version_producto_sha256": sha, "commit_producto": COMMIT,
            "nota": c.get("nota", ""),
        }
        return fila

    for grupo in ("anexo_c", "sinteticos", "historicos"):
        for c in casos[grupo]:
            if c.get("espera_dominio_error"):
                try:
                    O.p_estrella_trazos(c["V"], c["p"], c["k"])
                except O.DominioError as e:
                    from fractions import Fraction
                    Vf2 = [float(Fraction(x)) for x in c["V"]]
                    pf2 = [float(Fraction(x)) for x in c["p"]]
                    kf2 = float(Fraction(str(c["k"])))
                    Pp, err_p = producto_p_estrella(mod, Vf2, pf2, kf2)
                    calc, err_c = producto_calcular(mod, Vf2, pf2, kf2, float(Fraction(str(c["precio"]))))
                    filas.append({"grupo": grupo, "caso": c["id"], "V": c["V"], "p": c["p"], "k": c["k"],
                                  "dominio_error_oraculo": str(e),
                                  "P_estrella_producto": (f"{Pp:.12f}" if Pp is not None else ""),
                                  "salida_calcular_producto": ("sin_lectura: " + calc["sin_lectura"] if calc and "sin_lectura" in calc else (err_c or "")),
                                  "version_producto_sha256": sha, "commit_producto": COMMIT, "nota": c.get("nota", "")})
                continue
            filas.append(fila_base(grupo, c))
    for g in casos["variantes"]:
        for v in g["filas"]:
            if not v.get("V") or not v.get("p"):
                continue
            c = {"id": v["clave"], "V": [repr(x) for x in v["V"]], "p": [repr(x) for x in v["p"]],
                 "k": repr(v["k"] if v["k"] is not None else g["k"]), "v_normal": repr(v["V"][1]),
                 "precio": repr(g["precio"]) if g.get("precio") else None,
                 "precio_si_publicado": v.get("precio_si_publicado"), "nota": f"variante {g['grupo']} · varía {v.get('parametros_variados')}"}
            filas.append(fila_base(g["grupo"], c))

    destino = os.path.join(AQUI, "..", "COMPARACION_IMPLEMENTACION.csv")
    campos = list(filas[0].keys())
    for f in filas:
        for k in f:
            if k not in campos:
                campos.append(k)
    with open(destino, "w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=campos, extrasaction="ignore")
        w.writeheader()
        w.writerows(filas)
    max_res = max((float(f["residuo_oraculo_vs_producto"]) for f in filas if f.get("residuo_oraculo_vs_producto")), default=None)
    print(json.dumps({"filas": len(filas), "version_producto_sha256": sha,
                      "max_residuo_oraculo_vs_producto": max_res,
                      "destino": os.path.normpath(destino)}, ensure_ascii=False, indent=1))


if __name__ == "__main__":
    main()
