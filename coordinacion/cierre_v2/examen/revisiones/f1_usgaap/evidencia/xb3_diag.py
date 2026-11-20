#!/usr/bin/env python3
"""Revisión R1 · F1 US GAAP · diagnóstico de XB3/XB4: motor B con libro US GAAP y sin declaración F1 (o con una declaración que no dice US_GAAP).
¿Por qué el gancho, la vigencia y el cierre no exigen F1? Uso: flock … python3 -B xb3_diag.py [SALIDA.txt]"""
import json, os, shutil, sys, tempfile
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import adversarial_pipeline as AP
PU, TS = AP.PU, AP.TS
sys.path.insert(0, os.path.join(AP.PV, "scripts"))
import motor_a_f1 as M
import cierre_v2 as CIE
from v63_xml import LibroV63
SAL = []
def p(*a):
    t = " ".join(str(x) for x in a); SAL.append(t); print(t, flush=True)
base0, TS.BASE = TS.BASE, tempfile.mkdtemp(prefix="rev_usgaap_xb3_")
try:
    for nombre, quitar, norma in (("XB3 · sin motor_a_f1.json", True, None), ("XB4 · declaración F1 que dice NIIF (mezcla) con libro US GAAP", False, "NIIF")):
        d = PU.declaracion()
        if norma:
            d["norma_contable"]["valor"] = norma
        c = AP.preparar("EmpresaX_" + nombre[:3], d, sin_decl=quitar)
        rc, out = AP.correr(c, motor="B")
        st = TS.estado(c)
        E = os.path.basename(c)
        rec = os.path.join(c, "recalc", f"{E}_v63_evaluada.xlsx")
        ev = os.path.join(c, f"{E}_v63_evaluada.xlsx")
        p(f"\n== {nombre}")
        p(f"   estado final: {st.get('estado_analisis')} · paso {st.get('paso')} · motor {st.get('motor')} · registro F1 en el estado: {st.get('motor_a_f1')} · ¿existe motor_a_f1_resultado.json?: {os.path.exists(os.path.join(c, 'motor_a_f1_resultado.json'))}")
        for et, lib in (("libro recalculado (recalc/, el que recibe el gancho)", rec), ("libro evaluado del expediente", ev)):
            if os.path.exists(lib):
                v = LibroV63(lib).leer("Control maestro", "L4")
                L = M.leer_libro(lib)
                p(f"   {et}: LibroV63.leer(Control maestro, L4) = {v!r} → norma_del_libro = {M.norma_del_libro({'Control maestro!L4': v})} · leer_libro (openpyxl) = {L.get('Control maestro!L4')!r} → {M.norma_del_libro(L)}")
                p(f"      Historia L22 = {L.get('Historia!L22')} · L23 = {L.get('Historia!L23')} · C64 = {L.get('Historia!C64')} (lo que resta el puente)")
        p(f"   us_gaap_del_expediente(carpeta) = {M.us_gaap_del_expediente(c)} · exigido_puente(carpeta, libro recalculado) = {M.exigido_puente(c, libro=rec)} · con el libro leído entero (L=leer_libro): {M.exigido_puente(c, L=M.leer_libro(rec))}")
        v = M.vigencia(c, motor="B")
        p(f"   vigencia(motor B): exigido {v.get('exigido')} · motivo: {v.get('motivo')}")
        p(f"   objeción F1 del cierre a «concluido»: {CIE.motivo_f1(c, dict(st, motor='B'))}")
        fi = PU.leer(c, "ficha.json")
        p(f"   ficha: estado {fi.get('estado_analisis')} · cubo {fi.get('cubo')} · bloque motor_a_f1 en la ficha: {'sí' if fi.get('motor_a_f1') else 'no'}")
        inf = open(os.path.join(c, "informe.md"), encoding="utf-8").read() if os.path.exists(os.path.join(c, "informe.md")) else ""
        p(f"   informe.md nombra F1: {'· F1:' in inf}")
finally:
    shutil.rmtree(TS.BASE, ignore_errors=True)
    TS.BASE = base0
if len(sys.argv) > 1:
    open(sys.argv[1], "w", encoding="utf-8").write("\n".join(SAL) + "\n")
