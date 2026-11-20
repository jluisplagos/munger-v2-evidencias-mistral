#!/usr/bin/env bash
# genera la hoja en copias (solo archivos de primer nivel) de una lista de expedientes
W=/tmp/claude-0/revision_hoja; SRC=/home/user/e_work/wt_hoja/munger_v2_r1/personaje_v2
cd $W/pkg/munger_v2_r1/personaje_v2
while IFS='|' read -r nombre ruta; do
  [ -z "$nombre" ] && continue
  $W/copiar_exp.sh "$SRC/$ruta" "$nombre" >/dev/null
  s=$(date +%s)
  TMPDIR=$W/tmp python3 -I scripts/hoja_resumen.py $W/exp/$nombre --trabajo $W/tmp > $W/exp/$nombre/_hoja_stdout.txt 2>&1
  rc=$?
  echo "$nombre | rc=$rc | $(( $(date +%s) - s )) s | $(tail -c 300 $W/exp/$nombre/_hoja_stdout.txt | tr '\n' ' ')"
done
