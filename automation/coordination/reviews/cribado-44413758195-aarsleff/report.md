# Cribado · Aarsleff

Estado de la ejecución: `AUDITORIA_DOCUMENTAL_PENDIENTE_ACEPTACION`

Cribado pendiente de revisión humana. No es una recomendación de compra, ni aceptación, ni aptitud para dinero real. Tasa 9 % provisional.

C-ARR (decisión de la persona responsable): los arrendamientos se cuentan una sola vez, en el flujo. El alquiler se resta de la caja libre; la deuda, deuda/EBITDA y deuda/caja libre se miden sin arrendamientos; el pasivo por arrendamientos se muestra aparte, como dato.

Cifras de la etapa 1 tal como las guardó la hoja, a su fecha de análisis; sin las decisiones posteriores (P-O1, P-O2, F1-A/F1-B, D-US1/2, D-WM) ni verificación contra la fuente oficial.

| Campo | Valor |
|---|---|
| Fecha de la hoja | 2026-10-17 |
| Tarea | cribado-44413758195-aarsleff |
| SHA del código | 833cd50a9bba34006519119c72a29c70a1656fb7 |
| Huella del paquete (package_sha256) | 8098463ae5ba286b3e75db5e3564aab4d111e8da110657097cb37f1911b7803f |
| Huella del envío (bundle_sha256) | e08a970adb3355c8cd4136d92383e3aef16304708c70474045694220f108a334 |
| Huella del encargo | 32b5c7f313e61a61fb0f5e68a75b3c44004eb902e97b98720fb98fa8d383e6cf |
| Huella de la Release | 4d30f7352948fe7e7fe3b133386eabedbddcc71d997e972a1c6db7964d58b0a9 |
| Huella del libro | 516524ab0a5627060623ee638214f90615bd24d1c4868ad4fa1209826eb78fb0 |
| Modelo pedido / devuelto | claude-opus-5-5 / claude-opus-5-5 |
| Esfuerzo | high |
| Gramática del servidor | True |
| Mensajes enviados | 1 |
| Cota de entrada antes de llamar | 131631 tokens |
| Reserva estimada antes de llamar | USD 1.181884 |
| Uso de tokens | entrada 59679, salida 4165 |
| Coste | CONOCIDO_ESTIMADO; estimado USD 0.322016; cota 0.322016 |

| id | ruta | sha256 | bytes |
|---|---|---|---|
| respuesta | EMPRESAS_LOTES_COMPLETOS/Aarsleff/Aarsleff_respuesta.md | c9372ed305ae985e74a4d0a19e992ebc90a3a1a331b34e14502b069cb32c2200 | 28330 |
| cambios_v2 | EMPRESAS_LOTES_COMPLETOS/Aarsleff/Aarsleff_cambios_v2.md | 3fa17f251531d2143199d9fdad6d3d87e8f5e5810f9e682d98daf216bc414816 | 5005 |
| hoja_analisis | EMPRESAS_LOTES_COMPLETOS/Aarsleff/Aarsleff_evaluada.xlsx#Análisis | 91a0461aa99df721dcfaa63e2659ddf4f94533624824a55f787962f703edc6d5 | 22827 |
| hoja_control_maestro | EMPRESAS_LOTES_COMPLETOS/Aarsleff/Aarsleff_evaluada.xlsx#Control maestro | f80470ba8e06b0eb72ea0adb22c0675ca848272dafdc44e71a722bd56aeeb054 | 54374 |

## Salida del modelo (datos, sin acciones ejecutables)

Veredicto `vigilar` · DCF de la plantilla aplica: `dudoso`

| Filtro | Resultado |
|---|---|
| calidad | dudoso |
| caja | dudoso |
| balance | pasa |
| precio | no_pasa |
| encaje | no_aplica |

### Pasivo por arrendamientos (dato aparte)

    Control maestro!M51 = 1260 (arrendamientos incluidos en la deuda total de 3.361 mm de Análisis!C54; se excluyen del cociente)


### Tipo de negocio y motor

    Contratista de construcción e infraestructura (cíclico, de licitación, con reconocimiento del beneficio por grado de avance), centrado en Dinamarca y con cinco segmentos
    Caja de ciclo medio: FCF normalizado sin variación de circulante (≈619–648 mm) a lo largo del ciclo constructor, descontado al 9%, en lugar de la media de tres años con circulante dentro.

### calidad

    El negocio se entiende (backlog de 26.408 mm, ROIC del 10–19% durante once años y del 14,0% LTM, por encima del 9%), pero los márgenes EBIT son finos (3,4–5,3%), no hay foso demostrado y existe riesgo de megaproyecto (Fehmarnbelt); discrepo del «DESCARTAR · demasiado difícil» de la hoja, porque su bandera C13 se refiere al precio y no a la comprensión del negocio.
    Dato clave: Análisis!C24 = 0.14

### caja

    La caja libre normalizada es positiva y crece (361→592 en cinco años, 619 LTM), pero la base de la plantilla de 872,7 mm (Análisis!C52) lleva circulante y desfase de impuestos dentro, la media de cinco años es solo 377 mm y el FCF reportado fue negativo en FY20/21–21/22, así que la conversión recurrente no está demostrada.
    Dato clave: Análisis!C40 = 619

### balance

    El 0,64x de la hoja (Análisis!C33) incluye 1.260 mm de arrendamientos en el numerador y un EBITDA NIIF 16, así que no sirve tal cual; sin arrendamientos la deuda bancaria es 2.044 mm frente a 1.903 de caja y valores (≈0,10x), holgado incluso para un cíclico, con dos matices: la caja procede en parte de disposiciones de líneas (+1.218 mm en nueve meses) y la solvencia es del 30,2%, por debajo del objetivo del 35%.
    Dato clave: Control maestro!N51 = Sin arrendamientos: 2.044 (deuda neta sin arrendamientos ≈ 2.044 + 57 − 1.431 − 472 ≈ 198; ≈0,10x EBITDA pre-NIIF 16 aproximado, Control maestro!N36)

### precio

    La cotización de 682 DKK (Análisis!C37) está un 47% por encima del precio de Sí (≈465 DKK, el valor del escenario malo, menor que ¾ del ponderado de 773,7 ≈ 580) y la base de caja de la plantilla está inflada por el circulante (sobre caja normalizada el malo valdría ≈330 DKK y se pagan 20,8x), de modo que el resultado se mantiene aunque la tasa varíe ±2 puntos.
    Dato clave: Análisis!B78 = 464.959504719917

### encaje

    El paquete no trae la cartera de la persona responsable y la hoja no dice nada concreto sobre encaje (capitalización de 12.850 mm), así que este filtro no elimina.
    Dato clave: Análisis!C41 = 12850

### Qué lo cambiaría

    - Cotización en torno a 465 DKK o por debajo (≈330 DKK si se valora sobre caja normalizada) con balance y backlog intactos
    - FCF normalizado de 2025/26 por debajo de los 592 mm de FY24/25, lo que daría dos años de caída
    - Deuda neta sin arrendamientos que suba de forma material por adquisiciones, o pérdida reconocida en Fehmarnbelt

### Qué falta

    - FCF normalizado de 2025/26 (informe anual previsto el 15-dic-2026, posterior a la fecha de la hoja), que es la condición de revisión de C25
    - EBITDA sin NIIF 16 exacto: la hoja solo da un ≈0,10x aproximado para la deuda neta sin arrendamientos
    - Competidores con cuotas y desenlace estimado de Fehmarnbelt ('wide outcome range'), necesarios para juzgar el foso y el riesgo de ejecución

### Comprobaciones mecánicas y normalizaciones

    {
      "comprobaciones": {
        "avisos": [
          "Filtro balance: motivo de más de 400 caracteres."
        ],
        "nota": "Comprobaciones mecánicas informativas: no acreditan la calidad económica."
      },
      "normalizaciones": []
    }

