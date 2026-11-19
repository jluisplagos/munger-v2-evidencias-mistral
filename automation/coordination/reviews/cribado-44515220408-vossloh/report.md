# Cribado · Vossloh

Estado de la ejecución: `AUDITORIA_DOCUMENTAL_PENDIENTE_ACEPTACION`

Cribado pendiente de revisión humana. No es una recomendación de compra, ni aceptación, ni aptitud para dinero real. Tasa 9 % provisional.

C-ARR (decisión de la persona responsable): los arrendamientos se cuentan una sola vez, en el flujo. El alquiler se resta de la caja libre; la deuda, deuda/EBITDA y deuda/caja libre se miden sin arrendamientos; el pasivo por arrendamientos se muestra aparte, como dato.

Cifras de la etapa 1 tal como las guardó la hoja, a su fecha de análisis; sin las decisiones posteriores (P-O1, P-O2, F1-A/F1-B, D-US1/2, D-WM) ni verificación contra la fuente oficial.

| Campo | Valor |
|---|---|
| Fecha de la hoja | 2026-10-08 |
| Tarea | cribado-44515220408-vossloh |
| SHA del código | 833cd50a9bba34006519119c72a29c70a1656fb7 |
| Huella del paquete (package_sha256) | c59effdd7cccae62c7c3974c756e3926dd667ad1b1ce67010ed7e9ab250c243d |
| Huella del envío (bundle_sha256) | 641e65aaf434d25e49122df1e99c254c475faf625755bf685b0728639e52fb3d |
| Huella del encargo | 32b5c7f313e61a61fb0f5e68a75b3c44004eb902e97b98720fb98fa8d383e6cf |
| Huella de la Release | 4d30f7352948fe7e7fe3b133386eabedbddcc71d997e972a1c6db7964d58b0a9 |
| Huella del libro | 7a37c29b119d43d709db538f5976a4be61b99935c5df5f9adca374aef56b293e |
| Modelo pedido / devuelto | claude-opus-5-5 / claude-opus-5-5 |
| Esfuerzo | high |
| Gramática del servidor | True |
| Mensajes enviados | 1 |
| Cota de entrada antes de llamar | 137182 tokens |
| Reserva estimada antes de llamar | USD 1.204088 |
| Uso de tokens | entrada 62746, salida 5149 |
| Coste | CONOCIDO_ESTIMADO; estimado USD 0.353964; cota 0.353964 |

| id | ruta | sha256 | bytes |
|---|---|---|---|
| respuesta | EMPRESAS_LOTES_COMPLETOS/Vossloh/Vossloh_respuesta.md | 0ea9bb265005dc034e94bf9d34a2836751acf0fab7494bf5050e777c99f4def6 | 37114 |
| hoja_analisis | EMPRESAS_LOTES_COMPLETOS/Vossloh/Vossloh_evaluada.xlsx#Análisis | 3da1fc978ee5b675b8e556e39b95dfcf905d58d99e0258829a6a521de413890c | 23218 |
| hoja_control_maestro | EMPRESAS_LOTES_COMPLETOS/Vossloh/Vossloh_evaluada.xlsx#Control maestro | 0ed89af39325803000905f079e9e9dcd19536581facb258737c2aba474b66b50 | 56112 |

## Salida del modelo (datos, sin acciones ejecutables)

Veredicto `descartar` · DCF de la plantilla aplica: `dudoso`

| Filtro | Resultado |
|---|---|
| calidad | no_pasa |
| caja | dudoso |
| balance | dudoso |
| precio | no_pasa |
| encaje | no_aplica |

### Pasivo por arrendamientos (dato aparte)

    Control maestro!M51 = 68.0 (aprox., pasivos por arrendamientos incluidos en la deuda total de 754,4 a 30-jun-2026)


### Tipo de negocio y motor

    Industrial de componentes y servicios de vía ferroviaria (sujeciones, traviesas, desvíos y mantenimiento) para gestores de infraestructura mayoritariamente públicos; cíclico, ligado al presupuesto público, y recién apalancado por la compra de Sateba.
    Caja del accionista normalizada de ciclo medio con un año completo de Sateba (o valor de empresa sobre la caja operativa menos la deuda neta y el híbrido), porque la financiación ha cambiado mucho y el DCF de la plantilla mezcla perímetros.

### calidad

    El negocio se entiende y su demanda pública es duradera, pero el ROCE antes de impuestos es del 6,4 % (4,3–5,5 % después de impuestos), por debajo del WACC antes de impuestos del 9,5 % de la propia empresa y con un máximo de 10,8 % en 2016–25, con márgenes EBIT estables pero bajos (6–9 %): no se ve ventaja en los retornos; coincide con la bandera de C18, aunque no con el «demasiado difícil» de A6.
    Dato clave: Análisis!C24 = 0.064

### caja

    La caja libre del accionista es positiva pero escasa: 33,9 mill. de base (C52) y 22,0 en los últimos doce meses (C40), un 2,3 % de la capitalización, con un capex por encima de la amortización y una conversión CFO/beneficio de 1,96 (C26) inflada por la liberación de circulante y por el impuesto contable bajo; leo con reservas el ✓ de la hoja.
    Dato clave: Análisis!C52 = 33.9

### balance

    Sin arrendamientos, la deuda es de 686,4 y la deuda neta ronda 522,9 (686,4 − 163,5 de caja, de la que 34,9 está restringida), unas 3,1 veces el EBITDA previo a la NIIF 16 (la hoja da 3,17x con arrendamientos en Análisis!C33) y unas 15 veces la caja libre base de 33,9, sin contar el híbrido de 250; es alto para un negocio cíclico y ligado al presupuesto público, aunque la caja cubre la deuda corriente 1,71x y la guía apunta a 2,8–3,0x, por lo que queda en duda y no la descarta por sí solo.
    Dato clave: Control maestro!N51 = 686.4 (deuda sin arrendamientos a 30-jun-2026)

### precio

    A 50,5 € la cotización supera el precio de Sí de 20,6 €, el ponderado de 34,54 € y aun el escenario bueno de 48,77 € (D78), y con r del 7 % el ponderado sigue en 49,66 €; aunque el DCF simplificado es dudoso por el cambio de financiación (C62), el EV/EBITDA de 9,88x frente a una mediana histórica de 8,0x y la rentabilidad por caja libre del 2,3 % apuntan en el mismo sentido.
    Dato clave: Análisis!C83 = 34.5407869956052

### encaje

    El paquete no trae la cartera de la persona responsable y la hoja no dice nada concreto sobre encaje más allá de la capitalización de 975,7 mill.; este filtro no elimina.
    Dato clave: Análisis!C41 = 975.7

### Qué lo cambiaría

    - ROCE del grupo con Sateba integrada sostenidamente por encima del 9,5 % del WACC de la empresa (y hacia el 15 %) durante varios ejercicios.
    - Caja libre del accionista con un año completo de Sateba de 50–60 mill. o más de forma recurrente, sin liberación de circulante.
    - Deuda neta sin arrendamientos por debajo de 2 veces el EBITDA y una cotización por debajo del valor ponderado de unos 34,5 €.

### Qué falta

    - Umbral del covenant de deuda neta/EBITDA del préstamo sindicado y EBITDA pro forma con Sateba en doce meses y sin NIIF 16 (la hoja solo da una aproximación de 3,10x).
    - Cifras del semestral H1 2026 tomadas vía WebFetch, pendientes de cotejo con el PDF; los resultados de 9M 2026 aún no estaban publicados a la fecha de corte.
    - Historial de caja y retornos de Sateba antes de la compra, y caja del accionista del grupo con un ejercicio completo de Sateba.

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

