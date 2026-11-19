#!/bin/bash
# corre la capa vieja y la nueva sobre copias de los expedientes; salidas en /dev/shm/rev_m0/salidas/<caso>_<version>
set -u
O=/dev/shm/rev_m0/salidas; mkdir -p $O
casos=(
 "zoetis_t1c|/dev/shm/rev_m0/exp/zoetis_t1c/Zoetis|/dev/shm/rev_m0/exp/zoetis_t1c/Zoetis/recalc/Zoetis_v63_evaluada.xlsx|/dev/shm/rev_m0/exp/zoetis_t1c/Zoetis/Zoetis_v63_evaluada.xlsx"
 "ahold_f3|/dev/shm/rev_m0/exp/ahold_f3/Ahold|/dev/shm/rev_m0/exp/ahold_f3/Ahold/recalc/Ahold_v63_evaluada.xlsx|/dev/shm/rev_m0/exp/ahold_f3/Ahold/Ahold_v63_evaluada.xlsx"
 "jumbo_e|/dev/shm/rev_m0/exp/jumbo_e/Jumbo|/dev/shm/rev_m0/exp/jumbo_e/Jumbo/recalc/Jumbo_v63_evaluada.xlsx|/dev/shm/rev_m0/exp/jumbo_e/Jumbo/Jumbo_v63_evaluada.xlsx"
 "jumbo_f_heredado|/dev/shm/rev_m0/exp/jumbo_f/Jumbo|/dev/shm/rev_m0/exp/jumbo_f/antecedentes/heredados/recalc/Jumbo_v63_evaluada.xlsx|/dev/shm/rev_m0/exp/jumbo_f/antecedentes/heredados/Jumbo_v63_evaluada.xlsx"
 "elis_f1|/dev/shm/rev_m0/exp/elis_f1_wt_examen/Elis|/dev/shm/rev_m0/exp/elis_f1_wt_examen/Elis/recalc/Elis_v63_evaluada.xlsx|/dev/shm/rev_m0/exp/elis_f1_wt_examen/Elis/Elis_v63_evaluada.xlsx"
)
for c in "${casos[@]}"; do
  IFS='|' read -r n carpeta libro origen <<< "$c"
  for v in viejo nuevo; do
    d=$O/${n}_$v; rm -rf $d; mkdir -p $d
    python3 -B /dev/shm/rev_m0/$v/munger_v2_r1/personaje_v2/scripts/motor_a_f1.py evaluar "$carpeta" --libro "$libro" --motor A --libro-origen "$origen" --salida $d > $d/salida.txt 2>&1
    echo "rc=$?" >> $d/salida.txt
    echo "$n $v: $(tail -2 $d/salida.txt | tr '\n' ' ' | cut -c1-220)"
  done
done
