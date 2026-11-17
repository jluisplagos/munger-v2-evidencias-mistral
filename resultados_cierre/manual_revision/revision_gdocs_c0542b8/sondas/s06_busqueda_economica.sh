#!/bin/sh
# Ausencia de cambios economicos: barrido de todas las lineas cambiadas (102) buscando
# magnitudes economicas, parametros y valores; solo deben aparecer recuentos de pruebas,
# fechas, hashes y nombres de rama.
cat diff_*.txt | grep '^[+-]' | grep -E '€|C4[6-9]|C50|307,933|39,80|56,00|7,30|90,10|128,1|probabilidad|umbral|R,|θ|λ|k =' 
echo "== total de lineas cambiadas en los 4 diffs =="
cat diff_*.txt | grep -c '^[+-]'
echo "== lineas cambiadas que mencionan I19/I20/H9 (deben conservar H9 abierto) =="
cat diff_*.txt | grep '^[+-]' | grep -E 'I19|I20|H9'
