#!/usr/bin/env bash
# Comprobaciones de higiene del revisor (D2, bloques 1 y 2). Solo lectura: git show/diff/archive y sha256sum.
# Uso: bash comprobaciones_d2.sh <repo evidencias-mistral> <rev_D2>
set -u
R="$1"; S="$2"
for par in "3934bc9 entrega" "5f4b2a2 entrega2"; do
  set -- $par
  echo "== manifiesto en $1 (sha256sum -c desde resultados_qwen/ejecucion_d)"
  ( cd "$S/$2/resultados_qwen/ejecucion_d" && sha256sum -c MANIFIESTO_SHA256.txt 2>/dev/null | grep -v ': OK$'; echo "exit=${PIPESTATUS[0]}" )
  echo "== archivos del árbol fuera del manifiesto en $1"
  ( cd "$S/$2/resultados_qwen/ejecucion_d" && comm -13 <(awk '{print $2}' MANIFIESTO_SHA256.txt | sed 's|^\./||' | sort) <(find . -type f ! -name MANIFIESTO_SHA256.txt | sed 's|^\./||' | sort) )
done
for rango in "1ac661b 3934bc9" "1ac661b 5f4b2a2"; do
  set -- $rango
  echo "== git diff --name-only $1 $2"
  git -C "$R" diff --name-only "$1" "$2"
  echo "-- binarios/caches:"; git -C "$R" diff --name-only "$1" "$2" | grep -iE '\.(pdf|xlsx|xls|zip|pyc)$|__pycache__' || echo "ninguno"
  echo "-- numstat binario:"; git -C "$R" diff --numstat "$1" "$2" | awk '$1=="-"' | grep . || echo "ninguno"
  echo "-- patrones de secreto:"; git -C "$R" diff "$1" "$2" | grep -inE 'ghp_|github_pat|sk-[A-Za-z0-9]{10}|AKIA|BEGIN .*PRIVATE|api[_-]?key|password|bearer' || echo "ninguno"
  echo "-- salidas publicadas tocadas (ENTREGA, MATRIZ, relevo, evidencias, HALLAZGOS, RESUMEN, manifiesto):"
  git -C "$R" diff --name-only "$1" "$2" -- resultados_qwen/ejecucion_d/ENTREGA.json resultados_qwen/ejecucion_d/MATRIZ_EJECUCION.csv resultados_qwen/ejecucion_d/relevo resultados_qwen/ejecucion_d/evidencias resultados_qwen/ejecucion_d/HALLAZGOS.md resultados_qwen/ejecucion_d/RESUMEN_PARA_INTEGRADOR.md resultados_qwen/ejecucion_d/MANIFIESTO_SHA256.txt | grep . || echo "ninguna"
done
echo "== banco 4745f38 (sha256sum -c)"; ( cd "$S/banco/resultados_qwen/q1_v2/banco_revisado" && sha256sum -c MANIFIESTO_SHA256.txt >/dev/null; echo "exit=$?" )
echo "== ENTREGA.json publicado: base_revisada_sha y bloque"
python3 -I -c "import json,sys; d=json.load(open(sys.argv[1])); print(d['base_revisada_sha'], '|', d['bloque'])" "$S/entrega2/resultados_qwen/ejecucion_d/ENTREGA.json"
echo "== claves de la plantilla ausentes en ENTREGA.json"
python3 -I -c "import json,sys; p=json.loads(sys.stdin.read()); e=json.load(open(sys.argv[1])); print(sorted(set(p)-set(e)) or 'ninguna')" "$S/entrega2/resultados_qwen/ejecucion_d/ENTREGA.json" < <(git -C "$R" show origin/coordinacion/cierre-v2:coordinacion/cierre_v2/PLANTILLA_ENTREGA.json)
echo "== git status del repositorio"; git -C "$R" status --porcelain | grep . || echo "limpio"
