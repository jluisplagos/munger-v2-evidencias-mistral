#!/bin/bash
# uso: descargar.sh LISTA.tsv DESTINO LOG.tsv   (LISTA: nombre<TAB>url<TAB>descripcion)
set -u
LISTA=$1; DEST=$2; LOG=$3
[ -f "$LOG" ] || printf 'archivo\turl\tfecha_utc\thttp\tbytes\tsha256\tpaginas\tcontent_type\terror\tdescripcion\n' > "$LOG"
while IFS=$'\t' read -r nombre url desc; do
  [ -z "$nombre" ] && continue
  fecha=$(date -u +%Y-%m-%dT%H:%M:%SZ)
  tmp="$DEST/.parcial_$nombre"
  out=$(curl -sS -L --fail --proto '=https' --max-time 900 -A "Mozilla/5.0" -o "$tmp" -w '%{http_code}\t%{content_type}' "$url" 2>&1); rc=$?
  http=$(printf '%s' "$out" | tail -1 | cut -f1); ct=$(printf '%s' "$out" | tail -1 | cut -f2)
  if [ $rc -ne 0 ]; then
    err=$(printf '%s' "$out" | head -1 | tr '\t\n' '  ')
    rm -f "$tmp"; printf '%s\t%s\t%s\t%s\t\t\t\t%s\tcurl rc=%s %s\t%s\n' "$nombre" "$url" "$fecha" "$http" "$ct" "$rc" "$err" "$desc" >> "$LOG"; continue
  fi
  if [ "$(head -c 5 "$tmp")" != "%PDF-" ]; then
    rm -f "$tmp"; printf '%s\t%s\t%s\t%s\t\t\t\t%s\tno es PDF\t%s\n' "$nombre" "$url" "$fecha" "$http" "$ct" "$desc" >> "$LOG"; continue
  fi
  mv "$tmp" "$DEST/$nombre"
  bytes=$(stat -c %s "$DEST/$nombre"); sha=$(sha256sum "$DEST/$nombre" | cut -d' ' -f1)
  pags=$(pdfinfo "$DEST/$nombre" 2>/dev/null | awk '/^Pages:/{print $2}')
  printf '%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t\t%s\n' "$nombre" "$url" "$fecha" "$http" "$bytes" "$sha" "$pags" "$ct" "$desc" >> "$LOG"
done < "$LISTA"
