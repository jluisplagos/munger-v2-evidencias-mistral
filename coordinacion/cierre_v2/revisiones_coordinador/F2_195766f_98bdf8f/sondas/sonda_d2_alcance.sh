#!/bin/bash
# Uso: sonda_d2_alcance.sh <zip_Z1.txt> <INVENTARIO_Y_HUECOS.csv>
# Recuento independiente (awk sobre unzip -Z1) del alcance del inventario y de lo que queda fuera.
L="$1"; I="$2"
grep -v '/$' "$L" | sed 's|^munger_v2_r1/||' | awk -F/ '
 { tot++ }
 /^personaje_v2\/empresas_v2\// && NF>=3 { inx++; next }
 /^personaje_v2\/empresas_v2_correcciones\// && NF>=4 { inx++; next }
 /^personaje_v2\/empresas_v2_correcciones\// && NF==3 { huerf++; print "FUERA (archivo suelto en empresas_v2_correcciones/): " $0; next }
 /^contrastes\// && NF>=3 { inx++; next }
 { fuera[$1 (NF>1 ? "/" : "")]++ }
 END { print "archivos en el ZIP: " tot; print "dentro del alcance: " inx; print "sueltos en empresas_v2_correcciones/: " huerf+0;
       for (k in fuera) print "fuera del alcance, " k ": " fuera[k] }' | sort
echo "suma de recuentos del inventario: $(awk -F, 'NR>1 && $3!="" {s+=$3+$4+$5+$6+$7} END{print s}' "$I")"
echo "suma n_pdf del inventario: $(awk -F, 'NR>1 && $6!="" {s+=$6} END{print s}' "$I")"
echo "filas con motor_usado no vacio: $(awk -F, 'NR>1 && $8!=""' "$I" | wc -l)"
