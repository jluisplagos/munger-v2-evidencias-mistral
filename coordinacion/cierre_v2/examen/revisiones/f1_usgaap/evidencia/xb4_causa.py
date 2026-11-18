#!/usr/bin/env python3
"""Revisión R1 · XB4 (motor B, libro US GAAP, declaración que dice NIIF): por qué termina en el paso 8. Uso: flock … python3 -B xb4_causa.py [SALIDA.txt]"""
import json, os, shutil, sys, tempfile
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import adversarial_pipeline as AP
PU, TS = AP.PU, AP.TS
SAL = []
def p(*a):
    t = " ".join(str(x) for x in a); SAL.append(t); print(t, flush=True)
base0, TS.BASE = TS.BASE, tempfile.mkdtemp(prefix="rev_usgaap_xb4_")
try:
    d = PU.declaracion()
    d["norma_contable"]["valor"] = "NIIF"
    c = AP.preparar("EmpresaX_XB4", d)
    rc, out = AP.correr(c, motor="B")
    st = TS.estado(c)
    dg = PU.leer(c, "diagnostico.json")
    p(f"XB4 · motor B, libro US GAAP, declaración F1 que dice NIIF (y lleva el bloque arrendamientos_us_gaap y A2)")
    p(f"   estado final: {st.get('estado_analisis')} · paso {st.get('paso')} · registro F1 en el estado: {st.get('motor_a_f1')}")
    p(f"   causa: {json.dumps(dg.get('causa'), ensure_ascii=False)[:900]}")
    p(f"   salida del pipeline (final): {str(out)[-500:]}")
finally:
    shutil.rmtree(TS.BASE, ignore_errors=True)
    TS.BASE = base0
if len(sys.argv) > 1:
    open(sys.argv[1], "w", encoding="utf-8").write("\n".join(SAL) + "\n")
