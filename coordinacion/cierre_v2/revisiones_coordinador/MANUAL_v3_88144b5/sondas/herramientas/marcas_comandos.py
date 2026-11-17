"""S05: cada línea de comando en bloque del manual v3 y la marca de origen más cercana (párrafo anterior o siguiente).
Uso: python3 -I -B marcas_comandos.py MANUAL.md"""
import re, sys
L = open(sys.argv[1], encoding="utf-8").read().split("\n")
MARCAS = [("literal de la fuente, no probado", "LIT-NP"), ("literal de la fuente", "LIT"), ("probado en el traspaso", "TRASP"),
          ("probada en el traspaso", "TRASP"), ("probado en la preparación F1", "F1"), ("NO DOCUMENTADO", "ND"), ("adaptad", "ADAPT")]
def marcas(t):
    s = t.lower(); out = []
    for k, v in MARCAS:
        if k.lower() in s and v not in out: out.append(v)
    return out
infence = False; bloques = []; cur = []
for i, l in enumerate(L):
    if l.startswith("```"):
        infence = not infence
        if not infence and cur: bloques.append(cur); cur = []
        continue
    es_cmd = infence or (re.match(r"^ {4,}\S", l) and not re.match(r"^ {0,8}[-|*]|^ {2,}\d+\.", l.lstrip(" ")[:0] + l) and not l.strip().startswith(("-", "|", "*")))
    if es_cmd and l.strip() and not l.strip().startswith("#"):
        cur.append((i + 1, l.strip()))
    elif cur and not infence:
        bloques.append(cur); cur = []
def parrafo(i, paso):
    j = i
    while 0 <= j < len(L) and not L[j].strip(): j += paso
    txt = []
    while 0 <= j < len(L) and L[j].strip() and not re.match(r"^ {4,}\S", L[j]) or (0 <= j < len(L) and L[j].strip() and L[j].lstrip().startswith(("-", "«", "*"))):
        txt.append(L[j]); j += paso
        if len(txt) > 3: break
    return " ".join(txt)
n = 0; sin = 0
for b in bloques:
    ini, fin = b[0][0], b[-1][0]
    antes = parrafo(ini - 2, -1); despues = parrafo(fin, 1)
    ma, md = marcas(antes), marcas(despues)
    for ln, c in b:
        n += 1
    tag = "OK" if (ma or md) else "SIN MARCA"
    if not (ma or md): sin += len(b)
    print(f"L{ini}-{fin} ({len(b)} líneas) · antes {ma} · después {md} · {tag}")
    for ln, c in b: print(f"    {ln}: {c[:150]}")
print(f"\nlíneas de comando en bloque: {n} · sin marca en el párrafo anterior ni en el siguiente: {sin}")
