# Cribado · Oil-Dri

Estado de la ejecución: `AUDITORIA_DOCUMENTAL_PENDIENTE_ACEPTACION`

Cribado pendiente de revisión humana. No es una recomendación de compra, ni aceptación, ni aptitud para dinero real. Tasa 9 % provisional.

C-ARR (decisión de la persona responsable): los arrendamientos se cuentan una sola vez, en el flujo. El alquiler se resta de la caja libre; la deuda, deuda/EBITDA y deuda/caja libre se miden sin arrendamientos; el pasivo por arrendamientos se muestra aparte, como dato.

Cifras de la etapa 1 tal como las guardó la hoja, a su fecha de análisis; sin las decisiones posteriores (P-O1, P-O2, F1-A/F1-B, D-US1/2, D-WM) ni verificación contra la fuente oficial.

| Campo | Valor |
|---|---|
| Fecha de la hoja | 2026-10-09 |
| Tarea | cribado-44509331308-oil-dri |
| SHA del código | 833cd50a9bba34006519119c72a29c70a1656fb7 |
| Huella del paquete (package_sha256) | c8af6995af0d53d7f904ed1f4c63d43c10a518235626e80bafc65851473ca096 |
| Huella del envío (bundle_sha256) | ab583e48f843eb2e3f4c9578139bf0549f3b7d3c0f13e70808788d598941d527 |
| Huella del encargo | 32b5c7f313e61a61fb0f5e68a75b3c44004eb902e97b98720fb98fa8d383e6cf |
| Huella de la Release | 4d30f7352948fe7e7fe3b133386eabedbddcc71d997e972a1c6db7964d58b0a9 |
| Huella del libro | eff1ab29052a4c1d1dd6dd82cf65ff8d1f23f5658d1d62034405276c0d7d0879 |
| Modelo pedido / devuelto | claude-opus-5-5 / claude-opus-5-5 |
| Esfuerzo | high |
| Gramática del servidor | True |
| Mensajes enviados | 1 |
| Cota de entrada antes de llamar | 128395 tokens |
| Reserva estimada antes de llamar | USD 1.16894 |
| Uso de tokens | entrada 58358, salida 3311 |
| Coste | CONOCIDO_ESTIMADO; estimado USD 0.299652; cota 0.299652 |

| id | ruta | sha256 | bytes |
|---|---|---|---|
| respuesta | EMPRESAS_LOTES_COMPLETOS/Oil-Dri/Oil-Dri_respuesta.md | 78d8c072ea36a5f0a48c0844fe889799967b4569ccd5b72f161bc075ce1b6791 | 32187 |
| hoja_analisis | EMPRESAS_LOTES_COMPLETOS/Oil-Dri/Oil-Dri_evaluada.xlsx#Análisis | dbb51724f29d269c504660d1c68dee6384306b8b96f8b63475b1b52495bbdbad | 23692 |
| hoja_control_maestro | EMPRESAS_LOTES_COMPLETOS/Oil-Dri/Oil-Dri_evaluada.xlsx#Control maestro | dc2d36fc842450f975098715e894c4a495b4f5a9f00811d35e51821c2488a228 | 51760 |

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

    Control maestro!N51 = 14.7 (arrendamientos operativos, US GAAP; sin arrendamientos financieros materiales)


### Tipo de negocio y motor

    Productor integrado de minerales absorbentes (arcilla de minas propias) con venta de consumo básico, sobre todo arena para gatos, y productos B2B; cíclico por costes (flete, energía, embalaje) más que por demanda.
    Caja de ciclo medio: normalizar la caja libre sobre un ciclo completo de costes (por ejemplo, FY22–FY26 en lugar de solo FY24–FY26) y separar el capex de mantenimiento del de crecimiento antes de aplicar el DCF al 9 %.

### calidad

    El negocio se entiende: extrae arcilla propia y la vende como arena para gatos y absorbentes. El ROIC del 17,5 % solo existe desde FY23, el margen operativo osciló entre el 1,4 % y el 14 % en la década y Walmart pesa el 18 %, así que la ventaja no está probada a lo largo de un ciclo de costes.
    Dato clave: Análisis!C24 = 0.175

### caja

    La conversión de beneficio en caja operativa es alta (1,51x, Análisis!C26) y el FCF base de 3 años es de 35,5 mm, pero la caja libre no es estable. Según Control maestro!N43 fue negativa en FY18, FY21 y FY22, la media de 5 años con SBC baja a unos 22,6 mm y el capex es unas 1,5 veces la amortización sin desglose de mantenimiento.
    Dato clave: Análisis!C52 = 35.452

### balance

    La deuda financiera sin arrendamientos es de 39 mm frente a 73,7 mm de caja (Análisis!C53), es decir, caja neta. La deuda neta/EBITDA es de -0,38x (Análisis!C33) con un EBITDA US GAAP de 91,2 mm que ya resta el alquiler operativo. Los vencimientos son pequeños y la holgura sobra incluso para un negocio cíclico de costes.
    Dato clave: Análisis!C54 = 39

### precio

    La cotización de 84,37 $ (Análisis!C37) está muy por encima del valor ponderado de 47,48 $ al 9 % y también del escenario bueno de 71,81 $ (Análisis!D78); sigue por encima incluso con r al 7 % (70,19 $, Análisis!C91). El precio exige un crecimiento del 12,8 % anual (Análisis!C86), y con una base de caja de ciclo medio el valor saldría aún más bajo.
    Dato clave: Análisis!C83 = 47.4755556192232

### encaje

    El paquete no trae la cartera de la persona responsable, y la hoja solo aporta contexto como la capitalización de 1.221,6 mm, que no decide el encaje; este filtro no elimina.
    Dato clave: Análisis!C41 = 1221.6

### Qué lo cambiaría

    - Una cotización por debajo del valor ponderado de la hoja (≈47 $), o cercana al valor con caja de ciclo medio, pasaría el precio a estudiar_a_fondo.
    - Que el próximo choque de costes se supere con un margen operativo por encima del 12 % y un ROIC por encima del 15 % confirmaría la calidad.
    - Que FY27 vuelva a una caja libre negativa o por debajo de 30 mm sin un capex extraordinario que lo explique, o que el DSO quede por encima de 54 días, inclinaría hacia descartar.

### Qué falta

    - El desglose del capex entre mantenimiento y crecimiento: el capex de 34,2 mm frente a una amortización de unos 23 mm decide la caja normalizada.
    - Una cotización posterior a los resultados FY26: la de la hoja es el cierre del 08/10/2026, previo a su publicación, y el 09/10 ya cotizaba ≈85 $ intradía.
    - Las series de cuota de mercado y la identidad de los competidores, y el proxy con el % de insiders y los incentivos (Análisis!C96 vacía).

### Comprobaciones mecánicas y normalizaciones

    {
      "comprobaciones": {
        "avisos": [],
        "nota": "Comprobaciones mecánicas informativas: no acreditan la calidad económica."
      },
      "normalizaciones": []
    }

