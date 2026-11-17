#!/bin/sh
# Descarga (solo lectura) de los 4 diff_rutas en base 957af65 y en head c0542b83, y sus SHA-256
BASE=957af652cdc3bef3d67e8623c9572138bac685e9
HEAD=c0542b83b9923f98124d3c72e48b7fc7245284d2
mkdir -p material/base material/head
for f in "munger_v2_r1/personaje_v2/GUIA_RECORRIDO_SUPERVISADO.md" "munger_v2_r1/CONTINUIDAD.md" "munger_v2_r1/CAMBIOS_ARCHIVOS.txt" "munger_v2_r1/MANIFIESTO_SHA256.txt"; do
  n=$(echo "$f" | tr '/' '_')
  gh api "repos/jluisplagos/munger-v2/contents/$f?ref=$BASE" -H 'Accept: application/vnd.github.raw' > "material/base/$n"
  gh api "repos/jluisplagos/munger-v2/contents/$f?ref=$HEAD" -H 'Accept: application/vnd.github.raw' > "material/head/$n"
done
sha256sum material/base/* material/head/*
