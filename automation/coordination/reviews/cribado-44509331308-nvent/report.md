# Cribado · nVent

Estado de la ejecución: `AUDITORIA_DOCUMENTAL_PENDIENTE_ACEPTACION`

Cribado pendiente de revisión humana. No es una recomendación de compra, ni aceptación, ni aptitud para dinero real. Tasa 9 % provisional.

C-ARR (decisión de la persona responsable): los arrendamientos se cuentan una sola vez, en el flujo. El alquiler se resta de la caja libre; la deuda, deuda/EBITDA y deuda/caja libre se miden sin arrendamientos; el pasivo por arrendamientos se muestra aparte, como dato.

Cifras de la etapa 1 tal como las guardó la hoja, a su fecha de análisis; sin las decisiones posteriores (P-O1, P-O2, F1-A/F1-B, D-US1/2, D-WM) ni verificación contra la fuente oficial.

| Campo | Valor |
|---|---|
| Fecha de la hoja | 2026-10-09 |
| Tarea | cribado-44509331308-nvent |
| SHA del código | 833cd50a9bba34006519119c72a29c70a1656fb7 |
| Huella del paquete (package_sha256) | 7a3401ba51c168847ae69c3268f7fbcccbfc044b1f5c06633a1736bec64aa66d |
| Huella del envío (bundle_sha256) | 7823b99be667519670eb110d3ea71a32aa66cc5a224301998670c9a81802e1a6 |
| Huella del encargo | 32b5c7f313e61a61fb0f5e68a75b3c44004eb902e97b98720fb98fa8d383e6cf |
| Huella de la Release | 4d30f7352948fe7e7fe3b133386eabedbddcc71d997e972a1c6db7964d58b0a9 |
| Huella del libro | c56ed1405640ae5f7f02883f60043fc68e8256bcd77153d07a3a5e10735cb698 |
| Modelo pedido / devuelto | claude-opus-5-5 / claude-opus-5-5 |
| Esfuerzo | high |
| Gramática del servidor | True |
| Mensajes enviados | 1 |
| Cota de entrada antes de llamar | 142000 tokens |
| Reserva estimada antes de llamar | USD 1.22336 |
| Uso de tokens | entrada 64905, salida 4531 |
| Coste | CONOCIDO_ESTIMADO; estimado USD 0.35024; cota 0.35024 |

| id | ruta | sha256 | bytes |
|---|---|---|---|
| respuesta | EMPRESAS_LOTES_COMPLETOS/nVent/nVent_respuesta.md | 29ad165689da7e51721d279c162403222a8cd0107fc7a02f02a2a51a1d49e566 | 34723 |
| cambios_v2 | EMPRESAS_LOTES_COMPLETOS/nVent/nVent_cambios_v2.md | bd67ad06118b622d7c34cbf54df0564e8b4f866d0e732f1c1b6e1174b4471fbe | 4123 |
| hoja_analisis | EMPRESAS_LOTES_COMPLETOS/nVent/nVent_evaluada.xlsx#Análisis | 12287e7fd73e304eeed09a98603d504fd1e19fabc1ac31710916752577a1bd0b | 23719 |
| hoja_control_maestro | EMPRESAS_LOTES_COMPLETOS/nVent/nVent_evaluada.xlsx#Control maestro | e14c544ac02da698a177bed9c16c6acae79692c8da2863d58e9df68d30c9c3b5 | 58256 |

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

    Control maestro!N51 = 140.5 (arrendamientos operativos, fuera de la deuda); además, pasivo por arrendamiento financiero de 17,8 a dic-25 (Control maestro!N46).


### Tipo de negocio y motor

    Fabricante industrial de equipo eléctrico (envolventes, conexiones, refrigeración líquida y distribución de energía), semicíclico, con fuerte exposición a infraestructura (centros de datos y servicios públicos) y crecimiento apoyado en adquisiciones.
    El DCF de la plantilla sirve, pero con una caja libre de ciclo medio (no la de un año fuerte de la ola) y con el perímetro pro forma de Maverick: su FCF y el coste de su deuda.

### calidad

    El negocio se entiende (C11 = Sí), con ROIC del 15,1% (13,0% publicado, ~31% sin fondo de comercio) y margen operativo ajustado estable en torno al 20,6% LTM, pero el fondo de comercio pesa el 39,1% del activo, un cliente sin identificar supone el 11% de las ventas, el crecimiento depende de la ola de infraestructura y de compras, y el foso no está probado; discrepo del «DESCARTAR · demasiado difícil» de la hoja porque la dificultad está en la valoración, no en entender el negocio.
    Dato clave: Análisis!C24 = 0.151

### caja

    La caja libre es positiva todos los años, con FCF continuado de 234,8 → 561,0 mm (2022–2025), FCF base tras SBC de 518,2 mm, conversión CFO/beneficio de 1,05 (1,39 en continuing FY23–25) y capex de solo 93,3 mm; la reserva es que parte del crecimiento se compró (3.172 mm de compras frente a 2.882,5 mm de FCF acumulado).
    Dato clave: Análisis!C52 = 518.2

### balance

    Sin arrendamientos, la deuda de 1.492,4 mm menos la caja de 256 da una deuda neta de 1.236,4 sobre un EBITDA LTM de 1.058,4 (que ya resta el alquiler, US GAAP), es decir 1,17x (C33); tras Maverick la deuda sube a 3.150 mm pro forma y el cociente a ≈2,48x (estimación de la fase 1), un nivel aceptable para un negocio semicíclico con grado de inversión, covenant de 3,75x y primer vencimiento de 500 en 2028.
    Dato clave: Análisis!C54 = 1492.4

### precio

    A 164,2 USD la cotización está muy por encima del valor ponderado de 65,3 USD y del escenario bueno de 102,1, e incluso con r al 7% el máximo es 102,1 (C90); el DCF inverso exige un crecimiento del 19,1% anual, y no hay precio de Sí porque la etapa 1 lo dejó sin fijar (referencia ≈38).
    Dato clave: Análisis!C83 = 65.2730186593007

### encaje

    El paquete no trae la cartera de la persona responsable y la hoja solo aporta el tamaño de la empresa (capitalización de 26.577,1 mm), lo que no permite juzgar el encaje.
    Dato clave: Análisis!C41 = 26577.1

### Qué lo cambiaría

    - Una cotización por debajo del valor ponderado de la hoja (≈65 USD, Análisis!C83) pasaría el precio y llevaría a estudiar a fondo.
    - Que el 10-Q Q3-26 mostrara una deuda neta/EBITDA real tras Maverick claramente por encima de 2,5x y acercándose al covenant de 3,75x haría que el balance no pasara.
    - Un deterioro del fondo de comercio de EPG, Trachte o Maverick, o una caída de pedidos de infraestructura con márgenes de segmento a la baja, haría que la calidad no pasara.

### Qué falta

    - Primer balance con Maverick (10-Q Q3-26): deuda neta, EBITDA y FCF reales tras la compra; hoy solo hay el pro forma estimado de ≈2,48x.
    - Desglose de Infrastructure entre centros de datos y servicios públicos, e identidad y contrato del cliente del 11% de las ventas.
    - Porcentaje de insiders (Análisis!C96 vacía) y proxy 2026; además, la respuesta v2 es del 25-oct-2026, posterior a la fecha de corte de la hoja.

### Comprobaciones mecánicas y normalizaciones

    {
      "comprobaciones": {
        "avisos": [
          "Filtro calidad: motivo de más de 400 caracteres.",
          "Filtro balance: motivo de más de 400 caracteres."
        ],
        "nota": "Comprobaciones mecánicas informativas: no acreditan la calidad económica."
      },
      "normalizaciones": []
    }

