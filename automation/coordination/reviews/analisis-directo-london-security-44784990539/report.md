# Análisis directo · London_Security, etapa 1 del universo (hoja del 2026-10-31)

Estado de la ejecución: `AUDITORIA_DOCUMENTAL_PENDIENTE_ACEPTACION`

Revisión a ciegas pendiente. No es aceptación, ni integración, ni aptitud para dinero real.

| Campo | Valor |
|---|---|
| Empresa | london-security |
| Fecha de corte | 2026-10-31 |
| Tasa | 9 % |
| Tarea | analisis-directo-london-security-44784990539 |
| SHA del código | fcb18bba533554c32f9756d6fb49dc0ebcc2946c |
| Huella del paquete (package_sha256) | 4f807bacec7fefe05fbdea1a3938547d13f25536c89cbcd5cee74a4310de92e0 |
| Huella del envío (bundle_sha256) | 69c38f7614f5d6cce2d75b3e248ad4458a201378ebc224641295349bae91c8a2 |
| Huella del encargo | 022846e95b809a772317c2b17d6d946f3f91b9066c864911e473bb7ea15843e4 |
| Modelo pedido / devuelto | claude-opus-5-5 / claude-opus-5-5 |
| Esfuerzo | high |
| Mensajes enviados | 1 |
| Cota de entrada estimada antes de llamar | 140102 tokens |
| Reserva estimada antes de llamar | USD 1.215768 (máximo de la ejecución USD 3) |
| Reserva registrada | USD 1.215768 |
| Uso de tokens | entrada 62563, salida 13388 |
| Coste | CONOCIDO_ESTIMADO; estimado USD 0.518012; cota 0.518012 |

## Paquete de entrada

| id | ruta | commit | sha256 | bytes |
|---|---|---|---|---|
| respuesta | datos_analisis_directo/london-security/etapa1/London_Security_respuesta.md | fcb18bba5335 | 819e4dfc65ea8983f63914ec08c4d486ce9d974fd0ddc0561ab77a82f97b9bb6 | 31867 |
| hoja_analisis | datos_analisis_directo/london-security/etapa1/London_Security_evaluada__Análisis.csv | fcb18bba5335 | 1a3b603aca9014b3684c8f509f665e87dcf59cd11c01239c627a3ae6c257f891 | 23596 |
| hoja_guia_simply_wall_st | datos_analisis_directo/london-security/etapa1/London_Security_evaluada__Guía_Simply_Wall_St.csv | fcb18bba5335 | 2791cc208d21b779b2104db9848a271eded2ae7cb4392769b743a2d95f8c3e2f | 7794 |
| hoja_opciones | datos_analisis_directo/london-security/etapa1/London_Security_evaluada__Opciones.csv | fcb18bba5335 | b9f97b6706b77f7a28f70140d212f0790ee7334eb22965a4f538963e777a1a73 | 1537 |
| hoja_control_maestro | datos_analisis_directo/london-security/etapa1/London_Security_evaluada__Control_maestro.csv | fcb18bba5335 | c30c2537f73b749cfc7aae368a675cac4f1dd128e3b30242b3ef45c95609722d | 53667 |

## Salida del modelo (datos, sin acciones ejecutables)

Estado `concluido` · cubo «Vigilar» · acción `esperar` · zona `caro`

| Escenario | Valor por acción | Probabilidad |
|---|---|---|
| malo | 19.54 | 0.2 |
| normal | 27.22 | 0.6 |
| bueno | 37.62 | 0.2 |

| Escalera (k = 3) | Declarado | Recalculado (Anexo C) |
|---|---|---|
| Precio actual | 36.5 | |
| Precio del escenario malo | 19.54 | 19.54 |
| P* | 25.42 | 25.4143 |
| Precio de Sí = mín(P*, V_normal) | 25.42 | 25.4143 |
| Ponderado | 27.77 | 27.764 |
| Crecimiento implícito al precio actual / del normal (%) | 11.5 / 4 | |

| Tasa | Precio de Sí | Ponderado | Zona |
|---|---|---|---|
| 7 % | 34.82 | 38.65 | vigilar |
| 8 % | 29.34 | 32.28 | caro |
| 9 % | 25.42 | 27.77 | caro |
| 10 % | 22.47 | 24.4 | caro |
| 11 % | 20.17 | 21.79 | caro |

### Resumen

    London Security es un negocio de protección contra incendios: vende, instala y revisa equipos mediante visitas de ingenieros. Es sencillo y rentable, con ROCE antes de impuestos de alrededor del 18 %, caja neta y sin dilución. Sus puntos débiles son el margen operativo, que baja del 18,2 % al 13,4 %, un mercado que la propia empresa describe como maduro y con barreras mínimas para competidores baratos, un control del 98,85 % por dos sociedades y un free float de alrededor del 1,15 %. Parto de un FCF base de 18,26 mm £ y de 25 mm £ de exceso de caja. Al 9 % los escenarios valen 19,54 £, 27,22 £ y 37,62 £ por acción, y el ponderado es 27,77 £. La regla k = 3 da un precio de Sí de 25,42 £. El precio de 36,50 £ es un medio sin operaciones y queda en zona cara con cualquier tasa del 8 al 11 %; al 7 % pasa a la zona de vigilar, pero sigue por encima del precio de Sí. Para justificar el precio, la caja libre tendría que crecer alrededor del 11,5 % anual durante cinco años, frente al 4 % del escenario normal. Cubo Vigilar, acción esperar.


### Moneda

    GBP


### Justificación

    Concluido. El negocio es comprensible, tiene caja neta y no requiere capital, así que el DCF simplificado es aplicable. Cubo Vigilar y no Sí: a 36,50 £ el precio está un 31 % por encima del ponderado (27,77 £) y un 44 % por encima del precio de Sí (25,42 £). Solo el escenario bueno iguala el precio, y el precio exige alrededor del 11,5 % anual de crecimiento a cinco años. No elijo No porque la calidad (ROCE de alrededor del 18 %, sin dilución, demanda de cumplimiento) justifica seguirla. La acción es esperar a un precio ejecutable de 25,42 £ o menos, que el rango de 52 semanas (21-39 £) muestra posible. Antes de actuar habría que confirmar con una cotización en firme que se puede comprar, dado el free float de alrededor del 1,15 %.


### Probabilidades

    Mantengo 0,2/0,6/0,2. El riesgo de que el margen siga cayendo ya está en el escenario malo (crecimiento 0 % y g de 1 %), y subirle también la probabilidad lo castigaría dos veces. La mejora del primer semestre de 2026 es un solo semestre y no basta para dar más peso al bueno.


### Fórmula aplicada

    Con P entre V_malo y V_normal:
    G(P) = 0,6·(27,22−P) + 0,2·(37,62−P) = 23,857 − 0,8P
    L(P) = 0,2·(P − 19,54) = 0,2P − 3,908
    G = 3L ⇒ 23,857 − 0,8P = 0,6P − 11,725 ⇒ P* = 35,582 / 1,4 = 25,42
    Precio de Sí = mín(25,42; 27,22) = 25,42
    Ponderado = 0,2·19,54 + 0,6·27,22 + 0,2·37,62 = 27,77
    Precio 36,50 > 27,77 ⇒ zona caro


### Crecimiento implícito

    El modelo es de caja libre, no de ventas. Uso el crecimiento del FCF como aproximación al de las ventas, porque el escenario normal supone margen estable. El precio de 36,50 £ equivale a 447,45 mm £; restando los 25 mm £ de exceso de caja quedan 422,45 mm £ para la caja libre. Resuelvo el crecimiento de los años 1-5 que iguala ese valor manteniendo el resto del escenario normal: 4 % en los años 6-10, g de 2 %, r de 9 % y FCF base de 18,26. Sale alrededor del 11,5 % anual, frente al 4 % del normal. Su narrativa habla de ventas al 5-6 %, con una caja libre al 4 %. Como contraste, la hoja calcula que con crecimiento constante durante diez años el precio exige un 8,19 % anual.

### Escenario malo

    El margen sigue comprimiéndose hacia el 10-11 % y la caja libre se queda plana diez años: FCF de 18,26 mm £ con crecimiento del 0 % en los años 1-10 y del 1 % a perpetuidad. Se suman 25 mm £ de exceso de caja (cierre 2025 de 45,9 mm £ menos unos 20 mm £ operativos) y se divide entre 12,258977 mm de acciones. El valor presente de los años 1-10 es 117,19, el terminal 97,38 y el total 239,57 mm £, que dan 19,54 £ por acción. Recalculado con la fórmula de la plantilla; coincide con la hoja.

### Escenario normal

    El margen se mantiene en torno al 13,4 % de 2024-25. Las ventas crecen un 5-6 % con traslado de inflación y compras pequeñas de carteras (incluidas en el capex). La caja libre crece un 4 % anual en los años 1-10, en línea con su historial del 3,3 % anual 2016-18 a 2023-25, y un 2 % a perpetuidad. El valor presente de los años 1-10 es 142,33, el terminal 166,37 y el exceso de caja 25, lo que suma 333,69 mm £ y da 27,22 £ por acción. El múltiplo terminal implícito es de unas 14,6 veces el FCF.

### Escenario bueno

    El margen vuelve al 15-16 % de 2019-2021 y la caja acumulada se invierte en compras con buen retorno. La caja libre crece un 8 % anual en los años 1-10, por encima del 5,9 % anual del resultado operativo entre 2015 y 2025, y un 2,5 % a perpetuidad. El valor presente de los años 1-10 es 173,64, el terminal 262,59 y el exceso de caja 25, lo que suma 461,23 mm £ y da 37,62 £ por acción. Aun así, apenas supera el precio actual.

### Sensibilidad (comentarios)

    7 %: Valores por escenario: malo 25,25, normal 37,68 y bueno 54,96. El precio de 36,50 queda por encima del precio de Sí y por debajo del ponderado.
    8 %: Valores por escenario: malo 21,99, normal 31,58 y bueno 44,69. El precio supera al ponderado.
    9 %: Caso base; coincide con la escalera. Valores por escenario: 19,54, 27,22 y 37,62.
    10 %: Valores por escenario: malo 17,64, normal 23,96 y bueno 32,47.
    11 %: Valores por escenario: malo 16,11, normal 21,43 y bueno 28,54. El ponderado coincide con el de la hoja (21,79).

### Qué haría falsa la conclusión

    - Pasaría a Sí con un precio ejecutable, confirmado con cotización en firme, igual o inferior a unos 25,4 £.
    - Pasaría a Sí si el margen operativo de 2026 y 2027 se sitúa por encima del 15 % y la empresa publica un crecimiento orgánico del 4 % o más, lo que haría del escenario bueno el central.
    - Pasaría a No si el margen operativo baja del 12 % dos años seguidos o el ROCE bruto cae por debajo del 15 %.
    - Pasaría a No con una adquisición grande y cara pagada con la caja, o con un aumento material de las operaciones vinculadas con EOI o con la familia controladora.
    - Pasaría a No con una oferta de exclusión de minoritarios a un precio fijado por el controlador por debajo del valor.
    - Pasaría a Demasiado difícil si resulta imposible ejecutar operaciones a precios cercanos al medio cotizado, de modo que la cotización sea ficticia, o si el crecimiento orgánico resulta negativo y no se puede separar lo comprado de lo ganado.
    - Pasaría a No si la media de FCF 2024-26 queda por debajo de 17 mm £.

### Lo que no sabe

    - La elección del periodo del FCF base (media de tres años 2023-2025) figura en Control maestro como «Decisión del inversor (09-nov-2026)», fecha posterior al corte. No uso esa decisión: adopto la media de tres años como criterio propio porque los datos que la componen son anteriores al corte. Con la media de cinco años (16,99) el valor sería menor.
    - No tengo los informes primarios. Las cifras proceden de extractos y cálculos de la etapa 1, que trato como hipótesis verificadas solo en su aritmética.
    - Ni el crecimiento orgánico ni el desglose precio/volumen están publicados. Sin ellos no sé cuánto del crecimiento es comprado.
    - La retención de clientes tampoco se publica. No puedo verificar el foso.
    - El paquete no nombra competidores ni da su cuota de mercado.
    - No hay retorno publicado de las adquisiciones.
    - El precio de 36,50 £ es un medio sin operaciones ese día y el free float es de alrededor del 1,15 %. Un bloque podría no ejecutarse a ese precio.
    - El exceso de caja de 25 mm £ es un juicio heredado; la fase 1 da 34,7 como exceso central, que sumaría unos 0,8 £ por acción. Además, el accionista minoritario no controla el uso de la caja.
    - Desconozco quiénes son los beneficiarios de los Eden and Ariane Trusts y qué intenciones tienen sobre el 1,15 % restante.
    - No sé qué es la participación en una aeronave que figura en el inmovilizado.
    - Desconozco el motivo de la caída del margen bruto y del dividendo pagado en 2025.
    - El crecimiento implícito está calculado sobre la caja libre como aproximación al de las ventas; el paquete no trae un modelo de ventas y márgenes.
    - El valor de Simply Wall St (44,9 £) es derivado y de confianza baja; no lo uso.

### Citas

    [hoja_control_maestro] «Último cierre AIM 3.650p = 36,50 £ (precio medio, sin operaciones ese día). Horquilla 36,00/37,00.» → Precio actual y su iliquidez
    [hoja_control_maestro] «Cierre 30-oct-2026» → Fecha del precio
    [hoja_control_maestro] «Free float ≈1,15% (≈141.000 acciones). Rango 52 semanas 21–39 £.» → Liquidez y rango de precios
    [hoja_control_maestro] «Recompra de la sociedad a 24,00 en mar-2026; 38,00 el 16-sep-2026.» → Precios recientes por debajo del precio de Sí
    [hoja_control_maestro] «(CFO 31,50 − capex 10,50 − arrendamientos 2,74 → FCF base 18,26 mm GBP)» → FCF base
    [hoja_control_maestro] «Decisión del inversor (09-nov-2026)» → Decisión fechada después del corte; no la uso como tal
    [hoja_control_maestro] «FCF base resultante (C46−C47−C48−C49): 5 años 16,99; 3 años 18,26; LTM 23,94 (+41% vs 5 años, inflado por circulante 2025)» → Alternativas de FCF base
    [hoja_analisis] «Acciones diluidas (mm),Diluted shares outstanding.,12.258977» → Número de acciones
    [hoja_analisis] «Exceso de caja NO operativa que sumas (mm) · opcional,25,25,25» → Exceso de caja sumado
    [hoja_control_maestro] «31-dic-2025: 45,868; mínimo de cierres 5 años 29,6 (dic-2024).» → Base del exceso de caja
    [hoja_analisis] «Crecimiento de la caja libre · años 1–10,0,0.04,0.08» → Crecimientos de los escenarios
    [hoja_analisis] «Crecimiento para siempre · desde el año 11,0.01,0.02,0.025» → Crecimientos terminales
    [hoja_analisis] «Rentabilidad exigida al accionista (r / hurdle rate),Tu rentabilidad mínima objetivo. No pretende estimar un 'coste de equity verdadero' con precisión académica.,0.09» → Tasa del 9 %
    [hoja_analisis] «VALOR INTRÍNSECO POR ACCIÓN,19.5420750821087,27.2203452168066,37.6237483236999» → Valores por escenario (verificados con cálculo propio)
    [hoja_analisis] «0.0819413475172944» → Crecimiento implícito a diez años según la hoja
    [hoja_analisis] «r + 2 pts (11.0%),21.2691030517167,21.7913212803936» → Contraste de la sensibilidad al 11 %
    [respuesta] «Margen operativo 18,2% (2016), 16,2-16,4% (2019-2021), 14,4% (2022-23) y 13,4% (2024-25)» → Compresión del margen
    [respuesta] «minimal barriers to entry to those smaller businesses offering a lower price service» → Debilidad del foso
    [respuesta] «medias de tres años 15,1 (2016-18), 18,1 (2019-21), 14,7 (2022-24) y 18,9 (2023-25) mm £» → Historial de FCF que ancla el 4 % del escenario normal
    [hoja_control_maestro] «ROCE ANTES de impuestos = OP LTM 34,352 ÷ capital empleado bruto 188,24» → Calidad del negocio
    [hoja_control_maestro] «EOI Fire SARL 80,45% y Tristar Fire Corp. 18,40%» → Control y gobierno
    [hoja_control_maestro] «SBC = 0: sin partida en la conciliación ni en patrimonio» → Sin dilución
    [hoja_control_maestro] «Caja no restringida 54,823 ÷ préstamos a corto 0,199 = 275x» → Caja neta

### Comprobaciones mecánicas y normalizaciones

    {
      "comprobaciones": {
        "escalera_recalculada_anexo_c": {
          "p_estrella": 25.41428571428571,
          "precio_si": 25.41428571428571,
          "ponderado": 27.763999999999996,
          "precio_escenario_malo": 19.54
        },
        "citas_total": 23,
        "citas_literales": 23,
        "avisos": [],
        "nota": "Comprobaciones mecánicas informativas: no acreditan la calidad económica."
      },
      "normalizaciones_enum": []
    }

