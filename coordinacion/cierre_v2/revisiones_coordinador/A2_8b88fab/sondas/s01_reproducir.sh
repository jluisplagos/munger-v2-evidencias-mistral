#!/bin/bash
# Revisor A2 (8b88fab): re-ejecuta en la copia aislada REPRO los comandos de COMANDOS.md
# (sin red, sin LibreOffice, sin git add/commit/push) y compara byte a byte con los blobs
# publicados en ENTREGA (arbol extraido de 8b88fab con git archive, no modificado).
# generar_cambios_estado.py necesita `git show`; se le da GIT_DIR del clon local (solo lectura).
# Uso: bash s01_reproducir.sh REPRO ENTREGA GITDIR
REPRO=$1; ENT=$2; GD=$3; SC=$REPRO/resultados_m2/cobertura_vm/scripts
TMPO=$(mktemp)
cd "$REPRO"
run() { echo "## python3 -I -B $(basename $1) ${@:2}"; python3 -I -B "$@" > $TMPO 2>&1; rc=$?; head -c 1200 $TMPO; echo; echo "exit=$rc"; }
run $SC/inventario.py
run $SC/verificar_fuentes.py
run $SC/verificar_contexto.py
run $SC/derivaciones.py
run $SC/construir_cobertura.py
run $SC/control_negativo.py
run $SC/control_cobertura.py
run $SC/cola_pendientes.py
run $SC/resolver_bloque2.py
for L in $(seq -w 0 21); do python3 -I -B $SC/revisar_lote.py L$L > /dev/null 2>&1 || echo "revisar_lote L$L exit=$?"; done; echo "## revisar_lote L00..L21 ejecutado"
run $SC/control_cobertura.py
run $SC/asociacion_pdf.py
run $SC/generar_recuentos_doc.py
echo "## GIT_DIR=<clon> python3 -I -B generar_cambios_estado.py 9d676ce... a2_v4"
GIT_DIR=$GD python3 -I -B $SC/generar_cambios_estado.py 9d676cefdfeb3771a43414fcb93f430e9340fae0 a2_v4 > $TMPO 2>&1; rc=$?; head -c 1500 $TMPO; echo; echo "exit=$rc"
find $SC -name __pycache__ -prune -exec rm -rf {} +
run $SC/generar_manifiesto.py
echo "## comparacion sha256 publicado vs reproducido (archivos del manifiesto publicado)"
cd $ENT/resultados_m2/cobertura_vm
while read sha f; do r=$(sha256sum "$REPRO/resultados_m2/cobertura_vm/$f" | cut -d' ' -f1); [ "$r" = "$sha" ] && echo "IGUAL  $f" || echo "DIFIERE $f"; done < MANIFIESTO_SHA256.txt
echo "## archivos en REPRO que no estan en el manifiesto publicado"
cd $REPRO/resultados_m2/cobertura_vm; find . -type f ! -path '*__pycache__*' | sed 's|^\./||' | sort > $TMPO.a; cut -d' ' -f3- $ENT/resultados_m2/cobertura_vm/MANIFIESTO_SHA256.txt | sort > $TMPO.b; comm -23 $TMPO.a $TMPO.b
rm -f $TMPO $TMPO.a $TMPO.b
