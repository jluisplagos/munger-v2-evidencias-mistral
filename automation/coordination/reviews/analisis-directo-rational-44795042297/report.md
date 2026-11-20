# Análisis directo · Rational, etapa 1 del universo (hoja del 2026-10-08)

Estado de la ejecución: `AUDITORIA_DOCUMENTAL_PENDIENTE_ACEPTACION`

Revisión a ciegas pendiente. No es aceptación, ni integración, ni aptitud para dinero real.

| Campo | Valor |
|---|---|
| Empresa | rational |
| Fecha de corte | 2026-10-08 |
| Tasa | 9 % |
| Tarea | analisis-directo-rational-44795042297 |
| SHA del código | fcb18bba533554c32f9756d6fb49dc0ebcc2946c |
| Huella del paquete (package_sha256) | e3b0ddb2d444e67d3ab0b7ab7bf27e62b842fb4685502518d0ae62536ef14018 |
| Huella del envío (bundle_sha256) | 60302c52ef886dbd2e2e466b0fbf2ba6daee2632cacb46e777efeed4588880a1 |
| Huella del encargo | 022846e95b809a772317c2b17d6d946f3f91b9066c864911e473bb7ea15843e4 |
| Modelo pedido / devuelto | claude-opus-5-5 / claude-opus-5-5 |
| Esfuerzo | high |
| Mensajes enviados | 1 |
| Cota de entrada estimada antes de llamar | 147649 tokens |
| Reserva estimada antes de llamar | USD 1.245956 (máximo de la ejecución USD 3) |
| Reserva registrada | USD 1.245956 |
| Uso de tokens | entrada 66499, salida 15174 |
| Coste | CONOCIDO_ESTIMADO; estimado USD 0.569476; cota 0.569476 |

## Paquete de entrada

| id | ruta | commit | sha256 | bytes |
|---|---|---|---|---|
| respuesta | datos_analisis_directo/rational/etapa1/Rational_respuesta.md | fcb18bba5335 | 2862d98ea3608b73798069e916d13d2636f6d3b9e3375ed16c95b637ad9e4c06 | 32103 |
| cambios_v2 | datos_analisis_directo/rational/etapa1/Rational_cambios_v2.md | fcb18bba5335 | d1e26b17e4702abff5781b3b89c5842e1deb320b45ad0f5e18fb97f8b293a050 | 5028 |
| hoja_analisis | datos_analisis_directo/rational/etapa1/Rational_evaluada__Análisis.csv | fcb18bba5335 | 8b1e931fbb98cc60b073e1eb450d5814a21b2c2a576812a5dd02053bdc6d3b4c | 23333 |
| hoja_guia_simply_wall_st | datos_analisis_directo/rational/etapa1/Rational_evaluada__Guía_Simply_Wall_St.csv | fcb18bba5335 | 2791cc208d21b779b2104db9848a271eded2ae7cb4392769b743a2d95f8c3e2f | 7794 |
| hoja_opciones | datos_analisis_directo/rational/etapa1/Rational_evaluada__Opciones.csv | fcb18bba5335 | b9f97b6706b77f7a28f70140d212f0790ee7334eb22965a4f538963e777a1a73 | 1537 |
| hoja_control_maestro | datos_analisis_directo/rational/etapa1/Rational_evaluada__Control_maestro.csv | fcb18bba5335 | daa856580ed1034e596a8b873971d3712a1271fdae86703a2c6ffe3394184ebf | 55808 |

## Salida del modelo (datos, sin acciones ejecutables)

Estado `concluido` · cubo «Vigilar» · acción `esperar` · zona `caro`

| Escenario | Valor por acción | Probabilidad |
|---|---|---|
| malo | 288.2 | 0.2 |
| normal | 413.45 | 0.6 |
| bueno | 582.98 | 0.2 |

| Escalera (k = 3) | Declarado | Recalculado (Anexo C) |
|---|---|---|
| Precio actual | 566.5 | |
| Precio del escenario malo | 288.2 | 288.2 |
| P* | 383.99 | 383.99 |
| Precio de Sí = mín(P*, V_normal) | 383.99 | 383.99 |
| Ponderado | 422.31 | 422.306 |
| Crecimiento implícito al precio actual / del normal (%) | 13.8 / 6 | |

| Tasa | Precio de Sí | Ponderado | Zona |
|---|---|---|---|
| 7 % | 551.68 | 617.3 | vigilar |
| 8 % | 452.64 | 501.6 | caro |
| 9 % | 383.99 | 422.31 | caro |
| 10 % | 333.6 | 364.61 | caro |
| 11 % | 295.06 | 320.8 | caro |

### Resumen

    Rational es un negocio de calidad. Vende sistemas de cocción profesional y obtiene un 31 % de sus ventas en posventa. Tiene un ROCE del 36,7 %, no tiene deuda financiera y su número de acciones no ha cambiado. El problema es el precio. Con el FCF base de 219,2 m (media FY2023–25), 200 m de exceso de caja, 11,37 m de acciones y una tasa del 9 %, los valores son 288,20 € en el escenario malo, 413,45 € en el normal y 582,98 € en el bueno, con un ponderado de 422,31 €. La regla k = 3 da P* = 383,99 €, que es el precio de Sí. La cotización de 566,50 € (cierre del 7-oct-2026) está por encima del ponderado y casi iguala el escenario bueno: zona caro. El precio descuenta un crecimiento de las ventas y del FCF de un 13,8 % anual durante cinco años, frente al 6 % del escenario normal. Conclusión: Vigilar y esperar.


### Moneda

    EUR


### Justificación

    El análisis está concluido. Los datos objetivos necesarios (FCF base, caja, acciones y precio) están en el paquete y el DCF del accionista es aplicable: no hay deuda financiera, no hay SBC y las acciones son estables. Cubo Vigilar porque el negocio es comprensible y de alta calidad, con ROCE del 36,7 %, margen bruto del 59 % y 31 % de posventa. Pero a 566,50 € la cotización está un 34 % por encima del ponderado (422,31 €) y un 48 % por encima del precio de Sí (383,99 €). Solo con la tasa del 7 % saldría de la zona caro. Acción esperar: compraría hacia 384 € si la tesis sigue intacta.


### Probabilidades

    Mantengo las de partida (0,2 / 0,6 / 0,2). No hay datos para sesgarlas. Un nuevo año de volumen plano en 2026–2027 justificaría subir el malo. Ventas relevantes del combi de entrada en China justificarían subir el bueno. Hasta la fecha de corte no hay evidencia de ninguna de las dos cosas.


### Fórmula aplicada

    P* está entre V_malo = 288,20 y V_normal = 413,45.
    G(P) = 0,6·(413,45 − P) + 0,2·(582,98 − P) = 364,67 − 0,8·P.
    L(P) = 0,2·(P − 288,20).
    G = 3·L → 364,67 − 0,8·P = 0,6·P − 172,92 → P* = 537,59 / 1,4 = 383,99.
    Precio de Sí = mín(383,99; 413,45) = 383,99.
    Ponderado = 0,2·288,20 + 0,6·413,45 + 0,2·582,98 = 422,31.
    Precio 566,50 > 422,31 → caro.


### Crecimiento implícito

    El escenario normal supone margen estable, así que tomo el crecimiento de las ventas igual al del FCF. Mantengo el resto del normal: FCF base de 219,2 m, 6 % en los años 6–10, terminal del 2,5 %, 200 m de caja y tasa del 9 %. Busco el crecimiento de los años 1–5 que hace que el valor por acción iguale 566,50 €, es decir, un valor operativo de 6.441,1 − 200 = 6.241,1 m. Al 13 % sale 6.030,5 m y al 14 % sale 6.280,8 m; interpolando, unos 13,8 % anuales. Como contraste, el DCF inverso de la hoja da un 10,3 % anual durante diez años, por encima incluso del 10 % del escenario bueno. Es un cálculo propio aproximado. No modelizo ventas y márgenes por separado.

### Escenario malo

    FCF base de 219,2 m, media FY2023–25: CFO 264,8 − capex 33,3 − intereses en financiación 1,3 − principal de arrendamientos 11,0, sin SBC. Crece un 2 % anual en los años 1–10 y un 1,5 % a perpetuidad, descontado al 9 %. Se suman 200 m de exceso de caja y se divide entre 11,37 m de acciones. El supuesto es que el volumen sigue como en 2023–2024 (0 % y +3 %), que China no se recupera (−29 % en 2025) y que el margen EBIT baja hacia el 22–23 % por aranceles y divisas. Componentes: 1.549,4 m de los años 1–10, 1.527,5 m de valor terminal y 200 m de caja, en total 3.276,9 m; 3.276,9 / 11,37 = 288,20 €.

### Escenario normal

    El mismo FCF base de 219,2 m. Crece un 6 % anual en los años 1–10 (volumen del 4–5 % más un 1 % de precio, con margen EBIT estable en torno al 25–26 %) y un 2,5 % a perpetuidad, al 9 %. El terminal equivale a vender en el año 10 a unas 15,8 veces el FCF, por debajo del P/FCF histórico de 38,3 veces y de las 25,8 veces actuales. Componentes: 1.886,1 m de los años 1–10, 2.614,8 m de terminal y 200 m de caja, en total 4.701,0 m; 4.701,0 / 11,37 = 413,45 €.

### Escenario bueno

    El FCF crece un 10 % anual en los años 1–10, el ritmo de ventas de 2012–2019, y un 3 % a perpetuidad, al 9 %. El supuesto es que funcionan el combi de entrada fabricado en Suzhou, el iVario y el iHexagon. Componentes: 2.305,7 m de los años 1–10, 4.122,8 m de terminal y 200 m de caja, en total 6.628,5 m; 6.628,5 / 11,37 = 582,98 €.

### Sensibilidad (comentarios)

    7 %: Valores: malo 387,64, normal 600,51 y bueno 897,31. P* = (0,6·600,51 + 0,2·897,31 + 0,6·387,64) / 1,4 = 551,68. El ponderado coincide con la hoja (617,30). El precio de 566,50 supera el de Sí, pero queda por debajo del ponderado.
    8 %: Valores: malo 330,26, normal 489,82 y bueno 708,27. P* = 633,70 / 1,4 = 452,64. El precio supera el ponderado.
    9 %: Caso base, coincide con la escalera. Valores: 288,20, 413,45 y 582,98.
    10 %: Valores: malo 256,07, normal 357,65 y bueno 494,05. P* = 467,04 / 1,4 = 333,60. Incluso el bueno queda por debajo del precio.
    11 %: Valores: malo 230,71, normal 315,15 y bueno 427,82. P* = 413,08 / 1,4 = 295,06. El ponderado coincide con la hoja (320,80).

### Qué haría falsa la conclusión

    - La cotización baja a 384 € o menos con el volumen creciendo un 4–6 % y el margen EBIT en torno al 25 %: pasaría a Sí.
    - El volumen de 2026–2027 crece un 8–10 % anual sin subidas de precio, con margen EBIT de al menos el 26 %: subiría el escenario normal y el precio de Sí.
    - Un competidor identificado iguala la tecnología del combi a menor precio y gana cuota de forma visible: pasaría a No o a Demasiado difícil.
    - El margen EBIT sin extraordinarios queda de forma sostenida por debajo del 22 %, o el margen bruto por debajo del 55 %: pasaría a No.
    - El FCF de 2026 vuelve a caer con ventas al alza y el circulante (existencias y clientes) sigue creciendo por encima de las ventas.
    - Una adquisición grande fuera del núcleo, o un uso de la caja contrario a la política de reserva de liquidez.
    - El volumen cae dos años seguidos sin una causa externa clara.

### Lo que no sabe

    - Varios archivos del paquete son posteriores a la fecha de corte (2026-10-08). La respuesta y la hoja se corrigieron el 25-oct-2026 (v2), y la decisión del inversor sobre el periodo del FCF base es del 23-oct-2026. No uso esos juicios como hechos. Solo uso cifras que se refieren a periodos anteriores al corte (FY2023–25, balance a 30-jun-2026 y precio del 7-oct-2026). Elijo yo la media de tres años como FCF base porque el LTM (250,1 m) incluye un reembolso de aranceles de 13,9 m y circulante favorable.
    - El exceso de caja de 200 m es un juicio de la etapa 1 posterior al corte, que comparto. La liquidez total es de 431,7 m. Cada 100 m adicionales de caja sumarían unos 8,8 € por acción, sin cambiar la zona.
    - El informe semestral de H1 2026 no está auditado y se extrajo de forma indirecta. El precio procede de fuentes secundarias de mercado.
    - No se nombra a ningún competidor. La cuota del 50 % es una cifra de la propia empresa.
    - Faltan la inversión total en Suzhou, las primeras ventas del combi de entrada en China, la base instalada y la posventa por aparato.
    - El informe de remuneración de 2025 da dos tasas del bonus (110 % y 170 %). No se conoce la participación individual de los consejeros ejecutivos.
    - El precio de Sí de la etapa 1 (≈288 €) sale de otra fórmula, el mínimo entre el malo y 0,75 veces el ponderado. Con la regla k = 3 del encargo sale 383,99 €.
    - El crecimiento implícito es del FCF, asimilado al de las ventas porque el normal supone margen estable. No hay un modelo de ventas y márgenes por separado.
    - No uso nada posterior al 8-oct-2026 ni datos de memoria.

### Citas

    [hoja_analisis] «Precio actual,Cotización por acción.,566.5» → Precio actual usado: 566,50 €.
    [hoja_control_maestro] «Cierre 7-oct-2026,EUR/acción» → Fecha del precio: cierre del 7-oct-2026.
    [hoja_analisis] «Aproximación al flujo del accionista si la financiación es razonablemente estable.,219.2» → FCF base de 219,2 m.
    [hoja_control_maestro] «(CFO 264,8; capex 33,3; intereses en financiación 1,3; principal leases 11,0)» → Componentes de la media FY2023–25 del FCF base.
    [hoja_control_maestro] «CFO 304,6 − capex 41,1 − intereses pagados (financiación) 1,4 − principal leases (financiación) 12,0 = 250,1» → FCF de los últimos doce meses, de contraste.
    [hoja_control_maestro] «Sensibilidades: sin reembolso arancelario 236,3 (3,7%); media 3 años 219,2 (3,4%)» → El LTM está inflado por el reembolso; la base de tres años es más prudente.
    [hoja_control_maestro] «Acciones diluidas = básicas = 11,37 m (sin instrumentos dilutivos, autocartera 0)» → Número de acciones.
    [hoja_control_maestro] «Caja y equivalentes literal (vencimiento original <3 meses) = 205,98.» → Tope de caja para el exceso de caja de 200 m.
    [hoja_control_maestro] «Liquidez total con otros activos financieros corrientes (depósitos ≤12 meses, fondo monetario 10,1) = 431,7 mm» → Liquidez total, margen adicional no sumado.
    [hoja_control_maestro] «Deuda financiera 0 (bancos/bonos; última deuda bancaria repagada en 2023) + pasivos por arrendamiento 27,6 (9,8 corrientes + 17,8 no corrientes).» → Sin deuda financiera.
    [hoja_control_maestro] «13,5 mm con controles de capital (China). Nada comprometido a 30-jun (dividendo pagado 5-may-26).» → Ajustes al exceso de caja.
    [hoja_analisis] «Exceso de caja NO operativa que sumas (mm) · opcional,200,200,200» → 200 m de caja sumados en cada escenario.
    [hoja_analisis] «Crecimiento de la caja libre · años 1–10,0.02,0.06,0.1» → Crecimientos de los escenarios.
    [hoja_analisis] «Crecimiento para siempre · desde el año 11,0.015,0.025,0.03» → Crecimientos terminales.
    [hoja_analisis] «VALOR INTRÍNSECO POR ACCIÓN,288.204720059155,413.453584571944,582.978850068158» → Valores por escenario al 9 %, comprobados con cálculo propio.
    [hoja_analisis] «0.103154806164272,✗ BANDERA · > BUENO» → DCF inverso a diez años de la hoja: 10,3 %.
    [hoja_analisis] «r − 2 pts (7.0%),573.273428706852,617.296950649044» → Comprueba el ponderado al 7 %.
    [hoja_analisis] «r + 2 pts (11.0%),311.661205833266,320.795828960463» → Comprueba el ponderado al 11 %.
    [hoja_control_maestro] «Cifra principal: reportada FY2025 = 36,7%. Es ROCE, no ROIC.» → Calidad del negocio.
    [respuesta] «158 (2019), 59 (2020), 146–148 (2021), 123 (2022), 224 (2023), 251 (2024), 219 (2025) m» → Serie de FCF, positivo incluso en 2020.
    [respuesta] «el volumen creció 0 % en 2023 y 3 % en 2024, por debajo de lo que la propia empresa había previsto» → Base del escenario malo.
    [respuesta] «Asia Norte cayó un 16 % y China un 29 % en 2025» → Riesgo de China en el escenario malo.
    [respuesta] «Primer semestre de 2026: 26,5 %, pero 24,3 % sin el reembolso de aranceles de unos 14 m, según el CFO» → Presión sobre el margen.
    [respuesta] «un euro un 10 % más fuerte resta un 14 % al EBIT» → Sensibilidad a divisas.
    [hoja_control_maestro] «Mediana de años no distorsionados = 38,3x (rango 36,5–54,7).» → Contraste del múltiplo terminal implícito (15,8 veces).
    [hoja_control_maestro] «única operación: 9-dic-2025 VENTA de ~27.000 acciones (16,6 mm EUR a 614,66) por Franziska Würbser» → Operaciones de insiders anteriores al corte.
    [hoja_control_maestro] «Decisión del inversor (23-oct-2026)» → Parte del paquete es posterior a la fecha de corte.
    [respuesta] «v2 · corregida el 25-oct-2026» → La respuesta de la etapa 1 es posterior al corte; tratada solo como hipótesis.

### Comprobaciones mecánicas y normalizaciones

    {
      "comprobaciones": {
        "escalera_recalculada_anexo_c": {
          "p_estrella": 383.98999999999995,
          "precio_si": 383.98999999999995,
          "ponderado": 422.306,
          "precio_escenario_malo": 288.2
        },
        "citas_total": 28,
        "citas_literales": 28,
        "avisos": [],
        "nota": "Comprobaciones mecánicas informativas: no acreditan la calidad económica."
      },
      "normalizaciones_enum": []
    }

