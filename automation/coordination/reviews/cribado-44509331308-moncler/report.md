# Cribado · Moncler

Estado de la ejecución: `AUDITORIA_DOCUMENTAL_PENDIENTE_ACEPTACION`

Cribado pendiente de revisión humana. No es una recomendación de compra, ni aceptación, ni aptitud para dinero real. Tasa 9 % provisional.

C-ARR (decisión de la persona responsable): los arrendamientos se cuentan una sola vez, en el flujo. El alquiler se resta de la caja libre; la deuda, deuda/EBITDA y deuda/caja libre se miden sin arrendamientos; el pasivo por arrendamientos se muestra aparte, como dato.

Cifras de la etapa 1 tal como las guardó la hoja, a su fecha de análisis; sin las decisiones posteriores (P-O1, P-O2, F1-A/F1-B, D-US1/2, D-WM) ni verificación contra la fuente oficial.

| Campo | Valor |
|---|---|
| Fecha de la hoja | 25-oct-2026 |
| Tarea | cribado-44509331308-moncler |
| SHA del código | 833cd50a9bba34006519119c72a29c70a1656fb7 |
| Huella del paquete (package_sha256) | 6b108ea9444d1b414688fffbc6e92675a392674e94f4dd063f4ba3fe5edcf4bc |
| Huella del envío (bundle_sha256) | fedf6ae083fa6513ce670d6b23cebebc4faa3121f5af02d0c603a1d00a74a483 |
| Huella del encargo | 32b5c7f313e61a61fb0f5e68a75b3c44004eb902e97b98720fb98fa8d383e6cf |
| Huella de la Release | 4d30f7352948fe7e7fe3b133386eabedbddcc71d997e972a1c6db7964d58b0a9 |
| Huella del libro | 8d24cfc748c358d423cd5b204e129dbb9f8ca53edf63ccd6007dd44fa90e3bf0 |
| Modelo pedido / devuelto | claude-opus-5-5 / claude-opus-5-5 |
| Esfuerzo | high |
| Gramática del servidor | True |
| Mensajes enviados | 1 |
| Cota de entrada antes de llamar | 133181 tokens |
| Reserva estimada antes de llamar | USD 1.188084 |
| Uso de tokens | entrada 61143, salida 3681 |
| Coste | CONOCIDO_ESTIMADO; estimado USD 0.318192; cota 0.318192 |

| id | ruta | sha256 | bytes |
|---|---|---|---|
| respuesta | EMPRESAS_LOTES_COMPLETOS/Moncler/Moncler_respuesta.md | d8ae278c6eb6c9b9f790c0a87d2a9368e9038b97c6d88e1ec5e35fda30ede9bc | 30426 |
| hoja_analisis | EMPRESAS_LOTES_COMPLETOS/Moncler/Moncler_evaluada.xlsx#Análisis | 6f536f95cd7e10155d7c3e5a47ee9a8ce2953c8694c28a57054375bee200d3a5 | 22812 |
| hoja_control_maestro | EMPRESAS_LOTES_COMPLETOS/Moncler/Moncler_evaluada.xlsx#Control maestro | 969c76e2fd5e27b3d0b7445d7fe19d0b8044e6e6349f6754aaa20bac5621f431 | 58870 |

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

    Control maestro!M51 = 1198.8 (pasivo por arrendamientos a 30-jun-2026; la respuesta cita 1.198,6 mm y manda la hoja)


### Tipo de negocio y motor

    Lujo personal de marca (abrigos y ropa de lujo: Moncler 87 % y Stone Island 13 %), vendido sobre todo en tiendas propias.
    El DCF de caja libre del accionista de la plantilla, porque es un negocio de marca estable, sin deuda financiera y con alquileres ya restados del flujo, contrastado con escenarios de crecimiento de la marca.

### calidad

    El negocio se entiende y la ventaja de marca se ve en las cifras (ROIC 18,5 %, margen bruto 75,7 %→78,1 % y margen EBIT 28,6–30,2 % en 2016–25), aunque el ROIC incremental de FY23→25 (≈3 %), el CSSG de −1 % y el 52 % en Asia son dudas que el estudio debe resolver; el «DESCARTAR · demasiado difícil» de Análisis!A6 sale del embudo de la etapa 1 (C13 = No por precio), no de no entender el negocio.
    Dato clave: Análisis!C24 = 0.185

### caja

    La caja libre base es de 500,2 mm después de alquileres y SBC, con conversión CFO/beneficio de 1,53x (Análisis!C26) y FCF positivo todos los años; es recurrente pero plana en 2021–25 (587/322/538/584/500 mm) mientras el capex sube al 7 % de las ventas.
    Dato clave: Análisis!C52 = 500.2

### balance

    El 0,08x de Análisis!C33 incluye arrendamientos y no sirve tal cual; sin ellos, la deuda es de solo 37,4 mm (1.236,3 − 1.198,8) y la caja neta de 1.112,4 mm (Control maestro!N36), sin deuda bancaria ni bonos, así que hay caja neta y no apalancamiento, aunque el EBITDA sin alquiler es una aproximación no publicada (~1.006–1.028 mm).
    Dato clave: Control maestro!N51 = 37.4

### precio

    La cotización (42,66 €) casi duplica el precio de Sí (≈22,3 €, escenario malo), supera el valor normal (33,5 €) y el ponderado (35,4 €), y exige un 8,2 % de crecimiento del FCF (Análisis!C86); a r = 7 % el ponderado sería de 51,4 €, pero el precio de Sí seguiría muy por debajo de la cotización.
    Dato clave: Análisis!B78 = 22.3244403193734

### encaje

    El paquete no trae la cartera de la persona responsable y la hoja solo da contexto de mercado (capitalización de 11.603,1 mm), así que este filtro no aplica y no elimina.
    Dato clave: Análisis!C41 = 11603.1

### Qué lo cambiaría

    - Una cotización en el entorno de 22,3 € o menos (Análisis!B78) con margen bruto ≈78 % y margen EBIT ≥28 %: pasaría a estudiar_a_fondo.
    - Un FCF de FY26–27 por encima de 600 mm con el capex de vuelta al ≈6 % de las ventas, que subiría la base y el precio de Sí.
    - Un margen EBIT por debajo del 27 % fuera de un año excepcional, o un inventario que siga creciendo más que las ventas al cierre de FY26: rebajaría la calidad y llevaría a descartar.

### Qué falta

    - Márgenes y caja por marca: no se publican los de Stone Island (un solo segmento IFRS 8).
    - EBITDA sin NIIF 16 (después de alquileres): no se publica desde FY23; la hoja solo da una aproximación de ~1.006–1.028 mm.
    - Datos de competidores, precio frente a volumen y rebajas para juzgar si el deseo de la marca es duradero.

### Comprobaciones mecánicas y normalizaciones

    {
      "comprobaciones": {
        "avisos": [],
        "nota": "Comprobaciones mecánicas informativas: no acreditan la calidad económica."
      },
      "normalizaciones": []
    }

