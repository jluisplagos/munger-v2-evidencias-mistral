#!/usr/bin/env python3
"""Revisión R1 · compara los resultados del diferencial NIIF (base 1694f08 frente a la entrega 34b68fc). Uso: comparar_diferencial.py BASE.json NUEVO.json [SALIDA.txt]"""
import collections, json, sys
a, b = (json.load(open(p, encoding="utf-8")) for p in sys.argv[1:3])
out = []
assert [x["caso"] for x in a] == [x["caso"] for x in b]
iguales, distintos = 0, []
def aplanar(x, pref=""):
    if isinstance(x, dict):
        for k, v in x.items():
            yield from aplanar(v, f"{pref}/{k}")
    elif isinstance(x, list):
        for i, v in enumerate(x):
            yield from aplanar(v, f"{pref}[{i}]")
    else:
        yield pref, x
est = collections.Counter()
for x, y in zip(a, b):
    if x["resultado"] == y["resultado"]:
        iguales += 1
        continue
    fa, fb = dict(aplanar(x["resultado"])), dict(aplanar(y["resultado"]))
    difs = sorted(k for k in set(fa) | set(fb) if fa.get(k, "<ausente>") != fb.get(k, "<ausente>"))
    distintos.append((x["caso"], difs, fa, fb))
aplica = sum(1 for x in a if x["resultado"].get("aplica"))
util = sum(1 for x in a if x["resultado"].get("utilizable_para_conclusion"))
exc = sum(1 for x in a if "excepcion" in x["resultado"])
out.append(f"{len(a)} casos · con el motor A evaluado en la base: {aplica} · utilizables en la base: {util} · excepciones en la base: {exc}")
out.append(f"idénticos (todo el resultado salvo versión y fecha): {iguales} · distintos: {len(distintos)}")
for caso, difs, fa, fb in distintos:
    out.append(f"\n  DISTINTO · {caso} · {len(difs)} campos")
    for k in difs[:6]:
        out.append(f"      {k}\n         base : {str(fa.get(k, '<ausente>'))[:210]}\n         nuevo: {str(fb.get(k, '<ausente>'))[:210]}")
    ua, ub = fa.get("/utilizable_para_conclusion"), fb.get("/utilizable_para_conclusion")
    out.append(f"      utilizable: base {ua} → nuevo {ub} · estado: base {fa.get('/estado_propuesto')} → nuevo {fb.get('/estado_propuesto')}")
print("\n".join(out))
if len(sys.argv) > 3:
    open(sys.argv[3], "w", encoding="utf-8").write("\n".join(out) + "\n")
