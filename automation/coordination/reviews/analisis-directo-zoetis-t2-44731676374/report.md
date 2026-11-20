# Análisis directo · Zoetis, ejercicio 2025 y 2026 hasta el tercer trimestre (segundo tiempo)

Estado de la ejecución: `AUDITORIA_DOCUMENTAL_PENDIENTE_ACEPTACION`

Revisión a ciegas pendiente. No es aceptación, ni integración, ni aptitud para dinero real.

| Campo | Valor |
|---|---|
| Empresa | zoetis-t2 |
| Fecha de corte | 2026-11-05 |
| Tasa | 9 % |
| Tarea | analisis-directo-zoetis-t2-44731676374 |
| SHA del código | 779b55abd380e8427650233fcb8a9c9fa74472f4 |
| Huella del paquete (package_sha256) | 93552e31f53d70275f818ef87831a3a4b7fa23f3080a33528a09f8bca038d20e |
| Huella del envío (bundle_sha256) | 2c95f54b83ff012a2df419b203333badb694c782ae75a47b0c105f63471a7ad6 |
| Huella del encargo | 022846e95b809a772317c2b17d6d946f3f91b9066c864911e473bb7ea15843e4 |
| Modelo pedido / devuelto | claude-opus-5-5 / claude-opus-5-5 |
| Esfuerzo | high |
| Mensajes enviados | 1 |
| Cota de entrada estimada antes de llamar | 955377 tokens |
| Reserva estimada antes de llamar | USD 4.476868 (máximo de la ejecución USD 4.5) |
| Reserva registrada | USD 4.476868 |
| Uso de tokens | entrada 380348, salida 19523 |
| Coste | CONOCIDO_ESTIMADO; estimado USD 1.911852; cota 1.911852 |

## Paquete de entrada

| id | ruta | commit | sha256 | bytes |
|---|---|---|---|---|
| datos_v63_md | datos_analisis_directo/zoetis-t2/datos_v63.md | 779b55abd380 | 783c6e76b606a14b0856b862740ede5618304e939cb5afc14be7e4ff577cd06c | 91450 |
| etapa1_zoetis_analisis_csv | datos_analisis_directo/zoetis-t2/etapa1/Zoetis_evaluada__Análisis.csv | 779b55abd380 | e3f11ef73fe1173ad2f75e2acac92a2ff1347e6bf4c59eccbd6baf9e2ad2dbe5 | 22479 |
| etapa1_zoetis_control_maestro_csv | datos_analisis_directo/zoetis-t2/etapa1/Zoetis_evaluada__Control_maestro.csv | 779b55abd380 | abe7634d14078440a7d9a1315d56f657a2d5d0e42b5f1557082899d92fede723 | 51137 |
| etapa1_zoetis_guia_sws_csv | datos_analisis_directo/zoetis-t2/etapa1/Zoetis_evaluada__Guía_Simply_Wall_St.csv | 779b55abd380 | e3cabea03c1a776ed1203ce43f216ec3b29760e8c866e2b925b8990e31152651 | 7660 |
| etapa1_zoetis_opciones_csv | datos_analisis_directo/zoetis-t2/etapa1/Zoetis_evaluada__Opciones.csv | 779b55abd380 | 56246fb2e5ca7ca826b3c07c4786422bb1cf9c5a3a0d110abc53919735356a4d | 1486 |
| etapa1_zoetis_respuesta_md | datos_analisis_directo/zoetis-t2/etapa1/Zoetis_respuesta.md | 779b55abd380 | d5f62442438d0f130ed4a758fedebaafaef9e87a5fb021ec20e7c6219ac79a24 | 27829 |
| extracto_v63_md | datos_analisis_directo/zoetis-t2/extracto_v63.md | 779b55abd380 | 20b72dce714538a94d065cc86005b98d4f11d1ce7415667fcc00a24fbf4cc27d | 30378 |
| fase1_v63_json | datos_analisis_directo/zoetis-t2/fase1_v63.json | 779b55abd380 | 1958cab7e67c22a681a7eefa242174879872df25de6a329a463f4e19d49571be | 67059 |
| fuentes_10k_2025_seleccion | datos_analisis_directo/zoetis-t2/fuentes/zoetis-10k-fy2025.seleccion.compacto.txt | 779b55abd380 | 4cf5ba16a3760a8e3da48e06044d9dc4ce7a199f50f3c8c13a467152463d8704 | 331099 |
| fuentes_10q_2026_q2_estados | datos_analisis_directo/zoetis-t2/fuentes/zoetis-10q-2026-q2.estados.compacto.txt | 779b55abd380 | b7700801e9945aecd6a5116957e8f79366e4bfa2e2ebb9f8d5bcfb0c5fe242fe | 14055 |
| fuentes_10q_2026_q3_seleccion | datos_analisis_directo/zoetis-t2/fuentes/zoetis-10q-2026-q3.seleccion.compacto.txt | 779b55abd380 | 46c684ec831ef75e63364ccf3bee7c6eff29ccfcc72e1777b52201449c52d65f | 186563 |
| fuentes_3t_2026_comunicado | datos_analisis_directo/zoetis-t2/fuentes/zoetis-3q2026-press-release.texto.txt | 779b55abd380 | bf257c2bffc808951c7c7c02791b6716668e34d74f47c692b96220290d2fefda | 44703 |
| fuentes_3t_2026_presentacion | datos_analisis_directo/zoetis-t2/fuentes/zoetis-3q2026-financial-results.compacto.txt | 779b55abd380 | cf2c3e481f354bd282adabad704a5f6dec4a5b5ab3de4293e84837396ad3c8cd | 27987 |
| fuentes_cotizacion_5nov | datos_analisis_directo/zoetis-t2/fuentes/cotizacion_ZTS_hasta_2026-11-05.txt | 779b55abd380 | 78408bd849f2950fe816f6e17fceb39c3d2b54ff2dd075b3139ba0e852ad486f | 947 |

## Salida del modelo (datos, sin acciones ejecutables)

Estado `concluido` · cubo «Vigilar» · acción `esperar` · zona `caro`

| Escenario | Valor por acción | Probabilidad |
|---|---|---|
| malo | 46.61 | 0.3 |
| normal | 86.64 | 0.5 |
| bueno | 114.39 | 0.2 |

| Escalera (k = 3) | Declarado | Recalculado (Anexo C) |
|---|---|---|
| Precio actual | 82.11 | |
| Precio del escenario malo | 46.61 | 46.61 |
| P* | 67.59 | 67.5919 |
| Precio de Sí = mín(P*, V_normal) | 67.59 | 67.5919 |
| Ponderado | 80.18 | 80.181 |
| Crecimiento implícito al precio actual / del normal (%) | 3.3 / 4 | |

| Tasa | Precio de Sí | Ponderado | Zona |
|---|---|---|---|
| 7 % | 95.53 | 116.42 | cumple_regla_k |
| 8 % | 79.11 | 94.97 | vigilar |
| 9 % | 67.59 | 80.18 | caro |
| 10 % | 59.05 | 69.36 | caro |
| 11 % | 52.46 | 61.11 | caro |

### Resumen

    Zoetis sigue siendo un negocio muy rentable, pero el tercer trimestre de 2026 confirma lo que la etapa 1 dejaba sin explicar. Los ingresos de animal de compañía en EE. UU. caen un 8 % en el trimestre y un 10 % en nueve meses. Dermatología cae un 16 % orgánico. La propia empresa lo atribuye a demanda más débil, competencia más dura, sensibilidad al precio y genéricos. La cuota de dermatología en EE. UU. ha bajado 7 puntos en el segundo trimestre y 4 en el tercero, y el precio neto cayó un 1 % en el trimestre. La guía de 2026 prevé ingresos orgánicos de −2 % a −1 % y beneficio ajustado de −7 % a −5 %. Con un FCF base de 1.994 mm y 406,3 millones de acciones, los escenarios valen 46,6 (malo), 86,6 (normal) y 114,4 (bueno) USD al 9 %. El ponderado, con probabilidades 0,3/0,5/0,2, es 80,2 USD. El precio de Sí por la regla k = 3 es 67,6 USD. A 82,11 USD el precio queda en zona cara: cubo Vigilar, acción esperar.


### Moneda

    USD


### Justificación

    Estado concluido: la causa de la caída de 2026, que era la duda central de la etapa 1, ya está explicada por el 10-Q del tercer trimestre (competencia en dermatología, precio, genéricos, Librela) y el escenario malo la acota con un −3 % anual durante diez años.
    Cubo Vigilar y no Sí: a 82,11 USD el precio supera el ponderado (80,18) y queda un 21 % por encima del precio de Sí (67,59).
    No paso a No porque el negocio sigue generando unos 2.000 mm de FCF, ganado, diagnóstico e Internacional crecen, la pérdida de cuota en dermatología se frena y la dirección recompra ahora a unos 75 USD.
    Acción: esperar a un precio de ≈ 67,6 USD o a pruebas de estabilización que justifiquen mejores escenarios.


### Probabilidades

    Cambio de 0,2/0,6/0,2 a 0,3/0,5/0,2. La propia etapa 1 fijó ese disparador: subir el malo a 0,3 si el 10-Q del tercer trimestre atribuía la caída a pérdida de cuota en compañía, y bajar el normal a 0,5 si subía el malo. El 10-Q y la presentación del 5-nov-2026 lo confirman: competencia más dura en dermatología, pérdida de cuota de 7 y 4 puntos en el segundo y tercer trimestre, precio neto −1 % en el trimestre y genéricos de Convenia y Cerenia. No subo más el malo porque la pérdida de cuota se frena (de 7 a 4 puntos), Simparica Trio mantiene el liderazgo con un 23 % de cuota en clínicas y ganado, diagnóstico e Internacional crecen.


### Fórmula aplicada

    V = (46,61; 86,64; 114,39), p = (0,3; 0,5; 0,2).
    Para 46,61 ≤ P ≤ 86,64: G(P) = 0,5·(86,64 − P) + 0,2·(114,39 − P) = 66,20 − 0,7P; L(P) = 0,3·(P − 46,61) = 0,3P − 13,98.
    G = 3L ⇒ 66,20 − 0,7P = 0,9P − 41,95 ⇒ P* = 108,15 / 1,6 = 67,59.
    Precio de Sí = mín(67,59; 86,64) = 67,59.
    Ponderado = 0,3·46,61 + 0,5·86,64 + 0,2·114,39 = 80,18.
    Precio 82,11 > 80,18 ⇒ caro.


### Crecimiento implícito

    El modelo proyecta el FCF, no las ventas. Supongo márgenes estables, de modo que el crecimiento de las ventas es igual al del FCF. Tampoco proyecta a cinco años sino a diez, que es el horizonte del escenario normal.
    Con el resto de supuestos del normal (base 1.994 mm, crecimiento perpetuo 2,5 %, r = 9 %, 406,316 millones de acciones), al 3 % anual el valor es 80,35 USD y al 3,5 % es 83,43 USD. Interpolando, 82,11 USD equivale a ≈ 3,3 % anual, frente al 4 % del escenario normal.
    No es exactamente la métrica pedida (ventas a cinco años): es una aproximación.

### Escenario malo

    La erosión de las franquicias de compañía continúa: la cuota de dermatología sigue cayendo, Simparica Trio sufre presión de precio, Librela sigue bajando y hay genéricos de Convenia y Cerenia, con el precedente de Draxxin (−66 % en EE. UU.).
    Supuestos: FCF base 1.994 mm (C52; media 2023–25 de CFO − capex − SBC − arrendamientos financieros), que cae un 3 % anual durante 10 años, crecimiento perpetuo del 1 % y r = 9 %.
    Cálculo: valor presente de los años 1–10 = 11.097 mm; terminal = 1.470,4 × 1,01 / 0,08, descontado al año 10 = 7.842 mm; total 18.939 mm ÷ 406,316 millones de acciones (portada del 10-Q del tercer trimestre) = 46,61 USD.
    Es más duro que el −2 % de la etapa 1 porque el tercer trimestre ya muestra precio neto negativo y pérdida de cuota.

### Escenario normal

    2026 es un año de caída: guía de ingresos orgánicos de −2 % a −1 % y beneficio ajustado de −7 % a −5 %. Después, las defensas comerciales y los lanzamientos (Cytopoint de larga duración, Simparica Duo, Lenivia y Portela) estabilizan compañía, y ganado y diagnóstico siguen creciendo.
    Supuestos: FCF base 1.994 mm, que crece un 4 % anual durante 10 años (la etapa 1 ponía 5 %; la misma etapa 1 preveía 0,04 si el 10-Q del tercer trimestre explicaba la caída como estructural), crecimiento perpetuo del 2,5 % y r = 9 %.
    Cálculo: valor presente de los años 1–10 = 15.542 mm; terminal = 2.951,6 × 1,025 / 0,065, descontado = 19.661 mm; total 35.203 mm ÷ 406,316 = 86,64 USD.
    La base de 1.994 mm está por debajo del FCF de los últimos doce meses, unos 2.135 mm (CFO ≈ 2.728 − capex ≈ 493 − SBC ≈ 100, mezclando bases).

### Escenario bueno

    El pipeline repite lo que hicieron dermatología y parasiticidas: aprobaciones adelantadas, enfermedad renal crónica, oncología y anticuerpos de larga duración. Compañía vuelve a crecer y la cuota de dermatología se estabiliza.
    Supuestos: FCF base 1.994 mm, que crece un 7 % anual durante 10 años (por debajo del 8 % de la etapa 1, porque se parte de un año de caída), crecimiento perpetuo del 3 % y r = 9 %.
    Cálculo: valor presente de los años 1–10 = 18.035 mm; terminal = 3.922,5 × 1,03 / 0,06, descontado = 28.444 mm; total 46.478 mm ÷ 406,316 = 114,39 USD.

### Sensibilidad (comentarios)

    7 %: Valores 60,73 / 126,22 / 175,44 USD. P* = (63,11 + 35,09 + 0,9·60,73) / 1,6 = 95,53. Solo con una tasa del 7 % el precio cumple la regla.
    8 %: Valores 52,68 / 102,82 / 138,76 USD. P* = 79,11, apenas un 4 % por debajo del precio.
    9 %: Caso base; coincide con la escalera.
    10 %: Valores 41,86 / 74,79 / 97,05 USD. La hoja avisa de que la r mínima sería del 10,8 %.
    11 %: Valores 38,04 / 65,75 / 84,10 USD.

### Qué haría falsa la conclusión

    - A No: que la cuota de dermatología en EE. UU. siga cayendo a 4 puntos o más por trimestre en 2027 (≈ 80 % hoy), o que el ingreso de compañía en EE. UU. vuelva a caer en 2027.
    - A No: fechas de pérdida de exclusividad de Simparica Trio o Apoquel anteriores a 2030 con caída tipo Draxxin, o pérdida del liderazgo de Simparica Trio (≈ 23 % de cuota en clínicas).
    - A No: FCF de 2026 claramente por debajo de ≈ 1.800 mm, o recompras financiadas con deuda que lleven la deuda neta/EBITDA hacia 3x.
    - A No o demasiado difícil: que la demanda colectiva de valores (sobre la demanda y la cuota de Librela, Simparica Trio, Apoquel y Cytopoint) revele ocultación de información, o que el IRS gane la reclamación de ≈ 450 mm más intereses.
    - A Sí: precio por debajo de ≈ 67,6 USD sin deterioro adicional de los fundamentales.
    - A Sí con precio de Sí más alto: estabilización de la cuota de dermatología, aprobación y buena acogida de Cytopoint de larga duración y Simparica Duo, y compañía en EE. UU. con crecimiento orgánico positivo en 2027.

### Lo que no sabe

    - Fechas de pérdida de exclusividad de Simparica Trio, Apoquel, Cytopoint y Librela: no figuran en el paquete.
    - Ventas en dólares de cada producto: solo hay franquicias en la presentación del tercer trimestre. Tampoco sé quiénes son los nuevos competidores en dermatología ni su cuota.
    - FCF de los últimos doce meses: es aproximado (≈ 2.135–2.180 mm), porque mezcla el ejercicio 2025 publicado (sin reexpresar por la alineación del año fiscal) con nueve meses de 2025 reexpresados. No hay cuarto trimestre de 2025 reexpresado.
    - Acciones: uso 406,316 millones (30-oct-2026), no los 424,928 de la hoja (31-dic-2025). Con estos últimos, todos los valores bajarían ≈ 4,4 %.
    - Las recompras de 2026 se pagaron en parte con caja (de 2.450 a 1.333 + 200 mm), lo que reduce algo los ingresos por intereses. El FCF base no lo ajusta.
    - Deuda: el modelo no la resta (FCF después de intereses; convención de la plantilla) y supone que se refinancia siempre. El bono de 750 mm pasa a corriente (septiembre de 2027).
    - Litigios: el desenlace de la demanda colectiva de valores y de las demandas derivadas, y el de la reclamación del IRS (≈ 450 mm sin intereses), son desconocidos.
    - La prueba anual de deterioro del fondo de comercio no se detalla. Solo consta el deterioro de 78 mm de activos de I+D en curso de PetMedix.
    - Fechas posteriores al corte: datos_v63 y fase1_v63 contienen notas de método fechadas el 18-nov-2026, y la cotización se transcribió el 18-nov-2026. No uso ningún hecho posterior al 5-nov-2026. La fila del 4-nov (89,2 USD) no se ha podido contrastar.
    - Los porcentajes de crecimiento de cada escenario son juicio propio sobre la base de la etapa 1 (hipótesis heredada, no hecho). La propiedad y las operaciones de los directivos (proxy, pág. 92) siguen sin leer.
    - El crecimiento implícito se calcula sobre el FCF a diez años, no sobre las ventas a cinco años, porque el modelo no proyecta ventas ni márgenes por separado.

### Citas

    [fuentes_cotizacion_5nov] «Precio de cierre de ZTS en NYSE el 5-nov-2026: $82.11» → Precio actual
    [fuentes_10q_2026_q3_seleccion] «As of October 30, 2026, there were 406,316,147 shares of common stock outstanding.» → Acciones usadas en el valor por acción
    [datos_v63_md] «FCF base (C52, fórmula): 1994» → FCF base de los escenarios
    [fuentes_10k_2025_seleccion] «Net cash provided by operating activities 2,904 2,953 2,353» → CFO 2023–2025 de la base
    [fuentes_10k_2025_seleccion] «Capital expenditures (621) (655) (732)» → Capex 2023–2025 de la base
    [fuentes_10k_2025_seleccion] «Share-based compensation expense 83 74 60» → SBC restada en la base
    [fuentes_10q_2026_q3_seleccion] «Net cash provided by operating activities 1,880 2,056» → CFO de nueve meses de 2026 frente a 2025 (cálculo del FCF de los últimos doce meses)
    [fuentes_10q_2026_q3_seleccion] «Capital expenditures (334) (462)» → Capex de nueve meses de 2026 frente a 2025
    [fuentes_3t_2026_comunicado] «Narrowed revenue to a range of $9.220 billion to $9.320 billion (organic operational growth of (2)% to (1)%)» → Guía de ingresos de 2026: año de caída
    [fuentes_3t_2026_comunicado] «Raised adjusted net income to a range of $2.600 billion to $2.640 billion (organic operational growth of (7)% to (5)%)» → Caída del beneficio ajustado en 2026
    [fuentes_10q_2026_q3_seleccion] «Companion animal revenue decreased primarily due to softer end-market demand and an increasingly competitive landscape.» → Causa de la caída: competencia y demanda
    [fuentes_10q_2026_q3_seleccion] «price decrease driven by lower net price realization of approximately 1%» → Precio neto negativo en el trimestre (escenario malo más duro)
    [fuentes_3t_2026_presentacion] «Promotional defense slowed U.S. Dermatology share loss to 4pp1 in Q3» → Pérdida de cuota en dermatología, que se frena
    [fuentes_3t_2026_presentacion] «Key Dermatology $396 $469 (16)% —% —% (16)%» → Dermatología −16 % en el tercer trimestre
    [fuentes_3t_2026_presentacion] «Simparica Trio maintained its market-leading position in the U.S. with» → Simparica Trio mantiene el liderazgo (limita el malo)
    [fuentes_3t_2026_presentacion] «Long-acting Cytopoint is expected to receive U.S. approval in Q4» → Lanzamientos del escenario bueno y normal
    [datos_v63_md] «Lo sustituiría: 0,3 si el 10-Q 3T26 atribuye la caída a pérdida de cuota en compañía.» → Disparador heredado para subir la probabilidad del malo
    [etapa1_zoetis_analisis_csv] «Crecimiento de la caja libre · años 1–10,-0.02,0.05,0.08» → Crecimientos de partida de la etapa 1
    [fuentes_10q_2026_q3_seleccion] «6,685,325 $74.77 6,679,545 $770,134,979» → Recompras del tercer trimestre a ≈ 74,8 USD y autorización restante
    [fuentes_10q_2026_q3_seleccion] «Current portion of long-term debt $ 750 $ —» → Bono de 750 mm ya a corto plazo
    [fuentes_10q_2026_q3_seleccion] «Cash and cash equivalents(b) $ 1,333 $ 2,450» → Caída de la caja por las recompras
    [fuentes_10q_2026_q3_seleccion] «On May 27, 2026, a securities class action complaint was filed in federal court in New York against the company» → Riesgo de litigio
    [fuentes_10q_2026_q3_seleccion] «is approximately $450 million, excluding interest and penalties» → Reclamación del IRS
    [fuentes_10q_2026_q3_seleccion] «we recorded impairment charges on in-process research and development assets, acquired from PetMedix in 2023» → Deterioro del pipeline adquirido
    [fuentes_10k_2025_seleccion] «these five products and product lines contributed approximately 42% of our revenue» → Concentración en cinco productos
    [extracto_v63_md] «Draxxin: ventas en EE. UU. bajaron un 66% desde 2021, primer año de genérico» → Precedente del escenario malo
    [extracto_v63_md] «Fechas de pérdida de exclusividad de Simparica Trio, Apoquel, Cytopoint y Librela.» → Dato ausente clave

### Comprobaciones mecánicas y normalizaciones

    {
      "comprobaciones": {
        "escalera_recalculada_anexo_c": {
          "p_estrella": 67.59187500000002,
          "precio_si": 67.59187500000002,
          "ponderado": 80.181,
          "precio_escenario_malo": 46.61
        },
        "citas_total": 27,
        "citas_literales": 27,
        "avisos": [],
        "nota": "Comprobaciones mecánicas informativas: no acreditan la calidad económica."
      },
      "normalizaciones_enum": []
    }

