# Cribado · Gubre_Fabrikalari

Estado de la ejecución: `AUDITORIA_DOCUMENTAL_PENDIENTE_ACEPTACION`

Cribado pendiente de revisión humana. No es una recomendación de compra, ni aceptación, ni aptitud para dinero real. Tasa 9 % provisional.

C-ARR (decisión de la persona responsable): los arrendamientos se cuentan una sola vez, en el flujo. El alquiler se resta de la caja libre; la deuda, deuda/EBITDA y deuda/caja libre se miden sin arrendamientos; el pasivo por arrendamientos se muestra aparte, como dato.

Cifras de la etapa 1 tal como las guardó la hoja, a su fecha de análisis; sin las decisiones posteriores (P-O1, P-O2, F1-A/F1-B, D-US1/2, D-WM) ni verificación contra la fuente oficial.

| Campo | Valor |
|---|---|
| Fecha de la hoja | 2026-10-30 |
| Tarea | cribado-44502520327-gubre-fabrikalari |
| SHA del código | 833cd50a9bba34006519119c72a29c70a1656fb7 |
| Huella del paquete (package_sha256) | bb2b7aa067e628761358ee155eaf25aa62ab3a7f16ba0ec3fc0a5618823b1214 |
| Huella del envío (bundle_sha256) | 35ab23366c301a6d63dd89ac1758c717df4cc810ceea1e48598dcca5a74530e2 |
| Huella del encargo | 32b5c7f313e61a61fb0f5e68a75b3c44004eb902e97b98720fb98fa8d383e6cf |
| Huella de la Release | 4d30f7352948fe7e7fe3b133386eabedbddcc71d997e972a1c6db7964d58b0a9 |
| Huella del libro | e09af22a1e0c1c1ac6c3ff679346c161d8a42203f0bb41088e1666c946dbd736 |
| Modelo pedido / devuelto | claude-opus-5-5 / claude-opus-5-5 |
| Esfuerzo | high |
| Gramática del servidor | True |
| Mensajes enviados | 1 |
| Cota de entrada antes de llamar | 129724 tokens |
| Reserva estimada antes de llamar | USD 1.174256 |
| Uso de tokens | entrada 58410, salida 4340 |
| Coste | CONOCIDO_ESTIMADO; estimado USD 0.32044; cota 0.32044 |

| id | ruta | sha256 | bytes |
|---|---|---|---|
| respuesta | EMPRESAS_LOTES_COMPLETOS/Gubre_Fabrikalari/Gubre_Fabrikalari_respuesta.md | a4caa0d3f95d520df002c29c6bd1ce4d79f0a8839cf1e2585a4e9de166f21f67 | 30759 |
| hoja_analisis | EMPRESAS_LOTES_COMPLETOS/Gubre_Fabrikalari/Gubre_Fabrikalari_evaluada.xlsx#Análisis | f160c60a447e790544b210901601204764e504b4f7e0c4cc5d998f800357f2b5 | 22766 |
| hoja_control_maestro | EMPRESAS_LOTES_COMPLETOS/Gubre_Fabrikalari/Gubre_Fabrikalari_evaluada.xlsx#Control maestro | df4be55c20fa20b5c8be56593dccefeb65329725d1819da74ff81a4184c15fc0 | 55233 |

## Salida del modelo (datos, sin acciones ejecutables)

Veredicto `demasiado_dificil` · DCF de la plantilla aplica: `no`

| Filtro | Resultado |
|---|---|
| calidad | dudoso |
| caja | dudoso |
| balance | pasa |
| precio | dudoso |
| encaje | no_aplica |

### Pasivo por arrendamientos (dato aparte)

    Control maestro!M51 = 112.5 (pasivo por arrendamientos TFRS 16 a 30-06-26, de los que 51,2 a corto según Control maestro!M37)


### Tipo de negocio y motor

    Cíclica / materias primas: revendedor de fertilizante, casi todo importado y con margen del 3 %, más una mina de oro de vida no publicada que aporta casi todo el beneficio; con una filial iraní mantenida para la venta y un accionista de control que es a la vez el cliente principal.
    Suma de partes: la mina valorada por su vida (reservas × ley × margen por onza, año a año hasta el cierre, con oro de ciclo medio), el fertilizante con caja de ciclo medio, y Razi como opción o como pasivo.

### calidad

    El ROCE consolidado de 25,9 % sale casi entero de una mina de oro (51,3 % frente al 2,5 % del fertilizante, que tiene un margen del 3 %), y sin reservas, ley ni coste por onza publicados no se puede juzgar cuánto dura esa rentabilidad, a lo que se suman un 75 % de ventas al accionista de control, salvedades del auditor desde 2017 y un anticipo de 7.252 a filiales de TKK; coincido con las banderas de C12 y C18 de la hoja.
    Dato clave: Análisis!C24 = 0.259

### caja

    La caja libre base de 2.865 (media 2023–25) es menos de un tercio de los 10.064,2 TTM, la serie CFO−capex incluye años negativos (−3.485 en 2022) y el CFO/beneficio de 5,4 está inflado por la pérdida monetaria TMS 29 (0,87 sin ella), así que la caja reciente es un escalón de la mina y no está demostrada su recurrencia.
    Dato clave: Análisis!C52 = 2865 frente a Análisis!C40 = 10064.2

### balance

    Sin arrendamientos, la deuda de 9.624,4 frente a una caja de 15.043,4 deja caja neta de unos −5.419 (≈−0,39x un EBITDA TTM de 14.138,4 menos ≈93 de alquiler), y aun descontando el dividendo, las recompras y el anticipo posteriores (≈8.930) quedaría una deuda neta de ≈0,25x, holgada incluso para un negocio cíclico; el riesgo está en que el 100 % vence a menos de un año y el 77 % es en USD (Control maestro!N36).
    Dato clave: Control maestro!M51 = 9624.4 (préstamos sin arrendamientos; caja Análisis!C53 = 15043.4)

### precio

    La cotización de 250,25 supera el ponderado de la plantilla (151,88), su precio de Sí mecánico (≈71,5) y hasta el valor con r al 7 % (213,14), pero el DCF de la plantilla no aplica a una mina que se agota y el FCF TTM da un rendimiento del 12,1 %, así que sin un valor de la mina por su vida no se puede concluir.
    Dato clave: Análisis!C37 = 250.25 frente a Análisis!C83 = 151.881101236916

### encaje

    El paquete no trae la cartera de la persona responsable y la hoja solo da datos de la sociedad, como una capitalización de 82.888,1 mn TL con un free float del 21,12 %, así que este filtro no se puede evaluar ni elimina nada.
    Dato clave: Análisis!C41 = 82888.1

### Qué lo cambiaría

    - Un informe técnico de reservas que muestre una vida de mina larga (más de 12–15 años) con coste por onza bajo: pasaría a estudiar_a_fondo con el motor de suma de partes.
    - Que se confirme que el anticipo de 7.252 mn TL no tiene condiciones de mercado o que siguen las transferencias al controlador: pasaría a descartar.
    - La publicación de condiciones de mercado para el anticipo (o su devolución) y unas cuentas sin salvedades, con caja neta positiva después de las salidas posteriores al cierre.

### Qué falta

    - Reservas con ley, recuperación, coste por onza (AISC) y plan y vida de la mina de Söğüt: sin ellos no se puede aplicar el motor adecuado.
    - Condiciones del anticipo de 7.252 mn TL a filiales de TKK (solo hay fuente secundaria) y del contrato de distribución con TKK, que concentra el 75 % de las ventas.
    - Covenants y calendario de refinanciación de una deuda que vence entera a menos de un año; además, el Control maestro cita una decisión del 09-nov-2026, posterior a la fecha de corte de 2026-10-30, y la auditoría del DCF figura como pendiente.

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

