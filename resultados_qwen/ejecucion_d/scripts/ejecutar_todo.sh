#!/usr/bin/env bash
# Ejecuta todos los casos con especificación ejecutable y regenera la matriz.
# v2 (D-R1): cualquier caso con estado != COMPONENTE_OK hace exit != 0 del global.
set -u
AQUI="$(cd "$(dirname "$0")" && pwd)"
fallos=0
for dir in piloto bloque2; do
  for spec in "$AQUI"/especificaciones/$dir/*.json; do
    [ -e "$spec" ] || continue
    python3 "$AQUI/ejecutar_caso.py" "$spec" || { echo "FALLO/ERROR en $spec"; fallos=$((fallos+1)); }
  done
done
python3 "$AQUI/generar_matriz.py"
python3 "$AQUI/generar_correspondencia.py"
python3 "$AQUI/generar_relevo.py"
if [ "$fallos" -gt 0 ]; then
  echo "ejecutar_todo: $fallos caso(s) con estado != COMPONENTE_OK (Q1-026 BLOQUEO_ENTORNO cuenta como esperado solo si su spec lo declara; ver matriz)"
  exit 1
fi
echo "ejecutar_todo: todos los casos con spec ejecutable COMPONENTE_OK"
