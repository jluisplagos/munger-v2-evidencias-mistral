#!/bin/bash
# Scripts de los revisores n.º 1 a 8, sin cambios, sobre C18 (árbol de trabajo del autor). En secuencia. El registro de
# control va a revisores_C18b.log, no a las salidas. Versión anterior: C8 para los revisores 1 a 5 (como sobre C16) y C16
# (worktree de C17) para los revisores 6 a 8.
S=<scratchpad>
RAIZ=<home>/e_work/wt_main414/munger_v2_r1
LIBRO=$RAIZ/personaje_v2/empresas_v2_correcciones/2026-11_Vidrala_ensayo_4_14/elis_decisiones/Elis/Elis_v63_evaluada.xlsx
F=<repo_producto>/docs/validacion_economica_paralela/frente_E_F1_elis
FR=docs/validacion_economica_paralela/frente_E_F1_elis
C8=$S/c14/wt_9744177/$FR; C17=$S/c18/wt_863ddde/$FR
R=$F/resultados; L=$S/c18/revisores_C18b.log; PY=$S/c16/pylibs; W=$S/c18/w
run() { local nombre=$1 salida=$2; shift 2; echo "== $nombre $(date -u +%H:%M:%S)" >> $L; "$@" > "$salida" 2>&1; echo "   código $?" >> $L; }
: > $L; mkdir -p $W
cd $F/revision/scripts_revisor && run mutantes $R/mutantes_revisor_sobre_C18.txt python3 -I -B prueba_mutantes.py --raiz $RAIZ --autor $F --libro $LIBRO
cd $F/revision/scripts_revisor_3 && run m3 $R/revisor3_prueba_mutantes_3_sobre_C18.txt python3 -I -B prueba_mutantes_3.py --raiz $RAIZ --autor $F --libro $LIBRO
run m3b $R/revisor3_prueba_mutantes_3b_sobre_C18.txt python3 -I -B prueba_mutantes_3b.py --raiz $RAIZ --autor $F --libro $LIBRO
run sondas3 $R/revisor3_sondas_sobre_C18.txt python3 -I -B sondas_revisor.py --raiz $RAIZ --libro $LIBRO --version C18=$F
cd $F/revision/scripts_revisor_4 && run c4 $R/revisor4_contraejemplos_4_sobre_C18.txt python3 -I -B contraejemplos_4.py --raiz $RAIZ --autor $F --libro $LIBRO
run ancla $R/revisor4_paginas_sin_ancla_sobre_C18.txt python3 -I -B paginas_sin_ancla.py --contraste $R/contraste_f1.json
cd $F/revision/scripts_revisor_5 && run c5 $R/revisor5_contraejemplos_5_sobre_C18.txt python3 -I -B contraejemplos_5.py --raiz $RAIZ --version C18=$F
run clases5 $R/revisor5_clases_5_sobre_C18.txt python3 -I -B clases_5.py --raiz $RAIZ --anterior C8=$C8 --nueva C18=$F
run barrido5 $W/b5.log python3 -I -B barrido_tablas.py --raiz $RAIZ --nueva $F --anterior $C8 --salida $W/b5 && cp $W/b5/barrido_tablas.txt $R/revisor5_barrido_tablas_sobre_C18.txt
run cobpropia $R/revisor5_cobertura_propia_sobre_C18.txt python3 -I -B cobertura_propia.py --autor $F --libro $LIBRO
cd $F/revision/scripts_revisor_6 && run c6 $R/revisor6_contraejemplos_6_sobre_C18.txt python3 -I -B contraejemplos_6.py --raiz $RAIZ --version C16=$C17 --version C18=$F
run barrido6 $W/b6.log python3 -I -B barrido_6.py --raiz $RAIZ --anterior C16=$C17 --nueva C18=$F --todas $W/todas6.jsonl.gz --salida $R/revisor6_barrido_6_sobre_C18.txt --procesos 4
run lectura6 $W/lectura6.log python3 -I -B lectura_geometrica.py --raiz $RAIZ --autor $F --todas $W/todas6.jsonl.gz --salida $W/lectura6.jsonl.gz --solo-grupo
run clases6 $R/revisor6_clases_6_sobre_C18.txt python3 -I -B clases_6.py --todas $W/todas6.jsonl.gz --lectura $W/lectura6.jsonl.gz --anterior C16 --nueva C18
run consultas6 $R/revisor6_consultas_6_sobre_C18.txt python3 -I -B consultas_6.py --raiz $RAIZ --todas $W/todas6.jsonl.gz --anterior C16=$C17 --nueva C18=$F
run cob6 $R/revisor6_cobertura_6_sobre_C18.txt python3 -I -B cobertura_6.py --raiz $RAIZ --autor $F --libro $LIBRO
run lectura12 $R/revisor6_lectura_filas_c12_sobre_C18.txt python3 -I -B lectura_filas_c12.py --raiz $RAIZ --autor $F
cd $F/revision/scripts_revisor_7 && run c7 $R/revisor7_contraejemplos_7_sobre_C18.txt python3 -I -B contraejemplos_7.py --raiz $RAIZ --version C16=$C17 --version C18=$F
run barrido7 $W/b7.log python3 -I -B barrido_7.py --raiz $RAIZ --c13 $C17 --c14 $F --pylibs $PY --todas $W/todas7.jsonl.gz --salida $R/revisor7_barrido_7_sobre_C18.txt --procesos 4
run clases7 $R/revisor7_clases_7_sobre_C18.txt python3 -I -B clases_7.py --todas $W/todas7.jsonl.gz --raiz $RAIZ --autor $F --pylibs $PY
run lectura14 $R/revisor7_lectura_filas_c14_sobre_C18.txt python3 -I -B lectura_filas_c14.py --raiz $RAIZ --autor $F --pylibs $PY
cd $F/revision/scripts_revisor_8 && run c8 $R/revisor8_contraejemplos_8_sobre_C18.txt python3 -I -B contraejemplos_8.py --raiz $RAIZ --version C16=$C17 --version C18=$F
run barrido8 $W/b8.log python3 -I -B barrido_8.py --raiz $RAIZ --c14 $C17 --c16 $F --todas $W/todas8.jsonl.gz --salida $R/revisor8_barrido_8_sobre_C18.txt
run clases8 $R/revisor8_clases_8_sobre_C18.txt python3 -I -B clases_8.py --todas $W/todas8.jsonl.gz --raiz $RAIZ --c14 $C17 --c16 $F --pylibs $PY
run consultas8 $R/revisor8_consultas_8_sobre_C18.txt python3 -I -B consultas_8.py --todas $W/todas8.jsonl.gz --raiz $RAIZ --c14 $C17 --c16 $F
run saldos8 $R/revisor8_lectura_saldos_8_sobre_C18.txt python3 -I -B lectura_saldos_8.py --todas $W/todas8.jsonl.gz --raiz $RAIZ --c16 $F
echo "fin $(date -u +%H:%M:%S)" >> $L
