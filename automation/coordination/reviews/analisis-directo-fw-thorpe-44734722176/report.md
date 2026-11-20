# Análisis directo · FW_Thorpe, etapa 1 del universo (hoja del 2026-10-30)

Estado de la ejecución: `AUDITORIA_DOCUMENTAL_PENDIENTE_ACEPTACION`

Revisión a ciegas pendiente. No es aceptación, ni integración, ni aptitud para dinero real.

| Campo | Valor |
|---|---|
| Empresa | fw-thorpe |
| Fecha de corte | 2026-10-30 |
| Tasa | 9 % |
| Tarea | analisis-directo-fw-thorpe-44734722176 |
| SHA del código | 779b55abd380e8427650233fcb8a9c9fa74472f4 |
| Huella del paquete (package_sha256) | acd5f8ad4150d59d56e50cc1d121877de2ed5a07056a6f8b83c3d172aa76e5ee |
| Huella del envío (bundle_sha256) | 0beb9338ea5ccbe3a057ade7d1f77e711a2aa46fcf950573c7dff90caf4e7fbe |
| Huella del encargo | 022846e95b809a772317c2b17d6d946f3f91b9066c864911e473bb7ea15843e4 |
| Modelo pedido / devuelto | claude-opus-5-5 / claude-opus-5-5 |
| Esfuerzo | high |
| Mensajes enviados | 1 |
| Cota de entrada estimada antes de llamar | 140370 tokens |
| Reserva estimada antes de llamar | USD 1.21684 (máximo de la ejecución USD 3) |
| Reserva registrada | USD 1.21684 |
| Uso de tokens | entrada 63468, salida 19915 |
| Coste | CONOCIDO_ESTIMADO; estimado USD 0.652172; cota 0.652172 |

## Paquete de entrada

| id | ruta | commit | sha256 | bytes |
|---|---|---|---|---|
| respuesta | datos_analisis_directo/fw-thorpe/etapa1/FW_Thorpe_respuesta.md | 779b55abd380 | 2119beb5ea011fb4d57e4bd1416387c8ca225af3e86f92d8a112064a61a16857 | 31373 |
| hoja_analisis | datos_analisis_directo/fw-thorpe/etapa1/FW_Thorpe_evaluada__Análisis.csv | 779b55abd380 | 2055f34b6765a230e8793d1f33133ec1b1adfefbef4fb9cc754777350ca08df8 | 23638 |
| hoja_guia_simply_wall_st | datos_analisis_directo/fw-thorpe/etapa1/FW_Thorpe_evaluada__Guía_Simply_Wall_St.csv | 779b55abd380 | 2791cc208d21b779b2104db9848a271eded2ae7cb4392769b743a2d95f8c3e2f | 7794 |
| hoja_opciones | datos_analisis_directo/fw-thorpe/etapa1/FW_Thorpe_evaluada__Opciones.csv | 779b55abd380 | b9f97b6706b77f7a28f70140d212f0790ee7334eb22965a4f538963e777a1a73 | 1537 |
| hoja_control_maestro | datos_analisis_directo/fw-thorpe/etapa1/FW_Thorpe_evaluada__Control_maestro.csv | 779b55abd380 | 1f642ab6af976ddf890540ee2d83c3feb834dd34c077a790b1c817c784103afc | 54017 |

## Salida del modelo (datos, sin acciones ejecutables)

Estado `concluido` · cubo «Sí» · acción `comprar` · zona `cumple_regla_k`

| Escenario | Valor por acción | Probabilidad |
|---|---|---|
| malo | 2.3678 | 0.2 |
| normal | 3.5892 | 0.6 |
| bueno | 5.4089 | 0.2 |

| Escalera (k = 3) | Declarado | Recalculado (Anexo C) |
|---|---|---|
| Precio actual | 2.56 | |
| Precio del escenario malo | 2.3678 | 2.3678 |
| P* | 3.3257 | 3.3257 |
| Precio de Sí = mín(P*, V_normal) | 3.3257 | 3.3257 |
| Ponderado | 3.7089 | 3.7089 |
| Crecimiento implícito al precio actual / del normal (%) | -4.9 / 3 | |

| Tasa | Precio de Sí | Ponderado | Zona |
|---|---|---|---|
| 7 % | 4.6051 | 5.2189 | bajo_malo |
| 8 % | 3.8593 | 4.3351 | bajo_malo |
| 9 % | 3.3257 | 3.7089 | cumple_regla_k |
| 10 % | 2.9248 | 3.242 | cumple_regla_k |
| 11 % | 2.6126 | 2.8806 | cumple_regla_k |

### Resumen

    FW Thorpe diseña y fabrica luminarias profesionales. El 45 % de sus ventas es alumbrado de emergencia. No tiene deuda relevante y tiene caja neta. Su margen operativo lleva una década casi siempre en el 17–19 %, aunque las ventas caen ligeramente desde hace tres ejercicios. He rehecho el DCF del paquete al 9 % con estos datos: FCF base de 25,333 £mm (media FY24–26), 114,109 mm de acciones diluidas, 12 £mm de exceso de caja y escenarios de −2 %, 3 % y 8 % de crecimiento del FCF a diez años. Los valores por acción salen en 2,37 £ (malo), 3,59 £ (normal) y 5,41 £ (bueno), con un ponderado de 3,71 £. Con la regla k = 3, el precio de Sí sale en 3,33 £, y el precio de 2,56 £ (cierre del 29-oct-2026) queda en la zona que cumple la regla. El resultado aguanta tasas del 7 al 11 %, la ventana de FCF a cinco años y probabilidades más pesimistas. El precio descuenta una caída de las ventas de ≈4,9 % anual durante cinco años. Conclusión: Sí, comprar, condicionado a confirmar el precio y la tesis de márgenes.


### Moneda

    GBP


### Justificación

    Estado concluido: el DCF simplificado es aplicable (industrial con caja neta, FCF positivo y financiación estable) y los datos materiales están en el paquete. Cubo Sí y acción comprar: a 2,56 £ el precio está por debajo del precio de Sí (3,33 £) y solo un 8 % por encima del escenario malo. Además, la conclusión aguanta varias pruebas: tasas del 7 al 11 %; la ventana de FCF a cinco años (FCF 21,59 £mm, precio de Sí ≈2,85 £); un escenario malo del −5 % (P* ≈3,14 £); y probabilidades de 0,3/0,5/0,2 (P* ≈3,13 £). El precio descuenta una caída de las ventas de ≈4,9 % anual durante cinco años, peor que los tres años recientes (−0,5/−0,3/−1,3 %). Discrepo de la etapa 1, que fijaba el precio de Sí en el escenario malo: la regla k = 3 lo sitúa en 3,33 £. Riesgos asumidos: falta de poder de precio, filiales compradas débiles, gobierno familiar y préstamos a partes vinculadas.


### Probabilidades

    Mantengo 0,2/0,6/0,2. El riesgo de márgenes y de filiales ya está dentro del escenario malo, y el normal (3 %) es prudente. Prueba de robustez: con 0,3/0,5/0,2 el P* bajaría a ≈3,13 £, todavía por encima de 2,56 £.


### Fórmula aplicada

    Para P entre V_malo y V_normal: G(P) = 0,6·(3,5892−P) + 0,2·(5,4089−P) = 3,2353 − 0,8P; L(P) = 0,2·(P−2,3678). Con G = 3L: 3,2353 − 0,8P = 0,6P − 1,4207, luego P* = 4,6560 / 1,4 = 3,3257, que es ≤ V_normal (3,5892). Precio de Sí = mín(3,3257; 3,5892) = 3,3257. Ponderado = 0,2·2,3678 + 0,6·3,5892 + 0,2·5,4089 = 3,7089. Precio 2,56 > 2,3678 y ≤ 3,3257, por tanto cumple_regla_k. Comprobación en P = 2,56: G = 1,187 y L = 0,038.


### Crecimiento implícito

    El modelo no proyecta ventas. Con margen constante, el crecimiento del FCF equivale al de las ventas. Mantengo el escenario normal en lo demás: 3 % en los años 6–10, 2 % terminal, r del 9 %, 12 £mm de caja y 114,109 mm de acciones. Busco el crecimiento de los años 1–5 que iguala el valor a 2,56 £, es decir, 292,1 £mm. Con −5 % el valor sale en 279,2 £mm y con −4 % en 292,2 £mm; interpolando, −4,9 % anual. Contraste: el DCF inverso de la hoja (crecimiento constante a diez años) da −1,76 % anual.

### Escenario malo

    Los márgenes se comprimen: personal y material suben sin poder trasladarse a precio, y SchahlLED y Lightronics no se recuperan. El FCF base de 25,333 £mm cae un 2 % anual durante diez años (año 10: 20,70 £mm). El crecimiento terminal es del 1 %, la r del 9 % y se suman 12 £mm de exceso de caja. Cálculo: (147,80 + 110,39 + 12) ÷ 114,109 = 2,368 £. Con una caída del FCF del −5 % anual valdría ≈1,94–2,05 £.

### Escenario normal

    Margen estable en torno al 18 %, precio y volumen modestos. El FCF crece un 3 % anual en los años 1–10 (año 10: 34,05 £mm) y un 2 % terminal, lo que implica un múltiplo de salida de 14,6x frente a un P/FCF histórico de 16x. Con r del 9 % y 12 £mm de caja: (188,01 + 209,55 + 12) ÷ 114,109 = 3,589 £.

### Escenario bueno

    ALIOTH, SmartScan y Corkia funcionan, las filiales se recuperan y la caja se despliega bien. El FCF crece un 8 % anual en los años 1–10 (año 10: 54,69 £mm), parecido al BPA de la década (+7,8 % anual), con un 2,5 % terminal. Con r del 9 % y 12 £mm de caja: (240,89 + 364,31 + 12) ÷ 114,109 = 5,409 £. No resta gasto en adquisiciones.

### Sensibilidad (comentarios)

    7 %: Valores por escenario: malo 3,07, normal 5,01, bueno 7,99. Precio de Sí: P* = (0,6·5,0104 + 0,2·7,9923 + 0,6·3,0707) / 1,4. El ponderado coincide con la sensibilidad de la hoja (5,2189).
    8 %: Valores por escenario: malo 2,67, normal 4,18, bueno 6,46. El precio queda por debajo del escenario malo.
    9 %: Caso base; coincide con la escalera. Valores por escenario: malo 2,37, normal 3,59, bueno 5,41.
    10 %: Valores por escenario: malo 2,13, normal 3,15, bueno 4,64. Holgura de ≈14 % sobre el precio.
    11 %: Valores por escenario: malo 1,94, normal 2,80, bueno 4,06. Cumple por poco: el precio de Sí está solo ≈2 % por encima del precio. El ponderado coincide con la hoja (2,8806).

### Qué haría falsa la conclusión

    - Un precio actualizado por encima de ≈3,33 £ (o de ≈2,85 £ con la ventana de FCF a cinco años) sin mejora de la tesis.
    - Margen operativo del grupo por debajo del 15 % dos años seguidos fuera de una crisis puntual, o caída del margen de Thorlux.
    - Beneficio operativo de FY27 por debajo de 30 £mm o cuarto año seguido de caída de ventas con margen a la baja.
    - FCF sin circulante de FY27 por debajo de 22 £mm.
    - Una adquisición grande pagada cara o financiada con deuda o con pasivos de rescate, que consuma el exceso de caja.
    - Deterioro del goodwill de SchahlLED u otra pérdida en filiales compradas que confirme mala asignación de capital.
    - Nuevos préstamos a partes vinculadas o pérdidas en los existentes (Mr N Brangwin, distribuidores).
    - Evidencia de que los controles conectados y el software desplazan la decisión de compra hacia competidores con otra economía.

### Lo que no sabe

    - El paquete contiene referencias posteriores a la fecha de corte: 'Decisión del inversor (08-nov-2026)' sobre la ventana del FCF y otros datos. No uso esas decisiones como información. Las cifras subyacentes (medias FY24–26 de los informes anuales) son anteriores al corte; adopto la ventana de tres años como elección propia y muestro la de cinco años como sensibilidad.
    - El precio de 2,56 £ procede de fuentes secundarias (TipRanks, AJ Bell, Stoxray), no de la bolsa, que no mostró datos. Es precio con derecho al dividendo de 5,53p (ex-dividendo el 5-nov-2026). El 30-oct hubo un intradía de 263p; también estaría en zona cumple_regla_k.
    - No tengo los informes anuales primarios. Todas las cifras vienen de la hoja y de la respuesta de etapa 1, que trato como hipótesis.
    - La ventana de FCF cambia el valor: media de tres años 25,333 £mm frente a ≈21,59 £mm a cinco años. La media de tres años incluye una liberación de circulante de +7,4 £mm en FY24.
    - El DCF no modela ventas. El crecimiento implícito de ventas supone que el FCF crece al mismo ritmo (margen constante).
    - Uso 114,109 mm de acciones diluidas medias, aunque hoy hay 112,062 mm en circulación. Con estas, el valor por acción sería ≈1,8 % mayor.
    - El exceso de caja de 12 £mm es una estimación: descuenta el dividendo final de 6,197 £mm, que sin embargo cobrará quien compre a 2,56 £. El efecto es pequeño.
    - No sé qué competidores amenazan más, ni las cuotas de mercado, ni el crecimiento orgánico separado de precio y adquisiciones.
    - No conozco la holgura actual del test de deterioro del goodwill de SchahlLED, ni si siguen vivos los préstamos a Mr N Brangwin, ni si la base del bonus incluye ganancias de valor razonable.
    - La sección de auditoría de la hoja está desactualizada ('Sin escenarios aún', C76 vacío) frente a los valores rellenados; me fío de los valores calculados.
    - El valor de Simply Wall St es inconsistente y no lo uso.
    - La tasa del 9 % es una convención: solo 3,7 puntos sobre el gilt al 5,30 %.

### Citas

    [hoja_analisis] «Precio actual,Cotización por acción.,2.56» → Precio actual usado (2,56 £).
    [hoja_control_maestro] «Cierre 29-oct-2026,£ por acción,Secundaria (3 fuentes coincidentes)» → Fecha y naturaleza secundaria del precio.
    [hoja_control_maestro] «256,00p (AIM). londonstockexchange.com no mostró datos al consultarlo.» → Precio de 256p sin confirmación de la bolsa.
    [hoja_control_maestro] «Cum-dividendo: ex-dividendo 5-nov-2026 (5,53p). Intradía 30-oct 263p.» → El precio incluye el dividendo; intradía del día de corte.
    [hoja_control_maestro] «valores de fase 1: CFO 35,148 · capex 8,141 · intereses 0,254 · principal arrendamientos 0,920 · SBC 0,500 £mm» → Datos del FCF base: 35,148 − 8,141 − 0,254 − 0,920 − 0,500 = 25,333 £mm.
    [hoja_control_maestro] «Decisión del inversor (08-nov-2026): FCF base con media de 3 años FY2024–FY2026» → Referencia posterior a la fecha de corte, no usada como información.
    [hoja_control_maestro] «CFO medio 3a 35,148 / 5a 31,412.» → Sensibilidad a la ventana de cinco años.
    [hoja_control_maestro] «Capex (PP&E + intangibles incl. desarrollo capitalizado) medio 3a 8,141 / 5a 8,458.» → Capex a cinco años para la sensibilidad (FCF ≈21,59 £mm).
    [hoja_control_maestro] «3a: perímetro homogéneo pero incluye liberación de circulante +7,4 en FY24. CFO sin circulante 3a 34,099.» → Sesgo de circulante en el FCF base.
    [hoja_control_maestro] «Media ponderada diluida FY26 114,109 mm (= básica; opciones antidilutivas).» → Número de acciones usado.
    [hoja_control_maestro] «en circulación hoy 112,062 mm (coherente con C41) → valor por acción +1,8%.» → Sensibilidad al número de acciones.
    [hoja_analisis] «76,Exceso de caja NO operativa que sumas (mm) · opcional,12,12,12» → Exceso de caja sumado: 12 £mm.
    [hoja_control_maestro] «dividendo final 6,197 (pago 4-dic-2026)» → Dividendo descontado del exceso de caja.
    [hoja_analisis] «67,Crecimiento de la caja libre · años 1–10,-0.02,0.03,0.08» → Crecimiento del FCF por escenario.
    [hoja_analisis] «68,Crecimiento para siempre · desde el año 11,0.01,0.02,0.025» → Crecimiento terminal por escenario.
    [hoja_analisis] «69,Probabilidad que le das,0.2,0.6,0.2» → Probabilidades de los escenarios.
    [hoja_analisis] «78,VALOR INTRÍNSECO POR ACCIÓN,2.36776970403238,3.58920536269667,5.40887726726687» → Valores por acción al 9 %, recalculados por mí con el mismo resultado.
    [hoja_analisis] «Tu r (9.0%),3.56957019126882,3.70885261187785,3.86993296535743» → Ponderado al 9 %: 3,7089.
    [hoja_analisis] «r − 2 pts (7.0%),4.90066240835808,5.2188717328657» → Contraste del ponderado al 7 %.
    [hoja_analisis] «r + 2 pts (11.0%),2.80843891410908,2.8806099863876» → Contraste del ponderado al 11 %.
    [hoja_analisis] «Crecimiento que el precio ya da por hecho,DCF inverso: crecimiento de FCF (años 1–10) que haría que el valor fuese igual al precio actual.,-0.0175892045440848» → DCF inverso a diez años: −1,76 %.
    [hoja_control_maestro] «(préstamos 0,853 + arrendamientos 3,611 − caja 47,176) ÷ EBITDA reportado 41,763 = −1,02x (caja neta).» → Balance con caja neta.
    [hoja_control_maestro] «RO IFRS 18,2% (FY16) → 18,4% (FY26), rango 14,4–18,4% (mín. COVID FY20)» → Estabilidad del margen operativo.
    [respuesta] «ventas FY24–26 −0,5/−0,3/−1,3 %» → Ventas ligeramente a la baja tres años.
    [respuesta] «los ingresos en Alemania han caído de 21,5 £mm en FY23» → Deterioro de SchahlLED/Alemania.
    [respuesta] «is becoming more limited» → Límite a nuevas eficiencias de margen.
    [hoja_control_maestro] «Gilt UK 10 años 5,30% (GBP, moneda de los flujos).» → Diferencial de la r del 9 % sobre la tasa sin riesgo.
    [hoja_control_maestro] «3a 0,500 / 5a 0,300» → SBC a cinco años para la sensibilidad de la ventana.

### Comprobaciones mecánicas y normalizaciones

    {
      "comprobaciones": {
        "escalera_recalculada_anexo_c": {
          "p_estrella": 3.3256999999999994,
          "precio_si": 3.3256999999999994,
          "ponderado": 3.7088599999999996,
          "precio_escenario_malo": 2.3678
        },
        "citas_total": 28,
        "citas_literales": 28,
        "avisos": [],
        "nota": "Comprobaciones mecánicas informativas: no acreditan la calidad económica."
      },
      "normalizaciones_enum": []
    }

