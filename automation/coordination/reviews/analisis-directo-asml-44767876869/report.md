# Análisis directo · ASML, etapa 1 del universo (hoja del 2026-10-17)

Estado de la ejecución: `AUDITORIA_DOCUMENTAL_PENDIENTE_ACEPTACION`

Revisión a ciegas pendiente. No es aceptación, ni integración, ni aptitud para dinero real.

| Campo | Valor |
|---|---|
| Empresa | asml |
| Fecha de corte | 2026-10-17 |
| Tasa | 9 % |
| Tarea | analisis-directo-asml-44767876869 |
| SHA del código | fcb18bba533554c32f9756d6fb49dc0ebcc2946c |
| Huella del paquete (package_sha256) | 46d96906e23071211fa7fdc37f9fa66c0a47cb9e673d1b8c6482687b3581a704 |
| Huella del envío (bundle_sha256) | 965629e891519351b465271af90c45b066a553bc0d9a0fd7463928e07aae198e |
| Huella del encargo | 022846e95b809a772317c2b17d6d946f3f91b9066c864911e473bb7ea15843e4 |
| Modelo pedido / devuelto | claude-opus-5-5 / claude-opus-5-5 |
| Esfuerzo | high |
| Mensajes enviados | 1 |
| Cota de entrada estimada antes de llamar | 147105 tokens |
| Reserva estimada antes de llamar | USD 1.24378 (máximo de la ejecución USD 3) |
| Reserva registrada | USD 1.24378 |
| Uso de tokens | entrada 65744, salida 19971 |
| Coste | CONOCIDO_ESTIMADO; estimado USD 0.662396; cota 0.662396 |

## Paquete de entrada

| id | ruta | commit | sha256 | bytes |
|---|---|---|---|---|
| respuesta | datos_analisis_directo/asml/etapa1/ASML_respuesta.md | fcb18bba5335 | e98ef6e025f39803072cfab53b385b9c309273b8cba608dc018bda92f0c3d64a | 33131 |
| cambios_v2 | datos_analisis_directo/asml/etapa1/ASML_cambios_v2.md | fcb18bba5335 | 793bc064b79f95c802484bd7588564f791400b86ee5d15c146cfb6148088c1ba | 3788 |
| hoja_analisis | datos_analisis_directo/asml/etapa1/ASML_evaluada__Análisis.csv | fcb18bba5335 | 55c06bad78267a0f4cf64119d7e46d002768b77553da1f3ded56902239ac9e1f | 22729 |
| hoja_guia_simply_wall_st | datos_analisis_directo/asml/etapa1/ASML_evaluada__Guía_Simply_Wall_St.csv | fcb18bba5335 | 2791cc208d21b779b2104db9848a271eded2ae7cb4392769b743a2d95f8c3e2f | 7794 |
| hoja_opciones | datos_analisis_directo/asml/etapa1/ASML_evaluada__Opciones.csv | fcb18bba5335 | b9f97b6706b77f7a28f70140d212f0790ee7334eb22965a4f538963e777a1a73 | 1537 |
| hoja_control_maestro | datos_analisis_directo/asml/etapa1/ASML_evaluada__Control_maestro.csv | fcb18bba5335 | 3f85503938788341f2e61d9ade95c2b795e4ebeefe7af0b5a29dd485f4a3c78b | 56378 |

## Salida del modelo (datos, sin acciones ejecutables)

Estado `concluido` · cubo «Vigilar» · acción `esperar` · zona `caro`

| Escenario | Valor por acción | Probabilidad |
|---|---|---|
| malo | 240.97 | 0.2 |
| normal | 565.88 | 0.6 |
| bueno | 1149.68 | 0.2 |

| Escalera (k = 3) | Declarado | Recalculado (Anexo C) |
|---|---|---|
| Precio actual | 1477.2 | |
| Precio del escenario malo | 240.97 | 240.97 |
| P* | 510.03 | 510.0329 |
| Precio de Sí = mín(P*, V_normal) | 510.03 | 510.0329 |
| Ponderado | 617.66 | 617.658 |
| Crecimiento implícito al precio actual / del normal (%) | 31.4 / 7 | |

| Tasa | Precio de Sí | Ponderado | Zona |
|---|---|---|---|
| 7 % | 756.3 | 928.5 | caro |
| 8 % | 610.18 | 743.49 | caro |
| 9 % | 510.03 | 617.66 | caro |
| 10 % | 437.17 | 526.66 | caro |
| 11 % | 381.82 | 457.88 | caro |

### Resumen

    ASML cotizaba a 1.477,20 EUR (cierre del 16-oct-2026). Es un negocio excepcional: único fabricante de EUV, ROCE antes de impuestos muy alto, caja neta de unos 10.011 mm y clientes que anticipan la caja. Aun así, el precio queda muy por encima de su valor al 9 %. Construí tres escenarios con bases de FCF distintas: media FY2023–25 en el malo, FCF 2025 antes de circulante en el normal y FCF LTM antes de circulante en el bueno, siempre neto de SBC. Los valores por acción son 241 EUR (malo), 566 EUR (normal) y 1.150 EUR (bueno). El ponderado es 618 EUR, P* es 510 EUR y el precio de Sí es 510 EUR. El precio actual supera incluso el escenario bueno al 9 %. Para justificarlo, el FCF tendría que crecer en torno al 31 % anual cinco años, o al 20 % anual diez años, frente al 7 % del escenario normal. Conclusión: Vigilar y esperar. La zona es caro con cualquier tasa entre el 7 y el 11 %.


### Moneda

    EUR


### Justificación

    El estado es concluido porque los datos permiten acotar un rango de valor. El negocio es de muy alta calidad: monopolio EUV declarado, ROCE LTM antes de impuestos del 62,8 % con la caja incluida, caja neta, anticipos de clientes y márgenes en expansión. El DCF es aplicable porque se trata de un industrial con caja propia. Sin embargo, el precio (1.477,20 EUR) casi triplica el precio de Sí (510 EUR) y supera incluso el escenario bueno al 9 %. Cubo Vigilar y acción esperar: la calidad merece seguimiento, pero el precio no deja margen. No lo pongo en No porque el negocio pasa los filtros de calidad con hechos documentados. No lo pongo en Demasiado difícil porque el monopolio es un hecho del informe, aunque su duración tecnológica y el factor geopolítico son la mayor incertidumbre.


### Probabilidades

    Mantengo 0,2 / 0,6 / 0,2. El riesgo político sobre China y la ciclicidad (unidades de litografía de 449 a 327 entre 2023 y 2025) empujan hacia el escenario malo. La cartera de pedidos y los anticipos empujan hacia el bueno. No tengo un hecho concreto anterior al corte que justifique inclinarme hacia un lado.


### Fórmula aplicada

    Valores: Vm = 240,97, Vn = 565,88, Vb = 1.149,68; probabilidades 0,2 / 0,6 / 0,2.
    Para Vm < P ≤ Vn:
    G(P) = 0,6·(565,88 − P) + 0,2·(1.149,68 − P) = 569,46 − 0,8P
    L(P) = 0,2·(P − 240,97)
    G ≥ 3L ⇒ 569,46 − 0,8P ≥ 0,6P − 144,58 ⇒ P ≤ 714,05 / 1,4 = 510,03 = P*
    Comprobación en P*: G = 161,44 y 3L = 161,44.
    Precio de Sí = mín(510,03; 565,88) = 510,03.
    Ponderado = 0,2·240,97 + 0,6·565,88 + 0,2·1.149,68 = 617,66.
    Zona: 1.477,2 > 617,66 ⇒ caro.


### Crecimiento implícito

    El modelo proyecta FCF, no ventas. Equiparo ambos suponiendo un margen de FCF constante. Mantengo las hipótesis del escenario normal: base 9.798,5, 7 % en los años 6–10, 2,5 % terminal y tasa del 9 %. Busco el crecimiento de los años 1–5 que iguala el valor a 1.477,2 EUR: con 31 % sale 56,9 de factor y con 32 % sale 59,0, frente a un objetivo de 57,82; interpolando, unos 31,4 % anuales. Si el crecimiento implícito se aplica a los diez años, con el método de la tabla de DCF inverso de la hoja reescalada a mi base, sale cerca del 19,8 %. La hoja, con su base de 7.616, da 23,2 %.

### Escenario malo

    Supuestos: controles de exportación sobre China (29,1 % de las ventas de 2025), resaca del capex de IA y concentración de clientes (dos clientes son el 38,0 %). Base de FCF: 7.615,9 mm, que es la media FY2023–25 (CFO 9.756 − capex 1.970,2 − SBC 169,9) y describe una empresa más pequeña que la actual. Crecimiento del 0 % durante diez años y del 1,5 % a perpetuidad, descontado al 9 %, entre 383,5 M de acciones diluidas. Coincide con la hoja: 240,97 EUR por acción. No se suma el exceso de caja.

### Escenario normal

    Supuestos: la litografía sigue siendo el cuello de botella y el servicio crece con la base instalada. Base de FCF: 9.798,5 mm, que es el FCF 2025 antes de circulante (10.000,8) menos la SBC de 2025 (202,3). Es un punto intermedio entre la media de tres años (7.616) y el LTM antes de circulante (13.122,5); no uso el LTM con circulante (20.999,4) porque está inflado por anticipos. Crecimiento del 7 % durante diez años y del 2,5 % terminal, al 9 %. Cálculo: factor 22,1478 × 9.798,5 / 383,5 = 565,88 EUR. Es el mismo factor de la hoja (439,83 EUR con base 7.615,9) escalado por 9.798,5 / 7.615,9.

### Escenario bueno

    Supuestos: el superciclo de capacidad de IA se sostiene, High-NA se adopta en volumen y la capacidad ampliada se vende. Base de FCF: 12.904,1 mm, que es el FCF LTM antes de circulante (13.122,5) menos la SBC LTM (218,4). Crecimiento del 12 % durante diez años y del 3 % terminal, al 9 %. Cálculo: factor 34,1676 × 12.904,1 / 383,5 = 1.149,68 EUR, equivalente a escalar el valor de la hoja (678,53 EUR) por 12.904,1 / 7.615,9.

### Sensibilidad (comentarios)

    7 %: Valores por escenario: Vm = 325,78, Vn = 837,48, Vb = 1.804,28. P* = (0,6·Vm + 0,6·Vn + 0,2·Vb) / 1,4 = 756,30. Incluso con la tasa más favorable, el precio supera al ponderado.
    8 %: Valores por escenario: Vm = 276,89, Vn = 676,71, Vb = 1.410,41. Resultado: P* = 610,18.
    9 %: Caso base; coincide con la escalera.
    10 %: Valores por escenario: Vm = 213,45, Vn = 484,98, Vb = 964,90. Resultado: P* = 437,17.
    11 %: Valores por escenario: Vm = 191,68, Vn = 423,42, Vb = 827,49. Resultado: P* = 381,82.

### Qué haría falsa la conclusión

    - Que el precio cayera hasta unos 510 EUR o menos, con el monopolio EUV, el acceso a China y la asignación de capital intactos: pasaría a Sí.
    - Una nueva restricción de exportación concreta sobre EUV o DUV hacia China, que hoy es el 29,1 % de las ventas: subiría la probabilidad del escenario malo y bajaría el precio de Sí.
    - La aparición de un competidor creíble en EUV o pruebas de que los clientes adoptan arquitecturas con menos litografía: pasaría a No o a Demasiado difícil.
    - Pedidos cayendo dos trimestres seguidos con la cartera de pedidos menguando, o un margen bruto por debajo del 50 % sin cambio de mix que lo explique.
    - Un FCF antes de circulante sostenido por encima de los 13.122,5 mm del LTM y creciendo bastante más del 12 % anual durante varios años: obligaría a revisar al alza los escenarios normal y bueno.
    - Controles de exportación que cambien cada año el mercado accesible hasta impedir estimar un rango de caja a cinco años: pasaría a Demasiado difícil.

### Lo que no sabe

    - Documentos posteriores al corte: la respuesta y el registro de cambios están fechados el 25-oct-2026, y la decisión del inversor sobre la ventana de tres años es del 18-oct-2026; las dos fechas son posteriores al corte (17-oct-2026). Uso solo los datos de hechos con fecha anterior al corte (AR2025, estados del 3T26 a 27-sep-2026, precio del 16-oct-2026). No tomo esas decisiones como autoridad y elijo mis propias bases. Los juicios de la respuesta los trato como hipótesis.
    - No consta la fecha de publicación del comunicado del 3T26 (PR-Q3-26) ni la de la guía de ventas para 2026 (44–45 mil mm). Además es una proyección del propio interesado, y solo la uso como contexto del escenario bueno.
    - No conozco la definición exacta de 'FCF antes de circulante' (qué partidas no monetarias incluye). Supongo que añade de vuelta la SBC y por eso la resto.
    - El modelo proyecta FCF a diez años, no ventas a cinco. El crecimiento implícito de ventas supone un margen de FCF constante.
    - No sé dónde clasifica la empresa los intereses cobrados, así que no sumo el exceso de caja (3.300–5.300 mm, ≈8,6–13,8 EUR por acción). Sumarlo no cambiaría la zona.
    - No tengo la cuota de mercado por producto, los precios por sistema, la identidad de los grandes clientes ni la duración tecnológica del monopolio EUV más allá de lo que dice el informe.
    - Peso del factoring (6.212,5 mm vendidos en 2025) y de los anticipos sobre el CFO: hacen poco fiable cualquier base que incluya el capital circulante.
    - No sé si las ventas de directivos (10 ventas de 5 miembros del Board) son discrecionales o están ligadas a planes de retribución.
    - El precio es del 16-oct-2026 y procede de fuentes secundarias que coinciden entre sí. No tengo cotizaciones posteriores, y tampoco las usaría.

### Citas

    [hoja_control_maestro] «Último cierre Euronext Amsterdam 1.477,20 EUR» → Precio actual.
    [hoja_control_maestro] «Cierre 16-oct-2026» → Fecha del precio.
    [hoja_analisis] «Acciones diluidas (mm),Diluted shares outstanding.,383.5» → Número de acciones usado para el valor por acción.
    [hoja_analisis] «Aproximación al flujo del accionista si la financiación es razonablemente estable.,7615.9» → Base de FCF del escenario malo (media FY2023–25).
    [hoja_analisis] «Caja de las operaciones (mm),Cash from Operations. Media de 3–5 años.,9756» → CFO medio de tres años en la base del escenario malo.
    [hoja_control_maestro] «Antes de circulante: 5.013,1 / 4.726,3 / 6.910,8 / 7.029,8 / 10.000,8; LTM 13.122,5» → Bases de FCF de los escenarios normal (FY2025: 10.000,8) y bueno (LTM: 13.122,5).
    [hoja_control_maestro] «FY21–25 117,5 / 68,9 / 134,8 / 172,6 / 202,3; media 3a 169,9; 5a 139,2; LTM 218,4» → SBC restada: 202,3 (normal) y 218,4 (bueno).
    [hoja_control_maestro] «FCF (CFO−capex) FY21–25: 9.905,5 / 7.167,5 / 3.247,2 / 9.083,1 / 11.027,3; LTM 20.999,4» → Ciclicidad del FCF y LTM inflado; por eso descarto el LTM con circulante.
    [hoja_control_maestro] «Las medias describen una empresa más pequeña (ventas 2023 27,6 mil mm vs LTM 39,5 mil mm).» → Por qué la base de tres años es conservadora y solo la uso en el escenario malo.
    [hoja_analisis] «Crecimiento de la caja libre · años 1–10,0,0.07000000000000001,0.12» → Crecimientos de los años 1–10 por escenario.
    [hoja_analisis] «Crecimiento para siempre · desde el año 11,0.015,0.025,0.03» → Crecimientos terminales por escenario.
    [hoja_analisis] «VALOR INTRÍNSECO POR ACCIÓN,240.973906568264,439.831004780848,678.532133922694» → Valor del escenario malo y valores de la hoja que escalo a mis bases (normal × 9.798,5/7.615,9; bueno × 12.904,1/7.615,9).
    [hoja_analisis] «0.195,1126.50335708295» → Tabla del DCF inverso usada para interpolar el crecimiento implícito a diez años.
    [hoja_analisis] «0.2,1169.03361370379» → Tabla del DCF inverso (límite superior de la interpolación).
    [hoja_analisis] «Crecimiento que el precio ya da por hecho,DCF inverso: crecimiento de FCF (años 1–10) que haría que el valor fuese igual al precio actual.,0.23175487641611» → Contraste: crecimiento implícito con la base de la hoja.
    [hoja_control_maestro] «− caja 8.030,9 − STI 4.704,2 = −10.010,7 (caja neta)» → Balance con caja neta.
    [hoja_control_maestro] «Caja operativa necesaria estimada 4.000–6.000 → exceso 3.300–5.300 (8,6–13,8 €/acc ≈ 0,6–0,9% del precio).» → Efecto pequeño del exceso de caja no sumado.
    [hoja_control_maestro] «Cifra principal: ROCE ANTES de impuestos = EBIT LTM 15.217,8» → Calidad del negocio (retorno sobre el capital).
    [hoja_control_maestro] «Margen bruto (métrica menos distorsionada) 45,7% (2016) → 52,8% (2025)» → Márgenes en expansión.
    [hoja_control_maestro] «LTM sin circulante 13.122,5 → 2,33% (BAJO)» → FCF yield bajo al precio actual.
    [hoja_control_maestro] «Cuentas a cobrar distorsionadas por factoring (FY25 6.212,5 vendidas)» → Calidad del CFO afectada por el factoring.
    [respuesta] «China 29,1% de ventas» → Riesgo geopolítico del escenario malo.
    [respuesta] «concentración de clientes (dos = 38,0%)» → Concentración de clientes.
    [respuesta] «las unidades de litografía ya caen (449 en 2023, 418 en 2024, 327 en 2025)» → Ciclicidad en unidades.
    [respuesta] «la empresa ya guía 2026 a 44–45 mil mm de ventas, +36% sobre 2025» → Contexto del escenario bueno (guía del interesado).
    [hoja_control_maestro] «Vendiendo: 10 ventas en mercado de 5 miembros del Board of Management» → Ventas de directivos.
    [respuesta] «v2 · corregida el 25-oct-2026» → Documento posterior al corte; se trata como hipótesis.
    [hoja_control_maestro] «Decisión del inversor (18-oct-2026)» → Decisión posterior al corte; no la uso como autoridad.

### Comprobaciones mecánicas y normalizaciones

    {
      "comprobaciones": {
        "escalera_recalculada_anexo_c": {
          "p_estrella": 510.03285714285704,
          "precio_si": 510.03285714285704,
          "ponderado": 617.658,
          "precio_escenario_malo": 240.97
        },
        "citas_total": 28,
        "citas_literales": 28,
        "avisos": [],
        "nota": "Comprobaciones mecánicas informativas: no acreditan la calidad económica."
      },
      "normalizaciones_enum": []
    }

