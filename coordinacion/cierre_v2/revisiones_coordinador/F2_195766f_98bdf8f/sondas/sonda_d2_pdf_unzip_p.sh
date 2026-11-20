#!/bin/bash
# Uso: sonda_d2_pdf_unzip_p.sh <zip> <huellas_todas_las_fuentes.csv> <salida_dir>
# Calcula por su cuenta (unzip -p | sha256sum, wc -c) la huella de cada PDF del ZIP
# y la compara con el CSV publicado. No usa zipfile de Python.
set -u
Z="$1"; H="$2"; O="$3"; mkdir -p "$O"
unzip -Z1 "$Z" | grep -i '\.pdf$' | LC_ALL=C sort > "$O/pdf_en_zip.txt"
: > "$O/pdf_unzip_p.csv"
while IFS= read -r n; do
  rel="${n#munger_v2_r1/}"
  sha=$(unzip -p "$Z" "$n" | sha256sum | cut -d' ' -f1)
  sz=$(unzip -p "$Z" "$n" | wc -c)
  printf '%s,%s,%s\n' "$rel" "$sz" "$sha" >> "$O/pdf_unzip_p.csv"
done < "$O/pdf_en_zip.txt"
echo "PDF en el ZIP: $(wc -l < "$O/pdf_en_zip.txt")"
grep -v '^release/' "$H" | cut -d, -f1-3 | LC_ALL=C sort > "$O/pdf_publicado.csv"
LC_ALL=C sort "$O/pdf_unzip_p.csv" > "$O/pdf_unzip_p.sorted.csv"
echo "Filas PDF publicadas: $(wc -l < "$O/pdf_publicado.csv")"
if diff "$O/pdf_unzip_p.sorted.csv" "$O/pdf_publicado.csv" > "$O/diff.txt"; then echo "COINCIDEN 71/71 (ruta, bytes, SHA-256)"; else echo "DIFIEREN"; cat "$O/diff.txt"; fi
echo "SHA-256 distintos: $(cut -d, -f3 "$O/pdf_unzip_p.csv" | sort -u | wc -l)"
echo "Fila release: $(grep '^release/' "$H")"
echo "Longitud SHA release: $(grep '^release/' "$H" | cut -d, -f3 | tr -d '\r\n' | wc -c)"
echo "SHA del ZIP (sha256sum): $(sha256sum "$Z" | cut -d' ' -f1)"
