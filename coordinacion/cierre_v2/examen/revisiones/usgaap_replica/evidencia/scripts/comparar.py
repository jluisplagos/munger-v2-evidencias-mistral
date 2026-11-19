import json, sys
def aplanar(x, p=""):
    out = {}
    if isinstance(x, dict):
        for k, v in x.items():
            out.update(aplanar(v, f"{p}/{k}"))
    elif isinstance(x, list):
        # las guardas por id
        if x and all(isinstance(e, dict) and "id" in e for e in x):
            for e in x:
                out.update(aplanar(e, f"{p}[{e['id']}]"))
        else:
            for i, v in enumerate(x):
                out.update(aplanar(v, f"{p}[{i}]"))
    else:
        out[p] = x
    return out
a = aplanar(json.load(open(sys.argv[1]))); b = aplanar(json.load(open(sys.argv[2])))
ign = {"/version", "/fecha", "/declaracion_ruta"}
solo_a = sorted(k for k in a if k not in b and k not in ign)
solo_b = sorted(k for k in b if k not in a and k not in ign)
dif = sorted(k for k in a if k in b and a[k] != b[k] and k not in ign)
print(f"  claves solo en viejo: {len(solo_a)}; solo en nuevo: {len(solo_b)}; valores distintos: {len(dif)}")
for k in solo_a: print("   - viejo:", k, "=", str(a[k])[:160])
for k in solo_b: print("   + nuevo:", k, "=", str(b[k])[:160])
lim = int(sys.argv[3]) if len(sys.argv) > 3 else 60
for k in dif[:lim]: print("   ≠", k, ":", str(a[k])[:150], "→", str(b[k])[:150])
if len(dif) > lim: print(f"   … {len(dif) - lim} más")
