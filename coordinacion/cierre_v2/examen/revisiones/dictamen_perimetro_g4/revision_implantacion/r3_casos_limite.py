"""Revisión de la implantación de P-FOSO · R3: casos límite del módulo perimetro_f1.py (rama f1/perimetro-foso @ 688df46), sin escribir en
el repositorio. Usa el volcado y la declaración de Ahold (ahold_f2) y los textos del expediente para la comprobación de las fuentes.
Uso: r3_casos_limite.py RAIZ_PERSONAJE_V2 COPIA_EXPEDIENTE (con datos_v63.json y motor_a_f1.json con la serie de intereses, y texto/)"""
import copy, json, os, sys

PV, EXP = sys.argv[1], sys.argv[2]
sys.path.insert(0, os.path.join(PV, "scripts"))
sys.dont_write_bytecode = True
import perimetro_f1 as PF          # noqa: E402
import referencias_mecanicas as RM  # noqa: E402
import volcar_datos_v63 as VOL      # noqa: E402
import config_v2                    # noqa: E402
import motor_a_f1 as M              # noqa: E402

CFG = config_v2.cargar(os.path.join(PV, "config_v2_v631_f1.json"))
T = json.load(open(os.path.join(EXP, "datos_v63.json"), encoding="utf-8"))
T.pop("perimetro_f1", None)
D = json.load(open(os.path.join(EXP, "motor_a_f1.json"), encoding="utf-8"))
SI = "intereses_arrendamiento"


def ver(nombre, decl, t=None):
    t = copy.deepcopy(t or T)
    pf = PF.desde_datos(t, decl, EXP)
    if pf is None:
        print(f"{nombre}: perimetro_f1 = None (sin sección 1 bis; G7 y referencias con C55)")
        return None
    cf = pf["intereses_arrendamiento"]["comprobacion_fuentes"]
    rm = RM.calcular({**t, "perimetro_f1": pf}, CFG)["palancas"]["roic_lp"]
    md = "\n".join(PF.seccion_md(pf, "A"))
    cab = [l for l in md.splitlines() if l.startswith("- **Media") and "pagado todo el alquiler" in l]
    print(f"{nombre}: media {pf['roic_propio_pagado_el_alquiler_medio']} · utilizable {pf['roic_propio_utilizable']} · comprobada {cf['comprobada']} · "
          f"columna comprobada {cf['columna_comprobada']} · pendiente {len(cf['columna_pendiente'])} · inválidas {len(cf['invalidas'])} · "
          f"incompletas {len(cf['incompletas'])} · referencia BUENO {rm['BUENO']}")
    print("     titular de la sección:", (cab[0][:150] if cab else "—"), "| «NO COMPROBADOS» en la sección:", "NO COMPROBADOS" in md)
    return pf


print("— serie correcta —")
ver("A · serie con fila y columna", D)
print("\n— columna sin comprobar: sin «fila», la cifra de 2025 se sustituye por la de la columna de 2024 de la misma página (422 en lugar de 465) —")
d = copy.deepcopy(D)
for y in d["series"][SI]:
    d["series"][SI][y].pop("fila", None)
d["series"][SI]["2025"].update({"valor_fuente": -422, "literal": "(422)"})
ver("B · sin «fila» y cifra de otro ejercicio", d)
print("\n— la misma cifra equivocada, pero con «fila» —")
d2 = copy.deepcopy(D)
d2["series"][SI]["2025"].update({"valor_fuente": -422, "literal": "(422)"})
ver("C · con «fila» y cifra de otro ejercicio", d2)
print("\n— cifra que no está en la página —")
d3 = copy.deepcopy(D)
d3["series"][SI]["2025"].update({"valor_fuente": -265, "literal": "(265)"})
ver("D · literal ausente de la página", d3)
print("\n— falta un año de la serie —")
d4 = copy.deepcopy(D)
d4["series"][SI].pop("2022")
ver("E · sin 2022", d4)
print("\n— serie con los PAGOS en lugar de los intereses (fila «Repayment of lease liabilities» no está en esa página: se declara sin fila) —")
print("   coste implícito del arrendamiento = intereses ÷ pasivo medio (filas 23): lo que delataría una serie equivocada; el módulo no lo calcula")
pf = PF.desde_datos(copy.deepcopy(T), D, EXP)
for y in pf["anios"]:
    e, e0 = pf["por_anio"][str(y)], None
    arr = dict(zip([int(a) for a in T["historia"]["partidas"]["anio"]], T["historia"]["partidas"]["arrendamientos"]))
    print(f"   {y}: intereses {e['intereses_arrendamiento']:.0f} ÷ pasivo medio {(arr[y] + arr[y - 1]) / 2:.0f} = {e['intereses_arrendamiento'] / ((arr[y] + arr[y - 1]) / 2):.2%}")
print("\n— Historia con menos de diez años (el primero vacío) —")
t2 = copy.deepcopy(T)
t2["historia"]["partidas"]["anio"][0] = None
ver("F · año 1 vacío", D, t2)
print("\n— A0_total con etiquetas coincidentes: texto de V-F1g —")
COLS = "CDEFGHIJKL"; REG = {"fecha": "2026-11-18", "persona": "prueba", "motivo": "prueba"}
L = {"sha256": "x", "Diagnóstico V6!C5": "A", "Control maestro!L4": "IFRS", "Diagnóstico V6!C179": 0.05, "Análisis!C56": 0.09}
for c, y in zip(COLS, range(2016, 2026)):
    for fila, x in ((5, y), (6, 1000.0), (7, 70.0), (8, 30.0), (10, 0.2), (12, 20.0), (13, 0.0), (14, 0.0), (17, 0.0), (23, 0.0), (32, 600.0), (16, 0.0), (18, 0.0)):
        L[f"Historia!{c}{fila}"] = x
    L[f"Historia!{c}11"] = 72.0; L[f"Historia!{c}35"] = 50.0
L.update({"Historia!C57": 3, "Historia!C70": 50.0, "Historia!C44": 1000.0, "Historia!C48": 0.07, "Historia!C52": 0.2, "Historia!C53": "", "Historia!C54": 1.67,
          "Historia!C55": 0.0933, "Historia!C58": (56 - (20 - 30) - 50) / 1000, "Análisis!C46": 72.0, "Análisis!C47": 20.0, "Análisis!C48": 2.0, "Análisis!C49": 0.0,
          "Análisis!C50": 0.0, "Análisis!C51": "Sí", "Análisis!C52": 50.0})
s0 = {str(y): {"valor_fuente": 0, "signo": 1, "tratamiento": "ninguno", "documento": "x", "pagina": 1, "literal": "0"} for y in range(2016, 2026)}
dec = {"norma_contable": {"valor": "NIIF", "registro": REG}, "perimetro_reinversion": {"valor": "A0_total", "registro": REG},
       "perimetro_margen": {"valor": "EBIT_NIIF16_PPA_constante", "registro": REG}, "perimetro_palancas_s2c": {"valor": "A0_total", "registro": REG},
       "perimetro_roic": {"valor": "A0_total", "registro": REG}, "clasificacion_compras": {"valor": "sin_compras", "registro": REG},
       "transicion": {"conocida": False, "tratamiento": None, "registro": REG}, "series": {"da_rou": s0, "da_ppa": s0}}
r = M.evaluar(L, dec)
for g in r["guardas"]:
    if g["id"].startswith("V-F1g") or g["id"].startswith("V-F1k"):
        print("  ", g["id"], "·", g["detalle"][:200])
print("   filas «(valores)» presentes:", any("(valores)" in g["id"] for g in r["guardas"]), "· clave perimetro_f1_valores:", r.get("perimetro_f1_valores"))

print("\n— I+D capitalizada en las anclas (Historia!C68 = Sí): C55 pasa a ser la media de la fila 38, no de la 33 —")
t3 = copy.deepcopy(T)
t3["historia"]["anclas"]["roic_medio_5"] = 0.0700   # valor ilustrativo de la fila 38 (ROIC con I+D como inversión)
pf3 = PF.desde_datos(t3, D, EXP)
md3 = "\n".join(PF.seccion_md(pf3, "A"))
print("   línea de la sección:", [l for l in md3.splitlines() if "ROIC de todo el capital:" in l][0][:160])
print("   ¿el bloque menciona la I+D capitalizada o avisa de la diferencia?", ("I+D" in md3) or ("fila 38" in md3))
print("   ancla de G7 que se usaría:", pf3["roic_sin_arrendamientos_medio"], "(sin el ajuste de la I+D que sí lleva C55)")

print("\n— norma US GAAP en la declaración (arrendamiento operativo: el EBIT ya lleva todo el alquiler) —")
d5 = copy.deepcopy(D)
d5["norma_contable"]["valor"] = "US_GAAP"
pf5 = PF.desde_datos(copy.deepcopy(T), d5, EXP)
md5 = "\n".join(PF.seccion_md(pf5, "A")) if pf5 else ""
print("   ¿se emite el bloque con US_GAAP?", pf5 is not None, "· ¿resta intereses al EBIT?", pf5 is not None and pf5["roic_propio_pagado_el_alquiler_medio"] is not None,
      "· ¿el texto habla de «EBIT NIIF 16»?", "EBIT NIIF 16" in md5, "· ¿menciona la norma?", ("US GAAP" in md5) or ("US_GAAP" in md5))
