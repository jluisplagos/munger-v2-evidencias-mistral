# Cribado · Berkosan

Estado de la ejecución: `AUDITORIA_DOCUMENTAL_PENDIENTE_ACEPTACION`

Cribado pendiente de revisión humana. No es una recomendación de compra, ni aceptación, ni aptitud para dinero real. Tasa 9 % provisional.

C-ARR (decisión de la persona responsable): los arrendamientos se cuentan una sola vez, en el flujo. El alquiler se resta de la caja libre; la deuda, deuda/EBITDA y deuda/caja libre se miden sin arrendamientos; el pasivo por arrendamientos se muestra aparte, como dato.

Cifras de la etapa 1 tal como las guardó la hoja, a su fecha de análisis; sin las decisiones posteriores (P-O1, P-O2, F1-A/F1-B, D-US1/2, D-WM) ni verificación contra la fuente oficial.

| Campo | Valor |
|---|---|
| Fecha de la hoja | 2026-10-24 |
| Tarea | cribado-44413758195-berkosan |
| SHA del código | 833cd50a9bba34006519119c72a29c70a1656fb7 |
| Huella del paquete (package_sha256) | 5e1b9753ffa332f4c2d58265f7bed1c0e84068adf63ae96500cf72740f295ab1 |
| Huella del envío (bundle_sha256) | efe29a518277a7342a872e929b43310a1fabe175c96f906a28c95bd732ceee2b |
| Huella del encargo | 32b5c7f313e61a61fb0f5e68a75b3c44004eb902e97b98720fb98fa8d383e6cf |
| Huella de la Release | 4d30f7352948fe7e7fe3b133386eabedbddcc71d997e972a1c6db7964d58b0a9 |
| Huella del libro | 87aed53b40ab361c93ce2b84f16fcca7921e171c0e17336663e78788b1b35648 |
| Modelo pedido / devuelto | claude-opus-5-5 / claude-opus-5-5 |
| Esfuerzo | high |
| Gramática del servidor | True |
| Mensajes enviados | 1 |
| Cota de entrada antes de llamar | 159535 tokens |
| Reserva estimada antes de llamar | USD 1.2935 |
| Uso de tokens | entrada 72115, salida 3583 |
| Coste | CONOCIDO_ESTIMADO; estimado USD 0.36012; cota 0.36012 |

| id | ruta | sha256 | bytes |
|---|---|---|---|
| respuesta | EMPRESAS_LOTES_COMPLETOS/Berkosan/Berkosan_respuesta.md | e43c6a1eb399013b36049943afdc76f0fa08196e14f261c519de58bf5f30bff3 | 47861 |
| hoja_analisis | EMPRESAS_LOTES_COMPLETOS/Berkosan/Berkosan_evaluada.xlsx#Análisis | 0e32876ee5dbc34e215cb5442b572cb1c580db12a8e52cfe616e2d3c98243d07 | 24839 |
| hoja_control_maestro | EMPRESAS_LOTES_COMPLETOS/Berkosan/Berkosan_evaluada.xlsx#Control maestro | 2e69bc8e35bff418e4ed42589fd642efca626ea651eb16025c0469eea2f948a9 | 65935 |

## Salida del modelo (datos, sin acciones ejecutables)

Veredicto `descartar` · DCF de la plantilla aplica: `no`

| Filtro | Resultado |
|---|---|
| calidad | dudoso |
| caja | no_pasa |
| balance | pasa |
| precio | dudoso |
| encaje | no_aplica |

### Pasivo por arrendamientos (dato aparte)

    Control maestro!M51: arrendamientos = 14.58 (incluidos en Análisis!C54 = 29.26; sin ellos, la deuda es de 14.67)


### Tipo de negocio y motor

    Cíclico / materias primas: convertidor turco de resina en espumas técnicas (PE, XPE, PP) para construcción, automoción y embalaje, con un 64,4 % de exportación y cuentas bajo hiperinflación (TMS 29).
    Caja libre de ciclo medio en términos reales, con capex de mantenimiento al menos igual a la amortización, contrastada con el valor de los activos (inmuebles tasados), descontando que el control familiar limita su realización.

### calidad

    El negocio se entiende (convierte resina en espumas técnicas) y el margen bruto es estable, entre el 35 % y el 37 %, pero el ROCE real es del 13,2 %, no hay ventaja competitiva probada, las ventas reales caen tres periodos seguidos y un tercio del resultado operativo de 2025 (42,6 de 127,1 mm) son diferencias de cambio, de modo que los datos apuntan en las dos direcciones.
    Dato clave: Análisis!C24 = 0.132

### caja

    La conversión del beneficio en caja es de 0,61, con caja libre negativa en 2022 (−18,7 mm) y 2024 (−29,5 mm); el FCF base de 20,1 mm (Análisis!C52) se apoya en un capex de 21,1 mm, por debajo de una amortización de 46–56 mm, así que la caja libre no es recurrente ni estable.
    Dato clave: Análisis!C26 = 0.61

### balance

    Sin arrendamientos, la deuda bancaria es de 14,67 mm frente a 129,57 mm de caja: caja neta de unos 114,9 mm (la sensibilidad sin arrendamientos de la hoja da −0,64x, frente al −0,53x de Análisis!C33, que sí los incluye), así que pasa con holgura incluso para un negocio cíclico, aunque toda la deuda vence a corto.
    Dato clave: Control maestro!M51: deuda sin arrendamientos = 14.67 (frente a Análisis!C53 = 129.57 de caja)

### precio

    No hay precio de Sí: la cotización de 4,92 TL supera el valor ponderado de la plantilla (3,13 TL) e incluso el valor ponderado con r al 7 % (4,33 TL), pero ese DCF no aplica a este negocio y, solo con la ventana del FCF, su valor va de 1,42 a 13,97 TL, así que haría falta una caja de ciclo medio más el valor de los activos para concluir.
    Dato clave: Análisis!C37 = 4.92

### encaje

    El paquete no trae la cartera de la persona responsable y la hoja solo dice «0 %» en Análisis!C104, que es una decisión de la etapa 1 y no un dato de encaje.
    Dato clave: Análisis!C104 = 0 % · Demasiado difícil

### Qué lo cambiaría

    - Cuatro ejercicios seguidos de caja libre positiva en base homogénea, con capex igual o superior a la amortización.
    - Una caja libre normalizada y verificable por encima de unos 45 mm (yield superior al 10 % a la capitalización actual de 460,51 mm).
    - Un desglose precio/volumen que muestre poder de precio frente al coste de la resina.

### Qué falta

    - El capex de mantenimiento real: el flujo registra 21,1 mm frente a una amortización de 46–56 mm, mientras los informes de actividad dicen «Yoktur».
    - El principal de los arrendamientos es una estimación (Análisis!C49 = 2.7; la alternativa da 15,8) y no hay un EBITDA después del alquiler explícito en la hoja.
    - Una segunda tasación de los inmuebles: el fondo de revalorización de 318,4 mm descansa en un único tasador.

### Comprobaciones mecánicas y normalizaciones

    {
      "comprobaciones": {
        "avisos": [],
        "nota": "Comprobaciones mecánicas informativas: no acreditan la calidad económica."
      },
      "normalizaciones": []
    }

