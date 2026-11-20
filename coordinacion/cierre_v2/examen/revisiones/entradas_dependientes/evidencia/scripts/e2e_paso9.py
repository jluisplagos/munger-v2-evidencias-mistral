"""Paso 9 de verdad sobre una COPIA de jumbo_g (revisor): declara C46/C40 dependientes de C76 en el registro de la copia, corre el pipeline
hasta el paso 9 y, justo antes y justo después de recalcular_dependientes, toma una instantánea de los archivos que puede tocar.
Uso: python3 -I e2e_paso9.py ARBOL_PV COPIA_JUMBO_G SALIDA_JSON [--sin-declaracion] [--con-libreoffice]"""
import copy, hashlib, json, os, sys
PV, ENS, OUT = sys.argv[1:4]
SIN = "--sin-declaracion" in sys.argv; CON_LO = "--con-libreoffice" in sys.argv
sys.path.insert(0, os.path.join(PV, "scripts"))
os.environ["MUNGER_CONFIG"] = os.path.join(PV, "config_v2_v631_f1.json")
import config_v2, pipeline as PL, verificacion_entradas as VE  # noqa: E402
from v63_xml import LibroV63  # noqa: E402
C = os.path.join(ENS, "Jumbo")
REC46 = {"celdas_de_juicio": ["Análisis!C76"], "regla": "J1 (DECISIONES_PARA_EL_USUARIO.md, 18-nov-2026)", "conciliacion_f1": True}
REC40 = {"celdas_de_juicio": ["Análisis!C76"], "regla": "J1 (DECISIONES_PARA_EL_USUARIO.md, 18-nov-2026)"}
if not SIN:
    p = os.path.join(C, VE.REGISTRO); d = json.load(open(p, encoding="utf-8"))
    for e in d["entradas"]:
        if e["celda"] in ("Análisis!C46", "Análisis!C40"):
            e["derivacion"]["recalculo"] = copy.deepcopy(REC46 if e["celda"] == "Análisis!C46" else REC40)
    open(p, "w", encoding="utf-8").write(json.dumps(d, ensure_ascii=False, indent=1))
NOMBRES = ["verificacion_entradas.json", "fase1_v63.json", "fase1_metadatos.json", "motor_a_f1.json", "Jumbo_v63_datos.xlsx", "Jumbo_v63_evaluada.xlsx",
           "fase_b.json", "fase_a.json", "estado_pipeline.json", "recalculo_dependientes.json"]
def foto():
    f = {}
    for n in NOMBRES:
        p = os.path.join(C, n)
        f[n] = hashlib.sha256(open(p, "rb").read()).hexdigest() if os.path.isfile(p) else None
    jsons = {n: json.load(open(os.path.join(C, n), encoding="utf-8")) for n in NOMBRES[:4] if os.path.isfile(os.path.join(C, n))}
    libros = {}
    for n in ("Jumbo_v63_datos.xlsx", "Jumbo_v63_evaluada.xlsx"):
        lb = LibroV63(os.path.join(C, n)); libros[n] = {h: {r: v for r, v in lb.todas_las_celdas(h).items()} for h in lb.hojas()}
    huellas = VE.huellas_registro(C)
    return {"sha": f, "json": jsons, "libros": libros, "huellas": huellas}
P = PL.Pipeline(C, config_v2.cargar(os.environ["MUNGER_CONFIG"]))
fotos = {}
orig = P.recalcular_dependientes
def envuelto(ev, da):
    fotos["antes"] = foto(); r = orig(ev, da); fotos["despues"] = foto(); return r
P.recalcular_dependientes = envuelto
class Alto(Exception): pass
if not CON_LO:
    def recalc(libro): raise Alto()
    P.recalc_leer_precio = recalc
try:
    P.correr(hasta=9)
except Alto:
    pass
except PL.Esperando as ex:
    fotos["esperando"] = str(ex)
fotos["historial_final"] = (P.st.get("historial") or [])[-12:]
fotos["estado"] = {k: P.st.get(k) for k in ("paso", "estado_analisis", "esperando", "recalculo_dependientes")}
json.dump(fotos, open(OUT, "w", encoding="utf-8"), ensure_ascii=False, default=str)
print("hecho", list(fotos))
