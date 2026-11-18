# Cribado · Bossa

Estado de la ejecución: `AUDITORIA_DOCUMENTAL_PENDIENTE_ACEPTACION`

Cribado pendiente de revisión humana. No es una recomendación de compra, ni aceptación, ni aptitud para dinero real. Tasa 9 % provisional.

C-ARR (decisión de la persona responsable): los arrendamientos se cuentan una sola vez, en el flujo. El alquiler se resta de la caja libre; la deuda, deuda/EBITDA y deuda/caja libre se miden sin arrendamientos; el pasivo por arrendamientos se muestra aparte, como dato.

Cifras de la etapa 1 tal como las guardó la hoja, a su fecha de análisis; sin las decisiones posteriores (P-O1, P-O2, F1-A/F1-B, D-US1/2, D-WM) ni verificación contra la fuente oficial.

| Campo | Valor |
|---|---|
| Fecha de la hoja | 2026-10-30 |
| Tarea | cribado-44413758195-bossa |
| SHA del código | 833cd50a9bba34006519119c72a29c70a1656fb7 |
| Huella del paquete (package_sha256) | 46f1c19fcf50417e5bbea5013c55f34d6167cd6a975e5a0dc07bf792b0ba530d |
| Huella del envío (bundle_sha256) | a4ae4009aa3277f332dc18c061506f66c69507685431154b3f0ed823be850ee2 |
| Huella del encargo | 32b5c7f313e61a61fb0f5e68a75b3c44004eb902e97b98720fb98fa8d383e6cf |
| Huella de la Release | 4d30f7352948fe7e7fe3b133386eabedbddcc71d997e972a1c6db7964d58b0a9 |
| Huella del libro | 331049f3d88e24c3b45ea855a3512b220f043b1c3526451f50087bcbcb833089 |
| Modelo pedido / devuelto | claude-opus-5-5 / claude-opus-5-5 |
| Esfuerzo | high |
| Gramática del servidor | True |
| Mensajes enviados | 1 |
| Cota de entrada antes de llamar | 128356 tokens |
| Reserva estimada antes de llamar | USD 1.168784 |
| Uso de tokens | entrada 58425, salida 2778 |
| Coste | CONOCIDO_ESTIMADO; estimado USD 0.28926; cota 0.28926 |

| id | ruta | sha256 | bytes |
|---|---|---|---|
| respuesta | EMPRESAS_LOTES_COMPLETOS/Bossa/Bossa_respuesta.md | fda322d6d07a064cb5c54e7335fd299ea2d0b0ecb9693d6f6e97e3fb4de76358 | 32096 |
| hoja_analisis | EMPRESAS_LOTES_COMPLETOS/Bossa/Bossa_evaluada.xlsx#Análisis | b4ce7947eceaa2ea7f3ac3ee9946409cc7aa822013980539adf25e6f9f00fc99 | 22905 |
| hoja_control_maestro | EMPRESAS_LOTES_COMPLETOS/Bossa/Bossa_evaluada.xlsx#Control maestro | 56ab03ac3e3411fecd075ea4977464bf6c7358e9e04dfc299daad874346b7ef0 | 52551 |

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

    Control maestro!M51 = 5.4 mm TL (incluido en la deuda total Análisis!C54 = 2099.6; excluido del cociente)


### Tipo de negocio y motor

    Fabricante textil integrado (hilo, tejido denim y sportswear), cíclico y de tipo commodity, que opera en Turquía en un entorno de hiperinflación (TMS 29) y exporta.
    Caja de ciclo medio (poder de ganancia normalizado en TL constantes a lo largo del ciclo textil), contrastada con el valor de los activos (inmuebles e inmovilizado) aplicando un descuento por control mayoritario.

### calidad

    El negocio se entiende (C11 = Sí), pero no muestra ventaja en las cifras: ROIC TTM del 3,6 %, por debajo de cualquier coste real; ventas reales en caída cuatro periodos seguidos (−24,7 % en 1S26); margen bruto que baja del 20,2 % al 8,4 % en 2T26; y dudas de gestión hacia la minoría (C98 Dudosa). Discrepo de la etiqueta de A6, «demasiado difícil»: para mí es un negocio comprensible que no pasa.
    Dato clave: Análisis!C24 = 0.036

### caja

    El FCF base medio FY23–25 es de 453,8 mm TL y la conversión CFO/beneficio neto es de 0,93 (C26), pero la serie es errática (FY22 −1.034, FY24 −333) y el TTM de 1.185 se apoya en un capex inferior a la amortización y en la liberación de circulante (350 sin circulante).
    Dato clave: Análisis!C52 = 453.8

### balance

    Sin arrendamientos, la deuda neta de 1.813,9 mm TL equivale a unas 2,8x el EBITDA core TTM de 649,6 (1,6x con el reportado de 1.118, que incluye 468 de otros ingresos sin explicar); es demasiado justo para una cíclica en hiperinflación, con el 81 % de la deuda a menos de un año y una caja que solo cubre 0,17x la deuda a corto (Análisis!C34 = No); la hoja da 2,8 en C33, pero incluye 5,4 de arrendamientos.
    Dato clave: Control maestro!M51 = 2094.2 (préstamos bancarios sin arrendamientos; menos caja Análisis!C53 = 280.3 → deuda neta 1813.9)

### precio

    No hay precio de Sí. La cotización de 4,98 TL está cerca del ponderado de la plantilla (5,09 TL, margen del 2 %), pero ese DCF no aplica (C62), el resultado oscila entre 7,02 y 3,99 TL con r ±2 puntos, y la hoja es anterior a los resultados de 9M2026.
    Dato clave: Análisis!C37 = 4.98

### encaje

    El paquete no trae la cartera, y la cifra del 0 % de la hoja es una propuesta de la etapa 1 que no uso como criterio.
    Dato clave: Análisis!C104 = 0% · No · fuera de cartera

### Qué lo cambiaría

    - ROIC real sostenido por encima del 10 % con un margen bruto superior al 18 % a lo largo de un ciclo malo.
    - FCF sin circulante positivo y estable varios años con capex ≥ amortización (por ejemplo, de forma recurrente por encima de 450 mm TL).
    - Refinanciación de la deuda a corto a largo plazo y deuda neta sin arrendamientos por debajo de 2x el EBITDA core.

### Qué falta

    - Desglose de los otros ingresos de explotación (nota 20), que suponen unos 468 mm TL del EBITDA TTM: decide si el EBITDA relevante es 649,6 o 1.118.
    - Vencimientos por tramos, covenants y condiciones de renovación de las líneas en TL.
    - Varias celdas de Control maestro citan una «decisión del inversor (08-nov-2026)», posterior a la fecha de la hoja (30/10/2026); además, faltan los resultados de 9M2026.

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

