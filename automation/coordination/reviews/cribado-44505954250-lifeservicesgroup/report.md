# Cribado · Lifeservicesgroup

Estado de la ejecución: `AUDITORIA_DOCUMENTAL_PENDIENTE_ACEPTACION`

Cribado pendiente de revisión humana. No es una recomendación de compra, ni aceptación, ni aptitud para dinero real. Tasa 9 % provisional.

C-ARR (decisión de la persona responsable): los arrendamientos se cuentan una sola vez, en el flujo. El alquiler se resta de la caja libre; la deuda, deuda/EBITDA y deuda/caja libre se miden sin arrendamientos; el pasivo por arrendamientos se muestra aparte, como dato.

Cifras de la etapa 1 tal como las guardó la hoja, a su fecha de análisis; sin las decisiones posteriores (P-O1, P-O2, F1-A/F1-B, D-US1/2, D-WM) ni verificación contra la fuente oficial.

| Campo | Valor |
|---|---|
| Fecha de la hoja | 2026-11-04 |
| Tarea | cribado-44505954250-lifeservicesgroup |
| SHA del código | 833cd50a9bba34006519119c72a29c70a1656fb7 |
| Huella del paquete (package_sha256) | 3f84997f3c3204b64d44ca643f1c4c1c48d56ccd49ab63a281a9f2d5e56a61f6 |
| Huella del envío (bundle_sha256) | ebbde6dea87d61cfc77cdcb430407846265fd34fb69e08d6cb622cfb3c9b8486 |
| Huella del encargo | 32b5c7f313e61a61fb0f5e68a75b3c44004eb902e97b98720fb98fa8d383e6cf |
| Huella de la Release | 4d30f7352948fe7e7fe3b133386eabedbddcc71d997e972a1c6db7964d58b0a9 |
| Huella del libro | 08cf2683a34af7c05fe4d3ca35f34ee82bc9d2925b118bbd39ff89d75957f35b |
| Modelo pedido / devuelto | claude-opus-5-5 / claude-opus-5-5 |
| Esfuerzo | high |
| Gramática del servidor | True |
| Mensajes enviados | 1 |
| Cota de entrada antes de llamar | 131170 tokens |
| Reserva estimada antes de llamar | USD 1.18004 |
| Uso de tokens | entrada 58843, salida 2559 |
| Coste | CONOCIDO_ESTIMADO; estimado USD 0.286552; cota 0.286552 |

| id | ruta | sha256 | bytes |
|---|---|---|---|
| respuesta | EMPRESAS_LOTES_COMPLETOS/Lifeservicesgroup/Lifeservicesgroup_respuesta.md | 4bd5b2444b4f76f4c738257618df1821d9eb6389363407e714d4e993786739c4 | 32205 |
| hoja_analisis | EMPRESAS_LOTES_COMPLETOS/Lifeservicesgroup/Lifeservicesgroup_evaluada.xlsx#Análisis | d5f0777a4495b92a983584e79436b929a2c99bfb0510f8136f26d094e70f3c2f | 23132 |
| hoja_control_maestro | EMPRESAS_LOTES_COMPLETOS/Lifeservicesgroup/Lifeservicesgroup_evaluada.xlsx#Control maestro | a3086179d8a2503553fb03a7dc63a6b9b8cdf0600eb456cdd31562a38cbb7013 | 54936 |

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

    Control maestro!M51 = 81.6 (arrendamientos a principal, 26-dic-2025)


### Tipo de negocio y motor

    Servicios funerarios en el Reino Unido (funerales, crematorios, planes prepagados y herencias) en situación de reestructuración, muy apalancado y analizado por transparencia vía Castelnau.
    Suma de partes (crematorios, inmuebles en propiedad y excedente liberable de los Trusts menos la deuda externa y los préstamos PIK por delante) o caja normalizada pro forma de la estructura posterior a 2025, no el DCF de la plantilla con caja negativa.

### calidad

    El negocio se entiende (Análisis!C11 = Sí), pero el ROCE del 8,5% queda por debajo del 9%, el margen EBITDA ha caído del 37,0% al 14,1% y los funerales pierden cuota frente a la cremación directa; solo los crematorios mejoran.
    Dato clave: Análisis!C24 = 0.085

### caja

    La caja libre base del accionista (media FY23–FY25, ya neta de arrendamientos) es de -28,1, y la reducción de deuda se ha pagado con excedentes de los Trusts y ventas de inmuebles, no con caja operativa; el +9 pro forma 2026e es solo una estimación.
    Dato clave: Análisis!C52 = -28.1

### balance

    Sin arrendamientos, la deuda neta externa de 331,0 equivale a 7,7x un EBITDA post-renta de 43,2, muy por encima de lo que aguanta un negocio en declive que ya necesitó «equity cures» en 2022–2024; el 7,1x de Análisis!C33 incluye arrendamientos y no sirve tal cual, y además quedan detrás 389,4 de préstamos PIK de Valderrama.
    Dato clave: Control maestro!N36 = 331.0 (deuda neta externa sin arrendamientos; EBITDA post-renta 43,2 → 7,7x)

### precio

    Con caja libre negativa, el DCF de la plantilla da un valor ponderado de -426,2 frente a un precio implícito de 512,1, sin precio de Sí y con un EV/EBITDA de 16x; no es interpretable y haría falta una suma de partes (crematorios, inmuebles y excedente de los Trusts menos la deuda externa).
    Dato clave: Análisis!C83 = -426.249511504789

### encaje

    El paquete no trae la cartera y la hoja solo recoge un tamaño del 0%, que es de la etapa 1 y no se usa aquí.
    Dato clave: Análisis!C104 = 0% · No (descartada) · sin precio de Sí

### Qué lo cambiaría

    - Caja libre del accionista positiva durante varios años sin excedentes de los Trusts ni ventas de inmuebles (por ejemplo, que se confirme el +9 pro forma de 2026).
    - Deuda neta externa sin arrendamientos por debajo de 4x el EBITDA post-renta (unos 173 con un EBITDA de 43,2).
    - Un EBITDA LTM que deje de caer por debajo de 40,0 y que el EBITDA de funerales se estabilice.

### Qué falta

    - Conciliación entre los perímetros LSG, DGH y titulización (ingresos 287,9/328,8/277,5) y cuentas semestrales de LSG en 2026.
    - Términos de los préstamos PIK de Valderrama (389,4 en libros) y de las acciones M1/M2: el reparto del valor en una salida no está cuantificado.
    - El Control maestro cita decisiones del 11-nov-2026, posteriores a la fecha de la hoja (04-nov-2026): hay dudas sobre la coherencia temporal de la fuente.

### Comprobaciones mecánicas y normalizaciones

    {
      "comprobaciones": {
        "avisos": [],
        "nota": "Comprobaciones mecánicas informativas: no acreditan la calidad económica."
      },
      "normalizaciones": []
    }

