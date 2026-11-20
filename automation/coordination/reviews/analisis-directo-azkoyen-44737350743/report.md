# Análisis directo · Azkoyen, etapa 1 del universo (hoja del 2026-10-30)

Estado de la ejecución: `AUDITORIA_DOCUMENTAL_PENDIENTE_ACEPTACION`

Revisión a ciegas pendiente. No es aceptación, ni integración, ni aptitud para dinero real.

| Campo | Valor |
|---|---|
| Empresa | azkoyen |
| Fecha de corte | 2026-10-30 |
| Tasa | 9 % |
| Tarea | analisis-directo-azkoyen-44737350743 |
| SHA del código | 779b55abd380e8427650233fcb8a9c9fa74472f4 |
| Huella del paquete (package_sha256) | a6116f9e59582d10120316a5e2859cd36231a2e72a7e5da75de3c1a31d77558e |
| Huella del envío (bundle_sha256) | ce1ffb3bc1da5f8dc6252306af187469096f4522bd6da8cb9fced187a12c030f |
| Huella del encargo | 022846e95b809a772317c2b17d6d946f3f91b9066c864911e473bb7ea15843e4 |
| Modelo pedido / devuelto | claude-opus-5-5 / claude-opus-5-5 |
| Esfuerzo | high |
| Mensajes enviados | 1 |
| Cota de entrada estimada antes de llamar | 135585 tokens |
| Reserva estimada antes de llamar | USD 1.1977 (máximo de la ejecución USD 3) |
| Reserva registrada | USD 1.1977 |
| Uso de tokens | entrada 61196, salida 17823 |
| Coste | CONOCIDO_ESTIMADO; estimado USD 0.601244; cota 0.601244 |

## Paquete de entrada

| id | ruta | commit | sha256 | bytes |
|---|---|---|---|---|
| respuesta | datos_analisis_directo/azkoyen/etapa1/Azkoyen_respuesta.md | 779b55abd380 | 6da5c81755be20e03d80b63ee421e0a9d6450e6379cf5324e8df2ddcda8d5cfb | 30138 |
| hoja_analisis | datos_analisis_directo/azkoyen/etapa1/Azkoyen_evaluada__Análisis.csv | 779b55abd380 | d2e312e322290f17413548cbffae653b6311e730195e89220f0403049d928623 | 23128 |
| hoja_guia_simply_wall_st | datos_analisis_directo/azkoyen/etapa1/Azkoyen_evaluada__Guía_Simply_Wall_St.csv | 779b55abd380 | 2791cc208d21b779b2104db9848a271eded2ae7cb4392769b743a2d95f8c3e2f | 7794 |
| hoja_opciones | datos_analisis_directo/azkoyen/etapa1/Azkoyen_evaluada__Opciones.csv | 779b55abd380 | b9f97b6706b77f7a28f70140d212f0790ee7334eb22965a4f538963e777a1a73 | 1537 |
| hoja_control_maestro | datos_analisis_directo/azkoyen/etapa1/Azkoyen_evaluada__Control_maestro.csv | 779b55abd380 | eac944f110eca40fc2dbc686eb767e35b2bdb2a78cc6a9c8ad93b178e1fa0a06 | 51643 |

## Salida del modelo (datos, sin acciones ejecutables)

Estado `pendiente_de_investigacion` · cubo «Vigilar» · acción `esperar` · zona `cumple_regla_k`

| Escenario | Valor por acción | Probabilidad |
|---|---|---|
| malo | 9.2 | 0.2 |
| normal | 13.24 | 0.6 |
| bueno | 18.71 | 0.2 |

| Escalera (k = 3) | Declarado | Recalculado (Anexo C) |
|---|---|---|
| Precio actual | 10.4 | |
| Precio del escenario malo | 9.2 | 9.2 |
| P* | 12.29 | 12.29 |
| Precio de Sí = mín(P*, V_normal) | 12.29 | 12.29 |
| Ponderado | 13.53 | 13.526 |
| Crecimiento implícito al precio actual / del normal (%) | -1.5 / 4 | |

| Tasa | Precio de Sí | Ponderado | Zona |
|---|---|---|---|
| 7 % | 17.24 | 19.25 | bajo_malo |
| 8 % | 14.36 | 15.9 | bajo_malo |
| 9 % | 12.29 | 13.53 | cumple_regla_k |
| 10 % | 10.74 | 11.76 | cumple_regla_k |
| 11 % | 9.53 | 10.39 | caro |

### Resumen

    Azkoyen (AZK, BME) cotiza a 10,40 € (cierre del 29-oct-2026). Recalculo el DCF de la hoja al 9 % con caja libre base de 19,102 mm (media FY2023-25), 24,389 m de acciones y sin sumar caja. Los valores son 9,20 € (malo), 13,24 € (normal) y 18,71 € (bueno), con un ponderado de 13,53 €. La regla k = 3 da P* = 12,29 €, que es el precio de Sí. El precio actual cae en la zona cumple_regla_k, y aguanta incluso con un recorte del 10 % por capex. Aun así no concluyo compra, por tres motivos. Primero, la variable que decide el valor es si dura el margen del 29 % de Payment Technologies, que aporta el 81 % del resultado de explotación. El paquete no nombra competidores, y la propia empresa cita su tamaño insuficiente frente a ellos como riesgo principal. Por eso ningún escenario recoge una compresión de ese margen. Segundo, el test de deterioro de 2026 parte de hipótesis muy por encima de lo real en el 1S26. Tercero, hay una OPA a 10 € conocida solo por prensa. Además, la elección de la ventana de la base aparece fechada el 08-nov-2026, después del corte. Estado pendiente de investigación, cubo Vigilar, acción esperar.


### Moneda

    EUR


### Justificación

    Con los escenarios heredados, la regla k = 3 se cumple al 9 % y el precio sigue en esa zona aunque recorte un 10 % la base por capex. Por eso no lo llamo No ni Demasiado difícil sin más: el balance es sano (DFN/EBITDA 0,42x), el FCF ha sido positivo los once años de la serie y no hay dilución. Pero no lo concluyo como Sí, por estas razones:
    (1) La hipótesis que decide el valor, la durabilidad del margen del 29 % de Payment (81 % del EBIT), no se puede acotar con el paquete: no hay competidores, cuotas ni economía por unidad, y ningún escenario modela su erosión.
    (2) El test de deterioro de 2026 llega con Ascaso, Coges y Primion muy por debajo del plan.
    (3) La OPA a 10 € procede de prensa; sin el folleto, los compromisos de los dominicales ni el cambio de control de los 30 mm de préstamos, no sé qué precio relevante tendrá el minoritario.
    (4) La ventana de la base aparece decidida el 08-nov-2026, después del corte. La adopto como elección propia, pero la conclusión depende de ella.
    Por todo ello: Vigilar y esperar a investigar.


### Probabilidades

    Mantengo 0,2 / 0,6 / 0,2. El 1S26 empuja hacia el malo (resultado antes de impuestos −18 %, Coges −19,1 %), pero el malo ya supone caja plana sobre una base de tres años (19,1 mm) muy inferior al LTM (27,6 mm). Subir su probabilidad castigaría dos veces el mismo riesgo. El riesgo que no recogen los escenarios, la erosión del margen de Payment, no lo trato con probabilidades porque no puedo acotarlo: por eso el estado es pendiente de investigación.


### Fórmula aplicada

    V = 9,2033 / 13,2407 / 18,7111; p = 0,2 / 0,6 / 0,2.
    Para 9,2033 ≤ P ≤ 13,2407:
    G(P) = 0,6·(13,2407 − P) + 0,2·(18,7111 − P) = 11,6866 − 0,8P
    L(P) = 0,2·(P − 9,2033)
    G = 3L ⇒ 11,6866 − 0,8P = 0,6P − 5,5220 ⇒ P* = 17,2086 / 1,4 = 12,29.
    Precio de Sí = mín(12,29; 13,24) = 12,29.
    Ponderado = 0,2·9,2033 + 0,6·13,2407 + 0,2·18,7111 = 13,53.
    Precio 10,40 > 9,20 y ≤ 12,29 ⇒ cumple_regla_k.
    Con un recorte del 10 % en todos los valores (capex de mantenimiento ~2 mm más alto), P* ≈ 11,06.


### Crecimiento implícito

    Supongo, como el escenario normal, márgenes estables, de modo que la caja libre crece como las ventas. Busco el crecimiento x de los años 1-5 que iguala el valor a 10,40 € × 24,389 = 253,65 mm, dejando el resto del escenario normal: 4 % en los años 6-10, g 2 %, r 9 % y base 19,102 mm. Con x = 0 el valor es 271,4 mm (11,13 €); con x = −1,5 % es 253,95 mm. Interpolando, x ≈ −1,5 % anual. Como contraste, el DCF inverso de la hoja, con un crecimiento único a diez años, da 0,74 % anual. En ambos casos el precio descuenta mucho menos que el 4 % del normal.

### Escenario malo

    Cae el ciclo: Coffee & Vending y Coges siguen débiles y la cartera de Time & Security sigue bajando. Caja libre plana diez años (crecimiento 0 %) y g terminal del 1 %. Base FCF 19,102 mm = CFO 26,162 − capex 3,67 − intereses de arrendamiento 0,461 − principal de arrendamiento 2,929 − SBC 0 (medias FY2023-25). r = 9 %. Valor total 224,46 mm ÷ 24,389 m acciones = 9,20 €. No es un suelo: con −2 % anual el valor sería ≈7,98 € (cálculo propio), y no recoge una compresión del margen de Payment.

### Escenario normal

    Márgenes estables: ventas al 4-5 % con margen de explotación del 12-13 % y caja libre creciendo al 4 % anual durante diez años, con g terminal del 2 %. La salida implícita es de 14,6x la caja del año 10, por encima del P/FCF mediano histórico de 10,9x. Misma base de 19,102 mm. Valor total 322,93 mm ÷ 24,389 = 13,24 €. Se apoya en el crecimiento de ventas 2015-2025 (126,8 a 211,1 mm, ≈5,2 % anual con adquisiciones).

### Escenario bueno

    Payment Technologies sigue creciendo a doble dígito: Cashlogy fuera de Europa y suscripciones de Coges y Vendon. Gana peso en el mix y la caja libre crece al 8 % anual diez años, con g terminal del 2,5 %. Misma base. Valor total 456,34 mm ÷ 24,389 = 18,71 €. Referencia histórica: Payment pasó de 31,3 a 78,2 mm de ventas entre 2015 y 2025.

### Sensibilidad (comentarios)

    7 %: V = 12,20 / 18,74 / 27,83. P* = (0,6·18,74 + 0,2·27,83 + 0,6·12,20) / 1,4 = 17,24. El precio queda por debajo del valor malo (12,20).
    8 %: V = 10,49 / 15,53 / 22,43. P* = 14,36. El precio 10,40 queda justo por debajo del valor malo (10,49).
    9 %: Coincide con la escalera: V = 9,20 / 13,24 / 18,71.
    10 %: V = 8,20 / 11,53 / 16,00. P* = 10,74, solo un 3 % por encima del precio.
    11 %: V = 7,40 / 10,20 / 13,94. El ponderado (10,386) queda ligeramente por debajo de 10,40. Es el resultado más sensible: a partir del 10-11 % el margen desaparece.

### Qué haría falsa la conclusión

    - Hacia No o Demasiado difícil: el test de deterioro del cierre de 2026 recorta el fondo de comercio de Coges o de Primion.
    - Hacia No o Demasiado difícil: el margen de explotación de Payment Technologies cae por debajo del ~22 % en el cierre de 2026 o en el 1S27.
    - Hacia No: el capex de mantenimiento normalizado resulta de 5-6 mm, lo que baja la base hacia ~17 mm, combinado con un FCF de 2026 sin crecimiento.
    - Hacia No: se conoce que Cashlogy compite en precio contra rivales mayores, o pierde cuota.
    - Revisión: la OPA se autoriza con compromisos irrevocables de los dominicales (47,54 % del voto en el consejo), con exclusión de cotización o con deuda de adquisición que pase a la sociedad.
    - Hacia Sí: competidores nombrados con cuotas estables en Cashlogy y Coges, precios al alza sin pérdida de volumen, un test de deterioro de 2026 limpio y un capex normal que no reduzca la base de ~19 mm.
    - Hacia No: el precio supera ~12,3 € sin mejora de fundamentos, o el inversor fija una r ≥ 11 % (el precio pasa a caro).

### Lo que no sabe

    - Información posterior al corte: varias decisiones del Control maestro están fechadas el 08-nov-2026 (ventana de la base FCF FY2023-25, ROCE de C24 y criterio de C31). No las uso como decisiones del inversor. Adopto la media de tres años como elección propia y advierto que con el LTM (27,56 mm) todos los valores subirían ~44 %.
    - La respuesta de etapa 1 está fechada el 30-oct, pero cita una decisión del inversor sobre la ventana que el Control maestro fecha el 08-nov. Hay una incoherencia de fechas en las fuentes.
    - No hay competidores con nombre, cuotas ni economía por unidad (Cashlogy, Coges, Vendon, Coffetek, Ascaso, Primion). No puedo modelar ni dar probabilidad a una compresión del margen de Payment.
    - No sé qué parte de la amortización (6,2 mm) procede de intangibles de adquisiciones. Por tanto no conozco el capex de mantenimiento real frente al capex de 2,3 mm de 2025.
    - No conozco el resultado del test de deterioro de 2026 ni las cuentas del año 2026 completo.
    - Sobre la OPA de Ohmnia a 10 €: la fuente es prensa, recogida en una nota secundaria. Desconozco la identidad del oferente, su relación con los dominicales, compromisos irrevocables, el informe del Consejo, la intención de excluir de cotización y las cláusulas de cambio de control de los 30 mm de préstamos.
    - El precio de 10,40 € es de fuente secundaria (Bolsamanía/Morningstar) y no pude contrastarlo con BME.
    - No dispongo de las operaciones de insiders de los últimos 12 meses (CNMV inaccesible) ni de las condiciones exactas del incentivo de 2026 del Presidente ejecutivo.
    - Falta la caja generada entre julio y octubre de 2026. La deuda neta usada es la de junio, con el dividendo como pasivo. No sumo caja (C76 = 0).
    - Uso las ventas como proxy del crecimiento de la caja libre con margen constante. El modelo de la hoja proyecta FCF, no ventas.
    - No analizo la OPA como arbitraje ni el valor de control.

### Citas

    [hoja_analisis] «Precio actual,Cotización por acción.,10.4» → Precio actual usado: 10,40 €.
    [hoja_control_maestro] «Cierre 29-oct-2026» → Fecha del precio.
    [hoja_analisis] «Caja de las operaciones (mm),Cash from Operations. Media de 3–5 años.,26.162» → CFO medio FY2023-25 de la base.
    [hoja_analisis] «Capex: inversión en activos (mm),Capital Expenditures. Escríbelo en POSITIVO.,3.67» → Capex medio restado en la base.
    [hoja_analisis] «0.461,ℹ se resta del FCF» → Intereses de arrendamiento en financiación.
    [hoja_analisis] «2.929,ℹ se resta del FCF» → Principal de arrendamientos; base 26,162 − 3,67 − 0,461 − 2,929 − 0 = 19,102.
    [hoja_analisis] «Acciones diluidas (mm),Diluted shares outstanding.,24.389» → Acciones para el valor por acción.
    [hoja_analisis] «Crecimiento de la caja libre · años 1–10,0,0.04,0.08» → Crecimientos de los tres escenarios.
    [hoja_analisis] «Crecimiento para siempre · desde el año 11,0.01,0.02,0.025» → Crecimientos terminales.
    [hoja_analisis] «Probabilidad que le das,0.2,0.6,0.2» → Probabilidades de partida.
    [hoja_analisis] «VALOR INTRÍNSECO POR ACCIÓN,9.20332318783971,13.2407223758276,18.7110549532493» → Valores por escenario al 9 %, que coinciden con mi recálculo.
    [hoja_analisis] «0.00739850296639448» → DCF inverso de la hoja a diez años (0,74 %).
    [hoja_control_maestro] «Decisión del inversor (08-nov-2026): FCF base con media 3 años FY2023–25 (recomendación aceptada)» → Decisión fechada después del corte.
    [hoja_control_maestro] «cupones híbridos 0 = 27,559 mm» → FCF LTM, muy por encima de la base.
    [respuesta] «2,3 mm en 2025 frente a 6,2 mm de amortización de inmovilizado material e intangible» → Capex por debajo de la amortización: la base puede estar inflada.
    [respuesta] «22.980 / 78.168 k EUR en 2025» → Margen del 29 % de Payment.
    [respuesta] «22,98 de 28,35 mm de resultado de explotación en 2025 (81 %)» → Concentración del resultado en Payment.
    [respuesta] «Entorno competitivo y dimensionamiento insuficiente (concentración de competidores)» → Riesgo competitivo que la propia empresa reconoce.
    [hoja_control_maestro] «Ascaso ventas −19,8% vs plan +47,9%; Coges −19,1% vs +7,9%; Primion EBIT 0,2 mm vs 6,5 mm plan anual» → Riesgo del test de deterioro de 2026.
    [respuesta] «resultado antes de impuestos del grupo −18 % en 1S26 (10,1 frente a 12,3 mm)» → Deterioro reciente del resultado.
    [respuesta] «Pero 1S26 da 9,6 % y el LTM 11,9 %» → Margen EBIT a la baja.
    [hoja_control_maestro] «OPA Ohmnia 10,00 €/acción en efectivo (prensa; pendiente de autorización CNMV a 30-oct)» → OPA a 10 € de fuente de prensa.
    [hoja_control_maestro] «covenants y cambio de control de los 30 mm de 2026: no encontrados (relevante por OPA)» → Dato ausente sobre el cambio de control.
    [hoja_control_maestro] «DFN 13,341 mm (= APM de la empresa:» → Deuda neta tras el dividendo; justifica no sumar caja.
    [hoja_control_maestro] «Deuda bancaria pasó de 11,6 (dic-25) a 30,6 (jun-26) por préstamos nuevos de 30 mm.» → Préstamos nuevos de 2026.
    [hoja_control_maestro] «FY21–25 = 10,9x (8,8 / 13,4 / 19,8 / 5,0 / 10,9)» → P/FCF histórico frente a la salida implícita de 14,6x.
    [respuesta] «ventas de 126,8 a 211,1 mm entre 2015 y 2025 (≈5,2 % anual compuesto)» → Base del crecimiento del escenario normal.

### Comprobaciones mecánicas y normalizaciones

    {
      "comprobaciones": {
        "escalera_recalculada_anexo_c": {
          "p_estrella": 12.29,
          "precio_si": 12.29,
          "ponderado": 13.526,
          "precio_escenario_malo": 9.2
        },
        "citas_total": 27,
        "citas_literales": 27,
        "avisos": [],
        "nota": "Comprobaciones mecánicas informativas: no acreditan la calidad económica."
      },
      "normalizaciones_enum": []
    }

