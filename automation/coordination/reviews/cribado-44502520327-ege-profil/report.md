# Cribado · Ege_Profil

Estado de la ejecución: `AUDITORIA_DOCUMENTAL_PENDIENTE_ACEPTACION`

Cribado pendiente de revisión humana. No es una recomendación de compra, ni aceptación, ni aptitud para dinero real. Tasa 9 % provisional.

C-ARR (decisión de la persona responsable): los arrendamientos se cuentan una sola vez, en el flujo. El alquiler se resta de la caja libre; la deuda, deuda/EBITDA y deuda/caja libre se miden sin arrendamientos; el pasivo por arrendamientos se muestra aparte, como dato.

Cifras de la etapa 1 tal como las guardó la hoja, a su fecha de análisis; sin las decisiones posteriores (P-O1, P-O2, F1-A/F1-B, D-US1/2, D-WM) ni verificación contra la fuente oficial.

| Campo | Valor |
|---|---|
| Fecha de la hoja | 2026-10-30 |
| Tarea | cribado-44502520327-ege-profil |
| SHA del código | 833cd50a9bba34006519119c72a29c70a1656fb7 |
| Huella del paquete (package_sha256) | 89888cf9b35f3913d26d63787fef67240d8d3153754f7fd1953e7beceb01530d |
| Huella del envío (bundle_sha256) | 9d7c2852847670d0387be09f73b056135f4488a458c771e225bd8d2052ef34ed |
| Huella del encargo | 32b5c7f313e61a61fb0f5e68a75b3c44004eb902e97b98720fb98fa8d383e6cf |
| Huella de la Release | 4d30f7352948fe7e7fe3b133386eabedbddcc71d997e972a1c6db7964d58b0a9 |
| Huella del libro | da69d8f84f3d9b951ee76e4464cbf3bc55ccb55d56dee8c011534981ab173934 |
| Modelo pedido / devuelto | claude-opus-5-5 / claude-opus-5-5 |
| Esfuerzo | high |
| Gramática del servidor | True |
| Mensajes enviados | 1 |
| Cota de entrada antes de llamar | 130042 tokens |
| Reserva estimada antes de llamar | USD 1.175528 |
| Uso de tokens | entrada 59451, salida 4273 |
| Coste | CONOCIDO_ESTIMADO; estimado USD 0.323264; cota 0.323264 |

| id | ruta | sha256 | bytes |
|---|---|---|---|
| respuesta | EMPRESAS_LOTES_COMPLETOS/Ege_Profil/Ege_Profil_respuesta.md | b99a993b90e7528b5b5b8e2666d938dd03881cc23813ea7fbd552a8f275857f6 | 31353 |
| hoja_analisis | EMPRESAS_LOTES_COMPLETOS/Ege_Profil/Ege_Profil_evaluada.xlsx#Análisis | cba460389cd90b8a79be227530e8d210d9f4692a2a63ac01cd988d4cf9e3342b | 23342 |
| hoja_control_maestro | EMPRESAS_LOTES_COMPLETOS/Ege_Profil/Ege_Profil_evaluada.xlsx#Control maestro | 0882d2b529f6b7a0c3824c24559cddafaa3a87284964b3c00d59e5f1a628cf75 | 54433 |

## Salida del modelo (datos, sin acciones ejecutables)

Veredicto `estudiar_a_fondo` · DCF de la plantilla aplica: `dudoso`

| Filtro | Resultado |
|---|---|
| calidad | dudoso |
| caja | dudoso |
| balance | pasa |
| precio | dudoso |
| encaje | no_aplica |

### Pasivo por arrendamientos (dato aparte)

    Control maestro!M36 = 267.5 (arrendamientos incluidos en la deuda total de Análisis!C54 = 937.4)


### Tipo de negocio y motor

    Industrial cíclico ligado a la construcción en Turquía (fabricante de perfiles de PVC para ventanas), con materia prima importada, contabilidad por hiperinflación (TMS 29) y un accionista de control del 86,86 %.
    Caja libre de ciclo medio normalizada en TL reales (volumen y margen medios de un ciclo completo de la construcción), con un descuento aparte por el riesgo del controlador y de las operaciones intragrupo.

### calidad

    El negocio se entiende (perfiles de PVC con tres marcas y unos 650 distribuidores) y el ROCE es del 29,25 %, pero depende del ciclo de la construcción turca, con ventas reales del −21 % en 2024 y del −11 % en 2025, no hay cuota ni volúmenes que prueben una ventaja y el controlador del 86,86 % cobra cargos de 354,3 mm y tiene 266,5 mm vencidos intragrupo; discrepo del «demasiado difícil» de la etapa 1, porque eso afecta al motor de valoración y no a la comprensión del negocio.
    Dato clave: Análisis!C24 = 0.2925

### caja

    La caja libre base es positiva (962,9 mm, media 2022–25), pero la caja libre del accionista cae cuatro lecturas seguidas (1.646 → 1.080 → 810 → 408 mm LTM), la conversión de 1,568 de Análisis!C26 baja a 0,79 sin el resultado monetario y el capex de mantenimiento no se desglosa.
    Dato clave: Análisis!C52 = 962.9

### balance

    Sin arrendamientos, la deuda bancaria de 669,9 mm queda cubierta por 1.368,2 mm de caja: hay caja neta de 698,3 mm, o de unos 348 mm tras el dividendo comprometido de 350,0 mm, frente a un EBITDA LTM de 3.769,9 mm; el −0,11x de Análisis!C33 incluye arrendamientos y no sirve tal cual, aunque el resultado no cambia, y la deuda es toda a corto plazo en TL, con +481,6 mm nuevos en el 6M26.
    Dato clave: Control maestro!M36 = 669.9 (deuda bancaria sin arrendamientos; caja 1368.2 en Análisis!C53, caja neta sin arrendamientos 698.3 en Control maestro!N36)

### precio

    La cotización de 26,5 TL está prácticamente en el valor ponderado de 26,99 TL (margen del 1,8 %) y un 82 % por encima del escenario malo de 14,60 TL; el resultado cambia con ±2 puntos de tasa (21,05 TL al 11 % y 37,40 TL al 7 %), no hay precio de Sí y el DCF de caja libre es dudoso para un negocio cíclico.
    Dato clave: Análisis!C83 = 26.9867447899799

### encaje

    El paquete no trae la cartera y la hoja solo recoge un 0 % ligado al cubo de la etapa 1, así que no hay base para juzgar el encaje.
    Dato clave: Análisis!C104 = 0% · Demasiado difícil (decisión de cartera de la etapa 1, no usada)

### Qué lo cambiaría

    - Caja libre real de 2026 completo por debajo de unos 500 mm (inventario sin normalizar): pasaría a descartar; por encima de 900 mm reforzaría la caja.
    - Cobro de los 266,5 mm vencidos de sociedades del grupo y cargos de gestión que dejen de crecer más que las ventas, o lo contrario: evidencias de extracción por el controlador.
    - Una cotización claramente por debajo de unos 21 TL (valor ponderado al 11 %), que haría pasar el filtro de precio incluso con una tasa más exigente.

### Qué falta

    - Capex de mantenimiento frente a capex de crecimiento: el capex real ha caído un 64 % desde 2021 y la hoja no lo desglosa.
    - Volúmenes, precio medio y cuota de mercado, sin los que no se puede separar ciclo de tendencia ni normalizar la caja de ciclo medio.
    - Contratos de servicios con Deceuninck y la antigüedad de los 266,5 mm vencidos intragrupo; además, la hoja (30-10-2026) recoge decisiones fechadas el 08-11-2026.

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

