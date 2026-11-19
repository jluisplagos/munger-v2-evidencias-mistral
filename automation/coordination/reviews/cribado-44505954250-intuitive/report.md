# Cribado · Intuitive

Estado de la ejecución: `AUDITORIA_DOCUMENTAL_PENDIENTE_ACEPTACION`

Cribado pendiente de revisión humana. No es una recomendación de compra, ni aceptación, ni aptitud para dinero real. Tasa 9 % provisional.

C-ARR (decisión de la persona responsable): los arrendamientos se cuentan una sola vez, en el flujo. El alquiler se resta de la caja libre; la deuda, deuda/EBITDA y deuda/caja libre se miden sin arrendamientos; el pasivo por arrendamientos se muestra aparte, como dato.

Cifras de la etapa 1 tal como las guardó la hoja, a su fecha de análisis; sin las decisiones posteriores (P-O1, P-O2, F1-A/F1-B, D-US1/2, D-WM) ni verificación contra la fuente oficial.

| Campo | Valor |
|---|---|
| Fecha de la hoja | 09/10/2026 |
| Tarea | cribado-44505954250-intuitive |
| SHA del código | 833cd50a9bba34006519119c72a29c70a1656fb7 |
| Huella del paquete (package_sha256) | fa955da853e03b99a8158cbfaee46615ea7920dc1cf3972af842fb1a48addd64 |
| Huella del envío (bundle_sha256) | 034ea70cda39091794d39d233db579d839ac93254038b2c7e242d4a13177791d |
| Huella del encargo | 32b5c7f313e61a61fb0f5e68a75b3c44004eb902e97b98720fb98fa8d383e6cf |
| Huella de la Release | 4d30f7352948fe7e7fe3b133386eabedbddcc71d997e972a1c6db7964d58b0a9 |
| Huella del libro | a2caed4a56566b141254853852c89833f5f2acff770b19b6f8b12dbc139ba3dc |
| Modelo pedido / devuelto | claude-opus-5-5 / claude-opus-5-5 |
| Esfuerzo | high |
| Gramática del servidor | True |
| Mensajes enviados | 1 |
| Cota de entrada antes de llamar | 145296 tokens |
| Reserva estimada antes de llamar | USD 1.236544 |
| Uso de tokens | entrada 65868, salida 3006 |
| Coste | CONOCIDO_ESTIMADO; estimado USD 0.323592; cota 0.323592 |

| id | ruta | sha256 | bytes |
|---|---|---|---|
| respuesta | EMPRESAS_LOTES_COMPLETOS/Intuitive/Intuitive_respuesta.md | a1fbbe595f3821078e5681518b8ad83b8d0489225d1af99c79136a99b3ec6749 | 37959 |
| cambios_v2 | EMPRESAS_LOTES_COMPLETOS/Intuitive/Intuitive_cambios_v2.md | db570bcdec98da7879f89860fda2cf2300c06c0c044213cf3494a9448e7f5d03 | 3370 |
| hoja_analisis | EMPRESAS_LOTES_COMPLETOS/Intuitive/Intuitive_evaluada.xlsx#Análisis | 7522b68b30b73b1fa33dbd10568463d0921217eb473ee0871ca5b510b6e952e0 | 24356 |
| hoja_control_maestro | EMPRESAS_LOTES_COMPLETOS/Intuitive/Intuitive_evaluada.xlsx#Control maestro | 746bb2c7c83b74473edc46b0377b9ed2432117f79a5c918a6fec2dc1c4d441cb | 58516 |

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

    170,9 mm USD de pasivo por arrendamiento operativo a dic-25, en el texto de Control maestro!N51 (también en Control maestro!N36); no consta la cifra a jun-26.


### Tipo de negocio y motor

    Dispositivos médicos: plataforma de cirugía robótica con base instalada y venta recurrente de instrumentos, servicio y arrendamientos (modelo de cuchilla y maquinilla).
    El DCF de caja libre de la plantilla, porque es un negocio estable, sin deuda y con ingresos recurrentes; conviene contrastar la base de FCF (FY2025 frente a la media de 3 años y el LTM).

### calidad

    Pasa: el ROIC es del 22,1 %, el 84 % de los ingresos es recurrente sobre 11.106 sistemas y el margen bruto se mantiene entre el 65,6 % y el 70,2 %; pesan la competencia, el litigio antimonopolio y un cobro por procedimiento plano, y discrepo del «DESCARTAR · demasiado difícil» de A6, que viene del precio (C13 = No) y no de falta de entendimiento.
    Dato clave: Análisis!C24 = 0.221

### caja

    Pasa con matiz: el FCF tras SBC es de 1.702,5 M (C52), la conversión CFO/beneficio es de 1,07 (C26) y el FCF fue positivo todos los años, aunque la base FY2025 sale favorecida por un capex bajo (539,8 M frente a la guía de 650-800 M), la media de 3 años tras SBC rondaría 829 M y la SBC pesa el 32 % (C59).
    Dato clave: Análisis!C52 = 1702.5

### balance

    Pasa: la deuda financiera sin arrendamientos es 0 y la caja es de 2.760,4 M (C53), con deuda neta/EBITDA de -0,65x (C33); ese cociente ya excluye arrendamientos y usa un EBITDA US GAAP que resta el alquiler operativo, y no hay vencimientos financieros.
    Dato clave: Análisis!C54 = 0

### precio

    No pasa: la cotización de 415,41 $ (C37) está muy por encima del precio de Sí de unos 72 $ (escenario malo) y del ponderado de 129,0 $ (C83); incluso a r del 7 % el ponderado no pasa de 213,8 $ (C90) y el precio exige un crecimiento del 25,4 % anual (C86).
    Dato clave: Análisis!B78 = 71.9694758880409

### encaje

    No aplica: el paquete no trae la cartera de la persona responsable y la hoja solo da datos de la empresa (capitalización de 146.755,2 M), sin nada concreto sobre encaje.
    Dato clave: Análisis!C41 = 146755.2

### Qué lo cambiaría

    - Una cotización cerca o por debajo del precio de Sí de la hoja (unos 72 $; ¾ del ponderado, unos 97 $).
    - Un FCF tras SBC de 2026-2027 claramente por encima de 1.702,5 M con capex normalizado, que acerque el valor a la cotización.
    - Una sentencia antimonopolio que abra el mercado de instrumentos, o una pérdida de cuota documentada en EE. UU.: rebajaría la calidad y llevaría a descartar.

### Qué falta

    - Cuotas de mercado frente a los competidores y cobro oficial por procedimiento (da Vinci frente a Ion): no constan en el paquete.
    - Participación de los insiders (Análisis!C96 vacía: la tabla de la DEF 14A 2026 no se pudo leer) y remuneración del nuevo CEO.
    - Clasificación de los intereses cobrados en el flujo de caja, y pasivo por arrendamientos actualizado a jun-26.

### Comprobaciones mecánicas y normalizaciones

    {
      "comprobaciones": {
        "avisos": [],
        "nota": "Comprobaciones mecánicas informativas: no acreditan la calidad económica."
      },
      "normalizaciones": []
    }

