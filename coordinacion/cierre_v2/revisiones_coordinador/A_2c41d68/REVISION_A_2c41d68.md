# Revisión independiente · Frente A (Mistral, «M2 cobertura VM») · entrega `2c41d68`

Revisor: agente Claude distinto del autor (no ha escrito ni modificado este material). Fecha: 16-nov-2026.
Objeto: rama `origin/mistral/m2-cobertura-vm`, HEAD `2c41d689fde13dbb9e6affbdb470181291ec2519`; entrega anterior `d2419e5` (y `615b292`). Responde a la revisión externa `d375d80` (`revision_externa/a_d_20261116/`: leídos íntegros `REVISION_A_D.md`, `CORRECCION_A.md`, `A_REPRODUCCION.json`, `SONDAS.json`, `sondas_revision.py`).

No se ha hecho commit, push ni cambio en ningún repositorio. Ningún resultado de esta revisión atribuye aptitud financiera ni económica. Las sondas son sintéticas (no son datos de empresas), salvo s04/s05, que solo leen la salida reproducida y los insumos verificados.

## Dictamen

| # | Criterio | Veredicto |
|---|---|---|
| 1 | Importes 2000–2099 no se convierten en metadato de año | **CUMPLE CON LÍMITES** (corregido en reexpresión; sigue ocurriendo en la detección de la cabecera de columnas y en la versión) |
| 2 | Columna asignada por posición, no por búsqueda de texto | **NO CUMPLE** |
| 3 | Reexpresión: misma fila, columna, escala y perímetro; las 5 sondas del revisor siguen en CONFLICTO | **NO CUMPLE** (las 5 sondas sí dan CONFLICTO 5/5; la regla general no) |
| 4 | Escala validada en la cabecera del documento o de la tabla (miles frente a millones) | **NO CUMPLE** (sin impacto observado en los 8 casos reales por cabecera) |
| 5 | Coherencia código/salidas, control PASS exit 0, 0 CONFLICTO, manifiesto | **CUMPLE** (con límites menores) |
| 6 | Sin PDF/XLSX/ZIP nuevos, secretos ni cachés en el diff | **CUMPLE** |

En resumen, la entrega es **reproducible y coherente consigo misma**: el código regenera byte a byte las salidas publicadas y el control da PASS. Pero la acreditación contextual sigue dando por buenos casos que los criterios 2–4 prohíben. En los datos reales, **19 registros REVISADO_CONTEXTUAL** constan con «reexpresión confirmada» aunque el registro declara «no» reexpresado y el valor «original» procede de **otra fila**. Además, **32 REVISADO_CONTEXTUAL** tienen la columna dada por OK sin mapeo por posición. Esto no demuestra que esas cifras sean erróneas. Demuestra que esas dimensiones no están acreditadas y deberían figurar como pendientes (o en conflicto si hay contradicción).

## Preparación y ejecución (lo realmente ejecutado)

- Extracción con `git archive` de `2c41d68` → `rev_A/entrega`, de `d375d80` → `rev_A/revision` y de `d2419e5` → `rev_A/anterior`. No se usó checkout ni worktree.
- Insumos: ZIP local `<descargas>/munger_v2_r1_entrega4.14_cierre_verificacion_entradas.zip`, de 1.130.912.246 bytes, con SHA-256 `bb51942cefb848e409a4828e3faeb70f94aa4d29af39cda6d90cd0a97cb7b93e`, igual a `configuracion.json`. No se usó la red.
  - `preparar_insumos.py` no puede ejecutarse sobre una extracción `git archive`, porque exige `git remote` del auxiliar. Por eso se usó un extractor equivalente propio (`sondas/s00_preparar_copia.py`): mismos miembros, rutas seguras, bytes y SHA-256 por archivo.
  - Resultado: **251/251 insumos conformes**, exit 0. Es una selección parcial: no se materializan los 6.798 archivos.
- Reproducción en una copia aislada `rev_A/repro`, con `python3 -I -B` y rutas absolutas (`sondas/s01_reproducir.sh`). Python 3.13.18, openpyxl 3.1.5 y pypdf 6.17.0 (el autor declaró Python 3.12 y pypdf 7.1.0). No se ejecutó LibreOffice ni el pipeline del producto.

| Comando (orden de MAPA_REGENERACION/ENTREGA.json) | exit | Salida clave |
|---|---:|---|
| `inventario.py` | 0 | 677 / 617 nuevas / 22 lotes / 21 fuentes CONFORME / 0 huecos |
| `verificar_fuentes.py` | 0 | 467 COINCIDE_PROPUESTO |
| `verificar_contexto.py` | 0 | fuentes 241 REV / 183 PEND / 43 M1; reexpresión 199 OK / 180 ND / 88 NA |
| `derivaciones.py` | 0 | 101 nodos (14/87), 0 ciclos |
| `construir_cobertura.py` | 0 | CSV 282 REV / 229 PEND / 60 M1 / 106 NA / **0 CONFLICTO** |
| `control_negativo.py` | 0 | 218 mutaciones, 168 ctx, 40 mec, `bilaterales_ok=true`, `sondas_revisor` 5/5 CONFLICTO |
| `control_cobertura.py` | 0 | **PASS=true, 0 violaciones** |
| `revisar_lote.py L00..L21` | 0 (todos) | lotes regenerados |
| `asociacion_pdf.py` | **1** | `PdfReadError` de pypdf 6.17.0 (entorno del revisor); no reproducido |

Comparación byte a byte con los 52 archivos del manifiesto: **51 IGUALES**. Difiere `resultados/inventario.json` solo en la ruta absoluta `directorio` (`/workspace/github__…` frente a la ruta local). No está en el diff de esta entrega.

## Criterio 1 · Importes 2000–2099 · CUMPLE CON LÍMITES

**Corregido.** La v3.1 cambia `check_reexpresion` (`verificar_contexto.py:431-457`): ya no clasifica como metadato por el valor, sino por unidad/concepto (`es_metadato_anio`). Sondas propias (`s02`):

- 1a: cabecera «2025 2024» en una línea y fila «Share based payments 2045 2001» (miles). Resultado: REVISADO_CONTEXTUAL; columna por posición → 2024; reexpresión NO_APLICA por el camino normal.
- 1e: `es_metadato_anio` con unidad monetaria y valor 2045 → False.
- 1f: importe 2045 sin texto original → NO_DECIDIBLE, no NO_APLICA.

El caso real `Viscofan aux:AR2025_p27_pagos_acciones_2024` pasa de NO_APLICA a NO_DECIDIBLE (diff del CSV y de `verificacion_contexto.jsonl`).

**Límite (defecto latente).** `YEAR_RE = re.compile(r'20\d\d')` (línea 24) no tiene límites de palabra. `find_header_block` (líneas 164-182) elige como «línea de columnas» la que tenga más coincidencias (línea 174). `years_in_block` alimenta `check_columna` y `check_version` (línea 409). Los importes siguen convirtiéndose en años fuera de la reexpresión:

| Sonda | Entrada mínima | Obtenido | Debía |
|---|---|---|---|
| 1b | cabecera en dos líneas `2025` / `2024`; fila `Share-based payments 2045,3 2001,7`; declarado 2024 = 2001,7 | CONFLICTO «posicion 1 -> columna 2001 … (linea de columnas ['2045','2001'])» | OK o NO_DECIDIBLE |
| 1c | misma página + fila `Revenue 10.000 9.000`; declarado 2024 = 9.000 (correcto) | CONFLICTO, columnas `['2045','2001']` (el importe contamina las filas siguientes) | OK o NO_DECIDIBLE |
| 1d | página del informe 2019 (`2019 2018`) atribuida a `CF_2025.txt`; único «2025» = importe `2025,4` | versión **OK** «año 2025 figura en la página» | CONFLICTO o NO_DECIDIBLE |

Caso real: `Viscofan Análisis!C37`. Los precios del boletín `0,2050 0,2095 0,2072` se leen como años `[2050, 2072, 2095]` y se toman como encabezado (s04). Acaba en PENDIENTE, así que no hay aceptación falsa.

La afirmación de ENTREGA.json («importes 2000-2099 con unidad monetaria no se tratan como años») está sobredimensionada: solo es cierta en la reexpresión.

## Criterio 2 · Columna por posición · NO CUMPLE

`check_columna` (líneas 303-339) busca el **primer token que coincide textualmente** con el valor (línea 330) y lo mapea a `col_years`. Tiene tres salidas OK que no usan la posición:

- fila no alineable → «decidido por año» (línea 338);
- valor no localizado → OK solo porque el año figura en el encabezado (línea 339);
- valores < 1000 sin separador descartados por `value_like` (línea 316) → caen en la línea 339.

Contraejemplos mínimos (`s02`, módulo sin modificar):

| Sonda | Cabecera / fila | Declarado | Obtenido | Debía |
|---|---|---|---|---|
| **2a mismo literal en dos columnas** | `Consolidated 2025 2024 Parent 2025 2024` / `Revenue 10.000 9.000 7.000 6.000` | 2024 consolidado = 6.000 (es la columna 2024 *Parent*) | **OK** «posicion 3 → columna 2024» | NO_DECIDIBLE / CONFLICTO |
| 2b mismo valor en dos columnas | `2025 2024` / `Revenue 9.000 9.000` | 2024 = 9.000 (correcto) | CONFLICTO falso «posicion 0 → 2025» | OK / NO_DECIDIBLE |
| 2c valor ausente | `2025 2024` / `Revenue 10.000 9.000` | 2024 = 8.000 | **OK** | CONFLICTO / NO_DECIDIBLE |
| 2d valor < 1000 | `2025 2024` / `Earnings per share 950 900` | 2024 = 950 (es 2025) | **OK** | CONFLICTO / NO_DECIDIBLE |
| 2e columna de variación | `2025 2024 Variation` / `Revenue 10.000 9.000 1.000` | 2024 = 10.000 (es 2025) | **OK** «decidido por año» | CONFLICTO / NO_DECIDIBLE |

Controles positivos: 2f (OK) y 2g (la sonda 3 de d375d80, CONFLICTO) se comportan bien.

**Impacto real** (`s04`): 74 entradas con columna OK sin mapeo por posición. De ellas, **32 son REVISADO_CONTEXTUAL**, por ejemplo:

- `Vidrala Historia!D25…L25`: columna «Personnel» en una tabla de 5 valores;
- `Vidrala aux:italia_*`: segmento «Italy» en una fila de 4 valores;
- `Vidrala Configuración V6.4!B44/B45/B49/B50`;
- `Viscofan Configuración V6.4!B147/B148/B150/B151`.

En esas filas la columna (segmento o tipo de provisión) no se ha comprobado por posición. La regla de d375d80 («ambigüedad → pendiente») exige NO_DECIDIBLE.

## Criterio 3 · Reexpresión · NO CUMPLE

**Conservado:** las 5 sondas de `sondas_revision.py` (parte A), repetidas literalmente contra 2c41d68 (`s03`), dan **5/5 CONFLICTO**. Coinciden con `control_negativo.json` → `sondas_revisor`. Los controles positivos 3i y 1a pasan.

**Defectos** en `check_reexpresion` (líneas 442-514):

1. **Atajo de cita** (línea 481). Si la cita aplanada aparece en *cualquier* parte del texto original, se acepta sin mapear columna, fila, escala ni perímetro.
2. **Fila.** La fila se elige por un prefijo alfabético de la cita (12–80 caracteres) y gana la **primera** línea que lo contiene (líneas 488-497).
3. **Columna.** Se toma `cy2.index(yc)`, la primera aparición del año (línea 499).
4. **Escala y perímetro no se comparan en ningún punto**, aunque `RESPUESTA_A_D_20261116.md` (apartado 5) dice que sí.
5. **Contradicción.** Solo se detecta si lo declarado contiene literalmente `no aplica`, `no reexpres` o `igual al original` (líneas 483, 501, 504). Si no, toda diferencia es «reexpresión confirmada» OK (línea 506).

| Sonda | Original 2024 (CF_2024.txt) | Comparativo / declarado | Obtenido | Debía |
|---|---|---|---|---|
| 3c columnas ascendentes | `2023 2024` / `Revenue 9000 10000` | `Revenue 9000`, «no reexpresado; igual al original» | NO_APLICA «misma cita: coherente» | CONFLICTO |
| 3d prefijo numérico | `2024 2023` / `Revenue 90000 80000` | ídem | NO_APLICA | CONFLICTO / ND |
| 3e otro perímetro | tabla individual `Revenue 9000 7000` + consolidada `Revenue 10000 9000` | consolidado 9000, no reexpresado | NO_APLICA (toma la individual) | CONFLICTO / ND |
| 3f otra escala | «Amounts in millions» `Revenue 9.000 8.000` | miles, 9.000, no reexpresado | NO_APLICA | CONFLICTO / ND |
| 3g otra fila | `Revenue from discontinued operations 9000 8000` / `Revenue 10000 9500` | `Revenue 9000`, no reexpresado | NO_APLICA (fila equivocada) | CONFLICTO |
| 3h sin razón documental | `Revenue 10000 8000` | 9000, `reexpresado=''` | **OK** «reexpresión confirmada» | CONFLICTO / ND |
| 3j redacción «no (igual que…)» | `Revenue 10000 8000` | 9000, «no (igual que el informe original)» | **OK** «reexpresión confirmada» | CONFLICTO |

**Impacto real** (`s05`, sobre la salida reproducida, igual a la publicada). Hay 78 entradas con «reexpresión confirmada por columna»:

- **19 REVISADO_CONTEXTUAL** (+1 PENDIENTE) declaran «no» reexpresado y el «original» difiere: contradicción etiquetada OK. Ejemplos comprobados en los insumos:
  - `Vidrala aux:lyb_c_2017` (deuda corriente 41,519): se compara con la línea 105 de CF_2017 `Loans and borrowings 15 487,819 310,288`, que es la deuda **no corriente**. La fila corriente correcta (línea 112, `41,519 12,402`) coincide.
  - `Viscofan aux:CF2021_p8_var_existencias/deudores/acreedores_2020`: las tres se comparan con `Adjustment for income taxes … 37.143` (AR_2020, línea 385).
  - `Viscofan aux:CF2022_p25_var_*_2021` y `Historia!H8`: todas con 43,423.
  - `Vidrala aux:circ_2022_l1/l2/l4`, `aux:lyb_c_2018…2024`, `Viscofan Historia!F21/H13`.
- **37 REVISADO_CONTEXTUAL** (+7 M1) solo difieren en el signo (`25,544` frente a `-25544`). Se reportan como «reexpresión confirmada» aunque no hay reexpresión.
- 12 REVISADO declaran reexpresión con razón documental (Italia 2023, PPA 2023…). No se ha verificado su razón.

Observación menor: la etiqueta con guion («Share-based») no casa (`s02` obs). Por eso el caso real v3.1 `aux:AR2025_p27_pagos_acciones_2024` queda NO_DECIDIBLE con el motivo «no en la misma fila/columna 2024». Ese motivo es inexacto: CF_2024 p.9 imprime `Share-based payment 2,001 2,346` bajo `Notes 2024 2023`. El resultado es conservador, pero el motivo publicado en ENTREGA.json y HALLAZGOS.md no es correcto.

## Criterio 4 · Escala · NO CUMPLE

En `check_unidad` (líneas 204-240), si la página no tiene frase de miles ni de «euros» (`EUROS_ONLY_RE`, línea 203), basta `doc['miles']` para dar OK (línea 230). `doc['miles']` sale de cualquier mención en las 8 primeras páginas (`doc_info`). «Millones/millions» no se reconoce como escala contraria. `MILES_RE` (línea 202) incluye `in thousands` sin exigir euros.

| Sonda | Página | Cabecera doc | Declarado | Obtenido | Debía |
|---|---|---|---|---|---|
| 4a | `Amounts in millions of euros` | miles | miles, 0,001 | **OK** «acreditada en la cabecera» | CONFLICTO / ND |
| 4b | `Millones de euros` | miles | miles, 0,001 | **OK** | CONFLICTO / ND |
| 4c | `Number of shares (in thousands)` | — | miles de euros, 0,001 | **OK** «'in thousands'» | CONFLICTO / ND |
| 4d | `Amounts in millions of euros` | neutra | miles, 0,001 | NO_DECIDIBLE | correcto |

Controles: 4e (A-R3, escala 1 frente a cabecera en miles) → CONFLICTO. 4f (euros/miles) → CONFLICTO. 4g (positivo) → OK.

Impacto real (`s04`): 8 OK por cabecera (7 REVISADO). Sus páginas mencionan miles/thousand y ninguna menciona millones, así que no se observa aceptación falsa en los datos. La sonda pedida (miles frente a millones), en cambio, falla.

## Criterio 5 · Coherencia código/salidas · CUMPLE

- Pipeline re-ejecutado: salidas **idénticas byte a byte** a las publicadas (51/52; la excepción es solo una ruta absoluta en `inventario.json`, fuera del diff).
  - `control_cobertura.py` exit 0, PASS, 0 violaciones.
  - CSV con **0 CONFLICTO_CONTEXTUAL** (282/229/60/106).
  - `control_negativo.py` exit 0: 218/168/40, `bilaterales_ok=true` (15/15), `sondas_revisor` 5/5 CONFLICTO.
  - Coincide todo lo declarado en ENTREGA.json.
- SHA-256 reproducidos e iguales a los publicados:

  | Archivo | SHA-256 |
  |---|---|
  | `COBERTURA_677.csv` | `e83917e0fb31aabecc1949e1ac0e3d2369e74f2ff74dca0878476338285a2ec5` |
  | `DERIVADOS.json` | `ecb30f2d47fcbea183288e4f582d50255c015c4638ba3436e51bf4ae140112a3` |
  | `verificacion_contexto.jsonl` | `e5603fe5aa6c0ed0f819ea46645111d05003cc5693d8ba8069355bdf6295aabf` |
  | `control_cobertura.json` | `4f0230861b55c76709c0ddbfde0718dc2591cd933a4d09cc78637a00ea313ea3` |
  | `control_negativo.json` | `9df1fc4b1988ff0fedc1cc1466107b047a5a4a7b74e194581c53823f94393f2c` |

- Manifiesto: `sha256sum -c` exit 0, **52/52**. Cubre todos los archivos de la carpeta salvo el propio manifiesto (`s06`).

Límites:

- No existe `COMANDOS.md`; los comandos salen de `ENTREGA.json`, `MAPA_REGENERACION.md` y `PUNTO_DE_RECUPERACION.md`.
- `asociacion_pdf.py` no se reprodujo (exit 1 con pypdf 6.17.0; su salida no cambia en esta entrega).
- El PASS es una autocomprobación de coherencia: no detecta los defectos de los criterios 2–4.
- Hay recuentos desfasados: `MAPA_REGENERACION.md:57`, `HALLAZGOS.md:60` y `RESPUESTA_A_D_20261116.md:18,33,62` dicen reexpresión 179 ND / 89 NA; el código vigente da 180/88.

## Criterio 6 · Diff limpio · CUMPLE

Según `s06`, `git diff d2419e5 2c41d68` contiene 12 archivos de texto, todos en `resultados_m2/cobertura_vm/`:

- 0 binarios (numstat);
- ningún `.pdf`, `.xlsx`, `.zip`, `.pyc` ni `__pycache__`, ni en el diff `615b292..2c41d68` ni en el árbol de `2c41d68`;
- ningún patrón de secreto (`ghp_`, `github_pat_`, `sk-`, `AKIA`, claves privadas, `authorization:`, `password=`): grep exit 1;
- 0 líneas añadidas con rutas locales absolutas.

## Corrección mínima sugerida (para el autor; no aplicada)

1. **Años de columna.** `YEAR_RE` con límites (`(?<![\d.,])20\d\d(?![\d.,])`), y elegir la cabecera solo entre líneas sin importes. No acreditar la versión por un año dentro de una cifra.
2. **Columna.** Sustituir las tres salidas OK no posicionales (líneas 316, 338 y 339) por NO_DECIDIBLE. Detectar literales de año repetidos en la cabecera y valores repetidos en la fila (→ NO_DECIDIBLE).
3. **Reexpresión.**
   - Eliminar el atajo de cita, o exigir en él la misma fila y columna por posición.
   - Exigir etiqueta de fila completa e inequívoca, y la misma escala y perímetro de la tabla original.
   - Diferencia sin razón documental → NO_DECIDIBLE.
   - Declaración negativa en cualquier redacción («no», «no (igual que…)») con valor distinto → CONFLICTO.
   - Diferencia solo de signo → no es reexpresión; tratarla con la convención de signo.
4. **Escala.** Reconocer millones/millions como escala explícita contraria en la página. Limitar `in thousands` a importes en euros. Justificar el alcance de la cabecera sobre la tabla concreta.
5. Regenerar las salidas dependientes. Las 19 + 32 entradas REVISADO afectadas deberían pasar a PENDIENTE salvo evidencia, junto con sus derivados. Actualizar los recuentos 179/89 en los documentos.

## Archivos de esta revisión

- Sondas y salidas: `rev_A/sondas/`
  - `s00_preparar_copia.py/.out`
  - `s01_reproducir.sh/.out`
  - `s02_sondas_revisor_A.py/.json/.out`
  - `s03_sondas_d375d80_A.py/.json/.out`
  - `s04_impacto_datos_reales.py/.json/.out`
  - `s05_reexpresion_real.py/.json/.out`
  - `s06_integridad_diff.sh/.out`
- Copias: `rev_A/entrega` (2c41d68, sin modificar), `rev_A/repro` (reproducción con insumos), `rev_A/revision` (d375d80), `rev_A/anterior` (d2419e5).
