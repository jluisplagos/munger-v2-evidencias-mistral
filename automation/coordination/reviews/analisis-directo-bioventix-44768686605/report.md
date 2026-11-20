# Análisis directo · Bioventix, etapa 1 del universo (hoja del 2026-10-30)

Estado de la ejecución: `AUDITORIA_DOCUMENTAL_PENDIENTE_ACEPTACION`

Revisión a ciegas pendiente. No es aceptación, ni integración, ni aptitud para dinero real.

| Campo | Valor |
|---|---|
| Empresa | bioventix |
| Fecha de corte | 2026-10-30 |
| Tasa | 9 % |
| Tarea | analisis-directo-bioventix-44768686605 |
| SHA del código | fcb18bba533554c32f9756d6fb49dc0ebcc2946c |
| Huella del paquete (package_sha256) | aaa6c9b7f11d0456187e386f265256e98455a2f59e7c3526a2ebc4ffd899bbe1 |
| Huella del envío (bundle_sha256) | fb1b356b777451a4acbda620658dcffe571e8841ed1f92b291b85800a73dccd2 |
| Huella del encargo | 022846e95b809a772317c2b17d6d946f3f91b9066c864911e473bb7ea15843e4 |
| Modelo pedido / devuelto | claude-opus-5-5 / claude-opus-5-5 |
| Esfuerzo | high |
| Mensajes enviados | 1 |
| Cota de entrada estimada antes de llamar | 145663 tokens |
| Reserva estimada antes de llamar | USD 1.238012 (máximo de la ejecución USD 3) |
| Reserva registrada | USD 1.238012 |
| Uso de tokens | entrada 64455, salida 14252 |
| Coste | CONOCIDO_ESTIMADO; estimado USD 0.54286; cota 0.54286 |

## Paquete de entrada

| id | ruta | commit | sha256 | bytes |
|---|---|---|---|---|
| respuesta | datos_analisis_directo/bioventix/etapa1/Bioventix_respuesta.md | fcb18bba5335 | 2cef0e3b7198479c38754b5f9f5e8250068dbfaa4491c9cbe401b9c5ea339d68 | 36673 |
| hoja_analisis | datos_analisis_directo/bioventix/etapa1/Bioventix_evaluada__Análisis.csv | fcb18bba5335 | 7f043ae4295aed9d9f216e35c17dfde2ae9e5ced93f8cb3879e8d3d847f51d1d | 24150 |
| hoja_guia_simply_wall_st | datos_analisis_directo/bioventix/etapa1/Bioventix_evaluada__Guía_Simply_Wall_St.csv | fcb18bba5335 | 2791cc208d21b779b2104db9848a271eded2ae7cb4392769b743a2d95f8c3e2f | 7794 |
| hoja_opciones | datos_analisis_directo/bioventix/etapa1/Bioventix_evaluada__Opciones.csv | fcb18bba5335 | b9f97b6706b77f7a28f70140d212f0790ee7334eb22965a4f538963e777a1a73 | 1537 |
| hoja_control_maestro | datos_analisis_directo/bioventix/etapa1/Bioventix_evaluada__Control_maestro.csv | fcb18bba5335 | fab1f8ddc89f03084cac717625f6f7c4da895982ccc0a99c9d913ef39e9c74bc | 54076 |

## Salida del modelo (datos, sin acciones ejecutables)

Estado `concluido` · cubo «Vigilar» · acción `esperar` · zona `vigilar`

| Escenario | Valor por acción | Probabilidad |
|---|---|---|
| malo | 11.93 | 0.2 |
| normal | 19.53 | 0.6 |
| bueno | 34.48 | 0.2 |

| Escalera (k = 3) | Declarado | Recalculado (Anexo C) |
|---|---|---|
| Precio actual | 20.25 | |
| Precio del escenario malo | 11.93 | 11.93 |
| P* | 18.41 | 18.4086 |
| Precio de Sí = mín(P*, V_normal) | 18.41 | 18.4086 |
| Ponderado | 21 | 21 |
| Crecimiento implícito al precio actual / del normal (%) | 1.49 / 1 | |

| Tasa | Precio de Sí | Ponderado | Zona |
|---|---|---|---|
| 7 % | 25.55 | 29.64 | cumple_regla_k |
| 8 % | 21.39 | 24.58 | cumple_regla_k |
| 9 % | 18.41 | 21 | vigilar |
| 10 % | 16.17 | 18.33 | caro |
| 11 % | 14.43 | 16.27 | caro |

### Resumen

    Bioventix cobra royalties por anticuerpos de oveja incluidos en tests de diagnóstico de grandes fabricantes. Opera con margen operativo del 74–79 %, sin deuda y con un capex casi nulo, y reparte casi toda la caja. La parte heredada se erosiona: la vitamina D es el 49 % de las ventas y cae por China, la progesterona ya se ha ido y la troponina de Siemens vence en 2032. La neurología (p-Tau217) es una opción sin ningún ensayo clínico aprobado. Acepto como razonables los escenarios de la hoja: FCF base de 7,65m, crecimiento a diez años de −5 %, +1 % y +8 %, y g terminal de 1 %, 2 % y 2,5 %. Al 9 % dan unos valores de £11,93, £19,53 y £34,48, con un ponderado de £21,00. Con la regla k = 3, P* = £18,41 y el precio de Sí es £18,41. Al precio actual de £20,25, que incluye el dividendo de 80p, la acción queda en la zona vigilar. El precio exige que la caja libre crezca cerca de un 1,5 % anual cuando las ventas llevan dos años bajando. Cubo Vigilar; esperar.


### Moneda

    GBP


### Justificación

    El análisis se puede concluir: el negocio es simple, el FCF está bien documentado con fuentes primarias y la financiación es estable. La incertidumbre de la neurología queda acotada en los escenarios y el malo no la necesita. Al 9 % el precio de £20,25 supera el precio de Sí (£18,41) y queda por debajo del ponderado (£21,00), con un margen del 3,6 %. El escenario malo queda un 41 % por debajo del precio. La caja libre lleva cinco años plana y las ventas dos años cayendo, así que el precio ya pide que la caja crezca más que en el escenario normal. No es un No: es un negocio de alta calidad, sin deuda y que sé valorar. Tampoco es un Sí: no cumple la regla k al 9 %. Por eso Vigilar y esperar: lo compraría por debajo de unas £18,4 si los hechos no empeoran. El resultado depende de la tasa: al 7–8 % cumpliría la regla y al 10–11 % estaría caro.


### Probabilidades

    Mantengo las de partida: 0,2, 0,6 y 0,2. La erosión china ya está dentro del escenario normal. La neurología no tiene ningún ensayo clínico aprobado, así que no hay un hecho concreto para mover peso hacia ninguna de las colas.


### Fórmula aplicada

    V = 11,926 / 19,533 / 34,482 con p = 0,2 / 0,6 / 0,2. Para 11,926 ≤ P ≤ 19,533: G(P) = 0,6(19,533 − P) + 0,2(34,482 − P) = 18,616 − 0,8P y L(P) = 0,2(P − 11,926) = 0,2P − 2,385. Igualando G = 3L: 18,616 − 0,8P = 0,6P − 7,156, luego 1,4P = 25,772 y P* = 18,41. Por encima de 19,533 la regla no se cumple: G = 2,99 < 3L = 4,56. Precio de Sí = mín(18,41; 19,53) = 18,41. Ponderado = 0,2·11,926 + 0,6·19,533 + 0,2·34,482 = 21,00. Zona: 20,25 > 18,41 y 20,25 ≤ 21,00, luego vigilar.


### Crecimiento implícito

    Es un DCF inverso con las hipótesis del escenario normal (FCF base 7,65m, g terminal 2 %, r 9 %) que busca el crecimiento anual que iguala el valor a £20,25. Da un 1,49 % y coincide con la tabla auxiliar de la hoja. Tiene dos límites. Primero, el modelo proyecta caja libre a 10 años, no ventas a 5; no hay datos para separar ventas y márgenes, así que uso el crecimiento del FCF como aproximación. Con costes casi fijos, las ventas necesarias crecerían algo menos. Segundo, con el precio ex-dividendo (£19,45) el crecimiento implícito sería de un 0,9 % aproximadamente. El escenario normal supone un 1 %.

### Escenario malo

    FCF base 7,652769m (CFO medio 7,776746 − capex 0,035565 − intereses 0,000047 − SBC 0,088365) entre 5,302036m acciones diluidas. La caja libre cae un 5 % anual durante 10 años (FCF del año 10 ≈ 4,58m) y el g terminal es del 1 %, con r = 9 %. Supuestos: China sigue sustituyendo el anticuerpo (la dirección pone en riesgo un 2 % más un 3–4 % de los ingresos), la vitamina D (49 % de las ventas) sigue cayendo, la progesterona y la troponina de Siemens (2032) desaparecen y la neurología no aporta nada. El cálculo propio coincide con la hoja: 11,926.

### Escenario normal

    Mismo FCF base y mismas acciones. La caja libre crece un 1 % anual en los años 1–10 (FCF del año 10 ≈ 8,45m) y el g terminal es del 2 %, con un múltiplo de salida implícito de 14,6x frente a la mediana histórica de 23,9x. Supuestos: lo heredado cae un 2–3 % al año y la neurología llega a unos £2m de royalties en el año 10, desde £257k hoy. Es coherente con el ritmo de la caja libre en FY2022–26 (+1,1 % anual: de £7,55m a £7,88m). Valor de 19,533.

### Escenario bueno

    Mismo FCF base. La caja libre crece un 8 % anual en los años 1–10 (FCF del año 10 ≈ 16,5m) y el g terminal es del 2,5 %. Supuestos: los ensayos p-Tau217 pasan a uso clínico rutinario en varios grandes clientes con anticuerpo de Bioventix y los royalties de neurología llegan al orden del doble de la vitamina D. Es una apuesta difícil de juzgar sin datos de royalty por test. Valor de 34,482.

### Sensibilidad (comentarios)

    7 %: Valores calculados por mí: 15,34 / 27,19 / 51,28. P* = 25,55. El ponderado coincide con la sensibilidad de la hoja (29,637).
    8 %: Valores calculados por mí: 13,40 / 22,72 / 41,33. P* = 21,39, apenas por encima del precio.
    9 %: Es el caso base y coincide con la escalera. Valores: 11,93 / 19,53 / 34,48.
    10 %: Valores calculados por mí: 10,77 / 17,14 / 29,49. P* = 16,17.
    11 %: Valores calculados por mí: 9,84 / 15,27 / 25,69. El ponderado coincide con la hoja (16,267).

### Qué haría falsa la conclusión

    - Que el precio baje a £18,4 o menos sin que empeoren los hechos (FY2027 sin más caída que la salida de la progesterona): pasaría al cubo Sí.
    - Que antes de FY2028 se aprueben ensayos p-Tau217 de uso clínico con anticuerpo de Bioventix o que los royalties de neurología superen £1m: subiría el escenario normal y el precio de Sí.
    - Que las ventas de FY2027 caigan más del 5 % a tipo constante: subiría la probabilidad del escenario malo y podría llevar al cubo No.
    - Que un gran cliente cambie el anticuerpo de vitamina D o que la pérdida de royalties se extienda fuera de China: el malo pasaría a −10 % y el cubo a No.
    - Nuevos errores en el cálculo de royalties por parte de clientes, o un dividendo pagado con reservas de forma repetida hasta dejar la caja por debajo de unos £5m.
    - Que el informe anual FY2026 muestre una concentración en uno o dos clientes cuyo comportamiento no pueda juzgar: pasaría a Demasiado difícil.
    - Que el valor pase a depender mayoritariamente de la neurología porque lo heredado caiga deprisa: se volvería una apuesta binaria y pasaría a Demasiado difícil.

### Lo que no sabe

    - No tengo el informe anual FY2026. Faltan la concentración por cliente, el calendario y el porcentaje de cada royalty, la opinión del auditor y los riesgos declarados.
    - No sé cuánto pagará cada test de neurología ni si los ensayos clínicos usarán el anticuerpo de Bioventix. Es el mayor determinante del escenario bueno y no lo puedo acotar.
    - No sé qué parte de la troponina (c. £1,4m) corresponde a Siemens, que vence en 2032.
    - No sé por qué el crédito fiscal de I+D pasó de £29k a unos £297k: puede inflar el margen en unos 2 puntos.
    - No sé si la caída de acciones del CEO entre FY2022 y FY2024 fueron ventas, ni quién recibió 76.175 de las opciones de FY2026. También dudo de la volatilidad del 2,63 % usada para valorar esas opciones.
    - El precio de £20,25 sale de fuentes secundarias, corresponde al cierre del 29-oct-2026 y lleva el derecho al dividendo de 80p (ex-div 5-nov-2026). Ex-dividendo serían £19,45 frente a un valor rebajado en unos £0,75.
    - La hoja Control maestro incluye una 'Decisión del inversor (08-nov-2026)' sobre deudores (C31), posterior a la fecha de corte: no la uso.
    - Las cifras de ventas y de caja libre por año y los escenarios proceden del análisis heredado de la etapa 1. Las trato como hipótesis y solo he verificado su aritmética (recalculo los valores al 9 % y coinciden).
    - Entre el 50 % y el 60 % de las ventas están ligadas al USD: el modelo no recoge el riesgo de tipo de cambio.
    - El crecimiento implícito se refiere a la caja libre a 10 años, no a las ventas a 5 años, porque no hay datos para separar ventas y márgenes.
    - No uso el valor razonable de Simply Wall St (£33,49) ni el precio objetivo de analistas porque sus hipótesis son desconocidas.

### Citas

    [hoja_control_maestro] «£20,25 (2.025p), último cierre del AIM. Cotiza CON derecho al dividendo de 80p (ex-div 5-nov-2026).» → Precio actual y derecho al dividendo
    [hoja_control_maestro] «Rellenado y verificado,Cierre 29-oct-2026,GBP por acción» → Fecha del precio
    [hoja_analisis] «Cash from Operations. Media de 3–5 años.,7.776746» → CFO medio usado en el FCF base
    [hoja_analisis] «0.035565» → Capex medio
    [hoja_analisis] «0.088365» → SBC restada
    [hoja_analisis] «7.652769,✓ PASA» → FCF base normalizado de 7,65m
    [hoja_analisis] «Acciones diluidas (mm),Diluted shares outstanding.,5.302036» → Acciones diluidas
    [hoja_analisis] «Crecimiento de la caja libre · años 1–10,-0.05,0.01,0.08» → Crecimiento a diez años de cada escenario
    [hoja_analisis] «Crecimiento para siempre · desde el año 11,0.01,0.02,0.025» → g terminal de cada escenario
    [hoja_analisis] «Probabilidad que le das,0.2,0.6,0.2» → Probabilidades
    [hoja_analisis] «VALOR INTRÍNSECO POR ACCIÓN,11.9258621406902,19.533353821112,34.4817548050264» → Valores por acción al 9 %, que coinciden con mi cálculo
    [hoja_analisis] «Tu r (9.0%),20.2082104395773,21.0015356818105,21.9197533375061» → Ponderado de 21,00 al 9 %
    [hoja_analisis] «r − 2 pts (7.0%),27.8169871560266,29.6369043698075» → Contraste del ponderado al 7 %
    [hoja_analisis] «r + 2 pts (11.0%),15.8569576361962,16.2670644685852» → Contraste del ponderado al 11 %
    [hoja_analisis] «que haría que el valor fuese igual al precio actual.,0.0148771113935232» → Crecimiento implícito del 1,49 %
    [respuesta] «Ventas £13,61m en FY2024, £13,12m (−3,6 %) en FY2025 y £12,97m (−1,1 %) en FY2026» → Ventas en descenso
    [respuesta] «Caja libre (CFO − capex): £7,55m FY2022; £7,79m FY2023; £8,33m FY2024; £7,01m FY2025; £7,88m FY2026» → Caja libre plana en cinco años
    [respuesta] «la vitamina D (49 % de las ventas) sigue cayendo» → Concentración en la vitamina D
    [respuesta] «la dirección pone en riesgo un 2 % más un 3–4 % de los ingresos por China» → Riesgo de China en el escenario malo
    [respuesta] «la troponina de Siemens termina por contrato en junio de 2032.» → Vencimiento de contrato
    [respuesta] «aún no hay ensayo clínico aprobado y los royalties son £257k» → Neurología incipiente
    [respuesta] «margen operativo del 74–79 % durante once años» → Calidad del negocio
    [hoja_control_maestro] «= 11,423m) = 88,3%» → ROCE del 88 %
    [hoja_control_maestro] «Caja en bancos y en mano 5,265m.» → Caja disponible
    [hoja_control_maestro] «Comprometida en la práctica: 2.º dividendo interino 80p ≈4,18m» → Sin exceso de caja que sumar
    [hoja_control_maestro] «Mediana P/FCF 5 años (FY22–26) = 23,9x.» → Contraste del múltiplo terminal
    [hoja_control_maestro] «Opciones vivas 189.681 (3,6% del capital)» → Dilución potencial
    [hoja_control_maestro] «Rango 52 semanas 1.300–2.255p» → Volatilidad del precio
    [hoja_control_maestro] «Decisión del inversor (08-nov-2026)» → Dato posterior a la fecha de corte, no usado

### Comprobaciones mecánicas y normalizaciones

    {
      "comprobaciones": {
        "escalera_recalculada_anexo_c": {
          "p_estrella": 18.408571428571427,
          "precio_si": 18.408571428571427,
          "ponderado": 21.0,
          "precio_escenario_malo": 11.93
        },
        "citas_total": 29,
        "citas_literales": 29,
        "avisos": [],
        "nota": "Comprobaciones mecánicas informativas: no acreditan la calidad económica."
      },
      "normalizaciones_enum": []
    }

