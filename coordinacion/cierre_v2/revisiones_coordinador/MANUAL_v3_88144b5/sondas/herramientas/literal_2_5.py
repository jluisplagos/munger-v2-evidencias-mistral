"""S06: frases de CONTINUIDAD §2.5 en la Propuesta v3 frente a la candidata y frente al script del sondeo (byte a byte).
Uso: python3 -I -B literal_2_5.py <candidata> <aux> ; solo lee (git show)."""
import subprocess, sys, re, ast
C, A = sys.argv[1], sys.argv[2]
def show(repo, rev, p): return subprocess.run(["git","-C",repo,"show",f"{rev}:{p}"],capture_output=True,check=True).stdout.decode("utf-8")
cont = show(C, "3149128", "munger_v2_r1/CONTINUIDAD.md")
prop = show(A, "88144b5", "coordinacion/cierre_v2/manual/PROPUESTA_CONTINUIDAD_2_5.md")
scr = show(A, "88144b5", "coordinacion/cierre_v2/manual/sondeo_literales_v3/sondeo_literales_v3.py")
quotes = [l[2:] for l in prop.split("\n") if l.startswith("> ")]
print("citas en bloque de la Propuesta:", len(quotes))
nombres = ["frase 1 actual", "frase 1 nueva", "frase 2 actual", "frase 2 nueva", "frase 2 variante"]
for n, q in zip(nombres, quotes):
    print(f"- {n}: {len(q.encode())} bytes · apariciones en CONTINUIDAD.md@3149128: {cont.count(q)} · línea(s): {[i+1 for i,l in enumerate(cont.split(chr(10))) if q in l]}")
# constantes del script
t = ast.parse(scr); vals = {}
for node in ast.walk(t):
    if isinstance(node, ast.Assign) and len(node.targets)==1 and isinstance(node.targets[0], ast.Name) and node.targets[0].id in ("s1a","s1b","s2a","s2b","s2c"):
        vals[node.targets[0].id] = ast.literal_eval(node.value)
for k, q in zip(("s1a","s1b","s2a","s2b","s2c"), quotes):
    print(f"  script {k} == cita de la Propuesta: {vals.get(k) == q}")
# frase 1 nueva: ¿la frase 1 actual de la 957af65 era la misma? y la candidata conserva la frase original (no aplicada)
c957 = show(C, "957af65", "munger_v2_r1/CONTINUIDAD.md")
print("frase 1 actual en 957af65:", c957.count(quotes[0]), "· frase 2 actual en 957af65:", c957.count(quotes[2]))
print("¿frase 1 nueva ya presente en la candidata (aplicada)?", cont.count(quotes[1]))
print("¿'antes de los controles de la 4.8 y la 4.8.1' en la candidata?", "antes de los controles de la 4.8" in cont)
