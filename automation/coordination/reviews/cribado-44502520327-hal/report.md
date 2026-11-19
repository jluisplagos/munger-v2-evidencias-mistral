# Cribado · Hal

Estado de la ejecución: `AUDITORIA_DOCUMENTAL_PENDIENTE_ACEPTACION`

Cribado pendiente de revisión humana. No es una recomendación de compra, ni aceptación, ni aptitud para dinero real. Tasa 9 % provisional.

C-ARR (decisión de la persona responsable): los arrendamientos se cuentan una sola vez, en el flujo. El alquiler se resta de la caja libre; la deuda, deuda/EBITDA y deuda/caja libre se miden sin arrendamientos; el pasivo por arrendamientos se muestra aparte, como dato.

Cifras de la etapa 1 tal como las guardó la hoja, a su fecha de análisis; sin las decisiones posteriores (P-O1, P-O2, F1-A/F1-B, D-US1/2, D-WM) ni verificación contra la fuente oficial.

| Campo | Valor |
|---|---|
| Fecha de la hoja | 2026-11-05 |
| Tarea | cribado-44502520327-hal |
| SHA del código | 833cd50a9bba34006519119c72a29c70a1656fb7 |
| Huella del paquete (package_sha256) | 699a547ddd4733b4d2730d9a9ca4624dbd0d361a58716898de7e00ae83a174d9 |
| Huella del envío (bundle_sha256) | 9283aa40ccc9bb49d52f6cec2ff3b40272da8b8a7f03cf1ad4bf12827d026a40 |
| Huella del encargo | 32b5c7f313e61a61fb0f5e68a75b3c44004eb902e97b98720fb98fa8d383e6cf |
| Huella de la Release | 4d30f7352948fe7e7fe3b133386eabedbddcc71d997e972a1c6db7964d58b0a9 |
| Huella del libro | f002c8cb92523f45c5d9f3802ef9b4ad8b0fb29051728a0c767c6499ba0458e9 |
| Modelo pedido / devuelto | claude-opus-5-5 / claude-opus-5-5 |
| Esfuerzo | high |
| Gramática del servidor | True |
| Mensajes enviados | 1 |
| Cota de entrada antes de llamar | 127789 tokens |
| Reserva estimada antes de llamar | USD 1.166516 |
| Uso de tokens | entrada 57760, salida 3954 |
| Coste | CONOCIDO_ESTIMADO; estimado USD 0.31012; cota 0.31012 |

| id | ruta | sha256 | bytes |
|---|---|---|---|
| respuesta | EMPRESAS_LOTES_COMPLETOS/Hal/Hal_respuesta.md | d9070900ee12e2f763437fc390c819469ba9fa092cc7ac32010a545bc9ab612b | 30413 |
| hoja_analisis | EMPRESAS_LOTES_COMPLETOS/Hal/Hal_evaluada.xlsx#Análisis | 544a056556c6868ba58e31a48b84cf4d22bca230cee7590fa2f8e64b17909e9f | 23384 |
| hoja_control_maestro | EMPRESAS_LOTES_COMPLETOS/Hal/Hal_evaluada.xlsx#Control maestro | 064a7a60ba8be0f6e1caa75b9b52b06744848ae51b36c1a7c7184c64f76dc6ba | 53320 |

## Salida del modelo (datos, sin acciones ejecutables)

Veredicto `vigilar` · DCF de la plantilla aplica: `no`

| Filtro | Resultado |
|---|---|
| calidad | dudoso |
| caja | dudoso |
| balance | pasa |
| precio | dudoso |
| encaje | no_aplica |

### Pasivo por arrendamientos (dato aparte)

    Control maestro!M51 = 1102.9 (pasivos por arrendamiento a 30-06-2026, aparte de la deuda)


### Tipo de negocio y motor

    Holding de inversión diversificado con participaciones de control (dragado y offshore de Boskalis, terminales de Vopak, óptica de Safilo, cotizadas y más de veinte no cotizadas), cuyo valor depende del ciclo y de la suma de partes.
    Suma de partes sobre el NAV (cotizadas a mercado, Boskalis a mitad de ciclo, no cotizadas valoradas y cartera líquida), menos costes de la matriz, comparada con el descuento histórico sobre el NAV.

### calidad

    La estructura de holding se entiende y los márgenes EBITDA se mantienen en torno al 20 % (Análisis!C27 «Estable»), pero el ROCE de 11.7 % es en parte de ciclo récord de Boskalis (33 % del NAV) y el NAV más dividendos ha crecido solo un 3,9-6,7 % anual, por debajo del 9 %; por eso no lo dejo en «demasiado difícil» como la etapa 1, sino en duda de calidad.
    Dato clave: Análisis!C24 = 0.117

### caja

    El FCF consolidado es positivo todos los años (337/322/995/1020/1281 en 2021-2025) y la conversión CFO/beneficio es de 1.11, pero la base de 1088.6 incluye 586 de circulante en 2023-2025 e integra el 100 % de Vopak y Safilo, de modo que no mide la caja que llega al holding.
    Dato clave: Análisis!C52 = 1088.6

### balance

    Sin arrendamientos, la deuda financiera de 3710.4 queda por debajo de la caja de 4461.4, lo que da una caja neta de 751.0 (Control maestro!N36), así que el cociente sin arrendamientos es negativo y pasa con holgura incluso para un grupo cíclico; el 0.14x de Análisis!C33 incluye la NIIF 16 y no se usa tal cual, aunque la matriz no tiene deuda y unos 61 % de la deuda es de Vopak.
    Dato clave: Control maestro!M51: deuda financiera sin arrendamientos = 3710.4 (frente a caja Análisis!C53 = 4461.4)

### precio

    A 173.2 la cotización está claramente por encima del escenario malo de 122.85 que sirve de precio de Sí y por debajo del ponderado de 195.67, que cae a 150.69 con r + 2 puntos; como el DCF de la plantilla no aplica (C62), haría falta una suma de partes: el descuento del 11-12 % sobre el NAV es menor que su mediana del 22 % (precio hacia 154 €).
    Dato clave: Análisis!C37 = 173.2 (escenario malo Análisis!B78 = 122.85)

### encaje

    El paquete no trae la cartera de la persona responsable y la hoja solo recoge una cifra de posición de la etapa 1 (C104) que no se usa aquí; este filtro no elimina.
    Dato clave: Análisis!C104 = 0% · Demasiado difícil · sin posición

### Qué lo cambiaría

    - Una cotización en torno a 154 € o menos (descuento sobre el NAV en su mediana del 22 %) o por debajo de 122.85 €.
    - Que el FCF sin circulante se mantenga por encima de 1.000 en un año flojo de Boskalis.
    - Una caída fuerte de Boskalis en la declaración del tercer trimestre que rebaje el NAV y la caja base.

### Qué falta

    - FCF proporcional o caja que llega de verdad al holding (dividendos de participadas más rendimiento de la cartera líquida, menos costes de la matriz).
    - Series de Boskalis por división (utilización, márgenes, cartera) para estimar su beneficio de mitad de ciclo, y estimación del valor de las no cotizadas (8.431 a valor contable).
    - Fuentes con fechas posteriores al corte: la respuesta y las decisiones del inversor en Control maestro (C46, C47, C49) llevan fecha 10-11-2026, posterior a la hoja del 05-11-2026.

### Comprobaciones mecánicas y normalizaciones

    {
      "comprobaciones": {
        "avisos": [],
        "nota": "Comprobaciones mecánicas informativas: no acreditan la calidad económica."
      },
      "normalizaciones": []
    }

