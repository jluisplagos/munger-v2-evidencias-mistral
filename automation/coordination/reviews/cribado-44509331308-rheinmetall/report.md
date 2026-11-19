# Cribado · Rheinmetall

Estado de la ejecución: `AUDITORIA_DOCUMENTAL_PENDIENTE_ACEPTACION`

Cribado pendiente de revisión humana. No es una recomendación de compra, ni aceptación, ni aptitud para dinero real. Tasa 9 % provisional.

C-ARR (decisión de la persona responsable): los arrendamientos se cuentan una sola vez, en el flujo. El alquiler se resta de la caja libre; la deuda, deuda/EBITDA y deuda/caja libre se miden sin arrendamientos; el pasivo por arrendamientos se muestra aparte, como dato.

Cifras de la etapa 1 tal como las guardó la hoja, a su fecha de análisis; sin las decisiones posteriores (P-O1, P-O2, F1-A/F1-B, D-US1/2, D-WM) ni verificación contra la fuente oficial.

| Campo | Valor |
|---|---|
| Fecha de la hoja | 2026-10-17 |
| Tarea | cribado-44509331308-rheinmetall |
| SHA del código | 833cd50a9bba34006519119c72a29c70a1656fb7 |
| Huella del paquete (package_sha256) | 5cf0e034d7aae4ea20c98e7f498d8f78324107254779abea4c3af19d517218a6 |
| Huella del envío (bundle_sha256) | 0c7a3a4d830291bccfa4fda937d08802259b7f1ca2a8a9da9ff6691a20a526dc |
| Huella del encargo | 32b5c7f313e61a61fb0f5e68a75b3c44004eb902e97b98720fb98fa8d383e6cf |
| Huella de la Release | 4d30f7352948fe7e7fe3b133386eabedbddcc71d997e972a1c6db7964d58b0a9 |
| Huella del libro | cd522781bce193798b371c33a509f3c1de0b7de845c4ab8f5d9e51cdb2a33bb6 |
| Modelo pedido / devuelto | claude-opus-5-5 / claude-opus-5-5 |
| Esfuerzo | high |
| Gramática del servidor | True |
| Mensajes enviados | 1 |
| Cota de entrada antes de llamar | 130843 tokens |
| Reserva estimada antes de llamar | USD 1.178732 |
| Uso de tokens | entrada 59041, salida 3856 |
| Coste | CONOCIDO_ESTIMADO; estimado USD 0.313284; cota 0.313284 |

| id | ruta | sha256 | bytes |
|---|---|---|---|
| respuesta | EMPRESAS_LOTES_COMPLETOS/Rheinmetall/Rheinmetall_respuesta.md | e943a6ad8f048ccccda4efdf3f38c619470b86eb86088f31f7c4b362c7bfca49 | 29862 |
| cambios_v2 | EMPRESAS_LOTES_COMPLETOS/Rheinmetall/Rheinmetall_cambios_v2.md | 2db6591061d9763f8d1eef0279a54f373a5b327139cd3009ee9345befc7acb12 | 2435 |
| hoja_analisis | EMPRESAS_LOTES_COMPLETOS/Rheinmetall/Rheinmetall_evaluada.xlsx#Análisis | 7c29367293fd7e4dcc23e2d5db65d98d8ef9a13c93538e9f1dbf5fa1a5c827d6 | 23352 |
| hoja_control_maestro | EMPRESAS_LOTES_COMPLETOS/Rheinmetall/Rheinmetall_evaluada.xlsx#Control maestro | 5bda0878230ba3434470480f2a265107f22afb81b85a44ec82ddb0fa8a4dd94e | 54137 |

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

    Control maestro!M51 = 379 (arrendamientos ≈379 m, derivado; la deuda financiera sin arrendamientos es de 2.599 m, Control maestro!N51)


### Tipo de negocio y motor

    Fabricante de defensa (vehículos, munición, defensa aérea, naval y electrónica) cuyo cliente es casi siempre un Estado, con un ciclo ligado al gasto público en defensa y una caja muy dependiente de los anticipos de clientes.
    Caja libre de ciclo medio normalizada sin la entrada de anticipos de clientes, contrastada con la cartera firme (56.342 m de Order Backlog) y con márgenes de defensa a lo largo de un ciclo completo de compras públicas.

### calidad

    El negocio se entiende y hoy rinde, con un ROCE LTM del 28,6% y un margen operativo del 18,5% en 2025, pero antes de la ola de rearme el ROCE del grupo no pasó del 17,1% y el margen de defensa no pasó del 9,7%; además depende del Estado alemán (≈3.800 m de 9.935 m de ventas), y en eso el cribado coincide con la bandera de la hoja en C18.
    Dato clave: Análisis!C24 = 0.286

### caja

    El FCF base de 831 m es positivo, pero el LTM cae a 326 m (Control maestro!M40), el OFCF del primer semestre de 2026 fue de −1.616 m y la conversión CFO/beneficio de 1,81 baja a 0,34 sin anticipos de clientes, así que la recurrencia depende de los anticipos.
    Dato clave: Análisis!C52 = 831

### balance

    Sin arrendamientos la deuda neta de 2.344 m equivale a ≈1,0x el EBITDA LTM tras restar el alquiler, cómodo incluso para un negocio cíclico; el 1,12x de Análisis!C33 no sirve tal cual porque incluye arrendamientos, y queda el riesgo de refinanciar el puente de NVL de 999 m (≤ mar-2027) con solo 255 m de caja frente a 1.740 m de deuda corriente.
    Dato clave: Control maestro!N36 = 2344 (deuda neta sin arrendamientos ÷ EBITDA tras alquiler ≈2.345 ≈ 1,0x)

### precio

    La cotización de 1.090,2 € está muy por encima del ponderado de 406,6 €, del escenario bueno de 721,8 € y aun del ponderado con r del 7% (593,3 €); el DCF inverso pide un 21,3% de crecimiento anual, y aunque el DCF de la plantilla es dudoso, la conclusión se sostiene con un FCF yield de solo el 1,6% y un EV/EBITDA de 22,3x.
    Dato clave: Análisis!C83 = 406.628491903991

### encaje

    El paquete no trae la cartera de la persona responsable y la hoja no dice nada concreto de encaje más allá de una capitalización de 50.877,5 m, así que este filtro no elimina.
    Dato clave: Análisis!C41 = 50877.5

### Qué lo cambiaría

    - Una cotización cercana o inferior al ponderado de la hoja (≈407 €) llevaría el caso a estudiar a fondo.
    - Dos años seguidos de OFCF positivo y creciente con pasivos de contrato estables resolverían la duda de caja.
    - Que los márgenes caigan hacia el 10% al frenarse los pedidos, o que no se refinancie el puente de NVL de 999 m, llevaría a descartar.

### Qué falta

    - Caja libre normalizada sin anticipos: serie anual de pasivos de contrato y anticipos por cliente (la hoja solo da 3.866 / 5.642 / 6.265 m).
    - Qué parte de la cartera de 80.467 m es firme y cuáles son sus condiciones de cancelación (el Frame Backlog es de 24.126 m).
    - El LTM está a 30-06-2026; el tercer trimestre de 2026 no consta en el paquete, y tampoco consta el % agregado de insiders (Análisis!C96 vacía).

### Comprobaciones mecánicas y normalizaciones

    {
      "comprobaciones": {
        "avisos": [],
        "nota": "Comprobaciones mecánicas informativas: no acreditan la calidad económica."
      },
      "normalizaciones": []
    }

