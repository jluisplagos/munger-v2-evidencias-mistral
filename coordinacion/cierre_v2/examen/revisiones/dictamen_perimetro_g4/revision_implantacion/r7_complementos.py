"""Revisión de la implantación de P-FOSO · R7: complementos (rama f1/perimetro-foso @ 688df46), sin escribir en el repositorio.
 a) qué dice la sección cuando la columna del ejercicio queda PENDIENTE (serie sin «fila»);
 b) sin «fila», ¿pasa por comprobada cualquier cifra que esté en la página? (el «Total rent expense» (57) de la misma página, que no son intereses);
 c) valores de Ahold con las referencias mecánicas nuevas, con la réplica del dictamen;
 d) fórmulas del libro que siguen midiendo con todo el capital (Historia!C55/C68 y semáforo de la rentabilidad marginal).
Uso: r7_complementos.py RAIZ_PERSONAJE_V2 COPIA_EXPEDIENTE EXPEDIENTE_ORIGINAL(lectura) CARPETA_REPLICA"""
import copy, json, os, sys

PV, EXP, ORIG, REP = sys.argv[1:5]
sys.path.insert(0, os.path.join(PV, "scripts"))
sys.dont_write_bytecode = True
import perimetro_f1 as PF          # noqa: E402
import referencias_mecanicas as RM  # noqa: E402
import config_v2                    # noqa: E402

CFG = config_v2.cargar(os.path.join(PV, "config_v2_v631_f1.json"))
T = json.load(open(os.path.join(EXP, "datos_v63.json"), encoding="utf-8"))
T.pop("perimetro_f1", None)
D = json.load(open(os.path.join(EXP, "motor_a_f1.json"), encoding="utf-8"))
SI = "intereses_arrendamiento"


def ver(nombre, decl):
    pf = PF.desde_datos(copy.deepcopy(T), decl, EXP)
    cf = pf["intereses_arrendamiento"]["comprobacion_fuentes"]
    rm = RM.calcular({**copy.deepcopy(T), "perimetro_f1": pf}, CFG)["palancas"]["roic_lp"]
    md = PF.seccion_md(pf, "A")
    print(f"{nombre}: media {pf['roic_propio_pagado_el_alquiler_medio']:.4%} · utilizable {pf['roic_propio_utilizable']} · comprobada {cf['comprobada']} · "
          f"columna comprobada {cf['columna_comprobada']} · pendiente {len(cf['columna_pendiente'])} · inválidas {len(cf['invalidas'])} · referencia BUENO {rm['BUENO']}")
    for l in md:
        if l.startswith("- **Media") and "pagado todo el alquiler" in l:
            print("   titular  :", l[:112])
        if l.strip().startswith("- Intereses de arrendamiento:"):
            print("   fuente   :", l.strip())
    return pf


print("a) columna PENDIENTE: la serie correcta, declarada sin «fila»")
d = copy.deepcopy(D)
for y in d["series"][SI]:
    d["series"][SI][y].pop("fila", None)
ver("   A' · serie correcta sin «fila»", d)

print("\nb) sin «fila», otra cifra de la misma página: 2025 = (57), «Total rent expense» de AR2025 p. 272 (no son intereses)")
d2 = copy.deepcopy(d)
d2["series"][SI]["2025"].update({"valor_fuente": -57, "literal": "(57)"})
ver("   B2 · (57) sin «fila»", d2)
d3 = copy.deepcopy(D)
d3["series"][SI]["2025"].update({"valor_fuente": -57, "literal": "(57)"})
ver("   C2 · (57) con «fila»", d3)

print("\nc) Ahold con las referencias mecánicas nuevas (réplica del dictamen; S2C del fase_b.json vigente)")
sys.path.insert(0, REP)
from motor import leer, RANGOS, base_del_libro, palancas_del_libro, motor, escalera, ESC  # noqa: E402
L = leer(os.path.join(ORIG, "recalc", "Ahold_v63_evaluada.xlsx"), RANGOS)
base, pal = base_del_libro(L), palancas_del_libro(L)
pj = json.load(open(os.path.join(ORIG, "precio.json"), encoding="utf-8"))
fb = json.load(open(os.path.join(ORIG, "fase_b.json"), encoding="utf-8"))
s2c = tuple(fb["palancas"]["s2c"][e]["valor"] for e in ESC)
for nombre, roic in (("referencias anteriores 0,09/0,09/0,09", (0.09, 0.09, 0.09)), ("referencias nuevas 0,09/0,09/0,12", (0.09, 0.09, 0.12)),
                     ("tope sin foso 0,09/0,12/0,12", (0.09, 0.12, 0.12))):
    pl = {e: dict(pal[e], s2c=s2c[i], roic=roic[i]) for i, e in enumerate(ESC)}
    V = [motor(**base, **pl[e])["por_accion"] for e in ESC]
    esc = escalera(V, pj["p"], pj["precio"], pj["k"])
    print(f"   {nombre:<40} S2C {s2c} · V {V[0]:.2f} / {V[1]:.2f} / {V[2]:.2f} · precio de Sí {esc['precio_si']:.2f} · ponderado {esc['ponderado']:.2f} · {esc['zona']} (precio {pj['precio']})")

print("\nd) fórmulas del libro (sin recalcular, solo lectura)")
import openpyxl  # noqa: E402
wb = openpyxl.load_workbook(os.path.join(ORIG, "recalc", "Ahold_v63_evaluada.xlsx"), data_only=False)
wv = openpyxl.load_workbook(os.path.join(ORIG, "recalc", "Ahold_v63_evaluada.xlsx"), data_only=True)
for hoja, celdas in (("Historia", ("A55", "C55", "A68", "C68")), ("Palancas", ("A9", "C9", "F18", "H18")),
                     ("Diagnóstico V6", ("A42", "B42", "C42", "D42", "E42", "A35", "B35", "C35", "D35"))):
    for c in celdas:
        f, v = wb[hoja][c].value, wv[hoja][c].value
        if f is None and v is None:
            continue
        print(f"   {hoja}!{c}: {str(f)[:230]!r}" + (f" => {str(v)[:150]!r}" if str(f).startswith("=") else ""))
