# Guía histórica frente a los hitos 1 y 2 de la 4.15 · candidata `integracion/candidata-cierre-v2` @ 957af65 · BORRADOR

**Qué es.** Acompaña a `MANUAL_OPERATIVO_957af65.md`. Compara la guía histórica del recorrido supervisado (`PV2/GUIA_RECORRIDO_SUPERVISADO.md`, escrita para las entregas 4.13 y 4.14) y otros textos de continuidad con lo que cambiaron los hitos 1 y 2 de la 4.15. El hito 2 declara que «las guías del pipeline de la 4.14 no se han reescrito» (`E415/hito2/HITO_2_4_15.md:199-200`).

**Cómo se ha hecho.** Solo con lectura de archivos; no se ha ejecutado nada. Las abreviaturas de rutas son las del manual:

| Abreviatura | Ruta |
|---|---|
| `PV2/` | `munger_v2_r1/personaje_v2/` |
| `E414/` | `…/empresas_v2_correcciones/2026-11_Vidrala_ensayo_4_14/` |
| `E415/` | `…/empresas_v2_correcciones/2026-11_Vidrala_ensayo_4_15/` |
| `EVID/` | repositorio de evidencias de la coordinación, commit `9871f59` |

**Regla que se aplica.** Los límites I19 e I20 están corregidos y no se reintroducen: el relevo caducado (`PV2/pruebas/test_relevo_i19_415.py`, 5/5) y la aptitud por entradas en V6.3. Lo único que sigue abierto de I19 es **H9**: el relevo vuelve siempre al paso 12. Está **pendiente de verificar por cambio afectado** (`EVID/coordinacion/cierre_v2/PROGRAMA.md:40`).

---

## 1. Qué cambió en los hitos 1 y 2 y afecta a la operación

| Hito | Cambio | Efecto operativo | Fuente |
|---|---|---|---|
| 1 | R1: `pagina` es la página del PDF (entero); folio aparte; página inexistente = discrepancia | El extractor registra la página del PDF, no el folio impreso | `E415/HITO_1_4_15.md:16-22` |
| 1 | R2: fuente local con existencia y sha256 vigente; lectura externa no cuenta como comprobada | Sin huella o sin el archivo, la entrada queda pendiente | `E415/HITO_1_4_15.md:24-28` |
| 1 | R3: cifras numéricamente equivalentes, sin redondeo; redondeo declarado solo en importes | Una cita redondeada ya no acredita la cifra | `E415/HITO_1_4_15.md:30-40` |
| 1 | I13: vínculo con huella en cada comprobación; `sellar` lo hace solo el revisor, con la fecha de hoy | Sin vínculo, pendiente; si cambia lo vinculado, desactualizada | `E415/HITO_1_4_15.md:42-63`; `PV2/scripts/verificacion_entradas.py:83-84` |
| 1 | I8/I9: el universo incluye las cifras de juicio (`ambito = "juicio"`); recuentos separados | El registro cubre más entradas que en la 4.14 | `munger_v2_r1/CONTINUIDAD.md:15` |
| 1 | C48: entrada efectiva con su cálculo; modo «estricta» por defecto en los expedientes nuevos (`entrada_efectiva.json`); `rellenar_fase1_v63.py --estricta` se detiene con código 7 | Un expediente nuevo puede detenerse en el paso 2 | `E415/HITO_1_4_15.md:140-153`; `munger_v2_r1/CONTINUIDAD.md:16` |
| 1 | Consecuencia: los registros de los tres expedientes finales de la 4.14 pasan a «no apto por entradas» | El control de la 4.14 ya no da 35/35 (32/35 desde un ZIP; 29/35 en un clon Git) | `E415/HITO_1_4_15.md:203-211`; `munger_v2_r1/CONTINUIDAD.md:131` |
| 2 | R415-SIGNO: `valor_fuente` es la cifra publicada con su signo, leída en la línea de la página; un signo −1 exige `tratamiento` | El extractor declara el signo publicado y la transformación | `E415/hito2/HITO_2_4_15.md:29-43` |
| 2 | U1–U7: empates del redondeo, coste de las fórmulas, sensibilidad, derivados listados, HTML visible, modo de la entrada efectiva en cerrado, unidades | Más entradas pendientes por prudencia; el modo ilegible detiene el paso 2 | `E415/hito2/HITO_2_4_15.md:56-78` |
| 2 | **I20:** `verificacion_entradas` en la ficha y el informe de **todas** las plantillas, también V6.3; `entrada_efectiva.json` es material auditado | La aptitud por entradas se lee también en la ficha V6.3 | `E415/hito2/HITO_2_4_15.md:82-88`; `PV2/scripts/ficha.py:383-391` |
| 2 | **I19:** mientras espera, el paso 13 detecta el relevo caducado, lo registra en `relevos_caducados`, repite el paso 12 y pide la auditoría del material vigente | Basta relanzar el mismo comando **sin `--desde`** | `E415/hito2/HITO_2_4_15.md:89-92`; `PV2/scripts/pipeline.py:1060-1083`; `munger_v2_r1/CONTINUIDAD.md:147` |
| 2 | **Límite H9** (abierto): el relevo vuelve siempre al paso 12, aunque cambien salidas de fases anteriores | Pendiente de verificar por cambio afectado; propuesta sin aplicar | `E415/hito2/HITO_2_4_15.md:92-93`; `E415/hito2/PUNTO_DE_RECUPERACION.md:33-34`; `EVID/coordinacion/cierre_v2/PROGRAMA.md:40` |
| 2 | Batería nueva obligatoria `test_relevo_i19_415.py` (5, LibreOffice); entradas 4.15: 190; entrada efectiva: 62 | Quince baterías obligatorias en «completa» | `munger_v2_r1/verificar_paquete.sh:21-25`; `munger_v2_r1/CONTINUIDAD.md:130` |
| 2 | Arranque desde el repositorio, no desde un ZIP adjunto | Clon de `main`, `base_414.py` solo en la base 4.14, manifiesto propio en la 4.15 | `munger_v2_r1/PROMPT_NUEVA_VENTANA.md:3`, `munger_v2_r1/PROMPT_NUEVA_VENTANA.md:15-22` |

## 2. Textos de la guía histórica que hoy ya no son ciertos

| # | Texto histórico (fuente) | Qué dice | Qué es cierto en 957af65 (fuente) | Tipo |
|---|---|---|---|---|
| G-1 | `PV2/GUIA_RECORRIDO_SUPERVISADO.md:114` | «Relevo caducado … el pipeline no vuelve a fijar el material mientras espera (INCIDENCIAS I19). Se usa `--desde 12`, que emite una solicitud nueva.» | El paso 13 lo detecta al relanzar **sin `--desde`**: registra `relevos_caducados`, repite el paso 12 y pide la auditoría del material vigente; la solicitud antigua queda «sustituida» (`E415/hito2/HITO_2_4_15.md:89-92`; `munger_v2_r1/CONTINUIDAD.md:147`; `PV2/pruebas/test_relevo_i19_415.py:33-37`). Queda abierto H9: la vuelta es siempre al paso 12 (`E415/hito2/HITO_2_4_15.md:92-93`) | **No es cierto** (I19 corregido) |
| G-2 | `PV2/GUIA_RECORRIDO_SUPERVISADO.md:98` | «Con la V6.3 (motor A) no lo dicen [«apta por entradas»]: el resultado está en `estado_pipeline.json → verificacion_entradas` … (INCIDENCIAS I20).» | La ficha y el informe de todas las plantillas, también V6.3, llevan `verificacion_entradas` con `apto_para_dinero_real: false` y el modo de la entrada efectiva. No aparece en las salidas históricas sin registro ni modo (`E415/hito2/HITO_2_4_15.md:82-87`; `PV2/scripts/ficha.py:383-391`) | **No es cierto** (I20 corregido) |
| G-3 | `PV2/GUIA_RECORRIDO_SUPERVISADO.md:96` | «Un revisor distinto rellena `comprobacion` en cada entrada: revisor, resultado, fuente examinada y nota.» | Rellenarla no basta. La comprobación necesita un vínculo con huella que escribe `verificacion_entradas.py sellar … --revisor NOMBRE --fecha <hoy> CELDA…`; sin vínculo queda pendiente, y si cambia lo vinculado, desactualizada (`E415/HITO_1_4_15.md:42-61`; `PV2/scripts/verificacion_entradas.py:84`) | Incompleto: hoy induce a error |
| G-4 | `PV2/GUIA_RECORRIDO_SUPERVISADO.md:95` | El extractor da «fuente con archivo, página, cita que contenga la cifra, escala y signo». | `pagina` = página del PDF (entero) y `folio` aparte; fuente local con sha256 vigente; cifra equivalente sin redondeo; `valor_fuente` con el signo publicado y `signo`/`escala` como transformación; las cifras de juicio también entran (`E415/HITO_1_4_15.md:19-37`; `E415/hito2/HITO_2_4_15.md:30`, `E415/hito2/HITO_2_4_15.md:42-43`; `munger_v2_r1/CONTINUIDAD.md:15`) | Incompleto |
| G-5 | `PV2/GUIA_RECORRIDO_SUPERVISADO.md:100-103` | El cambio de base: `cambiar_base.py preparar`, `correcciones_fase1_partes` y el guardián de entradas `analisis`. | Además, las entradas `analisis` se declaran con su cálculo, las heredadas se reconocen o descartan (`analisis_que_se_conservan` / `_que_se_descartan`) y el expediente nuevo lleva `entrada_efectiva.json` en «estricta», que puede detener el relleno con código 7 (`E415/HITO_1_4_15.md:141-153`). Por lectura del código, el pipeline termina entonces en `pendiente_de_datos` en el paso 2 (`PV2/scripts/pipeline.py:667-669`) | Incompleto |
| G-6 | `PV2/GUIA_RECORRIDO_SUPERVISADO.md:65` | Aptitud de uso en `ficha.json → aptitud_de_uso`, en el informe §1 y en la columna del resumen V6.4. | Sigue valiendo para V6.4. Desde el hito 2 hay además un bloque `verificacion_entradas` en todas las plantillas, y un modo aplicado distinto del declarado impide «apto por entradas» también en `aptitud_de_uso` (`E415/hito2/HITO_2_4_15.md:82-86`) | Incompleto |
| G-7 | `PV2/GUIA_RECORRIDO_SUPERVISADO.md:1` | Título: «… entregas 4.13 y 4.14». | La guía no se ha puesto al día para la 4.15 (`E415/hito2/HITO_2_4_15.md:199-200`) | Desfasado |
| G-8 | `PV2/GUIA_RECORRIDO_SUPERVISADO.md:14` | «Comprobar el paquete en una descompresión limpia.» | En la 4.15 no hay un ZIP completo. Se clona `main`, se materializa la base 4.14 con `base_414.py`, se pasa a la rama 4.15, se contrasta con su `MANIFIESTO_SHA256.txt` y se verifica en una copia limpia (`README.md:5`; `munger_v2_r1/PROMPT_NUEVA_VENTANA.md:15-22`). La copia de los 1008 binarios a la rama 4.15 **[NO DOCUMENTADO]** como comando (`EVID/coordinacion/cierre_v2/pruebas_candidata/957af65/README.md:8-11`) | Desfasado |
| G-9 | `PV2/GUIA_RECORRIDO_SUPERVISADO.md:36-43` (tabla de códigos) | No menciona la parada del modo «estricta» de la entrada efectiva ni la de un `entrada_efectiva.json` ilegible. | El paso 2 se detiene con un modo ilegible, con errata o distinto del declarado (U6), y con el código 7 del relleno estricto (`E415/hito2/HITO_2_4_15.md:74-76`; `PV2/scripts/pipeline.py:662-669`) | Omisión |

**Textos de la guía que siguen siendo ciertos** y que no hay que retirar:
- `--desde N` cuando cambia una entrada del paso N; por ejemplo, `--desde 12` para el registro de las entradas (`PV2/GUIA_RECORRIDO_SUPERVISADO.md:112`).
- Relanzar `--desde 13` tras corregir un defecto del código que escribe el material provisional (`PV2/GUIA_RECORRIDO_SUPERVISADO.md:60`).
- La copia hermana para los relevos de expedientes anteriores (`PV2/GUIA_RECORRIDO_SUPERVISADO.md:115`).
- La fase C con el mismo agente en los dos turnos (`PV2/GUIA_RECORRIDO_SUPERVISADO.md:48`).
- La auditoría con un agente nuevo (`PV2/GUIA_RECORRIDO_SUPERVISADO.md:60`).

En ninguna fuente consta que el hito 2 los haya cambiado.

## 3. Otros textos de continuidad que hoy ya no son ciertos

| # | Texto (fuente) | Qué dice | Qué es cierto en 957af65 (fuente) |
|---|---|---|---|
| O-1 | `munger_v2_r1/CONTINUIDAD.md:351` | I19: «que el paso 13 vuelva a fijar el material … Toca código: requiere encargo y prueba.» | Corregido en el hito 2, con la batería `test_relevo_i19_415.py` 5/5 (`munger_v2_r1/CONTINUIDAD.md:9`; `EVID/coordinacion/cierre_v2/pruebas_candidata/957af65/verificar_paquete_completa.log:36`). Solo queda H9 |
| O-2 | `munger_v2_r1/CONTINUIDAD.md:352` | I20: «llevar `aptitud_de_uso` a la ficha y al informe V6.3 … requiere encargo.» | Corregido en el hito 2 con el bloque `verificacion_entradas` en todas las plantillas (`E415/hito2/HITO_2_4_15.md:82-88`) |
| O-3 | `munger_v2_r1/CONTINUIDAD.md:191` | «en la V6.3 queda en `estado_pipeline.json` (I20)» | Ver G-2 |
| O-4 | `munger_v2_r1/CONTINUIDAD.md:287` (§8, limitaciones) | «la ficha V6.3 no muestra la aptitud por entradas (I20); un relevo caducado no se avisa (I19)» | Escrito como limitación de la 4.14; en 957af65 ya no es una limitación vigente (`munger_v2_r1/CONTINUIDAD.md:9`) |
| O-5 | `munger_v2_r1/CONTINUIDAD.md:130` y `:132` | «Las doce que siguen a la sintética»; el modo rápido omite «las diez» | Son trece las que solo se ejecutan en «completa», de la vigencia H5 al cierre (`munger_v2_r1/verificar_paquete.sh:85-330`) |
| O-6 | `munger_v2_r1/CONTINUIDAD.md:371` (regla 11.4) | «las diez baterías obligatorias … integración V6.4 (198)» | Quince obligatorias; mínimo de la V6.4, 199 (`munger_v2_r1/CONTINUIDAD.md:130`; `munger_v2_r1/verificar_paquete.sh:209`) |
| O-7 | `munger_v2_r1/CONTINUIDAD.md:194` | `test_integracion_v64.py` (198) | 199 (`munger_v2_r1/verificar_paquete.sh:209`) |
| O-8 | `munger_v2_r1/CONTINUIDAD.md:386-390` (§12) | Adjuntar el ZIP de la 4.14 (o sus partes) y pegar el mensaje | El arranque es desde el repositorio (`munger_v2_r1/PROMPT_NUEVA_VENTANA.md:3`, `munger_v2_r1/PROMPT_NUEVA_VENTANA.md:15-22`) |
| O-9 | `munger_v2_r1/CONTINUIDAD.md:109` (§2.1) | «Descomprimir el ZIP en una carpeta nueva y vacía» | Ver G-8 |
| O-10 | `munger_v2_r1/CONTINUIDAD.md:370` y `:377`; `docs/RECEPCION_ENTREGA_CLAUDE.md:7-9` | Toda entrega es un ZIP completo, producido con `empaquetar_zip.py` | El hito 2 se entregó como rama, con un paquete de cambios no versionado (`E415/hito2/HITO_2_4_15.md:183-187`); el proyecto vive en el repositorio (`munger_v2_r1/PROMPT_NUEVA_VENTANA.md:3`) |
| O-11 | `munger_v2_r1/CONTINUIDAD.md:131` | El LEEME de la 4.14 «sustituye, para este árbol» al de la 4.13 | Ese LEEME describe el árbol 4.14 (`E414/resultados/LEEME_CONTROLES_HISTORICOS_4_14.md:1-3`); el esperado sobre el árbol 4.15 **[NO DOCUMENTADO]** |
| O-12 | `README.md:1-7`; `CLAUDE.md:1` | «Rama de revisión: 4.15, hito 1»; «conserva exactamente el código recibido» | La candidata es la 4.15 · hito 2 (`munger_v2_r1/VERSION:1`), en `integracion/candidata-cierre-v2` (`EVID/coordinacion/cierre_v2/PROGRAMA.md:12`) |
| O-13 | `README.md:17`; `CLAUDE.md:35`; `docs/MIGRATION_STATUS.json:9,12-13` | Las correcciones de Claude «no están incorporadas»; «esperar a que Claude termine» | El hito 2 está en el árbol (`E415/hito2/HITO_2_4_15.md:1-10`) |
| O-14 | `munger_v2_r1/PROMPT_NUEVA_VENTANA.md:19`; `munger_v2_r1/CONTINUIDAD.md:6` | La rama del hito 2 es `claude/hopeful-bardeen-qap6y0` | Es la rama de trabajo del autor; la candidata de integración es `integracion/candidata-cierre-v2` desde `957af65` (`EVID/coordinacion/cierre_v2/PROGRAMA.md:12`) |
| O-15 | `E414/documentacion_cierre_4_14/traspaso/PROMPT_DEL_AGENTE_RECEPTOR.md:31-32` (histórico) | Esperado: integración V6.4 198/198 y control de la 4.14 «todas sus comprobaciones PASAN» | 199/199 y 29/35 sobre un clon Git (`munger_v2_r1/PROMPT_NUEVA_VENTANA.md:23-26`; `munger_v2_r1/CONTINUIDAD.md:131`) |
| O-16 | `PV2/PROMPT_CLAUDE_CODE.md:5` (histórico) | Sesión principal: «Sonnet, esfuerzo medio» | Opus con esfuerzo alto para la coordinación (`CLAUDE.md:28`) |
| O-17 | `PV2/README_v2.md:29` y `PV2/PROMPT_CLAUDE_CODE.md:26` (históricos) | Crear `empresas_v2/<E>/` y ejecutar allí | No se modifica `PV2/empresas_v2/`: se trabaja en un expediente nuevo (`munger_v2_r1/CONTINUIDAD.md:369`; `PV2/GUIA_RECORRIDO_SUPERVISADO.md:16`) |
| O-18 | `PV2/ESTADO.md:11-15` (histórico) | «Cómo retomar» y «Siguiente paso exacto: pieza 5» | Superado: lo dice el propio aviso (`PV2/ESTADO.md:3`) y `munger_v2_r1/CONTINUIDAD.md:361` |

Los documentos O-15 a O-18 llevan su aviso de documento histórico (`munger_v2_r1/CONTINUIDAD.md:360-362`; `PV2/README_v2.md:1`; `PV2/ESTADO.md:3`). Se listan porque un receptor sin historial podría seguirlos.

## 4. H9 / I19: qué sigue pendiente

- **Hecho:** mientras el paso 13 espera, el relevo caducado se detecta y se resuelve con una solicitud nueva del material vigente, sin `--desde`. Así lo exigen las cinco pruebas de `test_relevo_i19_415.py` (`PV2/pruebas/test_relevo_i19_415.py:56-78`).
- **Límite declarado:** la vuelta es siempre al paso 12. Si lo cambiado son salidas de fases anteriores (fase_a/b/c, entrada efectiva), «haría falta volver al paso que las consume». Es una propuesta sin aplicar, porque cambia el recorrido del pipeline y necesita su propia prueba (`E415/hito2/HITO_2_4_15.md:92-93`; `E415/hito2/PUNTO_DE_RECUPERACION.md:33-34`).
- **Programa de cierre:** «H9/I19 (volver siempre a paso12) sigue pendiente de verificar por cambio afectado» (`EVID/coordinacion/cierre_v2/PROGRAMA.md:40`). La tarea T-CAMBIOS pide «ensayar cambio anterior y punto real de reanudación; no reintroducir límites I19/I20 ya corregidos» (`EVID/coordinacion/cierre_v2/CONTROL.json:594`).
- **Consecuencia para la operación:** el manual no presenta la vuelta al paso 12 como suficiente cuando `relevos_caducados[].archivos_cambiados` contiene salidas de fases anteriores. Tampoco presenta `--desde 12` como el procedimiento vigente de un relevo caducado. El procedimiento correcto para ese caso **[NO DOCUMENTADO]**.
