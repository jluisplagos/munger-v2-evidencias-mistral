"""Qué texto dispara cada marca de escala en las páginas cuya escala detectada es una sola y no la del informe. Uso: <scripts> <txt> <escala_real>"""
import sys, re
sys.path.insert(0, sys.argv[1])
import motor_a_f1 as M
t = open(sys.argv[2], encoding="utf-8", errors="replace").read(); real = sys.argv[3]
partes = re.split(r"\[PDF PAGE (\d+)\]\n", t)
for i in range(1, len(partes), 2):
    s = M._escala_de_pagina(partes[i + 1])
    if s and real not in s:
        tt = re.sub(r"\s+", " ", partes[i + 1]).lower()
        hits = [(esc, m.group(0), tt[max(0, m.start()-50):m.end()+30]) for esc, pats in M.MARCAS_ESCALA.items() for p in pats for m in [re.search(p, tt)] if m]
        print("p.", partes[i], sorted(s), "· tabla con cifras:", bool(re.search(r"\d{1,3}(?:,\d{3})+|\(\d", partes[i+1])))
        for h in hits[:2]: print("    ", h[0], "«", h[2], "»")
