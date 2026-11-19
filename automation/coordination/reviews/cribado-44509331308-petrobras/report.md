# Cribado · Petrobras

Estado de la ejecución: `AUDITORIA_DOCUMENTAL_PENDIENTE_ACEPTACION`

Cribado pendiente de revisión humana. No es una recomendación de compra, ni aceptación, ni aptitud para dinero real. Tasa 9 % provisional.

C-ARR (decisión de la persona responsable): los arrendamientos se cuentan una sola vez, en el flujo. El alquiler se resta de la caja libre; la deuda, deuda/EBITDA y deuda/caja libre se miden sin arrendamientos; el pasivo por arrendamientos se muestra aparte, como dato.

Cifras de la etapa 1 tal como las guardó la hoja, a su fecha de análisis; sin las decisiones posteriores (P-O1, P-O2, F1-A/F1-B, D-US1/2, D-WM) ni verificación contra la fuente oficial.

| Campo | Valor |
|---|---|
| Fecha de la hoja | 2026-10-26 |
| Tarea | cribado-44509331308-petrobras |
| SHA del código | 833cd50a9bba34006519119c72a29c70a1656fb7 |
| Huella del paquete (package_sha256) | b261d16c4e168b430e10561f282e8db896e1c529c5a8b5c9911d9e2476a7d784 |
| Huella del envío (bundle_sha256) | cc9fcd63289bd3c88f1469eb0b240aeac69a7e2da98017bc0dd880f7fa9a5882 |
| Huella del encargo | 32b5c7f313e61a61fb0f5e68a75b3c44004eb902e97b98720fb98fa8d383e6cf |
| Huella de la Release | 4d30f7352948fe7e7fe3b133386eabedbddcc71d997e972a1c6db7964d58b0a9 |
| Huella del libro | 8e7ae70f22a4eb4767520fc79ac8d7207de8b2d866978bb35a45debb9f79b8f5 |
| Modelo pedido / devuelto | claude-opus-5-5 / claude-opus-5-5 |
| Esfuerzo | high |
| Gramática del servidor | True |
| Mensajes enviados | 1 |
| Cota de entrada antes de llamar | 134525 tokens |
| Reserva estimada antes de llamar | USD 1.19346 |
| Uso de tokens | entrada 61398, salida 4932 |
| Coste | CONOCIDO_ESTIMADO; estimado USD 0.344232; cota 0.344232 |

| id | ruta | sha256 | bytes |
|---|---|---|---|
| respuesta | EMPRESAS_LOTES_COMPLETOS/Petrobras/Petrobras_respuesta.md | 82c5b04765b6aa699d6dd70c7a3daa9642288923c142f46794e1b23ec940a653 | 33197 |
| hoja_analisis | EMPRESAS_LOTES_COMPLETOS/Petrobras/Petrobras_evaluada.xlsx#Análisis | 1fa7ce9be2ff65916a1f93963f3aac114c115c467dc8fa10dd2d90dbd203e2b2 | 23865 |
| hoja_control_maestro | EMPRESAS_LOTES_COMPLETOS/Petrobras/Petrobras_evaluada.xlsx#Control maestro | 221c81242035abe23ec8ba3d57d66fd5c1ebc6795213dd2251cc65ee49ded646 | 56601 |

## Salida del modelo (datos, sin acciones ejecutables)

Veredicto `descartar` · DCF de la plantilla aplica: `no`

| Filtro | Resultado |
|---|---|
| calidad | no_pasa |
| caja | dudoso |
| balance | pasa |
| precio | dudoso |
| encaje | no_aplica |

### Pasivo por arrendamientos (dato aparte)

    Control maestro!M51 = 44972 (pasivo por arrendamientos a 30-06-2026, incluido en la deuda bruta de 70.806 de Análisis!C54); además, 18,9–20,4 bn de arrendamientos firmados sin iniciar.


### Tipo de negocio y motor

    Petrolera integrada de materias primas (E&P presal, refino y gas en Brasil), cíclica y bajo control estatal
    Caja de ciclo medio o valor de las reservas a un Brent de ciclo, restando arrendamientos, pensiones y desmantelamiento, con un descuento explícito por el riesgo del controlador estatal.

### calidad

    El negocio se entiende y el activo presal es de bajo coste, pero el ROCE (9,3 % LTM; 6,6 % en 2025, frente a un WACC real de 7,3 % en E&P) no muestra ventaja, el capex se triplicó mientras el ROCE caía, el controlador estatal capta renta (impuesto a la exportación del 12 % en 2026) y la asignación de capital es dudosa (dividendos de 7,5 bn con 5,3 bn de FCF en 2025); la etapa 1 lo llevó a «demasiado difícil», pero aquí el negocio se entiende y lo que falla es la calidad.
    Dato clave: Análisis!C24 = 0.093

### caja

    La caja libre del accionista es positiva pero inestable y decreciente: 7.813 mm LTM (CFO 40.667 − capex 20.547 − intereses 2.050 − arrendamientos 10.257), frente a 5.281 en FY25 y 19.582 de media de 5 años, sin desglose del capex de mantenimiento.
    Dato clave: Análisis!C52 = 7813

### balance

    El 1,14x de Análisis!C33 incluye 44.972 de arrendamientos y no sirve tal cual; sin ellos, la deuda neta de unos 15.416 mm sobre un EBITDA tras alquiler de unos 42.542 (52.799 − 10.257) da unos 0,36x, con plazo medio de 11,9 años, holgado incluso para un negocio cíclico (aparte quedan pensiones de 17.860 y desmantelamiento de 29.694).
    Dato clave: Control maestro!M36 = 25834 (deuda financiera sin arrendamientos; deuda neta sin arrendamientos 25834 − caja ajustada 10418 = 15416; ≈0,36x EBITDA tras alquiler según Control maestro!N36)

### precio

    La cotización de 9,94 US$ (indicativo de preapertura que la propia hoja marca como obsoleto) está por encima del valor ponderado de 9,71 y muy por encima del escenario malo de 5,01, y el ponderado va de 13,52 a 7,54 con r ±2 puntos; como el DCF de la plantilla no aplica (Análisis!C62), no sirve para concluir y haría falta una valoración por reservas o por caja de ciclo medio.
    Dato clave: Análisis!C37 = 9.94 frente a Análisis!C83 = 9.70608828995119

### encaje

    El paquete no trae la cartera y la hoja solo aporta datos generales (capitalización de 128.151 mm), así que este filtro no se evalúa y no elimina.
    Dato clave: Análisis!C41 = 128151

### Qué lo cambiaría

    - ROCE sostenido por encima del WACC con holgura (por ejemplo, más del 15 %) con un Brent medio y una paridad de precios respetada varios años.
    - Que el capex baje tras el ciclo de FPSO y la caja libre del accionista vuelva hacia la media de 3 años (13.881 mm) sin que suba la deuda.
    - Que la fórmula de dividendos pase a descontar los arrendamientos y deje de pagar más que la caja libre del accionista.

### Qué falta

    - Cotización de cierre del 26-10-2026: C37 es un indicativo de preapertura que la hoja marca como obsoleto, y hay notas de «decisión del inversor» fechadas el 01-11-2026, posteriores a la fecha de la hoja.
    - Desglose del capex entre mantenimiento y crecimiento, y una valoración por reservas a Brent de ciclo (el motor adecuado).
    - Historial de la compensación estatutaria por obligaciones de interés público y continuidad del impuesto a la exportación después del 31-12-2026.

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

