"""S06 · Revision de los 3 scripts SIN ejecutarlos (no hay .trabajo/ ni red aqui) y del texto de la entrega.
- Extrae la tabla CITAS de lectura_bloque2.py con ast.literal_eval (sin ejecutar el script) y comprueba
  si cada 'cita' registrada en LECTURA_FUENTES.jsonl casa con su propio patron (detecta truncado y alternativas).
- Señala dependencias de entorno de cada script (rutas .trabajo, commits ausentes, red).
- Rehace por separado la comprobacion cruzada del bloque 1 (fuentes.json @716cbd6 del producto frente a
  seleccion_fuentes.json @f5775dc del auxiliar) con git show de solo lectura.
- Recuenta la redaccion 'no localizado en esta busqueda' frente a afirmaciones absolutas de no publicacion.

Uso: python3 -I s06_scripts_y_texto.py <dir_entrega> <repo_producto> <repo_auxiliar> <salida.json>
"""
import ast
import json
import re
import subprocess
import sys
import unicodedata
from pathlib import Path

ent, prod, aux, salida = Path(sys.argv[1]), sys.argv[2], sys.argv[3], sys.argv[4]
out = {}
src = (ent / "scripts/lectura_bloque2.py").read_text(encoding="utf-8")
tree = ast.parse(src)
CITAS = None
for node in tree.body:
    if isinstance(node, ast.Assign) and getattr(node.targets[0], "id", "") == "CITAS":
        CITAS = ast.literal_eval(node.value)
regs = [json.loads(l) for l in open(ent / "LECTURA_FUENTES.jsonl", encoding="utf-8") if l.strip()]
citas = [r for r in regs if r["tipo"] == "cita"]
assert CITAS is not None and len(CITAS) == len(citas) == 28
res = []
for i, ((preg, fid, pag, patron, hall, nod, sal), c) in enumerate(zip(CITAS, citas), 1):
    assert (preg, fid, pag) == (c["pregunta"], c["documento"], c["pagina_pdf"])
    p = patron.replace(" ", r"\s+")
    casa = re.search(p, c["cita"], re.IGNORECASE | re.DOTALL) is not None
    alternativa = "|" in patron
    greedy = ".*" in patron
    res.append({"n": i, "doc": fid, "pag": pag, "cita_casa_con_su_patron": casa, "patron_con_alternativa": alternativa,
                "patron_con_.*": greedy, "longitud_cita": len(c["cita"]), "truncada_400": len(c["cita"]) >= 400})
    if not casa or alternativa or len(c["cita"]) >= 400:
        print(f"cita {i:2d} {fid} p{pag}: casa_con_patron={casa} alternativa={alternativa} .*={greedy} len={len(c['cita'])}")
        print("   patron:", patron)
        print("   cita  :", c["cita"][:160], "...")
        print("   hallazgo:", hall[:200])
out["citas_patron"] = res
print("citas con '.*' en el patron:", sum(r["patron_con_.*"] for r in res))

# dependencias de entorno
dep = {}
for s in ["inventario_bloque1.py", "descargar_fuentes_elis.py", "lectura_bloque2.py"]:
    t = (ent / "scripts" / s).read_text(encoding="utf-8")
    dep[s] = {"usa_.trabajo": ".trabajo" in t, "red_urllib": "urllib.request" in t, "git_show": "git\", \"-C\"" in t or "git_show(" in t,
              "mkdir": "mkdir" in t, "abre_en_modo_w_salida": "open(\"w\"" in t or ".open(\"w\"" in t,
              "lee_y_reescribe_csv_propio": s == "lectura_bloque2.py" and "campos += [" in t and "for r in fr:" in t}
out["dependencias"] = dep
print("dependencias:", json.dumps(dep, indent=None))


def gtype(repo, obj):
    r = subprocess.run(["git", "-C", repo, "cat-file", "-t", obj], capture_output=True, text=True)
    return r.stdout.strip() or "AUSENTE"


out["objetos"] = {"716cbd6 en auxiliar": gtype(aux, "716cbd6794b7fcde8b3862c9d1e7acdaf516d262"),
                  "716cbd6 en producto": gtype(prod, "716cbd6794b7fcde8b3862c9d1e7acdaf516d262"),
                  "f5775dc en auxiliar": gtype(aux, "f5775dc07a61b829df2b0e7a4a97c556869ae0f4"),
                  "ff0c60cd en auxiliar": gtype(aux, "ff0c60cd2901c42f9462acd19ed74c4192a13bfb")}
print("objetos:", out["objetos"])
f = json.loads(subprocess.run(["git", "-C", prod, "show", "716cbd6794b7fcde8b3862c9d1e7acdaf516d262:docs/validacion_economica_paralela/frente_E_F1_elis/datos/fuentes.json"], capture_output=True, text=True).stdout)
sel = json.loads(subprocess.run(["git", "-C", aux, "show", "f5775dc07a61b829df2b0e7a4a97c556869ae0f4:revision_externa/f1_v3_20261116/seleccion_fuentes.json"], capture_output=True, text=True).stdout)
by = {a["ruta"]: a for a in sel["archivos"]}
cruce = {tag: by[info["archivo"]]["sha256"] == info["sha256"] for tag, info in list(f["fuentes"].items()) + [("libro", f["libro"])]}
out["cruce_bloque1"] = cruce
print("cruce fuentes.json@716cbd6 vs seleccion_fuentes.json@f5775dc:", cruce)
csvf = (ent / "FUENTES_Y_BUSQUEDA.csv").read_text(encoding="utf-8")
out["csv_contiene_hashes_base"] = {tag: info["sha256"] in csvf for tag, info in list(f["fuentes"].items()) + [("libro", f["libro"])]}
print("FUENTES_Y_BUSQUEDA.csv contiene las 6 huellas base:", out["csv_contiene_hashes_base"])

# redaccion
def n(s):
    return unicodedata.normalize("NFC", s)
cuenta = {}
for p in sorted(ent.rglob("*")):
    if p.is_file() and p.suffix in (".md", ".csv", ".json", ".jsonl"):
        t = n(p.read_text(encoding="utf-8")).lower()
        cuenta[str(p.relative_to(ent))] = {
            "no_localizado_en_esta_busqueda": len(re.findall(r"no localizad[oa] en esta b[uú]squeda", t)),
            "no_publicad[oa]/sin publicar(se)": re.findall(r"[^.;|\n]{0,60}(?:no (?:est[aá] )?publicad[oa]|sin publicar(?:se)?|sigue sin publicar(?:se)?|no se publica)[^.;|\n]{0,40}", t),
            "ninguna_parte": len(re.findall(r"ninguna parte", t))}
out["redaccion"] = cuenta
for k, v in cuenta.items():
    print(k, "| 'no localizado en esta busqueda':", v["no_localizado_en_esta_busqueda"], "| 'ninguna parte':", v["ninguna_parte"])
    for frase in v["no_publicad[oa]/sin publicar(se)"]:
        print("     absoluta:", frase.strip()[:150])
Path(salida).write_text(json.dumps(out, ensure_ascii=False, indent=1), encoding="utf-8")
