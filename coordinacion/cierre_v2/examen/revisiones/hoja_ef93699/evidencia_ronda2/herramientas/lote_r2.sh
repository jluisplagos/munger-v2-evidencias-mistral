#!/usr/bin/env bash
# (revisor, ronda 2) genera la hoja v2 en las copias completas de los expedientes reales
R=/tmp/claude-0/revision_hoja_r2; SC=$R/limpia/munger_v2_r1/personaje_v2/scripts
for n in "$@"; do
  exp=$(ls -d $R/exp/$n/*/ | head -1); exp=${exp%/}
  s=$(date +%s)
  TMPDIR=$R/tmp python3 -I -B $SC/hoja_resumen.py $exp --trabajo $R/tmp > $R/exp/$n/_salida.txt 2>&1; rc=$?
  echo "$n | código $rc | $(( $(date +%s) - s )) s | $(tail -1 $R/exp/$n/_salida.txt | cut -c1-260)"
done
