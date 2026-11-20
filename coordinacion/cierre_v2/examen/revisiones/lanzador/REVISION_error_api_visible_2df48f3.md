# Revisión crítica independiente · error de la API visible (2df48f3)

- Repositorio: `jluisplagos/munger-v2-evidencias-mistral`
- Rama revisada: `automatizacion/error-api-visible`, commit `2df48f34246eadb38fdc1a282d0b3f1197824e46` sobre `main` `69f0385`
- Diff: `git diff 69f0385 2df48f3` (3 archivos: `automation/coordination/critical_review.py`, `automation/coordination/test_auto1_transporte.py`, `automation/direct_analysis/direct_analysis.py`)
- Revisor: agente distinto del autor del cambio. Sin modificar la rama, sin commit, sin llamadas a la API ni a GitHub Actions.
- Fecha: 18-nov-2026

## Veredicto

**CONFORME CON LÍMITES.**

El cambio hace lo que promete en lo esencial: tras un `HTTPError` de `/v1/messages` lee como máximo 4096 bytes del cuerpo de la respuesta, conserva solo `http_status`, `type` (≤ 80), `message` (≤ 600) y un `request_id` bien formado, y los lleva a `report.json`, al recibo publicado y a la línea de stdout del lanzador. No añade llamadas ni reintentos y no toca la reserva, el tope acumulado ni el estado de coste. No hay ningún hallazgo bloqueante. El límite principal es que, en el análisis directo, `report.md` (y por tanto el resumen del job) **no** muestra el error de la API, en contra de lo que dice la descripción del cambio (hallazgo 1).

## Respuestas a las cinco preguntas

### 1. Seguridad

- **Clave y cabeceras:** no pueden salir por este cambio. `api_error_of` solo llama a `err.read(4096)` y a `err.code`; no lee `err.headers`, `err.hdrs`, `err.url` ni el `Request` (donde está `x-api-key`). La API de Anthropic no devuelve la clave en el cuerpo del error (un 401 dice solo «invalid x-api-key»). Prueba ad hoc con `api_key='SECRETKEY123'`: la cadena no aparece en `report.json`, `report.md`, `sources.json` ni en lo publicado en el recibo. GitHub, además, enmascara los secretos en el log.
- **Cuerpo de la petición y paquete:** solo se copian dos cadenas del cuerpo de la respuesta (`error.type` y `error.message`); el resto del JSON se descarta. Los mensajes de Anthropic describen el fallo («prompt is too long: N tokens > M maximum», «max_tokens: …», nombre de modelo, ruta de campo como `messages.0.content.1`). No se puede garantizar que un error de validación nunca cite un valor de la petición, pero quedaría limitado a 600 caracteres. Lo único que podría citarse es contenido del paquete o del encargo, que ya está versionado en este mismo repositorio (`load_package` lo lee de un commit fijado); no es un secreto, aunque sí acabaría en el log y en el recibo publicado (hallazgo 4).
- **Inyección de comandos del runner:** la línea de stdout es `json.dumps(...)`, así que los saltos de línea quedan escapados (`\n`) y ninguna línea puede empezar por `::`. Comprobado con un mensaje `a\n::add-mask::zzz\n::error::pwn`: sale en una sola línea que empieza por `{`. En `report.md` de AUTO1 (`cr.write`) también se usa `json.dumps`.

### 2. Gasto

- **Sin segunda llamada ni reintento.** `api_error_of` se ejecuta dentro del `except HTTPError` y solo lee la respuesta ya recibida; después se lanza `TransportError` como antes. Prueba ad hoc con el `StreamingHTTP` real y un abridor que devuelve 400: 1 apertura de conexión; llamadas `GET /v1/models`, `POST count_tokens` y un único `POST /v1/messages`.
- **Reserva, tope y estado de coste sin cambios.** En `run()` la línea nueva va después de `_cost_fields` y de `report['error']`, y solo añade `report['api_error']`. Resultado comprobado: `state = INFERENCIA_SIN_VEREDICTO_COSTE_INCIERTO`, `cost_status = INCIERTO`, `cost_upper_bound_usd == budget.reserved_usd ==` la reserva registrada en el recibo. `publish` y `reservation.json` no incluyen `api_error`; `report.json` sí.
- El error 400 no se reclasifica como «no facturado»: el estado sigue INCIERTO con la reserva como cota, que es lo pedido.

### 3. Robustez

- **Excepciones contenidas:** todo el cuerpo de `api_error_of` está en `try/except Exception`, que devuelve `{'http_status': …, 'message': 'CUERPO_DEL_ERROR_ILEGIBLE'}` con `getattr(err, 'code', None)`. Comprobado: cuerpo no JSON, `error` como cadena en vez de objeto, `code=None` (el `int(None)` cae en el `except`), `read()` que lanza `OSError`. Ninguno escapa. Además, el `except HTTPError` de `call` ya estaba dentro de un `try` cuyo resultado acaba siempre en `TransportError`, y `run()` captura `Exception` tras la reserva.
- **Tamaño acotado de verdad:** `err.read(4096)` sobre un cuerpo de 10 MB consume exactamente 4096 bytes (`tell() == 4096`). Las cadenas se recortan a 80 y 600 caracteres y `request_id` debe cumplir `req_[A-Za-z0-9]{1,64}`.
- **Límite de tiempo:** la lectura del cuerpo no está sujeta al plazo `STREAM_DEADLINE_SECONDS`, solo al timeout de socket de 60 s por lectura (hallazgo 3).

### 4. Pruebas

Ejecutadas exactamente como en CI, en el worktree en `2df48f3`:

| Comando | Base 69f0385 | 2df48f3 |
|---|---|---|
| `python3 -I -m unittest discover -s automation/claude_review -p 'test_*.py'` | 49 OK | 49 OK |
| `python3 -I -m unittest discover -s automation/coordination -p 'test_*.py'` | 95 OK | 97 OK (+2) |
| `python3 -I -m unittest discover -s automation/direct_analysis -p 'test_*.py'` | 37 OK | 37 OK |

- No se rompe ninguna prueba de inventario ni de integridad. No hay ninguna prueba que fije la huella de `critical_review.py` ni que cuente pruebas. `verify_code` del lanzador compara los bytes locales con el SHA observado en tiempo de ejecución, sin huella fijada en el código.
- Lo que cubren las dos pruebas nuevas: el 400 completo a través de `cr.run` con el transporte real (`error`, `api_error`, estado y coste INCIERTO con la reserva como cota, `report.md` de AUTO1 y `report.json` del recibo); cuerpo no JSON; cuerpo enorme; `request_id` malformado descartado.
- Lo que no cubren (hallazgos 1, 2 y 5): la ruta del análisis directo (`make_writer`/`render` y la línea de stdout de `main`); que haya una sola apertura en la ruta de error; el recorte a 600 de un mensaje largo dentro de un JSON válido (la prueba de «cuerpo enorme» pasa porque el JSON truncado da `CUERPO_DEL_ERROR_ILEGIBLE`, no porque se recorte); que la clave no aparezca en las salidas.

### 5. Workflow `.github/workflows/analisis-directo.yml`

**No necesita cambios para que el mensaje se vea en el log.** El paso «Una llamada como maximo, sin reintentos» ejecuta `direct_analysis.py` sin redirigir stdout, así que la línea JSON con `api_error` sale en el log del job, y `report.json` va en el artefacto `munger-analisis-directo-<run_id>`. El paso «Resumen» vuelca `report.md` a `$GITHUB_STEP_SUMMARY`, pero ese `report.md` lo genera `render()` del análisis directo, que no incluye `api_error`. Si se quiere en el resumen, el cambio va en `render()` de `direct_analysis.py`, no en el workflow.

## Hallazgos

1. **Media. `report.md` del análisis directo no muestra el error de la API.** `direct_analysis.configured` sustituye `cr.write` por `make_writer(...)`, que usa `render()`, y `render()` solo añade ``Error: `ANTHROPIC_HTTP_400` `` (líneas 540-541). La línea «Error de la API» añadida a `cr.write` solo aparece en `report.md` de AUTO1 (`critical_review.py`, workflow `claude-critical-review.yml`). La descripción del cambio («report.json, report.md y la línea de stdout del lanzador») es exacta para AUTO1, pero no para el lanzador de análisis directo, que es el que falló. Consecuencia: en el resumen del job de Ahold seguiría viéndose solo `ANTHROPIC_HTTP_400`; la causa estaría en el log y en `report.json`. Corrección sugerida: en `render()`, justo después del bloque `if 'error' in report`, añadir una línea con `json.dumps(report['api_error'], ensure_ascii=False)` en un bloque de código (para que no se interprete como markdown), y una prueba en `automation/direct_analysis` que la compruebe.
2. **Baja. Las pruebas nuevas no recorren el lanzador de análisis directo.** Ninguna prueba de `automation/direct_analysis` comprueba que `main()` imprima `api_error`, ni que `DirectHTTP` (subclase de `StreamingHTTP`) lo propague. Funciona por herencia, pero no queda fijado por una prueba en la suite que corre el workflow de análisis directo.
3. **Baja. La lectura del cuerpo del error no respeta el plazo total.** `err.read(4096)` solo queda limitado por el timeout de socket de 60 s por lectura, no por `STREAM_DEADLINE_SECONDS`. Un servidor que gotee bytes podría alargar la lectura, en teoría, más allá del `timeout-minutes: 20` del job. Si eso pasa, la reserva ya está publicada y el informe no. El caso es muy improbable con `api.anthropic.com` y antes no se leía nada. Mitigación opcional: comprobar el plazo antes de leer, o leer con un plazo propio corto.
4. **Baja. El mensaje del proveedor pasa a ser público.** Hasta ahora `pilot.HTTP` se negaba explícitamente a imprimir el «cuerpo del proveedor» (`pilot.py:116`). Este cambio relaja esa regla para `/v1/messages`: hasta 600 caracteres del mensaje de Anthropic van al log, al artefacto y al `report.json` que el recibo publica en el repositorio. Es aceptable, porque lo único que podría citarse está ya versionado en el repo y nunca hay credenciales, pero conviene dejar constancia de la decisión. Los errores de `/v1/models` y `count_tokens` siguen opacos, porque pasan por `pilot.HTTP` sin cambios.
5. **Baja. Huecos de las pruebas nuevas.** (a) La clase `ApiErrorVisibleTests` está después de `if __name__ == '__main__': unittest.main(...)`, así que con `python3 test_auto1_transporte.py` no se ejecuta, porque `unittest.main` sale antes de definirla. Con `discover`, como en CI, sí se ejecuta. (b) Falta un caso con JSON válido y `message` de más de 600 caracteres dentro de 4 KB, que compruebe el recorte real. (c) Falta comprobar que la ruta de error abre una sola conexión y que la clave no aparece en las salidas. Las tres cosas las he comprobado aquí con una sonda propia, sin versionarla.
6. **Informativa. Un JSON truncado se pierde entero.** Si el cuerpo supera 4096 bytes, el JSON queda truncado y el resultado es `CUERPO_DEL_ERROR_ILEGIBLE` en lugar de un mensaje parcial. Los errores de Anthropic ocupan mucho menos, así que es aceptable.
7. **Informativa. Referencias de línea desplazadas.** `automation/coordination/ENTREGA_AUTO1.json` cita líneas de `critical_review.py` (236, 485, 550…) que, a partir de este commit, se desplazan unas 30 líneas. Es un registro histórico anclado a su propia base (`267ad18`) y ninguna prueba lo valida. No hay que cambiarlo; solo no debe leerse contra `2df48f3`.

## Comprobaciones realizadas

- Lectura del diff completo y del contexto: `StreamingHTTP.call`, `run`, `publish`, `write` de `critical_review.py`; `configured`, `make_writer`, `render`, `DirectHTTP`, `execute`, `main` de `direct_analysis.py`; `pilot.HTTP.call`; los workflows `analisis-directo.yml` y `claude-critical-review.yml`.
- Las tres suites de CI en `2df48f3` y en `69f0385` (en un worktree temporal, ya eliminado).
- Sonda ad hoc en el directorio temporal de la sesión (no versionada): lectura acotada con un cuerpo de 10 MB; `code=None`; `error` no objeto; `read()` que lanza; mensaje con `\n::add-mask::`; `cr.run` con el transporte real y un 400 (1 apertura, 1 `POST /v1/messages`, coste INCIERTO = reserva, clave ausente de todas las salidas).

## Respuesta del autor (coordinador) · 4ff75ab
- Hallazgo principal (render() del análisis directo no mostraba `api_error`): corregido; `report.md` y el resumen del job muestran tipo y mensaje (comillas invertidas neutralizadas). Prueba `ApiErrorRenderTests`.
- Clase de prueba nueva movida antes de `if __name__ == '__main__'`.
- Límites aceptados: el mensaje de Anthropic podría citar texto del paquete (ya versionado y público); la lectura del cuerpo usa el timeout de socket de 60 s.
- CI local: 49 + 97 + 38, todas OK.
