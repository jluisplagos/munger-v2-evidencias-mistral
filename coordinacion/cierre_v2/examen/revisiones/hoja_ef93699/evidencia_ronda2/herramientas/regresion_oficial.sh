#!/usr/bin/env bash
# (revisor, ronda 2) baterías oficiales que tocan cierre, vigencia y pipeline, en la copia limpia de 6406a99; cada una bajo flock del cerrojo común
R=/tmp/claude-0/revision_hoja_r2; P=$R/limpia/munger_v2_r1
cd $P/personaje_v2
correr() { nombre="$1"; shift; s=$(date +%s); ( "$@" ) > $R/evid/regresion_$nombre.txt 2>&1; rc=$?; echo "$nombre · código $rc · $(( $(date +%s) - s )) s · $(grep -E 'PASAN|FALLAN' $R/evid/regresion_$nombre.txt | tail -1)"; }
L=/home/user/e_work/libreoffice.lock
for t in test_cierre_v2 test_vigencia_h5 test_estados_v2 test_auditorias_v2 test_integridad_auditoria_v2 test_resumen_v2 test_trazabilidad_v2 test_relevo_i19_415; do
  correr $t env TMPDIR=$R/tmp flock $L python3 -B pruebas/$t.py
done
correr prueba_pipeline_f1 env TMPDIR=$R/tmp flock $L python3 -B empresas_v2_correcciones/2026-11_Vidrala_ensayo_4_15/f1_impl/scripts/prueba_pipeline_f1.py
( cd $P && correr prueba_pipeline_v631 env TMPDIR=$R/tmp flock $L python3 -B v6/v631_f1/scripts/prueba_pipeline_v631.py )
correr test_pipeline_sintetico env TMPDIR=$R/tmp flock $L python3 -B pruebas/test_pipeline_sintetico.py
correr test_integracion_v64 env TMPDIR=$R/tmp flock $L python3 -B pruebas/test_integracion_v64.py
