# Evidencia y reproducción · F1 revisión 3

Dictamen: REVISION_F1_V3.md. Siguiente encargo dirigido: CORRECCION_PARA_CLAUDE.md. Trabajo técnico separado: ENCARGO_C20_CSV.md. Plan de cierre: PLAN_DE_CIERRE.md.

## Versiones

- Autor: `jluisplagos/munger-v2@716cbd6794b7fcde8b3862c9d1e7acdaf516d262`.
- Último cambio sustantivo: fd474d3; comparación de revisión: bb28319→fd474d3.
- Fuentes/libro: seis archivos del ZIP base-4.14, con las huellas de `datos/fuentes.json`. Inventario en seleccion_fuentes.json. La selección local NO es la base materializada completa.
- Revisor anterior: los scripts bajo `revision/scripts_revisor_p1_p4/` conservados en el commit autor proceden de 8fcc7fd; se ejecutan con atribución. Las sondas W1–W3 de esta carpeta son nuevas.

## Ejecución del autor y comparación de resultados

Con FRENTE = `docs/validacion_economica_paralela/frente_E_F1_elis` del worktree fijado, BASE = raíz local de los seis archivos seleccionados, LIBRO = `Elis_v63_evaluada.xlsx` bajo la ruta de datos/fuentes.json y SALIDA = carpeta nueva:

```bash
python3 -I "$FRENTE/scripts/controles_sinteticos_f1.py" --salida "$SALIDA/controles_sinteticos_f1.json"
python3 -I "$FRENTE/scripts/copia_investigacion_f1.py" --cifras "$FRENTE/datos/cifras_fuente.csv" --verificacion "$FRENTE/resultados/verificacion_cifras.json" --libro "$LIBRO" --contraste "$FRENTE/resultados/contraste_f1.json" --raiz "$BASE" --salida "$SALIDA/copia_investigacion_f1.json" --informe "$SALIDA/copia_investigacion_f1.md"
python3 -I "$FRENTE/scripts/contraste_f1.py" --cifras "$FRENTE/datos/cifras_fuente.csv" --verificacion "$FRENTE/resultados/verificacion_cifras.json" --libro "$LIBRO" --caja-no-nula "$FRENTE/resultados/caja_no_nula.json" --salida "$SALIDA/contraste_f1.json" --informe "$SALIDA/contraste_f1.md"
```

En esta revisión los tres comandos terminaron exit 0; las cinco salidas son idénticas byte a byte a las publicadas. REPRODUCCION.json registra huellas y códigos. El contraste consume el resultado de LibreOffice conservado; no se ejecutó recálculo del libro. La batería sintética no ejecuta el producto.

## Recálculo separado y PDF

```bash
python3 -I "$FRENTE/revision/scripts_revisor_p1_p4/recalculo_independiente.py" --cifras "$FRENTE/datos/cifras_fuente.csv" --libro "$LIBRO" --copia-autor "$SALIDA/copia_investigacion_f1.json" --salida "$SALIDA/recalculo_independiente.json" --informe "$SALIDA/recalculo_independiente.txt"
python3 -I "$FRENTE/revision/scripts_revisor_p1_p4/evidencia_pdf.py" --base "$BASE" --fuentes "$FRENTE/datos/fuentes.json" --salida "$SALIDA/evidencia_pdf.json" --informe "$SALIDA/evidencia_pdf.txt"
```

Dependencias disponibles: Python 3.12.14, openpyxl, pdftotext 25.03.0 y pypdf 6.21.4. Ambos comandos terminaron exit 0; sus JSON, informes y logs están adjuntos. Los pasajes son acotados, no una lectura/auditoría nueva de las 752 filas.

## Sondas nuevas

```bash
python3 -B sondas_f1_v3.py --frente "$FRENTE" --libro "$LIBRO" --salida "$SALIDA/SONDAS.json"
```

Importa el motor sintético del autor para los flujos hasta el año 11 y calcula la caja finita con un oráculo de suma descontada separado. Prueba H=5/10/11/12, signo del salto frente al libro y tabla lógica A0. No genera una valoración de Elis, no cambia plantillas y no necesita LibreOffice ni llamadas a modelos de pago.

## Integridad y límites

Antes de reproducir, el manifiesto del frente autor dio 374/374 conforme. El manifiesto de esta carpeta cubre solo esta entrega de revisión. No se ejecutaron los 36 casos Qwen ni C20, no se incorporaron cifras al CSV verificado, no se integró ni adoptó nada. Los encargos están preparados, no enviados.
