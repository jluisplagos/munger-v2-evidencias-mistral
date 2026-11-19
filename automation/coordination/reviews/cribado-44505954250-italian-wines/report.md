# Cribado · Italian_Wines

Estado de la ejecución: `AUDITORIA_DOCUMENTAL_PENDIENTE_ACEPTACION`

Cribado pendiente de revisión humana. No es una recomendación de compra, ni aceptación, ni aptitud para dinero real. Tasa 9 % provisional.

C-ARR (decisión de la persona responsable): los arrendamientos se cuentan una sola vez, en el flujo. El alquiler se resta de la caja libre; la deuda, deuda/EBITDA y deuda/caja libre se miden sin arrendamientos; el pasivo por arrendamientos se muestra aparte, como dato.

Cifras de la etapa 1 tal como las guardó la hoja, a su fecha de análisis; sin las decisiones posteriores (P-O1, P-O2, F1-A/F1-B, D-US1/2, D-WM) ni verificación contra la fuente oficial.

| Campo | Valor |
|---|---|
| Fecha de la hoja | 2026-11-04 |
| Tarea | cribado-44505954250-italian-wines |
| SHA del código | 833cd50a9bba34006519119c72a29c70a1656fb7 |
| Huella del paquete (package_sha256) | 46bc436c061731a95ddc974ec8caebcc2688b173408922c8379520ee7c5a2dbb |
| Huella del envío (bundle_sha256) | 40b2c9f87c70aeaed5211daafe205af3e574da877555ea944a9c8cbb42428440 |
| Huella del encargo | 32b5c7f313e61a61fb0f5e68a75b3c44004eb902e97b98720fb98fa8d383e6cf |
| Huella de la Release | 4d30f7352948fe7e7fe3b133386eabedbddcc71d997e972a1c6db7964d58b0a9 |
| Huella del libro | 0ca0eaf0944e3183bc843738268ce5b88f3da3ff2cd98d4a42a957d4dfce8535 |
| Modelo pedido / devuelto | claude-opus-5-5 / claude-opus-5-5 |
| Esfuerzo | high |
| Gramática del servidor | True |
| Mensajes enviados | 1 |
| Cota de entrada antes de llamar | 132262 tokens |
| Reserva estimada antes de llamar | USD 1.184408 |
| Uso de tokens | entrada 59958, salida 5471 |
| Coste | CONOCIDO_ESTIMADO; estimado USD 0.349252; cota 0.349252 |

| id | ruta | sha256 | bytes |
|---|---|---|---|
| respuesta | EMPRESAS_LOTES_COMPLETOS/Italian_Wines/Italian_Wines_respuesta.md | 7c64b2efb92f41d4d3d47852467692261ee89f7dad493aa775fbc9ca0f620489 | 33807 |
| hoja_analisis | EMPRESAS_LOTES_COMPLETOS/Italian_Wines/Italian_Wines_evaluada.xlsx#Análisis | d7f08e649d69f1f9c65d520e0878ac7dde69ee60a576e3640a95a50bcdf5c2d3 | 22931 |
| hoja_control_maestro | EMPRESAS_LOTES_COMPLETOS/Italian_Wines/Italian_Wines_evaluada.xlsx#Control maestro | e80653871de156f0d813dcd8c5b434edda0994afe0ff876d8b449b29c84fc838 | 54758 |

## Salida del modelo (datos, sin acciones ejecutables)

Veredicto `estudiar_a_fondo` · DCF de la plantilla aplica: `si`

| Filtro | Resultado |
|---|---|
| calidad | dudoso |
| caja | dudoso |
| balance | pasa |
| precio | pasa |
| encaje | no_aplica |

### Pasivo por arrendamientos (dato aparte)

    Control maestro!M51 = 9.44 (pasivo por arrendamientos a 30/06/2026; fuera del cociente de deuda)


### Tipo de negocio y motor

    Embotellador y distribuidor de vino italiano de marca propia y de distribuidor, vendido sobre todo a supermercados y monopolios fuera de Italia, con poco capital tangible y crecimiento por adquisiciones.
    El DCF de caja al accionista de la plantilla, pero con una base de caja normalizada (circulante neutro, impuestos a devengo) y el cupón del bono refinanciado en lugar del 2,5 % actual.

### calidad

    Los datos apuntan en las dos direcciones: margen EBITDA ajustado estable en el 9,7-12,5 % (salvo el 8 % de 2022) y un ROCE sin goodwill del 28,8 %, frente a un ROCE total del 9,2 % antes de impuestos (≈6,6 % después), ventas comparables a la baja, precio fijado por supermercados y dos clientes con el 28 % de las ventas; la hoja marca el foso como bandera (C18 = No) y yo lo dejo en duda, no en suspenso.
    Dato clave: Análisis!C24 = 0.092

### caja

    La caja libre base de 20,45 m€ (media 2021-2025) contrasta con 5,79 m€ en los últimos doce meses, 0,37 m€ en 2021 y un CFO de -12,1 m€ en el primer semestre de 2026, y la conversión de 2,07x (Análisis!C26) está inflada por liberación de circulante, confirming de 13,6 m€ e impuestos bajos, así que la recurrencia no está demostrada.
    Dato clave: Análisis!C52 = 20.45

### balance

    Sin arrendamientos, la deuda neta de unos 72,5 m€ frente a un EBITDA LTM que resta el alquiler (≈39,06 − 3,4 ≈ 35,6 m€) da unas 2,0 veces, coherente con la sensibilidad de la hoja (~2,05x); el 2,09x de Análisis!C33 incluye arrendamientos y no sirve tal cual; es asumible para un negocio de margen estable, aunque el 92 % de la deuda es un bono de 130 m€ que vence el 13/05/2027, con caja que solo cubre 0,44x y una refinanciación anunciada sin importe ni cupón.
    Dato clave: Control maestro!M51 = 131.6 (deuda sin arrendamientos; neta ≈ 72.5 con Análisis!C53 = 59.067)

### precio

    La cotización de 14,7 € (Análisis!C37) está por debajo incluso del escenario malo (18,22 €) y del ponderado con r + 2 puntos (25,23 € en Análisis!C92); la respuesta dice que el precio de Sí «no aplica» por calidad, pero por el filtro de precio pasa, y aguanta aun con una base de caja de 14 m€ (normal ≈ 21,2 €).
    Dato clave: Análisis!B78 = 18.2169489444281

### encaje

    El paquete no trae la cartera y la hoja solo clasifica la oportunidad como «Deep value / especial» (EV/EBITDA de 5,6x en Análisis!C42), sin nada concreto sobre el encaje.
    Dato clave: Análisis!C14 = Deep value / especial

### Qué lo cambiaría

    - Que el bono nuevo salga con un cupón muy por encima del 2,5 % o con más importe para otra adquisición, lo que tensaría balance y caja.
    - Que la caja libre de 2026 completo cierre por debajo de 10 m€ sin un circulante que se revierta (caja pasaría a no_pasa).
    - Que el margen EBITDA ajustado de 2026 caiga por debajo del 11 % con ventas comparables otra vez a la baja (calidad pasaría a no_pasa).

### Qué falta

    - Importe y cupón del bono que sustituye al de 130 m€ al 2,5 % (refinanciación anunciada el 13/10/2026 sin condiciones).
    - Causa del CFO de -12,1 m€ del primer semestre de 2026 e importe cedido en factoring pro-soluto.
    - Serie de crecimiento orgánico (precio, volumen, mezcla) y peso de las Top Brands en ventas y margen.

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

