import json, os, shutil, subprocess, sys
W = "/tmp/claude-0/revision_v631/r2/munger_v2_r1"; PV = f"{W}/personaje_v2"
sys.path.insert(0, f"{W}/v6/v631_f1/scripts"); sys.path.insert(0, f"{PV}/scripts"); sys.dont_write_bytecode = True
import prueba_pipeline_v631 as P
TS, PF = P.TS, P.PF
RAIZ = "/tmp/claude-0/revision_v631/pipe2"
def leer(c, n):
    p = os.path.join(c, n); return json.load(open(p, encoding="utf-8")) if os.path.exists(p) else {}
def resumen(c, rc, txt=""):
    st, fi, dg = leer(c, "estado_pipeline.json"), leer(c, "ficha.json"), leer(c, "diagnostico.json")
    return {"rc": rc, "estado": st.get("estado_analisis"), "paso": st.get("paso"), "ficha": fi.get("estado_analisis"), "decision": (fi.get("decision") or {}).get("accion"),
            "motor_a_f1": (fi.get("motor_a_f1") or {}).get("rotulo", "")[:120], "F1_resultado": os.path.exists(os.path.join(c, "motor_a_f1_resultado.json")),
            "causa": ((dg.get("causa") or {}).get("detalle") or "")[:220], "salida": txt.strip().splitlines()[-1][:260] if txt.strip() else ""}
def pipe(c, *args):
    os.environ["MUNGER_CONFIG"] = P.CFG631
    try:
        r = subprocess.run([TS.PY, TS.PIPE, c, *args], capture_output=True, text=True)
        if r.returncode == 10:
            rc, t = P.correr(c, P.CFG631); return rc, r.stdout + t
        return r.returncode, r.stdout + r.stderr
    finally:
        os.environ.pop("MUNGER_CONFIG", None)
TS.BASE = os.path.join(RAIZ, "base"); os.makedirs(TS.BASE)
c = PF.preparar("EmpresaX_V631", P.declaracion())
rc, txt = P.correr(c, P.CFG631); R = {"P6": resumen(c, rc)}; print("P6", R["P6"], flush=True)
REF = c + "_ref"; shutil.copytree(c, REF)
def caso(nombre, frac, borrar, args):
    base = os.path.join(RAIZ, nombre); os.makedirs(base); TS.BASE = base
    cc = os.path.join(base, "EmpresaX_V631"); shutil.copytree(REF, cc)
    if frac is not None:
        d = P.declaracion(frac); json.dump(d, open(os.path.join(cc, "motor_a_f1.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1); PF.escribir_fuente(cc, d)
    for n in borrar:
        if os.path.exists(os.path.join(cc, n)): os.remove(os.path.join(cc, n))
    rc, txt = pipe(cc, *args); R[nombre] = resumen(cc, rc, txt); print(nombre, json.dumps(R[nombre], ensure_ascii=False), flush=True)
    return cc
RES = ["motor_a_f1_resultado.json", "motor_a_f1_resultado.md"]
caso("R21a_borrado_reiniciar_desde13", None, RES, ["--reiniciar", "--desde", "13"])
caso("R21b_decl40_borrado_reiniciar_desde13", 0.40, RES, ["--reiniciar", "--desde", "13"])
caso("R21d_decl40_borrado_estado_y_resultado_desde13", 0.40, RES + ["estado_pipeline.json"], ["--desde", "13"])
caso("R21e_sin_cambios_borrado_estado_y_resultado_desde13", None, RES + ["estado_pipeline.json"], ["--desde", "13"])
caso("R21f_decl40_borrado_estado_resultado_y_fase_a_desde13", 0.40, RES + ["estado_pipeline.json", "fase_a.json"], ["--desde", "13"])
json.dump(R, open("/tmp/claude-0/revision_v631/s2/resultado_pipe2.json", "w"), ensure_ascii=False, indent=1)
