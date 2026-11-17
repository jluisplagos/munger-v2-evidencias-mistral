#!/bin/sh
# Diffs base->head de los 4 archivos (evidencia completa en diff_*.txt)
for n in material/base/*; do h="material/head/$(basename "$n")"; b=$(basename "$n"); diff -u "$n" "$h" > "diff_${b#munger_v2_r1_}.txt" || true; done
wc -l diff_*.txt
