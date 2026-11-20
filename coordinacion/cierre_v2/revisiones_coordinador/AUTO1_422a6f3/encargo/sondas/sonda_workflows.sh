#!/bin/sh
# Sonda estática de workflows y escrituras (sin red). Uso: sh sonda_workflows.sh <rev_auto>
R="$1"
for f in "$R"/.github/workflows/*.yml; do
  n=$(basename "$f")
  echo "== $n"
  echo "  disparadores: $(grep -E '^\s*(push|pull_request|pull_request_target|workflow_dispatch|schedule|workflow_run):' "$f" | tr -s ' ' | tr '\n' ' ')"
  echo "  ramas: $(grep -A1 -E '^\s*push:' "$f" | grep branches | tr -s ' ')"
  echo "  permisos: $(grep -E 'contents: (read|write)' "$f" | tr -s ' ' | tr '\n' ' ')"
  echo "  secretos: $(grep -oE 'secrets\.[A-Z_]+' "$f" | sort -u | tr '\n' ' ')"
  echo "  pip_install_sin_hash: $(grep -c 'pip install' "$f")  setup-python: $(grep -c setup-python "$f")"
  echo "  execute_api/inferencia: $(grep -cE -- '--execute-api|qwen_.*review.py|run_vibe_auth.py|pilot.py' "$f")"
  echo "  persist-credentials false: $(grep -c 'persist-credentials: false' "$f")  acciones fijadas por SHA: $(grep -cE 'uses: [^@]+@[0-9a-f]{40}' "$f")/$(grep -c 'uses:' "$f")"
done
echo "== escrituras GitHub en código (método, rama)"
grep -nE "'(PUT|POST|DELETE|PATCH)'" "$R"/automation/coordination/*.py "$R"/automation/claude_review/pilot.py | sed "s#$R#<rev_auto>#"
grep -nE "'branch':|LEDGER_BRANCH =" "$R"/automation/coordination/*.py "$R"/automation/claude_review/pilot.py | sed "s#$R#<rev_auto>#"
echo "== referencias a main, coordinacion/cierre-v2, CONTROL.json, ESTADO.md en código Python"
grep -nE "heads/main|'main'|cierre-v2|CONTROL\.json|ESTADO\.md" "$R"/automation/coordination/*.py "$R"/automation/claude_review/pilot.py | sed "s#$R#<rev_auto>#" || echo "  (ninguna)"
echo "== bucles while/reintentos en código"
grep -nE "^\s*while |retry|for attempt" "$R"/automation/coordination/*.py "$R"/automation/claude_review/pilot.py | grep -v test_ | sed "s#$R#<rev_auto>#" || echo "  (ninguno)"
