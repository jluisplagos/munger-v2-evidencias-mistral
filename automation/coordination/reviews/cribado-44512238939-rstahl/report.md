# Cribado · RStahl

Estado de la ejecución: `AUDITORIA_DOCUMENTAL_PENDIENTE_ACEPTACION`

Cribado pendiente de revisión humana. No es una recomendación de compra, ni aceptación, ni aptitud para dinero real. Tasa 9 % provisional.

C-ARR (decisión de la persona responsable): los arrendamientos se cuentan una sola vez, en el flujo. El alquiler se resta de la caja libre; la deuda, deuda/EBITDA y deuda/caja libre se miden sin arrendamientos; el pasivo por arrendamientos se muestra aparte, como dato.

Cifras de la etapa 1 tal como las guardó la hoja, a su fecha de análisis; sin las decisiones posteriores (P-O1, P-O2, F1-A/F1-B, D-US1/2, D-WM) ni verificación contra la fuente oficial.

| Campo | Valor |
|---|---|
| Fecha de la hoja | 2026-11-04 |
| Tarea | cribado-44512238939-rstahl |
| SHA del código | 833cd50a9bba34006519119c72a29c70a1656fb7 |
| Huella del paquete (package_sha256) | 908f7d6a4adc6ba87e80ba9581f9c945e074d2ff5b7e4eb2c16094bb4fd67cb6 |
| Huella del envío (bundle_sha256) | 35221610e773527ac81265aa6036aef076df5c9266ea79eb7e54d3120eb8a87c |
| Huella del encargo | 32b5c7f313e61a61fb0f5e68a75b3c44004eb902e97b98720fb98fa8d383e6cf |
| Huella de la Release | 4d30f7352948fe7e7fe3b133386eabedbddcc71d997e972a1c6db7964d58b0a9 |
| Huella del libro | fff0ca3ddce727152e3c31e65bbfd501234c7c2ac125d7111d63220dab75d3df |
| Modelo pedido / devuelto | claude-opus-5-5 / claude-opus-5-5 |
| Esfuerzo | high |
| Gramática del servidor | True |
| Mensajes enviados | 1 |
| Cota de entrada antes de llamar | 133139 tokens |
| Reserva estimada antes de llamar | USD 1.187916 |
| Uso de tokens | entrada 60912, salida 3287 |
| Coste | CONOCIDO_ESTIMADO; estimado USD 0.309388; cota 0.309388 |

| id | ruta | sha256 | bytes |
|---|---|---|---|
| respuesta | EMPRESAS_LOTES_COMPLETOS/RStahl/RStahl_respuesta.md | c92b1a7a3789e8d81fcb0f292fdba944bdb2eca0c5f0427020b07b63d8fafb69 | 32252 |
| hoja_analisis | EMPRESAS_LOTES_COMPLETOS/RStahl/RStahl_evaluada.xlsx#Análisis | d2debcf451859862f8f7e8097ee387148247df7df135746ccfa669f561aa147e | 23376 |
| hoja_control_maestro | EMPRESAS_LOTES_COMPLETOS/RStahl/RStahl_evaluada.xlsx#Control maestro | 4271ced2934216e2ad7b7fe78903d727364b81db8e4e4446b99c0e4b71734dda | 56703 |

## Salida del modelo (datos, sin acciones ejecutables)

Veredicto `descartar` · DCF de la plantilla aplica: `no`

| Filtro | Resultado |
|---|---|
| calidad | no_pasa |
| caja | no_pasa |
| balance | no_pasa |
| precio | dudoso |
| encaje | no_aplica |

### Pasivo por arrendamientos (dato aparte)

    Control maestro!M51 = 17.20 (pasivos por arrendamiento a 30-jun-2026; aparte, pensiones de 67,02 mm en Control maestro!N51)


### Tipo de negocio y motor

    Industrial cíclico (equipos eléctricos certificados de protección contra explosiones para química, farma, GNL y petróleo/gas) en situación de reestructuración o turnaround.
    Caja libre del accionista normalizada a lo largo del ciclo (media de ciclo, descontada al 9 %), restando la deuda neta sin arrendamientos y teniendo en cuenta las pensiones sin fondo, porque se trata de una industrial cíclica en reestructuración.

### calidad

    El negocio se entiende, pero en diez años no muestra ventaja en las cifras: ROCE LTM del 5,2 % (media 2019–25 del 3,9 %, frente a un WACC antes de impuestos de 12,0–12,7 %), margen EBIT comprimido del 5,8 % (2023) al 1,4 % (H1 2026), ventas de 2025 iguales a las de 2015 y dirección provisional tras dos salidas de CEO.
    Dato clave: Análisis!C24 = 0.052

### caja

    La caja libre base es de 0,15 mm (media 2023–25), la de 5 años es −4,76 mm y la serie 2016–2025 es negativa seis años de diez; el ✓ de conversión de C26 (12,4x) es mecánico porque el beneficio acumulado ronda cero, y la hoja da un CFO/EBITDA de solo 0,56x.
    Dato clave: Análisis!C52 = 0.149999999999998

### balance

    Sin arrendamientos, la deuda neta ≈ 43,75 mm sobre un EBITDA tras alquiler ≈ 24,7 mm (29,23 − 4,49) da ≈ 1,77x, en línea con la sensibilidad de la hoja (la cifra de 2,09x de C33 incluye arrendamientos y no sirve tal cual); sin embargo, para un negocio cíclico es excesiva frente a una caja libre de 0,15 mm (≈ 290x) o de 1,49 mm LTM (≈ 29x), con la deuda neta subiendo de 4,2 a 43,7 mm desde 2019, el sindicado venciendo en agosto de 2028 y 67,02 mm de pensiones sin fondo, por encima de la capitalización de 65,04 mm.
    Dato clave: Control maestro!N51 = 57.99 (préstamos sin arrendamientos; menos caja Análisis!C53 = 14.24 da deuda neta ≈ 43.75)

### precio

    La cotización de 10,1 € está muy por encima del valor ponderado de la plantilla (0,62 €; 0,89 € incluso con r al 7 %), pero ese DCF no aplica porque C62 lo marca así sobre una base casi nula; con caja normalizada de ciclo, la respuesta estima a mano ≈ 3,8–4,6 €, también por debajo del precio, y falta el informe del tercer trimestre de 2026.
    Dato clave: Análisis!C83 = 0.616182652486513

### encaje

    El paquete no trae la cartera de la persona responsable y la hoja no da un dato concreto de encaje más allá de la cotización de 10,1 €; este filtro no elimina.
    Dato clave: Análisis!C37 = 10.1

### Qué lo cambiaría

    - Dos años seguidos de caja libre del accionista por encima de unos 5,5 mm, con la deuda neta sin arrendamientos bajando con caja propia desde 43,7 mm.
    - Un margen EBIT sostenido por encima del 10 % durante un ciclo, que eleve el ROCE claramente por encima del 5,2 %.
    - Un refinanciamiento del sindicado de 2028 sin tensión, junto con una reducción material de las pensiones sin fondo de 67 mm.

### Qué falta

    - El informe del tercer trimestre de 2026 (previsto para el 10-nov-2026, después de la fecha de la hoja): no se sabe si la guía de 2026, la deuda y los inventarios se mantienen.
    - Los niveles numéricos de los covenants del sindicado que vence en agosto de 2028 y su holgura; tampoco constan los competidores ni sus cuotas.
    - Incoherencia de fechas: Control maestro cita una «decisión del inversor 11-nov-2026» sobre el periodo base, posterior a la fecha de la hoja (04-11-2026).

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

