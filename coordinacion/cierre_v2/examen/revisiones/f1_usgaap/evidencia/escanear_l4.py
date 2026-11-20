#!/usr/bin/env python3
"""Revisión R1 de F1 · US GAAP: valores de Control maestro L4 en todos los libros .xlsx de un árbol (solo lectura)."""
import collections, json, os, sys, zipfile, re
import openpyxl
raiz = sys.argv[1]
vals = collections.Counter()
det = collections.defaultdict(list)
n = 0
for r, ds, fs in os.walk(raiz):
    ds[:] = [d for d in ds if d not in ("__pycache__", ".git", ".lo_perfil")]
    for f in fs:
        if not f.endswith(".xlsx") or f.startswith("~"):
            continue
        p = os.path.join(r, f)
        try:
            wb = openpyxl.load_workbook(p, data_only=True, read_only=True)
            if "Control maestro" not in wb.sheetnames:
                wb.close(); continue
            v = wb["Control maestro"]["L4"].value
            k4 = wb["Control maestro"]["K4"].value
            wb.close()
        except Exception as e:  # noqa
            vals[f"<ilegible: {type(e).__name__}>"] += 1
            continue
        n += 1
        vals[repr(v)] += 1
        det[repr(v)].append(os.path.relpath(p, raiz))
print("libros con Control maestro:", n)
for k, c in vals.most_common():
    print(c, k)
    if c <= 12:
        for x in det[k][:12]:
            print("     ", x)
