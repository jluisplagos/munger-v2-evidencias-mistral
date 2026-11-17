# Revisión independiente · Frente A (Mistral, «M2 cobertura VM») · respuesta a la corrección A3 · `0946971`

- **Revisor:** agente Claude distinto del autor. No ha escrito ni modificado este material. Fecha: 17-nov-2026.
- **Objeto:** rama `origin/mistral/m2-cobertura-vm`, ocho commits sobre `8b88fab`: `93a02e0` (A3-R1), `d11ee44` (R2), `74d94f8` (R3), `c472595` (R4), `2e4eb15` (R5), `447a977` (R6), `4f50e6a` (R7) y `0946971e1e4cf10cb85ed4c757968a4bd060d6a7` (R8). Carpeta `resultados_m2/cobertura_vm/`.
- **Alcance:** solo A3-R1…R8, según `coordinacion/cierre_v2/revisiones_coordinador/A2_8b88fab/CORRECCION_A3.md` y `REVISION_A2_8b88fab.md` (rama `origin/coordinacion/cierre-v2`, leídos con `git show`). He leído `RESPUESTA_A3_CIERRE_V2.md`, `ENTREGA.json`, `COMANDOS.md` y el diff de código de cada commit.
- **Restricciones respetadas:** sin commit, push ni cambios en ningún repositorio; sin red; sin LibreOffice; sin checkout ni worktree. Extracción con `git archive`. Todo Python con `-I -B`: `COMANDOS.md` ya no exige `-E -s` para `cola_pendientes.py` y `resolver_bloque2.py`, y con `-I` terminan con código 0.
- **Alcance del juicio:** ningún resultado de esta revisión atribuye aptitud financiera ni económica. Un PASS, un recuento o un CONFLICTO de software no prueban la verdad ni el error de una cifra.

## Dictamen

| Punto | Veredicto | En una línea |
|---|---|---|
| **A3-R1** signo impreso | **CERRADO CON LÍMITES** | Los **79 CONFLICTO de columna pasan a OK (79/79)**. En el commit R1, las 104 filas del CSV cambian exactamente como preveía el contrafactual A2 (70→REVISADO, 34→PENDIENTE). Límite: la comparación exige ahora el signo, pero no reconoce la raya U+2013 y pierde el cero inicial de los importes < 1. Son dos regresiones OK→CONFLICTO frente a `8b88fab`, sin impacto real hoy |
| **A3-R2** cabecera | **ABIERTO** | R1c y R1d dan el estado esperado y B150 queda PENDIENTE. Pero la regla nueva «a igualdad, gana la cabecera más próxima» **crea OK falsos que en `8b88fab` eran CONFLICTO**: una nota breve con los años invertidos entre la cabecera y la fila, y una cabecera partida a más de 3 líneas. El filtro por número de palabras descarta además cabeceras tabulares reales: 61 OK reales se apoyan en el título del estado |
| **A3-R3** importe con forma de año | **ABIERTO** | R1e queda NO_DECIDIBLE. Pero el cambio es global: los años sin puntuar pasan a ser «importes» también en la línea de cabecera y en el original. **3 CONFLICTO falsos reales nuevos en R3** (`Palancas!C48` y `Control maestro!H4`, con valor «EUR»; `aux:ing_fin_2017`), más 4 en R4 por la misma causa |
| **A3-R4** reexpresión | **ABIERTO** | Quitado el atajo: las 18 quedan PENDIENTE, incluidas las promociones 28/35. Pasan 3e–3g y R2a–R2f. Pero:<br>- la «polaridad» lee «sí: reexpresado **sin** Italia» como negación: **5 CONFLICTO falsos reales**, 2 de ellos REVISADO→CONFLICTO;<br>- no reconoce «None of … were restated» ni «ninguna», que pasan de ND a **OK falso**;<br>- el rótulo «sin dígitos» iguala «At 31 December 2015» con «… 2017»;<br>- escala y perímetro solo por página;<br>- B46 y B47 siguen igual |
| **A3-R5** versión | **CERRADO CON LÍMITES** | 1d y R4a dan CONFLICTO; `F6` y `J21` quedan PENDIENTE. Límites:<br>- un importe sin puntuar «2025» sigue acreditando la versión, en contradicción con A3-R3;<br>- un año seguido de coma o punto solo en el título del documento da CONFLICTO, una regresión;<br>- `G25` sigue en CONFLICTO, por otra causa (R3/R4).<br>0 casos reales |
| **A3-R6** escala | **CERRADO CON LÍMITES** | R3a y R3b dan CONFLICTO. Siguen dando OK por la cabecera «Cifras en millones», «(€m)», «MEUR» y «(M€)». Sin impacto real |
| **A3-R7** derivados como operandos | **CERRADO** | La propagación es transitiva (cadena de 3 niveles). El **control negativo con datos reales** funciona: con `0946971`, `Vidrala Análisis!C41` pasa a CONFLICTO y el control lo señala; con `8b88fab`, no. Latente y mitigado: un ciclo o un operando inexistente devuelven REVISADO en la función, pero `control_cobertura` los rechaza |
| **A3-R8** textos y huellas | **ABIERTO** | Se cumple: `-I` arreglado, sondas A2 publicadas (idénticas), mensaje claro con pypdf 6.17.0 y un commit por punto que se reproduce. **No se cumple:**<br>- el `ENTREGA.json` publicado **no es la salida del generador**: tiene una huella con un dígito cambiado, otro formato y `base_revisada_sha`/`naturaleza` desfasados;<br>- el «motivo corregido» de AR2025_p27 afirma «OK por igualdad», pero en `0946971` es NO_DECIDIBLE;<br>- HALLAZGOS omite los 4 derivados en CONFLICTO;<br>- `actualizar_textos_resumen.py` no se puede volver a ejecutar |

**Reproducibilidad: CUMPLE.**
- **192 de 196** archivos del manifiesto se reproducen byte a byte. Las 4 diferencias son:
  - la marca de tiempo (2 archivos);
  - la ruta absoluta de `inventario.json`;
  - `ENTREGA.json` (véase A3-R8).
- **Cada commit intermedio reproduce sus propias salidas:** `verificacion_contexto.jsonl`, `DERIVADOS.json`, `COBERTURA_677.csv` y `control_cobertura.json`, en 7/7 commits.
- Las listas `cambios_estado_a3_R1…R7.json` se regeneran iguales a partir de los pares de commits.

**Datos reales:**
- CSV de 169/209/133 a **209/283/19** (REVISADO/PENDIENTE/CONFLICTO).
- **0 entradas REVISADO sin todas sus dimensiones.**
- De las 28 que pierden REVISADO, 26 quedan PENDIENTE y **2 pasan a CONFLICTO sin contradicción documentada** (`Historia!J7` y `aux:bai_2023`, por el artefacto de polaridad).
- **Ninguno de los 15 CONFLICTO de fuente de `0946971` es una contradicción acreditada:** los 15 son artefactos, 13 de ellos introducidos por R3 y R4.

## Preparación y ejecución

**Extracción**
- `git archive 0946971` → `<rev_A3>/entrega`, sin modificar.
- Para comparar se usa `<rev_A2>/entrega` (`8b88fab`) de la revisión anterior.

**Insumos** (`sondas/s00_preparar_copia.py`, la misma lógica que en A2)
- ZIP `<zip>` con SHA-256 `bb51942cefb848e409a4828e3faeb70f94aa4d29af39cda6d90cd0a97cb7b93e`.
- **251/251 conformes**, código 0. Copia aislada en `<rev_A3>/repro`.

**Entorno del revisor**
- Python 3.13.18, openpyxl 3.1.5, pypdf 6.17.0.
- El autor declara Python 3.12.15 y pypdf 7.1.0.

**Reproducción** (`s01_reproducir.sh`, en el orden de `COMANDOS.md`, bloques v4.0 y A3)

| Comando | Código | Salida clave |
|---|---:|---|
| `inventario.py` | 0 | 677 / 617 / 22 lotes / 21 CONFORME |
| `verificar_fuentes.py` | 0 | 467 COINCIDE_PROPUESTO |
| `verificar_contexto.py` | 0 | fuentes 176 REV / 233 PEND / 15 CONFL / 43 M1 / 210 NA |
| `derivaciones.py` | 0 | 101 nodos, 0 ciclos |
| `construir_cobertura.py` | 0 | CSV **209 / 283 / 19 / 60 / 106** |
| `control_negativo.py` | 0 | 219 mutaciones: 140 ctx, 40 mec; bilaterales 15/15; d375d80 5/5 CONFLICTO; sonda A3-R7 detectada |
| `control_cobertura.py` (dos veces) | 0 | **PASS, 0 violaciones** |
| `cola_pendientes.py`, `resolver_bloque2.py` **con `-I`** | 0 | 233 fuentes / 50 derivados / 88 grupos; salidas IGUALES |
| `revisar_lote.py L00..L21` | 0 | 22 lotes IGUALES |
| `asociacion_pdf.py` | 1 | mensaje claro con pypdf 6.17.0, precedido de unas 1964 líneas de aviso de pypdf (`fontTools is required…`). Su salida no se regenera aquí |
| `generar_recuentos_doc.py` | 0 | igual salvo la marca de tiempo |
| `generar_cambios_estado.py 8b88fab a3` (con `GIT_DIR` del clon, solo lectura) | 0 | 142 fuentes / 184 filas; IGUAL |
| `generar_entrega_json.py` | 0 | produce un `ENTREGA.json` **distinto** del publicado (véase A3-R8) |
| `actualizar_textos_resumen.py` | **1** | `ANCLA NO ENCONTRADA en RESUMEN_PARA_CLAUDE.md`: es un parche de un solo uso con texto fijo, no un generador |
| `generar_manifiesto.py` | 0 | 196 archivos |

**Commits intermedios y listas por punto**
- `s01c_commits_intermedios.sh`: en cada uno de los 7 commits A3-R1…R7, la cadena inventario → control da código 0. Sus 4 salidas que fijan estados son IGUALES a las publicadas en ese mismo commit.
- `s01d_cambios_por_punto.sh`: las listas por punto se regeneran iguales. Recuentos fuentes/CSV:
  - R1 71/104;
  - R2 4/4;
  - R3 27/29;
  - R4 54/70;
  - R5, R6 y R7: 0/0.

## Sondas de la revisión anterior sobre `0946971`

Ejecuté `s02`, `s03` y `s07` de la revisión A2, sin cambios, sobre `<rev_A3>/repro/.../verificar_contexto.py`. Sus estados coinciden con los publicados por el autor en `sondas_a3/out/R8_*_final.json`.

**Pasan todas las de la lista de cierre:**
- 1b y 1c: OK, ahora con la cabecera partida fusionada;
- 1d: CONFLICTO;
- 2a–2g;
- 3a–3j, incluidas **3e** (ND, perímetro), **3f** (ND, escala) y **3g** (CONFLICTO);
- 4a–4g;
- d375d80: 5/5 CONFLICTO;
- R1a y R1b: OK;
- R1c: CONFLICTO;
- R1d y R1e: ND;
- R2a–R2c: CONFLICTO;
- R2d–R2f: ND;
- R3a y R3b: CONFLICTO;
- R4a: CONFLICTO.

Además, 1a pasa a REVISADO: la regresión conservadora de A2 desaparece.

## Sondas nuevas: una variante no literal por defecto (`s07_sondas_nuevas_A3.py`)

La misma sonda se ejecutó sobre `8b88fab` (`s07_sondas_nuevas_A3_sobre_8b88fab.*`) para separar lo que ya fallaba de lo que A3 introduce.

| Punto | Sonda | Entrada mínima | `8b88fab` | `0946971` | Debía | Clase |
|---|---|---|---|---|---|---|
| R1 | N1a | `2025 2024` / `Changes in working capital –47.708 –7.660` (U+2013); 2024 = −7660 | OK | **CONFLICTO** | OK | regresión: CONFLICTO falso |
| R1 | N1b | `2025 2024` / `Dividend per share (euros) 0,25 0,21`; 2024 = 0,21 | OK | **CONFLICTO** | OK | regresión: `Decimal("021")` = 21 |
| R1 | N1c (control) | `(10.000) (9.000)`; 2025 = −9000 | CONFLICTO | CONFLICTO | CONFLICTO | — |
| R2 | **N2a** | `Notes 2025 2024` / `* 2024 and 2025 figures restated` / `Revenue 10.000 9.000`; 2024 = 10.000 | CONFLICTO | **OK** | CONFLICTO / ND | **regresión: OK falso** |
| R2 | **N2b** | `2025` / `2024` / `Assets` / `Non-current assets` / `PPE 12.000 11.000` / `Goodwill 1.500 -`; 2024 = 1.500 | CONFLICTO | **OK** | CONFLICTO / ND | **regresión: OK falso** |
| R2 | N2c | `EQUITY AND LIABILITIES Note 2025 2024` / `Share capital 35.910 34.200`; 2024 = 34.200 | OK | ND | OK | regresión conservadora |
| R3 | **N3a** | `Share price € 2025 2024 2023` como fila, valor «EUR» | ND | **CONFLICTO** | NA / ND | regresión (patrón real C48 y H4) |
| R3 | N3b (control) | `2025 2024` / `Bonds maturing 2030 1.500 1.200`; 2024 = 1.200 | OK | ND | OK / ND | conservador |
| R4 | **N4a** | original `Revenue 10.000 8.000`; comparativo 9.000, «sí: 2024 reexpresado sin la filial vendida» | OK | **CONFLICTO** «declara no reexpresado» | OK / ND | regresión (patrón real J6, J7, J8, bai, impuesto) |
| R4 | **N4b** | ídem con «None of the comparative figures were restated» | ND | **OK** «reexpresión confirmada» | CONFLICTO / ND | **regresión: OK falso** |
| R4 | **N4c** | ídem con «reexpresión: ninguna» | ND | **OK** | CONFLICTO / ND | **regresión: OK falso** |
| R4 | **N4d** | original `2024 2023` / `At 31 December 2023 5.000`; cita `At 31 December 2024 6.000`, «no» | ND | **CONFLICTO** «imprime 2023 en la columna 2024» | ND | regresión (patrón real D25–H25 e ing_fin_2017) |
| R4 | N4e | misma página con la tabla consolidada (10.000) y la individual (9.000); cita 9.000, consolidado | NA | **NA** «coherente» | CONFLICTO / ND | acreditación indebida: el perímetro se decide por página |
| R4 | N4f | p.1 «(in millions of euros)», p.2 tabla `Revenue 9.000`; comparativo en miles | NA | **NA** «coherente» | CONFLICTO / ND | acreditación indebida: la escala se decide por página |
| R5 | N5a | página de 2019 atribuida a `CF_2025.txt`; fila `Number of employees 2025 1980` | OK | **OK** | CONFLICTO / ND | ya existía; contradice R3 |
| R5 | N5b | sin año en la página; título del documento «… at December 31, 2025, and directors report» | OK | **CONFLICTO** | OK | regresión conservadora |
| R6 | N6a–N6d | «Cifras en millones», «(€m)», «Amounts in MEUR», «(M€)», con cabecera en miles | OK | **OK** | CONFLICTO / ND | ya existía, sin cubrir |
| R7 | N7a / N7b | cadena D = f(E, H), E = f(G), G = f(F); F PENDIENTE, y luego todo REVISADO | — | PENDIENTE / REVISADO | ídem | — |
| R7 | N7c / N7d | ciclo D↔E; operando inexistente | — | REVISADO | PEND / CONF | latente, mitigado por `control_cobertura` |

**Lectura de las sondas nuevas:**
- **R1:** `check_columna` exige ahora el signo (`(s < 0) == neg_target`), pero `NUM_RE` solo lo reconoce como `(`, `−` y `-`. Además, la magnitud se compara como `normalize_num(str(abs(Decimal)))` frente a dígitos sin ceros. Cualquier signo no reconocido, o un importe < 1, pasa de OK a CONFLICTO. Hoy hay 0 casos reales: ningún valor < 1 y ninguna fila citada con U+2013.
- **R2:** el desempate `>=` en `find_header_block` (modo `max`) elige la línea de años más próxima a la fila.
  - Una nota breve entre la cabecera real y la fila gana, aunque tenga los años invertidos. El filtro solo exige «palabras ≤ años».
  - La fusión de la cabecera partida solo mira 3 líneas por encima de la fila (`row_idx - 3`). En una cabecera `2025`/`2024` a más distancia gana `2024` sola, como tabla de una columna.
  - En `8b88fab` las dos sondas daban CONFLICTO.
  - **En sentido inverso:** la cabecera real de un balance, «EQUITY AND LIABILITIES Note 2017 2016», tiene 3 palabras y se descarta como frase. En los datos reales, **61 columna OK (56 REVISADO)** se mapean con el título «31 December 2017 and 2016», es decir, con una línea que no es tabular. Aciertan porque el título y las columnas tienen el mismo orden, no por una cabecera inequívoca.
- **R3:** `nums` en `check_columna` y `nums_of` en `check_reexpresion` dejan de excluir los años sin puntuar en todas partes.
  - Una línea de cabecera citada como fila hace que sus años cuenten como importes, y un valor no numérico («EUR») se compara por posición.
  - Un rótulo de fecha («At 31 December 2015») aporta el «importe» 2015.
- **R4, polaridad:** la ventana es de 30 caracteres antes y 15 después.
  - Basta un «sin» o un «no» en la razón de una afirmación para clasificarla como negación.
  - Al revés, «None», «ninguna» o «nunca» no cuentan, y cualquier «restated» o «reexpres…» no negado da `affirm`.
- **R4, fila:** se toma por rótulo completo, pero tras quitar los dígitos (`re.sub(r'\d[\d.,]*', ' ', …)`), así que las fechas y las notas desaparecen del rótulo. No se distingue entre dos tablas con el mismo rótulo.
- **R4, escala y perímetro:** se comparan con `escala_pagina` y `perimetro_pagina` de la página de la fila. No se miran la tabla ni las páginas anteriores (`check_unidad` sí lo hace con `buscar_nota_escala_tabla`). Si la página no dice nada, no se compara.
- **R5:** `years_in_block` sigue contando como año un «2025» sin puntuar. `yb` (`(?![\d.,])`) excluye «2025,» y «2025.» en la cabecera y el título.
- **R6:** `MILLONES_RE` sigue siendo una lista de frases. Faltan las abreviaturas (m, mn, MEUR, M€) y «en millones» sin «de euros».

## Datos reales

### Estados frente a `8b88fab` (`s04_cambios_estado.py`)

| Nivel | `8b88fab` REV / PEND / CONFL | `0946971` REV / PEND / CONFL | Cambian |
|---|---|---|---:|
| Fuentes (`verificacion_contexto.jsonl`) | 148 / 183 / 93 (+43 M1, 210 NA) | **176 / 233 / 15** (+43 M1, 210 NA) | 142 |
| Derivados (DERIVADOS.json) | 21 / 26 / 40 (+14 M1) | **33 / 50 / 4** (+14 M1) | — |
| CSV 677 | 169 / 209 / 133 (+60 M1, 106 NA) | **209 / 283 / 19** (+60 M1, 106 NA) | 184 |

**Transiciones de fuente:**
- CONFLICTO→PENDIENTE 51;
- CONFLICTO→REVISADO 36;
- REVISADO→PENDIENTE 26;
- PENDIENTE→REVISADO 20;
- PENDIENTE→CONFLICTO 7;
- REVISADO→CONFLICTO 2.

**En el CSV** (fuentes y derivados):
- CONFLICTO→PENDIENTE 72 (49 fuentes + 21 derivados + 2 ceros);
- CONFLICTO→REVISADO 52 (36 + 16);
- REVISADO→PENDIENTE 30;
- PENDIENTE→REVISADO 20;
- PENDIENTE→CONFLICTO 8;
- REVISADO→CONFLICTO 2.

**Por dimensión:**
- columna: CONFLICTO→OK 79, ND→OK 20, OK→ND 11, ND→CONFLICTO 2;
- reexpresión: NA→ND 37, CONFLICTO→ND 18, OK→ND 10, ND→NA 9, OK→CONFLICTO 4, ND→CONFLICTO 4.

**Comprobaciones:**
- **0 entradas REVISADO con alguna dimensión ND o CONFLICTO**, y todas tienen las 7 dimensiones.
- **Pierden REVISADO 28:** 26 quedan PENDIENTE y **2 pasan a CONFLICTO** (`Vidrala Historia!J7` y `Vidrala aux:bai_2023`). Ninguna de las dos tiene una contradicción documentada: véase la muestra de CONFLICTO. El encargo pedía PENDIENTE.
- **Las 20 PENDIENTE→REVISADO** son los metadatos de año `Historia!C5…L5` de las dos empresas: la columna pasa de ND a OK. El valor es el propio año, comparado con su posición en la línea de años. Es una acreditación tautológica, pero correcta.

### A3-R1: los 79 de columna y los 104 (`s05_seguimiento_signo.py`)

- **Los 79 CONFLICTO de columna de `8b88fab` dan ahora OK (79/79).**
- **Las 71 fuentes con conflicto solo de columna quedan así:**
  - 36 REVISADO;
  - 34 PENDIENTE: 22 por reexpresión ND, igual que en el contrafactual A2, y 12 porque R4 retira una reexpresión NA por igualdad;
  - 1 CONFLICTO: `aux:impuesto_2023`, por el artefacto de polaridad de R4.
- **Los 104:** en el commit R1 (`cambios_estado_a3_R1.json`, que se reproduce), las 104 filas pasan de CONFLICTO a 70 REVISADO y 34 PENDIENTE. El CSV queda en 239/243/29, **exactamente el contrafactual A2** (`s09`).

### A3-R2, R5 y casos reales citados

- **R2:** `Viscofan Configuración V6.4!B150` queda PENDIENTE (columna ND «sin línea de columnas»). Lo mismo ocurre con `Historia!E21` y con las dos `derechos_uso`.
- **R5, los 3 casos del año con coma:**
  - `Viscofan Historia!F6` → PENDIENTE;
  - `Historia!J21` → PENDIENTE;
  - `Vidrala Historia!G25` **sigue en CONFLICTO**: antes «imprime 2020,»; ahora «imprime 2020», tomado de la fila «At December 31 2020 1,303». El artefacto ha cambiado de forma.

### A3-R4: atajo y reexpresión (`s06_atajo_y_reexpresion.py`)

- **Atajo:** las 18 entradas quedan **PENDIENTE (18/18)**, con reexpresión ND «el valor aparece … pero no en una fila con el rótulo completo».
  - Las dos promociones `aux:AR2019_p11_derechos_uso_c_2018` (35) y `_nc_2018` (28) vuelven a PENDIENTE.
  - El código del atajo ya no se usa.
- **ND→NA, 9 casos** (`Historia!E8…K8`, `J23`, `K23`, `aux:amort_2019`): igualdad en una fila con el mismo rótulo («Amortisation and depreciation 6&7», «Final balance at 12/31»). La fila es correcta en la muestra.

### Muestra de los CONFLICTO de `0946971`: 15 fuentes + 1 M1, todos examinados con su fuente

| Grupo | Entradas | Fuente | ¿Contradicción real? |
|---|---|---|---|
| **Polaridad (R4)** | `Vidrala Historia!J6`, `J7`, `J8`, `aux:bai_2023`, `aux:impuesto_2023` | Declaran «sí: 2023 reexpresado sin (Vidrala) Italia (original 1,558,765 / 289,838 / 97,865 / BAI 287,493, CF_2023 p.4/7)». `CF_2023.txt` imprime exactamente esos originales, por ejemplo `Revenues 4 & 22 1,558,765 1,345,610` en la línea 129 | **No.** Es una reexpresión afirmada y documentada; el motivo publicado dice «declara no reexpresado ("sí: …")». J7 y bai_2023 eran REVISADO |
| **Año en el rótulo leído como importe y rótulo sin dígitos (R3 + R4)** | `Vidrala Historia!D25`, `E25`, `F25`, `G25`, `H25`, `aux:ing_fin_2017` | `CF_2017.txt:2179`, «At 31 December 2015 6,871 297 …», de la tabla de activos por impuesto diferido, se toma como fila de «At 31 December 2017» de la tabla de provisiones, y «2015» como importe. `CF_2019.txt:650`, «At December 31 2019 1,672». `CF_2017.txt:3461`, «Finance income 2017 2016», es la propia cabecera | **No.** Comparan con un año |
| **Valor no numérico en una línea de años (R3)** | `Viscofan Palancas!C48`, `Control maestro!H4` | El valor declarado es «EUR» y la cita es «Share price € 2025 2024 2023 2022 2021» / «(Thousands of euros) Notes 2025 2024». Mensaje: «el valor declarado EUR no está en la fila ['2025', …]» | **No.** Es un metadato de moneda |
| **Tabla de movimiento cuyas columnas no son años** (defecto 8 de A2; persiste) | `Vidrala Configuración V6.4!B46`, `B47`; M1 `Viscofan aux:CF2024_p9_pagos_acciones_2023` | `CF_2021.txt:2405`, «Additions (435) - (3.109) (546) - - (4,090)»: las columnas son clases de activo. `CA_2023_es.txt:2442`, «Share-based payment 0 0 1,581 1,581», del estado de cambios en el patrimonio | **No acreditada.** La fila del original es idéntica; se compara otra columna |

**Ninguno de los 19 CONFLICTO del CSV (15 fuentes + 4 derivados) descansa en una contradicción acreditada.**
- 13 de las 15 fuentes son **artefactos nuevos** de R3 y R4, que antes estaban en PENDIENTE o REVISADO, o que ya eran CONFLICTO por otro artefacto.
- Las 2 restantes, B46 y B47, son el defecto 8 de A2 sin corregir.
- `RESPUESTA_A3_CIERRE_V2.md` dice «PENDIENTE (o CONFLICTO si hay contradicción documentada)»; no es así para estas entradas.

### A3-R7 con datos reales (`s08_r7_control_negativo_real.py`, en copias aisladas)

La única cadena real con un operando derivado no piloto es `Vidrala Análisis!C41 = C37 × C55`, con C55 derivado del piloto.

**(a) Propagación.** Mutación: C55 deja de ser piloto y su origen `aux:acciones_propias_2025` pasa a CONFLICTO.
- `derivaciones.py` de `0946971` → C55 CONFLICTO, **C41 CONFLICTO**.
- El de `8b88fab` → C41 PENDIENTE: la propagación no llega.

**(b) Control.** Mutación: C55 pasa a CONFLICTO en DERIVADOS.json sin recalcular C41.
- `control_cobertura.py` de `0946971` → exit 1, con «derivado Vidrala Análisis!C41: estado_contextual PENDIENTE_CONTEXTUAL != propagacion de orígenes CONFLICTO_CONTEXTUAL».
- El de `8b88fab` → exit 1, pero **sin** ninguna violación sobre C41.

**Diferencia con lo publicado.** El control negativo del autor (`control_negativo.py` §10) prueba solo la función `estado_operando`, no que `control_cobertura` detecte la violación. El control con datos reales que faltaba es este.

## A3-R8 en detalle

**`ENTREGA.json`: no es la salida del generador.**
- Al ejecutar `generar_entrega_json.py` sobre las salidas publicadas sale un JSON con sangría 2. El publicado tiene sangría 4.
- Hay una diferencia de contenido: `pruebas[0].evidencia` publica `resultados/control_cobertura.json sha256 8e0a23a26e7c55a43ab45c3**56**8c2cda9d4c6216c47595d1bec3c091441100ba9`. La huella real, y la que el mismo archivo publica en `recuentos_generados.hashes`, es `…c3**55**8c2…`.
- El archivo se editó después de generarse, y la huella de la evidencia principal no corresponde al archivo.
- Las otras 6 huellas citadas y `recuentos_generados` sí coinciden: CSV `729ac235…`, jsonl `9cbbf2e4…`, cola `f6b752a4…`, negativo `fa827fc2…`, DERIVADOS `01935bf2…`, bloque2 `4450ef76…`.

**Campos desfasados en `ENTREGA.json`:**
- `base_revisada_sha` = `9d676ce…`; la base de A3 es `8b88fab`.
- `naturaleza` = «v4.0, corrección A2-R1..R5».
- La plantilla tiene todas sus claves; sobran `bloque` y `recuentos_generados`, que son inocuas.
- Las 4 pruebas tienen las claves de la plantilla.
- `es_plantilla=false`, `commit_entrega` según la plantilla, `apto_dinero_real` = «No se declara por este formulario», `integrado_en_producto=false`.

**Textos:**
- **Motivo de `aux:AR2025_p27_pagos_acciones_2024`.** Lo insertan `RESUMEN_PARA_CLAUDE.md` (bloque 1) y `PUNTO_DE_RECUPERACION.md` (v3.1) como texto fijo (`MOTIVO_OK`): «…la reexpresión queda OK por igualdad». En `0946971` esa reexpresión es **NO_DECIDIBLE**: «el valor aparece en CF_2024.txt pero no en una fila con el rótulo completo…». El texto «corregido» vuelve a ser falso para el estado vigente.
- **`HALLAZGOS.md` §10** (línea generada): «Derivados: 33 REVISADO / 50 PENDIENTE / 14 REUTILIZADO_M1..». Omite los **4 CONFLICTO** (33+50+14 = 97 ≠ 101) y tiene doble punto. La línea está además en el apartado histórico «A-R1», a continuación de los totales v3 (282/229/0 CONFLICTO).
- **`RESUMEN_PARA_CLAUDE.md:20`:** cifras correctas (209/283/19) bajo un rótulo que sigue diciendo «tras … v3.2/v3.3».
- **`cola_pendientes.py`:** el docstring dice «en v4.0 son 26, no 46»; la salida vigente da 50.
- **`RESPUESTA_A3_CIERRE_V2.md`:**
  - «las que pierden acreditación quedan PENDIENTE (o CONFLICTO si hay contradicción documentada)» no se cumple (J7, bai_2023);
  - R5, «3 CONFLICTO de "2020," ya reparados en R3»: G25 sigue en CONFLICTO.
- **`actualizar_textos_resumen.py`** reemplaza anclas fijas por textos fijos. Al ejecutarlo de nuevo sale con código 1 («ANCLA NO ENCONTRADA»). No regenera los textos desde las salidas; solo los parcheó una vez.

**pypdf: mensaje claro, versión mínima no establecida.**
- Con 6.17.0, código 1 y el mensaje «pypdf 6.17.0 no pudo leer CF_2021.pdf (PdfReadError …). Use pypdf >= 7.0 (probado con 7.1.0)…».
- La guarda sigue en `>= 6.0`, y `COMANDOS.md:3` dice «exige pypdf >= 6.0».
- El «>= 7.0» del mensaje no está probado: solo se ha probado 7.1.0.
- La excepción captura cualquier error de lectura y lo atribuye a la versión.

**El resto de A3-R8:**
- **`-I`:** `cola_pendientes.py` y `resolver_bloque2.py` funcionan con `python3 -I -B` y sus salidas son IGUALES. **Cumple.**
- **Sondas A2:** se publican en `sondas_a3/sondas_informe/` s00–s10, idénticas byte a byte a las de `<rev_A2>/sondas`. **Cumple.**
- **Un commit por punto:** 8 commits, y cada intermedio reproduce sus salidas. El de R2 incluye un ajuste del código de R1, y lo declara. **Cumple.**

## Higiene (`s10_higiene.sh`, `s11_plantilla.py`)

- **Manifiesto:** `sha256sum -c` desde la raíz de la carpeta → código 0, **196/196 OK**. Cubre todos los archivos salvo el propio manifiesto.
- **`git diff --name-only 8b88fab 0946971`:**
  - 181 archivos, todos en `resultados_m2/cobertura_vm/`;
  - 0 binarios;
  - 0 `.pdf`, `.xlsx`, `.zip`, `.pyc`, `__pycache__` o `.trabajo/`.
  - El árbol de `0946971` tiene 0 PDF, XLSX, ZIP o pyc.
- **Secretos:** 0. El único acierto del patrón es la propia expresión regular de `s10_higiene.sh` de A2, publicada.
- **Rutas absolutas del entorno del autor** en las salidas publicadas: `/workspace/wt-a/…` en `sondas_a3/out/*.json` y `inventario.json`, y `/tmp/pylibs6`, `/tmp/_s10`, `/tmp/s02.json` en los comandos. Es menor, pero A2 tenía 0.
- **`ENTREGA.json` frente a la plantilla:** véase A3-R8.

## Defectos que quedan, con su contraejemplo mínimo

1. **R2 · desempate por proximidad: OK falsos nuevos** (`find_header_block`, `>=`, fusión en `row_idx-3`).
   - `Notes 2025 2024` / `* 2024 and 2025 figures restated` / `Revenue 10.000 9.000`, declarado 2024 = 10.000 → OK (en `8b88fab`, CONFLICTO).
   - `2025` / `2024` / 2 líneas / `Goodwill 1.500 -`, declarado 2024 = 1.500 → OK.
   - Inverso: la cabecera real «EQUITY AND LIABILITIES Note 2025 2024» se descarta. 61 OK reales dependen del título.
2. **R4 · polaridad que invierte afirmaciones.** «sí: 2024 reexpresado sin la filial vendida» + diferencia → CONFLICTO «declara no reexpresado». **5 reales:** J6, J7, J8, aux:bai_2023 y aux:impuesto_2023; J7 y bai_2023 eran REVISADO.
3. **R4 · negación no reconocida.** «None of the comparative figures were restated» o «reexpresión: ninguna» + diferencia → OK «reexpresión confirmada» (en `8b88fab`, ND).
4. **R3/R4 · años sin puntuar como importes y rótulo sin dígitos.**
   - Original `2024 2023` / `At 31 December 2023 5.000`; cita `At 31 December 2024 6.000`, «no» → CONFLICTO «imprime 2023 en la columna 2024».
   - **6 reales:** D25, E25, F25, G25, H25 y aux:ing_fin_2017.
5. **R3 · valor no numérico comparado por posición en una línea de años.** Cita `Share price € 2025 2024 2023`, valor «EUR» → CONFLICTO. **2 reales:** Palancas!C48 y Control maestro!H4.
6. **R4 · perímetro y escala por página, no por tabla.**
   - Página con la tabla consolidada (10.000) y la individual (9.000); cita 9.000, consolidado → NO_APLICA «coherente».
   - «(in millions)» en la página anterior → NO_APLICA. Sin caso real localizado.
7. **R4 / defecto 8 de A2 · tablas de movimiento cuyas columnas no son años.** `Additions (435) - (3.109) …` → CONFLICTO. Persisten B46, B47 y el M1 CF2024_p9.
8. **R1 · signo no reconocido y cero inicial.** `–7.660` (U+2013) y `0,21` → CONFLICTO, cuando en `8b88fab` daban OK. 0 reales.
9. **R5 · versión.**
   - Un «2025» sin puntuar en la página acredita la versión (`Number of employees 2025 1980` → OK).
   - «December 31, 2025,» solo en el título → CONFLICTO.
   - 0 reales.
10. **R6 · abreviaturas de millones.** «Cifras en millones», «(€m)», «MEUR» y «(M€)» → OK por la cabecera. 0 reales.
11. **R8 · `ENTREGA.json`.** Huella de `control_cobertura.json` con un dígito cambiado (`…3568…` frente a `…3558…`), archivo editado tras generarse, y `base_revisada_sha`/`naturaleza` desfasados.
12. **R8 · textos.**
    - Motivo de AR2025_p27 «OK por igualdad», falso en `0946971` (es ND), en RESUMEN y PUNTO.
    - HALLAZGOS omite los 4 derivados en CONFLICTO.
    - El docstring de `cola_pendientes` dice 26 (son 50).
    - RESPUESTA hace afirmaciones sobre los CONFLICTO y G25 que no se cumplen.
    - `actualizar_textos_resumen.py` no se puede volver a ejecutar.
13. **R8 · pypdf.** La guarda sigue en `>= 6.0` frente al «>= 7.0» del mensaje; no hay versión mínima probada.
14. **R7 (latente, mitigado).** `estado_operando` devuelve REVISADO ante un ciclo («CICLO») o un operando inexistente. `control_cobertura` falla en ambos casos.

## Lo que se conserva

- **Reproducción:**
  - 192/196 archivos byte a byte, y las 4 diferencias explicadas;
  - 7/7 commits intermedios coherentes con su código;
  - listas por punto regenerables.
- **Control:** PASS con código 0. Negativos 219, bilaterales 15/15 y d375d80 5/5 CONFLICTO.
- **Sondas de la revisión A2:** todas las de la lista de cierre dan el estado esperado (1b–1d, 2a–2g, 3a–3j, 4a–4g, R1a–R1e, R2a–R2f, R3a–R3c, R4a–R4c).
- **A3-R1:** los 79 de columna dan OK y los 104 cumplen el contrafactual.
- **A3-R4:** el atajo de las 18 queda retirado y las dos promociones 28/35 vuelven a PENDIENTE.
- **A3-R7:** la propagación transitiva queda comprobada con datos reales.
- **Datos:** 0 REVISADO sin todas sus dimensiones.
- **Higiene:** manifiesto y diff limpios de binarios y secretos.

## Archivos de esta revisión

**Sondas y salidas** en `<rev_A3>/sondas/` (ver `SHA256SUMS.txt`):
- `s00_preparar_copia.py/.out`: copia aislada e insumos (251/251).
- `s01_reproducir.sh/.out`: pipeline completo con `-I -B` y comparación byte a byte.
- `s01c_commits_intermedios.sh/.out`: los 7 commits intermedios frente a sus propias salidas.
- `s01d_cambios_por_punto.sh/.out`: listas `cambios_estado_a3_R1…R7` regeneradas.
- `s02_sondas_revisor_A.py`, `s03_sondas_d375d80_A.py`, `s07_sondas_nuevas_A2.py` (copias de A2) y sus salidas `*_0946971.json/.out`.
- `s04_cambios_estado.py/.json/.out`: estados por fuentes, CSV y dimensión; regla REVISADO; CONFLICTO vigentes.
- `s05_seguimiento_signo.py/.json/.out`: los 79 y las 71.
- `s06_atajo_y_reexpresion.py/.json/.out`: las 18 del atajo y los motivos de reexpresión.
- `s07_sondas_nuevas_A3.py/.json/.out` y `s07_sondas_nuevas_A3_sobre_8b88fab.json/.out`: variantes nuevas sobre los dos commits.
- `s08_r7_control_negativo_real.py/.json/.out`: control negativo de R7 con datos reales.
- `s10_higiene.sh/.out`, `s11_plantilla.py/.out`, `PLANTILLA_ENTREGA.json` (copia de la rama de coordinación) y `s12_pypdf.out`.

Las salidas `.out` y `.json` conservan las rutas originales del entorno, sin sustituir, como en las revisiones anteriores.

**Copias:**
- `<rev_A3>/entrega` (`0946971`, sin modificar);
- `<rev_A3>/repro` (reproducción);
- `<rev_A3>/commits/<sha>` (commits intermedios);
- `<rev_A3>/r7neg/` (mutaciones de R7).
