# Análisis directo · Inditex, etapa 1 del universo (hoja del 2026-10-09)

Estado de la ejecución: `AUDITORIA_DOCUMENTAL_PENDIENTE_ACEPTACION`

Revisión a ciegas pendiente. No es aceptación, ni integración, ni aptitud para dinero real.

| Campo | Valor |
|---|---|
| Empresa | inditex |
| Fecha de corte | 2026-10-09 |
| Tasa | 9 % |
| Tarea | analisis-directo-inditex-44776695520 |
| SHA del código | fcb18bba533554c32f9756d6fb49dc0ebcc2946c |
| Huella del paquete (package_sha256) | 73eb0d4694d47732cd493b9b1994c600cbc20988d42bd736c57342568a0ed686 |
| Huella del envío (bundle_sha256) | e4ed8fc731305308f44d58088700897a3395714e83eccb46ea8111b7251aabb9 |
| Huella del encargo | 022846e95b809a772317c2b17d6d946f3f91b9066c864911e473bb7ea15843e4 |
| Modelo pedido / devuelto | claude-opus-5-5 / claude-opus-5-5 |
| Esfuerzo | high |
| Mensajes enviados | 1 |
| Cota de entrada estimada antes de llamar | 145720 tokens |
| Reserva estimada antes de llamar | USD 1.23824 (máximo de la ejecución USD 3) |
| Reserva registrada | USD 1.23824 |
| Uso de tokens | entrada 66393, salida 17408 |
| Coste | CONOCIDO_ESTIMADO; estimado USD 0.613732; cota 0.613732 |

## Paquete de entrada

| id | ruta | commit | sha256 | bytes |
|---|---|---|---|---|
| respuesta | datos_analisis_directo/inditex/etapa1/Inditex_respuesta.md | fcb18bba5335 | 77afb99b2d1a148c72290183e5203d7857a4a4fe2c190915638476089c41829b | 32195 |
| hoja_analisis | datos_analisis_directo/inditex/etapa1/Inditex_evaluada__Análisis.csv | fcb18bba5335 | fe8d85882ac119152d2836ccae901edee2935b3c17e2fea31df182fc68d55920 | 22574 |
| hoja_guia_simply_wall_st | datos_analisis_directo/inditex/etapa1/Inditex_evaluada__Guía_Simply_Wall_St.csv | fcb18bba5335 | 2791cc208d21b779b2104db9848a271eded2ae7cb4392769b743a2d95f8c3e2f | 7794 |
| hoja_opciones | datos_analisis_directo/inditex/etapa1/Inditex_evaluada__Opciones.csv | fcb18bba5335 | b9f97b6706b77f7a28f70140d212f0790ee7334eb22965a4f538963e777a1a73 | 1537 |
| hoja_control_maestro | datos_analisis_directo/inditex/etapa1/Inditex_evaluada__Control_maestro.csv | fcb18bba5335 | 18d2708761a50fb1cb7526bd4a0465b3b092e415d5e3e0403b278f579b3b96f1 | 59983 |

## Salida del modelo (datos, sin acciones ejecutables)

Estado `concluido` · cubo «Vigilar» · acción `esperar` · zona `caro`

| Escenario | Valor por acción | Probabilidad |
|---|---|---|
| malo | 21.44 | 0.2 |
| normal | 29.08 | 0.6 |
| bueno | 44.8 | 0.2 |

| Escalera (k = 3) | Declarado | Recalculado (Anexo C) |
|---|---|---|
| Precio actual | 52.84 | |
| Precio del escenario malo | 21.44 | 21.44 |
| P* | 28.05 | 28.0514 |
| Precio de Sí = mín(P*, V_normal) | 28.05 | 28.0514 |
| Ponderado | 30.7 | 30.696 |
| Crecimiento implícito al precio actual / del normal (%) | 19.6 / 5 | |

| Tasa | Precio de Sí | Ponderado | Zona |
|---|---|---|---|
| 7 % | 40.78 | 45.37 | caro |
| 8 % | 33.27 | 36.66 | caro |
| 9 % | 28.05 | 30.7 | caro |
| 10 % | 24.22 | 26.36 | caro |
| 11 % | 21.29 | 23.06 | caro |

### Resumen

    Inditex es un negocio de calidad. Tiene ROCE publicado del 40 %, prácticamente sin deuda financiera, circulante negativo y FCF positivo todos los años. El precio de 52,84 € exige mucho más de lo que dan mis escenarios. Uso un FCF base de 4.761 M€ (media 2023-2025 neta de arrendamientos y SBC) y la tasa del 9 %. Con eso, los valores por acción son 21,44 € (malo), 29,08 € (normal) y 44,80 € (bueno), y el ponderado es 30,70 €. Con la regla k = 3, el precio de Sí es 28,05 €. Ni el escenario bueno alcanza la cotización. Para justificar el precio, las ventas y el FCF tendrían que crecer en torno al 19,6 % anual cinco años, frente al 5 % del escenario normal. El precio queda en la zona caro con cualquier tasa entre el 7 % y el 11 %. Concluyo VIGILAR: espero, sin comprar.


### Moneda

    EUR


### Justificación

    Estado: concluido. Los datos para valorar son suficientes y el DCF simplificado es aplicable: la financiación es estable, no hay deuda financiera y el FCF ha sido positivo todos los años.
    
    Cubo VIGILAR, no NO: el negocio supera los filtros de calidad (ROCE del 40 %, conversión de caja sana, margen bruto del 55,8-58,3 %). El problema es solo el precio.
    
    Acción: esperar. A 52,84 € el precio está por encima incluso del escenario bueno (44,80 €) y muy por encima del precio de Sí (28,05 €).
    
    La conclusión resiste a supuestos favorables, combinados de forma ilustrativa con el normal a r del 9 %:
    - FCF base LTM neto de SBC de 5.706 M€: normal ≈34,9 €.
    - Sumar además la posición financiera neta libre tras el dividendo (≈2,46 €/acción): ≈37 €, todavía lejos del precio.


### Probabilidades

    Mantengo las probabilidades de partida 0,2 / 0,6 / 0,2. Hay argumentos en ambos sentidos y no son concluyentes:
    - A favor de cargar el bueno: el crecimiento a tipo constante del 1S26 (+9,2 %) y el arranque del 2S (+9 %) están por encima del normal.
    - A favor de cargar el malo: el margen EBIT está en máximos de diez años y el FCF publicado bajó tres años seguidos.
    No ajusto las probabilidades a la cotización.


### Fórmula aplicada

    Datos: V = (21,44; 29,08; 44,80) y p = (0,2; 0,6; 0,2).
    Para 21,44 ≤ P ≤ 29,08:
    - G(P) = 0,6·(29,08 − P) + 0,2·(44,80 − P) = 26,41 − 0,8P
    - L(P) = 0,2·(P − 21,44)
    G = 3L ⇒ 26,41 − 0,8P = 0,6P − 12,87 ⇒ P* = 39,28 / 1,4 = 28,05.
    Comprobación: E − P = 2,64 = 2L.
    Precio de Sí = mín(28,05; 29,08) = 28,05.
    Ponderado = 0,2·21,44 + 0,6·29,08 + 0,2·44,80 = 30,70.
    Precio del escenario malo = 21,44.
    Precio 52,84 > 30,70 ⇒ caro.


### Crecimiento implícito

    Modelo del escenario normal con FCF proporcional a las ventas (margen y capex por euro estables), FCF base de 4.761 M€, r del 9 % y 3.116,652 M acciones. Busco el crecimiento x de los años 1-5 manteniendo un 5 % en los años 6-10 y un 2,5 % a perpetuidad. El valor por acción es 1,5276 · [Σ_{t=1..5}((1+x)/1,09)^t + (1+x)^5 · 11,410].
    - Con x = 19,5 % sale 52,63 €.
    - Con x = 20 % sale 53,66 €.
    - Interpolando, x ≈ 19,6 % iguala los 52,84 €.
    Contraste: el DCF inverso de la hoja, que aplica crecimiento uniforme durante diez años, da un 12,9 % anual.

### Escenario malo

    El margen EBIT vuelve al ~17 % de FY2016-FY2019 (17,2; 17,0; 16,7; 16,9 %) por fallos de moda, aranceles y divisas, y las ventas en euros crecen ~3 %. El FCF crece un 2 % anual en los años 1-10 y un 1,5 % a perpetuidad. FCF base 4.761 M€ = CFO medio 2023-25 de 9.062 (8.667; 9.288; 9.232) − capex de 2.419 (1.872; 2.672; 2.712) − cuota fija de arrendamientos de 1.790 − SBC de 92. Acciones: 3.116,652 M. Descuento al 9 %. No sumo caja. Resultado: 21,44 €, que coincide con la hoja (B78).

### Escenario normal

    Ventas ~+5 % en euros, margen bruto estable cerca del 58 % y capex ~7 % de ventas, de modo que el FCF crece con las ventas: 5 % anual en los años 1-10 y 2,5 % a perpetuidad, con el mismo FCF base de 4.761 M€ y r del 9 %. FCF del año 10: 7.755 M€. Valor actual de los años 1-10: 38.985 M€. Valor terminal descontado: 51.658 M€. Total: 90.643 M€ entre 3.116,652 M acciones = 29,08 €, que coincide con la hoja (C78). Como contraste, el crecimiento a tipo constante fue del +7,0 % en FY2025 y del +9,2 % en el 1S26.

### Escenario bueno

    Gana cuota en un sector fragmentado: +5 % de espacio bruto, online y aperturas tiran, ventas ~8 % y algo de apalancamiento operativo. El FCF crece un 10 % anual en los años 1-10 y un 3 % a perpetuidad, con FCF base de 4.761 M€ y r del 9 %. Resultado: 44,80 € (hoja D78). Aun así, queda un 15 % por debajo del precio.

### Sensibilidad (comentarios)

    7 %: V = 29,32 / 42,60 / 69,71. El ponderado coincide con la hoja (45,37). Aun con una tasa del 7 %, el precio supera el ponderado.
    8 %: V = 24,77 / 34,61 / 54,73. P* = 33,27, por debajo del normal.
    9 %: Caso base. Coincide con la escalera.
    10 %: V = 18,90 / 25,04 / 37,75.
    11 %: V = 16,89 / 21,96 / 32,51. El ponderado coincide con la hoja (23,06).

### Qué haría falsa la conclusión

    - Que la cotización baje a la zona de 28 € o menos con el negocio intacto (margen bruto ~58 % y ROCE ≥ 35 %). Pasaría a SÍ.
    - Que el FCF de FY2026-FY2027, sin capex extraordinario, supere con claridad los 6.000 M€ tras SBC y la base deje de estar deprimida por el capex logístico de 2024-2025. Subiría todos los escenarios en torno a un 25 % o más y habría que recalcular.
    - Que el crecimiento a tipo constante se mantenga en dos dígitos dos años seguidos con margen estable. Justificaría subir la probabilidad del escenario bueno.
    - Que el margen bruto baje del 55 % dos años seguidos sin causa externa, o que el crecimiento a tipo constante caiga por debajo del 3 % dos años. Pasaría a NO.
    - Que haya una adquisición grande, endeudamiento para recomprar o un cambio en la política de caja. Pasaría a NO o a revisión.
    - Que aranceles y divisas pasen a determinar el valor más que la propia ejecución, o que la valoración exija predecir qué competidor gana el online. Pasaría a demasiado difícil.

### Lo que no sabe

    - El paquete incluye material posterior a la fecha de corte (9-oct-2026) y no lo uso:
    - la revisión del 25-oct-2026 (notas del barrido sobre C40, C76, C88 y C97, incluida la serie P/FCF histórica de 24,5x documentada en ese barrido);
    - las decisiones del inversor fechadas el 20-oct-2026 (periodo de medias 3a para C46-C50 y clasificación de C31).
    Para el FCF base elegí yo la media 2023-2025 a partir de las series anuales de las fuentes; el resultado (4.761 M€) coincide con el de la hoja.
    - El precio es el cierre del 8-oct-2026 de fuentes secundarias, sin confirmar el 9-oct. Incluye el cupón de 0,875 € pagadero el 2-nov-2026.
    - No sumo caja: la posición financiera neta a 31-jul-2026 es de 10.398 M€ y, una vez pagado el dividendo pendiente, quedan ≈7.674 M€ (≈2,46 €/acción). Los ingresos financieros ya están dentro del CFO y sumarla los contaría dos veces. Además, parte de la caja procede del circulante negativo. Si la sumara, la zona no cambiaría.
    - Hay una diferencia del 22 % entre el FCF base y el LTM (5.819 M€ antes de SBC). El LTM está favorecido por un circulante casi neutro (−20). Desconozco cuál es el FCF normalizado tras terminar el capex logístico extraordinario.
    - Falta información sobre el negocio:
    - quiénes son los competidores y su cuota;
    - el crecimiento del mercado de moda por zonas;
    - las ventas comparables (LFL) y el desglose entre unidades y precio;
    - el retorno del programa logístico de 900 M€ al año.
    - Los escenarios y la tasa son convenciones heredadas de la etapa 1, que trato como hipótesis. No conozco el P/FCF al que cotizará la empresa en el año 10. El terminal del normal implica 15,8x.
    - El análisis no tiene en cuenta aranceles ni riesgos regulatorios más allá de lo que declara la empresa según la respuesta heredada.
    - Mi P* con k = 3 (28,05 €) difiere del precio de Sí heredado (21,4 €), que usaba otra regla: mín(malo; ¾ del ponderado).

### Citas

    [hoja_analisis] «Precio actual,Cotización por acción.,52.84» → Precio actual de 52,84 €.
    [hoja_control_maestro] «52,84 € = cierre BME del 8-oct-2026 (la sesión del 9-oct seguía abierta)» → Fecha del precio.
    [hoja_control_maestro] «Serie 2019–25: 6.900 / 3.017 / 6.754 / 6.674 / 8.667 / 9.288 / 9.232.» → CFO 2023-25; la media es 9.062.
    [hoja_control_maestro] «Serie 2019–25: 1.152 / 708 / 1.126 / 1.415 / 1.872 / 2.672 / 2.712.» → Capex 2023-25; la media es 2.419.
    [hoja_control_maestro] «Valor = cuota fija de arrendamientos en financiación (principal + intereses): 3a 1.790» → Arrendamientos restados del FCF.
    [hoja_control_maestro] «Cargo IFRS 2 liquidado en acciones: 2021 74 / 2022 64 / 2023 78 / 2024 85 / 2025 113. Media 3a 92» → SBC restada del FCF.
    [hoja_analisis] «si la financiación es razonablemente estable.,4761,✓ PASA» → FCF base = 9.062 − 2.419 − 1.790 − 92 = 4.761 M€.
    [hoja_control_maestro] «3.116,652 m = acciones emitidas (clase única, sin emisiones desde 2000)» → Número de acciones.
    [hoja_analisis] «Crecimiento de la caja libre · años 1–10,0.02,0.05,0.1» → Crecimientos de los escenarios.
    [hoja_analisis] «Crecimiento para siempre · desde el año 11,0.015,0.025,0.03» → Crecimientos terminales.
    [hoja_analisis] «VALOR INTRÍNSECO POR ACCIÓN,21.4427736055568,29.0833398614049,44.7998859808357» → Valores por escenario al 9 %, verificados con mi cálculo.
    [hoja_analisis] «Tu r (9.0%),29.332472656051,30.6985358341214,32.2959613537729» → Ponderado de 30,70 € al 9 %.
    [hoja_analisis] «r − 2 pts (7.0%),42.0583032458037,45.3671838421101,49.5306993617934» → Contraste del ponderado al 7 %.
    [hoja_analisis] «r + 2 pts (11.0%),22.3714171852047,23.0572929385957,23.8297370891795» → Contraste del ponderado al 11 %.
    [hoja_analisis] «0.12891911493664,✗ BANDERA · > BUENO» → DCF inverso a diez años: 12,9 %.
    [hoja_control_maestro] «híbridos 0 = 5.819 (cuadra con FCF APM 4.686 + 2.299 − 1.165 = 5.820)» → FCF LTM a julio de 2026.
    [hoja_control_maestro] «LTM − SBC del ej. 2025 (113): 5.706 (3,47%)» → Sensibilidad del FCF base.
    [hoja_control_maestro] «El LTM se beneficia del circulante: −20 en LTM frente a −803 en el ej. 2025» → Cautela sobre el LTM.
    [hoja_control_maestro] «PFN libre de esa distribución ≈7.674 (≈2,46 €/acción, 4,7% del precio)» → Caja neta que no sumo.
    [hoja_control_maestro] «Ingresos (339) y costes (155) financieros no-leasing quedan implícitamente en el CFO.» → Riesgo de doble cómputo si se suma la caja.
    [hoja_control_maestro] «ordinario ~2.300 + ~200 extraordinario (instalaciones corporativas)» → Capex guiado para 2026.
    [respuesta] «17 % es su propio margen EBIT de FY2016-FY2019 (17,2; 17,0; 16,7; 16,9 %)» → Antecedente del escenario malo.
    [respuesta] «FCF publicado (tras arrendamientos y capex): 3.942 (FY2019), 631 (covid), 3.959, 3.638, 5.062, 4.814 y 4.686 M€» → Historial del FCF.
    [respuesta] «En moneda constante desacelera: +18 %, +14,1 %, +10,5 % y +7,0 % de FY2022 a FY2025.» → Crecimiento reciente frente al 5 % del normal.
    [hoja_control_maestro] «ventas a tipo constante 1S +9,2% (≈ ritmo del inventario); inicio 2S +9% a tipo constante (1-ago a 7-sep)» → Datos de 2026 anteriores al corte.
    [hoja_control_maestro] «2025: 40% (2024 40%; 2023 39%; 2021 28%)» → Calidad: ROCE publicado.
    [respuesta] «propone repartir hasta 5.454 M€, ~88 % del beneficio consolidado de 6.220 (cálculo)» → Baja reinversión, que limita el crecimiento.
    [hoja_control_maestro] «52,84 × 3.116,367 m acciones en circulación netas de autocartera» → Capitalización de 164.669 M€.

### Comprobaciones mecánicas y normalizaciones

    {
      "comprobaciones": {
        "escalera_recalculada_anexo_c": {
          "p_estrella": 28.051428571428563,
          "precio_si": 28.051428571428563,
          "ponderado": 30.695999999999998,
          "precio_escenario_malo": 21.44
        },
        "citas_total": 28,
        "citas_literales": 28,
        "avisos": [],
        "nota": "Comprobaciones mecánicas informativas: no acreditan la calidad económica."
      },
      "normalizaciones_enum": []
    }

