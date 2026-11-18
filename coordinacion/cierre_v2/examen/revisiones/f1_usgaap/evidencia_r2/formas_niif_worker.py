#!/usr/bin/env python3
"""Revisión R2 · diferencial NIIF de FORMAS: una declaración NIIF válida y utilizable, y la misma con cada clave de primer nivel (y cada clave de
«series» y de «transicion») sustituida por None, {}, [], "" o 0, o eliminada. Se evalúa con el motor_a_f1.py de la carpeta que se pasa y se vuelca
utilizable/bloquean/excepción. Sirve para ver si la normalización de la ronda 2 (R1-14, _declaracion_bien_formada) cambia algún resultado NIIF.
Uso: python3 -B formas_niif_worker.py CARPETA_SCRIPTS CABECERA_PRUEBAS.py SALIDA.json"""
import copy
import json
import os
import sys
import tempfile

SCRIPTS, CAB, SALIDA = sys.argv[1:4]
sys.dont_write_bytecode = True
sys.path.insert(0, SCRIPTS)
tempfile.tempdir = os.environ.get("TMP_R2") or tempfile.gettempdir()
src = open(CAB, encoding="utf-8").read()
corte = src.index("# ================================================================== N ·")
ns = {"__name__": "cab", "__file__": CAB}
exec(compile(src[:corte].replace("AQUI = os.path.dirname(os.path.abspath(__file__))", f"AQUI = {os.path.dirname(CAB)!r}").replace(
    'sys.path.insert(0, os.path.join(PV, "scripts"))', "pass"), CAB, "exec"), ns)
M, libro, decl, fuentes = ns["M"], ns["libro"], ns["decl"], ns["fuentes"]
assert os.path.dirname(os.path.abspath(M.__file__)) == os.path.abspath(SCRIPTS), M.__file__
L = libro(l4="IFRS (adoptadas por la Unión Europea)")
base = decl(norma="NIIF", us=False, ppa=0)
base["series"]["da_rou"] = ns["serie"](0)
VALS = [("None", None), ("{}", {}), ("[]", []), ("''", ""), ("0", 0), ("'x'", "x")]
casos = [("base", base)]
for k in list(base) + ["normalizacion", "conciliacion_fcf_base", "terminos_explicitos", "fuentes_series", "umbral_v_f1a", "nota", "formato", "arrendamientos_us_gaap"]:
    for n, v in VALS:
        d = copy.deepcopy(base)
        d[k] = v
        casos.append((f"{k} = {n}", d))
    if k in base:
        d = copy.deepcopy(base)
        del d[k]
        casos.append((f"sin {k}", d))
for k in list(base["series"]):
    for n, v in VALS:
        d = copy.deepcopy(base)
        d["series"][k] = v
        casos.append((f"series.{k} = {n}", d))
for k in list(base["transicion"]):
    for n, v in VALS:
        d = copy.deepcopy(base)
        d["transicion"][k] = v
        casos.append((f"transicion.{k} = {n}", d))
c0 = fuentes(base)   # la fuente registrada (con su huella) de la declaración base; las variantes la conservan salvo que quiten «fuentes_series»
FS0 = copy.deepcopy(base["fuentes_series"])
out = []
for nombre, d in casos:
    dd = copy.deepcopy(d)
    if "fuentes_series" not in dd and not nombre.startswith(("fuentes_series", "sin fuentes_series")):
        dd["fuentes_series"] = copy.deepcopy(FS0)
    try:
        r = M.evaluar(L, dd, carpeta=c0)
        res = {"utilizable": r.get("utilizable_para_conclusion"), "estado": r.get("estado_propuesto"),
               "bloquean": sorted({g["id"] for g in r.get("guardas") or [] if g.get("salta") and g.get("severidad") == "BLOQUEA"})}
    except M.ErrorDeclaracion as ex:
        res = {"ErrorDeclaracion": str(ex)[:120]}
    except Exception as ex:  # noqa: BLE001
        res = {"excepcion": f"{type(ex).__name__}: {str(ex)[:120]}"}
    out.append({"caso": nombre, "res": res})
json.dump(out, open(SALIDA, "w", encoding="utf-8"), ensure_ascii=False, indent=0)
print(len(out), "formas evaluadas con", SCRIPTS)
