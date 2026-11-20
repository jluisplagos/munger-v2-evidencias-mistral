"""Escala detectada por _escala_de_pagina en cada página de textos reales. Uso: python3 -B escanear_escalas.py <scripts> <txt>..."""
import sys, re, collections
sys.path.insert(0, sys.argv[1])
import motor_a_f1 as M
for f in sys.argv[2:]:
    t = open(f, encoding="utf-8", errors="replace").read()
    partes = re.split(r"\[PDF PAGE (\d+)\]\n", t)
    c = collections.Counter(); ej = {}
    for i in range(1, len(partes), 2):
        s = tuple(sorted(M._escala_de_pagina(partes[i + 1]))); c[s] += 1; ej.setdefault(s, []).append(partes[i])
    print(f.split("/")[-1], dict(c), {k: v[:6] for k, v in ej.items() if len(k) > 1 or k == ("millones",) and "jumbo" in f})
