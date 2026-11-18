# Cribado · ABB

Estado de la ejecución: `AUDITORIA_DOCUMENTAL_PENDIENTE_ACEPTACION`

Cribado pendiente de revisión humana. No es una recomendación de compra, ni aceptación, ni aptitud para dinero real. Tasa 9 % provisional.

C-ARR (decisión de la persona responsable): los arrendamientos se cuentan una sola vez, en el flujo. El alquiler se resta de la caja libre; la deuda, deuda/EBITDA y deuda/caja libre se miden sin arrendamientos; el pasivo por arrendamientos se muestra aparte, como dato.

Cifras de la etapa 1 tal como las guardó la hoja, a su fecha de análisis; sin las decisiones posteriores (P-O1, P-O2, F1-A/F1-B, D-US1/2, D-WM) ni verificación contra la fuente oficial.

| Campo | Valor |
|---|---|
| Fecha de la hoja | 2026-10-08 |
| Tarea | cribado-44413758195-abb |
| SHA del código | 833cd50a9bba34006519119c72a29c70a1656fb7 |
| Huella del paquete (package_sha256) | 5bcc61efc9e68f4080d6fed497f7c4e4e5f1f44d1c3d4023d585755267d0b306 |
| Huella del envío (bundle_sha256) | 7242dc3c7e9f477fa187093f83a20c1978abc1dc7f708955c5926fe12484a25c |
| Huella del encargo | 32b5c7f313e61a61fb0f5e68a75b3c44004eb902e97b98720fb98fa8d383e6cf |
| Huella de la Release | 4d30f7352948fe7e7fe3b133386eabedbddcc71d997e972a1c6db7964d58b0a9 |
| Huella del libro | 748169b6de73c197108826acd42901a5edb9f2545fb9de5521cef521c176a8d1 |
| Modelo pedido / devuelto | claude-opus-5-5 / claude-opus-5-5 |
| Esfuerzo | high |
| Gramática del servidor | True |
| Mensajes enviados | 1 |
| Cota de entrada antes de llamar | 122175 tokens |
| Reserva estimada antes de llamar | USD 1.14406 |
| Uso de tokens | entrada 55599, salida 4760 |
| Coste | CONOCIDO_ESTIMADO; estimado USD 0.317596; cota 0.317596 |

| id | ruta | sha256 | bytes |
|---|---|---|---|
| respuesta | EMPRESAS_LOTES_COMPLETOS/ABB/ABB_respuesta.md | cac35cd68a3bedd5005bb417961bc7049274e519ba86f2d690f3c522cd5dba56 | 28967 |
| hoja_analisis | EMPRESAS_LOTES_COMPLETOS/ABB/ABB_evaluada.xlsx#Análisis | 47948fbbf06db01eb77dece4e493bfbfce94ab22fb2865f9e1ae4e6ae6c42a30 | 23133 |
| hoja_control_maestro | EMPRESAS_LOTES_COMPLETOS/ABB/ABB_evaluada.xlsx#Control maestro | 216e98f49cc4a184e316ef1ef3d1da53c3dc3c28f1342693557c5a50d2d8e1be | 49409 |

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

    Arrendamientos operativos 805 (Control maestro!M51, a 30-jun-2026) más arrendamientos financieros 175 (Control maestro!M46, a dic-2025): ≈980 mm USD, fuera del cociente de deuda.


### Tipo de negocio y motor

    Industrial de equipos eléctricos y automatización (Electrification 52 %, Motion 25 %, Automation 24 %), con una parte de ciclo corto y un viento de cola de electrificación.
    El DCF de caja libre de la plantilla, partiendo de una caja libre normalizada a margen de ciclo medio (no el pico del 19 %), porque es un industrial con parte de ciclo corto.

### calidad

    El ROCE del 25,3 % en 2025, por encima del 15 % desde 2022 (16,5 %, 21,1 % y 23,8 %), con un margen bruto del 32 % al 41 % y posiciones de número 1 o 2, indica calidad, aunque es reciente (10,3 % en 2020) y falta ver un ciclo completo; el negocio se entiende, así que discrepo del «DESCARTAR · demasiado difícil» de Análisis!A6, que procede de C13 = No, un fallo de precio y no de comprensión.
    Dato clave: Análisis!C24 = 0.253

### caja

    La caja libre base de 3.709 (media 2023–25, con la SBC restada) y la LTM de 4.953 confirman el beneficio, con una conversión de 0,96 y un capex de 857 sobre un CFO de 4.664, aunque la serie tuvo baches con causa identificada (999 en 2020 y 525 en 2022).
    Dato clave: Análisis!C52 = 3709

### balance

    Sin arrendamientos, la deuda es ≈8.002 (8.177 menos 175 de arrendamientos financieros) y la deuda neta ≈2.145, unas 0,29x del EBITDA LTM de 7.327, que en US GAAP ya resta el alquiler operativo (0,32x en la hoja); los vencimientos de 2026–2027 son pequeños (CHF 325, EUR 500, CHF 425) frente a una caja de 3.867, y la proforma con Rotork sería 0,44x, holgado incluso para un negocio con un ciclo corto.
    Dato clave: Análisis!C54 = 8177 (≈8002 sin los 175 de arrendamientos financieros, Control maestro!M46; deuda neta ≈2145 / EBITDA LTM 7327 ≈ 0,29x)

### precio

    La cotización de 94,52 USD triplica el precio de Sí de 28,64 (escenario malo, por debajo de 0,75 × 46,78 = 35,08) y supera incluso el escenario bueno (69,71) y el ponderado con r al 7 % (69,83); el precio exige un crecimiento del FCF del 16,8 % anual durante diez años.
    Dato clave: Análisis!C37 = 94.52 (precio de Sí = Análisis!C78 = 28.6374303326534)

### encaje

    El paquete no trae la cartera de la persona responsable; solo cabe anotar que cotiza en CHF (78,80) con flujos en USD al tipo de 0,83372, una exposición de divisa que la cartera tendría que valorar.
    Dato clave: Control maestro!J5 = Precio CHF→USD a 0,83372 CHF/USD

### Qué lo cambiaría

    - Una cotización en el entorno de 28,6 USD (≈24 CHF) o por debajo, con el negocio intacto, pasaría el filtro de precio y llevaría a estudiar_a_fondo.
    - Que en la próxima caída del ciclo corto el margen de Operational EBITA baje del 15 % o el de Electrification del 18 % haría que calidad no pasara.
    - Que Rotork se pague con deuda y la deuda neta sin arrendamientos supere unas 2x el EBITDA haría que balance no pasara.

### Qué falta

    - Margen y ROCE de un ciclo completo (antes de 2017) y una serie reexpresada sin cambios de perímetro, para saber si el margen del 19 % es estructural.
    - Precio, financiación y retorno esperado de Rotork (~5.500 mm), y el pasivo por arrendamientos financieros a 30-jun-2026 (solo consta 175 a dic-2025).
    - La hoja recoge decisiones fechadas el 18 y el 25-oct-2026, posteriores a la fecha de corte (08-oct-2026), y el paquete no trae el texto de cambios_v2.

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

