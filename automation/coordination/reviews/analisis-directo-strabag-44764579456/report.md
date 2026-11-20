# Análisis directo · Strabag, etapa 1 del universo (hoja del 2026-10-11)

Estado de la ejecución: `AUDITORIA_DOCUMENTAL_PENDIENTE_ACEPTACION`

Revisión a ciegas pendiente. No es aceptación, ni integración, ni aptitud para dinero real.

| Campo | Valor |
|---|---|
| Empresa | strabag |
| Fecha de corte | 2026-10-11 |
| Tasa | 9 % |
| Tarea | analisis-directo-strabag-44764579456 |
| SHA del código | 779b55abd380e8427650233fcb8a9c9fa74472f4 |
| Huella del paquete (package_sha256) | 1457f94e65237e5842a356f31748ddbd0d22657c5744c3b9a03453bdabac96e2 |
| Huella del envío (bundle_sha256) | 0966006d8ef3687e4bef3be6912ad9081fa4adb015c762686e487492def21980 |
| Huella del encargo | 022846e95b809a772317c2b17d6d946f3f91b9066c864911e473bb7ea15843e4 |
| Modelo pedido / devuelto | claude-opus-5-5 / claude-opus-5-5 |
| Esfuerzo | high |
| Mensajes enviados | 1 |
| Cota de entrada estimada antes de llamar | 143122 tokens |
| Reserva estimada antes de llamar | USD 1.227848 (máximo de la ejecución USD 3) |
| Reserva registrada | USD 1.227848 |
| Uso de tokens | entrada 64891, salida 17069 |
| Coste | CONOCIDO_ESTIMADO; estimado USD 0.600944; cota 0.600944 |

## Paquete de entrada

| id | ruta | commit | sha256 | bytes |
|---|---|---|---|---|
| respuesta | datos_analisis_directo/strabag/etapa1/Strabag_respuesta.md | 779b55abd380 | 81f37127f5d7cfbce2fe1e1afe30df44875957272560d78fa84c988766296c1a | 32624 |
| hoja_analisis | datos_analisis_directo/strabag/etapa1/Strabag_evaluada__Análisis.csv | 779b55abd380 | fc70dfabfda8b26e4b051d5467e07a3ba5e74b6f410e882cb41e9f509dbdf387 | 23064 |
| hoja_guia_simply_wall_st | datos_analisis_directo/strabag/etapa1/Strabag_evaluada__Guía_Simply_Wall_St.csv | 779b55abd380 | 2791cc208d21b779b2104db9848a271eded2ae7cb4392769b743a2d95f8c3e2f | 7794 |
| hoja_opciones | datos_analisis_directo/strabag/etapa1/Strabag_evaluada__Opciones.csv | 779b55abd380 | b9f97b6706b77f7a28f70140d212f0790ee7334eb22965a4f538963e777a1a73 | 1537 |
| hoja_control_maestro | datos_analisis_directo/strabag/etapa1/Strabag_evaluada__Control_maestro.csv | 779b55abd380 | ecee37c13bfa156d344efb9b4ebad1420a65b0cf45ecdbfe5a06e633399c0667 | 56474 |

## Salida del modelo (datos, sin acciones ejecutables)

Estado `concluido` · cubo «Vigilar» · acción `esperar` · zona `cumple_regla_k`

| Escenario | Valor por acción | Probabilidad |
|---|---|---|
| malo | 70.35 | 0.2 |
| normal | 124.06 | 0.6 |
| bueno | 203.4 | 0.2 |

| Escalera (k = 3) | Declarado | Recalculado (Anexo C) |
|---|---|---|
| Precio actual | 102.2 | |
| Precio del escenario malo | 70.35 | 70.35 |
| P* | 112.38 | 112.3757 |
| Precio de Sí = mín(P*, V_normal) | 112.38 | 112.3757 |
| Ponderado | 129.19 | 129.186 |
| Crecimiento implícito al precio actual / del normal (%) | -0.63 / 2 | |

| Tasa | Precio de Sí | Ponderado | Zona |
|---|---|---|---|
| 7 % | 156.44 | 182.82 | cumple_regla_k |
| 8 % | 130.74 | 151.42 | cumple_regla_k |
| 9 % | 112.38 | 129.19 | cumple_regla_k |
| 10 % | 98.6 | 112.63 | vigilar |
| 11 % | 87.87 | 99.81 | caro |

### Resumen

    STRABAG es un contratista de infraestructura con caja neta y cartera récord de 35.985 mn, sin foso visible y con el margen EBIT en máximos (6,7 % en 2025). Calculo una caja libre base de 982,9 mn, que sale de la media de 2023–2025: CFO 1.668,8 − capex 616,8 − principal de arrendamientos 69,1. Adopto como propios los tres escenarios de la hoja heredada, con crecimientos de −5 %, 2 % y 8 % durante diez años y terminales de 1 %, 2 % y 2,5 %. Al 9 % dan 70,35, 124,06 y 203,40 € por acción, con un ponderado de 129,19 € y un P* de 112,38 €. A 102,2 € el precio cae en la zona que cumple la regla k = 3, pero con poco colchón (≈9 %). Esa zona desaparece al 10 % (pasa a vigilar) y al 11 % (pasa a caro). La caja libre base lleva circulante de anticipos y el margen es de récord. Hay además litigios sin acotar del todo (Rasperia, daños del cártel, Chile) y ventas del núcleo accionarial. Por eso el cubo es Vigilar y la acción, esperar.


### Moneda

    EUR


### Justificación

    Doy el análisis por concluido: las cifras bastan para una escalera y los riesgos abiertos se pueden acotar en orden de magnitud. Por ejemplo, los litigios de Rasperia citados suman ≈1.416 mn, unos 12 € por acción, como máximo. Al 9 % el precio cumple la regla k = 3, pero el colchón es pequeño (112,38 frente a 102,2) y frágil por cuatro motivos. Primero, el escenario normal parte de una caja libre que incluye circulante de anticipos y un margen de récord. Segundo, con una tasa del 10 % la regla deja de cumplirse. Tercero, no hay foso: cuotas del 2–6 % y ROCE del 4,1–7,6 % en 2015–2020. Cuarto, quedan pasivos contingentes sin importe y el núcleo accionarial ha vendido. No es un No porque el precio está cerca de la zona de compra y el balance es sólido. Vigilar y esperar a un precio con más margen, o a pruebas de que el margen aguanta.


### Probabilidades

    Mantengo las probabilidades de partida 0,2 / 0,6 / 0,2. El riesgo del margen récord ya está recogido en el crecimiento negativo del escenario malo; subir también su probabilidad lo castigaría dos veces.


### Fórmula aplicada

    Ponderado = 0,2·70,35 + 0,6·124,06 + 0,2·203,40 = 129,19.
    Para 70,35 ≤ P ≤ 124,06:
    G(P) = 0,6·(124,06−P) + 0,2·(203,40−P) = 115,12 − 0,8P
    L(P) = 0,2·(P−70,35)
    G = 3L ⇒ 115,12 − 0,8P = 0,6P − 42,21 ⇒ P* = 157,33/1,4 = 112,38.
    Precio de Sí = mín(112,38; 124,06) = 112,38.
    Precio 102,2 > 70,35 y ≤ 112,38 ⇒ cumple_regla_k.


### Crecimiento implícito

    DCF inverso con las demás hipótesis del escenario normal (base de 982,9 mn, terminal del 2 %, tasa del 9 %), interpolando la tabla auxiliar de la hoja: −1 % da 99,48 € y −0,5 % da 103,19 €, así que 102,2 € corresponde a ≈−0,63 % anual. Es crecimiento de la caja libre durante 10 años, no de las ventas a 5 años. Lo uso como aproximación suponiendo conversión constante; no hay serie de ventas en el paquete para hacerlo a cinco años.

### Escenario malo

    El margen vuelve hacia el 4 % (nivel de 2018–2020 y antigua meta de la dirección) y los anticipos se devuelven. La caja libre cae un 5 % anual durante 10 años, de 982,9 a ≈588 mn en el año 10, y después crece al 1 % a perpetuidad. Descuento al 9 % sobre 115,44 M de acciones; no se suma caja ni se resta deuda, porque el flujo ya es del accionista. No incluye pérdidas por litigios.

### Escenario normal

    La cartera récord se ejecuta y el margen cede desde el 6,7 % hacia la guía de 5,5–6 %. La caja libre base de 982,9 mn crece un 2 % anual durante 10 años (≈1.198 mn en el año 10) y un 2 % a perpetuidad, descontada al 9 %. La base incluye ≈228–290 mn anuales de circulante y ≈100 mn de intereses cobrados. Lo compenso no sumando la caja neta: 3.430 mn de caja, de los que 497,6 mn se deben a Rasperia; el exceso estimado va de 0 a 21,3 € por acción. Contraste propio: una base sin circulante de ≈800 mn creciendo un 4 % daría ≈117 €.

### Escenario bueno

    El fondo alemán y los concursos de ferrocarril, energía y agua llegan a obra durante años y el margen se queda en el 6–7 %. La caja libre crece un 8 % anual durante 10 años (≈2.122 mn en el año 10) y un 2,5 % a perpetuidad, descontada al 9 %.

### Sensibilidad (comentarios)

    7 %: Valores: malo 90,51, normal 173,69, bueno 302,49. P* = 156,44.
    8 %: Valores: malo 79,04, normal 144,74, bueno 243,82. P* = 130,74.
    9 %: Coincide con la escalera; colchón de ≈9 % sobre el precio.
    10 %: Valores: malo 63,53, normal 108,56, bueno 173,93. El precio supera el precio de Sí.
    11 %: Valores: malo 58,03, normal 96,50, bueno 151,53. El precio supera el ponderado.

### Qué haría falsa la conclusión

    - Margen EBIT de 2026 por debajo de la guía de 5,5–6 %, o una media trienal de la caja libre antes de circulante inferior a 700 mn: bajaría el escenario normal y llevaría el cubo a No.
    - Que la demanda de 326 mn o la medida con daños fijos de 1.090 mn en Kaliningrado vayan contra STRABAG y sean ejecutables fuera de Rusia, o que las reclamaciones por el cártel o las provisiones de Chile resulten materiales: pasaría a No o a Demasiado difícil.
    - Un margen igual o superior al 5,5 % en un año de mercado de construcción a la baja (sobre todo en North + West): sería prueba de foso y podría llevar el cubo a Sí.
    - Una caída del precio hacia 90 € o menos con las cifras intactas: colchón amplio frente al precio de Sí incluso al 10 %; reconsideraría Sí.
    - Que la empresa confirme una caja sobrante grande (≥1.000 mn) neta de flotante y de lo debido a Rasperia y la devuelva a los accionistas: subiría el valor unos 9 € o más por acción.
    - Nuevos deterioros en adquisiciones recientes (como los 50 mn de WTE) o nuevas emisiones de acciones: pasaría a No.

### Lo que no sabe

    - El paquete contiene información posterior a la fecha de corte (2026-10-11): la nota «v1 · revisada el 25-oct-2026» y la «Decisión del inversor (19-oct-2026)» sobre el periodo de la base. No la uso. La base de 982,9 mn la recalculo yo con las medias 2023–2025 de CFO, capex y arrendamientos que constan en la hoja. Los valores de la hoja que reproduzco podrían estar guardados después del corte, aunque la nota dice que no hubo cambios de valor.
    - El paquete no trae serie de ventas utilizable para un DCF inverso de ventas a 5 años. Uso el crecimiento de la caja libre a 10 años como aproximación.
    - No sé qué parte de la caja de 3.430 mn es flotante de clientes y qué parte es sobrante. El exceso estimado va de 0 a 21,3 € por acción y no lo sumo.
    - La caja operativa incluye 97–132 mn anuales de intereses cobrados y ≈228–290 mn anuales de circulante. No sé cuánto de eso es recurrente.
    - Desconozco contra quién van las demandas de Rasperia (326 mn y 1.090 mn), el importe de las reclamaciones de clientes por el cártel y las provisiones de Chile.
    - No conozco a los competidores ni las pujas, así que no puedo juzgar si el alza de margen de 2021–2025 es estructural o cíclica.
    - No conozco los motivos de las ventas del núcleo accionarial, que vendió a 76–86,7 €, por debajo del precio actual.
    - Las cifras de 2026 proceden de un semestral sin auditar. El precio es el cierre del 9-oct-2026 según una sola anotación de la hoja.
    - Los escenarios y sus valores proceden de la hoja heredada. Los he recalculado y los asumo, pero son juicio y no hechos.

### Citas

    [hoja_control_maestro] «Último cierre del mercado principal: 102,20 €.» → Precio actual.
    [hoja_control_maestro] «Cierre 9-oct-2026,EUR/acción» → Fecha del precio.
    [hoja_analisis] «Caja de las operaciones (mm),Cash from Operations. Media de 3–5 años.,1668.8» → CFO medio que entra en la base.
    [hoja_analisis] «Capex: inversión en activos (mm),Capital Expenditures. Escríbelo en POSITIVO.,616.8» → Capex medio que entra en la base.
    [hoja_analisis] «69.09999999999999,ℹ se resta del FCF» → Principal de arrendamientos restado de la base.
    [hoja_analisis] «982.9,✓ PASA» → Caja libre base: 1.668,8 − 616,8 − 69,1 = 982,9.
    [hoja_analisis] «Acciones diluidas (mm),Diluted shares outstanding.,115.442696» → Número de acciones.
    [hoja_analisis] «67,Crecimiento de la caja libre · años 1–10,-0.05,0.02,0.08» → Crecimientos de los años 1–10 en cada escenario.
    [hoja_analisis] «68,Crecimiento para siempre · desde el año 11,0.01,0.02,0.025» → Crecimientos terminales.
    [hoja_analisis] «78,VALOR INTRÍNSECO POR ACCIÓN,70.3488054230952,124.063779165874,203.402507157046» → Valores al 9 % que he recalculado.
    [hoja_analisis] «-0.00633767935616624» → Crecimiento implícito en el precio.
    [hoja_analisis] «r − 2 pts (7.0%),171.49925708311,182.812493181269» → Contraste del ponderado al 7 % (182,81).
    [hoja_control_maestro] «Evidencia: margen EBIT 3,8/4,3/5,9/4,2/5,0/6,1/6,7% (2019–25), LTM 6,5%» → Margen en máximos de la serie.
    [respuesta] «Guía 2026: 5,5–6 % (SAR2026 p. 7)» → Guía de margen de la dirección.
    [hoja_control_maestro] «Circulante aporta +228/año (media 3a) y +480 LTM.» → La base lleva circulante.
    [respuesta] «el CFO medio 2023–2025 (1.669 mn) supera beneficio más amortización (unos 1.380 mn) en unos 290 mn al año (cálculo)» → Flotante dentro del CFO.
    [hoja_control_maestro] «antes de circulante LTM 877,8 (7,4%); media 3a 982,8 (8,3%); media 5a 754,3 (6,4%)» → Bases alternativas de caja libre.
    [hoja_control_maestro] «Intereses cobrados en CFO 97–132 mm/año 2023–25.» → Intereses de la caja incluidos en el CFO.
    [hoja_control_maestro] «Caja y equivalentes en balance 3.430,2 (incluye 0,15 pignorada).» → Caja de balance.
    [hoja_control_maestro] «Comprometida: 497,6 adeudados a Rasperia» → Caja comprometida con Rasperia.
    [hoja_control_maestro] «Rangos estimados de exceso: 0 / ~959 / ~1.781 / ~2.460 mm = 0 / 8,3 / 15,4 / 21,3 €/acc. (115,44 M acc.).» → Rango del exceso de caja no sumado.
    [respuesta] «nueva demanda de 326 mn y una solicitud de medida con daños fijos de 1.090 mn» → Litigios de Rasperia sin acotar del todo.
    [respuesta] «STRABAG aceptó el 11.3.2026 subir en 100,63 mn la multa del cártel austriaco de 45,37 mn y perdió su estatus de clemencia» → Riesgo de integridad y de litigios.
    [respuesta] «Cuotas del 2,0 % en Alemania, 5,6 % en Austria, 2,2 % en Polonia y 3,3 % en Rep. Checa» → Sin foso por cuota.
    [respuesta] «ROCE entre 4,1 % y 7,6 % en 2015–2020» → Rentabilidad histórica baja.
    [respuesta] «cartera de 35.985 mn a 30.6.2026 (+27 % interanual)» → Apoyo de volumen en los escenarios normal y bueno.
    [hoja_control_maestro] «Fundación Haselsteiner 2,5 M a 76,00 € el 14-oct-25; Raiffeisen-Holding NÖ-Wien 2,08 M a 86,50 € el 19-feb-26; UNIQA 2,36 M a 86,70 € el 17-abr-26» → Ventas del núcleo accionarial.
    [respuesta] «v1 · revisada el 25-oct-2026» → Información posterior al corte, no usada.
    [hoja_control_maestro] «Decisión del inversor (19-oct-2026)» → Decisión posterior al corte; recalculo la base por mi cuenta.

### Comprobaciones mecánicas y normalizaciones

    {
      "comprobaciones": {
        "escalera_recalculada_anexo_c": {
          "p_estrella": 112.37571428571427,
          "precio_si": 112.37571428571427,
          "ponderado": 129.186,
          "precio_escenario_malo": 70.35
        },
        "citas_total": 29,
        "citas_literales": 29,
        "avisos": [],
        "nota": "Comprobaciones mecánicas informativas: no acreditan la calidad económica."
      },
      "normalizaciones_enum": []
    }

