# Análisis directo · Zoetis, ejercicio 2025 y 2026 hasta el segundo trimestre (primer tiempo)

Estado de la ejecución: `AUDITORIA_DOCUMENTAL_PENDIENTE_ACEPTACION`

Revisión a ciegas pendiente. No es aceptación, ni integración, ni aptitud para dinero real.

| Campo | Valor |
|---|---|
| Empresa | zoetis |
| Fecha de corte | 2026-10-09 |
| Tasa | 9 % |
| Tarea | analisis-directo-zoetis-44405210664 |
| SHA del código | e96470eb0a4401b13d6a265312a2f421cea26f20 |
| Huella del paquete (package_sha256) | 962744ebf5b961d4122fd4e6098b4a931b46ea02a82440e5a66432fd5d524cf2 |
| Huella del envío (bundle_sha256) | 1090e887b554950932bd941420028888d7182a93384cdd368b7d61ed78806c58 |
| Huella del encargo | 022846e95b809a772317c2b17d6d946f3f91b9066c864911e473bb7ea15843e4 |
| Modelo pedido / devuelto | claude-opus-5-5 / claude-opus-5-5 |
| Esfuerzo | high |
| Mensajes enviados | 1 |
| Cota de entrada estimada antes de llamar | 943029 tokens |
| Reserva estimada antes de llamar | USD 4.427476 (máximo de la ejecución USD 5) |
| Reserva registrada | USD 4.427476 |
| Uso de tokens | entrada 369300, salida 19387 |
| Coste | CONOCIDO_ESTIMADO; estimado USD 1.86494; cota 1.86494 |

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
| malo | 47.83 | 0.3 |
| normal | 89.34 | 0.5 |
| bueno | 118.09 | 0.2 |

| Escalera (k = 3) | Declarado | Recalculado (Anexo C) |
|---|---|---|
| Precio actual | 73.08 | |
| Precio del escenario malo | 47.83 | 47.83 |
| P* | 69.58 | 69.5844 |
| Precio de Sí = mín(P*, V_normal) | 69.58 | 69.5844 |
| Ponderado | 82.64 | 82.637 |
| Crecimiento implícito al precio actual / del normal (%) | 2.3 / 5 | |

| Tasa | Precio de Sí | Ponderado | Zona |
|---|---|---|---|
| 7 % | 98.91 | 120.64 | cumple_regla_k |
| 8 % | 81.66 | 98.14 | cumple_regla_k |
| 9 % | 69.58 | 82.64 | vigilar |
| 10 % | 60.63 | 71.31 | caro |
| 11 % | 53.73 | 62.67 | caro |

### Resumen

    Zoetis es la mayor empresa de salud animal por ingresos. Tiene un ROIC alto, convierte bien el beneficio en caja y su balance es de grado de inversión (deuda neta/EBITDA 1,92x). En 2026 aparece un deterioro concreto: en el primer semestre, los ingresos de animal de compañía en EE. UU. caen un 11 % y las franquicias clave pierden alrededor de 3 puntos de volumen. La empresa lo atribuye a demanda más débil y a presión competitiva en dermatología y Simparica Trio. Valoro el flujo de caja al accionista con un FCF base de 1.994 mm, que es la media 2023-25 después de SBC. Uso tres escenarios de crecimiento a 10 años: −2 %, 5 % y 8 %, con crecimiento terminal de 1 %, 2,5 % y 3 %, descontados al 9 % y repartidos entre 424,928 m de acciones. Salen 47,83, 89,34 y 118,09 USD por acción. Subo la probabilidad del escenario malo a 0,3 porque la presión competitiva ya está documentada. Con eso, el ponderado es 82,64 USD y el precio de Sí con k = 3 es 69,58 USD. A 73,08 USD la acción queda en zona de vigilancia: el precio descuenta un crecimiento del FCF de ≈2,3 % anual, por debajo del 5 % del escenario normal, pero no deja margen frente al escenario malo. La acción es esperar.


### Moneda

    USD


### Justificación

    El análisis está concluido: el modelo de flujo al accionista es aplicable. Es US GAAP, los intereses ya van en el CFO, la deuda es estable salvo por el convertible y el balance es de grado de inversión. Las incógnitas, como las fechas de exclusividad, están recogidas en un escenario malo con probabilidad 0,3. El cubo es Vigilar. El negocio tiene calidad y el precio descuenta poco crecimiento (≈2,3 %), pero 73,08 USD está por encima del precio de Sí (69,58) y por debajo del ponderado (82,64). El deterioro competitivo de 2026 en las franquicias de compañía es real y todavía no tiene suelo visible. Además, el resultado depende de la tasa: al 8 % cumpliría la regla y al 10 % estaría caro. La acción es esperar: comprar solo por debajo de ≈69,6 USD, o antes si nuevos datos mejoran el escenario malo.


### Probabilidades

    Parto de 0,2/0,6/0,2 y paso a 0,3/0,5/0,2 subiendo el escenario malo. El 10-Q del 2T26 ya atribuye la caída de animal de compañía en EE. UU. (−11 % en el semestre) a un 'increasingly competitive landscape'. Señala presión competitiva en dermatología y Simparica Trio, genéricos de Cerenia y Convenia y menores ventas de Librela. Las franquicias clave restan unos 3 puntos de volumen. Es el disparador que la etapa 1 había fijado para subir el escenario malo a 0,3. Mantengo el escenario bueno en 0,2 porque Lenivia y Portela ya se lanzaron en Internacional y el historial de franquicias nuevas existe.


### Fórmula aplicada

    V = (47,83; 89,34; 118,09), p = (0,3; 0,5; 0,2). Ponderado = 0,3·47,83 + 0,5·89,34 + 0,2·118,09 = 14,35 + 44,67 + 23,62 = 82,64. Para 47,83 ≤ P ≤ 89,34: G(P) = 0,5·(89,34−P) + 0,2·(118,09−P) = 68,29 − 0,7P; L(P) = 0,3·(P−47,83). La condición G ≥ 3L da 68,29 − 0,7P ≥ 0,9P − 43,05, es decir, P ≤ 111,34/1,6 = 69,58. P* = 69,58 y precio de Sí = mín(69,58; 89,34) = 69,58. Como 69,58 < 73,08 ≤ 82,64, la zona es vigilar.


### Crecimiento implícito

    Busqué el crecimiento anual del FCF en los años 1 a 10 que iguala el valor del DCF a 73,08 USD (capitalización ≈31.054 mm), con el resto de hipótesis del escenario normal: base 1.994 mm, 2,5 % perpetuo y r = 9 %. Sale ≈2,3 %. El modelo trabaja con FCF y no con ventas: con márgenes estables, el crecimiento del FCF equivale al de las ventas, y el horizonte es de 10 años, no de 5. La tabla del DCF inverso de la etapa 1 da lo mismo (entre 2 % y 2,5 %).

### Escenario malo

    Las franquicias de compañía (Simparica Trio, dermatología, Librela) se erosionan por competencia y genéricos, como ya pasó con Draxxin (−66 % en EE. UU. desde 2021). El FCF base es 1.994 mm = CFO medio 2.736,667 − capex 669,333 − arrendamientos financieros 1 − SBC 72,333 (10-K 2025, p. 70 y p. 89). Supuestos: crecimiento del FCF −2 %/año durante 10 años y 1 % perpetuo, r = 9 %, sin restar deuda (el FCF ya va después de intereses) y sin sumar exceso de caja. Valor total ≈ 20.322 mm ÷ 424,928 m de acciones = 47,83 USD.

### Escenario normal

    Zoetis deja de batir al sector y crece con él. El sector se deriva en ≈5 % a partir de la afirmación de la empresa: 8 % desde 2013, 3 puntos por encima de la industria. Supuestos: FCF +5 %/año durante 10 años, 2,5 % perpetuo y márgenes estables. Parte de una base de 1.994 mm, que está por debajo del FCF TTM después de SBC (≈2.270 mm). Valor total ≈ 37.963 mm ÷ 424,928 = 89,34 USD. Múltiplo terminal implícito ≈15,8x FCF.

### Escenario bueno

    La cartera nueva (Lenivia/Portela, riñón, oncología) repite lo que hicieron dermatología (428 → 1.754 mm entre 2017 y 2025) y parasiticidas. Supuestos: FCF +8 %/año durante 10 años, igual que el ritmo histórico de 2017-25, y 3 % perpetuo. Valor total ≈ 50.178 mm ÷ 424,928 = 118,09 USD.

### Sensibilidad (comentarios)

    7 %: Escenarios al 7 %: 62,68 / 130,87 / 182,02. P* = (0,5·130,87 + 0,2·182,02 + 0,9·62,68)/1,6 = 98,91. Informativa.
    8 %: Escenarios al 8 %: 54,21 / 106,31 / 143,59. P* = 81,66. Informativa: con una tasa un punto más baja, el precio cumpliría la regla k.
    9 %: Coincide con la escalera: 47,83 / 89,34 / 118,09.
    10 %: Escenarios al 10 %: 42,84 / 76,93 / 99,95. P* = 60,63. El precio queda por encima del ponderado.
    11 %: Escenarios al 11 %: 38,83 / 67,47 / 86,42. P* = 53,73. Informativa: la r mínima de la hoja (10,8 %) caería en esta zona.

### Qué haría falsa la conclusión

    - Que el 10-Q del 3T26 o el 10-K de 2026 muestren otra caída de dos dígitos en animal de compañía en EE. UU. con pérdida de volumen en Simparica Trio y Apoquel/Cytopoint. Subiría el escenario malo hacia −5 % y el cubo pasaría a No o Demasiado difícil.
    - Que se publiquen fechas de pérdida de exclusividad de Simparica Trio o Apoquel anteriores a 2030.
    - Que la prueba de deterioro del fondo de comercio a 30-sep-2026 o la demanda colectiva sobre la seguridad de Librela y otros productos desemboquen en cargos o en retiradas de producto.
    - Que sigan las recompras financiadas con deuda y la deuda neta/EBITDA se acerque a 2,5–3x, lo que invalidaría no restar la deuda en el modelo.
    - En sentido favorable: que el precio baje por debajo de ≈69,6 USD sin deterioro adicional, o que el FCF de 2026 confirme ≈2.200 mm o más con el orgánico de compañía estabilizado. En cualquiera de los dos casos el cubo pasaría a Sí.

### Lo que no sabe

    - No hay en el paquete fechas de pérdida de exclusividad de Simparica Trio, Apoquel, Cytopoint ni Librela. Es la incógnita que más mueve el escenario malo.
    - No conozco las ventas de Librela en cifra ni la causa concreta de su caída. Tampoco las cuotas de mercado de los competidores ni cuál de ellos es el más peligroso.
    - No hay guía numérica de 2026 en los documentos. No tengo los resultados del 3T26 ni la prueba de deterioro del 30-sep-2026.
    - La demanda colectiva de valores (mayo de 2026) y las demandas derivadas están en fase inicial y su impacto no está cuantificado. La reclamación del IRS de ≈450 mm (sin intereses ni sanciones) está en apelación.
    - Uso 424,928 m de acciones (cierre de 2025), según el criterio fijado en el paquete. Con las 413,2 m del 31-jul-2026 los valores subirían ≈2,8 %: precio de Sí ≈71,6 y ponderado ≈85,0. La zona sigue siendo vigilar.
    - El FCF base es la media 2023-25 (1.994 mm), por debajo del TTM después de SBC (≈2.270 mm). El capex de 2026 es más bajo (227 mm en el semestre) y no sé si es estructural.
    - El modelo no resta la deuda neta (≈7.575 mm, ≈18 USD/acción): supone refinanciación indefinida. No modela el vencimiento de 2.000 mm del convertible en 2029.
    - El crecimiento implícito se mide sobre el FCF a 10 años, no sobre las ventas a 5 años. Es una aproximación con márgenes constantes.
    - El paquete contiene metadatos posteriores al corte: decisiones del orquestador fechadas el 18-oct y el 18-nov de 2026, y un cierre del 9-oct-2026 no consolidado. No los uso como hechos sobre la empresa.
    - El 10-Q del 1T26 dice que la línea de crédito vence en diciembre de 2027 y el 10-K y el 10-Q del 2T26 dicen agosto de 2030. Tomo agosto de 2030.
    - El proxy de 2026 no está disponible: no conozco incentivos ni propiedad de los directivos, y la asignación de capital es dudosa (recompras a ≈124–186 USD).

### Citas

    [datos_v63_md] «fecha 2026-10-08 · moneda de cotización USD» → Fecha y moneda del precio de 73,08 USD.
    [datos_v63_md] «FCF base (C52, fórmula): 1994» → FCF base del modelo.
    [datos_v63_md] «Acciones (C55): 424.928 con fecha 2025-12-31» → Acciones usadas para el valor por acción.
    [fuentes_10k_2025_seleccion] «Net cash provided by operating activities 2,904 2,953 2,353» → CFO 2023-25, media 2.736,667.
    [fuentes_10k_2025_seleccion] «Capital expenditures (621) (655) (732)» → Capex 2023-25, media 669,333.
    [fuentes_10k_2025_seleccion] «Share-based compensation expense 83 74 60» → SBC 2023-25, media 72,333.
    [fuentes_10k_2025_seleccion] «Financing cash flows – finance leases 2 1 —» → Principal de arrendamientos financieros, media 1.
    [etapa1_zoetis_analisis_csv] «Crecimiento de la caja libre · años 1–10,-0.02,0.05,0.08» → Crecimientos de FCF de los tres escenarios.
    [etapa1_zoetis_analisis_csv] «Crecimiento para siempre · desde el año 11,0.01,0.025,0.03» → Crecimientos terminales.
    [fuentes_10q_2026_q2_seleccion] «Companion animal revenue decreased primarily due to softer end-market demand and an increasingly competitive landscape.» → Causa declarada del deterioro de 2026; motivo para subir el escenario malo a 0,3.
    [fuentes_10q_2026_q2_seleccion] «volume decrease from key franchises of approximately 3%» → Pérdida de volumen en franquicias clave.
    [fuentes_10q_2026_q2_seleccion] «Companion animal $ 1,909 $ 2,149 (11) — (11)» → Animal de compañía en EE. UU., −11 % en el semestre.
    [fuentes_10q_2026_q2_seleccion] «Revenue $ 4,730 $ 4,672 1 2 (1)» → Ingresos del semestre: +1 % reportado, −1 % operativo.
    [fuentes_10q_2026_q2_seleccion] «Net cash provided by operating activities 1,056 1,120» → CFO del semestre de 2026.
    [fuentes_10q_2026_q2_seleccion] «Capital expenditures (227) (324)» → Capex del semestre más bajo.
    [fuentes_10q_2026_q2_seleccion] «Long-term debt, net of discount and issuance costs 9,048 9,042» → Deuda a 30-jun-2026.
    [fuentes_10q_2026_q2_seleccion] «Cash and cash equivalents(b) $ 1,476 $ 2,450» → Caja a 30-jun-2026.
    [datos_v63_md] «Deuda neta ÷ EBITDA (x) | 1.92» → Apalancamiento moderado.
    [datos_v63_md] «Tasa sin riesgo (Análisis!C57): 0.0522» → Referencia de la tasa del 9 %.
    [fuentes_10k_2025_seleccion] «these five products and product lines contributed approximately 42% of our revenue» → Concentración en cinco productos.
    [extracto_v63_md] «Draxxin: ventas en EE. UU. bajaron un 66% desde 2021, primer año de genérico» → Precedente de erosión tras perder la exclusividad.
    [extracto_v63_md] «Fechas de pérdida de exclusividad de Simparica Trio, Apoquel, Cytopoint y Librela.» → Dato ausente clave.
    [extracto_v63_md] «Acciones en circulación: 413.223.602 a 31-jul-2026» → Sensibilidad al número de acciones.
    [fuentes_10q_2026_q2_seleccion] «a securities class action complaint was filed in federal court in New York» → Riesgo legal abierto.
    [fuentes_10q_2026_q2_seleccion] «is approximately $450 million, excluding interest and penalties» → Contingencia fiscal con el IRS.
    [fuentes_10q_2026_q2_seleccion] «May 1 - May 31, 2026 3,095,163 $84.21» → Recompras recientes a precios más bajos.
    [extracto_v63_md] «Guía anual de 2026 (ventas, margen, BPA, capex): no encontrado en los documentos.» → No hay guía de 2026.

### Comprobaciones mecánicas y normalizaciones

    {
      "comprobaciones": {
        "escalera_recalculada_anexo_c": {
          "p_estrella": 69.58437500000001,
          "precio_si": 69.58437500000001,
          "ponderado": 82.637,
          "precio_escenario_malo": 47.83
        },
        "citas_total": 27,
        "citas_literales": 27,
        "avisos": [],
        "nota": "Comprobaciones mecánicas informativas: no acreditan la calidad económica."
      },
      "normalizaciones_enum": []
    }

