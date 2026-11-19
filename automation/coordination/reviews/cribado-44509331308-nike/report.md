# Cribado · Nike

Estado de la ejecución: `AUDITORIA_DOCUMENTAL_PENDIENTE_ACEPTACION`

Cribado pendiente de revisión humana. No es una recomendación de compra, ni aceptación, ni aptitud para dinero real. Tasa 9 % provisional.

C-ARR (decisión de la persona responsable): los arrendamientos se cuentan una sola vez, en el flujo. El alquiler se resta de la caja libre; la deuda, deuda/EBITDA y deuda/caja libre se miden sin arrendamientos; el pasivo por arrendamientos se muestra aparte, como dato.

Cifras de la etapa 1 tal como las guardó la hoja, a su fecha de análisis; sin las decisiones posteriores (P-O1, P-O2, F1-A/F1-B, D-US1/2, D-WM) ni verificación contra la fuente oficial.

| Campo | Valor |
|---|---|
| Fecha de la hoja | 2026-10-07 |
| Tarea | cribado-44509331308-nike |
| SHA del código | 833cd50a9bba34006519119c72a29c70a1656fb7 |
| Huella del paquete (package_sha256) | df2636fc2edb9cc260fec6ad8011e6d682fb2d47240329d66f6e5d53257b1051 |
| Huella del envío (bundle_sha256) | 7cb6fb91fabc251f32f3cda0ddb7c4c9a05547c74e1135e699bfe0c00248eaf9 |
| Huella del encargo | 32b5c7f313e61a61fb0f5e68a75b3c44004eb902e97b98720fb98fa8d383e6cf |
| Huella de la Release | 4d30f7352948fe7e7fe3b133386eabedbddcc71d997e972a1c6db7964d58b0a9 |
| Huella del libro | d49759fe9d8b8bd39f20471934f7abc5447e808e804aa0d62ca870aa87d88488 |
| Modelo pedido / devuelto | claude-opus-5-5 / claude-opus-5-5 |
| Esfuerzo | high |
| Gramática del servidor | True |
| Mensajes enviados | 1 |
| Cota de entrada antes de llamar | 145265 tokens |
| Reserva estimada antes de llamar | USD 1.23642 |
| Uso de tokens | entrada 67428, salida 4337 |
| Coste | CONOCIDO_ESTIMADO; estimado USD 0.356452; cota 0.356452 |

| id | ruta | sha256 | bytes |
|---|---|---|---|
| respuesta | EMPRESAS_LOTES_COMPLETOS/Nike/Nike_respuesta.md | 9c78525d7162c132ca1e4e0143d8ef04ccdaa81476bbcf7e77b6a9e5ee238a87 | 34102 |
| cambios_v2 | EMPRESAS_LOTES_COMPLETOS/Nike/Nike_cambios_v2.md | 4f365b19591ecec6a5d64d6e3b03c5151e185ace92b1176a4aa7ffa190857f2c | 5557 |
| hoja_analisis | EMPRESAS_LOTES_COMPLETOS/Nike/Nike_evaluada.xlsx#Análisis | 62fa08772bdd510a7298ed65334094a5b92621dd80f481c3b022048ff42a1efa | 24297 |
| hoja_control_maestro | EMPRESAS_LOTES_COMPLETOS/Nike/Nike_evaluada.xlsx#Control maestro | a7c18cf1de18de145958178a1e9151ab97657a9b1148a85c9166a44073f594d2 | 60112 |

## Salida del modelo (datos, sin acciones ejecutables)

Veredicto `vigilar` · DCF de la plantilla aplica: `si`

| Filtro | Resultado |
|---|---|
| calidad | dudoso |
| caja | dudoso |
| balance | pasa |
| precio | no_pasa |
| encaje | no_aplica |

### Pasivo por arrendamientos (dato aparte)

    Control maestro!N51 = 3179 (pasivos por arrendamiento operativo, citados en el texto de la celda; la deuda con ellos sería 11.072 mm); no entra en el cociente de deuda.


### Tipo de negocio y motor

    Marca global de consumo discrecional (calzado, ropa y equipamiento deportivo) que externaliza la fabricación y vende a mayoristas y de forma directa; hoy en reestructuración, con márgenes y cuota a la baja.
    El DCF de caja libre al accionista de la plantilla (US GAAP, caja neta, financiación estable), pero con una caja libre base normalizada de ciclo medio que no dependa del FY24 inflado por la liberación de inventario ni del FY26 deprimido, contrastada con el poder de ganancia que marca la guía de FY27.

### calidad

    El negocio se entiende (Análisis!C11 = Sí): una marca con fabricación externalizada, un ROIC del 18,7 % en un año malo y un margen bruto del 42,9 %; pero la ventaja se erosiona, porque el ROIC baja desde el 48,8 % de FY21, pierde 1,5 puntos de cuota, la marca Converse cae y la fase 1 estima un ROIC del 9,8-11,6 % para FY27; discrepo del «DESCARTAR · demasiado difícil» de Análisis!A6, que sale de C13 (valor no claro sin modelo) y no de que el negocio no se entienda.
    Dato clave: Análisis!C24 = 0.187

### caja

    La caja libre tras SBC es positiva, pero cae: la base de 3.280 mm es la media FY24-FY26 e incluye un FY24 inflado por la liberación de inventario, mientras que FY26 fue de 1.469 mm y el LTM de 1.417 mm (Control maestro!N40); el FCF antes de SBC (2.184 mm) ya no cubre el dividendo (2.407 mm), aunque la conversión CFO/beneficio a cinco años sea de 1,08 (Análisis!C26).
    Dato clave: Análisis!C52 = 3280

### balance

    Sin arrendamientos, la deuda financiera de 7.893 mm queda por debajo de la caja y las inversiones a corto (6.903 + 1.465), lo que deja caja neta de 475 mm y una deuda neta/EBITDA de −0,10x (Análisis!C33 = -0.103) sobre un EBITDA LTM de 4.603 mm que ya resta el alquiler (US GAAP); los vencimientos de 2.000 mm en 12 meses están cubiertos 3,45x por la caja, con 3.000 mm de líneas sin disponer y calificación A+.
    Dato clave: Análisis!C54 = 7893

### precio

    Con r = 9 %, el precio de Sí es el mínimo entre el escenario malo (18,24 $) y ¾ del ponderado (0,75 × 41,81 = 31,36 $), es decir, 18,24 $, y la cotización de 34,61 $ (Análisis!C37) lo supera en torno a un 90 %; incluso con r al 11 % el ponderado bajaría a 31,45 $ (Análisis!C92), por debajo del precio actual, así que está claramente por encima.
    Dato clave: Análisis!C78 = 18.2388778029759

### encaje

    El paquete no trae la cartera de la persona responsable; de la hoja solo consta como dato una capitalización de 51.406,5 mm, que no permite juzgar el encaje.
    Dato clave: Análisis!C41 = 51406.5

### Qué lo cambiaría

    - Una cotización por debajo del precio de Sí de unos 18,24 $ (Análisis!C78) con caja, balance y calidad sin deterioro adicional pasaría el precio y llevaría a estudiar a fondo.
    - Un FY27 cerrado con caja libre tras SBC por encima de unos 3.000 mm sin partidas únicas (frente a los 1.417 del LTM) haría pasar el filtro de caja y subiría el escenario malo.
    - Un margen bruto sostenido por debajo del 40 % (FY26: 42,9 %), una caída de NIKE Brand Norteamérica o un dividendo pagado con deuda harían fallar calidad o caja y llevarían a descartar.

### Qué falta

    - Resultados reales de FY27 (caja libre tras SBC, margen bruto y ROIC): la hoja solo trae la guía y el T1 FY27, con un CFO de 135 mm.
    - Coherencia de fechas: la hoja está fechada el 07/10/2026, pero cita decisiones de la persona responsable del 11-oct-2026 (C46, C47, C50 y C88) y del 25-oct-2026 (C97), y su auditoría (Control maestro, filas 88-97) sigue con comprobaciones «Pendiente».
    - Sensibilidad del escenario malo y del precio de Sí a r ±2 puntos: la hoja solo da la sensibilidad del valor ponderado.

### Comprobaciones mecánicas y normalizaciones

    {
      "comprobaciones": {
        "avisos": [
          "Filtro calidad: motivo de más de 400 caracteres.",
          "Filtro balance: motivo de más de 400 caracteres."
        ],
        "nota": "Comprobaciones mecánicas informativas: no acreditan la calidad económica."
      },
      "normalizaciones": []
    }

