#!/usr/bin/env python3
"""Sonda S14: perímetro A0 (empresa sin arrendamientos ni PPA) con un término explícito declarado (transición temporal o compras de reposición):
¿salta F1-LIBRO? El libro V6.3 no cobra términos explícitos. Uso: sondas_capa3.py RUTA_personaje_v2"""
import os, sys
sys.dont_write_bytecode = True
PV = sys.argv[1]
sys.path.insert(0, os.path.join(PV, "scripts"))
import motor_a_f1 as M
src = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "sondas_capa.py"), encoding="utf-8").read().split("# ---------------------------------------------------------------- S1")[0]
exec(src.replace('PV = sys.argv[1]', 'pass'))
L7 = libro([1000.0] * 10, [80.0] * 10, [20.0] * 10, [0.0] * 10, [20.0] * 10, [0.0] * 10, [0.0] * 10, [0.0] * 10, 80.0, 0.0)
base = M.evaluar(L7, decl("A0_total", rou=todos(0), ppa=todos(0)))
d = decl("A0_total", rou=todos(0), ppa=todos(0), trans=True)
d["transicion"].update({"tratamiento": "termino_explicito", "importes": {str(t): 7 for t in range(1, 6)}, "horizonte": 5, "naturaleza": "temporal",
                        "finalidad_documentada": "plan sintético (fuente)", "ancla_s2c_excluye_terminos": True})
r = M.evaluar(L7, d)
a = r["calculo_perimetro_declarado"]["escenarios"]["NORMAL"]; b = base["calculo_perimetro_declarado"]["escenarios"]["NORMAL"]
print("S14a · A0 + transición como término explícito (7 al año, 5 años):")
print("   flujos de la capa menos flujos del libro (NORMAL, años 1–10):", [round(x - y, 3) for x, y in zip(a["anios_1_10"], b["anios_1_10"])])
print("   F1-LIBRO salta:", any(g["id"] == "F1-LIBRO" and g["salta"] for g in r["guardas"]), "· utilizable_para_conclusion:", r["utilizable_para_conclusion"], "· bloquean:", bloq(r))
d2 = decl("A0_total", rou=todos(0), ppa=todos(0), compras="reposicion_con_importe")
d2["clasificacion_compras"].update({"proporcion_ventas": 0.009, "ancla_s2c_excluye_terminos": True})
La = dict(L7); La["Historia!L13"] = 9.0
r2 = M.evaluar(La, d2)
a2 = r2["calculo_perimetro_declarado"]["escenarios"]["NORMAL"]
print("S14b · A0 + compras de reposición del 0,9 % de las ventas como término explícito:")
print("   cargo anual que el libro no hace (NORMAL, años 1–3 y año 11):", [round(y - x, 3) for x, y in zip(a2["anios_1_10"][:3], b["anios_1_10"][:3])], round(b["anio_11"] - a2["anio_11"], 3))
print("   F1-LIBRO salta:", any(g["id"] == "F1-LIBRO" and g["salta"] for g in r2["guardas"]), "· utilizable_para_conclusion:", r2["utilizable_para_conclusion"], "· bloquean:", bloq(r2))
