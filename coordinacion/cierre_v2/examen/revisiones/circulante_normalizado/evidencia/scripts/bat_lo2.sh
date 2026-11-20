#!/bin/bash
S=/tmp/claude-0/-home-user/b9d62468-c45b-5fe5-8762-d58eebe9c95a/scratchpad/rev/r4
R=/dev/shm/rev4/nuevo/munger_v2_r1
L=/home/user/e_work/libreoffice.lock
export TMPDIR=/dev/shm/rev4/tmp
until [ -f $S/bat/FIN ]; do sleep 5; done
corre() { n=$1; shift; s=$(date +%s); ( cd "$1" && shift && flock $L timeout 3600 "$@" ) > $S/bat3/$n.txt 2>&1; echo "rc=$? · $(( $(date +%s) - s )) s" >> $S/bat3/$n.txt; }
corre diagnostico_vinci $R python3 -I personaje_v2/empresas_v2_correcciones/2026-11_Vidrala_ensayo_4_15/f1_circulante/scripts/diagnostico_vinci_circulante.py /home/user/e_work/wt_expedientes/munger_v2_r1/personaje_v2/empresas_v2_correcciones/2026-11_examen_universo/vinci/Vinci /dev/shm/rev4/diag_vinci --salida $S/vinci_diag
corre test_cierre_v2 $R/personaje_v2 python3 -B pruebas/test_cierre_v2.py
corre test_verificacion_entradas_415 $R/personaje_v2 python3 -B pruebas/test_verificacion_entradas_415.py
corre reparacion_completa $R/personaje_v2 bash pruebas/ejecutar_pruebas_reparacion.sh
corre test_integracion_v64 $R/personaje_v2 python3 -B pruebas/test_integracion_v64.py
echo FIN > $S/bat3/FIN
