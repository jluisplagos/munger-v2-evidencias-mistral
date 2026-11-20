# Análisis directo · Moncler, etapa 1 del universo (hoja del 2026-10-25)

Estado de la ejecución: `AUDITORIA_DOCUMENTAL_PENDIENTE_ACEPTACION`

Revisión a ciegas pendiente. No es aceptación, ni integración, ni aptitud para dinero real.

| Campo | Valor |
|---|---|
| Empresa | moncler |
| Fecha de corte | 2026-10-25 |
| Tasa | 9 % |
| Tarea | analisis-directo-moncler-44791629630 |
| SHA del código | fcb18bba533554c32f9756d6fb49dc0ebcc2946c |
| Huella del paquete (package_sha256) | d7479cc8ba0cf1f634e2c68476be3ea7a72b46a09ce6dd02d9376bdea5528b3d |
| Huella del envío (bundle_sha256) | ea9fef90e3dfcd242946ce587ff81aa48da981c94883af534f92d1adc2688086 |
| Huella del encargo | 022846e95b809a772317c2b17d6d946f3f91b9066c864911e473bb7ea15843e4 |
| Modelo pedido / devuelto | claude-opus-5-5 / claude-opus-5-5 |
| Esfuerzo | high |
| Mensajes enviados | 1 |
| Cota de entrada estimada antes de llamar | 143154 tokens |
| Reserva estimada antes de llamar | USD 1.227976 (máximo de la ejecución USD 3) |
| Reserva registrada | USD 1.227976 |
| Uso de tokens | entrada 65167, salida 14333 |
| Coste | CONOCIDO_ESTIMADO; estimado USD 0.547328; cota 0.547328 |

## Paquete de entrada

| id | ruta | commit | sha256 | bytes |
|---|---|---|---|---|
| respuesta | datos_analisis_directo/moncler/etapa1/Moncler_respuesta.md | fcb18bba5335 | d8ae278c6eb6c9b9f790c0a87d2a9368e9038b97c6d88e1ec5e35fda30ede9bc | 30426 |
| hoja_analisis | datos_analisis_directo/moncler/etapa1/Moncler_evaluada__Análisis.csv | fcb18bba5335 | 6f536f95cd7e10155d7c3e5a47ee9a8ce2953c8694c28a57054375bee200d3a5 | 22812 |
| hoja_guia_simply_wall_st | datos_analisis_directo/moncler/etapa1/Moncler_evaluada__Guía_Simply_Wall_St.csv | fcb18bba5335 | 2791cc208d21b779b2104db9848a271eded2ae7cb4392769b743a2d95f8c3e2f | 7794 |
| hoja_opciones | datos_analisis_directo/moncler/etapa1/Moncler_evaluada__Opciones.csv | fcb18bba5335 | b9f97b6706b77f7a28f70140d212f0790ee7334eb22965a4f538963e777a1a73 | 1537 |
| hoja_control_maestro | datos_analisis_directo/moncler/etapa1/Moncler_evaluada__Control_maestro.csv | fcb18bba5335 | 969c76e2fd5e27b3d0b7445d7fe19d0b8044e6e6349f6754aaa20bac5621f431 | 58870 |

## Salida del modelo (datos, sin acciones ejecutables)

Estado `concluido` · cubo «Vigilar» · acción `esperar` · zona `caro`

| Escenario | Valor por acción | Probabilidad |
|---|---|---|
| malo | 22.32 | 0.2 |
| normal | 33.51 | 0.6 |
| bueno | 53.96 | 0.2 |

| Escalera (k = 3) | Declarado | Recalculado (Anexo C) |
|---|---|---|
| Precio actual | 42.66 | |
| Precio del escenario malo | 22.32 | 22.32 |
| P* | 31.64 | 31.6357 |
| Precio de Sí = mín(P*, V_normal) | 31.64 | 31.6357 |
| Ponderado | 35.36 | 35.362 |
| Crecimiento implícito al precio actual / del normal (%) | 10.7 / 5 | |

| Tasa | Precio de Sí | Ponderado | Zona |
|---|---|---|---|
| 7 % | 45.37 | 51.44 | cumple_regla_k |
| 8 % | 37.3 | 41.96 | vigilar |
| 9 % | 31.64 | 35.36 | caro |
| 10 % | 27.44 | 30.51 | caro |
| 11 % | 24.21 | 26.79 | caro |

### Resumen

    Moncler es un negocio de marca de lujo de alta calidad: margen bruto en torno al 78 %, margen EBIT de 28,6–30,2 % en 2016–25 salvo 2020, sin deuda bancaria y con caja neta. El FCF del accionista lleva cinco años plano, cerca de 500 mm, porque han subido el capex, los alquileres y el inventario. El crecimiento se frena: CSSG −1 % en 2025 y T3 2026 de la marca −1 % cFX. Con un FCF base de 500,2 mm, 271,88 m de acciones y una tasa del 9 %, los escenarios valen 22,32 / 33,51 / 53,96 € y el ponderado 35,36 €. La regla k = 3 da un precio de Sí de 31,64 €. A 42,66 € la acción está por encima del ponderado (zona caro). Para justificar ese precio, las ventas y el FCF tendrían que crecer ≈10,7 % anual cinco años, frente al 5 % del escenario normal. Conclusión: Vigilar y esperar.


### Moneda

    EUR


### Justificación

    Estado concluido: los datos permiten un DCF sobre la caja del accionista con FCF positivo, financiación estable y sin deuda bancaria. Cubo Vigilar: el negocio es de calidad (margen estable una década, ROIC 18,5 %), pero a 42,66 € el precio supera el ponderado (35,36 €) y el valor del escenario normal (33,51 €). Además, exige un crecimiento (≈10,7 % anual cinco años) que el FCF plano de 2021–25 no respalda. Acción esperar: el precio de Sí está en ≈31,6 €. Aunque se sumara el posible exceso de caja (≈3 €/acción), el ponderado seguiría por debajo del precio.


### Probabilidades

    Se mantienen las de partida, 0,2/0,6/0,2. El escenario malo ya supone un FCF plano diez años, así que subir su probabilidad por el CSSG negativo castigaría dos veces el mismo riesgo. Los hechos de 2024–26 (crecimiento de un dígito, margen estable) son los del escenario normal.


### Fórmula aplicada

    V = (22,32; 33,51; 53,96) y p = (0,2; 0,6; 0,2). Para 22,32 ≤ P ≤ 33,51: G(P) = 0,6·(33,51−P) + 0,2·(53,96−P) = 30,90 − 0,8P y L(P) = 0,2·(P−22,32). La condición G = 3L da 30,897 − 0,8P = 0,6P − 13,395, de donde P* = 44,292/1,4 = 31,64. Precio de Sí = mín(31,64; 33,51) = 31,64. Ponderado = 0,2·22,32 + 0,6·33,51 + 0,2·53,96 = 35,36. Como el precio 42,66 > 35,36, la zona es caro.


### Crecimiento implícito

    El modelo no proyecta ventas por separado. Supongo margen y conversión a FCF constantes, de modo que el FCF crece al ritmo de las ventas. Se busca el crecimiento x de los años 1–5 que iguala el valor al precio (42,66 × 271,88 = 11.598 mm), con 5 % en los años 6–10, g terminal del 2 % y r del 9 %, partiendo de un FCF base de 500,2 mm. Resulta x ≈ 10,7 % anual. Contraste: la hoja da un crecimiento implícito del FCF a diez años del 8,22 %. El escenario normal supone el 5 %.

### Escenario malo

    La marca se enfría y la demanda de lujo en Asia no ayuda. El FCF base es de 500,2 mm: media FY23–25 de CFO 955,0 − capex 197,2 − intereses de arrendamiento 33,7 − principal de arrendamiento 183,8 − SBC 40,1. Crece al 0 % en los años 1–10 y al 1,5 % a perpetuidad desde el año 11. Descuento al 9 %. Valor hoy de los años 1–10 = 3.210,1 mm; valor terminal hoy = 2.859,5 mm; total 6.069,6 mm ÷ 271,88 m acciones = 22,32 €. Precedente: el FCF de 2021–25 ya estuvo plano (587/322/538/584/500).

### Escenario normal

    Crecimiento por aperturas (≈3 %, +9 DOS netas en 2025) y subidas de precio de un dígito bajo, con margen EBIT ≈29 % constante. FCF base de 500,2 mm creciendo al 5 % en los años 1–10 (FCF del año 10: 814,8 mm) y al 2 % a perpetuidad. Descuento al 9 %. Años 1–10 = 4.095,8 mm; terminal = 5.015,0 mm; total 9.110,8 mm ÷ 271,88 = 33,51 €. Múltiplo de salida implícito ≈14,6x, frente al P/FCF histórico de 29,4x.

### Escenario bueno

    La marca se extiende más allá del abrigo, Stone Island escala en venta directa y Américas gana peso. FCF creciendo al 10 % en los años 1–10 y al 3 % a perpetuidad. Descuento al 9 %. Años 1–10 = 5.261,5 mm; terminal = 9.407,9 mm; total 14.669,3 mm ÷ 271,88 = 53,96 €. Precedente: los ingresos de la marca crecieron ≈9 % anual en 2019–25.

### Sensibilidad (comentarios)

    7 %: Valores 30,18 / 47,69 / 83,95. El ponderado de 51,44 coincide con la sensibilidad de la hoja (51,44). Solo con una tasa del 7 % el precio actual cumple la regla k.
    8 %: Valores 25,65 / 39,41 / 65,91. El precio de 42,66 queda ligeramente por encima del ponderado.
    9 %: Caso base. Coincide con la escalera (valores 22,32 / 33,51 / 53,96).
    10 %: Valores 19,78 / 29,10 / 45,47.
    11 %: Valores 17,76 / 25,69 / 39,15. El ponderado de 26,79 coincide con la hoja (26,79).

### Qué haría falsa la conclusión

    - Una cotización igual o inferior a ≈31,6 € con la tesis intacta (margen bruto ≈78 %, margen EBIT ≥28 %) pasaría la acción a Sí.
    - Un FCF de FY26–27 por encima de 600 mm con el capex de vuelta a ≈6 % de las ventas subiría la base y el crecimiento normal, y con ellos el precio de Sí.
    - Un margen bruto que cae de forma sostenida por rebajas, o un margen EBIT por debajo del 27 % fuera de un año excepcional, llevaría a No.
    - Dos años más de CSSG negativo con aperturas que solo tapan la caída llevarían a Demasiado difícil, porque no se podría separar el ciclo de la pérdida de deseo por la marca.
    - Un deterioro de Stone Island (holgura de 30–40 pb) acompañado de otra compra grande cara llevaría a No.
    - Ventas discrecionales de Double R o de consejeros fuera de los planes de retribución serían una señal negativa.
    - Un inventario al cierre de FY26 que siga creciendo por encima de las ventas, o una mayor dotación por obsolescencia, apuntaría a un problema de demanda.

### Lo que no sabe

    - La hoja de control contiene anotaciones fechadas el 1-nov-2026, posteriores al corte: la elección del periodo de medias de C46–C50 y la clasificación de C28. No las uso como hechos. Adopto por criterio propio la media FY23–25, que ya figuraba como propuesta antes de esa fecha (955,0 − 197,2 − 33,7 − 183,8 − 40,1 = 500,2). Con la media de 5 años el FCF base sería ≈6,3 % menor.
    - No tengo los márgenes por marca: Stone Island no publica margen y el grupo tiene un solo segmento IFRS 8.
    - Las fuentes no nombran competidores ni dan cuota de mercado.
    - No tengo la serie de unidades frente a precio medio de 2016–25, ni el peso de rebajas y outlets.
    - No conozco el ROIC de las tiendas nuevas ni el de la nueva sede. El ROIC incremental de FY23→25 es ≈3 %.
    - No tengo el inventario al cierre de FY26.
    - No tengo historial del nuevo CEO ni su participación en acciones.
    - El valor intrínseco de Simply Wall St no es verificable. El consenso de analistas es secundario y probablemente anterior al 9M.
    - No sumo el posible exceso de caja (≈816–855 mm, unos 3 €/acción): los intereses bancarios ya van en el CFO y junio es el valle estacional. Si se sumara, todos los valores subirían ≈3 € y el cubo no cambiaría.
    - El crecimiento implícito de ventas supone margen y conversión a FCF constantes. El modelo no proyecta ventas por separado.
    - Las cifras proceden de una hoja CSV y de una respuesta de etapa 1 que trato como hipótesis. No he podido contrastarlas con los informes anuales originales.
    - El precio es el cierre del 23-oct-2026 y habría que actualizarlo antes de cualquier decisión.

### Citas

    [hoja_control_maestro] «Último cierre en Euronext Milan del viernes 23-oct-2026: 42,66 EUR» → Precio actual usado.
    [hoja_control_maestro] «Propuesta 3 años: 955,0 − 197,2 − 33,7 − 183,8 = 540,2 antes de SBC; 500,1 después.» → FCF base del DCF, propuesta anterior al corte.
    [hoja_control_maestro] «SBC IFRS 2: media 3 años 40,1; 5 años 37,1; LTM 31,6.» → SBC restada del FCF base.
    [hoja_control_maestro] «Media ponderada H1-26 271,88 m.» → Número de acciones del denominador.
    [hoja_analisis] «Crecimiento de la caja libre · años 1–10,0,0.05,0.1» → Crecimientos del FCF de los escenarios malo, normal y bueno.
    [hoja_analisis] «Crecimiento para siempre · desde el año 11,0.015,0.02,0.03» → Crecimientos terminales de los tres escenarios.
    [hoja_analisis] «VALOR INTRÍNSECO POR ACCIÓN,22.3244403193734,33.5105495976245,53.9552197604107» → Valores por acción al 9 %, que coinciden con mi recálculo.
    [hoja_analisis] «0.0822407483217129,⚠ REVISAR · exige escenario BUENO» → Crecimiento implícito del FCF a diez años según la hoja.
    [hoja_control_maestro] «Evidencia (FIN): FCF accionista antes de SBC FY21–25: 587 / 322 / 538 / 584 / 500; LTM 556.» → FCF plano en cinco años, base del escenario malo.
    [hoja_control_maestro] «margen bruto 75,7% (2016) → 78,1% (2025), LTM 78,2%; margen EBIT IFRS 28,6–30,2% (2016–25 salvo 2020)» → Estabilidad de márgenes y foso de marca.
    [respuesta] «el CSSG pasó de +19 % (2023) a −1 % (2025)» → Desaceleración de la demanda.
    [respuesta] «T3 2026 de la marca Moncler −1 % cFX con DTC −2 % y turismo flojo en EMEA» → Último dato trimestral antes del corte.
    [respuesta] «en T2 2026 creció el precio con volúmenes planos o algo negativos» → Crecimiento vía precio y no volumen.
    [respuesta] «demanda de Asia (52 % de la marca Moncler; AR25 p.37)» → Dependencia de Asia.
    [respuesta] «+9 DOS netas en 2025 sobre 286, ≈3 %» → Componente de aperturas del escenario normal.
    [respuesta] «caja neta sin ellos 1.112,4 mm a jun-26, sin deuda bancaria» → Balance sólido y riesgo de ruina bajo.
    [hoja_control_maestro] «Vigilancia: ROIC incremental FY23→25 ≈ 3% (capital +17%, EBIT +2%)» → Reinversión de baja rentabilidad reciente.
    [hoja_control_maestro] «existencias +10,2% (560,3 → 617,5) vs ingresos H1 +5,2% y LTM +3,0%» → El inventario crece más que las ventas.
    [hoja_control_maestro] «Capex al alza: 7,0–7,1% de ventas en FY25/LTM» → El capex al alza presiona el FCF.
    [hoja_control_maestro] «holgura estrecha, 30–40 pb (FY24: 60–80 pb)» → Riesgo de deterioro de Stone Island.
    [hoja_control_maestro] «excedente orientativo ≈816–855 (3,00–3,14 €/acción ≈ 7% del precio)» → Sensibilidad al exceso de caja, no sumado.
    [hoja_control_maestro] «Mediana FY21–25 = 29,4x» → P/FCF histórico frente al múltiplo terminal de 14,6x.
    [hoja_control_maestro] «hoy el mercado paga 20,9x el FCF LTM» → Valoración actual del mercado.
    [hoja_control_maestro] «Decisión del inversor (1-nov-2026): FCF base con media de 3 años FY2023–FY2025» → Anotación posterior al corte, no usada como hecho.

### Comprobaciones mecánicas y normalizaciones

    {
      "comprobaciones": {
        "escalera_recalculada_anexo_c": {
          "p_estrella": 31.635714285714283,
          "precio_si": 31.635714285714283,
          "ponderado": 35.362,
          "precio_escenario_malo": 22.32
        },
        "citas_total": 24,
        "citas_literales": 24,
        "avisos": [],
        "nota": "Comprobaciones mecánicas informativas: no acreditan la calidad económica."
      },
      "normalizaciones_enum": []
    }

