#!/bin/sh
# s01: identidad de la rama, commit y alcance exacto del diff (criterio 1, alcance)
# Uso: sh s01_identidad_rama_y_commit.sh
set -u
PROD=repos/jluisplagos/munger-v2
BASE=957af652cdc3bef3d67e8623c9572138bac685e9
HEAD=3d66437e797b6b0bf137b42fa62b561f39121722

echo "== s01 G-RAIZ $(date -u +%FT%TZ) =="
echo "-- branch integracion/hechos-raiz-957af65 HEAD:"
gh api "$PROD/branches/integracion/hechos-raiz-957af65" --jq '.commit.sha'
echo "-- commit $HEAD parents:"
gh api "$PROD/commits/$HEAD" --jq '{sha:.sha, parents:[.parents[].sha]}'
echo "-- compare $BASE...$HEAD:"
gh api "$PROD/compare/$BASE...$HEAD" --jq '{status, ahead_by, total_commits, files:[.files[]|{filename,status,additions,deletions}]}'
echo "-- diff_rutas esperados por la solicitud: CLAUDE.md, README.md, docs/MIGRATION_STATUS.json"
echo "-- commit message:"
gh api "$PROD/commits/$HEAD" --jq '.commit.message'
