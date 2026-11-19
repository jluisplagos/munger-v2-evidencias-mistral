# Cribado · Oyak

Estado de la ejecución: `AUDITORIA_DOCUMENTAL_PENDIENTE_ACEPTACION`

Cribado pendiente de revisión humana. No es una recomendación de compra, ni aceptación, ni aptitud para dinero real. Tasa 9 % provisional.

C-ARR (decisión de la persona responsable): los arrendamientos se cuentan una sola vez, en el flujo. El alquiler se resta de la caja libre; la deuda, deuda/EBITDA y deuda/caja libre se miden sin arrendamientos; el pasivo por arrendamientos se muestra aparte, como dato.

Cifras de la etapa 1 tal como las guardó la hoja, a su fecha de análisis; sin las decisiones posteriores (P-O1, P-O2, F1-A/F1-B, D-US1/2, D-WM) ni verificación contra la fuente oficial.

| Campo | Valor |
|---|---|
| Fecha de la hoja | 2026-11-01 |
| Tarea | cribado-44509331308-oyak |
| SHA del código | 833cd50a9bba34006519119c72a29c70a1656fb7 |
| Huella del paquete (package_sha256) | 92e162c03779f9bec423dc52f73884ad00685f97af3aa9ff9bd9f0f7f54c5718 |
| Huella del envío (bundle_sha256) | 8a096f3fd3e715d77e136b53bb470c37d7c733e9c0e42469eccae993324f0038 |
| Huella del encargo | 32b5c7f313e61a61fb0f5e68a75b3c44004eb902e97b98720fb98fa8d383e6cf |
| Huella de la Release | 4d30f7352948fe7e7fe3b133386eabedbddcc71d997e972a1c6db7964d58b0a9 |
| Huella del libro | ba2254a9e294913feb1bfe841b2f2bb16fca44b5e123235f5eabc1fd5d75b5bd |
| Modelo pedido / devuelto | claude-opus-5-5 / claude-opus-5-5 |
| Esfuerzo | high |
| Gramática del servidor | True |
| Mensajes enviados | 1 |
| Cota de entrada antes de llamar | 130504 tokens |
| Reserva estimada antes de llamar | USD 1.177376 |
| Uso de tokens | entrada 58683, salida 3589 |
| Coste | CONOCIDO_ESTIMADO; estimado USD 0.306512; cota 0.306512 |

| id | ruta | sha256 | bytes |
|---|---|---|---|
| respuesta | EMPRESAS_LOTES_COMPLETOS/Oyak/Oyak_respuesta.md | 6af64e06f0a7cdb79d166dcd919913cae6065b167aa848bd9492d26659cf97d5 | 31699 |
| hoja_analisis | EMPRESAS_LOTES_COMPLETOS/Oyak/Oyak_evaluada.xlsx#Análisis | 551e5fe1c2048ce38bc164b8de89ac6f5589c3200fbc42cd33d991196e40c472 | 23178 |
| hoja_control_maestro | EMPRESAS_LOTES_COMPLETOS/Oyak/Oyak_evaluada.xlsx#Control maestro | b6c70e84657816b0f8725d58f59afa340e9fcf9c2371a4c94c3ed1fc12228c6d | 54889 |

## Salida del modelo (datos, sin acciones ejecutables)

Veredicto `vigilar` · DCF de la plantilla aplica: `dudoso`

| Filtro | Resultado |
|---|---|
| calidad | dudoso |
| caja | dudoso |
| balance | pasa |
| precio | dudoso |
| encaje | no_aplica |

### Pasivo por arrendamientos (dato aparte)

    Control maestro!M51 = 350.5 (arrendamientos TFRS 16 a 30-jun-2026, incluidos en la deuda total de Análisis!C54 = 3056)


### Tipo de negocio y motor

    Cíclico de materias primas: productor de cemento y hormigón en Turquía, con exceso de capacidad en el país y flujos en TRY constantes (TMS 29).
    Caja libre de ciclo medio (margen y capex de mantenimiento normalizados a lo largo de un ciclo completo), contrastada con el coste de reposición de la capacidad, en lugar del DCF de la plantilla con una base de 3 años en pleno ciclo de capex.

### calidad

    El negocio se entiende: cemento y hormigón en Turquía, con un margen operativo del 30,9 % en el cemento en 2025. Pero el ROCE real estimado ha caído del 26,9 % al 15,5 % y el margen operativo del 25,1 % al 15,8 % en el 1S 2026, con exceso de capacidad declarado y muchas operaciones con vinculadas de un controlador con el 80,05 %; por eso no veo demostrada una ventaja duradera, aunque discrepo del 'demasiado difícil' de la etapa 1.
    Dato clave: Análisis!C24 = 0.155

### caja

    La caja libre base es positiva, 3.664 mm de media en 2023-2025, pero la serie baja: 3.278 mm en los últimos doce meses (C40) y −1.265 m TL en el 1S 2026 según la respuesta. Además, el capex de 7.999 mm se come el 62 % de la caja operativa, es 1,8-2,9 veces la amortización y no se sabe qué parte es de mantenimiento; la conversión caja operativa/beneficio es de 0,778 (C26).
    Dato clave: Análisis!C52 = 3664

### balance

    Sin arrendamientos, la deuda bancaria es de 2.705,5 mm frente a una caja de 12.230 mm, una caja neta de unos 9.525 mm. Equivale a unas −0,58x el EBITDA LTM de 16.539 mm después de restar unos 229 mm de pagos por arrendamientos, y sigue siendo caja neta aunque se sume el saldo con la matriz CGH (1.818,9 mm). El préstamo vence entero a corto plazo, pero la caja lo cubre 4,3 veces; el −0,555x de Análisis!C33 incluye arrendamientos y no se usa tal cual.
    Dato clave: Control maestro!M51 = 2705.5 (deuda bancaria sin arrendamientos, frente a caja Análisis!C53 = 12230)

### precio

    A 17,88 TRY la cotización está un 23 % por encima del valor ponderado a 9 % (14,58 TRY) y lejos del escenario malo (7,09 TRY), y no hay precio de Sí. Aun así, el resultado cambia con 2 puntos de tasa (20,55 TRY al 7 %, C90), la hoja es anterior a los 9M2026 y el DCF de un cíclico es de aplicabilidad dudosa.
    Dato clave: Análisis!C83 = 14.5753667668016

### encaje

    El paquete no trae la cartera; la hoja solo indica una capitalización de 86.443 mm y un tamaño de posición de la etapa 1 que no se hereda, así que este filtro no elimina.
    Dato clave: Análisis!C41 = 86443

### Qué lo cambiaría

    - Que los 9M2026 o el FY2026 muestren un margen operativo de en torno al 20 % o más y caja libre positiva con el capex a la baja (hacia estudiar a fondo); si el margen queda por debajo del 16 %, con existencias al alza y caja libre negativa, hacia descartar.
    - Una cotización por debajo del valor ponderado de 14,58 TRY a 9 % (Análisis!C83).
    - Un desglose de la empresa que sitúe el capex de mantenimiento cerca de la amortización (3.497 m TL en 2025).

### Qué falta

    - Resultados 9M2026, previstos a primeros de noviembre y posteriores a la fecha de la hoja (2026-11-01).
    - Desglose del capex entre mantenimiento y crecimiento, que decide si la caja libre base de 3.664 mm está deprimida o es la normal.
    - Toneladas, precio real por tonelada y márgenes de competidores durante un ciclo, para separar la ventaja de OYAK de la del nicho.

### Comprobaciones mecánicas y normalizaciones

    {
      "comprobaciones": {
        "avisos": [
          "Filtro calidad: motivo de más de 400 caracteres.",
          "Filtro balance: motivo de más de 400 caracteres.",
          "Un texto menciona un tamaño de posición o un porcentaje de cartera."
        ],
        "nota": "Comprobaciones mecánicas informativas: no acreditan la calidad económica."
      },
      "normalizaciones": []
    }

