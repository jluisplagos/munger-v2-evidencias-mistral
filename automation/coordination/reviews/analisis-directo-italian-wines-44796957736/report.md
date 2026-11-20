# Análisis directo · Italian_Wines, etapa 1 del universo (hoja del 2026-11-04)

Estado de la ejecución: `AUDITORIA_DOCUMENTAL_PENDIENTE_ACEPTACION`

Revisión a ciegas pendiente. No es aceptación, ni integración, ni aptitud para dinero real.

| Campo | Valor |
|---|---|
| Empresa | italian-wines |
| Fecha de corte | 2026-11-04 |
| Tasa | 9 % |
| Tarea | analisis-directo-italian-wines-44796957736 |
| SHA del código | fcb18bba533554c32f9756d6fb49dc0ebcc2946c |
| Huella del paquete (package_sha256) | 86c48d7e681cc32b2b4d069d09e1314b8b6c4f0b5c4b8a160f20b81d65671a83 |
| Huella del envío (bundle_sha256) | 98ac7dc17ebb0b8def3c92c230c97d3496f373e9498c3178c344e3f9136f1807 |
| Huella del encargo | 022846e95b809a772317c2b17d6d946f3f91b9066c864911e473bb7ea15843e4 |
| Modelo pedido / devuelto | claude-opus-5-5 / claude-opus-5-5 |
| Esfuerzo | high |
| Mensajes enviados | 1 |
| Cota de entrada estimada antes de llamar | 142272 tokens |
| Reserva estimada antes de llamar | USD 1.224448 (máximo de la ejecución USD 3) |
| Reserva registrada | USD 1.224448 |
| Uso de tokens | entrada 64001, salida 21708 |
| Coste | CONOCIDO_ESTIMADO; estimado USD 0.690164; cota 0.690164 |

## Paquete de entrada

| id | ruta | commit | sha256 | bytes |
|---|---|---|---|---|
| respuesta | datos_analisis_directo/italian-wines/etapa1/Italian_Wines_respuesta.md | fcb18bba5335 | 7c64b2efb92f41d4d3d47852467692261ee89f7dad493aa775fbc9ca0f620489 | 33807 |
| hoja_analisis | datos_analisis_directo/italian-wines/etapa1/Italian_Wines_evaluada__Análisis.csv | fcb18bba5335 | d7f08e649d69f1f9c65d520e0878ac7dde69ee60a576e3640a95a50bcdf5c2d3 | 22931 |
| hoja_guia_simply_wall_st | datos_analisis_directo/italian-wines/etapa1/Italian_Wines_evaluada__Guía_Simply_Wall_St.csv | fcb18bba5335 | 2791cc208d21b779b2104db9848a271eded2ae7cb4392769b743a2d95f8c3e2f | 7794 |
| hoja_opciones | datos_analisis_directo/italian-wines/etapa1/Italian_Wines_evaluada__Opciones.csv | fcb18bba5335 | b9f97b6706b77f7a28f70140d212f0790ee7334eb22965a4f538963e777a1a73 | 1537 |
| hoja_control_maestro | datos_analisis_directo/italian-wines/etapa1/Italian_Wines_evaluada__Control_maestro.csv | fcb18bba5335 | e80653871de156f0d813dcd8c5b434edda0994afe0ff876d8b449b29c84fc838 | 54758 |

## Salida del modelo (datos, sin acciones ejecutables)

Estado `concluido` · cubo «Vigilar» · acción `esperar` · zona `cumple_regla_k`

| Escenario | Valor por acción | Probabilidad |
|---|---|---|
| malo | 12.47 | 0.2 |
| normal | 25.73 | 0.6 |
| bueno | 46.7 | 0.2 |

| Escalera (k = 3) | Declarado | Recalculado (Anexo C) |
|---|---|---|
| Precio actual | 14.7 | |
| Precio del escenario malo | 12.47 | 12.47 |
| P* | 23.04 | 23.0429 |
| Precio de Sí = mín(P*, V_normal) | 23.04 | 23.0429 |
| Ponderado | 27.27 | 27.272 |
| Crecimiento implícito al precio actual / del normal (%) | — / — | |

| Tasa | Precio de Sí | Ponderado | Zona |
|---|---|---|---|
| 7 % | 31.59 | 37.8 | bajo_malo |
| 8 % | 26.64 | 31.7 | cumple_regla_k |
| 9 % | 23.04 | 27.27 | cumple_regla_k |
| 10 % | 20.3 | 23.91 | cumple_regla_k |
| 11 % | 18.14 | 21.28 | cumple_regla_k |

### Resumen

    Italian Wine Brands embotella y vende vino italiano, sobre todo a supermercados y monopolios fuera de Italia. Cotiza a 14,70 € (cierre del 03/11/2026). Rehago la valoración heredada en un punto concreto: la caja libre base de 20,45 m€ lleva el cupón del 2,5 % de un bono de 130 m€ que vence el 13/05/2027. Con el Bund al 3,33 % y el BTP al 4,47 %, renovar a ese coste no es creíble. Además, la SBC actual (2,26 m€) triplica la media. Con bases de 14, 17 y 19 m€ según el escenario, al 9 % el valor por acción es de 12,47 € (malo), 25,73 € (normal) y 46,70 € (bueno). El ponderado es 27,27 € y el precio de Sí, 23,04 €, así que el precio actual cae en la zona que cumple la regla k = 3. Aun así no compro hoy, por dos razones. La calidad es floja: no hay poder de precio, dos clientes suman el 28 % de las ventas y el capital rinde un 6,6 % después de impuestos. Y la base de caja está sin verificar: la caja libre de los últimos doce meses es 5,79 m€, el CFO del primer semestre de 2026 fue de −12,1 m€ y el bono nuevo se ha anunciado sin importe ni cupón. Cubo Vigilar, acción esperar, hasta conocer el cupón nuevo y la caja libre de 2026 completo.


### Moneda

    EUR


### Justificación

    Estado concluido. La aritmética es robusta a la tasa: entre el 8 % y el 11 % el precio cumple la regla k = 3, y al 7 % queda por debajo del escenario malo. Pero la zona no es la conclusión. No hay foso: los supermercados bajan precios aunque suba el volumen, dos clientes suman el 28 % de las ventas y el ROIC después de impuestos es del 6,6 %. Las ventas caen un 5,3 % en el primer semestre de 2026 y el margen baja del 11,8 % al 10,9 %. Además, el valor depende de una base de caja que hoy no se observa: la caja libre de los últimos doce meses es 5,79 m€ y el CFO del semestre fue de −12,1 m€. Con una base cercana a la de los últimos doce meses, el escenario normal quedaría cerca del precio actual. A eso se suma un bono de 130 m€ que hay que renovar con 59 m€ de caja, con la refinanciación anunciada pero sin cupón conocido. Por eso Vigilar y esperar: los dos datos que deciden (cupón nuevo y caja libre de 2026) se conocerán en meses.


### Probabilidades

    Mantengo 0,2 / 0,6 / 0,2. El riesgo de la refinanciación y de los precios ya está dentro de las bases y los crecimientos de cada escenario; subir además la probabilidad del malo castigaría dos veces lo mismo.


### Fórmula aplicada

    Para P entre 12,47 y 25,73: G(P) = 0,6·(25,73 − P) + 0,2·(46,70 − P) = 24,778 − 0,8P; L(P) = 0,2·(P − 12,47). G = 3L ⇒ 24,778 − 0,8P = 0,6P − 7,482 ⇒ P* = 32,26 / 1,4 = 23,04. Precio de Sí = mín(23,04; 25,73) = 23,04. Ponderado = 0,2·12,47 + 0,6·25,73 + 0,2·46,70 = 27,27. Precio 14,70: está por encima de 12,47 y por debajo de 23,04, así que la zona es cumple_regla_k.


### Crecimiento implícito

    El modelo proyecta caja libre a diez años, no ventas a cinco años: no hay ningún puente ventas-margen-caja que pueda verificar con el paquete. Por eso no doy la cifra en ventas. Como aproximación, el DCF inverso con las hipótesis del escenario normal (base 17 m€, crecimiento terminal 1,5 %, 9 %) da que el precio de 14,70 € descuenta una caída de la caja libre de alrededor del −5,8 % anual durante diez años. Lo obtengo interpolando la tabla auxiliar de la hoja con un valor equivalente de 14,7 × 20,45 / 17 = 17,68 €. El escenario normal supone +2 %. La hoja, con la base de 20,45, da −8,5 %.

### Escenario malo

    Base de caja libre 14 m€, que sale de restar a 20,45: 0,65 por el cupón actual (3,25 frente a la media de 2,60), 1,41 por la SBC de los últimos doce meses (2,26 frente a 0,85) y unos 4,55 por un cupón nuevo de unos 3,5 puntos más (aprox. 6 %; cada punto son unos 1,3 m€ al año). Queda en 13,8, redondeado a 14. Sobre esa base, la caja libre cae un 5 % al año durante diez años, por precios de la GDO a la baja y por el vidrio y la energía al alza; crecimiento terminal del 1 %; descuento al 9 %. Cálculo: 18,217 × 14 / 20,45 = 12,47 € (el modelo es lineal en la base).

### Escenario normal

    Base de caja libre 17 m€, que sale de restar a 20,45: 0,65 por el cupón actual, 1,41 por la SBC de los últimos doce meses y unos 1,3-2,6 por refinanciar a cerca del 4,5 % (en línea con el BTP al 4,47 %). La caja libre crece un 2 % al año durante diez años (volumen algo al alza, precio algo a la baja, margen EBITDA ajustado del 11-12 %); crecimiento terminal del 1,5 %; descuento al 9 %. Cálculo: 30,948 × 17 / 20,45 = 25,73 €. Múltiplo de salida implícito de 13,5 veces la caja libre, frente a una mediana histórica de 7,5 veces.

### Escenario bueno

    Base de caja libre 19 m€: refinanciación barata (aprox. 3,5 %) y SBC algo por encima de la media. La caja libre crece un 8 % al año durante diez años, si funcionan a la vez la GDO italiana, las Top Brands y el ho.re.ca, sin ampliaciones de capital; crecimiento terminal del 2 %; descuento al 9 %. Cálculo: 50,263 × 19 / 20,45 = 46,70 €.

### Sensibilidad (comentarios)

    7 %: Valores: malo 16,05, normal 35,18 y bueno 67,43. El precio queda por debajo del valor del escenario malo.
    8 %: Valores: malo 14,01, normal 29,72 y bueno 55,31.
    9 %: Coincide con la escalera. Valores: malo 12,47, normal 25,73 y bueno 46,70.
    10 %: Valores: malo 11,26, normal 22,67 y bueno 40,28.
    11 %: Valores: malo 10,29, normal 20,26 y bueno 35,32. Incluso al 11 % el precio cumple la regla k.

### Qué haría falsa la conclusión

    - Pasaría hacia Sí si el bono nuevo se coloca por unos 130 m€ a un cupón del 4 % o menos, sin financiar otra adquisición, y la caja libre de 2026 completo vuelve a 17-18 m€ o más sin liberar circulante.
    - Pasaría a Sí solo si además hay pruebas de poder de precio: Top Brands o marcas propias con subidas de precio sostenidas y con peso conocido en el margen.
    - Pasaría a No si el cupón nuevo sale al 6-7 % o más, o si el importe del bono crece para comprar otra empresa.
    - Pasaría a No si la caja libre de 2026 completo queda por debajo de 10 m€ sin un circulante que se vaya a revertir, o si el margen EBITDA ajustado de 2026 baja del 11 % y las ventas vuelven a caer en 2027.
    - Pasaría a Demasiado difícil si la refinanciación no se cierra antes del vencimiento del 13/05/2027, o si el CFO negativo resulta venir de factoring o confirming que no se puede separar del negocio.
    - Pasaría a No si se pierde o se renegocia a la baja uno de los dos grandes clientes (15,5 % y 12,7 % de las ventas).

### Lo que no sabe

    - El importe y el cupón del bono que sustituirá al de 130 m€ al 2,5 %: solo consta que la refinanciación se anunció el 13/10/2026, sin importe ni cupón. Mis bases de 14, 17 y 19 m€ son supuestos sobre ese cupón.
    - Por qué el CFO del primer semestre de 2026 fue de −12,1 m€ (existencias, confirming o factoring) y cuánto hay cedido en factoring pro-soluto.
    - Crecimiento orgánico, precio, volumen y mezcla por canal: la empresa no los publica, y por eso no puedo dar el crecimiento implícito en ventas.
    - Quiénes son los dos grandes clientes, en qué condiciones compran y quiénes son los competidores directos y sus cuotas.
    - El peso de las Top Brands en ventas y margen.
    - Si el pacto parasocial Provinco–Gruppo Pizzolo (23,55 %) se renovó.
    - El efecto fiscal exacto del mayor cupón: uso el dato de 1,3 m€ por punto antes de impuestos como aproximación.
    - La hoja de control cita decisiones del inversor fechadas el 10-nov-2026, después de la fecha de corte. Uso las cifras históricas subyacentes (medias 2021-2025, balance al 30/06/2026), que son anteriores, y la elección de la ventana de cinco años la asumo como mía.
    - El precio es el cierre del 03/11/2026 según fuentes secundarias de mercado. No uso el valor de Simply Wall St ni los precios objetivo de analistas.
    - El número de acciones no es diluido según la IAS 33 (no se encontró); uso 9,275376 M acciones netas de autocartera.

### Citas

    [hoja_control_maestro] «Último cierre 14,70 €.» → Precio actual usado (cierre del 03/11/2026).
    [hoja_analisis] «Aproximación al flujo del accionista si la financiación es razonablemente estable.,20.45» → Base de caja libre de partida, 20,45 m€.
    [hoja_analisis] «Acciones diluidas (mm),Diluted shares outstanding.,9.275376» → Número de acciones usado en el valor por acción.
    [hoja_analisis] «Crecimiento de la caja libre · años 1–10,-0.05,0.02,0.08» → Crecimientos de la caja libre a diez años de cada escenario.
    [hoja_analisis] «Crecimiento para siempre · desde el año 11,0.01,0.015,0.02» → Crecimientos terminales de cada escenario.
    [hoja_analisis] «VALOR INTRÍNSECO POR ACCIÓN,18.2169489444281,30.9480207766151,50.2630936370755» → Valores con base 20,45 que escalo de forma lineal a mis bases de 14, 17 y 19 m€.
    [hoja_control_maestro] «Bono senior 130 m€ nominal, 2,50% fijo, bullet, vto. 13/05/2027 (≈92% de la deuda bruta).» → Cupón barato con vencimiento próximo, que obliga a ajustar la base.
    [hoja_control_maestro] «Cupón del bono pagado en financiación: 3,25 m€/año (2022–25); 0 en 2021. 3 años 3,25; 5 años 2,60; LTM 3,25.» → Ajuste de 0,65 m€ entre el cupón actual y la media que lleva la base.
    [hoja_control_maestro] «Cambiará con la refinanciación de 05/2027 (cada punto de cupón ≈1,3 m€/año antes de impuestos).» → Sensibilidad de la base al cupón nuevo.
    [hoja_control_maestro] «Refinanciación anunciada 13/10/2026 (sin importe ni cupón; secundaria).» → El cupón nuevo es desconocido.
    [hoja_control_maestro] «Bund 10 años (moneda EUR) 3,33%.» → Renovar al 2,5 % no es creíble.
    [hoja_control_maestro] «Riesgo país aparte: BTP 10a 4,47%, spread 114 pb» → Referencia para el cupón de aprox. 4,5 % del escenario normal.
    [hoja_control_maestro] «SBC liquidada en acciones (variación reserva stock grant): 0,42 / 0 / 0,79 / 0,79 / 2,26 (2021–25); media 3 años 1,28; 5 años 0,85; LTM 2,26.» → Ajuste de 1,41 m€ por la SBC actual.
    [hoja_control_maestro] «Neto de SBC: LTM 5,79 (4,3%), FY25 34,52 (25,3%), 3 años 31,05 (22,8%), 5 años 20,45 (15,0%), normalizado 20,6 (15,1%).» → Volatilidad de la caja libre; la de los últimos doce meses es muy baja.
    [hoja_control_maestro] «FCF normalizado (sin circulante, impuestos a devengo) ≈20,6 (3 años).» → La base de 20 m€ es coherente antes de los ajustes de cupón y SBC.
    [hoja_control_maestro] «CFO 2023–25 inflado por liberación de existencias, confirming 13,6 m€ en 2025 e impuestos bajos 2022–24.» → Calidad dudosa de la caja reciente.
    [respuesta] «Por qué el CFO del primer semestre de 2026 fue de -12,1 m€ frente a +15,5 m€ un año antes (H26 p.56)» → CFO negativo sin explicar en el primer semestre de 2026.
    [hoja_control_maestro] «Caja no restringida 59,067 ÷ deuda financiera corriente 134,324 = 0,44x → No.» → Necesidad de refinanciar; no hay exceso de caja.
    [hoja_control_maestro] «Covenant del bono: PFN/EBITDA adj ≤3,5x anual (1,77x); su incumplimiento no es default.» → Apalancamiento moderado: riesgo de coste más que de supervivencia.
    [respuesta] «Dos clientes son el 15,5 % y el 12,7 % de las ventas (A25 p.49).» → Concentración de clientes.
    [respuesta] «la dirección escribe que la atención de los supermercados a sus precios ha bajado los precios aunque el volumen mayorista suba un 3,77 % (A25 p.46)» → Falta de poder de precio.
    [respuesta] «y -5,3 % en el primer semestre de 2026 (H26 p.7)» → Ventas a la baja en 2026.
    [respuesta] «10,9 % en el primer semestre de 2026 frente a 11,8 % (H26 p.7)» → Margen EBITDA ajustado a la baja.
    [hoja_control_maestro] «ROIC después de impuestos (t=28,5% supuesto) 6,6%; sin goodwill 28,8%» → Rentabilidad del capital invertido por debajo del 9 %.
    [hoja_control_maestro] «headroom total 357 m€ (598 un año antes); CGU Giordano Vini headroom solo 0,2 m€.» → Riesgo de deterioro del goodwill.
    [hoja_control_maestro] «Mediana P/FCF al accionista FY2021–25 = 7,5x» → Contraste con el múltiplo terminal implícito de 13,5 veces.
    [hoja_analisis] «Crecimiento que el precio ya da por hecho,DCF inverso: crecimiento de FCF (años 1–10) que haría que el valor fuese igual al precio actual.,-0.0850950092695183» → DCF inverso de la hoja con base 20,45, que sirve de contraste al −5,8 % con base 17.

### Comprobaciones mecánicas y normalizaciones

    {
      "comprobaciones": {
        "escalera_recalculada_anexo_c": {
          "p_estrella": 23.04285714285714,
          "precio_si": 23.04285714285714,
          "ponderado": 27.272000000000002,
          "precio_escenario_malo": 12.47
        },
        "citas_total": 27,
        "citas_literales": 27,
        "avisos": [],
        "nota": "Comprobaciones mecánicas informativas: no acreditan la calidad económica."
      },
      "normalizaciones_enum": []
    }

