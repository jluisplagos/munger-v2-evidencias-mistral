#!/bin/sh
# s04: cada hecho nuevo declarado en 3d66437 se contrasta contra 957af65 (criterio 1)
# Uso: sh s04_hechos_verificables_en_957af65.sh
set -u
PROD=repos/jluisplagos/munger-v2
BASE=957af652cdc3bef3d67e8623c9572138bac685e9
W=$(mktemp -d /tmp/graiz_s04.XXXXXX)
P=munger_v2_r1/personaje_v2/empresas_v2_correcciones/2026-11_Vidrala_ensayo_4_15

echo "== s04 G-RAIZ $(date -u +%FT%TZ) workdir=$W =="

echo "-- [H1] VERSION @ $BASE (debe decir 'entrega 4.15 · hito 2'):"
gh api "$PROD/contents/munger_v2_r1/VERSION?ref=$BASE" -H 'Accept: application/vnd.github.raw' | head -c 400; echo; echo

echo "-- [H2] rama candidata: 957af65 es ancestro de integracion/candidata-cierre-v2 (status ahead, behind_by 0):"
gh api "$PROD/compare/$BASE...integracion/candidata-cierre-v2" --jq '{status, ahead_by, behind_by}'
echo

echo "-- [H3] VERSION @ main (criterio 3: main sigue con la 4.14):"
gh api "$PROD/contents/munger_v2_r1/VERSION?ref=main" -H 'Accept: application/vnd.github.raw' | head -c 200; echo
echo "-- main HEAD:"
gh api "$PROD/branches/main" --jq '.commit.sha'
echo

echo "-- [H4] rutas citadas existen en el árbol de $BASE:"
gh api "$PROD/git/trees/$BASE?recursive=1" --jq '.tree[].path' > "$W/tree.txt"
grep -E 'docs/revision_externa_4_15_hito1/REVISION\.md$|empresas_v2_correcciones/2026-11_Vidrala_ensayo_4_15/HITO_1_4_15\.md$|hito2/HITO_2_4_15\.md$|personaje_v2/pruebas/test_verificacion_entradas_415\.py$' "$W/tree.txt"
echo

echo "-- [H5] HITO_1_4_15.md @ $BASE: secciones de corrección R1/R2/R3 y hallazgos 4 y 5:"
gh api "$PROD/contents/$P/HITO_1_4_15.md?ref=$BASE" -H 'Accept: application/vnd.github.raw' > "$W/HITO_1.md"
grep -n -E '^### R1|^### R2|^### R3|hallazgo 4|hallazgo 5|hallazgos 1, 2|105/105' "$W/HITO_1.md"
echo

echo "-- [H6] HITO_2_4_15.md @ $BASE: 190/190, límite H9, F1 abierto, no cerrado:"
gh api "$PROD/contents/$P/hito2/HITO_2_4_15.md?ref=$BASE" -H 'Accept: application/vnd.github.raw' > "$W/HITO_2.md"
grep -n -E '190/190|L.mite \(H9\)|H9/I19|F1 \(bloqueo|No cerrado|main. y el ZIP no se han modificado|I19 .|I20 .' "$W/HITO_2.md" | head -12
echo

echo "-- [H7] test_verificacion_entradas_415.py @ $BASE (existe, tamaño, pasos):"
gh api "$PROD/contents/munger_v2_r1/personaje_v2/pruebas/test_verificacion_entradas_415.py?ref=$BASE" -H 'Accept: application/vnd.github.raw' > "$W/test415.py"
wc -c -l "$W/test415.py"
echo "llamadas paso( (estático, sin ejecutar): $(grep -c 'paso(' "$W/test415.py") (incluye la definición en línea 51)"
echo "el recuento 190/190 es el declarado por HITO_2_4_15.md línea 99; el test NO se ejecuta aquí (sin pipeline/LibreOffice)"
echo

echo "-- [H8] docs/revision_externa_4_15_hito1/ existe @ $BASE:"
gh api "$PROD/contents/docs/revision_externa_4_15_hito1?ref=$BASE" --jq '.[].name' | head -5
echo

echo "-- [H9] referencia al control del programa de cierre (README head línea 7): rama coordinacion/cierre-v2 del auxiliar:"
gh api repos/jluisplagos/munger-v2-evidencias-mistral/branches/coordinacion/cierre-v2 --jq '.commit.sha'
