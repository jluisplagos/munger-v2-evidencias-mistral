# CONTRASTE_D_d032691_D36 · revisión del bloque 3 de Mistral D frente a D3, y la aceptación de los 36 casos del personaje

- **Revisión contrastada:** `coordinacion/cierre_v2/revisiones_coordinador/D_d032691/` @ `30c314c`: `REVISION_D_d032691.md`, `ESTADO_D3_TRAS_d032691.md`, `sondas/`.
- **Veredicto del contraste: CONFORME.** La sonda se reproduce byte a byte; el estado por punto (R6 cerrado, regeneración cerrada, R1–R5/R8 abiertos con 7 variantes nuevas) cuadra con la salida; la aceptación de los 36 casos sigue en 0/36 y nada se acepta sin evidencia.

## Sondas propias (reproducción)

Copia con `git archive d032691`:

| Comprobación | Resultado mío | Informe/ESTADO |
|---|---|---|
| `sha256sum -c MANIFIESTO_SHA256.txt` en `resultados_qwen/ejecucion_d` @ `d032691` | exit 0; **204/204 OK** | R6 cerrado, 204/204 |
| `python3 -I -B sondas_arnes_d3.py <ejecucion_d d032691> <banco @4745f38> out.json` | exit 0; **diff profundo con `sondas_arnes_d3.json` publicado: cero diferencias** (R1 con las variantes nuevas N1a/N1b/N3/N4/N4b/N5a, matriz M2/N2a/N2b/M3, `ejecutar_todo` vs M2, R2 con controles negativos, R3 reevaluación, R4 relevos) | idéntica |
| Cronología | `d032691` (09:59:44 UTC) anterior a la publicación de `CORRECCION_D3.md` (`314c4dc`, 10:02:25 UTC) → el bloque 3 no es respuesta a D3; D3 sigue vigente | igual en ESTADO_D3_TRAS |

## Aceptación de los 36 casos del personaje (D-36)

- CONTROL.json D-36: `entrega=PARCIAL`, `revision=CORRECCIONES`, `integracion=NO`, pruebas `DECLARADAS/PARCIALES`; «**0/36 casos del personaje (correcto)**. No se ejecutan con un arnés sin aceptar; el runtime del coordinador los ejecutará cuando D3-R1…R4 estén cerrados»; bloqueo real = la adaptación a vías soportadas y la correspondencia criterio→observable (D2-R4/R5).
- La revisión de `d032691` declara «0/36 completos» y «no se ejecutan los 36 casos con este arnés mientras D3-R1…R4 sigan abiertos»; Q-CONTRASTE también declara 0/36 («nada se acepta automáticamente»).
- **Verificación:** en `d032691` la regeneración da 29 CUMPLE de componente + 1 BLOQUEO_ENTORNO + 6 NO_EJECUTADO = 0 casos completos; no hay ningún artefacto que afirme ejecución del personaje. **Nada aceptado sin evidencia: correcto.**

## Control (CONTROL.json)

- El evento «D bloque 3 (d032691) revisado frente a D3: R6 cerrado (manifiesto 204/204, comprobado por el coordinador), regeneración byte a byte y recuentos coherentes (0/36); R1–R5 y R8 abiertos, con 7 variantes nuevas» está en `registro_eventos` y coincide con la sonda reproducida; D-HARNESS/D-36 siguen en `CORRECCIONES`, no aceptados.
- Misma nota estructural que en D3: sin `solicitud_revision.informe_revision` formal; el veredicto queda en eventos/observación.

## Discrepancias

Ninguna. Pendiente (no discrepancia): la respuesta de Mistral D a D3 seguía sin publicarse en el corte (`mistral/d-qwen-aceptacion` @ `d032691`).
