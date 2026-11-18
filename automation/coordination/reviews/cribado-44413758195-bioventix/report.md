# Cribado · Bioventix

Estado de la ejecución: `AUDITORIA_DOCUMENTAL_PENDIENTE_ACEPTACION`

Cribado pendiente de revisión humana. No es una recomendación de compra, ni aceptación, ni aptitud para dinero real. Tasa 9 % provisional.

C-ARR (decisión de la persona responsable): los arrendamientos se cuentan una sola vez, en el flujo. El alquiler se resta de la caja libre; la deuda, deuda/EBITDA y deuda/caja libre se miden sin arrendamientos; el pasivo por arrendamientos se muestra aparte, como dato.

Cifras de la etapa 1 tal como las guardó la hoja, a su fecha de análisis; sin las decisiones posteriores (P-O1, P-O2, F1-A/F1-B, D-US1/2, D-WM) ni verificación contra la fuente oficial.

| Campo | Valor |
|---|---|
| Fecha de la hoja | 2026-10-30 |
| Tarea | cribado-44413758195-bioventix |
| SHA del código | 833cd50a9bba34006519119c72a29c70a1656fb7 |
| Huella del paquete (package_sha256) | a31892331260f8493fa9a003291067e58d5cb1f90adc41b8f210b01cceddf02a |
| Huella del envío (bundle_sha256) | c5aa146f53321d6eb0317c52effe0140d6de1c9d9d5d756cb58d50ca82a708d2 |
| Huella del encargo | 32b5c7f313e61a61fb0f5e68a75b3c44004eb902e97b98720fb98fa8d383e6cf |
| Huella de la Release | 4d30f7352948fe7e7fe3b133386eabedbddcc71d997e972a1c6db7964d58b0a9 |
| Huella del libro | dd4e735086ea45cd8c8777d3cd3a53d70b177128d85bff396a8f4399c049071b |
| Modelo pedido / devuelto | claude-opus-5-5 / claude-opus-5-5 |
| Esfuerzo | high |
| Gramática del servidor | True |
| Mensajes enviados | 1 |
| Cota de entrada antes de llamar | 135677 tokens |
| Reserva estimada antes de llamar | USD 1.198068 |
| Uso de tokens | entrada 60412, salida 3492 |
| Coste | CONOCIDO_ESTIMADO; estimado USD 0.311488; cota 0.311488 |

| id | ruta | sha256 | bytes |
|---|---|---|---|
| respuesta | EMPRESAS_LOTES_COMPLETOS/Bioventix/Bioventix_respuesta.md | 2cef0e3b7198479c38754b5f9f5e8250068dbfaa4491c9cbe401b9c5ea339d68 | 36673 |
| hoja_analisis | EMPRESAS_LOTES_COMPLETOS/Bioventix/Bioventix_evaluada.xlsx#Análisis | 7f043ae4295aed9d9f216e35c17dfde2ae9e5ced93f8cb3879e8d3d847f51d1d | 24150 |
| hoja_control_maestro | EMPRESAS_LOTES_COMPLETOS/Bioventix/Bioventix_evaluada.xlsx#Control maestro | fab1f8ddc89f03084cac717625f6f7c4da895982ccc0a99c9d913ef39e9c74bc | 54076 |

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

    Análisis!C54 = 0.01097 (pasivo por arrendamiento financiero, 0,0038 a corto y 0,0072 a largo según Control maestro fila 51; es toda la deuda que figura)


### Tipo de negocio y motor

    Proveedor de anticuerpos monoclonales de oveja para diagnóstico in vitro que cobra royalties sobre los tests de grandes fabricantes; negocio maduro, con muy poco capital y contratos que caducan.
    El DCF de caja libre de la plantilla sirve para un negocio de royalties sin capital y con caja estable, siempre que los escenarios recojan el vencimiento de contratos (progesterona ya perdida, troponina de Siemens en 2032) y la erosión en China.

### calidad

    El negocio se entiende y muestra una ventaja visible (ROCE del 88 % y margen operativo del 74–79 % en once años), aunque el legado se erosiona (vitamina D, 49 % de las ventas, a la baja; ventas −3,6 % y −1,1 % en FY2025–26); discrepo del «DESCARTAR · demasiado difícil» de Análisis!A6, que mezcla precio y crecimiento con comprensión.
    Dato clave: Análisis!C24 = 0.88

### caja

    La caja libre base es de 7,65m con un capex de solo 0,036m y una conversión CFO/beneficio de 0,983, aunque es plana desde FY2022 (+1,1 % al año), por lo que es recurrente pero no crece.
    Dato clave: Análisis!C52 = 7.652769

### balance

    Sin arrendamientos la deuda es 0 frente a una caja de 5,26m y un EBITDA de 10,144m, así que hay caja neta (deuda neta/EBITDA ≈ −0,52x, casi igual a los −0,518x de C33, que incluye el arrendamiento de 0,011m); incluso restando el dividendo de 4,18m pagado tras el cierre, la caja neta sigue en ≈1,07m.
    Dato clave: Análisis!C53 = 5.264706 (caja); deuda sin arrendamientos = 0, porque Análisis!C54 = 0.01097 es solo arrendamiento financiero

### precio

    A £20,25 (con derecho a 80p de dividendo) la cotización está muy por encima del precio de Sí de ≈£12 y del escenario malo (£11,93), con solo un 3,6 % de margen sobre el ponderado de £21,0; además exige un crecimiento implícito del 1,49 %, por encima del normal del 1 %, y con r al 11 % el ponderado cae a £16,3.
    Dato clave: Análisis!C37 = 20.25

### encaje

    El paquete no trae la cartera; solo consta una capitalización de 105,8m con liquidez baja (≈£0,35m al día según Control maestro), lo que no basta para juzgar el encaje y no elimina.
    Dato clave: Análisis!C41 = 105.803

### Qué lo cambiaría

    - Cotización en torno o por debajo de £12 (escenario malo, Análisis!B78 = 11.93) sin deterioro de los hechos: pasaría a estudiar a fondo.
    - Pérdida del anticuerpo de vitamina D en un gran cliente, o caída de ventas en FY2027 superior al 5 % a tipo constante: calidad o caja dejarían de pasar.
    - Varios ensayos p-Tau217 de uso clínico aprobados con anticuerpo de Bioventix antes de FY2028, o royalties de neurología por encima de £1m: subirían el escenario normal.

### Qué falta

    - Informe anual FY2026: peso de cada cliente y calendario de vencimiento de cada contrato de royalty (solo constan los de progesterona, NT-proBNP y troponina de Siemens).
    - Control maestro (fila 34, C31) cita una decisión del inversor del 08-nov-2026, posterior a la fecha de corte del 30-oct-2026: duda sobre la coherencia temporal de la hoja.
    - Precio de Sí ≈£12: es una estimación de la respuesta (mín. del escenario malo y ¾ del ponderado), no una celda calculada; además, el precio es con derecho al dividendo (ex-dividendo ≈£19,45).

### Comprobaciones mecánicas y normalizaciones

    {
      "comprobaciones": {
        "avisos": [],
        "nota": "Comprobaciones mecánicas informativas: no acreditan la calidad económica."
      },
      "normalizaciones": []
    }

