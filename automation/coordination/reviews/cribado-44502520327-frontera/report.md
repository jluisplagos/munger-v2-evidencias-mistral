# Cribado · Frontera

Estado de la ejecución: `AUDITORIA_DOCUMENTAL_PENDIENTE_ACEPTACION`

Cribado pendiente de revisión humana. No es una recomendación de compra, ni aceptación, ni aptitud para dinero real. Tasa 9 % provisional.

C-ARR (decisión de la persona responsable): los arrendamientos se cuentan una sola vez, en el flujo. El alquiler se resta de la caja libre; la deuda, deuda/EBITDA y deuda/caja libre se miden sin arrendamientos; el pasivo por arrendamientos se muestra aparte, como dato.

Cifras de la etapa 1 tal como las guardó la hoja, a su fecha de análisis; sin las decisiones posteriores (P-O1, P-O2, F1-A/F1-B, D-US1/2, D-WM) ni verificación contra la fuente oficial.

| Campo | Valor |
|---|---|
| Fecha de la hoja | 2026-10-26 |
| Tarea | cribado-44502520327-frontera |
| SHA del código | 833cd50a9bba34006519119c72a29c70a1656fb7 |
| Huella del paquete (package_sha256) | fbb8bc1a22bffcc075664d928dd9433d2986f59cc3894bc557ceaa353d06877d |
| Huella del envío (bundle_sha256) | 3de92cd4576927fdb9d34d87f7c0b15673d36b3c236ffc7c43cd50f30bd3bbb0 |
| Huella del encargo | 32b5c7f313e61a61fb0f5e68a75b3c44004eb902e97b98720fb98fa8d383e6cf |
| Huella de la Release | 4d30f7352948fe7e7fe3b133386eabedbddcc71d997e972a1c6db7964d58b0a9 |
| Huella del libro | 86e533a508870dad9bf1727471ceaa02de7b5aeb9e9f4deea46356e0cbf7adb8 |
| Modelo pedido / devuelto | claude-opus-5-5 / claude-opus-5-5 |
| Esfuerzo | high |
| Gramática del servidor | True |
| Mensajes enviados | 1 |
| Cota de entrada antes de llamar | 156907 tokens |
| Reserva estimada antes de llamar | USD 1.282988 |
| Uso de tokens | entrada 70240, salida 5564 |
| Coste | CONOCIDO_ESTIMADO; estimado USD 0.39224; cota 0.39224 |

| id | ruta | sha256 | bytes |
|---|---|---|---|
| respuesta | EMPRESAS_LOTES_COMPLETOS/Frontera/Frontera_respuesta.md | 71a6915ef1b68b96d58a9cd97cb04650776e4d06659621414534ceacd3e6a272 | 46493 |
| hoja_analisis | EMPRESAS_LOTES_COMPLETOS/Frontera/Frontera_evaluada.xlsx#Análisis | 1c78f77845336fd6fa461a56c9fccf22af5657d17636579ed7c4db7fece7ae3d | 23876 |
| hoja_control_maestro | EMPRESAS_LOTES_COMPLETOS/Frontera/Frontera_evaluada.xlsx#Control maestro | 29d872cde2894891ff9197375cf4669b234ee8cf814ed119774511317045a016 | 65604 |

## Salida del modelo (datos, sin acciones ejecutables)

Veredicto `faltan_datos` · DCF de la plantilla aplica: `no`

| Filtro | Resultado |
|---|---|
| calidad | dudoso |
| caja | dudoso |
| balance | dudoso |
| precio | dudoso |
| encaje | no_aplica |

### Pasivo por arrendamientos (dato aparte)

    Control maestro!M51 = 2.1 (leases IFRS 16 a 30-jun-2026, incluidos en la deuda total de 170,5); la FSRU no está en balance y entrará desde el T1-2027 por importe no publicado (estimación de la fase 1: 150–250, Control maestro!N36).


### Tipo de negocio y motor

    Holding de infraestructura energética en Colombia (situación especial tras vender el E&P): el 99,97% de Puerto Bahía con concesión hasta 2031, el 35% sin control del oleoducto ODL por puesta en equivalencia, un proyecto de GNL en desarrollo y Guyana casi a cero.
    Suma de partes: valor de las distribuciones del 35% de ODL hasta el vencimiento de su contrato, más la concesión de Puerto Bahía hasta 2031 sin perpetuidad, menos el FPI sin recurso y la deuda de Bancolombia, con el GNL tratado como opción neta de su capex y un suelo de liquidación.

### calidad

    El negocio actual se entiende (peajes con tarifa en USD indexada), pero el ROCE ajustado del 17% descansa casi entero en un 35% sin control de ODL cuyo plazo no consta, el EBITDA de infraestructura es plano (119,8/107,2/116,6), la concesión del puerto vence en 2031 y la asignación de capital es dudosa (deterioro de Guyana de 432,2), así que la durabilidad de la ventaja no se puede confirmar.
    Dato clave: Análisis!C24 = 0.17

### caja

    La caja libre base es de 23,3 (CFO 52,9 − capex 8,4 − intereses 19,1 − arrendamientos 0,8 − SBC 1,3) y es positiva, pero sale de un solo LTM del perímetro nuevo sin serie, depende de dividendos de ODL y se vuelve negativa (−23 a −4) tras la amortización obligatoria del FPI, con un capex de GNL y una FSRU que entrarán en el flujo por importe no publicado.
    Dato clave: Análisis!C52 = 23.3

### balance

    Sin arrendamientos, la deuda es 168,4 (FPI 158,4 + Bancolombia 10,0) y la neta 112,1, unas 0,96x un EBITDA ajustado de 116,8 que incluye el 35% proporcional de ODL (1,8–2,1x con EBITDA IFRS reconstruido) y unas 4,8x la caja libre de 23,3, con +20 de Bancolombia posterior al balance, amortizaciones del FPI de 37,8/44,3/30,7 que superan esa caja libre y una holgura de liquidez de 7,9, aunque el FPI no tiene recurso contra Frontera; por eso no hereda el 0,98x ✓ PASA de la hoja, que además incluye los 2,1 de arrendamientos.
    Dato clave: Análisis!C54 = 170.5 menos arrendamientos 2.1 (Control maestro!M51) = 168.4 de deuda sin arrendamientos; deuda neta 168.4 − Análisis!C53 56.3 = 112.1

### precio

    A 5,8386 la cotización está un 16% por encima del valor ponderado de 5,05 y más del doble del escenario malo de 2,72, que equivale al precio de Sí (la respuesta da 2,69 y 4,98; mandan las cifras de la hoja); además el resultado cambia dentro de ±2 puntos de tasa (7,01 a r 7% y 3,93 a r 11%) y el DCF de la plantilla no aplica, por lo que haría falta una suma de partes con los plazos de las concesiones.
    Dato clave: Análisis!C83 = 5.0463622975565

### encaje

    El paquete no trae la cartera; la hoja solo aporta una capitalización de 413,2 y una liquidez baja de 15–50 k acciones al día (Control maestro!N38), y este filtro no elimina.
    Dato clave: Análisis!C41 = 413.2

### Qué lo cambiaría

    - Que se publiquen por escrito el plazo del contrato de ODL (más allá de 2036) y la renovación de la concesión del puerto.
    - Que el importe de la FSRU y el capex del GNL se publiquen y la caja libre después de alquileres siga positiva, con una deuda neta sin arrendamientos por debajo de unas 3x la caja libre.
    - Que dos cierres del perímetro nuevo confirmen una caja libre repetible de 33–39 mm, o que la cotización caiga por debajo de 2,72 USD (valor del escenario malo en Análisis!B78).

### Qué falta

    - Plazo y tarifas del contrato de ODL y términos de renovación de la concesión de Puerto Bahía más allá de 2031.
    - Capex comprometido del GNL, importe del arrendamiento de la FSRU y umbrales de los covenants del FPI; tampoco consta qué contingencias del E&P (IRI, ANH, fiscales, ARO) quedaron en el perímetro.
    - Duda de fuente: el Control maestro cita una «decisión del inversor (28-oct-2026)», posterior a la fecha de la hoja (2026-10-26), y el T3-2026 no está publicado.

### Comprobaciones mecánicas y normalizaciones

    {
      "comprobaciones": {
        "avisos": [
          "Filtro balance: motivo de más de 400 caracteres.",
          "Filtro precio: motivo de más de 400 caracteres."
        ],
        "nota": "Comprobaciones mecánicas informativas: no acreditan la calidad económica."
      },
      "normalizaciones": []
    }

