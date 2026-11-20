#!/usr/bin/env python3
"""Revisión R2 (revisor): ejecuta SIN CAMBIOS un guion de mi revisión R1 contra la capa de la RONDA 2.

Montaje (el mismo que usó el autor en resultados/guiones_de_la_revision_R1_contra_la_ronda_2.txt, repetido aquí por mi cuenta):
  - personaje_v2/scripts de la ronda 2 (copia de revisión de bcb6dc3);
  - la cabecera de ayudas de la batería de la RONDA 1 (git show 34b68fc:…/test_motor_a_f1_usgaap.py), que es la que usaban mis guiones;
  - dos alias en memoria (no en ningún archivo): _LINEA_ARR_OP → _LINEA_ARR y _LINEA_ARR_NO → _LINEA_SUPL (nombres que la ronda 2 retiró).
Uso: COPIA_REVISION=<r1h> python3 -B correr_guion_r1.py <guion.py> [argumentos del guion]
"""
import os
import runpy
import sys
import tempfile

TMP_R2 = os.environ.get("TMP_R2") or os.path.join(tempfile.gettempdir(), "rev_f1_usgaap_r2")
os.makedirs(TMP_R2, exist_ok=True)
tempfile.tempdir = TMP_R2
sys.dont_write_bytecode = True
guion = sys.argv[1]
sys.argv = sys.argv[1:]
sys.path.insert(0, os.path.dirname(os.path.abspath(guion)))
import ayudas  # noqa: E402  (el de la R1: lee COPIA_REVISION)
sys.path.insert(0, os.path.join(ayudas.PV, "scripts"))
import motor_a_f1 as M  # noqa: E402
if not hasattr(M, "_LINEA_ARR_OP"):
    M._LINEA_ARR_OP = M._LINEA_ARR
if not hasattr(M, "_LINEA_ARR_NO"):
    M._LINEA_ARR_NO = M._LINEA_SUPL
runpy.run_path(guion, run_name="__main__")
