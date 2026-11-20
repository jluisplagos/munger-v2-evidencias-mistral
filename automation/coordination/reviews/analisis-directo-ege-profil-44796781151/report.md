# Análisis directo · Ege_Profil, etapa 1 del universo (hoja del 2026-10-30)

Estado de la ejecución: `AUDITORIA_DOCUMENTAL_PENDIENTE_ACEPTACION`

Revisión a ciegas pendiente. No es aceptación, ni integración, ni aptitud para dinero real.

| Campo | Valor |
|---|---|
| Empresa | ege-profil |
| Fecha de corte | 2026-10-30 |
| Tasa | 9 % |
| Tarea | analisis-directo-ege-profil-44796781151 |
| SHA del código | fcb18bba533554c32f9756d6fb49dc0ebcc2946c |
| Huella del paquete (package_sha256) | 8f83ce0211f3b9d80e6ce82762a9af92a91c7c2d7656d8b16e1e45435b39ccea |
| Huella del envío (bundle_sha256) | 14bba43cccc255f7bf4f27c10c419545a4122dde6cccd5098bf9f36b15c6c37a |
| Huella del encargo | 022846e95b809a772317c2b17d6d946f3f91b9066c864911e473bb7ea15843e4 |
| Modelo pedido / devuelto | claude-opus-5-5 / claude-opus-5-5 |
| Esfuerzo | high |
| Mensajes enviados | 1 |
| Cota de entrada estimada antes de llamar | 140034 tokens |
| Reserva estimada antes de llamar | USD 1.215496 (máximo de la ejecución USD 3) |
| Reserva registrada | USD 1.215496 |
| Uso de tokens | entrada 63499, salida 15612 |
| Coste | CONOCIDO_ESTIMADO; estimado USD 0.566236; cota 0.566236 |

## Paquete de entrada

| id | ruta | commit | sha256 | bytes |
|---|---|---|---|---|
| respuesta | datos_analisis_directo/ege-profil/etapa1/Ege_Profil_respuesta.md | fcb18bba5335 | b99a993b90e7528b5b5b8e2666d938dd03881cc23813ea7fbd552a8f275857f6 | 31353 |
| hoja_analisis | datos_analisis_directo/ege-profil/etapa1/Ege_Profil_evaluada__Análisis.csv | fcb18bba5335 | cba460389cd90b8a79be227530e8d210d9f4692a2a63ac01cd988d4cf9e3342b | 23342 |
| hoja_guia_simply_wall_st | datos_analisis_directo/ege-profil/etapa1/Ege_Profil_evaluada__Guía_Simply_Wall_St.csv | fcb18bba5335 | 2791cc208d21b779b2104db9848a271eded2ae7cb4392769b743a2d95f8c3e2f | 7794 |
| hoja_opciones | datos_analisis_directo/ege-profil/etapa1/Ege_Profil_evaluada__Opciones.csv | fcb18bba5335 | b9f97b6706b77f7a28f70140d212f0790ee7334eb22965a4f538963e777a1a73 | 1537 |
| hoja_control_maestro | datos_analisis_directo/ege-profil/etapa1/Ege_Profil_evaluada__Control_maestro.csv | fcb18bba5335 | 0882d2b529f6b7a0c3824c24559cddafaa3a87284964b3c00d59e5f1a628cf75 | 54433 |

## Salida del modelo (datos, sin acciones ejecutables)

Estado `concluido` · cubo «Demasiado difícil» · acción `demasiado_dificil` · zona `vigilar`

| Escenario | Valor por acción | Probabilidad |
|---|---|---|
| malo | 14.6 | 0.2 |
| normal | 26.69 | 0.6 |
| bueno | 40.28 | 0.2 |

| Escalera (k = 3) | Declarado | Recalculado (Anexo C) |
|---|---|---|
| Precio actual | 26.5 | |
| Precio del escenario malo | 14.6 | 14.6 |
| P* | 23.45 | 23.45 |
| Precio de Sí = mín(P*, V_normal) | 23.45 | 23.45 |
| Ponderado | 26.99 | 26.99 |
| Crecimiento implícito al precio actual / del normal (%) | 2.84 / 3 | |

| Tasa | Precio de Sí | Ponderado | Zona |
|---|---|---|---|
| 7 % | 32.08 | 37.4 | cumple_regla_k |
| 8 % | 27.09 | 31.37 | cumple_regla_k |
| 9 % | 23.45 | 26.99 | vigilar |
| 10 % | 20.67 | 23.66 | caro |
| 11 % | 18.48 | 21.05 | caro |

### Resumen

    Ege Profil fabrica perfiles de PVC para ventanas en Turquía. Tiene caja neta, un ROCE alto y un múltiplo EV/EBITDA bajo. En contra: el FCF del accionista en TL reales ha caído cuatro lecturas seguidas (de 1.646 a 408 mm), las ventas reales bajaron un 21 % en 2024 y un 11 % en 2025, el margen actual es el más alto de su historia y el accionista de control (86,86 %) cobra cargos intragrupo crecientes y tiene cobros vencidos sin provisión. Con el DCF de la hoja (FCF base de 962,9 mm, media de 2022 a 2025, en TL reales, al 9 %) salen estos valores por acción: malo 14,60 TL, normal 26,69 TL, bueno 40,28 TL y ponderado 26,99 TL. El precio de Sí por la regla k = 3 es 23,45 TL. El precio de 26,5 TL cae en la zona vigilar, sin margen. La conclusión depende sobre todo de la base de FCF, que según la ventana elegida va de 430,5 a 1.244,3 mm, y de la macro turca, el coste del PVC en divisa y el controlador. Ninguno de esos factores sé acotarlo. Por eso el cubo es Demasiado difícil.


### Moneda

    TL


### Justificación

    El análisis está concluido: hay datos suficientes para ver que no sé estimar el FCF real a diez años. La base cambia el valor de forma decisiva. Con la base LTM de 430,5 mm el ponderado ronda 12 TL; con la de tres años, 1.244,3 mm, ronda 35 TL. Además, el FCF real cae cuatro lecturas seguidas, el margen está en máximos históricos frente a un 9,6-19,4 % en 2016-22, hay exposición al PVC en divisa con una posición corta de −530,7 mm, y el controlador cobra 354,3 mm en cargos y tiene 266,5 mm de cobros vencidos sin provisión. Incluso con la base central, a 26,5 TL el precio está casi en el ponderado (26,99) y por encima del precio de Sí (23,45), sin margen. Por eso el cubo es Demasiado difícil y no hay compra.


### Probabilidades

    Mantengo las probabilidades de partida 0,2 / 0,6 / 0,2. El riesgo de deterioro ya está dentro del −5 % anual del escenario malo y no lo castigo dos veces. Si el FCF de 2026 completo confirmara el nivel LTM de 408 mm, subiría el malo a 0,3.


### Fórmula aplicada

    Entre 14,60 y 26,69: G(P) = 0,6·(26,686−P) + 0,2·(40,278−P) = 24,067 − 0,8P; L(P) = 0,2·(P−14,598) = 0,2P − 2,920. Con G = 3L: 24,067 − 0,8P = 0,6P − 8,759, de donde P* = 32,826/1,4 = 23,45. Precio de Sí = mín(23,45; 26,69) = 23,45. Ponderado = 0,2·14,598 + 0,6·26,686 + 0,2·40,278 = 26,99. Como 26,5 > 23,45 y 26,5 ≤ 26,99, la zona es vigilar.


### Crecimiento implícito

    La hoja no modela ventas, solo FCF. En el escenario normal los márgenes se mantienen estables, así que uso el crecimiento del FCF como aproximación del de las ventas. Supuestos: +3 % en los años 6 a 10, g terminal del 1,5 % y r del 9 %. Resuelvo el crecimiento de los años 1 a 5 que iguala el valor a 26,5 TL (frente a 26,69 TL): sale ≈2,84 % anual. Es una aproximación por sensibilidad lineal, hecha por mí. Como contraste, el DCF inverso de la hoja, a 10 años, da 2,90 %.

### Escenario malo

    Supuestos: el bache de 2024-25 se alarga y el margen vuelve hacia los niveles de 2016-22. Cifras: FCF base de 962,9 mm (TL reales de sep-26), crecimiento del FCF del −5 % anual en los años 1 a 10, g terminal del 1 %, r del 9 %, 545 mm de acciones y sin sumar caja. FCF del año 10 = 576,5 mm. Valor total = 7.956 mm, que entre 545 mm de acciones dan 14,60 TL.

### Escenario normal

    Supuestos: el volumen sigue a su mercado y los márgenes quedan cerca de la media de 2023-25. Cifras: FCF base de 962,9 mm, +3 % anual en los años 1 a 10, g terminal del 1,5 % y r del 9 %. El valor terminal equivale a unas 13,5 veces el FCF del año 10. Valor total = 14.543,7 mm, es decir, 26,69 TL por acción.

### Escenario bueno

    Supuestos: el ciclo de la construcción se recupera, el volumen vuelve al nivel de 2023, la planta de Menemen se llena hacia las 100.000 t y se mantienen los márgenes LTM. Cifras: FCF +8 % anual en los años 1 a 10, g terminal del 2 % y r del 9 %. Valor total = 21.951,7 mm, es decir, 40,28 TL por acción.

### Sensibilidad (comentarios)

    7 %: Escenarios recalculados por mí: malo 18,78, normal 36,69 y bueno 58,16. El ponderado coincide con el de la hoja (37,40). Con un 7 % el precio cumpliría la regla k, pero esa tasa es solo informativa.
    8 %: Escenarios: malo 16,40, normal 30,91 y bueno 47,70. El precio (26,5) queda justo por debajo del precio de Sí: el resultado es muy sensible a la tasa.
    9 %: Coincide con la escalera. Escenarios: 14,60 / 26,69 / 40,28.
    10 %: Escenarios: malo 13,18, normal 23,46 y bueno 34,74.
    11 %: Escenarios: malo 12,04, normal 20,92 y bueno 30,47. El ponderado coincide con el de la hoja (21,05).

### Qué haría falsa la conclusión

    - Que el FCF del accionista de 2026 completo vuelva a 900 mm o más en TL reales, con el inventario normalizado, y se mantenga en 2027.
    - Que se publiquen volúmenes en toneladas, precio medio y cuota de mercado, y muestren una posición estable a lo largo del bache de 2024-25.
    - Que se publiquen los contratos de servicios con Deceuninck con su base de cálculo y se cobren los 266,5 mm vencidos intragrupo.
    - Que el precio baje claramente por debajo del precio de Sí, unos 23,45 TL, y mejor hacia el escenario malo, unos 14,6 TL, con una base de FCF defendible.
    - Hacia No: que los cargos intragrupo crezcan más que las ventas, que los cobros intragrupo se condonen, que llegue una oferta a minoritarios por debajo del valor o que el margen operativo vuelva al 10-14 %.

### Lo que no sabe

    - La hoja de control fecha el 08-nov-2026 decisiones del inversor (base de FCF con media de 2022 a 2025 y moneda en TL reales de sep-26). Esa fecha es posterior al corte, así que no uso esas decisiones como tales. Adopto por mi cuenta la misma media de cuatro años sobre los datos de la fase 1, que son anteriores al corte.
    - No hay volúmenes, precios, cuota ni competidores con nombre, y no hay desglose del capex entre mantenimiento y crecimiento.
    - No sé si el margen de 2023 a 2026 se debe a poder de precio de las marcas o a fijar precios en lira con inflación.
    - Las importaciones (52,2 m EUR en 2025) no tienen desglose; el peso del PVC es una suposición de la fase 1.
    - La base del modelo está en TL reales de sep-26 y el precio en TL nominales de oct-26: hay un desfase de un mes de inflación que no corrijo.
    - El precio sale de fuentes secundarias concordantes. No he podido comprobar operaciones de directivos entre el 24 y el 30-10-2026.
    - Desconozco los importes de los litigios (fiscal de 2022, laborales de Gebze, subcontratación) y el precio esperado de venta de Gebze.
    - Desconozco si sigue vigente la pignoración de acciones a favor de un banco que consta en 2016 y qué intención tiene el controlador con el flotante.
    - El crecimiento implícito de ventas es una aproximación que usa el FCF y sensibilidad lineal, no un modelo de ventas.
    - No tengo un P/FCF histórico verificable para contrastar el múltiplo terminal.

### Citas

    [hoja_analisis] «Precio actual,Cotización por acción.,26.5» → Precio actual de 26,5 TL
    [hoja_control_maestro] «Cierre 30-10-2026» → Fecha del precio
    [hoja_analisis] «razonablemente estable.,962.9» → FCF base de 962,9 mm
    [hoja_control_maestro] «Valores de fase 1 en TL jun-26: CFO 1.725 · capex 589 · intereses 154 · arrendamientos 70 (FCF 912 → 962,9 en TL sep-26)» → Componentes de la base de FCF
    [hoja_analisis] «Acciones diluidas (mm),Diluted shares outstanding.,545» → 545 mm de acciones
    [hoja_analisis] «67,Crecimiento de la caja libre · años 1–10,-0.05,0.03,0.08» → Crecimiento del FCF por escenario
    [hoja_analisis] «Crecimiento para siempre · desde el año 11,0.01,0.015,0.02» → g terminal por escenario
    [hoja_analisis] «Probabilidad que le das,0.2,0.6,0.2» → Probabilidades
    [hoja_analisis] «78,VALOR INTRÍNSECO POR ACCIÓN,14.5981740417732,26.6857197022577,40.2783908013531» → Valores por acción al 9 %
    [hoja_analisis] «26.9867447899799,✗ BANDERA · poco margen,Valor ponderado · margen 2%» → Ponderado de 26,99 TL
    [hoja_analisis] «0.029033576236807,✓ PASA · ≤ NORMAL» → Crecimiento implícito a 10 años del 2,90 %
    [hoja_analisis] «r − 2 pts (7.0%),35.3253166160487,37.4014267963151» → Contraste del ponderado al 7 %
    [hoja_analisis] «r + 2 pts (11.0%),20.5441837758384,21.0510909158692» → Contraste del ponderado al 11 %
    [hoja_analisis] «Exceso de caja NO operativa que sumas (mm) · opcional,0,0,0» → No se suma caja
    [hoja_control_maestro] «Opciones: LTM 430,5 (yield 2,98%, ⚠ BAJO) · 3a 1.244,3 (8,6%) · 4a 962,6 (6,7%) · 5a 836,6 (5,8%).» → Rango de la base de FCF según la ventana
    [respuesta] «1.646 (2023) → 1.080 (2024) → 810 (2025) → 408 (LTM)» → FCF del accionista en caída
    [respuesta] «las ventas reales cayeron un 21 % en 2024 y un 11 % en 2025» → Bache de ventas reales
    [respuesta] «margen operativo nominal 2016–22 entre 9,6 % y 19,4 %» → Riesgo de reversión del margen
    [respuesta] «Margen EBITDA (TMS 29) 13,9 % (2022) → 23,7 % → 20,8 % → 21,5 % → 24,6 % LTM» → Margen en máximos
    [respuesta] «posición neta corta en divisa de −530,7 mm» → Exposición a divisa
    [hoja_control_maestro] «Deceuninck NV 86,86% (accionista de control); free float ≈13,14%» → Control y flotante
    [respuesta] «cargos de Deceuninck (gestión, TI, marca) de 354,3 mm en 2025, 2,9 % de las ventas y 17,5 % del EBIT» → Cargos intragrupo
    [respuesta] «266,5 mm de cobros vencidos a sociedades del grupo sin provisión (196,4 un año antes)» → Cobros intragrupo vencidos
    [hoja_control_maestro] «Con el dividendo comprometido (350,0, pagado 20-07-26): caja neta 80,8 (−0,02x).» → No hay exceso de caja claro
    [hoja_control_maestro] «inventarios +17,9% frente a ventas +10,7%» → Consumo de circulante en 2026
    [hoja_control_maestro] «decisión del inversor 08-nov-2026» → Contenido con fecha posterior al corte

### Comprobaciones mecánicas y normalizaciones

    {
      "comprobaciones": {
        "escalera_recalculada_anexo_c": {
          "p_estrella": 23.449999999999996,
          "precio_si": 23.449999999999996,
          "ponderado": 26.990000000000002,
          "precio_escenario_malo": 14.6
        },
        "citas_total": 26,
        "citas_literales": 26,
        "avisos": [],
        "nota": "Comprobaciones mecánicas informativas: no acreditan la calidad económica."
      },
      "normalizaciones_enum": []
    }

