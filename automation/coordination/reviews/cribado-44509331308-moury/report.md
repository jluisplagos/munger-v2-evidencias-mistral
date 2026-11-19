# Cribado · Moury

Estado de la ejecución: `AUDITORIA_DOCUMENTAL_PENDIENTE_ACEPTACION`

Cribado pendiente de revisión humana. No es una recomendación de compra, ni aceptación, ni aptitud para dinero real. Tasa 9 % provisional.

C-ARR (decisión de la persona responsable): los arrendamientos se cuentan una sola vez, en el flujo. El alquiler se resta de la caja libre; la deuda, deuda/EBITDA y deuda/caja libre se miden sin arrendamientos; el pasivo por arrendamientos se muestra aparte, como dato.

Cifras de la etapa 1 tal como las guardó la hoja, a su fecha de análisis; sin las decisiones posteriores (P-O1, P-O2, F1-A/F1-B, D-US1/2, D-WM) ni verificación contra la fuente oficial.

| Campo | Valor |
|---|---|
| Fecha de la hoja | 2026-10-31 |
| Tarea | cribado-44509331308-moury |
| SHA del código | 833cd50a9bba34006519119c72a29c70a1656fb7 |
| Huella del paquete (package_sha256) | 6a400e2b6961a690559649b90797c3f5113f16fd4c00ab89cee9a8d0ad3bad7f |
| Huella del envío (bundle_sha256) | 17a23aa9b4cbf19a639fbba69ea8c8ef16f371c3094c733cf9faad210a7deb29 |
| Huella del encargo | 32b5c7f313e61a61fb0f5e68a75b3c44004eb902e97b98720fb98fa8d383e6cf |
| Huella de la Release | 4d30f7352948fe7e7fe3b133386eabedbddcc71d997e972a1c6db7964d58b0a9 |
| Huella del libro | 733112d1d9daefb5381b148f134dc7b2315e6c6a6cc79f0086982a5db226f48b |
| Modelo pedido / devuelto | claude-opus-5-5 / claude-opus-5-5 |
| Esfuerzo | high |
| Gramática del servidor | True |
| Mensajes enviados | 1 |
| Cota de entrada antes de llamar | 122498 tokens |
| Reserva estimada antes de llamar | USD 1.145352 |
| Uso de tokens | entrada 54857, salida 3860 |
| Coste | CONOCIDO_ESTIMADO; estimado USD 0.296628; cota 0.296628 |

| id | ruta | sha256 | bytes |
|---|---|---|---|
| respuesta | EMPRESAS_LOTES_COMPLETOS/Moury/Moury_respuesta.md | 9cae644803d7e8fc746a798555592c51bd2e6b7dd25074dd06f725e24f7083f5 | 28782 |
| hoja_analisis | EMPRESAS_LOTES_COMPLETOS/Moury/Moury_evaluada.xlsx#Análisis | de90ec95371f4ef88d8dfeab268a502cba378d98ee91d586f5d860b42701f599 | 23089 |
| hoja_control_maestro | EMPRESAS_LOTES_COMPLETOS/Moury/Moury_evaluada.xlsx#Control maestro | f14ab0e82e81e5c385bd23a18d00157aae3ec76f20ccbe6674220f7a7a660920 | 49957 |

## Salida del modelo (datos, sin acciones ejecutables)

Veredicto `estudiar_a_fondo` · DCF de la plantilla aplica: `dudoso`

| Filtro | Resultado |
|---|---|
| calidad | dudoso |
| caja | pasa |
| balance | pasa |
| precio | dudoso |
| encaje | no_aplica |

### Pasivo por arrendamientos (dato aparte)

    Control maestro!M51 ≈ 0.27 M€ (arrendamientos NIIF 16, un único contrato: la sede de Bemat, alquilada a Immo Moury), incluido en Análisis!C54 = 1.7 y excluido aquí de la deuda


### Tipo de negocio y motor

    Constructora regional belga (edificación, renovación y técnicas especiales en Valonia), cíclica y con contratos de obra, circulante negativo y gran caja neta
    Caja libre de ciclo medio (normalizada con márgenes de un ciclo completo, no solo 2023–2025) más la caja neta realmente sobrante; el DCF de la plantilla sirve solo como contraste por escenarios.

### calidad

    El negocio se entiende (contratista general con un solo segmento y ningún cliente por encima del 10 %) y el ROCE es del 29 %, pero el margen operativo del 15 % es unas 2,5 veces el 5–6 % de 2016–2019, sin foso identificado y con márgenes estatutarios de 2025 a la baja (8,2 % y 13,2 %), así que la etapa 1 marca «Estable» en Análisis!C27 y yo no puedo confirmar que esa rentabilidad sea duradera.
    Dato clave: Análisis!C24 = 0.29

### caja

    El beneficio se convierte en caja (caja operativa/beneficio de 1,09 en 2021–2025, capex de 1,97 M€ ≈ amortización) y la caja libre reportada fue positiva cada año (9,7/8,0/42,9/19,0/35,8 M€), aunque es volátil por el circulante y el LTM es de 23,8 M€, un 24 % menos que la base de 31,37 M€.
    Dato clave: Análisis!C26 = 1.09

### balance

    Sin arrendamientos, la deuda es de 1,45 M€ frente a 109,5 M€ de caja, es decir, caja neta de unos 108 M€ y una deuda neta/EBITDA de unos −2,40x sobre un EBITDA aproximado de 45,0 M€; el −2,39x de Análisis!C33 incluye arrendamientos, pero la diferencia es irrelevante y el balance aguanta de sobra incluso a un negocio cíclico, con 37,7 M€ de garantías de obra fuera de balance a vigilar.
    Dato clave: Control maestro!N51 = 1.45 (deuda bancaria sin arrendamientos) frente a Análisis!C53 = 109.5 → caja neta ≈ 108.05 M€

### precio

    A 680 € la cotización está un 14 % por encima del precio de Sí de la etapa 1 (escenario malo, 595,54 €), aunque muy por debajo del ponderado de 1.348,67 €, que sigue por encima de 1.000 € con r ±2 puntos y descuenta un crecimiento de la caja libre del −8,3 %; como ese DCF parte de una caja libre de años de margen máximo, falta valorarla con caja de ciclo medio más caja neta para concluir.
    Dato clave: Análisis!B78 = 595.544998633503

### encaje

    El paquete no trae la cartera; solo consta una capitalización de 268,37 M€ con una liquidez muy baja (unos 52 k€ al día según Control maestro), que es contexto y no elimina.
    Dato clave: Análisis!C41 = 268.37

### Qué lo cambiaría

    - Margen operativo NIIF de 2026 por debajo del ~13 % o hacia el 8–10 %: confirmaría que era ciclo y llevaría a descartar o vigilar.
    - Una cotización por debajo de 595,54 € (escenario malo, Análisis!B78), o una caja libre de ciclo medio que justifique el precio actual.
    - Caja libre sin circulante de 2026 por debajo de ~25 M€ con la cartera actual (370 M€), o un aumento de las operaciones con sociedades del controlador.

### Qué falta

    - Explicación del salto de margen del 5–6 % (2016–2019) al 15 % (2022–2025): márgenes por tipo de obra y de cliente, competidores y cuota; sin ella no se puede fijar una caja libre de ciclo medio.
    - Cuánta de la caja de 109,5 M€ es realmente sobrante: caja de obra en sociedades simples sin desglosar, circulante negativo (proveedores 69,4 M€) y garantías de 37,7 M€; el EBITDA sin arrendamientos (45,0 M€) es solo aproximado.
    - Coherencia de fechas: Control maestro cita una decisión del 9-nov-2026 sobre el FCF base (C46/C47), posterior a la fecha de la hoja (31-oct-2026), y su auditoría deja el DCF como «Pendiente».

### Comprobaciones mecánicas y normalizaciones

    {
      "comprobaciones": {
        "avisos": [],
        "nota": "Comprobaciones mecánicas informativas: no acreditan la calidad económica."
      },
      "normalizaciones": []
    }

