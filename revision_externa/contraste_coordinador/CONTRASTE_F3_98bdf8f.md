# CONTRASTE_F3_98bdf8f · revisión del coordinador que emite CORRECCION_F3 (respuesta F2 de Mistral C/F)

- **Revisión contrastada:** `coordinacion/cierre_v2/revisiones_coordinador/F2_195766f_98bdf8f/` @ `30c314c`: `REVISION_F2_195766f_98bdf8f.md`, `CORRECCION_F3.md`, `sondas/` (34 archivos).
- **Objeto:** rama `mistral/f-alcance-real` de `195766f` a `98bdf8f`, carpeta `resultados_cierre/alcance_real/`.
- **Veredicto del contraste: CONFORME.** El hallazgo medio F3-R5 se confirma en el código del producto; el manifiesto se reproduce; CONTROL refleja la revisión. Sin hallazgos falsos ni omitidos detectados en lo contrastado.

## Sondas propias (verificación)

| Comprobación | Resultado mío | Informe |
|---|---|---|
| Manifiesto @ `98bdf8f` (`resultados_cierre/alcance_real`) | exit 0; **46/46 OK** | «46/46 en 98bdf8f» |
| **F3-R5 (medio)** en el producto | `jluisplagos/munger-v2` @ `957af65`, `munger_v2_r1/v6/scripts/V6.1/build_v6.py`: **:581-582** el motor (`Diagnóstico V6!C5`) = `IF(Análisis!$C$62="Sí","A", … "C" …)` → **se elige en `Análisis!C62`**; V01 **:1102-1103** «Motor elegido (Análisis C62)»; `Palancas C6` (caso especial «Financiera») solo produce el aviso `⛔ REVISAR` (~:589-592, `D_COHER`) y **V11 (:1133)** bloquea A/B para financieras | CORRECCION_F3: «comprobado por el coordinador en build_v6.py: el motor se elige en Análisis!C62 (V01, :1102-1103; Diagnóstico V6 A5). Palancas C6 solo produce el aviso REVISAR (:589-590) y bloquea A y B (V11, :1133)» → **exacto** |
| Cita «Financiera → motor C» | está en la nota de la lista `Lista_Caso` (:586-ish, fila 6 de la tabla de tipo de empresa), no en la fórmula del motor | coherente con R5 |
| Alcance/higiene | el informe declara 71/71 PDF con huella (necesita el ZIP base-4.14; no reejecutado aquí), 323 de 6799 archivos fuera del alcance sin aviso (sonda del informe) | no reejecutado por mí (ZIP de 1,13 GB); coherente con la sonda publicada |

## Control (CONTROL.json)

F-B3 y F-C1: `revision=CORRECCIONES`, `commit_origen=98bdf8f…`, `pruebas_externas=REPRODUCIDAS`, `integracion=NO`; el evento «F2 de Mistral C/F (195766f…98bdf8f) revisado: D1 y D4 cerrados, el resto con límites; CORRECCION_F3 (R5 medio, comprobado por el coordinador en build_v6.py: el motor se elige en Análisis!C62…)» está en `registro_eventos` y es exacto. Nada aceptado sin evidencia.

## Discrepancias / pendientes

- Ninguna en la revisión contrastada.
- **Pendiente (no discrepancia):** la rama `mistral/f-alcance-real` ya avanzó a `c504830` con la respuesta completa a F3 (R3–R15); en el corte no hay revisión del coordinador de esos commits y CONTROL sigue en `98bdf8f`. Queda pendiente la próxima revisión del coordinador, como prevé el encargo.
