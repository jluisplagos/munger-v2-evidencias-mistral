# Cribado · CocaCola

Estado de la ejecución: `AUDITORIA_DOCUMENTAL_PENDIENTE_ACEPTACION`

Cribado pendiente de revisión humana. No es una recomendación de compra, ni aceptación, ni aptitud para dinero real. Tasa 9 % provisional.

C-ARR (decisión de la persona responsable): los arrendamientos se cuentan una sola vez, en el flujo. El alquiler se resta de la caja libre; la deuda, deuda/EBITDA y deuda/caja libre se miden sin arrendamientos; el pasivo por arrendamientos se muestra aparte, como dato.

Cifras de la etapa 1 tal como las guardó la hoja, a su fecha de análisis; sin las decisiones posteriores (P-O1, P-O2, F1-A/F1-B, D-US1/2, D-WM) ni verificación contra la fuente oficial.

| Campo | Valor |
|---|---|
| Fecha de la hoja | 2026-10-30 |
| Tarea | cribado-44502520327-cocacola |
| SHA del código | 833cd50a9bba34006519119c72a29c70a1656fb7 |
| Huella del paquete (package_sha256) | e2132e87422ca9b8c78c66a90ba4cc9076907271a7522ac57f6b7d3ea0e137c9 |
| Huella del envío (bundle_sha256) | 4ba12fc45c7024901b2fa2d0f0eb3f9cb4cc03c2a654db4a25ae621fb820ed2e |
| Huella del encargo | 32b5c7f313e61a61fb0f5e68a75b3c44004eb902e97b98720fb98fa8d383e6cf |
| Huella de la Release | 4d30f7352948fe7e7fe3b133386eabedbddcc71d997e972a1c6db7964d58b0a9 |
| Huella del libro | ea1750efbed6a22232b7adb25c436e8965205f62527bb11c433c0d3329167501 |
| Modelo pedido / devuelto | claude-opus-5-5 / claude-opus-5-5 |
| Esfuerzo | high |
| Gramática del servidor | True |
| Mensajes enviados | 1 |
| Cota de entrada antes de llamar | 136471 tokens |
| Reserva estimada antes de llamar | USD 1.201244 |
| Uso de tokens | entrada 61785, salida 5480 |
| Coste | CONOCIDO_ESTIMADO; estimado USD 0.35674; cota 0.35674 |

| id | ruta | sha256 | bytes |
|---|---|---|---|
| respuesta | EMPRESAS_LOTES_COMPLETOS/CocaCola/CocaCola_respuesta.md | b908166f858139c6b597e9e05043ccc801dd67d81ee0a58ba64d6ba515e0b1d7 | 35992 |
| hoja_analisis | EMPRESAS_LOTES_COMPLETOS/CocaCola/CocaCola_evaluada.xlsx#Análisis | 8bc9d80bc0f8e9f623a48598efdfc09fbb2ebdc44a8629f0639d45a9f6bd9e3c | 23786 |
| hoja_control_maestro | EMPRESAS_LOTES_COMPLETOS/CocaCola/CocaCola_evaluada.xlsx#Control maestro | ba0eb2f9dad5e05e5789153a4e7465e32d2e0a523b5aba1c0856829936fb28a8 | 55976 |

## Salida del modelo (datos, sin acciones ejecutables)

Veredicto `estudiar_a_fondo` · DCF de la plantilla aplica: `dudoso`

| Filtro | Resultado |
|---|---|
| calidad | pasa |
| caja | dudoso |
| balance | pasa |
| precio | dudoso |
| encaje | no_aplica |

### Pasivo por arrendamientos (dato aparte)

    Control maestro!M36 = 1.539,9 mm TL CT (≈33,1 mm USD a 46,5747 TL/USD); fuera del cociente de deuda


### Tipo de negocio y motor

    Embotellador y distribuidor en exclusiva de las marcas de TCCC en 12 países emergentes (Türkiye y Asia Central, Pakistán, Irak, Bangladés), con contabilidad por hiperinflación (NIC 29) y exposición fuerte a divisas.
    Caja libre de ciclo medio en USD, normalizada por divisa e hiperinflación (FCF antes de intereses o con un interés real que descuente la compensación por inflación de la deuda en TL), contrastada con el FCF LTM y con una serie larga a tipos de cambio históricos.

### calidad

    Es un embotellador comprensible, con derechos exclusivos de TCCC, un ROIC del 14 % (14,4 % en USD) y un margen operativo estable en la banda del 13–16 % desde 2020 (Análisis!C27 = Estable); en contra pesan la dependencia de TCCC, a quien compra el 28 % de sus ventas, y las operaciones bajo control común sin explicar, que no bastan para rebajar la calidad; discrepo de la etapa 1 en que el riesgo de divisa sea motivo de «demasiado difícil», porque afecta al motor y al precio, no a entender el negocio.
    Dato clave: Análisis!C24 = 0.14

### caja

    CFO menos capex deja unos 263 mm USD de media en 2023–2025 (615,2 − 352,2) y el cociente CFO/beneficio es 0,99, pero tras restar 253,3 mm USD de intereses y 11,9 de arrendamientos la caja libre base queda en −2,2 mm USD; solo el LTM es positivo (221,8 mm USD), los dividendos superaron al FCF en 2024–2025 y parte del interés en TL compensa inflación, así que el estudio debe normalizarlo.
    Dato clave: Análisis!C52 = -2.19999999999996

### balance

    Sin arrendamientos, la deuda neta es unos 28.511 mm TL CT sobre un EBITDA pre-NIIF 16, lo que da 0,65x (la hoja muestra 0,67x en Análisis!C33, pero esa cifra incluye arrendamientos); la caja cubre la deuda a corto 1,18x (≈0,92x en el estrés de caja atrapada), así que pasa con holgura incluso para un negocio expuesto a divisas, con la vigilancia de la deuda en TL a corto y del 57 % de la deuda en USD.
    Dato clave: Control maestro!M36 = deuda financiera 56.449,1 mm TL CT sin arrendamientos (≈1.212 mm USD a 46,5747); deuda neta sin arrendamientos 28.511,2 mm TL CT (≈612 mm USD) → 0,65x EBITDA pre-NIIF 16 (Control maestro!N36)

### precio

    El DCF de la plantilla da un valor ponderado negativo (−0,0146 USD, Análisis!C83) porque parte de un FCF base de −2,2, no hay precio de Sí y las sensibilidades de tasa (filas 90–92) no tienen valor calculado; con el FCF LTM de 221,8 mm USD la acción cotiza a 19,2x frente a un P/FCF histórico de 11,1x (rentabilidad por FCF ≈5,2 %), y la estimación de la etapa 1 sobre esa base (ponderado ≈1,47 USD) queda cerca del precio de 1,5221 USD: no se puede concluir sin el motor adecuado.
    Dato clave: Análisis!C37 = 1.5221

### encaje

    El paquete no trae la cartera de la persona responsable y solo consta una capitalización de 4.259,1 mm USD, que no basta para juzgar el encaje; este filtro no elimina.
    Dato clave: Análisis!C41 = 4259.1

### Qué lo cambiaría

    - Que el FCF tras intereses del ejercicio 2026 completo vuelva a ser ≤ 0 en USD mientras se pagan dividendos: la caja no pasaría y el veredicto sería descartar.
    - Que el FCF normalizado en USD no supere los 221,8 mm USD del LTM con la cotización por encima de 1,52 USD (≈19x FCF frente a 11,1x histórico): el veredicto pasaría a vigilar.
    - Que la deuda neta sin arrendamientos supere 2x el EBITDA o que la caja deje de cubrir la deuda a corto (hoy 1,18x).

### Qué falta

    - Serie de FCF en USD de 2016–2025 a tipos de cambio históricos, tras intereses y con intereses reales, para saber si la caja libre es recurrente.
    - Condiciones de los Bottler's Agreements con TCCC (fecha de renovación y fijación del precio del concentrado) y detalle de las compras de 2021 y 2023 y de las operaciones bajo control común de 2024.
    - La Control maestro cita decisiones del 08-nov-2026 (C37, C40, C26), posteriores a la fecha de la hoja (2026-10-30), y las celdas de sensibilidad Análisis!B90:D92 no tienen valor calculado: conviene confirmar la versión.

### Comprobaciones mecánicas y normalizaciones

    {
      "comprobaciones": {
        "avisos": [
          "Filtro calidad: motivo de más de 400 caracteres.",
          "Filtro balance: motivo de más de 400 caracteres.",
          "Filtro precio: motivo de más de 400 caracteres."
        ],
        "nota": "Comprobaciones mecánicas informativas: no acreditan la calidad económica."
      },
      "normalizaciones": []
    }

