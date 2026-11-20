# Análisis directo · CocaCola, etapa 1 del universo (hoja del 2026-10-30)

Estado de la ejecución: `AUDITORIA_DOCUMENTAL_PENDIENTE_ACEPTACION`

Revisión a ciegas pendiente. No es aceptación, ni integración, ni aptitud para dinero real.

| Campo | Valor |
|---|---|
| Empresa | cocacola |
| Fecha de corte | 2026-10-30 |
| Tasa | 9 % |
| Tarea | analisis-directo-cocacola-44752364135 |
| SHA del código | 779b55abd380e8427650233fcb8a9c9fa74472f4 |
| Huella del paquete (package_sha256) | b7749f72dfe92e567731279c8a53cac095e1155b3093795e34be7b0a53e426ee |
| Huella del envío (bundle_sha256) | 0825e81a086e9aab2cb4932ef5867d2819774ac6bbe980642b6f29bc7d08e875 |
| Huella del encargo | 022846e95b809a772317c2b17d6d946f3f91b9066c864911e473bb7ea15843e4 |
| Modelo pedido / devuelto | claude-opus-5-5 / claude-opus-5-5 |
| Esfuerzo | high |
| Mensajes enviados | 1 |
| Cota de entrada estimada antes de llamar | 146450 tokens |
| Reserva estimada antes de llamar | USD 1.24116 (máximo de la ejecución USD 3) |
| Reserva registrada | USD 1.24116 |
| Uso de tokens | entrada 65813, salida 17467 |
| Coste | CONOCIDO_ESTIMADO; estimado USD 0.612592; cota 0.612592 |

## Paquete de entrada

| id | ruta | commit | sha256 | bytes |
|---|---|---|---|---|
| respuesta | datos_analisis_directo/cocacola/etapa1/CocaCola_respuesta.md | 779b55abd380 | b908166f858139c6b597e9e05043ccc801dd67d81ee0a58ba64d6ba515e0b1d7 | 35992 |
| hoja_analisis | datos_analisis_directo/cocacola/etapa1/CocaCola_evaluada__Análisis.csv | 779b55abd380 | 8bc9d80bc0f8e9f623a48598efdfc09fbb2ebdc44a8629f0639d45a9f6bd9e3c | 23786 |
| hoja_guia_simply_wall_st | datos_analisis_directo/cocacola/etapa1/CocaCola_evaluada__Guía_Simply_Wall_St.csv | 779b55abd380 | 2791cc208d21b779b2104db9848a271eded2ae7cb4392769b743a2d95f8c3e2f | 7794 |
| hoja_opciones | datos_analisis_directo/cocacola/etapa1/CocaCola_evaluada__Opciones.csv | 779b55abd380 | b9f97b6706b77f7a28f70140d212f0790ee7334eb22965a4f538963e777a1a73 | 1537 |
| hoja_control_maestro | datos_analisis_directo/cocacola/etapa1/CocaCola_evaluada__Control_maestro.csv | 779b55abd380 | ba0eb2f9dad5e05e5789153a4e7465e32d2e0a523b5aba1c0856829936fb28a8 | 55976 |

## Salida del modelo (datos, sin acciones ejecutables)

Estado `modelo_no_aplicable` · cubo «Demasiado difícil» · acción `demasiado_dificil` · zona `sin_zona`

| Escenario | Valor por acción | Probabilidad |
|---|---|---|
| malo | — | 0.2 |
| normal | — | 0.6 |
| bueno | — | 0.2 |

| Escalera (k = 3) | Declarado | Recalculado (Anexo C) |
|---|---|---|
| Precio actual | 1.5221 | |
| Precio del escenario malo | — | — |
| P* | — | — |
| Precio de Sí = mín(P*, V_normal) | — | — |
| Ponderado | — | — |
| Crecimiento implícito al precio actual / del normal (%) | — / — | |

| Tasa | Precio de Sí | Ponderado | Zona |
|---|---|---|---|
| 7 % | — | — | sin_zona |
| 8 % | — | — | sin_zona |
| 9 % | — | — | sin_zona |
| 10 % | — | — | sin_zona |
| 11 % | — | — | sin_zona |

### Resumen

    Coca-Cola İçecek (CCOLA, Borsa İstanbul) cotiza a 1,5221 USD (75,65 TL el 28/10/2026 a 49,6997 TL/USD). El DCF simplificado al accionista no es aplicable. La caja libre base tras intereses es de −2,2 mm USD (media 2023–2025). Solo el LTM a junio de 2026 es positivo, con 221,8 mm USD, y llega con márgenes de 1S26 que la empresa explica en parte por inventarios baratos. La contabilidad por hiperinflación hace que los intereses nominales en TL lleven dentro una compensación por inflación cuya contrapartida es una ganancia monetaria sin caja, así que el flujo al accionista depende sobre todo de la estructura financiera. Con la base de 3 años, todos los escenarios dan un valor negativo. Como contraste he usado la base más favorable del paquete (LTM): da 0,81 / 1,44 / 2,20 USD por acción, un ponderado de 1,47, un P* de 1,28 y un precio de Sí de 1,28. El precio actual queda por encima del ponderado incluso en ese caso. Además, el valor para un accionista en USD depende de la relación entre devaluaciones y subidas de precio locales en Türkiye, Pakistán, Asia Central e Irak, y no sé acotarla. Estado: modelo no aplicable; cubo y acción: demasiado difícil.


### Moneda

    USD


### Justificación

    Modelo no aplicable. La caja libre al accionista tras intereses es de −2,2 mm USD de media en 2023–2025, la financiación está distorsionada por la hiperinflación (intereses nominales en TL frente a una ganancia monetaria sin caja) y la propia hoja marca la financiación como inestable. El único FCF positivo es el LTM, apoyado en márgenes de 1S26 que la empresa atribuye en parte a inventarios baratos. Demasiado difícil: el negocio local parece sólido (deuda neta/EBITDA de 0,67x, ROIC ≈14 % en TL constantes), pero lo que llega a un accionista en USD depende de la carrera entre devaluaciones y precios locales en varios países, del contrato con TCCC (proveedor del 28 % de las ventas y accionista) y de operaciones con el grupo sin explicar. Ni siquiera con la base LTM el precio deja margen: queda por encima del ponderado de contraste. Por eso no hay precio de Sí ni compra.


### Probabilidades

    Mantengo las de partida (0,2 / 0,6 / 0,2), que suman 1. No las muevo porque no hay escenarios de valor válidos sobre los que aplicarlas. Tampoco cargo más el escenario malo, porque el riesgo de moneda ya lleva el caso a Demasiado difícil.


### Fórmula aplicada

    No se aplica. Con la base de 3 años, V = −0,0080 / −0,0143 / −0,0219: V_malo ≤ 0, no hay precio del escenario malo y P* sería negativo. Contraste con la base LTM, que no es conclusión: V = 0,808 / 1,444 / 2,203. Entre V_malo y V_normal: G(P) = 0,6·(1,444 − P) + 0,2·(2,203 − P) = 1,307 − 0,8P; L(P) = 0,2·(P − 0,808) = 0,2P − 0,162. G = 3L da 1,307 − 0,8P = 0,6P − 0,485, de donde P* = 1,792/1,4 ≈ 1,28. Precio de Sí = mín(1,28; 1,444) = 1,28. Ponderado = 0,2·0,808 + 0,6·1,444 + 0,2·2,203 ≈ 1,469. Con el precio de 1,5221 esa zona sería «caro».


### Crecimiento implícito

    No hay un modelo de ventas en USD en el paquete, así que no puedo dar el crecimiento de ventas a cinco años. Con la base de 3 años (FCF ≤ 0), el DCF inverso no tiene solución. Contraste en FCF, no en ventas: con la base LTM de 221,8 mm USD, g terminal del 2 % y r del 9 %, la capitalización de 4.259,1 mm USD exige 19,20 veces la base. Eso equivale a un crecimiento del FCF a 10 años de ≈5,7 % anual (5,5 % da 18,91x y 6 % da 19,63x), frente al 5 % del escenario normal.

### Escenario malo

    Supuesto: las devaluaciones superan a las subidas de precio locales; FCF −2 % anual durante 10 años y g terminal del 1 %. Con la base de 3 años (−2,2 mm USD) el valor es −0,008 USD por acción, un número sin sentido económico. Con la base LTM de 221,8 mm USD saldría ≈0,81 USD: 22,4215/2,2 = 10,192 veces la base; 10,192 × 221,8 / 2.798,08. Solo lo doy como contraste: no hay una base de FCF sostenible en USD que pueda defender.

### Escenario normal

    Supuesto: volumen a un dígito medio y precios que compensan la moneda; FCF +5 % anual durante 10 años y g terminal del 2 %. Con la base de 3 años da −0,0143 USD por acción. Con la base LTM daría ≈1,44 USD (18,214 veces la base). No disponible: el resultado depende enteramente de la base elegida, y la del LTM está inflada por el 1S26.

### Escenario bueno

    Supuesto: las plantas se llenan y el capex/ventas baja; FCF +10 % anual durante 10 años y g terminal del 2,5 %. Con la base de 3 años da −0,0219 USD por acción. Con la base LTM daría ≈2,20 USD (27,796 veces la base). No disponible por la misma razón.

### Sensibilidad (comentarios)

    7 %: Con la base de 3 años, el valor es negativo a cualquier tasa; el modelo no es aplicable.
    8 %: Igual que al 7 %: no hay una base de FCF válida.
    9 %: Coincide con la escalera, que no está disponible. Contraste con la base LTM: precio de Sí ≈1,28 y ponderado ≈1,47, con el precio de 1,5221 por encima de ambos.
    10 %: Una tasa mayor solo reduciría los valores de contraste; no cambia la conclusión.
    11 %: Igual que al 10 %.

### Qué haría falsa la conclusión

    - Una serie de 10 años de FCF tras intereses en USD, a tipos de cambio históricos, que muestre FCF positivo y creciente también en años de devaluación. Me sacaría de Demasiado difícil hacia Vigilar.
    - Que el ejercicio 2026 completo y el 2027 den un FCF tras intereses positivo en USD de un orden parecido al LTM (≈220 mm USD) con el margen EBIT por encima del 15 % y el azúcar y los inventarios a precio normal. Haría utilizable una base positiva.
    - La publicación de los Bottler's Agreements renovados, con su plazo y sin cambios unilaterales de precio del concentrado a favor de TCCC.
    - Hacia No: el FCF tras intereses sigue ≤ 0 dos ejercicios más mientras se pagan dividendos por encima del FCF, o la deuda neta/EBITDA supera 2x.
    - Hacia No: las operaciones bajo control común de 2024 o las compras de 2021 y 2023 resultan ser compras caras a empresas del grupo.
    - Si se resolviera la competencia, una cotización claramente por debajo de ≈1,28 USD (P* de contraste con la base LTM) haría relevante el precio.

### Lo que no sabe

    - No dispongo de una serie de FCF tras intereses en USD de 2016 a 2025 a tipos históricos: los años anteriores a 2023 están en TL nominales y los posteriores reexpresados por TMS 29.
    - No sé qué parte de los intereses pagados (253,3 mm USD de media) es compensación por inflación en la deuda en TL. Tampoco tengo los intereses cobrados, que van en financiación y la base no suma. Sin ese desglose no puedo construir un flujo al accionista en términos reales.
    - No sé qué parte del FCF LTM de 221,8 mm USD es repetible, dado el efecto de los inventarios baratos y del azúcar en el 1S26.
    - No conozco los términos de los Bottler's Agreements: renovación, precio del concentrado y qué parte de las compras a TCCC (28 % de las ventas) es concentrado.
    - No sé qué se compró en 2021 y 2023 ni qué fueron las operaciones bajo control común de 2024, y no tengo los resultados de Bangladés.
    - No hay en el paquete un modelo de ventas en USD, así que no puedo calcular el crecimiento implícito de ventas a cinco años.
    - Hay registros posteriores a la fecha de corte: varias notas de la hoja Control maestro llevan «Decisión del inversor (08-nov-2026)», que fijan la moneda USD, la ventana de 3 años y el valor de C26. No uso esas decisiones como hechos. Solo uso los datos de mercado y contables subyacentes, con fecha anterior al corte (precio del 28/10/2026, tipo de cambio del 27/10/2026, cuentas hasta el 30/06/2026). La fila 4 aún marca la moneda base como pendiente de inversor.
    - El precio es del 28/10/2026, no del 30/10/2026; no tengo cotización en la fecha de corte.
    - La respuesta de etapa 1 es un juicio heredado que cita documentos que no están en el paquete (AR2025, Webcast 2Q26, KAP). Solo puedo verificar sus cifras contra la hoja, no contra la fuente primaria.
    - La respuesta heredada estima un precio de Sí de ≈0,81 USD con la base LTM, pero esa cifra es el valor del escenario malo. Aplicando la regla k = 3 a esos mismos escenarios, el precio de Sí de contraste sería ≈1,28.
    - Falta el porcentaje de participación de consejeros y directivos (celda vacía), y buena parte de la auditoría del modelo figura como Pendiente.

### Citas

    [hoja_analisis] «Precio actual,Cotización por acción.,1.5221» → Precio actual en USD usado en el modelo.
    [hoja_control_maestro] «Precio 75,65 TL (28/10/2026) ÷ 49,6997» → Origen y fecha del precio: 75,65 / 49,6997 = 1,5221 USD.
    [hoja_control_maestro] «49,6997 y 55,4243 (27/10/2026)» → Tipo de cambio USD/TRY anterior a la fecha de corte.
    [hoja_control_maestro] «FCF base = 615,2 − 352,2 − 253,3 − 11,9 − 0 = −2,2 mm USD» → FCF base de 3 años negativo tras intereses.
    [hoja_control_maestro] «Solo el LTM jun-26 da positivo (221,8 mm USD)» → Base de contraste LTM.
    [hoja_control_maestro] «Decisión del inversor (08-nov-2026): FCF base con media de 3 años 2023–2025 en USD.» → Existe una decisión fechada después del corte; no la uso como hecho.
    [hoja_control_maestro] «Capital 2.798.078.602 TL; unidad de cotización 1 TL nominal → 2.798,08 mm acciones» → Número de acciones para el valor por acción.
    [hoja_control_maestro] «capitalización 1,5221 × 2.798,08; rf = UST 10 años 5,05 % → C41 = 4259.1» → Capitalización de 4.259,1 mm USD, usada en el DCF inverso de contraste.
    [hoja_analisis] «-2.19999999999996,✗ BANDERA · FCF ≤ 0» → La hoja marca el FCF base ≤ 0.
    [hoja_analisis] «No · financiación cambia mucho,✗ BANDERA · financiación inestable» → El DCF simplificado no es aplicable por la financiación.
    [hoja_guia_simply_wall_st] «Bancos/aseguradoras, FCF negativo, financiación/deuda que cambia mucho o negocios extremadamente cíclicos/inestables.» → Criterio de la plantilla sobre cuándo no usar este DCF.
    [hoja_analisis] «VALOR INTRÍNSECO POR ACCIÓN,-0.00801318140880083,-0.0143211428932861,-0.0218546170419402» → Valores negativos de los tres escenarios con la base de 3 años; dividiendo el valor total por −2,2 se obtienen los multiplicadores usados en el contraste LTM.
    [hoja_analisis] «Crecimiento de la caja libre · años 1–10,-0.02,0.05,0.1» → Crecimientos de los escenarios.
    [hoja_analisis] «Crecimiento para siempre · desde el año 11,0.01,0.02,0.025» → Crecimientos terminales de los escenarios.
    [respuesta] «CFO − capex − arrendamientos da ≈251 mm USD de media 2023–2025; los intereses pagados en financiación (253,3, Control maestro C48) lo llevan a −2,2.» → Son los intereses los que llevan la base a cero.
    [respuesta] «una ganancia monetaria sin caja (6,8 mil millones TL en 2025, extracto 2.1)» → Distorsión por hiperinflación en el flujo financiero.
    [respuesta] «que el 1S26 revirtió con ayuda, según la empresa, de inventarios de materias primas comprados más baratos y azúcar favorable» → El LTM positivo está inflado por factores no repetibles.
    [respuesta] «el 69% del volumen y el 72% del EBITDA están fuera de Türkiye (Webcast 2Q26 p.6-7), el 57% de la deuda está en USD (AR2025 p.195)» → Exposición a monedas y a deuda en USD.
    [respuesta] «el NSR/uc de Türkiye en USD subió un 13,8% hasta 3,33, el más alto de la década (AR2025 p.194)» → La moneda jugó a favor en 2025; riesgo de giro.
    [respuesta] «Compra a TCCC 51,9 mil millones TL en 2025, el 28% de sus ventas netas» → Dependencia del dueño de la marca.
    [respuesta] «tras intereses la caja libre media de 2023–2025 es −2,2 mm USD; los dividendos de 2024 y 2025 superaron al FCF» → Los dividendos superaron al FCF.
    [hoja_control_maestro] «= 30.051,0 ÷ EBITDA LTM (resultado operativo + D&A) 44.912,5 = 0,67x» → Balance poco apalancado.
    [hoja_control_maestro] «estrés de caja atrapada en UZS/PKR: ≈0,92x» → Holgura de liquidez estrecha en un caso de estrés.
    [hoja_control_maestro] «Hoy: 19,2x el FCF LTM (USD).» → Múltiplo actual frente a una mediana histórica de 11,1x.
    [respuesta] «la parte en TL (19%), toda a corto, con depósitos en TL al 35–40%» → Coste y plazo de la deuda en TL.

### Comprobaciones mecánicas y normalizaciones

    {
      "comprobaciones": {
        "escalera_recalculada_anexo_c": null,
        "citas_total": 25,
        "citas_literales": 25,
        "avisos": [],
        "nota": "Comprobaciones mecánicas informativas: no acreditan la calidad económica."
      },
      "normalizaciones_enum": []
    }

