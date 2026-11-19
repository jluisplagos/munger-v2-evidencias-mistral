# Cribado · Sarantis

Estado de la ejecución: `AUDITORIA_DOCUMENTAL_PENDIENTE_ACEPTACION`

Cribado pendiente de revisión humana. No es una recomendación de compra, ni aceptación, ni aptitud para dinero real. Tasa 9 % provisional.

C-ARR (decisión de la persona responsable): los arrendamientos se cuentan una sola vez, en el flujo. El alquiler se resta de la caja libre; la deuda, deuda/EBITDA y deuda/caja libre se miden sin arrendamientos; el pasivo por arrendamientos se muestra aparte, como dato.

Cifras de la etapa 1 tal como las guardó la hoja, a su fecha de análisis; sin las decisiones posteriores (P-O1, P-O2, F1-A/F1-B, D-US1/2, D-WM) ni verificación contra la fuente oficial.

| Campo | Valor |
|---|---|
| Fecha de la hoja | 2026-11-04 |
| Tarea | cribado-44512238939-sarantis |
| SHA del código | 833cd50a9bba34006519119c72a29c70a1656fb7 |
| Huella del paquete (package_sha256) | fd2246c820a8a08c5308931d57fd7cbc778954b8b24a38bb6e0680b2b6333f7f |
| Huella del envío (bundle_sha256) | 985325d587dcb7d3f811cd07e8f978dd06487255f8f141cc5862ccf111d15d5e |
| Huella del encargo | 32b5c7f313e61a61fb0f5e68a75b3c44004eb902e97b98720fb98fa8d383e6cf |
| Huella de la Release | 4d30f7352948fe7e7fe3b133386eabedbddcc71d997e972a1c6db7964d58b0a9 |
| Huella del libro | eb4d43b09b163ddfcf8bbac999333955e1da90ce01615c3e9c63129655ceff9c |
| Modelo pedido / devuelto | claude-opus-5-5 / claude-opus-5-5 |
| Esfuerzo | high |
| Gramática del servidor | True |
| Mensajes enviados | 1 |
| Cota de entrada antes de llamar | 163610 tokens |
| Reserva estimada antes de llamar | USD 1.3098 |
| Uso de tokens | entrada 72269, salida 4598 |
| Coste | CONOCIDO_ESTIMADO; estimado USD 0.381036; cota 0.381036 |

| id | ruta | sha256 | bytes |
|---|---|---|---|
| respuesta | EMPRESAS_LOTES_COMPLETOS/Sarantis/Sarantis_respuesta.md | dcdce3c63fa0259024242ec97f6c9ff3ee72718f2b44378ef60443f1d6ed7488 | 49848 |
| hoja_analisis | EMPRESAS_LOTES_COMPLETOS/Sarantis/Sarantis_evaluada.xlsx#Análisis | 948257ef2156509ccfb41e2d4b2d5f52384975830a0f66f3ab79c135b53f9f8f | 25737 |
| hoja_control_maestro | EMPRESAS_LOTES_COMPLETOS/Sarantis/Sarantis_evaluada.xlsx#Control maestro | d5fe5590a912a1a588b5b021ff2c660daa441f5acbd09a4c71d0f734dde9cbee | 66909 |

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

    Control maestro!M51 = 38.36 (pasivo por arrendamientos a 30-jun-26, que sube desde 20,0 en dic-25 por los nuevos almacenes; fuera del cociente de deuda)


### Tipo de negocio y motor

    Consumo básico: cosmética, cuidado personal y productos de hogar con marcas propias en Europa Central y del Este, más distribución de marcas de terceros (26,3% de las ventas) y marca blanca (8,5%); la sensibilidad a polietileno y aluminio no lo convierte en negocio de materias primas, aunque la hoja lo clasifique como cíclico.
    El DCF de caja libre al accionista de la plantilla, con la caja libre normalizada a un capex de mantenimiento separado y el múltiplo de salida implícito (14,6x) contrastado con el P/FCF histórico (19,0–26,8x).

### calidad

    Es un negocio de consumo básico que se entiende, pero el ROCE LTM del 14,5% (ROIC después de impuestos del 11,6%, casi la tasa de su test de deterioro), el margen bruto plano (37,47% → 37,11%) y el orgánico casi nulo (+0,4% l-f-l) no demuestran foso; lo marco dudoso y no no_pasa como la etapa 1 (C18 = No), porque la falta de cuotas publicadas es ausencia de dato, no prueba en contra.
    Dato clave: Análisis!C24 = 0.145

### caja

    La caja libre del accionista fue positiva todos los años (FY21 15,5 · FY22 7,3 · FY23 47,0 · FY24 37,5 · FY25 32,4 · LTM 31,0) y la caja operativa cubre 1,21 veces el beneficio neto (Análisis!C26), aunque la base de 38,29 de la hoja (frente a 38 en la respuesta) se apoya en un FY23 con capex de solo 0,5x la amortización y la media de 5 años sería 27,95.
    Dato clave: Análisis!C52 = 38.29

### balance

    El 0,82x de la hoja (Análisis!C33) incluye 38,36 de arrendamientos y no sirve tal cual; sin ellos, la deuda financiera es 63,75 menos 29,84 de caja, es decir, 33,91 de deuda neta, que sobre el EBITDA tras alquiler estimado de 80,48 da unos 0,42x, holgado para un negocio de consumo básico, aunque la deuda subió desde 42,00 en dic-25 y hay una línea de 120 sin disponer.
    Dato clave: Control maestro!M51 = 63.75

### precio

    A 12,06 € la cotización está muy por encima del precio de Sí (mín(6,19; ¾×9,85) = 6,19 €, con la hoja y no con los 6,14 € de la respuesta), por encima del ponderado de 9,85 € (margen −22%) y exige un crecimiento del 6,2% frente al 3% normal; ni con r al 7% (13,98 €) la cotización se acerca al precio de Sí.
    Dato clave: Análisis!C37 = 12.06

### encaje

    El paquete no trae la cartera de la persona responsable y la hoja solo aporta datos de la empresa (capitalización de 758,33 mm), así que el encaje no se puede juzgar y no elimina.
    Dato clave: Análisis!C41 = 758.33

### Qué lo cambiaría

    - Una cotización que se acerque al precio de Sí de unos 6,2 € (escenario malo, Análisis!B78) pasaría el veredicto a estudiar_a_fondo.
    - Un margen bruto por debajo del 36%, ventas orgánicas en caída o el private label en pérdidas otra vez en la actualización de 9M-2026 pasarían el veredicto a descartar por calidad.
    - Una disposición de la línea de 120 mm de Alpha Bank para una compra grande que lleve la deuda neta sin arrendamientos por encima de unas 2x el EBITDA tras alquiler.

### Qué falta

    - Cuotas de mercado por categoría y país, competidores y margen bruto por segmento, sin los que no se puede cerrar el filtro de calidad.
    - Reparto del capex entre mantenimiento y crecimiento; además, el EBITDA tras alquiler (80,48) es una estimación de la hoja (EBITDA menos pagos de arrendamientos LTM).
    - La actualización de 9M-2026 (10-nov-2026) es posterior a la fecha de la hoja y no figura en el paquete.

### Comprobaciones mecánicas y normalizaciones

    {
      "comprobaciones": {
        "avisos": [],
        "nota": "Comprobaciones mecánicas informativas: no acreditan la calidad económica."
      },
      "normalizaciones": []
    }

