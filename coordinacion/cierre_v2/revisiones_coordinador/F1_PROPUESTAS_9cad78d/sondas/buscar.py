"""Sonda del revisor: busca una expresión regular en el texto completo (pdftotext -layout) de una fuente y da la página PDF.
Uso: python3 -I buscar.py DOC 'regex' [contexto]"""
import re, sys
from pathlib import Path
doc, pat = sys.argv[1], sys.argv[2]
ctx = int(sys.argv[3]) if len(sys.argv) > 3 else 0
txt = (Path(__file__).resolve().parent / "textos" / f"{doc}.txt").read_text(encoding="utf-8")
pags = txt.split("\f")
rx = re.compile(pat, re.I)
for n, p in enumerate(pags, 1):
    ls = p.splitlines()
    for i, l in enumerate(ls):
        if rx.search(l):
            print(f"--- {doc} p.{n} l.{i}")
            for j in range(max(0, i - ctx), min(len(ls), i + ctx + 1)):
                print("   " + ls[j].rstrip()[:260])
