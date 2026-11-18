#!/usr/bin/env python3
"""Segunda ronda · ataques sobre el código NUEVO (340d78c/24e9a30) con los agentes simulados de su batería. LibreOffice: ejecutar con flock.
Uso (desde personaje_v2/ de la copia NUEVA): r2_ataques_pipeline.py DIR_EXPEDIENTE_ANTIGUO_CERRADO DIR_TRABAJO SALIDA.json"""
import json, os, shutil, subprocess, sys
PV = os.getcwd()
sys.path.insert(0, os.path.join(PV, "pruebas")); sys.path.insert(0, os.path.join(PV, "scripts")); sys.dont_write_bytecode = True
import test_pipeline_sintetico as TS
import motor_a_f1 as F1
ORIG, BASE, SALIDA = os.path.abspath(sys.argv[1]), os.path.abspath(sys.argv[2]), sys.argv[3]
os.makedirs(BASE, exist_ok=True)
SAL = {}
reac = TS.reaccion_normal()

def lanzar(c, *extra, max_vueltas=40):
    args = list(extra); log = []
    for _ in range(max_vueltas):
        r = subprocess.run([TS.PY, TS.PIPE, c] + args, capture_output=True, text=True)
        args = []
        log.append((r.stdout + r.stderr).strip().splitlines()[-1][:260] if (r.stdout + r.stderr).strip() else "")
        if r.returncode != 10:
            return r.returncode, log
        reac(c, open(os.path.join(c, "ESPERANDO.md"), encoding="utf-8").read().split("**")[1])
    return 10, log + ["demasiadas vueltas"]

def foto(c, etiqueta, rc=None, log=None):
    st = json.load(open(os.path.join(c, "estado_pipeline.json"), encoding="utf-8")) if os.path.exists(os.path.join(c, "estado_pipeline.json")) else {}
    fi = json.load(open(os.path.join(c, "ficha.json"), encoding="utf-8")) if os.path.exists(os.path.join(c, "ficha.json")) else None
    inf = open(os.path.join(c, "informe.md"), encoding="utf-8").read() if os.path.exists(os.path.join(c, "informe.md")) else ""
    d = {"codigo": rc, "ultimas_lineas": (log or [])[-2:], "estado": st.get("estado_analisis"), "paso": st.get("paso"), "auditoria": st.get("auditoria"), "motor_en_estado": st.get("motor"),
         "ficha_oficial": None if fi is None else {"estado": fi.get("estado_analisis"), "cubo": fi.get("cubo"), "accion": (fi.get("decision") or {}).get("accion"),
                                                  "precio_objetivo": (fi.get("decision") or {}).get("precio_objetivo"), "cierre": fi.get("cierre"),
                                                  "bloque_f1": None if not isinstance(fi.get("motor_a_f1"), dict) else {k: fi["motor_a_f1"].get(k) for k in ("utilizable_para_conclusion", "vigencia")}},
         "informe_estado": next((l for l in inf.splitlines() if l.startswith("**Estado")), "")[:150],
         "cierre_vigente.json": os.path.exists(os.path.join(c, "cierre_vigente.json")), "resultado_f1": os.path.exists(os.path.join(c, "motor_a_f1_resultado.json")),
         "vigencia_f1": F1.vigencia(c), "historial_f1": [h[-200:] for h in st.get("historial", []) if ("F1" in h or "FIN" in h or "CIERRE" in h)][-4:]}
    SAL[etiqueta] = d
    print("--- " + etiqueta + "\n" + json.dumps(d, ensure_ascii=False, indent=1))

def copia(nombre):
    d = os.path.join(BASE, nombre); shutil.rmtree(d, ignore_errors=True); os.makedirs(d)
    c = os.path.join(d, "EmpresaY"); shutil.copytree(ORIG, c, symlinks=True)
    for f in os.listdir(os.path.dirname(ORIG)):
        if f.endswith(".csv"):
            shutil.copy(os.path.join(os.path.dirname(ORIG), f), d)
    return c

foto(ORIG, "A0 · expediente cerrado con el código anterior (sin tocar), visto con el código nuevo")
# A1 · relanzamiento simple
c = copia("a1"); rc, log = lanzar(c); foto(c, "A1 · pipeline.py sin opciones", rc, log)
# A2 · --desde 13
c = copia("a2"); rc, log = lanzar(c, "--desde", "13"); foto(c, "A2 · --desde 13", rc, log)
# A3 · --reiniciar --desde 13
c = copia("a3"); rc, log = lanzar(c, "--reiniciar", "--desde", "13"); foto(c, "A3 · --reiniciar --desde 13", rc, log)
# A4 · --desde 14
c = copia("a4"); rc, log = lanzar(c, "--desde", "14"); foto(c, "A4 · --desde 14", rc, log)
# A5 · --reiniciar --desde 14
c = copia("a5"); rc, log = lanzar(c, "--reiniciar", "--desde", "14"); foto(c, "A5 · --reiniciar --desde 14", rc, log)
# A6 · ficha.py a mano
c = copia("a6")
r = subprocess.run([TS.PY, os.path.join(PV, "scripts", "ficha.py"), c, "--estado", "concluido"], capture_output=True, text=True)
foto(c, "A6 · ficha.py --estado concluido a mano", r.returncode, [(r.stdout + r.stderr).strip()[-300:]])
# A7 · --reiniciar --desde 12 (el paso 12 vuelve a evaluar F1, pero el estado no dice el motor)
c = copia("a7"); rc, log = lanzar(c, "--reiniciar", "--desde", "12"); foto(c, "A7 · --reiniciar --desde 12", rc, log)

# B · expediente NUEVO con el código nuevo, no exento, con arrendamientos, sin archivos de la 4.15 ni declaración
TS.BASE = os.path.join(BASE, "b")
def nuevo(nombre, antes=None):
    c = TS.preparar(nombre, precio=8)
    p = os.path.join(c, "fase1_v63.json"); f1 = json.load(open(p, encoding="utf-8")); f1["empresa"] = "Empresa Z S.A."
    json.dump(f1, open(p, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    if antes: antes(c)
    return c
c = nuevo("EmpresaZ1"); rc, log = lanzar(c); foto(c, "B1 · expediente nuevo con arrendamientos, sin archivos de la 4.15 ni declaración", rc, log)
ELIS_CV = os.path.join(PV, "empresas_v2_correcciones", "2026-11_Vidrala_ensayo_4_14", "elis_decisiones", "Elis", "cierre_vigente.json")
c = nuevo("EmpresaZ2", antes=lambda c: shutil.copy(ELIS_CV, os.path.join(c, "cierre_vigente.json")))
print("B2 antes de lanzar: exención =", str(F1.exencion(c))[:80])
rc, log = lanzar(c); foto(c, "B2 · lo mismo con el cierre_vigente.json registrado de Elis copiado antes de empezar", rc, log)
# B3 · la copia se hace mientras el pipeline espera a la fase A (paso 6): ¿salta el gancho del paso 7?
c = nuevo("EmpresaZ3")
hecho = {"x": False}
normal = reac
def reac_b3(c_, nombre):
    normal(c_, nombre)
    if nombre == "fase_a" and not hecho["x"]:
        shutil.copy(ELIS_CV, os.path.join(c_, "cierre_vigente.json")); hecho["x"] = True
reac = reac_b3
rc, log = lanzar(c); foto(c, "B3 · cierre_vigente.json de Elis copiado mientras se espera a la fase A", rc, log)
json.dump(SAL, open(SALIDA, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print("escrito", SALIDA)
