# Cribado · AirtelAfrica

Estado de la ejecución: `AUDITORIA_DOCUMENTAL_PENDIENTE_ACEPTACION`

Cribado pendiente de revisión humana. No es una recomendación de compra, ni aceptación, ni aptitud para dinero real. Tasa 9 % provisional.

C-ARR (decisión de la persona responsable): los arrendamientos se cuentan una sola vez, en el flujo. El alquiler se resta de la caja libre; la deuda, deuda/EBITDA y deuda/caja libre se miden sin arrendamientos; el pasivo por arrendamientos se muestra aparte, como dato.

Cifras de la etapa 1 tal como las guardó la hoja, a su fecha de análisis; sin las decisiones posteriores (P-O1, P-O2, F1-A/F1-B, D-US1/2, D-WM) ni verificación contra la fuente oficial.

| Campo | Valor |
|---|---|
| Fecha de la hoja | 2026-10-24 |
| Tarea | cribado-44413758195-airtelafrica |
| SHA del código | 833cd50a9bba34006519119c72a29c70a1656fb7 |
| Huella del paquete (package_sha256) | 0dd2660f7e0486bd34bc6f0f08b3223d0ddeebe431f55d96e6bf8b27059be51f |
| Huella del envío (bundle_sha256) | baa503525ed267f12573efe90379005ea9af20198122d07d70d740757d544b2e |
| Huella del encargo | 32b5c7f313e61a61fb0f5e68a75b3c44004eb902e97b98720fb98fa8d383e6cf |
| Huella de la Release | 4d30f7352948fe7e7fe3b133386eabedbddcc71d997e972a1c6db7964d58b0a9 |
| Huella del libro | 3d28d288b50b09fcaca0711aa6b4d146455970d95a831b5b110264ea770e1c4a |
| Modelo pedido / devuelto | claude-opus-5-5 / claude-opus-5-5 |
| Esfuerzo | high |
| Gramática del servidor | True |
| Mensajes enviados | 1 |
| Cota de entrada antes de llamar | 159480 tokens |
| Reserva estimada antes de llamar | USD 1.29328 |
| Uso de tokens | entrada 71087, salida 4424 |
| Coste | CONOCIDO_ESTIMADO; estimado USD 0.372828; cota 0.372828 |

| id | ruta | sha256 | bytes |
|---|---|---|---|
| respuesta | EMPRESAS_LOTES_COMPLETOS/AirtelAfrica/AirtelAfrica_respuesta.md | 6092558b91cf1e08b023fe483e61fae3bc61367879c94a66922b3ba438a232c0 | 47403 |
| hoja_analisis | EMPRESAS_LOTES_COMPLETOS/AirtelAfrica/AirtelAfrica_evaluada.xlsx#Análisis | fe21fb84c87d92623f068df1c243930c4b99d46b2a3be329ff64f8c6df93f94e | 24050 |
| hoja_control_maestro | EMPRESAS_LOTES_COMPLETOS/AirtelAfrica/AirtelAfrica_evaluada.xlsx#Control maestro | 4c7d96c02ab7b4cfdbcb31651c93829c0a8a9f3fa5a0185c9bed256e90bb2734 | 67043 |

## Salida del modelo (datos, sin acciones ejecutables)

Veredicto `vigilar` · DCF de la plantilla aplica: `dudoso`

| Filtro | Resultado |
|---|---|
| calidad | pasa |
| caja | dudoso |
| balance | pasa |
| precio | no_pasa |
| encaje | no_aplica |

### Pasivo por arrendamientos (dato aparte)

    Control maestro!M51 = 4224 (pasivo por arrendamientos a 31/03/2026, fuera de los cocientes de deuda)


### Tipo de negocio y motor

    Operador de telecomunicaciones móviles y dinero móvil en 14 países de África subsahariana, de suscripción prepago, intensivo en capex y con flujos en monedas locales reportados en dólares.
    Suma de partes por filial y moneda, con la caja realmente repatriable a la matriz, neta de minoritarios y de saldos de clientes, y valorando Airtel Money aparte; el DCF de la plantilla solo como contraste.

### calidad

    El negocio se entiende (prepago, primer o segundo operador en 13 de 14 mercados) y rinde: ROCE del 23,1% antes de impuestos (13,9% después, con un tipo efectivo del 40,1%) y margen EBITDAaL plano en torno al 39%. Hay reservas: precios autorizados por reguladores, accionista de control con el 79% y valor en dólares expuesto a catorce monedas.
    Dato clave: Análisis!C24 = 0.231

### caja

    La caja libre al accionista fue positiva en los cinco años: 651/269/466/515/1277 en bruto y 597/631/386/386/998 sin monederos ni espectro. Pero oscila 4,7 veces, la base de 725 incluye entradas de saldos de clientes (+279 en FY26) y la conversión de 4,68x (Análisis!C26) está inflada por pérdidas de cambio, así que la recurrencia en dólares no está demostrada.
    Dato clave: Análisis!C52 = 725

### balance

    Sin arrendamientos, la deuda es 2188 y la deuda neta unos 1366 (5590 − 4224), 0,55x el EBITDA después de alquileres y unas 1,9x la caja libre base de 725, holgado para un negocio de suscripción prepago; la vigilancia está en la liquidez, porque la caja de 646 no cubre los 1019 de préstamos a corto. El 1,77x de Análisis!C33 incluye arrendamientos y no sirve tal cual.
    Dato clave: Control maestro!N51 = 2188 (préstamos sin arrendamientos; deuda neta sin arrendamientos ≈1366 y 0,55x EBITDAaL según Control maestro!N36)

### precio

    La cotización de 3,6522 $ está un 56% por encima del precio de Sí (2,35 $, escenario malo) y prácticamente en el valor ponderado de 3,70 $ (margen 1,3%), que baja a 2,83 $ con r + 2 puntos. El DCF de la plantilla probablemente sobrevalora porque no descuenta el 16,5% de minoritarios ni los monederos, y la hoja es anterior a los resultados semestrales del 30/10/2026.
    Dato clave: Análisis!C37 = 3.6522 frente a Análisis!B78 = 2.34599634578889

### encaje

    El paquete no trae la cartera de la persona responsable y la hoja solo aporta datos de la empresa, como una capitalización de 13236,5 mm $, así que el encaje no se puede juzgar ni elimina.
    Dato clave: Análisis!C41 = 13236.5

### Qué lo cambiaría

    - Una cotización igual o inferior a unos 2,35 $ por acción (valor del escenario malo, Análisis!B78) pasaría el precio y llevaría a estudiar_a_fondo.
    - Una caja libre limpia de monederos por debajo de 386 mm $ dos años seguidos, o negativa, haría fallar el filtro de caja y llevaría a descartar.
    - Una deuda neta sin arrendamientos por encima de 2 veces el EBITDAaL, con la caja sin cubrir los préstamos a corto, haría fallar el balance.

### Qué falta

    - Resultados semestrales a 30/09/2026 (publicación prevista el 30/10/2026, posterior a la fecha de la hoja) con deuda, caja y caja libre actualizadas.
    - Caja libre por filial y moneda, y cuánta se puede repatriar a la matriz, neta de dividendos a minoritarios.
    - EBITDAaL de FY26 como cifra explícita en una celda (el 0,55x sin arrendamientos solo figura como sensibilidad).

### Comprobaciones mecánicas y normalizaciones

    {
      "comprobaciones": {
        "avisos": [],
        "nota": "Comprobaciones mecánicas informativas: no acreditan la calidad económica."
      },
      "normalizaciones": []
    }

