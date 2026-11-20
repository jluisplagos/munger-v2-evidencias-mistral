#!/bin/bash
# uso: cita.sh RUTA_ABREVIADA LINEAS   (LINEAS: "10" o "10-12" o "" para todo)
C=${CAND:?definir CAND=<candidata>}; A=${AUX:?definir AUX=<aux>}
p="$1"; l="$2"
repo=$C; rev=3149128
case "$p" in
  PV2/*) p="munger_v2_r1/personaje_v2/${p#PV2/}";;
  E414/*) p="munger_v2_r1/personaje_v2/empresas_v2_correcciones/2026-11_Vidrala_ensayo_4_14/${p#E414/}";;
  E415/*) p="munger_v2_r1/personaje_v2/empresas_v2_correcciones/2026-11_Vidrala_ensayo_4_15/${p#E415/}";;
  EVID/*) repo=$A; rev=ef36ab1; p="${p#EVID/}";;
  PRUEBAS/*) repo=$A; rev=ef36ab1; p="coordinacion/cierre_v2/pruebas_candidata/957af65/${p#PRUEBAS/}";;
  TRASP/*) repo=$A; rev=ef36ab1; p="coordinacion/cierre_v2/traspaso/resultado_20261117/${p#TRASP/}";;
  REG/*) repo=$A; rev=ef36ab1; p="coordinacion/cierre_v2/traspaso/resultado_20261117/registro/${p#REG/}";;
  REVT/*) repo=$A; rev=ef36ab1; p="coordinacion/cierre_v2/traspaso/revision_20261117/${p#REVT/}";;
  HERR/*) repo=$A; rev=ef36ab1; p="coordinacion/cierre_v2/herramientas/${p#HERR/}";;
  F1PREP/*) rev=03e7851; p="docs/validacion_economica_paralela/frente_E_F1_elis/evidencias/preparacion/${p#F1PREP/}";;
  OLD:*) rev=957af65; p="${p#OLD:}";;
esac
if [ -z "$l" ]; then git -C $repo show "$rev:$p" | cat -n; exit; fi
a=${l%-*}; b=${l#*-}
git -C $repo show "$rev:$p" | sed -n "${a},${b}{=;p}" | paste - - | sed "s|^|[$1:] |"
