#!/usr/bin/env python3
"""Revisión R1 de F1 · US GAAP (revisor, no autor). Ayudas comunes de los casos adversariales.

Carga las MISMAS ayudas de la batería del autor (libro, decl, serie, fuentes…) ejecutando solo la cabecera de
personaje_v2/pruebas/test_motor_a_f1_usgaap.py (hasta el primer bloque de pruebas), sobre la copia de revisión: así los libros
sintéticos y las declaraciones son los del autor y lo único nuevo son los casos. No toca la rama.
"""
import os
import sys

COPIA = os.environ.get("COPIA_REVISION", "/home/user/e_work/revision_usgaap/copia/munger_v2_r1")
PV = os.path.join(COPIA, "personaje_v2")
sys.dont_write_bytecode = True
sys.path.insert(0, os.path.join(PV, "scripts"))


def cargar():
    ruta = os.path.join(PV, "pruebas", "test_motor_a_f1_usgaap.py")
    src = open(ruta, encoding="utf-8").read()
    corte = src.index("# ================================================================== N ·")
    cab = src[:corte].replace("AQUI = os.path.dirname(os.path.abspath(__file__))", f"AQUI = {os.path.join(PV, 'pruebas')!r}")
    ns = {"__name__": "ayudas_autor", "__file__": ruta}
    exec(compile(cab, ruta, "exec"), ns)
    return ns
