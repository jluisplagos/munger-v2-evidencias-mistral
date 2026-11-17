# Punto de recuperación · Frente A M2 · rama `mistral/m2-cobertura-vm`

Propuesta de evidencia de Mistral; pendiente de revisión e incorporación por el integrador. No APROBADO ni aptitud financiera general.

## Estado actual

- Repositorio auxiliar: `jluisplagos/munger-v2-evidencias-mistral`, origin verificado (`https://github.com/jluisplagos/munger-v2-evidencias-mistral`). Rama `mistral/m2-cobertura-vm` traída de origin y publicada; **no** se trabaja sobre `main` ni sobre `jluisplagos/munger-v2`.
- Escritura exclusively en `resultados_m2/cobertura_vm/`. No se tocan frentes B/C, ni el producto, ni `resultados/` del piloto M1.
- Insumos: `python3 docs/programa_mistral_m2/herramientas/preparar_insumos.py --download` ejecutado; ZIP base-4.14 (1.130.912.246 bytes, sha256 `bb51942c…b7b93e` verificado por la herramienta) y **251 archivos conformes** con huella verificada en `.trabajo/insumos_m2/` (29 PDF candidatos). Selección parcial: `producto_completo_verificado: false`.
- Inventario generado (`scripts/inventario.py` → `INVENTARIO.md`, `resultados/inventario.json`): 677 entradas (Vidrala 347, Viscofan 330), 60 del piloto, 617 nuevas; clases 454 dato_publicado / 13 cero_comprobado / 101 derivado / 6 dato_ausente / 52 hipótesis / 35 convención / 16 no aplicable; concilia con `entrada/configuracion.json` y `entrada/catalogo_entradas.csv`. 21 fuentes referenciadas, todas CONFORME (huella sha256 verificada). Grafo de derivados: 101 nodos, **0 huecos, 0 ciclos**. 22 lotes definidos (L00 piloto de 60; L01–L21 de ≤30 entradas nuevas, agrupadas por documento/página).

## Hecho en este punto

- `scripts/`: `comun.py`, `inventario.py`, `verificar_fuentes.py`, `derivaciones.py`, `construir_cobertura.py`, `revisar_lote.py`, `control_cobertura.py`, `asociacion_pdf.py` (cálculos con `Decimal`, solo lectura sobre insumos).
- Verificación mecánica ejecutada (`verificar_fuentes.py`): 467 entradas con fuente → **467 COINCIDE_PROPUESTO** (archivo conforme + página `[PDF PAGE n]` localizada + cita localizada + valor localizado + transformación `valor_fuente × escala × signo = valor_modelo` + comparación con el libro XLSX en solo lectura / registro oficial para aux). 123 observaciones por página en `OBSERVACIONES.jsonl`.
- Derivados (`derivaciones.py` → `DERIVADOS.json`): 101 nodos (14 reutilizados del piloto, 87 nuevos), recalculados con `Decimal` → **101 COINCIDE_PROPUESTO** (71 exactos, 30 dentro del redondeo a 3 decimales del libro).
- `COBERTURA_677.csv`: 677 filas; estados: 568 COINCIDE_PROPUESTO, 52 HIPOTESIS, 35 CONVENCION, 16 NO_APLICABLE, 6 DATO_AUSENTE; 60 filas con `origen_revision=M1_REUTILIZADA`.
- Control (`control_cobertura.py` → `resultados/control_cobertura.json`): **PASS, 0 violaciones** (sin filas duplicadas/faltantes, sin fuentes inexistentes presentadas como examinadas, sin operandos incoherentes, sin reutilización tras cambio sin recalcular; recuentos conciliados con 677/60/617/101/14/87).

## Lotes publicados

- `L00`: 60 entradas (PILOTO_M1_REUTILIZADA); estados COINCIDE_PROPUESTO=57, DATO_AUSENTE=1, HIPOTESIS=2; archivo `resultados/lotes/lote_L00.json`
- `L01`: 30 entradas (NUEVO); estados COINCIDE_PROPUESTO=6, CONVENCION=12, HIPOTESIS=9, NO_APLICABLE=3; archivo `resultados/lotes/lote_L01.json`
- `L02`: 30 entradas (NUEVO); estados COINCIDE_PROPUESTO=27, CONVENCION=1, NO_APLICABLE=2; archivo `resultados/lotes/lote_L02.json`
- `L03`: 30 entradas (NUEVO); estados COINCIDE_PROPUESTO=17, CONVENCION=4, HIPOTESIS=9; archivo `resultados/lotes/lote_L03.json`
- `L04`: 30 entradas (NUEVO); estados COINCIDE_PROPUESTO=23, HIPOTESIS=7; archivo `resultados/lotes/lote_L04.json`
- `L05`: 30 entradas (NUEVO); estados COINCIDE_PROPUESTO=30; archivo `resultados/lotes/lote_L05.json`
- `L06`: 30 entradas (NUEVO); estados COINCIDE_PROPUESTO=30; archivo `resultados/lotes/lote_L06.json`
- `L07`: 30 entradas (NUEVO); estados COINCIDE_PROPUESTO=30; archivo `resultados/lotes/lote_L07.json`
- `L08`: 30 entradas (NUEVO); estados COINCIDE_PROPUESTO=30; archivo `resultados/lotes/lote_L08.json`
- `L09`: 30 entradas (NUEVO); estados COINCIDE_PROPUESTO=30; archivo `resultados/lotes/lote_L09.json`
- `L10`: 30 entradas (NUEVO); estados COINCIDE_PROPUESTO=29, DATO_AUSENTE=1; archivo `resultados/lotes/lote_L10.json`
- `L11`: 30 entradas (NUEVO); estados COINCIDE_PROPUESTO=20, CONVENCION=5, DATO_AUSENTE=2, HIPOTESIS=3; archivo `resultados/lotes/lote_L11.json`
- `L12`: 30 entradas (NUEVO); estados COINCIDE_PROPUESTO=4, CONVENCION=11, HIPOTESIS=5, NO_APLICABLE=10; archivo `resultados/lotes/lote_L12.json`
- `L13`: 30 entradas (NUEVO); estados COINCIDE_PROPUESTO=27, DATO_AUSENTE=2, NO_APLICABLE=1; archivo `resultados/lotes/lote_L13.json`
- `L14`: 30 entradas (NUEVO); estados COINCIDE_PROPUESTO=11, CONVENCION=2, HIPOTESIS=17; archivo `resultados/lotes/lote_L14.json`
- `L15`: 30 entradas (NUEVO); estados COINCIDE_PROPUESTO=30; archivo `resultados/lotes/lote_L15.json`
- `L16`: 30 entradas (NUEVO); estados COINCIDE_PROPUESTO=30; archivo `resultados/lotes/lote_L16.json`
- `L17`: 30 entradas (NUEVO); estados COINCIDE_PROPUESTO=30; archivo `resultados/lotes/lote_L17.json`
- `L18`: 30 entradas (NUEVO); estados COINCIDE_PROPUESTO=30; archivo `resultados/lotes/lote_L18.json`
- `L19`: 30 entradas (NUEVO); estados COINCIDE_PROPUESTO=30; archivo `resultados/lotes/lote_L19.json`
- `L20`: 30 entradas (NUEVO); estados COINCIDE_PROPUESTO=30; archivo `resultados/lotes/lote_L20.json`
- `L21`: 17 entradas (NUEVO); estados COINCIDE_PROPUESTO=17; archivo `resultados/lotes/lote_L21.json`

## Lotes publicados (revision externa A / correccion de contexto)

- `L00` (revision A): 60 entradas; mecanico [COINCIDE_PROPUESTO=57, DATO_AUSENTE=1, HIPOTESIS=2]; contextual [REUTILIZADO_M1=60]; `resultados/lotes/lote_L00.json`
- `L01` (revision A): 30 entradas; mecanico [COINCIDE_PROPUESTO=6, CONVENCION=12, HIPOTESIS=9, NO_APLICABLE=3]; contextual [NO_APLICA=24, REVISADO_CONTEXTUAL=6]; `resultados/lotes/lote_L01.json`
- `L02` (revision A): 30 entradas; mecanico [COINCIDE_PROPUESTO=27, CONVENCION=1, NO_APLICABLE=2]; contextual [NO_APLICA=3, PENDIENTE_CONTEXTUAL=1, REVISADO_CONTEXTUAL=26]; `resultados/lotes/lote_L02.json`
- `L03` (revision A): 30 entradas; mecanico [COINCIDE_PROPUESTO=17, CONVENCION=4, HIPOTESIS=9]; contextual [NO_APLICA=13, REVISADO_CONTEXTUAL=17]; `resultados/lotes/lote_L03.json`
- `L04` (revision A): 30 entradas; mecanico [COINCIDE_PROPUESTO=23, HIPOTESIS=7]; contextual [NO_APLICA=7, REVISADO_CONTEXTUAL=23]; `resultados/lotes/lote_L04.json`
- `L05` (revision A): 30 entradas; mecanico [COINCIDE_PROPUESTO=30]; contextual [REVISADO_CONTEXTUAL=30]; `resultados/lotes/lote_L05.json`
- `L06` (revision A): 30 entradas; mecanico [COINCIDE_PROPUESTO=30]; contextual [PENDIENTE_CONTEXTUAL=1, REVISADO_CONTEXTUAL=29]; `resultados/lotes/lote_L06.json`
- `L07` (revision A): 30 entradas; mecanico [COINCIDE_PROPUESTO=30]; contextual [REVISADO_CONTEXTUAL=30]; `resultados/lotes/lote_L07.json`
- `L08` (revision A): 30 entradas; mecanico [COINCIDE_PROPUESTO=30]; contextual [REVISADO_CONTEXTUAL=30]; `resultados/lotes/lote_L08.json`
- `L09` (revision A): 30 entradas; mecanico [COINCIDE_PROPUESTO=30]; contextual [REVISADO_CONTEXTUAL=30]; `resultados/lotes/lote_L09.json`
- `L10` (revision A): 30 entradas; mecanico [COINCIDE_PROPUESTO=29, DATO_AUSENTE=1]; contextual [NO_APLICA=1, REVISADO_CONTEXTUAL=29]; `resultados/lotes/lote_L10.json`
- `L11` (revision A): 30 entradas; mecanico [COINCIDE_PROPUESTO=20, CONVENCION=5, DATO_AUSENTE=2, HIPOTESIS=3]; contextual [NO_APLICA=10, REVISADO_CONTEXTUAL=20]; `resultados/lotes/lote_L11.json`
- `L12` (revision A): 30 entradas; mecanico [COINCIDE_PROPUESTO=4, CONVENCION=11, HIPOTESIS=5, NO_APLICABLE=10]; contextual [NO_APLICA=26, REVISADO_CONTEXTUAL=4]; `resultados/lotes/lote_L12.json`
- `L13` (revision A): 30 entradas; mecanico [COINCIDE_PROPUESTO=27, DATO_AUSENTE=2, NO_APLICABLE=1]; contextual [NO_APLICA=3, REVISADO_CONTEXTUAL=27]; `resultados/lotes/lote_L13.json`
- `L14` (revision A): 30 entradas; mecanico [COINCIDE_PROPUESTO=11, CONVENCION=2, HIPOTESIS=17]; contextual [NO_APLICA=19, REVISADO_CONTEXTUAL=11]; `resultados/lotes/lote_L14.json`
- `L15` (revision A): 30 entradas; mecanico [COINCIDE_PROPUESTO=30]; contextual [REVISADO_CONTEXTUAL=30]; `resultados/lotes/lote_L15.json`
- `L16` (revision A): 30 entradas; mecanico [COINCIDE_PROPUESTO=30]; contextual [REVISADO_CONTEXTUAL=30]; `resultados/lotes/lote_L16.json`
- `L17` (revision A): 30 entradas; mecanico [COINCIDE_PROPUESTO=30]; contextual [REVISADO_CONTEXTUAL=30]; `resultados/lotes/lote_L17.json`
- `L18` (revision A): 30 entradas; mecanico [COINCIDE_PROPUESTO=30]; contextual [REVISADO_CONTEXTUAL=30]; `resultados/lotes/lote_L18.json`
- `L19` (revision A): 30 entradas; mecanico [COINCIDE_PROPUESTO=30]; contextual [REVISADO_CONTEXTUAL=30]; `resultados/lotes/lote_L19.json`
- `L20` (revision A): 30 entradas; mecanico [COINCIDE_PROPUESTO=30]; contextual [REVISADO_CONTEXTUAL=30]; `resultados/lotes/lote_L20.json`
- `L21` (revision A): 17 entradas; mecanico [COINCIDE_PROPUESTO=17]; contextual [REVISADO_CONTEXTUAL=17]; `resultados/lotes/lote_L21.json`

## Entrega final (universo completo)

- Lotes L00–L21 publicados con commit+push tras cada lote (ver sección anterior); asociación texto↔PDF ejecutada (`resultados/asociacion_pdf_texto.json`: 21 textos, 426 valores en muestra, 100% en página alineada, offset 0).
- Entregables completos en esta carpeta: `COBERTURA_677.csv` (677 filas), `OBSERVACIONES.jsonl` (123), `DERIVADOS.json` (101 nodos: 14 piloto / 87 nuevos), `scripts/` (8 scripts), `resultados/` (inventario, verificación, lotes, asociación, recuentos, control), `INVENTARIO.md`, `HALLAZGOS.md`, `MAPA_REGENERACION.md`, `RESUMEN_PARA_CLAUDE.md`, `MANIFIESTO_SHA256.txt` (45 archivos con huella), este archivo.
- Control final: `python3 resultados_m2/cobertura_vm/scripts/control_cobertura.py` → **PASS, 0 violaciones** (`resultados/control_cobertura.json`); recuentos: 677 = 568 COINCIDE_PROPUESTO + 52 HIPOTESIS + 35 CONVENCION + 16 NO_APLICABLE + 6 DATO_AUSENTE; 60 M1_REUTILIZADA / 617 M2_NUEVA; derivados 101 = 14 + 87.

## Corrección de la revisión externa (A1) — completada

- `git fetch origin revision/chatgpt-m2-20261116`; leídos con `git show 9366bdd…`: `REVISION_CHATGPT_M2.md`, `SONDA_A_SEMANTICA.json`, `CORRECCION_A.md` (rama propia confirmada: `mistral/m2-cobertura-vm`).
- Ejecutado: `verificar_contexto.py` (677 entradas; 509 REVISADO_CONTEXTUAL / 60 REUTILIZADO_M1 / 2 PENDIENTE / 106 NO_APLICA / 0 CONFLICTO), `derivaciones.py` (límites propagados a 101 nodos), `construir_cobertura.py` (columnas `estado_mecanico` + `estado_contextual`), `control_negativo.py` (154 mutaciones: 108 detectadas por contextual, 0 por mecánico), `control_cobertura.py` PASS 0 violaciones, `revisar_lote.py L00..L21` con commit+push por lote, `RESPUESTA_REVISION_EXTERNA.md`.
- Pendientes contextuales declarados: `Vidrala Historia!G22`/`G23` (fila de continuación ambigua, CF_2019 p.19); unidad no decidible en 8 páginas de nota; perímetro no decidible en 51 páginas; columna no decidible en 3 filas no tabulares.

## Seguimiento externo 63e366b (apartado A) — ejecutado

- Leídos con `git show 63e366b:...` (rama `revision/chatgpt-seguimiento-20261116`, sin fusionar): PROMPTS.md («Mistral A») y SEGUIMIENTO.md apartado A. Base `54c8ddc` = HEAD remoto confirmado.
- verificar_contexto.py v2: REVISADO_CONTEXTUAL exige todas las dimensiones OK/NO_APLICA (fuentes 423→264; totales 315 REVISADO / 196 PENDIENTE / 60 REUTILIZADO_M1 / 106 NO_APLICA / 0 CONFLICTO); unidad exige escala explícita (sonda euros/miles del revisor → CONFLICTO); versión con año del informe en página/cabecera (467 OK); reexpresión contrastada con el texto original del año comparativo (238 OK / 158 no decidible / 71 no aplica); signo de ceros y perímetro «no aplica» como NO_APLICA.
- Negativos: 198 mutaciones → 151 detectadas por contextual (sonda euros/miles 1/1; versión 40/40; reexpresión 3/3; columna 33/40; perímetro 38/40; partida 32/40; unidad 4/34), 40 por mecánico (solo versión). `control_cobertura.py` PASS 0 violaciones.
- Propagado a 101 derivados (51 REVISADO / 36 PENDIENTE / 14 REUTILIZADO_M1) y al mapa de regeneración. Respuesta numerada en `RESPUESTA_SEGUIMIENTO_20261116.md`.

## Revisión externa d375d80 (apartado A, A-R1–R3) — ejecutado

- Leídos con `git fetch origin revision/chatgpt-a-d-20261116` + `git show d375d80a5df19a661f80bab9cbdd42b39a28742b:...` (sin fusionar): `REVISION_A_D.md` apartados A, `CORRECCION_A.md`, `A_REPRODUCCION.json`, `SONDAS.json`, `sondas_revision.py`. Base `0224b71` = HEAD remoto confirmado.
- verificar_contexto.py v3: `columna_year` (año de columna ≠ año del informe), columna por posición, reexpresión misma fila/ejercicio/columna/escala/perímetro contra el texto original del año (año 20xx → NO_APLICA; contradicción explícita → CONFLICTO nunca OK), unidad con validación de escala también desde cabecera del documento.
- Regeneración completa con el código definitivo en un pase: fuentes 241 REVISADO / 183 PENDIENTE / 43 REUTILIZADO_M1; derivados 41/46/14; CSV 677 filas **282 REVISADO_CONTEXTUAL / 229 PENDIENTE / 60 REUTILIZADO_M1 / 106 NO_APLICA / 0 CONFLICTO**; mecánicos sin cambio (568/52/35/16/6); `control_cobertura.py` **PASS exit 0** (coherente código=resultados; el revisor obtenía exit 1/21 conflictos sobre `0224b71` por los 20 metadatos de año).
- 5/5 sondas del revisor → CONFLICTO, incrustadas en `control_negativo.py` (`sondas_revisor` en `resultados/control_negativo.json`); negativos: 203 mutaciones, 154 ctx, 40 mec (solo versión).
- Lotes L00–L21 regenerados; `RESPUESTA_A_D_20261116.md` con respuesta numerada, comandos y hashes; `HALLAZGOS.md` §10, `MAPA_REGENERACION.md` tabla v3, `RESUMEN_PARA_CLAUDE.md` actualizados; manifiesto regenerado.
- Pendientes: 183 fuentes PENDIENTE (reexpresión ND 179, perímetro 40, unidad 8, signo 7, columna 4, fila 1 — solapados) y 46 derivados que heredan; 52 HIPOTESIS / 35 CONVENCION / 16 NO_APLICABLE / 6 DATO_AUSENTE sin cambio.

## Programa de cierre v2 · Bloque 1 (cerrar y facilitar revisión) — ejecutado

- Encargo leído con `git show ec707a5ba2bd684381a63ce0f6f6c143aa59f4c0:coordinacion/cierre_v2/PROMPT_MISTRAL_A.md` (+ LEEME/PROGRAMA/INTEGRACION/PLANTILLA_ENTREGA/CONTROL); control remoto consultado también en `ff0c60c` (`coordinacion/cierre-v2`): A-CTX ENTREGADO en `d2419e5`, revisión PENDIENTE (Claude), señal explícita «comprobar importe20xx frente a metadato de año». Rama de revisión `revision/chatgpt-cierre-mistral-01` consultada en solo lectura (afecta a otro frente, no a A).
- **v3.1** (`verificar_contexto.es_metadato_anio`): metadato de año solo por unidad/concepto; importe monetario 2000–2099 ya no pasa a NO_APLICA por parecer año. Caso real: `Viscofan aux:AR2025_p27_pagos_acciones_2024` (2001 miles de euros) → NO_DECIDIBLE en v3.1; motivo corregido (A3-R8): CF_2024 línea 414 imprime 2,001 en la MISMA fila y columna 2024 (Share-based payment 2,001 2,346); el rótulo completo confirma la fila y la reexpresión queda OK por igualdad (no reexpresado). Reexpresión: 199 OK / 180 ND / 88 NA (antes 199/179/89).
- **Sondas bilaterales** (15, todas ok) en `control_negativo.py` §9: columna correcta/equivocada, perímetro consolidado/individual, versión correcta/inexistente, miles en página y en cabecera con escala 0.001 vs euros/escala 1, reexpresión confirmada/igualdad/ambigüedad, importe 2025 monetario (→ OK por camino normal, no NO_APLICA), año real por unidad (→ NO_APLICA). 5/5 sondas del revisor d375d80 en CONFLICTO.
- Pipeline regenerado en un pase con código definitivo: fuentes 241 REVISADO / 183 PENDIENTE / 43 REUTILIZADO_M1; derivados 41/46/14; CSV **282 / 229 / 60 / 106 / 0 CONFLICTO**; mecánicos sin cambio (568/52/35/16/6); `control_cobertura.py` **PASS exit 0**; negativos 218 mutaciones (168 ctx / 40 mec); lotes L00–L21 regenerados.
- **Conciliación**: 677 = 467 con fuente + 101 derivados + 109 sin fuente (52H/35C/16NA/6DA). 229 pendientes = **183 fuentes + 46 derivados** (no 229 fuentes). CSV: 282=241+41; 229=183+46; 60=43+14+3 piloto no-aplica; 106=109−3.
- Publicado `ENTREGA.json` (modelo PLANTILLA_ENTREGA.json), manifiesto regenerado; commit+push en `mistral/m2-cobertura-vm`.

## Programa de cierre v2 · Bloque 2 · pasada sistemática (v3.2/v3.3) — ejecutada

- `scripts/cola_pendientes.py` → `resultados/cola_pendientes.json`: **240 fuentes pendientes en 81 grupos documento/página + 73 derivados**, ordenados por `material_declarada` + derivados materiales dependientes (transitivamente). No es política económica.
- v3.2: perímetro raíz `consolid` (ES+EN) → 40 ND resueltos con evidencia; unidad por nota de escala de la misma tabla (≤8 páginas atrás, control escala==0.001) y metadatos en todo el documento con página citada; signo en bloque de fila (±2 líneas) y NO_APLICA en valores no numéricos.
- v3.3: reexpresión con bloque de continuación (3 líneas) + tokens canónicos; años 20xx fuera de los valores de fila; **differ+no-reexpresado nunca OK** (CONFLICTO solo ante contradicción explícita 'igual al original' sin el valor en el original; NO_DECIDIBLE con motivo en ambigüedad/alcance/diferencia sin declaración); differ+afirmación → OK por columna.
- Resultados coherentes (regeneración en un pase): fuentes **184 REVISADO / 240 PENDIENTE / 43 REUTILIZADO_M1 / 0 CONFLICTO**; CSV **198 / 313 / 60 / 106 / 0** (313 = 240 fuentes + 73 derivados); mecánicos sin cambio; control **PASS exit 0**; bilaterales 15/15 ok; sondas revisor 5/5 CONFLICTO; negativos 218 (169 ctx / 40 mec); lotes L00–L21 regenerados.
- Bloqueos cuantificados (reexpresión ND 250): 36 sin texto del año original (falta el documento del ejercicio; no está en los 251 insumos) · 79 valor en el original pero no en la misma fila/columna 1:1 · 45 fila localizada, columnas no mapeables 1:1 · 44 declara no-reexpresado pero difiere · 40 no-aplica con razón de alcance (falta puente verificado) · 6 partida no localizada. Columna ND 4, fila ND 1, unidad ND 1.
- ENTREGA.json actualizado con hashes (CSV `dd7d3913…edbf`, control `bc648281…e43e`, cola `26535ee5…cfff`).

## Cierre v2 · Bloque 2 · v3.4 (firma y cabecera de tabla en original) — ejecutada

- Comparación de reexpresión con **signo** (paréntesis = negativo, magnitud ES/EN normalizada) y cabecera de tabla del texto original por **línea más próxima con ≥2 años** (modo 'near'; antes se confundía con tablas de proyección de la misma página). Desempate de filas por los números citados en el comparativo.
- Fuentes **294 REVISADO / 130 PENDIENTE / 43 REUTILIZADO_M1 / 0 CONFLICTO**; CSV **337 / 174 / 60 / 106 / 0** (174 = 130 fuentes + 44 derivados); reexpresión 87 OK / 134 ND / 246 NA; control **PASS exit 0**; bilaterales 15/15; sondas revisor 5/5 CONFLICTO; negativos 218 (169 ctx / 40 mec); lotes regenerados. Cola: 130 fuentes en **55 grupos** + 44 derivados (`cola_pendientes.json` sha256 `755e208e…0d39`).
- Grupo top CF_2023 p.7: 5 de 7 pendientes pasan a REVISADO (igualdad confirmada con signo en CF_2022: (117,296), (85,880), (82,341), (84,515), (4,070)); quedan 2 (aux:capex_int_2022 ambigüedad de fila, Historia!I13 columnas no mapeables 1:1).

## Cierre v2 · Bloque 2 · v3.5/v3.6 + registro de resoluciones — ejecutado

- v3.5: `columna_year` ignora años de citas de archivo en la descripción (D13 → REVISADO). v3.6: puente aritmético citado verificado (F7: 177,548 = 165,980 − 1,004 + 6,595 + 5,977, componentes en CF_2019 p.9 → OK).
- Fuentes **296 REVISADO / 128 PENDIENTE / 43 REUTILIZADO_M1 / 0 CONFLICTO**; CSV **339 / 172 / 60 / 106 / 0** (172 = 128 fuentes + 44 derivados); control **PASS exit 0**; bilaterales 15/15; sondas revisor 5/5 CONFLICTO; negativos 218 (169 ctx / 40 mec); lotes L00–L21 regenerados.
- `resolver_bloque2.py` → `resultados/resoluciones_bloque2.json`: 54 grupos documento/página, 128 fuentes + 44 derivados pendientes, cada una con motivo exacto y **qué faltaría**: SIN_ORIGINAL 36 (falta el documento del ejercicio entre los 251 insumos fijados; no amplío insumos), ALCANCE_SIN_PUENTE 49, DECLARA_NO_DIFIERE 18, AMBIGÜEDAD_FILA_COLUMNA 13, NO_MAPEABLE_1:1 6, NO_LOCALIZADA 4, NO_TABULAR 2, CONTINUACIÓN 1, UNIDAD_SIN_FRASE 1.

## Cierre v2 · Bloque 2 · v3.7 (léxico ES/EN) — ejecutado

- SYNONYMS ampliado (arrendamiento/derecho de uso/pasivos/deudas ES↔EN). Grupo top Viscofan CF_2024 p.3: arrend_cp/lp_2023 → REVISADO (igualdad con signo confirmada en CA_2023_es p.3). Fuentes **298 REVISADO / 126 PENDIENTE / 43 REUTILIZADO_M1 / 0 CONFLICTO**; CSV **342 / 169 / 60 / 106 / 0**; control **PASS exit 0**; bilaterales 15/15; sondas revisor 5/5 CONFLICTO; lotes regenerados; registro actualizado (126 fuentes / 54 grupos / 43 derivados).

## Cierre v2 · Bloque 2 · v3.8/v3.9 — ejecutado

- v3.8 léxico financiero ES/EN + umbral de tokens; v3.9 corroboración por fila 1:1 que confirma el valor (con signo) en la columna yc (+62 mejoras, 0 regresiones).
- Fuentes **356 REVISADO / 68 PENDIENTE / 43 REUTILIZADO_M1 / 0 CONFLICTO**; CSV **426 / 85 / 60 / 106 / 0** (85 = 68 fuentes + 17 derivados); control **PASS exit 0**; bilaterales 15/15; sondas revisor 5/5 CONFLICTO; lotes regenerados; registro: 33 grupos restantes, bloqueos SIN_ORIGINAL 36 (falta doc. 2016 entre los 251 insumos fijados), ALCANCE_SIN_PUENTE 11, AMBIGÜEDAD 9, NO_MAPEABLE 5, DECLARA_NO_DIFIERE 4, otros 5.

## Cierre v2 · Bloque 2 · v3.10 — ejecutado

- Metadatos de norma/moneda por palabras en el documento (unidad 467/467 OK); valor no numérico → NO_APLICA en reexpresión. Fuentes **358 REVISADO / 66 PENDIENTE / 43 REUTILIZADO_M1 / 0 CONFLICTO**; CSV **428 / 83 / 60 / 106 / 0** (83 = 66 fuentes + 17 derivados); control **PASS exit 0**; bilaterales 15/15; sondas revisor 5/5 CONFLICTO; lotes regenerados. Registro: 31 grupos restantes; SIN_ORIGINAL 36 confirmado como bloqueo (falta el doc. 2016 entre los 251 insumos fijados).

## Pendiente / siguiente acción exacta

1. **Claude coordinador revisa Bloque 1 y esta pasada sistemática** — no autoaprobación.
2. **Bloque 2 por grupos documentales**: resolver cada grupo de la cola en orden de prioridad examinando página/tabla y texto del año original; registrar cada resolución con evidencia (cita + página + sha256) o el bloqueo preciso (qué faltaría) en `resultados/resoluciones_bloque2.json`; aplicar con `scripts/aplicar_resoluciones.py`, regenerar pipeline completo y publicar commit+push **por bloque documental terminado**. Primer grupo: `Vidrala texto/CF_2023.txt p.7` (7 pendientes, prioridad 762, materiales: aux:capex_int_2022, aux:capex_mat_2022, …).
2. **Bloque 2 del encargo**: cola de las 183 fuentes pendientes + 46 derivados agrupada por documento/página, priorizada por dependencias de entradas materiales del motor; resolver con evidencia o dejar pendiente con motivo preciso; propagar a derivados/mapa/lotes. Termina cuando toda la cola tenga evidencia o bloqueo preciso, no al llegar a cero pendientes.
3. Bloque 3 (cola G-MANUAL) solo si CONTROL.json lo asigna a A tras terminar el bloque A: rama nueva `mistral/g-manual-traspaso`, carpeta `resultados_cierre/manual_traspaso/`.
4. Nada más en este frente: no PR, no fusión, no tocar producto/main/B/C/D/E/F ni M1; escritura solo en `resultados_m2/cobertura_vm/` (y la carpeta del bloque 3 si se asigna). Hallazgos materiales pendientes: 6 DATO_AUSENTE y 52 HIPOTESIS quedan como tales (ver `HALLAZGOS.md`).

## Modelo, herramientas y consumo

- Sesión Vibe Code de Mistral AI, modelo **`mistral-large-4-0`** (único modelo expuesto por la interfaz; no hay selector de esfuerzo). Herramientas: Python 3.12 (stdlib) + openpyxl 3.1.5 + pypdf 7.1.0 instalados en `.trabajo/pylibs` (pip del sandbox), git/gh, sha256. Sin LibreOffice ni pipeline (prohibidos y no ejecutados). XLSX solo lectura.
- Consumo/facturación: **no visible desde la sesión**; no se afirma ningún límite ni tope. No se compraron créditos ni recargas.
- Red: usada solo para GitHub (clon del auxiliar y descarga verificada de la release base-4.14 con la herramienta preparada).

## Commit congelado de esta ronda (d375d80)

- `615b29241bf2e886f1ee344bef3867e894c563ab` en `mistral/m2-cobertura-vm`, publicado en origin (verificado con `git ls-remote`: HEAD local = remoto). Rama de revisión `revision/chatgpt-a-d-20261116` leída solo con `git fetch` + `git show`, sin fusionar. Diff respecto a la base revisada `0224b71` confinado a `resultados_m2/cobertura_vm/` (comprobado con `git diff --name-only 0224b71..HEAD`).

## Correccion A2 (control coordinacion/cierre-v2 @ 8b8c9c1, A2-R1..R5) — v4.0 ejecutada

- Encargo leido con `git fetch origin coordinacion/cierre-v2` + `git show 8b8c9c17481abfa3c5e94e8a7906b4bcc6897715:coordinacion/cierre_v2/revisiones_coordinador/A_2c41d68/{CORRECCION_A2.md,REVISION_A_2c41d68.md}` (sin fusionar). A-CTX = CORRECCIONES sobre 2c41d68; base publicada corregida: `9d676ce`.
- v4.0 en `verificar_contexto.py`: A2-R1 columna posicional estricta; A2-R2 reexpresion reescrita (rotulo completo, sin atajo de cita, no-claim+differ -> CONFLICTO, SOLO_SIGNO aparte); A2-R3 pagina manda sobre cabecera y "thousands" solo euros; A2-R4 YEAR_RE con limites de palabra + cabecera sin importes + version no por importe. `control_cobertura.py` exige propagacion exacta del estado_contextual a los 101 derivados (CONFLICTO se propaga per A2-R2).
- A2-R5: `generar_recuentos_doc.py` -> `resultados/RECUENTOS_VIGENTES.md` + bloque generado en `MAPA_REGENERACION.md`; motivo `aux:AR2025_p27_pagos_acciones_2024` corregido (HALLAZGOS §11: CF_2024 p.9 fila 414 columna 2024 = 2,001, misma fila/columna); `COMANDOS.md`; guard pypdf>=6.0 en `asociacion_pdf.py`.
- Resultados regenerados en un pase: fuentes 148 REVISADO / 183 PENDIENTE / 93 CONFLICTO / 43 REUTIL / 210 NO_APLICA; CSV 677 = **169 REVISADO / 209 PENDIENTE / 133 CONFLICTO / 60 REUTILIZADO_M1 / 106 NO_APLICA**; mecanicos sin cambio; `control_cobertura.py` **PASS 0 violaciones exit 0**; negativos 218 (149 ctx/40 mec), bilaterales 15/15, sondas revisor 5/5 CONFLICTO.
- Cambios de estado vs `9d676ce` generados: `resultados/cambios_estado_a2_v4.json` (230 fuentes / 286 filas CSV; transiciones listadas anterior->nuevo). Ver `RESPUESTA_A2_CIERRE_V2.md`, `HALLAZGOS.md` §15, `ENTREGA.json`, `COMANDOS.md`.
- Pendiente: revision de A-CTX por Claude sobre v4.0; bloque 2 del cierre sigue con su cola (`cola_pendientes.json`); G-MANUAL solo si CONTROL.json lo asigna.

## Relevo 2026-11-17 · CORRECCIÓN A3 (A3-R1…R8 sobre 8b88fab) — ejecutada

- Encargo leído con `git show origin/coordinacion/cierre-v2:coordinacion/cierre_v2/revisiones_coordinador/A2_8b88fab/{CORRECCION_A3.md,REVISION_A2_8b88fab.md}` (control vigente `57b34a60`, sin cambios posteriores sobre `coordinacion/cierre_v2`). G-DOCS atendido antes en bloque separado: informe en `mistral/g-manual-traspaso` (`resultados_cierre/manual_revision/revision_gdocs_c0542b8/`, commit `a0524d9`) — CONFORME CON LÍMITES, no integrado.
- Commits por punto en esta rama: A3-R1 `93a02e0` (signo impreso), A3-R2 `d11ee44` (cabeceras), A3-R3 `74d94f8` (importes con forma de año), A3-R4 `c472595` (reexpresión: sin atajo, rótulo completo, escala/perímetro, polaridad), A3-R5 `2e4eb15` (versión con límites de palabra), A3-R6 `447a977` (MILLONES_RE ampliada), A3-R7 `4f50e6a` (operando derivado desde su nodo + control negativo), A3-R8 (este bloque: textos/huellas generados, -I, pypdf mensaje claro, sondas publicadas).
- Estado final generado (`resultados/RECUENTOS_VIGENTES.md`): CSV **209 REVISADO / 283 PENDIENTE / 19 CONFLICTO / 60 REUTILIZADO_M1 / 106 NO_APLICA** (en 8b88fab: 169/209/133/60/106; los 133 no eran 133 errores económicos). Control PASS exit 0; negativos 219 (140 ctx / 40 mec), bilaterales 15/15, d375d80 5/5 CONFLICTO, A3-R7 ok. Diff vs 8b88fab: `resultados/cambios_estado_a3.json` (142 fuentes / 184 CSV) y por punto `cambios_estado_a3_R1…R7.json`.
- Sondas: informe s02/s03/s07 reproducidas sin defectos (`sondas_a3/out/R8_*_final.*`); sondas nuevas propias `sondas_a3/s11_R1…R7` ok. Sondas del informe publicadas en `sondas_a3/sondas_informe/`.
- Ejecutado realmente: pipeline completo con Python 3.12.15 + openpyxl 3.1.5 + pypdf 7.1.0 (insumos 251/251 desde ZIP base-4.14 sha256 bb51942c…b7b93e); sondas con `python3 -I -B`; pypdf 6.17.0 probado aparte (mensaje claro, exit 1). Sin LibreOffice ni pipeline del producto.
- Modelo: `mistral-large-4-0` (Vibe Code, Mistral AI); consumo no visible.
- Pendiente: revisión del coordinador sobre solo lo afectado (A-CTX abierta; A2-R3 cerrada con límites). No se escribe en CONTROL/ESTADO ni en el producto; T-TRASPASO no se duplica (sigue con su receptor). Siguiente acción exacta: el coordinador registra G-DOCS (rama G, commit remoto) y revisa estos 8 commits; solo entonces decidir integración.
