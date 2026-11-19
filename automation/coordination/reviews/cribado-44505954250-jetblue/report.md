# Cribado · JetBlue

Estado de la ejecución: `AUDITORIA_DOCUMENTAL_PENDIENTE_ACEPTACION`

Cribado pendiente de revisión humana. No es una recomendación de compra, ni aceptación, ni aptitud para dinero real. Tasa 9 % provisional.

C-ARR (decisión de la persona responsable): los arrendamientos se cuentan una sola vez, en el flujo. El alquiler se resta de la caja libre; la deuda, deuda/EBITDA y deuda/caja libre se miden sin arrendamientos; el pasivo por arrendamientos se muestra aparte, como dato.

Cifras de la etapa 1 tal como las guardó la hoja, a su fecha de análisis; sin las decisiones posteriores (P-O1, P-O2, F1-A/F1-B, D-US1/2, D-WM) ni verificación contra la fuente oficial.

| Campo | Valor |
|---|---|
| Fecha de la hoja | 2026-10-08 |
| Tarea | cribado-44505954250-jetblue |
| SHA del código | 833cd50a9bba34006519119c72a29c70a1656fb7 |
| Huella del paquete (package_sha256) | 1948c2a95046106062919e4f94b49ad14732dc30afaec5bf444b200e765f5baa |
| Huella del envío (bundle_sha256) | 93804eb38ee0c17bb2af4e7f70bc6b68570e66283116ba7acc5110a1853a4dd6 |
| Huella del encargo | 32b5c7f313e61a61fb0f5e68a75b3c44004eb902e97b98720fb98fa8d383e6cf |
| Huella de la Release | 4d30f7352948fe7e7fe3b133386eabedbddcc71d997e972a1c6db7964d58b0a9 |
| Huella del libro | 4f40a510017ec485afacedb3c363d307350dfae536ba38b219fcb18f7fe70aea |
| Modelo pedido / devuelto | claude-opus-5-5 / claude-opus-5-5 |
| Esfuerzo | high |
| Gramática del servidor | True |
| Mensajes enviados | 1 |
| Cota de entrada antes de llamar | 140660 tokens |
| Reserva estimada antes de llamar | USD 1.218 |
| Uso de tokens | entrada 63293, salida 2946 |
| Coste | CONOCIDO_ESTIMADO; estimado USD 0.312092; cota 0.312092 |

| id | ruta | sha256 | bytes |
|---|---|---|---|
| respuesta | EMPRESAS_LOTES_COMPLETOS/JetBlue/JetBlue_respuesta.md | c47f760da7aff1830d9cb34ce384cf5c22714ac3f1bfadf543c82f24fe071ba4 | 35258 |
| cambios_v2 | EMPRESAS_LOTES_COMPLETOS/JetBlue/JetBlue_cambios_v2.md | 952c8334c52bab75de8cdc820a4323c8e124617dbb1e62425bcc4064e0bf0cc2 | 4144 |
| hoja_analisis | EMPRESAS_LOTES_COMPLETOS/JetBlue/JetBlue_evaluada.xlsx#Análisis | 000c46a9474bfafe2749f36345dfd23c13262d7ca435b35d09f946a14d881882 | 23170 |
| hoja_control_maestro | EMPRESAS_LOTES_COMPLETOS/JetBlue/JetBlue_evaluada.xlsx#Control maestro | 661e92d4c0b9379724cbc5d325ac49ea58f7a39090004a45ad24f3018c717495 | 57096 |

## Salida del modelo (datos, sin acciones ejecutables)

Veredicto `descartar` · DCF de la plantilla aplica: `no`

| Filtro | Resultado |
|---|---|
| calidad | no_pasa |
| caja | no_pasa |
| balance | no_pasa |
| precio | no_aplica |
| encaje | no_aplica |

### Pasivo por arrendamientos (dato aparte)

    Arrendamientos operativos de 908 aparte de la deuda, más 431 de finance leases incluidos en la deuda de Análisis!C54 (Control maestro!N51 = 908 y 431; total ≈ 1.339).


### Tipo de negocio y motor

    Aerolínea de pasajeros (transporte aéreo, con programa de fidelización TrueBlue): negocio cíclico de tipo commodity, en reestructuración (plan JetForward).
    Caja libre de ciclo completo o valor de los activos (flota y TrueBlue) frente a la deuda, porque es una aerolínea cíclica con una caja libre base negativa que el DCF de la plantilla no puede representar.

### calidad

    El negocio se entiende (vende asientos y puntos TrueBlue), pero no muestra ventaja en las cifras: ROCE del −4,6 % en los últimos doce meses, márgenes operativos negativos de 2020 a 2025 y comprimiéndose (C27), sin foso (C18 = No) y con una asignación de capital dudosa (C98).
    Dato clave: Análisis!C24 = -0.046

### caja

    La caja libre base de la plantilla es de −1.230 (media 2023-2025) y la de los últimos doce meses, de −1.225 (C40), con una caja operativa media de solo 150 frente a un capex de 1.315,7: el negocio no convierte en caja de forma recurrente.
    Dato clave: Análisis!C52 = -1230

### balance

    Sin arrendamientos, la deuda neta de unos 6.027 frente a un EBITDA LTM de solo 146 da unas 41x, muy por encima de cualquier límite razonable para un negocio cíclico; la caja libre negativa hace que la deuda/caja libre ni se pueda calcular, y en 2029 vencen 1.835; el 44,2x de C33 incluye finance leases y la hoja manda sobre los 6.310 de deuda neta de la respuesta.
    Dato clave: Análisis!C54 = 8478 (incluye 431 de finance leases, Control maestro!N51); deuda sin arrendamientos ≈ 8047; deuda neta sin arrendamientos ≈ 6027 (8047 − caja 1656 − inversiones a corto 364)

### precio

    El DCF de la plantilla no aplica porque la base de caja libre es negativa (valor ponderado de −45,75 en C83 y de −55,11 en el escenario malo, C78), así que no hay precio de Sí con el que comparar la cotización de 3,97; haría falta una caja de ciclo medio o un valor de los activos frente a la deuda, y además la hoja es anterior a los resultados del 3T26.
    Dato clave: Análisis!C37 = 3.97

### encaje

    El paquete no trae la cartera de la persona responsable y la hoja solo recoge en C104 un tamaño de etapa 1 que no se hereda, así que este filtro no aplica y no elimina.
    Dato clave: Análisis!C104 = 0% · No · sin precio de Sí (la fórmula da valor negativo)

### Qué lo cambiaría

    - Dos años seguidos de caja libre positiva después de capex y PDP, sin ventas de activos ni sale-leasebacks.
    - Una deuda neta sin arrendamientos por debajo de unas 4x un EBITDA positivo y creciente, en lugar de los ≈6.027 sobre 146 actuales.
    - Tres años seguidos de margen operativo positivo con ROCE por encima del 9 %.

### Qué falta

    - Resultados del 3T26 (previstos el 27/10/2026), posteriores a la fecha de la hoja y no incluidos en el paquete.
    - Importe de la liquidez mínima exigida en las cláusulas de TrueBlue y margen hasta incumplirlas (Control maestro!N36: no localizado).
    - El EBITDA después de restar los pagos de finance leases, porque el principal de los últimos doce meses (≈96) es una estimación; no cambia la conclusión.

### Comprobaciones mecánicas y normalizaciones

    {
      "comprobaciones": {
        "avisos": [],
        "nota": "Comprobaciones mecánicas informativas: no acreditan la calidad económica."
      },
      "normalizaciones": []
    }

