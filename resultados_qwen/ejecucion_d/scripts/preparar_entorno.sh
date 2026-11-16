#!/usr/bin/env bash
# Prepara el entorno del frente D: clon del producto en main, materializa la base 4.14
# (ZIP de la Release base-4.14, un solo intento de descarga) y hace checkout de la
# candidata fijada. Después clona/extrae el banco desde revision/qwen-q1-v2.
# No modifica jluisplagos/munger-v2: todo ocurre en copias locales de /workspace.
set -u
CAND="${CANDIDATA_DIR:-/workspace/base_414_main}"
BANCO_OUT="${BANCO_DIR:-/workspace/banco_q1_v2}"
AUX_REPO="${AUX_REPO:-/workspace/github__jluisplagos__munger-v2-evidencias-mistral}"

echo "== 1. producto: clone main + base 4.14 + checkout candidata 957af652cdc3bef3d67e8623c9572138bac685e9"
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
git checkout 957af652cdc3bef3d67e8623c9572138bac685e9 || exit 1
echo "HEAD: $(git rev-parse HEAD)"

echo "== 2. banco: extrae resultados_qwen/q1_v2 desde revision/qwen-q1-v2 del auxiliar"
mkdir -p "$BANCO_OUT"
git -C "$AUX_REPO" archive origin/revision/qwen-q1-v2 resultados_qwen/q1_v2 | tar -x -C "$BANCO_OUT"
cd "$BANCO_OUT/resultados_qwen/q1_v2/banco_revisado"
sha256sum -c MANIFIESTO_SHA256.txt || exit 1
python3 -I comprobar_banco.py >/dev/null 2>&1 && echo "comprobar_banco: exit 0" || { echo "comprobar_banco exit != 0"; exit 1; }

echo "== 3. dependencias python"
python3 -c "import openpyxl, lxml, pypdf, jsonschema" 2>/dev/null || python3 -m pip install --quiet openpyxl lxml pypdf jsonschema
python3 -c "import openpyxl, lxml, pypdf, jsonschema; print('deps OK')"
command -v soffice >/dev/null && echo "soffice disponible" || echo "AVISO: sin soffice (sin root); el pipeline con recálculo de libros no se ejecuta en este entorno"
command -v pdftotext >/dev/null && echo "pdftotext disponible" || echo "AVISO: sin pdftotext; las fuentes PDF del producto no se re-leen (los fixtures son TXT/CSV/JSON)"
echo "== entorno listo"
