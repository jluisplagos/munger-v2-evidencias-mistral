# Cribado · Azkoyen

Estado de la ejecución: `AUDITORIA_DOCUMENTAL_PENDIENTE_ACEPTACION`

Cribado pendiente de revisión humana. No es una recomendación de compra, ni aceptación, ni aptitud para dinero real. Tasa 9 % provisional.

C-ARR (decisión de la persona responsable): los arrendamientos se cuentan una sola vez, en el flujo. El alquiler se resta de la caja libre; la deuda, deuda/EBITDA y deuda/caja libre se miden sin arrendamientos; el pasivo por arrendamientos se muestra aparte, como dato.

Cifras de la etapa 1 tal como las guardó la hoja, a su fecha de análisis; sin las decisiones posteriores (P-O1, P-O2, F1-A/F1-B, D-US1/2, D-WM) ni verificación contra la fuente oficial.

| Campo | Valor |
|---|---|
| Fecha de la hoja | 2026-10-30 |
| Tarea | cribado-44413758195-azkoyen |
| SHA del código | 833cd50a9bba34006519119c72a29c70a1656fb7 |
| Huella del paquete (package_sha256) | a1b3e2dc79c459c2e3f9f7863ed50d3112c30c0088549fcf89be699c4551f7cd |
| Huella del envío (bundle_sha256) | 465b91ae786b76124a2b4a120464610e5e04bb15fea1ff9646eea89f977c5d9b |
| Huella del encargo | 32b5c7f313e61a61fb0f5e68a75b3c44004eb902e97b98720fb98fa8d383e6cf |
| Huella de la Release | 4d30f7352948fe7e7fe3b133386eabedbddcc71d997e972a1c6db7964d58b0a9 |
| Huella del libro | b05d268bf46b6497d4f5802ea6d75d117fa7d16ae74023d6e66dd10a2fd6e99d |
| Modelo pedido / devuelto | claude-opus-5-5 / claude-opus-5-5 |
| Esfuerzo | high |
| Gramática del servidor | True |
| Mensajes enviados | 1 |
| Cota de entrada antes de llamar | 125611 tokens |
| Reserva estimada antes de llamar | USD 1.157804 |
| Uso de tokens | entrada 57187, salida 4483 |
| Coste | CONOCIDO_ESTIMADO; estimado USD 0.318408; cota 0.318408 |

| id | ruta | sha256 | bytes |
|---|---|---|---|
| respuesta | EMPRESAS_LOTES_COMPLETOS/Azkoyen/Azkoyen_respuesta.md | 6da5c81755be20e03d80b63ee421e0a9d6450e6379cf5324e8df2ddcda8d5cfb | 30138 |
| hoja_analisis | EMPRESAS_LOTES_COMPLETOS/Azkoyen/Azkoyen_evaluada.xlsx#Análisis | d2e312e322290f17413548cbffae653b6311e730195e89220f0403049d928623 | 23128 |
| hoja_control_maestro | EMPRESAS_LOTES_COMPLETOS/Azkoyen/Azkoyen_evaluada.xlsx#Control maestro | eac944f110eca40fc2dbc686eb767e35b2bdb2a78cc6a9c8ad93b178e1fa0a06 | 51643 |

## Salida del modelo (datos, sin acciones ejecutables)

Veredicto `estudiar_a_fondo` · DCF de la plantilla aplica: `si`

| Filtro | Resultado |
|---|---|
| calidad | dudoso |
| caja | pasa |
| balance | pasa |
| precio | dudoso |
| encaje | no_aplica |

### Pasivo por arrendamientos (dato aparte)

    Control maestro!M51 = 6.56 (arrendamientos NIIF 16 a 30-jun-2026, mm EUR)


### Tipo de negocio y motor

    Grupo industrial de bienes de equipo en tres nichos (medios de pago y gestión del efectivo, máquinas de café y vending, control de accesos), con ciclicidad moderada y beneficio concentrado en Payment Technologies.
    El DCF de caja libre de la plantilla, con la base media de tres años como aproximación a caja de ciclo medio y revisando el capex de mantenimiento normal; una suma de partes por segmento (Payment frente a Coffee & Vending y Time & Security) serviría de contraste.

### calidad

    El negocio se entiende (C11 = Sí) y muestra ROCE del 17 %, margen EBIT del 12-13 % estable y ningún cliente por encima del 10 %, pero el 81 % del resultado depende de Payment Technologies sin foso demostrado (C18 = No), dos de tres segmentos se deterioran en 1S26 y el fondo de comercio pesa un 25,3 % del activo (C32) con test de 2026 en riesgo; discrepo de la etapa 1 en que esto es una duda resoluble, no un 'demasiado difícil'.
    Dato clave: Análisis!C24 = 0.17

### caja

    La caja libre base de 19,1 mm (media FY23-25, ya neta de 0,461 de intereses y 2,929 de principal de arrendamientos) es positiva los once años de la serie y la conversión CFO/beneficio es de 1,453x (Análisis!C26), con la reserva de que un capex medio de 3,67 mm (C47) por debajo de la amortización puede inflarla en unos 2 mm.
    Dato clave: Análisis!C52 = 19.102

### balance

    La deuda/EBITDA de la hoja (0,42x en Análisis!C33) incluye 6,56 mm de arrendamientos y EBITDA NIIF 16; sin ellos, Control maestro!N36 da 0,24x (deuda neta ≈6,8 mm sobre EBITDA ≈28,4 mm), muy holgado incluso para un negocio algo cíclico; los 30 mm de préstamos nuevos vencen a 5 años, aunque no se conocen sus cláusulas de cambio de control ante la OPA.
    Dato clave: Control maestro!N51 = 32.64 (deuda sin arrendamientos); deuda neta sin arrendamientos ≈ 6.78 (13.341 − 6.56) sobre EBITDA pre-NIIF 16 de 28.41 ≈ 0.24x (Control maestro!N36)

### precio

    La cotización de 10,40 € está un 13 % por encima del precio de Sí de 9,20 € (escenario malo), pero por debajo del ponderado de 13,53 € (C83), y el resultado cambia dentro de ±2 puntos de tasa (ponderado de 19,25 € a r 7 % y 10,39 € a r 11 %, C90-C92), con una OPA a 10 € pendiente que ancla el precio.
    Dato clave: Análisis!C78 = 9.20332318783971 (precio de Sí = mín(9,20; 0,75 × 13,53 = 10,15)) frente a Análisis!C37 = 10.4

### encaje

    El paquete no trae la cartera de la persona responsable y la hoja solo aporta datos de contexto como una capitalización de 253,64 mm, así que este filtro no aplica en el cribado.
    Dato clave: Análisis!C41 = 253.64

### Qué lo cambiaría

    - Un test de deterioro de 2026 que recorte el fondo de comercio de Coges o Primion, o un cierre de 2026 con margen EBIT por debajo del 11 %, llevaría a descartar.
    - Un capex de mantenimiento normal de 5-6 mm que baje la caja libre base de 19,1 mm a unos 17 mm reduciría el precio de Sí por debajo de 9,2 €.
    - Una cotización por debajo de 9,2 € con el foso de Payment verificado haría pasar el filtro de precio.

### Qué falta

    - Competidores con nombre, cuotas y evolución de precios en Cashlogy y Coges, que deciden si el margen del 29 % de Payment es duradero.
    - Capex de mantenimiento real frente a la amortización (3,67 mm de capex medio frente a unos 6,2 mm de amortización en 2025) y cuánta amortización procede de intangibles de compras.
    - Condiciones de la OPA a 10 € y cláusulas de cambio de control y covenants de los 30 mm de préstamos de 2026.

### Comprobaciones mecánicas y normalizaciones

    {
      "comprobaciones": {
        "avisos": [
          "Filtro calidad: motivo de más de 400 caracteres."
        ],
        "nota": "Comprobaciones mecánicas informativas: no acreditan la calidad económica."
      },
      "normalizaciones": []
    }

