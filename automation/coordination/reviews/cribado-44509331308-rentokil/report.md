# Cribado · Rentokil

Estado de la ejecución: `AUDITORIA_DOCUMENTAL_PENDIENTE_ACEPTACION`

Cribado pendiente de revisión humana. No es una recomendación de compra, ni aceptación, ni aptitud para dinero real. Tasa 9 % provisional.

C-ARR (decisión de la persona responsable): los arrendamientos se cuentan una sola vez, en el flujo. El alquiler se resta de la caja libre; la deuda, deuda/EBITDA y deuda/caja libre se miden sin arrendamientos; el pasivo por arrendamientos se muestra aparte, como dato.

Cifras de la etapa 1 tal como las guardó la hoja, a su fecha de análisis; sin las decisiones posteriores (P-O1, P-O2, F1-A/F1-B, D-US1/2, D-WM) ni verificación contra la fuente oficial.

| Campo | Valor |
|---|---|
| Fecha de la hoja | 2026-11-07 |
| Tarea | cribado-44509331308-rentokil |
| SHA del código | 833cd50a9bba34006519119c72a29c70a1656fb7 |
| Huella del paquete (package_sha256) | 6126aaa77f0b4a75d44f6e1410f83e22d5bcb460bfa114fcb94a124756bf2cdd |
| Huella del envío (bundle_sha256) | 43aeefdb2f2b8bc6a403520d092dc2648806a0e9515dcd7acfdc5e1fd7bd9cfb |
| Huella del encargo | 32b5c7f313e61a61fb0f5e68a75b3c44004eb902e97b98720fb98fa8d383e6cf |
| Huella de la Release | 4d30f7352948fe7e7fe3b133386eabedbddcc71d997e972a1c6db7964d58b0a9 |
| Huella del libro | 23274dbad7ea1dadb1782335a623763e01e06ddf06e23aac5fa87146a0c5f2ea |
| Modelo pedido / devuelto | claude-opus-5-5 / claude-opus-5-5 |
| Esfuerzo | high |
| Gramática del servidor | True |
| Mensajes enviados | 1 |
| Cota de entrada antes de llamar | 133418 tokens |
| Reserva estimada antes de llamar | USD 1.189032 |
| Uso de tokens | entrada 60398, salida 4881 |
| Coste | CONOCIDO_ESTIMADO; estimado USD 0.339212; cota 0.339212 |

| id | ruta | sha256 | bytes |
|---|---|---|---|
| respuesta | EMPRESAS_LOTES_COMPLETOS/Rentokil/Rentokil_respuesta.md | 0446a9494143954a81ef0909dfb36da97f6424e82c7bf44a7dcbfeb11ac8b1bb | 31084 |
| hoja_analisis | EMPRESAS_LOTES_COMPLETOS/Rentokil/Rentokil_evaluada.xlsx#Análisis | 4e6ec99beb0d69c780ed871fa49278894f4ad0500dbd85ccd3d70b3d553bea4c | 23167 |
| hoja_control_maestro | EMPRESAS_LOTES_COMPLETOS/Rentokil/Rentokil_evaluada.xlsx#Control maestro | d634122bbe800aeec81c794c74d7c12f2f4401fe2b83ec241fb78cc0aff44655 | 58163 |

## Salida del modelo (datos, sin acciones ejecutables)

Veredicto `vigilar` · DCF de la plantilla aplica: `si`

| Filtro | Resultado |
|---|---|
| calidad | dudoso |
| caja | pasa |
| balance | pasa |
| precio | no_pasa |
| encaje | no_aplica |

### Pasivo por arrendamientos (dato aparte)

    Control maestro!M51 = 543 (pasivos por arrendamiento a 30-jun-2026, fuera del cociente de deuda)


### Tipo de negocio y motor

    Servicios recurrentes a empresas y hogares: control de plagas (83 %) e higiene con rutas de técnicos propios, en reestructuración de Norteamérica tras la compra de Terminix.
    El DCF de caja libre de la plantilla, sobre un FCF del accionista normalizado de costes puntuales y de la cola de pagos de termitas, porque es un servicio recurrente de poca intensidad de capital.

### calidad

    La demanda es recurrente (70 % en contratos anuales) y el negocio se entiende, pero el ROIC del 7,7 % queda por debajo del 9 % tras Terminix (13–15,6 % antes), los márgenes estatutarios caen (11,4 % → 8,5 %) y Norteamérica es un turnaround con CEO nuevo y CFO de salida; coincide con la bandera de moat de la hoja, aunque no basta para descartar la calidad del negocio de plagas en sí.
    Dato clave: Análisis!C24 = 0.077

### caja

    El FCF base, ya neto de arrendamientos y SBC, es positivo (406 M USD; LTM 500, o 467 con la SBC restada) y la serie de continuadas 598/494/615 es recurrente, con CFO/beneficio de 2,15x inflado por amortizaciones de intangibles y one-offs no monetarios.
    Dato clave: Análisis!C52 = 406

### balance

    El 3,05x de Análisis!C33 incluye 543 M USD de arrendamientos; sin ellos la deuda neta es ≈3.032 M USD, que da 3,09x sobre el EBITDA statutory que ya resta el alquiler (2,33x ajustado), aceptable para un negocio 70 % recurrente con BBB, sin covenants, RCF de 1.000 M USD sin disponer y el bono de jun-27 prefinanciado, aunque equivale a ≈7,5 años del FCF base de 406 y existen provisiones de termitas de 392 M USD.
    Dato clave: Control maestro!N36 = 3,09x sin arrendamientos (deuda neta sin arrendamientos ≈ 3.575 − 543 = 3.032 M USD ÷ EBITDA pre-NIIF 16 statutory)

### precio

    A 4,71 USD la cotización coincide con el escenario bueno (4,70) y supera en un 46 % el valor ponderado a r 9 % (3,22) y en más del doble el precio de Sí orientativo de la etapa 1 (≈2,25); solo con r al 7 % el ponderado (4,76) alcanza el precio, y el DCF inverso exige un crecimiento del 10,75 %, por encima del escenario bueno.
    Dato clave: Análisis!C37 = 4.7128 frente a Análisis!C83 = 3.21851741325467

### encaje

    El paquete no trae la cartera de la persona responsable y la hoja solo da datos de la empresa (capitalización de 11.896 M USD), así que el encaje no se juzga.
    Dato clave: Análisis!C41 = 11896

### Qué lo cambiaría

    - Una cotización por debajo del valor ponderado de la hoja (≈3,22 USD) acercaría el precio al rango de estudio a fondo.
    - Un ROIC por encima del 9 % (Análisis!C24) con el orgánico de NA al ritmo de su mercado en FY26 confirmaría la calidad.
    - Otro escalón en la provisión de termitas (como los +201 M USD de 2025) o un deterioro del fondo de comercio de NA rebajaría calidad y balance hacia descartar.

### Qué falta

    - El EBITDA sin arrendamientos (pre-NIIF 16) es una aproximación de la hoja (3,09x / 2,33x), no una cifra publicada; además falta la holgura del test de deterioro del fondo de comercio de NA (5.718 M USD) en 2025.
    - Varias decisiones de Control maestro (C24, C33, C46–C50) están fechadas el 11-nov-2026, después de la fecha de la hoja (07-11-2026): incoherencia de fechas en las fuentes.
    - El precio de Sí (≈2,25 USD) es una estimación de la etapa 1, pendiente de recálculo por el script; no hay dato de FY26 ni del plan de feb-2027.

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

