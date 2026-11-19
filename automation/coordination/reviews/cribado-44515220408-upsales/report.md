# Cribado · Upsales

Estado de la ejecución: `AUDITORIA_DOCUMENTAL_PENDIENTE_ACEPTACION`

Cribado pendiente de revisión humana. No es una recomendación de compra, ni aceptación, ni aptitud para dinero real. Tasa 9 % provisional.

C-ARR (decisión de la persona responsable): los arrendamientos se cuentan una sola vez, en el flujo. El alquiler se resta de la caja libre; la deuda, deuda/EBITDA y deuda/caja libre se miden sin arrendamientos; el pasivo por arrendamientos se muestra aparte, como dato.

Cifras de la etapa 1 tal como las guardó la hoja, a su fecha de análisis; sin las decisiones posteriores (P-O1, P-O2, F1-A/F1-B, D-US1/2, D-WM) ni verificación contra la fuente oficial.

| Campo | Valor |
|---|---|
| Fecha de la hoja | 2026-10-26 |
| Tarea | cribado-44515220408-upsales |
| SHA del código | 833cd50a9bba34006519119c72a29c70a1656fb7 |
| Huella del paquete (package_sha256) | ac65ad9ae978158d0abe8f8443ac9e1976339692b670b81766f50bc4bec703e7 |
| Huella del envío (bundle_sha256) | 542733744a629bf5f0b3be3d541a0f8e93c08217373cbd604c8bfb80d641e439 |
| Huella del encargo | 32b5c7f313e61a61fb0f5e68a75b3c44004eb902e97b98720fb98fa8d383e6cf |
| Huella de la Release | 4d30f7352948fe7e7fe3b133386eabedbddcc71d997e972a1c6db7964d58b0a9 |
| Huella del libro | eb90849bbce2c8b6504a3c5ed889f6c043ca8f9f1d5403922ae81e26ecc9df06 |
| Modelo pedido / devuelto | claude-opus-5-5 / claude-opus-5-5 |
| Esfuerzo | high |
| Gramática del servidor | True |
| Mensajes enviados | 1 |
| Cota de entrada antes de llamar | 155390 tokens |
| Reserva estimada antes de llamar | USD 1.27692 |
| Uso de tokens | entrada 70313, salida 3618 |
| Coste | CONOCIDO_ESTIMADO; estimado USD 0.353612; cota 0.353612 |

| id | ruta | sha256 | bytes |
|---|---|---|---|
| respuesta | EMPRESAS_LOTES_COMPLETOS/Upsales/Upsales_respuesta.md | 5fb901ed7b213958a165372c01a9e5c10381ae6af119be06fdfc0c55da210561 | 35972 |
| hoja_analisis | EMPRESAS_LOTES_COMPLETOS/Upsales/Upsales_evaluada.xlsx#Análisis | ae34a5c6cb40da3fe618b18b0330344efa4e3a9ebdc598ec64425fe378a64034 | 23023 |
| hoja_control_maestro | EMPRESAS_LOTES_COMPLETOS/Upsales/Upsales_evaluada.xlsx#Control maestro | dae659c0914e3ec2af37b0cc3bdf897b7a7e8c3418f2057c7cbcb8bdc5a0c795 | 75649 |

## Salida del modelo (datos, sin acciones ejecutables)

Veredicto `vigilar` · DCF de la plantilla aplica: `si`

| Filtro | Resultado |
|---|---|
| calidad | dudoso |
| caja | pasa |
| balance | pasa |
| precio | no_pasa |
| encaje | no_aplica |

### Pasivo por arrendamientos (dato aparte)

    Análisis!C54 = 1.332 (Control maestro!C51: arrendamiento financiero a largo plazo, 1.332 TSEK); como contexto, los compromisos futuros de alquiler operativo suman 22.249 TSEK (Control maestro!N36) y ya van restados en el EBITDA y en la caja libre.


### Tipo de negocio y motor

    Software SaaS de CRM por suscripción anual prepagada para pymes B2B, con el 95,5 % de las ventas en Suecia; está en situación especial tras la escisión de Aira y el cambio de CEO.
    El DCF de caja libre de la plantilla sirve para un SaaS sin deuda, con circulante negativo y flujo estable, pero conviene recalcularlo sobre una base continuada sin Aira (unos 45 mm estimados) cuando haya trimestres limpios.

### calidad

    El modelo se entiende (SaaS prepagado, 95,0 % recurrente, capital invertido negativo y margen EBIT del 18,6 % en 2025), pero la durabilidad es dudosa: el ARR está casi plano (+0,4 % en el tercer trimestre de 2026), los clientes han bajado de unos 1.900 a algo más de 1.000 y el foso no se ve en las cifras (Análisis!C18 = No); la hoja lo lleva a demasiado difícil, pero esto es una duda de calidad, no un negocio que no se entienda.
    Dato clave: Análisis!C24 = N/A (capital invertido negativo, −18.073 TSEK según Control maestro!N29)

### caja

    La caja libre ya neta del principal de arrendamiento es positiva en todos los periodos (FCF por acción de 1,73 a 0,91 SEK entre 2021 y 2025 y 1,942 en el LTM) y la caja operativa equivale a 1,71 veces el beneficio, gracias al prepago anual, aunque el salto del LTM a 32,701 mm se debe al perímetro sin Aira y no a las ventas.
    Dato clave: Análisis!C52 = 32.701

### balance

    Sin arrendamientos la deuda financiera es 0 frente a una caja de 36,371 mm y un EBITDA UDM de 47,929 mm ya neto de alquiler (K3), lo que da caja neta de unos −0,76x (la hoja da −0,73x en Análisis!C33 porque resta los 1,332 mm de arrendamiento; mismo veredicto).
    Dato clave: Análisis!C53 = 36.371 (deuda financiera sin arrendamientos = 0, porque Análisis!C54 = 1.332 es todo arrendamiento financiero)

### precio

    La cotización de 28,8 SEK está claramente por encima del precio de Sí de unos 19,8 SEK (el menor entre el escenario malo, 19,79, y ¾ del ponderado de 31,61, que son 23,70), el margen sobre el ponderado es solo del 8,9 % y con r + 2 puntos el valor baja a 24,58 SEK, por debajo del precio.
    Dato clave: Análisis!B78 = 19.7926195839424

### encaje

    El paquete no trae la cartera; solo consta una capitalización de 484,945 mm y una liquidez de unos 2,2 MSEK al día (Control maestro!N38), un dato que no elimina la empresa en el cribado.
    Dato clave: Análisis!C41 = 484.945

### Qué lo cambiaría

    - Una cotización en torno a 19,8 SEK o por debajo (escenario malo de Análisis!B78), que pasaría el filtro de precio y llevaría a estudiar a fondo.
    - Un ARR que crezca ≥ +6 % interanual dos trimestres seguidos, con churn o NRR publicados y un número de clientes estable, que resolvería la duda de calidad.
    - Un ARR negativo dos trimestres seguidos o menos de 900 clientes, que haría no pasar la calidad y llevaría a descartar.

### Qué falta

    - Churn y NRR por cohortes desde 2021 y número de clientes por tamaño: el último dato es una renovación del 95 % en 2021.
    - Capex de mantenimiento sin Aira medido en un ejercicio completo: hoy es una estimación de 5.000 a 8.500 TSEK (Control maestro!N44), y de él depende la base continuada de 44.992 TSEK.
    - Participación de los insiders a una fecha común posterior al 31-12-2022 (Análisis!C96 está vacía por dato no verificable).

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

