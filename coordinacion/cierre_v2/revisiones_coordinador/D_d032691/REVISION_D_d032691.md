# Revisión independiente · frente D (Mistral D) · bloque 3 `d032691` frente a la corrección D3

- **Revisor:** subagente Claude, en un contexto distinto del autor (Mistral D). No he escrito este material.
- **Fecha:** 2026-11-17.
- **Objeto:** `origin/mistral/d-qwen-aceptacion`, commit `d032691` sobre `5f4b2a2`. Mensaje: «D2-R1..R7 (bloque 3): re-ejecución real de las 28 specs con arnés v3 (29 CUMPLE de componente, Q1-026 BLOQUEO_ENTORNO, 0/36 casos completos); pruebas_arnes 16/16 PASA; sondas D2 P1-P9…».
- **Referencia única:** `CORRECCION_D3.md` (sha256 `f9d95a98…48e0`), con `REVISION_D2_3934bc9_a_5f4b2a2.md` y sus sondas, en `origin/coordinacion/cierre-v2` (publicados en `314c4dc`; sin cambios hasta `be6e9d5`). Además, `MECANISMO_PERSONAJE.md` §4 (`coordinacion/cierre_v2/pruebas_candidata/957af65/`) y el banco `4745f38`.
- **Método:**
  - Copia aislada con `git archive d032691 | tar -x -C <rev_D3>/entrega`; banco con `git archive 4745f38 resultados_qwen/q1_v2/banco_revisado` en `<rev_D3>/banco`. Sin checkout ni worktree. Python siempre con `-I -B`.
  - Las sondas usan una **candidata falsa con scripts de juguete (stubs)** que imitan la interfaz del producto. Miden la lógica del arnés y de los generadores, no Munger.
  - He ejecutado sin cambios la sonda original de la revisión D2 (`<rev_D2>/sondas/sondas_arnes_d2.py`, sha256 `a466c31a…a07d`, igual a la publicada) contra `d032691`, y una sonda nueva (`sondas_arnes_d3.py`) con las variantes nuevas.
  - No he ejecutado el producto, LibreOffice, agentes, la red, `pruebas_arnes.py`, `ejecutar_todo.sh` ni `preparar_entorno.sh`.
  - No he hecho commit, push ni cambios en ningún repositorio. `git status` del repositorio muestra un único elemento ajeno a esta revisión: `?? coordinacion/cierre_v2/traspaso/resultado_20261117/`, que corresponde al trabajo T-TRASPASO de otra sesión (`be6e9d5`). No lo he creado ni tocado.

## Contexto que condiciona la lectura

- **`d032691` es anterior a la corrección D3.** El commit es de 2026-11-17 09:59:44 +0000. `CORRECCION_D3.md` se publicó en `314c4dc` a las 10:02:25 +0000. El autor no pudo leerla.
- Por eso `ENTREGA.json`, `RESPUESTA_D2.md`, HALLAZGOS y RESUMEN responden a **D2 sobre `1ac661b`**, no a D3. Esta revisión mide si el bloque cierra los defectos D3 de todas formas, como pide el encargo, sin reprochar al autor que no la cite.
- **Comprobado** con `git diff --stat 5f4b2a2 d032691`: entre `.py` y `.sh` solo cambian `ejecutar_todo.sh` (+2 llamadas a generadores y dos mensajes) y la nueva `sondas/sondas_d2.py`. **No cambian** `lib_arnes.py`, `ejecutar_caso.py`, `generar_matriz.py`, `generar_relevo.py`, `generar_correspondencia.py`, `pruebas_arnes.py` ni `preparar_entorno.sh`. Coincide con la observación de `REVISION_1005.md` @ `35d0fb9`.
- El resto del diff: evidencia regenerada (logs y resultados de 30 casos, y tres archivos de Q1-026), especificaciones Q1-026, Q1-027, Q1-034 y `adaptaciones.json`, documentos, MATRIZ, MAPA (nuevo), relevo y manifiesto.

## Dictamen

**El bloque 3 cierra lo que dependía de regenerar y publicar; no cierra nada que dependiera de cambiar el código.**

- Cierra: la regeneración de lo publicado (MATRIZ, MAPA, relevo y recuentos coinciden byte a byte con los que regenero), la evidencia v3, el manifiesto y la publicación del MAPA.
- Siguen abiertos: todos los invariantes de D3-R1, los controles negativos de D3-R2, la clasificación de Q1-026 desde su resultado, los relevos por caso, `preserva_sentido` y la entrega por bloque.
- Hay una **regresión** respecto de lo conservado en D2: Q1-027 vuelve a sellar 45.054 miles como caja verificada, en vez de los 95 millones del banco.
- Se mantiene correctamente la declaración de **0/36 casos completos del personaje**, y los 29 CUMPLE se presentan como de componente.

| D3-R | Veredicto | En una línea |
|---|---|---|
| **D3-R1** rutas e identificadores | **ABIERTO** | Las 7 variantes de la revisión anterior siguen pasando, y las 7 variantes nuevas (una o dos por invariante) también. Solo `ejecutar_todo.sh` neutraliza el resultado forjado, y solo dentro de su propio flujo |
| **D3-R2** controles negativos | **ABIERTO** | Prueba 15 sin cambios (vacía). Q1-027 C4 sigue contando. Q1-034 C1 ya no falla, pero porque se quitó la comprobación de la clase, y sigue siendo tautológico. Q1-026 C1 casa con el stderr real, pero pasa con un CAMBIO inválido |
| **D3-R3** regeneración | **ABIERTO** (regeneración: CERRADO) | MATRIZ, MAPA, relevo y recuentos: idénticos byte a byte. Evidencia v3 coherente. Q1-026 sigue clasificándose BLOQUEO_ENTORNO sea cual sea su resultado. Deuda neta 210 solo como texto |
| **D3-R4** relevos | **ABIERTO** | Generador sin cambios: el paso de agente sigue dependiendo de PARCIAL_COMPONENTE. Mismo texto genérico en 29 casos. Ni estado, ni fases por caso, ni artefacto por criterio. Q1-028 y Q1-032 con `comando_relevo` null; Q1-032 sin ningún paso de agente |
| **D3-R5** `preserva_sentido` y MAPA | **ABIERTO** (publicación del MAPA: CERRADO) | 36/36 «si», 35 con la misma frase; falsa en Q1-001, Q1-032 y Q1-034, y ahora también en Q1-027. MAPA publicado, pero con las mismas sobredeclaraciones |
| **D3-R6** manifiesto | **CERRADO** | `sha256sum -c` exit 0; 204 entradas = 204 archivos |
| **D3-R7** (menor) | fuera de la lista de este encargo; no reabierto | Código sin cambios: los límites latentes siguen (`--revisor` de la especificación sin marca, auxiliar por defecto, `ARNES_EVIDENCIAS_LIMPIAS=0`, `KeyError 'good'`). En lo publicado, los 22 `sellar` llevan «[SIMULADO]» y hay un log por ejecución |
| **D3-R8** entrega por bloque | **ABIERTO** | Una sola `ENTREGA.json`, declarada como respuesta a D2 sobre `1ac661b`, sin D3-R1…R8 ni entrega por bloque. Contiene afirmaciones que no se sostienen |

## Comandos ejecutados (todos sobre copias aisladas)

| Comando | Exit | Resultado |
|---|---|---|
| `git archive d032691 \| tar -x -C <rev_D3>/entrega`; `git archive 4745f38 resultados_qwen/q1_v2/banco_revisado \| tar -x -C <rev_D3>/banco` | 0 | Copias |
| `git diff --stat 5f4b2a2 d032691 -- '*.py' '*.sh'` | 0 | Solo `ejecutar_todo.sh` y `sondas/sondas_d2.py` |
| `sha256sum -c MANIFIESTO_SHA256.txt`, desde `entrega/resultados_qwen/ejecucion_d` | **0** | 204/204; lista igual a la carpeta (`diff` exit 0) |
| `sha256sum -c` del banco | 0 | 57/57 |
| `generar_matriz.py`, `generar_correspondencia.py`, `generar_relevo.py` sobre una copia, con `BANCO_DIR=<rev_D3>/banco/…` | 0, 0, 0 | `cmp` exit 0 en MATRIZ, MAPA, `PAQUETES_RELEVO.json` y `recuentos.json` |
| `python3 -I -B sondas/sondas_arnes_d3.py entrega/resultados_qwen/ejecucion_d banco/… sondas/sondas_arnes_d3.json` | 0 | Variantes R1, controles R2, reevaluación R3, relevo R4 |
| `python3 -I -B <rev_D2>/sondas/sondas_arnes_d2.py <d032691> <d032691> banco/… sondas/sondas_arnes_d2_original_sobre_d032691.json` | 0 | Sonda D2 original, sin cambios, contra `d032691` |
| `bash sondas/comprobaciones_d3.sh <repo> <rev_D3>` | 0 | Diff, fechas, manifiesto, regeneración, marcas; log en `sondas/comprobaciones_d3.log` |

---

## D3-R1 · Invariantes de rutas e identificadores — ABIERTO

El código no ha cambiado, así que las variantes de la revisión anterior se reproducen igual. Las variantes nuevas confirman que no son casos sueltos, sino invariantes ausentes.

| Invariante | Variante | Origen | `d032691` | Estado |
|---|---|---|---|---|
| **1. Toda ruta, también de salida, dentro del `RUN_DIR` del caso** | `copiar_artefacto` `archivo="../../Q1-036/Viscofan/informe_provisional.md"` y aserción sobre la copia | D2 (P3va) | exit 0, **COMPONENTE_OK** | Abierto |
| | `comprobar` con `guardar="../Q1-036/07_informe_provisional.md"` | D2 (P3vb) | exit 0; la evidencia de Q1-036 queda en `{}` | Abierto |
| | `escribir_fuente` con `nombre="../../../Q1-036/Viscofan/verificacion_entradas.json"` | **nueva (N1a)** | exit 0, COMPONENTE_OK; el registro de Q1-036 en el `RUN_DIR` queda como «[PDF PAGE 1] PISADO POR Q1-031» | Abierto |
| | `copiar_artefacto` con una **ruta absoluta** a la evidencia de otro caso (`os.path.join(exp, "/…")` descarta `exp`) | **nueva (N1b)** | exit 0, COMPONENTE_OK | Abierto |
| **2. La matriz vuelve a evaluar las aserciones** | Q1-001 sustituido por `{"harness_version":"3.0","estado_caso":"COMPONENTE_OK","spec_sha256":<sha de la spec>,"criterios":[{"id":"C1","estado":"CUMPLE_COMPONENTE"}]}` (4 campos, 1 de 2 criterios, sin evidencia) | D2 (M2) | **PARCIAL_COMPONENTE / CUMPLE** | Abierto |
| | Q1-003: salidas del producto vaciadas (`comprobadas`/`pendientes` = [], `universo` 0) con `resultado_ejecucion.json` intacto | **nueva (N2a)** | **CUMPLE** | Abierto |
| | Q1-004 con `candidata_sha` = 40 ceros, `banco_casos_sha256` = 64 «f» y `harness_version` 2.0 | **nueva (N2b)** | **CUMPLE**: la matriz no mira candidata ni banco | Abierto |
| **3. Las aserciones no leen archivos que escribe el propio arnés** | `archivo_existe ejecucion.log` y `texto_contiene ejecucion.log "# Caso"` | D2 (P1v) | exit 0, COMPONENTE_OK | Abierto |
| | `texto_contiene` sobre `run:Viscofan/fuentes_sinteticas/f6_031_precio.txt`, que escribe `escribir_fuente`; criterios «precio histórico» y «capitalización 710» | **nueva (N3)** | exit 0, **COMPONENTE_OK** sin mirar ninguna salida del producto | Abierto |
| | Ya ocurre en especificaciones publicadas: Q1-034 C1.0/C1.1 (registro escrito por `poner_entrada`); Q1-026 C2 (`origen_estado.txt`) y C3 (`CAMBIO_Q1-026.json`, copia del `cambio` de la propia especificación) | lectura | CUMPLE en lo publicado | Abierto |
| **4. El id se valida antes de tocar el disco** | `"id": "."` | D2 (P9w) | la evidencia de Q1-001 desaparece | Abierto |
| | `"id": "../fuera"` | **nueva (N4)** | exit 2, pero **antes** borra una carpeta hermana de `EVIDENCIAS`, fuera del árbol de evidencias | Abierto |
| | `"id": ""` | **nueva (N4b)** | `os.path.join(EV, "")` es `EV/`: borra toda la carpeta de evidencias | Abierto |
| **5. Candidata limpia** | script rastreado alterado y oculto con `git update-index --skip-worktree` | D2 (P8va) | COMPONENTE_OK; `git status` vacío; el log muestra «SCRIPT ALTERADO» | Abierto |
| | `scripts/override.txt` no rastreado que cambia la salida | D2 (P8vb) | COMPONENTE_OK; se registra `candidata_no_rastreadas: 1` pero no se rechaza | Abierto |
| | script alterado con `--assume-unchanged` | **nueva (N5a)** | COMPONENTE_OK; `git status` vacío | Abierto |
| | `override.txt` oculto en `.git/info/exclude` | **nueva (N5b)** | COMPONENTE_OK; `candidata_no_rastreadas: 0` | Abierto |

**¿Lo cierra otra vía?**
- **`ejecutar_todo.sh`.** Reejecuta cada especificación publicada, y `Caso.__init__` borra la carpeta del caso antes de escribir el resultado. Con un resultado forjado en Q1-001 y una reejecución con la candidata de juguete, la matriz da `ERROR (COMPONENTE_FALLA)`, sin CUMPLE (sonda `R1_ejecutar_todo_y_M2`).
  - Neutraliza M2 y N2a **solo dentro de ese flujo completo**.
  - `generar_matriz.py` por separado los sigue aceptando. Ese es el uso que hacen `RESPUESTA_D2.md` (reproducción) y la prueba 7 de `pruebas_arnes.py`, que regenera la MATRIZ publicada.
  - `ejecutar_todo.sh` no valida ids, rutas ni candidata. Ejecuta las especificaciones de `piloto/` y `bloque2/`, y una especificación ahí con `"id": "."` o una ruta `../` se ejecutaría igual.
- **El manifiesto** detectaría una alteración posterior de la evidencia publicada (N2a), mientras nadie lo regenere. No es un invariante del arnés.
- **`preparar_entorno.sh`.** No cambia. Reutiliza `$CAND` si ya existe `.git`, y `git checkout <sha>` no deshace `skip-worktree`, `assume-unchanged` ni `info/exclude`. No cierra las variantes del invariante 5.

**La sonda del propio autor.** `sondas/sondas_d2.py` repite las sondas **literales** de la revisión de `1ac661b` (P1–P9), no las variantes de la revisión D2. Por eso informa «DETECTA» en todas. Con la sonda original de la revisión D2 sobre `d032691` el resultado es el mismo que en `5f4b2a2`: P1v, P3va, P3vb, P5w, P8va, P8vb y P9w siguen abiertos.

## D3-R2 · Controles negativos frente al estado previo — ABIERTO

**Prueba 15.** No cambia. Reproducida tal cual sobre las 28 especificaciones de `d032691`: 99 aserciones, ninguna pasa en vacío, así que da PASA. Pero no detecta ninguno de los casos siguientes. Sigue siendo un control contra un estado **vacío**, no contra el **estado previo**.

**Q1-027** (evidencia publicada, código de `d032691`). El «estado previo» es la salida `02` copiada como `03`, y el primer sellado como `04`:

| Aserción | Vacío | Estado previo | Publicada | Lectura |
|---|---|---|---|---|
| C1.0 `comprobadas` contiene C24 (en `02`) | F | V | V | Correcto: C1 *es* la precondición antes de mutar |
| C2.0 desactualizada por sha256 | F | F | V | Discrimina |
| C2.1 no comprobada | F | F | V | Discrimina |
| C3.0 «rechazadas 1» | F | F | V | Discrimina |
| **C4.0 / C4.1** `apto_por_entradas == false` | F | **V** | V | **No discrimina, y sigue contando**: C4 CUMPLE en el resultado publicado y entra en COMPONENTE_OK y en los 29 CUMPLE |

**Q1-034 C1.**
- La especificación cambió `clase eq "hipotesis"` por `hipotesis.fundamento contiene "0-200"`. Ya no «falla siempre», pero porque **se ha quitado la comprobación de la clase**, no porque se evalúe sobre el estado de su paso.
- C1.0 y C1.1 dan V con **solo el registro escrito por el arnés** (`poner_entrada` del paso 3) y ninguna salida del producto.
- Cuando se evalúa C1, la clase final de `aux:litigio` es `dato_publicado` (sonda con stub). El texto de C1 sigue diciendo «clase hipotesis».
- Con un producto de juguete que no lee el registro y devuelve siempre la nota que escribió el arnés, Q1-034 da **COMPONENTE_OK** (sonda D3 y P5w de la sonda D2).
- Límite a favor: la salida publicada `01` sí dice «la hipotesis tiene la comprobación pendiente», que proviene del producto. Pero ninguna aserción lo usa: C1.3 busca «rango acotado», que es el eco de la nota del arnés.

**Q1-026 C1.**
- Prefijo corregido: `fase1_historia.py` contiene `ipal`, más AR_2019 y AR_2020 contienen `cita`.
- Con el stderr real (P7c), C1 CUMPLE. Con la variante antigua P7v, C1 FALLA. **El literal queda cerrado.**
- **Variante nueva P7v2:** stderr = «ERROR: CAMBIO inválido: analisis.C24.valor no coincide con la evidencia declarada» + las 9 líneas reales. Resultado: **C1 CUMPLE, COMPONENTE_OK**, y la matriz lo llamaría BLOQUEO_ENTORNO.
- No está anclado al origen: nada exige que `otros_errores` sea exactamente el conjunto esperado ni que falte un error ajeno al entorno. Un CAMBIO mal construido quedaría enmascarado como bloqueo de entorno.

## D3-R3 · Regeneración — ABIERTO (la regeneración en sí: CERRADO)

**Regeneración, byte a byte.**
- Con el `generar_matriz.py`, `generar_correspondencia.py` y `generar_relevo.py` de `d032691`, sobre la evidencia publicada, `cmp` da 0 en `MATRIZ_EJECUCION.csv` (sha256 `2d6d5948…6307`), `MAPA_CRITERIOS_BANCO.csv` (`182a930e…ddad`), `relevo/PAQUETES_RELEVO.json` (`7673c8aa…20e7`) y `evidencias/recuentos.json` (`90d32ab9…fe8a`).
- La sonda D2 original también da `matriz_publicada_igual_a_regenerada: true`.

**Recuentos: coinciden.**
- 29 PARCIAL_COMPONENTE / CUMPLE de componente, 1 BLOQUEO_ENTORNO (Q1-026) y 6 NO_EJECUTADO.
- Veredicto de caso: 29 «sin veredicto (pendiente de agente)», 1 NO_OBSERVABLE, 4 sin veredicto y 2 DECISION_PENDIENTE: **0/36 completos**.
- 109 criterios del banco: 59 con aserción y 50 sin ella.

**Evidencia v3, de verdad:**
- 30/30 `resultado_ejecucion.json` con `harness_version` 3.0.
- `spec_sha256` igual al sha256 de la especificación en `d032691` (30/30), y los ids de criterio iguales a los de la especificación.
- `candidata_sha` observado `957af652…` = esperado. `banco_casos_sha256` `e505e0c1…48d9`, igual al del banco `4745f38`.
- `precondiciones_simuladas` presente. Los 22 `sellar` llevan `--revisor … [SIMULADO]`. Un solo «# Caso» por log; los 9 logs acumulados desaparecen.
- Reevaluación independiente con el `evaluar_afirmacion` de `d032691` sobre la evidencia publicada: **58/58 criterios coinciden** con los declarados. Las aserciones `run:` de Q1-034 C1 no se pueden reevaluar, porque el `RUN_DIR` no se publica.
- Las 80 salidas guardadas coinciden con el `stdout` registrado en el resultado, y los sha256 de los artefactos coinciden.

**¿Reutilización?** No lo parece, con un límite:
- Los logs y los resultados son nuevos. El log de Q1-027 trae la descripción y la huella nueva de la especificación, y la huella de la fuente sintética nueva (`ceb19b38…` frente a `584a66a2…` en `5f4b2a2`).
- Las demás salidas del producto (JSON/TXT de `comprobar`, `sellar`, `ficha` e `informe`) son idénticas byte a byte a las de `5f4b2a2`, salvo en Q1-026. Es compatible con un producto determinista: las salidas no llevan rutas, fechas ni la huella de la fuente.
- Sin ejecutar el producto no puedo probar que se reejecutara. Solo puedo decir que la evidencia es coherente y no contradictoria.

**Componente, no personaje.**
- RESUMEN («los CUMPLE son de componente mecánico»), HALLAZGOS, README y PUNTO_DE_RECUPERACION declaran 0/36 casos del personaje.
- La «re-ejecución real» del commit es de comandos del producto (`verificacion_entradas.py`, `ficha.py`, `informe.py`, `cambiar_base.py preparar`) sobre `957af65`. **No se presenta como ejecución del personaje.** Conforme.

**Q1-026:**
- **Cifras del banco: sí.** `CAMBIO_Q1-026.json` lleva C24 = 90, «Caja 90; Deuda financiera 300», 95→90 y el bloque `evidencia` de nivel superior.
  - La cita sigue sin ser literal: intercala «(fixture f5_026_nota.txt)».
  - C3 asevera sobre esa copia de la especificación: comprobación estática, no del producto.
- **Deuda neta 210: solo texto.** Aparece en `descripcion` y en `evidencia.M` («300-90=210»).
  - El CAMBIO solo declara `Análisis!C24` (caja). No hay entrada que lleve la deuda 300 a la copia, ni cálculo observado.
  - Se mantiene el límite económico señalado en D2: no se demuestra de dónde saldría el 210, y la cifra es de «SINTETICA CUATRO S.A.» inyectada en Viscofan.
- **Clasificación desde su resultado: no.** `generar_matriz.py:87` sigue con `if bloqueo and res:`. Con un resultado `ERROR_ENTORNO` sin criterios, la matriz da **BLOQUEO_ENTORNO** (M3, reproducida).
  - Lo mismo con P7v2: un CAMBIO inválido acaba como BLOQUEO_ENTORNO.
  - El resultado publicado es COMPONENTE_OK con C1–C3 CUMPLE, pero la clasificación no lo usa.

## D3-R4 · Relevos — ABIERTO

- **Generador sin cambios.**
  - Los 29 casos tienen ahora el paso de agente solo porque son PARCIAL_COMPONENTE.
  - Contraejemplo: si Q1-005 pasa a COMPONENTE_FALLA, su paquete queda con una sola línea, «revisión externa por otro contexto», **sin paso de agente** (sonda R4).
- **No es un relevo por caso.**
  - Los 29 paquetes repiten el mismo `qué` (`FALTA_AGENTE`) y el mismo `necesita`.
  - `recorrido_personaje` es global.
  - Los paquetes tienen solo estas claves: `entrada_usuario`, `archivos_sinteticos`, `comando_relevo` (el del componente), `criterios_banco` y `falta_para_caso_completo`.
  - Falta lo que exige `MECANISMO_PERSONAJE.md` §4:
    - **qué estado del producto preparar**: qué expediente y en qué ruta, y cómo se cargan los fixtures;
    - **qué fases recorrer** en ese caso;
    - **qué artefacto se observa por criterio**. En los 50 criterios sin aserción solo hay una razón genérica; 31 dicen «sin asercion propia: observable de actividad/conclusion no asertado por el componente (relevo)».
  - `entrada_usuario` es el texto del banco, sin indicar dónde se carga.
- **Q1-028:** `comando_relevo: null`. Un único paso, «reaprobación NUEVA con auditor real … deuda neta 245», con quién y qué necesita, pero sin estado, fases ni artefacto por criterio.
- **Q1-032:** `comando_relevo: null` y **ningún paso de agente**, aunque su criterio 1 del banco lleva la razón «relevo: fase A/objetivo con agente real». La alternativa «o registrar NO_OBSERVABLE» queda abierta, sin decidir.
- **Q1-031 y Q1-033:** siguen remitiendo a un «fase1_v63.json del expediente de prueba» que no se identifica.

## D3-R5 · `preserva_sentido` y MAPA — ABIERTO (publicación del MAPA: CERRADO)

- **`preserva_sentido`:** «si» en 36/36. En 35, la misma frase: «la adaptacion usa los fixtures y cifras del banco; la spec y las aserciones se evaluan contra ellos». Solo Q1-026 tiene una justificación propia. Es falsa en:
  - **Q1-001:** la línea cero es `Historia!C23`, arrendamientos;
  - **Q1-032:** universo 321 frente a 5;
  - **Q1-034:** la adaptación sigue diciendo «parámetro de configuración como rango», aunque la especificación usa `aux:litigio`;
  - **Q1-027 (nueva, regresión):** la especificación de `d032691` sella como caja verificada **45.054 miles** («valor del libro»), y no los 95 millones de `f5_027_revision.json`. La fuente sintética dice «caja = 45054 miles de euros (valor del libro; f5_027_revision.json declara valor_verificado 95 millones EUR…)».
    - Está declarado en la descripción y en la adaptación.
    - Pero contradice la frase de `preserva_sentido`, y deshace lo que la revisión D2 dio por conservado («cifras del banco en Q1-027»).
    - El sentido del caso (invalidar tras el cambio de la fuente) se mantiene, y el esperado 300−80=220 no cambia. La cifra verificada del banco, no.
  - `generar_matriz.py:123` mantiene el valor por defecto `"sí"`.
- **MAPA:** publicado, 109 filas, 59 «asercion» y 50 sin aserción. Las filas señaladas en D2 siguen sobredeclarando:
  - Q1-027 índice 0 → C2: la aprobación no se observa.
  - Q1-027 índice 2 → C4: no discrimina y trata de otra cosa; ninguna aserción toca la deuda 300.
  - Q1-026 índice 2 («no se cambian fórmulas ni palancas») → C3: estática, sobre la especificación.
  - Q1-025 índices 0, 1 y 2 → la misma C1: los seis ejes y la referencia en la matriz no se observan.
  - Q1-034 índice 0 → C1: tautológico (§D3-R2).
  - Como antes, no he auditado una por una las demás filas.

## D3-R6 · Manifiesto — CERRADO

- `cd resultados_qwen/ejecucion_d && sha256sum -c MANIFIESTO_SHA256.txt`: **exit 0**.
- 204 entradas para 204 archivos. La lista es igual a la carpeta (`diff` exit 0), incluidos `generar_correspondencia.py`, `MAPA_CRITERIOS_BANCO.csv` y `sondas/`.
- Nota: ejecutar `pruebas_arnes.py` reescribe la MATRIZ, `recuentos.json` y `pruebas_arnes.log` publicados (pruebas 7 y final). Mientras su salida sea idéntica, el manifiesto se mantiene.

## D3-R8 · Entrega por bloque — ABIERTO

Hay una sola `ENTREGA.json`, con estas características:
- `base_revisada_sha = 1ac661b` y `bloque`: «Respuesta D2-R1..R7 a CORRECCION_D2.md».
- No hay ninguna ENTREGA de los bloques 1 y 2, ni una lista D3-R1…R8.
- Trae comandos y exits para cuatro pruebas: `ejecutar_todo.sh` 0, `pruebas_arnes.py` 16/16, sondas y manifiesto 0. De estas, solo he podido comprobar el manifiesto (exit 0).

Afirmaciones de ENTREGA o de `RESPUESTA_D2.md` que no se sostienen frente a D3:
- «rutas fuera del caso → ERROR»: falso para `copiar_artefacto`, `guardar` y `escribir_fuente` (§R1).
- «matriz recalcula CUMPLE desde criterios+aserciones»: no reevalúa nada (M2, N2a y N2b).
- «control negativo por aserción (prueba 15)»: es contra un estado vacío (§R2).
- «preserva_sentido justificado caso a caso»: 35/36 con la misma frase.
- «sondas P1–P9 DETECTA»: son las literales de la revisión de `1ac661b`. Las variantes de la revisión D2 siguen abiertas.
- «relevos completos»: §R4.

Se explica por la fecha (§Contexto), pero no cumple D3-R8.

## `pruebas_arnes.py` (16/16) — leído, no ejecutado

**No lo he ejecutado: invoca el producto real.**
- Las pruebas 1, 2, 6, 14 y 16 ejecutan `ejecutar_caso.py` sobre la candidata por defecto (`/workspace/base_414_main`), que lanza `verificacion_entradas.py` real.
- Las pruebas 4 y 13 copian `personaje_v2/scripts` reales a una candidata falsa y los ejecutan. La 4 lanza `ficha.py`; no he comprobado si `ficha.py` llama a LibreOffice.
- La prueba 7 y el final escriben en la carpeta publicada (`MATRIZ_EJECUCION.csv`, `recuentos.json` y `pruebas_arnes.log`).

**Qué cubre y si discrimina:**

| Prueba | Discrimina | Observación |
|---|---|---|
| 1, 2 | sí (positivo y negativo real) | — |
| 3 candidata vacía | sí | — |
| 4 artefacto heredado | sí | — |
| 5 matriz sin evidencias | sí | — |
| 6 salida mutada → aserción FALLA | sí, para la aserción | No prueba la matriz |
| 7 recuentos == CSV | **no** | Compara dos salidas del mismo generador. Además sobrescribe lo publicado |
| 8, 9 especificación vacía / sin `afirma` | sí, para el literal | No cubre P1v ni N3 |
| 10 ruta `../` en una aserción | sí, para el literal | No cubre `copiar_artefacto`, `guardar`, `escribir_fuente` ni rutas absolutas |
| 11 negativo sin universo | sí | — |
| 12 resultado forjado de 2 campos | solo el literal | No cubre M2 (4 campos), N2a ni N2b |
| 13 rastreado modificado | sí, para el literal | No cubre skip-worktree, assume-unchanged, no rastreados ni exclude |
| 14 un log por ejecución | sí | No cubre `ARNES_EVIDENCIAS_LIMPIAS=0` ni ids `.`, `""` o `../` |
| 15 control negativo | **no** | Estado vacío; no detecta Q1-027 C4 |
| 16 marcas SIMULADA | parcial | `revisor_sim` usa `any`; Q1-001 y Q1-002 no dan un `revisor` propio, así que no prueba el hueco de `paso.get("revisor", REVISOR)` |

Ninguna de las 16 pruebas cubre una variante de D3-R1, ni el estado previo de D3-R2. Que den **16/16 PASA no dice nada de los defectos D3**.

## Defectos con contraejemplo mínimo

| ID | Gravedad | D3-R | Defecto | Contraejemplo mínimo (sonda) |
|---|---|---|---|---|
| D3-1 | material | R1 | Lectura fuera del caso con `copiar_artefacto` | `{"op":"copiar_artefacto","archivo":"../../Q1-036/Viscofan/informe_provisional.md","guardar":"x.md"}` → COMPONENTE_OK (P3va); con ruta absoluta, igual (N1b) |
| D3-2 | material | R1 | Escritura fuera del caso | `guardar:"../Q1-036/07_informe_provisional.md"` → Q1-036 = `{}` (P3vb); `escribir_fuente nombre:"../../../Q1-036/Viscofan/verificacion_entradas.json"` pisa el registro de Q1-036 (N1a) |
| D3-3 | material | R1 | La matriz no vuelve a evaluar | Resultado de 4 campos con `spec_sha256` → CUMPLE (M2); salidas vaciadas → CUMPLE (N2a); candidata y banco ajenos con harness 2.0 → CUMPLE (N2b) |
| D3-4 | material | R1 | Aserciones sobre archivos del arnés | `texto_contiene run:Viscofan/fuentes_sinteticas/f6_031_precio.txt "710"` → COMPONENTE_OK (N3); `ejecucion.log` (P1v) |
| D3-5 | material | R1 | El id no se valida antes de `rmtree` | `"id":"."` (P9w), `"id":""` (N4b) y `"id":"../fuera"` (N4): borran evidencia propia o ajena antes de validar |
| D3-6 | menor | R1 | La candidata «limpia» admite alteraciones ocultas | skip-worktree (P8va), assume-unchanged (N5a), no rastreado (P8vb) y `.git/info/exclude` (N5b) → COMPONENTE_OK con salida alterada |
| D3-7 | material | R2 | La prueba 15 es vacía; Q1-027 C4 no discrimina y cuenta | C4.0/C4.1 V en el estado previo; la prueba 15 reproducida da `pasan_en_vacio: []` |
| D3-8 | material | R2 | Q1-034 C1, tautológico | C1.0/C1.1 V con solo el registro del arnés; clase final `dato_publicado` con C1 CUMPLE; con un producto que devuelve un eco, COMPONENTE_OK |
| D3-9 | material | R2/R3 | Q1-026 C1 no está anclado al origen; la clasificación no depende del resultado | P7v2: «CAMBIO inválido» + líneas reales → COMPONENTE_OK → BLOQUEO_ENTORNO; M3: ERROR_ENTORNO → BLOQUEO_ENTORNO |
| D3-10 | menor | R3 | La deuda neta 210 de Q1-026 solo aparece como texto | El CAMBIO solo declara C24; no hay entrada de deuda 300 ni cálculo observado |
| D3-11 | material | R4 | El relevo depende de PARCIAL_COMPONENTE y no es por caso | Q1-005 → COMPONENTE_FALLA: solo «revisión externa por otro contexto»; 29× el mismo texto; Q1-032 sin paso de agente; Q1-028 y Q1-032 con `comando_relevo` null |
| D3-12 | material | R5 | `preserva_sentido` genérico y falso | 35/36 con la misma frase; falso en Q1-001, Q1-032, Q1-034 y Q1-027 |
| D3-13 | menor | R5 | Regresión de Q1-027: caja verificada 45.054 miles en vez de 95 millones del banco | `piloto/Q1-027.json` paso 3, `valor_fuente: 45054` |
| D3-14 | material | R5 | El MAPA sobredeclara cobertura | Q1-027 índices 0 y 2; Q1-026 índice 2; Q1-025 índices 0–2; Q1-034 índice 0 |
| D3-15 | menor | R8 | ENTREGA no es por bloque ni sobre D3, y tiene afirmaciones inexactas | `ENTREGA.json`: `base_revisada_sha 1ac661b`; §D3-R8 |

## Lo que queda conforme y se conserva

- **D3-R6:** manifiesto con exit 0 y la lista igual a la carpeta.
- **Regeneración:** MATRIZ, MAPA, relevo y recuentos se reproducen byte a byte desde la evidencia publicada.
- **Evidencia v3:** harness 3.0, `spec_sha256` = especificación del disco, `candidata_sha` observado `957af65`, huella del banco, «[SIMULADO]» en los 22 `sellar` publicados, un log por ejecución, y 58/58 criterios reevaluados coinciden.
- **MAPA publicado** con los 109 criterios del banco y «sin aserción» donde no la hay.
- **Q1-026:** cifras del banco en el CAMBIO (95→90 y deuda 300 citada); stderr real separado en `errores_bloqueo.json`; C1 casa con el mensaje real (`fase1_historia.py … ipal`); origen intacto y la candidata sin escribir.
- **Q1-027:** C2 y C3 siguen discriminando.
- **Lo ya cerrado en D2, que se mantiene:** P1, P2, P3 (lectura literal), P5, P7 (residuo y origen), P8 (rastreado modificado) y P9 (un log); `verify` sin `|| true`; banco fijado por SHA; D2-R7 cerrado con límites en el código (no reabierto).
- **Declaración de 0/36 casos completos del personaje**, y los 29 CUMPLE presentados como de componente.

## Límites de esta revisión

- Las sondas usan stubs y no dicen nada del comportamiento de Munger.
- No puedo afirmar que la evidencia publicada salga de una reejecución real: solo que es coherente, que es v3 y que no es la evidencia anterior en los archivos que la identifican (logs y resultados).
- No he ejecutado `pruebas_arnes.py`, `ejecutar_todo.sh` ni el producto.
- No he auditado una por una las 59 filas «asercion» del MAPA.
- No he verificado la base 4.14 ni la materialización del autor.
- D3-R7 no se ha revisado a fondo; solo hay constataciones.
- Esto no es aceptación, ni integración, ni aptitud para dinero real.

## Archivos del revisor

- Este informe: `<rev_D3>/REVISION_D_d032691.md`.
- En `<rev_D3>/sondas/`:
  - `sondas_arnes_d3.py`, `sondas_arnes_d3.json` y `sondas_arnes_d3.stdout`: variantes R1 y N1–N5, R2, R3 y R4;
  - `sondas_arnes_d2_original_sobre_d032691.json` y `.stdout`: la sonda D2 original, sin cambios, contra `d032691`. Su marcador de ruta se ha cambiado a `<rev_D3>`;
  - `comprobaciones_d3.sh` y `comprobaciones_d3.log`.
- Las sondas originales de la revisión D2 siguen sin sustituir en `<rev_D2>/sondas/`.
