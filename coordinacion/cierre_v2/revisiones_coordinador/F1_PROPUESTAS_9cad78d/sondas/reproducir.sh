#!/bin/bash
# Revisión de las propuestas F1 (9cad78d) · reproducción completa de las sondas del revisor.
# Uso: sondas/reproducir.sh   (escribe solo dentro de la carpeta de la revisión)
# Requiere: la copia del commit 9cad78d en ../copia (git archive), con los cinco PDF de Elis y el libro evaluado
# copiados en su ruta de munger_v2_r1 (huellas de datos/fuentes.json), y la Release fuentes-elis-e-20261117 en ../release/pdf.
set -u
AQUI="$(cd "$(dirname "$0")" && pwd)"
REV="$(dirname "$AQUI")"
F="$REV/copia/docs/validacion_economica_paralela/frente_E_F1_elis"
RAIZ="$REV/copia/munger_v2_r1"
ELIS="$RAIZ/personaje_v2/empresas_v2_correcciones/2026-11_Vidrala_ensayo_4_14/elis_decisiones/Elis"
LIBRO="$ELIS/Elis_v63_evaluada.xlsx"
REL="$REV/release/pdf"
OUT="$AQUI/repro"
mkdir -p "$OUT"
export PYTHONDONTWRITEBYTECODE=1
ok=0; mal=0
paso() { if [ "$2" -eq 0 ]; then echo "[OK ] $1"; ok=$((ok+1)); else echo "[MAL] $1 (código $2)"; mal=$((mal+1)); fi; }

echo "== 0. Material"
echo "commit revisado: 9cad78ddc6bba6e3597517cde6a8045960f0bdda (copia por git archive)"
( cd "$ELIS" && sha256sum fuentes_pdf/*.pdf Elis_v63_evaluada.xlsx )
( cd "$REL" && sha256sum -c SHA256SUMS ) ; paso "Release fuentes-elis-e-20261117: 11 PDF con su SHA256SUMS" $?
python3 -I - "$F" <<'EOF'
import hashlib, os, re, sys
base = sys.argv[1]; ok = bad = 0
for ln in open(os.path.join(base, "MANIFIESTO_SHA256.txt"), encoding="utf-8"):
    m = re.match(r"^([0-9a-f]{64})\s+\*?(.+)$", ln.rstrip("\n"))
    if m:
        h, p = m.groups()
        good = os.path.exists(os.path.join(base, p)) and hashlib.sha256(open(os.path.join(base, p), "rb").read()).hexdigest() == h
        ok += good; bad += not good
print(f"manifiesto del frente: {ok} de {ok + bad}")
sys.exit(1 if bad else 0)
EOF
paso "manifiesto del frente" $?

echo; echo "== 1. Scripts del autor sobre la copia (salidas fuera del árbol del autor)"
( cd "$F/scripts" && python3 -I verificar_cifras.py --raiz "$RAIZ" --datos ../datos/cifras_fuente.csv --fuentes ../datos/fuentes.json --salida "$OUT/verificacion_cifras.json" > "$OUT/verificar_cifras.log" 2>&1 ); rc=$?
[ "$rc" -eq 2 ]; paso "verificar_cifras.py (código 2 = hay PENDIENTE y ningún FALLO)" $?
cmp -s "$F/resultados/verificacion_cifras.json" "$OUT/verificacion_cifras.json"; paso "salida idéntica byte a byte a la entregada: verificacion_cifras.json" $?
( cd "$F/scripts" && python3 -I copia_investigacion_f1.py --cifras ../datos/cifras_fuente.csv --verificacion ../resultados/verificacion_cifras.json \
    --libro "$LIBRO" --contraste ../resultados/contraste_f1.json --salida "$OUT/copia_investigacion_f1.json" --informe "$OUT/copia_investigacion_f1.md" --raiz "$RAIZ" )
paso "copia_investigacion_f1.py" $?
( cd "$F/scripts" && python3 -I n1_alcance_y_actualizacion.py --cifras ../datos/cifras_fuente.csv --verificacion ../resultados/verificacion_cifras.json \
    --libro "$LIBRO" --copia ../resultados/copia_investigacion_f1.json --salida "$OUT/n1_alcance_y_actualizacion.json" --informe "$OUT/n1_alcance_y_actualizacion.md" \
    --raiz "$RAIZ" --release "$REL" )
paso "n1_alcance_y_actualizacion.py (107 controles; 103 lecturas; 19 pasajes)" $?
( cd "$F/scripts" && python3 -I umbral_v_f1a_frontera.py --salida "$OUT/umbral_v_f1a_frontera.json" --informe "$OUT/umbral_v_f1a_frontera.md" \
    --cifras ../datos/cifras_fuente.csv --verificacion ../resultados/verificacion_cifras.json --n1 ../resultados/n1_alcance_y_actualizacion.json )
paso "umbral_v_f1a_frontera.py (30 casos; 14 directas; 6 variantes)" $?
for a in copia_investigacion_f1.json copia_investigacion_f1.md n1_alcance_y_actualizacion.json n1_alcance_y_actualizacion.md umbral_v_f1a_frontera.json umbral_v_f1a_frontera.md; do
  cmp -s "$F/resultados/$a" "$OUT/$a"; paso "salida idéntica byte a byte a la entregada: $a" $?
done

echo; echo "== 2. Sondas del revisor"
cd "$AQUI"
python3 -I s1_recalculo_independiente_n1.py "$F/datos/cifras_fuente.csv" "$LIBRO" > s1_recalculo_independiente_n1.log 2>&1; paso "s1 · recálculo independiente de N1 (18 cifras)" $?
python3 -I s2_mutantes_script_n1.py "$F/scripts" "$RAIZ" "$REL" "$LIBRO" > s2_mutantes_script_n1.log 2>&1; grep -q "no detectados: 0" s2_mutantes_script_n1.log; paso "s2 · 14 mutantes del script de N1, todos detectados" $?
python3 -I s2b_mutantes_sin_control.py "$F/scripts" "$RAIZ" "$REL" "$LIBRO" > s2b_mutantes_sin_control.log 2>&1; paso "s2b · mutantes sobre cifras sin control propio (informativa)" $?
python3 -I s3_umbral_independiente.py "$F/scripts" "$F/datos/cifras_fuente.csv" "$LIBRO" > s3_umbral_independiente.log 2>&1; paso "s3 · regla del umbral escrita aparte: 30 de 30 casos" $?
python3 -I s3b_coma_flotante.py > s3b_coma_flotante.log 2>&1; paso "s3b · coma flotante (informativa)" $?
python3 -I s3c_mutantes_script_umbral.py "$F/scripts" > s3c_mutantes_script_umbral.log 2>&1; ! grep -q "NO DETECTADO" s3c_mutantes_script_umbral.log; paso "s3c · 6 mutantes del script del umbral, todos detectados" $?
python3 -I s4_indicacion_fiscal_2021.py > s4_indicacion_fiscal_2021.log 2>&1; paso "s4 · indicación fiscal de 2021 y línea fiscal 2022–25 (lecturas en página)" $?
python3 -I s5_pasivo_pagos_intereses.py > s5_pasivo_pagos_intereses.log 2>&1; paso "s5 · pasivo, residuo de 2024 e intereses pagados de 2023 (lecturas en página)" $?
python3 -I s6_segundo_extractor.py > s6_segundo_extractor.log 2>&1; paso "s6 · 25 cifras clave con un segundo extractor (pypdf)" $?
rm -rf "$AQUI/mut" "$AQUI/mut_umbral" "$AQUI/mut_datos" "$AQUI/__pycache__" "$F/scripts/__pycache__"
echo; echo "RESUMEN: $ok pasos correctos, $mal con fallo"
exit $mal
