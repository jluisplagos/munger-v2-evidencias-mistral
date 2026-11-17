#!/usr/bin/env bash
# Revisión E2 de ea641e7 (E-ELIS): reproduce todas las sondas en copias desechables.
# Variables (sustituir por rutas locales):
#   AUX   = clon de jluisplagos/munger-v2-evidencias-mistral (con ea641e7 y f00c5dd tras git fetch)
#   REV   = carpeta de esta revisión (rev_E2)
#   PDF   = $REV/pdf, assets de la Release fuentes-elis-e-20261117 (descargados con la API REST de gh)
#   URD   = URD 2025 de base-4.14 (sha256 04bfd087...)
#   ZIP   = ZIP de la Release base-4.14 (sha256 bb51942c...)
#   LIBS  = PYTHONPATH con PyMuPDF 2.1 (pypdf local: 6.17.0; la entrega fija 7.1.0, no disponible sin red)
set -u
: "${AUX:?}" "${REV:?}" "${URD:?}" "${ZIP:?}" "${LIBS:?}"
PDF=${PDF:-$REV/pdf}
cd "$PDF" && sha256sum -c SHA256SUMS                                   # Release 11/11
# Árboles de referencia
mkdir -p "$REV/arbol" "$REV/f00" "$REV/coord"
git -C "$AUX" archive ea641e7 resultados_cierre/elis_fuentes | tar -x -C "$REV/arbol"
git -C "$AUX" archive f00c5dd resultados_cierre/elis_fuentes | tar -x -C "$REV/f00"
git -C "$AUX" archive origin/coordinacion/cierre-v2 coordinacion/cierre_v2/revisiones_coordinador/E1_23718fb | tar -x -C "$REV/coord"
# Copia desechable para reproducir el pipeline del autor sin red (s01, s03, s04)
R=$REV/repro; rm -rf "$R"; mkdir -p "$R/pdfdir" "$R/raiz/.trabajo"
git -C "$AUX" archive ea641e7 resultados_cierre/elis_fuentes | tar -x -C "$R/raiz"
cp "$PDF"/*.pdf "$R/pdfdir/"; cp "$URD" "$R/pdfdir/urd2025.pdf"; ln -s "$ZIP" "$R/raiz/.trabajo/base414.zip"
( cd "$R/raiz" && export PYTHONPATH=$LIBS PYTHONWARNINGS=ignore S=resultados_cierre/elis_fuentes/scripts
  ELIS_PDF_DIR=$R/pdfdir python3 $S/descargar_fuentes_elis.py; echo rc=$?
  python3 $S/lectura_bloque2.py; echo rc=$?; python3 $S/lectura_bloque2.py; echo rc=$?
  python3 $S/publicar_extractos.py; echo rc=$?
  python3 $S/verificar_segundo_extractor.py; echo rc=$?
  python3 $S/comprobar_clasificacion_m6.py; echo rc=$?
  python3 $S/verificar_base_4_14.py; echo rc=$?
  python3 $S/verificar_preservacion_release.py --dir "$PDF"; echo rc=$? ) > "$REV/sondas/s01_reproduccion.out" 2>&1
python3 -I "$REV/sondas/s02_pypdf617_fallos.py" "$PDF" > "$REV/sondas/s02_pypdf617_fallos.out" 2>/dev/null
# s03: diferencias con lo publicado, enmascarando marcas de tiempo; s04: idempotencia (ver .out)
# s05: manifiesto
( cd "$REV/arbol/resultados_cierre/elis_fuentes" && sha256sum -c --quiet MANIFIESTO_SHA256.txt; echo rc=$? )
# s07/s09: tercer extractor (poppler) sobre las 68 citas y la tabla de p.341/p.342
python3 -I "$REV/sondas/s07_citas_pdftotext.py" "$REV/arbol/resultados_cierre/elis_fuentes/LECTURA_FUENTES.jsonl" "$R/pdfdir" > "$REV/sondas/s07_citas_pdftotext.out"
python3 -I "$REV/sondas/s09_d1_tabla_p341.py" "$URD" > "$REV/sondas/s09_d1_tabla_p341.out"
# s12: negativos D4/D5 y procedencia sintética en modo ELIS_PDF_DIR (ver s12_negativos.out para los comandos exactos)
