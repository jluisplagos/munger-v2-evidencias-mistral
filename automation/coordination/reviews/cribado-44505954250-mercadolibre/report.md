# Cribado · MercadoLibre

Estado de la ejecución: `AUDITORIA_DOCUMENTAL_PENDIENTE_ACEPTACION`

Cribado pendiente de revisión humana. No es una recomendación de compra, ni aceptación, ni aptitud para dinero real. Tasa 9 % provisional.

C-ARR (decisión de la persona responsable): los arrendamientos se cuentan una sola vez, en el flujo. El alquiler se resta de la caja libre; la deuda, deuda/EBITDA y deuda/caja libre se miden sin arrendamientos; el pasivo por arrendamientos se muestra aparte, como dato.

Cifras de la etapa 1 tal como las guardó la hoja, a su fecha de análisis; sin las decisiones posteriores (P-O1, P-O2, F1-A/F1-B, D-US1/2, D-WM) ni verificación contra la fuente oficial.

| Campo | Valor |
|---|---|
| Fecha de la hoja | 2026-10-09 |
| Tarea | cribado-44505954250-mercadolibre |
| SHA del código | 833cd50a9bba34006519119c72a29c70a1656fb7 |
| Huella del paquete (package_sha256) | 5a91c47bd783d10a92098238ef02e9f0ab72df2fa6010e2f41e85866735a2cb6 |
| Huella del envío (bundle_sha256) | 123da66e2ae9be112fe5f21f6463bafd9072a3e9a16c5486b9a8de472d916af5 |
| Huella del encargo | 32b5c7f313e61a61fb0f5e68a75b3c44004eb902e97b98720fb98fa8d383e6cf |
| Huella de la Release | 4d30f7352948fe7e7fe3b133386eabedbddcc71d997e972a1c6db7964d58b0a9 |
| Huella del libro | 7d4e67b07bbc84db49bff77fb1e8d9f0fd87af7bc6aa342115b97fc82e0e25f5 |
| Modelo pedido / devuelto | claude-opus-5-5 / claude-opus-5-5 |
| Esfuerzo | high |
| Gramática del servidor | True |
| Mensajes enviados | 1 |
| Cota de entrada antes de llamar | 128472 tokens |
| Reserva estimada antes de llamar | USD 1.169248 |
| Uso de tokens | entrada 58414, salida 4736 |
| Coste | CONOCIDO_ESTIMADO; estimado USD 0.328376; cota 0.328376 |

| id | ruta | sha256 | bytes |
|---|---|---|---|
| respuesta | EMPRESAS_LOTES_COMPLETOS/MercadoLibre/MercadoLibre_respuesta.md | f2cf0bce879ea4496336012a69c583f79240f7dea7e08f145cea75f8b0c1fe5b | 30946 |
| hoja_analisis | EMPRESAS_LOTES_COMPLETOS/MercadoLibre/MercadoLibre_evaluada.xlsx#Análisis | 06847cc001aae07a4ecf7a3e9646654a6a8ac4a68257d4e0e49b73d2c972f75e | 23623 |
| hoja_control_maestro | EMPRESAS_LOTES_COMPLETOS/MercadoLibre/MercadoLibre_evaluada.xlsx#Control maestro | ad7af46cbc63a94a1e83ec9cb7399dd1f51521ec0070aa4913f32cc21860da10 | 52995 |

## Salida del modelo (datos, sin acciones ejecutables)

Veredicto `demasiado_dificil` · DCF de la plantilla aplica: `no`

| Filtro | Resultado |
|---|---|
| calidad | dudoso |
| caja | dudoso |
| balance | dudoso |
| precio | dudoso |
| encaje | no_aplica |

### Pasivo por arrendamientos (dato aparte)

    Control maestro!N51: operating leases 2.550 (deuda con operating leases 13.176), más 115 de finance leases incluidos en Análisis!C54 = 10626 y excluidos del cociente.


### Tipo de negocio y motor

    Híbrido de comercio electrónico (marketplace, logística, publicidad) y fintech con cartera de crédito al consumo y a comerciantes, y float de clientes, en Latinoamérica.
    Suma de partes: el comercio y los pagos valorados por su caja libre sin float de clientes, y la fintech de crédito valorada por la rentabilidad sobre el capital propio que exige su cartera, a lo largo de un ciclo de crédito.

### calidad

    La demanda crece (compradores de 85 a 121 m) y el ROIC LTM es del 16,8 %, pero cae desde el 33,2 % del FY24, el margen operativo baja del 14,6 % al 11,1 % y el propio 10-K reconoce barreras de entrada bajas; además, la mitad fintech es un prestamista con balance de tipo banco cuya rentabilidad para el accionista no se puede juzgar con el paquete.
    Dato clave: Análisis!C24 = 0.168

### caja

    El FCF LTM literal de 12.345 (13,1 % de rendimiento) se apoya en un float de clientes que fue el 57 % del CFO del FY25; el FCF ajustado de la propia empresa es de solo 1.127 LTM (1,2 %), y sin float ni crecimiento de la cartera sale −4.073, de modo que no puedo dar por buena la conversión de 5,33x de la hoja.
    Dato clave: Análisis!C40 = 12345

### balance

    Sin arrendamientos, la deuda neta/EBITDA baja a 1,76x desde el 1,79x de la hoja, pero la deuda pasó de 5.715 a 10.626 en dieciocho meses, la caja solo cubre 0,56x la deuda corriente de 6.482 y la deuda financia una cartera de crédito de 12.508 con un 25 % de reserva, así que en un negocio expuesto al ciclo de crédito el cociente no basta para dar el ✓ PASA de la hoja.
    Dato clave: Deuda sin arrendamientos = Análisis!C54 = 10626 − 115 de finance leases (Control maestro!M51) = 10.511; deuda neta 6.862 ÷ EBITDA LTM 3.892 (Control maestro!M36) = 1,76x

### precio

    La cotización de 1.856,66 queda por debajo del ponderado de 3.061,6 a r 9 % (2.285,6 a r 11 %), pero ese DCF descansa en un FCF base de 7.444 con float que la propia hoja declara no aplicable (C62); con el FCF ajustado de la empresa, el escenario normal saldría en torno a 600, y no hay precio de Sí.
    Dato clave: Análisis!C37 = 1856.66

### encaje

    El paquete no trae la cartera de la persona responsable; solo consta como contexto que Brasil, México y Argentina suman el 96 % de los ingresos, sin efecto eliminatorio.
    Dato clave: Control maestro!M19: Brasil 52,6 %, México 22,4 %, Argentina 20,6 % de los ingresos FY25

### Qué lo cambiaría

    - Que la empresa publique la caja del comercio separada del balance financiero y salga un FCF sin float claramente positivo frente a la capitalización de 94.127.
    - Que las cosechas de crédito muestren write-offs (1.796 en FY25) que crecen menos que la cartera, con pérdidas contenidas en un año malo.
    - Que la deuda financiera (10.626) deje de crecer más deprisa que la cartera y que la caja cubra la deuda corriente (hoy 0,56x).

### Qué falta

    - Caja libre del comercio separada del float de clientes y de la inversión en la cartera de crédito, y cosechas de crédito por país y producto a lo largo de un ciclo.
    - Capital propio o regulatorio que exige la fintech y el calendario de vencimientos de la deuda por plazos; la hoja solo da la parte corriente (6.482) y el pro forma de las notes 2036 (1.000).
    - Duda de fuentes: varias entradas (C40, C46, C47, C49, C60, C88) llevan «Decisión del inversor (18-oct-2026)» y una revisión del 25-oct-2026, posteriores a la fecha de la hoja (09-oct-2026).

### Comprobaciones mecánicas y normalizaciones

    {
      "comprobaciones": {
        "avisos": [],
        "nota": "Comprobaciones mecánicas informativas: no acreditan la calidad económica."
      },
      "normalizaciones": []
    }

