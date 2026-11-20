# Análisis directo · Ferrari, etapa 1 del universo (hoja del 2026-10-25)

Estado de la ejecución: `AUDITORIA_DOCUMENTAL_PENDIENTE_ACEPTACION`

Revisión a ciegas pendiente. No es aceptación, ni integración, ni aptitud para dinero real.

| Campo | Valor |
|---|---|
| Empresa | ferrari |
| Fecha de corte | 2026-10-25 |
| Tasa | 9 % |
| Tarea | analisis-directo-ferrari-44769519411 |
| SHA del código | fcb18bba533554c32f9756d6fb49dc0ebcc2946c |
| Huella del paquete (package_sha256) | 414dda31b115a2e5fd8685ff4f6552b66438a0169544062b1d369ad0b1ded0c5 |
| Huella del envío (bundle_sha256) | 2b004243acd8ef1de37169ed6f715cd07536b61381fa8507cb30efce47da0a00 |
| Huella del encargo | 022846e95b809a772317c2b17d6d946f3f91b9066c864911e473bb7ea15843e4 |
| Modelo pedido / devuelto | claude-opus-5-5 / claude-opus-5-5 |
| Esfuerzo | high |
| Mensajes enviados | 1 |
| Cota de entrada estimada antes de llamar | 155798 tokens |
| Reserva estimada antes de llamar | USD 1.278552 (máximo de la ejecución USD 3) |
| Reserva registrada | USD 1.278552 |
| Uso de tokens | entrada 69240, salida 16295 |
| Coste | CONOCIDO_ESTIMADO; estimado USD 0.60286; cota 0.60286 |

## Paquete de entrada

| id | ruta | commit | sha256 | bytes |
|---|---|---|---|---|
| respuesta | datos_analisis_directo/ferrari/etapa1/Ferrari_respuesta.md | fcb18bba5335 | 93c6208b2578a209e8429f765bbe5459054957eee27087bbb50dec6a801361c8 | 38633 |
| hoja_analisis | datos_analisis_directo/ferrari/etapa1/Ferrari_evaluada__Análisis.csv | fcb18bba5335 | 0f14232d7f0a539b8bde0206f4dc06060a88accc303882bad14a3915e94432fa | 24019 |
| hoja_guia_simply_wall_st | datos_analisis_directo/ferrari/etapa1/Ferrari_evaluada__Guía_Simply_Wall_St.csv | fcb18bba5335 | 2791cc208d21b779b2104db9848a271eded2ae7cb4392769b743a2d95f8c3e2f | 7794 |
| hoja_opciones | datos_analisis_directo/ferrari/etapa1/Ferrari_evaluada__Opciones.csv | fcb18bba5335 | b9f97b6706b77f7a28f70140d212f0790ee7334eb22965a4f538963e777a1a73 | 1537 |
| hoja_control_maestro | datos_analisis_directo/ferrari/etapa1/Ferrari_evaluada__Control_maestro.csv | fcb18bba5335 | 1a6d2565ba2334c41965cd7fcf2973c041d9c971c3e3d6bb27d7e39fddf36b02 | 62024 |

## Salida del modelo (datos, sin acciones ejecutables)

Estado `concluido` · cubo «Vigilar» · acción `esperar` · zona `caro`

| Escenario | Valor por acción | Probabilidad |
|---|---|---|
| malo | 77.93 | 0.2 |
| normal | 121.48 | 0.6 |
| bueno | 159.64 | 0.2 |

| Escalera (k = 3) | Declarado | Recalculado (Anexo C) |
|---|---|---|
| Precio actual | 349.5 | |
| Precio del escenario malo | 77.93 | 77.93 |
| P* | 108.27 | 108.2671 |
| Precio de Sí = mín(P*, V_normal) | 108.27 | 108.2671 |
| Ponderado | 120.4 | 120.402 |
| Crecimiento implícito al precio actual / del normal (%) | 34.3 / 7 | |

| Tasa | Precio de Sí | Ponderado | Zona |
|---|---|---|---|
| 7 % | 153.82 | 173.56 | caro |
| 8 % | 127.25 | 142.43 | caro |
| 9 % | 108.27 | 120.4 | caro |
| 10 % | 94.04 | 104.02 | caro |
| 11 % | 82.99 | 91.37 | caro |

### Resumen

    Ferrari es un negocio de alta calidad: escasez administrada, margen EBIT cercano al 30 %, ROIC estimado del 31,7 % y deuda neta/EBITDA de 0,61x. A 349,5 € está muy por encima de lo que vale al 9 %. Con un FCF base normalizado de 1.015,4 mm € (media FY23-25, neta de capex, arrendamientos y SBC) y 176,8 m de acciones diluidas, los escenarios dan 77,93 € (malo), 121,48 € (normal) y 159,64 € (bueno), con un ponderado de 120,40 €. La regla k = 3 da un precio de Sí de 108,27 €. El precio actual queda en zona caro con cualquier tasa entre el 7 % y el 11 %, y también con bases de FCF más generosas (LTM o guía 2026). Para justificarlo, el FCF tendría que crecer un 21,2 % anual durante diez años, o las ventas cerca de un 34 % anual durante cinco con margen constante. Cubo Vigilar y acción esperar.


### Moneda

    EUR


### Justificación

    Concluido: el DCF simplificado es aplicable (un solo segmento, capex financiado con caja propia, deuda pequeña) y no falta ningún dato que pueda cambiar la conclusión. Ninguna variante razonable acerca el valor al precio: con la base de 5 años (823,6 mm €) el ponderado baja a ≈97,7 €; con el FCF LTM (1.384,5) sube a ≈164 €; y con la guía de FCF industrial 2026 (≥1.550) a ≈184 €. Todas quedan muy por debajo de 349,5 €. El negocio es de calidad y está dentro del círculo, así que el cubo es Vigilar y no No. El precio, sin embargo, es unas 3,2 veces el precio de Sí (108,27 €) y unas 2,9 veces el ponderado, así que la acción es esperar.


### Probabilidades

    Mantengo las probabilidades de partida 0,2/0,6/0,2. Las señales de demanda (inventario de producto terminado +20,2 % con envíos −4 % y China y Reino Unido a la baja) apuntan a subir el malo, pero la empresa lo atribuye a un cambio de gama y la normalización solo se podría verificar con datos posteriores al corte. Ningún reparto razonable cambia la zona: incluso con el bueno al 100 % el valor (159,64 €) está muy por debajo de 349,5 €.


### Fórmula aplicada

    V = (77,93; 121,48; 159,64), p = (0,2; 0,6; 0,2). Para 77,93 < P < 121,48: G(P) = 0,6·(121,48−P) + 0,2·(159,64−P) = 104,82 − 0,8P y L(P) = 0,2·(P−77,93). La condición G ≥ 3L da 104,82 − 0,8P ≥ 0,6P − 46,76, es decir P ≤ 151,58/1,4 = 108,27. Por tanto P* = 108,27 y precio de Sí = mín(108,27; 121,48) = 108,27. Ponderado = 0,2·77,93 + 0,6·121,48 + 0,2·159,64 = 120,40. Como 349,5 > 120,40, la zona es caro.


### Crecimiento implícito

    El modelo no proyecta ventas: proyecta FCF. Supongo una relación FCF/ventas constante, de modo que el crecimiento del FCF iguala al de las ventas. Mantengo el escenario normal (7 % en los años 6-10, 2 % terminal, r = 9 %, base de 1.015,4 mm € y 176,8 m de acciones) y busco el crecimiento de los años 1-5 que iguala el valor a 349,5 € (61.792 mm €, factor 60,85 sobre la base). Por iteración, con 34 % sale un factor de 60,27 y con 34,5 % de 61,35; interpolando, ≈34,3 % anual. El escenario normal supone ≈7 %. Como contraste, el DCF inverso de la hoja (FCF a diez años con terminal del 2 %) da un 21,2 % anual.

### Escenario malo

    La demanda se enfría donde ya lo hace: China/HK/Taiwán pasan de 1.490 a 941 entregas y Reino Unido de 1.011 a 571, y las entregas del 1S26 bajan de 7.087 a 6.802. Aranceles y divisa presionan el margen. El FCF crece un 2 % anual en los años 1-10 y un 1 % a perpetuidad. Base FCF 1.015,4 mm € = 1.997,5 − 933,7 − 21,2 − 27,2; r = 9 %; 176,8 m de acciones. Valor total 13.778 mm € / 176,8 = 77,93 € por acción.

### Escenario normal

    Volumen plano por decisión propia, precio, mezcla y personalización a un dígito medio y margen EBIT estable cerca del 30 % (1S26 30,5 % frente a 30,6 %). El FCF crece un 7 % anual en los años 1-10, por debajo de los ingresos de 2025 (+7,0 %; +8,0 % a tipo constante), y un 2 % terminal. Misma base de 1.015,4 mm € y r = 9 %. Valor total 21.478 mm € / 176,8 = 121,48 € por acción. El 57 % del valor viene del terminal.

### Escenario bueno

    Cuatro modelos nuevos al año (2026-2030), personalización por encima de lo previsto, patrocinio y lifestyle al alza, margen por encima del 31 % y capex bajando hacia el 12 % de los ingresos. El FCF crece un 10 % anual en los años 1-10 y un 2,5 % terminal. Base de 1.015,4 mm € y r = 9 %. Valor total 28.224 mm € / 176,8 = 159,64 € por acción.

### Sensibilidad (comentarios)

    7 %: Escenarios 104,47 / 174,59 / 239,56. P* = (0,6·174,59 + 0,2·239,56 + 0,6·104,47)/1,4 = 153,82 < V_normal. El ponderado coincide con el 173,56 de la hoja. Caro.
    8 %: Escenarios 89,30 / 143,55 / 192,21. P* = 127,25. Caro.
    9 %: Caso base, coincide con la escalera (77,93 / 121,48 / 159,64).
    10 %: Escenarios 69,10 / 105,02 / 135,92. P* = 94,04. Caro.
    11 %: Escenarios 62,05 / 92,29 / 117,93. P* = 82,99. El ponderado coincide con el 91,37 de la hoja. Caro.

### Qué haría falsa la conclusión

    - Que el precio baje a 108 € o menos con los supuestos del negocio intactos: pasaría a Sí.
    - Que el FCF normalizado se asiente de forma recurrente por encima de unos 1.800 mm € con el volumen todavía limitado y el margen EBIT subiendo otra vez: subiría la base y todos los escenarios.
    - Que el inventario de producto terminado no se normalice en el cierre de 2026 y las entregas caigan dos años seguidos: subiría la probabilidad del malo y apuntaría a No.
    - Que la empresa empiece a vender más volumen o a descontar precio para sostener los ingresos: el foso de escasez se debilitaría y pasaría a No.
    - Que el margen EBIT caiga más de dos puntos frente al mismo semestre del año anterior por aranceles o divisa.
    - Que el eléctrico pase a ser la mayoría de la gama y el valor residual de los eléctricos se separe del de los térmicos: pasaría a Demasiado difícil.
    - Que el negocio financiero (cartera FFS de 1.613 mm €) llegue a decidir el resultado del grupo, o que haya una adquisición grande fuera del coche de lujo o pagada con acciones.

### Lo que no sabe

    - Hay datos posteriores al corte (2026-10-25) que no uso como hechos. La hoja Control maestro registra una "Decisión del inversor (28-oct-2026)" sobre el periodo de la media del FCF y menciona los resultados del 3T26 del 3-nov-2026. Uso la media de 3 años porque los datos subyacentes son anteriores al corte, no por esa decisión, y doy como sensibilidad la base de 5 años (1.735,7 − 868,6 − 20,3 − 23,2 = 823,6 mm €).
    - El precio es el cierre del 23-oct-2026; no tengo cotización del 24 al 25 de octubre.
    - La normalización del FCF es discutible. La media 3a incluye anticipos del F80 (+221 mm € en el CFO de 2025), mientras que el CFO absorbe el crecimiento de la cartera FFS (≈127-138 mm €/año), lo que lo hace conservador. No sé cuál es el FCF recurrente exacto.
    - No tengo el tamaño de la cartera de pedidos ni la longitud de la lista de espera, ni la subida de precios cuantificada (va dentro de la mezcla).
    - No sé si el aumento del inventario de producto terminado (+20,2 % dic-25 a jun-26) es un cambio de gama o debilidad de demanda; falta el desglose a junio de 2025.
    - No tengo los objetivos financieros a 2030 del Capital Markets Day ni el importe en euros del efecto de los aranceles de EE. UU.
    - No sé si la recompra de 3.500 mm € para 2026-2030 está condicionada al precio.
    - Las ventas no se modelizan explícitamente. El crecimiento implícito de ventas supone una relación FCF/ventas constante, y el 7 % del escenario normal es crecimiento de FCF asimilado a ventas.
    - El valor de Simply Wall St (99,47 €) es una referencia secundaria cuyas hipótesis no conozco.
    - Las supuestas ventas de directivos de agosto-septiembre de 2026 vistas en un agregador no están verificadas en el registro AFM y no las uso.
    - La respuesta heredada usaba otra regla para el precio de Sí (mínimo entre el valor malo y ¾ del ponderado, ≈78 €); aquí aplico la regla k = 3, que da 108,27 €.
    - Las cifras del semestral de 2026 no están auditadas. El ROIC es una estimación propia de la etapa 1, no una métrica publicada.

### Citas

    [hoja_analisis] «Precio actual,Cotización por acción.,349.5» → Precio actual usado: 349,5 €.
    [hoja_control_maestro] «Cierre vie 23-oct-2026» → Fecha del precio.
    [hoja_analisis] «Cash from Operations. Media de 3–5 años.,1997.5» → CFO medio FY23-25.
    [hoja_analisis] «Capital Expenditures. Escríbelo en POSITIVO.,933.7» → Capex medio FY23-25.
    [hoja_analisis] «21.2,ℹ se resta del FCF» → Principal de arrendamientos restado.
    [hoja_analisis] «27.2,ℹ se resta del FCF» → SBC restada.
    [hoja_analisis] «Aproximación al flujo del accionista si la financiación es razonablemente estable.,1015.4» → FCF base = 1.997,5 − 933,7 − 21,2 − 27,2 = 1.015,4 mm €.
    [hoja_analisis] «Diluted shares outstanding.,176.8» → Acciones diluidas (millones).
    [hoja_analisis] «No pretende estimar un 'coste de equity verdadero' con precisión académica.,0.09» → r = 9 %.
    [hoja_analisis] «Crecimiento de la caja libre · años 1–10,0.02,0.07000000000000001,0.1» → Crecimientos del FCF en los años 1-10 por escenario.
    [hoja_analisis] «Crecimiento para siempre · desde el año 11,0.01,0.02,0.025» → Crecimientos terminales por escenario.
    [hoja_analisis] «Probabilidad que le das,0.2,0.6,0.2» → Probabilidades.
    [hoja_analisis] «VALOR INTRÍNSECO POR ACCIÓN,77.9306896310482,121.48307392675,159.637730723583» → Valores por escenario al 9 %.
    [hoja_analisis] «120.403528426976,—,Solo calcula si los 3 escenarios tienen valor» → Valor ponderado al 9 %.
    [hoja_analisis] «0.211954984890682,✗ BANDERA · > BUENO» → DCF inverso: el precio implica un 21,2 % anual de crecimiento del FCF durante diez años.
    [hoja_analisis] «r − 2 pts (7.0%),162.280995722229,173.562497601803,187.411581334542» → Contraste del ponderado al 7 % (173,56).
    [hoja_analisis] «r + 2 pts (11.0%),88.7971518210705,91.3687056533969,94.2451645948867» → Contraste del ponderado al 11 % (91,37).
    [hoja_control_maestro] «CFO 2.407,2 − capex 969,1 − intereses fuera del CFO 0 (van dentro) − principal arrendamientos 27,1 − cupones híbridos 0 − SBC 26,5 = 1.384,5» → FCF LTM usado en la sensibilidad de la base.
    [hoja_control_maestro] «Valores preparados: 5a 1.735,7 · 3a 1.997,5» → CFO a 5 años para la base alternativa.
    [hoja_control_maestro] «Valores preparados: 5a 868,6 · 3a 933,7» → Capex a 5 años para la base alternativa.
    [hoja_control_maestro] «Decisión del inversor (28-oct-2026): media de 3 años FY23–25» → Dato posterior al corte, no usado como hecho.
    [hoja_control_maestro] «Actualizar LTM con el 3T26 (3-nov-2026).» → Los resultados del 3T26 son posteriores al corte.
    [respuesta] «en el primer semestre de 2026 los ingresos crecieron un 5,8 % con las entregas cayendo de 7.087 a 6.802» → Ritmo reciente de ingresos y entregas.
    [respuesta] «guía de 2026 de ~7,6 mm € y FCF industrial ≥1,55 mm €» → Guía 2026 usada en la sensibilidad de la base.
    [hoja_control_maestro] «Partida relevante: inventario de producto terminado (+20,2% dic-25→jun-26) con envíos −4% y depreciación de inventarios ×2,4 (34,5 vs 14,2).» → Señal de demanda por aclarar.
    [hoja_control_maestro] «LTM 29,5%; 1S26 30,5% vs 1S25 30,6%.» → Margen EBIT en meseta.
    [respuesta] «China continental, Hong Kong y Taiwán de 1.490 a 941 entregas y Reino Unido de 1.011 a 571» → Base del escenario malo.
    [hoja_control_maestro] «÷ EBITDA LTM 2.846,9 (2.772 + 1.477 − 1.402) = 0,61x» → Deuda baja frente al flujo.
    [respuesta] «the long-term response of our clients to electric powertrains, as well as to other new technologies, remains unknown» → Riesgo del tren motriz eléctrico sobre el foso.
    [hoja_control_maestro] «RACE (€349.5) is trading above our estimate of future cash flow value (€99.47)» → Contraste externo secundario.

### Comprobaciones mecánicas y normalizaciones

    {
      "comprobaciones": {
        "escalera_recalculada_anexo_c": {
          "p_estrella": 108.26714285714286,
          "precio_si": 108.26714285714286,
          "ponderado": 120.402,
          "precio_escenario_malo": 77.93
        },
        "citas_total": 30,
        "citas_literales": 30,
        "avisos": [],
        "nota": "Comprobaciones mecánicas informativas: no acreditan la calidad económica."
      },
      "normalizaciones_enum": []
    }

