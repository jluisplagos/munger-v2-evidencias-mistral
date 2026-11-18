#!/usr/bin/env python3
"""Revisión R2 (revisor) · el expediente REAL de Zoetis del examen si la fase A eligiera el MOTOR B (el coordinador lo anota como posible):
qué dice F1 del puente de deuda con la fila 23 real (248 de pasivo por arrendamiento operativo en 2025). Solo lectura del expediente.
Uso: python3 -B zoetis_real_motor_b_r2.py [SALIDA.txt]"""
import copy
import importlib.util
import os
import shutil
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
spec = importlib.util.spec_from_file_location("zr", os.path.join(os.path.dirname(os.path.abspath(__file__)), "zoetis_real_r2.py"))
zr = importlib.util.module_from_spec(spec)
spec.loader.exec_module(zr)
M, SAL = zr.M, []


def p(*a):
    t = " ".join(str(x) for x in a)
    SAL.append(t)
    print(t, flush=True)


def caso(nombre, L, d, c):
    r = M.evaluar(L, d, carpeta=c, motor_libro="B")
    bl = [(g["id"], g.get("efecto")) for g in r["guardas"] if g["salta"] and g["severidad"] == "BLOQUEA"]
    p(f"\n== {nombre}")
    p(f"   utilizable: {r.get('utilizable_para_conclusion')} · estado propuesto: {r.get('estado_propuesto')} · bloquean: {bl}")
    p(f"   rótulo: {str(r.get('rotulo'))[:200]}")
    pu = (r.get("us_gaap") or {}).get("puente_de_deuda") or {}
    p(f"   puente: fila 22 = {pu.get('deuda_financiera_fila_22')} · fila 23 = {pu.get('pasivo_por_arrendamientos_fila_23')} · pasivo operativo dentro = {pu.get('pasivo_operativo_dentro_de_la_fila_23')} · "
      f"C64 del libro = {pu.get('deuda_del_puente_del_libro_C64')} · deuda coherente = {pu.get('deuda_del_puente_coherente')}")
    p(f"   líneas de arrendamiento operativo sumadas en la fila 23 (fase 1 real): {pu.get('lineas_de_arrendamiento_operativo_sumadas_en_la_fila_23')}")
    for gid in ("F1-US-PUENTE", "F1-US-ANCLA", "F1-SERIES", "F1-US-DESGLOSE", "F1-NORMA"):
        for g in r["guardas"]:
            if g["id"] == gid and g["salta"]:
                p(f"   {gid} · {g['severidad']} · {g.get('efecto')} · {str(g['detalle'])[:420]}")


L = M.leer_libro(os.path.join(zr.Z, "recalc", "Zoetis_v63_datos.xlsx"))
c = zr.carpeta()
try:
    caso("ZB1 · motor B, libro real tal cual (fila 23 = 248) y pasivo operativo declarado 248 (nota, página 89)", L, zr.declaracion(), c)
    d2 = zr.declaracion()
    d2["series"]["pasivo_arr_operativo"]["2025"].update({"valor_fuente": 0, "literal": "—"})
    caso("ZB2 · motor B, mismo libro, declarando que la fila 23 no lleva pasivo operativo (0)", L, d2, c)
    caso("ZB3 · motor B y SIN declaración F1", L, {}, c)
finally:
    shutil.rmtree(os.path.dirname(c), ignore_errors=True)
if len(sys.argv) > 1:
    open(sys.argv[1], "w", encoding="utf-8").write("\n".join(SAL) + "\n")
