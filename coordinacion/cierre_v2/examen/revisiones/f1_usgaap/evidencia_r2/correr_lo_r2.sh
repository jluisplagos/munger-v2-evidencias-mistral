#!/usr/bin/env bash
# Ronda 2 · reproducción de las pruebas con LibreOffice del autor (copia de revisión de bcb6dc3; con el cerrojo de LibreOffice, una detrás de otra)
set -uo pipefail
export PYTHONDONTWRITEBYTECODE=1
R=${COPIA_REVISION:-/home/user/e_work/revision_usgaap/copia2/munger_v2_r1}
EV=${EV:-/home/user/e_work/revision_usgaap/evidencia_r2}
SP=${TMP_R2:-${TMPDIR:-/tmp}/rev_f1_usgaap_r2}/lo2
US=empresas_v2_correcciones/2026-11_Vidrala_ensayo_4_15/f1_usgaap/scripts
IM=empresas_v2_correcciones/2026-11_Vidrala_ensayo_4_15/f1_impl/scripts
L=/home/user/e_work/libreoffice.lock
rm -f "$EV/lo_resumen.txt"
cd "$R/personaje_v2"
( time flock $L python3 -B "$US/prueba_pipeline_usgaap.py" ) > "$EV/prueba_pipeline_usgaap.txt" 2>&1; echo "pipeline_usgaap rc=$?" >> "$EV/lo_resumen.txt"
cd "$R"
rm -rf "$SP/d_us"; ( time flock $L python3 -I "personaje_v2/$US/probar_libro_v631_usgaap.py" "$SP/d_us" ) > "$EV/probar_libro_v631_usgaap.txt" 2>&1; echo "libro_v631_usgaap rc=$?" >> "$EV/lo_resumen.txt"
cd "$R/personaje_v2"
( time flock $L python3 -B "$IM/prueba_pipeline_f1.py" ) > "$EV/prueba_pipeline_f1.txt" 2>&1; echo "pipeline_f1 rc=$?" >> "$EV/lo_resumen.txt"
echo FIN >> "$EV/lo_resumen.txt"
