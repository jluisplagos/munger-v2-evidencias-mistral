# Revisión independiente · frente D (Mistral D) · respuesta a la corrección D3 · bloques A `328fa31` y B `c734ca1`

- **Revisor:** subagente Claude, en un contexto distinto del autor (Mistral D). No he escrito este material ni las revisiones anteriores.
- **Fecha:** 2026-11-17 (última consulta del remoto a las 14:41 UTC: la rama sigue en `c734ca1`).
- **Objeto:** `origin/mistral/d-qwen-aceptacion`, de `d032691` a `c734ca1`: `328fa31` (13:25:45 UTC, «bloque A: R1/R2/R7») y `c734ca1` (13:30:36 UTC, «bloque B: R3/R5»). Carpeta `resultados_qwen/ejecucion_d/`.
- **Encargo de referencia** (`origin/coordinacion/cierre-v2`): `CORRECCION_D3.md` (sha256 `f9d95a98…`), `ESTADO_D3_TRAS_d032691.md` (`3b6fbb64…`), `REANUDAR_MISTRAL_20261117.md` bloque 1, `MECANISMO_PERSONAJE.md`, el banco `4745f38` (manifiesto 57/57) y el contraste `munger-d-relevos-002`.
- **Método:**
  - `git worktree add --detach <rev_D3>/wt c734ca1`; todo se ejecuta sobre copias de esa carpeta bajo `<rev_D3>/trabajo/`. El worktree queda limpio.
  - **Producto real**, a diferencia de las dos revisiones anteriores: clon local propio del producto en `957af65` (`<rev_D3>/cand_957af65`) con los 1008 binarios copiados de la candidata materializada; su `MANIFIESTO_SHA256.txt` da 7762/7762. Sobre él he reejecutado las 30 especificaciones y `pruebas_arnes.py`.
  - **Stubs** para medir la lógica del arnés: las sondas de las dos revisiones anteriores, sin cambios, y una sonda nueva (`s02`).
  - No he ejecutado LibreOffice, agentes ni el pipeline. Los comandos del producto que lanza el arnés no invocan LibreOffice (comprobado por lectura). Sin red, salvo `git fetch`.
  - Sin commit ni push. En el repositorio auxiliar solo quedan el registro del worktree pedido y los `git fetch`. No he escrito en el producto ni en la candidata compartida: sobre ella solo he lanzado un caso en lectura (0 cambios y 0 archivos nuevos después).
  - Todo se reproduce con `bash sondas/comprobaciones_d4.sh <aux> <rev_D3> <cand957> [<candidata>]` (código 0; registro en `sondas/comprobaciones_d4.log`).

## Contexto que condiciona la lectura

- **La respuesta es parcial.** Solo hay bloques A y B. No hay bloque para R4 ni para R8, ni `RESPUESTA_D3`. `ENTREGA.json`, `PUNTO_DE_RECUPERACION.md`, README, HALLAZGOS, RESUMEN, RELEVO_SUPERVISADO, CONFIGURACION, el manifiesto y `pruebas_arnes.log` siguen siendo los de `d032691` (09:59 UTC): describen el arnés v3 y la respuesta a D2 sobre `1ac661b`.
- **`pruebas_arnes.py` ya contiene una prueba 36 de D3-R4** (relevos completos) que falla sobre lo publicado. Indica que el trabajo quedó a medias, no que se diera por hecho.
- **La candidata ha cambiado.** El worktree `<candidata>` está en `b129b36` (`3149128` más G-RAIZ; `CONTROL.json` @ `5f5f471` lo confirma), no en `3149128`. Entre `957af65` y `b129b36` no cambia ningún archivo de `personaje_v2/scripts`. El arnés y la evidencia publicada siguen fijados a `957af65`.
- **Son 30 especificaciones, no 28.** Los documentos caducados repiten «28» (4 archivos); en disco hay 30 y 30 resultados, igual que en `1ac661b`.

## Dictamen

**No aceptable como cierre de D3: correcciones materiales. D-HARNESS y D-36 siguen sin aceptar.**

Lo que el autor afirma en los dos commits se reproduce casi entero, y la evidencia v4 es real: la he reproducido byte a byte con el producto. Pero la prioridad del encargo (R4) no se ha tocado, quedan otros cuatro hallazgos materiales (H2 a H5), el manifiesto ha vuelto a romperse y las pruebas del propio autor no llegan a ejecutarse.

| D3-R | Veredicto | En una línea |
|---|---|---|
| **R1** rutas, aserciones, id, candidata | **ABIERTO** | Las 16 variantes anteriores, cerradas. Pero las aserciones siguen pudiendo leer lo que escribe el arnés por cinco vías nuevas (COMPONENTE_OK y CUMPLE en la matriz), y dos alteraciones ocultas de la candidata pasan |
| **R2** controles negativos | **ABIERTO** | C4 fuera del cómputo, Q1-034 C1 sobre su paso y las 9 líneas de Q1-026: hechos. La prueba 34 «contra el estado previo» no puede fallar; Q1-017 da CUMPLE sin ningún paso del caso; el «bloqueo de entorno» de Q1-026 no es de entorno |
| **R3** regeneración | **ABIERTO** (evidencia y derivados: CERRADO) | Evidencia v4, MATRIZ, MAPA, relevo y recuentos: reproducidos byte a byte. Documentos y log, sin regenerar. Q1-026 se clasifica BLOQUEO_ENTORNO con cualquier ERROR_ENTORNO y con las herramientas presentes |
| **R4** relevos | **ABIERTO · NO TRATADO** | `generar_relevo.py` no cambia desde `5f4b2a2`. 0 de 36 paquetes con estado inicial, fases, entrada o artefacto por criterio. Q1-028 y Q1-032 siguen con `comando_relevo` null |
| **R5** `preserva_sentido` y MAPA | **ABIERTO** (mejora) | 36 justificaciones distintas y 5 filas corregidas. Siguen sobredeclaradas Q1-034#0 y Q1-025#0 (señaladas en D3) y, en mi auditoría de las 54 filas, 13 no observan su criterio |
| **R6** manifiesto | **ABIERTO · REGRESIÓN** | Estaba cerrado en `d032691`. En `c734ca1`: código 1, 106 de 204 fallan |
| **R7** (menor) | **ABIERTO** (3 de 4 puntos corregidos) | Marcas y aviso de evidencias: corregidos y comprobados. Sigue el `KeyError 'good'`. Las pruebas 16 y 35, que debían acreditarlo, no funcionan |
| **R8** entrega por bloque | **ABIERTO · NO TRATADO** | `ENTREGA.json` sigue con base `1ac661b` y «respuesta D2». No hay entrega de los bloques A ni B |

**¿Puede el coordinador ejecutar ya los casos del personaje con este paquete? No: 0 de 36.** Detalle en la sección «Ejecución de los casos del personaje».

## Comandos ejecutados (todos sobre copias)

| Comando | Código | Resultado |
|---|---|---|
| `git fetch origin mistral/d-qwen-aceptacion coordinacion/cierre-v2` | 0 | `c734ca1`; coordinación `fcbf345` al empezar y `5f5f471` al terminar (los documentos del encargo no cambian) |
| `cd resultados_qwen/ejecucion_d && sha256sum -c MANIFIESTO_SHA256.txt` | **1** | 98 OK, **106 FAILED**; 204 entradas para 204 archivos |
| `generar_matriz.py`, `generar_correspondencia.py`, `generar_relevo.py` sobre la evidencia publicada | 0, 0, 0 | `cmp` 0 en MATRIZ, MAPA, PAQUETES_RELEVO y recuentos |
| `sondas_arnes_d3.py` y `sondas_arnes_d2.py` de las revisiones anteriores, sin cambios | 0, 0 | `s01`, `s01b` |
| `sondas/sondas_d2.py` del autor | 0 | 10 DETECTA y 1 OK (`s11`) |
| `python3 -B scripts/pruebas_arnes.py` (producto real `957af65`) | **1** | 3 PASA y `FileExistsError` en la prueba 4 (`s03`) |
| ídem con 4 parches mínimos del revisor al propio guion de pruebas | **1** | 33 PASA, la 16 FALLA, `FileNotFoundError` en la 35, la 36 no llega (`s04`) |
| ídem sobre el arnés mutado (sin contención de rutas; Q1-027 C4 sin marca) | 1 | las pruebas 17, 18, 19, 20 y 34 siguen en PASA (`s05`) |
| `bash scripts/ejecutar_todo.sh` (producto real, sin pdftotext ni soffice en el PATH) | 0 | 30 COMPONENTE_OK; 29 CUMPLE, 1 BLOQUEO_ENTORNO, 6 NO_EJECUTADO (`s06`) |
| ídem con pdftotext y soffice en el PATH | 0 | idéntico, también el stderr de Q1-026 (`s06`) |
| `fase1_historia.py construir` sobre el origen de Q1-026 y sobre 4 expedientes de la 4.14 | 1; 0, 0, 0, 0 | `s08` |
| Q1-026 publicado con `PLANTILLA_EXP` = Viscofan 4.14 | 1 | `cambiar_base.py preparar` da **0**; la especificación esperaba 1 (`s08b`) |
| `s02_sondas_arnes_d4.py`, `s09`, `s10`, `s12`, `s13` | 0 | sondas nuevas |
| A1 y A2 de `s02` con el producto real (`s16`) | 0, 0 | COMPONENTE_OK en las dos |

---

## D3-R1 · Invariantes del arnés — ABIERTO

### Las 16 variantes de D3 y de `ESTADO_D3`: cerradas

Reproducidas con la sonda de la revisión anterior, sin tocarla (`s01`; sha256 `b61d927f…`), contra `c734ca1`. Coincide con lo que afirma el commit `328fa31`.

| Invariante | Variante | `d032691` | `c734ca1` | Estado | Dónde se cierra |
|---|---|---|---|---|---|
| 1 rutas | P3va `copiar_artefacto ../../Q1-036/…` | COMPONENTE_OK | exit 1, ERROR | CERRADO | `lib_arnes.py:216` |
| | P3vb `guardar="../Q1-036/…"` | pisa Q1-036 | víctima intacta | CERRADO | `lib_arnes.py:174-180` |
| | N1a `escribir_fuente` con `../` | pisa el registro ajeno | registro intacto | CERRADO | `ejecutar_caso.py:150-155` |
| | N1b `copiar_artefacto` con ruta absoluta | COMPONENTE_OK | exit 1, ERROR | CERRADO | `lib_arnes.py:75-84` |
| 2 matriz | M2 resultado de 4 campos | CUMPLE | ERROR (COMPONENTE_OK), sin CUMPLE | CERRADO | `generar_matriz.py:67-89, 127-137` |
| | N2a salidas vaciadas | CUMPLE | sin CUMPLE | CERRADO | ídem |
| | N2b candidata de ceros, banco ajeno, harness 2.0 | CUMPLE | sin CUMPLE | CERRADO | `generar_matriz.py:128-133` |
| 3 aserciones | P1v sobre `ejecucion.log` | COMPONENTE_OK | exit 1, ERROR | CERRADO | `ejecutar_caso.py:62-65` |
| | N3 `run:` sobre la fuente del arnés | COMPONENTE_OK | exit 1, ERROR | CERRADO | `ejecutar_caso.py:55-57` |
| 4 id | P9w `"."`, N4 `"../fuera"`, N4b `""` | borran evidencia | exit 2 sin borrar | CERRADO | `ejecutar_caso.py:288-291`, `lib_arnes.py:87-93` |
| 5 candidata | P8va skip-worktree, N5a assume-unchanged | COMPONENTE_OK | exit 2, ERROR_ENTORNO | CERRADO | `lib_arnes.py:115-118` |
| | P8vb no rastreado, N5b oculto por `info/exclude` | COMPONENTE_OK | exit 2, ERROR_ENTORNO | CERRADO | `lib_arnes.py:120-131` |

**Estado por invariante, contando las variantes nuevas de abajo:**

| Invariante | Estado | Qué queda |
|---|---|---|
| 1 · toda ruta dentro del caso | CERRADO_CON_LIMITES | `entrada.fuente.archivo` y los `args` no se validan; el producto real rechaza la fuente ajena |
| 2 · la matriz reevalúa | CERRADO_CON_LIMITES | ignora `EVIDENCIAS_DIR`; ERROR_ENTORNO pasa sin validar a BLOQUEO_ENTORNO (R3) |
| 3 · las aserciones no leen archivos del arnés | **ABIERTO** | A1 a A5 |
| 4 · id validado antes de tocar el disco | CERRADO_CON_LIMITES | ids con salto de línea, no ASCII o ajenos al banco; id distinto del archivo |
| 5 · candidata limpia | **ABIERTO** (menor) | D1 y D2 |

- La matriz vuelve a evaluar de verdad: además de exigir `harness 4.0`, huella de la especificación, candidata y banco, reaplica cada aserción a los archivos de evidencia.
- `ejecutar_todo.sh` sigue sustituyendo un resultado forjado.

### Variantes nuevas: el invariante 3 sigue abierto (material)

La prueba de cierre de D3 dice: «Las aserciones no pueden leer archivos que escribe el propio arnés». La v4 lo aplica con una lista de nombres (`archivos_producto`), y esa lista se puede llenar con contenido del arnés. Sonda `s02`, con un producto de juguete que **no lee el registro** y cuya salida es constante:

| Variante | Especificación mínima | Arnés | Matriz v4 |
|---|---|---|---|
| **A1** | `escribir_fuente` «precio histórico 14,20…; capitalización 710» y después `copiar_artefacto archivo="fuentes_sinteticas/f6_031_precio.txt"`; aserciones sobre la copia | exit 0, **COMPONENTE_OK** | **PARCIAL_COMPONENTE / CUMPLE** |
| **A2** | `entrada aux:litigio` (hipótesis, «0-200») y `copiar_artefacto archivo="verificacion_entradas.json"`; aserción sobre el registro copiado | exit 0, **COMPONENTE_OK** | **CUMPLE** |
| **A3** | `informe --provisional`, después `mutar_fuente archivo="informe_provisional.md"` con «4 verificadas / 1 pendiente / 5 total» y `copiar_artefacto` | exit 0, **COMPONENTE_OK** | **CUMPLE** |
| **A4** | `comprobar` con `guardar="ejecucion.log"` y `escribir_fuente` con un nombre que lleva el texto buscado | exit 0, **COMPONENTE_OK** | **CUMPLE** |
| **A5** | Q1-026 con `guardar="origen_estado.txt"` y aserción `intacto=true`; el producto falla por un motivo ajeno («CAMBIO inválido») | exit 0, **COMPONENTE_OK** | **BLOQUEO_ENTORNO** |

**A1 y A2, repetidas con el producto real `957af65` (`s16`): exit 0, COMPONENTE_OK.** El único comando del producto que se ejecuta es `plantilla`; los «archivos del producto» según el arnés son la fuente y el registro que él mismo escribió.

Causas, todas en `c734ca1`:
- `copiar_artefacto` acepta cualquier archivo del expediente, también los que escriben `escribir_fuente`, `poner_entrada` o `mutar_fuente`. Solo pide que el último paso registrado no fallara, y ese paso puede ser el `plantilla` inicial (`lib_arnes.py:214-240`).
- `mutar_fuente` escribe en cualquier ruta del expediente, no solo en `fuentes_sinteticas/` (`ejecutar_caso.py:194-203`).
- `_guardar` admite los nombres del propio arnés y los añade a la lista (`lib_arnes.py:174-184`); `preparar_cambio` escribe después `origen_estado.txt` y `errores_bloqueo.json` con ese mismo nombre (`ejecutar_caso.py:259-281`).
- La matriz reconstruye la lista de permitidos con lo que declaran el resultado y la especificación (`generar_matriz.py:70-76`); nada de eso acredita el origen, así que certifica los cinco.

Alcance: **ninguna de las 30 especificaciones publicadas usa estas vías** (`copiar_artefacto` solo aparece en Q1-036, sobre la ficha y el informe; `mutar_fuente` solo en Q1-027, sobre su fuente). No afecta a los 29 CUMPLE publicados. Sí afecta a la garantía del arnés, que es lo que D3 pedía, y a las especificaciones que falten por escribir.

### Variantes nuevas: candidata limpia (menor, como en D3)

| Variante | Qué se hace | Resultado |
|---|---|---|
| **D1** | script rastreado alterado con `--assume-unchanged` **y** `--skip-worktree` | `git ls-files -v` muestra `s`; `lib_arnes.py:116` solo mira `h` y `S`. exit 0, **COMPONENTE_OK** con la salida alterada |
| **D2** | enlace no rastreado a un directorio, `scripts/ast -> <fuera>/`, oculto por `.git/info/exclude`. Suplanta el módulo `ast`, que el script de juguete importa igual que el `verificacion_entradas.py` real (línea 86) | `os.walk` no entra en enlaces a directorios (`lib_arnes.py:125`). exit 0, **COMPONENTE_OK** con la salida alterada |

En ambas la aserción solo se cumple porque la candidata está alterada. Los cuatro controles (skip-worktree, assume-unchanged, no rastreado, exclude) dan ERROR_ENTORNO con la misma sonda.

### Límites menores de los otros invariantes

- **Rutas.** `entrada.fuente.archivo` no se valida: el arnés calcula la huella de un archivo de otro caso o de una ruta absoluta y la escribe en el registro sin error (`ejecutar_caso.py:175-176`; B1a y B1b). **El producto real sí lo rechaza** («la fuente local … no está en el expediente ni en el paquete», COMPONENTE_FALLA), así que hoy no da un falso CUMPLE. Los `args` de `ficha` e `informe` pasan sin validar (`ejecutar_caso.py:349, 352`; `ficha.py` admite `--config RUTA`).
- **Id.** `re.match` con `$` y `\d` acepta `"Q1-001\n"`, dígitos no ASCII y `Q1-999`. Se crea la carpeta y el caso termina con una traza `StopIteration` sin resultado (`lib_arnes.py:40`, `ejecutar_caso.py:211`). Una especificación con el id de otro caso borra la evidencia de ese caso (C3).
- **Matriz.** `generar_matriz.py:27` ignora `EVIDENCIAS_DIR`, que el README documenta como variable. Tras reejecutar un caso con `EVIDENCIAS_DIR` propio (COMPONENTE_FALLA), la matriz sigue mostrando el CUMPLE publicado (E3).
- **Una ejecución fallida borra la evidencia publicada del caso.** Ocurrió: ver «Bloque A por separado».

## D3-R2 · Controles negativos — ABIERTO

**Hecho y comprobado:**
- Q1-027 C4 queda `OBSERVACION_NO_DISCRIMINANTE`, fuera del cómputo, y ya no figura en el MAPA (`ejecutar_caso.py:378-381, 390`; `generar_matriz.py:82-88`).
- Q1-034 C1 se evalúa sobre la salida de su paso (`01`), no sobre el registro. Con el producto de eco de la revisión anterior, FALLA.
- Q1-026 C1 exige las 9 líneas exactas (`stderr_lineas_eq`, `ejecutar_caso.py:136-144`). P7v y P7v2 dan COMPONENTE_FALLA; el stderr real, COMPONENTE_OK.
- Q1-027 usa las cifras del banco (95 → 80 en `aux:caja`): la regresión de `d032691` está corregida.

**Abierto 1 · la prueba 34 no es un control contra el estado previo (material).**
- Para cada aserción copia solo los archivos de pasos **anteriores** al que produce el archivo leído (`pruebas_arnes.py:449-456`; las dos condiciones de las líneas 452 y 454 excluyen siempre el propio archivo). El archivo leído nunca está, la aserción falla por «ruta no permitida» y `mal` queda vacío siempre.
- Demostración: quitando la marca `no_discriminante` de Q1-027 C4, la prueba 34 sigue en PASA (`s05`).
- La prueba 15 no cambia y sigue siendo sobre un estado vacío.

**Abierto 2 · Q1-017 da CUMPLE sin hacer nada (material).** Control hecho de verdad (`s09`): cada aserción sobre una salida de `comprobar` se evalúa sobre la salida anterior del mismo caso o, si es la primera, sobre la del expediente recién creado (salida real del producto, `s09_estado_previo_plantilla_957af65.json`).
- De 56 criterios, dos pasan íntegros sobre su estado previo: Q1-027 C4 (marcado) y **Q1-017 C1 (sin marca; es su único criterio y cuenta en los 29 CUMPLE)**.
- Contraejemplo con el producto real (`s09b`): Q1-017 con los pasos reducidos a `nuevo_expediente`, una entrada vacía y `comprobar` da **exit 0, COMPONENTE_OK** con los criterios publicados.
- Además, el motivo que da el producto es otro: «la comprobación no está vinculada… o sin sellar», no la falta de bytes. `lecturas_externas` sale vacío. El caso no llega a probar su escenario.

**Abierto 3 · el origen del mensaje de Q1-026 no es el entorno (material).** D3 pedía anclar C1 «al mensaje real y a su origen». El mensaje está anclado; el origen que se le atribuye es falso:
- Con pdftotext y soffice en el PATH, `cambiar_base_preparar.txt` es **idéntico** al publicado (`s06`).
- Las 9 líneas son los últimos 600 caracteres (`cambiar_base.py:300`) de **14** errores de `fase1_historia.py construir`: 6 textos ausentes (AR_2016, AR_2018 y AR_2021 a AR_2024) y 8 «cero sin cita». «ipal:» es el final cortado de «arrendamientos_principal» (`s08`).
- En toda la candidata no hay PDF ni texto AR_2021…AR_2024 de Viscofan. La frase «son PDF y falta pdftotext» no tiene base: no hay nada que convertir.
- En la misma candidata, `construir` da exit 0 sobre los expedientes de la 4.14 (Viscofan, Viscofan decisiones, Vidrala decisiones, Elis decisiones).
- Con la especificación publicada y `PLANTILLA_EXP` apuntando al Viscofan de la 4.14, **`cambiar_base.py preparar` da exit 0**: origen sin cambios, expediente nuevo y «C24 → 90.0» (`s08b`). El arnés lo informa como ERROR porque espera exit 1 y las 9 líneas.
- Conclusión: Q1-026 no está bloqueado por el entorno sino por el expediente base que usa el arnés por defecto. Un POSITIVO del banco figura como NO_OBSERVABLE cuando su primer paso sí se puede ejecutar. No he ejecutado lo que sigue (recálculo, pipeline, auditoría).

## D3-R3 · Regeneración — ABIERTO (evidencia y derivados: CERRADO)

**Cerrado y verificado con el producto:**
- Los 30 resultados son `harness 4.0`, con `spec_sha256` igual al de la especificación en disco, candidata `957af65` y banco `e505e0c1…`. Hay un log por ejecución y los 22 `sellar` llevan «[SIMULADO]».
- **Reejecución independiente** de las 30 especificaciones sobre `957af65`: 30 COMPONENTE_OK. De 84 salidas del producto, **82 idénticas byte a byte** a las publicadas; las otras 2 (`CAMBIO_Q1-026.json`, `origen_estado.txt`) solo difieren en la ruta de `RUN_DIR`. MATRIZ, MAPA, PAQUETES_RELEVO y recuentos: `cmp` 0. Igual con y sin pdftotext.
- El CAMBIO de Q1-026 se valida contra el banco antes de llamar al producto: valor 85, resultado 215, operandos 250/90, cita sin la línea del fixture, sin `evidencia` o sin `derivados_esperados` dan ERROR_ESPECIFICACION con exit 2 (`s12`).

**Abierto:**
- **Lo publicado no está regenerado entero.** D3 pedía también log, HALLAZGOS, RESUMEN y ENTREGA. Siguen en v3: `CONFIGURACION.harness_version` «3.0»; «59 con aserción» en 4 documentos (el MAPA dice 54); «16/16» en 7 (el guion declara 36 pruebas); `pruebas_arnes.log` es el de la v3.
- **Clasificación de Q1-026.** Sale del resultado cuando es COMPONENTE_OK o COMPONENTE_FALLA. Pero `generar_matriz.py:138-141` da BLOQUEO_ENTORNO a **cualquier** ERROR_ENTORNO sin validar nada: un resultado de un solo campo (E1), o el caso ejecutado con la candidata sucia (E2), salen como «NO_OBSERVABLE (bloqueo de entorno: faltan pdftotext/soffice/agente…)». La prueba 33 del autor consagra ese comportamiento, que la revisión anterior había señalado como defecto (M3). Y el rótulo es falso aun con el resultado legítimo (R2, abierto 3).
- **Deuda neta 210: sigue siendo una declaración.** `derivados_esperados` solo lo lee el arnés; el producto no lo usa (0 apariciones en sus scripts). Un texto de evidencia que diga «Deuda financiera 999» pasa la validación (`s12` a7). Ninguna entrada lleva la deuda 300 a la copia. Límite ya conocido; lo doy por cerrado con límites.
- **El CAMBIO publicado lleva `origen` y `destino` en `/workspace/ejecucion_d_run/…`**, rutas de la máquina del autor. El relevo lo ofrece como «CAMBIO para el runtime», pero no se puede usar sin editarlo.

## D3-R4 · Relevos — ABIERTO · NO TRATADO

- `scripts/generar_relevo.py` no cambia en ninguno de los dos commits (último cambio: `5f4b2a2`, 09:45 UTC). El paquete publicado sigue rotulado «respuesta D2-R4 sobre 1ac661b» (línea 116).
- `relevo/PAQUETES_RELEVO.json` solo cambia en los recuentos y en los criterios de 4 paquetes (Q1-025, Q1-026, Q1-027 y Q1-034), arrastrados del MAPA. **Los paquetes de Q1-028 y Q1-032 son idénticos a los de `d032691`.**
- **La prueba 36 del autor, aplicada literalmente a lo publicado, FALLA con 253 incumplimientos** (`s13`): 36 paquetes sin `estado_inicial`, 36 sin `fases`, 36 sin `entrada`, 36 sin `artefacto_por_criterio` y 109 criterios sin `artefacto`.
- Q1-028 y Q1-032: `comando_relevo` null y un único paso de una línea. Q1-032 sigue sin paso de agente y con la alternativa «o registrar NO_OBSERVABLE» sin decidir.
- 29 paquetes repiten el mismo texto genérico. En los 30 con comando, `comando_relevo` es el del **componente** (`python3 scripts/ejecutar_caso.py …`), no el del personaje.
- El paso de agente sigue dependiendo de `PARCIAL_COMPONENTE` (línea 64): con Q1-005 en COMPONENTE_FALLA solo queda «revisión externa por otro contexto» (`s01`).
- Los hallazgos del contraste `munger-d-relevos-002` (6 materiales y 1 menor sobre Q1-028 y Q1-032) siguen vigentes: lo que examinó no ha cambiado.
- Tampoco se ha hecho la adaptación que pide el bloque 1 de `REANUDAR`: qué expediente o paso del producto corresponde a cada caso.

## D3-R5 · `preserva_sentido` y MAPA — ABIERTO (mejora)

**Hecho:** 36 justificaciones distintas; «no» en Q1-032, «parcial» en Q1-001 y Q1-034. Cinco filas del MAPA pasan a «sin aserción»: Q1-025#2, Q1-026#0, Q1-026#2, Q1-027#0 y Q1-027#2. Quedan 54 con aserción y 55 sin ella.

**Abierto:**
- **Dos filas señaladas en D3 no cambian.** Q1-034#0 sigue en C1: la salida del producto no contiene «0-200»; lo que dice es «la hipotesis tiene la comprobación pendiente», y el resto de la línea es el eco de la nota que escribió el arnés. Q1-025#0 sigue contada como aserción aunque su propia `razon` dice «parcial». El commit dice haber corregido «Q1-034 idx 2», pero esa fila ya era «sin aserción» en `d032691`.
- **Auditoría de las 54 filas «asercion»** (`s10`; las revisiones anteriores no la hicieron; es juicio del revisor, con el motivo fila a fila en el CSV): **12 observan** el criterio, **29 lo observan en parte** y **13 no lo observan**: Q1-001#2, Q1-005#0, Q1-007#0, Q1-010#1, Q1-012#1, Q1-017#0, Q1-017#1, Q1-019#1, Q1-020#0, Q1-023#1, Q1-034#0, Q1-036#1 y Q1-036#2.
- **Trato desigual del mismo criterio.** «4 verificadas / 1 pendiente / 5 total» es NO_OBSERVABLE en Q1-032#0 y «asercion» en Q1-019#1, donde la salida dice «4 de 321». «Recuentos 3/2/5 visibles» es «asercion» en Q1-036#1, cuya C3 solo asevera «apta por entradas: no». La invalidación de aprobaciones es «sin aserción» en Q1-027#0 y «asercion» en Q1-020#1.
- **El recuento «con aserción» es un dato declarado.** `generar_correspondencia.py:35-40` cuenta lo que diga `adaptaciones.json`. Declarando una aserción para un caso sin especificación y otra sobre un criterio no discriminante, el MAPA pasa de 54 a 56 (`s12`).
- **`preserva_sentido` «si» discutible.** Q1-025 usa 45054 miles del libro en vez de los 95 millones del banco: el mismo defecto que se corrigió en Q1-027. Q1-019, Q1-029 y Q1-036 dicen «si» con la misma carencia que justifica el «no» de Q1-032. La justificación de Q1-034 afirma que el rango 0-200 «se conserva en la salida del producto», y no es así. Q1-017 dice «si» y no prueba su escenario.
- `generar_matriz.py:180` conserva el valor por defecto «sí».

## D3-R6 · Manifiesto — ABIERTO · REGRESIÓN

`sha256sum -c MANIFIESTO_SHA256.txt` da **código 1**: 106 de 204 archivos fallan (67 de evidencia de casos, las 30 especificaciones, `adaptaciones.json`, 4 scripts, MATRIZ, MAPA, PAQUETES_RELEVO y recuentos). La lista sigue coincidiendo con la carpeta. El manifiesto no se regeneró tras los bloques A y B.

## D3-R7 · (menor) — ABIERTO: 3 de 4 puntos

| Punto | Estado | Evidencia |
|---|---|---|
| `--revisor` de la especificación sin marca | corregido | `ejecutar_caso.py:341-343`; con el producto real: «revisora independiente (nombre de persona) [SIMULADO]» |
| comprobación «pendiente» por defecto sin `_simulada` | corregido | `lib_arnes.py:327-328`; registro real: `_simulada: true` |
| `ARNES_EVIDENCIAS_LIMPIAS=0` sin registrar | corregido | `evidencias_limpiadas: false` y aviso en el log. La sonda antigua dice «sin registrarlo» porque busca otra clave |
| 8 casos publicados sin marca | corregido | 22 de 22 `sellar` con «[SIMULADO]» |
| `KeyError 'good'` | **sin corregir** | `preparar_entorno.sh:33` sigue leyendo `r['good']`; `base_414.py` escribe `verified` |
| «una prueba por punto» | **no cumple** | la prueba 16 falla con el producto real y la 35 aborta |

## D3-R8 · Entrega por bloque — ABIERTO · NO TRATADO

- `ENTREGA.json` no cambia desde `d032691`: `base_revisada_sha 1ac661b`, «Respuesta D2-R1..R7», «16/16 PASA», «sha256sum -c exit 0».
- No hay entrega de los bloques A ni B ni lista D3-R1…R8. Los mensajes de commit hacen de entrega.
- **`PUNTO_DE_RECUPERACION.md` está caducado y su comando de «Reproducir» ya no pasa:** `pruebas_arnes.py` sale con 1 y el manifiesto también.
- El commit `328fa31` afirma haber pasado la sonda de la revisión anterior, y es cierto, pero no publica su salida.

---

## `pruebas_arnes.py` v4 — no se ejecuta

Ejecutado con el producto real, que las revisiones anteriores no pudieron usar.

| Hecho | Evidencia |
|---|---|
| Aborta en la prueba 4 con `FileExistsError` | `candidata_falsa` crea el directorio y después llama a `shutil.copytree` sobre él (`pruebas_arnes.py:86-87`). Solo corren las pruebas 1 a 3 |
| Tras arreglar eso, aborta en la 5 | copia `generar_matriz.py` solo, y la v4 importa `lib_arnes` y `ejecutar_caso` (línea 153) |
| Tras arreglar eso, aborta en la 12 | mismo error de `copytree` (líneas 214 y 218) |
| Con los 4 parches (`s04_parches…diff`): 33 PASA, **16 FALLA**, **35 aborta**, 36 no llega | la 16 exige `_simulada` en las 320 entradas que escribe el producto (línea 267); la 35 lee un registro que su candidata de prueba no puede crear (línea 476) |
| **Las pruebas 4 y 17 a 20 no prueban lo que anuncian** | en su candidata de prueba, `plantilla` del producto real falla (`TypeError`), el caso se aborta en el primer paso y ni `ficha` ni la operación con `../` llegan a ejecutarse. Con `ruta_dentro` sin contención, las 17 a 20 siguen en PASA (`s05`) |
| **La prueba 34 no puede fallar** | ver D3-R2 |
| La prueba 36 fallaría | ver D3-R4 |
| La prueba 33 fija como correcto el defecto M3 | ver D3-R3 |

Las pruebas 1, 2, 3, 5, 6, 8 a 14 y 21 a 33 sí discriminan (la 7 compara dos salidas del mismo generador; la 15 sigue siendo sobre un estado vacío). No he visto intención de engaño: son errores de un guion reescrito que no se llegó a ejecutar. El `pruebas_arnes.log` publicado (16/16) es el de la v3 y no dice nada de este guion.

## Recuentos y presentación

- **29 CUMPLE de componente, Q1-026 BLOQUEO_ENTORNO, 6 NO_EJECUTADO: se reproducen** por tres vías (regeneración, reejecución real en dos entornos y sonda D2 original).
- **0 de 36 casos del personaje: correcto y bien declarado.** La matriz dice «sin veredicto de caso (pendiente de agente)» en los 29; los documentos, «0/36 casos completos del personaje»; los commits, «0/36 completos». Nada se presenta como ejecución del personaje.
- Matices que no cambian la cifra pero sí su lectura:
  - Uno de los 29 CUMPLE (Q1-017) no prueba nada.
  - El BLOQUEO_ENTORNO de Q1-026 se reproduce como rótulo, no como hecho.
  - «54 con aserción» es un dato declarado; por mi auditoría, 12 observan su criterio.
  - HALLAZGOS dice que «el producto se comportó conforme al contrato del banco» en 29 casos. Con lo anterior, la frase dice más de lo que la evidencia sostiene.

## Rutas absolutas y pruebas que pasan sin verificar

- **Especificaciones, `adaptaciones.json`, MATRIZ, MAPA y PAQUETES_RELEVO:** ninguna ruta absoluta.
- **Scripts:** solo valores por defecto bajo `/workspace/…`, sustituibles por variables de entorno; `preparar_entorno.sh` usa además `/tmp/base_414_verify.json` fijo.
- **Evidencia:** los logs y resultados registran las rutas del autor (`/workspace/…`, `/tmp/banco`), como corresponde a un registro. La excepción con efecto es `CAMBIO_Q1-026.json` (R3).
- **Pruebas que pasan sin verificar:** las 4, 15, 17, 18, 19, 20 y 34 del autor, y el criterio único de Q1-017.
- **Higiene:** los dos commits solo tocan `resultados_qwen/ejecucion_d/`; sin binarios, `.pyc` ni secretos.

## Bloque A por separado (`328fa31`)

No es coherente por sí solo; el bloque B lo arregla.
- La evidencia de Q1-001 en `328fa31` es la salida de una sonda con candidata de juguete (`candidata_sha d5dec122…`, `/tmp/tmpxiump0yo/R1_ejecutar_todo_y_M2/cand_et`, COMPONENTE_FALLA). La MATRIZ de ese commit la da por CUMPLE; regenerada desde su evidencia sale 28 CUMPLE y 1 ERROR.
- El MAPA de `328fa31` aún remite Q1-026 a C2 y C3, que ya no existen en su especificación.
- Causa probable: `EVIDENCIAS_DIR` exportado al lanzar la sonda. Confirma que una ejecución ajena puede pisar la evidencia publicada.

---

## Ejecución de los casos del personaje

**El paquete no permite ejecutar todavía ningún caso del personaje sin interpretar: 0 de 36.** `MECANISMO_PERSONAJE.md` §4 pide, por caso, qué estado del producto preparar, qué pasos recorrer con agentes reales, qué entrada se carga y qué artefacto mirar por criterio. Ningún paquete lo dice.

| Grupo | Casos | ¿Caso del personaje ejecutable? | Qué hay y qué falta |
|---|---|---|---|
| Con especificación de componente | 29: Q1-001 a Q1-025, Q1-027, Q1-029, Q1-034, Q1-036 | **No** | Hay comando de componente (abajo). Falta el relevo del personaje: expediente base y cómo se cargan los fixtures, fases y actores, entrada, artefacto por criterio y el comando del pipeline |
| Q1-026 | 1 | **No** | Con la plantilla por defecto, `cambiar_base.py preparar` falla en cualquier entorno, y la especificación lo da por bueno. Con el Viscofan de la 4.14, `preparar` da 0. Falta: especificación y relevo sobre una base válida, recálculo con LibreOffice en secuencia y auditoría nueva |
| Sin especificación | Q1-028, Q1-031, Q1-032, Q1-033 | **No** | Sin comando. Falta todo, o decidir NO_OBSERVABLE por criterio con su motivo |
| Decisión del usuario | Q1-030, Q1-035 | **No** | DECISION_PENDIENTE: caducidad temporal y validación de motores |

**Lo que sí se puede ejecutar hoy: los 30 componentes** (no son casos del personaje). Comando comprobado, sobre una copia de `resultados_qwen/ejecucion_d/` @ `c734ca1`:

```bash
export CANDIDATA_DIR=<candidata> SHA_CANDIDATA_ESPERADO=<sha de la candidata> \
       BANCO_DIR=<banco_revisado @4745f38> RUN_DIR=<carpeta de trabajo>
python3 -B scripts/ejecutar_caso.py scripts/especificaciones/piloto/Q1-001.json   # un caso
bash scripts/ejecutar_todo.sh                                                     # los 30, matriz, mapa y relevo
```

- En `957af65`: 30 de 30 COMPONENTE_OK, con salidas idénticas a las publicadas.
- En la candidata compartida (`b129b36`): Q1-001 da OK con `SHA_CANDIDATA_ESPERADO=b129b36…`. Sin esa variable el arnés la rechaza con ERROR_ENTORNO, como debe.
- Precauciones:
  - trabajar sobre una copia: ejecutar en la carpeta publicada sobrescribe su evidencia;
  - no usar `EVIDENCIAS_DIR`: la matriz lo ignora;
  - `generar_matriz.py` necesita el mismo `SHA_CANDIDATA_ESPERADO`;
  - Q1-026 dará COMPONENTE_OK y BLOQUEO_ENTORNO también con las herramientas instaladas: no leerlo como bloqueo real.

---

## Hallazgos

| ID | Gravedad | D3-R | Hallazgo | Contraejemplo mínimo | Prueba de cierre |
|---|---|---|---|---|---|
| H1 | material | R4 | Relevos sin tratar | La prueba 36 del autor sobre lo publicado: 253 incumplimientos (`s13`) | Los 36 paquetes generados con estado inicial, fases, entrada, artefacto por criterio y comando del personaje; la 36 PASA; Q1-028 y Q1-032 reproducibles por el coordinador sin editar nada |
| H2 | material | R1 | Las aserciones leen contenido del arnés | A1 a A5 (`s02`): COMPONENTE_OK y CUMPLE o BLOQUEO en la matriz | A1 a A5 dan ERROR; solo son asertables el stdout de un comando del producto y los artefactos que el arnés no ha escrito ni modificado; nombres del arnés reservados |
| H3 | material | R2, R3 | El «bloqueo de entorno» de Q1-026 no es de entorno | Mismo stderr con pdftotext y soffice; `preparar` da 0 con el Viscofan 4.14 (`s06`, `s08`, `s08b`) | Q1-026 sobre una base en la que `construir` dé 0; la especificación asevera el resultado real de `preparar`; BLOQUEO_ENTORNO solo con la herramienta ausente comprobada |
| H4 | material | R2 | Sin control real contra el estado previo; Q1-017 CUMPLE sin pasos | Mutante B y prueba 34 en PASA (`s05`); Q1-017 reducido da COMPONENTE_OK (`s09b`) | La prueba 34 evalúa sobre el contenido del estado previo y falla con el mutante B; Q1-017 con una aserción positiva sobre el motivo real, o fuera del cómputo |
| H5 | material | R2, R7 | `pruebas_arnes.py` no se ejecuta; las 4 y 17 a 20 no prueban nada | `python3 -B scripts/pruebas_arnes.py`: exit 1 en la prueba 4 (`s03`); mutante A (`s05`) | Las 36 terminan con exit 0 sobre el producto real; 17 a 20 fallan con el mutante A y la 4 llega a ejecutar `ficha`; log regenerado |
| H6 | medio | R6 | Manifiesto roto de nuevo | `sha256sum -c`: código 1, 106 fallos | Código 0 y lista igual a la carpeta en el último commit |
| H7 | medio | R3, R8 | Documentos, log y ENTREGA de la v3; sin entrega de bloque | ENTREGA con base `1ac661b`; «harness 3.0», «59», «16/16», «28» | Todo lo publicado regenerado con v4; ENTREGA por bloque con D4-R1…R8; punto de recuperación vigente |
| H8 | medio | R5 | MAPA sobredeclarado y recuento sin respaldo | Q1-034#0 y Q1-025#0 sin cambio; 13 filas que no observan (`s10`); 54 → 56 con dos filas declaradas (`s12`) | Cobertura `observa` / `parcial` / `sin_asercion` con motivo; solo `observa` cuenta; el generador rechaza filas sin aserción real; mismo criterio, mismo trato |
| H9 | medio | R3 | ERROR_ENTORNO se convierte en BLOQUEO_ENTORNO | Resultado de un campo; candidata sucia (`s02` E1, E2) | ERROR_ENTORNO nunca da BLOQUEO_ENTORNO; la prueba 33 se invierte |
| H10 | menor | R1 | Dos alteraciones ocultas de la candidata pasan | D1 (`s`), D2 (enlace a directorio) (`s02`) | D1 y D2 dan ERROR_ENTORNO: cualquier marca distinta de `H` y cualquier entrada no rastreada bajo `scripts/` |
| H11 | menor | R5 | `preserva_sentido` «si» con cifras del libro o justificación falsa | Q1-025 (45054 frente a 95), Q1-034, Q1-019/029/036 frente a Q1-032, Q1-017 | Valor y justificación coherentes con la cobertura real |
| H12 | menor | R1 | Rutas, ids y evidencia sin proteger del todo | B1; C1 a C3; `EVIDENCIAS_DIR` ignorado; Q1-001 pisado en `328fa31` | `fuente.archivo` dentro del expediente; id con `fullmatch`, presente en el banco e igual al nombre del archivo; la matriz respeta `EVIDENCIAS_DIR`; la evidencia previa no se borra hasta terminar bien |
| H13 | menor | R3 | CAMBIO publicado con rutas del autor; deuda 210 declarada | `origen` y `destino` en `/workspace/…`; `s12` a7 | El CAMBIO del relevo, sin rutas de máquina o generado por el comando del relevo |
| H14 | menor | R7 | `KeyError 'good'` | `preparar_entorno.sh:33` | Lee `verified` |

## Lo conforme, que se conserva

- Las 16 variantes de D3 y de `ESTADO_D3`, cerradas tal como estaban escritas, reproducidas con la sonda de la revisión anterior sin cambios.
- La matriz reevalúa las aserciones y exige arnés, especificación, candidata y banco.
- El id se valida antes de tocar el disco para `"."`, `""` y `"../fuera"`.
- **La evidencia v4 es real:** reproducida byte a byte con el producto `957af65`, en dos entornos. MATRIZ, MAPA, relevo y recuentos se regeneran byte a byte.
- Recuentos 29 / 1 / 6 y 0 de 36 del personaje, bien declarados.
- Q1-027 con las cifras del banco y C4 fuera del cómputo. Q1-034 C1 sobre la salida de su paso. Q1-026 C1 con las líneas exactas y el CAMBIO validado contra el banco antes de llamar al producto.
- D3-R7: marcas `[SIMULADO]` y `_simulada`, y aviso de evidencias no limpiadas.
- `preserva_sentido` con 36 justificaciones propias; «no» y «parcial» donde D3 lo señaló; 5 filas del MAPA corregidas.
- Sin rutas absolutas en especificaciones ni paquetes; sin binarios ni secretos; cambios solo en la carpeta del frente.
- Lo ya cerrado en D2: `verify` sin `|| true`, banco fijado por SHA, especificación vacía o sin aserciones, negativo sin universo.

## Límites de esta revisión

- No he ejecutado el personaje, agentes, el pipeline ni LibreOffice. De Q1-026 con la base 4.14 solo he comprobado `cambiar_base.py preparar`.
- La reejecución real es sobre `957af65`, en un clon propio verificado por el manifiesto del producto. Sobre la candidata compartida (`b129b36`) solo he lanzado Q1-001. Python 3.13 aquí; el autor declara 3.12.
- No he verificado la base 4.14 con `tools/base_414.py verify` ni he ejecutado `preparar_entorno.sh` (necesita red).
- Las sondas con stubs miden el arnés, no Munger. Las variantes A1 a A5, D1 y D2 son especificaciones o candidatas construidas a propósito: ninguna especificación publicada las usa.
- La clasificación de las 54 filas del MAPA es juicio mío. Son mecánicas: Q1-017 (`s09`, `s09b`), Q1-034#0 (contenido de la salida) y los recuentos de Q1-019, Q1-029 y Q1-036 (contenido de la salida y trato de Q1-032).
- No he auditado las 55 filas «sin aserción» ni el contenido económico de las adaptaciones.
- Observación fuera del frente D: el expediente Viscofan del ensayo 4.13 no se reconstruye con `fase1_historia.py construir` en `957af65` (14 errores). Puede interesar a T-EXP.
- Esto no es aceptación, ni integración, ni aptitud para dinero real.

## Archivos del revisor

- Este informe: `<rev_D3>/REVISION_D3_328fa31_c734ca1.md`.
- Corrección propuesta: `<rev_D3>/CORRECCION_D4.md`.
- `<rev_D3>/sondas/` (rutas sustituidas por `<rev_D3>`, `<aux>` y `<candidata>`; `<tmp>` en las sondas con stubs):
  - `comprobaciones_d4.sh` y `comprobaciones_d4.log`: todo lo anterior, en un solo guion;
  - `s01`, `s01b`: sondas D3 y D2 de las revisiones anteriores, sin cambios, sobre `c734ca1`; `s11`: la sonda D2 del autor;
  - `s02_sondas_arnes_d4.*`: variantes nuevas (A1 a A5, B1, C1 a C3, D0 a D2, E1 a E3); `s16`: A1 y A2 con el producto real;
  - `s03`, `s04`, `s05`: `pruebas_arnes.py` tal cual, con los 4 parches del revisor y sobre el arnés mutado;
  - `s06`: `ejecutar_todo.sh` real con y sin pdftotext; `s08`, `s08b`: Q1-026;
  - `s09*`: control contra el estado previo y Q1-017 sin pasos; `s10*`: auditoría de las 54 filas;
  - `s12*`: validación del CAMBIO y MAPA declarado; `s13*`: prueba 36 sobre los paquetes; `s14`, `s15`: especificaciones de N1c y R7.
- `MANIFIESTO_SHA256.txt`: huellas de este informe, de la corrección y de `sondas/`.
- Áreas de trabajo que no forman parte de la entrega: `<rev_D3>/wt` (worktree en `c734ca1`, registrado en el repositorio auxiliar), `<rev_D3>/cand_957af65`, `<rev_D3>/banco`, `<rev_D3>/previas`, `<rev_D3>/trabajo`.
