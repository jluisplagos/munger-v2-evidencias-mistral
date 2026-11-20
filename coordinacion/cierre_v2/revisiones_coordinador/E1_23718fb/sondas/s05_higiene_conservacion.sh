#!/usr/bin/env bash
# s05 · Higiene del diff 93a9780..f00c5dd y conservacion (solo lectura con git; sin checkout ni worktree).
# Uso: bash s05_higiene_conservacion.sh <repo_auxiliar> <rev_E1>
set -u
A="$1"; REV="$2"; ENT="$REV/entrega/resultados_cierre/elis_fuentes"
g() { git -C "$A" "$@"; }
echo "== commits"; g log --format='%h %an %s' 93a97801f8c4f6a4dc5cabd4540248390cf113d0..f00c5dd | cut -c1-110
echo "padre de f00c5dd: $(g rev-parse --short f00c5dd^)  | padre de 23718fb: $(g rev-parse --short 23718fb^)"
echo "== archivos del diff fuera de resultados_cierre/elis_fuentes/:"; g diff --name-only 93a9780 f00c5dd | grep -v '^resultados_cierre/elis_fuentes/' || echo "(ninguno)"
echo "== n archivos en diff: $(g diff --name-only 93a9780 f00c5dd | wc -l)"
echo "== binarios en diff (numstat '-'):"; g diff --numstat 93a9780 f00c5dd | awk '$1=="-"' ; echo "(fin)"
echo "== extensiones prohibidas en diff y en arbol f00c5dd:"; { g diff --name-only 93a9780 f00c5dd; g ls-tree -r --name-only f00c5dd; } | grep -iE '\.(pdf|xlsx|xls|zip|pyc|docx|png|jpg)$|__pycache__|\.trabajo/' || echo "(ninguno)"
echo "== archivo mayor del diff:"; g diff --name-only 93a9780 f00c5dd | while read f; do echo "$(g cat-file -s f00c5dd:"$f" 2>/dev/null || echo 0) $f"; done | sort -n | tail -1
echo "== patrones de secreto en el diff:"; g diff 93a9780 f00c5dd | grep -nE '^\+' | grep -iE 'ghp_[A-Za-z0-9]{20,}|github_pat_|gho_|xox[bp]-|AKIA[0-9A-Z]{16}|-----BEGIN [A-Z ]*PRIVATE KEY|api[_-]?key\s*[:=]|password\s*[:=]|token\s*[:=]\s*["'"'"'][A-Za-z0-9]' || echo "(ninguno)"
echo "== B/P-M1"; echo "origin/mistral/m2-fundamento-pm1 = $(g rev-parse origin/mistral/m2-fundamento-pm1)"
echo "resultados_m2 en diff 93a9780..f00c5dd: $(g diff --name-only 93a9780 f00c5dd -- resultados_m2 | wc -l)"
echo "resultados_m2 identico ec707a5 vs f00c5dd: $(g diff --quiet ec707a5 f00c5dd -- resultados_m2 && echo si || echo NO)"
echo "== estados en PREGUNTAS_Y_RESULTADOS.csv (estado_tras_revision_e1)"
python3 -I -c "
import csv,sys
for r in csv.DictReader(open(sys.argv[1],encoding='utf-8')): print(r['id'], '->', r['estado_tras_revision_e1'][:60])
" "$ENT/PREGUNTAS_Y_RESULTADOS.csv"
echo "== Elis pendiente_de_datos:"; grep -rlo 'pendiente_de_datos' "$ENT" --include=*.md --include=*.json | sed "s|$ENT/||" | tr '\n' ' '; echo
echo "== otros estados de Elis distintos de pendiente_de_datos (valorad|apta|desbloque):"; grep -rnoiE ".{0,60}(elis (queda|pasa a|esta) (valorad|apt|desbloque)|estado.{0,10}(valorado|apto)).{0,40}" "$ENT" --exclude-dir=extractos | sed "s|$ENT/||" || echo "(ninguno)"
echo "== eleccion de R, theta, lambda, k o umbrales (frases de adopcion):"
grep -rnoiE ".{0,50}(se (elige|adopta|fija|propone)|elegimos|adoptamos|proponemos) (r|θ|theta|λ|lambda|k|el umbral|un umbral)\b.{0,40}" "$ENT" --exclude-dir=extractos | sed "s|$ENT/||" || echo "(ninguna adopcion)"
grep -rnoiE ".{0,40}(no se elige|sin elegir)[^.]{0,80}" "$ENT" --exclude-dir=extractos --include=*.md --include=*.json | sed "s|$ENT/||" | head -5
echo "== ENTREGA.json: integrado, apto, revision"
python3 -I -c "
import json,sys; d=json.load(open(sys.argv[1],encoding='utf-8'))
print('integrado_en_producto=',d['integrado_en_producto'],'| apto_dinero_real=',d['apto_dinero_real'],'| precondiciones_simuladas=',d['precondiciones_simuladas'])
" "$ENT/ENTREGA.json"
echo "== Release fuentes-elis-e-20261117 en el control (coordinacion/cierre-v2)"
g log --format='%h %s' origin/coordinacion/cierre-v2 -3 | cut -c1-120
g grep -n "fuentes-elis-e-20261117" origin/coordinacion/cierre-v2 -- coordinacion | head -3 | cut -c1-200
echo "== la entrega sigue llamando PROVISIONAL a los 11 PDF (desfase no imputable al autor):"
grep -rlc "PROVISIONAL" "$ENT" | sed "s|$ENT/||" | tr '\n' ' '; echo; grep -rc "fuentes-elis-e-20261117" "$ENT" | awk -F: '$2>0' || echo "(ninguna mencion a la Release nueva)"
