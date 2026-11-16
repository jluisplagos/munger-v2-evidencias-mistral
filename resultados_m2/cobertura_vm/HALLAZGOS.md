# Hallazgos · Frente A M2 · cobertura integral (677 entradas)

Propuesta de evidencia de Mistral; pendiente de revisión e incorporación por el integrador. Ningún hallazgo edita el XLSX, el registro oficial, las decisiones ni el producto.

Clasificación usada: [CONFLICTO_FUENTE] [LIMITE_COBERTURA] [HIPOTESIS] [ESTRUCTURA] [VERIFICACION].

## 1. [VERIFICACION] Cobertura mecánica completa sin diferencias numéricas
- 467 entradas con fuente (454 dato_publicado + 13 cero_comprobado): en los bytes conservados (`​.trabajo/insumos_m2`, 251 archivos con sha256 verificada) se localizaron el 100% de las páginas declaradas (`[PDF PAGE n]`), el 100% de las citas literales y el 100% de los valores numéricos; la transformación `valor_modelo = valor_fuente × escala × signo` cuadra en las 467 con `Decimal`, y la comparación con el libro (XLSX `*_v63_evaluada.xlsx` en solo lectura para celdas `Hoja!Celda`; `verificacion_entradas.json` del expediente para celdas `aux:`) coincide en las 677 entradas (las 24 celdas vacías declaradas están vacías en ambos lados).
- 101 derivados recalculados con `Decimal` desde sus orígenes: 71 exactos y 30 dentro del redondeo a 3 decimales del libro (diferencia ≤ 0,0005 mm); **0 ciclos, 0 huecos, 0 errores de fórmula**. Estado: 101 COINCIDE_PROPUESTO.
- Estados finales propuestos (677): 568 COINCIDE_PROPUESTO, 52 HIPOTESIS, 35 CONVENCION, 16 NO_APLICABLE, 6 DATO_AUSENTE, 0 DIFERENCIA, 0 NO_ACREDITADO. «COINCIDE» no significa suficiente para invertir.
- Control reproducible (`scripts/control_cobertura.py` → `resultados/control_cobertura.json`): **PASS, 0 violaciones** (sin filas duplicadas/faltantes; sin fuentes inexistentes o de huella no conforme presentadas como examinadas; sin operandos incoherentes; sin reutilización tras cambio sin recalcular — hash de entradas vigente; recuentos conciliados con 677/60/617/101/14/87).

## 2. [VERIFICACION] Asociación texto↔PDF por contenido
- Las 21 fuentes de texto referenciadas (11 Vidrala, 10 Viscofan) se asociaron a su PDF candidato conservado (por sha256 declarado en `version` o por año del archivo) con **desplazamiento 0** entre el marcador `[PDF PAGE n]` del .txt y la página física del PDF; en una muestra de ≤60 páginas citadas por grupo, los **426 valores comprobados aparecen en la página PDF alineada (100%)** (`resultados/asociacion_pdf_texto.json`, pypdf). Compartir números no basta: se comprobó página a página en la muestra.
- Límite: la comprobación texto↔PDF es por muestra (≤60 páginas por grupo), no por documento completo.

## 3. [LIMITE_COBERTURA] Selección parcial de insumos
- `.trabajo/insumos_m2` contiene 251 archivos conformes y 29 PDF candidatos, no el producto completo (`producto_completo_verificado: false`). 7 PDF candidatos conservados no tienen asociación declarada a ninguna entrada del registro en este frente: `PDF_M2_06` (BORME 2026-5696), `PDF_M2_07` (CNMV OIR Vidrala), `PDF_M2_08` (1279_en-2016), `PDF_M2_15` (2275 otra información relevante), `PDF_M2_24` (IA_2016), `PDF_M2_26` (IA_2021), `PDF_M2_27` (IA_2023). Siguen disponibles con huella; no se usaron para acreditar entradas.

## 4. [HIPOTESIS] Se conservan como tales (no se convierten en hechos)
- 52 HIPOTESIS (Vidrala: 16 Palancas, 6 Análisis, 5 Configuración V6.4; Viscofan: 17 Palancas, 4 Análisis, 4 Configuración V6.4), 35 CONVENCION, 16 NO_APLICABLE y 6 DATO_AUSENTE se mantienen con su justificación: Vidrala `Análisis!C48` + `aux:intereses_financiacion_2023/2024/2025` (intereses de financiación no publicados como línea propia; ver hallazgo 4 del piloto M1) y Viscofan `Historia!H26`/`I26` (minoritarios).
- Los 13 ceros comprobados conservan su fundamento en `fuente.tratamiento` (p. ej., «la columna imprime «-» (cero)»; NIIF 16 no reexpresa 2018 en Viscofan). Un cero no se acreditó por ausencia de la palabra.
- Piloto M1: las 60 entradas se marcan `origen_revision=M1_REUTILIZADA` (57 COINCIDE_PROPUESTO, 1 DATO_AUSENTE = C48, 2 HIPOTESIS = C49/C50), reutilizando la evidencia corregida (`resultados/lectura_fuentes.jsonl`, `revision_externa/REVISION_CHATGPT_2.md`) sin contarla como investigación nueva. Los 14 derivados del piloto solo se revisarían si cambiara un origen; ningún origen cambió (hash de entradas vigente).

## 5. [CONFLICTO_FUENTE] Avisos heredados del piloto que siguen vigentes
- La versión inglesa de Vidrala invierte el sentido de «Payments from sale of PPE» y del subtotal de circulante (el español prevalece; ver `resultados/HALLAZGOS.md` del piloto, hallazgo 1). En este frente se contrastó sobre los textos conservados; las citas en inglés se localizaron literalmente, pero el signo se tomó del original cuando difiere.
- Viscofan 2024 reexpresado en AR_2025 (acreedores −2.953 frente a −2.639 del CF_2024 original): el libro usa el comparativo reexpresado; documentado como conflicto resuelto, no error (piloto, hallazgo 3).

## 6. [ESTRUCTURA] Observaciones por página reutilizables
- `OBSERVACIONES.jsonl`: 123 observaciones (empresa, archivo, página PDF, documento, sha256, ubicaciones, citas de ejemplo, entradas y estados). La misma tabla se comprueba una sola vez y se reutiliza por las entradas que la citan; el registro antiguo no se usa como prueba de sí mismo.
- `resultados/lotes/lote_L00..L21.json`: revisión por lotes (≤30 entradas; L00 = piloto de 60) con fragmento acotado de la página citada por entrada; no se volcaron documentos enteros.

## 7. [LIMITE_COBERTURA] Lo que esta cobertura no acredita
- La lectura numérica no acredita significado económico: subtotales pueden incluir partidas presentadas en otra línea; importe devengado ≠ pago; mantenimiento ≠ categoría contable. Los estados HIPOTESIS/CONVENCION/DATO_AUSENTE/NO_APLICABLE siguen pendientes de decisión o de fuente.
- No se generó ningún `verificacion_entradas.json` oficial ni se simularon sellos o revisores; no hay PR, fusión ni modificación del producto. La revisión independiente corresponde a otro contexto sobre el commit congelado.

## 8. [RESPUESTA A A1] Coincidencia mecánica ≠ revisión contextual (corrección ejecutada)

La revisión externa (`9366bdd`, `SONDA_A_SEMANTICA.json`) demostró que el control mecánico antiguo devuelve COINCIDE_PROPUESTO aunque se muten periodo/columna/perímetro/concepto. Se añadió verificación contextual (`scripts/verificar_contexto.py`) que lee encabezado, fila, columna (posición del valor), unidad, signo impreso y perímetro desde los bytes conservados:

- Estados contextuales (677): 509 REVISADO_CONTEXTUAL, 60 REUTILIZADO_M1, 2 PENDIENTE_CONTEXTUAL (`Vidrala Historia!G22`/`G23`, fila de continuación ambigua en CF_2019 p.19), 106 NO_APLICA, 0 CONFLICTO. Los estados mecánicos se conservan en columna aparte (`estado_mecanico` vs `estado_contextual`).
- Controles negativos (`resultados/control_negativo.json`): 154 mutaciones en memoria; 108 detectadas por el verificador contextual, **0 por el mecánico** (reproduce el límite de la sonda). Límites del automatismo declarados: unidad no decidible en 8 páginas de nota sin frase de unidad; columna no decidible en 3 filas no tabulares; perímetro no decidible en 51 páginas sin marca; 1 fila de continuación pendiente.
- Los límites de los orígenes se propagan a los 101 derivados (`estado_contextual`, `limites_contextuales`, `coherencia_unidades_origenes` en `DERIVADOS.json`).
- Ver `RESPUESTA_REVISION_EXTERNA.md` para la respuesta numerada completa.

## 9. [SEGUIMIENTO 63e366b] Corrección del sobrealcance contextual, unidad y versión/reexpresión

- Regla v2: REVISADO_CONTEXTUAL exige todas las dimensiones pertinentes OK/NO_APLICA; las fuentes revisadas bajan 423 → 264 (totales 677: 315 REVISADO_CONTEXTUAL, 196 PENDIENTE_CONTEXTUAL, 60 REUTILIZADO_M1, 106 NO_APLICA, 0 CONFLICTO).
- Unidad: fuera la aceptación «menciona euros ⇒ miles»; se exige frase de escala explícita en página o cabecera del documento; la sonda del revisor («Amounts in euros» vs miles declarados) ahora es CONFLICTO (negativo 1/1).
- Versión/reexpresión: versión OK solo con el año del informe en página/cabecera (467/467); reexpresión contrastada con el texto original del año comparativo conservado (238 OK incl. reexpresados confirmados como acreedores 2024 de Viscofan; 158 no decidible; 71 no aplica).
- No aplicable (signo de ceros, perímetro «no aplica», columna corriente) separado de no comprobado (→ PENDIENTE).
- Negativos: 198 mutaciones, 151 detectadas por el contextual (sonda euros/miles 1/1; versión 40/40; reexpresión 3/3; columna 33/40; perímetro 38/40; partida 32/40; unidad 4/34), 40 por el mecánico (solo versión por archivo). Límites del automatismo declarados.
- Ver `RESPUESTA_SEGUIMIENTO_20261116.md`.

## 10. [REVISION A-D d375d80] Coherencia código/resultados, columna por posición, reexpresión misma fila/columna, escala en cabecera (v3)

- **A-R1 coherente**: semántica v3 reconciliada primero y todas las salidas regeneradas con el código definitivo en un pase; los 20 conflictos del revisor eran metadato de año (`Historia!C5..K5`, `Historia!I23`, `Palancas!C48` → derivada `Historia!I22`): en v3 un año 20xx es NO_APLICA en reexpresión (no se reexpresa como importe); `I23`/`Palancas!C48` quedan PENDIENTE (NO_DECIDIBLE) sin conflicto falso. Totales 677: **282 REVISADO_CONTEXTUAL, 229 PENDIENTE_CONTEXTUAL, 60 REUTILIZADO_M1, 106 NO_APLICA, 0 CONFLICTO**; control **PASS exit 0** (el revisor obtenía exit 1 con 21 conflictos al reproducir `0224b71`). Mecánicos sin cambio (568/52/35/16/6).
- **A-R2 columna/reexpresión**: `columna_year` separa año del informe del año de columna; el valor se mapea por posición en la línea de columnas (`check_columna`); `check_reexpresion` compara misma fila/ejercicio/columna (posición)/escala/perímetro contra el texto original del año conservado, y contradicción explícita («no reexpresado» con valor distinto) → CONFLICTO nunca OK. Las **5 sondas del revisor pasan a CONFLICTO 5/5** (estaban 1/5) e van incrustadas en `control_negativo.json` (`sondas_revisor`). Positivos: años → NO_APLICA (89 con columna corriente), 0 conflictos falsos en las 677.
- **A-R3 escala en cabecera**: `check_unidad` valida `escala==0.001` también cuando la unidad viene de la cabecera del documento (sonda `escala_erronea_con_cabecera` → CONFLICTO).
- Dimensiones (467 fuentes): columna 463 OK/4 ND; fila 466/1; perímetro 423 OK/40 ND/4 NA; reexpresión 199 OK/179 ND/89 NA; signo 447/7/13; unidad 459/8; versión 467/467 OK. Derivados: 41 REVISADO / 46 PENDIENTE / 14 REUTILIZADO_M1.
- Negativos: 203 mutaciones, 154 detectadas por el contextual (5/5 sondas del revisor), 40 por el mecánico (solo versión). Límites declarados: unidad 4/34, partida 32/40, columna 33/40, perímetro 37–38/40.
- Ver `RESPUESTA_A_D_20261116.md`.

## 11. [CIERRE V2 · BLOQUE 1] v3.1: importe 2000–2099 ≠ metadato de año; sondas bilaterales; ENTREGA.json

- `es_metadato_anio` (v3.1): año solo por unidad/concepto que lo identifiquen. Caso real corregido: `Viscofan aux:AR2025_p27_pagos_acciones_2024` (2001 **miles de euros**) ya no es NO_APLICA por parecer año → NO_DECIDIBLE (motivo corregido según A2-R5: CF_2024 p.9 imprime 2,001 en la MISMA fila 414 y columna 2024; en v4.0 el rótulo completo confirma la fila y la reexpresión queda OK como «no reexpresado» con igualdad). Reexpresión: 199 OK / 180 ND / 88 NA (antes 199/179/89); totales CSV sin cambio (la fila es piloto M1).
- 15 sondas bilaterales (positivo+negativo) de columna, perímetro, versión/edición, unidad/escala (página y cabecera), reexpresión (confirmada/igualdad/ambigüedad), importe 20xx monetario y año real: **15/15 ok**; 5/5 sondas del revisor d375d80 en CONFLICTO. Negativos: 218 mutaciones, 168 ctx / 40 mec.
- Código y salidas coherentes (regenerados en un pase): CSV 282 REVISADO / 229 PENDIENTE / 60 REUTILIZADO_M1 / 106 NO_APLICA / **0 CONFLICTO**; control **PASS exit 0**. Conciliación: 677 = 467 fuentes + 101 derivados + 109 sin fuente; **229 pendientes = 183 fuentes + 46 derivados**.
- Publicado `ENTREGA.json` según PLANTILLA_ENTREGA.json; control remoto consultado (`coordinacion/cierre-v2` @ ff0c60c): A-CTX revisión pendiente asignada a Claude. Ver `PUNTO_DE_RECUPERACION.md`.

## 12. [CIERRE V2 · BLOQUE 2 sistemática] v3.2/v3.3 + cola de pendientes por documento/página

- Cola (`cola_pendientes.py` → `cola_pendientes.json`): 240 fuentes pendientes en **81 grupos documento/página** + 73 derivados, prioridad = material_declarada + derivados materiales dependientes.
- v3.2: perímetro ES/EN (`consolid`) resuelve 40 ND; unidad por nota de escala de la misma tabla con control de escala y metadatos en documento; signo en bloque de fila ±2 y NO_APLICA en no-numéricos.
- v3.3 reexpresión estricta: bloque de continuación + tokens; años 20xx no son valores; differ+no-reexpresado **nunca OK** (CONFLICTO solo con contradicción explícita; NO_DECIDIBLE con motivo en el resto); differ+afirmación → OK por columna.
- Totales: fuentes 184/240/43, CSV **198 REVISADO / 313 PENDIENTE / 60 REUTILIZADO_M1 / 106 NO_APLICA / 0 CONFLICTO**; control PASS exit 0; bilaterales 15/15; sondas revisor 5/5 CONFLICTO. Bloqueos cuantificados: 36 sin texto del año original · 79 valor en otra fila/columna · 45 columnas no mapeables 1:1 · 44 declara no-reexpresado pero difiere · 40 falta puente de alcance · 6 partida no localizada.

## 13. [CIERRE V2 · BLOQUE 2 · v3.4] Reexpresión con signo y cabecera de tabla correcta en el original

- Comparación con signo (paréntesis=negativo) y `find_header_block(..., 'near')` en el texto original (línea de columnas más próxima con ≥2 años; evita tablas de proyección). Desempate por números citados en el comparativo.
- Fuentes 294 REVISADO / 130 PENDIENTE / 43 REUTILIZADO / 0 CONFLICTO; CSV **337 / 174 / 60 / 106 / 0**; reexpresión 87 OK / 134 ND / 246 NA; control PASS exit 0; sondas 15/15 bilaterales + 5/5 revisor CONFLICTO. Cola: 130 fuentes en 55 grupos + 44 derivados. Ejemplo resuelto: CF_2023 p.7 → 5/7 a REVISADO con igualdad confirmada con signo en CF_2022.

## 14. [CIERRE V2 · BLOQUE 2 · v3.5/v3.6 + registro] Cola clasificada con bloqueos precisos

- v3.5: años de citas de archivo en la descripción no son año de columna. v3.6: puente aritmético citado verificado en el original (F7 → OK: componentes en CF_2019 p.9).
- Fuentes 296 REVISADO / 128 PENDIENTE / 43 REUTILIZADO / 0 CONFLICTO; CSV **339 / 172 / 60 / 106 / 0**; control PASS exit 0. Registro `resoluciones_bloque2.json`: 54 grupos, 128 fuentes + 44 derivados con motivo y qué faltaría (SIN_ORIGINAL 36, ALCANCE_SIN_PUENTE 49, DECLARA_NO_DIFIERE 18, AMBIGÜEDAD 13, NO_MAPEABLE 6, NO_LOCALIZADA 4, NO_TABULAR 2, CONTINUACIÓN 1, UNIDAD 1). Sin forzar recuentos.

## 15. [CORRECCION A2 (coordinacion/cierre-v2 @ 8b8c9c1) · v4.0] A2-R1..R5 sobre 2c41d68/9d676ce

- **A2-R1 columna estrictamente posicional**: `check_columna` mapea por posición en la línea de columnas; OK sin posición, años repetidos en cabecera o valor repetido en fila → NO_DECIDIBLE; valor ausente o posición que mapea a otra columna → CONFLICTO. Sondas 2a–2g verificadas (2a/2b/2e NO_DECIDIBLE; 2c/2d/2g CONFLICTO; 2f OK). Las 32 entradas REVISADO sin mapeo pasan a PENDIENTE (lista en `resultados/cambios_estado_a2_v4.json`).
- **A2-R2 reexpresión reescrita (v4.0)**: sin atajo de cita; fila elegida por rótulo completo; compara misma fila/columna (posición)/escala/perímetro; toda declaración con «no» + diferencia → CONFLICTO; diferencia sin declaración documental → NO_DECIDIBLE; solo-signo en clase aparte (SOLO_SIGNO); afirmación + diferencia → OK. Las 19 entradas comparadas con otra fila y las 44 solo-signo se regeneran (ver diff de estados).
- **A2-R3 escala**: la página manda sobre la cabecera del documento; millones (incl. «millones de euros») = escala contraria; «thousands» solo acredita miles de euros (no miles de acciones). Sondas 4a–4g verificadas.
- **A2-R4 años con límites de palabra**: `YEAR_RE` con `(?<![\d.,])20\d\d(?![\d.,])` (importes 2045,3 / 0,2050 / 2025,4 no son año); `YEAR_FILE_RE` solo en nombres de archivo; la cabecera no se toma de líneas con importes (caso real Viscofan `Análisis!C37` precios 0,2050…); la versión no se acredita por un importe. Sondas 1b–1d verificadas.
- **A2-R5 textos**: recuentos vigentes GENERADOS (`scripts/generar_recuentos_doc.py` → `resultados/RECUENTOS_VIGENTES.md` + bloque generado en `MAPA_REGENERACION.md`); motivo de `aux:AR2025_p27_pagos_acciones_2024` corregido en §11; `COMANDOS.md` creado con comandos exactos y versiones (Python 3.12.15, openpyxl 3.1.5, pypdf 7.1.0); `asociacion_pdf.py` exige pypdf >= 6.0 con mensaje claro.
- **Control actualizado**: `control_cobertura.py` ahora exige que el `estado_contextual` de cada derivado sea exactamente la propagación de sus orígenes (CONFLICTO se propaga, A2-R2); antes rechazaba todo derivado con contexto CONFLICTO. Con v4.0: **PASS, 0 violaciones, exit 0**.
- **Resultados vigentes (generados, ver `resultados/RECUENTOS_VIGENTES.md`)**: fuentes 148 REVISADO / 183 PENDIENTE / 93 CONFLICTO / 43 REUTILIZADO_M1 (+210 NO_APLICA de clase); CSV 677: **169 REVISADO / 209 PENDIENTE / 133 CONFLICTO / 60 REUTILIZADO_M1 / 106 NO_APLICA**; dimensión: columna 273 OK/115 ND/79 CONFL, fila 466/1, perímetro 463/4 NA, reexpresión 51 OK/144 ND/248 NA/24 CONFL, signo 448 OK/19 NA, unidad 467/467 OK, versión 467/467 OK; mecánicos sin cambio (568/52/35/16/6); negativos 218 (149 ctx / 40 mec), bilaterales 15/15 ok, sondas revisor d375d80 5/5 CONFLICTO.
- **Cambios de estado vs `9d676ce`**: 230 fuentes y 286 filas CSV cambian (REVISADO→CONFLICTO 77 fuentes/110 CSV; REVISADO→PENDIENTE 135/151; PENDIENTE→CONFLICTO 16/23; PENDIENTE→REVISADO 2/2) — lista completa anterior→nuevo en `resultados/cambios_estado_a2_v4.json` (generada por `scripts/generar_cambios_estado.py`). Ninguna cifra ni fuente sustituida; las entradas que pierden acreditación quedan PENDIENTE y las contradicciones documentadas CONFLICTO.
- Ver `RESPUESTA_A2_CIERRE_V2.md`, `COMANDOS.md`, `ENTREGA.json`, `PUNTO_DE_RECUPERACION.md`.
