# Análisis directo · Jumbo, ejercicio 2025 y primer semestre de 2026

Estado de la ejecución: `AUDITORIA_DOCUMENTAL_PENDIENTE_ACEPTACION`

Revisión a ciegas pendiente. No es aceptación, ni integración, ni aptitud para dinero real.

| Campo | Valor |
|---|---|
| Empresa | jumbo |
| Fecha de corte | 2026-11-17 |
| Tasa | 9 % |
| Tarea | analisis-directo-jumbo-44403694814 |
| SHA del código | e96470eb0a4401b13d6a265312a2f421cea26f20 |
| Huella del paquete (package_sha256) | 8a1efe2a9b9b9e259718b6998db0555f52c04808dc73e1d000aca02ec08c2fcb |
| Huella del envío (bundle_sha256) | ff0a8b544cf0c0c9591337c23d79fb16d67e276672bd8852955531e32f78c371 |
| Huella del encargo | 022846e95b809a772317c2b17d6d946f3f91b9066c864911e473bb7ea15843e4 |
| Modelo pedido / devuelto | claude-opus-5-5 / claude-opus-5-5 |
| Esfuerzo | high |
| Mensajes enviados | 1 |
| Cota de entrada estimada antes de llamar | 814919 tokens |
| Reserva estimada antes de llamar | USD 3.915036 (máximo de la ejecución USD 5) |
| Reserva registrada | USD 3.915036 |
| Uso de tokens | entrada 342723, salida 19676 |
| Coste | CONOCIDO_ESTIMADO; estimado USD 1.764412; cota 1.764412 |

## Paquete de entrada

| id | ruta | commit | sha256 | bytes |
|---|---|---|---|---|
| datos_v63_md | datos_analisis_directo/jumbo/datos_v63.md | e96470eb0a44 | 43e17e6c7f1d37c704bdbe709dc2d835dc52090a5cb99ade4f8a015eb51a94cc | 91017 |
| etapa1_jumbo_analisis_csv | datos_analisis_directo/jumbo/etapa1/Jumbo_evaluada__Análisis.csv | e96470eb0a44 | d4d3324c17533fc6d5be26b0d80c8fa881829f1cd1b545cf5c1ea842f8499c87 | 22121 |
| etapa1_jumbo_control_maestro_csv | datos_analisis_directo/jumbo/etapa1/Jumbo_evaluada__Control_maestro.csv | e96470eb0a44 | bb4f31cdfac49fdfd45c04e898ebb213f5d2abe30785ec3f08347059c4b1f051 | 49431 |
| etapa1_jumbo_guia_sws_csv | datos_analisis_directo/jumbo/etapa1/Jumbo_evaluada__Guía_Simply_Wall_St.csv | e96470eb0a44 | e3cabea03c1a776ed1203ce43f216ec3b29760e8c866e2b925b8990e31152651 | 7660 |
| etapa1_jumbo_opciones_csv | datos_analisis_directo/jumbo/etapa1/Jumbo_evaluada__Opciones.csv | e96470eb0a44 | 56246fb2e5ca7ca826b3c07c4786422bb1cf9c5a3a0d110abc53919735356a4d | 1486 |
| etapa1_jumbo_respuesta_md | datos_analisis_directo/jumbo/etapa1/Jumbo_respuesta.md | e96470eb0a44 | 127e92ec909e1a754b844a4a7d5fd958acde83bbdfde77b5c887e2cb99353572 | 28539 |
| extracto_v63_md | datos_analisis_directo/jumbo/extracto_v63.md | e96470eb0a44 | 3ccb83eea715dc1acfec0a48fac14be147674d78c0ad1ad8da219f520c3bfd0e | 35561 |
| fase1_v63_json | datos_analisis_directo/jumbo/fase1_v63.json | e96470eb0a44 | 90ad33506a3b6d623109ca197f49bf26ca5a6b4f37ae20c01c8090e1e04cf146 | 65113 |
| fuentes_ar_2025_seleccion | datos_analisis_directo/jumbo/fuentes/jumbo-annual-report-fy2025.seleccion.compacto.txt | e96470eb0a44 | d31bceb7083b5dffd7517963e21a6e65b9e1fbb193519c46b9d2ca54db76e209 | 289350 |
| fuentes_h1_2026_compact | datos_analisis_directo/jumbo/fuentes/jumbo-h1-2026-financial-results.compacto.txt | e96470eb0a44 | 3d515049ffc159fd442ee6bfeb388539d5bc607edd05698831568e4af45b7ee7 | 176221 |

## Salida del modelo (datos, sin acciones ejecutables)

Estado `concluido` · cubo «Vigilar» · acción `esperar` · zona `vigilar`

| Escenario | Valor por acción | Probabilidad |
|---|---|---|
| malo | 18.8 | 0.2 |
| normal | 30.87 | 0.6 |
| bueno | 40.29 | 0.2 |

| Escalera (k = 3) | Declarado | Recalculado (Anexo C) |
|---|---|---|
| Precio actual | 27.28 | |
| Precio del escenario malo | 18.8 | 18.8 |
| P* | 27.04 | 27.0429 |
| Precio de Sí = mín(P*, V_normal) | 27.04 | 27.0429 |
| Ponderado | 30.34 | 30.34 |
| Crecimiento implícito al precio actual / del normal (%) | 2.3 / 4 | |

| Tasa | Precio de Sí | Ponderado | Zona |
|---|---|---|---|
| 7 % | 37.62 | 42.87 | cumple_regla_k |
| 8 % | 31.46 | 35.54 | cumple_regla_k |
| 9 % | 27.04 | 30.34 | vigilar |
| 10 % | 23.73 | 26.46 | caro |
| 11 % | 21.14 | 23.46 | caro |

### Resumen

    Jumbo es un minorista de precio bajo con mucho surtido en Grecia, Chipre, Bulgaria y Rumanía. No tiene deuda bancaria, su ROCE ronda el 27 % y reparte casi toda la caja. Su margen bruto y su margen EBITDA llevan varios años bajando por la presión de Rumanía, de los fletes y de las plataformas transfronterizas. La valoración parte de un FCF base de 241,45 mm (medias 2023–2025, cifra C52 del paquete) y suma 65,6 mm de caja sobrante. Esa caja sale de los 200 mm de la etapa 1 menos los 134,37 mm de la distribución extraordinaria de 1,00 €, que el precio de 27,28 € ya no incluye. Al 9 % los valores por acción son 18,80 € en el escenario malo, 30,87 € en el normal y 40,29 € en el bueno. El ponderado es 30,34 € y el precio de Sí por la regla k=3 es 27,04 €. El precio actual queda un 0,9 % por encima del precio de Sí, en zona vigilar. Conclusión: cubo Vigilar y acción esperar. El resultado depende mucho de cuánta caja sobrante se suma y de la tasa: al 10 % la acción ya está cara.


### Moneda

    EUR


### Justificación

    El análisis está concluido: hay datos suficientes y el método de FCF al accionista aplica a una empresa sin deuda financiera y con financiación estable. Al 9 % el precio (27,28 €) supera por poco el precio de Sí (27,04 €) y queda por debajo del ponderado (30,34 €), así que el cubo es Vigilar y la acción esperar. La conclusión es frágil en los dos sentidos. Si se sumara la caja sobrante de 200 mm de la etapa 1 sin descontar el 1,00 € ya pagado, el precio de Sí subiría a ≈28,0 € y cumpliría la regla k; pero eso contaría dos veces una caja que sale de la empresa con la distribución. Al 10 % la acción ya está cara. El escenario malo (18,80 €) queda un 31 % por debajo del precio.


### Probabilidades

    Mantengo 0,2 / 0,6 / 0,2. La compresión de margen y la debilidad de Rumanía ya están dentro de los escenarios malo y normal, así que no las cuento dos veces subiendo la probabilidad del malo. Tampoco hay datos que permitan subir la del bueno.


### Fórmula aplicada

    Para P entre 18,80 y 30,87: G(P) = 0,6 × (30,87 − P) + 0,2 × (40,29 − P) = 26,578 − 0,8P, y L(P) = 0,2 × (P − 18,80) = 0,2P − 3,761. Igualando G = 3L: 26,578 − 0,8P = 0,6P − 11,282, de donde P* = 37,860 / 1,4 = 27,04. Precio de Sí = mín(27,04; 30,87) = 27,04. Ponderado = 0,2 × 18,80 + 0,6 × 30,87 + 0,2 × 40,29 = 30,34. Como 27,28 > 27,04 y 27,28 ≤ 30,34, la zona es vigilar.


### Crecimiento implícito

    DCF inverso con las demás hipótesis del escenario normal: FCF base 241,454, g terminal del 2 %, tasa del 9 % y caja sobrante de 65,6 mm. Para valer 27,28 € hace falta que (A + T) = (27,28 − 0,488) / 1,797 = 14,91. Interpolando entre un crecimiento del 2 % (14,57) y del 2,5 % (15,12) sale ≈2,3 % anual. Supongo margen y conversión a caja constantes, de modo que el crecimiento del FCF equivale al de las ventas. El horizonte explícito del modelo es de 10 años, no de 5: es el crecimiento anual medio de ese tramo.

### Escenario malo

    Las plataformas transfronterizas, el flete y Rumanía recortan precio y volumen, y el margen EBITDA cae hacia el 25–28 %. Hoy está en el 35,34 % en 2025 y en el 32,73 % en H1 2026. Supuestos: FCF base 241,454 mm (C52 = CFO ajustado 316,475 − capex 63,788 − intereses de arrendamientos 2,664 − principal 8,569 − SBC 0), crecimiento del FCF del −2 % anual en los años 1–10 y del 1 % a perpetuidad, descuento al 9 %. Se suma la caja sobrante de 65,6 mm y se divide entre 134,366 mm de acciones. Cálculo: (241,454 × 10,1916 + 65,6) / 134,366 = 18,80 €.

### Escenario normal

    Unas dos aperturas al año, ventas que crecen un 5–6 % y un margen que se sigue erosionando poco a poco, con más capex en centros de distribución. Resultado: el FCF crece un 4 % anual en los años 1–10 y un 2 % a perpetuidad. Rebajo el 5 % de la etapa 1 porque el beneficio creció un 2,96 % en H1 2026 y quedó plano en 2025, aunque las ventas de enero a agosto suben un ~6 %. Múltiplo terminal implícito de 14,6x el FCF, frente a un P/FCF histórico de 15,2x. Cálculo: (241,454 × 16,9054 + 65,6) / 134,366 = 30,87 €.

### Escenario bueno

    Rumanía se recupera y avanza hacia duplicar sus tiendas en una década, las franquicias y Balfin crecen sin capital propio y el margen aguanta. Supuestos: FCF que crece un 7 % anual en los años 1–10 y un 2,5 % a perpetuidad, descuento al 9 %, más la caja sobrante de 65,6 mm. Cálculo: (241,454 × 22,1476 + 65,6) / 134,366 = 40,29 €.

### Sensibilidad (comentarios)

    7 %: Valores: malo 24,49; normal 43,49; bueno 59,39. El precio está holgadamente por debajo del precio de Sí.
    8 %: Valores: malo 21,25; normal 36,12; bueno 48,08.
    9 %: Coincide con la escalera. El precio está un 0,9 % por encima del precio de Sí.
    10 %: Valores: malo 16,89; normal 26,94; bueno 34,60. La hoja calcula una r mínima del 10,2 %, cerca de esta tasa.
    11 %: Valores: malo 15,36; normal 23,89; bueno 30,27.

### Qué haría falsa la conclusión

    - Que el precio baje a 27,04 € o menos sin que cambien los fundamentales: pasaría a cumplir la regla k y el cubo sería Sí.
    - Que el balance de 31-12-2026 muestre más caja sobrante de la estimada, por ejemplo con caja de cierre ≥ 500 mm tras pagar el 1,00 € y la inversión en centros de distribución contenida. El precio de Sí subiría por encima del precio actual.
    - Que el margen bruto anual de 2026 baje del 52 % o el margen EBITDA del 30 %, o que lo hagan dos años seguidos: el escenario malo pasaría a ser el central y el cubo a No.
    - Que el beneficio neto de 2026 o de 2027 quede por debajo de 320 mm, o que el FCF baje de 200 mm dos años seguidos. El crecimiento del 4 % del escenario normal dejaría de sostenerse.
    - Que Rumanía siga cayendo en ventas en 2027 tras el −6,50 % de H1 2026.
    - Una adquisición grande no relacionada con el negocio, o que se comprometa capital propio en Balfin o en inmuebles no comerciales.
    - Que no se haya pagado la distribución extraordinaria de 1,00 € (pago previsto el 20-11-2026): la caja sobrante sería mayor.

### Lo que no sabe

    - La distribución extraordinaria de 1,00 € (≈134,37 mm, ex 16-11-2026, pago 20-11-2026) solo aparece en las notas del volcado, no en un texto primario. Allí se describe además como propuesta sujeta a aprobación. La descuento de la caja porque el precio ya es ex-distribución.
    - No conozco la caja a 17-11-2026. La caja sobrante de 65,6 mm (200 − 134,37) es un juicio heredado: no sé cuánta caja ha generado el segundo semestre hasta noviembre ni cuánta ha absorbido el inventario de Navidad.
    - El CFO ajustado (C46) reparte los intereses cobrados según una caja sobrante de 200 mm. Con 65,6 mm sumaría unos +3,8 mm al FCF base, pero la base de caja sobre la que se cobran intereses es ahora menor. Mantengo 241,454 mm sin recalcular.
    - El importe de los centros de distribución tras la reevaluación de Oinofyta no está publicado; la guía anterior era de más de 95 mm en tres años. Tampoco hay capex presupuestado para 2026.
    - Faltan datos de ventas comparables, tráfico y ventas por m², y no hay cuota de las plataformas transfronterizas en las categorías de Jumbo. Esto limita separar el efecto de la competencia del ciclo de consumo.
    - Los ceros de SBC (2023–2025), de minoritarios y de algunos años de arrendamientos están pendientes de verificación humana. Su efecto previsible es nulo.
    - El crecimiento implícito se calcula sobre un horizonte de 10 años del FCF, no de 5 años de ventas, y supone margen constante.
    - Hay datos posteriores al corte que no uso: la fecha de análisis del 18-11-2026 y la lectura del Bund de ese día. El precio usado es el cierre del 17-11-2026.
    - No uso las referencias externas de valor (Simply Wall St 33,04 €; analistas 32,24 €).
    - No sé qué hay detrás de la sucesión del presidente y accionista de control ni del voto del 57,96 % sobre la remuneración de 2024.

### Citas

    [datos_v63_md] «Precio posterior a la fecha ex (16-nov-2026) de la distribución extraordinaria de 1,00 € por acción: sin derecho a ella.» → El precio de 27,28 € del 17-11-2026 ya no incluye el 1,00 €.
    [datos_v63_md] «134,37 (1,00 € extraordinario ANUNCIADO, ex 16.11 / pago 20.11.2026» → Salida de caja de 134,37 mm que resto de la caja sobrante.
    [datos_v63_md] «Quedan ~200 mm claramente sobrantes (≤ C53).» → Caja sobrante de la etapa 1, de la que parto: 200 − 134,37 = 65,6 mm.
    [datos_v63_md] «FCF base (C52, fórmula): 241.454» → FCF base del modelo.
    [datos_v63_md] «(334,957 + 309,713 + 304,755) / 3 = 316,4750» → CFO ajustado medio 2023–2025 (C46).
    [fuentes_ar_2025_seleccion] «Net cash flows from operating activities 296.912.917 300.687.098 151.095.759 182.343.360» → CFO del grupo en 2025 y 2024.
    [fuentes_ar_2025_seleccion] «assets (38.384.015) (66.338.285) (29.107.865) (33.850.367)» → Capex del grupo en 2025 y 2024.
    [fuentes_ar_2025_seleccion] «Lease repayments (2.325.789) (3.001.882) (1.821.081) (1.946.824)» → Pagos por arrendamientos en financiación (componente de interés).
    [fuentes_ar_2025_seleccion] «Interest paid for leases (9.727.205) (8.533.836) (6.333.624) (6.113.854)» → Pagos por arrendamientos en financiación (componente de principal; etiquetas cruzadas por el emisor).
    [fuentes_ar_2025_seleccion] «Interest received 9.916.790 13.791.382 3.004.653 5.106.255» → Intereses cobrados, que forman parte de C46.
    [extracto_v63_md] «capital de 134.365.561 acciones» → Número de acciones: 134,366 mm.
    [fuentes_h1_2026_compact] «Cash and cash equivalents 4.15 546.140.091 536.668.758 234.183.560 180.572.205» → Caja del grupo a 30-06-2026.
    [fuentes_h1_2026_compact] «payment to the beneficiaries commenced on 28.07.2026» → El dividendo de 0,70 € (94,06 mm) ya se ha pagado.
    [fuentes_h1_2026_compact] «Total cash distributions made during 2026 to date amounted to €161,24 million.» → Las distribuciones de 2026 drenan caja.
    [fuentes_h1_2026_compact] «It is noted that neither the Company nor the Group has any borrowings.» → Sin deuda financiera: el DCF al accionista es aplicable.
    [fuentes_h1_2026_compact] «stood at 53,53% from 53,86% for the previous respective period» → El margen bruto sigue bajando.
    [fuentes_h1_2026_compact] «depreciation and amortization margin stood at 32,73% from 33,25%.» → El margen EBITDA de H1 sigue bajando.
    [fuentes_ar_2025_seleccion] «depreciation and amortization margin stood at 35,34% from 36,77%.» → Compresión del margen EBITDA anual en 2025.
    [fuentes_ar_2025_seleccion] «at the same level as in the previous financial year (€ 320,10 million)» → Beneficio de 2025 plano: apoya rebajar el crecimiento del escenario normal al 4 %.
    [fuentes_h1_2026_compact] «previous respective period when those stood at € 117,18 mil., i.e. increased by 2,96%.» → El beneficio de H1 2026 crece un 2,96 %.
    [fuentes_h1_2026_compact] «increased by approximately 6% compared to the corresponding period last year.» → Ventas de enero a agosto de 2026 en torno a +6 %.
    [fuentes_h1_2026_compact] «Sales in Romania during the first half of 2026 decreased by 6,50% compared with the» → Debilidad de Rumanía.
    [fuentes_ar_2025_seleccion] «intensifying competition, often through practices that may disrupt the level playing field of the market.» → Amenaza de las plataformas transfronterizas (escenario malo).
    [fuentes_ar_2025_seleccion] «are expected to exceed €95 million over the next three years.» → Capex previsto en centros de distribución.
    [fuentes_h1_2026_compact] «70% of the Group's products come from Asia, with China accounting for the largest share.» → Dependencia de Asia como riesgo del escenario malo.
    [fuentes_h1_2026_compact] «Consequently, no new hyper-store may open in Greece during» → Freno a las aperturas en Grecia en 2027.

### Comprobaciones mecánicas y normalizaciones

    {
      "comprobaciones": {
        "escalera_recalculada_anexo_c": {
          "p_estrella": 27.04285714285714,
          "precio_si": 27.04285714285714,
          "ponderado": 30.34,
          "precio_escenario_malo": 18.8
        },
        "citas_total": 26,
        "citas_literales": 26,
        "avisos": [],
        "nota": "Comprobaciones mecánicas informativas: no acreditan la calidad económica."
      },
      "normalizaciones_enum": []
    }

