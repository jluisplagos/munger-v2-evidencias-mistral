# Motor A · perímetro F1 · F1-IMPL 2 (4.15 · decisiones F1 del 17-nov-2026 · US GAAP, ASC 842: D-US1, D-US2, D-US2 bis y D-WM del 18-nov-2026 · cierre de la revisión R2 · margen de partida según Palancas C8, 19-nov-2026)

Libro `532504ee82b7c74a…` · declaración `d85c2ea4820fa304…` · 2026-11-19

**motor A utilizable para una conclusión CONDICIONADA según F1 · hipótesis D-US1 (no es un dato): la empresa no publica en qué líneas del flujo van la amortización del derecho de uso ni la variación del pasivo del arrendamiento operativo; se suponen dentro del flujo de explotación, fuera de las filas 8 y 14 · cota: el flujo sin crecimiento podría cambiar entre -64.231 y +63.537 mm (-2.6 % y +2.6 %); el valor presente de los flujos en el escenario NORMAL, entre -3.1 % y +3.1 % (condición necesaria, no suficiente; no apto para dinero real)**

Estado propuesto: — · apto para dinero real: no.

## Conclusión condicionada

- **D-US1** (hipótesis general declarada): hipótesis D-US1 (no es un dato): la empresa no publica en qué líneas del flujo van la amortización del derecho de uso ni la variación del pasivo del arrendamiento operativo; se suponen dentro del flujo de explotación, fuera de las filas 8 y 14

cota: el flujo sin crecimiento podría cambiar entre -64.231 y +63.537 mm (-2.6 % y +2.6 %); el valor presente de los flujos en el escenario NORMAL, entre -3.1 % y +3.1 %

## Guardas

| Id | Salta | Severidad | Efecto | Decisión | Detalle |
|---|---|---|---|---|---|
| F1-NORMA | no | — | — | generalidad | US GAAP declarada; libro: US GAAP |
| V-F1e | no | — | — | (1a) | invariantes de E1 y signos declarados: conformes |
| V-F1b | no | — | — | (1a) | D&A ROU declarada en la ventana o C49 = 0 |
| V-F1a | no | — | — | (1a) | no aplica: el perímetro no es A0 |
| V-F1m | no | — | — | (1a) | no aplica: el perímetro no es A0 |
| F1-M-SIM | no | — | — | (1a) · simétrica de V-F1m | no salta |
| F1-ROU-HISTORIA | no | — | — | (1a) | sin conflicto entre la ROU declarada y las filas 17 y 23 de la Historia |
| F1-US-MEZCLA | no | — | — | US GAAP · ASC 842 | sin partidas propias de NIIF en un libro US GAAP (C48 y fila 16 a cero) |
| F1-US-DESGLOSE | no | — | — | US GAAP · ASC 842 | arrendamientos operativos y financieros declarados por separado, con sus series · hipótesis D-US1 en amortizacion_rou, variacion_pasivo |
| F1-US-C49 | no | — | — | US GAAP · ASC 842 | C49 = 1.0 es el principal publicado de los arrendamientos financieros (1.0 de media en la ventana; redondeo de C49 ±0.5) |
| F1-US-DA | no | — | — | US GAAP · ASC 842 | la amortización del derecho de uso operativo no queda dentro de la reinversión |
| F1-US-SIM | no | — | — | simétrica · US GAAP · ASC 842 | la variación del pasivo operativo no queda sola dentro de la reinversión |
| F1-US-FILAS | no | — | — | US GAAP · ubicaciones frente a las líneas del expediente (D-US1: manda el dato) | la amortización del derecho de uso: no publicada (hipótesis D-US1) · hipotesis D US1; la variación del pasivo: no publicada (hipótesis D-US1) · hipotesis D US1; la amortización del derecho de uso de los arrendamientos financieros: dentro de la fila 8 · por omision · lo declarado no contradice las líneas que la fase 1 sumó en las filas 8 y 14 en los años que usa el modelo (2021–2025; informes 2016–2025) |
| F1-2i | no | — | — | (2)(i) | el perímetro no trata la PPA como reposición |
| V-F1l | no | — | — | (5a) | sin ajustes de normalización (el diagnóstico se muestra como diagnóstico) |
| V-F1j | no | — | — | (4b) | compras: crecimiento_por_hipotesis |
| V-F1i | no | — | — | (5b) | sin transición conocida |
| V-F1d | no | — | — | (3a) | no aplica: el perímetro no es A3_estimado |
| V-F1c | no | — | — | (3a) | no aplica: el perímetro no es A3_estimado |
| V-F1h | no | — | — | (2) | margen EBIT_NIIF16_PPA_constante coherente con A2_propio |
| V-F1g | no | — | — | (4a) | perímetro declarado de las palancas S2C = perímetro de la reinversión (A2_propio): compara etiquetas de la declaración, no cifras; los valores, en «V-F1g (valores)» (P-FOSO, D3) |
| V-F1k | no | — | — | (4a) | perímetro declarado del ROIC del terminal = el de las palancas S2C (A2_propio): compara etiquetas de la declaración, no cifras; los valores, en «V-F1k (valores)» (P-FOSO, D3) |
| F1-REPLICA | no | — | — | T1/T7 | la réplica A0 reproduce el libro (f, τ, m0 = Historia!C49, ancla y flujos): la capa F1 y el libro son el mismo motor |
| F1-K3a | no | — | — | K3 | caja base por dos vías: cada diferencia entre C70 y la fila 35 está explicada por una partida declarada |
| F1-K3b | no | — | — | K3 | alquiler contado una vez (operativos, financieros) · según la hipótesis D-US1 (no es un dato ni una comprobación independiente) |
| F1-K3c | no | — | — | K3 | reinversión media 599.333 ≥ 0 (o ventas a la baja) |
| F1-LIBRO | no | — | — | (1a) · implantación | el libro V6.3.1 F1 calcula el perímetro declarado (A2_propio): f, ancla, D_X, series y 33 flujos del Motor coinciden con la capa |
| V-F1k (salto del terminal) | sí | AVISO | AVISO | (4a) | /salto/ > C179 en ['MALO', 'NORMAL', 'BUENO']: G8 (vigente) exige justificación en la tesis u Observación de B18:D18 |
| V-F1g (valores) | no | — | — | (4a) · P-FOSO | perímetro A2_propio declarado; medidas del perímetro no aplicables: norma contable 'US_GAAP': la medida solo tiene fórmula con NIIF (NIIF 16). Con US GAAP el arrendamiento operativo va entero en el EBIT y restarle su interés lo contaría dos veces; no se emite hasta que tenga su fórmula. G7 y las referencias usan C55, de todo el capital, como antes |
| V-F1k (valores) | no | — | — | (4a) · P-FOSO | perímetro A2_propio declarado; medidas del perímetro no aplicables: norma contable 'US_GAAP': la medida solo tiene fórmula con NIIF (NIIF 16). Con US GAAP el arrendamiento operativo va entero en el EBIT y restarle su interés lo contaría dos veces; no se emite hasta que tenga su fórmula. G7 y las referencias usan C55, de todo el capital, como antes |
| V-F1f | sí | INFORMA | INFORMA | (2) | {"PPA: media ÷ ventas medias (lo que devuelve f en A2)": 0.01544, "PPA: lo que lleva m0": "no calculable con la base del margen «Media del ciclo» (Palancas C8): la serie no cubre todos los años con ventas", "ROU: media ÷ ventas medias (lo que devuelve f en A1 y A2)": 0.00011, "ROU: lo que lleva m0": "no calculable con la base del margen «Media del ciclo» (Palancas C8): la serie no cubre todos los años con ventas"} |
| F1-US-BASE | sí | INFORMA | INFORMA | D-US2 | arrendamientos operativos: la proyección cuenta los PAGOS (D-US2); coste lineal medio 61.000, pagos medios 61.667: coste − pagos = -0.667 de media en la ventana (-0.694 a la escala del año base) |
| F1-US-HIPOTESIS | sí | AVISO | AVISO | D-US1 · D-WM · R1-3 | hipótesis D-US1 (no es un dato): la empresa no publica en qué líneas del flujo van la amortización del derecho de uso ni la variación del pasivo del arrendamiento operativo; se suponen dentro del flujo de explotación, fuera de las filas 8 y 14. CONCLUSIÓN CONDICIONADA. Cota: si la variación del pasivo estuviera sola dentro de la fila 14 (el alquiler se omitiría): como máximo, los pagos: flujo sin crecimiento -64.231 mm (-2.6 %); si la amortización del derecho de uso estuviera dentro de la fila 8, o sola dentro de la fila 14 (se contaría dos veces): como máximo, el coste lineal: flujo sin crecimiento +63.537 mm (+2.6 %) · registro de las reglas: D-US1: 2026-11-18, munger-v2-evidencias-mistral, coordinacion/cierre_v2/DECISIONES_PARA_EL_USUARIO.md:96–98 |
| F1-US-PUENTE | no | — | — | puente de deuda · US GAAP | la fila 23 no lleva pasivo por arrendamiento operativo: la deuda del puente es la del libro |
| F1-SERIES-CERO | sí | AVISO | PENDIENTE | (1a) · F1-SERIES-ESCALA | CERO SIN CIFRA IMPRESA, PENDIENTE DE REVISOR (no comprobado: el programa solo ha visto que la frase está en la página; no bloquea F1-SERIES y la aptitud por entradas sigue en «no»): series.da_rou.2021: motivo «Sin arrendamientos financieros en 2021: «Our current portfolio includes only operating leases»; la amortización del derecho de uso de los operativos no está dentro de la fila 8 (D-US1). Cero por lectura, PENDIENTE DE REVISOR»; cita (p. 78 de 'Zoetis · Form 10-K FY2021') «Our current portfolio includes only operating leases which are recorded as a right of use» · series.da_rou.2022: motivo «Sin arrendamientos financieros en 2022: «Our current portfolio includes only operating leases»; la amortización del derecho de uso de los operativos no está dentro de la fila 8 (D-US1). Cero por lectura, PENDIENTE DE REVISOR»; cita (p. 70 de 'Zoetis · Form 10-K FY2022') «Our current portfolio includes only operating leases which are recorded as a right of use» · series.pasivo_arr_operativo.2025: motivo «Pasivo por arrendamiento OPERATIVO dentro de la fila 23 de la Historia en 2025 = 0: la fila 23 lleva solo el pasivo por arrendamientos financieros (1 + 6 = 7, PDF p. 89) por la corrección registrada de fase1_partes (resultados/correccion_fase1_partes.json); el pasivo operativo publicado (52 + 196 = »; cita (p. 89 de 'Zoetis · Form 10-K FY2025') «Supplemental information for our lease portfolio is as follows:» |
| F1-SERIES | no | — | — | (1a) · H12 · V631-2 | US GAAP · 2 clasificaciones con su cita en la página citada y 2 páginas examinadas sin línea propia (D-US1) · D&A de derechos de uso y PPA: cifra publicada con su signo, como cifra completa, en una página existente de una fuente del expediente con su huella; columna del ejercicio comprobada en 0 años, PENDIENTE en 20 (la aptitud por entradas sigue en «no») |

## Flujo sin crecimiento por perímetro (diagnóstico)

| Perímetro | f | Flujo sin crecimiento | Frente a A0 | Ancla S2C (E4) |
|---|---|---|---|---|
| A0_total | 0.025645344 | 2337.420 | +0.000 | 1.036377 |
| A1_sin_ROU | 0.025535321 | 2338.462 | +1.042 | 1.035224 |
| A2_propio | 0.010095412 | 2484.631 | +147.211 | 0.808572 |
| B_cota_capex | 0.045192782 | 2152.365 | -185.056 | 1.388364 |

## K3 · perímetro declarado (A2_propio)

| Partida | mm | Clase |
|---|---|---|
| FCF base que calibra f (Historia C70, entrada registrada) | 1994.001 | caja |
| + nivel del EBIT de partida (margen medio del ciclo, Historia C49, × ventas del año base; Palancas C8 «Media del ciclo») frente a la media de la ventana, al τ de proyección | -118.140 | explicada |
| + τ de proyección frente al τ de cada año de la ventana | 13.253 | explicada |
| − f aplicada a las ventas del año base en lugar de las medias | -3.816 | explicada |
| + inversión neta propia y circulante de la ventana (capex − D&A propia + circulante) | 599.333 | explicada |
| − amortización ROU que D_X devuelve como reposición, con los pagos de arrendamiento ya dentro del FCF base | 0.000 | explicada |
| − amortización PPA que D_X devuelve como reposición (no es caja: política (2)(i)) | 0.000 | explicada |
| **= flujo sin crecimiento** | **2484.631** | cuadra |

## K3 · perímetro A0 (lo que calcula el libro)

| Partida | mm | Clase |
|---|---|---|
| FCF base que calibra f (Historia C70, entrada registrada) | 1994.001 | caja |
| + nivel del EBIT de partida (margen medio del ciclo, Historia C49, × ventas del año base; Palancas C8 «Media del ciclo») frente a la media de la ventana, al τ de proyección | -118.140 | explicada |
| + τ de proyección frente al τ de cada año de la ventana | 13.253 | explicada |
| − f aplicada a las ventas del año base en lugar de las medias | -9.694 | explicada |
| + inversión neta propia y circulante de la ventana (capex − D&A propia + circulante) | 599.333 | explicada |
| − amortización ROU que D_X devuelve como reposición, con los pagos de arrendamiento ya dentro del FCF base | -1.000 | doble_computo |
| − amortización PPA que D_X devuelve como reposición (no es caja: política (2)(i)) | -140.333 | reposicion_no_monetaria |
| **= flujo sin crecimiento** | **2337.420** | cuadra |

Doble cómputo señalado por K3 en A0: 141.333 mm de media en la ventana; 147.211 a la escala del año base.

## US GAAP (ASC 842) · arrendamientos operativos y financieros por separado

```
{
 "decisiones": {
  "D-US1": {
   "regla": "si la empresa no publica en qué líneas del estado de flujos van los dos tramos del arrendamiento operativo (la amortización del derecho de uso y la variación del pasivo), se supone que van netos dentro del flujo de explotación, fuera de las filas 8 (D&A) y 14 (circulante) de la Historia: hipótesis declarada, no dato; la conclusión se presenta como condicionada, con su cota de sensibilidad. Donde la empresa publica las líneas, manda el dato",
   "registro": {
    "fecha": "2026-11-18",
    "persona": "persona responsable del proyecto (decisión registrada; no se firma aquí)",
    "motivo": "munger-v2-evidencias-mistral, coordinacion/cierre_v2/DECISIONES_PARA_EL_USUARIO.md:96–98"
   }
  },
  "D-US2": {
   "regla": "cuando el coste lineal del arrendamiento operativo y los pagos del año difieren, se cuentan los pagos y la diferencia queda a la vista, sin bloquear",
   "registro": {
    "fecha": "2026-11-18",
    "persona": "persona responsable del proyecto (decisión registrada; no se firma aquí)",
    "motivo": "munger-v2-evidencias-mistral, coordinacion/cierre_v2/DECISIONES_PARA_EL_USUARIO.md:96–98"
   }
  },
  "D-US2 bis": {
   "regla": "con el alquiler operativo mezclado en las líneas de otros activos y otros pasivos (los dos tramos dentro de la fila 14) no se bloquea: se publica el valor de la hoja, que cuenta el coste contable, y al lado cuánto cambiaría contando los pagos; antes, el programa comprueba que el expediente muestra las dos líneas (la del activo y la del pasivo)",
   "registro": {
    "fecha": "2026-11-18",
    "persona": "persona responsable del proyecto (decisión registrada; no se firma aquí)",
    "motivo": "munger-v2-evidencias-mistral, coordinacion/cierre_v2/DECISIONES_PARA_EL_USUARIO.md:112–114 (tras la revisión R1 de F1 con US GAAP)"
   }
  },
  "D-WM": {
   "regla": "los arrendamientos financieros que la empresa no desglosa se tratan como deuda y activos propios (hipótesis declarada): su amortización queda dentro de la propia y sus pagos no se restan de la caja base; la diferencia estimada (caja pagada − gasto total) se enseña junto al resultado",
   "registro": {
    "fecha": "2026-11-18",
    "persona": "persona responsable del proyecto (decisión registrada; no se firma aquí)",
    "motivo": "munger-v2-evidencias-mistral, coordinacion/cierre_v2/DECISIONES_PARA_EL_USUARIO.md:112–114 (tras la revisión R1 de F1 con US GAAP)"
   }
  }
 },
 "base_del_arrendamiento_operativo": "pagos (D-US2)",
 "operativos": {
  "existen": true,
  "ubicacion_de_la_amortizacion_del_derecho_de_uso": "fuera_de_las_filas_8_y_14",
  "ubicacion_de_la_variacion_del_pasivo": "fuera_de_las_filas_8_y_14",
  "hipotesis_D_US1_en": [
   "amortizacion_rou",
   "variacion_pasivo"
  ],
  "pagos_medios_de_la_ventana": 61.666667,
  "coste_lineal_medio_de_la_ventana": 61.0,
  "coste_comparable_con_los_pagos": true,
  "amortizacion_dentro_de_la_fila_8_media": 0.0,
  "tramos_dentro_de_la_fila_14": [],
  "retirado_del_circulante_medio": null
 },
 "financieros": {
  "existen": true,
  "tratados_como_deuda_D_WM": false,
  "ubicacion_de_la_amortizacion_del_derecho_de_uso": "fila_8",
  "principal_publicado_medio_de_la_ventana": 1.0,
  "amortizacion_dentro_de_la_fila_8_media": 1.0
 },
 "diferencia_coste_lineal_menos_pagos": {
  "coste_lineal_medio_de_la_ventana": 61.0,
  "pagos_medios_de_la_ventana": 61.666667,
  "coste_menos_pagos_medio": -0.666667,
  "coste_menos_pagos_a_la_escala_del_año_base": -0.694392,
  "coste_menos_pagos_del_año_base": 1.0,
  "coste_entre_pagos": 0.9892,
  "nota": "D-US2: se cuentan los pagos. Si se contara el coste lineal, el flujo sin crecimiento cambiaría en −(coste − pagos) a la escala del año base. El coste declarado es el de los contratos capitalizados (sin corto plazo ni variable): si la diferencia no es de calendario sino de perímetro, se declara «coste_comparable_con_los_pagos»: false"
 },
 "D_US2_bis": null,
 "D_WM": null,
 "cota_D_US1": {
  "flujo_sin_crecimiento_con_la_hipotesis": 2484.631379,
  "tramos_con_hipotesis": [
   "amortizacion_rou",
   "variacion_pasivo"
  ],
  "si la variación del pasivo estuviera sola dentro de la fila 14 (el alquiler se omitiría): como máximo, los pagos": {
   "variacion_maxima_de_f": 0.006784758,
   "variacion_maxima_del_flujo_sin_crecimiento_mm": -64.231305,
   "variacion_maxima_del_flujo_sin_crecimiento_%": -2.585,
   "por_escenario (valor presente de los flujos a la r del libro, sin exceso de caja ni quiebra)": {
    "MALO": {
     "variacion_maxima_del_valor_presente_de_los_flujos_mm": -767.244,
     "variacion_maxima_%": -2.91
    },
    "NORMAL": {
     "variacion_maxima_del_valor_presente_de_los_flujos_mm": -1072.012,
     "variacion_maxima_%": -3.13
    },
    "BUENO": {
     "variacion_maxima_del_valor_presente_de_los_flujos_mm": -1384.842,
     "variacion_maxima_%": -3.08
    }
   }
  },
  "si la amortización del derecho de uso estuviera dentro de la fila 8, o sola dentro de la fila 14 (se contaría dos veces): como máximo, el coste lineal": {
   "variacion_maxima_de_f": -0.006711409,
   "variacion_maxima_del_flujo_sin_crecimiento_mm": 63.536913,
   "variacion_maxima_del_flujo_sin_crecimiento_%": 2.557,
   "por_escenario (valor presente de los flujos a la r del libro, sin exceso de caja ni quiebra)": {
    "MALO": {
     "variacion_maxima_del_valor_presente_de_los_flujos_mm": 758.95,
     "variacion_maxima_%": 2.88
    },
    "NORMAL": {
     "variacion_maxima_del_valor_presente_de_los_flujos_mm": 1060.423,
     "variacion_maxima_%": 3.1
    },
    "BUENO": {
     "variacion_maxima_del_valor_presente_de_los_flujos_mm": 1369.87,
     "variacion_maxima_%": 3.04
    }
   }
  },
  "nota": "cotas, no estimaciones (salvo la de D-WM): la parte del pago que reduce el pasivo es menor que el pago y la amortización del derecho de uso es menor que el coste lineal; si los dos tramos estuvieran netos dentro de la fila 14, la variación sería solo −(pagos − coste lineal)",
  "resumen": {
   "flujo_sin_crecimiento_mm": [
    -64.231305,
    63.536913
   ],
   "flujo_sin_crecimiento_%": [
    -2.585,
    2.557
   ],
   "valor_presente_NORMAL_%": [
    -3.13,
    3.1
   ],
   "texto": "cota: el flujo sin crecimiento podría cambiar entre -64.231 y +63.537 mm (-2.6 % y +2.6 %); el valor presente de los flujos en el escenario NORMAL, entre -3.1 % y +3.1 %"
  }
 },
 "contraste_de_ubicaciones": {
  "tramos": {
   "amortizacion_rou": {
    "ubicacion_declarada": "no_publicada",
    "estado": "hipotesis_D_US1",
    "motivo": "la empresa no publica la línea: hipótesis general declarada (no es un dato)"
   },
   "variacion_pasivo": {
    "ubicacion_declarada": "no_publicada",
    "estado": "hipotesis_D_US1",
    "motivo": "la empresa no publica la línea: hipótesis general declarada (no es un dato)"
   },
   "amortizacion_rou_financiero": {
    "ubicacion_declarada": "fila_8",
    "estado": "por_omision",
    "motivo": "dentro de la fila 8 por omisión (como NIIF 16): ninguna línea sumada en la fila 8 la nombra en [2021, 2022, 2023, 2024, 2025]; no se ha contrastado con una línea (el importe es el declarado en series.da_rou)"
   }
  },
  "fundamento": "hipótesis",
  "fase1_partes": {
   "informes": [
    2016,
    2017,
    2018,
    2019,
    2020,
    2021,
    2022,
    2023,
    2024,
    2025
   ],
   "sin_examinar": [],
   "ilegibles": [],
   "sha256": "e327a9f6163ad32ed68b387695b6919f2264b8e26bd8b4e78aeb7243c5bdff18"
  },
  "sin_contrastar": {},
  "importe_sin_contrastar": [],
  "lineas_ajenas_al_tramo": []
 },
 "puente_de_deuda": {
  "ejercicio": 2025,
  "motor": "A",
  "deuda_financiera_fila_22": 9042.0,
  "pasivo_por_arrendamientos_fila_23": 7.0,
  "pasivo_operativo_dentro_de_la_fila_23": 0.0,
  "deuda_del_puente_del_libro_C64": 9049.0,
  "deuda_del_puente_coherente": 9049.0,
  "exceso_que_restaria_el_motor_B": 0.0,
  "lineas_de_arrendamiento_operativo_sumadas_en_la_fila_23": [],
  "regla": "deuda del puente = deuda financiera + pasivo por arrendamientos financieros; el pasivo por arrendamiento operativo no entra: su pago ya está entero en el EBIT (una sola vez)"
 }
}
```

## Parámetros sin valor adoptado

- alcance_n1_ejercicios_tau: sin valor (N1_ALCANCE_EJERCICIOS_TAU.md (propuesta, no adoptada))
- n1_actualizacion_financiera_earnout: sin valor (N1_ACTUALIZACION_EARNOUT_MEXICO.md (propuesta, no adoptada))
- umbral_v_f1a: sin valor (PROPUESTA_UMBRAL_V-F1a.md (propuesta, no adoptada))
