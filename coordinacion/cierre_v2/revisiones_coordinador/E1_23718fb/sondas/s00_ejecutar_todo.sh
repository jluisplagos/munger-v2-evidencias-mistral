#!/usr/bin/env bash
# s00 · Ejecuta todas las sondas de la revision de E-ELIS @ 23718fb/f00c5dd y normaliza rutas en las salidas.
# Uso: bash s00_ejecutar_todo.sh <rev_E1> <dir_pdf_11> <urd2025.pdf> <informe_semestral_2026_EN_base.pdf> <repo_auxiliar> <python_con_PyMuPDF_y_pypdf>
# Requisito previo: <rev_E1>/entrega = git -C <repo_auxiliar> archive f00c5dd resultados_cierre/elis_fuentes | tar -x
set -u
REV="$1"; PDF="$2"; URD="$3"; S1="$4"; AUX="$5"; PY="$6"; S="$REV/sondas"; ENT="$REV/entrega/resultados_cierre/elis_fuentes"
BASE414="${URD%%/personaje_v2/*}"
n() { sed "s|$REV|<rev_E1>|g; s|$PDF|<pdf>|g; s|$BASE414|<base414>|g; s|$AUX|<aux>|g"; }
cd "$S"
python3 -I s01_citas_52.py "$ENT/LECTURA_FUENTES.jsonl" "$PDF" "$URD" 2>&1 | n > s01_citas_52.out; echo "s01 exit ${PIPESTATUS[0]}"
"$PY" -I -W ignore s02_extractos.py "$ENT" "$PDF" "$URD" 2>&1 | n > s02_extractos.out; echo "s02 exit ${PIPESTATUS[0]}"
python3 -I s03_cifras_y_clasificacion.py "$URD" "$ENT" 2>&1 | n > s03_cifras_y_clasificacion.out; echo "s03 exit ${PIPESTATUS[0]}"
bash s04_reproduccion.sh "$REV" "$PDF" "$URD" "$PY" 2>&1 | n > s04_reproduccion.out; echo "s04 exit ${PIPESTATUS[0]}"
bash s05_higiene_conservacion.sh "$AUX" "$REV" 2>&1 | n > s05_higiene_conservacion.out; echo "s05 exit ${PIPESTATUS[0]}"
bash s06_textos.sh "$ENT" "$S1" "$PDF" 2>&1 | n > s06_textos.out; echo "s06 exit ${PIPESTATUS[0]}"
echo "== manifiestos (sha256sum -c desde su raiz)"
( cd "$ENT" && sha256sum -c --quiet MANIFIESTO_SHA256.txt; echo "f00c5dd: exit $? ($(wc -l < MANIFIESTO_SHA256.txt) entradas)" )
T=$(mktemp -d "$REV/tmp_23718fb.XXXX"); git -C "$AUX" archive 23718fb resultados_cierre/elis_fuentes | tar -x -C "$T"
( cd "$T/resultados_cierre/elis_fuentes" && sha256sum -c --quiet MANIFIESTO_SHA256.txt 2>&1 | n; echo "23718fb: exit ${PIPESTATUS[0]} ($(wc -l < MANIFIESTO_SHA256.txt) entradas; pyc listados: $(grep -c '\.pyc$' MANIFIESTO_SHA256.txt))" ); rm -rf "$T"
# los .json de las sondas pueden llevar rutas: normalizarlas
for f in "$S"/*.json; do sed -i "s|$REV|<rev_E1>|g; s|$PDF|<pdf>|g; s|$BASE414|<base414>|g; s|$AUX|<aux>|g" "$f"; done
