# Revisión independiente · respuesta D2 de Mistral D · bloques 1 (`3934bc9`) y 2 (`5f4b2a2`)

- **Revisor:** subagente Claude, en un contexto distinto del autor (Mistral D). No he escrito este material.
- **Fecha:** 2026-11-17.
- **Objeto:**
  - `origin/mistral/d-qwen-aceptacion`, del commit `3934bc9` («D2-R1/R7 (bloque 1): arnés v3») sobre `1ac661b`;
  - el commit `5f4b2a2` («D2-R2/R3/R4/R5 (bloque 2)») sobre `3934bc9`. Lo añadió el coordinador al ampliar el alcance.
- **Referencias:**
  - `CORRECCION_D2.md` y `REVISION_D_1ac661b.md`, con sus sondas, en `origin/coordinacion/cierre-v2`;
  - banco `4745f38` (`resultados_qwen/q1_v2/banco_revisado`; manifiesto 57/57, exit 0);
  - `MECANISMO_PERSONAJE.md` (`coordinacion/cierre_v2/pruebas_candidata/957af65/`).
- **Método:**
  - Copias extraídas con `git archive` en `<rev_D2>/entrega` (`3934bc9`), `<rev_D2>/entrega2` (`5f4b2a2`) y `<rev_D2>/banco` (`4745f38`). Python siempre con `-I -B`.
  - Las sondas usan una **candidata falsa con scripts de juguete (stubs)** que imitan la interfaz del producto. Por eso miden la lógica del arnés y de los generadores, no Munger.
  - Para atribuir los fallos he leído en solo lectura (`git show 957af65:…`) `cambiar_base.py` y `tools/base_414.py`.
  - No he ejecutado el producto, LibreOffice, agentes, la red, `pruebas_arnes.py`, `ejecutar_todo.sh` ni `preparar_entorno.sh` completo.
  - No he hecho commit, push ni cambios en ningún repositorio (`git status` limpio).

## Dictamen

**Ninguno de los dos bloques puede aceptarse como cierre de D2.**

**Bloque 1** (arnés v3):
- Cierra las sondas literales P1, P2, P3 (lectura), P5, P7 (residuo y origen reutilizado), P8 y P9.
- Las variantes no literales abren huecos equivalentes:
  - un artefacto de otro caso se copia sin control y da CUMPLE;
  - un `guardar` sobrescribe la evidencia de otro caso;
  - aserciones sobre el log del propio arnés dan COMPONENTE_OK;
  - un script de la candidata alterado con `skip-worktree`, o un archivo no rastreado en `scripts/`, pasan como candidata limpia;
  - un `id` «.» borra la evidencia de todos los casos.
- No toca la matriz: P4 sigue dando CUMPLE, y además la matriz rechaza como ERROR un resultado v3 legítimo.

**Bloque 2** (especificaciones y generadores):
- Corrige en la especificación las cifras de Q1-026 y Q1-027 y separa Q1-026 como BLOQUEO_ENTORNO en el generador.
- Pero:
  - las aserciones nuevas de Q1-026 C1 y Q1-034 C1 **fallarían con el producto real**: el prefijo `ipal` no casa con el stderr publicado, y la clase de `aux:litigio` ya no es `hipotesis` cuando se evalúa;
  - el «rango acreditado» lee lo que escribe el propio arnés;
  - la «prueba 15» de controles negativos es vacía;
  - la matriz acepta un resultado forjado de cinco campos;
  - al regenerar sobre la evidencia publicada salen 0 CUMPLE y 30 relevos sin ningún paso de agente;
  - `preserva_sentido` lleva la misma frase en 35 de 36 casos.

**En ninguno de los dos bloques** se han regenerado ni actualizado las salidas publicadas: evidencias, MATRIZ, relevo, `MAPA_CRITERIOS_BANCO.csv` (no existe), `pruebas_arnes.log`, HALLAZGOS, RESUMEN, ENTREGA ni manifiesto. El manifiesto falla en 4 archivos en `3934bc9` y en 11 archivos más 1 sin registrar en `5f4b2a2`.

**Se sigue declarando correctamente que hay 0 casos del personaje ejecutados.**

| D2-R | Declarado en | Veredicto |
|---|---|---|
| **R1** (a,b,c,d,e) | bloque 1 (a,b,c,e) · bloque 2 (d) | **ABIERTO**: (a)(b)(e) cerrados con límites; (c) y (d) abiertos |
| **R2** | bloque 2 (el bloque 1 lo anuncia en un docstring) | **ABIERTO** |
| **R3** | bloque 2 (el bloque 1 aporta la separación del stderr y RUN_DIR) | **ABIERTO**: corregido en especificación y generador, no en lo publicado; C1 mal construido |
| **R4** | bloque 2 | **ABIERTO** |
| **R5** | bloque 2 | **ABIERTO**: la tabla existe como dato y queda CON LÍMITES; `preserva_sentido`, textos caducados y log siguen abiertos |
| **R6** | ninguno | **ABIERTO**, y peor: no lo declara ningún bloque |
| **R7** (a,b,c) | bloque 1 | **CERRADO CON LÍMITES** (código); la evidencia publicada no se ha regenerado |

## Comandos ejecutados (todos sobre copias aisladas)

| Comando | Exit | Resultado |
|---|---|---|
| `git archive 3934bc9 \| tar -x -C <rev_D2>/entrega`; igual con `5f4b2a2 → entrega2` y `4745f38 → banco` | 0 | Copias |
| `sha256sum -c MANIFIESTO_SHA256.txt`, desde `entrega/resultados_qwen/ejecucion_d` | **1** | Fallan 4: RESUMEN, `ejecutar_caso.py`, `lib_arnes.py`, `preparar_entorno.sh` |
| ídem, desde `entrega2/…` | **1** | Fallan 11 (RESUMEN, 3 especificaciones, `adaptaciones.json`, 6 scripts). `generar_correspondencia.py` no está en el manifiesto |
| `sha256sum -c` del banco `4745f38` | 0 | 57/57 |
| `python3 -I sondas/sondas_arnes_d2.py entrega/… entrega2/… banco/… sondas/sondas_arnes_d2.json` | 0 | Sondas del arnés en los dos bloques, matriz, R2 y regeneración |
| `bash sondas/sonda_verify_preparar.sh …/preparar_entorno.sh <dir>` | 0 | Fragmento `verify` con un `base_414.py` de juguete (§R7c) |
| `bash sondas/comprobaciones_d2.sh <repo> <rev_D2>` | 0 | Manifiestos, diff, binarios, secretos, ENTREGA y plantilla; log en `sondas/comprobaciones_d2.log` |

---

## Bloque 1 · `3934bc9`

### D2-R1 — ABIERTO

| Sonda | Antes (`1ac661b`) | `3934bc9` | `5f4b2a2` | Veredicto |
|---|---|---|---|---|
| **P1** especificación vacía | exit 0 COMPONENTE_OK | **exit 2 ERROR_ESPECIFICACION** | igual | Literal cerrado |
| **P2** `afirma: []` | exit 0 COMPONENTE_OK | **exit 2 ERROR_ESPECIFICACION** | igual | Literal cerrado |
| **P1v/P2v (nueva)** `pasos:[nuevo_expediente]` con aserciones `archivo_existe ejecucion.log` y `texto_contiene ejecucion.log "# Caso"` | — | **exit 0 COMPONENTE_OK** | igual | Falso positivo: ninguna aserción mira una salida del producto |
| **P3** aserción sobre `../Q1-036/…` | CUMPLE | **exit 1 ERROR** («ruta fuera del RUN_DIR/evidencias del caso») | igual | Literal cerrado |
| **P3va (nueva)** `copiar_artefacto archivo="../../Q1-036/Viscofan/informe_provisional.md"` y luego una aserción sobre la copia | — | **exit 0 COMPONENTE_OK**; artefacto «nuevo: true», productor = paso `plantilla` | igual | **Abierto**: la contención solo cubre la lectura de las aserciones, no `copiar_artefacto` (`lib_arnes.py:156-178`) |
| **P3vb (nueva)** `comprobar` con `guardar="../Q1-036/07_informe_provisional.md"` | — | exit 0; **la evidencia de Q1-036 queda sustituida por `{}`** | igual | **Abierto**: `guardar` no se contiene (`lib_arnes.py:140-142`) |
| **P4** `resultado_ejecucion.json` forjado con dos campos | CUMPLE | **CUMPLE** (`generar_matriz.py` sin cambios en este bloque) | sin CUMPLE | Ver bloque 2 |
| **P4w (nueva)** resultado v3 legítimo (Q1-002 con `harness_version 3.0`) | — | **ERROR (COMPONENTE_OK)**: la matriz solo acepta `"2.0"` (`generar_matriz.py:67`) | CUMPLE | Incoherencia arnés/matriz dentro del bloque 1 |
| **P5** Q1-034 sin `universo` | C1 CUMPLE | **C1 FALLA** («salida sin universo positivo») | C1 FALLA | Literal cerrado |
| **P5v (nueva)** Q1-034 con `{"universo":321,"comprobadas":[],"datos_como_hipotesis":[],"pendientes":["…sin mención de rango"]}` | — | **C1 CUMPLE, COMPONENTE_OK** | C1 FALLA (por otra causa, §R2) | Con límites: `universo` mide el registro entero (321 en el producto real), no la entrada evaluada; el negativo sigue sin acreditar el rango |

**Sub-veredictos:**
- (a)(b): CERRADO CON LÍMITES. La validez solo exige listas no vacías; una aserción tautológica pasa.
- (c): ABIERTO. La prueba de cierre pedía que «una ruta fuera del RUN_DIR del caso dé ERROR». P3va lee y P3vb escribe fuera del caso con exit 0.
- (d): no tratado en el bloque 1. Ver el bloque 2.
- (e): CERRADO CON LÍMITES.

Más observaciones:
- La especificación no se valida contra un esquema. Una aserción `{}` provoca un `KeyError` y el caso termina sin `resultado_ejecucion.json`. Es un fallo, pero no un ERROR_ESPECIFICACION.
- La nueva aserción `json_entrada_campo` no la usa ninguna especificación del bloque 1. La usa Q1-034 en el bloque 2.

### D2-R7 — CERRADO CON LÍMITES

**(a) Marca de simulada:**
- Las comprobaciones dadas como diccionario reciben `_simulada` y «[SIMULADO]» (`lib_arnes.py marcar_simulada`, `ejecutar_caso.py:173-175`).
- `REVISOR` y `EXTRACTOR` llevan «[SIMULADO]».

Límites (sonda R7a):
- `sellar` usa `paso.get("revisor", REVISOR)`. Un `revisor` dado por la especificación pasa sin marca: se observa `--revisor "revisora independiente (nombre de persona)"`.
- Una auxiliar creada sin comprobación recibe del arnés `{"resultado":"pendiente",…}` sin `_simulada` (`lib_arnes.py:264`).
- Ninguna especificación actual hace ninguna de las dos cosas: es un hueco latente.
- La evidencia publicada no se ha regenerado. Los 30 `resultado_ejecucion.json` son de `harness 2.0`, y en 8 casos (Q1-002, 014, 018, 019, 020, 025, 027 y 036) el `sellar` del log y del resultado lleva «revisor independiente de prueba D (arnés externo)» sin «[SIMULADO]».

**(b) Un log por ejecución:**
- P9: con dos ejecuciones queda **1** cabecera.

Límites:
- P9v: con `ARNES_EVIDENCIAS_LIMPIAS=0` el log vuelve a acumularse (2 cabeceras) y el resultado no registra esa opción.
- P9w (defecto nuevo de este bloque): con una especificación con `"id": "."`, el `rmtree` de `Caso.__init__` borra **la evidencia de todos los casos**. El borrado ocurre antes de validar la especificación, y la sonda comprueba que la evidencia de Q1-001 desaparece. Con `id` del tipo `../x` saldría del directorio.
- Además, cualquier ejecución fallida (por ejemplo ERROR_ENTORNO) borra la evidencia previa del caso en `EVIDENCIAS` (por defecto `ejecucion_d/evidencias`, es decir, la publicada).
- Los 9 logs acumulados publicados (Q1-002, 014, 017, 018, 019, 020, 026, 027 y 036) siguen igual.

**(c) SHA observado y estado del árbol:**
- P8 (archivo rastreado modificado): **exit 2 ERROR_ENTORNO**.
- El residuo `pruebas_d/` en la candidata da ERROR_ENTORNO (P7a).
- `candidata_sha` es ahora el observado, y se registran `spec_sha256` y `banco_casos_sha256` (R7c).

Límites:
- P8va: un script rastreado alterado y ocultado con `git update-index --skip-worktree` **pasa**. Da COMPONENTE_OK, `git status` sale vacío y el log muestra que se ejecutó el script alterado.
- P8vb: se admite cualquier archivo no rastreado salvo `pruebas_d`. Un `scripts/override.txt` no rastreado cambia la salida del stub y el caso sale COMPONENTE_OK. Esto contradice el docstring («solo se admiten no rastreados de la base materializada»).
- No se comprueba la huella de los binarios materializados durante la ejecución.

`base_414.py verify` en `preparar_entorno.sh:31-33`:
- Ya no lleva `|| true`, y el código lo respeta: con un `base_414.py` de juguete incompleto da **exit 1**; completo, exit 0.
- Defecto menor: el mensaje final lee `r['good']`, una clave que `base_414.py` no produce (produce `verified`). Con la base completa imprime un `KeyError` y «base 4.14 verificada completa ()».
- `verify` se ejecuta antes del `git checkout` de la candidata, y `/tmp/base_414_verify.json` es una ruta fija compartida.

### D2-R2 y D2-R3 en el bloque 1

- El docstring de `ejecutar_caso.py:12-13` afirma que «pruebas_arnes.py evalúa cada aserción contra un estado previo vacío». En `3934bc9`, `pruebas_arnes.py` no cambió, así que la afirmación era falsa en ese commit. La prueba llega en el bloque 2 (§R2).
- Q1-026: ahora se trabaja bajo `RUN_DIR` y el origen se recrea siempre.
  - P7b: el origen mutado preexistente no se reutiliza y la candidata queda limpia.
  - Pero con la especificación del bloque 1, C1 **sigue dando CUMPLE** con un fallo ajeno que contiene la subcadena.
  - `errores_bloqueo.json` clasifica esa línea como «pdftotext».
  - Su `nota` es una constante («también hay errores de ipal/AR_2019/AR_2020») que se escribe aunque esos errores no existan (P7b).

---

## Bloque 2 · `5f4b2a2`

### D2-R1(d) · matriz — ABIERTO

`generar_matriz.py` v3 exige ahora `harness_version` 2.0/3.0, COMPONENTE_OK, criterios no vacíos y todos CUMPLE_COMPONENTE, y además un `spec_sha256` igual al de la especificación en disco.

- P4 literal (dos campos): **sin CUMPLE**. Cerrado.
- **P4v (nueva):**
  - Contraejemplo: borrar toda la evidencia de Q1-001 y escribir solo `{"harness_version":"3.0","estado_caso":"COMPONENTE_OK","spec_sha256":"<sha256 de piloto/Q1-001.json>","criterios":[{"id":"C1","estado":"CUMPLE_COMPONENTE"}]}`.
  - Resultado: **Q1-001 PARCIAL_COMPONENTE / CUMPLE**.
  - Por qué: la matriz sigue confiando en campos que se declaran a sí mismos. No vuelve a evaluar ninguna aserción sobre la evidencia, no compara los criterios del resultado con los de la especificación (aquí hay 1 de los suyos) y no comprueba que existan los archivos evaluados.
  - La prueba de cierre («recalcular desde los criterios y las aserciones») no se cumple.
- **Efecto sobre lo publicado:** la evidencia publicada es v2 y no tiene `spec_sha256`. Al regenerar con el código del bloque 2:
  - salen **29 «ERROR (COMPONENTE_OK)», 1 BLOQUEO_ENTORNO, 6 NO_EJECUTADO y 0 CUMPLE**;
  - la MATRIZ publicada dice **30 CUMPLE**, y no coincide byte a byte con la regenerada.
  - La prueba 7 de `pruebas_arnes.py` v3 regenera la matriz **sobre `L.EVIDENCIAS` publicada**, así que sobrescribiría la MATRIZ del repositorio con ese resultado y aun así daría PASA, porque solo compara el CSV con `recuentos.json`.

### D2-R2 · aserciones que no prueban nada — ABIERTO

**Q1-027 C4 no discrimina.** Sonda R2: cada aserción de Q1-027 se evalúa en tres estados, que son el vacío, el estado previo (02 copiado como 03) y la evidencia publicada.

| Aserción | Vacío | Estado previo | Publicada |
|---|---|---|---|
| C2.0 desactualizada por sha256 | F | **F** | V |
| C2.1 no comprobada | F | **F** | V |
| C3.0 «rechazadas 1» | F | **F** | V |
| C4.0 / C4.1 `apto_por_entradas == false` | F | **V** | V |

- La propia especificación etiqueta C4 como «NO discriminante», pero C4 **sigue siendo un criterio que cuenta para COMPONENTE_OK**.
- `adaptaciones.json` lo hace corresponder con el criterio 2 del banco («la actividad no dependiente continúa; el nuevo contraste usa deuda 300»), que no tiene nada que ver con él. Ninguna aserción toca la deuda 300.

**La prueba 15 de `pruebas_arnes.py` es vacía:**
- Solo comprueba que todas las aserciones fallen **sin ningún archivo**. Cualquier aserción falla ahí por «falta archivo».
- No detecta C4. Tampoco detectaría la C1 antigua de Q1-026, que acepta cualquier fallo con la subcadena.
- El encargo pedía que fallara «sobre el estado previo o con un mensaje de otro origen».

**Q1-034, «rango acreditado»:**
- C1.0 (`hipotesis.limites contiene "0-200"`) y C1.1 (`clase == "hipotesis"`) leen `run:Viscofan/verificacion_entradas.json`. Es **el registro que escribe el propio arnés** (`poner_entrada`): son tautologías sobre la precondición, no sobre el producto.
- C1.3 (`pendientes` contiene «rango acotado») casa con la `nota` que escribe el arnés, «rango acotado preservado como hipótesis; sin punto». El producto real la devuelve tal cual: así se ve en la evidencia publicada `01_comprobar_rango_acotado.json`.
- **Además, C1 fallaría siempre.** El paso 5 de la especificación cambia `aux:litigio` a `clase: "dato_publicado"`, y las aserciones `run:` se evalúan sobre el registro final. P5, P5v y P5w lo muestran: incluso con un stub que devuelve la nota, C1.1 da «clase = 'dato_publicado' → FALLA».
- La especificación no se ha ejecutado contra el producto, y la evidencia publicada sigue siendo la de v2.

**Q1-026:**
- C3 asevera sobre `CAMBIO_Q1-026.json`, que es la copia que hace el arnés del `cambio` de la propia especificación. Es una comprobación estática de la especificación, no del producto.
- C1, con un fallo ajeno que imprime las líneas con los prefijos esperados (P7v), da **CUMPLE**. Sigue siendo una prueba por subcadena.

### D2-R3 · Q1-026 — ABIERTO

Corregido en la especificación (`bloque2/Q1-026.json`):
- C24 = 90, con la cita de `f5_026_nota.txt` (caja 90; deuda financiera 300). El texto de la cita está parafraseado con «(fixture f5_026_nota.txt)» intercalado, así que no es una subcadena literal.
- Descripción con 95→90 y deuda neta 300−90=210.
- Bloque `evidencia` restaurado: `Análisis!C24` E/M con la misma estructura que en `b42f453`, con las cifras del banco.
- `bloqueo_entorno` declarado.
- `generar_matriz` clasifica BLOQUEO_ENTORNO y no lo cuenta como CUMPLE.
- `generar_relevo` lleva 210 y la nota sobre ipal, AR_2019 y AR_2020.

Pendiente:
- **Lo publicado no ha cambiado.**
  - `evidencias/Q1-026/CAMBIO_Q1-026.json` sigue con `valor 45.0`, «caja 45000 miles … deuda 82019» y sin bloque `evidencia` de nivel superior.
  - La MATRIZ publicada cuenta Q1-026 como PARCIAL_COMPONENTE / CUMPLE.
  - El relevo publicado sigue con 45.000/82.019/37.019.
  - El `paquete_runtime` regenerado dice «evidencias/Q1-026/CAMBIO_Q1-026.json (coherente con el banco…)», y el archivo al que remite no lo es.
- **C1 fallaría con el stderr real.**
  - P7c reproduce de forma literal el stderr publicado (`cambiar_base_preparar.txt`). La aserción `prefijo "ipal"` da **FALLA**, porque la línea real empieza por «fase1_historia.py construir falló: ipal: …».
  - El caso saldría COMPONENTE_FALLA. Aun así, la matriz lo seguiría llamando BLOQUEO_ENTORNO.
- **La clasificación no depende del resultado.** Con un `resultado_ejecucion.json` de Q1-026 en ERROR_ENTORNO y sin criterios, la matriz da **BLOQUEO_ENTORNO** (M3). Basta con que la especificación lleve `bloqueo_entorno` y con que exista un resultado.
- **Límite económico.** El CAMBIO solo declara `Análisis!C24` (la caja). Ninguna entrada lleva la deuda 300 a la copia del expediente Viscofan. No se demuestra de dónde saldría el 210, y no se descarta que el recálculo use una deuda ajena a las fuentes del caso, que es justo una conducta inaceptable del banco. El relevo lo deja en «actualizar verificacion_entradas.json … deuda 300». La cifra pertenece a «SINTETICA CUATRO S.A.» y se inyecta en Viscofan; la justificación de `preserva_sentido` no lo trata.

### Q1-027 (cifras del banco) — CERRADO CON LÍMITES

- Cifras alineadas: 95 verificado el 05/11, 80 el 10/11 y deuda 300, todo en millones (95000→80000 miles con `escala 0.001`).
- C2 y C3 discriminan.
- C4 no discrimina y cuenta (§R2).
- La invalidación de la aprobación y el esperado 220 siguen en relevo.
- La especificación tiene la clave `harness_version` duplicada.
- La evidencia publicada sigue siendo la de 45054→80054.

### D2-R4 · relevos — ABIERTO

- **Q1-028 y Q1-032** (generador regenerado): nombran lo pendiente, quién lo hace y lo que necesita (reaprobación con auditor nuevo y deuda neta 245; recuento 4/1/5 o NO_OBSERVABLE).
  - Siguen con `comando_relevo: null`.
  - El relevo de Q1-032 no nombra ningún paso de agente, aunque su criterio 1 del banco dice «relevo: fase A … con agente real».
  - Son entradas **escritas a mano por caso** (`generar_relevo.py:70-75`).
- **El relevo publicado no ha cambiado:** Q1-028 y Q1-032 dicen todavía «nada pendiente declarado».
- **Regresión general.** El paso de agente solo se añade si `estado_ejecucion == PARCIAL_COMPONENTE`. Si no, cae en «revisión externa por otro contexto».
  - Al regenerar sobre la evidencia publicada, **30 paquetes** (Q1-001…025, 027, 029, 032, 034 y 036) quedan **sin ningún paso de agente**.
  - Ocurrirá también con cualquier caso que dé COMPONENTE_FALLA o ERROR, como Q1-034 por lo dicho en §R2.
  - Es el mismo defecto que se pedía corregir.
- **Recorrido del personaje.** `RECORRIDO_PERSONAJE` es global: pasos 5/6/8/10/13, modelos y fase C con el mismo agente, que coinciden con `MECANISMO_PERSONAJE.md`.
  - Pero no dice, **caso por caso**, qué estado del producto preparar, qué fases recorrer ni qué artefacto mirar por criterio, que es lo que exige `MECANISMO_PERSONAJE.md` §4.
  - En los criterios de agente, `criterios_banco[].razon` repite «relevo: fase A … con agente real». En Q1-031 remite a un «precio histórico 14,20 EUR» dentro de un «fase1_v63.json del expediente de prueba» que no se identifica.

### D2-R5 · matriz, correspondencia y textos — ABIERTO

**Tabla de correspondencia: CON LÍMITES.**
- `adaptaciones.json → cobertura_banco` cubre los 109 criterios del banco, uno por índice. Por recuento propio: 59 «asercion», 31 «sin_asercion», 12 de relevo, 6 de decisión del usuario y 1 de bloqueo.
- `generar_correspondencia.py` la convierte en CSV, pero **`MAPA_CRITERIOS_BANCO.csv` no está publicado**.
- La tabla está escrita a mano y sobredeclara cobertura en las filas que he revisado:
  - Q1-027, índice 0 (aprobación invalidada) → C2: la aprobación no se observa.
  - Q1-027, índice 2 → C4: no discrimina y trata de otra cosa.
  - Q1-026, índice 2 («no se cambian fórmulas ni palancas») → C3: tautología sobre la especificación.
  - Q1-025, índices 0, 1 y 2 → la misma C1: la coincidencia por los seis ejes y la referencia en la matriz no se observan.
  - Q1-034, índice 0 → C1, que es tautológica y además falla.
- Solo he revisado esas filas. No he auditado una por una las 59.

**`preserva_sentido`: ABIERTO.**
- Vale «si» en los 36 casos.
- En 35 la justificación es la misma frase: «la adaptacion usa los fixtures y cifras del banco; la spec y las aserciones se evaluan contra ellos».
- La frase es falsa al menos en:
  - Q1-001, donde la línea cero pasa a ser `Historia!C23` arrendamientos;
  - Q1-032, donde el universo es 321 frente a los 5 del banco;
  - Q1-034, cuya adaptación sigue diciendo «parámetro de configuración como rango», aunque la especificación usa `aux:litigio`.
- `generar_matriz.py:123` mantiene un valor por defecto `"sí"`.

**Textos caducados:**
- `HALLAZGOS.md:24` («27 ejecuciones propias (28 especificaciones…)») no ha cambiado.
- La adaptación de Q1-025 sí se ha corregido. La de Q1-034 no.
- `RESUMEN_PARA_INTEGRADOR.md:18` («rango 0–200 preservado») y `ENTREGA.json:89` («30 casos … 8/8 PASA») no han cambiado.

**`pruebas_arnes.log`:** no se ha regenerado. Sigue siendo el de `9ed248a`, con 8 pruebas. Las «16 pruebas» de v3 no tienen ningún log publicado.

### D2-R6 · manifiesto — ABIERTO (sin declarar)

- Ningún bloque lo trata ni lo menciona.
- `sha256sum -c` da exit 1 en ambos commits: 4 fallos en `3934bc9`; 11 fallos más 1 archivo sin registrar en `5f4b2a2`.

---

## 2 · Qué queda para bloques siguientes y si se declara

**No se declara en ningún sitio:**
- `ENTREGA.json` no ha cambiado desde `1ac661b`: sigue con `base_revisada_sha = bdcbba7` y «Bloques 3/4 … cierre de la matriz de 36».
- No hay ningún otro archivo de entrega. `CORRECCION_D2` §3 pedía «un commit por bloque con `ENTREGA.json`» y la lista D2-R1…R7 con su comando, código y salida.
- Lo único que hay son los mensajes de commit («bloque 1», «bloque 2») y los docstrings.

**Pendiente según esta revisión:**
- R1(c): `copiar_artefacto` y `guardar`.
- R1(d): volver a evaluar las aserciones sobre la evidencia.
- R2: un control negativo real frente al estado previo; retirar C4 o etiquetarlo fuera del cómputo; rehacer Q1-034 C1.
- R3: regenerar la evidencia y lo publicado; corregir el prefijo `ipal`.
- R4: no depender de PARCIAL_COMPONENTE; detallar el recorrido por caso.
- R5: publicar el CSV; justificar `preserva_sentido` caso a caso; actualizar HALLAZGOS, RESUMEN y adaptaciones; regenerar el log.
- **R6**: manifiesto.
- **Regenerar todas las salidas** (evidencia v3, MATRIZ, MAPA, relevo, recuentos y log) con un `ENTREGA.json` nuevo.

## 3 · Precondiciones simuladas

- En el código, todo lo que escriben `comprobacion_verificada` y `marcar_simulada` lleva la marca.
- Excepciones (R7a): el `--revisor` dado por la especificación y la auxiliar creada por defecto. También van sin marca las fuentes, hipótesis y justificaciones que el arnés escribe en el registro; la marca solo está en la comprobación.
- En lo publicado, nada se ha regenerado: siguen los registros sin marca que señaló la revisión anterior.

## 4 · Aislamiento

| Punto | Resultado |
|---|---|
| Un log por ejecución | Sí en el código. Límites: opción `ARNES_EVIDENCIAS_LIMPIAS=0` sin registrar; `id` «.» que borra todo. Los 9 logs publicados siguen acumulados |
| SHA observado y árbol limpio | Sí para los archivos rastreados modificados. Se escapan `skip-worktree` y los archivos no rastreados en `scripts/` |
| `verify` sin `\|\| true` | Sí. Defecto menor en el mensaje (`good`) |

## 5 · Recuentos

- Se siguen declarando **0 casos del personaje ejecutados** (`RESUMEN_PARA_INTEGRADOR.md:10,30`; `ENTREGA.json:16,83`). Los generadores nuevos no presentan ninguna salida como ejecución real; `PAQUETES_RELEVO.json` repite la regla «una respuesta del arnés no es ejecución del producto».
- Lo publicado sigue sobredeclarando el componente: 30 CUMPLE (incluido Q1-026, que el propio bloque 2 reclasifica), «rango 0–200 preservado» y «8/8 PASA».
- Al regenerar con el código entregado salen 0 CUMPLE.

## 6 · Higiene

- `git diff --name-only 1ac661b 3934bc9`: 3 scripts.
- `git diff --name-only 1ac661b 5f4b2a2`: 11 archivos (scripts, especificaciones y `adaptaciones.json`).
- En ninguno de los dos hay PDF, XLSX, ZIP, `__pycache__`, `.pyc`, binarios (`numstat`) ni patrones de secreto.
- `ENTREGA.json` tiene todas las claves de `PLANTILLA_ENTREGA.json`, pero no se ha actualizado para ninguno de los dos bloques.
- Manifiesto: ver §R6.

## Defectos con contraejemplo mínimo

| ID | Gravedad | Bloque | Defecto | Contraejemplo |
|---|---|---|---|---|
| D2-1 | material | 1 y 2 | Un artefacto de otro caso se copia y da CUMPLE | P3va: `copiar_artefacto "../../Q1-036/Viscofan/informe_provisional.md"`, exit 0 |
| D2-2 | material | 1 y 2 | `guardar` escribe en la evidencia de otro caso | P3vb: `guardar "../Q1-036/07_informe_provisional.md"`; Q1-036 queda `{}` |
| D2-3 | material | 1 y 2 | `id` «.» borra la evidencia de todos los casos antes de validar | P9w |
| D2-4 | material | 2 | La matriz acepta un resultado forjado de 5 campos sin evidencia | P4v (M2): Q1-001 CUMPLE |
| D2-5 | material | 2 | Q1-034 C1 es tautológico y además falla siempre (clase cambiada en el paso 5) | P5, P5v, P5w: «clase = 'dato_publicado' → FALLA» |
| D2-6 | material | 2 | Q1-026 C1 falla con el stderr real (`ipal` no es prefijo) y pasa con un fallo ajeno | P7c y P7v |
| D2-7 | material | 2 | La prueba 15 (control negativo) es vacía; Q1-027 C4 no discrimina y cuenta | Sonda R2 |
| D2-8 | material | 2 | Al regenerar: 0 CUMPLE y 30 relevos sin paso de agente | Regeneración |
| D2-9 | material | 1 y 2 | Salidas publicadas sin regenerar (Q1-026 a 45.000, relevos «nada pendiente», 30 CUMPLE) | `comprobaciones_d2.log` |
| D2-10 | material | 2 | `preserva_sentido` con la misma frase en 35/36; la correspondencia sobredeclara cobertura | §R5 |
| D2-11 | menor | 1 | Pasan aserciones tautológicas sobre el log del arnés | P1v/P2v |
| D2-12 | menor | 1 | `skip-worktree` y archivos no rastreados en `scripts/` pasan como candidata limpia | P8va y P8vb |
| D2-13 | menor | 1 | `ARNES_EVIDENCIAS_LIMPIAS=0` acumula sin registrarlo; `--revisor` de la especificación y auxiliar por defecto sin marca | P9v, R7a |
| D2-14 | menor | 1 | La matriz del bloque 1 rechaza resultados v3 | P4w (M4) |
| D2-15 | menor | 1 | `preparar_entorno.sh` imprime `KeyError 'good'` | `sonda_verify_preparar.log` |
| D2-16 | menor | 1 y 2 | Manifiesto roto; `ENTREGA.json` sin actualizar; el docstring del bloque 1 afirmaba una prueba que no existía | §R6, §2 |

## Lo que se puede conservar

- Cierre literal de P1, P2, P3 (lectura), P5, P7 (residuo y origen) y P8.
- Un log por ejecución por defecto.
- SHA observado, huella de la especificación y huella del banco.
- `verify` respetado.
- Banco fijado por SHA en `preparar_entorno.sh`.
- Q1-026 bajo `RUN_DIR`, con el stderr separado.
- Cifras del banco en las especificaciones de Q1-026 y Q1-027.
- C2 y C3 de Q1-027 discriminan.
- La clasificación BLOQUEO_ENTORNO existe.
- Hay una tabla de los 109 criterios del banco.
- Los relevos de Q1-028 y Q1-032 nombran lo pendiente en el generador.
- Se mantiene la declaración de 0 casos del personaje.

## Límites de esta revisión

- Las sondas usan stubs y no dicen nada del comportamiento de Munger. Las afirmaciones sobre lo que haría el producto real (P7c y Q1-034) se apoyan en la evidencia publicada (stderr y `pendientes`) y en la lectura del código de la especificación.
- No he ejecutado `pruebas_arnes.py` v3: invoca el producto.
- No he auditado una por una las 59 filas «asercion» de la correspondencia.
- No he verificado la base 4.14 ni la materialización del autor.
- Esto no es aceptación, ni integración, ni aptitud para dinero real.

## Archivos del revisor

- Este informe: `<rev_D2>/REVISION_D2_3934bc9_a_5f4b2a2.md`.
- En `<rev_D2>/sondas/`: `sondas_arnes_d2.py`, `sondas_arnes_d2.json`, `sondas_arnes_d2.stdout`, `sonda_verify_preparar.sh`, `sonda_verify_preparar.log`, `comprobaciones_d2.sh` y `comprobaciones_d2.log`.
- Las sondas originales siguen sin sustituir en `<rev_D>/sondas/`.
