#!/usr/bin/env bash
# Ejecuta todos los casos con especificación ejecutable y regenera la matriz.
set -u
AQUI="$(cd "$(dirname "$0")" && pwd)"
for spec in "$AQUI"/especificaciones/piloto/*.json; do
  python3 "$AQUI/ejecutar_caso.py" "$spec" || echo "AVISO: fallo en $spec"
done
python3 "$AQUI/generar_matriz.py"
