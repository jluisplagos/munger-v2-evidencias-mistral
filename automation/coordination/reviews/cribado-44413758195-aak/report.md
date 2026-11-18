# Cribado · AAK

Estado de la ejecución: `AUDITORIA_DOCUMENTAL_PENDIENTE_ACEPTACION`

Cribado pendiente de revisión humana. No es una recomendación de compra, ni aceptación, ni aptitud para dinero real. Tasa 9 % provisional.

C-ARR (decisión de la persona responsable): los arrendamientos se cuentan una sola vez, en el flujo. El alquiler se resta de la caja libre; la deuda, deuda/EBITDA y deuda/caja libre se miden sin arrendamientos; el pasivo por arrendamientos se muestra aparte, como dato.

Cifras de la etapa 1 tal como las guardó la hoja, a su fecha de análisis; sin las decisiones posteriores (P-O1, P-O2, F1-A/F1-B, D-US1/2, D-WM) ni verificación contra la fuente oficial.

| Campo | Valor |
|---|---|
| Fecha de la hoja | 2026-10-24 |
| Tarea | cribado-44413758195-aak |
| SHA del código | 833cd50a9bba34006519119c72a29c70a1656fb7 |
| Huella del paquete (package_sha256) | 3d1e1894818e1370dad4a45e0d2d48f30ba1e62600ff464dfe134292e0033dcf |
| Huella del envío (bundle_sha256) | 87a12000569f64934dfbc55f15879fcacad8b7ec66ee7458e26fa9227b6f2013 |
| Huella del encargo | 32b5c7f313e61a61fb0f5e68a75b3c44004eb902e97b98720fb98fa8d383e6cf |
| Huella de la Release | 4d30f7352948fe7e7fe3b133386eabedbddcc71d997e972a1c6db7964d58b0a9 |
| Huella del libro | 8c1318ab4f97f4a3c6e4b0a29d8c37747cb18e502c336e371787f067d5c53afe |
| Modelo pedido / devuelto | claude-opus-5-5 / claude-opus-5-5 |
| Esfuerzo | high |
| Gramática del servidor | True |
| Mensajes enviados | 1 |
| Cota de entrada antes de llamar | 161058 tokens |
| Reserva estimada antes de llamar | USD 1.299592 |
| Uso de tokens | entrada 72096, salida 4258 |
| Coste | CONOCIDO_ESTIMADO; estimado USD 0.373544; cota 0.373544 |

| id | ruta | sha256 | bytes |
|---|---|---|---|
| respuesta | EMPRESAS_LOTES_COMPLETOS/AAK/AAK_respuesta.md | 13f2a3def1458fd87b89b433ac79c6c5787a7d6428380fefe6e585357fc63e0b | 50891 |
| hoja_analisis | EMPRESAS_LOTES_COMPLETOS/AAK/AAK_evaluada.xlsx#Análisis | d0276116b4117c3a2c0ab09a76ec7486661ad42f3c78536253ef2752d16d3c10 | 24803 |
| hoja_control_maestro | EMPRESAS_LOTES_COMPLETOS/AAK/AAK_evaluada.xlsx#Control maestro | 61c34ec4e141091aded06da0bca373f51d7e3849013340616df7cb5b73ae1c4e | 64678 |

## Salida del modelo (datos, sin acciones ejecutables)

Veredicto `vigilar` · DCF de la plantilla aplica: `dudoso`

| Filtro | Resultado |
|---|---|
| calidad | dudoso |
| caja | dudoso |
| balance | pasa |
| precio | no_pasa |
| encaje | no_aplica |

### Pasivo por arrendamientos (dato aparte)

    Control maestro!M36 = 465 (pasivo por arrendamientos incluido en la deuda neta de 3.335 y en Análisis!C54 = 5289; dato aparte, fuera del cociente)


### Tipo de negocio y motor

    Transformador industrial B2B de aceites y grasas vegetales con capa de especialidad: la materia prima supone el 70-75 % del precio de venta, el volumen está plano y el margen por kilo es parcialmente cíclico.
    Caja libre de ciclo medio, normalizando el capital circulante ligado al precio de la materia prima, contrastada con EV/EBIT de ciclo y con el EBIT/kg por volumen; no basta una media de tres años de caja libre reportada.

### calidad

    El negocio se entiende (C11 = Sí) y el ROCE es del 19,1 %, pero ese nivel solo existe desde 2023 (14,2-15,8 % en 2015-2022), el EBIT/kg ya cae en las tres áreas, el volumen lleva diez años plano y el paquete no identifica a ningún competidor; coincido en parte con la bandera de foso de C18, aunque sin rebajarla a no_pasa.
    Dato clave: Análisis!C24 = 0.191

### caja

    La caja operativa solo cubrió 0,681 veces el beneficio neto en 2021-2025, y la caja libre fue negativa en 2021, 2022 y 2025 porque el circulante absorbió 9.098 mm. Antes de circulante la conversión es de 1,37 y en los últimos doce meses de 1,20, así que la duda es si ese circulante revierte.
    Dato clave: Análisis!C26 = 0.681

### balance

    Sin arrendamientos, la deuda neta es ≈2.870 mm (3.335 de Control maestro!M36 menos 465 de arrendamientos), unas 0,52x el EBITDA que ya resta el alquiler; es holgado incluso para un negocio con componente cíclico. La caja cubre solo 0,79x la deuda a corto, pero hay 8.521 mm de líneas comprometidas sin usar. El 0,59x de Análisis!C33 incluye arrendamientos y no se usa tal cual.
    Dato clave: Análisis!C54 = 5289 (incluye 465 de arrendamientos; deuda sin arrendamientos 4824 y deuda neta sin arrendamientos ≈2870, ≈0,52x el EBITDA estimado tras alquiler de ≈5488 según Control maestro!N36)

### precio

    La cotización de 182,6 SEK (Análisis!C37) queda muy por encima del valor ponderado de 97,4 y del escenario bueno de 148,9, y sigue por encima a r − 2 puntos (139,1); el DCF inverso exige un 13,4 % de crecimiento, más que el escenario bueno. La conclusión depende de la base de caja libre: con la base de los últimos doce meses (2.704 mm), la respuesta estima ≈190.
    Dato clave: Análisis!C83 = 97.4340109590643

### encaje

    El paquete no trae la cartera de la persona responsable (capitalización de 47.368 mm SEK como único dato de contexto), así que este filtro no se evalúa ni elimina.
    Dato clave: Análisis!C41 = 47368

### Qué lo cambiaría

    - Que el circulante vuelva al 19-21 % de las ventas y la caja libre de 2026 salga positiva y cercana al beneficio, lo que llevaría la caja a pasa.
    - Que el EBIT/kg del Q4 2026 se estabilice por encima de 2,3 SEK o, al contrario, pierda los 2 SEK, lo que decidiría el filtro de calidad.
    - Una cotización en torno o por debajo del valor ponderado de 97,4 SEK, o una base de caja libre de ciclo medio que justifique los 182,6 SEK.

### Qué falta

    - Reversibilidad del capital circulante (28,6 % de las ventas frente al 18,6-20,7 % de 2019-20): desglose de inventario por precio y por volumen, y días de cobro y pago por área.
    - Estructura competitiva: competidores de especialidad, cuotas y poder de precio cuantificado; el paquete no los trae.
    - Coherencia de fechas y vencimientos: la decisión de la base de caja libre figura como del 28-oct-2026, posterior a la fecha de la hoja (24-oct-2026), y la refinanciación de la deuda a corto no está documentada.

### Comprobaciones mecánicas y normalizaciones

    {
      "comprobaciones": {
        "avisos": [],
        "nota": "Comprobaciones mecánicas informativas: no acreditan la calidad económica."
      },
      "normalizaciones": []
    }

