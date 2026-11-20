# Revisión independiente de la automatización · a508d6b

Rama `automatizacion/coordinacion-api-v1` @ `a508d6b`, repositorio
`jluisplagos/munger-v2-evidencias-mistral`. Fecha: 17-nov-2026.

**Estado: revisado, con hallazgos. No está aceptado ni integrado.** Lo ha revisado
un agente distinto del autor. La revisión consiste en leer el código y ejecutar
pruebas y sondas locales sin red. No se ha llamado a Anthropic, Mistral, Qwen ni
GitHub Actions. No se ha lanzado ningún workflow. No se han leído secretos. Las
pruebas mecánicas que se citan **no equivalen a una auditoría recibida**: en
particular, no sustituyen la auditoría Fable `audit-pilot-code-001`, que no se
recibió.

Rutas: `<rev_auto>` es el worktree revisado, que no se ha modificado. `<salida>`
es el directorio de esta entrega.

## 1. Alcance revisado

- Objetivo principal: commit `0956bc5` «Corregir transporte SSE sin repetir inferencia».
  Incluye `read_stream` y `StreamingHTTP` en `automation/coordination/critical_review.py:58-119`
  y sus pruebas en `test_critical_review.py`.
- El uso de esas funciones en `run()`, `budget()` y `Receipt` (`critical_review.py:149-263`),
  y su reutilización en `qwen_peer_review.py`.
- Revisión breve de `automation/claude_review/pilot.py`. Su única diferencia con la rama
  `automatizacion/piloto-claude-api` (7d9001e) es el parámetro `model` con lista de modelos
  autorizados. También `vibe_connection.py`, `run_vibe_auth.py`, `qwen_bank_review.py`,
  `qwen_group_review.py`, `qwen_peer_review.py` y los 6 workflows de `.github/workflows/`.
- Se consultó en local la rama de registro
  `origin/automatizacion/claude-api-piloto-registro`, solo para leer (`git show`).

## 2. Resultado de las pruebas existentes

Se ejecutaron sobre una copia: `<salida>/copia`, copiada con `cp -r` y sin el archivo
`.git`. Python 3.13.18. `python3 -I -m pytest` no se pudo usar porque pytest no está
instalado (`ModuleNotFoundError`), así que se usó unittest. El registro completo está
en `<salida>/sondas/pruebas_existentes.log`.

| Comando (cwd `<salida>/copia`) | Código | Recuento |
|---|---|---|
| `python3 -I -m unittest discover -s automation/claude_review -p test_pilot.py -v` | 0 | 49 OK |
| `python3 -I -m unittest discover -s automation/coordination -p test_critical_review.py -v` | 0 | 22 OK |
| `python3 -I -m unittest discover -s automation/coordination -p test_qwen_bank_review.py -v` | 0 | 14 OK |
| `python3 -I -m unittest discover -s automation/coordination -p test_qwen_group_review.py -v` | 0 | 3 OK |
| `python3 -I -m unittest discover -s automation/coordination -p test_qwen_peer_review.py -v` | 0 | 5 OK |
| `python3 -I -m unittest discover -s automation/coordination -p test_vibe_auth.py -v` | 0 | 7 OK |

Total: 100 pruebas, 0 fallos. Las 7 pruebas SSE nuevas alimentan `read_stream` con
`io.BytesIO`, en líneas completas. Ninguna prueba ejercita `StreamingHTTP.call`. Tampoco
cubren `http.client` real, CRLF, varias líneas `data:`, cortes a mitad, `message_delta`
sin `usage` ni datos JSON que no sean objeto.

## 3. Sondas propias (sin red)

- `<salida>/sondas/sonda_sse.py` → `<salida>/sondas/sonda_sse.salida.jsonl`
  - Comando: `python3 -I <salida>/sondas/sonda_sse.py <salida>/copia`. Código 0.
  - Resultado: 25 casos, 16 conformes y 9 hallazgos.
  - Método: un `http.client.HTTPResponse` real lee bytes simulados desde un socket falso.
    Entrega trozos de 7 bytes, con chunked de 11 bytes y caracteres multibyte partidos.
    Solo se sustituye `build_opener` dentro del proceso.
- `<salida>/sondas/sonda_workflows.sh` → `<salida>/sondas/sonda_workflows.salida.txt`
  - Comando: `sh <salida>/sondas/sonda_workflows.sh <rev_auto>`. Código 0.
  - Es un inventario estático de disparadores, permisos, secretos, escrituras y bucles.

## 4. Hallazgos

No se encontró ningún hallazgo **material**: ningún caso produce una segunda inferencia,
libera la reserva ni acepta un resultado falso. Los hallazgos medios afectan a la
trazabilidad del estado «sin veredicto / coste incierto» y a los controles de gasto.

### Medios

**M1. Un corte limpio a mitad de un chunk escapa del transporte. No queda informe ni estado.**

- Dónde: `critical_review.py:114-119` (excepciones capturadas), `critical_review.py:256`
  (`run` solo captura `PilotError`) y `critical_review.py:278` (`main`). También
  `qwen_peer_review.py:190`.
- Causa: `http.client.IncompleteRead` y `LineTooLong` heredan de `HTTPException`, no de
  `OSError` ni de `ValueError`. Esto ocurre ante un EOF limpio de TLS o de un proxy.
- Contraejemplo: sondas S08 y S17. El servidor responde
  `HTTP/1.1 200`, `Transfer-Encoding: chunked`, `message_start`… y después `40\r\n`
  seguido de 37 bytes y EOF.
  - Resultado: `ESCAPA:http.client.IncompleteRead`.
  - En `run()`: solo queda `sources.json` en local y no se publica nada. La reserva queda
    en `RESERVADO_NO_REINTENTAR` y el proceso termina con traceback (código 1).
  - Lo que sí está bien: hay una sola inferencia y la segunda ejecución devuelve
    `YA_RESERVADO_SIN_NUEVA_LLAMADA`.
- Efecto: el fallo no se publica como «enviado, sin veredicto, coste incierto», que es
  justo lo que la corrección quería garantizar.
- Corrección propuesta:
  - Añadir `http.client.HTTPException` a la rama de red de `StreamingHTTP.call`.
  - En `run()`, después de `receipt.reserve`, capturar cualquier `Exception` y convertirla
    en un estado de fallo publicado.
- Prueba de cierre: S08 y S17 dan `PilotError(..._NO_REINTENTAR)`. `report.json`, `report.md`
  y `reservation.json` se publican con el estado de M4 y hay exactamente 1 inferencia.

**M2. Los eventos con JSON válido que no es un objeto, o anidado en exceso, escapan con `AttributeError` o `RecursionError`.**

- Dónde: `critical_review.py:71-93`, en las llamadas `event.get`, `block.get`, `delta.get`
  y `message.update`, y en la lista de capturas de `critical_review.py:118`.
- Contraejemplo (sondas S11, S11b, S12):
  - `data: []` → `AttributeError: 'list' object has no attribute 'get'`.
  - `{"type":"content_block_delta","index":1,"delta":"x"}` → `AttributeError`.
  - `data: ` seguido de 200 000 `[` y 200 000 `]` (menos de 2 MB) → `RecursionError`.
- Consecuencia: la misma que en M1.
- Corrección propuesta: comprobar `isinstance(..., dict)` en `event`, `message`,
  `content_block`, `delta` y `usage`, y que los índices y textos tengan el tipo esperado.
  Capturar `RecursionError` y convertirla en `ANTHROPIC_STREAM_INVALIDO_NO_REINTENTAR`.
- Prueba de cierre: S11, S11b y S12 dan `PilotError`. Se añade una prueba unitaria por
  cada tipo incorrecto.

**M3. El uso final no se exige: un stream sin `usage` en `message_delta` se acepta con el `output_tokens` provisional.**

- Dónde: `critical_review.py:89-98`, y la verificación posterior en `critical_review.py:248-253`.
- Contraejemplo (sonda S10): un stream completo cuyo `message_delta` solo trae
  `{"delta":{"stop_reason":"end_turn"}}`. Se devuelve
  `usage={"input_tokens":200,"output_tokens":1,...}`.
  - `run()` lo trata como consumo verificable y calcula un coste ínfimo.
  - La acumulación con un `message_delta` acumulativo sí es correcta (S09: 200/500).
- Corrección propuesta: exigir al menos un `message_delta` con `usage.output_tokens` entero
  antes de `message_stop`. Si falta, devolver `STREAM_SIN_USO_FINAL`, con el estado de M4
  y el coste anotado como incierto.
- Prueba de cierre: S10 da `PilotError`. Se añade una prueba unitaria con dos
  `message_delta` y con `usage` acumulativo que incluya `input_tokens`.

**M4. Un fallo con coste incierto no se distingue en el estado de un rechazo con coste conocido, y se pierde el uso parcial.**

- Dónde: `critical_review.py:242` y `256-262`.
- Contraejemplo (sonda S18): un timeout de lectura tras `message_start` produce
  `state=RESULTADO_NO_ACEPTADO_NO_REINTENTAR`, `estimated_cost_usd=null` y no guarda `usage`.
  - Un rechazo por `max_tokens` (S19) o por una cita inventada produce el mismo `state`,
    aunque con coste calculado.
  - En el registro real, `audit-pilot-code-001` tiene `state=RESULTADO_NO_ACEPTADO_NO_REINTENTAR`,
    `error=ANTHROPIC_ERROR_RED_TIMEOUT` y `estimated_cost_usd=null`. No tiene ningún campo
    que diga «coste incierto, cota USD 1,912936».
- Qué está bien: no hay repetición (S18: 1 inferencia y `YA_RESERVADO_SIN_NUEVA_LLAMADA`).
  `api_messages_sent=1` se fija antes de la llamada.
- Corrección propuesta:
  - Un estado propio, p. ej. `INFERENCIA_SIN_VEREDICTO_COSTE_INCIERTO`.
  - Un campo `cost_status` con valor `INCIERTO`, `cost_upper_bound_usd = budget.reserved_usd`
    y `usage_partial`, este último tomado de `message_start` como cota inferior.
  - Aplicarlo también a `CONSUMO_NO_VERIFICABLE` y `FACTURACION_NO_PREVISTA`.
- Prueba de cierre: en S18 el estado y la cota aparecen en `report.json` y en
  `reservation.json`. Se añade una prueba unitaria que compare los estados de un timeout
  y de `max_tokens`.

**M5. No hay un tope acumulado: solo hay una reserva por tarea.**

- Dónde: `critical_review.py:23` y `149-155` (`MAX_USD` por llamada) y
  `qwen_peer_review.py:153-155` (USD 0,50 por tanda).
- Comparación: `pilot.py:190-198` sí suma el ensayo previo, pero solo dentro de su piloto.
- Contraejemplo: `Receipt.prior()` solo busca `reviews/<TASK>/reservation.json`.
  - Si se cambia `TASK` a `audit-pilot-code-002`, se puede reservar hasta USD 2 adicionales.
    No se tienen en cuenta los USD 1,912936 inciertos del intento 001: la exposición
    conjunta llega a unos USD 3,9.
  - Si la matriz de `qwen-bank-mistral-groups.yml:24` pasa de `[1]` a `[1..6]`, se abren
    6 reservas de USD 0,50 sin ningún techo conjunto.
- Corrección propuesta: un registro global, create-only, de reservas y costes (los ciertos
  más las cotas de los inciertos). Antes de cada `reserve`, verificar
  `suma + nueva_reserva ≤ techo autorizado por la persona responsable`.
  - Este revisor no fija esa cifra: es una decisión económica humana.
- Prueba de cierre: una prueba unitaria con dos tareas distintas cuya suma supere el
  techo, en la que la segunda falla antes de `reserve` y antes de `count_tokens`.

**M6. La inferencia de pago se dispara al hacer push del código, sin una puerta humana.**

- Dónde:
  - `claude-critical-review.yml:2-8` y `38-42` (`--execute-api` en cada push que toque
    `critical_review.py` o su test).
  - `qwen-bank-mistral-groups.yml:2-8` y `42-49`.
  - `qwen-bank-mistral-review.yml:2-9`.
  - `vibe-auth.yml:2-8`.
- Contraejemplo:
  - Un push que incluya el cambio de `critical_review.py` de `0956bc5` dispara el job
    `review` con la clave. Que llegara a ejecutarse no se ha comprobado sin red.
  - Lo único que impide el gasto es que ya existe la reserva de `audit-pilot-code-001`.
    En el registro está y bloquea, lo que es conforme.
  - Pero cualquier commit que cambie `TASK` o los límites gasta en cuanto se hace push,
    sin aprobación previa.
- Corrección propuesta: `workflow_dispatch` (o push solo para las pruebas) y un
  `environment` con revisores obligatorios para los pasos que usan
  `ANTHROPIC_API_KEY` o `MISTRAL_VIBE_CLI_KEY`.
- Prueba de cierre: la sonda de workflows no muestra ningún paso con secreto de inferencia
  bajo `push` sin `environment:` protegido.

**M7. Se instala un paquete de terceros en el mismo job que la clave de Anthropic y un token con escritura.**

- Dónde: `qwen-bank-mistral-groups.yml:33` (`pip install mistral-vibe==3.1.2` sin
  `--require-hashes`, con dependencias transitivas sin fijar), en el mismo job que
  `ANTHROPIC_API_KEY` (líneas 42-49) y `contents: write`.
- Riesgo: un `.pth` o `sitecustomize` instalado se ejecuta en el paso posterior de
  `python ... qwen_peer_review.py`, que ya tiene la clave en su entorno.
- Corrección propuesta: separar en jobs distintos el contraste Mistral y la revisión
  Claude, pasando artefactos entre ellos, e instalar con hashes (`pip install --require-hashes -r`).
- Prueba de cierre: la sonda de workflows no encuentra ningún job que combine
  `pip install` sin hash y `ANTHROPIC_API_KEY`.

### Menores

- **m1. Se ignora la línea `event:`.** `critical_review.py:66-74`. S13: `event: error` con
  `data: {"type":"overloaded_error"}` se ignora y el stream termina con éxito. Es un caso
  artificial: Anthropic envía `data.type=error`. Corrección: guardar el nombre del evento
  y rechazar `error` o cualquier discrepancia entre `event:` y `data.type`.
  Prueba de cierre: S13 da `PilotError`.
- **m2. La cota de tamaño se comprueba después de leer la línea entera.**
  `critical_review.py:61-64`. S16: una línea de 5 MB se materializa completa antes de
  `STREAM_DEMASIADO_GRANDE`. Corrección: `response.readline(65537)` en bucle, con un
  límite por línea. Prueba de cierre: S16 con `bytes_en_memoria ≤ 2 000 001`.
- **m3. El modelo del cuerpo no está ligado a la lista de modelos autorizados.**
  `pilot.py:83` y `critical_review.py:103-109`: la lista solo cubre la ruta
  `/v1/models/<modelo>`. S20: un cuerpo con `model=claude-opus-5-5` se envía.
  `run()` lo rechaza después (`FACTURACION_NO_PREVISTA`), pero la llamada ya está pagada.
  Corrección: en `call()`, exigir `body['model'] == self.model`, `service_tier` y ausencia
  de `tools`. Prueba de cierre: S20 rechazado antes de abrir la conexión.
- **m4. No se verifican los campos de facturación del uso.** `critical_review.py:249-253`:
  no se comprueban `usage.service_tier`, `usage.speed` ni `usage.inference_geo`. En el
  registro de `qwen-peer-group-01` aparecen `standard/standard/global`. El coste estimado
  supone precio estándar global. Corrección: si esos campos tienen otro valor, devolver
  `FACTURACION_NO_PREVISTA`. Prueba de cierre: una prueba unitaria con `speed=fast` rechazado.
- **m5. No hay un plazo total para la inferencia.**
  - Dónde: el timeout de 60 s es por operación de socket (`critical_review.py:111-112`).
    El job tiene `timeout-minutes: 15` (`claude-critical-review.yml:27`).
  - Riesgo: si GitHub mata el job a mitad de stream, no queda informe. Con
    `EFFORT='max'` y `MAX_OUTPUT=32768` en Fable 5.2 también existe el riesgo de
    `max_tokens`: pago sin veredicto.
    - Ese riesgo es una observación económica, no una decisión de este revisor.
  - Corrección: un plazo total en el código, inferior al del job, que publique el estado de M4.
  - Prueba de cierre: una sonda con lector lento que supere el plazo y dé un estado publicado.
- **m6. La restricción de ramas solo está en el código.** El `GITHUB_TOKEN` con
  `contents: write` vale para todo el repositorio, y la rama solo la fija el código
  (`pilot.py:260`, `qwen_bank_review.py:58`). No se encontró ninguna escritura en `main`
  ni en `coordinacion/cierre-v2`, ni en `CONTROL.json` o `ESTADO.md`. Las únicas
  escrituras son PUT/POST sobre `automatizacion/claude-api-piloto-registro`.
  - `pilot.py:121` solo **lee** `coordinacion/cierre_v2/`.
  - Las reglas de protección remotas no se pudieron verificar sin red.
  - Corrección: un ruleset que impida a `github-actions[bot]` escribir en `main` y en
    `coordinacion/cierre-v2`.
  - Prueba de cierre: la consulta del ruleset, que debe hacer la persona responsable.
- **m7. El CLI de Vibe arranca en la raíz del repositorio y la invocación previa no se cuenta.**
  - Dónde: `qwen_bank_review.py:195-197` y `214-217` llaman a `subprocess.run` sin `cwd=`.
    En cambio, `vibe_connection.py:47` usa `cwd=work`. El proceso del CLI arranca en la
    raíz del checkout, aunque `--workdir` apunte a un directorio vacío.
  - Además, la invocación preparatoria con `--max-tokens 0` no cuenta en
    `generation_invocations_started`.
  - Corrección: `cwd=work` y un contador para la invocación preparatoria.
  - Prueba de cierre: una prueba unitaria con un `runner` falso que compruebe `cwd`.
- **m8. Las sustituciones de texto pueden fallar en silencio.** `qwen_group_review.py:60-64`
  modifica `q.SYSTEM` y `q.BASE_CONFIG` con `str.replace`. Si el texto cambia, no ocurre
  nada y no se avisa, aunque la reserva declara `max_output_tokens: 32768` en cualquier
  caso. Corrección: comprobar que cada reemplazo se aplicó.
  Prueba de cierre: la prueba falla si `BASE_CONFIG` no contiene `32768`.
- **m9. Se entrega el secreto a un paso que no lo necesita.** `vibe-readiness.yml:24-26`
  pasa `MISTRAL_VIBE_CLI_KEY` a un paso que nunca usa `--execute`, después de instalar
  el paquete. Corrección: quitar el secreto de ese paso.

### Límites de esta revisión

- No es posible comprobar «sin pago por uso» desde el código. Una clave de API de Anthropic
  se factura por consumo o con créditos: `credit_source=NO_COMPROBADA_EN_CONSOLE`. Los
  límites `--max-price` de Vibe son acumulados y no un techo previo, como el propio código
  documenta. Hay que verificarlo en las consolas.
- No se ha observado el ritmo real de los `ping` de Anthropic durante el razonamiento con
  `display` omitido.
  - La comprobación en vivo queda fuera de esta revisión, que no hace llamadas.
  - En el registro, `qwen-peer-group-01` (código a508d6b, Sonnet 5.5) consta con
    `end_turn` y 6735 tokens de salida a través de `StreamingHTTP`. Es un dato del registro,
    no verificado ante el proveedor.
- Los precios 8/40 (Fable 5.2) y 2/10 (Sonnet 5.5) coinciden con la tabla pública conocida
  por el revisor (caché del 3-nov-2026). No se consultaron en vivo.

## 5. Conforme

- **Sin reintentos automáticos.** `urllib` no reintenta, `NoRedirect` está activo y no hay
  bucles `while`. Ante RST, timeout de lectura, EOF entre chunks o EOF sin chunked hay
  exactamente 1 apertura y un `PilotError ..._NO_REINTENTAR` (S08b-e). Que `run()` no
  repita en un timeout se comprueba en `test_timeout_not_retried` y en S18.
- **Reserva create-only antes de la llamada de pago:**
  - `receipt.prior()` se consulta antes de cualquier llamada a Anthropic
    (`critical_review.py:231-234`), y `reserve` va antes de `/v1/messages` (línea 240).
  - Cualquier error de GitHub distinto de 404 bloquea la inferencia.
  - La reserva nunca se borra. La reescritura final conserva `budget` y solo cambia
    `state` (línea 262).
  - Un fallo de publicación mantiene el bloqueo (`test_publication_failure_keeps_reservation`).
  - `claim_after_zero_generation` (`qwen_bank_review.py:55-59`) solo reabre con una prueba
    fijada de cero generaciones, y después vuelve a `RESERVADO_NO_REINTENTAR`.
- **`audit-pilot-code-001` no puede repetirse.** En el registro existe `reservation.json`
  con `state=RESULTADO_NO_ACEPTADO_NO_REINTENTAR`, `code_sha=501fd8b…` y
  `reserved_usd=1.912936`. Con `TASK` sin cambiar, `run()` devuelve
  `YA_RESERVADO_SIN_NUEVA_LLAMADA` antes de `/v1/models` y `count_tokens`.
- **Parser SSE:**
  - Eventos y UTF-8 partidos entre lecturas o chunks (S01), varias líneas `data:` (S02),
    CRLF (S03), `ping` y comentarios (S07).
  - `error` a mitad (S04), `message_stop` ausente (S05, S14), JSON sin SSE (S15).
  - `max_tokens`: se devuelve, y `run()` lo rechaza con coste calculado (S06a, S19).
  - Acumulación correcta del `usage` acumulativo (S09).
  - No se guarda el razonamiento, se rechazan los bloques `tool_use`, hay cota de tamaño
    y se detecta el `message_start` duplicado.
- **Presupuesto:**
  - La reserva previa se calcula con el límite de salida (`max_tokens = MAX_OUTPUT`) y
    con una cota de entrada de `max(tokens contados, bytes) + 4096`, y se comprueba
    antes de reservar (`test_budget_blocks_before_reserving`).
  - Después de la llamada se comprueban el modelo devuelto y la caché, y se pide
    `service_tier: standard_only`.
- **Secretos:**
  - No van en prompts ni en informes, y los errores solo llevan códigos.
  - Vibe se ejecuta sin `GH_TOKEN`, `GITHUB_TOKEN` ni `ANTHROPIC_API_KEY`, en un
    `VIBE_HOME` vacío y sin herramientas.
  - `persist-credentials: false`, todas las acciones fijadas por SHA y ningún
    `pull_request_target`, `schedule` ni `workflow_run`.
- **Sin bucles de workflow:** las escrituras con `GITHUB_TOKEN` van a la rama de registro,
  que no figura en ningún disparador.

## 6. Resumen de cierre propuesto

Reejecutar `<salida>/sondas/sonda_sse.py` sobre la versión corregida y obtener 25/25
CONFORME. Añadir como pruebas unitarias S08, S10, S11, S12, S13, S16, S17, S18 y S20 y
las pruebas de M4 y M5. La corrección debe revisarla un agente distinto de su autor.
Ninguna corrección autoriza otra inferencia de `audit-pilot-code-001`, ni una tarea nueva
de pago sin aprobación humana explícita y un tope acumulado fijado por la persona responsable.
