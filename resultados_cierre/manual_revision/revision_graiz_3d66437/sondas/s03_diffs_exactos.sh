#!/bin/sh
# s03: diffs exactos base->head de los 3 diff_rutas
# Uso: sh s03_diffs_exactos.sh [workdir de s02]  (si no se indica, descarga de nuevo)
set -u
PROD=repos/jluisplagos/munger-v2
BASE=957af652cdc3bef3d67e8623c9572138bac685e9
HEAD=3d66437e797b6b0bf137b42fa62b561f39121722
W=${1:-}
if [ -z "$W" ] || [ ! -d "$W" ]; then
  W=$(mktemp -d /tmp/graiz_s03.XXXXXX)
  for f in CLAUDE.md README.md docs/MIGRATION_STATUS.json; do
    o=$(echo "$f" | tr '/' '_')
    gh api "$PROD/contents/$f?ref=$BASE" -H 'Accept: application/vnd.github.raw' > "$W/base_$o"
    gh api "$PROD/contents/$f?ref=$HEAD" -H 'Accept: application/vnd.github.raw' > "$W/head_$o"
  done
fi
echo "== s03 G-RAIZ $(date -u +%FT%TZ) workdir=$W =="
for pair in "CLAUDE.md CLAUDE.md" "README.md README.md" "docs/MIGRATION_STATUS.json docs_MIGRATION_STATUS.json"; do
  set -- $pair
  echo "===== diff -u base/$2 head/$2 ($1) ====="
  diff -u "$W/base_$2" "$W/head_$2" || true
done
echo "== líneas cambiadas por archivo (add/del del compare): CLAUDE.md +5/-5, README.md +4/-4, docs/MIGRATION_STATUS.json +6/-4 =="
