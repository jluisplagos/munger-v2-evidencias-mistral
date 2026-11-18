# Análisis directo · Ahold Delhaize, ejercicio 2025 y 2026 hasta el tercer trimestre

Estado de la ejecución: `AUDITORIA_DOCUMENTAL_PENDIENTE_ACEPTACION`

Revisión a ciegas pendiente. No es aceptación, ni integración, ni aptitud para dinero real.

| Campo | Valor |
|---|---|
| Empresa | ahold |
| Fecha de corte | 2026-11-17 |
| Tasa | 9 % |
| Tarea | analisis-directo-ahold-44381043620 |
| SHA del código | e1d5f4baacb89b2adef3261592c5012cb9287266 |
| Huella del paquete (package_sha256) | 95ac4b468142b1d8195acbfb0bfb274c296ea3cad27bd240b433dfdede60a64f |
| Huella del envío (bundle_sha256) | 46119837825fc26cafe0660eff63f60fa0314098294304e823cad93ce61a89d2 |
| Huella del encargo | 022846e95b809a772317c2b17d6d946f3f91b9066c864911e473bb7ea15843e4 |
| Modelo pedido / devuelto | claude-opus-5-5 / claude-opus-5-5 |
| Esfuerzo | high |
| Mensajes enviados | 1 |
| Cota de entrada estimada antes de llamar | 962711 tokens |
| Reserva estimada antes de llamar | USD 4.506204 (máximo de la ejecución USD 5) |
| Reserva registrada | USD 4.506204 |
| Uso de tokens | entrada 388449, salida 19955 |
| Coste | CONOCIDO_ESTIMADO; estimado USD 1.952896; cota 1.952896 |

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
| malo | 24.35 | 0.2 |
| normal | 34.14 | 0.6 |
| bueno | 42 | 0.2 |

| Escalera (k = 3) | Declarado | Recalculado (Anexo C) |
|---|---|---|
| Precio actual | 36.05 | |
| Precio del escenario malo | 24.35 | 24.35 |
| P* | 31.07 | 31.0671 |
| Precio de Sí = mín(P*, V_normal) | 31.07 | 31.0671 |
| Ponderado | 33.75 | 33.754 |
| Crecimiento implícito al precio actual / del normal (%) | 3.8 / 2.5 | |

| Tasa | Precio de Sí | Ponderado | Zona |
|---|---|---|---|
| 7 % | 43.03 | 47.34 | cumple_regla_k |
| 8 % | 36.07 | 39.4 | cumple_regla_k |
| 9 % | 31.07 | 33.75 | caro |
| 10 % | 27.29 | 29.52 | caro |
| 11 % | 24.33 | 26.23 | caro |

### Resumen

    Ahold Delhaize es un minorista de alimentación de margen bajo (margen operativo subyacente del 4,0 %) y foso local estrecho. Su caja libre para el accionista, después de capex, intereses, arrendamientos y SBC, está estancada en torno a 2.000 M€ (media 2023-2025: 1.999 M€). El 4-nov-2026 la empresa recortó su guía: caja libre de unos 2.100 M€ (antes, al menos 2.300 M€), por el ciberincidente y las nuevas normas de pago a proveedores en Serbia. Con un DCF al accionista al 9 %, cinco años de crecimiento explícito, valor terminal de Gordon y 872 M de acciones diluidas, el valor por acción sale en 24,35 € en el escenario malo, 34,14 € en el normal y 42,00 € en el bueno. El ponderado es 33,75 € y el precio de Sí, según la regla k=3, es 31,07 €. A 36,05 € (13-nov-2026) el precio queda por encima del ponderado (zona caro) y descuenta un crecimiento anual de la caja libre de alrededor del 3,8 % durante cinco años, frente al 2,5 % del escenario normal. Conclusión: Vigilar y esperar.


### Moneda

    EUR


### Justificación

    El estado es concluido: hay datos suficientes (diez años de historia, informes del 2T y del 3T-2026 y precio del 13-nov) y el DCF al accionista es aplicable, con los arrendamientos e intereses restados del flujo. El cubo es Vigilar y no No porque el negocio es comprensible, con cuota defendida, rating BBB+/Baa1 y deuda neta/EBITDA de 2,2x, y porque el precio de Sí (31,07 €) está a solo un 14 % del precio actual. No es Sí porque a 36,05 € el precio supera tanto el valor del escenario normal como el ponderado y exige un crecimiento del 3,8 % anual que la caja libre no ha mostrado desde 2022. La acción es esperar a un precio igual o inferior a unos 31 € sin deterioro del negocio.


### Probabilidades

    Mantengo 0,2 / 0,6 / 0,2. El recorte de la guía, el estancamiento de la caja libre y la compresión del margen en EE. UU. ya están recogidos en el diseño del escenario malo (−3 % anual) y en el crecimiento moderado del normal. Penalizarlos además en la probabilidad sería contar dos veces el mismo riesgo. Suman 1.


### Fórmula aplicada

    G(P) = 0,6·max(34,14−P;0) + 0,2·max(42,00−P;0); L(P) = 0,2·max(P−24,35;0). Para P entre 24,35 y 34,14: G = 28,884 − 0,8P y 3L = 0,6P − 14,61. G ≥ 3L ⇔ 43,494 ≥ 1,4P ⇔ P ≤ 31,07, así que P* = 31,07. Precio de Sí = mín(31,07; 34,14) = 31,07. Ponderado = 0,2·24,35 + 0,6·34,14 + 0,2·42,00 = 33,75. Como 36,05 > 24,35, 36,05 > 31,07 y 36,05 > 33,75, la zona es caro.


### Crecimiento implícito

    En el escenario normal el margen de caja libre sobre ventas es constante, de modo que el crecimiento de las ventas es igual al de la caja libre. Mantengo la base de 1.999,33 M€, el crecimiento perpetuo del 2 %, r = 9 % y 872 M acciones, y busco el crecimiento de los años 1-5 que iguala el valor al precio: 36,05 × 872 = 31.436 M€. Con un 3,75 % el valor es 31.403 M€ (36,01 €); con un 4 %, 31.739 M€ (36,40 €). Interpolando sale aproximadamente un 3,8 % anual, frente al 2,5 % del escenario normal.

### Escenario malo

    Supuestos: caja libre base de 1.999,33 M€ (CFO medio 6.559,67 − capex 2.432,33 − intereses 239 − arrendamientos 1.834 − SBC 55), que cae un 3 % al año en los años 1-5 hasta unos 1.717 M€, y crecimiento perpetuo del 1 % desde el año 6. Narrativa: la inversión de 1.000 M$ en precios en EE. UU. no se recupera, el margen subyacente pasa del 4,0 % al 3,5 % y el capex y los arrendamientos siguen subiendo. Es la prolongación del 3T-2026: margen de EE. UU. en el 4,3 % (−0,3 pp), comparables de EE. UU. del 0,5 % y guía de caja libre rebajada. Cálculo: valor actual de los años 1-5 = 7.141 M€; valor terminal descontado = 14.088 M€; total 21.229 M€ ÷ 872 M acciones = 24,35 €.

### Escenario normal

    Supuestos: ventas nominales con un crecimiento del 2,5 % anual en los años 1-5 y margen de caja libre sobre ventas constante, por lo que la caja libre crece también un 2,5 %; crecimiento perpetuo del 2 % desde el año 6. Apoyo: comparables del grupo del 3,2 % en 2025 y del 1,2-1,4 % en 2026, aperturas netas, margen subyacente defendido en torno al 4 % y una base de caja libre de 1.999,33 M€. El múltiplo de salida implícito, (1,02)/(0,09−0,02) = 14,6x, coincide con la mediana histórica de P/FCF de 14,7x. Cálculo: años 1-5 = 8.344 M€; valor terminal descontado = 21.423 M€; total 29.767 M€ ÷ 872 = 34,14 €. Ni el exceso de caja (0) ni la deuda se tocan, porque el flujo ya va después de intereses y arrendamientos.

### Escenario bueno

    Supuestos: caja libre que crece un 6 % anual en los años 1-5, hasta unos 2.676 M€, y crecimiento perpetuo del 2,5 %. Narrativa: el ahorro de Save for Our Customers (1.294 M€ en 2025; 5.000 M€ previstos en 2025-2028) y los ingresos complementarios llegan al margen, que sube hacia el 4,4-4,5 %; la integración de Profi y el online ya rentable apalancan. Cálculo: años 1-5 = 9.201 M€; valor terminal descontado = 27.422 M€; total 36.622 M€ ÷ 872 = 42,00 €. El múltiplo de salida implícito es de 15,8x.

### Sensibilidad (comentarios)

    7 %: Valores de los escenarios: 32,25 / 47,83 / 60,98. Con una tasa del 7 % el precio actual cumpliría la regla k. Es solo información: la conclusión se toma al 9 %.
    8 %: Valores de los escenarios: 27,74 / 39,84 / 49,76. El precio de Sí (36,07) queda prácticamente igual al precio actual (36,05): está en el límite.
    9 %: Coincide con la escalera. Valores de los escenarios: 24,35 / 34,14 / 42,00.
    10 %: Valores de los escenarios: 21,71 / 29,86 / 36,31.
    11 %: Valores de los escenarios: 19,59 / 26,53 / 31,96.

### Qué haría falsa la conclusión

    - Que el precio baje a 31 € o menos sin que empeoren el margen ni la caja libre: pasaría a Sí.
    - Dos ejercicios con margen operativo subyacente por encima del 4,2 % y caja libre de la empresa por encima de 2.300 M€ sin ayuda del circulante: subiría el escenario normal y, con él, el precio de Sí.
    - Que el margen subyacente de 2026-2027 baje del 3,8 % o que las comparables sean negativas a la vez en EE. UU. y en Europa: el escenario malo pasaría a ser el central y el cubo a No.
    - Que la caja libre con mi definición (CFO − capex − intereses − arrendamientos − SBC) caiga por debajo de 1.700 M€ en 2027 una vez pasado el ciberincidente.
    - Un sobreprecio o problemas de integración en Tesco Chequia y Eslovaquia (valor de empresa de unos 1.200 M€; 1.700 M€ ajustado por arrendamientos), o una rebaja del rating por debajo de BBB/Baa2.
    - Pruebas en las cifras de que el precio y el surtido se deciden en agregadores o agentes de IA: pasaría a Demasiado difícil.

### Lo que no sabe

    - El precio de 36,05 € procede de una fuente secundaria (Trivano), es del 13-nov-2026, sin hora, y no hay cotización del 16 o del 17 de noviembre.
    - El archivo datos_v63 lleva fecha de análisis 2026-11-18, un día después del corte. Solo uso de él datos fechados antes del corte; no hay en él hechos posteriores identificables.
    - Número de acciones: uso la media diluida del 3T-2026 (872 M). Las acciones en circulación eran 865,17 M a 27-sep-2026 y la recompra sigue, así que la cifra a fecha de corte puede ser algo menor, lo que daría un valor por acción algo mayor.
    - La compra de Tesco Chequia y Eslovaquia no está modelada: no se publican sus ventas, resultado ni múltiplo. La trato como neutral en valor.
    - No conozco el efecto real del ciberincidente ni los resultados del 4T-2026 (solo hay estimaciones: ventas −200 a −250 M€ y resultado operativo −75 a −100 M€).
    - La base de caja libre de 2023-2025 incluye la devolución fiscal belga de 2023 (+367 M€) y circulante favorable en 2025. La caja libre normalizada podría ser más baja: el LTM es de unos 1.763 M€ después de SBC y la guía de 2026 implica menos de 2.000 M€ con mi definición.
    - No existe una serie publicada de ROIC/ROCE, ni desglose de precio, volumen y mezcla, ni competidores nombrados, ni cuota fuera de Países Bajos.
    - No hay confirmación de las calificaciones crediticias vigentes en 2026.
    - Los ceros de minoritarios están pendientes de verificación (no son materiales). El valor externo de Simply Wall St (61,27 €) no se usa porque no está verificado.
    - Límite del modelo: DCF simplificado con cinco años de crecimiento explícito y valor terminal de Gordon. Más del 60 % del valor viene del valor terminal, así que el resultado es muy sensible a r y a g.

### Citas

    [datos_v63_md] «Trivano (trivano.com, ficha Ahold Delhaize AD, Euronext Amsterdam), 36,05 EUR, +2,12 % el 2026-11-13, hora no indicada» → Precio actual y su fecha.
    [datos_v63_md] «fecha de análisis 2026-11-18» → La fecha del archivo es posterior al corte (se declara en lo que no sé).
    [datos_v63_md] «2023 cfo (Historia) 6466.0; 2024 cfo (Historia) 6224.0; 2025 cfo (Historia) 6989.0» → CFO medio de 6.559,67 M€.
    [datos_v63_md] «2023 capex (Historia) 2434.0; 2024 capex (Historia) 2299.0; 2025 capex (Historia) 2564.0» → Capex medio de 2.432,33 M€.
    [etapa1_ahold_evaluada_control_maestro_csv] «CFO 6.559,7 − capex 2.432,3 − intereses 239,0 − arrendamientos 1.834,0 − SBC 55 = 1.999,4 M€» → Construcción de la caja libre base.
    [datos_v63_md] «FCF base (C52, fórmula): 1999.33» → Caja libre base usada en los tres escenarios.
    [fuentes_ar_2025_seleccion] «Repayments of lease liabilities (1,944) (1,743)» → Pagos de arrendamientos (principal más intereses) en aumento.
    [fuentes_ar_2025_seleccion] «Interest paid (261) (230)» → Intereses pagados, clasificados en financiación.
    [fuentes_ad_q3_2026_interim_report_compact] «Diluted 872 902 880 909» → Acciones diluidas medias del 3T-2026 (872 M), usadas para el valor por acción.
    [fuentes_ad_q3_2026_interim_report_compact] «The number of outstanding common shares as of September 27, 2026, was 865,173,863» → Acciones en circulación recientes.
    [fuentes_ad_q3_2026_interim_report_compact] «of around €2.1 billion (previously at least €2.3 billion)» → Recorte de la guía de caja libre de 2026.
    [fuentes_ad_q3_2026_interim_report_compact] «between €200 and €250 million and underlying and IFRS operating income by between €75 million and» → Efecto estimado del ciberincidente en el 4T.
    [fuentes_ad_q3_2026_interim_report_compact] «Underlying operating margin in the U.S. was 4.3%, down 0.3 percentage points as a result of the cycling of» → Compresión del margen en EE. UU. (escenario malo).
    [fuentes_ad_q3_2026_interim_report_compact] «Q3 comparable sales excluding gasoline increased 0.5% in the U.S.» → Crecimiento comparable débil en EE. UU.
    [fuentes_ad_q3_2026_interim_report_compact] «Free cash flow 445 389 747 1,104» → Caja libre acumulada a 39 semanas inferior a la de 2025.
    [fuentes_ad_q3_2026_interim_report_compact] «Net debt 16,087 15,961 14,699» → Deuda neta en aumento.
    [fuentes_ad_q3_2026_interim_report_compact] «enterprise value of approximately €1.2 billion, corresponding to a lease-adjusted enterprise value of €1.7» → Compra de Tesco Chequia y Eslovaquia, no modelada.
    [fuentes_ad_q3_2026_interim_report_compact] «Ahold Delhaize announces a €1 billion share buyback program to start at the beginning of 2027» → La recompra continúa y reduce el número de acciones.
    [fuentes_ar_2025_seleccion] «Underlying operating income margin 4.0% 4.0% 0.0pp» → Margen subyacente estancado en el 4,0 %.
    [fuentes_ar_2025_seleccion] «we delivered €1,294 million in savings» → Ahorro que no se refleja en el margen (palanca del escenario bueno).
    [extracto_v63_md] «Compromiso de invertir 1.000 millones de dólares en precios en EE. UU. de 2025 a 2028.» → Presión sobre los márgenes.
    [extracto_v63_md] «Ventas comparables sin gasolina, Grupo: 3,2 % (2025; 86.680 frente a 84.004 millones)» → Base del crecimiento de ventas del escenario normal.
    [etapa1_ahold_evaluada_control_maestro_csv] «Mediana P/FCF con la definición de la fila 52 (antes de SBC): 14,7x» → Contraste del múltiplo de salida implícito (14,6x).
    [etapa1_ahold_evaluada_control_maestro_csv] «= 16.065 ÷ EBITDA LTM 7.252» → Deuda neta/EBITDA de 2,2x: balance sostenible.
    [fuentes_ar_2025_seleccion] «Leased % of total 85% 46%» → Rigidez por arrendamientos.
    [fuentes_ar_2025_seleccion] «the recoverable amount for Profi marginally exceeds the carrying amount» → Riesgo de deterioro de Profi.
    [datos_v63_md] «Bund alemán a 10 años, 3,34 % a cierre de octubre de 2026» → Referencia sin riesgo; los crecimientos perpetuos quedan por debajo de r.

### Comprobaciones mecánicas y normalizaciones

    {
      "comprobaciones": {
        "escalera_recalculada_anexo_c": {
          "p_estrella": 31.067142857142855,
          "precio_si": 31.067142857142855,
          "ponderado": 33.754,
          "precio_escenario_malo": 24.35
        },
        "citas_total": 27,
        "citas_literales": 27,
        "avisos": [],
        "nota": "Comprobaciones mecánicas informativas: no acreditan la calidad económica."
      },
      "normalizaciones_enum": []
    }

