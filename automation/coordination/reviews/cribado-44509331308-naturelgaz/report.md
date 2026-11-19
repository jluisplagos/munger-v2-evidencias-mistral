# Cribado · Naturelgaz

Estado de la ejecución: `AUDITORIA_DOCUMENTAL_PENDIENTE_ACEPTACION`

Cribado pendiente de revisión humana. No es una recomendación de compra, ni aceptación, ni aptitud para dinero real. Tasa 9 % provisional.

C-ARR (decisión de la persona responsable): los arrendamientos se cuentan una sola vez, en el flujo. El alquiler se resta de la caja libre; la deuda, deuda/EBITDA y deuda/caja libre se miden sin arrendamientos; el pasivo por arrendamientos se muestra aparte, como dato.

Cifras de la etapa 1 tal como las guardó la hoja, a su fecha de análisis; sin las decisiones posteriores (P-O1, P-O2, F1-A/F1-B, D-US1/2, D-WM) ni verificación contra la fuente oficial.

| Campo | Valor |
|---|---|
| Fecha de la hoja | 2026-11-01 |
| Tarea | cribado-44509331308-naturelgaz |
| SHA del código | 833cd50a9bba34006519119c72a29c70a1656fb7 |
| Huella del paquete (package_sha256) | fc8f61aaa814feafa43340cad1b23f159104ffdb18d6e51bd7533fadefe438eb |
| Huella del envío (bundle_sha256) | 2e2abf0792d976a8a2d97b665449ab5f4067d86dbba849c365a6e0073880e11e |
| Huella del encargo | 32b5c7f313e61a61fb0f5e68a75b3c44004eb902e97b98720fb98fa8d383e6cf |
| Huella de la Release | 4d30f7352948fe7e7fe3b133386eabedbddcc71d997e972a1c6db7964d58b0a9 |
| Huella del libro | d52e7f551a7bcaf4922bceb5e228d49ff2b5b7d8a06085ea633786bd3e5d18dc |
| Modelo pedido / devuelto | claude-opus-5-5 / claude-opus-5-5 |
| Esfuerzo | high |
| Gramática del servidor | True |
| Mensajes enviados | 1 |
| Cota de entrada antes de llamar | 131274 tokens |
| Reserva estimada antes de llamar | USD 1.180456 |
| Uso de tokens | entrada 60005, salida 4919 |
| Coste | CONOCIDO_ESTIMADO; estimado USD 0.3384; cota 0.3384 |

| id | ruta | sha256 | bytes |
|---|---|---|---|
| respuesta | EMPRESAS_LOTES_COMPLETOS/Naturelgaz/Naturelgaz_respuesta.md | 353bd0f251eb8ddbe75a4aa18f1d6546c4db03e8ebe17e6624daac7808775a38 | 32734 |
| hoja_analisis | EMPRESAS_LOTES_COMPLETOS/Naturelgaz/Naturelgaz_evaluada.xlsx#Análisis | 431eb012484d1638b0e0c490d769652094c95db00787b53258a86f08de6f492e | 23463 |
| hoja_control_maestro | EMPRESAS_LOTES_COMPLETOS/Naturelgaz/Naturelgaz_evaluada.xlsx#Control maestro | a46c732a39e46482f0c52638d7e01bf590c355ae3e58d5c10702ff0d2cfdd126 | 54303 |

## Salida del modelo (datos, sin acciones ejecutables)

Veredicto `vigilar` · DCF de la plantilla aplica: `dudoso`

| Filtro | Resultado |
|---|---|
| calidad | dudoso |
| caja | pasa |
| balance | pasa |
| precio | no_pasa |
| encaje | no_aplica |

### Pasivo por arrendamientos (dato aparte)

    Control maestro!M51 = 238.7 (pasivo por arrendamientos a 30.06.2026; la deuda total con arrendamientos es Análisis!C54 = 484.9)


### Tipo de negocio y motor

    Distribución por carretera de gas natural comprimido o licuado (CNG/LNG) a distritos e industrias sin gasoducto en Turquía: nicho regulado, con un precio igual al coste del gas trasladado más un margen por Sm³, y cifras en contabilidad de hiperinflación (TMS 29).
    DCF en términos reales con horizonte finito: flujos del gas urbano hasta la llegada prevista del gasoducto a cada distrito, más el valor de las líneas industriales y nuevas, en lugar de una perpetuidad.

### calidad

    El producto se entiende y las cifras muestran rentabilidad (ROCE antes de impuestos del 23,8 % y margen bruto estable de 6,00 → 6,05 TL/Sm³), pero el foso es del nicho: los distritos atendidos bajaron de 141 a 130 en un semestre, la asignación de capital está marcada como Dudosa y hay flujos con vinculadas de 108,6 mm, así que la durabilidad y la gestión quedan sin resolver.
    Dato clave: Análisis!C24 = 0.238

### caja

    La caja libre base es de 390,9 mm (media de 2023–2025) y fue positiva los cinco años (368 / 773 / 548 / 244 / 380 mm), con una conversión CFO/beneficio de 1,59x, aunque sin tendencia (CV 0,44) y después de un capex de expansión de 1.018,2 mm sin desglose de mantenimiento.
    Dato clave: Análisis!C52 = 390.9

### balance

    Sin arrendamientos, los préstamos son 246,2 mm frente a 801 mm de caja, es decir, caja neta de unos 555 mm y −0,27x sobre el EBITDA previo a la NIIF 16 que da la hoja; el −0,14x de Análisis!C33 incluye arrendamientos y no se usa, y queda el matiz de una caja estacional (394,4 mm a 31.12.2025 según la hoja, 334,9 según la respuesta: manda la hoja) y de una deuda 100 % en divisa sin cobertura.
    Dato clave: Control maestro!N51 = 246.2 (préstamos sin arrendamientos; caja Análisis!C53 = 801)

### precio

    A 9,51 TL la cotización supera el valor ponderado de 9,04 TL y dobla el escenario malo de 4,68 TL que la etapa 1 toma como referencia de precio de Sí; con una r del 7 % el ponderado sube a 12,57 TL, pero ¾ de esa cifra (9,43) sigue por debajo del precio, y un motor con fecha de fin solo restaría valor.
    Dato clave: Análisis!C83 = 9.04498911304843

### encaje

    El paquete no trae la cartera de la persona responsable; solo consta una capitalización de 6.561,9 mm TL, que no basta para juzgar el encaje.
    Dato clave: Análisis!C41 = 6561.9

### Qué lo cambiaría

    - Una cotización en torno a 4,7 TL o menos (escenario malo de Análisis!B78 = 4.68).
    - Un plan oficial de gasoductos que muestre que la mayoría de los distritos atendidos conservan el CNG diez años o más.
    - Que 9M2026 o el cierre de 2026 confirmen una caída del volumen urbano y del margen por Sm³, o que las vinculadas resulten una vía de salida de caja; eso llevaría a descartar.

### Qué falta

    - Plan oficial de gasoductos para los 130 distritos atendidos y cláusulas de los contratos con distribuidoras sobre la llegada de la tubería.
    - Desglose del capex entre mantenimiento y crecimiento, y resultados de 9M2026 (no publicados a la fecha de la hoja).
    - Detalle de las operaciones con vinculadas (Naturelgaz Gaz İletim, «Diğer» de 108,6 mm, vigencia de la prenda de 2022) y de la remuneración de la dirección.

### Comprobaciones mecánicas y normalizaciones

    {
      "comprobaciones": {
        "avisos": [],
        "nota": "Comprobaciones mecánicas informativas: no acreditan la calidad económica."
      },
      "normalizaciones": []
    }

