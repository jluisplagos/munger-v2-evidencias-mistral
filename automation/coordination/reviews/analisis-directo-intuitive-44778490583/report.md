# Análisis directo · Intuitive, etapa 1 del universo (hoja del 2026-10-09)

Estado de la ejecución: `AUDITORIA_DOCUMENTAL_PENDIENTE_ACEPTACION`

Revisión a ciegas pendiente. No es aceptación, ni integración, ni aptitud para dinero real.

| Campo | Valor |
|---|---|
| Empresa | intuitive |
| Fecha de corte | 2026-10-09 |
| Tasa | 9 % |
| Tarea | analisis-directo-intuitive-44778490583 |
| SHA del código | fcb18bba533554c32f9756d6fb49dc0ebcc2946c |
| Huella del paquete (package_sha256) | e8a6c9f65c23065842a8cab4167bf41c45759472181cef46cafc77338cdf2207 |
| Huella del envío (bundle_sha256) | 88e19aa7c99cfad2866730cdf5ad2c37f584ef45bfda97260701e1543457b01f |
| Huella del encargo | 022846e95b809a772317c2b17d6d946f3f91b9066c864911e473bb7ea15843e4 |
| Modelo pedido / devuelto | claude-opus-5-5 / claude-opus-5-5 |
| Esfuerzo | high |
| Mensajes enviados | 1 |
| Cota de entrada estimada antes de llamar | 155438 tokens |
| Reserva estimada antes de llamar | USD 1.277112 (máximo de la ejecución USD 3) |
| Reserva registrada | USD 1.277112 |
| Uso de tokens | entrada 69972, salida 18225 |
| Coste | CONOCIDO_ESTIMADO; estimado USD 0.644388; cota 0.644388 |

## Paquete de entrada

| id | ruta | commit | sha256 | bytes |
|---|---|---|---|---|
| respuesta | datos_analisis_directo/intuitive/etapa1/Intuitive_respuesta.md | fcb18bba5335 | a1fbbe595f3821078e5681518b8ad83b8d0489225d1af99c79136a99b3ec6749 | 37959 |
| cambios_v2 | datos_analisis_directo/intuitive/etapa1/Intuitive_cambios_v2.md | fcb18bba5335 | db570bcdec98da7879f89860fda2cf2300c06c0c044213cf3494a9448e7f5d03 | 3370 |
| hoja_analisis | datos_analisis_directo/intuitive/etapa1/Intuitive_evaluada__Análisis.csv | fcb18bba5335 | 7522b68b30b73b1fa33dbd10568463d0921217eb473ee0871ca5b510b6e952e0 | 24356 |
| hoja_guia_simply_wall_st | datos_analisis_directo/intuitive/etapa1/Intuitive_evaluada__Guía_Simply_Wall_St.csv | fcb18bba5335 | 2791cc208d21b779b2104db9848a271eded2ae7cb4392769b743a2d95f8c3e2f | 7794 |
| hoja_opciones | datos_analisis_directo/intuitive/etapa1/Intuitive_evaluada__Opciones.csv | fcb18bba5335 | b9f97b6706b77f7a28f70140d212f0790ee7334eb22965a4f538963e777a1a73 | 1537 |
| hoja_control_maestro | datos_analisis_directo/intuitive/etapa1/Intuitive_evaluada__Control_maestro.csv | fcb18bba5335 | 746bb2c7c83b74473edc46b0377b9ed2432117f79a5c918a6fec2dc1c4d441cb | 58516 |

## Salida del modelo (datos, sin acciones ejecutables)

Estado `concluido` · cubo «Vigilar» · acción `esperar` · zona `caro`

| Escenario | Valor por acción | Probabilidad |
|---|---|---|
| malo | 71.97 | 0.2 |
| normal | 122.79 | 0.6 |
| bueno | 204.52 | 0.2 |

| Escalera (k = 3) | Declarado | Recalculado (Anexo C) |
|---|---|---|
| Precio actual | 415.41 | |
| Precio del escenario malo | 71.97 | 71.97 |
| P* | 112.69 | 112.6857 |
| Precio de Sí = mín(P*, V_normal) | 112.69 | 112.6857 |
| Ponderado | 128.97 | 128.972 |
| Crecimiento implícito al precio actual / del normal (%) | 41.1 / 9 | |

| Tasa | Precio de Sí | Ponderado | Zona |
|---|---|---|---|
| 7 % | 167.41 | 194.8 | caro |
| 8 % | 135 | 155.65 | caro |
| 9 % | 112.69 | 128.97 | caro |
| 10 % | 96.4 | 109.65 | caro |
| 11 % | 84.01 | 95.05 | caro |

### Resumen

    Intuitive Surgical cotiza a 415,41 $ (cierre del 08-oct-2026). Es un negocio comprensible y de calidad: no tiene deuda, el 84 % de los ingresos es recurrente y en el 1S26 los ingresos crecieron un 20,7 %. Al 9 % y con los tres escenarios de la hoja de etapa 1, que reviso y mantengo (FCF tras SBC de partida 1.702,5 M; crecimientos del 3 %, 9 % y 15 % a diez años; terminales del 1,5 %, 2,5 % y 3 %), el valor por acción es de 71,97 $ en el malo, 122,79 $ en el normal y 204,52 $ en el bueno. El ponderado es 128,97 $. Con la regla k = 3, el precio de Sí es 112,69 $. El precio actual queda por encima incluso del escenario bueno. Para justificarlo, el FCF tendría que crecer un 25,4 % anual durante diez años, o un 41 % anual durante cinco años y después un 9 %. La conclusión aguanta entre el 7 % y el 11 % de tasa, con otra base de FCF y sumando toda la caja. Cubo Vigilar y acción esperar: el negocio no es el problema, el precio sí.


### Moneda

    USD


### Justificación

    Concluido: el negocio se entiende, no tiene deuda, el FCF es positivo y el DCF del accionista es aplicable. La conclusión no depende de ninguna hipótesis abierta. Con cualquier tasa del 7 % al 11 %, con la base de FCF del LTM sin impuestos diferidos (2.026,1 M, un 19 % más) y sumando toda la caja e inversiones (8.625,5 M, unos 24 $ por acción), el precio de 415,41 $ sigue por encima del escenario bueno. Cubo Vigilar y no No, porque el negocio es de calidad y entendible: el fallo está en el precio, que tendría que bajar a unos 112,69 $ (un 73 % menos) para cumplir la regla k = 3. Acción: esperar.


### Probabilidades

    Mantengo 0,2 / 0,6 / 0,2. Hay riesgos nuevos antes del corte: J&J OTTAVA autorizado por la FDA (22-jul), el caso SIS reabierto por el 9.º Circuito (13-ago), el juicio de la demanda colectiva de hospitales fijado para el 14-sep-2027 y el Extended Use de EndoWrist anunciado para el 1S27. También hay apoyos: los ingresos crecen un 18,5-20,7 % en 2026. Ningún hecho del paquete cuantifica un sesgo. Subir el malo a 0,3 no cambiaría la conclusión, porque el precio supera incluso al escenario bueno.


### Fórmula aplicada

    Entre V_malo y V_normal: G(P) = 0,6·(122,79 − P) + 0,2·(204,52 − P) = 114,58 − 0,8P y L(P) = 0,2·(P − 71,97) = 0,2P − 14,39. La condición G ≥ 3L da 114,58 − 0,8P ≥ 0,6P − 43,18, es decir, P ≤ 157,76 / 1,4 = 112,69. Comprobación en 122,79: G = 16,35 < 3L = 30,49, así que P* = 112,69. Precio de Sí = mín(112,69; 122,79) = 112,69. Ponderado = 0,2·71,97 + 0,6·122,79 + 0,2·204,52 = 128,97. Como 415,41 > 128,97, la zona es caro.


### Crecimiento implícito

    Uso el modelo del escenario normal con FCF 1.702,5 M, 357,3 M de acciones, un 9 % de crecimiento en los años 6-10, un terminal del 2,5 % y r = 9 %. Supongo un margen de FCF constante, de modo que las ventas crecen igual que el FCF. Busco el crecimiento de los años 1-5 que iguala el valor a 415,41 $ (148.427 M): 1.702,5·[Σq^t (t = 1..5) + 20,769·q^5] = 148.427, con q = 1,2948, lo que da un 41,1 % anual. La hoja calcula, con el mismo crecimiento durante los diez años, un 25,4 % anual. El escenario normal supone un 9 %.

### Escenario malo

    La competencia (Johnson & Johnson, Medtronic y empresas chinas), los topes de precio en China, la presión en el cobro por procedimiento, los aranceles y la mayor amortización frenan el negocio. El FCF tras SBC crece un 3 % anual en los años 1-10 y un 1,5 % perpetuo. Base: FCF 1.702,5 M = CFO 3.030,5 − capex 539,8 − SBC 788,2 (FY2025), dividido entre 357,3 M de acciones diluidas y descontado al 9 %, sin sumar caja. Valor total 25.714,7 M ÷ 357,3 = 71,97 $. He recalculado la fórmula y coincide con la hoja.

### Escenario normal

    Los procedimientos frenan desde el 18 % de 2025 hacia un dígito alto, el cobro por procedimiento sigue plano (1.870-1.980 $ desde 2017) y los márgenes se mantienen estables. El FCF tras SBC crece un 9 % anual durante diez años (2017-2025: 10,9 % anual) y un 2,5 % perpetuo. Como la tasa de crecimiento iguala a la de descuento, cada año 1-10 vale hoy 1.702,5 M (suma 17.025 M). El terminal es 4.030,4 × 1,025 / 0,065 / 1,09^10 = 26.847 M. Total 43.872 M ÷ 357,3 = 122,79 $.

### Escenario bueno

    da Vinci 5, Ion, SP y la expansión fuera de EE. UU. funcionan. El FCF tras SBC crece un 15 % anual durante diez años, al ritmo de las ventas de 2017-2025 (15,7 %), y un 3 % perpetuo. Total 73.076 M ÷ 357,3 = 204,52 $. Como contraste: un 20 % anual durante diez años con un 3 % terminal daría unos 298 $ (cálculo mío), todavía por debajo de 415,41 $.

### Sensibilidad (comentarios)

    7 %: Escenarios: 98,95 / 183,45 / 324,70 $. El ponderado coincide con la hoja (194,80). Ni el bueno llega a 415,41 $.
    8 %: Escenarios: 83,37 / 147,52 / 252,34 $ (cálculo mío).
    9 %: Coincide con la escalera. Escenarios: 71,97 / 122,79 / 204,52 $.
    10 %: Escenarios: 63,27 / 104,77 / 170,70 $ (cálculo mío).
    11 %: Escenarios: 56,41 / 91,08 / 145,60 $. El ponderado coincide con la hoja (95,05).

### Qué haría falsa la conclusión

    - Que la cotización baje hasta unos 112,69 $ o menos sin que cambien el cobro por procedimiento, la cuota en EE. UU. ni el litigio: pasaría a Sí.
    - Que el FCF tras SBC suba de forma sostenida, sin partidas no recurrentes, hasta acercar el valor del escenario normal al precio: por ejemplo, cerca de 5.700 M con los mismos supuestos.
    - Datos publicados de pérdida de cuota en EE. UU. o Europa frente a J&J (OTTAVA), Medtronic u otro competidor: pasaría a No o bajaría el escenario normal.
    - Una caída de más del 10 % en los ingresos de instrumentos y accesorios por procedimiento, por ejemplo tras el Extended Use de EndoWrist del 1S27: pasaría a No.
    - Una sentencia en el caso SIS o en la demanda colectiva de hospitales que abra el mercado de instrumentos y reparación con pérdida de margen.
    - Un margen bruto por debajo del 60 %, o procedimientos da Vinci creciendo menos del 8 % dos años seguidos sin causa externa.
    - Que en el 3T26 el DSO siga subiendo sin que lo explique el AR no facturado del arrendamiento por uso, o que el arrendamiento crezca hasta convertir a Intuitive en una financiera de hospitales: pasaría a Demasiado difícil.

### Lo que no sabe

    - Hay contenido posterior a la fecha de corte (09-oct-2026), que no uso como hecho: la versión v2 de la respuesta está fechada el 25-oct-2026, la regla C97 del inversor el 25-oct-2026 y la decisión de usar FY2025 como base del FCF el 20-oct-2026. Elijo yo esa base con datos anteriores al corte (10-K FY2025), con sensibilidad a otras bases.
    - El precio (415,41 $, cierre del 08-oct-2026) sale de fuentes secundarias coincidentes. No tengo la cotización del 09-oct-2026.
    - Base de FCF discutible: media 2023-2025 de unos 829 M, FY2025 de 1.702,5 M, LTM de 2.396,4 M (2.026,1 M sin impuestos diferidos). El capex de FY2025 quedó por debajo de su guía de 650-800 M. El valor se mueve casi en proporción a la base, pero ninguna base razonable del paquete acerca el valor a 415 $.
    - No sumo caja (C76 = 0). No sé si los intereses cobrados están en el CFO. Sumar los 8.625,5 M de caja e inversiones añadiría unos 24 $ por acción a cada escenario y al precio de Sí.
    - No hay cuotas de mercado por país ni por procedimiento, ni colocaciones de competidores.
    - El cobro por procedimiento (1.870-1.980 $) es un cálculo aproximado del analista, no una cifra oficial. Tampoco sé cuánto lo reducirá el Extended Use de EndoWrist del 1S27.
    - No conozco el remedio que piden en los litigios antimonopolio (SIS reabierto; demanda colectiva con juicio el 14-sep-2027) ni la parte de los ingresos expuesta.
    - No he visto la tabla de participaciones de insiders del proxy 2026 ni la remuneración del CEO. El 0,5-0,6 % es una cifra secundaria.
    - No tengo datos del 3T26. El dato de procedimientos en EE. UU. del 2T26 (+12 %) es secundario y no conozco el total mundial.
    - El crecimiento implícito supone un margen de FCF constante, de modo que las ventas crecen igual que el FCF. El modelo de la hoja es de diez años y el de cinco años es una adaptación mía.
    - La respuesta de etapa 1 daba un precio de Sí de unos 72 $ con otra regla (mínimo entre el malo y ¾ del ponderado). Aquí aplico la regla k = 3 del encargo, que da 112,69 $.
    - El valor razonable de Simply Wall St (404,67 $) y los precios objetivo de los analistas (unos 477 $) son referencias secundarias con hipótesis desconocidas. No los uso para decidir.

### Citas

    [hoja_analisis] «Precio actual,Cotización por acción.,415.41» → Precio actual usado.
    [hoja_control_maestro] «Cierre 08-oct-2026 (Nasdaq)» → Fecha del precio.
    [hoja_control_maestro] «C46 = 3030.5» → CFO de FY2025.
    [hoja_control_maestro] «C47 = 539.8» → Capex de FY2025.
    [hoja_control_maestro] «C50 = 788.2» → SBC de FY2025.
    [hoja_analisis] «Aproximación al flujo del accionista si la financiación es razonablemente estable.,1702.5» → FCF base tras SBC: 3.030,5 − 539,8 − 788,2.
    [hoja_analisis] «Diluted shares outstanding.,357.3» → Acciones diluidas.
    [hoja_analisis] «Crecimiento de la caja libre · años 1–10,0.03,0.09,0.15» → Crecimientos de los escenarios.
    [hoja_analisis] «Crecimiento para siempre · desde el año 11,0.015,0.025,0.03» → Crecimientos terminales.
    [hoja_analisis] «VALOR INTRÍNSECO POR ACCIÓN,71.9694758880409,122.787896402506,204.523500203356» → Valores por escenario al 9 %, recalculados por mí.
    [hoja_analisis] «128.971333059783,—,Solo calcula si los 3 escenarios tienen valor» → Valor ponderado.
    [hoja_analisis] «0.253540296623228,✗ BANDERA · > BUENO» → Crecimiento a diez años implícito en el precio.
    [hoja_analisis] «r − 2 pts (7.0%),179.736723583761,194.798310688409» → Contraste del ponderado al 7 %.
    [hoja_analisis] «r + 2 pts (11.0%),91.9481662413113,95.0491790449479» → Contraste del ponderado al 11 %.
    [hoja_control_maestro] «Si C51 = Sí: 2.396,4 (FCF LTM − SBC; yield 1,63%)» → Base alternativa LTM.
    [hoja_control_maestro] «LTM sin impuestos diferidos 1S26: 2.852,3 (1,94%) / 2.026,1 con SBC (1,38%).» → Base LTM sin partidas no recurrentes.
    [hoja_control_maestro] «capex FY25 por debajo de su guía 650–800» → El FCF de 2025 sale favorecido.
    [respuesta] «de 2017 a 2025 el FCF tras SBC creció un 10,9 % anual y las ventas un 15,7 % (cálculo mío)» → Contraste de los crecimientos normal y bueno.
    [respuesta] «ingresos de instrumentos y accesorios por procedimiento planos en unos 1.870-1.980 $ (cálculo mío)» → Sin poder de precio visible.
    [hoja_control_maestro] «frente a ingresos 2T +18,5% / 1S +20,7%» → Crecimiento de ingresos en 2026.
    [hoja_control_maestro] «resultados 2T26 del 16-jul (procedimientos EE. UU. +12%)» → Freno de los procedimientos en EE. UU. (dato secundario).
    [hoja_control_maestro] «anuncio del Extended Use de EndoWrist para 1S27, autorización FDA de J&J OTTAVA (22-jul), fallo del 9.º Circuito en SIS (13-ago)» → Riesgos de precio, competencia y litigio anteriores al corte.
    [hoja_control_maestro] «Contingencias no provisionadas: SIS (reabierto, 9.º Circuito 13-ago-2026) y demanda colectiva de hospitales (juicio 14-sep-2027).» → Litigio antimonopolio abierto.
    [hoja_control_maestro] «Sin deuda financiera (sin préstamos, bonos, papel comercial ni revolving encontrados).» → Sin deuda: el DCF del accionista es aplicable.
    [hoja_control_maestro] «+ inversiones CP 2.455,8 + LP 3.409,3 = 8.625,5» → Sensibilidad a sumar la caja (unos 24 $ por acción).
    [respuesta] «v2 · corregida el 25-oct-2026» → Contenido posterior a la fecha de corte.
    [hoja_control_maestro] «Decisión del inversor (20-oct-2026): FCF base con el último ejercicio FY2025» → Decisión posterior al corte, no usada como hecho.

### Comprobaciones mecánicas y normalizaciones

    {
      "comprobaciones": {
        "escalera_recalculada_anexo_c": {
          "p_estrella": 112.68571428571427,
          "precio_si": 112.68571428571427,
          "ponderado": 128.972,
          "precio_escenario_malo": 71.97
        },
        "citas_total": 27,
        "citas_literales": 27,
        "avisos": [],
        "nota": "Comprobaciones mecánicas informativas: no acreditan la calidad económica."
      },
      "normalizaciones_enum": []
    }

