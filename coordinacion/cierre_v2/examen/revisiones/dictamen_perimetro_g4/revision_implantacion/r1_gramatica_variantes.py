"""Revisión de la implantación de P-FOSO (rama f1/perimetro-foso @ 688df46) · R1: la gramática NUEVA del producto sobre copias del
expediente de Ahold con cada juego de palancas del dictamen. No escribe en el repositorio: trabaja en carpetas temporales.
Uso: r1_gramatica_variantes.py RAIZ_PERSONAJE_V2 COPIA_EXPEDIENTE_CON_DATOS_NUEVOS"""
import copy, json, os, shutil, subprocess, sys, tempfile

PV, EXP = sys.argv[1], sys.argv[2]
ESC = ("MALO", "NORMAL", "BUENO")
fb0 = json.load(open(os.path.join(EXP, "fase_b.json"), encoding="utf-8"))
refs = json.load(open(os.path.join(EXP, "referencias_mecanicas.json"), encoding="utf-8"))
print("referencias mecánicas nuevas · roic_lp:", {e: refs["palancas"]["roic_lp"][e] for e in ESC}, "· s2c:", {e: refs["palancas"]["s2c"][e] for e in ESC})


def variante(nombre, s2c, roic, c18=None, quitar_just=("G4", "G7")):
    fb = copy.deepcopy(fb0)
    for i, e in enumerate(ESC):
        fb["palancas"]["s2c"][e]["valor"] = s2c[i]
        x = fb["palancas"]["roic_lp"][e]
        ref = refs["palancas"]["roic_lp"][e]
        x["valor"], x["referencia_mecanica"], x["desviacion"] = roic[i], ref, round(roic[i] - ref, 10)
    fb["desviaciones_justificadas"] = [j for j in fb.get("desviaciones_justificadas") or [] if j.get("comprobacion") not in quitar_just]
    tmp = tempfile.mkdtemp(prefix="rev_pfoso_")
    try:
        for n in ("fase_a.json", "referencias_mecanicas.json", "datos_v63.json"):
            shutil.copy(os.path.join(EXP, n), os.path.join(tmp, n))
        if c18:
            d = json.load(open(os.path.join(tmp, "datos_v63.json"), encoding="utf-8"))
            d["analisis"]["C18"] = c18
            json.dump(d, open(os.path.join(tmp, "datos_v63.json"), "w", encoding="utf-8"), ensure_ascii=False)
        json.dump(fb, open(os.path.join(tmp, "fase_b.json"), "w", encoding="utf-8"), ensure_ascii=False)
        r = subprocess.run([sys.executable, "-B", os.path.join(PV, "scripts", "comprobar_gramatica.py"), tmp, "--antes-de-recalculo", "--config",
                            os.path.join(PV, "config_v2_v631_f1.json")], capture_output=True, text=True)
        g = json.load(open(os.path.join(tmp, "gramatica.json"), encoding="utf-8"))
        hs = [f"{h['id']} {h['escenario'] or ''}{'' if not h['requiere_justificacion'] else (' ✓' if h['justificada'] else ' ✗')}" for h in g["hallazgos"]]
        print(f"{nombre:<52} S2C {s2c} ROIC {roic} C18 {c18 or 'No'} → código {r.returncode}: {'; '.join(hs) or '—'}")
        return g
    finally:
        shutil.rmtree(tmp, ignore_errors=True)


S = (3.9, 5.4, 5.9)
variante("referencias nuevas tal cual (0,09/0,09/0,12)", S, (0.09, 0.09, 0.12))
variante("referencia del dictamen (0,09/0,09/0,09)", S, (0.09, 0.09, 0.09))
variante("tope sin foso (0,09/0,12/0,12)", S, (0.09, 0.12, 0.12))
variante("vigente (0,13/0,15/0,15), C18 = No", S, (0.13, 0.15, 0.15))
g = variante("vigente (0,13/0,15/0,15), C18 = Sí, sin justificar", S, (0.13, 0.15, 0.15), c18="Sí")
variante("S2C de todo el capital (2,5/3,2/3,5) y 0,08/0,09/0,09", (2.5, 3.2, 3.5), (0.08, 0.09, 0.09))
variante("S2C 9,0 en el BUENO (rentabilidad 0,318 > 0,296)", (3.9, 5.4, 9.0), (0.09, 0.09, 0.12))
variante("S2C 7,6 en el BUENO (0,269: entre 2×C55 y 2×perímetro)", (3.9, 5.4, 7.6), (0.09, 0.09, 0.12))
print("\ntexto del hallazgo G4 con C18 = Sí:", [h["detalle"] for h in g["hallazgos"] if h["id"] == "G4"][0][:400])
