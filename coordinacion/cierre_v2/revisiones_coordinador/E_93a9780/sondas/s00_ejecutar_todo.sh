#!/usr/bin/env bash
# S00 · Ejecuta todas las sondas del revisor en secuencia, sin red y sin escribir en ningun repositorio.
# Uso: bash s00_ejecutar_todo.sh <base414> <rev_E> <repo_auxiliar> <repo_producto>
# Las salidas .out se normalizan sustituyendo rutas absolutas por <base414>, <rev_E>, <aux> y <prod>.
set -u
B414="$1"; REV="$2"; AUX="$3"; PROD="$4"
S="$REV/sondas"; E="$REV/entrega/resultados_cierre/elis_fuentes"
URD="$B414/personaje_v2/empresas_v2_correcciones/2026-11_Vidrala_ensayo_4_14/elis_decisiones/Elis/fuentes_pdf/Elis - 2025 Universal Registration Document.pdf"
DEC="$B414/personaje_v2/empresas_v2_correcciones/2026-11_Vidrala_ensayo_4_14/elis_decisiones"
FR="$DEC/Elis/fuentes_2026/pdf/Elis_Resultats_annuels_2025_communique.pdf"
cd "$S" || exit 2
run() { local n="$1"; shift; "$@" > "$S/$n.out" 2>&1; echo "exit=$?" >> "$S/$n.out"; }
run s01_citas_urd2025 python3 -I s01_citas_urd2025.py "$URD" "$E/LECTURA_FUENTES.jsonl" "$S/s01_citas_urd2025.json"
run s02_cifras_urd2025 python3 -I s02_cifras_urd2025.py "$URD" "$S/s02_cifras_urd2025.json"
run s03_corroboracion_local python3 -I s03_corroboracion_local.py "$DEC" "$E/LECTURA_FUENTES.jsonl" "$S/s03_corroboracion_local.json"
run s03b_equivalentes_fr python3 -I s03b_equivalentes_fr.py "$FR"
run s04_entrega_y_preservacion python3 -I s04_entrega_y_preservacion.py "$E" "$REV/coord/PLANTILLA_ENTREGA.json" /home /tmp /root /srv /opt /var /mnt -- "$S/s04_entrega_y_preservacion.json"
run s05_higiene bash s05_higiene.sh "$AUX" "$REV/entrega"
run s06_scripts_y_texto python3 -I s06_scripts_y_texto.py "$E" "$PROD" "$AUX" "$S/s06_scripts_y_texto.json"
for f in "$S"/*.out "$S"/*.json; do
  sed -i -e "s#$B414#<base414>#g" -e "s#$REV#<rev_E>#g" -e "s#$AUX#<aux>#g" -e "s#$PROD#<prod>#g" "$f"
done
grep -H '^exit=' "$S"/*.out
