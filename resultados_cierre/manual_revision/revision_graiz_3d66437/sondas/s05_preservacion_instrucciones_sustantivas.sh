#!/bin/sh
# s05: criterio 2 — todas las instrucciones sustantivas se conservan (mismas líneas en base y head)
# Uso: sh s05_preservacion_instrucciones_sustantivas.sh [workdir de s02/s03]
set -u
PROD=repos/jluisplagos/munger-v2
BASE=957af652cdc3bef3d67e8623c9572138bac685e9
HEAD=3d66437e797b6b0bf137b42fa62b561f39121722
W=${1:-}
if [ -z "$W" ] || [ ! -d "$W" ]; then
  W=$(mktemp -d /tmp/graiz_s05.XXXXXX)
  for f in CLAUDE.md README.md docs/MIGRATION_STATUS.json; do
    o=$(echo "$f" | tr '/' '_')
    gh api "$PROD/contents/$f?ref=$BASE" -H 'Accept: application/vnd.github.raw' > "$W/base_$o"
    gh api "$PROD/contents/$f?ref=$HEAD" -H 'Accept: application/vnd.github.raw' > "$W/head_$o"
  done
fi
echo "== s05 G-RAIZ $(date -u +%FT%TZ) workdir=$W =="

echo "-- líneas ELIMINADAS o cambiadas en CLAUDE.md (diff, lado base):"
diff "$W/base_CLAUDE.md" "$W/head_CLAUDE.md" | grep '^<' || echo "(ninguna)"
echo
echo "-- líneas ELIMINADAS o cambiadas en README.md:"
diff "$W/base_README.md" "$W/head_README.md" | grep '^<' || echo "(ninguna)"
echo
echo "-- palabras clave de instrucciones sustantivas presentes en AMBOS (base -> head), CLAUDE.md:"
for kw in 'originales' 'fuentes ni huellas' 'LibreOffice y pipelines que lo usan van en secuencia' 'aprobaciones retiradas' 'pol.tica econ.mica' 'Opus con esfuerzo alto' 'Fable con esfuerzo' 'agente distinto del autor del cambio' 'ZIP original completo de la Release base-4.14' 'herramientas de recuperaci.n son exclusivas'; do
  b=$(grep -c -i "$kw" "$W/base_CLAUDE.md" || true)
  h=$(grep -c -i "$kw" "$W/head_CLAUDE.md" || true)
  printf '  %-70s base=%s head=%s\n' "$kw" "$b" "$h"
done
echo
echo "-- mismas palabras clave en README.md:"
for kw in 'base-4.14' 'base_414.py' 'en secuencia' 'aprobaciones retiradas' 'originales, fuentes y evidencias' 'No a.adir credenciales' 'versión nueva en otra rama'; do
  b=$(grep -c -i "$kw" "$W/base_README.md" || true)
  h=$(grep -c -i "$kw" "$W/head_README.md" || true)
  printf '  %-70s base=%s head=%s\n' "$kw" "$b" "$h"
done
echo
echo "-- líneas de instrucción intactas (head CLAUDE.md 22-26, 28-31, 37; head README 5, 55-56, 60):"
sed -n '22,26p;28,31p;37p' "$W/head_CLAUDE.md"
sed -n '5p;55,56p;60p' "$W/head_README.md"
echo
echo "-- bloques intactos: ¿cuadran los diffs solo en las líneas de hechos? (líneas añadadas):"
diff "$W/base_CLAUDE.md" "$W/head_CLAUDE.md" | grep '^>' | wc -l
diff "$W/base_README.md" "$W/head_README.md" | grep '^>' | wc -l
