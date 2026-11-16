#!/usr/bin/env bash
# Comprobaciones del revisor sobre la copia aislada de 1ac661b (no ejecuta el producto).
# Uso: bash comprobaciones_revisor.sh <rev_D>
set -u
S="$1"; E="$S/entrega/resultados_qwen/ejecucion_d"; B="$S/banco/resultados_qwen/q1_v2/banco_revisado"
echo "== manifiesto entrega"; (cd "$E" && sha256sum -c --quiet MANIFIESTO_SHA256.txt; echo "exit=$?")
echo "== manifiesto banco 4745f38"; (cd "$B" && sha256sum -c --quiet MANIFIESTO_SHA256.txt; echo "exit=$?")
echo "== regeneración matriz/recuentos/relevo en copia"
W="$S/trabajo_regen"; rm -rf "$W"; cp -a "$E" "$W"
BANCO_DIR="$B" python3 -I -B "$W/scripts/generar_matriz.py" >/dev/null; echo "generar_matriz exit=$?"
BANCO_DIR="$B" python3 -I -B "$W/scripts/generar_relevo.py" >/dev/null; echo "generar_relevo exit=$?"
for f in MATRIZ_EJECUCION.csv evidencias/recuentos.json relevo/PAQUETES_RELEVO.json; do cmp -s "$E/$f" "$W/$f" && echo "IGUAL $f" || echo "DIFIERE $f"; done
rm -rf "$W"
