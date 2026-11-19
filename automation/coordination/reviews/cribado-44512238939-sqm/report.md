# Cribado · SQM

Estado de la ejecución: `AUDITORIA_DOCUMENTAL_PENDIENTE_ACEPTACION`

Cribado pendiente de revisión humana. No es una recomendación de compra, ni aceptación, ni aptitud para dinero real. Tasa 9 % provisional.

C-ARR (decisión de la persona responsable): los arrendamientos se cuentan una sola vez, en el flujo. El alquiler se resta de la caja libre; la deuda, deuda/EBITDA y deuda/caja libre se miden sin arrendamientos; el pasivo por arrendamientos se muestra aparte, como dato.

Cifras de la etapa 1 tal como las guardó la hoja, a su fecha de análisis; sin las decisiones posteriores (P-O1, P-O2, F1-A/F1-B, D-US1/2, D-WM) ni verificación contra la fuente oficial.

| Campo | Valor |
|---|---|
| Fecha de la hoja | 2026-11-07 |
| Tarea | cribado-44512238939-sqm |
| SHA del código | 833cd50a9bba34006519119c72a29c70a1656fb7 |
| Huella del paquete (package_sha256) | c4786fd755e17b6e75118d5e6ca1104130c35297a57cbd850b962a142fe8e3c7 |
| Huella del envío (bundle_sha256) | 75e9689d572a940060dd150e0bd49f747dd453b5bb9615789114744935b030b7 |
| Huella del encargo | 32b5c7f313e61a61fb0f5e68a75b3c44004eb902e97b98720fb98fa8d383e6cf |
| Huella de la Release | 4d30f7352948fe7e7fe3b133386eabedbddcc71d997e972a1c6db7964d58b0a9 |
| Huella del libro | 84c29cda30484fc58f16df78c1709102952622738811fa369908ce9076f40ccb |
| Modelo pedido / devuelto | claude-opus-5-5 / claude-opus-5-5 |
| Esfuerzo | high |
| Gramática del servidor | True |
| Mensajes enviados | 1 |
| Cota de entrada antes de llamar | 141561 tokens |
| Reserva estimada antes de llamar | USD 1.221604 |
| Uso de tokens | entrada 63712, salida 4639 |
| Coste | CONOCIDO_ESTIMADO; estimado USD 0.347628; cota 0.347628 |

| id | ruta | sha256 | bytes |
|---|---|---|---|
| respuesta | EMPRESAS_LOTES_COMPLETOS/SQM/SQM_respuesta.md | c46913ca1a6a66d24dc6b5cc76effa5dc749292d49afde3eb5231920389505b2 | 39989 |
| hoja_analisis | EMPRESAS_LOTES_COMPLETOS/SQM/SQM_evaluada.xlsx#Análisis | fadc3c63e78a8c1aeb76c9cbd0ccb128bff8c5d1fe93b8cf5373c1405b17510c | 23767 |
| hoja_control_maestro | EMPRESAS_LOTES_COMPLETOS/SQM/SQM_evaluada.xlsx#Control maestro | 3999c6419b248483a33a7740a57ad5bbb5676dec8602ea723d91573d7a7e1bcb | 57133 |

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

    Control maestro!M36 = 97.9 (pasivo por arrendamientos a 30-jun-2026; deuda con arrendamientos de 5.314,3 en Control maestro!N51); fuera del cociente de deuda.


### Tipo de negocio y motor

    Minera y química cíclica de materias primas (litio, yodo, nutrición vegetal y potasio) con el activo principal, el Salar de Atacama, bajo contrato con Corfo y control de Codelco desde 2031.
    Caja libre de ciclo medio normalizada por producto (precio y volumen de litio y yodo) combinada con el valor de la concesión del Salar hasta 2030 y del tramo 2031-2060 con Codelco, sumando por partes yodo, caliche y nutrición vegetal.

### calidad

    Activo singular de litio, yodo y nutrición sin ningún cliente que llegue al 10 % de los ingresos y con ROCE alto (0,261 LTM en pico, mediana de 0,196 en 2016–2025 y 0,12 en FY2025), pero con márgenes que se comprimen (C27), ventas muy cíclicas y un Salar que pasa a control de Codelco desde 2031.
    Dato clave: Análisis!C24 = 0.261

### caja

    La caja libre media de 5 años es positiva (581,4 mm en C52; 581,3 en C40, diferencia de redondeo) y la conversión del beneficio es sana (CFO/beneficio de 1,08 en C26), pero la serie anual va de −1.281,9 (2023) a 3.172,3 (2022), con dos años negativos y un capex medio de 864,4 sin separar el de mantenimiento.
    Dato clave: Análisis!C52 = 581.4

### balance

    Sin arrendamientos, la deuda de 5.216,5 mm (incluye el híbrido de 600), menos la caja de 3.376,8 y los depósitos de 975,9, deja una deuda neta de unos 863,8 mm: unas 0,29x el EBITDA LTM de 3.011,3 neto de unos 29,9 de principal de alquiler, 1,5x la caja libre base, unas 0,79x si se suman como caja comprometida los impuestos (815,6) y las provisiones (662,9), y holgado frente al covenant (0,24 contra 1,00), aun para un negocio cíclico; el 0,12x de la hoja (C33) no sirve tal cual porque suma 97,9 de arrendamientos y excluye el híbrido.
    Dato clave: Análisis!C54 = 5216.5

### precio

    La cotización de 57,52 supera el valor ponderado de 32,83 (C83), el escenario bueno de 53,91 e incluso los 45,73 con r del 7 % (C90), pero la propia hoja marca que el DCF no aplica (C62) y con una base LTM el precio de Sí estimado en la respuesta llegaría a 59,75, así que no se puede concluir sin un valor por caja de ciclo medio y por concesión.
    Dato clave: Análisis!C37 = 57.52

### encaje

    El paquete no trae la cartera; la hoja solo da un tamaño del 0 % (C104), que es decisión de etapa 1 y no se usa aquí.
    Dato clave: Análisis!C104 = 0% · Demasiado difícil (dato de etapa 1, no heredado)

### Qué lo cambiaría

    - Una caja libre de ciclo medio documentada con volúmenes y capex de mantenimiento en torno o por encima de unos 1.225 mm (cerca del 7,5 % de rentabilidad a 57,52) llevaría a estudiar_a_fondo.
    - Unos términos 2031-2060 que dejen al accionista una parte clara y estable de la caja del Salar despejarían la duda de calidad.
    - Un fallo firme del SII por 818,0 + 108,8 mm convertido en caja, o un deterioro del intangible Corfo (2.388), empeoraría el balance y la calidad hacia descartar.

### Qué falta

    - Serie de precios y volúmenes por producto y desglose del capex entre mantenimiento y crecimiento, imprescindibles para la caja de ciclo medio.
    - Reparto de la caja del Salar para el accionista de SQM en 2031-2060 (contrato Corfo y pacto con Codelco) y peso de los minoritarios.
    - Valor contable y clasificación del híbrido de 600 mm, y los resultados del 3T26 (conference call del 18-nov-2026), posteriores a la hoja.

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

