# Revisión independiente · salida máxima elegible del análisis directo

**Veredicto: CONFORME CON CORRECCIONES.**

Rama `automatizacion/analisis-directo-salida-64k`, commits `5a1ae21` y `3dfedb7` sobre
`origin/main` `fcb18bb`. Revisor: un agente distinto del autor del cambio (20-nov-2026).
No he hecho commits en la rama revisada. Las mutaciones se hicieron en un clon aparte, en
el scratchpad.

El código hace lo que dice. Con la opción por defecto el comportamiento es idéntico al de
`main`, salvo campos informativos. Con 65 536 todos los sitios usan 65 536 y 1500 s.
`configured` restaura siempre. La entrada se valida con una lista cerrada. El timeout del
job cubre el peor caso. Las cifras del README que he comprobado son correctas. Las
correcciones son una afirmación falsa en el comentario del código y en el README, y un
hueco de pruebas en el camino real del workflow.

## Correcciones necesarias (lista exacta)

1. **La causa citada es falsa: el esfuerzo era `high`, no `max`.**
   - Dónde: `automation/direct_analysis/direct_analysis.py:44` («con esfuerzo `max` un
     análisis de Vinci agotó la salida») y `automation/direct_analysis/README.md:331` (lo
     mismo). El mensaje del commit `5a1ae21` dice lo mismo.
   - Evidencia: en la rama de registro, el informe
     `automation/coordination/reviews/analisis-directo-vinci-44554333055/report.json` tiene
     `effort_requested: "high"`, `stop_reason: "max_tokens"`, `output_tokens: 32768` y
     `thinking_tokens: 31289`.
   - De las 38 ejecuciones del análisis directo del registro, ninguna usó `max`.
   - Qué cambiar: poner «con esfuerzo `high`» y la ejecución 44554333055.
   - Por qué importa: el hecho real es más fuerte que el citado. Con `high` ya se puede
     agotar 32 768 (la orientación del README da de 18 000 a 24 000 de salida), y la
     persona tiene que saberlo al elegir la salida.
2. **Falta una prueba del camino CLI con 65 536 válido.**
   - El workflow usa `main()` → `execute(..., max_output=max_output)`
     (`direct_analysis.py:860` y `:866-867`). Si se borra `max_output=max_output` de la
     llamada a `execute` (mutante M8 de abajo), las 72 pruebas de `direct_analysis` y las
     45 del cribado siguen en OK.
   - Consecuencia: el workflow con `salida_maxima=65536` lanzaría 32 768 sin que fallara
     nada. Solo se vería en el resumen de `preparar`.
   - Qué añadir: una prueba de `da.main([... '--max-output', '65536' ...])`. Por ejemplo,
     con `execute` parcheado, que compruebe que recibe `max_output=65536`. O sin
     `--execute-api`, que compruebe la fila `65536 tokens / 1500 s` en `report.md`.
3. **Documentar el tope de 2 MB del stream con 65 536.**
   - El transporte de AUTO1 corta a `STREAM_LIMIT_BYTES = 2_000_000`
     (`automation/coordination/critical_review.py:27`, `:139-140`), con el resultado pagado
     y no aceptado.
   - Ese tope se dimensionó para 32 768. Con 65 536 el stream puede tener el doble de bytes
     si el pensamiento llega en deltas visibles. No hay ninguna medida de los bytes del
     stream de Vinci 44554333055.
   - Qué cambiar: no hace falta tocar AUTO1. Basta con decirlo en «Límites conocidos» del
     README (`STREAM_DEMASIADO_GRANDE` posible con 65 536, sin medir). Lo ideal es anotar
     el tamaño del primer stream real de 65 536.

## Recomendaciones (no bloquean)

- R1. `automation/screening/screening.py:608-642`: el `configured` del cribado fija
  `MAX_OUTPUT=32768`, pero no fija `STREAM_DEADLINE_SECONDS`. Depende de que el análisis
  directo haya restaurado el suyo. Hoy eso está garantizado (ver hallazgo 3). Fijar
  también `STREAM_DEADLINE_SECONDS=720` en el cribado lo blindaría ante un fallo futuro.
  El mutante M11 (que el cribado lea `cr.MAX_OUTPUT`) es equivalente con el estado
  actual, y por eso ninguna prueba lo detecta.
- R2. `automation/direct_analysis/test_direct_analysis.py:399`: se cambió `max_usd='1'` a
  `'2'` sin explicarlo. Con `'1'` la prueba también pasa en HEAD (lo he comprobado), así
  que el cambio no hace falta. Es inocuo. Conviene devolverlo o explicarlo.
- R3. El caso que motivó el cambio (Vinci) no cabe con 65 536 bajo la cota de un token
  por byte: 955 094 + 65 536 > 1 000 000. El README lo dice con claridad (líneas 222-227
  y 333-334).
  - La entrada real de Vinci fue de 391 893 tokens. La cota es unas 2,4 veces más
    conservadora que lo observado.
  - Cambiarla es una decisión humana. El código no recorta, y eso es correcto.

## Hallazgos por punto

### 1. Opción por defecto: sin cambios respecto a `main` salvo campos informativos

- Ejecuté `da.execute` con `FakeHTTP` en los dos clones (`main` fcb18bb y HEAD 3dfedb7),
  en tres casos: ejecución correcta, salida 40 000 > 32 768 y aborto por contexto.
- Las llamadas a Anthropic son idénticas: `max_tokens` 32768, mismos cuerpos y mismo
  orden. También son idénticas las rutas de las llamadas a GitHub.
- Las diferencias son solo informativas:
  - `budget.stream_deadline_seconds: 720` en `reservation.json` y `report.json`
    (`direct_analysis.py:752`);
  - `max_output_tokens` y `stream_deadline_seconds` en la raíz de `report.json`
    (`:662-666`);
  - la fila `| Salida máxima / plazo del stream | 32768 tokens / 720 s |` en `report.md`
    (`:604`);
  - `stream_deadline_seconds` en `preflight.json`, y el orden de las líneas del
    `report.md` de aborto.
- `exposure()` y `Receipt` solo leen `budget.reserved_usd`
  (`critical_review.py` `exposure`, `Receipt.reserve`), así que la clave añadida a
  `budget` no altera el tope acumulado.
- La cota de contexto tras `count_tokens` (`direct_analysis.py:749`) y la de `preflight`
  (`:780`, `:793`) usan 32 768, como antes.

### 2. Con 65 536, todos los sitios usan 65 536 y 1500 s

`configured` (`direct_analysis.py:743-760`) fija `cr.MAX_OUTPUT=max_output` y
`cr.STREAM_DEADLINE_SECONDS=deadline`. `critical_review` los lee como globales del módulo
en el momento de cada llamada:

| Sitio | Dónde | Comprobado |
|---|---|---|
| Cuerpo `max_tokens` | `critical_review.py:570` | prueba con el transporte real: `max_tokens` 65536 |
| `check_usage` | `critical_review.py:488` | 65 537 da `CONSUMO_SUPERA_RESERVA`, 60 000 se acepta |
| Reserva `budget` | `critical_review.py:307`, `:311` | reserva = (cota·4 + 65536·20)/1e6 con Opus |
| Plazo del stream | `critical_review.py:254` | plazo observado ∈ (1495, 1500] |
| Socket | `critical_review.py:257` | 60 s |
| `preflight` | `direct_analysis.py:780-795` | reserva y contexto con `cr.MAX_OUTPUT` |
| Cota tras `count_tokens` | `direct_analysis.py:749` | 1 000 000 − 65 536 + 1 aborta sin reservar |

### 3. `configured` restaura siempre, y no hay herencia hacia AUTO1 ni hacia el cribado

- La validación (modelo, esfuerzo y `parse_max_output`, `:740-743`) va antes de cualquier
  `setattr`.
- La restauración está en `finally` (`:762-769`).
- El mutante M5 (restaurar solo a la salida normal) hace fallar 22 pruebas.
- Ningún módulo modifica `cr` al importarse: no hay ningún `cr.X =` fuera de `configured`.
- `test_auto1_run_still_sends_32768_with_720_s_deadline` ejecuta `cr.run` de AUTO1 después
  de un análisis directo con cada salida, y ve 32768/720.
- El cribado tenía `da.MAX_OUTPUT`. Ahora tiene su propia constante `MAX_OUTPUT = 32768`
  (`screening.py:87`). `da.preflight` lee la del cribado a través de `cr.MAX_OUTPUT`
  dentro del `configured` del cribado.
- `PER_CALL_WORST_SECONDS` (`screening.py:83`) sigue en 720 + 60 + 120.
- El único efecto visible en el cribado es una clave más (`stream_deadline_seconds`) en
  `row['preflight']`, que no se publica en ninguna tabla.
- `revalidar.py:38` usa el valor por defecto; `validate` no depende de la salida.

### 4. Validación de la entrada

- `parse_max_output` (`direct_analysis.py:680-688`) acepta solo `'32768'` y `'65536'`
  (o esos enteros). Rechaza `bool`, espacios, `0x8000`, `3.2768e4`, `32768.0`, `None` y
  listas.
- `main` lo valida antes de `verify_code` y de crear el cliente (`:860`). Con un valor
  inválido sale con código 2 y `SALIDA_MAXIMA_INVALIDA`, sin escribir nada en la salida.
- En el workflow, la entrada es de tipo `choice` con las opciones `['32768','65536']` y
  el valor por defecto `'32768'`. Llega a `env: SALIDA_MAXIMA: ${{ inputs.salida_maxima }}`
  y de ahí a `--max-output "$SALIDA_MAXIMA"` entrecomillado.
- No hay interpolación en el shell; lo cubre `test_inputs_never_interpolated_into_shell`.
- Los dos jobs, `preparar` y `analisis`, leen el mismo `inputs.salida_maxima` (con prueba).
- Un «Re-run» reutiliza las entradas y queda bloqueado por la reserva.

### 5. Invariante del workflow y publicación

- `timeout-minutes: 35` (`analisis-directo.yml:98`), es decir, 2100 s. El peor caso es
  1500 + 60 + 420 = 1980 s, así que quedan 120 s más que el margen de AUTO1.
- Evidencia real: el job `analisis` de Vinci 44554333055, que agotó 32 768 tokens, duró
  375 s de principio a fin (15:27:43 → 15:33:58), con preparación y publicación incluidas.
  Eso son unos 100 tokens por segundo, así que 65 536 tardarían del orden de 11 min.
  1500 s es holgado.
- La reserva se publica antes de la llamada (`critical_review.py:563`). Ante
  `PLAZO_TOTAL_SUPERADO`, el error de transporte se recoge en `run` y se ejecutan `write` y
  `publish` (`:580-592`).
- `Resumen` y `upload-artifact` llevan `if: always()`.
- Arrastrado de AUTO1, no introducido aquí: `publish` hace 8 peticiones a GitHub con un
  timeout de 180 s cada una (`pilot.py:110`). En el peor caso teórico eso supera el margen
  de 420 s. Pasaba igual con 20 min y 720 s.

### 6. Pruebas: mutaciones en un clon aparte

| Mutante | Resultado |
|---|---|
| M1 sin `STREAM_DEADLINE_SECONDS` en `configured` | falla (28) |
| M2 `MAX_OUTPUT` fijo en 32768 | falla (35) |
| M3 cota tras `count_tokens` fija en 32768 | falla (1, `test_context_check_after_count_uses_the_choice`) |
| M4 `preflight` con salida fija | falla (34) |
| M5 sin restaurar ante excepción | falla (22) |
| M6 `parse` con `strip()` | falla (2) |
| M7 `main` valida después de leer | falla (1) |
| **M8 `main` no pasa `max_output` a `execute`** | **no falla ninguna prueba** (corrección 2) |
| M9 el writer sin los campos | falla (3) |
| M10 65536 con plazo de 720 s | falla (28) |
| M11 el cribado lee `cr.MAX_OUTPUT` | no falla: mutante equivalente con el estado actual (R1) |
| M12 timeout del job de 20 min | falla (1) |
| M13 job `analisis` sin `--max-output` | falla (1) |
| M14 reserva fija en 32768 dentro de `budget` | falla (1) |

### 7. README

He comprobado las reservas de todos los manifiestos (31 paquetes) con los 3 modelos y las
2 salidas, ejecutando `preflight` en HEAD. Todas coinciden con el README:

- Ahold: 4,51 con 32 768 y 5,16 con 65 536, que aborta por contexto.
- Elis: 5,01 con 65 536, que aborta por coste; Sonnet sí cabe (2,50).
- Jumbo: 4,57 con 65 536; Fable 9,14, que no cabe.
- Vinci, Zoetis T1 y Zoetis T2 abortan por contexto con los tres modelos.
- Fable con 32 768 en los paquetes de examen: 8,85-9,01.
- Los 25 `universo_*`:
  - Opus: 1,18-1,43 con 32 768 y 1,84-2,09 con 65 536;
  - Fable: 2,37-2,86 con 32 768 y 3,68-4,17 con 65 536.
- Las ocho finalistas con 65 536 suman 15,232184 («15,23»). Las reservas de la tanda con
  32 768 suman 18,941908 («18,94»).
- Las cotas de entrada máximas son 934 464 con 65 536 y 967 232 con 32 768. Fable con
  65 536 admite unos 297 320 tokens de cota (unos 293 KB).

La única falsedad encontrada es la de la corrección 1.

### 8. Secretos, red y AUTO1

- El diff no toca `automation/coordination`, `automation/claude_review` ni
  `claude-critical-review.yml`.
- No hay secretos en el diff. Las claves de las pruebas son `fake-key` y `fake-gh`.
- Las pruebas nuevas no usan la red. Hay `build_opener` parcheado, y con `unshare -rn`
  pasan todas las nuevas.
- Sin red sí fallan 9 pruebas de `PackageTests`/`UniversoTests` y 1 de `test_finalistas`
  en el cribado. Es por la identidad de `git commit` dentro del espacio de nombres, y
  falla igual en `main`.

## Salida de las pruebas

En el worktree `/home/user/e_work/wt_salida64k`, HEAD 3dfedb7, con
`python3 -I -m unittest discover -s automation/<dir> -p 'test_*.py' -v`:

```
== claude_review
Ran 49 tests in 0.036s

OK
== coordination
Ran 97 tests in 0.709s

OK
== direct_analysis
Ran 72 tests in 11.613s

OK
== screening
Ran 45 tests in 1.029s

OK
```

En `main` fcb18bb: 49, 97, 60 y 44, todas OK. Las nuevas son 12 en `direct_analysis` y 1
en el cribado.

---

## Verificación de 68f1c91

**Veredicto final: CONFORME.**

Contexto:
- Commit `68f1c91` sobre `3dfedb7`. Verificado el 20-nov-2026 por el mismo revisor, que
  no es el autor del cambio.
- El worktree `/home/user/e_work/wt_salida64k` está en la cabeza remota (`git fetch` y
  `checkout` de `origin/automatizacion/analisis-directo-salida-64k`) y no tiene cambios
  locales.
- Las mutaciones se hicieron en un clon aparte, en el scratchpad.
- El diff con `origin/main` sigue sin tocar `automation/coordination`,
  `automation/claude_review` ni otros workflows.

### Las tres correcciones y las recomendaciones

1. **Vinci con `high`: hecho.**
   - `direct_analysis.py:43-45` y `README.md:116-117` y `:333-338` citan ahora la ejecución
     44554333055 con esfuerzo `high`.
   - Ya no queda en el código ni en el README la frase «esfuerzo `max` un análisis de Vinci».
   - Datos del README comprobados en el registro:
     - 39 carpetas del análisis directo, ninguna con `max`;
     - las demás con `high` van de 13 315 a 24 400 tokens de salida.
2. **Prueba de `main` con 65 536: hecho.**
   - `test_cli_passes_65536_to_execute` hace pasar `main()` real sin red.
   - El mutante N1 (quitar `max_output=max_output`) ahora falla.
3. **Tope de bytes del stream: hecho.**
   - `STREAM_LIMITS = {32768: 2 000 000, 65536: 4 000 000}` (`direct_analysis.py:60`).
   - Se fija en `cr.STREAM_LIMIT_BYTES` solo dentro de `configured` (`:753`, `:768`) y se
     restaura en el `finally`.
   - `read_stream`/`_lines` lo leen como global en cada lectura
     (`critical_review.py:135`, `:139`).
   - Queda registrado en `preflight` (`:797`), `report.json` (`:673`), `report.md` (`:613`)
     y `budget.stream_limit_bytes` (`:762`).
   - La prueba con unos 3 MB de SSE válido pasa con 4 MB y da `STREAM_DEMASIADO_GRANDE` con
     2 MB y fuera de `configured`.
4. **R1 (cribado):** `screening.py` fija sus propios `STREAM_DEADLINE_SECONDS = 720` y
   `STREAM_LIMIT_BYTES = 2 000 000` en su `configured`. `PER_CALL_WORST_SECONDS` sale de su
   constante y vale lo mismo, 900. Hay una prueba con `cr` dejado a propósito en
   65536/1500/4 MB: el cribado sigue enviando y usando 32768/720/2 MB.
5. **R2:** `max_usd` vuelve a `'1'`.

### Con 32 768, lo enviado y lo aceptado es idéntico a `main`

- Repetí la comparación con `FakeHTTP` en los mismos tres casos (correcto, salida 40 000 y
  aborto), con `main` fcb18bb y con 68f1c91.
- Las llamadas a Anthropic son idénticas, con `max_tokens` 32768, y también las rutas de
  GitHub.
- El tope de bytes efectivo es 2 000 000, el mismo de AUTO1. Plazo, `check_usage` y
  validación no cambian. El caso de 40 000 tokens acaba en el mismo error y el mismo estado
  de coste.
- Las diferencias son solo informativas: `stream_deadline_seconds: 720` y
  `stream_limit_bytes: 2000000` en `budget` (reserva e informe), las mismas claves y
  `max_output_tokens` en la raíz de `report.json`, y dos filas en `report.md`.

### El nuevo tope no se filtra a AUTO1 ni al cribado

| Mutante | Resultado |
|---|---|
| N1 `main` no pasa `max_output` | falla (1) |
| N2 `configured` sin `STREAM_LIMIT_BYTES` | falla (4) |
| N3 tope de 65536 = 2 MB | falla (5) |
| N4 tope de 32768 = 4 MB | falla (5) |
| N5 sin restaurar ante excepción | falla (23) |
| N6 el cribado no fija plazo ni tope | falla (1, cribado) |
| N7 el cribado no fija el tope | falla (1, cribado) |
| N8 el cribado toma `MAX_OUTPUT` de `cr` | falla (1, cribado) |
| N9 `budget` sin `stream_limit_bytes` | falla (3) |
| N10 `preflight` con tope fijo | falla (3) |

Los dos mutantes que sobrevivían en la revisión anterior (M8 y M11) ahora fallan: son N1 y
N8.

### ¿Son honestas la medición y la justificación de los 4 MB?

En lo esencial, sí. Recalculé las cifras desde la rama de registro:

- **2,3 bytes por token** del texto visible escapado en JSON: en las 37 ejecuciones del
  análisis directo con uso registrado va de 2,22 a 2,47. Coincide.
- **De 5 700 a 8 200 tokens visibles con `high`:** 5 736-8 212, sin contar el Vinci
  truncado. Coincide.
- **Vinci 44554333055** cerró el stream con uso final, así que entró en menos de 2 MB.
- **Cuentas:** 65 536 × 120 B ≈ 7,8 MB y 8 200 × 120 B ≈ 1 MB. Bien hechas.
- **Lo que no se sabe:** el README reconoce que no se registran los bytes totales y que
  4 MB «cubre el doble de lo que cupo con 32 768, no un caso extremo». Además recomienda
  anotar el primer stream real. Es honesto.
- **«El pensamiento llega omitido»:** no es una medición. Coincide con el comportamiento
  documentado de la API: con Opus 5.5, Fable 5.2 y Sonnet 5.5, `thinking.display` es
  `"omitted"` por defecto y los bloques de pensamiento llegan en streaming con el texto
  vacío. Es una afirmación correcta, aunque convendría decir que sale de la documentación y
  no de una medida.

Dos imprecisiones menores. No cambian el veredicto, pero conviene arreglarlas si se toca de
nuevo el texto:

- `README.md:346-347` dice «2,22-2,47 en las 37 ejecuciones … y en el cribado». En el
  cribado el rango es 2,29-2,50 (sony 2,50, airbus 2,49), así que el 2,47 no lo cubre.
- `direct_analysis.py:58` habla de «38 ejecuciones del análisis directo», mientras que el
  README dice 37 con uso registrado y 39 carpetas. Hay que unificar la cifra.

### Salida de las pruebas

En `/home/user/e_work/wt_salida64k`, HEAD 68f1c91, con
`python3 -I -m unittest discover -s automation/<dir> -p 'test_*.py' -v`:

```
== claude_review
Ran 49 tests in 0.050s

OK
== coordination
Ran 97 tests in 0.789s

OK
== direct_analysis
Ran 75 tests in 12.810s

OK
== screening
Ran 46 tests in 1.095s

OK
```
