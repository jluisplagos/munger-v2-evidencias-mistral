#!/usr/bin/env python3
"""Segunda ronda · preparación con el código ANTERIOR (2e9442f): un expediente sintético NO exento por su nombre (empresa «Empresa Y S.A.»),
NIIF, motor A, con arrendamientos (C49 = 3,71; pasivo 50), sin archivos de la 4.15, llevado hasta su cierre. Con ese código F1 no se exigía.
LibreOffice: ejecutar con flock. Uso (desde personaje_v2/ de la copia ANTIGUA): r2_preparar_antiguo.py DIR_BASE"""
import json, os, sys
sys.path.insert(0, os.path.join(os.getcwd(), "pruebas")); sys.dont_write_bytecode = True
import test_pipeline_sintetico as TS
TS.BASE = os.path.abspath(sys.argv[1]); os.makedirs(TS.BASE, exist_ok=True)
c = TS.preparar("EmpresaY", precio=8)
p = os.path.join(c, "fase1_v63.json"); f1 = json.load(open(p, encoding="utf-8")); f1["empresa"] = "Empresa Y S.A."
json.dump(f1, open(p, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
rc, out = TS.correr(c, TS.reaccion_normal())
st = TS.estado(c); fi = json.load(open(os.path.join(c, "ficha.json"), encoding="utf-8"))
print("código", rc, "·", out.strip().splitlines()[-1][:160])
print({"estado": st.get("estado_analisis"), "paso": st.get("paso"), "auditoria": st.get("auditoria"), "motor": st.get("motor"), "ficha": [fi.get("estado_analisis"), fi.get("cubo"), (fi.get("decision") or {}).get("accion"), fi.get("cierre")],
       "motor_a_f1_en_ficha": "motor_a_f1" in fi, "archivos_415": [n for n in ("entrada_efectiva.json", "motor_a_f1.json", "motor_a_f1_resultado.json") if os.path.exists(os.path.join(c, n))]})
