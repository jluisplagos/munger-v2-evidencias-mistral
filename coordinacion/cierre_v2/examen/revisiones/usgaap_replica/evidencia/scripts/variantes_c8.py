"""Crea variantes del libro evaluado de zoetis_t1c (copia) cambiando Palancas C8 (y una con C49 incalculable). Solo escribe en /dev/shm."""
import os, shutil, sys
sys.path.insert(0, "/dev/shm/rev_m0/nuevo/munger_v2_r1/personaje_v2/scripts")
from v63_xml import LibroV63
ORIG = "/dev/shm/rev_m0/exp/zoetis_t1c/Zoetis/Zoetis_v63_evaluada.xlsx"
BASE = "/dev/shm/rev_m0/var"
VARS = {
    "v_control": {"Palancas!C8": "Media del ciclo"},
    "v_ultimo": {"Palancas!C8": "Último año"},
    "v_vacio": {"Palancas!C8": None},
    "v_minusculas": {"Palancas!C8": "media del ciclo"},
    "v_ciclo_c49vacia": {"Palancas!C8": "Media del ciclo", "Historia!C7": None},
}
for n, celdas in VARS.items():
    d = os.path.join(BASE, n); shutil.rmtree(d, ignore_errors=True); os.makedirs(d)
    lb = LibroV63(ORIG)
    for k, v in celdas.items():
        hoja, ref = k.split("!")
        lb.escribir(hoja, ref, v, tipo=("texto" if isinstance(v, str) else None))
        lb._modificadas.add(hoja)
    lb.borrar_caches()
    lb.guardar(os.path.join(d, "Zoetis_v63_evaluada.xlsx"))
    print("escrita", n, celdas)
