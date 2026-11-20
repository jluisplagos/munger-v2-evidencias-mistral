#!/bin/bash
# Revisor A3: para cada commit A3-R1..R7, extrae su arbol con git archive (sin checkout), enlaza
# los insumos verificados de la copia REPRO y ejecuta la cadena que fija los estados
# (inventario, verificar_fuentes, verificar_contexto, derivaciones, construir_cobertura,
# control_cobertura) con python3 -I -B; compara byte a byte con lo publicado en ESE commit.
# Uso: bash s01c_commits_intermedios.sh GITDIR REPRO DESTDIR
GD=$1; REPRO=$2; DEST=$3
for c in 93a02e0 d11ee44 74d94f8 c472595 2e4eb15 447a977 4f50e6a; do
  W=$DEST/$c; rm -rf $W; mkdir -p $W/.trabajo; git --git-dir=$GD archive $c | tar -x -C $W
  ln -s $REPRO/.trabajo/insumos_m2 $W/.trabajo/insumos_m2
  SC=$W/resultados_m2/cobertura_vm/scripts; cd $W
  echo "### $c"
  for s in inventario verificar_fuentes verificar_contexto derivaciones construir_cobertura control_cobertura; do
    python3 -I -B $SC/$s.py > $W/$s.out 2>&1; echo "$s exit=$?"; done
  for f in resultados/verificacion_contexto.jsonl DERIVADOS.json COBERTURA_677.csv resultados/control_cobertura.json; do
    git --git-dir=$GD show $c:resultados_m2/cobertura_vm/$f > $W/pub.tmp
    cmp -s $W/pub.tmp $W/resultados_m2/cobertura_vm/$f && echo "IGUAL   $f" || echo "DIFIERE $f"; done
  rm -f $W/pub.tmp; find $SC -name __pycache__ -prune -exec rm -rf {} +
done
