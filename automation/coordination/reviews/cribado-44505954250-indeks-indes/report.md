# Cribado · Indeks_Indes

Estado de la ejecución: `AUDITORIA_DOCUMENTAL_PENDIENTE_ACEPTACION`

Cribado pendiente de revisión humana. No es una recomendación de compra, ni aceptación, ni aptitud para dinero real. Tasa 9 % provisional.

C-ARR (decisión de la persona responsable): los arrendamientos se cuentan una sola vez, en el flujo. El alquiler se resta de la caja libre; la deuda, deuda/EBITDA y deuda/caja libre se miden sin arrendamientos; el pasivo por arrendamientos se muestra aparte, como dato.

Cifras de la etapa 1 tal como las guardó la hoja, a su fecha de análisis; sin las decisiones posteriores (P-O1, P-O2, F1-A/F1-B, D-US1/2, D-WM) ni verificación contra la fuente oficial.

| Campo | Valor |
|---|---|
| Fecha de la hoja | 2026-10-31 |
| Tarea | cribado-44505954250-indeks-indes |
| SHA del código | 833cd50a9bba34006519119c72a29c70a1656fb7 |
| Huella del paquete (package_sha256) | 479d3839ed6fa645c79fd72117d335b915473a37adc5a62aaeb62492cd29420a |
| Huella del envío (bundle_sha256) | 11200f71207072a1a96c4dc0ee7e5475efaf1158d03732861968209eb9e1f4fd |
| Huella del encargo | 32b5c7f313e61a61fb0f5e68a75b3c44004eb902e97b98720fb98fa8d383e6cf |
| Huella de la Release | 4d30f7352948fe7e7fe3b133386eabedbddcc71d997e972a1c6db7964d58b0a9 |
| Huella del libro | 905a7ab992e5d96b6752725e6fabf2d8c0b302fad2ee6370a84ad63e79cfb2fc |
| Modelo pedido / devuelto | claude-opus-5-5 / claude-opus-5-5 |
| Esfuerzo | high |
| Gramática del servidor | True |
| Mensajes enviados | 1 |
| Cota de entrada antes de llamar | 130460 tokens |
| Reserva estimada antes de llamar | USD 1.1772 |
| Uso de tokens | entrada 59423, salida 5167 |
| Coste | CONOCIDO_ESTIMADO; estimado USD 0.341032; cota 0.341032 |

| id | ruta | sha256 | bytes |
|---|---|---|---|
| respuesta | EMPRESAS_LOTES_COMPLETOS/Indeks_Indes/Indeks_Indes_respuesta.md | 2e3f6564d2038fd379a98c273bf31b3ecc02927c3fd9d37bed1e4e4e6fcd6c4c | 32327 |
| hoja_analisis | EMPRESAS_LOTES_COMPLETOS/Indeks_Indes/Indeks_Indes_evaluada.xlsx#Análisis | 108bd0007bdb4c1996eab4fad95694442e70616f9d8b59019b6ef3e4bf46c264 | 23506 |
| hoja_control_maestro | EMPRESAS_LOTES_COMPLETOS/Indeks_Indes/Indeks_Indes_evaluada.xlsx#Control maestro | c0f8ae004f2739e2d4b9a2c475907a95ac9fd813eddc64fdbd1da1aeffe0c804 | 53739 |

## Salida del modelo (datos, sin acciones ejecutables)

Veredicto `descartar` · DCF de la plantilla aplica: `no`

| Filtro | Resultado |
|---|---|
| calidad | no_pasa |
| caja | dudoso |
| balance | pasa |
| precio | dudoso |
| encaje | no_aplica |

### Pasivo por arrendamientos (dato aparte)

    Control maestro!M51 = 122,6 mn TL (arrendamientos NIIF 16, incluidos en Análisis!C54 = 6615)


### Tipo de negocio y motor

    Distribuidor mayorista de TI y electrónica en Turquía, de margen fino, intensivo en circulante financiado por proveedores y ligado al ciclo y a la macro turca (inflación, lira, régimen de importación).
    Beneficio atribuible normalizado en TL reales frente al patrimonio (ROE frente a r y precio/valor contable) y caja de ciclo medio neta de circulante y de minoritarios, en lugar del DCF de caja libre residual.

### calidad

    El mecanismo se entiende, pero la ventaja no se ve en las cifras del accionista: el ROCE del 62 % lo financian los proveedores y al dueño le llega un ROE atribuible del 6,8 % en 2025 (por debajo del 9 %), con margen operativo del 3–4 %, fabricantes sin exclusividad y asignación de capital dudosa (remuneración de la alta dirección de 260,7 mn, el 50 % del beneficio atribuible); discrepo del cubo de etapa 1 en que el problema no es solo de círculo, sino de calidad.
    Dato clave: Control maestro!N29: ROE atribuible FY25 = 6,84 % (LTM 11,9 %) frente a ROCE Análisis!C24 = 0.62

### caja

    La caja libre base es positiva (963 mn, media 2023–25) y la CFO/beneficio es de 4,3x, pero la cifra va de 651 (LTM) a 2.149 (5 años) según la ventana, fue negativa en 2019 y 2023 en los informes originales y depende del circulante, así que no es recurrente ni estable.
    Dato clave: Análisis!C52 = 963

### balance

    Sin arrendamientos, la deuda financiera es de 6.492,4 mn frente a 7.259,8 mn de caja: caja neta de unos 767 mn, equivalente a ≈−0,15x el EBITDA LTM (la hoja da −0,12x con NIIF 16 en Análisis!C33); la caja cubre 1,70x la deuda a corto, aunque la deuda está en dólares (99,9 %) y los proveedores (31.259 mn) financian el circulante.
    Dato clave: Control maestro!M51: deuda sin arrendamientos = 6615 − 122,6 = 6492,4 mn TL (Análisis!C54 = 6615; caja Análisis!C53 = 7259.8)

### precio

    La cotización de 10,19 TL está por debajo incluso del escenario malo (11,06) y del ponderado (20,45; 15,95 con r + 2 puntos), pero la hoja marca el DCF como no aplicable por financiación inestable (C62), no hay precio de Sí y, según la respuesta, con r = 11 % el malo baja a ≈9,1 TL, por debajo del precio.
    Dato clave: Análisis!B78 = 11.0603501826993 frente a Análisis!C37 = 10.19

### encaje

    El paquete no trae la cartera de la persona responsable y la hoja solo da la capitalización de 7.330,7 mn TL, sin nada concreto sobre encaje.
    Dato clave: Análisis!C41 = 7330.7

### Qué lo cambiaría

    - Un ROE atribuible real normalizado sostenido claramente por encima del 9 % (no solo el 11,9 % LTM de un semestre fuerte).
    - Datos que muestren continuidad de las grandes marcas y pérdidas de crédito pequeñas en años de devaluación, con la posición corta en divisa (2.971 mn) cerrada.
    - Remuneración de la alta dirección desglosada y razonable, y Gebze (≈3,3 bn) para uso propio con ahorro de costes medible.

### Qué falta

    - Reparto de ventas por marca y duración y renovación de los contratos con fabricantes, que no dan exclusividad.
    - Pérdidas por impago en años de devaluación (notas 2016–2024) y causa del stock +76,8 % frente a ventas +37,6 % en el 1S26.
    - Resultados del 3T2026 (previstos para ≈10.11.2026) y coherencia de fechas: Control maestro cita una decisión del inversor del 09-nov-2026, posterior a la fecha de la hoja (31-oct-2026).

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

