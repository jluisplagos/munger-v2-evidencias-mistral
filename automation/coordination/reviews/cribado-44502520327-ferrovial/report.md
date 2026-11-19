# Cribado · Ferrovial

Estado de la ejecución: `AUDITORIA_DOCUMENTAL_PENDIENTE_ACEPTACION`

Cribado pendiente de revisión humana. No es una recomendación de compra, ni aceptación, ni aptitud para dinero real. Tasa 9 % provisional.

C-ARR (decisión de la persona responsable): los arrendamientos se cuentan una sola vez, en el flujo. El alquiler se resta de la caja libre; la deuda, deuda/EBITDA y deuda/caja libre se miden sin arrendamientos; el pasivo por arrendamientos se muestra aparte, como dato.

Cifras de la etapa 1 tal como las guardó la hoja, a su fecha de análisis; sin las decisiones posteriores (P-O1, P-O2, F1-A/F1-B, D-US1/2, D-WM) ni verificación contra la fuente oficial.

| Campo | Valor |
|---|---|
| Fecha de la hoja | 2026-10-09 |
| Tarea | cribado-44502520327-ferrovial |
| SHA del código | 833cd50a9bba34006519119c72a29c70a1656fb7 |
| Huella del paquete (package_sha256) | de5f6a626a4ed24ffb99ff439032ca38d6ed57016bf108f35fdeb49aac8d00f0 |
| Huella del envío (bundle_sha256) | d62121a440b2a2d4d01f8cb123aec220185be4600fc786a3c28af45e8d9db4e9 |
| Huella del encargo | 32b5c7f313e61a61fb0f5e68a75b3c44004eb902e97b98720fb98fa8d383e6cf |
| Huella de la Release | 4d30f7352948fe7e7fe3b133386eabedbddcc71d997e972a1c6db7964d58b0a9 |
| Huella del libro | 6368e33355b6342c7e3cf39f07173dcbc3e5d50e7c0030ffbcd51cdfa49bccae |
| Modelo pedido / devuelto | claude-opus-5-5 / claude-opus-5-5 |
| Esfuerzo | high |
| Gramática del servidor | True |
| Mensajes enviados | 1 |
| Cota de entrada antes de llamar | 134362 tokens |
| Reserva estimada antes de llamar | USD 1.192808 |
| Uso de tokens | entrada 60729, salida 4937 |
| Coste | CONOCIDO_ESTIMADO; estimado USD 0.341656; cota 0.341656 |

| id | ruta | sha256 | bytes |
|---|---|---|---|
| respuesta | EMPRESAS_LOTES_COMPLETOS/Ferrovial/Ferrovial_respuesta.md | a6551713c239be6b3ff5bbe845f5c8322ff176dccbe3346478aef9b5a6c9c6f4 | 32690 |
| cambios_v2 | EMPRESAS_LOTES_COMPLETOS/Ferrovial/Ferrovial_cambios_v2.md | 979645756e856bd9d2e88f415d1a519191c9f6ac02d6b378fb09f204289f9510 | 3516 |
| hoja_analisis | EMPRESAS_LOTES_COMPLETOS/Ferrovial/Ferrovial_evaluada.xlsx#Análisis | c583ea02d3a81f59200353d8296ec8d360486ba1425e4d29225f6daba6e6a0e5 | 23534 |
| hoja_control_maestro | EMPRESAS_LOTES_COMPLETOS/Ferrovial/Ferrovial_evaluada.xlsx#Control maestro | c603a058e9df991c957c67c1628dc48be3a2129ef488f2f6c4cc44323dcc135a | 53605 |

## Salida del modelo (datos, sin acciones ejecutables)

Veredicto `faltan_datos` · DCF de la plantilla aplica: `no`

| Filtro | Resultado |
|---|---|
| calidad | dudoso |
| caja | dudoso |
| balance | pasa |
| precio | dudoso |
| encaje | no_aplica |

### Pasivo por arrendamientos (dato aparte)

    Control maestro!M51 = 333 (arrendamientos incluidos en la deuda total de Análisis!C54 = 10657; deuda financiera bruta sin arrendamientos 10.324)


### Tipo de negocio y motor

    Grupo de concesiones de infraestructuras de transporte (autopistas de peaje, sobre todo en EE. UU. y Canadá, y aeropuertos) con deuda sin recurso por proyecto, más una constructora grande de margen fino.
    Suma de partes: valor de cada concesión (407 ETR, carriles gestionados de Texas, I-66, I-77, NTO…) descontando sus flujos al accionista hasta el vencimiento, neto de su deuda sin recurso y de minoritarios, más la constructora a un múltiplo de caja de ciclo medio y la caja neta ex-infra.

### calidad

    Las autopistas muestran ventaja visible: aportan el 68 % del EBITDA ajustado con margen del 72–73 % y tarifa dinámica. Pero el ROCE consolidado antes de impuestos es del 8,7 % (≈7 % después, por debajo del 9 %) y el 79 % de los ingresos viene de una constructora de margen fino (−365 mm de EBIT en 2019); por eso no doy por buenos sin más los ✓ de moat de C18.
    Dato clave: Análisis!C24 = 0.087

### caja

    El FCF base de 440,3 mm (media 2023–2025, con 339/313/697 mm por año) es positivo pero irregular, y la conversión de 0,91 (C26) está en el umbral. Además, los 367–444 mm anuales de dividendos a minoritarios y las compras de participaciones que no resta lo reducen a un rendimiento de 0,2–1,0 % (Control maestro!N40); discrepo del ✓ PASA de C25.
    Dato clave: Análisis!C52 = 440.3

### balance

    Sin arrendamientos, la deuda neta consolidada de 6.283 mm sobre un EBITDA que ya resta el alquiler (≈1.548 − 104 ≈ 1.444 mm) da ≈4,35x (la hoja da ≈4,39x pre-NIIF 16 en Control maestro!N36). Ese nivel es tolerable para concesiones estables porque 7.591 mm son deuda de proyectos sin recurso, a 18 años y 98,7 % a tipo fijo, y el perímetro con recurso tiene caja neta de 1.307 mm; discrepo de la BANDERA de Análisis!C33 = 4,27, que además incluye arrendamientos.
    Dato clave: Control maestro!M36 = 6283 (deuda neta consolidada APM sin arrendamientos; con ellos 6.616)

### precio

    A 44,3 € la cotización está muy por encima del ponderado de 13,40 € de la hoja y exige un crecimiento del 23,6 % anual (C86); ni a r = 7 % pasa de 19,4 € (C90), y no hay precio de Sí. Como el DCF de la plantilla no aplica (C62) y la propia hoja apunta a participaciones infravaloradas (407 ETR implícita en ≈11.905 mm frente a 1.725 contables), haría falta una suma de partes por concesión para concluir.
    Dato clave: Análisis!C83 = 13.3996281841387 (frente a Análisis!C37 = 44.3)

### encaje

    El paquete no trae la cartera de la persona responsable y la hoja solo da contexto ajeno a ella, como el 30,2 % de insiders; este filtro no elimina.
    Dato clave: Análisis!C96 = 0.302 (participación de insiders, no es dato de cartera)

### Qué lo cambiaría

    - Una suma de partes con datos por concesión que dé un valor por acción por encima de la cotización de 44,3 €, o una cotización claramente por debajo del límite inferior de esa suma de partes.
    - Una caja libre después de minoritarios y de compras de participaciones que se mantenga positiva y creciente, con un rendimiento sobre la capitalización de 31.909 mm por encima del 3 %.
    - La vuelta de construcción a pérdidas (como los −365 mm de EBIT de 2019) o el paso de caja neta ex-infra (1.307 mm) a deuda neta con recurso, lo que llevaría a descartar.

### Qué falta

    - Cuadro por concesión: plazo, régimen tarifario, deuda sin recurso, calendario de amortización y política de reparto; sin él no se aplica el motor adecuado ni se juzga el precio.
    - Caja libre atribuible al accionista tras dividendos a minoritarios (367–444 mm al año) y tras compras de participaciones y capital en proyectos en equivalencia, como serie homogénea de varios años.
    - Retornos previstos frente a reales de las concesiones compradas o ganadas (I-66, I-77, 5,06 % de la 407 ETR, NTO), para medir la calidad del capital reinvertido.

### Comprobaciones mecánicas y normalizaciones

    {
      "comprobaciones": {
        "avisos": [
          "Filtro balance: motivo de más de 400 caracteres.",
          "Filtro precio: motivo de más de 400 caracteres."
        ],
        "nota": "Comprobaciones mecánicas informativas: no acreditan la calidad económica."
      },
      "normalizaciones": []
    }

