# Análisis directo · Jumbo, ejercicio 2025 y primer semestre de 2026

Estado de la ejecución: `AUDITORIA_DOCUMENTAL_PENDIENTE_ACEPTACION`

Revisión a ciegas pendiente. No es aceptación, ni integración, ni aptitud para dinero real.

| Campo | Valor |
|---|---|
| Empresa | jumbo |
| Fecha de corte | 2026-11-17 |
| Tasa | 9 % |
| Tarea | analisis-directo-jumbo-44400554324 |
| SHA del código | e96470eb0a4401b13d6a265312a2f421cea26f20 |
| Huella del paquete (package_sha256) | 8a1efe2a9b9b9e259718b6998db0555f52c04808dc73e1d000aca02ec08c2fcb |
| Huella del envío (bundle_sha256) | 93f04fdf160337365c06d17394e6915304ba6baab7233abc480490034e80377e |
| Huella del encargo | 022846e95b809a772317c2b17d6d946f3f91b9066c864911e473bb7ea15843e4 |
| Modelo pedido / devuelto | claude-opus-5-5 / claude-opus-5-5 |
| Esfuerzo | high |
| Mensajes enviados | 1 |
| Cota de entrada estimada antes de llamar | 814919 tokens |
| Reserva estimada antes de llamar | USD 3.915036 (máximo de la ejecución USD 5) |
| Reserva registrada | USD 3.915036 |
| Uso de tokens | entrada 342723, salida 19820 |
| Coste | CONOCIDO_ESTIMADO; estimado USD 1.767292; cota 1.767292 |

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
| Crecimiento implícito al precio actual / del normal (%) | 1.1 / 4 | |

| Tasa | Precio de Sí | Ponderado | Zona |
|---|---|---|---|
| 7 % | 37.62 | 42.87 | cumple_regla_k |
| 8 % | 31.46 | 35.54 | cumple_regla_k |
| 9 % | 27.04 | 30.34 | vigilar |
| 10 % | 23.73 | 26.46 | caro |
| 11 % | 21.15 | 23.46 | caro |

### Resumen

    Jumbo es un minorista de hiperstores de precio bajo y gran surtido en Grecia, Chipre, Bulgaria y Rumanía. No tiene deuda financiera, tiene caja neta y un ROCE de la empresa del 26,6 %. El margen se comprime poco a poco: el margen bruto pasó del 55,6 % al 54,7 % y después al 53,5 %. Rumanía cae y la presión de las plataformas transfronterizas es real. Valoro el flujo de caja libre (FCF) al accionista con una base de 241,45 mm (medias 2023–2025) y una caja sobrante de 65,6 mm. Esa caja son los 200 mm de la etapa 1 menos la distribución extraordinaria de 1,00 € ya descontada en el precio. Al 9 % obtengo un escenario malo de 18,80 €, un normal de 30,87 € y un bueno de 40,29 €, con un ponderado de 30,34 €. La regla k=3 da un precio de Sí de 27,04 €. El precio de 27,28 € (17-nov-2026, ex distribución) queda apenas por encima: zona vigilar. El resultado es muy sensible a la tasa: al 8 % cumple la regla y al 10 % es caro. Cubo vigilar, acción esperar.


### Moneda

    EUR


### Justificación

    **Estado.** Concluido: hay datos suficientes y el DCF al accionista es aplicable. No hay deuda financiera, la financiación es estable y la SBC es nula.
    
    **Cubo y acción.** Vigilar y esperar.
    - El negocio es entendible y de calidad: ROCE del 26–27 %, caja neta, conversión de caja ≈1,04.
    - Al 9 % el precio (27,28 €) queda justo por encima del precio de Sí (27,04 €) y por debajo del ponderado (30,34 €).
    - El margen de seguridad es casi nulo frente al escenario malo (18,80 €, un 31 % por debajo del precio).
    - La conclusión cambia de signo con ±1 punto de tasa. Con esa fragilidad y el margen comprimiéndose, no corresponde comprar.


### Probabilidades

    Mantengo las probabilidades de partida 0,2/0,6/0,2. El margen bruto del primer semestre de 2026 (53,53 %) está por encima del umbral del 53 % que la etapa 1 fijó para subir el malo a 0,3. La compresión gradual ya está dentro del escenario normal (crecimiento del 4 % en vez del 5 %), y la amenaza de las plataformas ya está en el malo: no la cuento dos veces.


### Fórmula aplicada

    V = (18,80; 30,87; 40,29), p = (0,2; 0,6; 0,2).
    - Para 18,80 ≤ P ≤ 30,87: G(P) = 0,6·(30,87−P) + 0,2·(40,29−P) = 26,578 − 0,8P; L(P) = 0,2·(P−18,80).
    - G = 3L ⇒ 26,578 − 0,8P = 0,6P − 11,282 ⇒ 1,4P = 37,860 ⇒ P* = 27,04.
    - Precio de Sí = mín(27,04; 30,87) = 27,04.
    - Ponderado = 0,2·18,80 + 0,6·30,87 + 0,2·40,29 = 30,34.
    - Precio 27,28 > 18,80, > 27,04 y ≤ 30,34 ⇒ zona vigilar.


### Crecimiento implícito

    DCF inverso al 9 %. Valor operativo exigido por el precio = 27,28 × 134,3656 − 65,6 = 3.599,9 mm. Mantengo el resto del normal: FCF base 241,45 mm, 4 % en los años 6–10 y terminal del 2 %. Busco el crecimiento de los años 1–5 que iguala ese valor: con 0 % sale 3.430 mm, con 1 % sale 3.584 mm, y la interpolación da ≈1,1 %. Supongo un margen de FCF sobre ventas constante, así que es un crecimiento del FCF usado como aproximación del crecimiento de las ventas. El normal supone un 4 %.

### Escenario malo

    Las plataformas transfronterizas, el flete y Rumanía llevan el margen EBITDA hacia el 25–28 %.
    - FCF base de 241,454 mm = C46 316,475 − capex 63,788 − interés de arrendamientos 2,664 − principal 8,569 − SBC 0.
    - El FCF cae un 2 % al año durante 10 años: el año 10 queda en ≈197,3 mm. Crecimiento terminal del 1 %.
    - Valor de los años 1–10 ≈1.408,7 mm; terminal descontado ≈1.052,1 mm; caja sobrante 65,6 mm.
    - Total ≈2.526,4 mm entre 134,3656 mm de acciones = 18,80 €.

### Escenario normal

    Unas dos aperturas al año, ventas comparables cerca de la inflación, franquicias creciendo y margen algo por debajo del actual.
    - FCF +4 % anual durante 10 años, desde 241,454 mm; el año 10 llega a ≈357,4 mm. Crecimiento terminal del 2 %.
    - Bajo un punto el 5 % de la etapa 1 por tres motivos: el beneficio está plano (320,31 mm en 2025; +2,96 % en el primer semestre de 2026), Rumanía cae un 6,5 % y la guía prevé más de 95 mm en centros de distribución en tres años.
    - El contraste histórico es un crecimiento anual de las ventas del 9,1 % en 2022–2025 y de ≈6 % en enero–agosto de 2026.
    - Valor de los años 1–10 ≈1.882,0 mm; terminal descontado ≈2.199,9 mm; caja sobrante 65,6 mm.
    - Total ≈4.147,5 mm, es decir, 30,87 €.

### Escenario bueno

    Rumanía duplica tiendas en una década, las franquicias y Balfin crecen sin capital propio y el margen aguanta.
    - FCF +7 % anual durante 10 años; el año 10 llega a ≈475,0 mm. Crecimiento terminal del 2,5 %.
    - Valor de los años 1–10 ≈2.183,9 mm; terminal descontado ≈3.163,9 mm; caja sobrante 65,6 mm.
    - Total ≈5.413,4 mm, es decir, 40,29 €.

### Sensibilidad (comentarios)

    7 %: V = 24,49 / 43,49 / 59,39. En el bueno g = r, así que los años 1–10 valen 10 × FCF0. El precio cumple la regla holgadamente.
    8 %: V = 21,25 / 36,12 / 48,08. Con un punto menos de tasa, el precio ya cumple k=3.
    9 %: Coincide con la escalera. El precio está 0,24 € por encima del precio de Sí.
    10 %: V = 16,89 / 26,94 / 34,60. La hoja marca una r mínima del 10,2 %; con esa exigencia el precio es caro.
    11 %: V = 15,36 / 23,89 / 30,27.

### Qué haría falsa la conclusión

    - Que el precio baje a ≤ 27,04 € sin deterioro del negocio: pasaría a cumplir la regla k=3 (cubo Sí).
    - Que el margen bruto anual de 2026 quede por debajo del 53 % o el margen EBITDA por debajo del 30 % dos años seguidos: subiría la probabilidad del malo y el cubo tendería a No.
    - Que el beneficio neto de 2026 o de 2027 quede por debajo de 320 mm: el normal del 4 % dejaría de sostenerse.
    - Que al 31.12.2026 el inventario vuelva a crecer bastante más que las ventas (en 2025 fue +19 % frente a +7,2 %).
    - Que la inversión en centros de distribución supere claramente los 95 mm o que la cooperación con Balfin exija capital propio de Jumbo.
    - Que Rumanía siga cayendo en ventas en 2027, o que haya un arancel o embargo sobre China que corte el suministro.
    - Que haya una adquisición grande no relacionada con el negocio o un conflicto en la sucesión del accionista de control.

### Lo que no sabe

    - La distribución extraordinaria de 1,00 € (≈134,37 mm, ex 16-nov-2026, pago 20-nov-2026) solo consta en notas de datos_v63, no en un documento primario del paquete; allí se describe como propuesta sujeta al consejo. La resto de la caja sobrante (200 − 134,37 = 65,6 mm) porque el precio ya cotiza ex derecho.
    - La caja sobrante es un juicio heredado (200 mm en la etapa 1). No sumo la caja que se genera en el segundo semestre de 2026, que es estacionalmente fuerte, y eso hace la cifra conservadora. Con 200 mm, cada escenario subiría ≈1,0 €/acción.
    - El FCF base de 241,45 mm incluye dividendos cobrados de la cartera cotizada e intereses de depósitos (C46). Los intereses bajan con los tipos (18,5 → 13,8 → 9,9 mm). Con el CFO solo (232,15 mm de la etapa 1), los valores serían ≈4 % menores y el precio de Sí ≈26 €.
    - No hay guía numérica de capex para 2026 ni importe actualizado de los centros de distribución tras la reevaluación de Oinofyta. Tampoco consta cuánto pagó Jumbo por la tienda de Militari.
    - No hay ventas comparables, tráfico, ventas por m² ni ventas a tipo de cambio constante. No puedo separar las aperturas de la evolución de las tiendas existentes, ni el efecto de las plataformas del ciclo de Rumanía.
    - El crecimiento implícito es un crecimiento del FCF usado como aproximación del de las ventas (margen constante); la plantilla no modela ventas y márgenes por separado.
    - Los ceros de SBC, minoritarios y adquisiciones de varios años están pendientes de verificación humana. No afectan materialmente a la valoración.
    - El precio es del 17-nov-2026 y las acciones son las de 31-dic-2025; el semestral confirma que el número es el mismo a 30-jun-2026. El volcado de datos lleva fecha 18-nov-2026; solo uso el cierre del 17-nov.
    - Hay datos contradictorios sobre las operaciones de insiders en la etapa 1 (ventas de Tanocerian frente a compras de una consejera en 2026 aún sin cotejar). No pesan en la valoración.
    - La hoja señala una r mínima del 10,2 % por la prima de riesgo país, superior al 9 % del encargo. Con ella la conclusión sería 'caro'.

### Citas

    [datos_v63_md] «Previous Close: 27,2800 EUR» → Precio actual de 27,28 € al cierre del 17-nov-2026.
    [datos_v63_md] «Precio posterior a la fecha ex (16-nov-2026) de la distribución extraordinaria de 1,00 € por acción: sin derecho a ella.» → El precio ya no incluye la distribución de 1,00 €; la caja sobrante debe descontarla.
    [datos_v63_md] «134,37 (1,00 € extraordinario ANUNCIADO, ex 16.11 / pago 20.11.2026» → Importe de la distribución extraordinaria (134,37 mm) que resto de la caja sobrante.
    [etapa1_jumbo_respuesta_md] «Quedan ~200 mm claramente sobrantes (≤ C53).» → Caja sobrante de partida (200 mm); 200 − 134,37 = 65,6 mm.
    [fuentes_ar_2025_seleccion] «134.365.561 ordinary registered shares with a nominal value of €0,88 each» → Número de acciones usado como denominador.
    [datos_v63_md] «(334,957 + 309,713 + 304,755) / 3 = 316,4750» → CFO ampliado medio de 2023–2025 (C46).
    [datos_v63_md] «FCF base (C52, fórmula): 241.454» → FCF base de los escenarios: 316,475 − 63,788 − 2,664 − 8,569 − 0.
    [fuentes_ar_2025_seleccion] «Net cash flows from operating activities 296.912.917 300.687.098» → CFO del grupo en 2025 y 2024.
    [fuentes_ar_2025_seleccion] «assets (38.384.015) (66.338.285)» → Capex del grupo en 2025 y 2024.
    [fuentes_ar_2025_seleccion] «Lease repayments (2.325.789) (3.001.882)» → Pagos de arrendamientos en financiación que se restan del FCF.
    [fuentes_ar_2025_seleccion] «Interest paid for leases (9.727.205) (8.533.836)» → Segundo componente de los pagos de arrendamientos restados del FCF.
    [datos_v63_md] «Capex 2025 (38,4) y LTM (30,5) en mínimo» → El capex reciente está en mínimos; por eso uso la media de 3 años (63,8).
    [fuentes_ar_2025_seleccion] «are expected to exceed €95 million over the next three years» → Capex adicional en centros de distribución que modera el crecimiento normal.
    [fuentes_h1_2026_compact] «Cash and cash equivalents 4.15 546.140.091 536.668.758» → Caja del grupo a 30.06.2026.
    [fuentes_h1_2026_compact] «It is noted that neither the Company nor the Group has any borrowings.» → Sin deuda financiera: el DCF al accionista es aplicable.
    [fuentes_h1_2026_compact] «€94.055.892,70, based on the Company’s 134.365.561 shares» → Dividendo de julio de 2026, ya restado en la caja sobrante de la etapa 1.
    [fuentes_h1_2026_compact] «Total cash distributions made during 2026 to date amounted to €161,24 million.» → Distribuciones de 2026 hasta septiembre (sin la extraordinaria de noviembre).
    [fuentes_h1_2026_compact] «stood at 53,53% from 53,86% for the previous respective period» → Compresión del margen bruto en el primer semestre de 2026.
    [fuentes_ar_2025_seleccion] «reached 54,72% from 55,61% the previous year» → Compresión del margen bruto anual en 2025.
    [fuentes_h1_2026_compact] «depreciation and amortization margin stood at 32,73% from 33,25%.» → Compresión del margen EBITDA en el primer semestre de 2026.
    [fuentes_h1_2026_compact] «Sales in Romania during the first half of 2026 decreased by 6,50%» → Debilidad de Rumanía.
    [fuentes_h1_2026_compact] «increased by approximately 6% compared to the corresponding period last year» → Crecimiento de ventas de enero a agosto de 2026, contraste del escenario normal.
    [fuentes_h1_2026_compact] «The Net Consolidated Profits after tax reached € 120,65 mil.» → Beneficio del primer semestre de 2026 (+2,96 %): crecimiento lento.
    [fuentes_ar_2025_seleccion] «The Net Consolidated Profits after tax reached € 320,31 million» → Beneficio plano en 2025.
    [fuentes_ar_2025_seleccion] «The Group’s turnover for the financial year 2025 stood at € 1.232,90 mil» → Ventas de 2025.
    [datos_v63_md] «cagr_3 | C45 | 0.0910124» → Crecimiento anual compuesto de las ventas en 2022–2025 del 9,1 %.
    [fuentes_h1_2026_compact] «no new hyper-store may open in Greece during» → Grecia sin aperturas en 2027: freno al crecimiento.
    [fuentes_ar_2025_seleccion] «intensifying competition, often through practices that may disrupt the level playing field of the market» → Amenaza de las plataformas transfronterizas (escenario malo).
    [fuentes_ar_2025_seleccion] «70% of the Group’s products come from Asia and especially China.» → Riesgo de suministro y de margen (escenario malo).

### Comprobaciones mecánicas y normalizaciones

    {
      "comprobaciones": {
        "escalera_recalculada_anexo_c": {
          "p_estrella": 27.04285714285714,
          "precio_si": 27.04285714285714,
          "ponderado": 30.34,
          "precio_escenario_malo": 18.8
        },
        "citas_total": 29,
        "citas_literales": 29,
        "avisos": [],
        "nota": "Comprobaciones mecánicas informativas: no acreditan la calidad económica."
      },
      "normalizaciones_enum": []
    }

