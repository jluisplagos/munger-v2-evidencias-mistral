# Análisis directo · Puigbrands, etapa 1 del universo (hoja del 2026-10-26)

Estado de la ejecución: `AUDITORIA_DOCUMENTAL_PENDIENTE_ACEPTACION`

Revisión a ciegas pendiente. No es aceptación, ni integración, ni aptitud para dinero real.

| Campo | Valor |
|---|---|
| Empresa | puigbrands |
| Fecha de corte | 2026-10-26 |
| Tasa | 9 % |
| Tarea | analisis-directo-puigbrands-44791668660 |
| SHA del código | fcb18bba533554c32f9756d6fb49dc0ebcc2946c |
| Huella del paquete (package_sha256) | 106f0c276e816c0d0045b6d1c4cecf7cb575c213f36a8753182972325161f826 |
| Huella del envío (bundle_sha256) | d1af72017038fc9d26b4b86ad2addf3d98527fd260ec16a3f893e88a7c838187 |
| Huella del encargo | 022846e95b809a772317c2b17d6d946f3f91b9066c864911e473bb7ea15843e4 |
| Modelo pedido / devuelto | claude-opus-5-5 / claude-opus-5-5 |
| Esfuerzo | high |
| Mensajes enviados | 1 |
| Cota de entrada estimada antes de llamar | 194120 tokens |
| Reserva estimada antes de llamar | USD 1.43184 (máximo de la ejecución USD 3) |
| Reserva registrada | USD 1.43184 |
| Uso de tokens | entrada 88417, salida 20111 |
| Coste | CONOCIDO_ESTIMADO; estimado USD 0.755888; cota 0.755888 |

## Paquete de entrada

| id | ruta | commit | sha256 | bytes |
|---|---|---|---|---|
| respuesta | datos_analisis_directo/puigbrands/etapa1/Puigbrands_respuesta.md | fcb18bba5335 | 66efa2e7d14ca5e5992c112e548d9874bcd3dd4cb6e283d07a1c347e7900123a | 38722 |
| hoja_analisis | datos_analisis_directo/puigbrands/etapa1/Puigbrands_evaluada__Análisis.csv | fcb18bba5335 | 97f478bf3901abdd3a58b62ddce787fe573c238eaf2a2aeaa530479870516606 | 24195 |
| hoja_guia_simply_wall_st | datos_analisis_directo/puigbrands/etapa1/Puigbrands_evaluada__Guía_Simply_Wall_St.csv | fcb18bba5335 | 2791cc208d21b779b2104db9848a271eded2ae7cb4392769b743a2d95f8c3e2f | 7794 |
| hoja_opciones | datos_analisis_directo/puigbrands/etapa1/Puigbrands_evaluada__Opciones.csv | fcb18bba5335 | b9f97b6706b77f7a28f70140d212f0790ee7334eb22965a4f538963e777a1a73 | 1537 |
| hoja_control_maestro | datos_analisis_directo/puigbrands/etapa1/Puigbrands_evaluada__Control_maestro.csv | fcb18bba5335 | 1c826830900eddae6713585c8c2f7f2f321ef3239ce08d1d013aa48ea7e0a294 | 100166 |

## Salida del modelo (datos, sin acciones ejecutables)

Estado `concluido` · cubo «Vigilar» · acción `esperar` · zona `caro`

| Escenario | Valor por acción | Probabilidad |
|---|---|---|
| malo | 9.12 | 0.2 |
| normal | 13.09 | 0.6 |
| bueno | 20.07 | 0.2 |

| Escalera (k = 3) | Declarado | Recalculado (Anexo C) |
|---|---|---|
| Precio actual | 19.14 | |
| Precio del escenario malo | 9.12 | 9.12 |
| P* | 12.39 | 12.3857 |
| Precio de Sí = mín(P*, V_normal) | 12.39 | 12.3857 |
| Ponderado | 13.69 | 13.692 |
| Crecimiento implícito al precio actual / del normal (%) | 14.1 / 5 | |

| Tasa | Precio de Sí | Ponderado | Zona |
|---|---|---|---|
| 7 % | 17.71 | 19.77 | vigilar |
| 8 % | 14.6 | 16.21 | caro |
| 9 % | 12.39 | 13.69 | caro |
| 10 % | 10.74 | 11.82 | caro |
| 11 % | 9.46 | 10.38 | caro |

### Resumen

    Puig Brands es un negocio de marcas de perfume con margen bruto alto, márgenes operativos estables en torno al 16 % y deuda moderada. Su crecimiento orgánico se está frenando (+4,8 % en 9M-26). Tiene puntos débiles visibles: margen de Makeup y Skincare hundido en H1-26, existencias que crecen más que las ventas, menos holgura en las pruebas de deterioro y la compra de Isdin a 7,1 veces su valor en libros. Rehago la valoración con una base propia: 410,4 mm de FCF al accionista neto de SBC (UDM) en los escenarios normal y bueno, y 373,5 mm en el malo. Uso r = 9 % y ajusto por los 558,2 mm de put/call y earn-outs y por los 455,2 mm de asociadas. Salen 9,12 / 13,09 / 20,07 € por acción y un ponderado de 13,69 €. Con la regla k = 3, el precio de Sí es 12,39 €. A 19,14 € el precio queda en zona cara y exige que el FCF crezca en torno al 14 % anual durante cinco años. Cubo Vigilar y acción esperar.


### Moneda

    EUR


### Justificación

    Estado concluido: el negocio se puede acotar con FCF positivo y estable, una deuda simple y un rango de bases de FCF documentado.
    
    Cubo Vigilar y no No: la calidad del núcleo (fragancias de marca, margen operativo de ~16 %, conversión a caja sana) justifica seguirla.
    
    Acción esperar: a 19,14 € el precio supera el ponderado (13,69 €) y casi iguala el escenario bueno (20,07 €). Además exige un crecimiento del FCF del ~14 % anual a cinco años, frente al 5 % del normal. Solo con r = 7 % queda en zona vigilar, y nunca entra en la regla k = 3. El precio de Sí es 12,39 €.


### Probabilidades

    Mantengo 0,2 / 0,6 / 0,2. Los riesgos visibles (márgenes de Makeup y Skincare, existencias, deterioro e Isdin) ya están en la base y el crecimiento más bajos del escenario malo. El orgánico de 9M-26 (+4,8 %) sostiene el escenario normal. Mover probabilidades castigaría dos veces lo mismo.


### Fórmula aplicada

    Escenarios: V = (9,12; 13,09; 20,07) y p = (0,2; 0,6; 0,2).
    Para P entre 9,12 y 13,09:
    G(P) = 0,6·(13,09 − P) + 0,2·(20,07 − P) = 11,868 − 0,8P
    L(P) = 0,2·(P − 9,12) = 0,2P − 1,824
    G = 3L ⇒ 11,868 − 0,8P = 0,6P − 5,472 ⇒ P* = 17,340 / 1,4 = 12,39.
    Precio de Sí = mín(12,39; 13,09) = 12,39.
    Ponderado = 0,2·9,12 + 0,6·13,09 + 0,2·20,07 = 13,69.
    Precio 19,14 > 13,69 ⇒ zona caro.


### Crecimiento implícito

    Con margen estable, el crecimiento del FCF equivale al de las ventas. Planteamiento:
    - Valor del accionista que el precio debe justificar: 19,14 × 563,29 = 10.781,4 mm, más 103 mm de ajuste neto por put/call y asociadas = 10.884,4 mm.
    - Partiendo de la base de 410,4 mm, busco el crecimiento x de los años 1-5 que iguala ese valor. Mantengo las demás hipótesis del normal: 5 % en los años 6-10, g del 2 % y r del 9 %.
    - El factor necesario es 26,52, frente a 18,21 del escenario normal. Sale x ≈ 14,1 % anual (14 % da 26,46 y 14,1 % da 26,56).
    - Equivalente a diez años: ~10,0 % anual, interpolando la tabla del DCF inverso de la hoja reescalada a la base de 410,4.
    
    La hoja da 11,1 % porque parte de una base de 373,5.

### Escenario malo

    Las fragancias se normalizan, se pierde algo de cuota, Makeup y Skincare no recuperan margen y la publicidad sube. Supuestos y cifras:
    - Base: 373,5 mm, que es la media FY2023-FY2025 de 397,7 mm menos 24,2 de SBC. Queda un 9 % por debajo del FCF UDM neto de SBC (410,4) y equivale aproximadamente a perder un punto de margen operativo sobre unas ventas de ~5.042 mm.
    - Crecimiento del FCF del 2 % en los años 1-10 y g terminal del 1,5 %, con r = 9 %.
    - El valor de la plantilla es 9,307 € (hoja, fila 78).
    - Ajuste: (455,2 de asociadas − 558,2 de put/call y earn-outs) / 563,29 millones de acciones = −0,18 €.
    - Resultado: 9,12 €.

### Escenario normal

    Orgánico del 4-5 % (H1-26 +4,4 %, 9M-26 +4,8 %) con margen operativo estable (~16 %). Supuestos y cifras:
    - Base: 410,4 mm, el FCF al accionista UDM a 30/06/2026 (434,6) menos la SBC (24,2). Es un periodo sin efecto neto del factoring, que es cero en ambos extremos.
    - Crecimiento del FCF del 5 % anual en los años 1-10 y g terminal del 2 %, con r = 9 %.
    - Valor: 18,214 veces la base / 563,29 = 13,27 €.
    - Ajuste por put/call y asociadas: −0,18 €.
    - Resultado: 13,09 €.

### Escenario bueno

    Las grandes marcas de fragancias recuperan cuota, Charlotte Tilbury y Asia-Pacífico siguen creciendo a dos dígitos y Makeup y Skincare vuelven a los márgenes de 2025. Supuestos y cifras:
    - Base: 410,4 mm.
    - Crecimiento del FCF del 10 % anual en los años 1-10 (sin compras) y g terminal del 2,5 %, con r = 9 %.
    - Valor: 27,796 veces la base / 563,29 = 20,25 €.
    - Ajuste: −0,18 €.
    - Resultado: 20,07 €.

### Sensibilidad (comentarios)

    7 %: Escenarios 12,54 / 18,70 / 30,21. Solo aquí el precio cae por debajo del ponderado, y sigue por encima del precio de Sí.
    8 %: Escenarios 10,57 / 15,42 / 24,20.
    9 %: Coincide con la escalera. Escenarios 9,12 / 13,09 / 20,07.
    10 %: Escenarios 8,02 / 11,34 / 17,06.
    11 %: Escenarios 7,15 / 9,99 / 14,78.

### Qué haría falsa la conclusión

    - Que el FCF al accionista de FY2026, neto de SBC y con circulante neutro, quede por debajo de ~370 mm. Eso validaría el escenario malo como base y bajaría el cubo a No.
    - Que el margen operativo del grupo de FY2026 completo baje del 15 % o que la cuota de fragancias vuelva a caer desde el 11,1 %.
    - Que Isdin se cierre con deuda neta / EBITDA por encima de 2,5x, o que se anuncien más compras grandes con deuda que hagan depender el crecimiento del M&A.
    - Un deterioro relevante de la UGE Charlotte Tilbury o de Niche & Wellness, o existencias que sigan creciendo más que las ventas a 31/12/2026 con menor cobertura de obsolescencia.
    - Al alza: un FCF FY2026 de 480 mm o más (neto de SBC) con circulante neutro, orgánico por encima del 5 % y Makeup por encima del 10 % de margen. Subiría la base y el precio de Sí hacia ~14 €.
    - Al alza en precio: una cotización en torno a 12,4 € o menos con el negocio intacto llevaría a la zona de la regla k = 3.

### Lo que no sabe

    - Uso de datos posteriores al corte: el paquete incluye «decisiones del inversor» fechadas el 01-nov-2026, posteriores al corte (ventana del FCF base, definición del ROIC y SBC). No las uso como decisiones; elijo la base yo con datos anteriores al corte. Tampoco uso el Capital Markets Day del 28-10-2026 ni la lectura no confirmada de 19,41 € del 26/10.
    - Precio: procede de proveedores secundarios (cierre del 23/10/2026), no de BME ni de la CNMV.
    - Isdin: no conozco su beneficio, su caja ni su deuda. Trato la compra del 50 % restante (900 mm al cierre más 300 en 2029) como neutral en valor, aunque 7,1 veces el valor en libros sugiere riesgo de sobrepago.
    - Asociadas: las sumo a su valor en libros (455,2 mm), que probablemente infravalora la mitad de Isdin que ya se posee. Si se valoraran al precio implícito de la operación, el valor subiría en torno a 1-1,8 € por acción.
    - Charlotte Tilbury: no hay ventas ni beneficio publicados, aunque es el 42,3 % del fondo de comercio y las marcas.
    - Huecos de datos: falta el tipo impositivo efectivo, el umbral del covenant, el peso y el vencimiento de las licencias de moda, la separación entre precio y volumen y los competidores concretos.
    - Base del FCF: la de 410,4 mm (UDM) está deprimida por el acopio de existencias de H1-26 y la de 373,5 mm mezcla ventanas. El rango razonable va de 345 a 497 mm netos de SBC.
    - Dilución futura: no sé si el LTIP 2025-2029 se liquidará con acciones nuevas. La SBC UDM se está duplicando.
    - Referencias externas: el fair value de Simply Wall St tiene tres meses y es inestable; no lo uso.
    - Ventas: no conozco el resultado del cuarto trimestre de 2026 ni las ventas anuales cerradas de 2026.

### Citas

    [hoja_control_maestro] «Se registra el cierre del viernes 23/10/2026 (19,14 EUR)» → Precio actual y su fecha.
    [hoja_analisis] «Precio actual,Cotización por acción.,19.14» → Precio usado en la hoja.
    [hoja_control_maestro] «UDM = CFO 786,6 - capex 206,9 - intereses bancarios 48,2 - intereses de arrendamiento 11,1 - principal de arrendamientos 85,8 = 434,6.» → FCF al accionista UDM.
    [hoja_control_maestro] «neta de SBC 410,4» → Base de 410,4 mm de los escenarios normal y bueno.
    [hoja_control_maestro] «media 4a 344,8 · media 3a 397,7 · último FY 520,8 · UDM a 30/06/2026 434,6» → Rango de bases de FCF y media de 3 años del escenario malo.
    [hoja_analisis] «razonablemente estable.,373.5,✓ PASA» → Base de 373,5 mm (media de 3 años menos SBC) del escenario malo.
    [hoja_control_maestro] «520,8 mm (FY2025, dato cerrado y auditado pero diez meses atrasado y con una aportación de circulante atípicamente favorable de +41,3)» → No uso FY2025 como base.
    [hoja_control_maestro] «AMBAS fechas tienen factoring de clientes CERO» → El UDM a junio está limpio de factoring.
    [hoja_control_maestro] «568.187.026 emitidas - 4.894.911 de autocartera = 563.292.115» → Número de acciones.
    [hoja_control_maestro] «558,2 mm de pasivos por combinaciones de negocio (opciones put/call sobre minoritarios y earn-outs» → Ajuste negativo del valor.
    [hoja_control_maestro] «Asociadas a 455,2, saldo a 30/06/2026» → Ajuste positivo por asociadas.
    [hoja_control_maestro] «los 24,0 mm efectivamente cobrados se clasifican en INVERSIÓN» → El FCF no recoge las asociadas, por eso se suman aparte.
    [hoja_control_maestro] «pagará 900 mm en efectivo al cierre más un pago diferido FIJO y SIN INTERESES de 300 mm en Q1 2029» → Términos de Isdin.
    [hoja_control_maestro] «Puig acuerda pagar 1.200 mm por un 50% cuyo valor en libros es 168 mm, es decir 7,1 veces» → Riesgo de sobrepago en Isdin.
    [hoja_control_maestro] «pro forma la ratio iría a ~2,4x (deuda neta 2.789 / EBITDA ~1.182 estimado)» → Apalancamiento tras Isdin.
    [respuesta] «el orgánico se desacelera: +7,8 % en 2025, +4,4 % en H1-26, +4,8 % en 9M-26» → Crecimiento del 5 % en el escenario normal.
    [hoja_control_maestro] «margen operativo 14,8 / 16,1 / 15,8 / 16,1 % en FY2022-FY2025 y 16,1 % UDM» → Margen estable en el escenario normal.
    [respuesta] «en H1-26 Makeup y Skincare tuvieron márgenes del 1,8 % y 1,5 % (3,6 % y 7,6 % en H1-25) sin explicación» → Riesgo del escenario malo.
    [hoja_control_maestro] «Existencias 844,6 (30/06/2026) frente a 765,4 (30/06/2025) = +10,35%, frente a ventas del semestre +2,37%» → Señal de existencias.
    [hoja_control_maestro] «El impacto de +1,5 pp en la tasa de descuento pasa de 9,5 mm (FY2024) a 220,6 mm (FY2025), x23» → Menor holgura en las pruebas de deterioro.
    [respuesta] «la cuota de fragancias bajó de 11,5 % a 11,1 % en 2025» → Pérdida de cuota.
    [hoja_analisis] «78,VALOR INTRÍNSECO POR ACCIÓN,9.30739242610205,12.0773613009326,18.4305196921659» → Valores de la plantilla con base 373,5; los reescalo a 410,4 para el normal y el bueno.
    [hoja_analisis] «67,Crecimiento de la caja libre · años 1–10,0.02,0.05,0.1» → Crecimientos de los escenarios.
    [hoja_analisis] «68,Crecimiento para siempre · desde el año 11,0.015,0.02,0.025» → g terminal de los escenarios.
    [hoja_analisis] «148,0.1,17.5603500819079» → Tabla del DCF inverso usada para el equivalente a diez años.
    [hoja_control_maestro] «la tasa anual se está duplicando» → Riesgo de una SBC creciente.
    [hoja_control_maestro] «924,0 mm de LÍNEAS DE CRÉDITO CONTRATADAS Y NO DISPUESTAS» → Liquidez: la deuda no amenaza la continuidad.
    [hoja_control_maestro] «Decisión del inversor (01-nov-2026)» → Dato posterior al corte, no usado como decisión.

### Comprobaciones mecánicas y normalizaciones

    {
      "comprobaciones": {
        "escalera_recalculada_anexo_c": {
          "p_estrella": 12.385714285714283,
          "precio_si": 12.385714285714283,
          "ponderado": 13.692,
          "precio_escenario_malo": 9.12
        },
        "citas_total": 28,
        "citas_literales": 28,
        "avisos": [],
        "nota": "Comprobaciones mecánicas informativas: no acreditan la calidad económica."
      },
      "normalizaciones_enum": []
    }

