# CONTRASTE_RESUMEN · contraste externo de las revisiones del coordinador (corte `30c314c`)

**Veredicto global: CONFORME CON UNA DISCREPANCIA DE CONTROL.** Las siete revisiones contrastadas se sostienen: sus hallazgos se reproducen con sus sondas (las reejecuté sobre copias de los commits revisados), no se acepta nada sin evidencia, no detecté hallazgos falsos ni omitidos, y CONTROL.json refleja las revisiones salvo una discrepancia puntual (abajo).

| Revisión contrastada | Veredicto del contraste | Hallazgos reproducen | Aceptación sin evidencia | Hallazgos falsos/omitidos | CONTROL refleja |
|---|---|---|---|---|---|
| AUTO_a508d6b (T-AUTO) | CONFORME | Sí: 100/100 pruebas; sonda SSE idéntica (25/16/9); sonda workflows idéntica; M1/M6/M7/m6 verificados en código | No (CORRECCIONES, no aceptado) | Ninguno detectado | Sí |
| MANUAL_v2_ef36ab1 (G-MANUAL) | Revisión se sostiene | Sí: S01-S16 clave (603 citas, literales, 476/274, M1/M2/M3, S05, S13) | No | Ninguno; el «FUERA DE RANGO» de L635 es falso positivo de la herramienta (`:375` → CONTINUIDAD.md:375) | **No del todo: D-MANUAL-1** |
| D3 · D2_3934bc9_5f4b2a2 | CONFORME | Sí: manifiestos (4 y 11+1 fallos; banco 57/57); `sondas_arnes_d2.py` idéntica salvo rutas temporales; log de comprobaciones idéntico; regeneración 29/1/6/0 vs 30 CUMPLE publicados | No; 0/36 declarado correctamente | Ninguno detectado | Sí (en eventos; sin `solicitud_revision` formal) |
| D_d032691 (bloque 3) + D-36 | CONFORME | Sí: 204/204; `sondas_arnes_d3.json` **idéntica** (cero diferencias); 0/36 casos del personaje, nada aceptado | No; 0/36 correcto | Ninguno detectado | Sí (en eventos) |
| A4 · A3_0946971 | CONFORME (límite: pipeline completo no reejecutado, requiere ZIP de 1,13 GB) | Sí en lo git-verificable: 196/196; CSV 209/283/19; polaridad invertida en las 5 celdas; huella c3568c2 vs c3558c2 real; docstring 26 vs 50 reales | No | Ninguno detectado | Sí |
| E2 · E1_23718fb | CONFORME (límite: 52/52 citas no reejecutadas, requiere los PDF de la Release) | Sí en lo verificable: manifiestos (2 .pyc en 23718fb; 49/49 en f00c5dd); 32 extractos; E-R2 confirmado en URD p.306/p.341 (Acquaflash sí es importante; Lavartex no) | No | Ninguno detectado | Sí |
| F3 · F2_195766f_98bdf8f | CONFORME | Sí: 46/46; F3-R5 confirmado en `build_v6.py` @957af65 (motor en `Análisis!C62`, :581-582; V01 :1102-1103; Palancas C6 solo aviso/V11) | No | Ninguno detectado | Sí |

## Discrepancias

1. **D-MANUAL-1 (control):** `CONTROL.json` `tareas[G-MANUAL].revision = "CONFORME_CON_LIMITES"`, pero el `informe_revision.veredicto` enlazado y el `registro_eventos` dicen **CORRECCIONES (4 medios, 12 menores)**; `ESTADO.md` hereda el campo en la tabla y contradice su propio texto de «Próxima acción» («CORRECCIONES (M1–M4 y 12 menores)»). Parece residuo de la revisión v1 (`78ba1ca`, CONFORME_CON_LÍMITES). No hay aceptación indebida, pero el campo no refleja el veredicto revisado. Sugerencia: `revision = "CORRECCIONES"`.
2. **Nota estructural (no error):** las revisiones de D (D3 y d032691) quedan en `registro_eventos`/`observacion` sin `solicitud_revision.informe_revision` formal, a diferencia de T-AUTO/A-CTX/E-ELIS/G-MANUAL. El veredicto sí está reflejado.
3. **Pendiente, no discrepancia:** `mistral/f-alcance-real` avanzó a `c504830` (respuesta a F3) sin revisión del coordinador publicada todavía; CONTROL sigue en `98bdf8f`, lo cual es correcto.

## Límites del contraste

- Sin red, sin API de pago, sin workflows, sin LibreOffice, sin ejecutar el producto ni el personaje.
- No reejecuté: el pipeline de A completo (ZIP base-4.14 de 1,13 GB + pypdf/openpyxl), las 52/52 citas de E contra los PDF de la Release, ni las sondas de F que leen el ZIP (71 PDF). En esos puntos acepto la evidencia publicada del revisor y lo declaro.
- Python 3.12.15 en mi entorno (el revisor de AUTO declaró 3.13.18); las sondas igualmente reprodujeron idénticas.
