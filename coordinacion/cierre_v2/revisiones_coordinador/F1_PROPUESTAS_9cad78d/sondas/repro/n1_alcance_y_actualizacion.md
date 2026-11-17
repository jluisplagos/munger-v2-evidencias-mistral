# N1 · alcance en los ejercicios de τ y actualización del earnout de México (cálculo de apoyo)

Generado por `scripts/n1_alcance_y_actualizacion.py`. **No adopta nada: no es una entrada registrada ni una valoración.** Elis sigue en `pendiente_de_datos`. Mismas funciones que `contraste_f1.py`; los cálculos solo usan filas verificadas del CSV, salvo el escenario rotulado [LECTURA].

Controles: 107, fallidos: 0. [LECTURA]: 103 de 103 en su línea del PDF; pasajes: 19 de 19; búsquedas sin resultado confirmadas: 2 de 2; huellas de los PDF: todas iguales a las declaradas.

## A · Alcance de N1 (perímetro A0_total; la variación es la misma en A1_sin_ROU y A2_propio)

| Escenario | τ 2021 / 2022 / 2023 / 2024 / 2025 | τ de proyección | f (A0) | Flujo sin crecimiento | Frente al libro: flujo · año 11 M / N / B | Frente a N1 2023–25: flujo · año 11 M / N / B |
|---|---|---|---|---|---|---|
| Sin ajustes (libro) | 0.331 / 0.2823 / 0.2963 / 0.2754 / 0.256 | 0.2882 | 0.041681455 | 248.496 | 0.0 · 0.0 / 0.0 / 0.0 | 11.605 · 15.433 / 18.609 / 19.976 |
| C · N1 en 2023–25 (solo la ventana) | 0.331 / 0.2823 / 0.2619 / 0.2806 / 0.2559 | 0.28234 | 0.044900433 | 236.891 | -11.605 · -15.433 / -18.609 / -19.976 | 0.0 · 0.0 / 0.0 / 0.0 |
| B · N1 en 2022–25 (los ejercicios de τ con ajuste no deducible según lo publicado) | 0.331 / 0.2847 / 0.2619 / 0.2806 / 0.2559 | 0.28282 | 0.044900433 | 236.588 | -11.908 · -15.681 / -18.948 / -20.371 | -0.302 · -0.248 / -0.339 / -0.395 |
| A′ · N1 en 2021–25, con el ajuste de 2021 gravado al tipo teórico de 2021 [LECTURA: 28,41 %] | 0.3302 / 0.2847 / 0.2619 / 0.2806 / 0.2559 | 0.28266 | 0.044900433 | 236.689 | -11.807 · -15.599 / -18.835 / -20.24 | -0.202 · -0.165 / -0.226 / -0.264 |
| A · N1 en 2021–25, todos sin efecto fiscal (2021 por hipótesis) | 0.3253 / 0.2847 / 0.2619 / 0.2806 / 0.2559 | 0.28168 | 0.044900433 | 237.307 | -11.19 · -15.093 / -18.142 / -19.433 | 0.416 · 0.341 / 0.466 / 0.543 |
| descomposición · N1 en 2023–25 y 2021 sin efecto fiscal (sin 2022) | 0.3253 / 0.2823 / 0.2619 / 0.2806 / 0.2559 | 0.2812 | 0.044900433 | 237.609 | -10.887 · -14.845 / -17.803 / -19.037 | 0.718 · 0.588 / 0.806 / 0.939 |
| sensibilidad de B · en 2022 tributa la parte que la línea fiscal no cubre [LECTURA: 0,5] | 0.331 / 0.2843 / 0.2619 / 0.2806 / 0.2559 | 0.28274 | 0.044900433 | 236.639 | -11.858 · -15.64 / -18.891 / -20.305 | -0.252 · -0.206 / -0.283 / -0.329 |

### Línea fiscal publicada frente a (ajuste − actualización) × tipo teórico

| Año | Ajuste de earnout | Actualización | Tipo teórico | Solo el ajuste | Ajuste y actualización | Línea publicada | ¿Cuadra solo con el ajuste? | ¿Y con la actualización? |
|---|---|---|---|---|---|---|---|---|
| 2021 | -3.0 | 0.0 | 28.41 % | -0.852 | -0.852 | no hay línea | — | — |
| 2022 | 2.4 | 0.0 | 25.83 % | 0.62 | 0.62 | 0.5 | no | no |
| 2023 | -48.9 | 12.4 | 25.83 % | -12.631 | -15.834 | -15.8 | no | sí |
| 2024 | 8.7 | 5.6 | 25.83 % | 2.247 | 0.801 | 0.8 | no | sí |
| 2025 | -0.2 | 0.7 | 25.83 % | -0.052 | -0.232 | -0.2 | no | sí |

2022: con la cifra anterior a la reexpresión (2.1), 0.542: cuadra.

### Estado de flujos: línea que devuelve los ajustes de earnout (no monetarios)

| Año | Línea del estado de flujos | Ajuste de earnout con signo contrario | Diferencia (otros elementos sin efecto en caja) |
|---|---|---|---|
| 2021 | 2.9 | 3.0 | -0.1 |
| 2022 | -2.5 | -2.4 | -0.1 |
| 2023 | 48.4 | 48.9 | -0.5 |
| 2024 | -9.3 | -8.7 | -0.6 |
| 2025 | -0.1 | 0.2 | -0.3 |

### Pasivo y pagos de 2021–22 (la nota 2.4 de esos años no tiene fila propia de earnouts)

- pasivo_ligado_a_adquisiciones (valor razonable, nivel 3): cierre_2021: 27.1; cierre_2022 (URD 2022): 90.4; cierre_2022 (URD 2023, reexpresado): 90.5
- 2021 · Brasil: precio_de_las_compras_del_año: 1.4; pagado_en_el_año: 9.4; pagado_de_más_sobre_el_precio: 8.0
- 2021 · Rusia: precio_de_las_compras_del_año: 15.4; pagado_en_el_año: 5.7; pendiente_al_cierre: 9.7
- 2022 · Rusia (sin compra en 2022): pagado_en_el_año: 7.8
- nota: columnas por país: muestran que el importe pagado de la nota 2.4 incluye pagos de compras de años anteriores; no identifican earnouts

### Presentación neta de impuesto de 2021–2023 (medida alternativa de rendimiento)

- 2021 · costes de adquisición y ajustes de earnout: bruto: 5.1; neto_de_impuesto_publicado: 3.7; efecto_fiscal_implicito: 1.4; efecto_fiscal_implicito_pct: 27.5; tipo_teorico_pct: 28.41; neto_si_todo_lleva_el_tipo_teorico: 3.651; neto_si_el_ajuste_de_earnout_no_lleva_efecto_fiscal: 4.503; parte_del_ajuste_de_earnout_con_efecto_fiscal: 2.83; parte_minima_con_el_redondeo: 2.43; ajuste_de_earnout: 3.0; tipo_que_necesitarian_los_costes_de_transaccion_si_el_earnout_no_llevara_efecto_fiscal_pct: 66.7; ese_tipo_minimo_con_el_redondeo_pct: 60.5
- 2021 · reestructuración: bruto: 6.4; neto_de_impuesto_publicado: 4.8; efecto_fiscal_implicito_pct: 25.0; intervalo_con_el_redondeo_pct: [23.6, 26.4]; tipo_teorico_pct: 28.41
- 2020 · costes de adquisición y ajustes de earnout: bruto: 5.7; neto_de_impuesto_publicado: 4.6; efecto_fiscal_implicito_pct: 19.3; tipo_teorico_pct: 32.02
- 2021 · nota 4.6 entera: bruto: 16.1; neto_de_impuesto_publicado: 11.5; efecto_fiscal_implicito_pct: 28.6
- 2022 · nota 4.6 entera: bruto: 9.0; neto_de_impuesto_publicado: 7.0; efecto_fiscal_implicito_pct: 22.2
- 2023 · nota 4.6 entera: bruto: 67.9; neto_de_impuesto_publicado: 64.6; efecto_fiscal_implicito_pct: 4.9

### Límite declarado (no es una propuesta)

- partida: deterioro del fondo de comercio de 2022 (no deducible; línea fiscal propia)
- importe: 58.7
- linea_fiscal_publicada: -15.1
- importe_por_tipo_teorico: 15.162
- tau_2022_registrado: 0.2823
- tau_2022_sin_la_partida_en_el_BAI: 0.2337
- efecto_en_el_tau_de_cinco_años: -0.00972
- equivalente_en_el_flujo_sin_crecimiento: 6.126
- efecto_del_alcance_de_N1_en_el_tau_de_cinco_años (opción B: 2022–25): 0.00048
- efecto_del_alcance_de_N1_en_el_tau_de_cinco_años (opción A: 2021–25 sin efecto fiscal): -0.00066
- nota: N1 no la alcanza; (5a) aprobó que ninguna otra partida se normaliza. Solo mide que el τ de cinco años no queda «normalizado» por extender N1

## B · Actualización del earnout de México

| Escenario | τ 2021 / 2022 / 2023 / 2024 / 2025 | τ de proyección | f (A0) | Flujo sin crecimiento | Frente al libro: flujo · año 11 M / N / B | Frente a N1 2023–25: flujo · año 11 M / N / B |
|---|---|---|---|---|---|---|
| N1 en 2023–25, sin la actualización | 0.331 / 0.2823 / 0.2619 / 0.2806 / 0.2559 | 0.28234 | 0.044900433 | 236.891 | -11.605 · -15.433 / -18.609 / -19.976 | 0.0 · 0.0 / 0.0 / 0.0 |
| N1 en 2023–25, con la actualización fuera del BAI que da el tipo | 0.331 / 0.2823 / 0.2544 / 0.2772 / 0.2556 | 0.2801 | 0.045359475 | 236.101 | -12.396 · -16.91 / -20.27 / -21.668 | -0.79 · -1.476 / -1.661 / -1.692 |
| N1 en 2022–25 (opción B del alcance), sin la actualización | 0.331 / 0.2847 / 0.2619 / 0.2806 / 0.2559 | 0.28282 | 0.044900433 | 236.588 | -11.908 · -15.681 / -18.948 / -20.371 | -0.302 · -0.248 / -0.339 / -0.395 |
| N1 en 2022–25 (opción B del alcance), con la actualización fuera del BAI que da el tipo | 0.331 / 0.2847 / 0.2544 / 0.2772 / 0.2556 | 0.28058 | 0.045359475 | 235.798 | -12.698 · -17.157 / -20.609 / -22.064 | -1.093 · -1.724 / -2.0 / -2.088 |
| N1 en 2021–25 sin efecto fiscal (opción A del alcance), sin la actualización | 0.3253 / 0.2847 / 0.2619 / 0.2806 / 0.2559 | 0.28168 | 0.044900433 | 237.307 | -11.19 · -15.093 / -18.142 / -19.433 | 0.416 · 0.341 / 0.466 / 0.543 |
| N1 en 2021–25 sin efecto fiscal (opción A del alcance), con la actualización fuera del BAI que da el tipo | 0.3253 / 0.2847 / 0.2544 / 0.2772 / 0.2556 | 0.27944 | 0.045359475 | 236.517 | -11.98 · -16.569 / -19.803 / -21.125 | -0.374 · -1.136 / -1.195 / -1.149 |

### Mecanismo del efecto

- parte_de_f (el NOPAT de la ventana sube y f, que es un residuo, sube): -2.202
- parte_del_tau_de_cinco_años (el tipo proyectado baja): 1.412
- suma: -0.79
- con_el_tau_de_la_ventana (convención NO adoptada; E8.1 mantiene cinco años): flujo_sin_crecimiento: 0.151; año_11_NORMAL: -0.606
- nota: el signo y el tamaño salen de promediar el tipo en tres años dentro de f y en cinco en la proyección

### Conciliación del pasivo ligado a adquisiciones (valor razonable, nivel 3)

| Año y edición | Inicial | Altas | Revaluación | Actualización | Pagos | Calculado | Publicado | Residuo | Cota | Residuo sin la actualización |
|---|---|---|---|---|---|---|---|---|---|---|
| 2023 · con el cierre del URD 2023 | 90.5 | n. d. | 48.9 | 12.4 | -34.4 | 117.4 | 117.3 | -0.1 | 0.25 | 12.3 |
| 2023 · con el cierre reexpresado del DEU 2024 | 90.5 | n. d. | 48.9 | 12.4 | -34.4 | 117.4 | 118.2 | 0.8 | 0.25 | 13.2 |
| 2024 · con el DEU 2024 (precio provisional) | 118.2 | 1.5 | -8.7 | 5.6 | -93.9 | 22.7 | 23.5 | 0.8 | 0.35 | 6.4 |
| 2024 · con el URD 2025 (precio definitivo y cierre reexpresado) | 118.2 | 1.9 | -8.7 | 5.6 | -93.9 | 23.1 | 23.9 | 0.8 | 0.35 | 6.4 |
| 2025 · URD 2025 | 23.9 | 11.4 | 0.2 | 0.7 | -23.3 | 12.9 | 12.9 | 0.0 | 0.35 | 0.7 |

### Lavartex: del pendiente en la compra a los pagos (columnas por sociedad, [LECTURA])

- precio_de_adquisicion (valor razonable en la fecha de compra): 220.2
- pagado_en_2022: 148.0
- pendiente_en_la_compra (precio − pagado): 72.2
- pagos_2023_2024_2025: [31.4, 83.2, 19.7]
- pagos_2023_25: 134.3
- actualizacion_2023_25: 18.7
- revaluacion_neta_2023_25 (toda la nota 4.6; «principalmente» México): 40.4
- pendiente + revaluación + actualización: 131.3
- residuo_frente_a_los_pagos: 3.0
- residuo_si_se_quita_la_actualizacion: 21.7
- actualizacion_sobre_los_pagos_pct: 13.9
- nota: el residuo recoge la conversión, los ajustes de 2022 y la parte de los ajustes que no es de México; no se publica

### Conciliación publicada entre el resultado financiero y los intereses pagados (Release)

- 2024: partidas_de_caja (en los dos lados): -78.9; partidas_solo_de_resultados: -51.5; de_ellas_actualizacion_del_earnout_de_Mexico: -5.6; cargo_en_resultados_publicado: -130.4; suma: -130.4; salida_de_caja_publicada: -78.9; intereses_netos_pagados_del_EFE (fila verificada): -78.9
- 2025: partidas_de_caja (en los dos lados): -99.3; partidas_solo_de_resultados: -37.7; de_ellas_actualizacion_del_earnout_de_Mexico: -0.7; cargo_en_resultados_publicado: -137.1; suma: -137.0; salida_de_caja_publicada: -99.4; intereses_netos_pagados_del_EFE (fila verificada): -99.4

### Semestres

- actualizacion_S1_2024 [LECTURA, Release]: 7.8
- actualizacion_2024 (fila verificada): 5.6
- actualizacion_S2_2024 (derivada): -2.2
- actualizacion_S1_2025 [LECTURA, Release]: 0.7
- actualizacion_2025 (fila verificada): 0.7
- actualizacion_S2_2025 (derivada): 0.0
- actualizacion_S1_2026 [LECTURA, Release; impresa «-»]: 0.0

### Dónde está la actualización

- 2023: gastos_de_actualizacion_nota_8_2: 13.8; de_ellos_earnout_de_Mexico: 12.4; resto: 1.4; resultado_financiero_neto: -124.6; EBIT_de_la_Historia (BAI + financiero): 496.8
- 2024: gastos_de_actualizacion_nota_8_2: 8.8; de_ellos_earnout_de_Mexico: 5.6; resto: 3.2; resultado_financiero_neto: -130.4; EBIT_de_la_Historia (BAI + financiero): 596.3
- 2025: gastos_de_actualizacion_nota_8_2: 3.8; de_ellos_earnout_de_Mexico: 0.7; resto: 3.1; resultado_financiero_neto: -137.1; EBIT_de_la_Historia (BAI + financiero): 630.0
