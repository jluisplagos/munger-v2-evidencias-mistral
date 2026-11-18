#!/usr/bin/env bash
# Reproducción de las pruebas con LibreOffice declaradas en F1_USGAAP.md §8 (copia de revisión; con el cerrojo de LibreOffice)
set -uo pipefail
export PYTHONDONTWRITEBYTECODE=1
R=/home/user/e_work/revision_usgaap/copia/munger_v2_r1
EV=/home/user/e_work/revision_usgaap/evidencia
SP=/tmp/claude-0/-home-user/b9d62468-c45b-5fe5-8762-d58eebe9c95a/scratchpad/lo
US=empresas_v2_correcciones/2026-11_Vidrala_ensayo_4_15/f1_usgaap/scripts
IM=empresas_v2_correcciones/2026-11_Vidrala_ensayo_4_15/f1_impl/scripts
L=/home/user/e_work/libreoffice.lock
cd "$R/personaje_v2"
( time flock $L python3 -B "$US/prueba_pipeline_usgaap.py" ) > "$EV/prueba_pipeline_usgaap.txt" 2>&1; echo "pipeline_usgaap rc=$?" >> "$EV/lo_resumen.txt"
cd "$R"
rm -rf "$SP/d_us"; ( time flock $L python3 -I "personaje_v2/$US/probar_libro_v631_usgaap.py" "$SP/d_us" ) > "$EV/probar_libro_v631_usgaap.txt" 2>&1; echo "libro_v631_usgaap rc=$?" >> "$EV/lo_resumen.txt"
rm -rf "$SP/d_a0"; ( time flock $L python3 -I v6/v631_f1/scripts/probar_v631_f1.py a0 "$SP/d_a0" ) > "$EV/probar_v631_a0.txt" 2>&1; echo "v631_a0 rc=$?" >> "$EV/lo_resumen.txt"
rm -rf "$SP/d_f1"; ( time flock $L python3 -I v6/v631_f1/scripts/probar_v631_f1.py f1 "$SP/d_f1" ) > "$EV/probar_v631_f1.txt" 2>&1; echo "v631_f1 rc=$?" >> "$EV/lo_resumen.txt"
cd "$R/personaje_v2"
( time flock $L python3 -B "$IM/prueba_pipeline_f1.py" ) > "$EV/prueba_pipeline_f1.txt" 2>&1; echo "pipeline_f1 rc=$?" >> "$EV/lo_resumen.txt"
cd "$R"
( time flock $L python3 -B v6/v631_f1/scripts/prueba_pipeline_v631.py ) > "$EV/prueba_pipeline_v631.txt" 2>&1; echo "pipeline_v631 rc=$?" >> "$EV/lo_resumen.txt"
echo FIN >> "$EV/lo_resumen.txt"
