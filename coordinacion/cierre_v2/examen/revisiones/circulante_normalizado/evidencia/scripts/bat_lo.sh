#!/bin/bash
# baterías con LibreOffice sobre la copia limpia de fbb146d: cada una con su propio flock, en secuencia
S=/tmp/claude-0/-home-user/b9d62468-c45b-5fe5-8762-d58eebe9c95a/scratchpad/rev/r4
R=/dev/shm/rev4/nuevo/munger_v2_r1
L=/home/user/e_work/libreoffice.lock
export TMPDIR=/dev/shm/rev4/tmp
corre() { n=$1; shift; s=$(date +%s); ( cd "$1" && shift && flock $L timeout 3000 "$@" ) > $S/bat/$n.txt 2>&1; echo "rc=$? · $(( $(date +%s) - s )) s" >> $S/bat/$n.txt; }
corre v632_estructura $R/v6/v632_f1/scripts python3 -I probar_v632_f1.py estructura
corre v632_a0 $R/v6/v632_f1/scripts python3 -I probar_v632_f1.py a0 /dev/shm/rev4/lo_v632_a0
corre v632_circ $R/v6/v632_f1/scripts python3 -I probar_v632_f1.py circ /dev/shm/rev4/lo_v632_circ
corre v632_pipeline $R/v6/v632_f1/scripts python3 -B prueba_pipeline_v632.py /dev/shm/rev4/pipeline_v632.txt
corre v631_f1 $R python3 -I v6/v631_f1/scripts/probar_v631_f1.py f1 /dev/shm/rev4/lo_v631_f1
corre v631_pipeline $R python3 -B v6/v631_f1/scripts/prueba_pipeline_v631.py /dev/shm/rev4/pipeline_v631.txt
corre gancho_f1 $R/personaje_v2 python3 -B empresas_v2_correcciones/2026-11_Vidrala_ensayo_4_15/f1_impl/scripts/prueba_pipeline_f1.py /dev/shm/rev4/gancho.txt
corre libro_v631_usgaap $R python3 -I personaje_v2/empresas_v2_correcciones/2026-11_Vidrala_ensayo_4_15/f1_usgaap/scripts/probar_libro_v631_usgaap.py /dev/shm/rev4/lo_usgaap
echo FIN > $S/bat/FIN
