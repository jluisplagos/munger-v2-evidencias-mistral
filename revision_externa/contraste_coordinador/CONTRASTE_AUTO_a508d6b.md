# CONTRASTE_AUTO_a508d6b · revisión del coordinador sobre T-AUTO (`automatizacion/coordinacion-api-v1` @ `a508d6b`)

- **Revisión contrastada:** `coordinacion/cierre_v2/revisiones_coordinador/AUTO_a508d6b/` (rama `coordinacion/cierre-v2` @ `30c314c`): `REVISION_AUTOMATIZACION_a508d6b.md`, `CORRECCION_AUTO1.md`, `sondas/`.
- **Veredicto del contraste: CONFORME.** Los hallazgos se reproducen con sus sondas, nada queda aceptado sin evidencia y CONTROL.json refleja la revisión. Sin discrepancias.

## Sondas propias (reproducción)

Sobre una copia con `git archive a508d6b` (sin `.git`), Python 3.12.15:

| Sonda | Comando | Resultado | Comparación con lo publicado |
|---|---|---|---|
| Pruebas del autor | 6 × `python3 -I -m unittest discover -s automation/... -p test_*.py` | exit 0 en las 6; 49+22+14+3+5+7 = **100 OK** | Idéntico al informe §2 (100/100) |
| `sonda_sse.py` | `python3 -I sondas/sonda_sse.py <copia>` | exit 0; **26 líneas idénticas byte a byte** a `sonda_sse.salida.jsonl`: 25 casos, 16 conformes, 9 hallazgos (S08, S10, S11, S11b, S12, S13, S16, S17, S20) | Idéntica |
| `sonda_workflows.sh` | `sh sondas/sonda_workflows.sh <copia>` | exit 0; salida **idéntica** a `sonda_workflows.salida.txt` tras sustituir la ruta por `<rev_auto>` | Idéntica |
| Cabecera `267ad18` | `git diff a508d6b..267ad18 --stat` | solo 2 archivos bajo `automation/coordination/observations/` | Confirma «la cabecera solo cambia observations/» |

## Hallazgos verificados en el código (copia de `a508d6b`)

- **M1:** `http.client.IncompleteRead.__mro__` = `IncompleteRead → HTTPException → Exception` (no `OSError`/`ValueError`); las cláusulas `except` de `critical_review.py:113-117` no la cubren y `run()` solo captura `PilotError`. Confirmado.
- **M6:** `claude-critical-review.yml`, `qwen-bank-mistral-groups.yml`, `qwen-bank-mistral-review.yml` y `vibe-auth.yml` tienen `on: push` a la rama, pasos con `--execute-api`/scripts de inferencia y **ningún `environment:`** en ningún workflow. Confirmado estáticamente (no se ejecutó ningún workflow).
- **M7:** `qwen-bank-mistral-groups.yml:33` `pip install mistral-vibe==3.1.2` sin `--require-hashes`, mismo job con `contents: write` (:19) y `ANTHROPIC_API_KEY` (:45). Confirmado.
- **m6 (higiene):** el grep de la sonda no encuentra referencias a `main`/`cierre-v2`/`CONTROL.json`/`ESTADO.md` en el código Python; las escrituras van solo a `LEDGER_BRANCH = 'automatizacion/claude-api-piloto-registro'`. Confirmado.

## Verificaciones adicionales sobre el registro y los PR

- `relevos-002/report.json` en `953af02` y en `5b12950`: sha256 `1bd8a6388dc798cb8217cfd13f59edaa087c657d6bf9aaac2289cfa53065b9fa` en ambos; `REPLAY_SHA256` en el `sources.json` del registro lleva el mismo valor. La afirmación de CONTROL se cumple.
- Reserva `audit-pilot-code-001`: `state=RESULTADO_NO_ACEPTADO_NO_REINTENTAR`, `code_sha=501fd8b9…`, `budget.reserved_usd=1.912936`. Confirmado.
- PR #1 (borrador, abierto): `automatizacion/piloto-claude-api` `7d9001e` → `main` `e137b85`. PR #2 (borrador, abierto): `automatizacion/coordinacion-api-v1` `267ad18` → `automatizacion/piloto-claude-api` `7d9001e`. Ambos en estado borrador, sin fusionar. Confirmado.

## Control (CONTROL.json)

T-AUTO: `revision=CORRECCIONES`, `integracion=NO`, `alcance_aceptado=[]`, `solicitud_revision.estado=RESPONDIDA` con `informe_revision` en la ruta publicada y veredicto «Sin hallazgos materiales. Medios M1–M7 y menores m1–m9. Pruebas del autor reproducidas: 100/100. Sondas propias: 16 conformes de 25», que coincide con el informe. El evento de revisión está en `registro_eventos`. **Nada aceptado sin evidencia.**

## Discrepancias

Ninguna. Límite heredado del informe (y confirmado): «sin pago por uso» no es comprobable desde el código; no se lanzó red ni workflow para comprobarlo.
