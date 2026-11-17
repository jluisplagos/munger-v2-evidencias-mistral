#!/usr/bin/env bash
# Comprobaciones del revisor sobre d032691 (sin producto, sin LibreOffice, sin red).
# Uso: bash comprobaciones_d3.sh <repo munger-v2-evidencias-mistral> <rev_D3>
set -u
REPO="$1"; R="$2"
E="$R/entrega/resultados_qwen/ejecucion_d"; B="$R/banco/resultados_qwen/q1_v2/banco_revisado"
echo "== diff --stat 5f4b2a2 d032691 (solo .py y .sh)"; git -C "$REPO" diff --stat 5f4b2a2 d032691 -- '*.py' '*.sh'; echo "exit=$?"
for f in lib_arnes.py ejecutar_caso.py generar_matriz.py generar_relevo.py generar_correspondencia.py pruebas_arnes.py preparar_entorno.sh; do
  n=$(git -C "$REPO" diff --name-only 5f4b2a2 d032691 -- "resultados_qwen/ejecucion_d/scripts/$f" | wc -l); echo "  $f cambiado_en_d032691=$n"; done
echo "== fechas"; git -C "$REPO" log -1 --format='d032691 %ci' d032691
git -C "$REPO" log -1 --format='CORRECCION_D3 publicada en %h %ci' origin/coordinacion/cierre-v2 -- coordinacion/cierre_v2/revisiones_coordinador/D2_3934bc9_5f4b2a2/CORRECCION_D3.md
echo "== manifiesto"; (cd "$E" && sha256sum -c MANIFIESTO_SHA256.txt >/dev/null 2>&1; echo "sha256sum -c exit=$?"; \
  echo "entradas=$(wc -l < MANIFIESTO_SHA256.txt) archivos=$(find . -type f ! -name MANIFIESTO_SHA256.txt | wc -l)"; \
  diff <(find . -type f ! -name MANIFIESTO_SHA256.txt | sed 's|^\./||' | sort) <(awk '{print $2}' MANIFIESTO_SHA256.txt | sed 's|^\*||;s|^\./||' | sort) >/dev/null; echo "lista_igual_a_carpeta diff_exit=$?")
echo "== banco"; (cd "$B" && sha256sum -c MANIFIESTO_SHA256.txt >/dev/null 2>&1; echo "banco sha256sum -c exit=$?")
echo "== regeneración en copia"
T=$(mktemp -d); cp -a "$E" "$T/d"
for s in generar_matriz generar_correspondencia generar_relevo; do BANCO_DIR="$B" python3 -I -B "$T/d/scripts/$s.py" >/dev/null; echo "  $s exit=$?"; done
for f in MATRIZ_EJECUCION.csv MAPA_CRITERIOS_BANCO.csv relevo/PAQUETES_RELEVO.json evidencias/recuentos.json; do cmp -s "$E/$f" "$T/d/$f"; echo "  cmp $f exit=$?"; done
python3 -I -B -c "import json,sys; r=json.load(open(sys.argv[1])); print('  recuentos:', r['estado_ejecucion'], r['veredicto_componente'], r['veredicto_caso'], r.get('criterios_banco'))" "$E/evidencias/recuentos.json"
rm -rf "$T"
echo "== marcas y logs publicados"
echo "  sellar --revisor distintos: $(grep -ho -- '--revisor [^-]*' "$E"/evidencias/Q1-*/ejecucion.log | sort -u | tr '\n' '|')"
echo "  logs con más de una cabecera: $(grep -c '^# Caso' "$E"/evidencias/Q1-*/ejecucion.log | grep -vc ':1$')"
echo "  archivos de evidencia cambiados en d032691 que no son log ni resultado:"; git -C "$REPO" diff --name-only 5f4b2a2 d032691 -- resultados_qwen/ejecucion_d/evidencias | grep -v -E 'ejecucion.log$|resultado_ejecucion.json$' | sed 's/^/    /'
echo "== git status del repositorio (debe estar vacío)"; git -C "$REPO" status --porcelain | head -5; echo "fin"
