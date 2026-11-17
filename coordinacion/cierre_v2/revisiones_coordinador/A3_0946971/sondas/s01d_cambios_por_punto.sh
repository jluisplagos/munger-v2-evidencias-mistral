#!/bin/bash
# Revisor A3: regenera con generar_cambios_estado.py (de 0946971, en la copia REPRO) la lista de
# cambios de cada punto entre el commit anterior y el del punto (blobs publicados) y la compara
# con cambios_estado_a3_R*.json publicados (solo las listas cambios_fuente/cambios_csv).
# Uso: bash s01d_cambios_por_punto.sh REPRO ENTREGA GITDIR
REPRO=$1; ENT=$2; GD=$3; SC=$REPRO/resultados_m2/cobertura_vm/scripts
prev=8b88fab28261506c60bc7631fd24894e225099d2; i=1
for c in 93a02e0 d11ee44 74d94f8 c472595 2e4eb15 447a977 4f50e6a; do
  GIT_DIR=$GD python3 -I -B $SC/generar_cambios_estado.py $prev revA3_R$i $c > /dev/null 2>&1; echo -n "R$i ($prev..$c) exit=$? "
  python3 -I -B -c "
import json,sys
a=json.load(open('$REPRO/resultados_m2/cobertura_vm/resultados/cambios_estado_revA3_R$i.json'));b=json.load(open('$ENT/resultados_m2/cobertura_vm/resultados/cambios_estado_a3_R$i.json'))
print('fuentes', a['n_cambios_fuente'], 'csv', a['n_cambios_csv'], 'listas_iguales', a['cambios_fuente']==b['cambios_fuente'] and a['cambios_csv']==b['cambios_csv'])"
  rm -f $REPRO/resultados_m2/cobertura_vm/resultados/cambios_estado_revA3_R$i.json
  prev=$c; i=$((i+1))
done
