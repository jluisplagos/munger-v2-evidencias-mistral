#!/usr/bin/env bash
# s04 · Reproduce sin red los scripts de E-ELIS @ f00c5dd sobre los PDF locales, en copias desechables.
# Uso: bash s04_reproduccion.sh <rev_E1> <dir_pdf_11> <urd2025.pdf> <python_con_pymupdf_y_pypdf>
set -u
REV="$1"; PDF="$2"; URD="$3"; PY="$4"
S="$REV/sondas"; ENT="$REV/entrega/resultados_cierre/elis_fuentes"
W="$REV/repro"; rm -rf "$W"; mkdir -p "$W"
n() { sed "s|$REV|<rev_E1>|g; s|$PDF|<pdf>|g; s|$URD|<urd2025>|g"; }
hashes() { (cd "$1/resultados_cierre/elis_fuentes" && find . -type f ! -path './scripts/*' | sort | xargs sha256sum); }
prep() { mkdir -p "$1"; cp -r "$REV/entrega/resultados_cierre" "$1/"; }
echo "== entorno"; "$PY" -I -c "import sys,fitz,pypdf; print('python',sys.version.split()[0],'| PyMuPDF',fitz.VersionBind,'| pypdf',pypdf.__version__)" 2>/dev/null
echo "== A. descarga simulada (sin red) + lectura x2 + extractos x2 + segundo extractor x2"
A="$W/A"; prep "$A"
"$PY" -I "$S/s04_descarga_simulada.py" "$A/resultados_cierre/elis_fuentes/scripts/descargar_fuentes_elis.py" "$PDF" "$URD" ok 2>&1 | n | tail -3
echo "carpetas creadas: $(ls -d $A/.trabajo/elis_fuentes/pdf $A/.trabajo/elis_fuentes/texto 2>/dev/null | n | tr '\n' ' ')"
# para comparar con lo entregado, el indice de trabajo se fija al publicado en Git (solo cambian fecha_descarga y version)
diff <(cut -d, -f1-8 "$A/resultados_cierre/elis_fuentes/fuentes_descargadas/INDICE_DESCARGAS.csv") <(cut -d, -f1-8 "$ENT/fuentes_descargadas/INDICE_DESCARGAS.csv") >/dev/null && echo "indice regenerado = indice publicado en id..sha256 (columnas 1-8)" || echo "indice regenerado DIFIERE del publicado en columnas 1-8"
cp "$ENT/fuentes_descargadas/INDICE_DESCARGAS.csv" "$A/.trabajo/elis_fuentes/INDICE_DESCARGAS.csv"
cp "$ENT/fuentes_descargadas/INDICE_DESCARGAS.csv" "$A/resultados_cierre/elis_fuentes/fuentes_descargadas/INDICE_DESCARGAS.csv"
for i in 1 2; do
  "$PY" -I "$A/resultados_cierre/elis_fuentes/scripts/lectura_bloque2.py" >/dev/null 2>&1; echo "lectura run$i exit $?"
  "$PY" -I "$A/resultados_cierre/elis_fuentes/scripts/publicar_extractos.py" >/dev/null 2>&1; echo "extractos run$i exit $?"
  "$PY" -I "$A/resultados_cierre/elis_fuentes/scripts/verificar_segundo_extractor.py" 2>&1 | tail -1 | n; echo "segundo extractor run$i exit ${PIPESTATUS[0]}"
  hashes "$A" > "$W/hash_run$i.txt"
done
echo "-- idempotencia (run1 vs run2):"; diff "$W/hash_run1.txt" "$W/hash_run2.txt" | n || true
echo "-- run2 frente a lo entregado en f00c5dd (archivos distintos):"
(cd "$ENT" && find . -type f ! -path './scripts/*' | sort | xargs sha256sum) > "$W/hash_entrega.txt"
diff "$W/hash_entrega.txt" "$W/hash_run2.txt" | grep '^[<>]' | awk '{print $1, $3}' | sort -k2 | n
echo "-- detalle de diferencias en VERIFICACION_SEGUNDO_EXTRACTOR.json (si las hay):"
diff <("$PY" -I -c "import json,sys; d=json.load(open(sys.argv[1])); d.pop('fecha'); print(json.dumps(d,sort_keys=True,indent=0))" "$ENT/VERIFICACION_SEGUNDO_EXTRACTOR.json") \
     <("$PY" -I -c "import json,sys; d=json.load(open(sys.argv[1])); d.pop('fecha'); print(json.dumps(d,sort_keys=True,indent=0))" "$A/resultados_cierre/elis_fuentes/VERIFICACION_SEGUNDO_EXTRACTOR.json") && echo "iguales salvo 'fecha'"
echo "== B. negativo: excepcion de red en una descarga"
B="$W/B"; prep "$B"
cp "$ENT/fuentes_descargadas/INDICE_DESCARGAS.csv" "$W/indice_antes.csv"
"$PY" -I "$S/s04_descarga_simulada.py" "$B/resultados_cierre/elis_fuentes/scripts/descargar_fuentes_elis.py" "$PDF" "$URD" excepcion 2>&1 | n | tail -3
echo "indice publicado en Git tras el fallo: filas FALLO_DESCARGA = $(grep -c FALLO_DESCARGA "$B/resultados_cierre/elis_fuentes/fuentes_descargadas/INDICE_DESCARGAS.csv"); igual al anterior: $(cmp -s "$W/indice_antes.csv" "$B/resultados_cierre/elis_fuentes/fuentes_descargadas/INDICE_DESCARGAS.csv" && echo si || echo NO)"
"$PY" -I "$B/resultados_cierre/elis_fuentes/scripts/lectura_bloque2.py" 2>&1 | tail -1 | n; echo "lectura tras descarga fallida exit ${PIPESTATUS[0]}"
echo "== C. negativo: 200 text/html en una descarga"
C="$W/C"; prep "$C"
"$PY" -I "$S/s04_descarga_simulada.py" "$C/resultados_cierre/elis_fuentes/scripts/descargar_fuentes_elis.py" "$PDF" "$URD" html 2>&1 | n | tail -3
echo "== D. negativo: patron desplazado a otra pagina -> lectura debe fallar"
D="$W/D"; prep "$D"; cp -r "$A/.trabajo" "$D/"
sed -i 's|("N2", "urd2025", 349, r"Change in receivables|("N2", "urd2025", 348, r"Change in receivables|' "$D/resultados_cierre/elis_fuentes/scripts/lectura_bloque2.py"
"$PY" -I "$D/resultados_cierre/elis_fuentes/scripts/lectura_bloque2.py" 2>&1 | tail -1 | n; echo "exit ${PIPESTATUS[0]}"
echo "== E. negativo: patron con alternativa -> guarda"
E2="$W/E"; prep "$E2"; cp -r "$A/.trabajo" "$E2/"
sed -i 's|r"Change in receivables on disposal of fixed assets 16\\.9 \\(0\\.1\\)"|r"Change in receivables on disposal of fixed assets 16\\.9 \\(0\\.1\\)\|XYZ"|' "$E2/resultados_cierre/elis_fuentes/scripts/lectura_bloque2.py"
grep -c 'XYZ' "$E2/resultados_cierre/elis_fuentes/scripts/lectura_bloque2.py" | sed 's/^/lineas modificadas: /'
"$PY" -I "$E2/resultados_cierre/elis_fuentes/scripts/lectura_bloque2.py" 2>&1 | tail -1 | n; echo "exit ${PIPESTATUS[0]}"
echo "== F. inventario_bloque1.py en un directorio sin los commits (repo git vacio)"
F="$W/F"; prep "$F"; git -C "$F" init -q
"$PY" -I "$F/resultados_cierre/elis_fuentes/scripts/inventario_bloque1.py" 2>&1 | n; echo "exit ${PIPESTATUS[0]}"
echo "== G. dependencias de importacion declaradas en los scripts"
grep -nE "^\s*(import|from) " "$ENT"/scripts/*.py | sed "s|$ENT/||" | grep -vE "import (csv|json|re|sys|hashlib|ssl|subprocess|urllib.request)$|from (datetime|pathlib) " 
grep -rniE "pymupdf|pypdf|requirements|pip install|dependenc" "$ENT/README.md" "$ENT/PUNTO_DE_RECUPERACION.md" | sed "s|$ENT/||" | cut -c1-220
echo "== H. fallo de descarga DESPUES de una ejecucion buena (textos y PDF viejos presentes) y lectura"
H="$W/H"; prep "$H"; cp -r "$A/.trabajo" "$H/"
"$PY" -I "$S/s04_descarga_simulada.py" "$H/resultados_cierre/elis_fuentes/scripts/descargar_fuentes_elis.py" "$PDF" "$URD" excepcion 2>&1 | n | tail -1
"$PY" -I "$H/resultados_cierre/elis_fuentes/scripts/lectura_bloque2.py" 2>&1 | tail -1 | n; echo "lectura exit ${PIPESTATUS[0]}"
"$PY" -I -c "
import json,sys
for l in open(sys.argv[1],encoding='utf-8'):
    d=json.loads(l)
    if d['documento' if d['tipo']=='cita' else 'id']=='q1_2025_revenue': print(d['tipo'], 'sha256=', repr(d.get('sha256_doc', d.get('sha256'))), 'estado=', d.get('estado_preservacion','-')[:20])
" "$H/resultados_cierre/elis_fuentes/LECTURA_FUENTES.jsonl"
echo "== I. descargar sin PyMuPDF instalado (python del sistema)"
I="$W/I"; prep "$I"
python3 -I -c "import fitz" 2>/dev/null && echo "aviso: el python del sistema tiene fitz" || echo "python del sistema sin fitz"
python3 -I "$S/s04_descarga_simulada.py" "$I/resultados_cierre/elis_fuentes/scripts/descargar_fuentes_elis.py" "$PDF" "$URD" ok 2>&1 | n | tail -2
head -c 80 "$I/.trabajo/elis_fuentes/texto/urd2025.txt"; echo
grep -c . "$I/resultados_cierre/elis_fuentes/fuentes_descargadas/INDICE_DESCARGAS.csv" | sed 's/^/lineas indice: /'
python3 -I -c "import csv,sys; print('paginas_pdf registradas sin PyMuPDF:', sorted({r['paginas_pdf'] for r in csv.DictReader(open(sys.argv[1],encoding='utf-8'))}))" "$I/.trabajo/elis_fuentes/INDICE_DESCARGAS.csv"
