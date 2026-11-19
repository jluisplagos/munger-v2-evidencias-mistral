# Cribado · FW_Thorpe

Estado de la ejecución: `AUDITORIA_DOCUMENTAL_PENDIENTE_ACEPTACION`

Cribado pendiente de revisión humana. No es una recomendación de compra, ni aceptación, ni aptitud para dinero real. Tasa 9 % provisional.

C-ARR (decisión de la persona responsable): los arrendamientos se cuentan una sola vez, en el flujo. El alquiler se resta de la caja libre; la deuda, deuda/EBITDA y deuda/caja libre se miden sin arrendamientos; el pasivo por arrendamientos se muestra aparte, como dato.

Cifras de la etapa 1 tal como las guardó la hoja, a su fecha de análisis; sin las decisiones posteriores (P-O1, P-O2, F1-A/F1-B, D-US1/2, D-WM) ni verificación contra la fuente oficial.

| Campo | Valor |
|---|---|
| Fecha de la hoja | 2026-10-30 |
| Tarea | cribado-44502520327-fw-thorpe |
| SHA del código | 833cd50a9bba34006519119c72a29c70a1656fb7 |
| Huella del paquete (package_sha256) | 4de71d2389f636217a63db4f5e752d95eedb05ebd76d80eb2b5762a064278d0b |
| Huella del envío (bundle_sha256) | 5635c675c28fd597b8fc7205c7e0dff335c6fe490394f8d0944a710ab98ec3bd |
| Huella del encargo | 32b5c7f313e61a61fb0f5e68a75b3c44004eb902e97b98720fb98fa8d383e6cf |
| Huella de la Release | 4d30f7352948fe7e7fe3b133386eabedbddcc71d997e972a1c6db7964d58b0a9 |
| Huella del libro | b9c564553df6c3aa5c4e50520225939fa82bd90a5e4e1c90e759b49f87d42007 |
| Modelo pedido / devuelto | claude-opus-5-5 / claude-opus-5-5 |
| Esfuerzo | high |
| Gramática del servidor | True |
| Mensajes enviados | 1 |
| Cota de entrada antes de llamar | 130384 tokens |
| Reserva estimada antes de llamar | USD 1.176896 |
| Uso de tokens | entrada 59429, salida 3301 |
| Coste | CONOCIDO_ESTIMADO; estimado USD 0.303736; cota 0.303736 |

| id | ruta | sha256 | bytes |
|---|---|---|---|
| respuesta | EMPRESAS_LOTES_COMPLETOS/FW_Thorpe/FW_Thorpe_respuesta.md | 2119beb5ea011fb4d57e4bd1416387c8ca225af3e86f92d8a112064a61a16857 | 31373 |
| hoja_analisis | EMPRESAS_LOTES_COMPLETOS/FW_Thorpe/FW_Thorpe_evaluada.xlsx#Análisis | 2055f34b6765a230e8793d1f33133ec1b1adfefbef4fb9cc754777350ca08df8 | 23638 |
| hoja_control_maestro | EMPRESAS_LOTES_COMPLETOS/FW_Thorpe/FW_Thorpe_evaluada.xlsx#Control maestro | 1f642ab6af976ddf890540ee2d83c3feb834dd34c077a790b1c817c784103afc | 54017 |

## Salida del modelo (datos, sin acciones ejecutables)

Veredicto `estudiar_a_fondo` · DCF de la plantilla aplica: `si`

| Filtro | Resultado |
|---|---|
| calidad | pasa |
| caja | pasa |
| balance | pasa |
| precio | dudoso |
| encaje | no_aplica |

### Pasivo por arrendamientos (dato aparte)

    Control maestro!M51 = 3.611 (£mm, a 30-jun-2026; fuera del cociente de deuda)


### Tipo de negocio y motor

    Fabricante industrial de luminarias profesionales y de emergencia (Reino Unido, Países Bajos, España), con demanda ligada a la inversión en edificios y obra pública; estable, con algo de ciclo.
    El DCF de caja libre de la plantilla, porque es un fabricante estable sin deuda, contrastado con una caja de ciclo medio por su exposición a la construcción y a la obra pública.

### calidad

    El negocio se entiende y es de calidad: ROCE del 15,6 % con caja (22,5 % sin caja) y margen operativo estable en el 17–19 % durante una década, sin cliente por encima del 10 %; pesan las ventas planas FY24–26 (−0,5/−0,3/−1,3 %), las compras fallidas (SchahlLED) y un consejo familiar con un solo independiente; discrepo del «DESCARTAR · demasiado difícil» de A6, que nace de C13 = No y no de que el negocio no se entienda.
    Dato clave: Análisis!C24 = 0.156

### caja

    Convierte el beneficio en caja de forma recurrente: CFO/beneficio de 1,32, FCF base de 25,3 £mm con capex de 8,1 £mm frente a un CFO de 35,1 £mm y FCF positivo doce años seguidos, aunque el FCF del accionista baja en FY24–26 (32,9/23,7/20,8 £mm).
    Dato clave: Análisis!C52 = 25.333

### balance

    La deuda neta/EBITDA de la hoja (−1,02x en Análisis!C33) incluye arrendamientos; sin ellos, préstamos de 0,853 £mm frente a caja de 47,176 £mm dan una caja neta de ≈46,3 £mm (≈−1,14x sobre el EBITDA sin NIIF 16 de ≈40,530), sin vencimientos relevantes y con una política declarada de no endeudarse.
    Dato clave: Control maestro!M51 = 0.853 (préstamos sin arrendamientos; Análisis!C54 = 4.464 los incluye)

### precio

    La cotización de 2,56 £ está ≈8 % por encima del precio de Sí (escenario malo de 2,37 £), pero cerca de él; queda un 31 % por debajo del ponderado de 3,71 £, y con r +2 puntos el ponderado sigue en 2,88 £, de modo que el resultado depende de qué referencia se tome.
    Dato clave: Análisis!B78 = 2.36776970403238 (cotización Análisis!C37 = 2.56)

### encaje

    El paquete no trae la cartera de la persona responsable; la hoja solo da contexto, como un 47,7 % de insiders, y este filtro no elimina.
    Dato clave: Análisis!C96 = 0.4774142521292784

### Qué lo cambiaría

    - Una cotización por debajo de 2,37 £ (Análisis!B78) haría pasar el filtro de precio sin dudas.
    - Un margen operativo del grupo por debajo del 15 % dos años seguidos, o un FCF sin circulante inferior a 22 £mm en FY27, rebajaría calidad y caja.
    - Una adquisición grande financiada con deuda o con pasivos de rescate cambiaría el balance y la aplicabilidad del DCF.

### Qué falta

    - Varias decisiones de la hoja (ventana de medias de C46–C50, C24) llevan fecha 08-nov-2026, posterior a la fecha de corte del 30-oct-2026: conviene confirmar la versión del libro.
    - El precio de 2,56 £ es cum-dividendo (ex-dividendo 5-nov-2026, 5,53p) y la propia hoja pide actualizarlo; el EBITDA sin arrendamientos (40,530) es aproximado.
    - Falta el crecimiento orgánico separado de compras y precios, y la holgura del test de deterioro del goodwill de SchahlLED (14,3 £mm), no cuantificada desde FY24.

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

