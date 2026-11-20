# Análisis directo · Spie, etapa 1 del universo (hoja del 2026-11-07)

Estado de la ejecución: `AUDITORIA_DOCUMENTAL_PENDIENTE_ACEPTACION`

Revisión a ciegas pendiente. No es aceptación, ni integración, ni aptitud para dinero real.

| Campo | Valor |
|---|---|
| Empresa | spie |
| Fecha de corte | 2026-11-07 |
| Tasa | 9 % |
| Tarea | analisis-directo-spie-44756195216 |
| SHA del código | 779b55abd380e8427650233fcb8a9c9fa74472f4 |
| Huella del paquete (package_sha256) | fefc4380d011f56cc503e0e4bac20eeed85d93a4960232917878cc475f66abe2 |
| Huella del envío (bundle_sha256) | 51914ab9bba9b31c4d3fe43add26cce1f217a1cd360e4742d5a3438a8d142474 |
| Huella del encargo | 022846e95b809a772317c2b17d6d946f3f91b9066c864911e473bb7ea15843e4 |
| Modelo pedido / devuelto | claude-opus-5-5 / claude-opus-5-5 |
| Esfuerzo | high |
| Mensajes enviados | 1 |
| Cota de entrada estimada antes de llamar | 178166 tokens |
| Reserva estimada antes de llamar | USD 1.368024 (máximo de la ejecución USD 3) |
| Reserva registrada | USD 1.368024 |
| Uso de tokens | entrada 78881, salida 13315 |
| Coste | CONOCIDO_ESTIMADO; estimado USD 0.581824; cota 0.581824 |

## Paquete de entrada

| id | ruta | commit | sha256 | bytes |
|---|---|---|---|---|
| respuesta | datos_analisis_directo/spie/etapa1/Spie_respuesta.md | 779b55abd380 | 1930d35286a3692bc73aced2a2321e5f213f78a231d436fa554baf3df38c99c7 | 51080 |
| hoja_analisis | datos_analisis_directo/spie/etapa1/Spie_evaluada__Análisis.csv | 779b55abd380 | 168fae80eb531475659f46d19c61982e0f3a649e1cca15531b10f248fcafccf9 | 24205 |
| hoja_guia_simply_wall_st | datos_analisis_directo/spie/etapa1/Spie_evaluada__Guía_Simply_Wall_St.csv | 779b55abd380 | 2791cc208d21b779b2104db9848a271eded2ae7cb4392769b743a2d95f8c3e2f | 7794 |
| hoja_opciones | datos_analisis_directo/spie/etapa1/Spie_evaluada__Opciones.csv | 779b55abd380 | b9f97b6706b77f7a28f70140d212f0790ee7334eb22965a4f538963e777a1a73 | 1537 |
| hoja_control_maestro | datos_analisis_directo/spie/etapa1/Spie_evaluada__Control_maestro.csv | 779b55abd380 | ea8eb8604d09ef0bc8ce6a1ee5fb50c60406ffb5d11ac36a3feae91f7e0f0842 | 71921 |

## Salida del modelo (datos, sin acciones ejecutables)

Estado `concluido` · cubo «Vigilar» · acción `esperar` · zona `vigilar`

| Escenario | Valor por acción | Probabilidad |
|---|---|---|
| malo | 31.81 | 0.2 |
| normal | 47.75 | 0.6 |
| bueno | 72.87 | 0.2 |

| Escalera (k = 3) | Declarado | Recalculado (Anexo C) |
|---|---|---|
| Precio actual | 44.54 | |
| Precio del escenario malo | 31.81 | 31.81 |
| P* | 44.51 | 44.5071 |
| Precio de Sí = mín(P*, V_normal) | 44.51 | 44.5071 |
| Ponderado | 49.59 | 49.586 |
| Crecimiento implícito al precio actual / del normal (%) | 4.07 / 5 | |

| Tasa | Precio de Sí | Ponderado | Zona |
|---|---|---|---|
| 7 % | 63.18 | 71.25 | cumple_regla_k |
| 8 % | 52.27 | 58.55 | cumple_regla_k |
| 9 % | 44.51 | 49.59 | vigilar |
| 10 % | 38.72 | 42.93 | caro |
| 11 % | 34.22 | 37.79 | caro |

### Resumen

    SPIE es una empresa de servicios técnicos de mantenimiento e instalación. Tiene una caja muy recurrente, circulante negativo y capex mínimo, pero crece sobre todo comprando empresas. No se ha demostrado un foso: cuota del 4 % en Alemania y un sector fragmentado. Su ROCE después de impuestos es de ~10,4 %. Con el FCF base de 457,2 M€, 174,39 M de acciones y los escenarios del paquete (0 %/5 %/10 % de crecimiento del FCF a 10 años; g terminal 1,5 %/2 %/2,5 %), los valores al 9 % son 31,81 / 47,75 / 72,87 €, con un ponderado de 49,59 €. P* según la regla k = 3 es 44,51 €. El precio de 44,54 € (cierre del 06-nov-2026) queda justo por encima: zona vigilar. Al 10 % ya sale caro. El precio descuenta ~4,1 % anual de crecimiento del FCF, frente al 5 % del escenario normal. Conclusión: Vigilar y esperar, sin margen para comprar con la incertidumbre sobre el retorno del M&A y la expansión de margen que exige el escenario normal.


### Moneda

    EUR


### Justificación

    El estado es concluido: el DCF al accionista es aplicable, con caja predecible y datos completos para el FCF base, las acciones y el precio. El cubo es Vigilar y no Sí por tres razones. Primero, al 9 % el precio está en el umbral de la regla k = 3, ligeramente por encima, y la conclusión cambia a caro con solo +1 punto de tasa. Segundo, el escenario normal exige una expansión de margen sostenida en un negocio sin foso demostrado (cuota del 4 %, licitaciones frecuentes, margen del 7,6 %). Tercero, la base de FCF no resta el M&A, que consume el 74–84 % del FCF, con un retorno después de impuestos de ~10,4 %, apenas por encima del 9 %. No es No porque el negocio es recurrente, convierte bien a caja y el precio está por debajo del ponderado. Acción: esperar a un precio claramente por debajo de ~44,5 € o a pruebas de mejor retorno sobre el capital.


### Probabilidades

    Mantengo 0,2/0,6/0,2. Hay riesgos a la baja concretos: Francia en orgánico negativo, holgura decreciente del test de goodwill y CEO nuevo. También hay apoyos al alza: cartera récord y subida a BBB−. No encuentro un hecho del paquete que justifique sesgar las probabilidades en un sentido.


### Fórmula aplicada

    Para P entre 31,81 y 47,75: G(P) = 0,6·(47,75−P) + 0,2·(72,87−P) = 43,226 − 0,8P y L(P) = 0,2·(P−31,81). G = 3L da 43,226 − 0,8P = 0,6P − 19,088, luego P* = 62,314/1,4 = 44,51. Precio de Sí = mín(44,51; 47,75) = 44,51. Ponderado = 0,2·31,81 + 0,6·47,75 + 0,2·72,87 = 49,59. Precio 44,54: mayor que 31,81 y que 44,51, y menor o igual que 49,59, luego zona vigilar.


### Crecimiento implícito

    El paquete no tiene un modelo de ventas: el DCF proyecta el FCF a 10 años. Uso como aproximación el DCF inverso sobre el FCF, con g terminal del 2 % y r del 9 %. Interpolando la tabla auxiliar (4 % da 44,32 € y 4,5 % da 46,00 €), el precio de 44,54 € descuenta ~4,07 % anual de crecimiento del FCF en los años 1–10, frente al 5 % del normal. No es crecimiento de ventas a cinco años.

### Escenario malo

    El orgánico se queda en cero, los costes laborales no se repercuten y el margen EBITA vuelve hacia el 6,5 %. FCF plano 10 años sobre la base de 457,2 M€ (media 2023–2025: CFO 840,3 − capex 75,1 − intereses 84,1 − arrendamientos 185,1 − SBC 38,8). g terminal 1,5 %, r 9 %, 174,39 M de acciones diluidas. Valor = (2.934,2 + 2.613,6) / 174,39 = 31,81 €. Coincide con la hoja.

### Escenario normal

    Orgánico ~2 % (+2,0 % en 2025; +1,2 % en H1 2026) más una deriva de margen de 20–40 pb al año. FCF +5 % anual 10 años, g terminal 2 % (el mismo que SPIE usa en sus tests de deterioro), r 9 %. El escenario no suma crecimiento comprado porque la base no resta el M&A. Valor = (3.743,7 + 4.583,9) / 174,39 = 47,75 €. Duda: un 5 % con un orgánico del 2 % implica un margen cercano al 10 % en el año 10.

### Escenario bueno

    Se aceleran la electrificación, los centros de datos y la defensa; orgánico del 4–5 % (Alemania hizo +5,3 % en 2025) y margen por encima del 8 %. FCF +10 % anual 10 años, g terminal 2,5 %, r 9 %. Valor = (4.809,2 + 7.899,1) / 174,39 = 72,87 €.

### Sensibilidad (comentarios)

    7 %: V = 43,01 / 67,95 / 109,36. P* = (0,6·67,95 + 0,2·109,36 + 0,6·43,01)/1,4 = 63,18.
    8 %: V = 36,55 / 56,15 / 87,74. P* = 52,27.
    9 %: Coincide con la escalera; el precio queda 0,03 € por encima del precio de Sí.
    10 %: V = 28,18 / 41,47 / 62,05. El precio supera el ponderado.
    11 %: V = 25,30 / 36,61 / 53,83.

### Qué haría falsa la conclusión

    - Que SPIE publique el retorno sobre el capital de las adquisiciones o un ROIC por segmento claramente por encima del 12 % después de impuestos (subiría hacia Sí).
    - Que el precio caiga claramente por debajo de 44,5 € sin deterioro de los fundamentales, entrando con holgura en la zona cumple_regla_k (posible paso a Sí).
    - Un deterioro de goodwill en el test de FY2026, o una nueva caída del WACC de equilibrio por debajo del 10,0 % (pasaría a No).
    - Un orgánico del grupo negativo dos ejercicios seguidos, o un margen EBITA volviendo hacia el 6,5 % (pasaría a No).
    - Que la deuda neta siga creciendo (793,0 → 1.967,1 entre 2023 y jun-2026) sin que el EBITA consolidado la acompañe.
    - Múltiplos pagados en las compras persistentemente por encima del ‹mid to high single-digit› anunciado (ROFA ~17–18x EBITA según el cálculo de la etapa 1).

### Lo que no sabe

    - El retorno sobre el capital de las adquisiciones: SPIE no publica ROCE ni ROIC. El 14,9 % antes y el 10,4 % después de impuestos son cálculos de la etapa 1.
    - El crecimiento orgánico anual de 2016 a 2024: solo constan 2025 (+2,0 %) y H1 2026 (+1,2 %).
    - El precio es el cierre del 06-nov-2026 de fuentes secundarias; la propia hoja pide actualizarlo. No tengo cotización del 07-nov-2026.
    - El paquete contiene referencias posteriores a la fecha de corte: la 'Decisión del inversor (15-nov-2026)' que fija el periodo de medias 2023–2025, y la emisión de SHARE FOR YOU del 3-dic-2026. Uso solo los datos históricos (medias 2023–2025, anteriores al corte) y no el hecho de esa decisión. La dilución de SHARE FOR YOU 2026 no está en las 174,39 M de acciones.
    - El FCF base depende del periodo elegido: antes de SBC sería 496,0 (3 años), 409,4 (5 años) o 632,2 (LTM, con +112 de circulante). Ninguna base incluye ROFA ni SGS.
    - No hay modelo de ventas ni márgenes proyectados. El crecimiento implícito se da sobre el FCF a 10 años, no sobre las ventas a cinco años.
    - No se conoce el umbral vigente del covenant a junio de 2026, el factoring alemán a junio, el supplier finance ni el precio medio de las recompras.
    - La deuda a junio de 2026 incluye ≈698 M€ pagados por sociedades aún no consolidadas, sin su EBITDA. Los ratios de apalancamiento están sesgados al alza.
    - Los escenarios y las cifras base proceden de la etapa 1 (juicio heredado). Los he verificado aritméticamente, pero no contra los estados financieros originales, que no están en el paquete.

### Citas

    [hoja_control_maestro] «Dato: 44,54 € cierre Euronext Paris 06-nov-2026. ACTUALIZAR ANTES DE CUALQUIER DECISIÓN.» → Precio actual y su fecha.
    [hoja_control_maestro] «CFO 840,3 − capex 75,1 − intereses en financiación 84,1 − principal arrendamientos 185,1 − SBC 38,8 = 457,2» → FCF base del DCF.
    [hoja_control_maestro] «Dato: 174,39 M = 172,86 M acciones actuales (incl. conversión ORNANE) + 1,54 M PSP vivas (planes 2024–2026).» → Acciones diluidas.
    [hoja_analisis] «67,Crecimiento de la caja libre · años 1–10,0,0.05,0.1» → Crecimiento del FCF por escenario.
    [hoja_analisis] «68,Crecimiento para siempre · desde el año 11,0.015,0.02,0.025» → g terminal por escenario.
    [hoja_analisis] «69,Probabilidad que le das,0.2,0.6,0.2» → Probabilidades.
    [hoja_analisis] «78,VALOR INTRÍNSECO POR ACCIÓN,31.8125731061905,47.7529019161083,72.8727722217717» → Valores por acción al 9 %, verificados con cálculo propio.
    [hoja_analisis] «Crecimiento que el precio ya da por hecho,DCF inverso: crecimiento de FCF (años 1–10) que haría que el valor fuese igual al precio actual.,0.0406500625901058» → Crecimiento implícito en el precio.
    [hoja_analisis] «Precio actual,Cotización por acción.,44.54» → Precio usado en la hoja.
    [hoja_control_maestro] «después de impuestos 0,104» → Retorno sobre el capital empleado después de impuestos.
    [hoja_control_maestro] «Ojo: el FCF base no resta adquisiciones (M&A 74–84% del FCF en 2020–2025).» → La base de FCF no paga el crecimiento comprado.
    [respuesta] «crecimiento orgánico (+2,0% en 2025; +1,2% en H1 2026)» → Orgánico reciente.
    [respuesta] «el margen EBITA sobre producción subió de 5,1% (2020) a 6,1% (2021), 6,3% (2022), 6,7% (2023), 7,2% (2024) y 7,6% (2025)» → Tendencia de margen.
    [hoja_control_maestro] «Dato principal: 2,31x = deuda neta publicada sin IFRS 16 1.967,1 + pasivos por arrendamiento 621,2 = 2.588,3 ÷ EBITDA IFRS 16 LTM 1.122,1» → Apalancamiento.
    [hoja_control_maestro] «WACC de equilibrio (g 2%) 11,9% (2023) → 10,0% (2025) vs 8,5% usado» → Holgura decreciente del test de goodwill.
    [hoja_control_maestro] «Dato: 11,8x = mediana del precio de cierre de año ÷ FCF al accionista por acción diluida (antes de SBC), 2016–2025.» → Múltiplo histórico frente al terminal implícito de 14,6x.
    [hoja_control_maestro] «Diluidas medias +1,09%/año (3 años) y +1,37%/año (5 años)» → Dilución recurrente.
    [respuesta] «los impuestos pagados en caja subieron de 96,7 (2023) a 200,1 (2025)» → Viento de cara en la caja.
    [hoja_control_maestro] «Pro forma refinanciación ORNANE → bono 4,875%: +16,4 €m/año de intereses (−0,2 pp de yield).» → Más intereses que presionan el FCF.
    [hoja_control_maestro] «FCF base antes de SBC: 496,0 / 409,4 / 632,2.» → Sensibilidad del FCF base al periodo.
    [hoja_control_maestro] «Sesgo de perímetro: deuda incluye ≈698 €m pagados por sociedades aún no consolidadas sin su EBITDA.» → Sesgo en los ratios de deuda.
    [hoja_control_maestro] «Decisión del inversor (15-nov-2026)» → Referencia posterior a la fecha de corte, no usada como hecho.

### Comprobaciones mecánicas y normalizaciones

    {
      "comprobaciones": {
        "escalera_recalculada_anexo_c": {
          "p_estrella": 44.50714285714285,
          "precio_si": 44.50714285714285,
          "ponderado": 49.586,
          "precio_escenario_malo": 31.81
        },
        "citas_total": 22,
        "citas_literales": 22,
        "avisos": [],
        "nota": "Comprobaciones mecánicas informativas: no acreditan la calidad económica."
      },
      "normalizaciones_enum": []
    }

