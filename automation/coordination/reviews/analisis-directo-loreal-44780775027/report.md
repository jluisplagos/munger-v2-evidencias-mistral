# Análisis directo · LOreal, etapa 1 del universo (hoja del 2026-10-25)

Estado de la ejecución: `AUDITORIA_DOCUMENTAL_PENDIENTE_ACEPTACION`

Revisión a ciegas pendiente. No es aceptación, ni integración, ni aptitud para dinero real.

| Campo | Valor |
|---|---|
| Empresa | loreal |
| Fecha de corte | 2026-10-25 |
| Tasa | 9 % |
| Tarea | analisis-directo-loreal-44780775027 |
| SHA del código | fcb18bba533554c32f9756d6fb49dc0ebcc2946c |
| Huella del paquete (package_sha256) | 4a53fbc9cab4c4d3f452dbf9577b81bd98bc42125ebd2a7e4aaac22f43dffb2a |
| Huella del envío (bundle_sha256) | 9787533344463d1a7fa7d1d0331591394f2bc55c56b59a5c83e2e2dfb4611059 |
| Huella del encargo | 022846e95b809a772317c2b17d6d946f3f91b9066c864911e473bb7ea15843e4 |
| Modelo pedido / devuelto | claude-opus-5-5 / claude-opus-5-5 |
| Esfuerzo | high |
| Mensajes enviados | 1 |
| Cota de entrada estimada antes de llamar | 156025 tokens |
| Reserva estimada antes de llamar | USD 1.27946 (máximo de la ejecución USD 3) |
| Reserva registrada | USD 1.27946 |
| Uso de tokens | entrada 69675, salida 15992 |
| Coste | CONOCIDO_ESTIMADO; estimado USD 0.59854; cota 0.59854 |

## Paquete de entrada

| id | ruta | commit | sha256 | bytes |
|---|---|---|---|---|
| respuesta | datos_analisis_directo/loreal/etapa1/LOreal_respuesta.md | fcb18bba5335 | 634e431326b16348992311e768fa377d02a4b29eaf36843e70c11dc90dc4e37b | 39840 |
| hoja_analisis | datos_analisis_directo/loreal/etapa1/LOreal_evaluada__Análisis.csv | fcb18bba5335 | eac3b02cb90e18976a8643c26a0604db9be5bf3c6b3f7ca09aed29fa1f1c0ab7 | 24490 |
| hoja_guia_simply_wall_st | datos_analisis_directo/loreal/etapa1/LOreal_evaluada__Guía_Simply_Wall_St.csv | fcb18bba5335 | 2791cc208d21b779b2104db9848a271eded2ae7cb4392769b743a2d95f8c3e2f | 7794 |
| hoja_opciones | datos_analisis_directo/loreal/etapa1/LOreal_evaluada__Opciones.csv | fcb18bba5335 | b9f97b6706b77f7a28f70140d212f0790ee7334eb22965a4f538963e777a1a73 | 1537 |
| hoja_control_maestro | datos_analisis_directo/loreal/etapa1/LOreal_evaluada__Control_maestro.csv | fcb18bba5335 | c803af6abcb56d55ee37b0d5a4cf6c108638a8384ae4daff3e43224d6a52c674 | 60997 |

## Salida del modelo (datos, sin acciones ejecutables)

Estado `concluido` · cubo «Vigilar» · acción `esperar` · zona `caro`

| Escenario | Valor por acción | Probabilidad |
|---|---|---|
| malo | 156.62 | 0.2 |
| normal | 218.99 | 0.6 |
| bueno | 310.13 | 0.2 |

| Escalera (k = 3) | Declarado | Recalculado (Anexo C) |
|---|---|---|
| Precio actual | 436.3 | |
| Precio del escenario malo | 156.62 | 156.62 |
| P* | 205.28 | 205.28 |
| Precio de Sí = mín(P*, V_normal) | 205.28 | 205.28 |
| Ponderado | 224.74 | 224.744 |
| Crecimiento implícito al precio actual / del normal (%) | 23.1 / 6 | |

| Tasa | Precio de Sí | Ponderado | Zona |
|---|---|---|---|
| 7 % | 292.5 | 323.84 | caro |
| 8 % | 241.53 | 265.77 | caro |
| 9 % | 205.28 | 224.74 | caro |
| 10 % | 178.19 | 194.26 | caro |
| 11 % | 157.2 | 170.75 | caro |

### Resumen

    L'Oréal es un negocio de calidad. Tiene un margen operativo que subió del 17,6 % (2016) al 20,2 % (2025), un ROIC estimado del 23,7 % y una deuda neta de 1,15x EBITDA. El precio de 436,30 € (cierre del 23-oct-2026) queda muy por encima de cualquier valor razonable al 9 %. Con un FCF base de 5.969,2 M€ (media FY23-25, neta de arrendamientos y SBC), 535 M de acciones y los escenarios heredados de la etapa 1 (FCF +2 %/+6 %/+10 % diez años; g terminal 1,5/2/2,5 %), los valores son 156,62 / 218,99 / 310,13 €. El ponderado es 224,74 € y el precio de Sí con k = 3 es 205,28 €. Incluso el escenario bueno queda un 29 % por debajo del precio. El resultado aguanta tres cambios: usar el FCF LTM, sumar la participación en Galderma y bajar la tasa al 7 %. El precio exige un crecimiento del FCF de ≈23 % anual durante cinco años, o de ≈15 % durante diez. Cubo Vigilar y acción esperar: el negocio pasa los filtros, el precio no.


### Moneda

    EUR


### Justificación

    Estado concluido: el DCF simplificado es aplicable. El FCF es estable y positivo, la conversión es de 1,29x y los intereses van dentro del CFO. Los datos bastan, y la conclusión no cambia con las incertidumbres abiertas: base LTM, participaciones fuera del modelo, tasa del 7-11 %. Cubo Vigilar: es un buen negocio que entiendo, con foso de marca y escala y balance sólido, pero el precio duplica el precio de Sí (205,28 €). No hay margen ni en el escenario bueno (310 €). Acción esperar: no descarto el negocio, el fallo es de precio. Con el FCF LTM de 6.847,7 M€ el ponderado subiría a ≈258 €, y sumando Galderma (≈17,7 €/acción) a ≈275 €. Sigue siendo caro.


### Probabilidades

    Mantengo las probabilidades de partida: 0,2 / 0,6 / 0,2. El motivo candidato para subir la del escenario malo es el litigio de talco y alisadores en EE. UU., que no tiene provisión. El paquete no lo cuantifica, así que moverla sería inventar. La conclusión no depende de esto: con el 100 % en el escenario bueno el valor seguiría por debajo del precio.


### Fórmula aplicada

    Para V_malo ≤ P ≤ V_normal: G(P) = 0,6·(218,99 − P) + 0,2·(310,13 − P) y L(P) = 0,2·(P − 156,62). G = 3L ⇒ P* = (0,6·218,99 + 0,2·310,13 + 0,6·156,62)/1,4 = (131,39 + 62,03 + 93,97)/1,4 = 205,28. Comprobación: G(205,28) = 29,20 y 3·L = 29,20. Precio de Sí = mín(205,28; 218,99) = 205,28. Ponderado = 0,2·156,62 + 0,6·218,99 + 0,2·310,13 = 224,74. Como 436,30 > 224,74, la zona es caro.


### Crecimiento implícito

    DCF inverso propio. Busco el crecimiento g de los años 1-5 que iguala el valor a 436,30 €, con el resto del escenario normal: 6 % en los años 6-10, 2 % perpetuo, r = 9 %, FCF base 5.969,2 M€ y 535 M de acciones. Resulta g ≈ 23,1 % anual: con 23 % el valor sale ≈434 € y con 23,5 % ≈443 €. Supongo un margen de FCF constante, de modo que crecimiento del FCF = crecimiento de ventas; el paquete no trae un modelo de ventas. Como contraste, la hoja calcula que el precio exige un 15,2 % anual de FCF durante diez años, frente al 6 % del escenario normal y el 10 % del bueno.

### Escenario malo

    El viento de cola se frena: Asia del Norte sigue plana, las compras de 2025-26 no rinden y el litigio de EE. UU. sale en contra. Supuestos: el FCF crece un 2 % nominal en los años 1-10 y un 1,5 % perpetuo, con r = 9 %. Cifras: FCF base 5.969,2 M€ (CFO 8.182,5 − capex 1.541,9 − principal de arrendamientos 452,8 − SBC 218,6), 535 M de acciones y exceso de caja 0. El valor coincide con la celda 78 de la hoja (156,615 €). No incluye ninguna cifra del litigio, porque el paquete no la cuantifica.

### Escenario normal

    El mercado de belleza crece ~4 %, L'Oréal lo bate ligeramente, el margen operativo se mantiene cerca del 20-21 % y el interés de la deuda nueva resta parte de la mejora. Supuestos: el FCF crece un 6 % en los años 1-10 y un 2 % perpetuo, con r = 9 %. El terminal equivale a vender a 14,6x el FCF del año 10, frente a una mediana histórica de 34,6x en años de tipos más bajos. El FCF del año 10 es 10.689,9 M€. El valor coincide con la hoja (218,99 €).

### Escenario bueno

    Los márgenes suben por escala y precio, las compras de 2025-26 (Kering Beauté, licencia de Gucci desde jul-2027) aportan y Asia del Norte se recupera. Supuestos: el FCF crece un 10 % en los años 1-10 y un 2,5 % perpetuo, con r = 9 %. El FCF del año 10 es 15.482,6 M€. El valor coincide con la hoja (310,13 €) y sigue un 29 % por debajo del precio.

### Sensibilidad (comentarios)

    7 %: Malo/normal/bueno = 214,16 / 313,21 / 465,42 €. El ponderado coincide con la hoja (323,84). Ni siquiera al 7 % el precio entra en la zona vigilar.
    8 %: Malo/normal/bueno = 180,95 / 258,16 / 373,41 €. Recálculo propio con la misma fórmula de la hoja.
    9 %: Coincide con la escalera. Malo/normal/bueno = 156,62 / 218,99 / 310,13 €.
    10 %: Malo/normal/bueno = 138,02 / 189,74 / 264,06 €.
    11 %: Malo/normal/bueno = 123,34 / 167,10 / 229,10 €. El ponderado coincide con la hoja (170,75).

### Qué haría falsa la conclusión

    - Que la cotización baje a 205 € o menos con la tesis intacta: margen operativo ≥ 20 % y LFL positivo. Pasaría a cubo Sí.
    - Que el FCF del accionista se consolide claramente por encima de la base: por ejemplo, ≥ 8.500 M€ recurrentes después de SBC y del coste de la deuda nueva. Eso movería todos los escenarios al alza.
    - Que el litigio de talco y alisadores en EE. UU. se cuantifique en miles de millones. Subiría la probabilidad del escenario malo y podría llevar a No.
    - Una caída del margen bruto de más de 150 pb dos años seguidos sin efecto divisa, o un margen operativo de 2026 por debajo del 20 %. Debilitaría el foso y podría llevar a No.
    - Deterioros en Kering Beauté o Galderma, o un ROIC de FY2026 por debajo del 15 % con la definición operativa.
    - Que China y el Travel Retail pasen a decidir el resultado, o que IFRS 18 (2027) deje sin serie de caja comparable. Llevaría a demasiado difícil.

### Lo que no sabe

    - La hoja de Control maestro registra decisiones del inversor fechadas el 28-oct-2026, posteriores a la fecha de corte (25-oct-2026). No las uso como hechos. Adopto la base FCF FY23-25 por criterio propio y contrasto con el LTM.
    - No hay cuantificación ni provisión del litigio de talco (~760 casos) y alisadores (~12.600 casos) en EE. UU. Lo trato como dato ausente.
    - La participación del 20 % en Galderma (9.487,5 M€ de mercado) queda fuera del FCF descontado. La de Sanofi también, aunque sus dividendos ya están en el CFO. Sumar Galderma añadiría ≈17,7 €/acción, pero la deuda que financió su compra y la de Kering Beauté no tiene todavía su coste completo en la base.
    - La base FY23-25 no recoge la aportación de Kering Beauté ni el coste financiero completo de ~10.600 M€ de deuda neta nueva.
    - No hay desglose de precio y volumen, reparto por canal, concentración de clientes ni cuota por categoría. Tampoco un modelo de ventas: el crecimiento implícito de ventas supone un margen de FCF constante.
    - El ROIC es una estimación propia de fase 1; la empresa no lo publica. La serie del mercado de belleza (~4 % anual) es estimación de la propia L'Oréal.
    - El precio procede de fuentes secundarias (Boursorama y otras); Euronext no se pudo leer. La base de la AMF solo estaba indexada hasta el 26-ago-2026.
    - Los escenarios y tasas de crecimiento son juicio heredado de la etapa 1. Los acepto como hipótesis, no como hechos. El precio de Sí de ≈157 € de la respuesta usaba otra regla; con k = 3 sale 205,28 €.
    - IFRS 18, desde 2027, cambiará la definición de CFO y la comparabilidad del FCF.

### Citas

    [hoja_analisis] «Precio actual,Cotización por acción.,436.3» → Precio actual usado: 436,30 €.
    [hoja_control_maestro] «Cierre 23-oct-2026,€/acción» → Fecha del precio.
    [hoja_control_maestro] «Rango 52 semanas 338,85–438,65» → Contexto: el precio está cerca del máximo de 52 semanas.
    [hoja_analisis] «Cash from Operations. Media de 3–5 años.,8182.5» → CFO medio FY23-25.
    [hoja_analisis] «Capital Expenditures. Escríbelo en POSITIVO.,1541.9» → Capex medio.
    [hoja_analisis] «452.8,ℹ se resta del FCF» → Principal de arrendamientos restado.
    [hoja_analisis] «218.6,ℹ se resta del FCF» → SBC restada.
    [hoja_analisis] «razonablemente estable.,5969.2» → FCF base: 8.182,5 − 1.541,9 − 452,8 − 218,6 = 5.969,2 M€.
    [hoja_analisis] «Acciones diluidas (mm),Diluted shares outstanding.,535» → Número de acciones.
    [hoja_analisis] «67,Crecimiento de la caja libre · años 1–10,0.02,0.06,0.1» → Crecimiento del FCF por escenario.
    [hoja_analisis] «68,Crecimiento para siempre · desde el año 11,0.015,0.02,0.025» → g terminal por escenario.
    [hoja_analisis] «69,Probabilidad que le das,0.2,0.6,0.2» → Probabilidades.
    [hoja_analisis] «78,VALOR INTRÍNSECO POR ACCIÓN,156.615030546846,218.99158541868,310.129440388459» → Valores por escenario al 9 %.
    [hoja_analisis] «224.743845438269,—,Solo calcula» → Ponderado al 9 %.
    [hoja_analisis] «Exceso de caja NO operativa que sumas (mm) · opcional,0,0,0» → No se suma caja sobrante.
    [hoja_analisis] «0.152110570566739,✗ BANDERA · > BUENO» → DCF inverso a diez años: 15,2 %.
    [hoja_analisis] «r − 2 pts (7.0%),302.742704479252,323.837021348806» → Control del ponderado al 7 %.
    [hoja_analisis] «r + 2 pts (11.0%),165.970609832619,170.749870556515» → Control del ponderado al 11 %.
    [hoja_analisis] «ℹ 14.6x implícito vs 34.6x histórico» → Múltiplo terminal frente a la historia.
    [hoja_control_maestro] «Contexto: tipos de esos años muy inferiores a los actuales.» → El P/FCF histórico se dio con tipos más bajos.
    [hoja_control_maestro] «Restando SBC (255,7): 6.847,7 → 2,94% (BAJO)» → FCF LTM neto de SBC para la sensibilidad.
    [hoja_control_maestro] «Los intereses pagados (incl. intereses de leases) están DENTRO del CFO» → El FCF ya es del accionista; no se resta deuda.
    [hoja_control_maestro] «la deuda neta pasó de 2.051 (dic-25) a 12.664 (jun-26) por Kering Beauté» → Salto de deuda por M&A, fuera de la base.
    [hoja_control_maestro] «7.023 / 29.665 = 23,7%» → ROIC estimado.
    [respuesta] «el 20% de Galderma (9.487,5 M€ de valor de mercado a 30-jun-2026) y el 7,3% de Sanofi (6.657,4 M€) están fuera del flujo descontado» → Participaciones fuera del DCF.
    [hoja_control_maestro] «dividendos de Sanofi dentro de CFO y del beneficio» → No se suma Sanofi para no contarla dos veces.
    [respuesta] «Unos 760 procedimientos de talco y 11.554 federales más 1.082 estatales de alisadores capilares a 30-jun-2026» → Exposición a litigios en EE. UU.
    [respuesta] «No provisions have been recognized to date» → Litigio sin provisión ni cuantificación.
    [hoja_control_maestro] «Decisión del inversor (28-oct-2026): FCF base con media 3 años FY23-25» → Contenido posterior a la fecha de corte, no usado como hecho.
    [hoja_control_maestro] «IFRS 18 (desde 1-ene-2027) moverá intereses a financiación» → Riesgo de comparabilidad futura del FCF.

### Comprobaciones mecánicas y normalizaciones

    {
      "comprobaciones": {
        "escalera_recalculada_anexo_c": {
          "p_estrella": 205.28000000000003,
          "precio_si": 205.28000000000003,
          "ponderado": 224.744,
          "precio_escenario_malo": 156.62
        },
        "citas_total": 30,
        "citas_literales": 30,
        "avisos": [],
        "nota": "Comprobaciones mecánicas informativas: no acreditan la calidad económica."
      },
      "normalizaciones_enum": []
    }

