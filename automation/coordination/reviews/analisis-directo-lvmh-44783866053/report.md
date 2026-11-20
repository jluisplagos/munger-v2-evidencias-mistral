# Análisis directo · LVMH, etapa 1 del universo (hoja del 2026-10-25)

Estado de la ejecución: `AUDITORIA_DOCUMENTAL_PENDIENTE_ACEPTACION`

Revisión a ciegas pendiente. No es aceptación, ni integración, ni aptitud para dinero real.

| Campo | Valor |
|---|---|
| Empresa | lvmh |
| Fecha de corte | 2026-10-25 |
| Tasa | 9 % |
| Tarea | analisis-directo-lvmh-44783866053 |
| SHA del código | fcb18bba533554c32f9756d6fb49dc0ebcc2946c |
| Huella del paquete (package_sha256) | 9fccf0caa755895a7b3262d921eb8d449ab88b7657f4e9093f98f3769a7c7c98 |
| Huella del envío (bundle_sha256) | 1a677f35032e27f53e4e257ba1aa2dff7974236e0bce7a9c35a4ea56238c4b34 |
| Huella del encargo | 022846e95b809a772317c2b17d6d946f3f91b9066c864911e473bb7ea15843e4 |
| Modelo pedido / devuelto | claude-opus-5-5 / claude-opus-5-5 |
| Esfuerzo | high |
| Mensajes enviados | 1 |
| Cota de entrada estimada antes de llamar | 166376 tokens |
| Reserva estimada antes de llamar | USD 1.320864 (máximo de la ejecución USD 3) |
| Reserva registrada | USD 1.320864 |
| Uso de tokens | entrada 73843, salida 14194 |
| Coste | CONOCIDO_ESTIMADO; estimado USD 0.579252; cota 0.579252 |

## Paquete de entrada

| id | ruta | commit | sha256 | bytes |
|---|---|---|---|---|
| respuesta | datos_analisis_directo/lvmh/etapa1/LVMH_respuesta.md | fcb18bba5335 | c1b05496e35bcd5e58f9dbc8590fc004d6e023ea30b5e19aae5f964bd566059b | 43458 |
| hoja_analisis | datos_analisis_directo/lvmh/etapa1/LVMH_evaluada__Análisis.csv | fcb18bba5335 | 54229e800f96c202ab6c128a3f85529509e940ae4d0b1795b5d618b7844fe204 | 24263 |
| hoja_guia_simply_wall_st | datos_analisis_directo/lvmh/etapa1/LVMH_evaluada__Guía_Simply_Wall_St.csv | fcb18bba5335 | 2791cc208d21b779b2104db9848a271eded2ae7cb4392769b743a2d95f8c3e2f | 7794 |
| hoja_opciones | datos_analisis_directo/lvmh/etapa1/LVMH_evaluada__Opciones.csv | fcb18bba5335 | b9f97b6706b77f7a28f70140d212f0790ee7334eb22965a4f538963e777a1a73 | 1537 |
| hoja_control_maestro | datos_analisis_directo/lvmh/etapa1/LVMH_evaluada__Control_maestro.csv | fcb18bba5335 | d1e6c229ebfabbece434efd03d887c6597693320807838204378076e532ab088 | 67917 |

## Salida del modelo (datos, sin acciones ejecutables)

Estado `concluido` · cubo «Vigilar» · acción `esperar` · zona `caro`

| Escenario | Valor por acción | Probabilidad |
|---|---|---|
| malo | 233.55 | 0.2 |
| normal | 362.02 | 0.6 |
| bueno | 512.17 | 0.2 |

| Escalera (k = 3) | Declarado | Recalculado (Anexo C) |
|---|---|---|
| Precio actual | 383 | |
| Precio del escenario malo | 233.55 | 233.55 |
| P* | 328.41 | 328.4114 |
| Precio de Sí = mín(P*, V_normal) | 328.41 | 328.4114 |
| Ponderado | 366.35 | 366.356 |
| Crecimiento implícito al precio actual / del normal (%) | 5.75 / 5 | |

| Tasa | Precio de Sí | Ponderado | Zona |
|---|---|---|---|
| 7 % | 462.81 | 524.07 | cumple_regla_k |
| 8 % | 384.44 | 431.73 | cumple_regla_k |
| 9 % | 328.41 | 366.35 | caro |
| 10 % | 286.37 | 317.67 | caro |
| 11 % | 253.67 | 280.04 | caro |

### Resumen

    LVMH es un negocio de marcas de lujo con balance sólido: deuda neta de 1,02x el EBITDA y caja libre positiva todos los años de la serie. Su poder de ganancia, sin embargo, se está estrechando. El margen recurrente ha pasado del 26,7% al 22,0%, el ROIC después de impuestos del 19,7% al 12,7–12,5%, y la caja libre normalizada está plana. El DCF parte de una caja libre base de 9.790 mm (media 2023-25 neta de la SBC) y 492,57 millones de acciones diluidas, descontado al 9%. Da 233,55 € en el escenario malo, 362,02 € en el normal y 512,17 € en el bueno, con un ponderado de 366,35 €. Con la regla k = 3, el precio de Sí es 328,41 €. A 383 € (cierre del 23-oct-2026) la acción está por encima del ponderado, en la zona caro. El precio descuenta un crecimiento de la caja libre de ≈5,75% anual, por encima del 5% del escenario normal. Conclusión: Vigilar y esperar. La conclusión es muy sensible a la tasa: al 8% el precio actual cumpliría por poco la regla k.


### Moneda

    EUR


### Justificación

    Estado concluido: el modelo es aplicable (caja libre positiva, financiación estable, intereses dentro del CFO, arrendamientos restados) y los datos materiales están en el paquete.
    
    Cubo Vigilar: el negocio es comprensible y el foso de marca parece real (margen bruto 64,5–68,8% desde 2017, 78% de las ventas en tiendas propias). Pero al 9% el precio de 383 € supera tanto el ponderado (366,35 €) como el precio de Sí (328,41 €), y exige un crecimiento del 5,75% frente al 5% del escenario normal.
    
    No es No porque el balance es fuerte y la tesis no está rota; tampoco es Sí porque el precio no da margen. Acción: esperar a un precio igual o inferior a ≈328 €, o a evidencia de recuperación del ROIC y del margen.


### Probabilidades

    Mantengo las de partida (0,2 / 0,6 / 0,2). El deterioro reciente ya está cargado en los crecimientos: 0% en el malo y 5% en el normal desde una base media de tres años inferior al LTM. Sesgar además las probabilidades castigaría dos veces el mismo riesgo. Suman 1.


### Fórmula aplicada

    Para P entre V_malo y V_normal:
    G(P) = 0,6·(362,02−P) + 0,2·(512,17−P) = 319,65 − 0,8P
    L(P) = 0,2·(P − 233,55)
    G = 3L → 319,65 − 0,8P = 0,6P − 140,13 → 1,4P = 459,77 → P* = 328,41
    Precio de Sí = mín(328,41; 362,02) = 328,41
    Ponderado = 0,2·233,55 + 0,6·362,02 + 0,2·512,17 = 366,35
    Precio 383 > 366,35 → caro


### Crecimiento implícito

    El dato sale del DCF inverso de la hoja: el crecimiento anual de la caja libre en los años 1–10 que iguala el valor a 383 €, con g terminal del 2%, base de 9.790 mm y r = 9%. Interpolando la tabla auxiliar (5,5% → 375,79 €; 6,0% → 390,10 €) se obtiene ≈5,75%. El paquete no permite un DCF por ventas a cinco años. Uso el crecimiento de la caja libre a diez años como aproximación del de ventas, porque el escenario normal supone margen estable. Es una aproximación, no la cifra exacta pedida.

### Escenario malo

    La normalización de la demanda continúa y el margen sigue cediendo. La caja libre se queda plana diez años en 9.790 mm (crecimiento 0%) y después crece al 1% perpetuo. Se apoya en que la caja libre normalizada ya está plana (11.601 → 11.682), el beneficio recurrente cae desde 2023 (22.802 → 17.755) y el inventario crece +4,7% con las ventas a −2,9% en H1 2026. Base: CFO 18.733 − capex 5.883 − arrendamientos 2.902 − SBC 158 = 9.790 mm, entre 492,570133 millones de acciones, descontado al 9%.

### Escenario normal

    LVMH crece como su mercado: volumen plano o algo al alza, precio y mezcla aportando el resto y margen recurrente estabilizado cerca del 22% (22,0% en 2025, 21,9% LTM). La caja libre crece al 5% anual diez años desde 9.790 mm y después al 2% perpetuo, lo que equivale a un múltiplo terminal de 14,6x. El 5% es exigente frente al orgánico reciente (+1%, −1%, +2%), pero parte de una base un 16% inferior al FCF LTM de 11.352 mm.

### Escenario bueno

    Vuelve el ciclo bueno: Asia recupera y Moda y Marroquinería rehace parte del margen perdido desde 2021 (41,6% → 34,1%), sin volver al pico. La caja libre crece al 9% anual diez años y después al 2,5% perpetuo. Misma base de 9.790 mm, mismas acciones y descuento al 9%.

### Sensibilidad (comentarios)

    7 %: Escenarios: malo 309,67, normal 515,16, bueno 765,20. P* = 462,81. El ponderado coincide con la sensibilidad de la hoja (524,07).
    8 %: Escenarios: malo 266,20, normal 425,71, bueno 615,33. El precio de 383 € queda apenas 1,44 € por debajo del precio de Sí: el umbral es frágil.
    9 %: Caso base. Coincide con la escalera.
    10 %: Escenarios: malo 208,12, normal 314,41, bueno 437,00.
    11 %: Escenarios: malo 187,75, normal 277,51, bueno 379,91. El ponderado coincide con la hoja (280,04).

### Qué haría falsa la conclusión

    - A No: margen recurrente por debajo del 20% dos años seguidos, o caja libre normalizada (circulante neutral) cayendo de forma sostenida por debajo de ≈11.000 mm.
    - A No: pérdida de cuota donde se publica (champán por debajo del 20%, Hennessy por debajo del 45%) o ROIC después de impuestos estabilizado en el 12–13% o menos dos años más.
    - A No: deterioro relevante de Tiffany/TAG Heuer (15.131 mm cerca del valor recuperable) o una adquisición grande pagada por encima de 15x EBITDA.
    - A Sí: cotización igual o inferior a ≈328 € con la tesis intacta (margen recurrente en torno al 22%, caja libre por encima de 10.000 mm, deuda neta por debajo de 1,5x EBITDA).
    - A Sí al precio actual: dos años de crecimiento orgánico del 5% o más con el ROIC volviendo al 15%, que elevarían el escenario normal.
    - A Demasiado difícil: ejercicio de la opción de venta de Diageo sobre el 34% de Moët Hennessy que cambie el perímetro, o que el resultado pase a depender sobre todo de divisas o aranceles.

### Lo que no sabe

    - La hoja Control maestro recoge decisiones del inversor fechadas el 28-oct-2026, posteriores a la fecha de corte: periodo de medias de tres años, definición de ROIC y C34. No las uso como hecho. Adopto por decisión propia la media FY2023-25, usando los datos de partida que ya constaban (CFO 18.733, capex 5.883, arrendamientos 2.902, SBC 158).
    - El precio de 383 € procede de fuentes secundarias coincidentes (abcbourse, boursorama, Simply Wall St), no de Euronext. Las recompras de octubre no están incorporadas al número de acciones.
    - El paquete no contiene ventas proyectadas ni un DCF por ventas. El crecimiento implícito se aproxima con el crecimiento de la caja libre a diez años, suponiendo margen constante.
    - No hay descomposición precio/volumen, ni cuotas de mercado fuera de vinos y licores, ni competidores nombrados.
    - No conozco la evolución de Tiffany por separado desde 2021.
    - El ROIC no lo publica la empresa. El 12,5% es un cálculo derivado y no sé si es nivel normal o punto bajo del ciclo.
    - La caja libre está consolidada al 100% e incluye a los minoritarios (Diageo, ≈3% del beneficio). El valor por acción puede estar ligeramente sobrestimado.
    - El perímetro ha cambiado tras el último balance (DFS en venta, Marc Jacobs vendida), y existen compromisos de compra de minoritarios por 6.416 mm.
    - El análisis de etapa 1 (respuesta) da un precio de Sí de ≈234 € con otra regla. Aquí aplico la regla k = 3 del encargo, que da 328,41 €. El juicio heredado se trata solo como hipótesis.
    - El valor de Simply Wall St (442,8 €) y el precio objetivo medio de analistas no se usan para concluir; son solo contraste externo.
    - La base de 9.790 mm es un 16% inferior al FCF LTM (11.352 mm). Elegir la base LTM elevaría todos los valores de forma material.

### Citas

    [hoja_analisis] «Precio actual,Cotización por acción.,383» → Precio actual de 383 €.
    [hoja_control_maestro] «Último cierre de mercado usado: 23-oct-2026.» → Fecha del precio.
    [hoja_analisis] «razonablemente estable.,9790,✓ PASA» → Caja libre base de 9.790 mm.
    [hoja_analisis] «Cash from Operations. Media de 3–5 años.,18733» → CFO medio de 18.733 mm.
    [hoja_analisis] «Escríbelo en POSITIVO.,5883» → Capex medio de 5.883 mm.
    [hoja_analisis] «2902,ℹ se resta del FCF» → Principal de arrendamientos de 2.902 mm.
    [hoja_analisis] «158,ℹ se resta del FCF» → SBC media de 158 mm restada.
    [hoja_analisis] «Diluted shares outstanding.,492.570133» → 492,57 millones de acciones diluidas.
    [hoja_analisis] «Crecimiento de la caja libre · años 1–10,0,0.05,0.09» → Crecimientos de los escenarios en los años 1-10.
    [hoja_analisis] «Crecimiento para siempre · desde el año 11,0.01,0.02,0.025» → Crecimientos terminales de los escenarios.
    [hoja_analisis] «VALOR INTRÍNSECO POR ACCIÓN,233.5470807223,362.017647150904,512.172282339273» → Valores por acción de los escenarios al 9%.
    [hoja_analisis] «366.354460902857,✗ BANDERA · poco margen» → Valor ponderado al 9%.
    [hoja_analisis] «0.0575182052787101,⚠ REVISAR · exige escenario BUENO» → Crecimiento implícito en el precio (DCF inverso).
    [hoja_analisis] «Tu r (9.0%),351.729485010865,366.354460902857,383.262870671635» → Contraste de la sensibilidad al 9%.
    [hoja_control_maestro] «Decisión del inversor (28-oct-2026): FCF base con media 3 años FY23-25» → Decisión con fecha posterior al corte, señalada en lo que no sé.
    [hoja_control_maestro] «CFO medio 3 a 18.733; 5 a 18.536; LTM 18.640» → Dato de partida del CFO, previo a la decisión.
    [hoja_control_maestro] «3 a 5.883; 5 a 5.134; LTM 4.317.» → Dato de partida del capex.
    [hoja_control_maestro] «3 a 2.902; 5 a 2.782; LTM 2.971.» → Dato de partida de los arrendamientos.
    [hoja_control_maestro] «Medias: 3 a 158; 5 a 147.» → Dato de partida de la SBC.
    [hoja_control_maestro] «CFO 18.640 − capex bruto en caja 4.317 − intereses fuera del CFO 0 − principal de arrendamientos 2.971 − cupones híbridos 0 = 11.352.» → FCF LTM de 11.352 mm.
    [hoja_control_maestro] «FCF normalizado (circulante neutral, impuesto corriente de PyG): 11.601 / 12.861 / 12.302 / 12.530 / 11.682 → plano/bajista.» → Caja libre normalizada plana.
    [hoja_control_maestro] «margen PRO (métrica menos distorsionada) 18,5% (2015) → 21,4% (2019) → pico 26,5–26,7% (2021–23) → 22,0% (2025) → 21,9% LTM» → Compresión del margen recurrente.
    [hoja_control_maestro] «después: 19,7/20,0/19,7/15,0/12,7%» → Caída del ROIC después de impuestos.
    [hoja_control_maestro] «÷ EBITDA LTM IFRS 16 23.936 = 1,02x» → Deuda neta / EBITDA.
    [hoja_control_maestro] «383,00 × 491.717.814 acciones netas = 188.328» → Capitalización bursátil.
    [hoja_control_maestro] «Inventario +4,7% (+3,8% sin divisa) vs ventas H1 −2,9% publicadas (+2% orgánico).» → Inventario creciendo más que las ventas.
    [hoja_control_maestro] «LVMH indica que Tiffany y TAG Heuer (15.131) están cerca del valor recuperable: +1 pt de tasa de descuento → deterioro de 1.667.» → Riesgo de deterioro de Tiffany y TAG Heuer.
    [respuesta] «beneficio recurrente 22.802 (2023) → 19.571 (2024) → 17.755 (2025)» → Caída del beneficio recurrente.
    [respuesta] «con una opción de venta de Diageo ejercitable en cualquier momento con seis meses de aviso» → Riesgo de cambio de perímetro.
    [hoja_control_maestro] «19 compras en mercado, 0 ventas: 1.230.882 acciones, 659,7 mm, precio medio 535,95 €.» → Compras de insiders.

### Comprobaciones mecánicas y normalizaciones

    {
      "comprobaciones": {
        "escalera_recalculada_anexo_c": {
          "p_estrella": 328.41142857142853,
          "precio_si": 328.41142857142853,
          "ponderado": 366.356,
          "precio_escenario_malo": 233.55
        },
        "citas_total": 30,
        "citas_literales": 30,
        "avisos": [],
        "nota": "Comprobaciones mecánicas informativas: no acreditan la calidad económica."
      },
      "normalizaciones_enum": []
    }

