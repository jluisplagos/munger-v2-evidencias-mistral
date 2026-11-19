# Cribado · LOreal

Estado de la ejecución: `AUDITORIA_DOCUMENTAL_PENDIENTE_ACEPTACION`

Cribado pendiente de revisión humana. No es una recomendación de compra, ni aceptación, ni aptitud para dinero real. Tasa 9 % provisional.

C-ARR (decisión de la persona responsable): los arrendamientos se cuentan una sola vez, en el flujo. El alquiler se resta de la caja libre; la deuda, deuda/EBITDA y deuda/caja libre se miden sin arrendamientos; el pasivo por arrendamientos se muestra aparte, como dato.

Cifras de la etapa 1 tal como las guardó la hoja, a su fecha de análisis; sin las decisiones posteriores (P-O1, P-O2, F1-A/F1-B, D-US1/2, D-WM) ni verificación contra la fuente oficial.

| Campo | Valor |
|---|---|
| Fecha de la hoja | 2026-10-25 |
| Tarea | cribado-44505954250-loreal |
| SHA del código | 833cd50a9bba34006519119c72a29c70a1656fb7 |
| Huella del paquete (package_sha256) | 68fb5dc3027b005198cdc2b3ac129cf55314a34aa06f7a055e2e8bba10aa8368 |
| Huella del envío (bundle_sha256) | 5be0c00c99211ecf0ac793f3ab73d170a20e14f23d8e2db2cc9354964d7228c7 |
| Huella del encargo | 32b5c7f313e61a61fb0f5e68a75b3c44004eb902e97b98720fb98fa8d383e6cf |
| Huella de la Release | 4d30f7352948fe7e7fe3b133386eabedbddcc71d997e972a1c6db7964d58b0a9 |
| Huella del libro | d234bba25757ad4ef572fab91ed8eaa8920df27c8b31cd0d19c03567ede19b49 |
| Modelo pedido / devuelto | claude-opus-5-5 / claude-opus-5-5 |
| Esfuerzo | high |
| Gramática del servidor | True |
| Mensajes enviados | 1 |
| Cota de entrada antes de llamar | 146057 tokens |
| Reserva estimada antes de llamar | USD 1.239588 |
| Uso de tokens | entrada 65642, salida 3572 |
| Coste | CONOCIDO_ESTIMADO; estimado USD 0.334008; cota 0.334008 |

| id | ruta | sha256 | bytes |
|---|---|---|---|
| respuesta | EMPRESAS_LOTES_COMPLETOS/LOreal/LOreal_respuesta.md | 634e431326b16348992311e768fa377d02a4b29eaf36843e70c11dc90dc4e37b | 39840 |
| hoja_analisis | EMPRESAS_LOTES_COMPLETOS/LOreal/LOreal_evaluada.xlsx#Análisis | eac3b02cb90e18976a8643c26a0604db9be5bf3c6b3f7ca09aed29fa1f1c0ab7 | 24490 |
| hoja_control_maestro | EMPRESAS_LOTES_COMPLETOS/LOreal/LOreal_evaluada.xlsx#Control maestro | c803af6abcb56d55ee37b0d5a4cf6c108638a8384ae4daff3e43224d6a52c674 | 60997 |

## Salida del modelo (datos, sin acciones ejecutables)

Veredicto `vigilar` · DCF de la plantilla aplica: `si`

| Filtro | Resultado |
|---|---|
| calidad | pasa |
| caja | pasa |
| balance | pasa |
| precio | no_pasa |
| encaje | no_aplica |

### Pasivo por arrendamientos (dato aparte)

    ≈2.375,3 M€ = Control maestro!M51 deuda bruta con arrendamientos 16.712,6 − sin arrendamientos 14.337,3 (dato derivado; la hoja no da el pasivo en una celda propia).


### Tipo de negocio y motor

    Consumo de marca estable: cosmética y belleza (4 divisiones, 150 países), con poco capital y un margen bruto alto
    El DCF de caja libre de la plantilla para un negocio de consumo estable, sumando aparte las participaciones fuera del flujo (20% de Galderma, 7,3% de Sanofi) como suma de partes.

### calidad

    Es un negocio de marcas de consumo que se entiende, con un ROIC estimado del 23,7% (no publicado por la empresa) y un margen operativo que se expande (17,6% → 20,2%); discrepo del «DESCARTAR · demasiado difícil» de Análisis!A6, que viene del precio (C13, C20) y no de que el negocio no se entienda (C11 y C12 = Sí).
    Dato clave: Análisis!C24 = 0.237

### caja

    La caja libre base normalizada es de 5.969,2 M€ (CFO 8.182,5 − capex 1.541,9 − arrendamientos 452,8 − SBC 218,6), con una conversión de 1,29x el beneficio (Análisis!C26) y un capex bajo; la serie de caja libre al accionista sube de 4.606 a 7.103 M€ LTM.
    Dato clave: Análisis!C52 = 5969.2

### balance

    El 1,15x de Análisis!C33 incluye arrendamientos y no sirve tal cual: recalculado sin ellos, la deuda neta queda en ≈10.288,5 M€ (14.337,3 − 4.048,8), ≈1,0x un EBITDA que ya resta el alquiler (10.996,2 − ≈439,4 de principal; el interés de los arrendamientos no consta) y ≈1,7x la caja libre base de 5.969,2. Es holgado para un negocio de consumo tan estable, aunque la caja no cubre los vencimientos corrientes (0,83x) y se apoya en 7.000 M€ de líneas no dispuestas.
    Dato clave: Control maestro!M51 = 14337.3 (deuda bruta sin arrendamientos; menos caja Análisis!C53 = 4048.8 → deuda neta sin arrendamientos ≈ 10288.5)

### precio

    A 436,3 € (Análisis!C37), la cotización está muy por encima del valor ponderado de 224,7 €, del escenario bueno de 310,1 € (D78) y del precio de Sí ≈156,6 € (escenario malo, B78); incluso con r del 7% el ponderado es 323,8 € (C90), y el precio implica un crecimiento del 15,2% (C86). Las participaciones en Galderma y Sanofi (≈30 €/acción según la respuesta) no cierran la brecha.
    Dato clave: Análisis!C83 = 224.743845438269

### encaje

    El paquete no trae la cartera y la hoja no dice nada concreto de encaje, más allá de clasificarla como Compounder con un ROIC de 0,237, así que este filtro no se evalúa y no elimina.
    Dato clave: Análisis!C14 = Compounder

### Qué lo cambiaría

    - Una cotización por debajo del valor ponderado de ≈225 € (y en el entorno del precio de Sí de ≈157 €) con la tesis intacta pasaría el filtro de precio y llevaría a estudiar_a_fondo.
    - Un ROIC del perímetro completo de FY2026 por debajo del 15% o un deterioro relevante de Kering Beauté o Galderma pondrían en cuestión la calidad.
    - Una cuantificación grande del litigio de EE. UU. o una deuda neta sin arrendamientos por encima de ~2,5x el EBITDA después del alquiler harían fallar el balance.

### Qué falta

    - Interés pagado por arrendamientos en los últimos doce meses, para calcular exactamente el EBITDA después del alquiler (la hoja solo da el principal, 439,4–452,8 M€).
    - Exposición cuantificada a los litigios de talco y alisadores en EE. UU.: no hay provisión ni rango en el paquete.
    - Coherencia de fechas: el Control maestro registra decisiones del inversor del 28-oct-2026, posteriores a la fecha de la hoja (25-oct-2026); además, la caja libre base no recoge el coste completo de la deuda nueva del M&A de 2025-26.

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

