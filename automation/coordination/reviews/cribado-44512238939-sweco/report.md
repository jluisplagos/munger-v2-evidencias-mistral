# Cribado · Sweco

Estado de la ejecución: `AUDITORIA_DOCUMENTAL_PENDIENTE_ACEPTACION`

Cribado pendiente de revisión humana. No es una recomendación de compra, ni aceptación, ni aptitud para dinero real. Tasa 9 % provisional.

C-ARR (decisión de la persona responsable): los arrendamientos se cuentan una sola vez, en el flujo. El alquiler se resta de la caja libre; la deuda, deuda/EBITDA y deuda/caja libre se miden sin arrendamientos; el pasivo por arrendamientos se muestra aparte, como dato.

Cifras de la etapa 1 tal como las guardó la hoja, a su fecha de análisis; sin las decisiones posteriores (P-O1, P-O2, F1-A/F1-B, D-US1/2, D-WM) ni verificación contra la fuente oficial.

| Campo | Valor |
|---|---|
| Fecha de la hoja | 2026-11-08 |
| Tarea | cribado-44512238939-sweco |
| SHA del código | 833cd50a9bba34006519119c72a29c70a1656fb7 |
| Huella del paquete (package_sha256) | 163311d23e1349a62058a5d772656f456e3b34255d10c4f533cac977d47e7f8a |
| Huella del envío (bundle_sha256) | 78d5b7c022cfd74b9591e7c95ab2f1a7a9630271a37a9f4d8aed1499842b64ae |
| Huella del encargo | 32b5c7f313e61a61fb0f5e68a75b3c44004eb902e97b98720fb98fa8d383e6cf |
| Huella de la Release | 4d30f7352948fe7e7fe3b133386eabedbddcc71d997e972a1c6db7964d58b0a9 |
| Huella del libro | 2f2010650ff364021e185cb6195fd6c4d41b055292c3ae94ede6fa4624cb10ca |
| Modelo pedido / devuelto | claude-opus-5-5 / claude-opus-5-5 |
| Esfuerzo | high |
| Gramática del servidor | True |
| Mensajes enviados | 1 |
| Cota de entrada antes de llamar | 150494 tokens |
| Reserva estimada antes de llamar | USD 1.257336 |
| Uso de tokens | entrada 66443, salida 4165 |
| Coste | CONOCIDO_ESTIMADO; estimado USD 0.349072; cota 0.349072 |

| id | ruta | sha256 | bytes |
|---|---|---|---|
| respuesta | EMPRESAS_LOTES_COMPLETOS/Sweco/Sweco_respuesta.md | 8fb465386ef03df4e2dd6636900cc2b271c079a4834e17794ef3b913deb9ebdc | 46995 |
| hoja_analisis | EMPRESAS_LOTES_COMPLETOS/Sweco/Sweco_evaluada.xlsx#Análisis | ba899e8bc00b36c44a876113cf070279d05fdecd577062d9a4a64937934f07c8 | 24899 |
| hoja_control_maestro | EMPRESAS_LOTES_COMPLETOS/Sweco/Sweco_evaluada.xlsx#Control maestro | 8b99905fb8e24995184325e10fd9b9857319628ddccc96e6faaa6a2bf1499e29 | 57886 |

## Salida del modelo (datos, sin acciones ejecutables)

Veredicto `vigilar` · DCF de la plantilla aplica: `si`

| Filtro | Resultado |
|---|---|
| calidad | pasa |
| caja | pasa |
| balance | pasa |
| precio | no_pasa |
| encaje | no_aplica |

### Pasivo por arrendamientos (dato aparte)

    Control maestro!M51 = 3600 (pasivos por arrendamiento a 30-09-2026; Análisis!C54 = 7394 los incluye junto a la deuda financiera de 3.794)


### Tipo de negocio y motor

    Consultoría europea de ingeniería y arquitectura que vende horas por proyecto, con poco capital fijo, demanda ligada al ciclo macro con retraso y crecimiento apoyado en adquisiciones pequeñas.
    El DCF de caja libre de la plantilla con flujo normalizado a tres años por el circulante, contrastado con el P/FCF histórico, es adecuado para una consultora de horas facturables, ligera en capital y de demanda ligada al ciclo con retraso.

### calidad

    Es un negocio entendible y de calidad razonable: ROCE del 17,1 % antes de impuestos (12,6 % después y 39 % sin fondo de comercio), margen EBITA en expansión del 8,1 % al 10,6 % y baja concentración de clientes. Discrepo de la bandera de foso de la hoja (C18) en el sentido de que no rebaja la calidad, aunque la ventaja duradera, el M&A no auditable y la sucesión de la CEO quedan como dudas para el estudio.
    Dato clave: Análisis!C24 = 0.171

### caja

    La caja libre base es positiva, de 2.152,3 tras restar el capex, el principal de arrendamientos de 896 y la SBC. La conversión CFO/beneficio es de 1,68x, o 1,22x restando arrendamientos (Control maestro!M31), y el capex de mantenimiento es bajo (394). Hay volatilidad anual por el circulante, que se resuelve con la media de tres años.
    Dato clave: Análisis!C52 = 2152.3

### balance

    La hoja usa una deuda neta/EBITDA de 1,36x (Análisis!C33) que incluye 3.600 de arrendamientos, así que no sirve tal cual; sin ellos queda una deuda financiera de 3.794 menos 634 de caja (Análisis!C53), es decir, 3.160 de deuda neta frente a un EBITDA pre-NIIF 16 de 3.852 (Control maestro!N42): ≈0,82x, holgado para un negocio de demanda poco cíclica. La caja a corto es baja (0,36x la deuda a corto), pero hay 4.246 de líneas no dispuestas.
    Dato clave: Control maestro!N51 = 3794

### precio

    La cotización de 142,7 queda muy por encima del precio de Sí (≈70, el escenario malo de 69,9) y del valor ponderado de 109,7, con un margen de -30 %. Aunque con r al 7 % el ponderado sube a 156,9 (Análisis!C90), el escenario malo y los 3/4 del ponderado seguirían muy por debajo del precio, y el DCF inverso exige un 8,7 % de crecimiento anual (Análisis!C86).
    Dato clave: Análisis!B78 = 69.9220452410413

### encaje

    El paquete no trae la cartera de la persona responsable, y la hoja solo aporta datos de la empresa, como una capitalización de 51.549 (Análisis!C41), sin nada concreto sobre el encaje.
    Dato clave: no consta (el paquete no trae la cartera)

### Qué lo cambiaría

    - Una cotización de SWEC B por debajo de ≈70-82 SEK (escenario malo 69,9; 3/4 del ponderado ≈82) la llevaría a estudiar a fondo.
    - Un deterioro del fondo de comercio del Reino Unido o de Bélgica, o dos años seguidos de crecimiento orgánico negativo, la llevarían a descartar.
    - Que la deuda neta sin arrendamientos supere ≈2x el EBITDA pre-NIIF 16 por una adquisición grande cambiaría el filtro de balance.

### Qué falta

    - Niveles numéricos de los covenants y vencimiento confirmado de la RCF de EUR 400 m (dic-2027 según AR24, no confirmado en AR25).
    - Retorno por adquisición y cartera de pedidos en SEK, imprescindibles para juzgar el foso y el crecimiento comprado.
    - Duda de fuente: Control maestro!M43 cita una decisión del inversor del 15-nov-2026, posterior a la fecha de hoja (2026-11-08).

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

