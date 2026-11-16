#!/usr/bin/env bash
# Ejecuta todos los casos con especificación ejecutable y regenera la matriz.
set -u
AQUI="$(cd "$(dirname "$0")" && pwd)"
for dir in piloto bloque2; do
  for spec in "$AQUI"/especificaciones/$dir/*.json; do
    [ -e "$spec" ] || continue
    python3 "$AQUI/ejecutar_caso.py" "$spec" || echo "AVISO: fallo en $spec"
  done
done
python3 "$AQUI/generar_matriz.py"
