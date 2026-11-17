# Revisión independiente de la corrección AUTO1 · 422a6f3

- **Objeto:** `origin/automatizacion/correccion-auto1` @ `422a6f3d273cf6f0e731f4cb6affa255cedb43d1`,
  sobre `267ad18` (que solo cambia `observations/` respecto de `a508d6b`). El diff de código
  `267ad18..422a6f3` coincide con `a508d6b..422a6f3`, salvo `observations/`.
- **Encargo:** `CORRECCION_AUTO1.md`, `REVISION_AUTOMATIZACION_a508d6b.md` y sus sondas
  (rama `coordinacion/cierre-v2`, `coordinacion/cierre_v2/revisiones_coordinador/AUTO_a508d6b/`).
  Entrega del autor: `automation/coordination/ENTREGA_AUTO1.json`.
- **Revisor:** un agente distinto del autor. No ha escrito ni modificado el código revisado.
- **Fecha:** 17-nov-2026.

**Estado: revisado. Conforme con observaciones. No está aceptado ni integrado, y no autoriza
ninguna inferencia.**

Cómo se hizo la revisión:
- Se leyó el código y se ejecutaron pruebas y sondas locales con la red bloqueada en el proceso.
  No hubo ningún intento de conexión en ninguna ejecución.
- No se ha llamado a Anthropic, Mistral, Qwen ni GitHub Actions, ni se han leído secretos.
- No se ha modificado ninguna rama, no se ha hecho commit y no se ha hecho push.
- El worktree `git worktree add --detach <wt> 422a6f3` sigue limpio (`git status` vacío).

Superar estas pruebas **no equivale a una auditoría recibida**. En particular, no sustituye
`audit-pilot-code-001`.

Rutas usadas en este informe:
- `<wt>`: el worktree revisado.
- `<rev>`: este directorio de entrega.
- `<base>`: `<rev>/base_a508d6b`, obtenido con `git archive a508d6b automation .github`.

## 1. Veredicto global

**CONFORME CON OBSERVACIONES. No hay hallazgos materiales.**

Las siete correcciones medias y ocho de las nueve menores están hechas en el código y tienen
pruebas que detectan el defecto.

Quedan pendientes, como declara la entrega:
- **M7, parcial:** falta `--require-hashes`.
- **m6:** el ruleset remoto.
- **M5 y M6:** necesitan configuración y decisiones humanas fuera del repositorio:
  - el `environment` con revisores;
  - los secretos solo en ese environment;
  - la cifra del tope;
  - copiar los workflows a la rama por defecto.

Se mantienen los dos invariantes:
- una sola llamada de pago, sin reintentos;
- `audit-pilot-code-001` sigue bloqueada por su reserva.

Hay seis hallazgos nuevos, todos menores u observaciones (§5). Ninguno produce una segunda
inferencia, libera una reserva ni acepta un resultado falso.

## 2. Pruebas y sondas ejecutadas

| Comando | Código | Resultado |
|---|---|---|
| `python3 -I -m unittest discover -v` (cwd `<wt>/automation/coordination`) | 0 | 95 OK, 0 omitidas |
| `python3 -I -m unittest discover -v` (cwd `<wt>/automation/claude_review`) | 0 | 49 OK |
| Las mismas desde la raíz, con `-s … -p 'test_*.py'` | 0 / 0 | 95 / 49 OK |
| `python3 -I <rev>/sondas/sin_red_unittest.py` sobre ambos directorios | 0 | 95 + 49 OK, **0 intentos de red** |
| `python3 -I <rev>/sondas/sonda_sse.py <wt>` (sonda del coordinador, sin cambios, sha256 `af3d8fd6…`) | 0 | **25/25 CONFORME**. S16 se comenta en §5-N4 |
| `sh <rev>/sondas/sonda_workflows.sh <wt>` | 0 | Los 5 workflows con secretos de inferencia solo tienen `workflow_dispatch`. Hay `push` en `automation-tests.yml` y `vibe-readiness.yml`, ambos sin secretos |
| `python3 -I <rev>/sondas/sonda_workflows_por_job.py <wt>` | 0 | 13 jobs, **0 no conformes**, 6 con secreto de inferencia, todos con `environment: inferencia-aprobada` (a508d6b: 6 no conformes) |
| `python3 -I <rev>/sondas/sonda_complementaria.py <wt> <rev>/sondas/registro_reservas_953af02.json` | 0 | 14 casos: 11 conformes y 3 hallazgos (C03 ×2 y C09; §5) |
| `python3 -I <rev>/sondas/sonda_piloto.py <wt>` | 0 | 2 hallazgos fuera del alcance original (§5-N3) |
| `python3 -I <rev>/sondas/mutantes.py <wt> <rev>/mutantes <rev>/sondas/mutantes.salida.jsonl` | 0 | 10/10 mutantes detectados (§4) |

Notas:
- Entorno: Python 3.13.18 y PyYAML 6.0.1 instalado. Las 7 pruebas de workflows se ejecutaron.
- `registro_reservas_953af02.json` se extrajo con `git show` de la rama local
  `origin/automatizacion/claude-api-piloto-registro` @ `953af02`. Solo contiene recuentos de
  tokens e importes, sin secretos.

## 3. Veredicto por hallazgo

| | Veredicto | Prueba de cierre comprobada |
|---|---|---|
| **M1** corte a mitad de chunk | **CERRADO** | Se reprodujo lo siguiente: <ul><li>S08 da `ANTHROPIC_STREAM_CORTADO_NO_REINTENTAR` con 1 apertura.</li><li>S17 da `INFERENCIA_SIN_VEREDICTO_COSTE_INCIERTO`, publica las 4 piezas (`report.json`, `report.md`, `reservation.json`, `sources.json`) y la segunda llamada da `YA_RESERVADO_SIN_NUEVA_LLAMADA`.</li><li>`run()` captura cualquier `Exception` después de `reserve` (`critical_review.py:550`) y `publish` intenta las cuatro piezas aunque falle una.</li><li>`qwen_peer_review.py` hereda la corrección a través de `cr.run`.</li></ul>Queda un residuo en `pilot.py` (§5-N3). |
| **M2** JSON que no es objeto o anidado | **CERRADO** | S11, S11b y S12 dan `ANTHROPIC_STREAM_INVALIDO_NO_REINTENTAR`. Hay 13 subcasos unitarios de tipos incorrectos. |
| **M3** sin uso final | **CERRADO** | S10 da `STREAM_SIN_USO_FINAL_NO_REINTENTAR`. Con dos `message_delta` acumulativos se obtiene 210/600. Sin `input_tokens` se rechaza. |
| **M4** coste incierto | **CERRADO con observación** | Se comprobó con C02: Receipt real y rama en memoria. `report.json` y `reservation.json` publicados llevan `state=INFERENCIA_SIN_VEREDICTO_COSTE_INCIERTO`, `cost_status=INCIERTO`, `cost_upper_bound_usd` igual a `reserved_usd` y `usage_partial` = {200, 1}. En cambio, `max_tokens` da `RESULTADO_NO_ACEPTADO_NO_REINTENTAR`, `CONOCIDO_ESTIMADO` y 0.0216. Observación: la cota no se contrasta con el uso parcial (§5-N1). |
| **M5** tope acumulado | **CERRADO EN CÓDIGO** (`critical_review` y `qwen_peer_review`). Faltan la cifra humana y la configuración remota | Comprobado con C04–C07: <ul><li>Con el registro real, la exposición es exactamente 2.438158 (4 reservas Anthropic; las de Vibe se omiten).</li><li>Una tarea nueva sin la variable da `TOPE_ACUMULADO_NO_FIJADO_POR_RESPONSABLE`, con 0 llamadas a Anthropic y 0 PUT.</li><li>Con tope 4 o 4.438157 da `TOPE_ACUMULADO_SUPERADO` antes de `/v1/models`. Con 4.438158 se admite.</li><li>La comprobación se repite dentro de `reserve()`.</li></ul>Residuos: `pilot.py` queda fuera (§5-N3), la carrera concurrente la declara el autor y la integridad del registro se trata en §5-N2. |
| **M6** puerta humana | **CERRADO EN REPOSITORIO**. Falta la configuración remota | <ul><li>Los 6 jobs con `ANTHROPIC_API_KEY` o `MISTRAL_VIBE_CLI_KEY` solo tienen `workflow_dispatch` y `environment: inferencia-aprobada`.</li><li>No hay `pull_request_target`, `schedule` ni `workflow_run`.</li><li>Las acciones siguen fijadas por SHA y con `persist-credentials: false`.</li></ul>Ver «Pendiente remoto» después de la tabla. |
| **M7** pip en el mismo job que la clave | **PARCIAL** (coincide con el autor) | <ul><li>El job con `ANTHROPIC_API_KEY` no instala nada y no comparte job con Mistral.</li><li>Vibe se instala en un venv aparte, sin secretos en el paso y con `--only-binary=:all:`.</li><li>Falta `--require-hashes`.</li></ul>Hay un residuo nuevo: `GH_TOKEN` con escritura queda al alcance del CLI de terceros (§5-N2). |
| **m1** línea `event:` | **CERRADO** | S13 da `ANTHROPIC_ERROR_STREAM`, y una discrepancia entre `event:` y `data.type` da `STREAM_EVENTO_INCOHERENTE`. |
| **m2** cota de línea | **CERRADO EN CÓDIGO. La prueba es débil** | C01: una línea de 5 MB por un `HTTPResponse` real da `STREAM_DEMASIADO_GRANDE` tras leer 2 000 358 bytes (chunked) o 2 000 072 (close). Pero la prueba unitaria del autor y S16 no ejercitan la cota (§5-N4). |
| **m3** modelo del cuerpo | **CERRADO** | S20 da `MODELO_DEL_CUERPO_NO_AUTORIZADO`, con 0 aperturas. Se rechazan `tools`, `tool_choice`, `mcp_servers`, `container` y `service_tier` distinto de `standard_only`. También en el transporte sin stream. |
| **m4** campos de facturación | **CERRADO** | `speed=fast`, `inference_geo=us` o `service_tier=priority` dan `FACTURACION_NO_PREVISTA` e `INCIERTO_SIN_COTA`. Si los campos faltan se aceptan, como pedía el encargo («si tienen otro valor»). |
| **m5** plazo total | **CERRADO con límite** | El plazo es de 720 s, comprobado en cada `read1`. Los mutantes que lo eliminan se detectan. Límite: después del stream, la publicación puede hacer hasta 8 llamadas a GitHub de 60 s cada una. En el peor caso, el job de 20 min puede terminar antes de publicar. Aun así la reserva queda en `RESERVADO_NO_REINTENTAR` y bloquea. |
| **m6** ruleset | **NO CERRADO** (coincide con el autor) | Es remoto. Lo verifica la persona responsable. |
| **m7** `cwd` de Vibe | **CERRADO** | Las dos invocaciones usan `cwd=work` y se cuenta `preflight_invocations_started`. |
| **m8** sustituciones | **CERRADO** | Cada sustitución debe aplicarse exactamente una vez, antes de reservar. Si falla, no se invoca nada. |
| **m9** secreto en readiness | **CERRADO** | `vibe-readiness.yml` no tiene secretos. |

**Pendiente remoto de M6.** Hasta que la persona responsable configure GitHub, la única
barrera es que `workflow_dispatch` exige que el workflow esté en la rama por defecto, y ahora
no lo está. Hay que hacer cuatro cosas:
1. **Crear `inferencia-aprobada` con revisores obligatorios.** Si un job hace referencia a un
   environment que no existe, GitHub lo crea sin protección.
2. **Mover las dos claves al environment y borrarlas del nivel de repositorio.** Si no se
   borran, cualquier workflow con `on: push` que se suba a cualquier rama puede leerlas.
3. **Definir `MUNGER_TOPE_ACUMULADO_ANTHROPIC_USD` como variable del environment**, no del
   repositorio.
4. **Copiar o no los workflows a la rama por defecto.** Lo decide la persona responsable.

**Invariantes (punto 2 del encargo): intactos.**
- **Una sola llamada, sin reintentos:**
  - `StreamingHTTP.call` abre una sola vez con `NoRedirect` y `timeout=60`.
  - Los dos `while` de `critical_review.py:104` y `:116` solo leen del mismo stream.
  - S08, S08b–e y los mutantes registran 1 apertura.
  - `test_timeout_not_retried` sigue exigiendo 1 inferencia.
- **`audit-pilot-code-001`:**
  - `prior()` se consulta antes de `admit`, de `/v1/models` y de `count_tokens`.
  - C05: incluso sin la variable de tope devuelve `YA_RESERVADO_SIN_NUEVA_LLAMADA`, con 0
    llamadas a Anthropic y 0 PUT.
  - El registro real conserva `reservation.json` de esa tarea (`reserved_usd=1.912936`).

## 4. Las pruebas nuevas no están vacías (punto 4)

Se copiaron los 4 `test_auto1_*.py`, más el `test_critical_review.py` modificado, sobre
`<base>` (a508d6b) y se ejecutaron sin red. Salidas:
- `sondas/pruebas_nuevas_sobre_a508d6b.jsonl`;
- `sondas/prueba_modificada_sobre_a508d6b.jsonl`.

**Resultado: de las 44 pruebas nuevas, 41 fallan sobre a508d6b y 3 pasan.**

Las 41 que fallan se reparten así:
- **20 por comportamiento:** escapa la excepción, «PilotError not raised» o falla la aserción
  sobre el workflow.
- **5 porque falta un campo nuevo:** `cost_status`, `usage_partial` o `error`.
- **16 porque falta un símbolo:** sobre todo M5, que en a508d6b no existía.

**Muestra de fallos por comportamiento sobre a508d6b (8):**
- `test_m1_incomplete_read_inside_chunk_is_pilot_error_one_open`: `ERROR IncompleteRead`, la excepción escapa.
- `test_m1_line_too_long_is_pilot_error`: `ERROR LineTooLong`.
- `test_m2_deep_nesting_is_rejected`: `ERROR RecursionError`.
- `test_m2_each_wrong_type_is_rejected`: `AttributeError: 'list' object has no attribute 'get'`.
- `test_m3_missing_final_usage_is_rejected`: `FAIL PilotError not raised`.
- `test_m1_event_line_error_or_mismatch_is_rejected` (m1): `FAIL PilotError not raised`.
- `test_m3_body_model_bound_before_connection` (m3): `FAIL PilotError not raised`, ×3 subcasos.
- `test_m6_inference_jobs_never_on_push_and_always_gated`: `['push'] != ['workflow_dispatch']`.
  También fallan las de M7 y m9 y la del timeout del job de m5.

**Mutación sobre 422a6f3.** Las pruebas de M5 y M4 solo fallan sobre a508d6b porque falta el
símbolo, así que se reintrodujo cada defecto sobre una copia de 422a6f3. **Los 10 mutantes se
detectan:**

| Mutante | Pruebas que lo detectan |
|---|---|
| `admit` no compara | 3 |
| sin comprobación previa a `count_tokens` | 3 |
| tope por defecto sin variable | 1 |
| los inciertos cuentan 0 | 2 |
| estado único | 6 |
| sin uso parcial | 3 |
| lectura sin cota | 2 |
| sin plazo total | 1 |
| sin exigir uso final | 3 |
| sin capturar `HTTPException` | 2 |

**Las 3 que pasan sobre a508d6b:**
- `test_m3_two_cumulative_deltas_with_input_tokens`: es un control positivo legítimo.
- `test_m6_actions_pinned_and_credentials_not_persisted`: es un invariante que ya se cumplía.
  No prueba ningún cierre, pero es razonable como no regresión.
- **`test_m2_long_line_bounded_in_memory`: no detecta el defecto de m2.** Debería fallar sobre
  a508d6b y no falla (§5-N4).

**Pruebas que se acercan a una tautología:**
- `test_m5_deadline_fits_inside_job_timeout` compara constantes (720 + 60 < 1080) con los
  20 min escritos en la propia prueba. Lo compensa en parte `test_m5_review_job_timeout_…`,
  que lee el workflow.
- La modificación de `test_timeout_not_retried` está justificada por M4 y conserva la
  aserción de 1 inferencia.

## 5. Hallazgos nuevos

Ninguno es material.

**N1 (menor) · M4: la cota se declara sin contrastarla con el uso parcial ya conocido.**
- Dónde: `critical_review.py:550-557` y `_cost_fields`. `TransportError` solo guarda `usage`,
  no el `model` de `message_start`.
- Contraejemplo (C03): timeout después de un `message_start` con `input_tokens=10 000 000`
  (`reserved_input_tokens=5898`), o con `model=claude-opus-5-5`.
  - Se publica `cost_status=INCIERTO` con `cost_upper_bound_usd=1.357904`.
  - El uso parcial ya demuestra que esa cota no lo es.
  - `Register` lo contaría por la reserva, en lugar de bloquear como `INCIERTO_SIN_COTA`.
- Probabilidad: baja. La reserva acota la entrada (conteo + bytes + 4096), y m3 fija el modelo
  del cuerpo.
- Corrección: guardar el modelo de `message_start` en el parcial. Si el parcial supera
  `reserved_input_tokens` o `MAX_OUTPUT`, o el modelo no coincide, aplicar `INCIERTO_SIN_COTA`.

**N2 (menor-medio, residuo de M7) · El CLI de terceros puede leer `GH_TOKEN` con escritura.**
- Dónde: los jobs `mistral`, `review` (Mistral) y `connection` tienen `contents: write`, y el
  paso que lanza `vibe` tiene `GH_TOKEN` en su `env`. Filtrar el entorno del proceso hijo
  (`qwen_bank_review.py:194`) no aísla.
- Contraejemplo (C09, con una variable ficticia): un hijo lanzado con el entorno filtrado lee
  la variable en `/proc/<padre>/environ`, porque comparte el mismo uid.
- Efecto potencial, ante un paquete comprometido: reescribir la rama de registro. Puede:
  - borrar o cambiar la reserva de `audit-pilot-code-001`;
  - poner `cost_status=CONOCIDO_ESTIMADO` con coste 0.

  Así eludiría el bloqueo de `prior()` y rebajaría el comprometido de M5. La aprobación del
  environment sigue siendo necesaria para gastar.
- No lo introduce AUTO1: ya existía en a508d6b.
- Corrección:
  - el job que ejecuta Vibe, con `contents: read`;
  - la publicación en el registro, en otro job sin código de terceros;
  - o aceptar el riesgo por escrito, junto con `--require-hashes`.

**N3 (menor) · `pilot.py` queda fuera del tope acumulado y de la generalización de M1 y M4.**
- P1: sin `MUNGER_TOPE_ACUMULADO_ANTHROPIC_USD`, `pilot.run` reserva y hace la llamada de pago.
  Solo aplica su techo propio de 0,25 USD.
- P2: si el `content` de la respuesta no es un objeto, `AttributeError` escapa después de la
  reserva. No queda informe y la reserva sigue en `RESERVADO_NO_REINTENTAR`, que bloquea.
  Causa: `pilot.py:379` solo captura `PilotError`.
- Exposición actual: nula. `munger-d-relevos-002` ya tiene su reserva en el registro y el
  `PILOT_ID` es fijo. Solo importaría si se cambia el código.
- Corrección: usar `Receipt.admit` desde `pilot.run`, o documentar que el piloto está cerrado.

**N4 (menor, pruebas) · La evidencia de m2 en la prueba unitaria y en S16 no ejercita la cota.**
- `test_m2_long_line_bounded_in_memory` cuenta solo los bytes que pasan por `read1`.
  - Sobre a508d6b la línea se lee por iteración: el contador queda en 0 y la prueba pasa.
  - El mutante «lectura por iteración» no lo detecta esta prueba.
- S16 de la sonda del coordinador pasa ahora por `STREAM_SIN_LECTURA_ACOTADA`, con
  `bytes_en_memoria=0`, sin llegar a la cota. El 25/25 es correcto, pero en S16 prueba otra cosa.
- El cierre se ha acreditado aparte, con C01 (`HTTPResponse` real).
- Corrección: contar los bytes en el `RawIOBase` que hay bajo un `HTTPResponse`.

**N5 (observación) · La prueba de workflows se omite si falta PyYAML.**
- `test_auto1_workflows.py` usa `skipIf(yaml is None)`. No se ha verificado si el `python3` de
  `ubuntu-latest` trae PyYAML.
- Si no lo trae, `automation-tests.yml` saldría con éxito sin comprobar M6, M7, m5 ni m9.
- Corrección: que falle en lugar de omitirse cuando `GITHUB_ACTIONS` está definido.

**N6 (observación, funcional) · La auditoría `claude-critical-review` queda inoperante y falla cerrada.**
- C08: `snapshot()` da `PAQUETE_EXCESIVO_NO_SE_TRUNCA`.
  - El paquete pesa 94 715 B y el payload, 98 712 B.
  - `main()` devuelve 2 antes de cualquier llamada.
- Aunque se subiera el límite de 74 000, `budget()` daría `RESERVA_SUPERA_2_USD` (unos
  2,13 USD). El límite 74 000 va ligado a `MAX_USD=2`.
- `main()` llama a `snapshot()` antes que a `prior()`, así que ya no se produce el informe
  `YA_RESERVADO_SIN_NUEVA_LLAMADA`.
- **No es un defecto de seguridad.** Falla cerrado, y el autor lo declara.
- Una auditoría de pago del código corregido necesita una decisión humana sobre el alcance de
  `PATHS`, el límite, `MAX_USD`, la `TASK` y el tope.

### Respuestas a los efectos del punto 3

- **Paquete de más de 74 000 bytes.** No es un defecto de seguridad (N6).
- **M5 sin la variable:**
  - **Sí, sin la variable no se reserva nada:** falla cerrado antes de `/v1/models` (C06).
  - Las tareas ya reservadas siguen devolviendo `YA_RESERVADO` (C05).
  - Es el comportamiento pedido: la cifra es una decisión humana. Conviene que la variable
    viva en el environment protegido.
- **`automation-tests.yml`:**
  - **No se lanza en push a cualquier rama.** Solo en `automatizacion/coordinacion-api-v1` y
    `automatizacion/piloto-claude-api`, con filtro `paths` (`automation/**`,
    `.github/workflows/**`), más `workflow_dispatch`.
  - No tiene secretos ni instalaciones, y tiene `contents: read`. Es conforme.
  - No se dispara en `automatizacion/correccion-auto1`: esta entrega no tiene ejecución en CI.
  - Ver N5.
- **Cambio de estado del timeout (M4):**
  - Antes: `RESULTADO_NO_ACEPTADO_NO_REINTENTAR`, con coste nulo. Ahora:
    `INFERENCIA_SIN_VEREDICTO_COSTE_INCIERTO`, con cota y uso parcial.
  - Consumidores actualizados: `main()` y `qwen_peer_review.py` usan `FAILED_STATES`, con
    código 1. No hay otro consumidor de ese estado.
  - El registro histórico de `audit-pilot-code-001` conserva el estado antiguo y no tiene
    `cost_status`. `exposure()` lo cuenta por su reserva completa (1.912936), lo que es conservador.
  - `pilot.py` conserva la semántica antigua (N3).

## 6. Rutas locales y secretos (punto 5)

En las líneas añadidas por `a508d6b..422a6f3`:
- **Rutas locales:** no hay ninguna (`/home/`, `/tmp/`, `/root/`, `/Users/`, `C:\`, `/mnt/`).
  La entrega usa marcadores como `<copia_temporal>` y `<raiz_del_worktree>`.
- **Secretos:** no hay patrones de credenciales (`sk-ant-`, `ghp_`, `github_pat_`, `AKIA…`,
  claves PEM, `xox?-`), ni correos aparte de `noreply@anthropic.com`.
- **Workflows:** los secretos solo aparecen como `${{ secrets.* }}`.
- **Informes:** los errores solo llevan códigos. `test_m1_any_exception_after_reserve_is_published`
  comprueba que el detalle de la excepción no se publica.

**Observación de proceso.** El commit `422a6f3` está firmado por `Claude <noreply@anthropic.com>`,
con el trailer `Claude-Session: …session_01W2RVAnAbM8rydCEdcDNjDs`. Es la sesión desde la que
se lanza esta revisión. `CORRECCION_AUTO1.md` preveía que corrigiera «el usuario, con ChatGPT»
y no «esta sesión».
- Este revisor es un contexto de agente distinto y no es autor del cambio.
- Aun así, conviene que el coordinador registre quién fue el autor, para dejar constancia de que
  la revisión la hace un agente distinto.

## 7. Límites

- Sin red no se han podido verificar:
  - el environment ni sus revisores;
  - dónde están los secretos (repositorio o environment);
  - las reglas de protección o rulesets;
  - si PyYAML está en el runner;
  - los hashes de `mistral-vibe`;
  - los precios en vivo;
  - el ritmo real de los `ping` SSE.
- Las sondas simulan `http.client` con bytes; no son tráfico real de Anthropic.
- La mutación cubre 10 defectos elegidos por el revisor, no todo el espacio posible.
- No se ha revisado la semántica de `qwen_*` más allá de lo que toca AUTO1.
- La carrera entre dos ejecuciones simultáneas de workflows distintos sobre el registro está
  reconocida por el autor y no se ha probado.
- Nada de esto autoriza otra inferencia de `audit-pilot-code-001` ni una tarea de pago nueva.

## 8. Archivos de esta entrega (`<rev>/sondas/`)

**Sondas:**
- `sonda_sse.py`: copia idéntica de la del coordinador. Salida: `sonda_sse_422a6f3.salida.jsonl`.
- `sonda_workflows.sh`: copia de la del coordinador. Salida: `sonda_workflows_422a6f3.salida.txt`.
- `sonda_workflows_por_job.py`. Salidas: `sonda_workflows_por_job_{422a6f3,a508d6b}.salida.jsonl`.
- `sonda_complementaria.py`. Salidas: `sonda_complementaria.salida.jsonl` y `.stderr`.
  Entrada: `registro_reservas_953af02.json`.
- `sonda_piloto.py`. Salida: `sonda_piloto.salida.jsonl`.

**Ejecución de pruebas y mutación:**
- `sin_red_unittest.py`: ejecuta unittest con la red bloqueada. Salidas:
  - `pruebas_422a6f3*.jsonl` y `pruebas_422a6f3.log`;
  - `pruebas_nuevas_sobre_a508d6b.jsonl`;
  - `prueba_modificada_sobre_a508d6b.jsonl`.
- `mutantes.py`. Salidas: `mutantes.salida.jsonl` y `<rev>/mutantes/*.jsonl`.
  Las copias mutadas se borraron después de ejecutarlas.

**Copias:**
- `<rev>/encargo/`: el encargo y las sondas originales.
- `<rev>/base_a508d6b/`: la copia de a508d6b, con las pruebas nuevas copiadas.
