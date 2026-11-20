# Análisis directo · Lifco, etapa 1 del universo (hoja del 2026-11-05)

Estado de la ejecución: `AUDITORIA_DOCUMENTAL_PENDIENTE_ACEPTACION`

Revisión a ciegas pendiente. No es aceptación, ni integración, ni aptitud para dinero real.

| Campo | Valor |
|---|---|
| Empresa | lifco |
| Fecha de corte | 2026-11-05 |
| Tasa | 9 % |
| Tarea | analisis-directo-lifco-44783948606 |
| SHA del código | fcb18bba533554c32f9756d6fb49dc0ebcc2946c |
| Huella del paquete (package_sha256) | 38033e489eeaa97c842e61250bc7ae26310287c044e7185ee74872420e042dca |
| Huella del envío (bundle_sha256) | 4c7d888267fb4d4f709918051443bede4e2bfadcf9dc6c1bf1117acc3e0cf0a9 |
| Huella del encargo | 022846e95b809a772317c2b17d6d946f3f91b9066c864911e473bb7ea15843e4 |
| Modelo pedido / devuelto | claude-opus-5-5 / claude-opus-5-5 |
| Esfuerzo | high |
| Mensajes enviados | 1 |
| Cota de entrada estimada antes de llamar | 143204 tokens |
| Reserva estimada antes de llamar | USD 1.228176 (máximo de la ejecución USD 3) |
| Reserva registrada | USD 1.228176 |
| Uso de tokens | entrada 63887, salida 14162 |
| Coste | CONOCIDO_ESTIMADO; estimado USD 0.538788; cota 0.538788 |

## Paquete de entrada

| id | ruta | commit | sha256 | bytes |
|---|---|---|---|---|
| respuesta | datos_analisis_directo/lifco/etapa1/Lifco_respuesta.md | fcb18bba5335 | b9de9a1f431f9e8fba60caf3c2629e7927a901dc20d951536bda76c1cef9836f | 33187 |
| hoja_analisis | datos_analisis_directo/lifco/etapa1/Lifco_evaluada__Análisis.csv | fcb18bba5335 | f5c5ef328c92ec4ee592af5e453eb3bd7bd498464b7779cea97c90bb614fe341 | 23257 |
| hoja_guia_simply_wall_st | datos_analisis_directo/lifco/etapa1/Lifco_evaluada__Guía_Simply_Wall_St.csv | fcb18bba5335 | 2791cc208d21b779b2104db9848a271eded2ae7cb4392769b743a2d95f8c3e2f | 7794 |
| hoja_opciones | datos_analisis_directo/lifco/etapa1/Lifco_evaluada__Opciones.csv | fcb18bba5335 | b9f97b6706b77f7a28f70140d212f0790ee7334eb22965a4f538963e777a1a73 | 1537 |
| hoja_control_maestro | datos_analisis_directo/lifco/etapa1/Lifco_evaluada__Control_maestro.csv | fcb18bba5335 | b12a857067acaf3d81217c2efaa92aec15f84cc5bb0d506524c50803574cd1bd | 56056 |

## Salida del modelo (datos, sin acciones ejecutables)

Estado `concluido` · cubo «Vigilar» · acción `esperar` · zona `caro`

| Escenario | Valor por acción | Probabilidad |
|---|---|---|
| malo | 120.8 | 0.2 |
| normal | 190.6 | 0.6 |
| bueno | 294.05 | 0.2 |

| Escalera (k = 3) | Declarado | Recalculado (Anexo C) |
|---|---|---|
| Precio actual | 289.2 | |
| Precio del escenario malo | 120.8 | 120.8 |
| P* | 175.47 | 175.4643 |
| Precio de Sí = mín(P*, V_normal) | 175.47 | 175.4643 |
| Ponderado | 197.33 | 197.33 |
| Crecimiento implícito al precio actual / del normal (%) | 17.1 / 7 | |

| Tasa | Precio de Sí | Ponderado | Zona |
|---|---|---|---|
| 7 % | 257.62 | 294.59 | vigilar |
| 8 % | 209.03 | 236.82 | caro |
| 9 % | 175.47 | 197.33 | caro |
| 10 % | 150.89 | 168.66 | caro |
| 11 % | 132.13 | 146.93 | caro |

### Resumen

    Lifco es un grupo sueco que compra empresas B2B de nicho. Tiene un margen EBITA de alrededor del 22 %, un ROCE del 20,5 % y deuda moderada. Su crecimiento depende sobre todo de las compras, que paga con su propio FCF. Con el DCF de la hoja (FCF base 3.909 m SEK, 454,2163 m de acciones, r = 9 %), los valores por acción son 120,80 (malo), 190,60 (normal) y 294,05 SEK (bueno). El ponderado es 197,33 SEK. Con la regla k = 3, el precio de Sí es 175,47 SEK. A 289,2 SEK (cierre del 4-nov-2026) la acción queda en la zona 'caro'. Para justificar ese precio, el FCF tendría que crecer un 12,5 % anual durante 10 años, o unos 17 % anuales durante 5 años manteniendo el resto del normal. El negocio es de calidad y el precio no deja margen: Vigilar y esperar.


### Moneda

    SEK


### Justificación

    El estado es concluido porque los datos bastan y el DCF de FCF al accionista es aplicable: SBC nula, acciones constantes y deuda moderada. El cubo es Vigilar porque el negocio es entendible y de calidad, con ROCE del 20,5 %, margen EBITA estable en torno al 22 % y compras disciplinadas. Pero a 289,2 SEK el precio supera el ponderado (197,33) y prácticamente iguala el escenario bueno. Solo con r = 7 % se acercaría al ponderado. La acción es esperar a un precio cercano a 175 SEK o a que nuevos hechos eleven los escenarios. Los sesgos del modelo (no resta deuda neta, put/call ni la fuga a minoritarios, y el normal está por encima del contraste por componentes) empujan el valor a la baja, no al alza.


### Probabilidades

    Mantengo 0,2/0,6/0,2. El paquete no da una razón concreta para sesgarlas: los insiders compran, pero el orgánico es débil. No las ajusto a la cotización.


### Fórmula aplicada

    Para 120,80 < P < 190,60: G(P) = 0,2·(294,05 − P) + 0,6·(190,60 − P) = 173,17 − 0,8P y L(P) = 0,2·(P − 120,80) = 0,2P − 24,16. Con G = 3L: 173,17 − 0,8P = 0,6P − 72,48, de donde P* = 245,65 / 1,4 = 175,47. Precio de Sí = mín(175,47; 190,60) = 175,47. Ponderado = 0,2·120,80 + 0,6·190,60 + 0,2·294,05 = 197,33. Como 289,2 > 197,33, la zona es caro.


### Crecimiento implícito

    El paquete no trae proyección de ventas. Supongo un margen de FCF constante, de modo que el crecimiento de las ventas es igual al del FCF. Mantengo el resto del normal: 7 % en los años 6–10, terminal del 2,5 % y r = 9 %. Busco el crecimiento de los años 1–5 que iguala el valor a 289,2 SEK: con 17,0 % sale 287,8 y con 17,2 % sale 290,1. Interpolando, ≈17,1 %. Con 7 % sale 190,6, igual que el normal. El DCF inverso de la hoja (10 años a tipo único) da 12,5 %, por encima del bueno (12 %).

### Escenario malo

    El FCF crece un 2 % anual en los años 1–10 y un 1,5 % después. Las compras dejan de rendir por encima de r y el orgánico queda plano (EBITA orgánico −3,8 % en 2024 y +0,1 % en 2025). FCF base de 3.909 m (CFO 4.737 − capex 520 − principal de arrendamientos 308; media FY23–25), 454,2163 m de acciones y r = 9 %. Recalculado: coincide con la hoja (120,80). No resta la deuda neta (9.569 m) ni el put/call (2.718 m).

### Escenario normal

    El FCF crece un 7 % anual en los años 1–10 y un 2,5 % después. Lifco sigue comprando a unas 7x EBITA, con orgánico de ciclo medio y margen EBITA del 22 %. Usa la misma base (3.909 m), las mismas acciones y r = 9 %. Valor terminal: 59 % del total. Recalculado: 190,60. El contraste por componentes de la respuesta de etapa 1 da 170–177 SEK, así que este normal no es conservador.

### Escenario bueno

    El FCF crece un 12 % anual en los años 1–10 y un 3 % después. El historial 2016–2025 se repite casi entero a mayor escala, frente a un FCF por acción histórico de ≈19 % anual. Usa la misma base y r = 9 %. Recalculado: 294,05. Es casi igual al precio actual (+1,7 %).

### Sensibilidad (comentarios)

    7 %: Valores recalculados: 165,19 / 282,09 / 461,47. El ponderado coincide con la hoja (294,58). P* = 360,66 / 1,4. Incluso al 7 % el precio no cumple la regla k.
    8 %: Valores recalculados: 139,57 / 227,93 / 360,74. P* = 292,65 / 1,4.
    9 %: Caso base. Coincide con la escalera y con la hoja (197,33).
    10 %: Valores recalculados: 106,46 / 163,35 / 246,79. P* = 211,24 / 1,4.
    11 %: Valores recalculados: 95,14 / 142,62 / 211,64. El ponderado coincide con la hoja (146,93).

### Qué haría falsa la conclusión

    - Que la cotización baje hacia 175 SEK o menos con el motor intacto: compras a unas 7x EBITA, ROCE ≥ 20 % y deuda con interés por debajo de 2x EBITDA. Pasaría a Sí.
    - Que se consolide un FCF base más alto (≈4.700 m LTM o más, recurrente) junto con un orgánico ≥ 4 % durante varios años. Eso subiría los escenarios y el precio de Sí.
    - Múltiplos de compra por encima de 10x EBITA, ROCE reportado por debajo del 18 % de forma sostenida, deterioros de goodwill relevantes o emisión de acciones para comprar. Pasaría a No.
    - Deuda con interés por encima de 3x EBITDA o problemas para refinanciar la deuda a corto (la caja cubre 0,19x). Pasaría a No.
    - Un cambio del accionista de control (Carl Bennet AB) sin visibilidad sobre la disciplina de compra, o la pérdida de la serie comparable del orgánico. Pasaría a Demasiado difícil.

### Lo que no sabe

    - El Control maestro registra una 'Decisión del inversor (10-nov-2026)' sobre el periodo del FCF base, posterior a la fecha de corte. No uso esa decisión. Elijo por mi cuenta la media FY23–25 (3.909 m) con las cifras históricas del paquete, y lo señalo como límite.
    - No tengo el informe del 3T26 ni los informes anuales originales. Las cifras LTM y de balance salen de la hoja de etapa 1, que actúa como fuente secundaria.
    - El precio de 289,2 SEK sale de Google Finance, una fuente secundaria, y es el cierre del 4-nov-2026.
    - El paquete no tiene proyección de ventas. El crecimiento implícito de ventas a 5 años supone un margen de FCF constante y es una aproximación mía.
    - El DCF no resta la deuda neta (9.569 m, ≈21 SEK por acción) ni el put/call de minoritarios (2.718 m, ≈6 SEK). El FCF consolidado incluye la parte de los minoritarios. Con esos ajustes, los valores y el precio de Sí bajarían.
    - El FCF crece gracias a compras que se pagan con ese mismo FCF (el 92 % en 2021–25). Tratar el FCF entero como distribuible y a la vez hacerlo crecer al 7 % puede sobrestimar el valor. La respuesta de etapa 1 estima 170–177 SEK para el normal por componentes.
    - No conozco el precio ni el resultado de cada compra, los competidores en la compra de empresas, el orgánico por área ni la identidad del mayor cliente (≈6 %).
    - No sé qué plan de sucesión hay en el accionista de control. Carl Bennet tiene el 50,23 % del capital y el 68,93 % de los votos.
    - No sé por qué la acción cayó ≈12 % el día del 3T26.
    - No uso el valor de Simply Wall St (384,74), que es externo y anterior al 3T26. Tampoco uso ningún conocimiento propio fuera del paquete.

### Citas

    [hoja_control_maestro] «Último cierre en el mercado principal: SEK 289,20 (4-nov-2026).» → Precio actual y fecha
    [hoja_analisis] «Caja de las operaciones (mm),Cash from Operations. Media de 3–5 años.,4737» → CFO medio FY23–25
    [hoja_analisis] «Capex: inversión en activos (mm),Capital Expenditures. Escríbelo en POSITIVO.,520» → Capex medio
    [hoja_analisis] «308,ℹ se resta del FCF» → Principal de arrendamientos medio
    [hoja_analisis] «razonablemente estable.,3909» → FCF base = 4.737 − 520 − 308 = 3.909
    [hoja_analisis] «Acciones diluidas (mm),Diluted shares outstanding.,454.2163» → Número de acciones
    [hoja_analisis] «Crecimiento de la caja libre · años 1–10,0.02,0.07000000000000001,0.12» → Crecimiento de los años 1–10 por escenario
    [hoja_analisis] «Crecimiento para siempre · desde el año 11,0.015,0.025,0.03» → Crecimiento terminal por escenario
    [hoja_analisis] «Probabilidad que le das,0.2,0.6,0.2» → Probabilidades
    [hoja_analisis] «VALOR INTRÍNSECO POR ACCIÓN,120.801978271237,190.604404061448,294.047512833523» → Valores por escenario al 9 %
    [hoja_analisis] «Tu r (9.0%),188.232522484735,197.332540657821,207.977872935641» → Ponderado al 9 %
    [hoja_analisis] «r − 2 pts (7.0%),272.499709050333,294.58393683062,322.391231912841» → Contraste del ponderado al 7 %
    [hoja_analisis] «r + 2 pts (11.0%),142.363209512782,146.926862137832,152.067780810751» → Contraste del ponderado al 11 %
    [hoja_analisis] «crecimiento de FCF (años 1–10) que haría que el valor fuese igual al precio actual.,0.125100763352844» → DCF inverso a 10 años
    [hoja_control_maestro] «FCF base resultante: 3.909 (3a) / 3.338 (5a) / 4.708 (LTM).» → Sensibilidad de la base de FCF
    [hoja_control_maestro] «Decisión del inversor (10-nov-2026): FCF base con media 3 años FY2023–FY2025» → Dato posterior a la fecha de corte, no usado
    [hoja_control_maestro] «préstamos y bonos 9.328 + leases 1.624 − caja 1.383 = 9.569» → Deuda neta no restada en el DCF
    [hoja_control_maestro] «minoritarios (put/call 2.718 a valor contractual + intereses minoritarios en patrimonio 163)» → Put/call de minoritarios
    [hoja_control_maestro] «el beneficio de minoritarios con put/call (319 en FY25, ~9% del beneficio) está dentro del FCF consolidado» → Fuga a minoritarios
    [hoja_control_maestro] «adquisiciones 2021–25 = 92% del FCF» → El crecimiento depende de compras pagadas con el FCF
    [hoja_control_maestro] «EBITA antes de costes de adquisición (6.790) ÷ capital empleado medio de 4 trimestres (33.051) = 20,5%» → ROCE
    [hoja_control_maestro] «EBIT IFRS (5.597, tras amortizar intangibles de adquisición) antes de impuestos 16,9% y después de impuestos 12,8%» → Retorno después de impuestos cercano a r
    [hoja_control_maestro] «margen EBITA 15,3% (2016) → 21,2% (2021) → 23,2% (2023) → 22,6% (2024) → 22,4% (2025) → 22,8% LTM sep-26.» → Estabilidad de márgenes
    [respuesta] «EBITA orgánico −3,8% en 2024 y +0,1% en 2025» → Orgánico débil (escenario malo)
    [hoja_control_maestro] «caja 1.383 ÷ deuda financiera a corto 7.226 (sin leases) = 0,19x» → Dependencia de la refinanciación
    [hoja_control_maestro] «Carl Bennet AB 50,23% del capital y 68,93% de los votos» → Concentración del control
    [hoja_control_maestro] «El CEO Per Waldemarson compró 120.000 acciones en 5 operaciones» → Compras de insiders
    [respuesta] «Mi contraste da ≈170–177 SEK, equivalente a 0,06» → El normal de la hoja puede estar algo alto

### Comprobaciones mecánicas y normalizaciones

    {
      "comprobaciones": {
        "escalera_recalculada_anexo_c": {
          "p_estrella": 175.46428571428572,
          "precio_si": 175.46428571428572,
          "ponderado": 197.33,
          "precio_escenario_malo": 120.8
        },
        "citas_total": 28,
        "citas_literales": 28,
        "avisos": [],
        "nota": "Comprobaciones mecánicas informativas: no acreditan la calidad económica."
      },
      "normalizaciones_enum": []
    }

