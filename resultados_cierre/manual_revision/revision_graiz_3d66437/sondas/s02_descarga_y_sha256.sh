#!/bin/sh
# s02: descarga de los 3 diff_rutas en ambos refs (solo lectura) y sha256
# Uso: sh s02_descarga_y_sha256.sh  (deja los archivos en $TMPDIR/graiz_s02)
set -u
PROD=repos/jluisplagos/munger-v2
BASE=957af652cdc3bef3d67e8623c9572138bac685e9
HEAD=3d66437e797b6b0bf137b42fa62b561f39121722
W=$(mktemp -d /tmp/graiz_s02.XXXXXX)
echo "== s02 G-RAIZ $(date -u +%FT%TZ) workdir=$W =="
for f in CLAUDE.md README.md docs/MIGRATION_STATUS.json; do
  o=$(echo "$f" | tr '/' '_')
  gh api "$PROD/contents/$f?ref=$BASE" -H 'Accept: application/vnd.github.raw' > "$W/base_$o"
  gh api "$PROD/contents/$f?ref=$HEAD" -H 'Accept: application/vnd.github.raw' > "$W/head_$o"
done
sha256sum "$W"/base_* "$W"/head_*
echo "-- tamaños (bytes):"
wc -c "$W"/base_* "$W"/head_*
echo "$W" > /tmp/graiz_s02_last_workdir
