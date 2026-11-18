# Revisión crítica independiente · esquema sin gramática (08fa48f)

- Repositorio: `jluisplagos/munger-v2-evidencias-mistral`
- Rama `automatizacion/esquema-sin-gramatica`, commit `08fa48f` sobre `main` `4ff75ab`
  (worktree `/home/user/e_work/wt_analisis_directo`, HEAD verificado = `08fa48ffb6d5…`).
- Diff revisado: `git diff 4ff75ab 08fa48f` (`direct_analysis.py`, `test_direct_analysis.py`).
- Revisor: agente distinto del autor del cambio. No se ha modificado la rama ni hecho commit.
  No se ha hecho ninguna llamada a la API de Anthropic.
- Evidencia consultada: registro de la ejecución 44288081039 (`gh run view --log`) y su
  `reservation.json` y `sources.json` publicados en `automatizacion/claude-api-piloto-registro`.

## Veredicto

**CONFORME CON LÍMITES.**

El control de gasto queda intacto y el cambio resuelve el 400 sin abrir ningún camino de
aceptación indebida. El límite real: sin gramática, un fallo de **forma** (no de contenido)
se paga y queda `RESULTADO_NO_ACEPTADO_NO_REINTENTAR`. Hay mejoras baratas (sección 2) que
conviene aplicar antes de gastar otra vez unos 4,5 USD de reserva, y hay una alternativa
(sonda de compilación de un esquema simplificado) que, si la persona responsable la
autoriza, es la opción más segura.

## 1. Gasto

| Comprobación | Resultado |
|---|---|
| Una sola llamada de inferencia, sin reintentos | **Sí.** `cr.run` sin cambios: `GET /v1/models`, `count_tokens` (gratis) y un único `POST /v1/messages` tras la reserva create-only. El transporte SSE no tiene bucle de reintento. |
| `preflight` cuenta el sistema ampliado | **Sí.** `preflight` usa `cr.payload`, que dentro de `configured()` es `payload_sin_gramatica`, y este lee `cr.SYSTEM = system_con_esquema(encargo)`. Comprobado: `payload_bytes == len(canonical(payload))` con el esquema dentro de `system`. |
| `budget` y `count_tokens` cuentan el sistema ampliado | **Sí.** `cr.run` y `cr.budget` llaman a `payload(bundle)` por nombre global del módulo `cr`, que resuelve al sustituto en tiempo de llamada. Comprobado: `reserved_input_tokens = len(canonical(payload_nuevo)) + 4096`. |
| `cr.payload` restaurado al salir | **Sí** (comprobado a mano). Tras salir de `configured()`, `cr.payload is` la función original, que vuelve a llevar `output_config.format` y el `SYSTEM` de AUTO1. AUTO1 (`critical_review.main`) corre en su propio proceso y no se ve afectado. |
| Cifras Ahold con el cambio | Reproducido sobre el `sources.json` publicado: `payload_bytes` 958 075; cota 962 171 tokens; reserva **4,504044 USD** (antes 4,498352). Margen al contexto: **5 061** tokens de cota. Conteo real de la ejecución fallida: 389 242 tokens, así que el coste real esperado ronda 1,6 USD de entrada más hasta 0,66 USD de salida. |

Nota: la ejecución 44288081039 sigue contando su reserva completa (4,498352 USD) en el tope
acumulado mientras su coste esté `INCIERTO`; conciliarla en Console (un 400 no debería
facturarse) libera ese margen.

## 2. Riesgo de pagar y perder sin gramática

Pruebas sobre `validate` con variantes de una respuesta correcta en contenido:

| Variante | Resultado |
|---|---|
| Enumeración con mayúsculas o tildes (`"Vigilar"`) | Aceptada y anotada (bien). |
| Bloque ```` ``` ```` sin `json` | Aceptada por la extracción tolerante y anotada (bien). |
| `null` en una cifra con `disponible: false` | `ESQUEMA_INVALIDO` |
| Número como texto (`"95"`) | `ESQUEMA_INVALIDO` |
| Clave extra (`"notas"`) | `ESQUEMA_INVALIDO:$` |
| Sinónimo de enumeración (`"mantener"`) | `ESQUEMA_INVALIDO` (correcto: es contenido) |
| Comillas sin escapar dentro de `cita` | `JSON_INVALIDO` |
| Llave `{` en el texto previo | `JSON_INVALIDO` |
| Dos objetos (borrador y final) | `JSON_INVALIDO` |
| Clave duplicada | **Aceptada en silencio** (gana la última) |

Estimación razonable (juicio, no medida): con Opus 5.5, esfuerzo alto, el esquema en el
sistema y el encargo que ya pide números con punto, `0` en cifras no disponibles y
minúsculas, la probabilidad de un fallo de forma es baja pero no despreciable: **del orden
de unos pocos por ciento por llamada**. El riesgo principal de sintaxis está en `citas`: el
encargo exige copiar fragmentos literales y el paquete incluye `.json` y `.csv` con comillas
y barras invertidas; una sola comilla sin escapar invalida todo. Le siguen el `null` en
cifras no disponibles y alguna clave añadida. (Independiente del cambio: con 389 k tokens de
entrada y esfuerzo alto, agotar `MAX_OUTPUT = 32 768` con el pensamiento sigue siendo el
otro modo de pagar y perder; no cambia aquí.)

### Mejoras baratas que no aflojan la validación del contenido

1. **Rescate sin llamada (la más rentable).** `report.json` ya conserva `raw_model_output`.
   Un modo fuera de línea, sin red, que vuelva a pasar `validate` sobre esa salida en bruto
   con una versión corregida del validador y lo registre como **expediente nuevo** (sin
   tocar el original ni reactivar nada) convierte un fallo de forma en «pagado y
   recuperable». Necesita una decisión humana registrada sobre su uso.
2. **Instrucciones explícitas en el bloque añadido** (`SCHEMA_EN_ENCARGO`), unas pocas
   líneas: escapar `"` y `\` dentro de las cadenas (sobre todo en `cita`); nunca `null`
   (usar `0` con `disponible: false`); ninguna clave fuera del esquema; un único objeto.
3. **Coerciones mínimas, registradas y de solo forma:** `null` → `0` **solo** cuando el
   hermano `disponible` es `false` (la cifra no significa nada). No convertir textos con
   coma decimal ni sinónimos de enumeraciones.
4. **Rechazar claves duplicadas** (`object_pairs_hook`): hoy se acepta la última en
   silencio, algo que con gramática no podía ocurrir.
5. Con el margen de Ahold (5 061 tokens de cota por bytes), no añadir un ejemplo completo
   del objeto de más de unos 4 KB: la comprobación previa abortaría (sin coste, pero
   bloquearía Ahold).

### Alternativas

- **`strict: true` en una herramienta:** compila la misma gramática; el propio mensaje de
  error menciona las herramientas estrictas. Previsiblemente el mismo 400. No recomendada.
- **Herramienta no estricta (`tool_choice: auto`):** la API devuelve `input` ya analizado
  como JSON, lo que eliminaría los fallos de sintaxis, pero Opus 5.5 rechaza `tool_choice`
  forzado (400), el modelo podría contestar en texto, y el transporte actual de AUTO1 corta
  con `STREAM_BLOQUE_INESPERADO` ante un bloque `tool_use`. Supone cambiar código de
  transporte probado. No recomendada para esta llamada.
- **Simplificar el esquema y mantener la gramática:** p. ej. `escenarios` y
  `sensibilidad_tasa` como listas de un solo tipo de objeto (con un campo `escenario`/`tasa`
  en enumeración) en lugar de 3 + 5 objetos repetidos; quitar campos derivables que ya
  recalculan las comprobaciones mecánicas. No se puede saber sin probar si compila: el
  `count_tokens` no compila la gramática (la ejecución fallida pasó el conteo).

### Recomendación para gastar unos 4,5 USD de reserva

La opción más segura es **una sonda de compilación** antes de la llamada cara: una llamada
mínima a `claude-opus-5-5`, mismo `thinking`/`effort`/`output_config.format` con el esquema
simplificado, mensaje de usuario trivial y `max_tokens` pequeño. Un 400 de compilación
no consume inferencia; si compila, cuesta céntimos. Si compila, mantener la gramática
(forma garantizada) y adaptar `render`/`mechanical_checks` con pruebas. Esto es un gasto
nuevo con la API: requiere autorización de la persona responsable y su registro.

Si no se autoriza la sonda, el cambio revisado es aceptable para la llamada **tras aplicar
1, 2 y 4** (y opcionalmente 3).

## 3. Extracción tolerante

- **No puede tomar un bloque de pensamiento:** el transporte SSE descarta los bloques
  `thinking`/`redacted_thinking` (no entran en `content`), y `validate` solo concatena
  bloques `text`.
- **No puede aceptar otro objeto citado:** el tramo del primer `{` al último `}` solo se
  acepta si es un único JSON válido que además pasa `check_schema` completo (todas las
  claves exactas, tipos y enumeraciones). Un objeto ajeno no lo pasa; uno citado junto a la
  respuesta hace fallar el análisis (`JSON_INVALIDO`). El único caso aceptado es un objeto
  conforme rodeado de texto, que queda anotado y la salida completa sigue en
  `raw_model_output`.
- **No conviene exigir texto corto ni ausencia de otro `{`:** solo añadiría rechazos de
  respuestas pagadas sin ganar seguridad, porque la seguridad la da `check_schema`. Mejora
  opcional: buscar candidatos con `json.JSONDecoder().raw_decode` en cada `{` y aceptar
  **solo si exactamente uno** pasa el esquema; si pasan dos (borrador y final), rechazar
  por ambigüedad y dejarlo para la revisión humana.
- Menor: la nota `texto_fuera_del_objeto_json_descartado` se guarda dentro de
  `normalizaciones_enum` (lista de diccionarios de enumeraciones) como cadena. Funciona
  (`render` lo vuelca en JSON), pero mejor en un campo propio (`extraccion_json`).

## 4. Coherencia del encargo y huellas

- **Coherente.** El encargo verificado (sin cambios en este diff; su SHA coincide con el
  `encargo_sha256` publicado de Ahold) ya dice «solo con el objeto JSON del esquema
  suministrado», números con punto, `0` en cifras no disponibles y enumeraciones en
  minúsculas. El bloque añadido no lo contradice.
- **Integridad cubierta:** el esquema y el texto añadido viven en `direct_analysis.py`, que
  está en `CODE_PATHS` y `verify_code` compara byte a byte con el SHA observado. Lo enviado
  es una función determinista de archivos verificados.
- **Hueco de trazabilidad (menor):** `encargo_sha256` (y con él `package_sha256`) solo
  cubre el archivo del encargo, no el `system` que se envía (encargo + esquema). Dos
  ejecuciones, una con gramática y otra sin ella, comparten `package_sha256` aunque las
  instrucciones difieren; el README usa esa huella para la repetibilidad. Recomendado:
  registrar `system_sha256` del sistema enviado en `report.json`/`report.md`.

## 5. Pruebas, como CI

Ejecutadas en el worktree, HEAD `08fa48f`:

| Orden | Resultado |
|---|---|
| `python3 -I -m unittest discover -s automation/claude_review -p 'test_*.py'` | 49 pruebas, OK |
| `python3 -I -m unittest discover -s automation/coordination -p 'test_*.py'` | 97 pruebas, OK |
| `python3 -I -m unittest discover -s automation/direct_analysis -p 'test_*.py'` | 41 pruebas, OK |

Huecos en las pruebas (menores):

- `test_preflight_counts_schema_in_system` no comprueba lo que dice su nombre: solo verifica
  que falta `format`. Debería afirmar que `payload_bytes` de `preflight` y
  `reserved_input_tokens` incluyen el esquema dentro de `system`.
- `test_success_one_call_payload_record_and_restored_config` no incluye `cr.payload` en la
  tupla de restauración (lo restaurado se comprobó aquí a mano).
- Sin pruebas de clave duplicada, `null` en cifra no disponible ni texto previo con `{`.

## Hallazgos

| # | Gravedad | Hallazgo |
|---|---|---|
| H1 | Media | Sin gramática, un fallo de forma (comilla sin escapar en `cita`, `null`, clave extra, número como texto) se paga y no se acepta. No hay vía de rescate sin llamada. Mitigación: sección 2, puntos 1–4, o la sonda de compilación autorizada. |
| H2 | Baja | Claves duplicadas aceptadas en silencio (gana la última). |
| H3 | Baja | `system_sha256` no registrado: `encargo_sha256`/`package_sha256` no cubren el sistema enviado (la integridad sí la cubre `code_sha`). |
| H4 | Baja | README desactualizado: «Límites conocidos» sigue describiendo el riesgo de compilación del esquema y no explica el modo sin gramática ni el 400 de 44288081039. |
| H5 | Baja | Prueba con nombre engañoso y restauración de `cr.payload` no cubierta por la prueba existente. |
| H6 | Informativa | La nota de extracción se mezcla con `normalizaciones_enum`. |
| H7 | Informativa | Margen de Ahold: 5 061 tokens de cota hasta el contexto; cualquier ampliación del sistema de más de unos 5 KB aborta la comprobación previa (sin coste). |
| H8 | Informativa | Sin cambio en el riesgo de agotar `MAX_OUTPUT` (32 768) con pensamiento a esfuerzo alto sobre unos 389 k tokens. |

## Respuesta del autor (coordinador) · 3300424
- H1 (riesgo de pagar y perder): reglas de forma explícitas en el encargo (sin claves de más ni repetidas, sin null, números sin comillas, comillas y saltos escapados, citas acortables con «…»); `null` → 0 solo en cifras de objetos con `disponible` = false, anotado en `normalizaciones_enum`; `raw_model_output` se conserva para revisión fuera de línea con decisión humana (README).
- H2: claves duplicadas rechazadas (`JSON_INVALIDO`).
- H3: `system_sha256` registrado en el preflight y el informe.
- H4: README «Límites conocidos» actualizado.
- H5: prueba renombrada y ampliada (cota ≥ sistema, `cr.payload` restaurado, huella del paquete); pruebas nuevas de duplicadas y de null.
- No se adopta la sonda de esquema simplificado: cambia salida, validación y presentación, y requiere su propia revisión; queda como alternativa si la tasa de rechazo por forma resulta material.
- CI local: 49 + 97 + 43 OK. Prueba en seco de Ahold: cota 962 631 tokens, reserva 4,505884 USD (< 5).
