#!/usr/bin/env python3
"""Revisión R1 · deja la COPIA de revisión como recién descomprimida: borra de munger_v2_r1/ todo archivo que no esté en MANIFIESTO_SHA256.txt
(salidas de pruebas, perfil de LibreOffice, __pycache__) y comprueba el manifiesto. Solo actúa sobre /home/user/e_work/revision_usgaap/copia."""
import hashlib, os, shutil, sys
R = "/home/user/e_work/revision_usgaap/copia/munger_v2_r1"
assert os.path.realpath(R).startswith("/home/user/e_work/revision_usgaap/copia/")
os.chdir(R)
esperado = {}
for l in open("MANIFIESTO_SHA256.txt", encoding="utf-8"):
    if l.strip() and not l.startswith("#"):
        h, p = l.rstrip("\n").split("  ", 1)
        esperado[p] = h
borrados = 0
for r, ds, fs in os.walk(".", topdown=False):
    for f in fs:
        p = os.path.relpath(os.path.join(r, f), ".")
        if p != "MANIFIESTO_SHA256.txt" and p not in esperado:
            os.remove(p); borrados += 1
    for d in ds:
        q = os.path.join(r, d)
        if os.path.isdir(q) and not os.listdir(q):
            os.rmdir(q)
mod = [p for p, h in esperado.items() if os.path.exists(p) and hashlib.sha256(open(p, "rb").read()).hexdigest() != h]
falt = [p for p in esperado if not os.path.exists(p)]
print(f"borrados {borrados} archivos que no están en el manifiesto · modificados {len(mod)} · ausentes {len(falt)}")
for p in (mod + falt)[:10]: print("  ", p)
sys.exit(0 if not (mod or falt) else 1)
