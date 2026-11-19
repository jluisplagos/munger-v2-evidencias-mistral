# Cribado · Veolia

Estado de la ejecución: `AUDITORIA_DOCUMENTAL_PENDIENTE_ACEPTACION`

Cribado pendiente de revisión humana. No es una recomendación de compra, ni aceptación, ni aptitud para dinero real. Tasa 9 % provisional.

C-ARR (decisión de la persona responsable): los arrendamientos se cuentan una sola vez, en el flujo. El alquiler se resta de la caja libre; la deuda, deuda/EBITDA y deuda/caja libre se miden sin arrendamientos; el pasivo por arrendamientos se muestra aparte, como dato.

Cifras de la etapa 1 tal como las guardó la hoja, a su fecha de análisis; sin las decisiones posteriores (P-O1, P-O2, F1-A/F1-B, D-US1/2, D-WM) ni verificación contra la fuente oficial.

| Campo | Valor |
|---|---|
| Fecha de la hoja | 2026-11-08 |
| Tarea | cribado-44515220408-veolia |
| SHA del código | 833cd50a9bba34006519119c72a29c70a1656fb7 |
| Huella del paquete (package_sha256) | b8720edaf6971cff972bef1d87ca77d68b99b4ea75a8980e85f29b853724970a |
| Huella del envío (bundle_sha256) | ba3146ee432c2c425bf68c4a4ef31bd5747f7bb77e20bae96f0f438e0870d046 |
| Huella del encargo | 32b5c7f313e61a61fb0f5e68a75b3c44004eb902e97b98720fb98fa8d383e6cf |
| Huella de la Release | 4d30f7352948fe7e7fe3b133386eabedbddcc71d997e972a1c6db7964d58b0a9 |
| Huella del libro | d83f78ce7d14d8030fccff2d5ef3cc25465c8608f0d16d58189444e823196af5 |
| Modelo pedido / devuelto | claude-opus-5-5 / claude-opus-5-5 |
| Esfuerzo | high |
| Gramática del servidor | True |
| Mensajes enviados | 1 |
| Cota de entrada antes de llamar | 167648 tokens |
| Reserva estimada antes de llamar | USD 1.325952 |
| Uso de tokens | entrada 74442, salida 5513 |
| Coste | CONOCIDO_ESTIMADO; estimado USD 0.408028; cota 0.408028 |

| id | ruta | sha256 | bytes |
|---|---|---|---|
| respuesta | EMPRESAS_LOTES_COMPLETOS/Veolia/Veolia_respuesta.md | 38e5a9f062fb5ee617bb8ed677de80c66461688238cda5b20f8059e554537fb2 | 48822 |
| hoja_analisis | EMPRESAS_LOTES_COMPLETOS/Veolia/Veolia_evaluada.xlsx#Análisis | 5fd2788b473eaabda2726ff73277008c21b09f5b46a1be6450be95b3fcaefbdd | 24907 |
| hoja_control_maestro | EMPRESAS_LOTES_COMPLETOS/Veolia/Veolia_evaluada.xlsx#Control maestro | 3a61858a19e9e6959ba6cd081254856242eb1d772bc37286fd9517b62476fa98 | 72945 |

## Salida del modelo (datos, sin acciones ejecutables)

Veredicto `faltan_datos` · DCF de la plantilla aplica: `dudoso`

| Filtro | Resultado |
|---|---|
| calidad | dudoso |
| caja | dudoso |
| balance | dudoso |
| precio | dudoso |
| encaje | no_aplica |

### Pasivo por arrendamientos (dato aparte)

    ≈ 2.177 mm a 30/06/2026 (Análisis!C54 = 33779 con NIIF 16 menos Control maestro!N51 = 31602 sin NIIF 16; cálculo propio)


### Tipo de negocio y motor

    Servicios medioambientales esenciales (agua, residuos y energía) a municipios e industriales, con contratos largos indexados y concesiones, con un componente cíclico de energía (unos 11.260 de 44.396 de ingresos) y con híbridos y minoritarios relevantes.
    Flujo atribuible al accionista ordinario (después de cupones de híbridos y de minoritarios y con el capex de mantenimiento separado) o suma de partes por negocio con capital empleado y ROCE, dado que es un grupo de contratos y concesiones con estructura financiera cambiante.

### calidad

    El negocio se entiende: servicios esenciales con contratos de 11 años de media, el 85 % indexados a la inflación, y margen EBITDA que sube del 13,3 % al 15,9 %. Pero el ROCE del 9,4 % solo supera en 2,8 puntos el WACC del 6,6 %, la empresa retiene el 47 % de las eficiencias y la hoja marca el foso como ✗; calidad media, no evidente.
    Dato clave: Análisis!C24 = 0.094

### caja

    El FCF base es positivo y creciente (−131 en 2022 y 774 en 2025, según Control maestro), pero es un residuo fino: 639 sobre 24.722,5 de capitalización (2,4 % de rendimiento según la hoja), 244 tras dividendos a minoritarios y por debajo del dividendo de 1.099. Además, no hay desglose del capex entre mantenimiento y crecimiento, así que la recurrencia queda en duda.
    Dato clave: Análisis!C52 = 639

### balance

    La hoja da 3,45x con NIIF 16 (Análisis!C33) y unos 3,44x sin ella (Control maestro!N36). Mi recálculo da unos 23.246 de deuda neta sin arrendamientos frente a un EBITDA después de alquiler de unos 6.707 (7.374 − ~667), es decir, ~3,5x EBITDA y ~36x el FCF base de 639. A eso se suman 3.600 de híbridos, una caja que cubre solo 0,80 la deuda a corto, 6.385 de papel comercial frente a un techo de 6.500 y una deuda neta un 29 % mayor en nueve meses; para un negocio contractual con BBB/Baa1 es aguantable pero no holgado, de ahí dudoso.
    Dato clave: Control maestro!N51 = 31602 (deuda bruta sin IFRS 16 a 30/06/2026); deuda neta sin arrendamientos ≈ 23.246 (25.423 − 2.177, cálculo propio)

### precio

    Con la plantilla al 9 %, los 33,78 € quedan muy por encima del precio de Sí de 8,87 €, del ponderado de 14,75 € y hasta del valor a r − 2 puntos (20,99 €), y el DCF inverso exige un 15,1 % de crecimiento. Pero la plantilla es dudosa aquí: con el NFCF publicado (1.178) o antes de capex discrecional (1.782), en lugar de 639, la conclusión podría cambiar, así que queda dudoso hasta aplicar el motor adecuado.
    Dato clave: Análisis!C78 = 8.8652779277652 (precio de Sí de la plantilla, frente a Análisis!C37 = 33.78)

### encaje

    El paquete no trae la cartera de la persona responsable y la hoja solo aporta datos de mercado, como los 24.722,5 mm de capitalización; el plan de cartera de la etapa 1 no se hereda.
    Dato clave: Análisis!C41 = 24722.5

### Qué lo cambiaría

    - Que la deuda neta sin arrendamientos baje de 3x el EBITDA después de alquiler con Clean Earth dentro y que la caja cubra la deuda a corto (hoy 0,80).
    - Que se publique un flujo del accionista ordinario, después de híbridos y minoritarios, estable y claramente superior a los 639 mm del FCF base.
    - Que, con el motor adecuado, la cotización de 33,78 € quede en el valor por acción o por debajo; con la plantilla haría falta bajar a unos 8,87 €.

### Qué falta

    - Desglose del capex contabilizado entre mantenimiento y crecimiento: la hoja dice que no lo encontró (Control maestro!N44), y es material para la caja recurrente.
    - Flujo atribuible al accionista ordinario después de cupones de híbridos y de dividendos a minoritarios, en una cifra coherente: C40 = 595 frente a C52 = 639 no cuadra con los ~450 mm/año de cupones que cita la respuesta.
    - Pasivo por arrendamientos y deuda neta a la misma fecha (la DFN es a 30/09/2026 y la deuda sin NIIF 16 a 30/06/2026); además, Control maestro cita decisiones del 15-nov-2026, posteriores a la fecha de la hoja (08/11/2026).

### Comprobaciones mecánicas y normalizaciones

    {
      "comprobaciones": {
        "avisos": [
          "Filtro balance: motivo de más de 400 caracteres.",
          "Filtro precio: motivo de más de 400 caracteres."
        ],
        "nota": "Comprobaciones mecánicas informativas: no acreditan la calidad económica."
      },
      "normalizaciones": []
    }

