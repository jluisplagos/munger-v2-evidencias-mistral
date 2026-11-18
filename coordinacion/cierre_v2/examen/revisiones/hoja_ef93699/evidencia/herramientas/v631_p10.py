#!/usr/bin/env python3
"""(revisor) P10: copia del expediente V6.3.1 F1 cerrado (P6), declaración F1 cambiada después del cierre (D&A ROU 30 % → 31 %) y
relanzamiento con «--desde 12» (el gancho F1 del paso 12). Ejecutar bajo flock."""
import json, os, shutil, subprocess, sys
W = "/tmp/claude-0/revision_hoja"
RAIZ = os.path.join(W, "pkg", "munger_v2_r1")
sys.path.insert(0, os.path.join(RAIZ, "v6", "v631_f1", "scripts"))
sys.dont_write_bytecode = True
import prueba_pipeline_v631 as PP
TS, PF = PP.TS, PP.PF
src = os.path.join(W, "sint631", "P6_cerrado", "EmpresaX_V631")
dst = os.path.join(W, "sint631", "P10_desde12", "EmpresaX_V631")
shutil.rmtree(os.path.dirname(dst), ignore_errors=True)
shutil.copytree(src, dst)
d = PP.declaracion(0.31)
PF.escribir_fuente(dst, d)
json.dump(d, open(os.path.join(dst, "motor_a_f1.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
os.environ["MUNGER_CONFIG"] = PP.CFG631
r = subprocess.run([TS.PY, TS.PIPE, dst, "--desde", "12"], capture_output=True, text=True)
os.environ.pop("MUNGER_CONFIG", None)
TS.BASE = os.path.dirname(dst)
rc2, out2 = (r.returncode, "") if r.returncode != 10 else PP.correr(dst, PP.CFG631)
st = TS.estado(dst)
print("P10 · códigos", r.returncode, rc2, "· estado", st.get("estado_analisis"), "· paso", st.get("paso"), "· fin", st.get("fin"), "· F1", st.get("motor_a_f1"))
print((r.stdout + r.stderr)[-900:])
