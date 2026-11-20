#!/bin/bash
# Uso: sonda_d3_citas.sh <raiz munger_v2_r1 de la candidata>
# Imprime cada linea citada por CONTRATO_C_PROPUESTA.md @c761cc8 para comprobar la cita a mano.
R="$1"; B=$R/v6/scripts/V6.1/build_v6.py; T=$R/v6/scripts/V6.1/test_fill.py; M=$R/v6/scripts/relacion_entradas_materiales.py; P=$R/v6/scripts/patch_v62_base.py
p(){ echo "-- $1:$2"; sed -n "$2p" "$3" | cut -c1-170; }
p build_v6.py 146,153 $B; p build_v6.py 282p\;294 $B; p build_v6.py 312 $B; p build_v6.py 444,453 $B
p build_v6.py 934,945 $B; p build_v6.py 966,970 $B; p build_v6.py 1136,1147 $B
p test_fill.py 79 $T; p test_fill.py 84,99 $T; p relacion 143,152 $M; p patch_v62_base.py 255,257 $P
grep -n "B69\|B\$69\|69:D69\|C55\b\|'C55'\|C\$55\|C\$56" $B | head -8 | sed 's/^/-- grep build_v6.py: /' | cut -c1-200
