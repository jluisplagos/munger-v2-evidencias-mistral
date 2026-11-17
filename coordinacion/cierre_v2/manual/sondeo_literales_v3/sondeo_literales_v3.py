#!/usr/bin/env python3
"""Sondeo de literales para el manual v3 (m9 de REVISION_MANUAL_v2_ef36ab1.md) y para PROPUESTA_CONTINUIDAD_2_5.md.

Parte de `revisiones_coordinador/MANUAL_v2_ef36ab1/sondas/herramientas/sonda_literales.py` (la herramienta de la revisión) y añade:
  - las frases nuevas de la propuesta en su redacción de v3 (cambio 1 ampliado al 4.8; temporal citado como ${TMPDIR:-/tmp});
  - para cada literal que cambia de presencia, en qué scripts está, si el script es uno de los 19 controles de
    controles_historicos_4_13.py, si el script nombra CONTINUIDAD y qué controles lo nombran (lo llaman o lo leen).

Qué es un «literal»: toda constante de texto no vacía (ast.Constant de tipo str; en una f-string, cada trozo fijo) de los scripts
*.py de munger_v2_r1/personaje_v2/empresas_v2_correcciones/*/scripts/, munger_v2_r1/personaje_v2/pruebas/ y
munger_v2_r1/contrastes/*/scripts/ en 3149128. «Cambia de presencia» = está en un texto de CONTINUIDAD.md y no en el otro.
Solo lee con `git show`; no ejecuta nada del producto ni escribe nada.

Uso: python3 -I -B sondeo_literales_v3.py RUTA_DEL_REPOSITORIO_DE_LA_CANDIDATA   (o la variable CAND)
"""
import ast
import os
import re
import subprocess
import sys

C = sys.argv[1] if len(sys.argv) > 1 else os.environ["CAND"]
REV = "3149128"


def show(rev, p):
    return subprocess.run(["git", "-C", C, "show", f"{rev}:{p}"], capture_output=True, check=True).stdout.decode("utf-8")


files = subprocess.run(["git", "-C", C, "ls-tree", "-r", "--name-only", REV], capture_output=True, text=True, check=True).stdout.split("\n")
pat = re.compile(r"^munger_v2_r1/(personaje_v2/empresas_v2_correcciones/[^/]+/scripts/|personaje_v2/pruebas/|contrastes/[^/]+/scripts/).*\.py$")
sel = [f for f in files if pat.match(f)]
lits = {}
textos = {}
for f in sel:
    t = show(REV, f)
    textos[f] = t
    try:
        arbol = ast.parse(t)
    except SyntaxError as e:
        print("no se puede analizar", f, e)
        continue
    for n in ast.walk(arbol):
        if isinstance(n, ast.Constant) and isinstance(n.value, str) and n.value:
            lits.setdefault(n.value, set()).add(f)

# los 19 controles que lanza controles_historicos_4_13.py (lista CONTROLES)
CH = "munger_v2_r1/personaje_v2/empresas_v2_correcciones/2026-11_Vidrala_ensayo_4_13/scripts/controles_historicos_4_13.py"
ch = show(REV, CH)
pref = "personaje_v2/empresas_v2_correcciones/"
controles = []
for m in re.finditer(r'\("([0-9a-z_]+)", (C \+ )?"([^"]+\.py)"', ch):
    controles.append("munger_v2_r1/" + (pref if m.group(2) else "") + m.group(3))

c957 = show("957af65", "munger_v2_r1/CONTINUIDAD.md")
cact = show(REV, "munger_v2_r1/CONTINUIDAD.md")

s1a = "Si falta espacio, terminada la verificación se pueden borrar los `*.xlsx` y `vigencia/` de `personaje_v2/pruebas/_v64/` (los controles no recorren `_v64/`), registrando las rutas (regla 11.10)."
s1b = ("Si falta espacio, terminada la verificación se pueden borrar los `*.xlsx` y `vigencia/` de `personaje_v2/pruebas/_v64/`, registrando las rutas (regla 11.10). "
       "Hay que hacerlo antes de los controles de la 4.8 y la 4.8.1: los dos copian `personaje_v2/` con `pruebas/_v64/` en el temporal del sistema "
       "(`${TMPDIR:-/tmp}`; `comprobar_entrega_4_8.py`, función `arbol_codigo_471`, y `comprobar_entrega_4_8_1.py`, función `arbol`). "
       "El de la 4.8.1 no evalúa su contenido.")
s2a = "Conviene tener al menos 7 GB libres después de descomprimir."
s2b = ("Conviene tener al menos 7 GB libres después de descomprimir. En la prueba de traspaso de la 4.15 (vía del repositorio, 17-nov-2026), unos 8,4 GB libres "
       "al empezar los controles no bastaron para el de la 4.8.1; tras la limpieza que sigue, con unos 13 GB, terminó con el mismo resultado que en el árbol 4.14 (25 de 30).")
s2c = ("Conviene tener al menos 7 GB libres después de descomprimir. En la prueba de traspaso de la 4.15 (vía del repositorio) esa cantidad no bastó para el control "
       "de la 4.8.1, que terminó después de la limpieza que sigue.")

print(f"scripts analizados: {len(sel)} · literales distintos: {len(lits)} · controles de controles_historicos_4_13.py: {len(controles)}")
print(f"controles que existen en {REV}: {sum(1 for c in controles if c in textos)} de {len(controles)}")
print("frase 1 actual en CONTINUIDAD.md:", cact.count(s1a), "vez/veces · frase 2 actual:", cact.count(s2a), "vez/veces")
nuevo = cact.replace(s1a, s1b, 1).replace(s2a, s2b, 1)
variante = cact.replace(s1a, s1b, 1).replace(s2a, s2c, 1)


def informe(nombre, a, b):
    d = sorted(l for l in lits if (l in a) != (l in b))
    print(f"\n{nombre}: literales que aparecen o desaparecen = {len(d)}")
    for l in d:
        fs = sorted(lits[l])
        print(f"  {l!r}: {'aparece' if l in b else 'desaparece'}")
        for f in fs:
            base = os.path.basename(f)
            en19 = f in controles
            nombra_cont = "CONTINUIDAD" in textos[f]
            lo_nombran = sorted(os.path.basename(c) for c in controles if c in textos and c != f and base in textos[c])
            lineas = [i + 1 for i, x in enumerate(textos[f].splitlines()) if l in x]
            print(f"    {f}:{','.join(map(str, lineas))} · ¿uno de los 19 controles? {'sí' if en19 else 'no'}"
                  f" · ¿nombra CONTINUIDAD? {'sí' if nombra_cont else 'no'} · controles que lo nombran: {', '.join(lo_nombran) or 'ninguno'}")
    en19 = [l for l in d if lits[l] & set(controles)]
    lec = [l for l in d if any("CONTINUIDAD" in textos[f] for f in lits[l])]
    print(f"  filtro A · literales de los 19 controles: {len(en19)} {en19}")
    print(f"  filtro B · literales de scripts que nombran CONTINUIDAD: {len(lec)} {lec}")
    return d


informe("957af65 -> 3149128 (CONTINUIDAD.md)", c957, cact)
informe("propuesta v3: cambios 1 y 2", cact, nuevo)
informe("propuesta v3: cambio 1 y variante del 2", cact, variante)
lec = sorted(f for f in sel if "CONTINUIDAD" in textos[f])
print(f"\nscripts que nombran CONTINUIDAD: {len(lec)} (de ellos, entre los 19 controles: {sum(1 for f in lec if f in controles)})")
for f in lec:
    print("  ", f, "· control" if f in controles else "")
