#!/usr/bin/env bash
# Prepara el entorno del frente D (v2, CORRECCION_D D-R5):
# - clona main del producto, materializa la base 4.14 (ZIP descargado una vez y
#   verificado por SHA-256) y hace checkout de la candidata fijada;
# - VERIFICA en ejecución el SHA real de la candidata (falla si no es el esperado);
# - extrae el banco y deja BANCO_DIR apuntando a la carpeta banco_revisado
#   (la que contiene casos_aceptacion.jsonl): el ejecutor (lib_arnes) espera ese nivel,
#   no la raíz del repositorio auxiliar;
# - verifica el manifiesto del banco y ejecuta comprobar_banco.py.
# No modifica jluisplagos/munger-v2: todo ocurre en copias locales de /workspace.
set -u
CAND="${CANDIDATA_DIR:-/workspace/base_414_main}"
SHA_ESPERADO="${SHA_CANDIDATA_ESPERADO:-957af652cdc3bef3d67e8623c9572138bac685e9}"
BANCO_ROOT="${BANCO_ROOT:-/workspace/banco_q1_v2}"           # raíz de extracción
export BANCO_DIR="${BANCO_DIR:-$BANCO_ROOT/resultados_qwen/q1_v2/banco_revisado}"  # nivel que espera el ejecutor
AUX_REPO="${AUX_REPO:-/workspace/github__jluisplagos__munger-v2-evidencias-mistral}"

echo "== 1. producto: clone main + base 4.14 + checkout candidata $SHA_ESPERADO"
if [ ! -d "$CAND/.git" ]; then
  gh repo clone jluisplagos/munger-v2 "$CAND" -- --depth 1 --branch main || exit 1
fi
cd "$CAND"
if [ ! -f .downloads/munger_v2_r1_entrega4.14_cierre_verificacion_entradas.zip ]; then
  mkdir -p .downloads
  gh release download base-4.14 --repo jluisplagos/munger-v2 \
    --pattern 'munger_v2_r1_entrega4.14_cierre_verificacion_entradas.zip' --dir .downloads || exit 1
fi
echo "bb51942cefb848e409a4828e3faeb70f94aa4d29af39cda6d90cd0a97cb7b93e  .downloads/munger_v2_r1_entrega4.14_cierre_verificacion_entradas.zip" | sha256sum -c - || exit 1
python3 tools/base_414.py materialize --source .downloads/munger_v2_r1_entrega4.14_cierre_verificacion_entradas.zip || exit 1
python3 tools/base_414.py verify --report docs/VERIFICACION_BASE_COMPLETA_LOCAL.json || true
git fetch --depth 1 origin claude/hopeful-bardeen-qap6y0 || exit 1
git checkout "$SHA_ESPERADO" || exit 1
SHA_REAL="$(git rev-parse HEAD)"
if [ "$SHA_REAL" != "$SHA_ESPERADO" ]; then echo "FALLO: SHA real $SHA_REAL != esperado $SHA_ESPERADO"; exit 1; fi
echo "HEAD verificado en ejecución: $SHA_REAL"

echo "== 2. banco: extrae resultados_qwen/q1_v2 desde revision/qwen-q1-v2 y fija BANCO_DIR=$BANCO_DIR"
mkdir -p "$BANCO_ROOT"
git -C "$AUX_REPO" archive origin/revision/qwen-q1-v2 resultados_qwen/q1_v2 | tar -x -C "$BANCO_ROOT"
cd "$BANCO_DIR" || { echo "FALLO: BANCO_DIR=$BANCO_DIR no existe (debe ser .../banco_revisado)"; exit 1; }
[ -f casos_aceptacion.jsonl ] || { echo "FALLO: BANCO_DIR no contiene casos_aceptacion.jsonl"; exit 1; }
sha256sum -c MANIFIESTO_SHA256.txt || exit 1
python3 -I comprobar_banco.py >/dev/null 2>&1 && echo "comprobar_banco: exit 0" || { echo "comprobar_banco exit != 0"; exit 1; }

echo "== 3. dependencias python"
python3 -c "import openpyxl, lxml, pypdf, jsonschema" 2>/dev/null || python3 -m pip install --quiet openpyxl lxml pypdf jsonschema
python3 -c "import openpyxl, lxml, pypdf, jsonschema; print('deps OK')"
command -v soffice >/dev/null && echo "soffice disponible" || echo "AVISO: sin soffice (sin root); el pipeline con recálculo de libros no se ejecuta en este entorno"
command -v pdftotext >/dev/null && echo "pdftotext disponible" || echo "AVISO: sin pdftotext; los textos de los PDF no se re-leen (Q1-026 queda bloqueado por esto)"
echo "== entorno listo: export CANDIDATA_DIR=$CAND BANCO_DIR=$BANCO_DIR RUN_DIR=${RUN_DIR:-/workspace/ejecucion_d_run}"
