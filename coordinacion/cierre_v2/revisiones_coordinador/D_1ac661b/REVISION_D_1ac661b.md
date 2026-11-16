# Revisión independiente · frente D (Mistral, aceptación Qwen) · `1ac661b`

**Revisor:** subagente Claude. Es un contexto distinto del autor (Mistral D) y no ha escrito este material.
**Fecha:** 2026-11-16.
**Objeto:** `origin/mistral/d-qwen-aceptacion` @ `1ac661b8efd954a5c79f91a493f9b082a9455e82`. Commits nuevos: `1fc46f3`, `d24dbe3`, `1ac661b`, sobre `bdcbba7`.
**Referencias:** revisión externa `d375d80` (`revision_externa/a_d_20261116/`), programa `origin/coordinacion/cierre-v2` @ `61deb19` (tareas D-HARNESS y D-36) y banco `4745f38`.
**Método:** copias aisladas extraídas con `git archive` en `rev_D/{entrega,revision,coord,banco}`. Python siempre con `-I`. No he ejecutado el producto Munger, LibreOffice, agentes ni nada que use la red. Las sondas del arnés usan una **candidata falsa con scripts de juguete (stubs)**, así que miden la lógica del arnés y no el producto. No he hecho commit, push ni cambios en ningún repositorio (`git status` limpio).

## Dictamen

**La entrega no puede aceptarse como cierre de D-HARNESS ni de D-36.** La corrección del D-R2 (artefacto heredado) funciona, y las dos sondas D del revisor externo ahora se detectan. Pero el arnés todavía da por buenos resultados vacíos o falsos. Q1-026 contiene cifras que contradicen el banco y su propia adaptación. Los relevos de Q1-028 y Q1-032 dicen «nada pendiente». El manifiesto no verifica. Ningún caso del personaje está ejecutado, cosa que la entrega reconoce correctamente.

| # | Criterio | Veredicto |
|---|---|---|
| 1 | Precondiciones simuladas declaradas y no contadas como ejecución real | **CUMPLE CON LÍMITES** |
| 2 | Aserciones por criterio; un resultado falso o vacío falla | **NO CUMPLE** |
| 3 | Aislamiento de artefactos; diff sin `__pycache__`, secretos ni binarios | **CUMPLE CON LÍMITES** |
| 4 | Q1-026 restaurado y coherente; evidencia de Q1-027 | **NO CUMPLE** (Q1-026) · **CUMPLE CON LÍMITES** (Q1-027, componente real con precondiciones simuladas) |
| 5 | Matriz de 36 recontada desde la evidencia; relevos | **NO CUMPLE** |
| 6 | Coherencia código/salidas; manifiesto SHA-256 | **NO CUMPLE** (manifiesto); la regeneración de matriz, recuentos y relevo coincide byte a byte |

## Comandos ejecutados (todos en copias aisladas)

| Comando | Exit | Resultado |
|---|---|---|
| `git archive 1ac661b`, `d375d80`, `origin/coordinacion/cierre-v2`, `4745f38` → `rev_D/...` | 0 | Copias extraídas |
| `cd entrega/resultados_qwen/ejecucion_d && sha256sum -c MANIFIESTO_SHA256.txt` | **1** | 196/197; falla `./RESUMEN_PARA_INTEGRADOR.md` |
| `cd banco/.../banco_revisado && sha256sum -c MANIFIESTO_SHA256.txt` | 0 | 57/57 |
| `BANCO_DIR=… python3 -I -B scripts/generar_matriz.py` (copia) | 0 | MATRIZ y recuentos **idénticos** a los publicados |
| `BANCO_DIR=… python3 -I -B scripts/generar_relevo.py` (copia) | 0 | PAQUETES_RELEVO.json **idéntico** al publicado |
| `python3 -I sondas/recuento_independiente.py …` | 0 | Recuento propio (§5); 0 incoherencias stdout↔archivo |
| `python3 -I sondas/sondas_arnes_d.py …` | 0 | 11 sondas del arnés (§2, §3); salida en `sondas/sondas_arnes_d.json` |
| `bash sondas/comprobaciones_revisor.sh rev_D` | 0 | Repite manifiestos y regeneración; log en `sondas/comprobaciones_revisor.log` |

No ejecutado: `pruebas_arnes.py` y `ejecutar_todo.sh`, porque invocan los scripts reales del producto (fuera del alcance permitido), y `preparar_entorno.sh`, porque usa la red, `gh` y una descarga de 1,13 GB. **No he reproducido ninguna ejecución de componentes del producto.** Lo que digo de ellas sale de los logs y JSON publicados.

---

## 1 · Precondiciones simuladas — CUMPLE CON LÍMITES

Lo que está bien:
- La simulación se declara para cada caso:
  - `lib_arnes.py:51-52,87` pone `precondiciones_simuladas` en cada `resultado_ejecucion.json`.
  - La cabecera de cada `ejecucion.log` dice «precondición SIMULADA».
  - Lo recogen `ENTREGA.json:76-78` y `RESUMEN_PARA_INTEGRADOR.md:30-32`.
- `comprobacion_verificada()` añade `"_simulada": true` (`lib_arnes.py:286-290`).
- No hay respuestas de agente simuladas. La entrega declara «0 casos completos del personaje» y no cuenta lo simulado como ejecución real del producto.

Límites:
- `ENTREGA.json:77` afirma que extractor y revisor van «marcados _simulada/SIMULADA» **en cada registro**. No es así en todos:
  - Las comprobaciones que la especificación da como diccionario no reciben `_simulada`. Por ejemplo, `Q1-002.json:38` y `Q1-020.json:16` llevan `"resultado": "verificado"` con «revisor independiente de prueba D».
  - `sellar` pasa al producto `--revisor "revisor independiente de prueba D (arnés externo)"` (`ejecutar_caso.py:29,169`) sin ninguna marca.
  - Solo Q1-034 añade «[SIMULADO]» a los nombres.
  - La etiqueta existe a nivel de caso, pero en el registro del producto queda escrito «revisor independiente».
- Q1-034 también usa una comprobación escrita por el arnés (estado «pendiente»). Por eso los 29 casos con resultado propio dependen de precondiciones escritas por el arnés, y 28 de ellos usan verificación o sellado simulados.

## 2 · Aserciones por criterio — NO CUMPLE

**Sondas del revisor externo reproducidas contra el arnés nuevo.** Están adaptadas de `sondas_revision.py`, porque la parte A de ese script no aplica aquí.

| Sonda (d375d80) | Antes | Ahora | Veredicto |
|---|---|---|---|
| `D_arnes_sin_scripts_producto` (candidata sin scripts, Q1-001 real) | exit 0, «OK Q1-001» | **exit 2, ERROR_ENTORNO** | Detecta |
| `D_matriz_sin_evidencias` (scripts sin carpeta `evidencias`) | exit 0, 29 CUMPLE | exit 1 (`FileNotFoundError` en `recuentos.json`), 36 filas, **0 CUMPLE** | Detecta (por el fallo, no por un control explícito) |
| `D_SALIDA_OBSOLETA` con la especificación real Q1-036 (oficial exit 3, provisional exit 2) | exit 0, copia los heredados | **exit 1, ERROR, 0 copiados**, exits `[0,1,1,3,2]` | Detecta |

**Falsos positivos nuevos** (salida en `sondas/sondas_arnes_d.json`; candidata falsa y stubs, no el producto):

- **P1 · especificación vacía**
  - Contraejemplo: `{"id":"Q1-031","harness_version":"2.0","pasos":[],"criterios":[]}`.
  - Resultado: `ejecutar_caso.py` termina con **exit 0, COMPONENTE_OK**.
  - Causa: `ejecutar_caso.py:239-244` no exige al menos un criterio. `pruebas_arnes.py:58` tampoco lo detectaría, porque `all([])` es verdadero.
- **P2 · criterio sin aserciones**
  - Contraejemplo: `"afirma": []`.
  - Resultado: el criterio queda `NO_EVALUADO`, pero el caso sale **COMPONENTE_OK, exit 0** (`ejecutar_caso.py:233-244`).
- **P3 · evidencia de otro caso**
  - Contraejemplo: una aserción con `"archivo": "../Q1-036/07_informe_provisional.md"` en el caso Q1-032.
  - Resultado: **CUMPLE_COMPONENTE**. No hay contención de ruta (`ejecutar_caso.py:42`). Una observación compartida puede así convertirse en CUMPLE propio.
- **P4 · resultado forjado**
  - Contraejemplo: escribir `{"harness_version":"2.0","estado_caso":"COMPONENTE_OK"}` en `evidencias/Q1-031/resultado_ejecucion.json`.
  - Resultado: `generar_matriz.py` da **Q1-031 PARCIAL_COMPONENTE / CUMPLE**, sin criterios ni especificación, y los recuentos pasan a CUMPLE 31.
  - Causa: la matriz confía en dos campos (`generar_matriz.py:67`). No comprueba criterios, huella de la especificación ni SHA observado.
- **P5 · Q1-034 con una especificación real**
  - Contraejemplo: una salida que no conserva ningún rango, `{"comprobadas":[],"pendientes":["aux:litigio: no está acreditado (sin mención de rango)"]}`.
  - Resultado: **C1 «el rango 0-200 se conserva como hipótesis acotada» queda CUMPLE_COMPONENTE** y el caso sale COMPONENTE_OK.
  - Causa: C1 solo tiene dos aserciones `json_lista_no_contiene`. Además `obj.get(lista) or []` (`ejecutar_caso.py:68,73,78`) hace que pasen también con un `{}` vacío.
  - Consecuencia: la afirmación «rango 0–200 preservado» (`RESUMEN_PARA_INTEGRADOR.md:18`, `HALLAZGOS.md:36-38`) **no la acredita ninguna aserción**. La propia matriz dice que la validación del rango sigue sin comprobar.
- **P7 · Q1-026 con una especificación real**
  - Contraejemplo: el stub de `cambiar_base.py` falla por un motivo ajeno («CAMBIO inválido») pero su mensaje contiene la subcadena «ausente o inexistente en texto/».
  - Resultado: **C1 CUMPLE**. Es decir, C1 da por bueno cualquier exit 1 cuyo mensaje contenga esa subcadena.
  - En la evidencia real, `evidencias/Q1-026/cambiar_base_preparar.txt:4-8` muestra además errores de AR_2019, AR_2020 e ipal («cero» sin «cita» literal) que no se deben a la falta de `pdftotext`. Atribuir el bloqueo solo a esa herramienta no está demostrado.
- **No discriminante (sobre la evidencia publicada).** En Q1-027, la aserción de C2 `apto_por_entradas == false` ya se cumplía **antes** de mutar la fuente (`02_comprobar_antes_mutacion.json`: `apto_por_entradas=False`, 320 errores). No aporta prueba de la invalidación. Las otras dos aserciones de C2 sí discriminan.

**Pruebas del autor (`pruebas_arnes.py`, «8/8 PASA»):**
- `evidencias/pruebas_arnes.log` no ha cambiado desde `9ed248a`, es decir, desde **antes** de que `1fc46f3` modificara `ejecutar_caso.py`. Su detalle de recuentos (27/6/1/2) no corresponde al estado actual (29/4/1/2). El «8/8» de `ENTREGA.json:56` no se ha vuelto a ejecutar sobre el código entregado.
- La prueba 7 (`pruebas_arnes.py:159-161`) no compara `recuentos.json` con el CSV, aunque su nombre lo dice.
- La prueba 5 crea la carpeta `evidencias` (`:122`) en vez de omitirla.

## 3 · Aislamiento de artefactos — CUMPLE CON LÍMITES

Lo que está bien:
- `git diff --name-only bdcbba7 1ac661b` no contiene ningún `__pycache__`, `.pyc`, PDF, XLSX ni ZIP. `--numstat` no muestra archivos binarios.
- La búsqueda de patrones de secreto (`ghp_`, `sk-`, `AKIA`, claves privadas, `api_key`, `password`, `bearer`) no da coincidencias.
- No hay `__pycache__` en el árbol.
- Ningún `resultado_ejecucion.json` referencia el `RUN_DIR` de otro caso.
- Ninguna especificación asevera sobre un archivo que su propia ejecución no produzca (comprobación estática hecha por el revisor).
- D-R2 corregido (sonda P6).

Límites (con contraejemplo):
- **Logs acumulados.** `Caso` no reinicia `ev_dir` y abre el log en modo `"a"` (`lib_arnes.py:80,91`). Hay **9 casos** cuyo `ejecucion.log` mezcla 2 o 3 ejecuciones: Q1-002, 014, 017, 018, 019, 020, 026, 027 y 036.
  - En Q1-002, Q1-017 y Q1-020 la primera ejecución tuvo `sellar` con exit 1 y la segunda con exit 0, ambos «esperado [0,1]».
  - El `resultado_ejecucion.json` solo corresponde a la última ejecución y no guarda la huella de la especificación. La sonda P9 lo reproduce.
- **Q1-026 escribe dentro de la candidata y reutiliza el origen.** `pruebas_d/` se crea en `CANDIDATA_DIR` (`ejecutar_caso.py:183`) y el origen solo se copia si no existe (`:186`). La sonda P7 coloca un `fase1_v63.json` «PREEXISTENTE Y MUTADO»: se reutiliza y el caso sale COMPONENTE_OK. `git status` de la candidata muestra `?? munger_v2_r1/pruebas_d/`.
- **SHA de la candidata sin estado del árbol.** `verificar_entorno` solo compara `rev-parse HEAD` (`lib_arnes.py:60-73`). La sonda P8 modifica sin commit el script de verificación y el caso sale COMPONENTE_OK. Además, `candidata_sha` guarda la constante esperada, no la observada (`lib_arnes.py:88`). El banco solo se comprueba por su presencia. Su huella la verifica `preparar_entorno.sh`, pero desde la punta de la rama, no desde el SHA fijado (`preparar_entorno.sh:39`). Hoy esa punta coincide con `4745f38`. `base_414.py verify … || true` (`:30`) ignora el resultado.

## 4 · Q1-026 y Q1-027

### Q1-026 — NO CUMPLE

El banco (`casos_aceptacion.jsonl`, Q1-026, y `fixtures/f5_026_nota.txt`) pide caja **95→90**, deuda **300** y deuda neta **210** millones de EUR.

El paquete «restaurado» no es coherente con eso:
- `evidencias/Q1-026/CAMBIO_Q1-026.json` (campo `analisis.C24.fuente`) atribuye a `f5_026_nota.txt` «caja 45000 miles; errata de v1 (45054) corregida; deuda 82019 miles». **Ese texto no está en el fixture**, cuyo contenido íntegro es «Caja 90; Deuda financiera 300 … Correccion de errata de v1 (caja 95)». Si se ejecutara, quedaría registrada una fuente con cifras que el documento no contiene.
- En `adaptaciones.json`, Q1-026 se contradice a sí mismo: `adaptacion` dice «caja 95->90 … deuda 300 … 300-90=210» y `sin_comprobar` dice «82.019-45.000=37.019».
- `evidencia.M` dice «45.000 mm (fixture f5_026 adaptado: 95->90)».
- `paquete_runtime` (`generar_relevo.py:62-63`) ordena al coordinador trabajar con «caja 45.000, deuda 82.019 … deuda neta 37.019». Con eso el esperado numérico del banco (210) no se puede observar.
- `periodo: "2016"` en una base económica fechada en 2025-12-31 queda sin justificar.
- La «restauración» no recupera el archivo original. Comparado con `b42f453`, `CAMBIO_Q1-026.json` se ha regenerado (24 líneas cambiadas) y se ha perdido el bloque `evidencia` (`Análisis!C24` E/M). `cambiar_base_preparar.txt` también se ha regenerado. La procedencia es la ejecución del 16-11 del arnés, no la del archivo eliminado.
- `origen_estado.txt` dice `destino_existe_tras_fallo=true`. El texto de C2 promete «no se sobrescribe», pero no lo asevera ninguna aserción.
- En la matriz, Q1-026 cuenta como **PARCIAL_COMPONENTE / CUMPLE** con 2 «CUMPLE_COMPONENTE». Esas aserciones solo dicen que el comando falló y que la copia de prueba no cambió. **No se observa ningún criterio del banco.** Debería clasificarse como **entorno**, no como componente cumplido.

### Q1-027 — CUMPLE CON LÍMITES

- **Evidencia:**
  - `evidencias/Q1-027/resultado_ejecucion.json`, añadido en `1fc46f3`: COMPONENTE_OK, criterios C1–C3 CUMPLE_COMPONENTE.
  - `ejecucion.log`: una **segunda ejecución añadida** a partir de la línea 2110.
  - `01_sellar.txt` … `05_comprobar_final.json`: **byte a byte iguales a los de `bdcbba7`** (no aparecen en el diff).
  - El `stdout` registrado coincide con el final de cada archivo guardado.
- **Naturaleza:**
  - Según el log, son comandos reales del componente `verificacion_entradas.py` (plantilla, sellar, comprobar) de la candidata `957af65`.
  - Las precondiciones son **simuladas**: comprobación «verificada» escrita por el arnés y `sellar --revisor` con «revisor independiente de prueba D».
  - **No lo he reproducido aquí.** No es una ejecución del personaje.
- **No cubierto** (frente a los criterios del banco):
  - Invalidación de la aprobación (pasa al relevo).
  - Nuevo contraste con deuda 300.
  - Esperado numérico 300−80=220.
  - La adaptación usa 45054→80054 miles y deuda 82019, con lo que el esperado del banco no es observable.
  - La aserción `apto=false` no discrimina (§2).
- **Conclusión:** «cerrado con resultado» es exacto solo como **resultado de componente con precondiciones simuladas**, no como caso cerrado.

## 5 · Matriz de 36 — NO CUMPLE

**Recuento independiente** desde `evidencias/` y el banco (`sondas/recuento_independiente.json`):

| Categoría (revisor) | n | Casos |
|---|---:|---|
| Ejecución real del personaje (agentes/fases/auditoría) | **0** | — |
| Componente real del producto, con resultado propio y precondiciones escritas por el arnés (simuladas) | **29** | Q1-001…Q1-025, Q1-027, Q1-029, Q1-034, Q1-036 (28 con verificación/sellado simulados; Q1-034 con comprobación «pendiente» preescrita) |
| Entorno: comando real que falla según lo esperado y sin ningún criterio del banco observado | **1** | Q1-026 |
| Observación compartida, sin ejecución propia | **2** | Q1-028, Q1-032 (de Q1-036) |
| Pendiente sin ejecución (necesita agente) | **2** | Q1-031, Q1-033 |
| Decisión del usuario | **2** | Q1-030, Q1-035 |
| Respuestas simuladas de agente | **0** | — |
| Relevo al coordinador | **36 paquetes** | ver la lista de abajo |

Criterios: el arnés define **56** propios, mientras el banco tiene **109** criterios observables. La matriz no relaciona unos con otros: los C1/C2 del arnés no son los criterios del banco. CORRECCION_D pedía «matriz por criterio y precondición».

**Comparación con `ENTREGA`:**

| ENTREGA / RESUMEN | Revisor | Diferencia |
|---|---|---|
| 30 PARCIAL_COMPONENTE, 30 CUMPLE de componente (`ENTREGA.json:23,37,89`) | 29 componentes + 1 de entorno | Q1-026 se cuenta como CUMPLE |
| «Q1-034 … rango 0–200 preservado» (`RESUMEN:18`) | No lo acredita ninguna aserción (P5); la propia matriz dice «sin comprobar: … validar con rango» | Afirmación exagerada |
| «arnés 8/8 PASA» | Log anterior al código y a los recuentos actuales | Evidencia caducada |
| 6 NO_EJECUTADO; 2 compartidos; 4 sin ejecutar | Igual | Coincide |
| 0 casos completos del personaje | Igual | Coincide |
| Naturaleza 31/3/2 | Igual (banco) | Coincide |

Restos a mano o caducados:
- `HALLAZGOS.md:24` sigue diciendo «27 ejecuciones propias (28 especificaciones; Q1-026 sin spec ejecutable)».
- En la matriz, Q1-025 dice todavía «ejecutado como patrón en Q1-027» (`adaptaciones.json`).
- `preserva_sentido = "sí"` sigue fijo para los 36 casos (`generar_matriz.py:104`), también para Q1-026, cuya adaptación contradice su CAMBIO.
- `VEREDICTO_CASO_FIJO` y `OBS_COMPARTIDA` están escritos a mano en el código (`generar_matriz.py:31-41`).

**Relevos de `d24dbe3` (`relevo/PAQUETES_RELEVO.json`, regenerado de forma idéntica). Lo que piden ejecutar al coordinador:**

1. **30 paquetes** (Q1-001…Q1-027, Q1-029, Q1-034, Q1-036).
   - Comando: `python3 scripts/ejecutar_caso.py scripts/especificaciones/{piloto|bloque2}/Q1-0xx.json`, desde `resultados_qwen/ejecucion_d`, con `CANDIDATA_DIR`, `BANCO_DIR`, `RUN_DIR` y opcionalmente `EVIDENCIAS_DIR` definidos.
   - Qué hace: vuelve a ejecutar el **componente** (`verificacion_entradas.py` plantilla/comprobar/sellar; `ficha.py` e `informe.py` en Q1-036; `cambiar_base.py preparar` en Q1-026).
   - Requisitos: candidata `957af65` con los binarios de la base 4.14 (expediente Viscofan y plantillas XLSX V6.4.1 y V6.3). **No necesita agentes ni LibreOffice.** El revisor externo lo reprodujo sin LibreOffice.
   - Además piden «recorrido del personaje con agente real (entrada_usuario pegada, fases A/B/C, verificación, auditoría APROBADO con agente nuevo)». **Para eso no dan comando**, ni modelo, ni configuración, ni el orden de fases por caso: solo la `entrada_usuario` y las rutas de los fixtures. **Necesita agentes reales.**
2. **Q1-026 `paquete_runtime`:**
   - Pasos: (a) `pdftotext` de AR_2021…AR_2024 hacia `texto/`; (b) `python3 -I personaje_v2/scripts/cambiar_base.py preparar pruebas_d/CAMBIO_Q1-026.json`; (c) actualizar el registro de la copia con «caja 45.000, deuda 82.019»; (d) **recalcular con soffice** en secuencia y recalcular los dependientes («deuda neta 37.019»); (e) **auditoría nueva con agente auditor distinto**.
   - Requisitos: `pdftotext`, **LibreOffice** y **agente real**.
   - Defectos: cifras incoherentes con el banco (§4), y no se ha demostrado que `pdftotext` baste (también hay errores de AR_2019, AR_2020 e ipal).
3. **Q1-031 y Q1-033:** «fase A/objetivo con agente real sobre fase1_v63.json (precio actual)». Sin comando. **Necesita agente real.**
4. **Q1-030 y Q1-035:** decisión de política del usuario. No es ejecución del coordinador.
5. **Q1-028 y Q1-032:** `comando_relevo: null` y **«falta_para_caso_completo: nada pendiente declarado»**. Es un **defecto**: los casos no se han ejecutado, y `RELEVO_SUPERVISADO.md` y la matriz dicen que falta la reaprobación con auditor real (Q1-028) y el recuento 4/1/5 (Q1-032). La causa está en `generar_relevo.py:37,55`, que solo añade lo que falta cuando el estado es PARCIAL_COMPONENTE.
6. **Reanudación** (`ENTREGA.json:85`): `bash scripts/preparar_entorno.sh && bash scripts/ejecutar_todo.sh && python3 -B scripts/pruebas_arnes.py && python3 scripts/generar_matriz.py && python3 scripts/generar_relevo.py`. `preparar_entorno.sh` necesita **red y `gh`** (clonado, descarga de la Release de 1,13 GB, `git fetch`) y posiblemente `pip`; escribe en `/workspace`. No usa LibreOffice ni agentes.

## 6 · Coherencia código/salidas — NO CUMPLE (manifiesto)

- **Manifiesto:** `sha256sum -c MANIFIESTO_SHA256.txt` da exit 1. 196 de 197 coinciden. Falla `RESUMEN_PARA_INTEGRADOR.md`: el manifiesto registra `3cee4cb3…`, que es el valor en `bdcbba7`, `1fc46f3` y `d24dbe3`, y el archivo entregado es `c1c27880…`. Se regeneró antes de editar RESUMEN en `1ac661b`. Cubre todos los archivos del árbol salvo el propio manifiesto.
- **Regeneración:** `MATRIZ_EJECUCION.csv`, `evidencias/recuentos.json` y `relevo/PAQUETES_RELEVO.json` coinciden **byte a byte** al regenerarlos desde la evidencia y el banco `4745f38` (manifiesto del banco 57/57).
- **Coherencia stdout↔archivo:** en los 30 `resultado_ejecucion.json` no hay ninguna incoherencia.
- **No reproducido aquí:** ninguna ejecución de componentes del producto (excluido por el encargo) ni `pruebas_arnes.py`, cuyo log además está caducado (§2).

## Defectos (resumen, con contraejemplo mínimo)

| ID | Gravedad | Defecto | Contraejemplo / evidencia |
|---|---|---|---|
| R-D1 | material | Una especificación vacía o un criterio sin aserciones dan COMPONENTE_OK, exit 0 | Sondas P1 y P2 |
| R-D2 | material | `json_lista_no_contiene` pasa con salida vacía; Q1-034 C1 acredita un «rango preservado» sin rango | Sonda P5; `ejecutar_caso.py:68-80` |
| R-D3 | material | La matriz asigna CUMPLE a cualquier `resultado_ejecucion.json` con dos campos | Sonda P4; `generar_matriz.py:67` |
| R-D4 | material | Q1-026: el CAMBIO atribuye al fixture cifras que no contiene; contradice el banco y su adaptación; el relevo arrastra 45.000/82.019/37.019 | `CAMBIO_Q1-026.json` frente a `fixtures/f5_026_nota.txt`; `generar_relevo.py:62-63` |
| R-D5 | material | Q1-026 cuenta como componente CUMPLE siendo un bloqueo de entorno; su C1 acepta cualquier fallo que contenga la subcadena | Sonda P7; matriz |
| R-D6 | material | Los relevos de Q1-028 y Q1-032 dicen «nada pendiente declarado» | `PAQUETES_RELEVO.json`; `generar_relevo.py:37,55` |
| R-D7 | menor | El manifiesto no verifica | `sha256sum -c`, exit 1 |
| R-D8 | menor | «8/8 PASA» viene de un log anterior al código actual; la prueba 7 no compara CSV y recuentos | `pruebas_arnes.log` sin cambios desde `9ed248a` |
| R-D9 | menor | Logs acumulados en 9 casos; sin huella de la especificación en el resultado | Sonda P9; `lib_arnes.py:80,91` |
| R-D10 | menor | Q1-026 escribe en la candidata y reutiliza un origen preexistente | Sonda P7 (`git status`) |
| R-D11 | menor | Control de SHA sin estado del árbol; `candidata_sha` constante; `verify … \|\| true` | Sonda P8; `lib_arnes.py:60-73,88`; `preparar_entorno.sh:30` |
| R-D12 | menor | Una aserción puede leer evidencia de otro caso (`../`) | Sonda P3 |
| R-D13 | menor | Documentación caducada (HALLAZGOS 27/28; adaptaciones de Q1-025 y Q1-034; `preserva_sentido` fijo) | §5 |
| R-D14 | observación | Q1-027 `apto=false` no discrimina; Q1-025 no comprueba los ejes de coincidencia del banco (§6) | §2, §4 |

## Lo que se puede conservar

- El D-R2 está corregido y comprobado con la especificación real de Q1-036 (P6).
- Los errores de entorno se propagan (R1).
- La matriz ya no da CUMPLE sin carpeta de evidencias (R2).
- Las salidas derivadas se regeneran de forma determinista.
- No hay `__pycache__`, secretos ni binarios.
- La separación entre componente y caso, y la declaración de «0 casos completos», son correctas.
- La naturaleza 31/3/2 del banco se conserva.

## Límites de esta revisión

- No he ejecutado el producto, ni LibreOffice, ni agentes, ni la red. Las sondas usan stubs y no dicen nada del comportamiento de Munger.
- No he releído ni auditado económicamente las 30 especificaciones; solo las de Q1-025, 026, 027, 034 y 036 en detalle.
- No he verificado la base 4.14 (6798/6798) ni la materialización del autor. Esa afirmación descansa en la declaración del autor.
- Esto no es aceptación, ni integración, ni aptitud para dinero real.

## Archivos del revisor

- Informe: `REVISION_D_1ac661b.md` (esta carpeta)
- Sondas: `sondas/` (esta carpeta), que contiene `sondas_arnes_d.py`, `sondas_arnes_d.json`, `sondas_arnes_d.stdout`, `recuento_independiente.py`, `recuento_independiente.json`, `comprobaciones_revisor.sh` y `comprobaciones_revisor.log`.
