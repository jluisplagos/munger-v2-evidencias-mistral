#!/usr/bin/env python3
"""Vuelca valores (caché) de un rango de un libro: uso volcar_hoja.py LIBRO HOJA RANGO [--formulas]"""
import sys, openpyxl
libro, hoja, rango = sys.argv[1:4]
formulas = "--formulas" in sys.argv
wb = openpyxl.load_workbook(libro, data_only=not formulas, read_only=True)
ws = wb[hoja]
for fila in ws[rango]:
    out = []
    for c in fila:
        if c.value is not None:
            v = c.value
            if isinstance(v, float):
                v = repr(v)
            out.append(f"{c.coordinate}={v}")
    if out:
        print(" | ".join(out))
