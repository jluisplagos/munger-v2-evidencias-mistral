# Cribado · Siemens

Estado de la ejecución: `AUDITORIA_DOCUMENTAL_PENDIENTE_ACEPTACION`

Cribado pendiente de revisión humana. No es una recomendación de compra, ni aceptación, ni aptitud para dinero real. Tasa 9 % provisional.

C-ARR (decisión de la persona responsable): los arrendamientos se cuentan una sola vez, en el flujo. El alquiler se resta de la caja libre; la deuda, deuda/EBITDA y deuda/caja libre se miden sin arrendamientos; el pasivo por arrendamientos se muestra aparte, como dato.

Cifras de la etapa 1 tal como las guardó la hoja, a su fecha de análisis; sin las decisiones posteriores (P-O1, P-O2, F1-A/F1-B, D-US1/2, D-WM) ni verificación contra la fuente oficial.

| Campo | Valor |
|---|---|
| Fecha de la hoja | 2026-10-11 |
| Tarea | cribado-44512238939-siemens |
| SHA del código | 833cd50a9bba34006519119c72a29c70a1656fb7 |
| Huella del paquete (package_sha256) | ffa879bcc4a4ffc277412b709d63ec591d7d3acaffc56912ff7b0fca7ea08db3 |
| Huella del envío (bundle_sha256) | 4b0f5f673caad94edda68acde9e3110fa376c8e3debe3b071309b54f96d45e61 |
| Huella del encargo | 32b5c7f313e61a61fb0f5e68a75b3c44004eb902e97b98720fb98fa8d383e6cf |
| Huella de la Release | 4d30f7352948fe7e7fe3b133386eabedbddcc71d997e972a1c6db7964d58b0a9 |
| Huella del libro | 474631315a82bbc81f576f83957e666987c95ce72e9e3d3ed2c14e5f88f65c5b |
| Modelo pedido / devuelto | claude-opus-5-5 / claude-opus-5-5 |
| Esfuerzo | high |
| Gramática del servidor | True |
| Mensajes enviados | 1 |
| Cota de entrada antes de llamar | 138867 tokens |
| Reserva estimada antes de llamar | USD 1.210828 |
| Uso de tokens | entrada 62526, salida 4743 |
| Coste | CONOCIDO_ESTIMADO; estimado USD 0.344964; cota 0.344964 |

| id | ruta | sha256 | bytes |
|---|---|---|---|
| respuesta | EMPRESAS_LOTES_COMPLETOS/Siemens/Siemens_respuesta.md | 19b8d22970360970465700ff35f99818d2cfc7dd5658ae598952949e62f68639 | 35487 |
| hoja_analisis | EMPRESAS_LOTES_COMPLETOS/Siemens/Siemens_evaluada.xlsx#Análisis | 6043dbc6af596131ab0900b7d0c2979c5ab7b6c110bd46e2f6f827e5572cabc4 | 23532 |
| hoja_control_maestro | EMPRESAS_LOTES_COMPLETOS/Siemens/Siemens_evaluada.xlsx#Control maestro | 3dee3809b5a3286690e8548af91f0fa15fd113d2ed16c4cc8abff9c2acbb4f86 | 59110 |

## Salida del modelo (datos, sin acciones ejecutables)

Veredicto `descartar` · DCF de la plantilla aplica: `dudoso`

| Filtro | Resultado |
|---|---|
| calidad | dudoso |
| caja | no_pasa |
| balance | pasa |
| precio | no_pasa |
| encaje | no_aplica |

### Pasivo por arrendamientos (dato aparte)

    Control maestro!N46 = 2085 (pasivo por arrendamientos a sep-2025); estimación de unos 2.180 m€ a jun-2026 incluida en la deuda total de 2.959 m€ (Control maestro!M51)


### Tipo de negocio y motor

    Industrial cíclico de bienes de equipo y proyectos largos (generación y transmisión eléctrica) con una base instalada de servicio, una unidad eólica en reestructuración y fuerte financiación por anticipos de clientes.
    Caja de ciclo medio normalizada sin la variación de anticipos de clientes, idealmente por suma de partes (Gas Services, Grid Technologies, Transformation of Industry, Siemens Gamesa), porque el DCF de la plantilla depende de una financiación de clientes que cambia mucho (Análisis!C62).

### calidad

    El negocio se entiende (turbinas de gas con un 66 % de ingresos de servicio, red y eólica) y los márgenes se expanden con un ROCE LTM de 0,19. Pero el ROCE medio de cinco años ronda el 0,01, hubo pérdidas netas en cuatro de siete ejercicios y Siemens Gamesa sigue con riesgo de flota, así que la ventaja no se demuestra a lo largo de un ciclo; la hoja ya marca ✗ en el foso (C18) aunque da ✓ a los márgenes (C27).
    Dato clave: Control maestro!N29 = 0.01 (ROCE medio de 5 años; LTM en Análisis!C24 = 0.19)

### caja

    La caja libre base de 1.247 m€ y la LTM de 7.172 m€ descansan en anticipos de clientes: sin su variación, la base de tres años sería de unos −2.164 m€ y la conversión caja/beneficio es de 0,5. No hay caja libre recurrente generada por el beneficio.
    Dato clave: Control maestro!N43 = -2164 (FCF base de 3 años sin variación de anticipos); Análisis!C26 = 0.5

### balance

    Sin arrendamientos, la deuda es de unos 780 m€ frente a 11.088 m€ de caja, y la propia hoja da unos −2,09x sobre un EBITDA sin alquiler de unos 4.930 m€ (Control maestro!N36). El −1,5x de Análisis!C33 incluye arrendamientos y no sirve tal cual. Pasa con holgura incluso en un negocio cíclico, aunque buena parte de esa caja es contrapartida de 28.071 m€ de anticipos de clientes.
    Dato clave: Control maestro!N51 = 780 (deuda sin arrendamientos, estimación) frente a Análisis!C53 = 11088 de caja

### precio

    A 145,36 € la cotización supera el valor ponderado de 39,39 €, el escenario bueno de 85,41 € y el ponderado con r al 7 % (58,44 €), y el DCF inverso exige un 28 % de crecimiento anual. Solo con la caja LTM, que trata los anticipos como permanentes, se acercaría (la respuesta habla de unos 223 €), y eso habría que validarlo con un motor de ciclo medio.
    Dato clave: Análisis!C37 = 145.36 frente a Análisis!D78 = 85.4066537760404

### encaje

    El paquete no trae la cartera de la persona responsable y la hoja no dice nada concreto sobre encaje para una empresa de 122.061 m€ de capitalización.
    Dato clave: Análisis!C41 = 122061 (capitalización; la hoja no trae datos de cartera)

### Qué lo cambiaría

    - Que la caja del accionista sin variación de anticipos salga positiva y creciente en FY2026 y FY2027, con la ratio de pasivos por contrato sobre ventas estable.
    - Que el ROCE se mantenga por encima del 15 % durante un ciclo completo, incluida una caída de pedidos, sin nuevos cargos de calidad en Siemens Gamesa.
    - Una cotización por debajo del valor de un escenario malo calculado con una base de caja defendible.

### Qué falta

    - Condiciones de devolución de los anticipos y de las tasas de reserva, y reparto por segmento de los 28.071 m€ de pasivos por contrato.
    - Desglose del capex entre mantenimiento y crecimiento (solo hay una aproximación de unos 700 m€ de crecimiento sobre 1.724 m€ en FY2025) y una serie de más de diez años que pase por una caída de pedidos.
    - Cuentas auditadas de FY2026: la hoja usa el LTM a 30-jun-2026 y el precio de cierre del 09-oct-2026.

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

