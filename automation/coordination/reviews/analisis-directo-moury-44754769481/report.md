# Análisis directo · Moury, etapa 1 del universo (hoja del 2026-10-31)

Estado de la ejecución: `AUDITORIA_DOCUMENTAL_PENDIENTE_ACEPTACION`

Revisión a ciegas pendiente. No es aceptación, ni integración, ni aptitud para dinero real.

| Campo | Valor |
|---|---|
| Empresa | moury |
| Fecha de corte | 2026-10-31 |
| Tasa | 9 % |
| Tarea | analisis-directo-moury-44754769481 |
| SHA del código | 779b55abd380e8427650233fcb8a9c9fa74472f4 |
| Huella del paquete (package_sha256) | 65c8355a61a36129ada87456e201c5b1881d8033bc6cb299428f2b2bf3e8d73f |
| Huella del envío (bundle_sha256) | a546d1a735de0d12eb696d350abe4aa1cd67b4da51ac67e7d3c7458274e40e21 |
| Huella del encargo | 022846e95b809a772317c2b17d6d946f3f91b9066c864911e473bb7ea15843e4 |
| Modelo pedido / devuelto | claude-opus-5-5 / claude-opus-5-5 |
| Esfuerzo | high |
| Mensajes enviados | 1 |
| Cota de entrada estimada antes de llamar | 132460 tokens |
| Reserva estimada antes de llamar | USD 1.1852 (máximo de la ejecución USD 3) |
| Reserva registrada | USD 1.1852 |
| Uso de tokens | entrada 58863, salida 24217 |
| Coste | CONOCIDO_ESTIMADO; estimado USD 0.719792; cota 0.719792 |

## Paquete de entrada

| id | ruta | commit | sha256 | bytes |
|---|---|---|---|---|
| respuesta | datos_analisis_directo/moury/etapa1/Moury_respuesta.md | 779b55abd380 | 9cae644803d7e8fc746a798555592c51bd2e6b7dd25074dd06f725e24f7083f5 | 28782 |
| hoja_analisis | datos_analisis_directo/moury/etapa1/Moury_evaluada__Análisis.csv | 779b55abd380 | de90ec95371f4ef88d8dfeab268a502cba378d98ee91d586f5d860b42701f599 | 23089 |
| hoja_guia_simply_wall_st | datos_analisis_directo/moury/etapa1/Moury_evaluada__Guía_Simply_Wall_St.csv | 779b55abd380 | 2791cc208d21b779b2104db9848a271eded2ae7cb4392769b743a2d95f8c3e2f | 7794 |
| hoja_opciones | datos_analisis_directo/moury/etapa1/Moury_evaluada__Opciones.csv | 779b55abd380 | b9f97b6706b77f7a28f70140d212f0790ee7334eb22965a4f538963e777a1a73 | 1537 |
| hoja_control_maestro | datos_analisis_directo/moury/etapa1/Moury_evaluada__Control_maestro.csv | 779b55abd380 | f14ab0e82e81e5c385bd23a18d00157aae3ec76f20ccbe6674220f7a7a660920 | 49957 |

## Salida del modelo (datos, sin acciones ejecutables)

Estado `concluido` · cubo «Sí» · acción `comprar` · zona `cumple_regla_k`

| Escenario | Valor por acción | Probabilidad |
|---|---|---|
| malo | 544.87 | 0.2 |
| normal | 1126.04 | 0.6 |
| bueno | 2025.58 | 0.2 |

| Escalera (k = 3) | Declarado | Recalculado (Anexo C) |
|---|---|---|
| Precio actual | 680 | |
| Precio del escenario malo | 544.87 | 544.87 |
| P* | 1005.47 | 1005.4729 |
| Precio de Sí = mín(P*, V_normal) | 1005.47 | 1005.4729 |
| Ponderado | 1189.71 | 1189.714 |
| Crecimiento implícito al precio actual / del normal (%) | -13.1 / 0 | |

| Tasa | Precio de Sí | Ponderado | Zona |
|---|---|---|---|
| 7 % | 1350.93 | 1627.54 | cumple_regla_k |
| 8 % | 1149.15 | 1371.02 | cumple_regla_k |
| 9 % | 1005.47 | 1189.71 | cumple_regla_k |
| 10 % | 897.78 | 1054.68 | cumple_regla_k |
| 11 % | 813.95 | 950.17 | cumple_regla_k |

### Resumen

    Moury Construct es una constructora valona controlada por su familia. Cobra por avance de obra, casi no necesita capex, trabaja con circulante negativo y tiene 109,5 M€ de caja frente a 1,7 M€ de deuda. No sé si su margen operativo del 15 % (2022-2025, frente al 5-6 % de 2016-2019) es de la empresa o del momento. Por eso no fijo el valor apostando por el margen: acoto la pérdida con un escenario malo anclado en su propio historial. Con un FCF base de 31,37 M€ y la tasa del 9 %, los valores por acción son 544,87 € (malo: vuelta al margen histórico y devolución de circulante), 1.126,04 € (normal: FCF nominal plano diez años, es decir, erosión parcial del margen) y 2.025,58 € (bueno: el margen aguanta y el FCF crece un 8 % anual). El ponderado es 1.189,71 € y el precio de Sí según la regla k = 3 es 1.005,47 €. A 680 € el precio cumple la regla con holgura: con la probabilidad del malo al 0,5, el umbral sería unos 735 €, todavía por encima. La pérdida en el escenario malo es del orden del 20 % y la ganancia en el normal es del 66 %. Concluyo Sí con acción comprar. La conclusión no depende de explicar el margen, sino de que el escenario malo con márgenes de su historial sea un suelo creíble y de que la caja acabe llegando al minoritario.


### Moneda

    EUR


### Justificación

    El análisis está concluido porque la hipótesis decisiva, la persistencia del margen, se puede acotar. El peor caso razonable es volver a los márgenes del propio historial (2016-2019) con devolución de circulante, y eso deja el valor en unos 545 €: una pérdida del orden del 20 % frente a 680 €, no una ruina. Ayudan la caja neta, el capex mínimo y la ausencia de deuda y de SBC. Con esos escenarios, el precio actual cumple la regla k = 3 con margen. Sigue cumpliéndola con tasas del 7 % al 11 % y con probabilidades del malo de hasta 0,5. Por eso el cubo es Sí y la acción es comprar. No elijo demasiado_dificil, como hizo la etapa 1, porque esa conclusión se apoyaba en una regla distinta (el menor entre el malo y ¾ del ponderado). Además, no saber explicar el margen no impide ver que el precio ya descuenta un FCF a la baja: el crecimiento implícito es de alrededor del -13 % anual en cinco años. Riesgos que asumo y no compenso con la cifra: el controlador (55,41 %) decide sobre la caja, hay operaciones vinculadas y la liquidez es muy baja.


### Probabilidades

    Mantengo 0,2 / 0,6 / 0,2. El riesgo de que el margen vuelva atrás ya está recogido en los supuestos y no lo penalizo dos veces. El malo usa el crecimiento mínimo (-10 %), el terminal más bajo (1 %) y menos caja (30 M€). El normal ya incorpora una erosión del margen (FCF plano en lugar de +3 %). Como comprobación, con 0,4 / 0,45 / 0,15 el precio de Sí sería de unos 814 €, y con 0,5 / 0,4 / 0,1, de unos 735 €. En ambos casos sigue por encima de 680 €.


### Fórmula aplicada

    Para 544,87 ≤ P ≤ 1.126,04:
    G(P) = 0,6·(1.126,04 - P) + 0,2·(2.025,58 - P) = 1.080,74 - 0,8P
    L(P) = 0,2·(P - 544,87) = 0,2P - 108,97
    G ≥ 3L  ⇔  1.080,74 - 0,8P ≥ 0,6P - 326,92  ⇔  P ≤ 1.407,66 / 1,4 = 1.005,47 = P*
    Precio de Sí = mín(1.005,47; 1.126,04) = 1.005,47
    Ponderado = 0,2·544,87 + 0,6·1.126,04 + 0,2·2.025,58 = 108,97 + 675,62 + 405,12 = 1.189,71
    Precio 680 > 544,87 y 680 ≤ 1.005,47, luego la zona es cumple_regla_k.


### Crecimiento implícito

    El paquete no permite un modelo de ventas con margen explícito, así que uso un sustituto: supongo un margen de FCF constante, de modo que el FCF crece al mismo ritmo que las ventas. Busco el crecimiento anual g de los años 1-5 que iguala el valor a 680 € (268,37 M€). El resto queda como en el normal: FCF plano en los años 6-10, crecimiento terminal del 2 %, tasa del 9 % y 50 M€ de caja. Resultado: unos -13,1 % anuales; con -13 % el valor es 683 € y con -13,2 %, 678 €. El escenario normal supone un 0 % de FCF. Contraste: el DCF inverso de la hoja, a diez años, da -8,27 % anual.

### Escenario malo

    El margen vuelve hacia el 5-6 % de 2016-2019. Supuestos: FCF base de 31,37 M€ con un crecimiento del -10 % anual en los años 1-10 (unos 10,9 M€ en el año 10) y del 1 % a partir del año 11; descuento al 9 %. Los valores presentes son los de la hoja: 126,71 M€ de los años 1-10 y 58,33 M€ del terminal. Me aparto de la hoja en el exceso de caja: sumo 30 M€ en lugar de 50 M€, porque una caída de actividad devolvería parte del circulante negativo (proveedores 69,4 M€). Operación: (126,71 + 58,33 + 30) / 0,394665 = 544,87 €. La hoja da 595,54 € con 50 M€ de caja. No sumo la cartera cotizada (27,0 M€).

### Escenario normal

    La cartera (unos 370 M€) sostiene 2026-2027. Después las ventas siguen al mercado belga y el margen se erosiona en parte, de modo que el FCF nominal queda plano en 31,37 M€ diez años. El FCF base sale de CFO ajustado 33,44 - capex 1,97 - principal de arrendamientos 0,1 (media FY2023-FY2025). Crecimiento del 0 % en los años 1-10 y del 2 % a partir del año 11; exceso de caja de 50 M€. Operación: 31,37 × 6,4177 = 201,32; terminal 31,9974 / 0,07 / 2,3674 = 193,09; (201,32 + 193,09 + 50) / 0,394665 = 1.126,04 €, que coincide con la tabla auxiliar de la hoja (fila 128). Es más prudente que el normal heredado (+3 % anual, 1.374,08 €), porque la base son los tres mejores años de su historia.

### Escenario bueno

    El margen del 15 % aguanta una década y el volumen crece con la cartera y con oficios integrados como D-FI. FCF base de 31,37 M€ con un crecimiento del 8 % anual en los años 1-10 (67,73 M€ en el año 10) y del 2,5 % a partir del año 11; exceso de caja de 50 M€. Valores de la hoja: 298,30 M€ de los años 1-10 y 451,13 M€ del terminal, que dan 799,42 M€, es decir, 2.025,58 €/acción. El 8 % queda por debajo del ritmo de ventas de 2016-2025, de alrededor del 11 % anual.

### Sensibilidad (comentarios)

    7 %: Malo 659,39; normal 1.509,25; bueno 2.950,56. P* = (0,6·1.509,25 + 0,2·2.950,56 + 0,6·659,39) / 1,4 = 1.350,93. El precio queda ligeramente por encima del escenario malo.
    8 %: Malo 594,48; normal 1.285,93; bueno 2.402,85.
    9 %: Caso base; coincide con la escalera. Malo 544,87; normal 1.126,04; bueno 2.025,58.
    10 %: Malo 505,52; normal 1.005,82; bueno 1.750,43.
    11 %: Malo 473,41; normal 912,06; bueno 1.541,25. Incluso a esta tasa, 680 € sigue por debajo del precio de Sí.

### Qué haría falsa la conclusión

    - Que el margen operativo IFRS de 2026 baje claramente del 13 %, o que el de 2027 vaya hacia el 8-10 %, con la cartera actual. Confirmaría que el margen era del ciclo y movería probabilidad hacia el malo.
    - Que el FCF sin circulante de 2026 quede por debajo de unos 25 M€, o que la cartera de pedidos caiga de forma marcada desde unos 370 M€ sin recuperarse.
    - Que la caja neta deje de llegar al minoritario: más préstamos u obras con sociedades del controlador (La Belle Liégeoise, Moury Promotion, Immo Moury), uso de la caja en promoción inmobiliaria con partes vinculadas, o un recorte del dividendo ordinario.
    - Que aparezca una pérdida grande en una obra a precio cerrado, o un litigio o una garantía (37,7 M€ fuera de balance) que se ejecute.
    - Que se demuestre que buena parte de la caja es caja de obra en sociedades simples, de forma que el exceso disponible baje claramente de 30 M€.
    - Que el precio suba por encima del precio de Sí, de unos 1.005 €, sin mejora de los fundamentales: pasaría a vigilar.

### Lo que no sabe

    - La fuente del salto de margen del 5-6 % al 15 %. Los textos no dan márgenes por tipo de obra ni por cliente, tasa de adjudicación, competidores ni cuota de mercado.
    - Por qué cayeron en 2025 los márgenes estatutarios de Les Entreprises G. Moury y de Bemat mientras el margen IFRS se mantenía, y cuánto del resultado latente se cobrará.
    - Cuánta caja es realmente sobrante. La de obra en sociedades simples no está desglosada; los 50 M€ (y los 30 M€ del malo) son supuestos analíticos, no datos.
    - El Control maestro y la respuesta citan una decisión del inversor del 9-nov-2026 sobre el periodo del FCF base, posterior a la fecha de corte. No la uso como autoridad: elijo por mi cuenta la media FY2023-FY2025 del CFO ajustado, con datos de informes anteriores al corte. Con la media de cinco años (CFO 25,75 y capex 1,66) el FCF base sería de unos 24 M€ y los valores serían menores.
    - No dispongo de un modelo por ventas y márgenes. El crecimiento implícito usa el FCF como sustituto de las ventas, con margen de FCF constante.
    - El precio de 680 € sale de fuentes secundarias (Yahoo, rendementbourse) y no se pudo verificar en Euronext. La liquidez es muy baja, de unos 52 k€ al día.
    - Las operaciones de insiders en la base de la FSMA no se pudieron consultar.
    - La participación económica exacta del controlador en Moury Finance, y la política futura sobre la caja y la cartera de inversiones (27 M€, que no sumo).
    - El valor de Simply Wall St es incoherente con su propia ficha; no lo uso.
    - Los escenarios son DCF simplificados con FCF de crecimiento constante. No modelan una caída brusca tras 2027 ni el ciclo año a año.

### Citas

    [hoja_control_maestro] «Cierre vie 30-oct-2026» → Fecha del precio actual.
    [hoja_analisis] «37,Precio actual,Cotización por acción.,680» → Precio actual de 680 €.
    [hoja_control_maestro] «Liquidez muy baja: ≈72 acciones/día ≈52 k€/día (3 meses).» → Liquidez baja.
    [hoja_control_maestro] «CFO ajustado (sin cartera): 33,44 / 25,75 / 29,20.» → CFO ajustado de 3 años, 5 años y LTM.
    [hoja_control_maestro] «Capex (inmovilizado material + intangible): 3a 1,97 / 5a 1,66 / LTM 1,94.» → Capex del FCF base.
    [hoja_control_maestro] «Principal IFRS 16 puro ≈0,097/año» → Resta por arrendamientos en el FCF base.
    [hoja_analisis] «Aproximación al flujo del accionista si la financiación es razonablemente estable.,31.37» → FCF base de 31,37 M€.
    [hoja_control_maestro] «Acciones en circulación actuales netas de autocartera: 400.585 − 5.920 = 394.665 (0,394665 mm).» → Número de acciones.
    [hoja_analisis] «Este DCF simplificado no la suma automáticamente.,109.5» → Caja y equivalentes de 109,5 M€.
    [hoja_control_maestro] «Deuda bancaria 1,45 (préstamo heredado de D-FI) + arrendamientos IFRS 16 ≈0,27 = 1,7.» → Deuda total de 1,7 M€.
    [hoja_control_maestro] «caja operativa necesaria (supuesto analítico) 20/30/40 → exceso 87,7/77,7/67,7 M€» → Rango del exceso de caja.
    [hoja_analisis] «76,Exceso de caja NO operativa que sumas (mm) · opcional,50,50,50» → Exceso de caja de 50 M€ en el normal y el bueno.
    [respuesta] «30 si se demuestra más caja de obra en sociedades simples» → Uso de 30 M€ de caja en el escenario malo.
    [respuesta] «circulante negativo (proveedores 69,4» → Riesgo de devolución de circulante en el malo.
    [hoja_control_maestro] «Los intereses cobrados (~2,2–2,6 M€/año) inflan el CFO: relevante si se usa C76.» → Motivo para limitar el exceso de caja y no contar dos veces los intereses.
    [hoja_analisis] «67,Crecimiento de la caja libre · años 1–10,-0.1,0.03,0.08» → Crecimientos heredados de los escenarios.
    [hoja_analisis] «68,Crecimiento para siempre · desde el año 11,0.01,0.02,0.025» → Crecimientos terminales.
    [hoja_analisis] «72,Valor HOY de los años 1–10 (mm),126.70888060242» → Valor presente de los años 1-10 del escenario malo.
    [hoja_analisis] «73,Valor HOY del 'para siempre' (mm),58.3318862832713» → Valor presente del terminal del escenario malo.
    [hoja_analisis] «78,VALOR INTRÍNSECO POR ACCIÓN,595.544998633503,1374.08087059348,2025.57764681453» → Valores heredados; el bueno se mantiene en 2.025,58 €.
    [hoja_analisis] «128,0,1126.03933891634» → Valor del normal con un 0 % de crecimiento del FCF.
    [hoja_analisis] «-0.0827296005973521» → DCF inverso a diez años de la hoja.
    [hoja_control_maestro] «margen EBIT 5–6% (2016–19) → salto en 2020–22 → 15,2–15,5% estable FY22–FY25; H1 26 15,1%.» → Historial de márgenes en el que se ancla el escenario malo.
    [respuesta] «márgenes estatutarios de 2025 de Les Entreprises G. Moury 8,2» → Señal temprana de compresión del margen.
    [respuesta] «flujo de explotación −6,1» → Consumo de circulante en el 1S 2026.
    [hoja_control_maestro] «Excluye cartera cotizada 27,0, rama 26 ≈3,1 y depósitos de garantía de obra (3,6).» → Activos que no se suman al valor.
    [hoja_control_maestro] «Moury Finance SA 49,51% + G4 Finance SRL 5,90% (ambas consejeras, vehículos de Gilles-Olivier Moury) = 55,41%.» → Peso del controlador.
    [hoja_control_maestro] «4,13 M€ vencidos de La Belle Liégeoise» → Riesgo de operaciones vinculadas.
    [hoja_control_maestro] «Garantías de obra fuera de balance 37,7 M€ (dic-25).» → Riesgo fuera de balance.
    [hoja_control_maestro] «Decisión del inversor (9-nov-2026): 3 años FY2023–FY2025 (CFO ajustado sin cartera)» → Dato posterior a la fecha de corte que no se usa como autoridad.

### Comprobaciones mecánicas y normalizaciones

    {
      "comprobaciones": {
        "escalera_recalculada_anexo_c": {
          "p_estrella": 1005.4728571428569,
          "precio_si": 1005.4728571428569,
          "ponderado": 1189.714,
          "precio_escenario_malo": 544.87
        },
        "citas_total": 30,
        "citas_literales": 30,
        "avisos": [],
        "nota": "Comprobaciones mecánicas informativas: no acreditan la calidad económica."
      },
      "normalizaciones_enum": []
    }

