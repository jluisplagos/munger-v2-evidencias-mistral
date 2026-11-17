"""S07: sondeo independiente de literales para la Propuesta §2.5 v3 (no reutiliza el script del autor).
Diferencias con el del autor: (1) todos los *.py del árbol de 3149128, no solo 145; (2) también *.sh (palabras entre comillas);
(3) comprueba la presencia por sección «## 3.» (como comprobar_entrega_4_9.py:217); (4) cuenta apariciones (no solo presencia).
Uso: python3 -I -B sondeo_independiente.py <candidata> <aux>. Solo lee con git show."""
import ast, re, subprocess, sys
C, A = sys.argv[1], sys.argv[2]
def show(repo, rev, p): return subprocess.run(["git","-C",repo,"show",f"{rev}:{p}"],capture_output=True,check=True).stdout.decode("utf-8","replace")
files = subprocess.run(["git","-C",C,"ls-tree","-r","--name-only","3149128"],capture_output=True,text=True,check=True).stdout.split("\n")
py = [f for f in files if f.endswith(".py")]; sh = [f for f in files if f.endswith(".sh")]
lits = {}; textos = {}
for f in py:
    t = show(C,"3149128",f); textos[f] = t
    try: tree = ast.parse(t)
    except SyntaxError: print("no analizable:", f); continue
    for n in ast.walk(tree):
        if isinstance(n, ast.Constant) and isinstance(n.value, str) and n.value: lits.setdefault(n.value,set()).add(f)
for f in sh:
    t = show(C,"3149128",f); textos[f] = t
    for m in re.finditer(r'"([^"\n]+)"|\'([^\'\n]+)\'', t):
        v = m.group(1) or m.group(2); lits.setdefault(v,set()).add(f)
print(f"archivos .py: {len(py)} · .sh: {len(sh)} · literales distintos: {len(lits)}")
cont = show(C,"3149128","munger_v2_r1/CONTINUIDAD.md")
prop = show(A,"88144b5","coordinacion/cierre_v2/manual/PROPUESTA_CONTINUIDAD_2_5.md")
q = [l[2:] for l in prop.split("\n") if l.startswith("> ")]
s1a, s1b, s2a, s2b, s2c = q
assert cont.count(s1a) == 1 and cont.count(s2a) == 1
nuevo = cont.replace(s1a, s1b, 1).replace(s2a, s2b, 1)
var = cont.replace(s1a, s1b, 1).replace(s2a, s2c, 1)
lectores = sorted(f for f in textos if "CONTINUIDAD" in textos[f])
print("archivos que nombran CONTINUIDAD:", len(lectores))
for f in lectores: print("   ", f.replace("munger_v2_r1/personaje_v2/empresas_v2_correcciones/","…/"))
def comparar(nombre, a, b):
    pres = sorted(l for l in lits if (l in a) != (l in b))
    cnt = sorted(l for l in lits if (l in a) and (l in b) and a.count(l) != b.count(l))
    a3, b3 = a.split("## 3.")[0], b.split("## 3.")[0]
    sec = sorted(l for l in lits if (l in a3) != (l in b3))
    print(f"\n{nombre}: cambian de presencia {len(pres)} {pres}")
    for l in pres:
        fs = sorted(lits[l]); rl = [f for f in fs if f in lectores]
        print(f"   {l!r}: en {len(fs)} archivos; de ellos nombran CONTINUIDAD: {len(rl)} {rl}")
    print(f"   cambian de presencia en §0–§2 (antes de «## 3.»): {len(sec)} {sec}")
    rc = [l for l in cnt if any(f in lectores for f in lits[l])]
    print(f"   cambian de número de apariciones: {len(cnt)}; de archivos que nombran CONTINUIDAD: {len(rc)}")
    for l in rc[:60]:
        print(f"      {l!r}: {a.count(l)} -> {b.count(l)} · {sorted(f.split('/')[-1] for f in lits[l] if f in lectores)}")
comparar("Propuesta v3, cambios 1 y 2", cont, nuevo)
comparar("Propuesta v3, cambio 1 y variante", cont, var)
# referencia: la frase nueva de la v2 (ef36ab1), para aislar el efecto de ${TMPDIR:-/tmp}
p2 = show(A,"ef36ab1","coordinacion/cierre_v2/manual/PROPUESTA_CONTINUIDAD_2_5.md")
q2 = [l[2:] for l in p2.split("\n") if l.startswith("> ")]
print("\ncitas en bloque de la Propuesta v2:", len(q2), "· frase 1 actual v2 == v3:", q2[0] == s1a, "· frase 2 actual v2 == v3:", q2[2] == s2a if len(q2) > 2 else None)
n2 = cont.replace(q2[0], q2[1], 1).replace(q2[2], q2[3], 1)
pres2 = sorted(l for l in lits if (l in cont) != (l in n2))
print("Propuesta v2, cambios 1 y 2 · cambian de presencia (con este universo):", len(pres2), pres2)
