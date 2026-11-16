#!/bin/bash
# Revisor A (2c41d68): re-ejecuta en la copia aislada REPRO los scripts declarados en
# ENTREGA.json / PUNTO_DE_RECUPERACION.md (sin red ni LibreOffice) y compara con los
# blobs publicados en ENTREGA (arbol extraido de 2c41d68, no modificado).
# Uso: bash s01_reproducir.sh REPRO ENTREGA
REPRO=$1; ENT=$2; SC=$REPRO/resultados_m2/cobertura_vm/scripts
cd "$(dirname "$REPRO")"
run() { echo "## python3 -I -B $(basename $1) ${@:2}"; python3 -I -B "$@" > /tmp/_o 2>&1; rc=$?; head -c 1500 /tmp/_o; echo; echo "exit=$rc"; }
run $SC/inventario.py
run $SC/verificar_fuentes.py
run $SC/verificar_contexto.py
run $SC/derivaciones.py
run $SC/construir_cobertura.py
run $SC/control_negativo.py
run $SC/control_cobertura.py
for L in $(seq -w 0 21); do python3 -I -B $SC/revisar_lote.py L$L > /dev/null 2>&1 || echo "revisar_lote L$L exit=$?"; done; echo "## revisar_lote L00..L21 ejecutado"
run $SC/asociacion_pdf.py
echo "## comparacion sha256 publicado vs reproducido (archivos del manifiesto)"
cd $ENT/resultados_m2/cobertura_vm
while read sha f; do r=$(sha256sum "$REPRO/resultados_m2/cobertura_vm/$f" | cut -d' ' -f1); [ "$r" = "$sha" ] && echo "IGUAL  $f" || echo "DIFIERE $f"; done < MANIFIESTO_SHA256.txt
