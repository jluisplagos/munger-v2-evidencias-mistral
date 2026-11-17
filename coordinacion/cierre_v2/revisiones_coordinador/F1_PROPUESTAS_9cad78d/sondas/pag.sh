#!/bin/bash
# Sonda del revisor: extrae una página (página PDF) de una fuente a texto con pdftotext -layout.
# Uso: pag.sh DOC PAGINA   (DOC: URD2021|URD2022|URD2023|DEU2024FR|URD2025|REL:<archivo>)
AQUI="$(cd "$(dirname "$0")" && pwd)"; REV="$(dirname "$AQUI")"
R="$REV/copia/munger_v2_r1/personaje_v2/empresas_v2_correcciones/2026-11_Vidrala_ensayo_4_14/elis_decisiones/Elis/fuentes_pdf"
case "$1" in
  URD2021) F="$R/Elis_URD_2021_EN.pdf";;
  URD2022) F="$R/Elis - 2022 Universal Registration Document.pdf";;
  URD2023) F="$R/Elis_Universal Registration Document_2023_EN.pdf";;
  DEU2024FR) F="$R/Elis_Document d'enregistrement universel_2024_FR.pdf";;
  URD2025) F="$R/Elis - 2025 Universal Registration Document.pdf";;
  REL:*) F="$REV/release/pdf/${1#REL:}";;
  *) echo "doc desconocido" >&2; exit 2;;
esac
O="$AQUI/paginas/$(echo "$1" | tr ':' '_')_p$2.txt"
pdftotext -layout -f "$2" -l "$2" "$F" "$O" && cat "$O"
