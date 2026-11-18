# Análisis directo · Zoetis, ejercicio 2025 y 2026 hasta el segundo trimestre (primer tiempo)

Estado de la ejecución: `AUDITORIA_DOCUMENTAL_PENDIENTE_ACEPTACION`

Revisión a ciegas pendiente. No es aceptación, ni integración, ni aptitud para dinero real.

| Campo | Valor |
|---|---|
| Empresa | zoetis |
| Fecha de corte | 2026-10-09 |
| Tasa | 9 % |
| Tarea | analisis-directo-zoetis-44402575472 |
| SHA del código | e96470eb0a4401b13d6a265312a2f421cea26f20 |
| Huella del paquete (package_sha256) | 962744ebf5b961d4122fd4e6098b4a931b46ea02a82440e5a66432fd5d524cf2 |
| Huella del envío (bundle_sha256) | 77c9ca18cfad95f8cff1f4edf272a63e54f84f8e26d0193a48ded7930081dedf |
| Huella del encargo | 022846e95b809a772317c2b17d6d946f3f91b9066c864911e473bb7ea15843e4 |
| Modelo pedido / devuelto | claude-opus-5-5 / claude-opus-5-5 |
| Esfuerzo | high |
| Mensajes enviados | 1 |
| Cota de entrada estimada antes de llamar | 943029 tokens |
| Reserva estimada antes de llamar | USD 4.427476 (máximo de la ejecución USD 5) |
| Reserva registrada | USD 4.427476 |
| Uso de tokens | entrada 369300, salida 19770 |
| Coste | CONOCIDO_ESTIMADO; estimado USD 1.8726; cota 1.8726 |

## Paquete de entrada

| id | ruta | commit | sha256 | bytes |
|---|---|---|---|---|
| datos_v63_md | datos_analisis_directo/zoetis/datos_v63.md | e96470eb0a44 | 9369c2ee3ef78c3320da80867ef3b8104fad7d4dbcd488c1a1da5d68504edde5 | 89876 |
| etapa1_zoetis_analisis_csv | datos_analisis_directo/zoetis/etapa1/Zoetis_evaluada__Análisis.csv | e96470eb0a44 | e3f11ef73fe1173ad2f75e2acac92a2ff1347e6bf4c59eccbd6baf9e2ad2dbe5 | 22479 |
| etapa1_zoetis_control_maestro_csv | datos_analisis_directo/zoetis/etapa1/Zoetis_evaluada__Control_maestro.csv | e96470eb0a44 | abe7634d14078440a7d9a1315d56f657a2d5d0e42b5f1557082899d92fede723 | 51137 |
| etapa1_zoetis_guia_sws_csv | datos_analisis_directo/zoetis/etapa1/Zoetis_evaluada__Guía_Simply_Wall_St.csv | e96470eb0a44 | e3cabea03c1a776ed1203ce43f216ec3b29760e8c866e2b925b8990e31152651 | 7660 |
| etapa1_zoetis_opciones_csv | datos_analisis_directo/zoetis/etapa1/Zoetis_evaluada__Opciones.csv | e96470eb0a44 | 56246fb2e5ca7ca826b3c07c4786422bb1cf9c5a3a0d110abc53919735356a4d | 1486 |
| etapa1_zoetis_respuesta_md | datos_analisis_directo/zoetis/etapa1/Zoetis_respuesta.md | e96470eb0a44 | d5f62442438d0f130ed4a758fedebaafaef9e87a5fb021ec20e7c6219ac79a24 | 27829 |
| extracto_v63_md | datos_analisis_directo/zoetis/extracto_v63.md | e96470eb0a44 | 20b72dce714538a94d065cc86005b98d4f11d1ce7415667fcc00a24fbf4cc27d | 30378 |
| fase1_v63_json | datos_analisis_directo/zoetis/fase1_v63.json | e96470eb0a44 | 66165b379399bd10aca91259f5fddb366ab08824ffe58bf7f377ab1d7a646561 | 66738 |
| fuentes_10k_2025_seleccion | datos_analisis_directo/zoetis/fuentes/zoetis-10k-fy2025.seleccion.compacto.txt | e96470eb0a44 | 4cf5ba16a3760a8e3da48e06044d9dc4ce7a199f50f3c8c13a467152463d8704 | 331099 |
| fuentes_10q_2026_q1_seleccion | datos_analisis_directo/zoetis/fuentes/zoetis-10q-2026-q1.seleccion.compacto.txt | e96470eb0a44 | 00410a8dd64ba4c6d7dc2d17aef04bba284ec15645fa789da5063ac290c77bb2 | 88098 |
| fuentes_10q_2026_q2_seleccion | datos_analisis_directo/zoetis/fuentes/zoetis-10q-2026-q2.seleccion.compacto.txt | e96470eb0a44 | 66e17a7422b275d7316dd0bbbb70b2d7f6826f205fbbbf355a45d943e924922d | 178220 |

## Salida del modelo (datos, sin acciones ejecutables)

Estado `concluido` · cubo «Vigilar» · acción `esperar` · zona `vigilar`

| Escenario | Valor por acción | Probabilidad |
|---|---|---|
| malo | 41.56 | 0.2 |
| normal | 82.84 | 0.6 |
| bueno | 109.38 | 0.2 |

| Escalera (k = 3) | Declarado | Recalculado (Anexo C) |
|---|---|---|
| Precio actual | 73.08 | |
| Precio del escenario malo | 41.56 | 41.56 |
| P* | 68.94 | 68.94 |
| Precio de Sí = mín(P*, V_normal) | 68.94 | 68.94 |
| Ponderado | 79.89 | 79.892 |
| Crecimiento implícito al precio actual / del normal (%) | 1.1 / 4 | |

| Tasa | Precio de Sí | Ponderado | Zona |
|---|---|---|---|
| 7 % | 98.76 | 116.73 | cumple_regla_k |
| 8 % | 81.16 | 94.89 | cumple_regla_k |
| 9 % | 68.94 | 79.89 | vigilar |
| 10 % | 59.95 | 68.96 | caro |
| 11 % | 53.05 | 60.63 | caro |

### Resumen

    Zoetis es un negocio de salud animal de alta calidad. Entre 2021 y 2025 tuvo un ROIC después de impuestos de entre el 26 % y el 30 %, convirtió en caja el 106 % del beneficio y sus márgenes crecieron durante nueve años. En 2026 se deteriora: las ventas de animales de compañía en EE. UU. caen un 11 % en el semestre. La empresa lo atribuye a más competencia contra la dermatología y Simparica Trio, a sensibilidad al precio, a genéricos de Cerenia y Convenia y a menores ventas de Librela. Además, en mayo de 2026 se presentó una demanda colectiva de valores. Valoro el flujo de caja libre al accionista con una base de 1.994 mm USD (media 2023–2025, neta de la remuneración en acciones), a diez años más un valor terminal y descontado al 9 %. Con 424,9 millones de acciones salen 41,56 USD por acción en el escenario malo, 82,84 en el normal y 109,38 en el bueno. El ponderado es 79,89 USD y el precio de Sí (regla k = 3) es 68,94 USD. A 73,08 USD el precio queda en la zona de vigilar: está por debajo del ponderado pero no cumple la regla k = 3. Al 9 % el precio descuenta un crecimiento de en torno al 1,1 % anual durante cinco años, frente al 4 % del escenario normal. Conclusión: Vigilar y esperar.


### Moneda

    USD


### Justificación

    El estado es concluido. Los datos bastan para una valoración por escenarios del flujo de caja libre: es estable, positivo y está después de intereses, con la deuda en 1,9 veces el EBITDA y el covenant cumplido. La incertidumbre clave (exclusividades de Simparica Trio y Apoquel, causa de la caída de 2026) queda acotada por el escenario malo. El cubo es Vigilar y no Sí porque, a 73,08 USD, el precio supera el precio de Sí de 68,94 USD. La pérdida esperada frente al escenario malo (−43 %) no queda compensada tres veces por la ganancia esperada. El cubo tampoco es No: el precio está por debajo del ponderado de 79,89 USD y el negocio conserva calidad. La acción es esperar: un precio por debajo de unos 69 USD, o una mejora visible de las franquicias de EE. UU., cambiaría la conclusión.


### Probabilidades

    Mantengo las probabilidades de partida 0,2 / 0,6 / 0,2. La evidencia negativa de 2026 (presión competitiva en las franquicias clave, demanda colectiva) ya está incorporada al endurecer los supuestos del escenario malo (−4 % frente a −2 %), del normal (4 % frente a 5 %) y del bueno (7 % frente a 8 %). Subir además el peso del escenario malo contaría dos veces el mismo hecho.


### Fórmula aplicada

    Para P entre 41,56 y 82,84:
    G(P) = 0,6·(82,84 − P) + 0,2·(109,38 − P) = 71,58 − 0,8·P
    L(P) = 0,2·(P − 41,56) = 0,2·P − 8,312
    G = 3L → 71,58 − 0,8·P = 0,6·P − 24,936 → 1,4·P = 96,516 → P* = 68,94
    Precio de Sí = mín(68,94; 82,84) = 68,94
    Ponderado = 0,2·41,56 + 0,6·82,84 + 0,2·109,38 = 79,89
    Precio 73,08: mayor que 41,56, mayor que 68,94 y menor o igual que 79,89 → zona vigilar


### Crecimiento implícito

    Supongo márgenes constantes, de modo que el flujo de caja libre crece al ritmo de las ventas. Busco el crecimiento x de los años 1–5 que iguala el valor al precio. Mantengo el 4 % del escenario normal en los años 6–10, el 2,5 % terminal, la tasa del 9 %, la base de 1.994 mm y 424,928 millones de acciones. Objetivo: 73,08 × 424,928 = 31.054 mm, es decir, 15,574 veces la base. Con x = 1 % sale 15,49 y con x = 1,5 % sale 15,84; interpolando, x ≈ 1,1 % anual.

### Escenario malo

    Las franquicias de compañía siguen el camino de Draxxin (−66 % en EE. UU. desde 2021). La competencia que ya se ve en 2026 en dermatología y Simparica Trio no se detiene, y el canal aprieta los precios. Supuestos: el flujo de caja libre cae un 4 % anual durante diez años (queda en 1.326 mm en el año 10) y luego crece un 1 % perpetuo; tasa del 9 %. Endurezco el −2 % de la etapa 1 porque el 10-Q del segundo trimestre de 2026 ya describe presión competitiva y una caída de la dermatología del 12 % en el semestre (747 frente a 852). Cálculo: valor presente de los años 1–10 = 10.590; valor terminal = 1.325,7 × 1,01 / 0,08 = 16.737, que traído a hoy da 7.070; total 17.660 mm, entre 424,928 millones de acciones = 41,56 USD. Base de flujo de caja libre = 2.736,667 − 669,333 − 1 − 72,333 = 1.994 mm.

### Escenario normal

    Zoetis deja de batir al sector, que crece en torno al 5 % según su propia afirmación de crecer 3 puntos por encima de la media. Rebajo el crecimiento al 4 % por el bache de 2026: −1 % operativo en el semestre y −3 puntos de volumen en las franquicias clave. Supuestos: el flujo de caja libre (1.994 mm) crece un 4 % anual durante diez años (2.952 mm en el año 10), con márgenes estables, y luego un 2,5 % perpetuo; tasa del 9 %. Cálculo: valor presente de los años 1–10 = 15.542; valor terminal = 2.951,6 × 1,025 / 0,065 = 46.545, que traído a hoy da 19.661; total 35.203 mm, entre 424,928 millones de acciones = 82,84 USD. El múltiplo terminal implícito es de unas 15,8 veces el flujo de caja libre, frente a una mediana histórica de 47,1 veces.

### Escenario bueno

    La cartera de I+D (riñón, oncología, monoclonales de acción larga como Lenivia y Portela) repite lo que hicieron la dermatología (428 → 1.754 mm entre 2017 y 2025) y los parasiticidas. Supuestos: el flujo de caja libre crece un 7 % anual durante diez años (en línea con el crecimiento de ventas a 5 años del 7,2 %) y luego un 3 % perpetuo; tasa del 9 %. Cálculo: valor presente de los años 1–10 = 18.034; valor terminal = 3.922,5 × 1,03 / 0,06 = 67.336, que traído a hoy da 28.444; total 46.477 mm, entre 424,928 millones de acciones = 109,38 USD.

### Sensibilidad (comentarios)

    7 %: Escenarios: malo 53,81, normal 120,70 y bueno 167,76 USD. P* = 98,76. Solo informativo: la conclusión se toma al 9 %.
    8 %: Escenarios: malo 46,83, normal 98,31 y bueno 132,68 USD. Con un punto menos de tasa el precio ya cumple la regla k, lo que muestra lo sensible que es la conclusión a la tasa.
    9 %: Caso base, coincide con la escalera. Escenarios: malo 41,56, normal 82,84 y bueno 109,38 USD.
    10 %: Escenarios: malo 37,43, normal 71,52 y bueno 92,80 USD. El precio supera al ponderado.
    11 %: Escenarios: malo 34,10, normal 62,87 y bueno 80,42 USD.

### Qué haría falsa la conclusión

    - Que el 10-Q del tercer trimestre de 2026 muestre que la caída de animales de compañía en EE. UU. se agrava (más del −11 %) o se extiende a Internacional en dermatología y parasiticidas. Llevaría el cubo hacia No o subiría la probabilidad del escenario malo.
    - Que se publiquen fechas de pérdida de exclusividad de Simparica Trio o Apoquel anteriores a 2030 sin un sustituto claro. El escenario malo pasaría a peor que −4 % y el cubo a No o demasiado difícil.
    - Que la prueba de deterioro del fondo de comercio a 30-sep-2026 dé cargos, o que suban las provisiones y los días de inventario (el inventario creció más que las ventas).
    - Que la demanda colectiva o reguladores aporten pruebas de problemas de seguridad en Librela, Apoquel, Cytopoint o Simparica Trio que reduzcan su uso.
    - Que la dirección siga recomprando con deuda hasta acercarse a 3 veces deuda neta sobre EBITDA, o que la calificación crediticia baje. El supuesto de no restar la deuda neta (unos 18 USD por acción) dejaría de valer.
    - Hacia Sí: un precio por debajo de unos 69 USD con la tesis intacta, o una estabilización de la dermatología en EE. UU. y lanzamientos de monoclonales de acción larga con ventas crecientes que eleven el escenario normal.
    - Que el IRS gane la reclamación de unos 450 mm más intereses: restaría alrededor de 1 USD por acción. No cambia el cubo por sí sola.

### Lo que no sabe

    - Las fechas de pérdida de exclusividad de Simparica Trio, Apoquel, Cytopoint y Librela no figuran en el paquete. Es la incertidumbre principal sobre el escenario malo.
    - No tengo cifras de ventas de Librela ni de los productos individuales, ni cuotas de mercado de Zoetis y sus competidores.
    - No sé si la caída de 2026 en EE. UU. es cíclica (macroeconomía, inventario en el canal) o estructural (pérdida de cuota). El 10-Q cita ambas cosas sin cuantificarlas.
    - El resultado de la prueba de deterioro del fondo de comercio a 30-sep-2026 y el 10-Q del tercer trimestre de 2026 no están en el paquete.
    - Desconozco el fondo y la probabilidad de la demanda colectiva de valores y de las demandas derivadas presentadas en mayo y junio de 2026.
    - El precio (73,08 USD, cierre del 8-oct-2026) procede de fuentes secundarias web según el paquete. No uso el cierre del 9-oct ni nada posterior al corte.
    - Uso 424,928 millones de acciones (cierre de 2025, criterio del paquete). Con las 413,2 millones de julio de 2026 los valores suben en torno a un 2,8 % (normal unos 85,2 USD, precio de Sí unos 70,9 USD). La zona no cambia.
    - El modelo no resta la deuda neta (unos 7.575 mm, alrededor de 18 USD por acción) porque el flujo ya va después de intereses. Supone refinanciación indefinida y no captura bien la subida de deuda de 2025, financiada con el convertible para recomprar acciones.
    - Tomo el flujo de caja libre como sustituto de las ventas para el crecimiento implícito, con márgenes constantes. El paquete no permite un modelo de ventas, márgenes y reinversión completo: las palancas de la hoja figuran como INCOMPLETAS.
    - El paquete contiene notas metodológicas fechadas después del corte (decisiones del 18-oct-2026 y del 18-nov-2026). Las trato como notas de proceso, no como hechos; las cifras que uso salen de los 10-K y 10-Q anteriores al corte.
    - La tasa del 9 % es inferior a la tasa mínima del 10,8 % que calcula la hoja. Al 10 % el precio estaría en la zona cara, así que la conclusión es sensible a la tasa.
    - Hay ceros pendientes de verificación (intereses en financiación y otros) que con US GAAP considero inmateriales. Hay discrepancias menores sin resolver: los ingresos por intereses de 2023 (103 frente a 105) y la descripción de la línea de crédito en el 10-Q del primer trimestre.

### Citas

    [datos_v63_md] «C37 | Precio actual | 73.08» → Precio actual usado.
    [datos_v63_md] «fecha 2026-10-08 · moneda de cotización USD» → Fecha y moneda del precio.
    [datos_v63_md] «FCF base (C52, fórmula): 1994» → Base de flujo de caja libre = 2.736,667 − 669,333 − 1 − 72,333.
    [fuentes_10k_2025_seleccion] «Net cash provided by operating activities 2,904 2,953 2,353» → Flujo de caja operativo 2023–2025 para la media de 2.736,667.
    [fuentes_10k_2025_seleccion] «Capital expenditures (621) (655) (732)» → Inversiones de capital 2023–2025, media de 669,333.
    [fuentes_10k_2025_seleccion] «Share-based compensation expense 83 74 60» → Remuneración en acciones 2023–2025, media de 72,333, restada del flujo.
    [fuentes_10k_2025_seleccion] «Financing cash flows – finance leases 2 1 —» → Principal de arrendamientos financieros, media de 1.
    [fuentes_10k_2025_seleccion] «501,891,243 and 501,891,243 shares issued; 424,927,535» → Acciones en circulación a 31-dic-2025 usadas en el modelo.
    [fuentes_10q_2026_q2_seleccion] «501,891,243 and 501,891,243 shares issued; 414,154,046 and» → Acciones a 30-jun-2026, usadas en la sensibilidad.
    [fuentes_10q_2026_q2_seleccion] «Long-term debt, net of discount and issuance costs 9,048 9,042» → Deuda a 30-jun-2026.
    [fuentes_10q_2026_q2_seleccion] «Cash and cash equivalents(b) $ 1,476 $ 2,450» → Caja a 30-jun-2026.
    [fuentes_10q_2026_q2_seleccion] «We were in compliance with all financial covenants as of June 30, 2026 and December 31, 2025.» → Solvencia: covenant cumplido.
    [fuentes_10k_2025_seleccion] «Interest payments $ 296 $ 296 $ 273 $ 216 $ 206 $ 1,958 $ 3,245» → Intereses esperados, cercanos a la media pagada; apoyan que el flujo ya va neto de intereses.
    [fuentes_10q_2026_q2_seleccion] «Revenue $ 2,468 $ 2,474 $ 4,730 $ 4,672» → Ventas planas en 2026.
    [fuentes_10q_2026_q2_seleccion] «Companion animal $ 1,044 $ 1,176 $ 1,909 $ 2,149» → Caída del 11 % de animales de compañía en EE. UU.
    [fuentes_10q_2026_q2_seleccion] «Companion animal revenue decreased primarily due to softer end-market demand and an increasingly competitive landscape.» → Causa declarada de la caída: base del escenario malo endurecido.
    [fuentes_10q_2026_q2_seleccion] «Simparica Trio faced heightened competitive pressure and persistent macroeconomic-driven price sensitivity» → Presión competitiva y de precio sobre las franquicias clave.
    [fuentes_10q_2026_q2_seleccion] «Dermatology 398 473 747 852» → Dermatología −12 % en el semestre.
    [fuentes_10q_2026_q2_seleccion] «volume decrease from key franchises of approximately 3%» → Erosión de volumen en las franquicias clave.
    [fuentes_10k_2025_seleccion] «these five products and product lines contributed approximately 42% of our revenue» → Concentración del riesgo.
    [extracto_v63_md] «Draxxin: ventas en EE. UU. bajaron un 66% desde 2021, primer año de genérico» → Precedente del escenario malo.
    [extracto_v63_md] ««3 puntos por encima de la media de la industria»» → Sector en torno al 5 %; ancla del escenario normal.
    [datos_v63_md] «| cagr_5 | C46 | 0.0723887 |» → Crecimiento de ventas a 5 años del 7,2 %, ancla del escenario bueno.
    [fuentes_10q_2026_q2_seleccion] «a securities class action complaint was filed in federal court in New York» → Riesgo legal y reputacional nuevo en 2026.
    [fuentes_10q_2026_q2_seleccion] «is approximately $450 million, excluding interest and penalties» → Contingencia fiscal con el IRS.
    [fuentes_10q_2026_q2_seleccion] «Net cash provided by operating activities 1,056 1,120» → Flujo operativo del semestre de 2026, estable.
    [fuentes_10q_2026_q2_seleccion] «Capital expenditures (227) (324)» → Inversiones de capital del semestre de 2026, menores: el flujo de 2026 no queda por debajo de la base.
    [fuentes_10q_2026_q2_seleccion] «June 1 - June 30, 2026 2,008,999 $79.18» → Recompras recientes cerca del precio actual.
    [datos_v63_md] «C57 | Tasa sin riesgo | 0.0522» → Contexto de la tasa del 9 %, unos 3,8 puntos sobre el Treasury a 10 años.

### Comprobaciones mecánicas y normalizaciones

    {
      "comprobaciones": {
        "escalera_recalculada_anexo_c": {
          "p_estrella": 68.94,
          "precio_si": 68.94,
          "ponderado": 79.892,
          "precio_escenario_malo": 41.56
        },
        "citas_total": 29,
        "citas_literales": 29,
        "avisos": [],
        "nota": "Comprobaciones mecánicas informativas: no acreditan la calidad económica."
      },
      "normalizaciones_enum": []
    }

