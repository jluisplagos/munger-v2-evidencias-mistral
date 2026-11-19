# Cribado · Methanex

Estado de la ejecución: `AUDITORIA_DOCUMENTAL_PENDIENTE_ACEPTACION`

Cribado pendiente de revisión humana. No es una recomendación de compra, ni aceptación, ni aptitud para dinero real. Tasa 9 % provisional.

C-ARR (decisión de la persona responsable): los arrendamientos se cuentan una sola vez, en el flujo. El alquiler se resta de la caja libre; la deuda, deuda/EBITDA y deuda/caja libre se miden sin arrendamientos; el pasivo por arrendamientos se muestra aparte, como dato.

Cifras de la etapa 1 tal como las guardó la hoja, a su fecha de análisis; sin las decisiones posteriores (P-O1, P-O2, F1-A/F1-B, D-US1/2, D-WM) ni verificación contra la fuente oficial.

| Campo | Valor |
|---|---|
| Fecha de la hoja | 2026-11-07 |
| Tarea | cribado-44505954250-methanex |
| SHA del código | 833cd50a9bba34006519119c72a29c70a1656fb7 |
| Huella del paquete (package_sha256) | c7d3a680b07373533cb732a0e6f99f675a0d292d6aa272f5aa05f8d7773dcc5d |
| Huella del envío (bundle_sha256) | 01fd027b036e69b462f1929afb6a1e506ed253306ab1640511df4a0ed6ad2e79 |
| Huella del encargo | 32b5c7f313e61a61fb0f5e68a75b3c44004eb902e97b98720fb98fa8d383e6cf |
| Huella de la Release | 4d30f7352948fe7e7fe3b133386eabedbddcc71d997e972a1c6db7964d58b0a9 |
| Huella del libro | 05722a0a30d94f1980da0aecea0e694f1a9dbb9246cc1b8447ab86bcac5691da |
| Modelo pedido / devuelto | claude-opus-5-5 / claude-opus-5-5 |
| Esfuerzo | high |
| Gramática del servidor | True |
| Mensajes enviados | 1 |
| Cota de entrada antes de llamar | 132508 tokens |
| Reserva estimada antes de llamar | USD 1.185392 |
| Uso de tokens | entrada 59688, salida 3991 |
| Coste | CONOCIDO_ESTIMADO; estimado USD 0.318572; cota 0.318572 |

| id | ruta | sha256 | bytes |
|---|---|---|---|
| respuesta | EMPRESAS_LOTES_COMPLETOS/Methanex/Methanex_respuesta.md | c703a7a9ff4d8d2ddf5c916fc5164a71bb32246ac2ab8ada95446cf56f596d99 | 32836 |
| hoja_analisis | EMPRESAS_LOTES_COMPLETOS/Methanex/Methanex_evaluada.xlsx#Análisis | 8f47f0db2e18e72dcd4faaf092bb5bd4b4811fa5faed3c711251a1125253e9f3 | 23630 |
| hoja_control_maestro | EMPRESAS_LOTES_COMPLETOS/Methanex/Methanex_evaluada.xlsx#Control maestro | 8916b0d7a00e61de9f69f6632b299cc9694ae64781866787a6703f434bfd3168 | 55438 |

## Salida del modelo (datos, sin acciones ejecutables)

Veredicto `descartar` · DCF de la plantilla aplica: `no`

| Filtro | Resultado |
|---|---|
| calidad | no_pasa |
| caja | dudoso |
| balance | dudoso |
| precio | dudoso |
| encaje | no_aplica |

### Pasivo por arrendamientos (dato aparte)

    Control maestro!M51 = 755.2 (dic-2025); 709 a sep-2026 según el MD&A del 3T-2026 (Control maestro!N51), fuera del cociente de deuda.


### Tipo de negocio y motor

    Productor y distribuidor de materia prima cíclica (metanol a partir de gas natural, con algo de amoníaco tras OCI).
    Caja libre atribuible (neta de minoritarios) de un ciclo completo con contabilidad homogénea, contrastada con el coste de reposición por tonelada de capacidad, en lugar del DCF de crecimiento constante sobre una media de tres años.

### calidad

    El negocio se entiende (diferencial metanol–gas), pero el ROCE medio 2021–2025 es del 10,5 % antes de impuestos y del 7,8–8,5 % después, por debajo del 9 %, sin foso, con cuota a la baja (14 % → 11 %) y plantas que pierden el gas (Titan, Atlas, Nueva Zelanda); el ✓ de márgenes estables de la hoja describe ciclo, no ventaja.
    Dato clave: Análisis!C24 = 0.105

### caja

    La caja libre base de 368,8 es positiva, pero incluye ≈98/año de minoritarios, el capex de 126,2 es menos de la mitad de la depreciación de activos propios (≈309) y en 2016 y 2020 el CFO − capex (150 y 119) no habría cubierto intereses y arrendamientos.
    Dato clave: Análisis!C52 = 368.8

### balance

    Sin arrendamientos, la deuda neta de dic-2025 es ≈2.327,6 (2.752,9 − 425,3) frente a un EBITDA que resta el alquiler de ≈764 (948,2 − 183,9), ≈3,0x, alto para un cíclico; el 3,25x de Análisis!C33 incluye arrendamientos y no sirve tal cual, y el LTM a sep-2026 (≈1,1x con deuda LP 2.398, caja 912 y EBITDA 1.553,6 menos alquiler) es indicativo, sin balance completo y con un muro de ≈1.770 en 2027–2029.
    Dato clave: Control maestro!M51 = 2752.9 (deuda sin arrendamientos a dic-2025; Análisis!C54 = 3508.1 la incluye)

### precio

    No hay precio de Sí y el DCF de la plantilla no aplica (Análisis!C62); a título indicativo, 66,33 queda por debajo del ponderado de 75,49 pero muy por encima del malo de 39,36, y con r al 11 % el valor cae a 58,16, así que el resultado cambia dentro de ±2 puntos y haría falta una caja atribuible de ciclo medio.
    Dato clave: Análisis!C37 = 66.33

### encaje

    El paquete no trae la cartera; la hoja solo registra un 0 % de etapa 1 en Análisis!C104, que no se hereda y no elimina en el cribado.
    Dato clave: Análisis!C104 = 0% · Demasiado difícil · sin precio de Sí

### Qué lo cambiaría

    - Un ROCE después de impuestos por encima del 9–12 % en un ciclo entero, con costes por planta que sitúen a Geismar y Beaumont en lo bajo de la curva.
    - Un balance a sep-2026 que confirme deuda neta sin arrendamientos por debajo de ≈2x el EBITDA después de alquiler en un año de precio medio, con los 700 de bonos 2027 ya amortizados.
    - Un contrato largo de gas para Titan tras septiembre de 2026 y sin nuevos cortes en Egipto.

### Qué falta

    - Balance completo a 30-sep-2026 (deuda, caja y EBITDA LTM solo indicativos en Control maestro!M36 y N51).
    - Capex de mantenimiento sostenible por planta y costes de caja por planta frente a la depreciación de activos propios de ≈309.
    - Caja atribuible al accionista neta de minoritarios (≈98/año) y de partidas de venta de gas y seguros (≈67/año) en un ciclo completo.

### Comprobaciones mecánicas y normalizaciones

    {
      "comprobaciones": {
        "avisos": [
          "Filtro balance: motivo de más de 400 caracteres."
        ],
        "nota": "Comprobaciones mecánicas informativas: no acreditan la calidad económica."
      },
      "normalizaciones": []
    }

