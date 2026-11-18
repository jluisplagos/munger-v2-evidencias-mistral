# Análisis directo · Zoetis, ejercicio 2025 y 2026 hasta el segundo trimestre (primer tiempo)

Estado de la ejecución: `AUDITORIA_DOCUMENTAL_PENDIENTE_ACEPTACION`

Revisión a ciegas pendiente. No es aceptación, ni integración, ni aptitud para dinero real.

| Campo | Valor |
|---|---|
| Empresa | zoetis |
| Fecha de corte | 2026-10-09 |
| Tasa | 9 % |
| Tarea | analisis-directo-zoetis-44399614319 |
| SHA del código | e96470eb0a4401b13d6a265312a2f421cea26f20 |
| Huella del paquete (package_sha256) | 962744ebf5b961d4122fd4e6098b4a931b46ea02a82440e5a66432fd5d524cf2 |
| Huella del envío (bundle_sha256) | df30e914c7c6c8bf07148585286b430e3f0e5f405114f30ab1eee55b9e34b80a |
| Huella del encargo | 022846e95b809a772317c2b17d6d946f3f91b9066c864911e473bb7ea15843e4 |
| Modelo pedido / devuelto | claude-opus-5-5 / claude-opus-5-5 |
| Esfuerzo | high |
| Mensajes enviados | 1 |
| Cota de entrada estimada antes de llamar | 943029 tokens |
| Reserva estimada antes de llamar | USD 4.427476 (máximo de la ejecución USD 5) |
| Reserva registrada | USD 4.427476 |
| Uso de tokens | entrada 369300, salida 24400 |
| Coste | CONOCIDO_ESTIMADO; estimado USD 1.9652; cota 1.9652 |

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
| malo | 46.37 | 0.2 |
| normal | 79.34 | 0.6 |
| bueno | 105.76 | 0.2 |

| Escalera (k = 3) | Declarado | Recalculado (Anexo C) |
|---|---|---|
| Precio actual | 73.08 | |
| Precio del escenario malo | 46.37 | 46.37 |
| P* | 68.98 | 68.9843 |
| Precio de Sí = mín(P*, V_normal) | 68.98 | 68.9843 |
| Ponderado | 78.03 | 78.03 |
| Crecimiento implícito al precio actual / del normal (%) | 1.1 / 3 | |

| Tasa | Precio de Sí | Ponderado | Zona |
|---|---|---|---|
| 7 % | 98.72 | 113.78 | cumple_regla_k |
| 8 % | 81.19 | 92.6 | cumple_regla_k |
| 9 % | 68.98 | 78.03 | vigilar |
| 10 % | 59.98 | 67.39 | caro |
| 11 % | 53.06 | 59.28 | caro |

### Resumen

    Zoetis es un negocio de salud animal de alta calidad. Tiene un ROIC del 24 al 29 % y una conversión de beneficio en caja de 1,06. En 2026 tiene un problema real: las ventas de animal de compañía en EE. UU. caen un 11 % en el primer semestre por competencia en dermatología y en Simparica Trio, sensibilidad al precio, genéricos de Cerenia y Convenia y menores ventas de Librela. El crecimiento operativo total del semestre es del −1 %. Valoro el flujo de caja libre al accionista: base de 1.994 mm, media 2023–2025 después de la compensación en acciones (SBC). Uso dos tramos de crecimiento y un valor terminal, descuento al 9 % y 424,93 m de acciones al cierre de 2025. Los valores por acción son 46,37 USD (malo), 79,34 (normal) y 105,76 (bueno); el ponderado es 78,03. Con la regla k = 3, el precio de Sí es 68,98 USD. El precio de 73,08 USD queda en la zona vigilar, a un 6 % por debajo del ponderado. El mercado descuenta un crecimiento de ventas de ≈1,1 % anual a cinco años, frente al 3 % de mi escenario normal. Cubo: Vigilar. Acción: esperar.


### Moneda

    USD


### Justificación

    El estado es concluido. Los datos materiales (FCF, deuda, acciones, precio, evolución de 2026) están en el paquete con fuente primaria. La incertidumbre principal, la erosión de franquicias, la recoge el escenario malo con cinco años de caída. El cubo es Vigilar y no Sí: a 73,08 USD el precio está por encima del precio de Sí (68,98) aunque por debajo del ponderado (78,03), así que no cumple la regla k = 3 al 9 %. Tampoco es No: el negocio conserva ROIC alto, balance cómodo (deuda neta / EBITDA ≈1,9x, A3/BBB+, sin vencimientos hasta septiembre de 2027) y el mercado solo descuenta ≈1 % de crecimiento. Acción: esperar a un precio igual o inferior a ≈69 USD, o a que el 10-Q del tercer trimestre aclare si la caída de EE. UU. es estructural.


### Probabilidades

    Mantengo 0,2 / 0,6 / 0,2. El deterioro observado en 2026 (competencia y sensibilidad al precio en EE. UU.) lo he metido en las hipótesis de crecimiento y no en las probabilidades: el escenario normal ya baja al 3 % a cinco años, desde el 5 % a diez años de la etapa 1. El malo supone cinco años de caída. Subiría el malo a 0,3 si el 10-Q del tercer trimestre confirma pérdida de cuota estructural en dermatología o en Simparica Trio.


### Fórmula aplicada

    Datos: V = (46,37; 79,34; 105,76) y p = (0,2; 0,6; 0,2).
    Para P entre 46,37 y 79,34:
    - G(P) = 0,6·(79,34 − P) + 0,2·(105,76 − P) = 68,756 − 0,8·P
    - L(P) = 0,2·(P − 46,37) = 0,2·P − 9,274
    Condición G ≥ 3·L: 68,756 − 0,8·P ≥ 0,6·P − 27,822, de donde P ≤ 96,578 / 1,4 = 68,98. Por tanto P* = 68,98.
    Precio de Sí = mín(68,98; 79,34) = 68,98.
    Ponderado = 0,2·46,37 + 0,6·79,34 + 0,2·105,76 = 78,03.
    Zona: 73,08 > 68,98 y 73,08 ≤ 78,03, luego vigilar.


### Crecimiento implícito

    Supongo un margen de FCF sobre ventas constante, de modo que el crecimiento del FCF en los años 1–5 es igual al de las ventas. Mantengo el resto del escenario normal: 4 % en los años 6–10, 2,5 % perpetuo, descuento al 9 %, base de 1.994 mm y 424,928 m de acciones. Con un 1 % en los años 1–5 el valor es 72,70 USD; con un 3 %, 79,34. Interpolando hasta 73,08 USD sale ≈1,1 % anual.

### Escenario malo

    Supuestos:
    - Flujo de caja libre (FCF) base de 1.994 mm: CFO medio 2.736,67 − capex medio 669,33 − arrendamientos financieros 1 − SBC 72,33 (2023–2025). Equivale a 4,6926 USD por acción con 424,928 m de acciones.
    - Años 1–5: −4 % anual. Prolonga la caída actual de animal de compañía en EE. UU. (−11 % en 6M26) y la pérdida de volumen de las franquicias clave (−3 puntos) sin reemplazo. Precedente: Draxxin perdió un 66 % en EE. UU. tras los genéricos.
    - Años 6–10: 0 %.
    - Crecimiento perpetuo del 1 %. Descuento al 9 %.
    Resultado: FCF del año 5 ≈ 1.626 mm; valor por acción 4,6926 × 9,8809 = 46,37 USD.

### Escenario normal

    Supuestos:
    - La misma base de 1.994 mm, que ya está un 12 % por debajo del FCF de los últimos doce meses después de SBC (≈2.270 = CFO 2.887 − capex 521 − SBC 95).
    - Años 1–5: +3 %. EE. UU. compañía se estabiliza tras el bache de 2026; Internacional sigue creciendo (+7 % operativo en 6M26) con precio de 1–4 puntos.
    - Años 6–10: +4 %, por debajo del ≈5 % de crecimiento del sector que se deduce del 8 % de Zoetis «3 puntos por encima» de la industria.
    - Crecimiento perpetuo del 2,5 %, por debajo de la tasa sin riesgo del 5,22 %.
    - Margen de FCF sobre ventas constante.
    Resultado: 4,6926 × 16,9069 = 79,34 USD.

### Escenario bueno

    Supuestos:
    - Años 1–5: +7 %; años 6–10: +6 %; crecimiento perpetuo del 3 %.
    - Requiere que las franquicias nuevas repitan lo hecho por dermatología y parasiticidas: monoclonales de dolor de acción trimestral (Lenivia y Portela, lanzados en Internacional en 2026), enfermedad renal crónica (primera aprobación esperada en 2027) y oncología (2028–2029, guía de la empresa).
    - Requiere también que EE. UU. vuelva a crecer.
    Está por debajo del ≈9 % anual de FCF de 2017–2025.
    Resultado: 4,6926 × 22,5367 = 105,76 USD.

### Sensibilidad (comentarios)

    7 %: Escenarios: malo 61,07, normal 115,42, bueno 161,57. P* = 138,208 / 1,4 = 98,72. Al 7 % el valor depende mucho del terminal (múltiplo de 22,8x en el normal).
    8 %: Escenarios: malo 52,68, normal 94,09, bueno 128,04. P* = 113,67 / 1,4 = 81,19. El precio actual cumpliría la regla k con solo 1 punto menos de tasa: la conclusión es sensible a la tasa.
    9 %: Coincide con la escalera: malo 46,37, normal 79,34, bueno 105,76.
    10 %: Escenarios: malo 41,45, normal 68,54, bueno 89,89. P* = 83,972 / 1,4 = 59,98.
    11 %: Escenarios: malo 37,50, normal 60,29, bueno 78,03. P* = 74,28 / 1,4 = 53,06.

### Qué haría falsa la conclusión

    - Que el 10-Q del tercer trimestre de 2026 muestre que animal de compañía en EE. UU. sigue cayendo a doble dígito y que la empresa lo atribuya a pérdida de cuota en Apoquel, Cytopoint o Simparica Trio frente a competidores. Haría más probable el malo y llevaría el cubo a No a este precio.
    - Que se publiquen fechas de pérdida de exclusividad de Simparica Trio o Apoquel anteriores a 2030. Bajaría el malo hacia −5 % o −8 % anual; el cubo pasaría a No o a Demasiado difícil si no se puede acotar.
    - Que la demanda colectiva de valores (presentada el 27-may-2026) o algún regulador establezcan problemas de seguridad en Librela u otros productos de compañía con retiradas o cambios de etiqueta.
    - Que la prueba de deterioro del fondo de comercio a 30-sep-2026 dé un cargo, o que suban las provisiones de inventario. Señal de que el inventario (≈340 días) se acumuló por encima de la demanda.
    - Que la dirección siga recomprando con deuda hasta acercar la deuda neta / EBITDA a 3x, o que el IRS gane la reclamación de ≈450 mm más intereses.
    - En sentido favorable: que el precio baje a 69 USD o menos sin deterioro adicional, o que EE. UU. vuelva a crecer y los monoclonales trimestrales despeguen. El cubo pasaría a Sí.

### Lo que no sabe

    - Fechas de pérdida de exclusividad de Simparica Trio, Apoquel, Cytopoint y Librela: el extracto dice que no las encontró. Es el mayor límite del análisis.
    - Ventas en dólares de Librela y causa concreta de su caída. La demanda colectiva alude a la seguridad de esos productos, pero el paquete no contiene más que la denuncia y no permite juzgar el fondo.
    - Resultados del tercer trimestre de 2026 y prueba de deterioro a 30-sep-2026: no publicados antes del corte.
    - El FCF base usa la media 2023–2025 y no el TTM (≈2.270 después de SBC). Tampoco ajusta el menor ingreso por intereses ni el mayor gasto financiero de 2026 (estimo un efecto de ≈−40 mm después de impuestos). Lo compensa en parte usar 424,9 m de acciones de diciembre de 2025 en lugar de las 414,2 m de junio de 2026, según el criterio P-O2. Con 414,2 m los valores subirían ≈2,6 %.
    - No resto la deuda neta (≈7.375 mm a junio de 2026, contando las inversiones a corto plazo). El FCF va después de intereses, y supongo que la deuda se refinancia; esto deja de valer si el apalancamiento sube mucho.
    - El paquete contiene anotaciones metodológicas fechadas después del corte (decisión del inversor del 18-oct-2026 y notas del orquestador del 18-nov-2026), además del cierre no consolidado del 9-oct-2026 (74,77–74,81). No las uso como información de mercado; solo uso las cifras de los 10-K y 10-Q que citan.
    - Discrepancia en el 10-Q del primer trimestre de 2026: describe la línea de crédito como de 1.300 mm con vencimiento en diciembre de 2027. El 10-K 2025 y el 10-Q del segundo trimestre dicen 1.250 mm con vencimiento en agosto de 2030. Uso estos últimos.
    - Tamaño del mercado, cuotas de los competidores y propiedad de directivos (proxy): no disponibles.
    - El crecimiento del sector (≈5 %) es una derivación de una afirmación de la propia empresa, sin fuente externa.

### Citas

    [datos_v63_md] «| C37 | Precio actual | 73.08 | Rellenado y verificado |» → Precio actual de 73,08 USD.
    [datos_v63_md] «fecha 2026-10-08 · moneda de cotización USD» → Fecha y moneda del precio.
    [datos_v63_md] «424.927.535 en circulación al 31-dic-2025» → Acciones usadas en la valoración.
    [fase1_v63_json] «el criterio de la persona responsable (P-O2) fija las acciones al cierre de las cuentas» → Criterio para usar las acciones al cierre de 2025.
    [datos_v63_md] «FCF base (C52, fórmula): 1994» → FCF base de 1.994 mm.
    [fuentes_10k_2025_seleccion] «Net cash provided by operating activities 2,904 2,953 2,353» → CFO 2023–2025 de la media del FCF base.
    [fuentes_10k_2025_seleccion] «Capital expenditures (621) (655) (732)» → Capex 2023–2025.
    [fuentes_10k_2025_seleccion] «Share-based compensation expense 83 74 60» → SBC restada del FCF.
    [fuentes_10k_2025_seleccion] «Financing cash flows – finance leases 2 1 —» → Principal de arrendamientos financieros (media de 1).
    [etapa1_zoetis_control_maestro_csv] «2.365 = CFO TTM 2.887 − capex 521» → FCF TTM: la base de 1.994 es conservadora.
    [fuentes_10q_2026_q2_seleccion] «Revenue $ 4,730 $ 4,672 1 2 (1)» → Ingresos de 6M26: +1 % reportado, −1 % operativo.
    [fuentes_10q_2026_q2_seleccion] «Companion animal $ 1,909 $ 2,149 (11) — (11)» → Caída del 11 % de animal de compañía en EE. UU. en 6M26.
    [fuentes_10q_2026_q2_seleccion] «Companion animal revenue decreased primarily due to softer end-market demand and an increasingly competitive landscape.» → Causa declarada de la caída en EE. UU.
    [fuentes_10q_2026_q2_seleccion] «faced heightened competitive pressure and persistent macroeconomic-driven price sensitivity» → Presión competitiva y de precio en las franquicias clave.
    [fuentes_10q_2026_q2_seleccion] «volume decrease from key franchises of approximately 3%» → Pérdida de volumen de las franquicias clave (supuesto del malo).
    [fuentes_10q_2026_q2_seleccion] «International segment revenue increased by $252 million, or 12%, in the six months ended June 30, 2026» → Crecimiento de Internacional (soporte del normal).
    [fuentes_10q_2026_q2_seleccion] «Net cash provided by operating activities was $1,056 million for the six months ended June 30, 2026» → CFO de 6M26.
    [fuentes_10q_2026_q2_seleccion] «Capital expenditures (227) (324)» → Capex de 6M26.
    [fuentes_10k_2025_seleccion] «these five products and product lines contributed approximately 42% of our revenue» → Concentración en cinco productos.
    [fuentes_10k_2025_seleccion] «Draxxin declined by 66% in the U.S., its largest market.» → Precedente de erosión tras genéricos (escenario malo).
    [extracto_v63_md] «crecimiento operativo medio anual de ingresos del 8% desde la salida a bolsa en 2013» → Base para derivar un sector de ≈5 % (años 6–10 del normal).
    [extracto_v63_md] «oncología, aprobaciones iniciales proyectadas para 2028–2029» → Calendario del pipeline del escenario bueno (guía, no hecho).
    [datos_v63_md] «Tasa sin riesgo (Análisis!C57): 0.0522» → Crecimiento perpetuo por debajo de la tasa sin riesgo.
    [fuentes_10q_2026_q2_seleccion] «Long-term debt, net of discount and issuance costs $ 9,048 $ 9,042» → Deuda a 30-jun-2026.
    [fuentes_10q_2026_q2_seleccion] «Cash and cash equivalents(b) $ 1,476 $ 2,450» → Caja a 30-jun-2026.
    [fuentes_10k_2025_seleccion] «Interest payments $ 296 $ 296 $ 273 $ 216 $ 206 $ 1,958 $ 3,245» → Intereses esperados: aumento moderado del coste financiero.
    [fuentes_10q_2026_q2_seleccion] «a securities class action complaint was filed in federal court in New York against the company» → Riesgo legal y reputacional abierto.
    [fuentes_10q_2026_q2_seleccion] «approximately $450 million, excluding interest and penalties» → Reclamación del IRS.
    [fuentes_10q_2026_q2_seleccion] «May 1 - May 31, 2026 3,095,163 $84.21» → Recompras recientes a precios cercanos al actual.
    [extracto_v63_md] «Fechas de pérdida de exclusividad de Simparica Trio, Apoquel, Cytopoint y Librela.» → Dato ausente clave.

### Comprobaciones mecánicas y normalizaciones

    {
      "comprobaciones": {
        "escalera_recalculada_anexo_c": {
          "p_estrella": 68.9842857142857,
          "precio_si": 68.9842857142857,
          "ponderado": 78.03,
          "precio_escenario_malo": 46.37
        },
        "citas_total": 30,
        "citas_literales": 30,
        "avisos": [],
        "nota": "Comprobaciones mecánicas informativas: no acreditan la calidad económica."
      },
      "normalizaciones_enum": []
    }

