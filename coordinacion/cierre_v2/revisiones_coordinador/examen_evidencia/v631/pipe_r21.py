"""Revisor: P6 de la V6.3.1 en el pipeline (estado final real) y R2-1 con la V6.3.1 (--reiniciar --desde 13 sin resultado F1)."""
import json, os, shutil, subprocess, sys, tempfile
W = "/tmp/claude-0/revision_v631/wt/munger_v2_r1"; PV = f"{W}/personaje_v2"
sys.path.insert(0, f"{W}/v6/v631_f1/scripts"); sys.dont_write_bytecode = True
import prueba_pipeline_v631 as P
TS, PF = P.TS, P.PF
BASE = sys.argv[1]; os.makedirs(BASE); TS.BASE = BASE
def leer(c, n):
    p = os.path.join(c, n); return json.load(open(p, encoding="utf-8")) if os.path.exists(p) else {}
def resumen(c, rc=None):
    st, fi, r = leer(c, "estado_pipeline.json"), leer(c, "ficha.json"), leer(c, "motor_a_f1_resultado.json")
    dg = leer(c, "diagnostico.json")
    return {"rc": rc, "estado": st.get("estado_analisis"), "paso": st.get("paso"), "ficha_estado": fi.get("estado_analisis"),
            "ficha_decision": (fi.get("decision") or fi.get("conclusion") or {}) if isinstance(fi.get("decision") or fi.get("conclusion"), (str, dict)) else None,
            "ficha_motor_a_f1": {k: (fi.get("motor_a_f1") or {}).get(k) for k in ("utilizable_para_conclusion", "rotulo")} if fi.get("motor_a_f1") else None,
            "cierre": leer(c, "cierre_vigente.json").get("resultado") or leer(c, "cierre_vigente.json").get("estado"),
            "F1_resultado": bool(r), "F1_bloquea": r.get("bloquea"), "causa": (dg.get("causa") or {}).get("detalle", "")[:300] if dg else None,
            "aptitud": (fi.get("aptitud_de_uso") or {}).get("apto_por_entradas")}
def pipe(c, *args):
    os.environ["MUNGER_CONFIG"] = P.CFG631
    try:
        r = subprocess.run([TS.PY, TS.PIPE, c, *args], capture_output=True, text=True)
        if r.returncode == 10:
            return P.correr(c, P.CFG631)
        return r.returncode, r.stdout + r.stderr
    finally:
        os.environ.pop("MUNGER_CONFIG", None)
out = {}
c = PF.preparar("EmpresaX_V631", P.declaracion())
rc, txt = P.correr(c, P.CFG631)
out["P6"] = resumen(c, rc); print("P6", out["P6"], flush=True)
ref = c + "_ref"; shutil.copytree(c, ref)
# R2-1a · borrar el resultado F1 y --reiniciar --desde 13
c1 = c + "_r21a"; shutil.copytree(ref, c1)
for n in ("motor_a_f1_resultado.json", "motor_a_f1_resultado.md"):
    if os.path.exists(os.path.join(c1, n)): os.remove(os.path.join(c1, n))
rc, txt = pipe(c1, "--reiniciar", "--desde", "13"); out["R21a_borrado_reiniciar_desde13"] = resumen(c1, rc); out["R21a_salida"] = txt[-600:]; print("R21a", out["R21a_borrado_reiniciar_desde13"], flush=True)
# R2-1b · lo mismo con la declaración cambiada (ROU 30 % → 40 %: el libro ya no corresponde)
c2 = c + "_r21b"; shutil.copytree(ref, c2)
d = P.declaracion(0.40); json.dump(d, open(os.path.join(c2, "motor_a_f1.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1); PF.escribir_fuente(c2, d)
for n in ("motor_a_f1_resultado.json", "motor_a_f1_resultado.md"):
    if os.path.exists(os.path.join(c2, n)): os.remove(os.path.join(c2, n))
rc, txt = pipe(c2, "--reiniciar", "--desde", "13"); out["R21b_decl_cambiada_borrado_reiniciar_desde13"] = resumen(c2, rc); out["R21b_salida"] = txt[-600:]; print("R21b", out["R21b_decl_cambiada_borrado_reiniciar_desde13"], flush=True)
# control · declaración cambiada, resultado borrado, --desde 13 SIN --reiniciar
c3 = c + "_ctrl"; shutil.copytree(ref, c3)
json.dump(d, open(os.path.join(c3, "motor_a_f1.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1); PF.escribir_fuente(c3, d)
for n in ("motor_a_f1_resultado.json", "motor_a_f1_resultado.md"):
    if os.path.exists(os.path.join(c3, n)): os.remove(os.path.join(c3, n))
rc, txt = pipe(c3, "--desde", "13"); out["CTRL_decl_cambiada_borrado_desde13"] = resumen(c3, rc); print("CTRL", out["CTRL_decl_cambiada_borrado_desde13"], flush=True)
# R2-1c · declaración cambiada, resultado CONSERVADO, --reiniciar --desde 13
c4 = c + "_r21c"; shutil.copytree(ref, c4)
json.dump(d, open(os.path.join(c4, "motor_a_f1.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1); PF.escribir_fuente(c4, d)
rc, txt = pipe(c4, "--reiniciar", "--desde", "13"); out["R21c_decl_cambiada_conservado_reiniciar_desde13"] = resumen(c4, rc); print("R21c", out["R21c_decl_cambiada_conservado_reiniciar_desde13"], flush=True)
json.dump(out, open(os.path.join(os.path.dirname(BASE), "resultado_pipe_r21.json"), "w"), ensure_ascii=False, indent=1, default=str)
