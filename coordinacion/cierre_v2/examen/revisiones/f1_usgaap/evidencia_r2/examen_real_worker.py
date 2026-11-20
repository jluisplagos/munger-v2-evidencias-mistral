#!/usr/bin/env python3
"""Revisión R2 · diferencial NIIF con DATOS REALES: cada expediente del examen que tiene declaración F1 (motor_a_f1.json) y un libro recalculado se evalúa
con el motor_a_f1.py de la carpeta que se pasa (solo lectura), y se vuelca el resultado sin versión ni fecha. Uso: … CARPETA_SCRIPTS SALIDA.json"""
import json
import os
import sys

sys.dont_write_bytecode = True
sys.path.insert(0, sys.argv[1])
import motor_a_f1 as M  # noqa: E402

RAIZ = "/home/user/e_work/wt_examen/munger_v2_r1/personaje_v2/empresas_v2_correcciones/2026-11_examen_universo"
out = {}
for caso in sorted(os.listdir(RAIZ)):
    for emp in sorted(os.listdir(os.path.join(RAIZ, caso))) if os.path.isdir(os.path.join(RAIZ, caso)) else []:
        c = os.path.join(RAIZ, caso, emp)
        dp = os.path.join(c, "motor_a_f1.json")
        if not os.path.isfile(dp):
            continue
        libros = [os.path.join(c, "recalc", f"{emp}_v63_evaluada.xlsx"), os.path.join(c, "recalc", f"{emp}_v63_datos.xlsx")]
        libro = next((x for x in libros if os.path.isfile(x)), None)
        if not libro:
            out[f"{caso}/{emp}"] = {"sin_libro": True}
            continue
        try:
            d = json.load(open(dp, encoding="utf-8"))
            r = M.evaluar(M.leer_libro(libro), d, carpeta=c, motor_libro="A")
            for k in ("version", "fecha"):
                r.pop(k, None)
            out[f"{caso}/{emp}"] = {"libro": os.path.basename(libro), "norma": M._valor(d, "norma_contable")[0], "resultado": json.loads(json.dumps(r, default=str))}
        except Exception as ex:  # noqa: BLE001
            out[f"{caso}/{emp}"] = {"excepcion": f"{type(ex).__name__}: {str(ex)[:200]}"}
json.dump(out, open(sys.argv[2], "w", encoding="utf-8"), ensure_ascii=False, indent=0, sort_keys=True)
print(len(out), "expedientes del examen con declaración F1")
