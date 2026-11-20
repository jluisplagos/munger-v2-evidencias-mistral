#!/usr/bin/env python3
"""Revisión R2 · F1 US GAAP · declaraciones Y archivos fase1_partes mal formados al azar (con las ayudas de la ronda 2 y sus claves nuevas):
evaluar() no debe lanzar excepciones distintas de ErrorDeclaracion, ni dar «utilizable» sin condición con una carpeta fase1_partes estropeada.
Uso: python3 -B fuzz_r2.py [N] [semilla]"""
import collections
import copy
import json
import os
import random
import shutil
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import ayudas2  # noqa: E402

A = ayudas2.cargar()
M, libro, decl, serie, expediente = A["M"], A["libro"], A["decl"], A["serie"], A["expediente"]
N = int(sys.argv[1]) if len(sys.argv) > 1 else 3000
rnd = random.Random(int(sys.argv[2]) if len(sys.argv) > 2 else 8422)
RAROS = [None, "", 0, 1, -1, 1.5, True, False, [], {}, "fila_8", "fila_14", "no_publicada", "fuera_de_las_filas_8_y_14", "fuera_de_la_fila_8", "publicado", "no_publicado", "x",
         {"ubicacion": "fila_14"}, [1, 2], "2025", {"valor": 3}, "Operating lease liabilities", 2, "2"]
CLAVES = ["ubicacion", "existen", "pagina", "cita", "2025", "valor_fuente", "signo", "literal", "fila", "operativos", "financieros", "registro", "desglose", "amortizacion_rou",
          "variacion_pasivo", "coste_comparable_con_los_pagos", "coste_no_comparable_motivo", "documento", "anio", "archivo", "partidas", "da", "circulante_lineas", "cfo",
          "arrendamientos", "actual", "anterior", "cero", "concepto", "impreso", "linea", "componentes"]


def mutar(x, prob):
    if isinstance(x, dict):
        out = {}
        for k, v in x.items():
            r = rnd.random()
            if r < prob * 0.4:
                continue
            out[k] = rnd.choice(RAROS) if r < prob else mutar(v, prob)
        if rnd.random() < prob * 0.3:
            out[rnd.choice(CLAVES)] = rnd.choice(RAROS)
        return out
    if isinstance(x, list):
        out = [rnd.choice(RAROS) if rnd.random() < prob else mutar(v, prob) for v in x if rnd.random() > prob * 0.3]
        return out
    return x


exc, n_util, n_util_sin_cond, estados = collections.Counter(), 0, 0, collections.Counter()
tmp = []
try:
    for i in range(N):
        fin = rnd.choice([True, False])
        base = decl(rnd.choice(["A0_total", "A2_propio", "A1_sin_ROU"]), fin=fin, ub_am=rnd.choice(["fila_8", "fila_14", "fuera_de_las_filas_8_y_14", "no_publicada"]),
                    ub_pas=rnd.choice(["fila_14", "fuera_de_las_filas_8_y_14", "no_publicada"]), a8=rnd.choice([None, 10]), ajuste=rnd.choice([None, 10, -10, 0]),
                    rou_fin=rnd.choice([None, 5]), fin_princ=rnd.choice([None, 5]), pasivo=rnd.choice([None, 0, 50]))
        b = base["arrendamientos_us_gaap"]
        if rnd.random() < 0.3:
            b["operativos"]["coste_comparable_con_los_pagos"] = rnd.choice([True, False, "no"])
            b["operativos"]["coste_no_comparable_motivo"] = rnd.choice([None, "incluye corto plazo"])
        if fin and rnd.random() < 0.4:
            b["financieros"]["desglose"] = rnd.choice(["publicado", "no_publicado", "x"])
            base["series"]["caja_pagada_arr_financiero"] = serie(6)
            base["series"]["gasto_arr_financiero"] = serie(5)
        if fin and rnd.random() < 0.3:
            b["financieros"]["amortizacion_rou"] = {"ubicacion": rnd.choice(["fila_8", "fuera_de_la_fila_8"]), "documento": A["DOC"], "pagina": 2, "cita": "Amortization of finance lease right-of-use assets"}
            base["series"]["da_rou_financiero_fuera"] = serie(1)
        verdad = (rnd.choice(["fuera", "fila_8", "fila_14", "no"]), rnd.choice(["fuera", "fila_14", "no"]))
        modo = rnd.choice(["decl", "partes", "ambos", "partes"])
        c = None
        try:
            c = expediente(copy.deepcopy(base) if modo != "partes" else base, verdad=verdad, partes=True)
            tmp.append(c)
        except Exception:  # noqa: BLE001
            c = None
        d = base
        if modo in ("decl", "ambos"):
            fs = base.get("fuentes_series")
            d = mutar(base, prob=rnd.choice([0.03, 0.1, 0.25]))
            if c is not None and "fuentes_series" not in d and rnd.random() < 0.7:
                d["fuentes_series"] = json.load(open(os.path.join(c, "x.json"))) if False else (fs or {})
            if c is not None and not d.get("fuentes_series"):
                # la huella registrada es la del expediente escrito: se recupera de un expediente gemelo
                pass
        roto = False
        if c is not None and modo in ("partes", "ambos"):
            dp = os.path.join(c, "fase1_partes")
            for n_ in sorted(os.listdir(dp)):
                if rnd.random() < 0.6:
                    j = json.load(open(os.path.join(dp, n_), encoding="utf-8"))
                    r_ = rnd.random()
                    if r_ < 0.1:
                        open(os.path.join(dp, n_), "w", encoding="utf-8").write(rnd.choice(["", "{", "[]", "null", "\"x\"", "3"]))
                    else:
                        json.dump(mutar(j, prob=rnd.choice([0.05, 0.15, 0.3])), open(os.path.join(dp, n_), "w", encoding="utf-8"), ensure_ascii=False)
                    roto = True
            if rnd.random() < 0.1:
                json.dump(rnd.choice([{"da": {"2024": 1}}, {"circulante_lineas": {"2025": 3, "2023": 1}}, [], "x", {"da": 3}]), open(os.path.join(c, "fase1_decisiones.json"), "w"))
        L = libro(da=rnd.choice([20.0, 25.0, 30.0]), dwc=rnd.choice([0.0, 10.0, -10.0]), C49=rnd.choice([0.0, 5.0]), princ=rnd.choice([0.0, 5.0]), fila23=rnd.choice([0.0, 50.0]),
                  motor=rnd.choice(["A", "A", "B"]), l4=rnd.choice(["US GAAP", "US GAAP", "IFRS", "Otro", ""]))
        try:
            r = M.evaluar(L, d, carpeta=c)
            json.dumps(r, default=str)
            M.informe_md(r) if r.get("aplica") else None
            if r.get("utilizable_para_conclusion"):
                n_util += 1
                if not r.get("condicionada"):
                    n_util_sin_cond += 1
                    tr = (((r.get("us_gaap") or {}).get("contraste_de_ubicaciones") or {}).get("tramos") or {})
                    estados["/".join(sorted({str(v.get("estado")) for v in tr.values()})) or "(sin tramos)"] += 1
        except M.ErrorDeclaracion:
            exc["ErrorDeclaracion (controlada)"] += 1
        except Exception as ex:  # noqa: BLE001
            import traceback
            tb = traceback.extract_tb(ex.__traceback__)[-1]
            exc[f"{type(ex).__name__}: {str(ex)[:70]} @ {os.path.basename(tb.filename)}:{tb.lineno} {tb.name} · {str(tb.line)[:110]}"] += 1
        if len(tmp) > 150:
            for t in tmp:
                shutil.rmtree(t, ignore_errors=True)
            tmp = []
finally:
    for t in tmp:
        shutil.rmtree(t, ignore_errors=True)
print(f"{N} casos (declaraciones y fase1_partes mal formados) · utilizables: {n_util} · de ellos sin condición: {n_util_sin_cond} · estados del contraste en los utilizables sin condición: {dict(estados)}")
for k, v in exc.most_common():
    print(f"  excepción · {v} veces · {k}")
