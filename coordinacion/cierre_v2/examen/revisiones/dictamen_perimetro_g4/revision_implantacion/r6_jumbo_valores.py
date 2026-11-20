"""Revisión de la implantación de P-FOSO · R6: la fila «V-F1g (valores)» en un arrendatario ligero (Jumbo, jumbo_d: A2_propio declarado,
arrendamientos 6 % del capital). Las palancas se ponen en memoria sobre los valores leídos del libro de datos recalculado; nada se escribe.
Uso: r6_jumbo_valores.py RAIZ_PERSONAJE_V2 LIBRO_RECALCULADO_JUMBO DECLARACION_JUMBO"""
import json, os, sys
PV, LIBRO, DECL = sys.argv[1:4]
sys.path.insert(0, os.path.join(PV, "scripts")); sys.dont_write_bytecode = True
import motor_a_f1 as M  # noqa: E402
L0 = M.leer_libro(LIBRO)
decl = json.load(open(DECL, encoding="utf-8"))
print("C53 (ancla E4 con D_X de A2):", L0.get("Historia!C53"), "· C54 (todo el capital):", L0.get("Historia!C54"), "· ventas ÷ (capital − arrendamientos) 2025:",
      L0["Historia!L6"] / (L0["Historia!L32"] - L0["Historia!L23"]))
for nombre, s2c in (("S2C en el ancla marginal del perímetro (C53)", (1.3, 1.7, 2.1)), ("S2C en el MEDIO del capital propio (1,19)", (0.9, 1.2, 1.5)),
                    ("S2C en C54, de todo el capital (1,11)", (0.8, 1.1, 1.4))):
    L = dict(L0)
    L["Diagnóstico V6!C5"] = "A"
    for c, s, g, m, ro, gi in zip("BCD", s2c, (0.03, 0.06, 0.08), (0.28, 0.31, 0.33), (0.09, 0.12, 0.12), (0.015, 0.02, 0.025)):
        L[f"Palancas!{c}14"], L[f"Palancas!{c}15"], L[f"Palancas!{c}16"], L[f"Palancas!{c}18"], L[f"Análisis!{c}68"] = g, m, s, ro, gi
    r = M.evaluar(L, decl, motor_libro="A", carpeta=os.path.dirname(DECL))
    g = {x["id"]: x for x in r["guardas"]}.get("V-F1g (valores)")
    print(f"{nombre}: {s2c} → salta {g['salta']} · {g['detalle'][:330]}")
