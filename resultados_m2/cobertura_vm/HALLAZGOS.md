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
