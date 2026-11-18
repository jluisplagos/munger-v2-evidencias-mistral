#!/usr/bin/env bash
# copia solo los archivos de primer nivel de un expediente (lo que lee hoja_resumen.py) a $W/exp/<nombre>
set -euo pipefail
src="$1"; nombre="$2"; W=/tmp/claude-0/revision_hoja
dst="$W/exp/$nombre"; rm -rf "$dst"; mkdir -p "$dst"
find "$src" -maxdepth 1 -type f -exec cp -p {} "$dst/" \;
echo "$dst"
