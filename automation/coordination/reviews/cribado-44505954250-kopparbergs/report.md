# Cribado · Kopparbergs

Estado de la ejecución: `AUDITORIA_DOCUMENTAL_PENDIENTE_ACEPTACION`

Cribado pendiente de revisión humana. No es una recomendación de compra, ni aceptación, ni aptitud para dinero real. Tasa 9 % provisional.

C-ARR (decisión de la persona responsable): los arrendamientos se cuentan una sola vez, en el flujo. El alquiler se resta de la caja libre; la deuda, deuda/EBITDA y deuda/caja libre se miden sin arrendamientos; el pasivo por arrendamientos se muestra aparte, como dato.

Cifras de la etapa 1 tal como las guardó la hoja, a su fecha de análisis; sin las decisiones posteriores (P-O1, P-O2, F1-A/F1-B, D-US1/2, D-WM) ni verificación contra la fuente oficial.

| Campo | Valor |
|---|---|
| Fecha de la hoja | 2026-10-31 |
| Tarea | cribado-44505954250-kopparbergs |
| SHA del código | 833cd50a9bba34006519119c72a29c70a1656fb7 |
| Huella del paquete (package_sha256) | 62f7e84fd22665a3175b8abbac89605f94b400ab09391b6747acd421e16856a1 |
| Huella del envío (bundle_sha256) | c705426195fd7eda470169cf33483e0747e6386f21ebecb01b5a9c4f82359d01 |
| Huella del encargo | 32b5c7f313e61a61fb0f5e68a75b3c44004eb902e97b98720fb98fa8d383e6cf |
| Huella de la Release | 4d30f7352948fe7e7fe3b133386eabedbddcc71d997e972a1c6db7964d58b0a9 |
| Huella del libro | 429f101d9767c3bc62a4a02bcf6c9b50ed386d0888e0015c6a00641b6f920f4f |
| Modelo pedido / devuelto | claude-opus-5-5 / claude-opus-5-5 |
| Esfuerzo | high |
| Gramática del servidor | True |
| Mensajes enviados | 1 |
| Cota de entrada antes de llamar | 127459 tokens |
| Reserva estimada antes de llamar | USD 1.165196 |
| Uso de tokens | entrada 58133, salida 3389 |
| Coste | CONOCIDO_ESTIMADO; estimado USD 0.300312; cota 0.300312 |

| id | ruta | sha256 | bytes |
|---|---|---|---|
| respuesta | EMPRESAS_LOTES_COMPLETOS/Kopparbergs/Kopparbergs_respuesta.md | 625aaae5b3007c14639242e3b35e79474c505069b7549c01ef040947dd1c26fb | 31301 |
| hoja_analisis | EMPRESAS_LOTES_COMPLETOS/Kopparbergs/Kopparbergs_evaluada.xlsx#Análisis | 3879bc3df213756095745a8a5adf54c904160719ccd5a4c3ba462671e2d8c940 | 23449 |
| hoja_control_maestro | EMPRESAS_LOTES_COMPLETOS/Kopparbergs/Kopparbergs_evaluada.xlsx#Control maestro | 485825df55ddcba359d4ca502a5fbd5e4549f198c61a652bdf66dddb7178210c | 51907 |

## Salida del modelo (datos, sin acciones ejecutables)

Veredicto `vigilar` · DCF de la plantilla aplica: `si`

| Filtro | Resultado |
|---|---|
| calidad | dudoso |
| caja | pasa |
| balance | pasa |
| precio | no_pasa |
| encaje | no_aplica |

### Pasivo por arrendamientos (dato aparte)

    No consta como pasivo en balance (K3, arrendamiento operativo como gasto, Control maestro!M46: gasto 2025 = 142.3); la hoja estima un valor actual capitalizado de ~391–413 mm SEK en Control maestro!N36.


### Tipo de negocio y motor

    Fabricante de bebidas de marca (sidra de frutas, cerveza, licores) con ventas mayoritariamente fuera de Suecia y una cadena de pubs; consumo básico maduro con exposición a la libra y a materias primas.
    El DCF de caja libre de la plantilla con un FCF normalizado de varios años (o antes de circulante), al tratarse de un negocio de consumo maduro con poca inversión y sin arrendamientos NIIF 16.

### calidad

    El negocio (sidra de marca líder en su nicho británico) se entiende y conserva un ROCE del 19 % con poca necesidad de capital, pero el margen EBIT cayó del 16,7 % (2016) al 8,1 % (2025) y no está claro si la marca da poder de precio; discrepo de la etapa 1 en que esto sea «demasiado difícil»: es una duda de calidad.
    Dato clave: Análisis!C24 = 0.19

### caja

    La caja libre fue positiva en todos los años 2019–2025 (95,8 a 276,7 Mkr) con conversión CFO/beneficio de 1,55 y FCF base de 140,3 (111,4 sin circulante), aunque es volátil y el CFO de los comunicados de cierre es menor que el de los informes anuales.
    Dato clave: Análisis!C26 = 1.55

### balance

    La deuda neta sin arrendamientos (380,2 − 163,8 = 216,4 estimada) es solo 0,82x un EBITDA de 264,8 que ya resta el alquiler operativo (K3), holgado para una marca de consumo, aunque la caja no cubre la deuda a corto a 30-06-26 (Análisis!C34 = No) y el dividendo supera el beneficio.
    Dato clave: Análisis!C54 = 380.2 (deuda financiera sin arrendamientos, estimada); Análisis!C33 = 0.82

### precio

    A 115,6 SEK la cotización está por encima del valor ponderado de 103,3 y del normal de 99,2 (margen −12 %), y muy por encima de la referencia de precio de Sí de ≈56 SEK, de modo que está claramente cara al 9 %.
    Dato clave: Análisis!C37 = 115.6 frente a Análisis!C83 = 103.295261846281

### encaje

    El paquete no trae la cartera y la hoja solo clasifica la idea como «Calidad a precio razonable» con un precio de 115,6 SEK, sin nada concreto sobre encaje.
    Dato clave: Análisis!C14 = Calidad a precio razonable

### Qué lo cambiaría

    - Una cotización por debajo de ~77 SEK (¾ del ponderado de 103,3) o cerca del escenario malo de 56,2 SEK pasaría el precio a estudiar a fondo.
    - Un margen EBIT sin otros ingresos de explotación por encima del 10 % dos años seguidos resolvería la duda de calidad a favor.
    - Que el 3T26 muestre otra caída de margen o un dividendo pagado de nuevo con deuda a corto llevaría a descartar.

### Qué falta

    - Informe 3T26 (18-11-2026), posterior a la fecha de la hoja: deuda a corto, cuentas a cobrar y margen sin otros ingresos.
    - Desglose real de la deuda a 30-06-26: los 380,2 Mkr de Análisis!C54 son una estimación (rango ~370–395).
    - Explicación de la diferencia de CFO entre informes anuales y comunicados de cierre (2023: 175,7 frente a 70,5), que bajaría el FCF base a ~91 Mkr.

### Comprobaciones mecánicas y normalizaciones

    {
      "comprobaciones": {
        "avisos": [],
        "nota": "Comprobaciones mecánicas informativas: no acreditan la calidad económica."
      },
      "normalizaciones": []
    }

