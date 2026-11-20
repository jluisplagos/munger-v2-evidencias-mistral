"""Variante «paso 7» del libro de zoetis_t1c (copia): sin palancas (Palancas B14:D16, B18:D18) ni g para siempre (Análisis B68:D68)."""
import os, shutil, sys
sys.path.insert(0, "/dev/shm/rev_m0/nuevo/munger_v2_r1/personaje_v2/scripts")
from v63_xml import LibroV63
ORIG = "/dev/shm/rev_m0/exp/zoetis_t1c/Zoetis/Zoetis_v63_evaluada.xlsx"
d = "/dev/shm/rev_m0/var/v_paso7"; shutil.rmtree(d, ignore_errors=True); os.makedirs(d)
lb = LibroV63(ORIG)
for hoja, refs in (("Palancas", [f"{c}{r}" for c in "BCD" for r in (14, 15, 16, 18)]), ("Análisis", ["B68", "C68", "D68"])):
    for ref in refs:
        lb.escribir(hoja, ref, None); lb._modificadas.add(hoja)
lb.borrar_caches(); lb.guardar(os.path.join(d, "Zoetis_v63_evaluada.xlsx")); print("escrita v_paso7")
