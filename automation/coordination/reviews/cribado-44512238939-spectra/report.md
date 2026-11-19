# Cribado · Spectra

Estado de la ejecución: `AUDITORIA_DOCUMENTAL_PENDIENTE_ACEPTACION`

Cribado pendiente de revisión humana. No es una recomendación de compra, ni aceptación, ni aptitud para dinero real. Tasa 9 % provisional.

C-ARR (decisión de la persona responsable): los arrendamientos se cuentan una sola vez, en el flujo. El alquiler se resta de la caja libre; la deuda, deuda/EBITDA y deuda/caja libre se miden sin arrendamientos; el pasivo por arrendamientos se muestra aparte, como dato.

Cifras de la etapa 1 tal como las guardó la hoja, a su fecha de análisis; sin las decisiones posteriores (P-O1, P-O2, F1-A/F1-B, D-US1/2, D-WM) ni verificación contra la fuente oficial.

| Campo | Valor |
|---|---|
| Fecha de la hoja | 2026-11-01 |
| Tarea | cribado-44512238939-spectra |
| SHA del código | 833cd50a9bba34006519119c72a29c70a1656fb7 |
| Huella del paquete (package_sha256) | 7ee99a59edf3674a5af8ab682f8d980b117e4e9975766660cb27dcb70e5d6ace |
| Huella del envío (bundle_sha256) | e7715cbd59401bc240e3e3d55f554ab24f02960af79c5c1ea91e346bf22bf558 |
| Huella del encargo | 32b5c7f313e61a61fb0f5e68a75b3c44004eb902e97b98720fb98fa8d383e6cf |
| Huella de la Release | 4d30f7352948fe7e7fe3b133386eabedbddcc71d997e972a1c6db7964d58b0a9 |
| Huella del libro | 1b32b5f4a45422ef9de69acd403a0b11013b7e6090aed9be880c253216e79759 |
| Modelo pedido / devuelto | claude-opus-5-5 / claude-opus-5-5 |
| Esfuerzo | high |
| Gramática del servidor | True |
| Mensajes enviados | 1 |
| Cota de entrada antes de llamar | 127636 tokens |
| Reserva estimada antes de llamar | USD 1.165904 |
| Uso de tokens | entrada 58035, salida 4645 |
| Coste | CONOCIDO_ESTIMADO; estimado USD 0.32504; cota 0.32504 |

| id | ruta | sha256 | bytes |
|---|---|---|---|
| respuesta | EMPRESAS_LOTES_COMPLETOS/Spectra/Spectra_respuesta.md | 42f6088375c57a5a530b65d0da761ef494ea3ee5dac371bcdbb1143ba24076e1 | 31325 |
| hoja_analisis | EMPRESAS_LOTES_COMPLETOS/Spectra/Spectra_evaluada.xlsx#Análisis | f0d3fbb6b13aeb8e553a535105379625bfd160e49b56ff11c7fddf4fc14f74e0 | 22837 |
| hoja_control_maestro | EMPRESAS_LOTES_COMPLETOS/Spectra/Spectra_evaluada.xlsx#Control maestro | c894d1c9a7f7aec0b5af6a66e7b79f8a88ab9da3e22597e434db40c3f5a5b006 | 52700 |

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

    Control maestro!M29 = arrendamientos operativos 5,21 mm$ a 30-jun-2026 (coherente con Control maestro!N51: deuda con arrendamientos 8,00 mm$ − 2,79 mm$ sin ellos).


### Tipo de negocio y motor

    Tecnología de seguridad y autenticación (materiales encubiertos, sensores y software para bancos centrales e impresores, más la imprenta de sellos Cartor): un núcleo recurrente con muy pocos clientes y contratos grandes de sensores cíclicos cada 6–8 años.
    Caja de ciclo medio del contrato de sensores (la media FY21–25 de la plantilla), contrastada con la caja recurrente sin contrato y con Cartor, es decir, el DCF de la plantilla con una base normalizada de ciclo y el escenario malo como suelo.

### calidad

    El mecanismo se entiende y el ROCE es alto (24,8 % LTM, 20,2–24,2 % en FY21–23), pero ese ROCE está inflado por el contrato de sensores, tres clientes suman el 75 % de los ingresos, el margen operativo baja al 16,4 % en el 6M-26 desde el 35–36 % y Cartor pierde dinero; el «demasiado difícil» de la etapa 1 lo leo como duda de calidad, no como negocio ininteligible.
    Dato clave: Análisis!C24 = 0.248

### caja

    La caja libre base es positiva, 7,71 mm$ (media FY21–25 neta de SBC), con conversión CFO/beneficio de 0,95 (Análisis!C26) y capex de 0,88 mm$ frente a una D&A de ~2,9 mm$; pasa, aunque sin el contrato de sensores la hoja la estima en ≈4,6 mm$ (Control maestro, N40) y el CFO del 6M-26 fue de −0,55 mm$.
    Dato clave: Análisis!C52 = 7.71

### balance

    Con una deuda financiera sin arrendamientos de 2,79 mm$, frente a 14,89 mm$ de caja (Análisis!C53), hay caja neta: deuda neta/EBITDA de −0,74x (Análisis!C33), con un EBITDA US GAAP LTM de 16,327 mm$ que ya resta el alquiler operativo; tras el dividendo de 6,586 mm$ sigue en caja neta (−0,34x), holgado incluso para un negocio cíclico por contratos.
    Dato clave: Análisis!C54 = 2.79

### precio

    La cotización de 2,41 $ (Análisis!C37) está muy por encima del escenario malo de 1,31 $, que es la referencia de precio de Sí de la regla (la etapa 1 no fija precio de Sí), y solo un 2,6 % por debajo del ponderado de 2,47 $ (Análisis!C84); con r a ±2 puntos el ponderado va de 1,91 $ a 3,50 $ (Análisis!C90 y C92), sin colchón en la tasa base del 9 %.
    Dato clave: Análisis!C78 = 1.30621743141386

### encaje

    El paquete no trae la cartera de la persona responsable y la hoja no dice nada concreto sobre encaje en una microcap de 116,79 mm$ de capitalización; este filtro no elimina.
    Dato clave: Análisis!C41 = 116.79

### Qué lo cambiaría

    - Una cotización igual o inferior a ~1,31 $ (Análisis!C78) con el núcleo de materiales intacto llevaría el precio a pasa y el veredicto a estudiar_a_fondo.
    - La renovación a largo plazo del contrato de materiales con el banco central despejaría la duda de calidad; su pérdida o un repacto a la baja la convertiría en no_pasa y el veredicto en descartar.
    - Un FCF de 2027 sin contrato de sensores por encima de ~6 mm$ reforzaría calidad y caja; por debajo de ~5 mm$ haría que caja no pase.

### Qué falta

    - Estado de la renovación del acuerdo de suministro de materiales con el banco central (renovado por cinco años en 2021, posible vencimiento hacia 2026) y su peso en ingresos y margen.
    - Caja libre recurrente sin el contrato de sensores: solo hay una estimación de ≈4,6 mm$, y falta confirmar el cobro de los 12,1 mm$ por facturar.
    - Holgura del test de deterioro del fondo de comercio de Cartor (3,56 mm$) y estado del contrato con Royal Mail; la cotización de 2,41 $ procede de fuentes secundarias.

### Comprobaciones mecánicas y normalizaciones

    {
      "comprobaciones": {
        "avisos": [],
        "nota": "Comprobaciones mecánicas informativas: no acreditan la calidad económica."
      },
      "normalizaciones": []
    }

