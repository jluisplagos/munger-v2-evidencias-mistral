#!/bin/bash
# Revisor A2: cola_pendientes.py y resolver_bloque2.py no insertan su carpeta en sys.path
# (hacen `import comun` a secas) y fallan con `python3 -I` (ModuleNotFoundError). Se ejecutan
# como en COMANDOS.md (`python3 -B`, sin -I, con -E -s para no leer variables ni site de usuario)
# y despues se rehace la cadena dependiente y se compara byte a byte con lo publicado.
# Uso: bash s01b_cola_resolver.sh REPRO ENTREGA
REPRO=$1; ENT=$2; SC=$REPRO/resultados_m2/cobertura_vm/scripts; TMPO=$(mktemp)
cd "$REPRO"
for s in cola_pendientes.py resolver_bloque2.py; do echo "## python3 -E -s -B $s"; python3 -E -s -B $SC/$s > $TMPO 2>&1; rc=$?; head -c 600 $TMPO; echo; echo "exit=$rc"; done
for L in $(seq -w 0 21); do python3 -I -B $SC/revisar_lote.py L$L > /dev/null 2>&1 || echo "revisar_lote L$L exit=$?"; done
python3 -I -B $SC/control_cobertura.py > $TMPO 2>&1; echo "## control_cobertura exit=$? $(head -c 60 $TMPO)"
find $SC -name __pycache__ -prune -exec rm -rf {} +
cd $ENT/resultados_m2/cobertura_vm
for f in resultados/cola_pendientes.json resultados/resoluciones_bloque2.json resultados/control_cobertura.json $(ls resultados/lotes/*.json); do r=$(sha256sum "$REPRO/resultados_m2/cobertura_vm/$f" | cut -d' ' -f1); p=$(sha256sum "$f" | cut -d' ' -f1); [ "$r" = "$p" ] && echo "IGUAL  $f" || echo "DIFIERE $f"; done
rm -f $TMPO
