# Análisis directo · Jumbo, ejercicio 2025 y primer semestre de 2026

Estado de la ejecución: `AUDITORIA_DOCUMENTAL_PENDIENTE_ACEPTACION`

Revisión a ciegas pendiente. No es aceptación, ni integración, ni aptitud para dinero real.

| Campo | Valor |
|---|---|
| Empresa | jumbo |
| Fecha de corte | 2026-11-17 |
| Tasa | 9 % |
| Tarea | analisis-directo-jumbo-44399376058 |
| SHA del código | e96470eb0a4401b13d6a265312a2f421cea26f20 |
| Huella del paquete (package_sha256) | 8a1efe2a9b9b9e259718b6998db0555f52c04808dc73e1d000aca02ec08c2fcb |
| Huella del envío (bundle_sha256) | 222caaa1b452d788c0a024b8f8853610eb9c8a11284bac644840798d544a9c94 |
| Huella del encargo | 022846e95b809a772317c2b17d6d946f3f91b9066c864911e473bb7ea15843e4 |
| Modelo pedido / devuelto | claude-opus-5-5 / claude-opus-5-5 |
| Esfuerzo | high |
| Mensajes enviados | 1 |
| Cota de entrada estimada antes de llamar | 814919 tokens |
| Reserva estimada antes de llamar | USD 3.915036 (máximo de la ejecución USD 5) |
| Reserva registrada | USD 3.915036 |
| Uso de tokens | entrada 342723, salida 23223 |
| Coste | CONOCIDO_ESTIMADO; estimado USD 1.835352; cota 1.835352 |

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

Estado `concluido` · cubo «Vigilar» · acción `esperar` · zona `cumple_regla_k`

| Escenario | Valor por acción | Probabilidad |
|---|---|---|
| malo | 18.8 | 0.2 |
| normal | 32.02 | 0.6 |
| bueno | 41.82 | 0.2 |

| Escalera (k = 3) | Declarado | Recalculado (Anexo C) |
|---|---|---|
| Precio actual | 27.28 | |
| Precio del escenario malo | 18.8 | 18.8 |
| P* | 27.76 | 27.7543 |
| Precio de Sí = mín(P*, V_normal) | 27.76 | 27.7543 |
| Ponderado | 31.34 | 31.336 |
| Crecimiento implícito al precio actual / del normal (%) | 0.7 / 4.5 | |

| Tasa | Precio de Sí | Ponderado | Zona |
|---|---|---|---|
| 7 % | 38.71 | 44.4 | cumple_regla_k |
| 8 % | 32.33 | 36.76 | cumple_regla_k |
| 9 % | 27.76 | 31.34 | cumple_regla_k |
| 10 % | 24.32 | 27.3 | vigilar |
| 11 % | 21.66 | 24.17 | caro |

### Resumen

    Jumbo es un minorista de hogar, temporada y juguetes en Grecia, Chipre, Bulgaria y Rumanía. No tiene deuda financiera, su retorno sobre el capital ronda el 26-27 % y genera caja libre de unos 230-250 mm al año. El valor se calcula con un DCF al accionista: FCF base de 241,45 mm (dato C52 de la hoja), diez años de crecimiento del −2 %, 4,5 % y 7,5 % según el escenario, crecimiento terminal del 1 %, 2 % y 2,5 %, y 65,6 mm de caja sobrante. La caja sobrante sale de los 200 mm de la etapa 1 menos la distribución extraordinaria de 1,00 € por acción (134,37 mm), porque el precio ya cotiza sin ella. Al 9 % salen 18,80 € (malo), 32,02 € (normal) y 41,82 € (bueno), con un ponderado de 31,34 €. El precio máximo que cumple la regla k = 3 es 27,76 €. A 27,28 € el precio queda dentro de la zona por solo 0,48 € (1,7 %). Esa holgura desaparece con un FCF base más prudente (232 mm: precio de Sí ≈ 26,7 €), si se quita la caja sobrante o con una tasa del 10 %. Los márgenes siguen bajando: el margen bruto pasa del 55,9 % en 2022 al 53,5 % en el primer semestre de 2026, y el EBITDA del 36,8 % al 32,7 %. Rumanía cae un 6,5 % y Grecia no abre tiendas en 2027. Conclusión: Vigilar y esperar a un precio que deje margen sobre los supuestos prudentes.


### Moneda

    EUR


### Justificación

    Estado concluido: el negocio se entiende, no hay deuda, el DCF simple es aplicable y los datos son suficientes. Cubo Vigilar y acción esperar. El precio cumple la regla k = 3 al 9 % por solo 0,48 € (1,7 %), y esa holgura depende de supuestos discutibles:
    - un FCF base que suma intereses cobrados (con 232 mm, el precio de Sí cae a ≈ 26,7 €);
    - 65,6 mm de caja sobrante estimada sin el anuncio de la distribución (sin ella, el precio de Sí queda en ≈ 27,27 €);
    - una r del 9 % inferior a la r mínima del 10,2 % que marca la hoja (al 10 %, zona vigilar).
    En paralelo, los márgenes bruto y EBITDA siguen bajando, Rumanía cae y Grecia no abre tiendas en 2027. No hay margen de error suficiente para comprar hoy; sí para vigilar con precio objetivo prudente de ≈ 26,5-26,7 €.


### Probabilidades

    Mantengo las probabilidades de partida 0,2/0,6/0,2. La amenaza de las plataformas y la compresión de margen ya están dentro de los escenarios malo y normal (crecimiento rebajado al 4,5 %), y subir la probabilidad del malo contaría dos veces lo mismo. La subiría a 0,3 si el margen bruto de 2026 cerrara por debajo del 53 %.


### Fórmula aplicada

    Para 18,80 ≤ P ≤ 32,02:
    G(P) = 0,6·(32,02 − P) + 0,2·(41,82 − P) = 27,577 − 0,8·P
    L(P) = 0,2·(P − 18,80) = 0,2·P − 3,761
    G = 3·L ⇒ 27,577 − 0,8·P = 0,6·P − 11,282 ⇒ P* = 38,859 / 1,4 = 27,76
    Precio de Sí = mín(27,76; 32,02) = 27,76
    Ponderado = 0,2·18,80 + 0,6·32,02 + 0,2·41,82 = 31,34
    Zona: precio 27,28 > 18,80 y 27,28 ≤ 27,76 ⇒ cumple_regla_k (holgura de 0,48 €)


### Crecimiento implícito

    Supongo que el FCF crece al ritmo de las ventas (margen de FCF constante). Dejo fijas el resto de hipótesis del escenario normal: FCF base 241,454, crecimiento del 4,5 % en los años 6-10, terminal del 2 %, r = 9 % y caja sobrante de 65,6. Busco el crecimiento de los años 1-5 que iguala el valor al precio. Valor necesario: 27,28 × 134,366 = 3.665,5 mm; menos 65,6 = 3.599,9 mm; entre 241,454 = múltiplo 14,91. El múltiplo vale 14,43 con un 0 % y 15,08 con un 1 %. Interpolando, el precio descuenta un crecimiento de ~0,7 % anual a cinco años, frente al 4,5 % del escenario normal.

### Escenario malo

    Las plataformas transfronterizas, el flete y el dólar quitan precio y volumen. El margen EBITDA baja hacia el 25-28 %. El FCF cae un 2 % anual durante 10 años y después crece un 1 % para siempre. Datos de partida: FCF base 241,454 mm (C52 = C46 316,475 − capex 63,788 − intereses de arrendamientos 2,664 − principal 8,569) y caja sobrante de 65,6 mm (200 − 134,37 de la distribución extraordinaria). Cálculo: múltiplo 5,834 (años 1-10) + 4,357 (terminal) = 10,192. Resultado: 10,192 × 241,454 = 2.460,8 mm; más 65,6 mm = 2.526,4 mm; entre 134,366 M de acciones = 18,80 €.

### Escenario normal

    Unas dos aperturas al año, ventas comparables cerca de la inflación y franquicias creciendo. El margen se queda algo por debajo del de 2025. Pongo un 4,5 % y no el 5 % de la etapa 1 por tres razones: Grecia sin hiperstore en 2027, Rumanía −6,5 % en el primer semestre y EBITDA del 32,73 % en el primer semestre. Contraste: ventas +7,2 % en 2025 y ~+6 % de enero a agosto de 2026. El FCF crece un 4,5 % anual durante 10 años y después un 2 % para siempre. Cálculo: múltiplo 7,989 + 9,559 = 17,548. Resultado: 17,548 × 241,454 = 4.236,9 mm; más 65,6 mm; entre 134,366 = 32,02 €.

### Escenario bueno

    Rumanía duplica tiendas en una década, las franquicias y Balfin abren mercados sin capital propio de Jumbo y el margen aguanta. El FCF crece un 7,5 % anual durante 10 años y después un 2,5 % para siempre. Cálculo: múltiplo 9,274 + 13,729 = 23,003. Resultado: 23,003 × 241,454 = 5.554,1 mm; más 65,6 mm; entre 134,366 = 41,82 €. Contraste con la etapa 1 (FCF base 232,15, caja sobrante 200, 5 % y 8 %): 19,10 / 32,96 / 42,76 €.

### Sensibilidad (comentarios)

    7 %: Valores por escenario: malo 24,49, normal 45,24, bueno 61,81. P* = 54,20 / 1,4 = 38,71. Holgura amplia, pero el 7 % está por debajo de la tasa del ejercicio.
    8 %: Valores por escenario: malo 21,25, normal 37,52, bueno 49,98. P* = 45,26 / 1,4 = 32,33.
    9 %: Coincide con la escalera: malo 18,80, normal 32,02, bueno 41,82. Holgura de solo 0,48 € sobre el precio.
    10 %: Valores por escenario: malo 16,89, normal 27,91, bueno 35,87. El precio de 27,28 queda casi en el ponderado. La hoja marca una r mínima del 10,2 %.
    11 %: Valores por escenario: malo 15,36, normal 24,72, bueno 31,35. El precio supera el ponderado.

### Qué haría falsa la conclusión

    - Hacia Sí: precio por debajo de ≈ 26,5 € con el negocio intacto, que cumple la regla k también con el FCF base prudente de 232 mm.
    - Hacia Sí: cierre de 2026 con margen bruto ≥ 54,5 % y margen EBITDA ≥ 34 %, que estabilizaría el escenario normal y permitiría el 5 % de crecimiento.
    - Hacia No: margen bruto anual de 2026 por debajo del 53 % o margen EBITDA por debajo del 32 %, que subiría la probabilidad del malo a 0,3 y dejaría el precio de Sí por debajo de ~25 €.
    - Hacia No: beneficio neto de 2026 y 2027 por debajo de 320 mm, o ventas de Rumanía en caída en el conjunto de 2026.
    - Hacia No: inventario a 31-12-2026 creciendo otra vez muy por encima de las ventas (en 2025 fue +19 % frente a +7,2 %) y FCF por debajo de 200 mm dos años seguidos.
    - Hacia No o demasiado difícil: uso de la caja en una adquisición no relacionada, en capital para Balfin o en inmuebles no comerciales, o desvío de coste en los centros de distribución (más de 95 mm en tres años).
    - Hacia demasiado difícil: caída de ventas comparables que no se pueda separar entre competencia de las plataformas y ciclo de consumo.

### Lo que no sabe

    - El paquete no contiene el anuncio de la distribución extraordinaria de 1,00 € (ex 16-11-2026). Solo la nota de la hoja lo menciona y lo describe como propuesta sujeta al consejo. Lo trato como ejecutado porque la fuente del precio dice que este cotiza ex distribución, y por eso resto 134,37 mm de los 200 mm de caja sobrante de la etapa 1.
    - Desconozco la caja real a mediados de noviembre de 2026 (antes de Navidad, con inventario alto). Los 65,6 mm de caja sobrante son una estimación. Las reducciones de capital de las filiales (69,52 y 19,88 mm) son intragrupo y no cambian la caja consolidada.
    - El FCF base de 241,45 mm suma intereses cobrados de 2023-2025 sobre una caja mayor que la actual. Con tipos de depósito del 1,75-2,75 % y menos caja, ese ingreso bajará. La variante sin intereses (232,15 mm) da un precio de Sí de ≈ 26,7 €.
    - La lectura del precio y de la tasa sin riesgo se hizo el 18-11-2026, posterior al corte. Solo uso el cierre del 17-11-2026, que es anterior. La tasa sin riesgo no la uso porque la r está fijada en el 9 %.
    - Faltan en las fuentes: ventas comparables, tráfico y ventas por m²; margen por categoría; cuota de las plataformas transfronterizas; capex presupuestado para 2026; coste de los centros tras la revisión de Oinofyta; capital comprometido con Balfin; política de dividendos.
    - Varios ceros de la historia (SBC, minoritarios, arrendamientos antes de 2019) están pendientes de verificación humana. Su efecto en el valor es nulo o mínimo.
    - El cruce de etiquetas «Lease repayments» / «Interest paid for leases» no está explicado en los textos. El total restado (≈ 11,2 mm) no cambia.
    - El efecto de que el tipo del impuesto de sociedades en Chipre suba al 15 % desde 2026 (Pilar II) no está modelizado por separado. Es menor.

### Citas

    [datos_v63_md] «Previous Close: 27,2800 EUR» → Precio actual de 27,28 € (cierre del 17-11-2026).
    [datos_v63_md] «Precio posterior a la fecha ex (16-nov-2026) de la distribución extraordinaria de 1,00 € por acción: sin derecho a ella.» → El precio ya no incluye la distribución de 1,00 €.
    [datos_v63_md] «134,37 (1,00 € extraordinario ANUNCIADO, ex 16.11 / pago 20.11.2026» → Salida de caja de 134,37 mm que resto de la caja sobrante.
    [datos_v63_md] «Quedan ~200 mm claramente sobrantes (≤ C53).» → Caja sobrante de la etapa 1 (200 mm). Cálculo: 200 − 134,37 = 65,6 mm.
    [fuentes_ar_2025_seleccion] «134.365.561 ordinary registered shares with a nominal value of €0,88 each» → Número de acciones (134,366 M), sin dilución.
    [datos_v63_md] «FCF base (C52, fórmula): 241.454» → FCF base usado en los tres escenarios.
    [datos_v63_md] «(334,957 + 309,713 + 304,755) / 3 = 316,4750 → 316,475» → CFO ajustado medio 2023-2025 (C46) que entra en el FCF base.
    [datos_v63_md] «86,6412 / 66,3383 / 38,384» → Capex 2023-2025, media de 63,788 mm.
    [fuentes_ar_2025_seleccion] «Net cash flows from operating activities 296.912.917 300.687.098 151.095.759 182.343.360» → CFO del grupo en 2025 y 2024.
    [fuentes_ar_2025_seleccion] «Lease repayments (2.325.789) (3.001.882) (1.821.081) (1.946.824)» → Pagos por arrendamientos en financiación que se restan del FCF.
    [fuentes_ar_2025_seleccion] «Interest paid for leases (9.727.205) (8.533.836) (6.333.624) (6.113.854)» → Pagos por arrendamientos en financiación que se restan del FCF.
    [fuentes_ar_2025_seleccion] «Interest received 9.916.790 13.791.382 3.004.653 5.106.255» → Intereses cobrados, en descenso, que forman parte de C46.
    [fuentes_h1_2026_compact] «Cash and cash equivalents 4.15 546.140.091 536.668.758 234.183.560 180.572.205» → Caja de 546,14 mm a 30-06-2026.
    [fuentes_h1_2026_compact] «It is noted that neither the Company nor the Group has any borrowings.» → Sin deuda financiera: el DCF al accionista es aplicable.
    [fuentes_h1_2026_compact] «€94.055.892,70, based on the Company’s 134.365.561 shares» → Dividendo de 0,70 € pagado en julio de 2026, ya descontado de la caja sobrante de la etapa 1.
    [extracto_v63_md] «Margen bruto del grupo: 2025 54,72 % (2024 55,61 %)» → Compresión del margen bruto.
    [extracto_v63_md] «H1 2026 53,53 % (H1 2025 53,86 %)» → Compresión del margen bruto en el primer semestre de 2026.
    [extracto_v63_md] «Margen EBITDA del grupo: 2025 35,34 % (2024 36,77 %)» → Compresión del margen EBITDA.
    [extracto_v63_md] «H1 2026 32,73 % (H1 2025 33,25 %)» → Compresión del margen EBITDA en el primer semestre de 2026.
    [extracto_v63_md] «H1 2026: Grecia +7,08 %; Chipre +3,92 %; Bulgaria +10,78 %; Rumanía −6,50 % (decreased by 6,50 %)» → Crecimiento por país y caída de Rumanía.
    [fuentes_h1_2026_compact] «increased by approximately 6% compared to the corresponding period last year.» → Ventas de enero a agosto de 2026 +6 %, contraste del escenario normal.
    [fuentes_h1_2026_compact] «2027 is expected to be a transitional year» → Sin aperturas en Grecia en 2027, motivo para rebajar el normal al 4,5 %.
    [fuentes_ar_2025_seleccion] «Profit after income tax 320.309.417 320.096.756 252.943.196 254.112.412» → Beneficio neto plano en 2025.
    [extracto_v63_md] «expected to exceed € 95 million over the next three years» → Inversión prevista en centros de distribución.
    [fuentes_ar_2025_seleccion] «often through practices that may disrupt the level playing field of the market» → Amenaza de las plataformas transfronterizas (escenario malo).
    [fuentes_ar_2025_seleccion] «70% of the Group’s products come from Asia and especially China» → Dependencia del suministro asiático.
    [extracto_v63_md] «26,58 % a 30.06.2026 (25,25 % a 30.06.2025)» → ROCE alto que sostiene el crecimiento terminal del 2 %.
    [etapa1_jumbo_analisis_csv] «VALOR INTRÍNSECO POR ACCIÓN,19.0970081849587,32.9584114228985,42.7641479713337» → Contraste con los valores de la etapa 1.
    [datos_v63_md] «tu r (9.0 %) < r mínima (10.2 %)» → La tasa del 9 % está por debajo de la r mínima de la hoja, por eso miro la sensibilidad al 10 %.

### Comprobaciones mecánicas y normalizaciones

    {
      "comprobaciones": {
        "escalera_recalculada_anexo_c": {
          "p_estrella": 27.754285714285714,
          "precio_si": 27.754285714285714,
          "ponderado": 31.336000000000002,
          "precio_escenario_malo": 18.8
        },
        "citas_total": 29,
        "citas_literales": 29,
        "avisos": [],
        "nota": "Comprobaciones mecánicas informativas: no acreditan la calidad económica."
      },
      "normalizaciones_enum": []
    }

