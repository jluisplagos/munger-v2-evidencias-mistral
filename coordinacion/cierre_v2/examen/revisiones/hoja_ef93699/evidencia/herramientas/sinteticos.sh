#!/usr/bin/env bash
# expedientes sintéticos producidos por el pipeline real con agentes simulados (cada prueba bajo flock del cerrojo común)
W=/tmp/claude-0/revision_hoja
cd $W/pkg/munger_v2_r1/personaje_v2
for t in sobrevive favorable datos_ausentes sin_base auditoria_repetir limite completa; do
  s=$(date +%s)
  TMPDIR=$W/tmp flock /home/user/e_work/libreoffice.lock python3 -B pruebas/test_pipeline_sintetico.py $t > $W/evid/sintetico_$t.txt 2>&1
  echo "$t rc=$? $(( $(date +%s) - s )) s · $(tail -1 $W/evid/sintetico_$t.txt)"
done
