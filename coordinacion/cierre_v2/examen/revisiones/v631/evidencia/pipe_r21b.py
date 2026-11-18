import json, os, shutil, subprocess, sys
W = "/tmp/claude-0/revision_v631/wt/munger_v2_r1"
sys.path.insert(0, f"{W}/v6/v631_f1/scripts"); sys.path.insert(0, "/tmp/claude-0/revision_v631/s"); sys.dont_write_bytecode = True
import prueba_pipeline_v631 as P
TS, PF = P.TS, P.PF
REF = "/tmp/claude-0/revision_v631/pipe/base/EmpresaX_V631_ref"
def leer(c, n):
    p = os.path.join(c, n); return json.load(open(p, encoding="utf-8")) if os.path.exists(p) else {}
def resumen(c, rc):
    st, fi, dg = leer(c, "estado_pipeline.json"), leer(c, "ficha.json"), leer(c, "diagnostico.json")
    return {"rc": rc, "estado": st.get("estado_analisis"), "paso": st.get("paso"), "ficha": fi.get("estado_analisis"), "plantilla": (fi.get("versiones") or {}).get("plantilla"),
            "decision": (fi.get("decision") or {}).get("accion"), "precio_objetivo": (fi.get("decision") or {}).get("precio_objetivo"),
            "motor_a_f1": {k: (fi.get("motor_a_f1") or {}).get(k) for k in ("exigido", "utilizable_para_conclusion", "rotulo")},
            "F1_resultado": os.path.exists(os.path.join(c, "motor_a_f1_resultado.json")), "causa": ((dg.get("causa") or {}).get("detalle") or "")[:260]}
def caso(nombre, decl_frac, borrar, args):
    base = f"/tmp/claude-0/revision_v631/pipe/{nombre}"; os.makedirs(base); TS.BASE = base
    c = os.path.join(base, "EmpresaX_V631"); shutil.copytree(REF, c)
    if decl_frac is not None:
        d = P.declaracion(decl_frac); json.dump(d, open(os.path.join(c, "motor_a_f1.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1); PF.escribir_fuente(c, d)
    if borrar:
        for n in ("motor_a_f1_resultado.json", "motor_a_f1_resultado.md"):
            if os.path.exists(os.path.join(c, n)): os.remove(os.path.join(c, n))
    os.environ["MUNGER_CONFIG"] = P.CFG631
    r = subprocess.run([TS.PY, TS.PIPE, c, *args], capture_output=True, text=True); rc = r.returncode
    os.environ.pop("MUNGER_CONFIG", None)
    if rc == 10: rc, _ = P.correr(c, P.CFG631)
    out = resumen(c, rc); print(nombre, json.dumps(out, ensure_ascii=False), flush=True); return out
R = {}
R["R21a"] = caso("R21a_borrado_reiniciar_desde13", None, True, ["--reiniciar", "--desde", "13"])
R["R21b"] = caso("R21b_declcambiada_borrado_reiniciar_desde13", 0.40, True, ["--reiniciar", "--desde", "13"])
R["CTRL1"] = caso("CTRL1_declcambiada_borrado_desde13", 0.40, True, ["--desde", "13"])
R["CTRL2"] = caso("CTRL2_declcambiada_conservado_reiniciar_desde13", 0.40, False, ["--reiniciar", "--desde", "13"])
json.dump(R, open("/tmp/claude-0/revision_v631/resultado_pipe_r21_v2.json", "w"), ensure_ascii=False, indent=1)
