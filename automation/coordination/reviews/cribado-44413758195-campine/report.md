# Cribado · Campine

Estado de la ejecución: `AUDITORIA_DOCUMENTAL_PENDIENTE_ACEPTACION`

Cribado pendiente de revisión humana. No es una recomendación de compra, ni aceptación, ni aptitud para dinero real. Tasa 9 % provisional.

C-ARR (decisión de la persona responsable): los arrendamientos se cuentan una sola vez, en el flujo. El alquiler se resta de la caja libre; la deuda, deuda/EBITDA y deuda/caja libre se miden sin arrendamientos; el pasivo por arrendamientos se muestra aparte, como dato.

Cifras de la etapa 1 tal como las guardó la hoja, a su fecha de análisis; sin las decisiones posteriores (P-O1, P-O2, F1-A/F1-B, D-US1/2, D-WM) ni verificación contra la fuente oficial.

| Campo | Valor |
|---|---|
| Fecha de la hoja | 2026-10-30 |
| Tarea | cribado-44413758195-campine |
| SHA del código | 833cd50a9bba34006519119c72a29c70a1656fb7 |
| Huella del paquete (package_sha256) | 37d59fdf3ac3e48cb22f46d51bdaa7b31991a8c90442f9899fd0872d5e2eb512 |
| Huella del envío (bundle_sha256) | 5a38d921031570067b4402dc6eb51c2897aed31633ea32b6576095e6b402af23 |
| Huella del encargo | 32b5c7f313e61a61fb0f5e68a75b3c44004eb902e97b98720fb98fa8d383e6cf |
| Huella de la Release | 4d30f7352948fe7e7fe3b133386eabedbddcc71d997e972a1c6db7964d58b0a9 |
| Huella del libro | 2f377adff40a08c2f917452e6dd62b4567e96742ee4e544be2f94f6ac696bceb |
| Modelo pedido / devuelto | claude-opus-5-5 / claude-opus-5-5 |
| Esfuerzo | high |
| Gramática del servidor | True |
| Mensajes enviados | 1 |
| Cota de entrada antes de llamar | 121420 tokens |
| Reserva estimada antes de llamar | USD 1.14104 |
| Uso de tokens | entrada 54626, salida 4708 |
| Coste | CONOCIDO_ESTIMADO; estimado USD 0.312664; cota 0.312664 |

| id | ruta | sha256 | bytes |
|---|---|---|---|
| respuesta | EMPRESAS_LOTES_COMPLETOS/Campine/Campine_respuesta.md | 41e0ad50b6cc6c9f0b54ca6d6ba7fe4db7fded4238091d40a7015b95bd413f7b | 29747 |
| hoja_analisis | EMPRESAS_LOTES_COMPLETOS/Campine/Campine_evaluada.xlsx#Análisis | 67500f332f2503380ba0b1757177be6c0516f9799873422b4fccb31d472ab59b | 22830 |
| hoja_control_maestro | EMPRESAS_LOTES_COMPLETOS/Campine/Campine_evaluada.xlsx#Control maestro | 92ac638658b748631e9d90f5ee4e08def204a26771703b07387af770310efb13 | 48153 |

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

    Control maestro!M51: arrendamientos 1,9 mm a 30/06/2026 (incluidos en Análisis!C54 = 9.4; excluidos del cociente de deuda)


### Tipo de negocio y motor

    Transformador cíclico ligado a materias primas: química especializada de antimonio (trióxido de antimonio, masterbatches retardantes) y reciclaje de plomo y baterías, con precios de venta que siguen al metal.
    Caja o beneficio de ciclo medio normalizado sobre un ciclo completo del antimonio y del plomo (margen por tonelada con circulante neutral), contrastado con el valor de los activos (patrimonio 152,2 mm, ≈101 €/acción).

### calidad

    El negocio se entiende, pero el ROCE de 0,33 es una estimación 2026E antes de impuestos sobre precios de pico, frente a ≈15 % después de impuestos en FY19–23 y márgenes EBIT de 1–8 % hasta 2023, con dependencia del antimonio y de la política china; además, el ✓ de márgenes «Expandiendo» de la hoja (C27) refleja precio del metal, no poder de precio.
    Dato clave: Análisis!C24 = 0.33

### caja

    La conversión del beneficio en caja es de 0,81 en 2021–2025 y la caja libre anual oscila entre −6,9 y 29,3 mm, con cuatro años negativos de diez porque el circulante sigue al metal; la base de 15,1 mm es positiva pero no recurrente ni estable.
    Dato clave: Análisis!C26 = 0.81

### balance

    Sin arrendamientos hay caja neta de unos 13,6 mm (−0,19x EBITDA LTM de 73,4, que apenas cambia por un alquiler inmaterial de 0,4–0,8 mm) con 77,6 mm de líneas no dispuestas, holgado incluso para un cíclico; el pico estacional con factoring (≈0,8x a 30/06/2025) y la compra Flamaway, sin precio publicado, son lo único a vigilar.
    Dato clave: Análisis!C54 = 9.4 (menos arrendamientos 1,9 = deuda bancaria 7,5; deuda neta sin arrendamientos 7,5 − 21,1 = −13,6 sobre EBITDA LTM 73,4 = −0,19x, Control maestro!N36)

### precio

    A 175 € la cotización está un 10 % por encima del ponderado de 159,5 € y del normal de 158,0 €, la hoja no tiene precio de Sí operativo, el resultado se invierte con r −2 puntos (226,4 €) y el DCF de la plantilla no aplica a un cíclico, así que hace falta valorar con caja de ciclo medio (por ejemplo, FCF medio a 5 años de 10,2 mm, rendimiento del 3,9 %).
    Dato clave: Análisis!C83 = 159.521561878503

### encaje

    El paquete no trae la cartera; la hoja solo aporta un dato concreto de liquidez muy baja (≈270 acciones/día, free float 28,14 %), que no elimina en el cribado.
    Dato clave: Control maestro!N38: liquidez ≈270 acciones/día (72 el 29/10/2026)

### Qué lo cambiaría

    - Una cotización por debajo de ≈123 € (ponderado con r +2 puntos, Análisis!C92) o cerca del valor contable de ≈101 €/acción.
    - Resultados del segundo semestre de 2026 con el antimonio a ≈18.000 USD/t que muestren margen por tonelada y caja con circulante neutral por encima de FY19–23 (pasaría calidad y caja).
    - Que Flamaway se pague con deuda que lleve la deuda neta sin arrendamientos por encima de ≈1,5x un EBITDA de ciclo medio.

### Qué falta

    - Margen por tonelada de ATO, masterbatches y plomo a lo largo de un ciclo completo de precios (no se publica), necesario para la caja de ciclo medio.
    - Precio y forma de pago de Flamaway (cierre previsto el 01/10/2026, anterior a la fecha de la hoja) que no figuran en deuda ni EBITDA.
    - Duda de fuentes: Control maestro recoge decisiones del inversor fechadas el 08-nov-2026, posteriores a la fecha de la hoja (30/10/2026), y la respuesta dice no tener la hoja aunque sus cifras coinciden.

### Comprobaciones mecánicas y normalizaciones

    {
      "comprobaciones": {
        "avisos": [],
        "nota": "Comprobaciones mecánicas informativas: no acreditan la calidad económica."
      },
      "normalizaciones": []
    }

