#!/bin/sh
# Sondas sobre el codigo y los registros de 957af65 (solo lectura, API GitHub) para comprobar
# que cada correccion del commit c0542b83 es cierta en 957af65. Salida: grep/sed con numeros de linea.
BASE=957af652cdc3bef3d67e8623c9572138bac685e9
mkdir -p codigo
for f in "munger_v2_r1/personaje_v2/scripts/pipeline.py" \
         "munger_v2_r1/personaje_v2/scripts/verificacion_entradas.py" \
         "munger_v2_r1/personaje_v2/scripts/ficha.py" \
         "munger_v2_r1/personaje_v2/scripts/cambiar_base.py" \
         "munger_v2_r1/personaje_v2/scripts/rellenar_fase1_v63.py" \
         "munger_v2_r1/personaje_v2/scripts/fase1_historia.py" \
         "munger_v2_r1/personaje_v2/pruebas/test_relevo_i19_415.py" \
         "munger_v2_r1/verificar_paquete.sh" \
         "munger_v2_r1/PROMPT_NUEVA_VENTANA.md" \
         "munger_v2_r1/VERSION" \
         "README.md" \
         "munger_v2_r1/personaje_v2/empresas_v2_correcciones/2026-11_Vidrala_ensayo_4_15/HITO_1_4_15.md" \
         "munger_v2_r1/personaje_v2/empresas_v2_correcciones/2026-11_Vidrala_ensayo_4_15/hito2/HITO_2_4_15.md" \
         "munger_v2_r1/personaje_v2/empresas_v2_correcciones/2026-11_Vidrala_ensayo_4_15/hito2/PUNTO_DE_RECUPERACION.md" \
         "munger_v2_r1/personaje_v2/empresas_v2_correcciones/2026-11_Vidrala_ensayo_4_15/scripts/generar_cambios_y_manifiesto_4_15.py"; do
  out=$(echo "$f" | tr '/' '_')
  gh api "repos/jluisplagos/munger-v2/contents/$f?ref=$BASE" -H 'Accept: application/vnd.github.raw' > "codigo/$out"
done
P=codigo/munger_v2_r1_personaje_v2_scripts_pipeline.py
echo "== pipeline.py paso 2: modo entrada_efectiva ilegible (no_entregable) y codigo 7 estricta (pendiente_de_datos) =="
sed -n '660,672p' $P
echo "== pipeline.py paso 13: I19 relevo caducado, relevos_caducados, repite paso 12, solicitud sustituida =="
sed -n '1060,1084p' $P
V=codigo/munger_v2_r1_personaje_v2_scripts_verificacion_entradas.py
echo "== verificacion_entradas.py: R1 pagina PDF entero + folio (35,390); sellar --revisor --fecha (84) =="
sed -n '35p;84p;390p' $V
F=codigo/munger_v2_r1_personaje_v2_scripts_ficha.py
echo "== ficha.py: I20 bloque verificacion_entradas en todas las plantillas tambien V6.3 (383-391) =="
sed -n '383,391p' $F
CB=codigo/munger_v2_r1_personaje_v2_scripts_cambiar_base.py
echo "== cambiar_base.py: analisis_que_se_conservan/_que_se_descartan y entrada_efectiva estricta por defecto (60-62,72-88) =="
sed -n '60,62p;83,88p' $CB
RF=codigo/munger_v2_r1_personaje_v2_scripts_rellenar_fase1_v63.py
echo "== rellenar_fase1_v63.py: --estricta detiene con codigo 7 (22-25) =="
sed -n '22,25p' $RF
FH=codigo/munger_v2_r1_personaje_v2_scripts_fase1_historia.py
echo "== fase1_historia.py: R415-SIGNO valor_fuente cifra publicada con signo (308-310,327-338) =="
sed -n '308,310p;327,329p;338,340p' $FH
T=codigo/munger_v2_r1_personaje_v2_pruebas_test_relevo_i19_415.py
echo "== test_relevo_i19_415.py: 5 comprobaciones paso(...) del relevo sin --desde =="
grep -n 'paso("19' $T
grep -n 'SIN \\u00ab--desde' $T || grep -n 'SIN.*--desde' $T
VP=codigo/munger_v2_r1_verificar_paquete.sh
echo "== verificar_paquete.sh: baterias obligatorias y recuentos 190/62/5/199 =="
sed -n '14,25p' $VP
PNV=codigo/munger_v2_r1_PROMPT_NUEVA_VENTANA.md
echo "== PROMPT_NUEVA_VENTANA.md: arranque desde el repositorio (3) y pasos 15-22, 23-26 =="
sed -n '3p;15,22p;23,26p' $PNV
echo "== VERSION @957af65 =="
cat codigo/munger_v2_r1_VERSION
echo "== README.md raiz: base_414.py solo sobre main/base 4.14 (5) =="
sed -n '5p' codigo/README.md
H1=codigo/munger_v2_r1_personaje_v2_empresas_v2_correcciones_2026-11_Vidrala_ensayo_4_15_HITO_1_4_15.md
echo "== HITO_1_4_15.md: R1 (19), R2 (27), R3 (30-40), I13 (42), C48 (134-153) =="
sed -n '19p;27p;30p;42p;134p;141,143p' $H1
H2=codigo/munger_v2_r1_personaje_v2_empresas_v2_correcciones_2026-11_Vidrala_ensayo_4_15_hito2_HITO_2_4_15.md
echo "== HITO_2_4_15.md: U6 (74-76), I20 (82-88), I19 (89-92), H9 limite abierto (92-93), guias no reescritas (199-200) =="
sed -n '74,76p;82,84p;89,93p;199,200p' $H2
PR=codigo/munger_v2_r1_personaje_v2_empresas_v2_correcciones_2026-11_Vidrala_ensayo_4_15_hito2_PUNTO_DE_RECUPERACION.md
echo "== hito2 PUNTO_DE_RECUPERACION.md: H9 parte abierta (33) =="
sed -n '33,34p' $PR
GEN=codigo/munger_v2_r1_personaje_v2_empresas_v2_correcciones_2026-11_Vidrala_ensayo_4_15_scripts_generar_cambios_y_manifiesto_4_15.py
echo "== generador del producto que firma la cabecera de CAMBIOS/MANIFIESTO (1-9) =="
sed -n '1,9p' $GEN
