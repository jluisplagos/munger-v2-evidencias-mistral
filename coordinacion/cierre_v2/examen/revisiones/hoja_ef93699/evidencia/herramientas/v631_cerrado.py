#!/usr/bin/env python3
"""(revisor) Reproduce P6 y P8 de v6/v631_f1/scripts/prueba_pipeline_v631.py en la copia de trabajo y CONSERVA los expedientes:
  P6_cerrado/EmpresaX_V631  : empresa sintética con arrendamientos, plantilla V6.3.1 F1, perímetro A1_sin_ROU declarado, cierre concluido;
  P8_f1_bloquea/EmpresaX_V631: copia de P6 con la declaración F1 cambiada después del cierre (D&A ROU 30 % → 31 %) y «--desde 7».
Ejecutar bajo flock del cerrojo común (el pipeline llama a LibreOffice sin flock)."""
import json, os, shutil, subprocess, sys
W = "/tmp/claude-0/revision_hoja"
RAIZ = os.path.join(W, "pkg", "munger_v2_r1")
PV = os.path.join(RAIZ, "personaje_v2")
sys.path.insert(0, os.path.join(RAIZ, "v6", "v631_f1", "scripts"))
sys.dont_write_bytecode = True
import prueba_pipeline_v631 as PP   # importa TS y PF con sus rutas
TS, PF = PP.TS, PP.PF
dest = os.path.join(W, "sint631")
shutil.rmtree(dest, ignore_errors=True)
os.makedirs(dest)
TS.BASE = os.path.join(dest, "P6_cerrado")
os.makedirs(TS.BASE)
c = PF.preparar("EmpresaX_V631", PP.declaracion())
rc, out = PP.correr(c, PP.CFG631)
st = TS.estado(c)
print("P6 · código", rc, "· estado", st.get("estado_analisis"), "· paso", st.get("paso"), "· fin", st.get("fin"), "· F1", (st.get("motor_a_f1") or {}))
# P8 sobre una copia
p8 = os.path.join(dest, "P8_f1_bloquea", "EmpresaX_V631")
shutil.copytree(c, p8)
d = PP.declaracion(0.31)
PF.escribir_fuente(p8, d)
json.dump(d, open(os.path.join(p8, "motor_a_f1.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
os.environ["MUNGER_CONFIG"] = PP.CFG631
r8 = subprocess.run([TS.PY, TS.PIPE, p8, "--desde", "7"], capture_output=True, text=True)
os.environ.pop("MUNGER_CONFIG", None)
TS.BASE = os.path.join(dest, "P8_f1_bloquea")
rc8, out8 = PP.correr(p8, PP.CFG631)
st8 = TS.estado(p8)
print("P8 · códigos", r8.returncode, rc8, "· estado", st8.get("estado_analisis"), "· paso", st8.get("paso"), "· fin", st8.get("fin"), "· F1", (st8.get("motor_a_f1") or {}))
print((r8.stdout + r8.stderr)[-600:])
