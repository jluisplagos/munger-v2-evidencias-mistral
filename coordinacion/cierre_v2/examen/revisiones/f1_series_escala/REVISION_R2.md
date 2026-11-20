# Revisión independiente · `f1/series-escala`, ronda 2 (última)

- **Revisado:** `7be4665` (código y pruebas `6ae2a60`) frente a mi ronda 1 (`REVISION.md`, sobre `b3998a8`).
- **Revisor:** el mismo agente de la ronda 1, distinto del autor. 18-nov-2026. No modifiqué la rama ni hice commit.
- **Copia:** `git archive 7be4665` con los 1008 binarios de la base 4.14 y los 51 del examen (huellas del manifiesto), en
  `/home/user/e_work/rev_series2_copia`; worktree `/home/user/e_work/wt_rev_series2`. Las borré al terminar.
- **Evidencia:** `evidencia_r2/` (sondas, escaneo de páginas reales, salidas de las baterías, arreglo propuesto).

## Veredicto: **CONFORME CON LÍMITES**

Las tres correcciones están hechas y funcionan: mis sondas de la ronda 1 dan ahora el resultado correcto, no hay regresiones y la fusión
con `f1/usgaap` está limpia salvo el manifiesto. Queda un límite en el contraste de la escala, que mira la **página** y no la **tabla**: en
dos casos que construí da un falso «comprobado» con una cifra mil veces menor. Lo pongo como límite y no como corrección porque en los
dos expedientes reales que escaneé (Jumbo y Ahold) no se produce. Hay que arreglar el patrón de «unidades» (dos líneas, probado) y
documentar el límite antes de usar una escala distinta de millones en otro expediente.

## 1. Sondas de la ronda 1 contra `7be4665`

| Sonda | Ronda 1 (`b3998a8`) | Ronda 2 (`7be4665`) |
|---|---|---|
| S1 · página «(EUR million)», declarado «miles» (−0,45) | no salta, comprobada | **DATOS INVÁLIDOS** («la página declara ['millones']») |
| S1b · misma, declarado «unidades» (−0,00045) | no salta, comprobada | **DATOS INVÁLIDOS** |
| S3 · guion de la etiqueta («Finance lease - principal») como cero de 2024 | no salta, comprobada | **DATOS INVÁLIDOS** |
| S4 / S4b · «- 7» / «- 5» como cero | no salta, comprobada | **DATOS INVÁLIDOS** |
| S10 · «—» real en la columna de 2023 | comprobada | comprobada (sin cambio) |
| Jumbo «(amounts in Euro)», «unidades» | comprobada | comprobada |
| 10-K «(in millions, except per share data)», «millones» | comprobada | comprobada |

## 2. Contraste de la escala: ¿falsos «comprobado»?

`_escala_de_pagina` busca las marcas en **todo el texto de la página**. Si encuentra una sola escala y es la declarada, la escala se da por
comprobada; si encuentra otra, DATOS INVÁLIDOS; si encuentra varias o ninguna, PENDIENTE. Sondas nuevas (`sondas_r2.py`):

| Sonda | Resultado | Juicio |
|---|---|---|
| R1 · página de continuación: la tabla de la ROU va en millones (su encabezado quedó en la página anterior) y debajo hay otra tabla «(in thousands)»; se declara «miles» con `valor_fuente` −0,45 | **no salta, comprobada** | **falso comprobado (límite 1)**: el encabezado es de otra tabla |
| R2 · «All amounts in euros (thousands)»; se declara «unidades» con `valor_fuente` 1000 veces menor | **no salta, comprobada** | **falso comprobado (límite 2)**: el patrón de «unidades» no excluye «(thousands)» |
| R2b · misma página, se declara «miles» (lo correcto) | DATOS INVÁLIDOS | falso rechazo (falla cerrado) por la misma causa |
| R3 · prosa «customers in millions of households» y tabla sin encabezado | la cuenta como «millones» | la prosa puede servir de encabezado; aquí no abre un error a la baja |
| R4 · «expressed in euros» en la prosa y «€000» en la tabla | PENDIENTE (dos escalas) | correcto, falla cerrado |
| R7 / R8 · sin campo `escala` | sin contraste (como antes) | R8 (página «(amounts in Euro)» con la cifra tomada como millones) no lo frena F1-SERIES; lo frena V-F1e (ROU > D&A total) |

**Escaneo de textos reales** (`escaneo_escalas_paginas_reales.txt`, `marcas_ajenas_ahold_2025.txt`):
- Jumbo FY2022–FY2025: todas las páginas con marca dan solo «unidades». Sin conflictos.
- Ahold 2024–2025, publicado en millones: unas 10 páginas por informe tienen varias escalas, y por tanto PENDIENTE. En 2025 hay 8 páginas
  donde solo aparece una escala que no es millones: las de remuneración («€ thousand», lo correcto) y las que llevan «(€)» como columna de
  un precio por acción o la frase «the euro (€) against the U.S. dollar» en la prosa. Ninguna de estas es una página de D&A o de
  arrendamientos, pero muestran que una marca ajena puede ser la única de la página.

**Límite 1 (página, no tabla).** Con la marca de otra tabla y sin la de la propia, una escala menor queda comprobada. Para cerrarlo,
habría que buscar el encabezado solo entre las líneas de la tabla de la cifra, por encima de su `fila`, hasta el encabezado de ejercicios
o una línea en blanco doble. Si no se hace, conviene que el detalle diga «escala comprobada en la página, no en la tabla» y añadirlo al
§10 del README.

**Límite 2 (patrón de «unidades»).** El lookahead negativo no admite un paréntesis delante de «thousands», «millions» o «'000».
*Arreglo probado en una copia* (`arreglo_r2_patron_unidades.diff`): cambiar `(?!\s?(?:m\b|…))` por `(?!\s?\(?\s?(?:m\b|…))`. Con él, R2 y
R2b quedan PENDIENTES (fallan cerrados) y la batería sigue en **74/74**. Conviene añadir también `\(\s*thousands?\s*\)` y
`\(\s*millions?\s*\)` a sus escalas, y R1 y R2 a la batería como mutaciones.

**Detalle menor.** Cuando la escala queda PENDIENTE, el código no hace `continue`: el mismo año suma a la vez en `columna_pendiente` y en
`columna_comprobada` si la columna se alinea («columna comprobada en 1 años, PENDIENTE en 1» para un solo año). No cambia el estado,
pero confunde al lector.

## 3. `F1-SERIES-CERO` y Jumbo

- `F1-SERIES-CERO` es un AVISO aparte, en estado PENDIENTE, con el motivo y la cita de cada año. `Guardas.bloquean()` solo cuenta
  BLOQUEA, así que el aviso no cambia el estado. La ficha lo pone en sus avisos (`ficha.py`, AVISO/INFORMA) y `motor_a_f1_resultado.md`
  en la tabla de guardas. Correcto.
- Jumbo (`motor_a_f1.json`, `comparacion_jumbo_r2.json`): la ROU de 2021–2025 sigue igual. La escala «unidades» queda comprobada en sus
  cuatro páginas y la columna sigue PENDIENTE por las 4 líneas «- Additions». La PPA de 2021–2024 vuelve a estar sin `literal`
  (INCOMPLETO). La de 2025 lleva `cero_comprobado` con la frase de AR2025 p. 189 y queda como F1-SERIES-CERO PENDIENTE. F1-SERIES da AVISO
  INCOMPLETO porque ya bloquean F1-K3a y F1-LIBRO. El estado sigue en `pendiente_de_datos` en los tres casos. Es lo que pedí en la ronda 1.
  Sigue en pie mi nota sobre 2025: la frase solo cubre la combinación HERALD 2. Que ningún intangible venga de combinaciones anteriores,
  y que la revalorización inmaterial del inmueble no cuente, lo tiene que confirmar el revisor.

## 4. Regresiones y baterías

- Las 9 declaraciones con series del paquete dan el mismo F1-SERIES y la misma `leer_serie` frente a `1a7a6c6` y frente a `b3998a8`
  (`comparar_decl_*.txt`: 0 distintas).
- Copia limpia nueva: `verificar_paquete.sh rapida` da **RESULTADO GLOBAL: PASA** (8723 archivos en el manifiesto, 0 modificados, 0
  ausentes, 0 de más; F1-SERIES 74/74). Después, en la misma copia: `test_f1_series_escala` 74/74, `test_motor_a_f1` 163/163, `test_v631_f1`
  28/28, `probar_v631_f1.py estructura` 21/21 y `prueba_pipeline_f1.py` 7/7 (LibreOffice, con `flock`). No repetí `probar_v631_f1 a0/f1` ni
  `prueba_pipeline_v631`: la ronda 2 no toca el libro ni el pipeline, y en la ronda 1 pasaron (22/22, 35/35, 9/9).
- **Fusión con `origin/f1/usgaap` (`bcb6dc3`):** `git merge-tree` da un solo conflicto, en `MANIFIESTO_SHA256.txt`. Árbol fusionado
  (código, pruebas y prompts sobre la copia limpia): 74/74, 163/163, US GAAP 246/246 y V6.3.1 29/29. Coincide con lo que dice el autor.

## Qué queda

1. Aplicar el arreglo del patrón de «unidades» (límite 2) y añadir R1 y R2 a la batería.
2. Documentar que la escala se contrasta en la página y no en la tabla (límite 1), o acotar la búsqueda a la tabla.
3. Opcional: no contar en `columna_comprobada` un año cuya escala quedó PENDIENTE.

No comprobé Excel real, `verificar_paquete.sh completa` ni el árbol fusionado con LibreOffice.
