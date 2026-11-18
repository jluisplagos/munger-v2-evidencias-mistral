#!/usr/bin/env python3
"""Segunda ronda · repetición de la sonda PC (declaración que cambia entre el paso 7 y el 12) sobre el código nuevo, y variantes con el estado
reiniciado. Empresa sintética SIN arrendamientos, expediente de la 4.15, declaración A0 completa (con la conciliación que pide K3a).
LibreOffice: ejecutar con flock. Uso (desde personaje_v2/ de la copia NUEVA): r2_pc_replay.py DIR SALIDA.json"""
import importlib.util, json, os, shutil, subprocess, sys
PV = os.getcwd()
sys.path.insert(0, os.path.join(PV, "pruebas")); sys.path.insert(0, os.path.join(PV, "scripts")); sys.dont_write_bytecode = True
spec = importlib.util.spec_from_file_location("PP", os.path.join(PV, "empresas_v2_correcciones", "2026-11_Vidrala_ensayo_4_15", "f1_impl", "scripts", "prueba_pipeline_f1.py"))
PP = importlib.util.module_from_spec(spec); spec.loader.exec_module(PP)
TS = PP.TS
import motor_a_f1 as F1
TS.BASE = os.path.abspath(sys.argv[1]); os.makedirs(TS.BASE, exist_ok=True)
SAL = {}
normal = TS.reaccion_normal()
cambiada = {"x": False}
def bloqueante():
    d = PP.declaracion()
    for k in ("perimetro_reinversion", "perimetro_palancas_s2c", "perimetro_roic"):
        d[k]["valor"] = "A2_propio"
    return d
def reac(c, nombre):
    if nombre == "fase_c_turno1" and not cambiada["x"]:
        json.dump(bloqueante(), open(os.path.join(c, "motor_a_f1.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1); cambiada["x"] = True
        print("   [sonda] la declaración pasa a A2_propio mientras se espera a la fase C")
    normal(c, nombre)
def lanzar(c, *extra, max_vueltas=40):
    args = list(extra); log = []
    for _ in range(max_vueltas):
        r = subprocess.run([TS.PY, TS.PIPE, c] + args, capture_output=True, text=True); args = []
        log.append((r.stdout + r.stderr).strip().splitlines()[-1][:260] if (r.stdout + r.stderr).strip() else "")
        if r.returncode != 10:
            return r.returncode, log
        reac(c, open(os.path.join(c, "ESPERANDO.md"), encoding="utf-8").read().split("**")[1])
    return 10, log + ["demasiadas vueltas"]
def foto(c, etiqueta, rc, log):
    st = TS.estado(c)
    fi = json.load(open(os.path.join(c, "ficha.json"), encoding="utf-8")) if os.path.exists(os.path.join(c, "ficha.json")) else None
    d = {"codigo": rc, "ultima_linea": log[-1:], "estado": st.get("estado_analisis"), "paso": st.get("paso"), "auditoria": st.get("auditoria"), "motor_en_estado": st.get("motor"),
         "ficha_oficial": None if fi is None else {"estado": fi.get("estado_analisis"), "cubo": fi.get("cubo"), "accion": (fi.get("decision") or {}).get("accion"), "cierre": fi.get("cierre"),
                                                  "bloque_f1": None if not isinstance(fi.get("motor_a_f1"), dict) else {"utilizable": fi["motor_a_f1"].get("utilizable_para_conclusion"),
                                                                                                                     "bloquean": sorted({g["id"] for g in fi["motor_a_f1"].get("bloquean") or []}),
                                                                                                                     "vigente": (fi["motor_a_f1"].get("vigencia") or {}).get("vigente")}},
         "vigencia_f1": {k: v for k, v in F1.vigencia(c).items() if k in ("motor", "exigido", "vigente", "utilizable")}}
    SAL[etiqueta] = d; print("--- " + etiqueta + "\n" + json.dumps(d, ensure_ascii=False, indent=1))
c = PP.preparar("EmpresaX_PC", PP.declaracion(), sin_arrendamientos=True)
p = os.path.join(c, "fase1_v63.json"); f1 = json.load(open(p, encoding="utf-8")); f1["precio"]["valor"] = 8; f1["capitalizacion"]["valor"] = 800
json.dump(f1, open(p, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
rc, log = lanzar(c); foto(c, "PC2-1 · F1 pasa en el paso 7; la declaración cambia antes del paso 12", rc, log)
respaldo = os.path.join(TS.BASE, "_respaldo_PC"); shutil.rmtree(respaldo, ignore_errors=True); shutil.copytree(c, respaldo, symlinks=True)
rc, log = lanzar(c, "--desde", "13"); foto(c, "PC2-2 · --desde 13 tras el bloqueo del paso 12", rc, log)
shutil.rmtree(c); shutil.copytree(respaldo, c, symlinks=True)
rc, log = lanzar(c, "--reiniciar", "--desde", "13"); foto(c, "PC2-3 · --reiniciar --desde 13 (el resultado F1 bloqueante sigue en la carpeta)", rc, log)
shutil.rmtree(c); shutil.copytree(respaldo, c, symlinks=True)
os.remove(os.path.join(c, "motor_a_f1_resultado.json"))
rc, log = lanzar(c, "--reiniciar", "--desde", "13"); foto(c, "PC2-4 · --reiniciar --desde 13 tras borrar motor_a_f1_resultado.json (la declaración bloqueante sigue en la carpeta)", rc, log)
json.dump(SAL, open(sys.argv[2], "w", encoding="utf-8"), ensure_ascii=False, indent=1)
