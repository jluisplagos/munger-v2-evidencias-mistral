#!/usr/bin/env bash
# Sonda 3: JSON válido y recuentos; aplicación limpia sobre 3149128; main con la 4.14; rutas locales y datos personales.
set -u
P="${PRODUCTO:?defina PRODUCTO=<producto>}"; C="${CANDIDATA:?defina CANDIDATA=<candidata>}"
TMPD=$(mktemp -d)
echo "== JSON"
git -C "$P" show 3d66437:docs/MIGRATION_STATUS.json | python3 -I -c 'import json,sys; d=json.load(sys.stdin); print("JSON válido;", {k:d[k] for k in ("tracked_baseline_files_copied","release_asset_files","binary_files_uploaded","candidate_branch","candidate_base_commit")})'
git -C "$P" diff 957af65 3d66437 -- docs/MIGRATION_STATUS.json | grep -E '^[-+] .*"(tracked|release_asset|binary)' ; echo "recuentos modificados: rc=$? (1 = ninguno)"
git -C "$P" cat-file -t 957af652cdc3bef3d67e8623c9572138bac685e9
echo "== candidata"; git -C "$C" rev-parse HEAD; git -C "$P" diff --name-only 957af65 3149128
echo "== merge-tree 3149128 + 3d66437"; T=$(git -C "$P" merge-tree --write-tree 3149128 3d66437); echo "rc=$? árbol=$T"
for f in CLAUDE.md README.md docs/MIGRATION_STATUS.json; do echo "$f fusion=$(git -C "$P" rev-parse $T:$f) cambio=$(git -C "$P" rev-parse 3d66437:$f)"; done
echo "== git apply --cached --check en índice temporal"
git -C "$P" diff 957af65 3d66437 > "$TMPD/d.diff"
GIT_INDEX_FILE="$TMPD/idx" git -C "$P" read-tree 3149128 && GIT_INDEX_FILE="$TMPD/idx" git -C "$P" apply --cached --check "$TMPD/d.diff"; echo "apply rc=$?"
echo "== main"; git -C "$P" merge-base --is-ancestor 957af65 origin/main; echo "957af65 en main rc=$? (1 = no)"
git -C "$P" show origin/main:munger_v2_r1/VERSION | cut -c1-40
MB=$(git -C "$P" merge-base origin/main 957af65); git -C "$P" diff --stat "$MB" origin/main -- munger_v2_r1 baselines tools | tail -1; echo "(vacío = árbol del producto en main sin cambios)"
echo "== rutas locales / correos / datos personales en el diff"
git -C "$P" diff 957af65 3d66437 | grep -E '^\+' | grep -nE '/home/|/root|/tmp/|[A-Za-z]:\\|@[A-Za-z0-9-]+\.[a-z]{2,}' ; echo "rc=$? (1 = ninguno)"
git -C "$P" diff 957af65 3d66437 | grep -E '^\+' | grep -oE 'jluisplagos/[A-Za-z0-9._-]+' | sort | uniq -c
rm -rf "$TMPD"
