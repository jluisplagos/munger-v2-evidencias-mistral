# Análisis directo · Omer, etapa 1 del universo (hoja del 2026-11-01)

Estado de la ejecución: `AUDITORIA_DOCUMENTAL_PENDIENTE_ACEPTACION`

Revisión a ciegas pendiente. No es aceptación, ni integración, ni aptitud para dinero real.

| Campo | Valor |
|---|---|
| Empresa | omer |
| Fecha de corte | 2026-11-01 |
| Tasa | 9 % |
| Tarea | analisis-directo-omer-44815199127 |
| SHA del código | fcb18bba533554c32f9756d6fb49dc0ebcc2946c |
| Huella del paquete (package_sha256) | b86b45d49bebb582785a9c534ef025c72bf50913c5a87537d893e775fd423d7f |
| Huella del envío (bundle_sha256) | c4cfc507ae68bb5b3d8822797b380d7261b56e5e9d32292603df867314dcf837 |
| Huella del encargo | 022846e95b809a772317c2b17d6d946f3f91b9066c864911e473bb7ea15843e4 |
| Modelo pedido / devuelto | claude-opus-5-5 / claude-opus-5-5 |
| Esfuerzo | high |
| Mensajes enviados | 1 |
| Cota de entrada estimada antes de llamar | 138624 tokens |
| Reserva estimada antes de llamar | USD 1.209856 (máximo de la ejecución USD 3) |
| Reserva registrada | USD 1.209856 |
| Uso de tokens | entrada 62488, salida 22878 |
| Coste | CONOCIDO_ESTIMADO; estimado USD 0.707512; cota 0.707512 |

## Paquete de entrada

| id | ruta | commit | sha256 | bytes |
|---|---|---|---|---|
| respuesta | datos_analisis_directo/omer/etapa1/Omer_respuesta.md | fcb18bba5335 | c4aa4e804549308f44226b4d5461c23c1192cbf0675573e88cadf47ff7c832ae | 30976 |
| hoja_analisis | datos_analisis_directo/omer/etapa1/Omer_evaluada__Análisis.csv | fcb18bba5335 | 842ea31b1ad9d3a02ce2059595811190d3b6b214b434802a9dac7e92309be8f5 | 23655 |
| hoja_guia_simply_wall_st | datos_analisis_directo/omer/etapa1/Omer_evaluada__Guía_Simply_Wall_St.csv | fcb18bba5335 | 2791cc208d21b779b2104db9848a271eded2ae7cb4392769b743a2d95f8c3e2f | 7794 |
| hoja_opciones | datos_analisis_directo/omer/etapa1/Omer_evaluada__Opciones.csv | fcb18bba5335 | b9f97b6706b77f7a28f70140d212f0790ee7334eb22965a4f538963e777a1a73 | 1537 |
| hoja_control_maestro | datos_analisis_directo/omer/etapa1/Omer_evaluada__Control_maestro.csv | fcb18bba5335 | 657c55f755310fa21b0063e94cc92cf6f22b97006db0dd786e10fa6165304558 | 53273 |

## Salida del modelo (datos, sin acciones ejecutables)

Estado `pendiente_de_investigacion` · cubo «Vigilar» · acción `esperar` · zona `cumple_regla_k`

| Escenario | Valor por acción | Probabilidad |
|---|---|---|
| malo | 2.997 | 0.2 |
| normal | 5.082 | 0.6 |
| bueno | 7.571 | 0.2 |

| Escalera (k = 3) | Declarado | Recalculado (Anexo C) |
|---|---|---|
| Precio actual | 3.46 | |
| Precio del escenario malo | 2.997 | 2.997 |
| P* | 4.544 | 4.544 |
| Precio de Sí = mín(P*, V_normal) | 4.544 | 4.544 |
| Ponderado | 5.163 | 5.1628 |
| Crecimiento implícito al precio actual / del normal (%) | -4.5 / 5 | |

| Tasa | Precio de Sí | Ponderado | Zona |
|---|---|---|---|
| 7 % | 6.271 | 7.252 | bajo_malo |
| 8 % | 5.263 | 6.028 | cumple_regla_k |
| 9 % | 4.544 | 5.163 | cumple_regla_k |
| 10 % | 4.006 | 4.519 | cumple_regla_k |
| 11 % | 3.588 | 4.023 | cumple_regla_k |

### Resumen

    OMER fabrica interiores de aluminio, módulos de aseo, carenados y puertas para constructores de trenes. Tiene caja neta de unos 28 mm frente a una capitalización de 99 mm. He recalculado los tres escenarios heredados al 9 % con FCF base 7,44 mm, 10 mm de caja sobrante y 28,635 millones de acciones: malo 3,00 €, normal 5,08 €, bueno 7,57 €. El ponderado es 5,16 €, P* es 4,54 € y el precio de Sí es 4,54 €. A 3,46 € el precio queda en la zona de la regla k = 3 a cualquier tasa entre el 8 % y el 11 %. También queda en esa zona con un escenario malo mucho más duro (2,50 €, e incluso 1,5 €). La conclusión no depende del escenario malo, sino del normal. Ese escenario supone un FCF que crece un 5 % anual con margen EBITDA cercano al 22 %. Si el FCF no creciera (V_normal ≈ 3,62 €), P* caería por debajo del precio. Esa hipótesis no se puede acotar con el paquete por cuatro motivos: no hay datos de clientes ni de competidores; el ROIC incremental es bajo (1,7 % FY21→FY25); el backlog ha bajado de 161 a 142 mm; y los resultados de 9M-2026 son posteriores al corte. Por eso dejo el análisis pendiente de investigación, en Vigilar, y espero.


### Moneda

    EUR


### Justificación

    Mecánicamente el precio cumple la regla k = 3 entre el 8 % y el 11 % y también con un escenario malo muy duro, porque la caja neta acota bien la caída. La conclusión depende del escenario normal. Con FCF plano, P* < 3,46. Ese escenario supone FCF +5 % anual con margen del 22 %, y no puedo acotarlo por cuatro razones: 1) el paquete no trae ventas por cliente ni competidores; 2) la propia empresa avisa de tendencia a bajar precios; 3) el crecimiento 2021–2025 apenas subió el EBIT (ROIC incremental del 1,7 %); 4) el backlog y los ingresos bajan en 2026, y los brókers implican un segundo semestre peor. A eso se suman el gobierno corporativo con un accionista de control del 73,6 %, los alquileres a partes vinculadas y la iliquidez. No lo dejo en Demasiado difícil porque las incógnitas se pueden investigar con datos concretos: 9M y FY2026, concentración de clientes, saldo de factoring y condiciones de alquiler. No compro hasta acotar el normal: Vigilar y esperar.


### Probabilidades

    Mantengo 0,2 / 0,6 / 0,2. Los hechos negativos (backlog de 161 a 142 mm, ingresos del primer semestre −6 %, EBITDA del segundo semestre de 2026 implícito por los brókers menor que el de 2025) ya están en la incertidumbre sobre el normal y en el contraste del malo. Mover también las probabilidades contaría dos veces el mismo riesgo. No las ajusto para cuadrar con la cotización.


### Fórmula aplicada

    Para 2,997 ≤ P ≤ 5,082: G(P) = 0,6·(5,082−P) + 0,2·(7,571−P) = 4,5634 − 0,8P y L(P) = 0,2·(P−2,997) = 0,2P − 0,5994. Imponiendo G = 3L: 4,5634 − 0,8P = 0,6P − 1,7983, de donde P* = 6,3617 / 1,4 = 4,544. Precio de Sí = mín(4,544; 5,082) = 4,544. Ponderado = 0,2·2,997 + 0,6·5,082 + 0,2·7,571 = 5,163. Con el precio de 3,46 €: G = 1,795 y L = 0,093 (cociente 19,4). Como 2,997 < 3,46 ≤ 4,544, la zona es cumple_regla_k. Con un malo de 2,50 €, P* sería 4,33 €.


### Crecimiento implícito

    Aproximo el FCF como proporcional a las ventas, con el margen y la intensidad de circulante del normal. Busco el crecimiento x de los años 1–5 que hace que el valor sea igual a 3,46 € (99,08 mm, de los que 10 mm son caja). Mantengo las demás hipótesis del normal: 5 % en los años 6–10, g del 2 % y r del 9 %. Con x = −4 % el valor es 101,1 mm y con −5 % es 97,1 mm; interpolando, x ≈ −4,5 % anual. Contraste: la hoja da un −0,67 % anual de FCF durante 10 años. El normal supone ventas y FCF de alrededor del +5 % anual.

### Escenario malo

    El FCF base de 7,44 mm es la media FY23–FY25: CFO 12,06 menos capex 4,62, con SBC 0. Cae un 2 % anual durante 10 años (FCF del año 10: 6,08 mm), con g terminal del 1 % y r del 9 %. Se suman 10 mm de caja sobrante (caja de 32,075 más títulos de 5,0, menos caja operativa e INNORAIL) y se divide entre 28,635 millones de acciones. La historia: los clientes aprietan precios y el backlog sigue bajando. Contraste más duro: con −5 % anual el valor sería ≈2,50 € (cálculo propio). Recalculado: 85,83 mm / 28,635 = 2,997 €.

### Escenario normal

    Mismo FCF base de 7,44 mm, que crece un 5 % anual durante 10 años (año 10: 12,12 mm), con g terminal del 2 %, más 10 mm de caja. Supone ventas +5–6 % con un backlog de unas 1,6 veces las ventas y margen EBITDA antes de provisiones cercano al 22 % (22,5 / 22,5 / 22,7 / 21,8 % en FY22–FY25). El FCF normalizado ya está en 10,8 mm LTM. El 55 % del valor viene del terminal. Valor: 145,52 mm / 28,635 = 5,082 €.

### Escenario bueno

    El FCF crece un 10 % anual durante 10 años (año 10: 19,30 mm, similar al FCF LTM de 19,7 con liberación de circulante), con g terminal del 2,5 % y 10 mm de caja. Exige que North America deje de perder dinero con Amtrak y Metra y que INNORAIL se llene al margen actual. Valor: 216,80 mm / 28,635 = 7,571 €.

### Sensibilidad (comentarios)

    7 %: Valores: malo 3,820, normal 7,084 y bueno 11,187. P* = (0,6·7,084 + 0,2·11,187 + 0,6·3,820)/1,4 = 6,271. El precio de 3,46 queda por debajo del malo.
    8 %: Valores: malo 3,350, normal 5,914 y bueno 9,045. P* = 5,263.
    9 %: Coincide con la escalera: malo 2,997, normal 5,082, bueno 7,571.
    10 %: Valores: malo 2,721, normal 4,459 y bueno 6,498. P* = 4,006.
    11 %: Valores: malo 2,499, normal 3,977 y bueno 5,684. P* = 3,588; el margen sobre 3,46 es estrecho. El ponderado coincide con la sensibilidad de la hoja (4,0228).

### Qué haría falsa la conclusión

    - 9M-2026 o FY2026 con backlog estable o recuperado (≥150 mm) y margen EBITDA antes de provisiones ≥22 %: acotaría el normal y llevaría a Sí con el precio aún por debajo de ~4,5 €.
    - Un desglose de ventas por cliente que muestre una concentración moderada y la condición de proveedor cualificado de pocos competidores: apoyaría el normal.
    - Margen EBITDA antes de provisiones por debajo del 20 % dos semestres seguidos con backlog por debajo de 130 mm: el normal se acercaría a crecimiento cero (≈3,6 €) y pasaría a No al precio actual.
    - Un saldo de factoring pro soluto grande y recurrente, o una caja restringida (SIMEST) que elimine el exceso de caja de 10 mm: reduce todos los valores en ~0,35 €.
    - Alquileres a sociedades del accionista de control por encima de mercado, nuevas operaciones vinculadas o un uso de la caja ajeno al negocio: pasaría a No.
    - INNORAIL con retornos por debajo del 9 % o North America en pérdidas en 2026: rebajaría el bueno y el normal.
    - Un precio por debajo del escenario malo (≈3,0 €) haría la decisión robusta incluso con el normal plano.

### Lo que no sabe

    - Ventas por cliente, concentración, competidores con nombre y cuota, y margen por contrato: no están en el paquete y son la hipótesis central.
    - Los resultados de 9M-2026 se publican el 16-11-2026, después del corte: no existen para este análisis.
    - El paquete cita decisiones del inversor fechadas el 9-nov-2026 (FCF base de media de 3 años y ventana de acciones), posteriores al corte. No las uso como decisión: elijo la media FY23–FY25 como criterio propio a partir de cifras publicadas antes del corte.
    - El saldo cedido en factoring (Hitachi Rail) no se publica desde FY24; el principal de leasing se interpreta como incluido dentro del CFO (sensibilidad: −0,38 mm/año).
    - El exceso de caja de 10 mm es una estimación: depende de la caja operativa necesaria (8–16 mm), de los ~14 mm propios de INNORAIL y de una posible cuenta SIMEST restringida.
    - Las condiciones de los alquileres con Betha y Omer Immobiliare frente a mercado, y la retribución individual del consejo.
    - El precio es un cierre puntual de un valor muy poco líquido (8.132 acciones el 30/10/2026); puede no ser representativo.
    - El escenario malo heredado (−2 % anual) puede ser blando frente a 2016–2018 (EBITDA −72 %). Lo contrasto con −5 % (≈2,50 €), pero no modelo un ciclo explícito.
    - No modelo la distribución de dividendos ni el capex extraordinario de INNORAIL más allá de lo restado de la caja.
    - Los objetivos de los brókers y el fair value de Simply Wall St son secundarios (el de SWS es de febrero de 2026); no los uso para el valor.

### Citas

    [hoja_control_maestro] «Precio de referencia de cierre 3,46 € (30/10/2026). ACTUALIZAR ANTES DE CUALQUIER DECISIÓN.» → Precio actual y fecha
    [hoja_control_maestro] «Valor muy poco líquido (8.132 acciones el 30/10; ~15.000/día en H1-26)» → Iliquidez y representatividad del precio
    [hoja_analisis] «Caja de las operaciones (mm),Cash from Operations. Media de 3–5 años.,12.06» → CFO medio FY23–FY25
    [hoja_analisis] «Capex: inversión en activos (mm),Capital Expenditures. Escríbelo en POSITIVO.,4.62» → Capex medio; FCF base = 12,06 − 4,62 = 7,44
    [hoja_analisis] «razonablemente estable.,7.44,✓ PASA» → FCF base de 7,44 mm
    [hoja_analisis] «Acciones diluidas (mm),Diluted shares outstanding.,28.635408» → Número de acciones
    [hoja_analisis] «Exceso de caja NO operativa que sumas (mm) · opcional,10,10,10» → Caja sobrante sumada en los tres escenarios
    [hoja_control_maestro] «Disponibilità liquide 32,075 (depósitos 32,069 + caja 0,006). Excluye títulos 5,000» → Caja del balance a 30/06/2026
    [hoja_control_maestro] «Deuda financiera bruta 3,964: bancos 1,885 (UniCredit, quirografaria)» → Deuda pequeña; caja neta
    [hoja_control_maestro] «INNORAIL ~14 de fondos propios en 36 meses.» → Uso futuro de caja restado del exceso
    [hoja_analisis] «Crecimiento de la caja libre · años 1–10,-0.02,0.05,0.1» → Crecimientos de los escenarios
    [hoja_analisis] «Crecimiento para siempre · desde el año 11,0.01,0.02,0.025» → g terminal de los escenarios
    [hoja_analisis] «Probabilidad que le das,0.2,0.6,0.2» → Probabilidades
    [hoja_analisis] «VALOR INTRÍNSECO POR ACCIÓN,2.99718142362823,5.08165329775924,7.5710969977542» → Valores por escenario al 9 % (coinciden con mi recálculo)
    [hoja_analisis] «plegarlo o abrirlo.,5.16264766293203» → Valor ponderado
    [hoja_analisis] «-0.00668890399896444,✓ PASA · ≤ NORMAL» → Crecimiento del FCF a 10 años implícito en el precio
    [hoja_analisis] «0,3.61585671544106» → Valor del normal con FCF plano: la regla k = 3 dejaría de cumplirse
    [hoja_analisis] «r + 2 pts (11.0%),3.9224343604195,4.02282651266046,4.13518484175703» → Contraste del ponderado al 11 %
    [hoja_analisis] «r − 2 pts (7.0%),6.80786733147829,7.25151921124079,7.7970895119091» → Contraste del ponderado al 7 %
    [hoja_control_maestro] «FCF (CFO−capex) 13,8 / −9,8 / 11,6 / 2,3 / 8,4; LTM 19,7 (con liberación de circulante +9,9). FCF normalizado (sin ΔCCN ni desfase de impuestos) 8,5 / 6,3 / 6,4 / 11,0 / 10,8; LTM 10,8.» → Volatilidad del FCF y nivel normalizado
    [hoja_control_maestro] «antes de provisiones 27,5 → 22,5 / 22,5 / 22,7 / 21,8 → LTM 23,0» → Margen estable desde 2022 (hipótesis del normal)
    [hoja_control_maestro] «ROIC incremental 2021→LTM 8,1% (FY21→FY25 1,7%)» → Crecimiento con poco retorno incremental
    [respuesta] «en el primer semestre de 2026 los ingresos caen un 6 % y el backlog baja de 161 a 142 mm» → Deterioro reciente del backlog y de las ventas
    [hoja_control_maestro] «Ojo: EBITDA H2-26 implícito por brokers (~6,7) < H2-25 (9,1): el LTM puede sobrestimar el recurrente.» → Riesgo a corto plazo sobre el normal
    [respuesta] «de 2016 a 2018 la matriz pasó de 32,4 a 22,1 mm de ingresos y de 10,2 a 2,8 mm de EBITDA» → Historial cíclico; contraste del malo
    [hoja_control_maestro] «Halfa S.r.l. 73,57% (indirecta; socios G. Russello 60% y V. Russello 40%, ambos consejeros)» → Accionista de control
    [respuesta] «compras a esas inmobiliarias de 0,56 mm en 2021 a 1,65 mm en 2025» → Operaciones con vinculadas
    [hoja_control_maestro] «saldo bruto cedido no publicado desde FY24» → Factoring no cuantificado
    [hoja_control_maestro] «Decisión del inversor (9-nov-2026): FCF base con media 3 años FY2023–FY2025» → Dato posterior al corte, no usado como decisión
    [hoja_control_maestro] «Datos 9M 2026 (no auditados) se publican el 16/11/2026: revisar.» → Resultados 9M posteriores al corte

### Comprobaciones mecánicas y normalizaciones

    {
      "comprobaciones": {
        "escalera_recalculada_anexo_c": {
          "p_estrella": 4.543999999999999,
          "precio_si": 4.543999999999999,
          "ponderado": 5.1628,
          "precio_escenario_malo": 2.997
        },
        "citas_total": 30,
        "citas_literales": 30,
        "avisos": [],
        "nota": "Comprobaciones mecánicas informativas: no acreditan la calidad económica."
      },
      "normalizaciones_enum": []
    }

