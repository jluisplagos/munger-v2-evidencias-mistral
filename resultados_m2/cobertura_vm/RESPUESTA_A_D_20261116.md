# Respuesta a la revisión externa A·D · Frente A M2 · base revisada `0224b71`

Revisión leída desde `d375d80a5df19a661f80bab9cbdd42b39a28742b` (`revision/chatgpt-a-d-20261116`, carpeta `revision_externa/a_d_20261116/`) con `git fetch` + `git show` (sin fusionar): `REVISION_A_D.md` apartados A, `CORRECCION_A.md`, `A_REPRODUCCION.json`, `SONDAS.json`, `sondas_revision.py`. Rama propia confirmada: `mistral/m2-cobertura-vm` (HEAD remoto = local = `0224b7182dd05d1e396223781d6f5db8b325ce2e` al empezar). Solo se ejecutó el encargo de A (A-R1–R3); no B/C/D.

**Propuesta de evidencia de Mistral; pendiente de revisión e incorporación por el integrador.**

## Respuesta numerada A-R1–R3

### A-R1 · Código y resultados ahora son coherentes (regeneración completa con el código definitivo)

1. Se reconcilió primero la semántica (v3 de `scripts/verificar_contexto.py`) y después **todas** las salidas dependientes se regeneraron con ese código definitivo en un solo pase: `verificar_contexto.py` → `derivaciones.py` → `construir_cobertura.py` → `control_negativo.py` → `control_cobertura.py` → `revisar_lote.py L00..L21`. No se tocaron recuentos a mano.
2. La causa de los 20 CONFLICTO del revisor eran filas de **metadato de año** (`Historia!C5..K5`, `Historia!I23`, `Palancas!C48`, propagadas a la derivada `Historia!I22`): la regla v2 convertía `reexpresado="no aplica"` en conflicto por ser año comparativo. En v3, `check_reexpresion` trata como NO_APLICA cualquier valor que sea un año 20xx (unidad `año` o valor-año): un año de columna no se reexpresa como importe. Verificado sobre las filas del revisor: `Historia!C5`/`K5`/`I5` → reexpresión NO_APLICA («el valor 2016 es un metadato de año…») → REVISADO_CONTEXTUAL; `Historia!I23` y `Palancas!C48` → NO_DECIDIBLE (no hay texto del año original mapeable) → **PENDIENTE_CONTEXTUAL**, nunca CONFLICTO falso; la derivada `Vidrala Historia!I22` → PENDIENTE_CONTEXTUAL con el límite propagado desde `Historia!I23`. **No eran 20 errores financieros demostrados y no se presentan como tales.**
3. Resultado regenerado (código = resultados): CSV 677 filas con estados contextuales **282 REVISADO_CONTEXTUAL / 229 PENDIENTE_CONTEXTUAL / 60 REUTILIZADO_M1 / 106 NO_APLICA / 0 CONFLICTO_CONTEXTUAL**; `control_cobertura.py` → **PASS, 0 violaciones, exit 0** (antes exit 1 con 21 conflictos en la reproducción del revisor). Estados mecánicos sin cambios: 568 COINCIDE_PROPUESTO / 52 HIPOTESIS / 35 CONVENCION / 16 NO_APLICABLE / 6 DATO_AUSENTE; origen 617 M2_NUEVA / 60 M1_REUTILIZADA; derivados 101 (41 REVISADO / 46 PENDIENTE / 14 REUTILIZADO_M1). Universo 677/60/101 conservado.

### A-R2 · Reexpresión y columna ya no acreditan otra columna ni otra fila

4. **Columna**: nueva `columna_year(columna, periodo, archivo)` separa el año del informe (`informe 20xx` en la descripción, o el año del nombre del archivo) del año de la columna (`yc`). `check_columna` mapea el valor por **posición** en la línea de columnas del encabezado (`declared_years={yc}`), no por cualquier año presente en el texto. Sonda del revisor «2024 comparativo del informe 2025 con valor 2025»: ahora **CONFLICTO** («posición 0 → columna 2025 … declarado ['2024']»). Columna: 463 OK / 4 NO_DECIDIBLE (filas no tabulares).
5. **Reexpresión**: `check_reexpresion` v3 compara la **misma fila, mismo ejercicio, misma columna (por posición), misma escala y perímetro** contra el texto conservado del año original (`CF_20xx.txt` etc.): localiza la partida por prefijos de etiqueta (80/60/40/25/12), exige que `yc` figure en el bloque de encabezado de esa fila y que `len(valores)==len(columnas)`, y compara `valor_original` vs `valor` en la posición `columnas.index(yc)`. Igual → OK/NO_APLICA (no reexpresado); distinto → reexpresado, y si el metadato declara «no aplica / no reexpresado / igual al original» → **CONFLICTO (nunca OK)**; no mapeable → NO_DECIDIBLE (→ PENDIENTE). Metadato de año → NO_APLICA. Reexpresión: 199 OK / 179 NO_DECIDIBLE / 89 NO_APLICA (incluye todos los años). Las dos sondas de reexpresión del revisor («toma otra columna», «contradicción devuelve OK») ahora son **CONFLICTO**.
6. **Las 5 sondas del revisor** (`SONDAS.json` → `A_sondas`) se replicaron y quedaron incrustadas en `control_negativo.py` (sección `sondas_revisor`, salida en `resultados/control_negativo.json`): `euros_no_miles` CONFLICTO, `escala_erronea_con_cabecera` CONFLICTO, `columna_equivocada_aceptada` CONFLICTO, `reexpresion_toma_otra_columna` CONFLICTO, `contradiccion_reexpresion_devuelve_ok` CONFLICTO — 5/5 detectadas, frente a 1/5 (solo euros) en la entrega revisada.
7. **Positivos comprobados** (no se introducen conflictos falsos): las filas de metadato de año quedan NO_APLICA (ej. `Historia!I5`: «el valor 2022 es un metadato de año…», antes acreditado como «reexpresado confirmado»); las cifras no reexpresadas de la columna corriente quedan NO_APLICA (89 en total); **0 CONFLICTO_CONTEXTUAL en las 677 filas**; control PASS exit 0.

### A-R3 · Escala validada también desde la cabecera del documento

8. `check_unidad` v3 aplica la misma validación de escala en ambos caminos: si la unidad sale de la **cabecera del documento** (páginas iniciales), se exige `escala == 0.001` para miles (y coherencia euros↔escala 1); si la página declara otra escala explícita («Amounts in euros») con miles declarados → CONFLICTO. La sonda `escala_erronea_con_cabecera` (doc en miles + escala declarada 1) pasa de OK a **CONFLICTO** (ver punto 6). Unidad: 459 OK / 8 NO_DECIDIBLE (páginas sin frase de escala ni en cabecera).

### Conservado íntegramente (conforme)

9. Universo 677 (Vidrala 347 / Viscofan 330), 60 piloto M1 (`REUTILIZADO_M1`), 617 nuevas, 101 derivados (14 piloto + 87 nuevos) recalculados con `Decimal`; estados mecánicos; regla de todas las dimensiones (cualquier NO_DECIDIBLE → PENDIENTE; cualquier CONFLICTO → CONFLICTO); 467/467 fuentes mecánicamente conformes; asociación texto↔PDF (426/426 en muestra); 52 HIPOTESIS / 35 CONVENCION / 16 NO_APLICABLE / 6 DATO_AUSENTE sin tocar; 251 insumos con sha256; piloto M1 sin reabrir.

## Comandos realmente ejecutados (todos `python3 -B`, `PYTHONPATH=.trabajo/pylibs`, desde la raíz del auxiliar)

- `git fetch origin revision/chatgpt-a-d-20261116` y `git show d375d80a5df19a661f80bab9cbdd42b39a28742b:revision_externa/a_d_20261116/{REVISION_A_D.md,CORRECCION_A.md,SONDAS.json,A_REPRODUCCION.json,sondas_revision.py}` (lectura, sin fusionar).
- `python3 -B resultados_m2/cobertura_vm/scripts/verificar_contexto.py` (v3) → `resultados/verificacion_contexto.jsonl` (677 entradas: 241 REVISADO / 183 PENDIENTE / 43 REUTILIZADO_M1 fuentes; dimensiones sobre 467 fuentes: columna 463 OK/4 ND, fila 466/1, perímetro 423/40/4 NA, reexpresión 199/179/89 NA, signo 447/7/13 NA, unidad 459/8, versión 467/467 OK) + `OBSERVACIONES.jsonl`.
- `python3 -B resultados_m2/cobertura_vm/scripts/derivaciones.py` → `DERIVADOS.json` (101 nodos, 0 ciclos/huecos; ctx 41 REVISADO / 46 PENDIENTE / 14 REUTILIZADO_M1).
- `python3 -B resultados_m2/cobertura_vm/scripts/construir_cobertura.py` → `COBERTURA_677.csv` (677 filas; ctx 282/229/60/106/0; mec 568/52/35/16/6; origen 617/60).
- `python3 -B resultados_m2/cobertura_vm/scripts/control_negativo.py` → `resultados/control_negativo.json` (203 mutaciones en memoria: 154 detectadas por el contextual, 40 por el mecánico solo-versión; **5/5 sondas del revisor CONFLICTO** en `sondas_revisor`).
- `python3 -B resultados_m2/cobertura_vm/scripts/control_cobertura.py` → `resultados/control_cobertura.json`: **PASS=true, n_violaciones=0 (exit 0)**; `resultados/recuentos.json`.
- `for L in L00 L01 … L21: python3 -B resultados_m2/cobertura_vm/scripts/revisar_lote.py $L` → `resultados/lotes/lote_L00..L21.json` regenerados.
- `python3 -B resultados_m2/cobertura_vm/scripts/generar_manifiesto.py` → `MANIFIESTO_SHA256.txt` (sin `__pycache__`).

## Hashes SHA256 de las salidas finales (sobre los bytes entregados)

| Salida | SHA256 |
|---|---|
| `COBERTURA_677.csv` | `4a8ce209dcf7c434bd8f83c16d94bf5f247a597f7e69294cefbd7af099f1dda0` |
| `DERIVADOS.json` | `019406b2a3087ebfde865bfd2710263bd513a074e0ddfb95da79b7f7a6237479` |
| `OBSERVACIONES.jsonl` | `44310e303e74c5aedc5c5c3901cd6a2215b6dfebb131d766bc0945c7aebab406` |
| `resultados/verificacion_contexto.jsonl` | `2e77ebc028a430110d003697d17891f1e2fd0580b9122a6d408f1285d10829a7` |
| `resultados/verificacion_fuentes.jsonl` | `9e212cab0c06400eb591e9a1c390fee3735d9db7d28c1b337f85bf4a75bb497` |
| `resultados/control_cobertura.json` (PASS) | `4f0230861b55c76709c0ddbfde0718dc2591cd933a4d09cc78637a00ea313ea3` |
| `resultados/control_negativo.json` (5/5 sondas CONFLICTO) | `737eb3eee55cabdfc5337199a0bf1f2c455da774ee44ff3b0a9ddc3d3de9a529` |
| `resultados/recuentos.json` | `7c29707f6418089f0248b744162e35ac79b6035ae8a23883280ac7dad88380e1` |
| `resultados/asociacion_pdf_texto.json` | `337bf344722463122b3483e57d06fe24a6f35027e50215868fb918652cd4bed4` |
| `resultados/inventario.json` | `8050bf4e3809bfb96b6cd2a72e6cc22deb2b6e2700237e58fef5af79eae7883e` |
| `resultados/lotes/lote_L00.json` / `lote_L21.json` | `88da1a840f4c063a44ccaed18b2fb00831b48f038e4a5c0e9cfde67f4c397083` / `275af0185b93b404ddcd565b37948fd9d67ea3b2276a3c7ff33272ed4ed95323` |

Los hashes de todos los archivos entregados (scripts incluidos) están en `MANIFIESTO_SHA256.txt`.

## Controles negativos y límites pendientes (honestos, no forzados)

- Negativos: 203 mutaciones en memoria; 154 detectadas por el verificador contextual (incluidas las 5 sondas del revisor, 5/5 CONFLICTO), 40 por el mecánico (solo versión, por cambio de archivo). Desglose por dimensión (detección contextual): unidad 4/34 (páginas sin frase de escala), partida 32/40, columna 33/40, perímetro 37–38/40. Son límites del automatismo declarados, no datos de empresa.
- 183 fuentes en PENDIENTE_CONTEXTUAL (reexpresión no decidible 179 — sin texto del año original mapeable en la misma fila/columna; perímetro 40; unidad 8; signo 7; columna 4; fila 1 — con solapamientos), y 46 derivados heredan esos límites vía `limites_contextuales`.
- 52 HIPOTESIS / 35 CONVENCION / 16 NO_APLICABLE / 6 DATO_AUSENTE sin cambio; 7 PDF candidatos sin asociación declarada; selección parcial de insumos (251 archivos, no los 6.798 del ZIP).
- Una dimensión no resuelta queda pendiente; no se inventaron datos para cerrar recuentos. «COINCIDE_PROPUESTO» y los estados contextuales no acreditan significado económico ni aptitud; el control es autocomprobación reproducible del propio frente, no revisión independiente.

## Entrega

Rama `mistral/m2-cobertura-vm`; commit congelado con push a origin (SHA al final de `PUNTO_DE_RECUPERACION.md`); escritura solo en `resultados_m2/cobertura_vm/`; sin PR, fusiones, `main`, producto, libros oficiales, frentes B/C/D, resultados M1, LibreOffice/pipeline/macros; XLSX solo lectura; sin ciclos de autoaprobación. Modelo: `mistral-large-4-0`; consumo/facturación no visible desde la sesión.
