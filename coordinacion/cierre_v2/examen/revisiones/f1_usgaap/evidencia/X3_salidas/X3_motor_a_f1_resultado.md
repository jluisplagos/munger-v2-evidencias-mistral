# Motor A · perímetro F1 · F1-IMPL 2 (4.15 · decisiones F1 del 17-nov-2026 · US GAAP, ASC 842: D-US1 y D-US2 del 18-nov-2026)

Libro `73a39a8f9db316aa…` · declaración `a81f51f2d2f2f12f…` · 2026-11-18

**motor A utilizable para una conclusión CONDICIONADA según F1 · hipótesis D-US1 (no es un dato): la empresa no publica en qué líneas del flujo van la amortización del derecho de uso ni la variación del pasivo del arrendamiento operativo; se suponen dentro del flujo de explotación, fuera de las filas 8 y 14 (condición necesaria, no suficiente; no apto para dinero real)**

Estado propuesto: — · apto para dinero real: no.

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
| F1-US-C49 | no | — | — | US GAAP · ASC 842 | C49 = 0.0 es el principal publicado de los arrendamientos financieros (0.0 de media en la ventana) |
| F1-US-DA | no | — | — | US GAAP · ASC 842 | la amortización del derecho de uso operativo no queda dentro de la reinversión |
| F1-US-SIM | no | — | — | simétrica · US GAAP · ASC 842 | la variación del pasivo operativo no queda sola dentro de la reinversión |
| F1-US-FILAS | sí | INFORMA | INFORMA | US GAAP · filas 8 y 14 del expediente | sin fase1_partes en el expediente: las ubicaciones declaradas de los tramos del arrendamiento operativo no se han podido contrastar con las líneas que la fase 1 sumó en las filas 8 y 14 |
| F1-2i | no | — | — | (2)(i) | el perímetro no trata la PPA como reposición |
| V-F1l | no | — | — | (5a) | sin ajustes de normalización (el diagnóstico se muestra como diagnóstico) |
| V-F1j | no | — | — | (4b) | compras: sin_compras |
| V-F1i | no | — | — | (5b) | sin transición conocida |
| V-F1d | no | — | — | (3a) | no aplica: el perímetro no es A3_estimado |
| V-F1c | no | — | — | (3a) | no aplica: el perímetro no es A3_estimado |
| V-F1h | no | — | — | (2) | margen EBIT_NIIF16_PPA_constante coherente con A2_propio |
| V-F1g | no | — | — | (4a) | palancas S2C en el mismo perímetro (A2_propio) |
| V-F1k | no | — | — | (4a) | ROIC del terminal en el perímetro de las palancas (A2_propio) |
| F1-REPLICA | no | — | — | T1/T7 | la réplica A0 reproduce el libro (f, τ, m0, ancla y flujos): la capa F1 y el libro son el mismo motor |
| F1-K3a | no | — | — | K3 | caja base por dos vías: cada diferencia entre C70 y la fila 35 está explicada por una partida declarada |
| F1-K3b | no | — | — | K3 | alquiler contado una vez (operativos) |
| F1-K3c | no | — | — | K3 | reinversión media 46.388 ≥ 0 (o ventas a la baja) |
| F1-LIBRO | no | — | — | (1a) · implantación | el libro V6.3.1 F1 calcula el perímetro declarado (A2_propio): f, ancla, D_X, series y 33 flujos del Motor coinciden con la capa |
| V-F1k (salto del terminal) | sí | AVISO | AVISO | (4a) | /salto/ > C179 en ['MALO', 'NORMAL', 'BUENO']: G8 (vigente) exige justificación en la tesis u Observación de B18:D18 |
| V-F1f | no | — | — | (2) | {"PPA: media ÷ ventas medias (lo que devuelve f en A2)": 0.0, "PPA: año base ÷ ventas del año base (lo que lleva m0)": 0.0, "efecto de escala de la PPA en el flujo sin crecimiento de A2 (mm)": 0.0, "ROU: media ÷ ventas medias (lo que devuelve f en A1 y A2)": 0.0, "ROU: año base ÷ ventas del año base (lo que lleva m0)": 0.0, "efecto de escala de la ROU en el flujo sin crecimiento de A1 y A2 (mm)": 0.0} |
| F1-US-BASE | sí | INFORMA | INFORMA | D-US2 | arrendamientos operativos: la proyección cuenta los PAGOS (D-US2); coste lineal medio 3.300, pagos medios 3.200: coste − pagos = +0.100 de media en la ventana (+0.108 a la escala del año base) |
| F1-US-HIPOTESIS | sí | AVISO | AVISO | D-US1 | hipótesis D-US1 (no es un dato): la empresa no publica en qué líneas del flujo van la amortización del derecho de uso ni la variación del pasivo del arrendamiento operativo; se suponen dentro del flujo de explotación, fuera de las filas 8 y 14. CONCLUSIÓN CONDICIONADA. Cota: si la variación del pasivo estuviera sola dentro de la fila 14 (el alquiler se omitiría): como máximo, los pagos: flujo sin crecimiento -3.449 mm (-2.3 %); si la amortización del derecho de uso estuviera dentro de la fila 8, o sola dentro de la fila 14 (se contaría dos veces): como máximo, el coste lineal: flujo sin crecimiento +3.557 mm (+2.4 %) · registro de la regla: 2026-11-18, munger-v2-evidencias-mistral, coordinacion/cierre_v2/DECISIONES_PARA_EL_USUARIO.md:96–98 |
| F1-US-PUENTE | sí | INFORMA | INFORMA | puente de deuda · US GAAP | la fila 23 lleva 50.0 de pasivo por arrendamiento operativo. El motor A no resta deuda, así que no afecta a su valor; sí entra en el capital invertido y en el ROIC histórico del libro (filas 32–33) y en Historia C64. Deuda coherente de un puente (motor B): 200.0 |
| F1-SERIES | no | — | — | (1a) · H12 · V631-2 | US GAAP · 2 clasificaciones con su cita en la página citada y 2 páginas examinadas sin línea propia (D-US1) · D&A de derechos de uso y PPA: cifra publicada con su signo, como cifra completa, en una página existente de una fuente del expediente con su huella; columna del ejercicio comprobada en 0 años, PENDIENTE en 17 (la aptitud por entradas sigue en «no») |

## Flujo sin crecimiento por perímetro (diagnóstico)

| Perímetro | f | Flujo sin crecimiento | Frente a A0 | Ancla S2C (E4) |
|---|---|---|---|---|
| A0_total | 0.001999980 | 148.000 | +0.000 | 1.481481 |
| A1_sin_ROU | 0.001999980 | 148.000 | +0.000 | 1.481481 |
| A2_propio | 0.001999980 | 148.000 | +0.000 | 1.481481 |
| B_cota_capex | 0.041999980 | 108.000 | -40.000 | 7.407407 |

## K3 · perímetro declarado (A2_propio)

| Partida | mm | Clase |
|---|---|---|
| FCF base que calibra f (Historia C70, entrada registrada) | 90.920 | caja |
| + nivel del EBIT del año base frente a la media de la ventana, al τ de proyección | 10.837 | explicada |
| + τ de proyección frente al τ de cada año de la ventana | 0.000 | explicada |
| − f aplicada a las ventas del año base en lugar de las medias | -0.144 | explicada |
| + inversión neta propia y circulante de la ventana (capex − D&A propia + circulante) | 46.388 | explicada |
| − amortización ROU que D_X devuelve como reposición, con los pagos de arrendamiento ya dentro del FCF base | 0.000 | explicada |
| − amortización PPA que D_X devuelve como reposición (no es caja: política (2)(i)) | 0.000 | explicada |
| **= flujo sin crecimiento** | **148.000** | cuadra |

## K3 · perímetro A0 (lo que calcula el libro)

| Partida | mm | Clase |
|---|---|---|
| FCF base que calibra f (Historia C70, entrada registrada) | 90.920 | caja |
| + nivel del EBIT del año base frente a la media de la ventana, al τ de proyección | 10.837 | explicada |
| + τ de proyección frente al τ de cada año de la ventana | 0.000 | explicada |
| − f aplicada a las ventas del año base en lugar de las medias | -0.144 | explicada |
| + inversión neta propia y circulante de la ventana (capex − D&A propia + circulante) | 46.388 | explicada |
| − amortización ROU que D_X devuelve como reposición, con los pagos de arrendamiento ya dentro del FCF base | 0.000 | explicada |
| − amortización PPA que D_X devuelve como reposición (no es caja: política (2)(i)) | 0.000 | explicada |
| **= flujo sin crecimiento** | **148.000** | cuadra |

Doble cómputo señalado por K3 en A0: 0.000 mm de media en la ventana; 0.000 a la escala del año base.

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
  "pagos_medios_de_la_ventana": 3.2,
  "coste_lineal_medio_de_la_ventana": 3.3,
  "amortizacion_dentro_de_la_fila_8_media": 0.0,
  "tramos_dentro_de_la_fila_14": [],
  "retirado_del_circulante_medio": null,
  "retirado_derivado_de_pagos_menos_coste_lineal_en": []
 },
 "financieros": {
  "existen": false,
  "principal_publicado_medio_de_la_ventana": 0.0,
  "amortizacion_dentro_de_la_fila_8_media": 0.0
 },
 "diferencia_coste_lineal_menos_pagos": {
  "coste_lineal_medio_de_la_ventana": 3.3,
  "pagos_medios_de_la_ventana": 3.2,
  "coste_menos_pagos_medio": 0.1,
  "coste_menos_pagos_a_la_escala_del_año_base": 0.107787,
  "coste_menos_pagos_del_año_base": 0.1,
  "nota": "D-US2: se cuentan los pagos. Si se contara el coste lineal, el flujo sin crecimiento cambiaría en −(coste − pagos) a la escala del año base"
 },
 "cota_D_US1": {
  "flujo_sin_crecimiento_con_la_hipotesis": 148.00002,
  "tramos_con_hipotesis": [
   "amortizacion_rou",
   "variacion_pasivo"
  ],
  "si la variación del pasivo estuviera sola dentro de la fila 14 (el alquiler se omitiría): como máximo, los pagos": {
   "variacion_maxima_de_f": 0.003449187,
   "variacion_maxima_del_flujo_sin_crecimiento_mm": -3.449187,
   "variacion_maxima_del_flujo_sin_crecimiento_%": -2.331,
   "por_escenario (valor presente de los flujos a la r del libro, sin exceso de caja ni quiebra)": {
    "MALO": {
     "variacion_maxima_del_valor_presente_de_los_flujos_mm": -50.749,
     "variacion_maxima_%": -2.79
    },
    "NORMAL": {
     "variacion_maxima_del_valor_presente_de_los_flujos_mm": -74.159,
     "variacion_maxima_%": -3.23
    },
    "BUENO": {
     "variacion_maxima_del_valor_presente_de_los_flujos_mm": -78.687,
     "variacion_maxima_%": -3.07
    }
   }
  },
  "si la amortización del derecho de uso estuviera dentro de la fila 8, o sola dentro de la fila 14 (se contaría dos veces): como máximo, el coste lineal": {
   "variacion_maxima_de_f": -0.003556974,
   "variacion_maxima_del_flujo_sin_crecimiento_mm": 3.556974,
   "variacion_maxima_del_flujo_sin_crecimiento_%": 2.403,
   "por_escenario (valor presente de los flujos a la r del libro, sin exceso de caja ni quiebra)": {
    "MALO": {
     "variacion_maxima_del_valor_presente_de_los_flujos_mm": 52.335,
     "variacion_maxima_%": 2.87
    },
    "NORMAL": {
     "variacion_maxima_del_valor_presente_de_los_flujos_mm": 76.477,
     "variacion_maxima_%": 3.33
    },
    "BUENO": {
     "variacion_maxima_del_valor_presente_de_los_flujos_mm": 81.146,
     "variacion_maxima_%": 3.16
    }
   }
  },
  "nota": "cotas, no estimaciones: la parte del pago que reduce el pasivo es menor que el pago y la amortización del derecho de uso es menor que el coste lineal; si los dos tramos estuvieran netos dentro de la fila 14, la variación sería solo −(pagos − coste lineal)"
 },
 "puente_de_deuda": {
  "ejercicio": 2025,
  "motor": "A",
  "deuda_financiera_fila_22": 200.0,
  "pasivo_por_arrendamientos_fila_23": 50.0,
  "pasivo_operativo_dentro_de_la_fila_23": 50.0,
  "deuda_del_puente_del_libro_C64": 250.0,
  "deuda_del_puente_coherente": 200.0,
  "exceso_que_restaria_el_motor_B": 50.0,
  "regla": "deuda del puente = deuda financiera + pasivo por arrendamientos financieros; el pasivo por arrendamiento operativo no entra: su pago ya está entero en el EBIT (una sola vez)"
 }
}
```

## Parámetros sin valor adoptado

- alcance_n1_ejercicios_tau: sin valor (N1_ALCANCE_EJERCICIOS_TAU.md (propuesta, no adoptada))
- n1_actualizacion_financiera_earnout: sin valor (N1_ACTUALIZACION_EARNOUT_MEXICO.md (propuesta, no adoptada))
- umbral_v_f1a: sin valor (PROPUESTA_UMBRAL_V-F1a.md (propuesta, no adoptada))
