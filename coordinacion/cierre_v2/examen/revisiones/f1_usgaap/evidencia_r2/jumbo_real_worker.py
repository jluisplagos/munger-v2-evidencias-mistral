#!/usr/bin/env python3
"""Revisión R2 · declaración F1 REAL de Jumbo (examen, jumbo_d; NIIF) evaluada con el motor_a_f1.py de la carpeta que se pasa (solo lectura del expediente).
Uso: python3 -B jumbo_real_worker.py CARPETA_SCRIPTS ETIQUETA"""
import json
import os
import sys

sys.dont_write_bytecode = True
sys.path.insert(0, sys.argv[1])
import motor_a_f1 as M  # noqa: E402

J = "/home/user/e_work/wt_examen/munger_v2_r1/personaje_v2/empresas_v2_correcciones/2026-11_examen_universo/jumbo_d/Jumbo"
d = json.load(open(os.path.join(J, "motor_a_f1.json"), encoding="utf-8"))
L = M.leer_libro(os.path.join(J, "recalc", "Jumbo_v63_datos.xlsx"))
r = M.evaluar(L, d, carpeta=J, motor_libro="A")
bl = [(g["id"], g.get("efecto")) for g in r["guardas"] if g["salta"] and g["severidad"] == "BLOQUEA"]
print(f"{sys.argv[2]:22} utilizable {r.get('utilizable_para_conclusion')} · estado {r.get('estado_propuesto')} · bloquean {sorted(set(bl))}")
for g in r["guardas"]:
    if g["id"] in ("F1-DECLARACION",) and g["salta"]:
        print("     F1-DECLARACION:", str(g["detalle"])[:260])
if len(sys.argv) > 3:
    d2 = json.loads(json.dumps(d))
    d2["series"].pop("pagos_arrendamiento_sin_declarar", None)
    r2 = M.evaluar(L, d2, carpeta=J, motor_libro="A")
    print(f"{'  · sin esa clave':22} utilizable {r2.get('utilizable_para_conclusion')} · estado {r2.get('estado_propuesto')} · bloquean {sorted({(g['id'], g.get('efecto')) for g in r2['guardas'] if g['salta'] and g['severidad'] == 'BLOQUEA'})}")
