# Cribado · TE_Connectivity

Estado de la ejecución: `AUDITORIA_DOCUMENTAL_PENDIENTE_ACEPTACION`

Cribado pendiente de revisión humana. No es una recomendación de compra, ni aceptación, ni aptitud para dinero real. Tasa 9 % provisional.

C-ARR (decisión de la persona responsable): los arrendamientos se cuentan una sola vez, en el flujo. El alquiler se resta de la caja libre; la deuda, deuda/EBITDA y deuda/caja libre se miden sin arrendamientos; el pasivo por arrendamientos se muestra aparte, como dato.

Cifras de la etapa 1 tal como las guardó la hoja, a su fecha de análisis; sin las decisiones posteriores (P-O1, P-O2, F1-A/F1-B, D-US1/2, D-WM) ni verificación contra la fuente oficial.

| Campo | Valor |
|---|---|
| Fecha de la hoja | 2026-10-11 |
| Tarea | cribado-44512238939-te-connectivity |
| SHA del código | 833cd50a9bba34006519119c72a29c70a1656fb7 |
| Huella del paquete (package_sha256) | e6527215e0fe82cfea57841944f7598f94538b5cfc05265d770ed4b42beb1c1a |
| Huella del envío (bundle_sha256) | 7e5daf5be39f0487ad47648d1702960af6902b27749e769fd776fe2e68ab9b9f |
| Huella del encargo | 32b5c7f313e61a61fb0f5e68a75b3c44004eb902e97b98720fb98fa8d383e6cf |
| Huella de la Release | 4d30f7352948fe7e7fe3b133386eabedbddcc71d997e972a1c6db7964d58b0a9 |
| Huella del libro | a832cf63f11d28030a2832b63a8894f4c654f339dd2ab38c3dfd43889680b848 |
| Modelo pedido / devuelto | claude-opus-5-5 / claude-opus-5-5 |
| Esfuerzo | high |
| Gramática del servidor | True |
| Mensajes enviados | 1 |
| Cota de entrada antes de llamar | 134557 tokens |
| Reserva estimada antes de llamar | USD 1.193588 |
| Uso de tokens | entrada 61399, salida 3170 |
| Coste | CONOCIDO_ESTIMADO; estimado USD 0.308996; cota 0.308996 |

| id | ruta | sha256 | bytes |
|---|---|---|---|
| respuesta | EMPRESAS_LOTES_COMPLETOS/TE_Connectivity/TE_Connectivity_respuesta.md | 886f84c16a0806975bf05715b752cc115a74e998ee498247b03c28be4e2df20c | 33607 |
| cambios_v2 | EMPRESAS_LOTES_COMPLETOS/TE_Connectivity/TE_Connectivity_cambios_v2.md | 91837989ca64db6456a54e51be0a314e92a335f8258dece8d8fa9abe9db4db26 | 2776 |
| hoja_analisis | EMPRESAS_LOTES_COMPLETOS/TE_Connectivity/TE_Connectivity_evaluada.xlsx#Análisis | 3c3350da5e57a6262111dfebee33ba7c537f4a17c1a3a9041ee8626496aa63d6 | 23084 |
| hoja_control_maestro | EMPRESAS_LOTES_COMPLETOS/TE_Connectivity/TE_Connectivity_evaluada.xlsx#Control maestro | 65c67279a01bab17d40f58e8ae22129c77cd44db7b08fcb2b079331a2d6771e5 | 53971 |

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

    Control maestro!M51 ≈ 491 (arrendamientos operativos, excluidos de la deuda de 5.632; pagos de 156 en doce meses ya dentro del CFO)


### Tipo de negocio y motor

    Fabricante industrial de componentes (conectores, terminales y sensores) para fabricantes, con exposición cíclica a automoción (≈41 % de las ventas) y crecimiento en redes de datos y energía.
    El DCF de caja libre de la plantilla, con FCF normalizado de ciclo medio por la exposición a automoción y restando la deuda neta para llegar al valor del accionista.

### calidad

    El negocio se entiende (C11 = Sí) y muestra ventaja en las cifras: ROIC del 16,7 % y margen operativo del 14-19 % salvo 2020. Tiene dos riesgos: automoción pesa ≈41 % y hay una erosión de precios del 1-2 % anual. Discrepo del veredicto global de la hoja («DESCARTAR · demasiado difícil»), que nace de C13 = No, una bandera de precio y no de comprensión.
    Dato clave: Análisis!C24 = 0.167

### caja

    La caja operativa equivale a 1,37 veces el beneficio neto acumulado FY2021-FY2025. El FCF tras SBC es de 2.667 de base y 3.141 en doce meses, y fue positivo todos los años de la serie. El de FY2025 se apoya en parte en impuestos pagados bajos (276 frente a 475).
    Dato clave: Análisis!C26 = 1.366

### balance

    La deuda sin arrendamientos es de 5.632 frente a 1.239 de caja. La deuda neta resultante, 4.393, equivale a 0,91 veces un EBITDA US GAAP que ya resta el alquiler (4.816). Pro forma Astrodyne sería ≤1,20x, holgado incluso para un negocio con ciclo de automoción.
    Dato clave: Análisis!C54 = 5632

### precio

    La cotización de 218,29 está claramente por encima del precio de Sí (escenario malo 127,77) y del ponderado (191,09), y descuenta un crecimiento del 8,0 % anual del FCF. Incluso a r 7 % el malo (≈175, según la respuesta) queda por debajo. Además, el DCF no resta la deuda neta de 4.393 (≈15 USD por acción).
    Dato clave: Análisis!C78 = 127.769291498758

### encaje

    El paquete no trae la cartera de la persona responsable y la hoja, más allá de la tasa de 0,09, no dice nada concreto sobre el encaje; este filtro no elimina.
    Dato clave: Análisis!C56 = 0.09

### Qué lo cambiaría

    - Una cotización en torno a 128 USD o por debajo con el negocio igual.
    - Un FCF tras SBC de FY2026 por debajo de ≈2.400, o un margen operativo de vuelta al 14-15 % sin causa cíclica.
    - Una deuda neta por encima de 3 veces el EBITDA tras Astrodyne, o un deterioro en Richards o Astrodyne.

### Qué falta

    - Resultados del 4T FY2026 (28/10/2026), posteriores a la fecha de la hoja: actualizan FCF, márgenes y deuda.
    - Desglose del capex entre mantenimiento y crecimiento (la guía sube del ≈5 % al ≈6 % de las ventas).
    - El valor por acción de la hoja no resta la deuda neta (4.393), así que el precio de Sí real sería algo menor que ≈128.

### Comprobaciones mecánicas y normalizaciones

    {
      "comprobaciones": {
        "avisos": [],
        "nota": "Comprobaciones mecánicas informativas: no acreditan la calidad económica."
      },
      "normalizaciones": []
    }

