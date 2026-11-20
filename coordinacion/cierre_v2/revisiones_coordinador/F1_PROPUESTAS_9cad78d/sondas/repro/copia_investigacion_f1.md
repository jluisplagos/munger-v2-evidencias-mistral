# Copia de investigación F1 · Elis (P2–P4 y correcciones V1–V11)

Generado por `scripts/copia_investigacion_f1.py`. **No es una entrada registrada, ni una política adoptada, ni una valoración.** Elis sigue en `pendiente_de_datos`. Mismas funciones que `contraste_f1.py`; solo cifras verificadas; libro en solo lectura.

Controles: 67, fallidos: 0.

## P3 · Ajustes y cálculo conjunto (perímetro A0; la variación es la misma en A1 y A2)

| Escenario | τ 2023 / 2024 / 2025 | τ 5 años | f (A0) | Flujo sin crecimiento | Variación | de ella: f / m0 / τ | Terminal NORMAL |
|---|---|---|---|---|---|---|---|
| Sin ajustes (libro) | 0.2963 / 0.2754 / 0.256 | 0.2882 | 0.041681455 | 248.496 | — | — | — |
| N1a · earnout de 2023, tipo fijo (fila 10 sin cambios) | 0.2963 / 0.2754 / 0.256 | 0.2882 | 0.044196893 | 236.43 | -12.066 | -12.066 / 0.0 / 0.0 | -17.778 |
| N1a · earnout de 2023, no deducible (gasto sin cambios) | 0.2619 / 0.2754 / 0.256 | 0.28132 | 0.045569131 | 234.182 | -14.314 | -18.648 / 0.0 / 4.334 | -22.614 |
| N1 · ajustes de earnout 2023–25, tipo fijo | 0.2963 / 0.2754 / 0.256 | 0.2882 | 0.043746946 | 238.731 | -9.765 | -9.908 / 0.142 / 0.0 | -14.598 |
| N1 · ajustes de earnout 2023–25, no deducibles | 0.2619 / 0.2806 / 0.2559 | 0.28234 | 0.044900433 | 236.891 | -11.605 | -15.441 / 0.144 / 3.692 | -18.609 |
| N2 · bajas de 2025 (seguros), tipo fijo | 0.2963 / 0.2754 / 0.256 | 0.2882 | 0.040283726 | 236.908 | -11.589 | 6.705 / -18.293 / 0.0 | 9.879 |
| N2 · bajas de 2025 (seguros), gravadas al tipo teórico | 0.2963 / 0.2754 / 0.2559 | 0.28818 | 0.040288143 | 236.899 | -11.598 | 6.683 / -18.294 / 0.013 | 9.861 |
| N2 · bajas de 2025 (seguros), no gravadas | 0.2963 / 0.2754 / 0.2701 | 0.29102 | 0.039660868 | 238.191 | -10.305 | 9.692 / -18.221 / -1.777 | 12.288 |
| N2s · bajas de inmovilizado 2023–25 (simétrica), tipo fijo | 0.2963 / 0.2754 / 0.256 | 0.2882 | 0.040424907 | 236.231 | -12.266 | 6.027 / -18.293 / 0.0 | 8.881 |
| N1 + N2 conjuntos · earnout no deducible; bajas de 2025 tipo fijo | 0.2619 / 0.2806 / 0.256 | 0.28236 | 0.043498096 | 225.162 | -23.335 | -8.714 / -18.3 / 3.679 | -8.712 |
| N1 + N2 conjuntos · earnout no deducible; bajas de 2025 gravadas al tipo teórico | 0.2619 / 0.2806 / 0.2558 | 0.28232 | 0.043506934 | 225.143 | -23.353 | -8.756 / -18.301 / 3.704 | -8.746 |
| N1 + N2 conjuntos · earnout no deducible; bajas de 2025 no gravadas | 0.2619 / 0.2806 / 0.27 | 0.28516 | 0.042879452 | 226.437 | -22.06 | -5.747 / -18.228 / 1.915 | -6.318 |
| Contraejemplo · regla literal «todo lo publicado como no recurrente» (nota 4.6 entera), tipo fijo | 0.2963 / 0.2754 / 0.256 | 0.2882 | 0.046322771 | 228.44 | -20.057 | -22.263 / 2.207 / 0.0 | -32.803 |

Diagnóstico conservado del contraste (no es un ajuste): earnout y otros no monetarios dentro de f (línea del EFE, tres años): 13.675; plusvalías netas de la ventana dentro de f (línea del EFE, tres años): -4.032; resultado por bajas de inmovilizado 2025 dentro de m0 (25,7 de la nota 4.6, al τ de 5 años): 18.293; suma (diagnóstico 27,936): 27.936.

## P2 · «PPA constante»

- PPA media 2023–25 ÷ ventas medias (lo que devuelve f en A2): 1.8743
- PPA 2025 ÷ ventas 2025 (lo que lleva m0): 1.7866
- diferencia aplicada a las ventas 2025 (mm): 4.206
- PPA 2025 (mm): 85.7
- PPA que f devuelve sobre las ventas 2025 (mm): 89.906
- sentido de la diferencia de la PPA: sube el flujo sin crecimiento de A2
- ROU media 2023–25 ÷ ventas medias (lo que devuelve f en A1 y A2): 2.9057
- ROU 2025 ÷ ventas 2025 (lo que lleva m0): 3.1167
- ROU que f devuelve sobre las ventas 2025 (mm): 139.382
- ROU 2025 (mm): 149.5
- diferencia de la ROU aplicada a las ventas 2025 (mm; baja el flujo sin crecimiento de A1 y A2): -10.118
- los dos efectos de escala juntos en A2 (mm): -5.913

## P4 · Arrendamientos

- pagos ÷ ventas, media de la ventana (%): 3.3589
- pagos ÷ ventas 2025 (%): 3.7087
- media escalada a las ventas 2025 (mm): 161.121763
- pagos 2025 (mm): 177.9
- sensibilidad del flujo sin crecimiento con el peso de 2025 (mm): -16.778237
- parte de los pagos (A0, A1 y A2; mm): -16.778237
- parte de la amortización ROU que devuelve f, con el peso de 2025 (solo A1 y A2; mm): 10.118279
- sensibilidad con el peso de 2025 en las dos cosas (A1 y A2; mm): -6.659958

## P4 · ROIC del terminal frente a S2C (palancas del libro)

| Escenario | g∞ | m_obj | S2C | ROIC | ROIC que reproduce S2C | S2C implícita | Inversión del terminal con ROIC | con S2C | Diferencia |
|---|---|---|---|---|---|---|---|---|---|
| MALO | 0.01 | 0.105 | 1.0 | 0.07 | 0.075486 | 0.927319 | 61.222 | 56.772 | 4.45 |
| NORMAL | 0.02 | 0.125 | 1.2 | 0.1 | 0.108905 | 1.101874 | 125.767 | 115.483 | 10.284 |
| BUENO | 0.025 | 0.135 | 1.5 | 0.12 | 0.147743 | 1.218332 | 154.244 | 125.281 | 28.964 |

## V6 · Bloque 10 del diagnóstico del libro (Convenciones V6.3 §3) frente a la igualdad exacta

| Escenario | Rentabilidad marginal del libro (fila 176) | ROIC (fila 177) | Salto del libro (fila 178 = marginal − ROIC), puntos | Salto con la igualdad exacta, puntos | Supera C179 (aviso y justificación G8) |
|---|---|---|---|---|---|
| MALO | 0.074739 | 0.07 | 0.474 | 0.549 | no |
| NORMAL | 0.10677 | 0.1 | 0.677 | 0.891 | no |
| BUENO | 0.14414 | 0.12 | 2.414 | 2.774 | no |

Umbral del aviso del libro: Umbral del aviso (puntos; ajustable) = 0.05.

## V3 y V4 · De qué depende la cifra de N1 (sensibilidades, no propuestas)

| Escenario | τ 2023 / 2024 / 2025 | τ de proyección | Variación del flujo sin crecimiento | Variación del año 11 MALO / NORMAL / BUENO |
|---|---|---|---|---|
| N1 + actualización del earnout fuera del BAI que da el tipo [cifras verificadas] | 0.2544 / 0.2772 / 0.2556 | 0.2801 | -12.396 | -16.91 / -20.27 / -21.668 |
| N1 + ajustes de earnout de 2021–22 fuera del BAI de su año, en el τ de cinco años [cifras verificadas] | 0.2619 / 0.2806 / 0.2559 | 0.28168 | -11.19 | -15.093 / -18.142 / -19.433 |
| N1 no deducible con el τ de proyección de la ventana (E8.1; convención no adoptada) | 0.2619 / 0.2806 / 0.2559 | 0.266133 | -9.141 | -13.417 / -15.848 / -16.759 |
| N1 con tipo fijo y el τ de proyección de la ventana (E8.1; convención no adoptada) | 0.2963 / 0.2754 / 0.256 | 0.2759 | -9.763 | -11.843 / -14.598 / -15.914 |

Cifras de earnout: 8 de las 14 lecturas de V3–V4 salen ya del CSV verificado (filas en el JSON). Las 6 restantes (columnas Lavartex y «otras adquisiciones») siguen [LECTURA]: son columnas por sociedad, no del grupo, y no intervienen en el cálculo. Reexpresión del ajuste de earnout de 2022: 2.1 en el URD 2022 y 2.4 en el URD 2023 (vigente).
Comprobación en el PDF (pdftotext, una página): 14 de 14 literales y 12 de 12 pasajes encontrados; huellas de los PDF: todas iguales a datos/fuentes.json.
