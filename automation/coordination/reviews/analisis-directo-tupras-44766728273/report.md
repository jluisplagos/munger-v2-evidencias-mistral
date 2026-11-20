# Análisis directo · Tupras, etapa 1 del universo (hoja del 2026-11-01)

Estado de la ejecución: `AUDITORIA_DOCUMENTAL_PENDIENTE_ACEPTACION`

Revisión a ciegas pendiente. No es aceptación, ni integración, ni aptitud para dinero real.

| Campo | Valor |
|---|---|
| Empresa | tupras |
| Fecha de corte | 2026-11-01 |
| Tasa | 9 % |
| Tarea | analisis-directo-tupras-44766728273 |
| SHA del código | 779b55abd380e8427650233fcb8a9c9fa74472f4 |
| Huella del paquete (package_sha256) | 0d89290a3c69fdeef9e68d19b23759032f3cc6b03af4668525779519df434fcf |
| Huella del envío (bundle_sha256) | 953d638888c92d554be01746dde828b3964c306511cb8cb91b482e832284cd15 |
| Huella del encargo | 022846e95b809a772317c2b17d6d946f3f91b9066c864911e473bb7ea15843e4 |
| Modelo pedido / devuelto | claude-opus-5-5 / claude-opus-5-5 |
| Esfuerzo | high |
| Mensajes enviados | 1 |
| Cota de entrada estimada antes de llamar | 133553 tokens |
| Reserva estimada antes de llamar | USD 1.189572 (máximo de la ejecución USD 3) |
| Reserva registrada | USD 1.189572 |
| Uso de tokens | entrada 60117, salida 23196 |
| Coste | CONOCIDO_ESTIMADO; estimado USD 0.704388; cota 0.704388 |

## Paquete de entrada

| id | ruta | commit | sha256 | bytes |
|---|---|---|---|---|
| respuesta | datos_analisis_directo/tupras/etapa1/Tupras_respuesta.md | 779b55abd380 | 84d150767721527dd94b69399f0429bdce22c42749b5d18dcf52cdbed1a4a284 | 29815 |
| hoja_analisis | datos_analisis_directo/tupras/etapa1/Tupras_evaluada__Análisis.csv | 779b55abd380 | c91b625aaca0915256211ad66c96ef89b87ab78a073b42be384b9ddf93d6ce6a | 23040 |
| hoja_guia_simply_wall_st | datos_analisis_directo/tupras/etapa1/Tupras_evaluada__Guía_Simply_Wall_St.csv | 779b55abd380 | 2791cc208d21b779b2104db9848a271eded2ae7cb4392769b743a2d95f8c3e2f | 7794 |
| hoja_opciones | datos_analisis_directo/tupras/etapa1/Tupras_evaluada__Opciones.csv | 779b55abd380 | b9f97b6706b77f7a28f70140d212f0790ee7334eb22965a4f538963e777a1a73 | 1537 |
| hoja_control_maestro | datos_analisis_directo/tupras/etapa1/Tupras_evaluada__Control_maestro.csv | 779b55abd380 | 6f438398f4fae546f498cd037e1a95dd7b38184f21298f3bf0459e8aac5845cc | 50058 |

## Salida del modelo (datos, sin acciones ejecutables)

Estado `concluido` · cubo «Demasiado difícil» · acción `demasiado_dificil` · zona `caro`

| Escenario | Valor por acción | Probabilidad |
|---|---|---|
| malo | 144.02 | 0.2 |
| normal | 306.91 | 0.6 |
| bueno | 522.28 | 0.2 |

| Escalera (k = 3) | Declarado | Recalculado (Anexo C) |
|---|---|---|
| Precio actual | 343.5 | |
| Precio del escenario malo | 144.02 | 144.02 |
| P* | 267.87 | 267.8671 |
| Precio de Sí = mín(P*, V_normal) | 267.87 | 267.8671 |
| Ponderado | 317.41 | 317.406 |
| Crecimiento implícito al precio actual / del normal (%) | 4 / 1 | |

| Tasa | Precio de Sí | Ponderado | Zona |
|---|---|---|---|
| 7 % | 353.01 | 422.33 | cumple_regla_k |
| 8 % | 304.15 | 361.96 | vigilar |
| 9 % | 267.87 | 317.41 | caro |
| 10 % | 239.83 | 283.15 | caro |
| 11 % | 217.51 | 255.98 | caro |

### Resumen

    Tüpraş es un refinador tomador de precios. Tiene el volumen en el techo de unas 30 Mt y su caja libre depende del margen internacional de refino: 7,0 USD/bbl en 2025 y 21,4 en el 2T26. Valoro con una caja libre normalizada a perpetuidad en TL constantes. Los supuestos son 20.500 mm en el malo, 42.000 en el normal y 64.257 en el bueno, con g real de 0 %, 1 % y 2 %, y en los tres sumo 35.000 mm de caja excedente. Paso los valores de TL de junio de 2026 a TL de septiembre con el IPC (+5,6 %). Al 9 % salen 144, 307 y 522 TL. El ponderado es 317 TL y el precio de Sí, 268 TL. A 343,5 TL la zona es «caro». El precio descuenta un crecimiento anual de alrededor del 4 % durante cinco años sobre la caja normal, frente al 1 % de mi escenario normal. El valor depende casi por entero del centro del ciclo del margen, que el paquete no permite acotar: la caja normal puede estar entre unos 20.000 y 64.000 mm y el valor entre 140 y 520 TL. Por eso la conclusión es «demasiado difícil», y en ningún caso hay compra al 9 %.


### Moneda

    TRY (liras turcas; valores en TL constantes llevados a sep-2026)


### Justificación

    El análisis está concluido: los escenarios se pueden calcular y la escalera al 9 % da zona caro. Pero el número que decide el valor, la caja libre de mitad de ciclo, depende del margen internacional de refino, que la empresa no controla. El paquete no da la serie larga de NRM ni de caja en moneda constante que permitiría fijarlo. Según la ventana que se elija, el valor va de unos 140 TL (2024-2025 como norma) a más de 500 TL (FY23-25 como norma), y la valoración de etapa 1 cambia siete veces según la base. Las ventajas de posición (70 % de la capacidad de Türkiye y logística propia) protegen el volumen, no el margen, y los retornos de los años flojos no muestran foso. Por eso el cubo es demasiado difícil y no «no». Aun así, al 9 % el precio supera el ponderado y el valor normal, así que no habría compra en ningún caso.


### Probabilidades

    Mantengo 0,2 / 0,6 / 0,2. El paquete no permite saber si 2024-2025 fue el suelo o el centro del ciclo. Tampoco permite saber si el 2T26 (guerra) cambia el centro. No hay base para mover el peso en ninguna dirección.


### Fórmula aplicada

    Vm = 144,02; Vn = 306,91; Vb = 522,28 (TL de sep-26). Ponderado = 0,2·144,02 + 0,6·306,91 + 0,2·522,28 = 317,41. En el tramo Vm ≤ P ≤ Vn: G = 0,6(306,91−P) + 0,2(522,28−P) y L = 0,2(P−144,02). G = 3L da P* = (0,6·306,91 + 0,2·522,28 + 0,6·144,02)/1,4 = 375,02/1,4 = 267,87. Comprobación en P = Vn: G = 43,07 < 3L = 97,74, así que P* < Vn. Precio de Sí = mín(267,87; 306,91) = 267,87. Como 343,5 > 317,41, la zona es caro.


### Crecimiento implícito

    Uso la caja libre como aproximación de las ventas, con margen constante. Parto de 42.000 mm en el año 1 y busco el crecimiento anual x de los años 1 a 6 (cinco tramos) que, seguido de g = 1 % y descontado al 9 %, más 35.000 de caja, iguala la capitalización de 661.854 mm, que son 626.756 en TL de jun-26 (÷1,056). Con x = 4 % salen 590.916 mm de flujos, frente a los 591.756 necesarios: x ≈ 4,0 %. En un refinador con costes fijos hace falta menos crecimiento de ventas que de caja. Y en TL reales las ventas dependen sobre todo del precio del crudo, así que la cifra es solo orientativa.

### Escenario malo

    El margen se queda en la zona de 2024-2025 (NRM de unos 7 USD/bbl, la guía de febrero de 2026 era de 6-7) y no hay crecimiento real. Caja libre normalizada: 20.500 mm TL de jun-26, media de los unos 19.000 y 22.000 mm reales de 2024 y 2025. g = 0 %. Operación: 20.500/0,09 = 227.778, más 35.000 de caja excedente (la mitad de los 70.130 estimados antes de deuda) = 262.778 mm. Entre 1.926,7956 mm de acciones dan 136,38 TL de jun-26; por 1,056 (IPC jun→sep) quedan 144,02 TL.

### Escenario normal

    El ciclo sigue con un año de bonanza cada cinco, no dos como en FY21-25. La media de FY21-25 es de 61.882 mm e incluye 2022 y 2023, con unos 117.000 y 152.000 mm deducidos de las medias de 3 y 5 años. Los años flojos quedan en unos 20.000 mm. Resultado: una caja libre normalizada de 42.000 mm TL de jun-26, coherente con un NRM medio de ciclo de unos 10-11 USD/bbl, entre los 7 de 2025 y la guía de 13-15 de 2026. Volumen plano en unas 30 Mt y g real del 1 %. Operación: 42.000/0,08 = 525.000, más 35.000 de caja = 560.000 mm, que entre las acciones dan 290,64 TL; por 1,056 quedan 306,91 TL.

### Escenario bueno

    El centro del ciclo es la media FY23-25: CFO 100.798 − capex 23.794 − intereses en financiación 12.526 − arrendamientos 221 = 64.257 mm, más o menos lo que daría la guía de 2026 (NRM 13-15). El propileno y Entek aportan algo y la g real es del 2 %. Operación: 64.257/0,07 = 917.957, más 35.000 de caja = 952.957 mm, que entre las acciones dan 494,58 TL; por 1,056 quedan 522,28 TL.

### Sensibilidad (comentarios)

    7 %: Vm 179,69; Vn 402,82; Vb 723,52. Solo con una tasa real del 7 % el precio cumpliría la regla k = 3, y por poco (353 frente a 343,5).
    8 %: Vm 159,62; Vn 348,02; Vb 606,13. El precio queda entre el precio de Sí y el ponderado.
    9 %: Coincide con la escalera. El precio supera incluso el valor del escenario normal (306,91).
    10 %: Vm 131,53; Vn 274,94; Vb 459,39.
    11 %: Vm 121,32; Vn 249,37; Vb 410,48.

### Qué haría falsa la conclusión

    - Que una serie de 10-15 años de NRM y caja libre en USD o en TL constantes muestre un margen de ciclo propio y estable por encima del de refinerías comparables del Mediterráneo. Eso permitiría fijar el centro del ciclo y pasar a vigilar.
    - Que los resultados de 9M26 y 2027 muestren márgenes de 13-15 USD/bbl o más sin el efecto de la guerra. Eso subiría la caja normal hacia 64.000 mm o más, y el normal se acercaría a 500 TL.
    - Que el NRM vuelva a 6-7 USD/bbl en 2027 mientras siguen el plan verde de USD 8.250 mm y las compras a partes vinculadas. Eso llevaría el cubo a no.
    - Que el precio cayera por debajo de unos 145 TL, el valor del escenario malo. A ese precio no haría falta acertar el ciclo.
    - Que se confirme que la caja excedente real tras deuda es cercana a cero, o muy superior a 35.000 mm. Cambiaría todos los valores en unos ±18 TL por acción.
    - Que la demanda turca de combustibles empiece a caer por la electrificación (17 % de las matriculaciones). El escenario malo tendría que ser aún peor.

### Lo que no sabe

    - No tengo una serie larga de NRM ni de caja libre en moneda constante. Las cifras de 2016-2022 son nominales en TL y no sé deflactarlas con el paquete. No puedo fijar el centro del ciclo.
    - Las cajas libres de 2022, 2023, 2024 y 2025 no vienen año a año. Las de 2024-2025 (unos 19.000 y 22.000) son un cálculo de la respuesta de etapa 1. Las de 2022 y 2023 las deduzco yo de las medias de 3 y 5 años.
    - La hoja de Control maestro contiene decisiones del inversor fechadas el 09-nov-2026, posteriores a la fecha de corte: moneda del DCF en TRY constantes, base FY23-25, ventana de acciones y tasa sin riesgo real del 6,12 %. No las uso como decisiones. Solo uso los datos de partida que ya figuraban antes («Antes: ...»).
    - Los resultados de 9M26 se publican el 06-11-2026, después del corte. No sé si el margen del 2T26 se mantuvo en el 3T26.
    - La caja excedente es incierta: 195.841 mm de caja bruta, 31.256 fuera del estado de flujos, dividendo de 13.000 pagado, +85.141 mm de proveedores que pueden revertir y 68.201 de deuda. Uso 35.000 mm, la mitad de la estimación de 70.130 antes de deuda, como compromiso. No es un dato.
    - Bajo la NIC 29 los intereses pagados (12.526 de media) y cobrados (unos 21.000 en 2025) son nominales y en buena parte compensan inflación. El FCF base resta los pagados y no suma los cobrados, lo que puede infravalorar algo.
    - La conversión de TL de jun-26 a TL de sep-26 (+5,6 %) no llega a octubre. Falta el IPC de octubre.
    - No conozco el precio interior regulado de los combustibles (EMRA), el alcance del veto de la acción del Grupo C ni las condiciones de la deuda (divisa, vencimientos, covenants).
    - No tengo los márgenes de refinerías comparables (STAR, Mediterráneo). Sin ellos no puedo juzgar si hay ventaja de margen o solo de volumen.
    - El crecimiento implícito usa la caja libre como aproximación de las ventas. El paquete no da ventas en TL constantes ni la estructura de costes fijos.

### Citas

    [hoja_control_maestro] «Último cierre BIST: 343,50 TL (vie 30.10.2026; 29.10 festivo).» → Precio actual y su fecha.
    [hoja_control_maestro] «1.926,795598 mm acciones de 1 TL nominal» → Número de acciones para el valor por acción.
    [hoja_control_maestro] «CFO 3a 100.798; 5a 95.090; TTM 175.603 (TL jun-26)» → CFO medio FY23-25, dato de partida del FCF base.
    [hoja_control_maestro] «Capex en caja 3a 23.794; 5a 18.655; TTM 23.430 (TL jun-26).» → Capex medio FY23-25.
    [hoja_control_maestro] «3a 12.526; 5a 14.296; TTM 12.820» → Intereses pagados en financiación (media 3 años).
    [hoja_control_maestro] «3a 221; 5a 257; TTM 278» → Principal de arrendamientos (media 3 años). 100.798 − 23.794 − 12.526 − 221 = 64.257.
    [hoja_control_maestro] «Media 3a 64.256 (≈10 %); 5a 61.882.» → FCF medio de 3 y de 5 años: base del bueno y de la deducción del normal.
    [respuesta] «Con ese margen, la caja libre de 2024 y 2025 fue de unos 19.000 y 22.000 mm TL reales (cálculo mío).» → Base del escenario malo (20.500 mm).
    [respuesta] «7,0 USD/bbl en 2025 y 21,4 en el 2T26» → Amplitud del ciclo del margen de refino.
    [respuesta] «la guía de 2026 pasó de 6-7 a 13-15 en seis meses» → Rango del NRM para los escenarios malo y bueno.
    [hoja_control_maestro] «FCF accionista = CFO 175.603 − capex 23.430 − intereses pagados (financiación) 12.820 − principal leases 278 = 139.075.» → FCF de los últimos doce meses en pico de márgenes (no usado como base).
    [hoja_control_maestro] «→ 70.130 antes de deuda (36,4 TL/acc.)» → Estimación de caja excedente. Uso la mitad, 35.000 mm.
    [hoja_control_maestro] «Caja y equivalentes del balance 195.841.» → Caja bruta a 30-06-2026.
    [hoja_control_maestro] «Borçlanmalar CP 17.579 + porción corriente LP 14.178 + LP 36.443 = 68.201» → Deuda bruta a 30-06-2026.
    [hoja_control_maestro] «precio y capitalización a 30.10.2026 (IPC jun→sep +5,6 %)» → Factor 1,056 para pasar los valores de TL de jun-26 a la base del precio.
    [respuesta] «120.508 en el 1S26 con +85.141 mm de proveedores» → La caja del 1S26 está inflada por el circulante: motivo para no sumar toda la caja.
    [respuesta] «margen bruto 10,5-11,5 % en 2016-2018, 5,5 % en 2019, 2,8 % en 2020, 13,0 % en 2022, 16,0 % en 2023, 8,4 % en 2024, 9,8 % en 2025 y 12,7 % en el 1S26» → Ciclicidad sin tendencia: 2024-2025 cerca de la media del margen bruto.
    [respuesta] «Volumen vendido 2021-2025: 27,6 / 29,5 / 30,1 / 30,4 / 29,4 Mt» → Volumen plano en el techo de capacidad: g real baja.
    [respuesta] «eléctricos cerca del 17 % de las matriculaciones nuevas, la propia empresa sitúa el pico de combustibles fósiles en 2035» → g real de 0 a 2 % a perpetuidad.
    [hoja_analisis] «VALOR INTRÍNSECO POR ACCIÓN,196.715101406204,421.033048779054,607.435157417028» → Valores heredados de la plantilla, tratados como hipótesis y no adoptados.
    [hoja_control_maestro] «Resultados 9M26 el 06.11.2026: actualizar TTM.» → Dato material posterior al corte, no disponible.
    [hoja_control_maestro] «Decisión del inversor (09-nov-2026): DCF en TRY constantes (IAS 29), no USD» → Contenido posterior a la fecha de corte que no uso como decisión.
    [respuesta] «Cuánto de los intereses cobrados (21.000 mm TL en 2025, en financiación)» → Intereses cobrados excluidos del FCF base.

### Comprobaciones mecánicas y normalizaciones

    {
      "comprobaciones": {
        "escalera_recalculada_anexo_c": {
          "p_estrella": 267.8671428571428,
          "precio_si": 267.8671428571428,
          "ponderado": 317.406,
          "precio_escenario_malo": 144.02
        },
        "citas_total": 23,
        "citas_literales": 23,
        "avisos": [],
        "nota": "Comprobaciones mecánicas informativas: no acreditan la calidad económica."
      },
      "normalizaciones_enum": []
    }

