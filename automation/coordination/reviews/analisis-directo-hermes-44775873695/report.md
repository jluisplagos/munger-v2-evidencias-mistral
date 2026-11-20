# Análisis directo · Hermes, etapa 1 del universo (hoja del 2026-10-08)

Estado de la ejecución: `AUDITORIA_DOCUMENTAL_PENDIENTE_ACEPTACION`

Revisión a ciegas pendiente. No es aceptación, ni integración, ni aptitud para dinero real.

| Campo | Valor |
|---|---|
| Empresa | hermes |
| Fecha de corte | 2026-10-08 |
| Tasa | 9 % |
| Tarea | analisis-directo-hermes-44775873695 |
| SHA del código | fcb18bba533554c32f9756d6fb49dc0ebcc2946c |
| Huella del paquete (package_sha256) | 2e30ec9f118f22fab84a26cf2457d9da73c3d141a78298d66428398b52c9b82e |
| Huella del envío (bundle_sha256) | 3c8771d88f94fea68a56e4bc49eabcb861547518b7cfb275cffbbf7a37bb0c29 |
| Huella del encargo | 022846e95b809a772317c2b17d6d946f3f91b9066c864911e473bb7ea15843e4 |
| Modelo pedido / devuelto | claude-opus-5-5 / claude-opus-5-5 |
| Esfuerzo | high |
| Mensajes enviados | 1 |
| Cota de entrada estimada antes de llamar | 133627 tokens |
| Reserva estimada antes de llamar | USD 1.189868 (máximo de la ejecución USD 3) |
| Reserva registrada | USD 1.189868 |
| Uso de tokens | entrada 60375, salida 15306 |
| Coste | CONOCIDO_ESTIMADO; estimado USD 0.54762; cota 0.54762 |

## Paquete de entrada

| id | ruta | commit | sha256 | bytes |
|---|---|---|---|---|
| respuesta | datos_analisis_directo/hermes/etapa1/Hermes_respuesta.md | fcb18bba5335 | 179ad694e610a95c4ab1d77597c96d4165a6c97d879c1ed7ca3d00362d1fc08c | 26522 |
| hoja_analisis | datos_analisis_directo/hermes/etapa1/Hermes_evaluada__Análisis.csv | fcb18bba5335 | 877d4da445bba796e4b9ab92f4d07e807586bafd35da514036cdc832da396953 | 22999 |
| hoja_guia_simply_wall_st | datos_analisis_directo/hermes/etapa1/Hermes_evaluada__Guía_Simply_Wall_St.csv | fcb18bba5335 | 2791cc208d21b779b2104db9848a271eded2ae7cb4392769b743a2d95f8c3e2f | 7794 |
| hoja_opciones | datos_analisis_directo/hermes/etapa1/Hermes_evaluada__Opciones.csv | fcb18bba5335 | b9f97b6706b77f7a28f70140d212f0790ee7334eb22965a4f538963e777a1a73 | 1537 |
| hoja_control_maestro | datos_analisis_directo/hermes/etapa1/Hermes_evaluada__Control_maestro.csv | fcb18bba5335 | 8e9c75b18b454f57177ec4ff62c2ce04389166253769a4b527ac68abbe8094b5 | 53214 |

## Salida del modelo (datos, sin acciones ejecutables)

Estado `concluido` · cubo «Vigilar» · acción `esperar` · zona `caro`

| Escenario | Valor por acción | Probabilidad |
|---|---|---|
| malo | 523.33 | 0.2 |
| normal | 792.7 | 0.6 |
| bueno | 1191.9 | 0.2 |

| Escalera (k = 3) | Declarado | Recalculado (Anexo C) |
|---|---|---|
| Precio actual | 1280 | |
| Precio del escenario malo | 523.33 | 523.33 |
| P* | 734.28 | 734.2843 |
| Precio de Sí = mín(P*, V_normal) | 734.28 | 734.2843 |
| Ponderado | 818.66 | 818.666 |
| Crecimiento implícito al precio actual / del normal (%) | 19.4 / 7 | |

| Tasa | Precio de Sí | Ponderado | Zona |
|---|---|---|---|
| 7 % | 1051.29 | 1193.96 | caro |
| 8 % | 863.84 | 971.07 | caro |
| 9 % | 734.28 | 818.66 | caro |
| 10 % | 639.43 | 708.01 | caro |
| 11 % | 567.04 | 624.15 | caro |

### Resumen

    Hermès es un negocio de calidad alta y fácil de explicar. Vende objetos artesanales escasos en tiendas propias, cobra al contado, tiene un margen operativo recurrente cercano al 41 % y no tiene deuda financiera. Valoro la caja libre base de 3.487,3 M€ (media FY23–25 neta de arrendamientos y SBC) a diez años, con un valor terminal, una tasa del 9 %, 6.000 M€ de caja sobrante y 105,003 M de acciones diluidas. Los valores por acción son 523,33 € (malo), 792,70 € (normal) y 1.191,90 € (bueno). El ponderado es 818,66 € y el precio de Sí con k = 3 es 734,28 €. A 1.280 € (cierre del 7-oct-2026) la acción está por encima incluso del escenario bueno. El precio descuenta un crecimiento de la caja libre de alrededor del 13,7 % anual durante diez años, o del 19,4 % durante cinco años si después vuelve al 7 %. Cubo Vigilar, acción esperar.


### Moneda

    EUR


### Justificación

    Doy el análisis por concluido: el modelo es aplicable (caja libre positiva y estable, sin deuda financiera, financiación estable) y los datos necesarios están en el paquete. El cubo es Vigilar y no No ni Demasiado difícil, porque el negocio se entiende y es de calidad. Lo que falla es el precio: 1.280 € supera el ponderado (818,66 €), el precio de Sí (734,28 €) e incluso el escenario bueno (1.191,90 €). La conclusión resiste a todas las tasas entre el 7 % y el 11 % (zona caro siempre) y a variaciones razonables de la caja sobrante o de la base de caja libre. Acción: esperar.


### Probabilidades

    Mantengo las de partida (0,2 / 0,6 / 0,2). La desaceleración ya está recogida en el escenario normal (7 % frente al 14 % histórico) y no hay un hecho concreto que obligue a sesgar hacia el malo o hacia el bueno. Además, la conclusión no cambia con sesgos razonables, porque incluso el escenario bueno vale menos que el precio.


### Fórmula aplicada

    Para P entre V_malo y V_normal:
    - G(P) = 0,6·(792,70 − P) + 0,2·(1.191,90 − P) = 714,00 − 0,8·P
    - L(P) = 0,2·(P − 523,33)
    - G = 3L ⇒ P* = (0,6·792,70 + 0,2·1.191,90 + 0,6·523,33) / 1,4 = 1.028,00 / 1,4 = 734,28
    - Precio de Sí = mín(734,28; 792,70) = 734,28
    - Ponderado = 0,2·523,33 + 0,6·792,70 + 0,2·1.191,90 = 818,66
    - Precio 1.280 > 818,66 ⇒ zona caro


### Crecimiento implícito

    El modelo proyecta caja libre, no ventas. Con el margen constante del escenario normal, el crecimiento de la caja libre equivale al de las ventas. Planteo el DCF inverso así: crecimiento x en los años 1–5, 7 % en los años 6–10, 2,5 % a perpetuidad, tasa del 9 %, 6.000 M€ de caja sobrante y 105,003 M de acciones. Igualar el valor a 1.280 € exige que el valor total sea 36,82 veces la caja libre base, y eso da x ≈ 19,4 % anual (interpolando entre 19 % y 20 %). Si el crecimiento se aplica a los diez años, la hoja da 13,72 %, por encima incluso del 12 % del escenario bueno. Las dos cifras son cálculo mío o de la hoja, no de la empresa.

### Escenario malo

    La ola post-Covid se agota. Las ventas crecen un 4–5 % a tipos constantes, las divisas restan 1–2 puntos y el margen baja hacia el 36–37 %. La caja libre crece un 2 % anual en los años 1–10 y un 1,5 % a perpetuidad. Base de caja libre: 3.487,3 M€ = 4.947 − 1.029 − 0 − 304,7 − 126 (medias FY23–25). Se suman 6.000 M€ de caja sobrante y se divide entre 105,003 M de acciones. Cálculo: valor actual de los años 1–10 (24.649 M€) + terminal (24.301 M€) + 6.000 M€ = 54.951 M€, es decir, 523,33 €/acción.

### Escenario normal

    Cada año abre un taller de piel más y hay algo de subida de precio. Resultado: ventas +6–8 % a tipos constantes, margen cerca del 40 % y capex en torno al 7 % de las ventas. La caja libre crece un 7 % en los años 1–10 y un 2,5 % a perpetuidad, con la misma base de 3.487,3 M€ y la misma caja sobrante de 6.000 M€. Cálculo: 31.540 + 45.695 + 6.000 = 83.236 M€, es decir, 792,70 €/acción. Es coherente con el +9 % a tipos constantes de 2025 y el +6 % del primer semestre de 2026.

### Escenario bueno

    La escasez y la capacidad nueva sostienen crecimientos de dos dígitos, como en 2017–2019 y en piel en 2024–2025. La caja libre crece un 12 % en los años 1–10 y un 3 % a perpetuidad, con la misma base y la misma caja sobrante. Cálculo: 40.613 + 78.540 + 6.000 = 125.153 M€, es decir, 1.191,90 €/acción. Aun así queda un 7 % por debajo del precio.

### Sensibilidad (comentarios)

    7 %: V: malo 694,62, normal 1.145,75 y bueno 1.837,97. P* = 1.051,29. El ponderado coincide con la hoja (1.193,97). El precio sigue por encima del ponderado.
    8 %: V: malo 595,77, normal 936,78 y bueno 1.449,26. P* = 863,84.
    9 %: Caso base. Coincide con la escalera y con la hoja (818,66).
    10 %: V: malo 467,96, normal 687,54 y bueno 1.009,51. P* = 639,43.
    11 %: V: malo 424,29, normal 607,52 y bueno 873,88. El ponderado coincide con la hoja (624,14).

### Qué haría falsa la conclusión

    - A Sí: una cotización igual o inferior a unos 734 € con el negocio intacto (crecimiento a tipos constantes ≥ 6 %, margen operativo recurrente ≥ 40 %, sin cambios de gestión).
    - Subiría el valor de forma material si se publicaran ventas a tipos constantes del ejercicio completo 2026 y 2027 por encima del 10 % sin ayuda de divisas, o datos de volumen que sostengan un crecimiento normal del 9–12 %. Aun así, para justificar 1.280 € haría falta ~13,7 % anual durante diez años.
    - A No: un margen bruto por debajo del 67 % sin causa de divisas, ventas de piel cayendo con talleres ociosos, una adquisición grande fuera del núcleo o más dinero hacia partes vinculadas (RDAI, Ardian).
    - A Demasiado difícil: dos años con Asia sin Japón plana y el resto de regiones compensando solo con precio, de modo que el valor pase a depender de predecir el consumo chino o el euro.
    - Que la contribución fiscal francesa se haga permanente y el tipo efectivo suba al 33–35 %. Bajaría el escenario normal, pero reforzaría la zona caro.

### Lo que no sabe

    - Algunos datos del paquete son posteriores a la fecha de corte (2026-10-08) y no los uso como evidencia: la revisión de la respuesta del 25-oct-2026 y las 'decisiones del inversor' del 11-oct-2026 en el Control maestro (periodo del FCF base, C31). Las cifras históricas que uso (medias FY23–25 de CFO, capex, arrendamientos y SBC) son anteriores al corte y la elección de la media a tres años es mía.
    - El precio de 1.280 € es el cierre del 7-oct-2026, tomado de agregadores. No tengo una cotización del 8-oct-2026.
    - No sé cuánto del crecimiento es precio y cuánto volumen. La empresa no publica unidades, subidas de precio ni listas de espera. Es la variable central del foso.
    - No tengo previsiones de ventas ni un modelo por márgenes. El crecimiento implícito se obtiene sobre la caja libre suponiendo un margen constante, así que el dato a cinco años es una aproximación mía.
    - La caja sobrante de 6.000 M€ es un juicio heredado: caja de 12.310 M€, menos unos 2.000 M€ operativos, menos unos 4.000 M€ para no contar dos veces su rendimiento, que ya está en el CFO. Con el exceso central del Control maestro (≈10.800 M€) el valor subiría ≈46 €/acción, sin cambiar la zona.
    - La base de caja libre de 3.487,3 M€ es más prudente que la de los últimos doce meses (4.216 M€ antes de SBC). Con 4.084 M€ (LTM menos SBC) el valor normal sería ≈919 €, todavía por debajo del precio.
    - La tasa del 9 % es una convención del ejercicio, no la r de un inversor concreto. Referencias del paquete: Bund al 3,49 % y WACC de deterioro de Hermès del 9,16 %.
    - Los informes no nombran competidores ni cuotas de mercado. Tampoco sé el peso real del cliente chino, incluido el turista, ni el retorno del capex inmobiliario.
    - La respuesta de la etapa 1 estimaba un precio de Sí de ≈520 € con otra regla (mín(V_malo; 0,75·ponderado)). Aquí aplico la regla k = 3 del encargo, que da 734,28 €.
    - El P/FCF histórico (57,9x de media) y el valor de Simply Wall St (856,32 €) son contexto secundario y no los uso para valorar.

### Citas

    [hoja_analisis] «Precio actual,Cotización por acción.,1280» → Precio actual usado: 1.280 €.
    [hoja_control_maestro] «Último cierre disponible a las 10:41 CEST del 8-oct-2026, con el mercado abierto.» → El precio es el cierre del 7-oct-2026.
    [hoja_control_maestro] «Serie FY21–25: 3,405 · 4,184 · 4,328 · 5,139 · 5,374» → CFO medio FY23–25 = (4.328 + 5.139 + 5.374) / 3 = 4.947.
    [hoja_control_maestro] «Serie: 532 · 518 · 859 · 1,067 · 1,161.» → Capex medio FY23–25 = 1.029.
    [hoja_control_maestro] «Serie: 212 · 261 · 277 · 305 · 332.» → Principal de arrendamientos medio FY23–25 = 304,7.
    [hoja_control_maestro] «Serie FY21–25: 59 · 55 · 104 · 142 · 132.» → SBC media FY23–25 = 126.
    [hoja_analisis] «3487.3,✓ PASA» → Caja libre base normalizada: 3.487,3 M€.
    [hoja_control_maestro] «105.003 (105,002,977 diluidas medias del H1 2026).» → Acciones diluidas usadas en el valor por acción.
    [hoja_control_maestro] «12,310 = tesorería 1,934 + valores negociables 10,376.» → Caja a 30-jun-2026.
    [respuesta] «Queda 6.000 M€, por debajo de C53. Rango 4.000–10.000 M€ (±20–40 € por acción).» → Caja sobrante sumada en los tres escenarios.
    [hoja_control_maestro] «Incluye ingresos financieros de la caja: 286 M€ antes de impuestos en FY25 (ver C76).» → El rendimiento de la caja ya está en el CFO; por eso no se suma toda la caja.
    [hoja_control_maestro] «exceso central ≈10,8 bn€ ≈103 €/acción (rango 96–115)» → Alternativa de caja sobrante para la sensibilidad.
    [hoja_control_maestro] «2,284 = deuda financiera 5 (1 de descubiertos + 4 de opciones de venta de minoritarios) + pasivos por arrendamiento IFRS 16 2,279.» → No hay deuda financiera relevante: el modelo es aplicable.
    [hoja_analisis] «Crecimiento de la caja libre · años 1–10,0.02,0.07000000000000001,0.12» → Crecimientos de los escenarios en los años 1–10.
    [hoja_analisis] «Crecimiento para siempre · desde el año 11,0.015,0.025,0.03» → Crecimientos terminales de los escenarios.
    [hoja_analisis] «VALOR INTRÍNSECO POR ACCIÓN,523.326651971495,792.700334163593,1191.896361979» → Valores por acción al 9 %, que coinciden con mi recálculo.
    [hoja_analisis] «818.664803288254» → Valor ponderado al 9 %.
    [hoja_analisis] «0.137201123580109,✗ BANDERA · > BUENO» → DCF inverso a diez años: 13,7 % de crecimiento implícito.
    [hoja_analisis] «r − 2 pts (7.0%),1108.74149762405,1193.96646922352,1301.27725940455» → Comprobación del ponderado al 7 %.
    [hoja_analisis] «r + 2 pts (11.0%),606.533334065698,624.144869738541,643.984125711339» → Comprobación del ponderado al 11 %.
    [respuesta] «Crecimiento a tipos constantes 9, 10, 12, −6, 42, 23, 21, 15 y 9 % (2017–2025) y +6 % en el primer semestre de 2026.» → Historial de crecimiento y desaceleración reciente.
    [respuesta] «Margen operativo recurrente 40,5 / 42,1 / 40,5 / 41,0 % (2022–2025) y 41,0 % en el primer semestre de 2026 (41,4 % un año antes).» → Margen estable, supuesto del escenario normal.
    [respuesta] «Asia sin Japón es el 42 % de las ventas y creció un 2 % cst en el primer semestre de 2026» → Riesgo principal del escenario malo.
    [respuesta] «las divisas restando 3,4 puntos en 2025 y 4,5 en el primer semestre de 2026» → Presión de las divisas sobre el crecimiento en euros.
    [hoja_control_maestro] «CFO 5,743 − capex 1,189 − intereses fuera del CFO 0 − principal de leases 338 − cupones de híbridos 0 = 4,216 (estado actual).» → Caja libre de los últimos doce meses, usada como sensibilidad de la base.
    [hoja_control_maestro] «Media 5 años: 57,9x (60,4 · 44,4 · 63,0 · 64,6 · 57,3). Mediana 60,4x. Actual (LTM): 31,8x.» → Contexto del múltiplo histórico frente al terminal implícito (~15,8x).
    [respuesta] «v1 · revisada el 25-oct-2026: sin cambios de valor.» → Material posterior a la fecha de corte, no usado como evidencia.
    [hoja_control_maestro] «Decisión del inversor (11-oct-2026): media 3 años FY23–25» → Decisión posterior al corte; la elección de la media a tres años la rehago con datos históricos.

### Comprobaciones mecánicas y normalizaciones

    {
      "comprobaciones": {
        "escalera_recalculada_anexo_c": {
          "p_estrella": 734.2842857142857,
          "precio_si": 734.2842857142857,
          "ponderado": 818.666,
          "precio_escenario_malo": 523.33
        },
        "citas_total": 28,
        "citas_literales": 28,
        "avisos": [],
        "nota": "Comprobaciones mecánicas informativas: no acreditan la calidad económica."
      },
      "normalizaciones_enum": []
    }

