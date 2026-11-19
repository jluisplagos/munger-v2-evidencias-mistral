# Cribado · Sulzer

Estado de la ejecución: `AUDITORIA_DOCUMENTAL_PENDIENTE_ACEPTACION`

Cribado pendiente de revisión humana. No es una recomendación de compra, ni aceptación, ni aptitud para dinero real. Tasa 9 % provisional.

C-ARR (decisión de la persona responsable): los arrendamientos se cuentan una sola vez, en el flujo. El alquiler se resta de la caja libre; la deuda, deuda/EBITDA y deuda/caja libre se miden sin arrendamientos; el pasivo por arrendamientos se muestra aparte, como dato.

Cifras de la etapa 1 tal como las guardó la hoja, a su fecha de análisis; sin las decisiones posteriores (P-O1, P-O2, F1-A/F1-B, D-US1/2, D-WM) ni verificación contra la fuente oficial.

| Campo | Valor |
|---|---|
| Fecha de la hoja | 2026-11-08 |
| Tarea | cribado-44512238939-sulzer |
| SHA del código | 833cd50a9bba34006519119c72a29c70a1656fb7 |
| Huella del paquete (package_sha256) | 1443ea88a6c57c599e7b165a4c13888b4be020263888ce3fbd2af440903eee93 |
| Huella del envío (bundle_sha256) | a8279eee3f95ed33e84b3e8303f8febae236ad39f5632058d7691c9af97717a8 |
| Huella del encargo | 32b5c7f313e61a61fb0f5e68a75b3c44004eb902e97b98720fb98fa8d383e6cf |
| Huella de la Release | 4d30f7352948fe7e7fe3b133386eabedbddcc71d997e972a1c6db7964d58b0a9 |
| Huella del libro | 06824c975d60eee315e8659aaad193d1ef7628da22bfe47ecc142244e53c3888 |
| Modelo pedido / devuelto | claude-opus-5-5 / claude-opus-5-5 |
| Esfuerzo | high |
| Gramática del servidor | True |
| Mensajes enviados | 1 |
| Cota de entrada antes de llamar | 155635 tokens |
| Reserva estimada antes de llamar | USD 1.2779 |
| Uso de tokens | entrada 69416, salida 4432 |
| Coste | CONOCIDO_ESTIMADO; estimado USD 0.366304; cota 0.366304 |

| id | ruta | sha256 | bytes |
|---|---|---|---|
| respuesta | EMPRESAS_LOTES_COMPLETOS/Sulzer/Sulzer_respuesta.md | d467ae5b74022f665fb3513d9c7e19c7e662a397fa6e2f268d3bec6de309bff4 | 46669 |
| hoja_analisis | EMPRESAS_LOTES_COMPLETOS/Sulzer/Sulzer_evaluada.xlsx#Análisis | f350af0d94e286b87e0457de801dcad663c06be1e3cfebd8ba52a1d327931392 | 23926 |
| hoja_control_maestro | EMPRESAS_LOTES_COMPLETOS/Sulzer/Sulzer_evaluada.xlsx#Control maestro | 331f3bb01ca6ad369a5e508919a35565379c67c4491ef24cf281405d91e794ff | 63790 |

## Salida del modelo (datos, sin acciones ejecutables)

Veredicto `vigilar` · DCF de la plantilla aplica: `si`

| Filtro | Resultado |
|---|---|
| calidad | pasa |
| caja | dudoso |
| balance | pasa |
| precio | no_pasa |
| encaje | no_aplica |

### Pasivo por arrendamientos (dato aparte)

    Control maestro!M51 = 123.2 (pasivo por arrendamientos a 30-jun-2026; deuda total con arrendamientos 1.201,9 en Análisis!C54)


### Tipo de negocio y motor

    Industrial de bienes de equipo semicíclico: bombas y equipos de fluidos (Flow, 43,6% de las ventas), servicios de posventa recurrentes (Services, 36,9%) y tecnología de separación química (Chemtech, 19,4%), con parte de los proyectos reconocida por avance de obra.
    El DCF de caja libre de la plantilla, pero sobre una caja libre normalizada de ciclo medio (con el circulante de proyectos normalizado), por la parte cíclica de proyectos y la caída de pedidos.

### calidad

    El negocio se entiende y muestra calidad en las cifras (ROIC del 20,1%, margen EBITDA del 10,0% en 2019 al 15,6% en 2025 y ningún cliente significativo), con la reserva de que el 48,82% del capital está en manos de un accionista sancionado y los pedidos caen un 8,9% en H1 2026; el «DESCARTAR · demasiado difícil» de Análisis!A6 viene del filtro de etapa 1 (C13 = No) y no lo comparto, porque el negocio sí se entiende.
    Dato clave: Análisis!C24 = 0.201

### caja

    La caja libre es positiva (base de 201,4 y CFO/beneficio de 1,43x a cinco años en Análisis!C26), pero cae tres años seguidos (268,3 → 201,7 → 176,0 → 145,0 LTM, Control maestro!M30) por unos activos contractuales que suben un 37,0% con ventas del −4,1%, y la conversión anual ha bajado a 0,92x LTM.
    Dato clave: Análisis!C52 = 201.4

### balance

    Sin arrendamientos, la deuda es de 1.078,7 frente a una caja de 843,2 (Análisis!C53), así que la deuda neta ronda 235,5: unas 0,45x un EBITDA de unos 525 una vez restado el alquiler y 1,2x la caja libre base de 201,4; aun sumando los 367,3 de pasivos con Tiwel/Renova queda en torno a 1,15x, holgado para un negocio semicíclico; el 0,64x de Análisis!C33 incluye arrendamientos y no sirve tal cual.
    Dato clave: Control maestro!M51 = 1078.7

### precio

    La cotización de 178,6 está muy por encima del precio de Sí de unos 72 (escenario malo de 71,5), del valor ponderado de 111,5 (Análisis!C83) e incluso del escenario bueno de 163,9; el precio exige un crecimiento del 11,8% anual (Análisis!C86) y ni con r al 7% (160,2 en Análisis!C91 de la fila 90) lo alcanza.
    Dato clave: Análisis!C37 = 178.6

### encaje

    El paquete no trae la cartera de la persona responsable y la hoja solo da contexto de mercado (capitalización de 6.047 mm CHF), así que este filtro no aplica y no elimina.
    Dato clave: Análisis!C41 = 6047

### Qué lo cambiaría

    - Una cotización por debajo de unos 111,5 CHF (valor ponderado de la hoja) o cerca del precio de Sí de unos 72 CHF pasaría el filtro de precio y llevaría a estudiar_a_fondo.
    - Que la caja libre LTM vuelva por encima de 250 con conversión de los activos contractuales en H2 2026 despejaría la duda de caja.
    - Que el margen de Services caiga por debajo del 15% dos años seguidos, o que los pasivos con Tiwel/Renova (367,3) se conviertan en salidas recurrentes, rebajaría calidad o balance y llevaría a descartar.

### Qué falta

    - El alquiler total pagado (principal más intereses de arrendamientos) del periodo LTM, para fijar con exactitud el EBITDA después de alquiler; la hoja solo da el principal medio (30,5) y una sensibilidad sin arrendamientos de 0,42–0,45x.
    - Fechas incoherentes: la respuesta y varias celdas de Control maestro citan decisiones del 15-nov-2026, posteriores a la fecha de la hoja (08-nov-2026); el precio de 178,6 es el cierre del 6-nov-2026 de fuentes secundarias.
    - Desglose de ventas por mercado final posterior a 2020 y umbrales de los covenants de la línea sindicada de 500, que no figuran en el paquete.

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

