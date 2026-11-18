# Análisis directo · Ahold Delhaize, ejercicio 2025 y 2026 hasta el tercer trimestre

Estado de la ejecución: `AUDITORIA_DOCUMENTAL_PENDIENTE_ACEPTACION`

Revisión a ciegas pendiente. No es aceptación, ni integración, ni aptitud para dinero real.

| Campo | Valor |
|---|---|
| Empresa | ahold |
| Fecha de corte | 2026-11-17 |
| Tasa | 9 % |
| Tarea | analisis-directo-ahold-44381146484 |
| SHA del código | e1d5f4baacb89b2adef3261592c5012cb9287266 |
| Huella del paquete (package_sha256) | 95ac4b468142b1d8195acbfb0bfb274c296ea3cad27bd240b433dfdede60a64f |
| Huella del envío (bundle_sha256) | 617044173708ed5a6defdb65af705027a852556ade0bfd22692288b5f3f8daad |
| Huella del encargo | 022846e95b809a772317c2b17d6d946f3f91b9066c864911e473bb7ea15843e4 |
| Modelo pedido / devuelto | claude-opus-5-5 / claude-opus-5-5 |
| Esfuerzo | high |
| Mensajes enviados | 1 |
| Cota de entrada estimada antes de llamar | 962711 tokens |
| Reserva estimada antes de llamar | USD 4.506204 (máximo de la ejecución USD 5) |
| Reserva registrada | USD 4.506204 |
| Uso de tokens | entrada 388449, salida 18338 |
| Coste | CONOCIDO_ESTIMADO; estimado USD 1.920556; cota 1.920556 |

## Paquete de entrada

| id | ruta | commit | sha256 | bytes |
|---|---|---|---|---|
| datos_v63_md | datos_analisis_directo/ahold/datos_v63.md | e1d5f4baacb8 | 2e68b9e31eb382a38da0bef6b71bef6c1ecc6358451cd8acbdde6b1bf5cb99fd | 99402 |
| etapa1_ahold_evaluada_analisis_csv | datos_analisis_directo/ahold/etapa1/Ahold_evaluada__Análisis.csv | e1d5f4baacb8 | c1f96126ddc3013e6d2a8baa9f6c403d2794e296de03bbde487b2de40e946634 | 24438 |
| etapa1_ahold_evaluada_control_maestro_csv | datos_analisis_directo/ahold/etapa1/Ahold_evaluada__Control_maestro.csv | e1d5f4baacb8 | 186883b5fa1a548a447fe94cbac2a4e41756d2697d9fc77975517973fa20b363 | 72799 |
| etapa1_ahold_evaluada_guia_simply_wall_st | datos_analisis_directo/ahold/etapa1/Ahold_evaluada__Guía_Simply_Wall_St.csv | e1d5f4baacb8 | e3cabea03c1a776ed1203ce43f216ec3b29760e8c866e2b925b8990e31152651 | 7660 |
| etapa1_ahold_evaluada_opciones_csv | datos_analisis_directo/ahold/etapa1/Ahold_evaluada__Opciones.csv | e1d5f4baacb8 | 56246fb2e5ca7ca826b3c07c4786422bb1cf9c5a3a0d110abc53919735356a4d | 1486 |
| etapa1_ahold_respuesta_md | datos_analisis_directo/ahold/etapa1/Ahold_respuesta.md | e1d5f4baacb8 | bb7597fa4e967e11eb70402c906a85440c5942b0cdc5c40b0e92c5cbc15aa013 | 49066 |
| extracto_v63_md | datos_analisis_directo/ahold/extracto_v63.md | e1d5f4baacb8 | fd9ea974c6f1320a54d82bee7888d762efaa1799f1f8d73b2e9c9af5c26a53d1 | 48919 |
| fase1_v63_json | datos_analisis_directo/ahold/fase1_v63.json | e1d5f4baacb8 | d072f96cf5d6b2a3a2aeedadc69d1d5224253b20f81dbc2d73ee276212fd8b59 | 46583 |
| fuentes_ar_2025_seleccion | datos_analisis_directo/ahold/fuentes/AD_annual-report-2025.seleccion.compacto.txt | e1d5f4baacb8 | f8d71271223ed69fd0f6cd76288a8609edc8c7a868e9617f356a31e209c2a9cb | 388466 |
| fuentes_ad_q2_2026_interim_report_compact | datos_analisis_directo/ahold/fuentes/AD_q2-2026-interim-report.compacto.txt | e1d5f4baacb8 | b03269b20b4f948389d4251ec701b7b491c128bc99d0ee3d4441da14914c471c | 76766 |
| fuentes_ad_q3_2026_interim_report_compact | datos_analisis_directo/ahold/fuentes/AD_q3-2026-interim-report.compacto.txt | e1d5f4baacb8 | 3cc9ceb064363e7f4ad57bd04fb2cff8ec1e63c87c0effda67ab6fce25548b23 | 86005 |
| registro_entradas_lista_entradas_csv | datos_analisis_directo/ahold/registro_entradas/LISTA_ENTRADAS.csv | e1d5f4baacb8 | 174ca2271d9dbb4b08ccdc27712ea61d48f29d1b108c35c0581a614987715c92 | 13418 |

## Salida del modelo (datos, sin acciones ejecutables)

Estado `concluido` · cubo «Vigilar» · acción `esperar` · zona `caro`

| Escenario | Valor por acción | Probabilidad |
|---|---|---|
| malo | 23.37 | 0.2 |
| normal | 34.67 | 0.6 |
| bueno | 47.08 | 0.2 |

| Escalera (k = 3) | Declarado | Recalculado (Anexo C) |
|---|---|---|
| Precio actual | 36.05 | |
| Precio del escenario malo | 23.37 | 23.37 |
| P* | 31.6 | 31.6 |
| Precio de Sí = mín(P*, V_normal) | 31.6 | 31.6 |
| Ponderado | 34.89 | 34.892 |
| Crecimiento implícito al precio actual / del normal (%) | 3.4 / 2.5 | |

| Tasa | Precio de Sí | Ponderado | Zona |
|---|---|---|---|
| 7 % | 43.89 | 49.2 | cumple_regla_k |
| 8 % | 36.73 | 40.83 | cumple_regla_k |
| 9 % | 31.6 | 34.89 | caro |
| 10 % | 27.73 | 30.45 | caro |
| 11 % | 24.71 | 27.01 | caro |

### Resumen

    Ahold Delhaize es un minorista de alimentación maduro. Su caja libre para el accionista es de unos 2.000 mm€ al año, después de capex, intereses, arrendamientos y SBC, y no crece desde 2022. En el 3T de 2026 la empresa rebajó su guía de caja libre a unos 2.100 mm€, por un incidente de ciberseguridad y por nuevas normas de pago en Serbia. Descuento ese flujo al 9 % con 872 millones de acciones diluidas. Salen 23,37 € en el escenario malo, 34,67 € en el normal y 47,08 € en el bueno. El ponderado es 34,89 € y el precio de Sí con la regla k=3 es 31,60 €. A 36,05 € (13-nov-2026) la acción queda en zona cara: el precio descuenta un crecimiento de alrededor del 3,4 % anual frente al 2,5 % de mi caso normal. El negocio es comprensible y sólido, pero no hay margen. Cubo Vigilar y acción esperar.


### Moneda

    EUR


### Justificación

    Estado concluido: las cifras del paquete bastan para valorar con un DCF del flujo al accionista, después de arrendamientos (IFRS 16) e intereses. El negocio es comprensible y estable: margen del 4 %, BBB+ y unos 2.000 mm€ de caja libre.
    Cubo Vigilar y no No: el foso local existe (cuota de Albert Heijn y racha de comparables de Food Lion) y el balance aguanta.
    Cubo Vigilar y no Sí, acción esperar:
    - A 36,05 € el precio supera el ponderado de 34,89 € y el precio de Sí de 31,60 €.
    - El precio descuenta un crecimiento del 3,4 %, cuando la caja libre está plana desde 2022 y la guía de 2026 acaba de bajar a ~2.100 mm€.
    - Solo a tasas del 7-8 % cumpliría la regla k.


### Probabilidades

    Mantengo las probabilidades de partida 0,2 / 0,6 / 0,2. La meseta de la caja libre y la rebaja de la guía de 2026 ya están recogidas en el crecimiento de los escenarios: rebajé el normal del 3 % al 2,5 % y el bueno del 8 % al 6 %. Penalizar además la probabilidad contaría dos veces el mismo riesgo.


### Fórmula aplicada

    Para 23,37 < P < 34,67:
    - G(P) = 0,6·(34,67−P) + 0,2·(47,08−P) = 30,218 − 0,8P
    - L(P) = 0,2·(P−23,37) = 0,2P − 4,674
    Condición G ≥ 3L: 30,218 − 0,8P ≥ 0,6P − 14,022, es decir P ≤ 44,240/1,4 = 31,60. Por tanto P* = 31,60.
    Precio de Sí = mín(31,60; 34,67) = 31,60.
    Ponderado = 0,2·23,37 + 0,6·34,67 + 0,2·47,08 = 34,89.
    Zona: el precio de 36,05 es mayor que el ponderado de 34,89, luego caro.


### Crecimiento implícito

    En el escenario normal la caja libre es un porcentaje fijo de las ventas, así que crece al mismo ritmo que ellas. Mantengo el resto del normal: años 6-10 al 2,5 %, perpetuidad al 2 %, tasa del 9 % y caja libre base de 1.999,33 mm€. Busco el crecimiento de los años 1-5 que iguala el valor a la capitalización (36,05 × 872 = 31.436 mm€). Interpolando entre el 3,3 % (factor 15,650) y el 3,5 % (15,785) frente al objetivo de 15,723, sale un 3,4 % aproximado.

### Escenario malo

    Supuestos:
    - Caja libre base de 1.999,33 mm€ (C52: media 2023-25 de CFO 6.559,67 − capex 2.432,33 − intereses 239 − arrendamientos 1.834 − SBC 55).
    - La caja libre cae un 2 % anual durante 10 años y después crece un 1 % a perpetuidad.
    - Tasa del 9 %.
    Relato: guerra de precios en EE. UU. y margen subyacente del 4,0 % hacia el 3,3-3,5 %. Las rentas suben más que el resultado: los pagos de arrendamientos pasaron de 1.743 a 1.944 mm€ y hay 14.721 mm€ de pagos no descontados. Las comparables de EE. UU. bajan al 0,5 % en el 3T de 2026.
    Cálculo: valor total 20.376 mm€ ÷ 872 M de acciones = 23,37 €.

### Escenario normal

    Supuestos:
    - Ventas y caja libre crecen un 2,5 % anual durante 10 años, con el margen de caja libre constante (2,17 % de las ventas de 2025, 92.352 mm€).
    - Crecimiento perpetuo del 2 %.
    - Tasa del 9 %.
    Justificación: la inflación de alimentos prevista por el USDA (+2,7 %) más las aperturas compensan unas comparables del 1,2-1,4 % en 2026. El margen subyacente se mantiene alrededor del 4 % (4,0 % en 2024 y 2025; 4,1 % en el 3T de 2026). La propia previsión de caja libre acumulada de 9.000 mm€ en 2025-28 implica una caja libre plana. Rebajo así el 3 % que suponía la etapa 1.
    Cálculo: 14.480 (valor actual de los años 1-10) + 15.753 (valor terminal) = 30.233 mm€ ÷ 872 = 34,67 €.

### Escenario bueno

    Supuestos:
    - La caja libre crece un 6 % anual durante 10 años y después un 2,5 % a perpetuidad.
    - Tasa del 9 %.
    Relato: el ahorro de 5.000 mm€ del programa 2025-28 y los 3.000 mm€ de ingresos complementarios llegan al margen, que sube hacia el 4,5 %. El canal online, ya rentable, apalanca el resultado, y el capex elevado (~2.700 mm€) empieza a rendir.
    Uso el 6 % y no el 8 % de la etapa 1, porque el margen lleva cinco años plano.
    Cálculo: 17.203 + 23.850 = 41.053 mm€ ÷ 872 = 47,08 €.

### Sensibilidad (comentarios)

    7 %: Escenarios: malo 30,63, normal 48,68 y bueno 69,33. El precio actual cumple la regla k; solo es informativo.
    8 %: Escenarios: malo 26,49, normal 40,50 y bueno 56,16. El precio cumple la regla k por muy poco (36,05 frente a 36,73).
    9 %: Tasa de la conclusión; coincide con la escalera. Escenarios: malo 23,37, normal 34,67 y bueno 47,08.
    10 %: Escenarios: malo 20,93, normal 30,30 y bueno 40,44.
    11 %: Escenarios: malo 18,97, normal 26,90 y bueno 35,39.

### Qué haría falsa la conclusión

    - Que el precio baje a 31,60 € o menos sin que empeoren los hechos del negocio: pasaría a Sí.
    - Que la caja libre del accionista supere 2.300 mm€ dos ejercicios seguidos sin ayuda del circulante, con el margen subyacente por encima del 4,2 %: subiría el escenario normal y el precio de Sí.
    - Que el margen subyacente quede por debajo del 3,8 % dos trimestres seguidos, o que las comparables de EE. UU. y de Europa sean negativas a la vez: pasaría a No o subiría la probabilidad del escenario malo.
    - Que los resultados del 4T y del año 2026 (17-feb-2027) muestren una caja libre claramente por debajo de ~2.100 mm€, o efectos del incidente de ciberseguridad que se prolonguen más allá del 4T.
    - Que la compra de Tesco Chequia y Eslovaquia (valor empresa de 1.200 mm€) eleve la deuda neta con arrendamientos por encima de 2,5 veces el EBITDA o rompa la política de recompras: revisaría la asignación de capital.
    - Que se materialice una desintermediación por agregadores o compras mediante agentes de IA que fijen precio y surtido: pasaría a Demasiado difícil.

### Lo que no sabe

    - El precio de 36,05 € procede de una fuente secundaria (Trivano), del 13-nov-2026 y sin hora. No hay cotización del 16 o del 17 de noviembre.
    - El archivo datos_v63 lleva fecha de análisis 18-nov-2026, posterior al corte. Uso solo sus datos, que son anteriores al corte (precio del 13-nov e informes hasta el 3T). No uso nada posterior a la fecha de corte.
    - Acciones: uso 872 M, la media diluida del 3T de 2026. Las acciones en circulación eran 865,2 M a 27-sep-2026 y la recompra siguió después. Con las 905 M de la hoja, los valores serían un 3,6 % menores.
    - La caja libre base (media 2023-25) incluye la devolución fiscal belga de 2023 y circulante favorable en 2025. A la vez excluye los intereses cobrados, los cobros por subarriendos y los dividendos de negocios conjuntos (≈300 mm€). Su sesgo neto es incierto.
    - No conozco el efecto real del incidente de ciberseguridad (solo la estimación del 3T), ni el efecto permanente de las nuevas normas de pago a proveedores en Serbia sobre el circulante.
    - No conozco el múltiplo pagado por Tesco Chequia y Eslovaquia ni las ventas y resultados de esa empresa; su efecto no está en la valoración.
    - No hay serie publicada de ROIC ni desglose de precio, volumen y mezcla. La empresa no nombra competidores.
    - No hay calificaciones crediticias de 2026 en los documentos.
    - El valor de Simply Wall St (61,27 €) no está verificado y no lo uso.
    - Hay ceros de arrendamientos (2016-17) y de minoritarios pendientes de verificación humana. No afectan a la base de 2023-25.
    - La holgura de deterioro es pequeña en Stop & Shop (~2 %), Giant Food (~1 %) y Profi (marginal); no está modelada.

### Citas

    [datos_v63_md] «Trivano (trivano.com, ficha Ahold Delhaize AD, Euronext Amsterdam), 36,05 EUR, +2,12 % el 2026-11-13» → Precio actual y su fecha
    [datos_v63_md] «FCF base (C52, fórmula): 1999.33» → Caja libre base de todos los escenarios
    [datos_v63_md] «| C46 | CFO medio (mm) | 6559.67 |» → CFO medio de 2023-25 usado en la caja libre base
    [fuentes_ar_2025_seleccion] «Operating cash flows from continuing operations 6,989 6,224» → CFO de 2025 y 2024
    [fuentes_ar_2025_seleccion] «Purchase of non-current assets (2,564) (2,299)» → Capex de 2025 y 2024
    [fuentes_ar_2025_seleccion] «Interest paid (261) (230)» → Intereses pagados, clasificados en financiación
    [fuentes_ar_2025_seleccion] «Repayment of lease liabilities 28 (1,944) (1,743)» → Pagos de arrendamientos restados de la caja libre
    [fuentes_ar_2025_seleccion] «Share-based compensation expenses 32 70 42» → SBC restada de la caja libre
    [fuentes_ad_q3_2026_interim_report_compact] «Diluted 872 902 880 909» → Acciones diluidas medias del 3T de 2026 (872 M) usadas en el valor por acción
    [fuentes_ad_q3_2026_interim_report_compact] «The number of outstanding common shares as of September 27, 2026, was 865,173,863» → Acciones en circulación recientes
    [fuentes_ad_q3_2026_interim_report_compact] «free cash flow of around €2.1 billion (previously at least» → Rebaja de la guía de caja libre de 2026
    [fuentes_ad_q3_2026_interim_report_compact] «to reduce Q4 net sales by between €200 million and €250 million and underlying and IFRS operating» → Efecto estimado del incidente de ciberseguridad
    [fuentes_ad_q3_2026_interim_report_compact] «enterprise value of approximately €1.2 billion, corresponding to a lease-adjusted enterprise value of €1.7» → Adquisición de Tesco Chequia y Eslovaquia
    [fuentes_ad_q3_2026_interim_report_compact] «Net debt 16,087 15,961 14,699» → Deuda neta con arrendamientos al 3T de 2026
    [fuentes_ad_q3_2026_interim_report_compact] «Q3 comparable sales excluding gasoline increased 0.5% in the U.S.» → Debilidad de las comparables en EE. UU. (escenario malo)
    [fuentes_ad_q3_2026_interim_report_compact] «Q3 net sales were €23.1 billion, up 1.9% at constant exchange rates» → Crecimiento de ventas reciente (escenario normal)
    [fuentes_ad_q3_2026_interim_report_compact] «Q3 underlying operating margin was 4.1%, a decrease of 0.1 percentage points at constant exchange» → Margen subyacente estable alrededor del 4 %
    [fuentes_ad_q3_2026_interim_report_compact] «Free cash flow 445 389 747 1,104» → Caja libre acumulada a 39 semanas inferior a la de 2025
    [fuentes_ad_q3_2026_interim_report_compact] «Ahold Delhaize announces a €1 billion share buyback program to start at the beginning of 2027» → Continuidad de la recompra
    [fuentes_ar_2025_seleccion] «Underlying operating income margin 4.0% 4.0% 0.0pp» → Margen subyacente plano en 2024-25
    [fuentes_ar_2025_seleccion] «Free cash flow2 2,600 2,545 2.2%» → Caja libre de 2025 en la definición de la empresa
    [fuentes_ar_2025_seleccion] «forecast of €9 billion over the four-year period» → Caja libre acumulada prevista para 2025-28, que implica una caja libre plana
    [fuentes_ar_2025_seleccion] «Total undiscounted lease payments 14,721 15,080» → Rigidez por arrendamientos (escenario malo)
    [fuentes_ar_2025_seleccion] «The recoverable amount for Stop & Shop exceeds the carrying amount by slightly more than 2%.» → Holgura de deterioro reducida en Stop & Shop
    [extracto_v63_md] «USDA, precios de alimentos +2,7 % (2025: 3,0 %)» → Inflación de alimentos que sostiene el crecimiento del 2,5 % del escenario normal
    [datos_v63_md] «Bund alemán a 10 años, 3,34 % a cierre de octubre de 2026» → Referencia de tasa sin riesgo frente a la tasa del 9 %

### Comprobaciones mecánicas y normalizaciones

    {
      "comprobaciones": {
        "escalera_recalculada_anexo_c": {
          "p_estrella": 31.599999999999998,
          "precio_si": 31.599999999999998,
          "ponderado": 34.892,
          "precio_escenario_malo": 23.37
        },
        "citas_total": 26,
        "citas_literales": 26,
        "avisos": [],
        "nota": "Comprobaciones mecánicas informativas: no acreditan la calidad económica."
      },
      "normalizaciones_enum": []
    }

