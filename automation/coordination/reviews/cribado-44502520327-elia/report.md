# Cribado · Elia

Estado de la ejecución: `AUDITORIA_DOCUMENTAL_PENDIENTE_ACEPTACION`

Cribado pendiente de revisión humana. No es una recomendación de compra, ni aceptación, ni aptitud para dinero real. Tasa 9 % provisional.

C-ARR (decisión de la persona responsable): los arrendamientos se cuentan una sola vez, en el flujo. El alquiler se resta de la caja libre; la deuda, deuda/EBITDA y deuda/caja libre se miden sin arrendamientos; el pasivo por arrendamientos se muestra aparte, como dato.

Cifras de la etapa 1 tal como las guardó la hoja, a su fecha de análisis; sin las decisiones posteriores (P-O1, P-O2, F1-A/F1-B, D-US1/2, D-WM) ni verificación contra la fuente oficial.

| Campo | Valor |
|---|---|
| Fecha de la hoja | 2026-10-17 |
| Tarea | cribado-44502520327-elia |
| SHA del código | 833cd50a9bba34006519119c72a29c70a1656fb7 |
| Huella del paquete (package_sha256) | 958643509021413842c91ebc483045fd9898fb39441d16a94b5da84ff5bd4744 |
| Huella del envío (bundle_sha256) | c444aa035c023a043c1769877f25c9750bf09b1ac4519ce1ade8842fdcf641f6 |
| Huella del encargo | 32b5c7f313e61a61fb0f5e68a75b3c44004eb902e97b98720fb98fa8d383e6cf |
| Huella de la Release | 4d30f7352948fe7e7fe3b133386eabedbddcc71d997e972a1c6db7964d58b0a9 |
| Huella del libro | 70fff82aa9a9bf8139f6643bc864aedb9677a609ffc1e4e9d856e4686b7db81f |
| Modelo pedido / devuelto | claude-opus-5-5 / claude-opus-5-5 |
| Esfuerzo | high |
| Gramática del servidor | True |
| Mensajes enviados | 1 |
| Cota de entrada antes de llamar | 135769 tokens |
| Reserva estimada antes de llamar | USD 1.198436 |
| Uso de tokens | entrada 61139, salida 4624 |
| Coste | CONOCIDO_ESTIMADO; estimado USD 0.337036; cota 0.337036 |

| id | ruta | sha256 | bytes |
|---|---|---|---|
| respuesta | EMPRESAS_LOTES_COMPLETOS/Elia/Elia_respuesta.md | 4dda78d727c746f97cb5ac9d4bbe37d2bd1660b1cbd2c0ffad8a323968fde9ec | 34424 |
| hoja_analisis | EMPRESAS_LOTES_COMPLETOS/Elia/Elia_evaluada.xlsx#Análisis | 6d7f34c588a6542b14e2171f7f84448fa98235f5e0f487687dbaff77a1972a0c | 23569 |
| hoja_control_maestro | EMPRESAS_LOTES_COMPLETOS/Elia/Elia_evaluada.xlsx#Control maestro | 9987e6bd6d9349ed304160d30a48449e205bbfeaaebdae9fef3764f60b085ea4 | 56913 |

## Salida del modelo (datos, sin acciones ejecutables)

Veredicto `descartar` · DCF de la plantilla aplica: `no`

| Filtro | Resultado |
|---|---|
| calidad | dudoso |
| caja | no_pasa |
| balance | dudoso |
| precio | dudoso |
| encaje | no_aplica |

### Pasivo por arrendamientos (dato aparte)

    85,3 mm (Control maestro!M51, incluido en la deuda total de Análisis!C54 = 17704.3); no entra en el cociente de deuda.


### Tipo de negocio y motor

    Operador regulado de redes de transporte eléctrico (TSO) en Bélgica y en la zona de 50Hertz en Alemania, con retorno fijado por el regulador sobre la RAB y en plena fase de inversión de crecimiento.
    Valor sobre la base de activos regulados (RAB): el capital propio regulado por el ROE permitido frente al 9 %, es decir, precio/valor contable o EV/RAB frente al retorno regulado, incluyendo la dilución de las ampliaciones necesarias para el plan de inversión.

### calidad

    El negocio se entiende: es un monopolio regulado con demanda duradera y ningún cliente llega al 10 % de los ingresos. Pero la ventaja no se ve en los retornos: ROCE del 5,3 %, ROE ajustado del 6,9–10 % fijado por el regulador y asignación de capital marcada como Dudosa (C98). Los ✓ PASA de foso y viento de cola de la hoja no bastan para un pasa limpio.
    Dato clave: Análisis!C24 = 0.053

### caja

    La caja libre base es −2.692,1 (LTM −3.756,7 en Análisis!C40) y fue negativa en 6 de 7 años entre 2019 y 2025. El hueco se cubre con deuda y con ampliaciones (2.200 de capital en 2025), así que el beneficio no llega al accionista como caja. El 2,96x de Análisis!C26 («pasa» en la hoja) refleja la amortización, no la caja libre, y discrepo de él como señal de calidad.
    Dato clave: Análisis!C52 = -2692.1

### balance

    La deuda neta sin arrendamientos (≈14.170,5 = 14.255,8 − 85,3) sobre un EBITDA que ya resta el alquiler da ≈7,35x según la sensibilidad de la hoja; la cifra de 7,32x de Análisis!C33 incluye arrendamientos y no sirve tal cual. Es un nivel alto incluso para una red regulada (deuda ≈60 % de la RAB por diseño). Con caja libre negativa no se puede calcular la deuda/caja libre, y la deuda neta se duplicó en 2021-25. A favor, la caja cubre 4,4x la deuda a corto plazo, pero solo 1,15x los vencimientos a 24 meses (≈2.686).
    Dato clave: Análisis!C54 = 17704.3 (incluye 85,3 de arrendamientos) − Análisis!C53 = 3448.5 → deuda neta sin arrendamientos ≈ 14170.5

### precio

    El DCF de la plantilla (valor ponderado −496,8 €) no sirve con caja libre negativa y no hay precio de Sí. Con el motor adecuado, a 123,7 € se paga ≈1,7x el patrimonio por acción (≈72 €) por un ROE del ≈7,3 % frente al 9 %, lo que apunta a caro. Sin embargo, la propia respuesta admite que con una tasa en torno al 7 % el resultado cambiaría.
    Dato clave: Análisis!C37 = 123.7

### encaje

    El paquete no trae la cartera de la persona responsable; la capitalización de 13.502,4 mm queda solo como contexto, y este filtro no elimina.
    Dato clave: Análisis!C41 = 13502.4

### Qué lo cambiaría

    - Un plan de inversión 2027-31 que muestre una meseta y una caja libre después de toda la inversión positiva y sostenida, sin nuevas ampliaciones de capital.
    - Un ROE regulado final en Alemania y Bélgica confirmado en el 9 % o más.
    - Una deuda neta sin arrendamientos sobre EBITDA (después de alquileres) que baje claramente de las ≈7,35x.

### Qué falta

    - Desglose de la inversión entre mantenimiento y crecimiento: sin él no se puede estimar la caja libre de un año sin crecimiento de la RAB.
    - ROE final de la metodología alemana (prevista para finales de 2026) y capital propio regulado por segmento, necesarios para el motor por RAB.
    - Calendario completo de vencimientos de deuda y umbrales de los covenants (la hoja dice que existen sin umbral publicado). Además, la revisión de la respuesta (25-oct-2026) y la decisión sobre C46 (20-oct-2026) son posteriores a la fecha de corte.

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

