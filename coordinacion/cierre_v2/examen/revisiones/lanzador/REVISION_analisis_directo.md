# Revisión independiente · lanzador de análisis directo

- **Material revisado:** rama `automatizacion/analisis-directo` @ `60c47fac1aff6392d30e35ad59cb7a4df9fde78e`, diff contra `main` @ `422a6f3` (6 archivos, +1330/−1). También el código de AUTO1 que reutiliza (`critical_review.py`, `pilot.py`, sin cambios en este diff).
- **Revisor:** agente distinto del autor. Revisión de código y pruebas en una copia (`/tmp/claude-0/revision_lanzador/repo`). **Ninguna llamada a la API de Anthropic.** Sí se consultaron dos páginas públicas de documentación (precios y salidas estructuradas), además de la skill `claude-api` (tabla en caché del 3-nov-2026).
- **Fecha:** 17-nov-2026.

## Veredicto: CORRECCIONES

El control de gasto es sólido: no he encontrado ningún camino a una segunda llamada, y la reserva queda por encima del coste máximo posible. Las correcciones son para que la **comparación** de la §10 sea válida y para no perder una llamada pagada:

1. el encargo define el precio de Sí **sin el tope del escenario normal** que usa el personaje (Anexo C). La comparación del precio de Sí y de la trampa de Zoetis queda sesgada;
2. dos riesgos documentados por la API pueden hacer que se pierda la única llamada pagada: el `enum` «Demasiado difícil» puede volver con otra capitalización, y los campos que piden «razonamiento» pueden provocar un rechazo `reasoning_extraction`;
3. la ceguera solo se apoya en nombres y en tres marcas de contenido. Deja pasar `universo/`, prompts y material de auditoría del personaje que ya están en el repositorio, y copias limpiadas de la rúbrica y de la lectura del informe crítico.

El cambio en la prueba de AUTO1 (de 6 a 7) es legítimo.

---

## Hallazgos

### H1 · Alta · El precio de Sí del encargo no es el del personaje: falta el tope V_NORMAL

**Evidencia.**
- `ENCARGO_ANALISIS_DIRECTO.md` §7: «precio de Sí = el mayor P con G(P) ≥ 3 · L(P) … Siempre queda entre el valor del escenario malo y el del bueno».
- `personaje_v2/ANEXO_C_precio_de_si.md` (en `wt_f1docs/munger_v2_r1`), regla 2: «**Precio de Sí** = mín(P\*, V_NORMAL)». Casos 2 y 5 del anexo: «**100** (tope NORMAL)» y «**70** (tope NORMAL)».
- `FRENTE_C_MATEMATICA.md` (cierre-v2): «salida de precio de Sí según el contrato que añade el límite del escenario normal».
- `precio_si_k3` tampoco aplica el tope. Prueba en la copia con el caso 2 del Anexo C (V = 90/100/160, p = 0,2/0,6/0,2): una respuesta correcta según el anexo (100) produce el aviso «El precio de Sí declarado difiere más de un 1 % del recalculado» (recalculado: 102,31).

**Efecto.** Cuando el escenario bueno está muy por encima, el análisis directo da por definición un precio de Sí más alto que el personaje. Eso hace más probable un «Sí» y sesga dos medidas de la §10 contra el análisis directo: el precio de Sí y la trampa de Zoetis. Además, el aviso mecánico castiga la respuesta correcta.

**Corrección.**
- En el encargo: «precio de Sí = mín(P\*, V_normal); nunca por encima del valor del escenario normal», y que los valores estén ordenados malo ≤ normal ≤ bueno (Anexo C, regla 0).
- En `precio_si_k3` o `mechanical_checks`: aplicar el mismo tope y avisar si los valores no están ordenados.
- Una prueba con los cinco casos del Anexo C.

### H2 · Media · Riesgo de perder la única llamada pagada: `enum` con espacio y campos de «razonamiento»

**Evidencia** (página oficial de salidas estructuradas, consultada hoy):
- «Structured outputs don't guarantee the capitalization of string `enum` … typically in the first letter of a word following a space». `CUBOS` incluye `'Demasiado difícil'`, el único valor con espacio. `check_schema` compara de forma estricta. En la copia, `check_schema('Demasiado Difícil', …)` devuelve `ESQUEMA_INVALIDO:$`. El resultado se paga, queda `RESULTADO_NO_ACEPTADO_NO_REINTENTAR` y no se repite.
- «A property that asks for the model's thinking or step-by-step reasoning might lead to a `reasoning_extraction` refusal. Ask for a short explanation instead.» El esquema tiene `razonamiento` (×3), `calculo` y `conclusion_razonada`. El encargo pide «su razonamiento: supuestos, cifras … y cómo llegas al valor». La skill confirma que Opus 5.5 tiene el clasificador `reasoning_extraction`. Un rechazo se factura y sin reintento se pierde la comparación.

**Corrección.**
- Normalizar los `enum` sin distinguir mayúsculas antes de validar, y guardar el valor canónico; o usar valores sin espacio (`demasiado_dificil`) y traducirlos al presentar.
- Renombrar los campos (`supuestos_y_cifras`, `justificacion_breve`, `formula_aplicada`) y pedir en el encargo «una explicación breve de supuestos y cifras», no el razonamiento paso a paso.

### H3 · Media · Ceguera: lo que se puede colar

Probado con `check_path` y `load_package` sobre commits de la copia, de `main` y de `coordinacion/cierre-v2` (6920b09). Scripts en `/tmp/claude-0/revision_lanzador/scripts/`.

**Lo que se bloquea:**

| Intento | Resultado |
|---|---|
| Rúbrica original bajo `examen/`; `EXAMEN/`, `Exámen/` | `RUTA_PROHIBIDA_EN_EL_PAQUETE` |
| `datos/p/RUBRICA.md`, `Rúbrica.md` | `RUTA_PROHIBIDA_EN_EL_PAQUETE` |
| Copia completa de la rúbrica renombrada `datos/p/notas.md` | `CONTENIDO_PROHIBIDO_EN_EL_PAQUETE` |
| Enlace simbólico a la rúbrica | `NO_ES_ARCHIVO_REGULAR` |
| `..`, `./`, ruta absoluta, `//` | `RUTA_INVALIDA` |
| Ruta con otras mayúsculas que la de git | `ARCHIVO_NO_ENCONTRADO` |
| `LECTURA_INFORME.md`, `SHA256SUMS` y PDF del informe crítico en `universo/` | rechazados por el nombre o por el contenido |

**Lo que pasa** (resultado literal `ACEPTADO`):

| Intento | Bytes aceptados |
|---|---|
| Rúbrica sin las 13 líneas que contienen las marcas (534 de 547 líneas) | 37 646 |
| `LECTURA_INFORME.md` (lectura del informe crítico) sin 5 líneas | 134 287 |
| La misma lectura con «informe  crítico» (doble espacio) y «rú​brica» (carácter de anchura cero) | 135 895 |

- **Rutas que pasa `check_path`:**
  - **cualquier archivo nuevo bajo `universo/`**: `coordinacion/cierre_v2/universo/notas.md`. `universo` no está en `FORBIDDEN_SEGMENTS`, aunque el encargo de revisión lo exige;
  - salidas de fase con otro nombre: `fase-a.json`, `fase_A1.json`, `copia.fase_b.json` (la raíz se corta en el primer punto), `phase_c.json`;
  - `mi_ficha.json`, `copia_auditoria.md`, `audit.md`, `objetivo.json`, `escalera.json`.
- **Salidas y prompts reales del personaje que ya están en `cierre-v2` y se aceptan enteros:**
  - `traspaso/resultado_20261117/registro/relevo_copia_base/13_verificacion.md`, 18 330 bytes. Es el prompt del paso 13 del personaje («Salida esperada: auditoria.md»);
  - `material_auditoria.json` (manifiesto de `fase_a/b/c`);
  - `solicitud_auditoria.json`.
  - En total, 181 de 961 rutas del repositorio pasan el filtro de nombre, entre ellas 56 de `traspaso/resultado_20261117/`.
- **Fuera del filtro:** `descripcion` y `caso` del manifiesto se envían al modelo sin control de contenido. El paquete incluye `repository: jluisplagos/munger-v2-evidencias-mistral`, que nombra a «Munger».

**Lo que está bien.** El README reconoce el límite: «La lista de rutas prohibidas es por nombre y por unas pocas marcas de contenido». El riesgo es un descuido de quien escribe el manifiesto, no un ataque. Pero el propio README manda copiar `LISTA_ENTRADAS.csv` fuera de `examen/`, así que la vía de la copia es el uso normal.

**Corrección** (por orden de valor):
1. **Lista de huellas prohibidas:** sha256 de todos los blobs bajo `examen/`, `universo/`, `traspaso/`, `relevo_*`, `pruebas_candidata/` y las carpetas de expedientes del personaje, tanto en el commit del código como en cada `commit` declarado. Rechazar cualquier fuente con la misma huella, salvo una lista explícita y versionada de entradas permitidas (`LISTA_ENTRADAS.csv`).
2. **Detección de solapamiento:** rechazar una fuente que contenga cualquier fragmento literal de unos 200 caracteres de la rúbrica, de `LECTURA_INFORME.md` o de `CONTRADICTOR.md`. Así se detectan las copias limpiadas.
3. **Rutas:** añadir `universo`, `traspaso`, `relevo`, `pruebas_candidata` a los segmentos prohibidos, y `fase`, `auditoria`, `verificacion` como subcadenas. Mejor aún, una **lista blanca** de raíz (p. ej. `datos_analisis_directo/<empresa>/`).
4. **Marcas de contenido:** comparar tras quitar espacios y caracteres de formato (`​`, etc.) y añadir variantes («informe-critico»).
5. **Lo que se envía:** quitar `repository` del contenido enviado al modelo (puede quedar en el registro) y limitar `descripcion` a texto revisado.

### H4 · Media-baja · El encargo pide menos que la rúbrica en la escalera y la sensibilidad

**Evidencia.**
- Rúbrica §0: «Escalera de precios (Anexo C, k = 3): precio del escenario malo, precio de Sí y valor ponderado», «Zona del precio» y «la hoja resumen tiene que mostrar el precio de Sí y la zona al 7, 8, 9, 10 y 11 %, y el crecimiento que exige el precio actual».
- El encargo y el esquema piden por tasa solo `precio_si` y `precio_actual_por_debajo`. No piden el ponderado, la zona, el precio del escenario malo ni el crecimiento implícito.
- Lo que se compara en la §10 sí se pide: estado, cubo, acción, tres escenarios, precio de Sí con k = 3, sensibilidad, qué la haría falsa y lo que no se sabe. No he encontrado pistas de las respuestas del examen: nada sobre la trampa de Zoetis, el retorno del 27 %, el doble cómputo de Ahold ni las preguntas K6. Las definiciones de estado, cubo y acción son las genéricas del Anexo D.

**Corrección.**
- Añadir `ponderado`, `zona` (`bajo_malo`, `cumple_regla_k`, `vigilar`, `caro`) y `crecimiento_implicito` como campos neutros del contrato de salida. Cada nuevo `anyOf` cuenta contra el límite (ver H5): usar números obligatorios con un campo `disponible` en lugar de `null`.
- Decidir y registrar qué reglas de salida del personaje se dan también al análisis directo (una sola tasa, sin tamaños de posición —D16—, sin apoyarse en la etapa 1). Si no se dan, la revisión a ciegas no debería contar como error económico lo que el análisis directo no podía saber.

### H5 · Baja · Esquema aceptable para la API, pero al borde de un límite

**Evidencia** (página oficial):
- `anyOf`, `null` y `enum` de cadenas están admitidos. `additionalProperties: false` y `required` completos, como exige la API. Sin restricciones numéricas ni de longitud.
- Límite explícito: «Parameters with union types · 16». El esquema tiene **15** `anyOf` y 0 opcionales (límite 24), contados por script.
- «Token counting: Count tokens without compilation». Por tanto, un 400 por complejidad («Schema is too complex for compilation») no aparecería en `count_tokens`, sino en la llamada de pago. El código lo trata como `INFERENCIA_SIN_VEREDICTO_COSTE_INCIERTO` y cuenta la reserva completa hasta reconciliarla. No hay segunda llamada.

**Corrección.** No añadir más `anyOf` (ver H4). Si se puede, sustituir los 10 de la sensibilidad por valores obligatorios con un indicador. Tras la primera ejecución real, conciliar en Console si hubo un 400.

### H6 · Baja · Prueba de tiempo de AUTO1 no cubre el nuevo workflow; inventario por número

- `test_m5_review_job_timeout_leaves_room_for_publication` solo mira `claude-critical-review.yml` y `qwen-bank-mistral-groups.yml`. El nuevo job tiene `timeout-minutes: 20`, pero ninguna prueba de AUTO1 lo fija.
- **Corrección:** incluir `analisis-directo.yml` en esa prueba y fijar por nombre el conjunto (workflow, job) de jobs con secretos, en lugar de solo el número (ver punto 5).

### Límites declarados (no bloquean)

- **L1.** El tope acumulado no es atómico entre workflows distintos. La concurrencia `munger-analisis-directo` no excluye a `claude-critical-review` ni a `qwen…/claude`. El README lo declara.
- **L2.** La puerta humana es la única defensa contra lanzar desde una rama con código modificado. `verify_code` solo prueba que el código local es el del SHA, no que el SHA esté revisado. Quien aprueba debe comprobar el `code_sha` que muestra `preparar`.
- **L3.** No se puede impedir que el modelo use su memoria posterior al corte (9-oct en Zoetis T1). Lo prohíbe el encargo, y las citas literales ayudan a detectarlo.
- **L4.** Con más de 1000 tareas en `automation/coordination/reviews`, la API de contenidos de GitHub trunca el listado y el tope acumulado se quedaría corto. Queda lejos.

---

## Comprobaciones pedidas

### 1. Gasto — conforme

- **Una sola llamada de pago.** `cr.run` hace como máximo un `POST /v1/messages`. Antes van `GET /v1/models/<modelo>` y `count_tokens`, que no se facturan.
- **Sin segunda llamada.** No hay bucles de reintento: los únicos bucles son la bisección local y la lectura SSE. El transporte es `urllib` con `NoRedirect`. El stream se abre una vez y no se reabre (prueba `test_real_sse_transport_cut_opens_once`).
- **Sin modelo de reserva.** No se envía `fallbacks` ni cabeceras beta. `check_anthropic_body` liga el cuerpo al modelo de `DirectHTTP` y prohíbe `tools`, `tool_choice`, `mcp_servers` y `container`. Un `refusal` queda `RESULTADO_NO_ACEPTADO` con coste conocido.
- **Orden de los controles antes de llamar:**
  1. `preflight` por bytes: contexto y máximo de la ejecución;
  2. `receipt.prior()`: un «Re-run» de la misma ejecución queda en `YA_RESERVADO`;
  3. `admit(MAX_USD)`: tope acumulado;
  4. `count_tokens`;
  5. `budget`: contexto y reserva ≤ máximo;
  6. `reserve()`: repite `admit` con la reserva exacta y hace el PUT create-only;
  7. la llamada.
- **Coste incierto bloquea.** `check_usage` marca `INCIERTO_SIN_COTA` si el uso supera lo reservado, si el modelo devuelto es otro, si hay caché o si la facturación no es la prevista. `exposure()` lanza `REGISTRO_CON_COSTE_SIN_COTA_RECONCILIAR` y bloquea toda reserva nueva.
- **Secretos.** `tests` y `preparar` no tienen secretos (inventario por script: `[]`). Solo `analisis` tiene `ANTHROPIC_API_KEY` y `GITHUB_TOKEN`, con `environment: inferencia-aprobada` y solo `workflow_dispatch`. Las entradas pasan por `env` y nunca se interpolan en el shell. `persist-credentials: false`.

### 2. Precios y modelo — conforme

- **Modelo.** `claude-opus-5-5` es el ID correcto, sin fecha.
- **Tarifas.** La página oficial de precios dice Opus 5.5 «$4 / MTok … $20 / MTok», Fable 5.2 $8/$40 y Sonnet 5.5 $2/$10, igual que la skill.
- **Sin recargo por contexto largo:** «Claude 4.6 and later models (except Claude Haiku 5.5) include the full 1M token context window at standard pricing».
- **`inference_geo`.** `"global"` es el valor por defecto y no lleva multiplicador; `"us"` multiplica por 1,1, pero el código no lo envía y `check_usage` marca cualquier otro valor como no previsto.
- **Salida.** Máximo del modelo: 128K. `MAX_OUTPUT = 32 768` es correcto y cubre pensamiento más respuesta, que se facturan como salida.
- **Pensamiento.** `thinking: adaptive` más `effort` explícito es lo correcto en Opus 5.5: no admite `disabled` ni `budget_tokens`, y su esfuerzo por defecto es `medium`.
- **Reserva frente a coste real máximo.** `entrada_reservada × 4 + 32 768 × 20`, con `entrada_reservada = máx(conteo, bytes de la carga) + 4096`. Como la API corta la salida en `max_tokens` y `check_usage` exige entrada ≤ reservada, **la reserva es mayor o igual que el coste máximo posible** con tarifa estándar, sin caché y con `global`. Ejemplo del README: 300 KB dan 1,87 USD de reserva, y la cuenta es correcta.
- **Esquema.** Aceptable para la API, con las salvedades de H2 y H5.

### 3. Ceguera — corrección necesaria

- Ver H3. El encargo sí fija la fecha de corte («Para ti no existe nada posterior a `fecha_corte`»), prohíbe la memoria (regla 1) y trata los textos como datos.
- La fecha la declara el manifiesto. Para Zoetis T1 tiene que ser 2026-10-09, y el código no lo comprueba.

### 4. Encargo — corrección necesaria

- Pide todo lo que mide la §10, sin pistas de las respuestas.
- La regla k = 3 está mal definida respecto al Anexo C (H1).
- Faltan escalera y zona (H4).
- La formulación de «razonamiento» tiene riesgo de rechazo (H2).

### 5. Cambio en la prueba de AUTO1 (6 → 7) — legítimo, no debilita la puerta

- El inventario real tiene 7 jobs con secretos de inferencia:
  - `analisis-directo/analisis` (nuevo);
  - `claude-critical-review/review`;
  - `piloto-claude-api/pilot`;
  - `qwen-groups/mistral` y `qwen-groups/claude`;
  - `qwen-review/review`;
  - `vibe-auth/connection`.
- Las aserciones que importan (solo `workflow_dispatch` y environment `inferencia-aprobada`) se siguen aplicando a cada job, y el nuevo las cumple. La m7 (sin instalaciones, sin mezclar con Mistral) también lo cubre.
- Mejora propuesta en H6: fijar el conjunto por nombre.

### 6. Pruebas (copia en `/tmp/claude-0/revision_lanzador/repo` @ 60c47fa, Python 3.13.18, PyYAML disponible)

```
=== automation/claude_review     Ran 49 tests in 0.048s   OK
=== automation/coordination      Ran 95 tests in 0.614s   OK
=== automation/direct_analysis   Ran 29 tests in 1.829s   OK
```

Total: 173 pruebas, todas OK, ninguna omitida. `test_auto1_workflows`: 7 de 7 OK. Mandato: `python3 -I -m unittest discover -s <dir> -p 'test_*.py'`.

Las pruebas no cubren H1, H2 ni H3, que se demostraron con los scripts de `/tmp/claude-0/revision_lanzador/scripts/` (`probe_paths.py`, `probe_tree.py`, `probe_load.py`).

---

## Segunda ronda · 50a5071 (diff 60c47fa..50a5071)

- **Alcance:** solo lo que toca la corrección. El diff no cambia `critical_review.py`, `pilot.py` ni el workflow.
- **Copia:** `/tmp/claude-0/revision_lanzador/repo2`, con commits de prueba solo en la copia. Sin llamadas a la API.
- **Scripts:** en `/tmp/claude-0/revision_lanzador/scripts/` (`r2_escalera.py`, `r2_probe_load.py`, `r2_e2e.py`).

### Veredicto: CONFORME CON LÍMITES

H1–H6 están corregidos. Quedan dos defectos pequeños, que conviene corregir antes de la primera ejecución de pago o declarar como límites:

- R2-1: una comprobación «informativa» que puede tumbar el resultado pagado;
- R2-2: el README afirma que la etapa 1 no entra, pero el código no lo impide.

### Comprobaciones pedidas

**1. El precio de Sí reproduce el Anexo C: conforme.**

`escalera()` aplicada a los cinco casos de §C.5 del `ANEXO_C_precio_de_si.md` (sha256 `36497345…`):

| Caso | V | p | P\* | Precio de Sí | Ponderado | Precio esc. malo | Resultado |
|---|---|---|---|---|---|---|---|
| 1 | 60/100/150 | 0,25/0,5/0,25 | 88,3333 | 88,3333 | 102,5 | 60 | COINCIDE |
| 2 | 90/100/160 | 0,2/0,6/0,2 | 102,3077 | **100** (tope) | 110 | 90 | COINCIDE |
| 3 | 100/100/100 | 0,2/0,6/0,2 | 100 | 100 | 100 | 100 | COINCIDE |
| 4 | −20/80/200 | 0,2/0,6/0,2 | 54,2857 | 54,2857 | 84 | sin precio | COINCIDE |
| 5 | 40/70/300 | 0,3/0,5/0,2 | 77,3077 | **70** (tope) | 107 | 40 | COINCIDE |

- **Contraste independiente:** bisección directa de G − 3L en 200 000 casos aleatorios. Error relativo máximo de P\*: 3·10⁻⁹.
- **Encargo:** define «Precio de Sí = mín(P*, V_normal)», exige el orden malo ≤ normal ≤ bueno y define la zona como en §C.4.4.

**2. La normalización de enumeraciones no convierte una respuesta inválida en válida: conforme.**

- **Qué se normaliza:** solo campos con `enum`. Se quitan tildes, mayúsculas y espacios de los extremos, y los espacios o guiones internos pasan a `_`. Las claves canónicas son únicas en las cuatro enumeraciones.
- **Se aceptan** (registradas en `normalizaciones_enum`): `Sí`, `SI`, `Demasiado Difícil`, `demasiado-difícil`, `DEMASIADO  DIFICIL`, `Si\n`, `ｓｉ`. Son variantes de escritura.
- **Se rechazan:** `sí, comprar`, `yes`, `Vigilar.`, `n o`, `-no`, `Comprar` (en `cubo`), `vigilar` + anchura cero, `''`, `1`, `None`, `True`. Las claves de más siguen rechazadas por `check_schema`.
- **De punta a punta, con la API simulada:**
  - `cubo='comprar ya'` da `RESULTADO_NO_ACEPTADO_NO_REINTENTAR · ESQUEMA_INVALIDO:$.cubo`;
  - `Demasiado Difícil` da `AUDITORIA_DOCUMENTAL_PENDIENTE_ACEPTACION` con las tres normalizaciones registradas;
  - en ambos casos, una sola llamada.

**3. Lista blanca de H3: conforme para todo lo de la primera ronda, con dos límites (R2-2 y R2-3).**

Todos los casos de la primera ronda quedan rechazados:

| Intento | Resultado |
|---|---|
| Rúbrica completa renombrada | `COPIA_DE_MATERIAL_CIEGO:…/RUBRICA_EXAMEN.md` |
| Rúbrica sin las 13 líneas con marcas | `SOLAPE_CON_MATERIAL_CIEGO:…/RUBRICA_EXAMEN.md` |
| Lectura del informe crítico sin 5 líneas | `SOLAPE_CON_MATERIAL_CIEGO` |
| Lectura con doble espacio y anchura cero | `CONTENIDO_PROHIBIDO_EN_EL_PAQUETE` |
| Archivo nuevo bajo `universo/`; ruta original del prompt del paso 13; `material_auditoria.json`; rúbrica original | `RUTA_FUERA_DE_LOS_DATOS_DECLARADOS` |
| `fase-a.json`, `copia.fase_b.json` | `RUTA_PROHIBIDA_EN_EL_PAQUETE` |
| Enlace simbólico | `NO_ES_ARCHIVO_REGULAR` |
| Prompt del paso 13 copiado a `fuentes/paso13.md` | `COPIA_DE_MATERIAL_CIEGO:…/13_verificacion.md` |

Intentos nuevos:

| Intento | Resultado |
|---|---|
| Rúbrica con el nombre fijo admitido `extracto_v63.md` | `COPIA_DE_MATERIAL_CIEGO` |
| `LISTA_ENTRADAS.csv` fuera de `registro_entradas/` | `COPIA_DE_MATERIAL_CIEGO` |
| `Datos_analisis_directo/…` y datos de otra empresa | `RUTA_FUERA_DE_LOS_DATOS_DECLARADOS` |
| Rúbrica con una letra cada 150 caracteres (marcas aún reconocibles) | `CONTENIDO_PROHIBIDO_EN_EL_PAQUETE` |
| **Rúbrica con una letra cada 150 caracteres y todas las marcas rotas** | **ACEPTADO** (40 901 bytes) → R2-3 |
| **Paráfrasis escrita a mano de lo que se espera** | **ACEPTADO** (215 bytes) → R2-3 |
| **Respuesta de etapa 1 de Zoetis renombrada** (`fuentes_usuario/zoetis_etapa1/Zoetis_respuesta.md`) | **ACEPTADO** (28 521 bytes) → R2-2 |
| **Respuesta de etapa 1 de Ahold renombrada** | **ACEPTADO** (49 066 bytes) → R2-2 |

**No rechaza datos legítimos.** Paquete de prueba con:
- `datos_v63.md`, `extracto_v63.md` y `fase1_v63.json` reales (expediente Nike);
- texto de `AD_annual-report-2025.pdf` (40 páginas) y de `AD_q3-2026-interim-report.pdf`;
- `DESCARGAS_2026.tsv`;
- copia de `LISTA_ENTRADAS.csv`;
- plantilla `verificacion_entradas` y una versión rellena.

Los 9 archivos se aceptan uno a uno y juntos (635 410 bytes, 0,9 s), sin falsos solapes.

**4. Esquema sin `anyOf`: conforme.**

- 0 uniones (límite 16), 0 opcionales (límite 24), 9 enumeraciones ASCII en minúsculas y sin espacios, 79 propiedades.
- Todos los objetos llevan `additionalProperties: false` y `required` completo.
- No usa `minimum`, `maxLength`, `pattern`, `format` ni `$ref`.
- Ni el esquema ni el encargo contienen «razonamiento», «reasoning» ni «paso a paso».
- No se puede descartar sin la API un 400 «Schema is too complex» por los límites internos. Se registraría como coste incierto sin segunda llamada (README).

**5. Ninguna segunda llamada pagada: conforme.**

- El transporte, la reserva y el registro no cambian.
- Lo nuevo es anterior a la llamada (ruta, huellas, solape) o posterior (validación, avisos, presentación).
- Las excepciones posteriores caen en el `except` de `cr.run` y el estado queda sin reintento. En la simulación siempre hubo una sola llamada a `/v1/messages`, y el «Re-run» acabó en `YA_RESERVADO_SIN_NUEVA_LLAMADA` con 0 llamadas a Anthropic.
- La prueba de AUTO1 fija ahora por nombre los 7 jobs con secretos e incluye `analisis-directo.yml` en la prueba de tiempos. Es más estricta que antes.

**Pruebas** (copia @ 50a5071, Python 3.13.18):

```
automation/claude_review     Ran 49 tests   OK
automation/coordination      Ran 95 tests   OK
automation/direct_analysis   Ran 35 tests   OK
```

Total 179, todas OK.

### Hallazgos de la segunda ronda

**R2-1 · Media · Una comprobación «informativa» puede tumbar la llamada pagada.**

- **Dónde:** `escalera()` acepta P solo si cae en el tramo con tolerancia **absoluta** 1e-12.
- **Cuándo falla:** con los tres valores iguales y cifras grandes, el redondeo deja P fuera de los dos tramos y `p_star` queda en `None`. `min(None, …)` lanza `TypeError`.
- **Frecuencia:** 91 de 200 000 casos aleatorios fallan, todos con tres valores iguales. Ninguno falla entre 0,01 y 1000 por acción, pero sí con 25 454,65 o 86 562,86 (acciones de precio alto, como Lindt o NVR).
- **Simulación de punta a punta:** con V = 86 562,86 ×3 y una respuesta válida, el estado final es `RESULTADO_NO_ACEPTADO_NO_REINTENTAR · ERROR_INESPERADO_NO_REINTENTAR_TypeError`. Eso contradice «Las comprobaciones mecánicas … No aceptan ni rechazan».
- **Coste:** no hay segunda llamada, pero el análisis pagado queda no aceptado.
- **Corrección:**
  - tolerancia relativa, p. ej. `1e-9·máx(1, |V|)`;
  - si ningún tramo admite P, tomar `V₍₁₎` cuando los tres valores coinciden, o hacer bisección;
  - envolver `mechanical_checks` para que un fallo suyo sea un aviso, nunca una excepción;
  - añadir una prueba con tres valores iguales grandes.

**R2-2 · Media-baja · «La etapa 1 no entra en el paquete» no se hace cumplir.**

- **Qué dice el README:** que la etapa 1 no entra, como decisión registrada.
- **Qué pasa:** las respuestas de etapa 1 (`fuentes_usuario/*_etapa1/*_respuesta.md`, en las ramas `fuentes/…`) no están entre las carpetas ciegas. Renombradas, pasan los cuatro filtros.
- **Por qué importa:** `LECTURA_INFORME.md` dice que la respuesta de etapa 1 de Ahold «reproduce exactamente las cifras del informe». Colarla equivale a filtrar el informe crítico (rúbrica, regla 1 de contaminación).
- **Corrección:** añadir `fuentes_usuario` (o los `*_respuesta.md` y `*_evaluada.xlsx`) al material ciego de huellas y solape, o corregir el README. La decisión es de la persona responsable.

**R2-3 · Límite declarado · El solape no resiste una alteración deliberada.**

- **Cómo funciona:** los fragmentos de 200 caracteres se toman sin solapar. Hace falta copiar 400 seguidos para detectarlo.
- **Qué lo burla:** una letra insertada cada 150 caracteres alfanuméricos y las marcas rotas. Una paráfrasis también pasa.
- **Por qué no bloquea:** el riesgo que se cubre es el descuido, no el engaño. El README ya dice que elegir los archivos es responsabilidad de quien hace el manifiesto.
- **Otros límites:**
  - solo se miran las puntas de las ramas, no versiones antiguas del historial;
  - la marca `rubrica` (texto sin espacios) daría falsos positivos en fuentes en español («bajo la rúbrica…»), aunque no en Ahold ni en Zoetis.
