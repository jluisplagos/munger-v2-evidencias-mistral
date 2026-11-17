#!/bin/bash
# Uso: sonda_d1_recuento_awk.sh <zip_Z1.txt> <INVENTARIO_Y_HUECOS.csv>
# Recuento independiente (awk, sin el script del autor) de las columnas n_* por (recurso, ubicacion)
# y comparacion con las filas de recuento publicadas (sin motor ni huecos).
L="$1"; I="$2"
grep -v '/$' "$L" | sed 's|^munger_v2_r1/||' | awk -F/ '
function tipo(n){ if(n~/\.xlsx$/)return 3; if(n~/\.pdf$/)return 6; if(n~/\.json$/)return 4; if(n~/\.(md|txt)$/)return 5; return 7 }
{ k="" }
/^personaje_v2\/empresas_v2\// { if(NF>3) k=$3",empresas_v2"; else if(NF==3) k="(raiz),empresas_v2" }
/^personaje_v2\/empresas_v2_correcciones\// { if(NF>4){ if($4=="fuentes") k=$3"/fuentes,correcciones · "$3; else k=$4",correcciones · "$3 } else if(NF==4) k=$3"/(raiz),correcciones · "$3 }
/^contrastes\// { if(NF>2) k=$2",contrastes" }
k!="" { c[k","tipo($0)]++; keys[k]=1 }
END { for(k in keys){ printf "%s", k; for(t=3;t<=7;t++) printf ",%d", c[k","t]+0; print "" } }' | LC_ALL=C sort > recuento_awk.csv
awk -F, 'NR>1 && $3!="" {print $1","$2","$3","$4","$5","$6","$7}' "$I" | LC_ALL=C sort > recuento_publicado.csv
echo "filas awk: $(wc -l < recuento_awk.csv); filas publicadas: $(wc -l < recuento_publicado.csv)"
if diff recuento_awk.csv recuento_publicado.csv; then echo "RECUENTO INDEPENDIENTE == PUBLICADO"; else echo "DIFIEREN"; fi
