# CONTRASTE_D3_3934bc9_5f4b2a2 · revisión del coordinador que emite CORRECCION_D3 (bloques 1 y 2 de Mistral D)

- **Revisión contrastada:** `coordinacion/cierre_v2/revisiones_coordinador/D2_3934bc9_5f4b2a2/` @ `30c314c`: `REVISION_D2_3934bc9_a_5f4b2a2.md`, `CORRECCION_D3.md`, `sondas/`.
- **Objeto:** rama `mistral/d-qwen-aceptacion` @ `3934bc9` (bloque 1) y `5f4b2a2` (bloque 2); banco `4745f38`.
- **Veredicto del contraste: CONFORME.** Todos los hallazgos materiales se reproducen con las sondas publicadas; la declaración de 0/36 casos del personaje es correcta; CONTROL registra la revisión. Sin discrepancias en la revisión; una nota estructural sobre el control (abajo).

## Sondas propias (reproducción)

Copias con `git archive` de `3934bc9` → `entrega`, `5f4b2a2` → `entrega2`, `4745f38` → `banco`:

| Comprobación | Resultado mío | Informe |
|---|---|---|
| `sha256sum -c MANIFIESTO_SHA256.txt` en `entrega/resultados_qwen/ejecucion_d` | exit 1; **4 FAILED** (RESUMEN, `scripts/ejecutar_caso.py`, `scripts/lib_arnes.py`, `scripts/preparar_entorno.sh`) | 4 fallos |
| ídem en `entrega2/…` | exit 1; **11 FAILED** (RESUMEN, `adaptaciones.json`, 3 especificaciones, 6 scripts) | 11 fallos |
| archivo fuera del manifiesto en `entrega2` (`comm` manifiesto vs disco) | **`scripts/generar_correspondencia.py`** existe en disco y no está en el manifiesto | «1 sin registrar» |
| `sha256sum -c` del banco `4745f38` | exit 0; **57/57 OK** | 57/57 |
| `python3 -I sondas_arnes_d2.py entrega/… entrega2/… banco/… out.json` | exit 0; diff profundo con `sondas_arnes_d2.json` publicado: **idéntico salvo** `R7c.candidata_sha/esperado` (hash del repo stub, dependiente del temporal; en mi ejecución ambos campos son iguales entre sí, como en la publicada) y la ruta temporal en `P9w.stderr_ultima`. Todos los veredictos de sondas (P1, P1v/P2v, P2, P3, P3va, P3vb, P4, P4v, P4w, P5, P5v, P5w, P7b, P7c, P7v, P8, P8va, P8vb, P9, P9v, P9w, R2, R7a, R7c, regeneración) coinciden | 25 sondas |
| `bash sondas/comprobaciones_d2.sh <repo> <dir>` | exit 0; log **idéntico** al publicado tras normalizar `<repo>`/`<rev_D2>` | idéntico |
| Regeneración sobre evidencia publicada (salida de mi ejecución) | `matriz_regenerada_estados` = {ERROR (COMPONENTE_OK): **29**, BLOQUEO_ENTORNO: **1**, NO_EJECUTADO: **6**} → **0 CUMPLE** | 29/1/6/0 |
| MATRIZ publicada en `entrega2` (`MATRIZ_EJECUCION.csv`) | 36 filas; `veredicto_componente` = CUMPLE en **30**; `preserva_sentido` = «sí» en **36** | «30 CUMPLE», «sí» 36/36 |
| `ENTREGA.json` | sin cambios desde `1ac661b`; `base_revisada_sha = bdcbba7…` | igual |
| Relevos Q1-028/Q1-032 regenerados | `comando_relevo: null` en ambos | igual |

## Control (CONTROL.json)

- D-HARNESS y D-36: `revision=CORRECCIONES`, `integracion=NO`, `commit_revisado` pertinente; el evento «D2 de Mistral D (3934bc9 y 5f4b2a2) revisado: no cierra D2 (R1–R6 abiertos, R7 con límites); CORRECCION_D3. Manifiesto con 11 fallos… 0/36 casos del personaje, declarado correctamente» está en `registro_eventos` y coincide con lo que reproduje.
- **Nota estructural (no es un hallazgo falso):** a diferencia de T-AUTO, A-CTX, E-ELIS y G-MANUAL, las revisiones de D no tienen entrada `solicitud_revision.informe_revision` en las tareas; quedan registradas solo en `registro_eventos` + `observacion`. El veredicto sí queda reflejado; se echa en falta el enlace formal al informe.
- Nada aceptado: D-HARNESS/D-36 no pasan a aceptado/integrado; 0/36 casos del personaje se declara correctamente.

## Discrepancias

Ninguna en la revisión. La clasificación de D3 (R1–R6 abiertos, R7 cerrado con límites; material) se sostiene con las sondas reproducidas.
