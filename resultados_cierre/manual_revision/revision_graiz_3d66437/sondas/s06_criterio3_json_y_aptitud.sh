#!/bin/sh
# s06: criterio 3 — no se declara aptitud, no se adopta nada, main sigue con la 4.14;
#      MIGRATION_STATUS.json: solo campos de texto de estado + 2 claves nuevas; JSON válido
# Uso: sh s06_criterio3_json_y_aptitud.sh [workdir de s02/s03]
set -u
PROD=repos/jluisplagos/munger-v2
BASE=957af652cdc3bef3d67e8623c9572138bac685e9
HEAD=3d66437e797b6b0bf137b42fa62b561f39121722
W=${1:-}
if [ -z "$W" ] || [ ! -d "$W" ]; then
  W=$(mktemp -d /tmp/graiz_s06.XXXXXX)
  for f in CLAUDE.md README.md docs/MIGRATION_STATUS.json; do
    o=$(echo "$f" | tr '/' '_')
    gh api "$PROD/contents/$f?ref=$BASE" -H 'Accept: application/vnd.github.raw' > "$W/base_$o"
    gh api "$PROD/contents/$f?ref=$HEAD" -H 'Accept: application/vnd.github.raw' > "$W/head_$o"
  done
fi
echo "== s06 G-RAIZ $(date -u +%FT%TZ) workdir=$W =="

echo "-- menciones de aptitud en head (todas deben ser negativas):"
grep -n -i 'apta\|apto\|aptitud' "$W/head_CLAUDE.md" "$W/head_README.md"
echo
echo "-- nada adoptado / no fusionar main:"
grep -n -i 'no fusionada con main\|no fusionar main\|main conserva la 4.14\|sin cambios' "$W/head_README.md" "$W/head_docs_MIGRATION_STATUS.json"
echo
echo "-- main sigue con la 4.14 (VERSION @ main empieza por 'entrega 4.14'):"
gh api "$PROD/contents/munger_v2_r1/VERSION?ref=main" -H 'Accept: application/vnd.github.raw' | head -c 120; echo
echo
echo "-- diff estructural de docs/MIGRATION_STATUS.json (solo note/next_action/ongoing_claude_work + 2 claves nuevas):"
python3 - "$W/base_docs_MIGRATION_STATUS.json" "$W/head_docs_MIGRATION_STATUS.json" <<'PY'
import json, sys
b = json.load(open(sys.argv[1])); h = json.load(open(sys.argv[2]))
def walk(a, c, path=''):
    if isinstance(a, dict) and isinstance(c, dict):
        for k in sorted(set(a) | set(c)):
            if k not in a: print('NUEVO', path + '/' + k, '=', c[k])
            elif k not in c: print('ELIMINADO', path + '/' + k)
            elif a[k] != c[k]: print('CAMBIADO', path + '/' + k)
            else: walk(a[k], c[k], path + '/' + k)
    elif a != c: print('CAMBIADO', path)
walk(b, h)
print('JSON head válido; claves head:', len(h), ' claves base:', len(b))
PY
