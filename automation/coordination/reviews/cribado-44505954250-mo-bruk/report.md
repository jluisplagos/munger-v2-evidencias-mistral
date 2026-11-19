# Cribado · Mo-BRUK

Estado de la ejecución: `AUDITORIA_DOCUMENTAL_PENDIENTE_ACEPTACION`

Cribado pendiente de revisión humana. No es una recomendación de compra, ni aceptación, ni aptitud para dinero real. Tasa 9 % provisional.

C-ARR (decisión de la persona responsable): los arrendamientos se cuentan una sola vez, en el flujo. El alquiler se resta de la caja libre; la deuda, deuda/EBITDA y deuda/caja libre se miden sin arrendamientos; el pasivo por arrendamientos se muestra aparte, como dato.

Cifras de la etapa 1 tal como las guardó la hoja, a su fecha de análisis; sin las decisiones posteriores (P-O1, P-O2, F1-A/F1-B, D-US1/2, D-WM) ni verificación contra la fuente oficial.

| Campo | Valor |
|---|---|
| Fecha de la hoja | 2026-10-09 |
| Tarea | cribado-44505954250-mo-bruk |
| SHA del código | 833cd50a9bba34006519119c72a29c70a1656fb7 |
| Huella del paquete (package_sha256) | bb182d7b18bd7eb5e4edb61b7e75cabbb1481c2e2e66cdf7bdae48e4cde7352c |
| Huella del envío (bundle_sha256) | e5a4eb0a3c2e5206b483f412b2e40ba58b755a9294467db81f096bf69cca64ce |
| Huella del encargo | 32b5c7f313e61a61fb0f5e68a75b3c44004eb902e97b98720fb98fa8d383e6cf |
| Huella de la Release | 4d30f7352948fe7e7fe3b133386eabedbddcc71d997e972a1c6db7964d58b0a9 |
| Huella del libro | f94cee315a225212e07903867939936e1f7b1b422278d23ff1076dba3cde4733 |
| Modelo pedido / devuelto | claude-opus-5-5 / claude-opus-5-5 |
| Esfuerzo | high |
| Gramática del servidor | True |
| Mensajes enviados | 1 |
| Cota de entrada antes de llamar | 149847 tokens |
| Reserva estimada antes de llamar | USD 1.254748 |
| Uso de tokens | entrada 68032, salida 4544 |
| Coste | CONOCIDO_ESTIMADO; estimado USD 0.363008; cota 0.363008 |

| id | ruta | sha256 | bytes |
|---|---|---|---|
| respuesta | EMPRESAS_LOTES_COMPLETOS/Mo-BRUK/Mo-BRUK_respuesta.md | 16f12e97931546b3453dc77fd6ef46636437c167651e0cf7fef3a1581e628625 | 39847 |
| cambios_v2 | EMPRESAS_LOTES_COMPLETOS/Mo-BRUK/Mo-BRUK_cambios_v2.md | 13af5e0c8628b1ab833643c5444bfedc0be54efce087c987f780143c227d8239 | 3539 |
| hoja_analisis | EMPRESAS_LOTES_COMPLETOS/Mo-BRUK/Mo-BRUK_evaluada.xlsx#Análisis | 8d364ffdab9a4238ae5c76d85c9a86b04a1cef81968eead9509fd270ad575be0 | 23789 |
| hoja_control_maestro | EMPRESAS_LOTES_COMPLETOS/Mo-BRUK/Mo-BRUK_evaluada.xlsx#Control maestro | cb87ccad29733acafcf183a8690202490391c4af1357fc28996fad281ae06b85 | 61595 |

## Salida del modelo (datos, sin acciones ejecutables)

Veredicto `vigilar` · DCF de la plantilla aplica: `dudoso`

| Filtro | Resultado |
|---|---|
| calidad | dudoso |
| caja | dudoso |
| balance | pasa |
| precio | no_pasa |
| encaje | no_aplica |

### Pasivo por arrendamientos (dato aparte)

    Control maestro!M51 = 76.65 (arrendamientos NIIF 16 a 30-06-2026: LP 62,13 + CP 14,53); dato aparte, fuera del cociente de deuda.


### Tipo de negocio y motor

    Gestión de residuos industriales y peligrosos en Polonia (incineración, solidificación, combustibles alternativos y aguas oleosas) basada en permisos integrados, con beneficio semicíclico ligado a licitaciones públicas y a precios regulados, en plena fase de inversión financiada con deuda.
    Caja libre normalizada de ciclo medio, con capex de mantenimiento separado del de crecimiento y coste financiero actual (intereses y arrendamientos al ritmo LTM), en lugar de la media 2021–2025 de la plantilla.

### calidad

    El negocio se entiende con el paquete, con demanda regulada y duradera y un ROCE LTM antes de impuestos del 19,6 % (ROIC después de impuestos del 15,9 %); pero el ROCE incremental 2022→LTM es de ≈6 %, por debajo del 9 %, el margen EBITDA cae del 57,8 % al 41,1 % y cada planta depende de un permiso revocable, así que discrepo del «demasiado difícil» de la etapa 1 y lo dejo en duda.
    Dato clave: Análisis!C24 = 0.196

### caja

    La conversión del beneficio en caja es sana (CFO/beneficio de 1,24 en Análisis!C26), pero la caja libre base es de solo 35,91 mm y el CFO menos capex fue de 134,9, 80,7, 5,3, −26,5 y 24,6 mm entre 2021 y 2025: el programa de crecimiento de unos 250 mm, sin capex de mantenimiento separado, impide saber si la caja recurrente es estable.
    Dato clave: Análisis!C52 = 35.91

### balance

    Sin arrendamientos, la deuda neta es de 63,44 mm frente a un EBITDA LTM de 110,25 mm (0,58x según la hoja, unas 0,65x si se resta un alquiler de unos 12 mm, y sobre 1,4x incluso sumando el dividendo de 53,5 pagado con deuda nueva); es holgado para un negocio algo cíclico, aunque la caja solo cubre 0,59x la deuda a corto, y el 1,27x de Análisis!C33 no sirve tal cual porque incluye arrendamientos.
    Dato clave: Control maestro!M51 = 88.10 (préstamos sin arrendamientos; deuda neta sin arrendamientos 88,10 − 24,66 de caja no restringida = 63,44)

### precio

    A 409 PLN la cotización supera el valor ponderado de 211,3, el escenario bueno de 330,5 y el valor con r − 2 puntos (305,75), y el precio da por hecho un crecimiento del 15,5 % anual (Análisis!C86); aunque el DCF de la plantilla es dudoso por la base deprimida, incluso la caja libre LTM normalizada de 66,83 mm solo rinde un 4,65 %.
    Dato clave: Análisis!C83 = 211.298465284947

### encaje

    El paquete no trae la cartera de la persona responsable y la hoja no dice nada concreto de encaje más allá de una cotización de 409 PLN, así que este filtro no elimina.
    Dato clave: Análisis!C37 = 409

### Qué lo cambiaría

    - Una cotización por debajo del valor ponderado de la hoja (unos 211 PLN) o del precio de Sí de unos 124 PLN, que pasaría a estudiar_a_fondo si calidad y caja se aclaran.
    - Una caja libre después de intereses y arrendamientos por encima de 60 mm en 2026 y 2027, con un ROCE incremental superior al 9 %, que despejaría las dudas de calidad y caja.
    - La revocación o limitación del permiso de Karsy o de EL-KAJO, o una deuda neta sin arrendamientos por encima de 2,5x el EBITDA, que llevaría a descartar.

### Qué falta

    - Separación entre capex de mantenimiento y de crecimiento, y caja libre recurrente después de intereses y arrendamientos al ritmo actual.
    - Importe, condiciones y vencimientos del crédito del 25-09-2026 con el que se pagó el dividendo de 53,5 mm (no leído por la fase 1) y deuda pro forma sin arrendamientos.
    - Vencimiento y estado de los permisos clave (Karsy, EL-KAJO, Niecew) y datos de competidores y capacidad del sector, que el paquete no trae.

### Comprobaciones mecánicas y normalizaciones

    {
      "comprobaciones": {
        "avisos": [],
        "nota": "Comprobaciones mecánicas informativas: no acreditan la calidad económica."
      },
      "normalizaciones": []
    }

