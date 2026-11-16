#!/usr/bin/env bash
# S05 · Higiene del diff ec707a5..93a9780, manifiesto, rama B/P-M1 y estado de los documentos de la carpeta.
# Uso: bash s05_higiene.sh <repo_auxiliar> <dir_entrega_extraida>
set -u
A="$1"; E="$2"
echo "== HEAD rama entrega"; git -C "$A" rev-parse origin/mistral/e-fuentes-elis
echo "== commits ec707a5..93a9780"; git -C "$A" log --format='%h %an <%ae> %ad %s' --date=iso ec707a5..93a9780 | cut -c1-140
echo "== archivos en el diff"; git -C "$A" diff --name-only ec707a5 93a9780
echo "== fuera de resultados_cierre/elis_fuentes/ (vacio = bien)"; git -C "$A" diff --name-only ec707a5 93a9780 | grep -v '^resultados_cierre/elis_fuentes/' || true
echo "== binarios/caches por extension o ruta (vacio = bien)"; git -C "$A" diff --name-only ec707a5 93a9780 | grep -Ei '\.(pdf|xlsx|xlsm|xls|zip|7z|gz|pyc|db|sqlite|env|pem|key|p12)$|__pycache__|\.trabajo/|\.cache' || true
echo "== numstat binario (vacio = bien)"; git -C "$A" diff --numstat ec707a5 93a9780 | awk '$1=="-"' 
echo "== patrones de secreto (vacio = bien)"; git -C "$A" diff ec707a5 93a9780 | grep -E '^\+' | grep -Eo '(ghp_[A-Za-z0-9]{20,}|github_pat_[A-Za-z0-9_]{20,}|AKIA[0-9A-Z]{16}|sk-[A-Za-z0-9]{20,}|-----BEGIN [A-Z ]*PRIVATE KEY-----|[Bb]earer [A-Za-z0-9._-]{20,})' || true
echo "== tamano maximo de archivo anadido (bytes)"; git -C "$A" ls-tree -r -l 93a9780 resultados_cierre/elis_fuentes | sort -k4 -n | tail -1
echo "== .gitignore en 93a9780"; git -C "$A" show 93a9780:.gitignore
echo "== INDICE_DESCARGAS / .trabajo en el arbol 93a9780 (vacio = no publicados)"; git -C "$A" ls-tree -r --name-only 93a9780 | grep -E 'INDICE_DESCARGAS|^\.trabajo' || true
echo "== sha256sum -c del manifiesto (en su carpeta)"; (cd "$E/resultados_cierre/elis_fuentes" && sha256sum -c MANIFIESTO_SHA256.txt; echo "exit=$?")
echo "== archivos de la carpeta no listados en el manifiesto"; (cd "$E/resultados_cierre/elis_fuentes" && find . -type f ! -name MANIFIESTO_SHA256.txt | sed 's#^\./##' | sort > /tmp/.s05_a.$$; awk '{print $2}' MANIFIESTO_SHA256.txt | sort > /tmp/.s05_b.$$; comm -23 /tmp/.s05_a.$$ /tmp/.s05_b.$$; rm -f /tmp/.s05_a.$$ /tmp/.s05_b.$$)
echo "== B/P-M1"; git -C "$A" rev-parse origin/mistral/m2-fundamento-pm1
git -C "$A" diff --name-only ec707a5 93a9780 | grep -E '^resultados_m2/' || echo "ningun archivo resultados_m2/ en el diff"
git -C "$A" diff --quiet ec707a5 93a9780 -- resultados_m2 && echo "resultados_m2 identico entre ec707a5 y 93a9780"
echo "== textos desfasados dentro de la entrega"
grep -n 'Bloque 2 (pendiente)\|Bloque 3 (pendiente)' "$E/resultados_cierre/elis_fuentes/README.md" || true
grep -n '^# ' "$E/resultados_cierre/elis_fuentes/RESUMEN_PARA_INTEGRADOR.md" "$E/resultados_cierre/elis_fuentes/HALLAZGOS_ELIS.md"
grep -n 'este commit' "$E/resultados_cierre/elis_fuentes/ENTREGA.json" "$E/resultados_cierre/elis_fuentes/PUNTO_DE_RECUPERACION.md"
grep -n 'ff0c60cd\|2fea890' "$E/resultados_cierre/elis_fuentes/PUNTO_DE_RECUPERACION.md" "$E/resultados_cierre/elis_fuentes/ENTREGA.json" "$E/resultados_cierre/elis_fuentes/RESUMEN_PARA_INTEGRADOR.md" | cut -c1-200
echo "== frases 'no publicado' / 'no localizado'"
grep -n -o -i '.\{0,50\}no publicad[ao].\{0,60\}\|.\{0,30\}not published.\{0,30\}\|.\{0,40\}sigue sin publicar.\{0,40\}\|.\{0,30\}ninguna parte.\{0,30\}' "$E"/resultados_cierre/elis_fuentes/*.md "$E"/resultados_cierre/elis_fuentes/*.csv "$E"/resultados_cierre/elis_fuentes/*.json "$E"/resultados_cierre/elis_fuentes/*.jsonl | cut -c1-220
echo "== recuento 'no localizado en esta busqueda'"; grep -o -i 'no localizado en esta b[uú]squeda' -r "$E/resultados_cierre/elis_fuentes" | wc -l
