# CONTRASTE_A4_0946971 · revisión del coordinador que emite CORRECCION_A4 (respuesta A3 de Mistral A)

- **Revisión contrastada:** `coordinacion/cierre_v2/revisiones_coordinador/A3_0946971/` @ `30c314c`: `REVISION_A3_0946971.md`, `CORRECCION_A4.md`, `sondas/` (40 archivos).
- **Objeto:** rama `mistral/m2-cobertura-vm` @ `0946971` (8 commits desde `8b88fab`), carpeta `resultados_m2/cobertura_vm/`.
- **Veredicto del contraste: CONFORME, con un límite de reproducción.** Todo lo verificable desde git se reproduce; la reproducción completa del pipeline (192/196 byte a byte) no la reejecuté (requiere el ZIP base-4.14 de 1,13 GB y pypdf/openpyxl, fuera de este entorno). CONTROL refleja la revisión. Sin hallazgos falsos ni omitidos detectados.

## Sondas propias (verificación sobre `git archive 0946971`)

| Comprobación | Resultado mío | Informe |
|---|---|---|
| `sha256sum -c MANIFIESTO_SHA256.txt` en `cobertura_vm` | exit 0; **196/196 OK** | manifiesto 196/196 |
| `COBERTURA_677.csv` (677 filas) | `estado_contextual`: **REVISADO 209 / PENDIENTE 283 / CONFLICTO 19** (+ NO_APLICA 106, REUTILIZADO_M1 60) | 169/209/133 → **209/283/19** (y 60/106) |
| Polaridad (A4-R1) en `resultados/verificacion_contexto.jsonl` | Vidrala `Historia!J6`, `J7`, `J8`, `aux:bai_2023`, `aux:impuesto_2023` llevan `["CONFLICTO", "declara no reexpresado (\"sí: 2023 reexpresado sin …\") …"]` — **5 entradas reales con polaridad invertida**, exactamente las del informe; la negación no reconocida («None of … were restated») es coherente con el patrón | 5 reales; J7 y bai_2023 pierden REVISADO |
| A4-R5 huella de ENTREGA | `ENTREGA.json` contiene `…c3568c2cda9d4c6216c47595d1bec3c091441100ba9`; el sha256 real de `resultados/control_cobertura.json` es `8e0a23a2…c3558c2cda9d4c6216c47595d1bec3c091441100ba9` → **un dígito cambiado (c3568c2 vs c3558c2)** | huella errónea confirmada |
| A4-R5 docstring de `cola_pendientes.py` | dice «en v4.0 son 26, no 46»; la salida real `cola_pendientes.json` da **233 fuentes / 50 derivados / 88 grupos** | docstring desfasado (26 donde son 50) |
| Reproducibilidad 192/196 | **No reejecutada por mí** (necesita el ZIP `munger_v2_r1_entrega4.14_cierre_verificacion_entradas.zip`, 1.130.912.246 bytes, Release `base-4.14`, sha `bb51942c…`, más pypdf/openpyxl). Las sondas s01/s01c/s01d del informe no se han vuelto a correr aquí | límite declarado |

## Control (CONTROL.json)

A-CTX: `revision=CORRECCIONES`, `integracion=NO`, `solicitud_revision.estado=RESPONDIDA` con `informe_revision.ruta = …/A3_0946971/REVISION_A3_0946971.md` y veredicto «R7 cerrado; R1, R5 y R6 cerrados con límites; R2, R3, R4 y R8 abiertos. CSV 169/209/133 → 209/283/19; ninguna entrada en REVISADO sin todas sus dimensiones; los 15 CONFLICTO de fuente examinados no son reales (13 artefactos nuevos de R3/R4)» — **coincide con el informe** y con mis recuentos (209/283/19). La observación «polaridad invertida en Vidrala Historia!J6/J7 comprobada por el coordinador» es exacta (la verifiqué en las 5 celdas). Nada aceptado sin evidencia.

## Discrepancias

Ninguna en la revisión. Límite: la reproducción byte a byte del pipeline queda como evidencia del revisor (no reejecutada aquí por tamaño/dependencias); los puntos comprobables desde git (manifiesto, recuentos CSV, polaridad, huellas, textos desfasados) reproducen.
