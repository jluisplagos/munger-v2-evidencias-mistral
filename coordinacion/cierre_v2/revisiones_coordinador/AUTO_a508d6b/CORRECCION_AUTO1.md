# Corrección AUTO1 · automatización de coordinación · sobre `a508d6b`

- **Para:** quien mantiene la rama `automatizacion/coordinacion-api-v1` (el usuario, con ChatGPT). No se corrige desde esta sesión: el revisor no es el autor.
- **De:** el coordinador, según [REVISION_AUTOMATIZACION_a508d6b.md](REVISION_AUTOMATIZACION_a508d6b.md). La revisión la hizo un contexto distinto del autor, sin red y sin llamadas a API ni a workflows. Las sondas están en `sondas/`.
- **Comprobado por el coordinador:**
  - M1: `http.client.IncompleteRead` deriva de `HTTPException` y `Exception`, no de `OSError`. No lo captura `critical_review.py:113-117` ni `run()`, que solo captura `PilotError`.
  - M6: `claude-critical-review.yml`, `qwen-bank-mistral-groups.yml`, `qwen-bank-mistral-review.yml` y `vibe-auth.yml` se disparan con `on: push` sobre la rama, cuando cambian los scripts, y no tienen `environment:` protegido.
- **La cabecera actual, `267ad18`, solo cambia `observations/`.** La revisión sigue valiendo para el código.

## Clasificación

**Conforme:**
- un único intento, sin reintentos ni segunda inferencia;
- `audit-pilot-code-001` no se repite: su reserva bloquea antes de cualquier llamada;
- el parser SSE trata bien los eventos partidos, varias líneas `data:`, CRLF, `ping`, `event: error`, la falta de `message_stop` y `max_tokens`;
- el uso se acumula bien;
- los secretos no aparecen en prompts ni en informes;
- solo se escribe en la rama de registro, nunca en `main`, `coordinacion/cierre-v2`, CONTROL ni ESTADO.

**Pruebas del autor reproducidas en copia:** 100/100, con `python3 -I -m unittest`, código 0. Ninguna ejercita `StreamingHTTP.call`. Superar pruebas mecánicas no equivale a una auditoría recibida.

**No hay hallazgos materiales.** Ningún resultado falso queda aceptado, no se libera ninguna reserva y no se repite ninguna inferencia.

## Defectos (medios)

| | Defecto | Prueba de cierre |
|---|---|---|
| **AUTO1-M1** | Un corte limpio a mitad de un chunk (`IncompleteRead`) escapa sin informe y la reserva queda en `RESERVADO_NO_REINTENTAR` | S08 y S17 dan `PilotError(..._NO_REINTENTAR)`, con informe y reserva actualizados |
| **AUTO1-M2** | Un evento JSON que no es un objeto, o que está anidado en exceso, escapa con `AttributeError` o `RecursionError` | S11, S11b y S12 dan `PilotError`, más una prueba unitaria |
| **AUTO1-M3** | Si `message_delta` no trae `usage`, se acepta con el `output_tokens` provisional y el coste queda subestimado | S10 da `PilotError` |
| **AUTO1-M4** | Un timeout queda con el mismo estado que un rechazo de coste conocido: no hay estado de coste incierto con cota y se pierde el uso parcial | S18: estado y cota en `report.json` y en la reserva |
| **AUTO1-M5** | No hay tope acumulado entre tareas: cambiar `TASK` permite otra reserva | Prueba con dos tareas cuya suma supera el tope |
| **AUTO1-M6** | Las inferencias de pago se disparan al hacer push, sin una puerta humana | `workflow_dispatch`, o push solo para las pruebas, y `environment` con revisores para los pasos con `ANTHROPIC_API_KEY` o `MISTRAL_VIBE_CLI_KEY`. La sonda de workflows no encuentra ninguno |
| **AUTO1-M7** | `pip install` sin hashes en el mismo job que `ANTHROPIC_API_KEY` y un token con escritura | Jobs separados e instalación con `--require-hashes` |

**Menores m1–m9:** su detalle y su prueba están en el informe, §4.

## Entrega

- Un commit con la corrección, más ENTREGA con los comandos y sus códigos de salida.
- `sondas/sonda_sse.py` da 25/25 conforme sobre el código corregido.
- La sonda de workflows no muestra ningún paso con secreto de inferencia bajo `push` sin una puerta.
- **No se lanza ninguna inferencia para probar la corrección.**
- El coordinador revisa solo lo afectado.
