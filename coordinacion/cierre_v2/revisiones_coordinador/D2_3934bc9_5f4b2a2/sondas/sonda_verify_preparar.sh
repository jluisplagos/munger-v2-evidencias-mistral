#!/usr/bin/env bash
# Sonda del revisor: ejecuta SOLO el fragmento de verify de preparar_entorno.sh (líneas 30-33)
# contra un tools/base_414.py de juguete que imita la salida real de base_414.py (claves
# scope/verified/expected/missing/changed/complete; exit 1 si incompleta). Sin red ni producto.
# Uso: bash sonda_verify_preparar.sh <preparar_entorno.sh> <dir de trabajo>
set -u
PREP="$1"; W="$2"; rm -rf "$W"; mkdir -p "$W/tools" "$W/run"
sed -n '30,33p' "$PREP" | sed "s#/tmp/base_414_verify.json#$W/verify.json#g" > "$W/fragmento.sh"
cat > "$W/tools/base_414.py" <<'PY'
import json, os, sys
c = os.environ.get("STUB_COMPLETA") == "1"
rep = {"scope": "full_baseline", "verified": 6798 if c else 6797, "expected": 6798, "missing": 0 if c else 1, "changed": 0, "complete": c}
if "--report" in sys.argv:
    open(sys.argv[sys.argv.index("--report") + 1], "w").write(json.dumps(rep))
print(json.dumps(rep)); sys.exit(0 if c else 1)
PY
for c in 1 0; do
  ( cd "$W" && STUB_COMPLETA=$c RUN_DIR="$W/run" bash fragmento.sh ) > "$W/out_$c.txt" 2>&1
  echo "STUB_COMPLETA=$c exit=$?"; sed 's#'"$W"'#<w>#g' "$W/out_$c.txt" | tail -4
done
