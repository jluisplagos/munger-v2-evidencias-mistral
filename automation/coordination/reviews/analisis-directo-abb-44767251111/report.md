# Análisis directo · ABB, etapa 1 del universo (hoja del 2026-10-08)

Estado de la ejecución: `AUDITORIA_DOCUMENTAL_PENDIENTE_ACEPTACION`

Revisión a ciegas pendiente. No es aceptación, ni integración, ni aptitud para dinero real.

| Campo | Valor |
|---|---|
| Empresa | abb |
| Fecha de corte | 2026-10-08 |
| Tasa | 9 % |
| Tarea | analisis-directo-abb-44767251111 |
| SHA del código | fcb18bba533554c32f9756d6fb49dc0ebcc2946c |
| Huella del paquete (package_sha256) | e3f8fbb45a410a2410fcacb84448bf7aa75da4fac05f50f372471d7405b73985 |
| Huella del envío (bundle_sha256) | 4943e5f7c3da6c1e37808c18da83d285c7900352d4a42665de35c1b0e8901d4b |
| Huella del encargo | 022846e95b809a772317c2b17d6d946f3f91b9066c864911e473bb7ea15843e4 |
| Modelo pedido / devuelto | claude-opus-5-5 / claude-opus-5-5 |
| Esfuerzo | high |
| Mensajes enviados | 1 |
| Cota de entrada estimada antes de llamar | 132125 tokens |
| Reserva estimada antes de llamar | USD 1.18386 (máximo de la ejecución USD 3) |
| Reserva registrada | USD 1.18386 |
| Uso de tokens | entrada 59633, salida 15285 |
| Coste | CONOCIDO_ESTIMADO; estimado USD 0.544232; cota 0.544232 |

## Paquete de entrada

| id | ruta | commit | sha256 | bytes |
|---|---|---|---|---|
| respuesta | datos_analisis_directo/abb/etapa1/ABB_respuesta.md | fcb18bba5335 | cac35cd68a3bedd5005bb417961bc7049274e519ba86f2d690f3c522cd5dba56 | 28967 |
| hoja_analisis | datos_analisis_directo/abb/etapa1/ABB_evaluada__Análisis.csv | fcb18bba5335 | 47948fbbf06db01eb77dece4e493bfbfce94ab22fb2865f9e1ae4e6ae6c42a30 | 23133 |
| hoja_guia_simply_wall_st | datos_analisis_directo/abb/etapa1/ABB_evaluada__Guía_Simply_Wall_St.csv | fcb18bba5335 | 2791cc208d21b779b2104db9848a271eded2ae7cb4392769b743a2d95f8c3e2f | 7794 |
| hoja_opciones | datos_analisis_directo/abb/etapa1/ABB_evaluada__Opciones.csv | fcb18bba5335 | b9f97b6706b77f7a28f70140d212f0790ee7334eb22965a4f538963e777a1a73 | 1537 |
| hoja_control_maestro | datos_analisis_directo/abb/etapa1/ABB_evaluada__Control_maestro.csv | fcb18bba5335 | 216e98f49cc4a184e316ef1ef3d1da53c3dc3c28f1342693557c5a50d2d8e1be | 49409 |

## Salida del modelo (datos, sin acciones ejecutables)

Estado `concluido` · cubo «Vigilar» · acción `esperar` · zona `caro`

| Escenario | Valor por acción | Probabilidad |
|---|---|---|
| malo | 28.64 | 0.2 |
| normal | 45.18 | 0.6 |
| bueno | 69.71 | 0.2 |

| Escalera (k = 3) | Declarado | Recalculado (Anexo C) |
|---|---|---|
| Precio actual | 94.52 | |
| Precio del escenario malo | 28.64 | 28.64 |
| P* | 41.6 | 41.5957 |
| Precio de Sí = mín(P*, V_normal) | 41.6 | 41.5957 |
| Ponderado | 46.78 | 46.778 |
| Crecimiento implícito al precio actual / del normal (%) | 25.4 / 7 | |

| Tasa | Precio de Sí | Ponderado | Zona |
|---|---|---|---|
| 7 % | 61.07 | 69.83 | caro |
| 8 % | 49.55 | 56.14 | caro |
| 9 % | 41.6 | 46.78 | caro |
| 10 % | 35.77 | 39.98 | caro |
| 11 % | 31.32 | 34.83 | caro |

### Resumen

    ABB vende aparamenta, productos eléctricos, motores, variadores y automatización. Tiene deuda baja (0,32x), una caja que sigue al beneficio y un margen de Operational EBITA que ha pasado del 10,9 % en 2018 al 19,0 % en 2025. La subida es reciente y no se ha probado en una caída del ciclo. He rehecho el DCF del accionista al 9 %: FCF base de 3.709 mm USD (media 2023–25 de CFO − capex − SBC), 1.818 mm de acciones y crecimientos del 2 %, 7 % y 12 % a diez años. Salen 28,64, 45,18 y 69,71 USD por acción, con un ponderado de 46,78. Con la regla k = 3, P* = 41,60 USD y el precio de Sí es 41,60 USD (≈34,7 CHF). El precio actual, 94,52 USD (78,80 CHF convertidos), supera incluso el escenario bueno. Para justificarlo, la caja tendría que crecer ≈16,8 % anual diez años, o ≈25 % anual cinco años manteniendo después el escenario normal. Con todas las tasas del 7 al 11 % la zona es «caro». El negocio es entendible y de calidad razonable, pero el precio no deja margen: Vigilar y esperar.


### Moneda

    USD


### Justificación

    Estado concluido porque los datos materiales están (FCF, acciones, precio, deuda) y el DCF simplificado es aplicable: US GAAP, intereses dentro del CFO y deuda neta / EBITDA de 0,32x. El negocio es entendible, tiene posiciones de liderazgo, ROCE del 25 % y conversión de caja de 0,96. Pero su calidad alta es reciente (ROCE del 10–11 % en 2019–2020) y depende en parte de una ola de inversión eléctrica. A 94,52 USD el precio supera los tres escenarios y queda en zona «caro» con cualquier tasa del 7 al 11 %. El precio de Sí (41,60 USD, ≈34,7 CHF) está a menos de la mitad del precio. Por eso el cubo es Vigilar, no No: el negocio merece seguimiento si el precio se acerca al precio de Sí con el negocio intacto. Acción: esperar.


### Probabilidades

    Mantengo las de partida (0,2 / 0,6 / 0,2). Había razones para subir el malo: el margen está en el máximo de la serie y la calidad solo se ve desde 2021. No lo hago porque la base de 3.709 ya es una media de tres años por debajo de la caja LTM y el escenario malo ya recoge la vuelta del margen. Además, ninguna redistribución razonable cambia la zona, porque el precio supera incluso el escenario bueno.


### Fórmula aplicada

    V = 28,64 / 45,18 / 69,71 con p = 0,2 / 0,6 / 0,2. Entre 28,64 y 45,18: G(P) = 0,6·(45,18−P) + 0,2·(69,71−P) = 41,05 − 0,8P y L(P) = 0,2·(P − 28,64) = 0,2P − 5,73. La condición G = 3L da 41,05 − 0,8P = 0,6P − 17,18, luego P* = 58,23 / 1,4 = 41,60. Precio de Sí = mín(41,60; 45,18) = 41,60. Ponderado = 0,2·28,64 + 0,6·45,18 + 0,2·69,71 = 46,78. Precio actual 94,52 > 46,78: zona caro.


### Crecimiento implícito

    Supongo un margen de FCF constante, de modo que el FCF crece con las ventas. Busco el crecimiento x de los años 1–5 que iguala el valor al precio: 94,52 × 1.818 = 171.837 mm, es decir, 46,33 veces la base de 3.709. Mantengo el resto del escenario normal: 7 % en los años 6–10, 2,5 % perpetuo y r del 9 %. Con x = 25 % el factor da 45,58 y con x = 26 % da 47,32; interpolando, x ≈ 25,4 % anual. El escenario normal supone un 7 % anual sobre la base, equivalente a ventas ≈5 % desde la caja de hoy. Contraste: el DCF inverso a diez años de la hoja da 16,8 % anual, por encima del escenario bueno (12 %).

### Escenario malo

    El margen vuelve al 14–15 % al enfriarse la inversión eléctrica y el ciclo corto, y Rotork no rinde lo pagado. La caja crece un 2 % anual diez años desde la base de 3.709 mm (CFO 4.664 − capex 857 − SBC 98, medias 2023–25), con un 1,5 % perpetuo. El FCF del año 10 (≈4.521) no supera el FCF LTM de hoy (4.953). Al 9 % el valor total es ≈52.063 mm, entre 1.818 mm de acciones: 28,64 USD. Precedente observable: margen del 11 % y ROCE del 10–11 % en 2018–2020.

### Escenario normal

    La demanda eléctrica sigue sin acelerar. Las ventas comparables crecen ≈5 % (media 2019–2025: +1, −5, +8, +9, +11, +3, +7 %) y el margen se mantiene entre el 18 % y el 20 %. La caja crece un 7 % anual desde la base de 3.709; parte de ese 7 % solo recupera la distancia hasta el FCF LTM (≈4.850 tras SBC), así que equivale a ≈5 % desde la caja de hoy. Crecimiento perpetuo del 2,5 %, que implica vender en el año 10 a 15,8x el FCF, frente a un P/FCF histórico mediano de 29,9x. Comprobación: FCF del año 10 = 3.709 × 1,07^10 = 7.296; VA de los años 1–10 = 33.546; VA terminal = 7.296 × 1,025 / 0,065 / 1,09^10 = 48.600. Total 82.146 / 1.818 = 45,18 USD.

### Escenario bueno

    La infraestructura eléctrica y los centros de datos siguen fuertes. Las ventas crecen al 7–8 %, el margen sube hacia el 22 % (Electrification ya gana un 23,5 %) y las adquisiciones rinden por encima de lo pagado. La caja crece un 12 % anual desde 3.709 (≈10 % desde la caja de hoy), con un 3 % perpetuo, el techo de la convención. FCF del año 10 ≈11.520; valor total ≈126.728 mm / 1.818 = 69,71 USD. Aun así queda un 26 % por debajo del precio.

### Sensibilidad (comentarios)

    7 %: V = 39,16 / 66,87 / 109,40. P* = (62,00 + 23,50) / 1,4 = 61,07, por debajo del normal. Incluso al 7 % el precio (94,52) supera el ponderado.
    8 %: V = 33,09 / 54,03 / 85,52. P* = (49,52 + 19,85) / 1,4 = 49,55. El precio también supera el escenario bueno.
    9 %: Coincide con la escalera: V = 28,64 / 45,18 / 69,71; el ponderado coincide con la hoja (46,78).
    10 %: V = 25,24 / 38,72 / 58,50. P* = (34,94 + 15,14) / 1,4 = 35,77.
    11 %: V = 22,55 / 33,81 / 50,17. P* = (30,32 + 13,53) / 1,4 = 31,32. El ponderado coincide con la sensibilidad de la hoja (34,83).

### Qué haría falsa la conclusión

    - Hacia Sí: que la cotización baje al entorno de 41–42 USD (≈35 CHF al tipo de 0,83372) sin deterioro del negocio.
    - Hacia Sí: que la próxima caída de pedidos de ciclo corto deje el margen de Operational EBITA en el 17–18 % o más, lo que permitiría subir el escenario malo.
    - Hacia No: que en una caída de demanda haya guerra de precios y el margen de Electrification baje del 18 % (23,5 % en 2025), o que el margen del grupo vuelva al 14–15 %.
    - Hacia No: pedidos por debajo de los ingresos dos años seguidos sin recesión, o una conversión de caja por debajo de 0,8–0,9 si el acopio de inventario del 1S 2026 (−725) se repite.
    - Hacia No: que Rotork (~5.500 mm) se pague cara o se financie con deuda hasta superar 2x EBITDA, o un deterioro de goodwill en Machine Automation (holgura de solo el 16 %).
    - Hacia Demasiado difícil: que una serie reexpresada sin los cambios de perímetro (Robotics fuera, Rotork dentro) no permita conocer el margen de ciclo completo.

### Lo que no sabe

    - Hay contenido posterior a la fecha de corte (2026-10-08) y no lo uso como hecho. La respuesta de etapa 1 dice estar rehecha el 25-oct-2026. El Control maestro cita una «Decisión del inversor (18-oct-2026)» sobre la ventana de tres años y una «Regla del inversor (25-oct-2026)» sobre insiders. Adopto la ventana FY2023–25 como elección mía con datos anteriores al corte, no por esa decisión. Tampoco uso el veredicto de insiders que se apoya en la regla posterior.
    - Moneda: la acción cotiza en CHF en SIX y los flujos están en USD. Uso el precio convertido (78,80 CHF / 0,83372 = 94,52 USD), así que el valor y la zona dependen del tipo USD/CHF. El ADR ABBNY cotiza a 94,48 USD.
    - No conozco el precio, la financiación ni el retorno esperado de Rotork (~5.500 mm, cierre en el 1S 2027). Tampoco el destino del cobro de Robotics (~4.800 netos). No están en el modelo: el FCF base no los incluye y C76 = 0.
    - No sé qué parte de la subida del margen del 11 % al 19 % es estructural y qué parte es ola: cartera récord, inflación, centros de datos. No hay margen ni ROCE de ciclo completo antes de 2017 ni una serie reexpresada sin cambios de perímetro.
    - FY2023 incluye Robotics sin reexpresar (efecto estimado de −1/−2 %). El FCF base mezcla perímetros.
    - Varias cifras del Q2 2026 llevan una URL alojada en media.rotork.com, un dominio de un tercero (la empresa objeto de compra). No puedo verificar la procedencia y la trato como dato del paquete sin contrastar.
    - No tengo los informes de remuneración de 2022–2025, las fechas de las ventas de insiders, los importes de factoring ni el efecto precio cuantificado por año.
    - El crecimiento implícito en ventas a cinco años supone un margen de FCF constante. El modelo de la hoja proyecta FCF a diez años, no ventas, así que la cifra del 25,4 % es una aproximación mía.
    - Los escenarios y probabilidades son juicio de etapa 1 que he revisado y adopto. No son hechos verificables y el valor es muy sensible al margen terminal.

### Citas

    [hoja_control_maestro] «Cierre SIX 78,80 CHF ÷ 0,83372 CHF/USD = 94,52 USD» → Precio actual en USD y su conversión desde CHF.
    [hoja_analisis] «Precio actual,Cotización por acción.,94.52» → Precio usado en la hoja (8-oct-2026).
    [hoja_analisis] «Cash from Operations. Media de 3–5 años.,4664» → CFO medio 2023–25 del FCF base.
    [hoja_analisis] «Capital Expenditures. Escríbelo en POSITIVO.,857» → Capex medio del FCF base.
    [hoja_control_maestro] «SBC: media 3a 98 · 5a 79 · LTM ≈103 · FY2025 91» → SBC restada (98). FCF base = 4.664 − 857 − 98 = 3.709.
    [hoja_control_maestro] «CFO continuadas: 3a 4.664 · 5a 3.733 · LTM 5.986.» → Alternativas de periodo para el CFO.
    [hoja_control_maestro] «CFO continuadas LTM 5.986 − capex en caja 1.033 = 4.953.» → FCF LTM de contraste.
    [hoja_control_maestro] «1.815 en circulación (1.823 emitidas − 8 autocartera) + ≈3 de efecto dilutivo = 1.818.» → Acciones diluidas del valor por acción.
    [hoja_analisis] «Crecimiento de la caja libre · años 1–10,0.02,0.07000000000000001,0.12» → Crecimientos de FCF de los tres escenarios.
    [hoja_analisis] «Crecimiento para siempre · desde el año 11,0.015,0.025,0.03» → Crecimientos perpetuos de los tres escenarios.
    [hoja_analisis] «VALOR INTRÍNSECO POR ACCIÓN,28.6374303326534,45.184858894867,69.7071793340408» → Valores por escenario al 9 %, que coinciden con mi recálculo.
    [hoja_analisis] «46.779837270259,—,Solo calcula si los 3 escenarios tienen valor» → Ponderado al 9 %.
    [hoja_analisis] «0.167803570170427,✗ BANDERA · > BUENO» → DCF inverso a diez años: 16,8 % anual.
    [hoja_analisis] «r − 2 pts (7.0%),64.599036748186,69.8343445101864» → Ponderado al 7 % que contrasta mi sensibilidad.
    [hoja_analisis] «r + 2 pts (11.0%),33.7487560443863,34.8306198183292» → Ponderado al 11 % que contrasta mi sensibilidad.
    [respuesta] «Margen de Operational EBITA sobre ingresos del 10,9 % (2018) al 19,0 % (2025)» → Expansión del margen, eje del escenario malo.
    [hoja_control_maestro] «Histórico ROCE ABB: 11,1% (2019), 10,3% (2020), 14,9% (2021), 16,5% (2022), 21,1% (2023), 23,8% (2024 sin Robotics)» → La calidad alta es reciente.
    [respuesta] «Crecimiento comparable o en moneda local: +1 % (2019), −5 % (2020), +8 %, +9 %, +11 %, +3 % y +7 % (2025); media ≈5 %.» → Base del crecimiento de ventas del escenario normal.
    [respuesta] «Pedidos 2025 de 36.765 frente a ingresos de 33.220 y cartera de 25.282 (+27 % sobre 19.975)» → Demanda que sostiene el escenario normal a corto plazo.
    [hoja_control_maestro] «Resultado 0,32x (ABB publica 0,3x).» → Deuda neta / EBITDA baja: DCF del accionista aplicable.
    [hoja_control_maestro] «Rotork (~5.500, cierre 1S 2027) y cobro de Robotics (~4.800 netos, 2S 2026) cambiarán la estructura» → Cambios de perímetro y capital no modelados.
    [hoja_control_maestro] «Machine Automation supera su valor contable solo en un 16% en el test de 2025» → Riesgo de deterioro de goodwill.
    [hoja_control_maestro] «acopio de inventario en H1-26 (−725 en flujos frente a −52 en H1-25)» → Señal de circulante a vigilar.
    [hoja_control_maestro] «Treasury 10 años 5,28% (flujos en USD).» → Referencia sin riesgo frente al rendimiento de caja del 2,9 %.
    [respuesta] «> v2 · rehecha con el kit v1.3 el 25-oct-2026» → Fuente con fecha posterior al corte, que trato con cautela.
    [hoja_control_maestro] «Decisión del inversor (18-oct-2026): ventana 3 años (FY2023–25)» → Decisión posterior al corte; no la uso como hecho.

### Comprobaciones mecánicas y normalizaciones

    {
      "comprobaciones": {
        "escalera_recalculada_anexo_c": {
          "p_estrella": 41.59571428571428,
          "precio_si": 41.59571428571428,
          "ponderado": 46.778,
          "precio_escenario_malo": 28.64
        },
        "citas_total": 26,
        "citas_literales": 26,
        "avisos": [],
        "nota": "Comprobaciones mecánicas informativas: no acreditan la calidad económica."
      },
      "normalizaciones_enum": []
    }

