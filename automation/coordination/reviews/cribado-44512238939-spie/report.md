# Cribado · Spie

Estado de la ejecución: `AUDITORIA_DOCUMENTAL_PENDIENTE_ACEPTACION`

Cribado pendiente de revisión humana. No es una recomendación de compra, ni aceptación, ni aptitud para dinero real. Tasa 9 % provisional.

C-ARR (decisión de la persona responsable): los arrendamientos se cuentan una sola vez, en el flujo. El alquiler se resta de la caja libre; la deuda, deuda/EBITDA y deuda/caja libre se miden sin arrendamientos; el pasivo por arrendamientos se muestra aparte, como dato.

Cifras de la etapa 1 tal como las guardó la hoja, a su fecha de análisis; sin las decisiones posteriores (P-O1, P-O2, F1-A/F1-B, D-US1/2, D-WM) ni verificación contra la fuente oficial.

| Campo | Valor |
|---|---|
| Fecha de la hoja | 2026-11-07 |
| Tarea | cribado-44512238939-spie |
| SHA del código | 833cd50a9bba34006519119c72a29c70a1656fb7 |
| Huella del paquete (package_sha256) | f35ca343cabda8233b25538184f58ca7a745616cdaac1b14901045eee550e803 |
| Huella del envío (bundle_sha256) | 7b285e203a26369c2eb14599a4be8df4b3bfe4fc6530ab944e4e62a7a24ba2b9 |
| Huella del encargo | 32b5c7f313e61a61fb0f5e68a75b3c44004eb902e97b98720fb98fa8d383e6cf |
| Huella de la Release | 4d30f7352948fe7e7fe3b133386eabedbddcc71d997e972a1c6db7964d58b0a9 |
| Huella del libro | 87ff507e381889d4ecd68f3cc194abf0f60428943b30c763d18c8feaada8f580 |
| Modelo pedido / devuelto | claude-opus-5-5 / claude-opus-5-5 |
| Esfuerzo | high |
| Gramática del servidor | True |
| Mensajes enviados | 1 |
| Cota de entrada antes de llamar | 168210 tokens |
| Reserva estimada antes de llamar | USD 1.3282 |
| Uso de tokens | entrada 74863, salida 4579 |
| Coste | CONOCIDO_ESTIMADO; estimado USD 0.391032; cota 0.391032 |

| id | ruta | sha256 | bytes |
|---|---|---|---|
| respuesta | EMPRESAS_LOTES_COMPLETOS/Spie/Spie_respuesta.md | 1930d35286a3692bc73aced2a2321e5f213f78a231d436fa554baf3df38c99c7 | 51080 |
| hoja_analisis | EMPRESAS_LOTES_COMPLETOS/Spie/Spie_evaluada.xlsx#Análisis | 168fae80eb531475659f46d19c61982e0f3a649e1cca15531b10f248fcafccf9 | 24205 |
| hoja_control_maestro | EMPRESAS_LOTES_COMPLETOS/Spie/Spie_evaluada.xlsx#Control maestro | ea8eb8604d09ef0bc8ce6a1ee5fb50c60406ffb5d11ac36a3feae91f7e0f0842 | 71921 |

## Salida del modelo (datos, sin acciones ejecutables)

Veredicto `estudiar_a_fondo` · DCF de la plantilla aplica: `si`

| Filtro | Resultado |
|---|---|
| calidad | dudoso |
| caja | pasa |
| balance | pasa |
| precio | dudoso |
| encaje | no_aplica |

### Pasivo por arrendamientos (dato aparte)

    Control maestro!M36 = 621.2 (pasivo por arrendamientos a 30-jun-2026; no entra en el cociente de deuda)


### Tipo de negocio y motor

    Servicios multitécnicos de mantenimiento e instalación (energía y comunicaciones), recurrentes, con capex mínimo y circulante negativo; crece sobre todo comprando empresas pequeñas (bolt-ons).
    El DCF de caja libre de la plantilla sirve para un negocio recurrente de capex bajo, pero contrastado con el gasto en adquisiciones: la base no resta el M&A, así que el crecimiento debe ser solo orgánico o restarse lo que cuestan las compras.

### calidad

    Es un negocio de servicios con más del 75% recurrente, margen EBITA que sube del 5,1% al 7,6% (2020–2025) y ROCE del 14,9% antes de impuestos (10,4% después), pero sin foso visible (4% de cuota en Alemania, C18 = No) y con crecimiento mayormente comprado: es una duda que el estudio puede resolver, no un descarte.
    Dato clave: Análisis!C24 = 0.149

### caja

    La caja libre base es de 457,2 mm después de intereses, principal de arrendamientos y SBC, con CFO/beneficio neto de 3,55x y un capex de solo 75,1 mm, aunque las adquisiciones se llevan el 74–84% de esa caja.
    Dato clave: Análisis!C52 = 457.2

### balance

    El 2,31x de Análisis!C33 incluye arrendamientos y no sirve tal cual; sin ellos, la deuda neta de 1.967,1 sobre el EBITDA que ya resta el alquiler da ≈2,26x (covenant 2,1x frente a un máximo de 4,00x), sin vencimientos antes de junio de 2027 y con un RCF de 1.000 sin disponer, lo que es asumible para un negocio recurrente, aunque junio es el pico estacional de deuda y las pensiones (601,4) lo elevan.
    Dato clave: Control maestro!M36 = 1967.1 (deuda neta sin arrendamientos; sin arrendamientos ÷ EBITDA antes de NIIF 16 ≈ 2.26x en Control maestro!N36; deuda bruta sin arrendamientos 2527.9 en Control maestro!M51)

### precio

    A 44,54 € cotiza un 10% por debajo del valor ponderado de 49,59 € y del escenario normal de 47,75 €, pero un 40% por encima del precio de Sí de la etapa 1 (31,81 €) y por encima de los 37,79 € que salen con r = 11%, de modo que el resultado cambia con ±2 puntos de tasa; discrepo del No de la etapa 1, que cuento como dato.
    Dato clave: Análisis!C83 = 49.5888102152574

### encaje

    El paquete no trae la cartera de la persona responsable; solo consta una capitalización de 7.699 mm, y este filtro no elimina.
    Dato clave: Análisis!C41 = 7699

### Qué lo cambiaría

    - Que se publique un retorno después de impuestos sobre las adquisiciones por debajo del 9% o un deterioro de goodwill en el test de FY2026: descartar.
    - Una cotización por debajo de ~37,8 € (valor ponderado a r = 11%, Análisis!B92/C92): el precio pasaría con holgura.
    - Que la deuda neta sin arrendamientos supere ~3x el EBITDA tras alquiler a diciembre de 2026 sin que entre el EBITDA de lo comprado.

### Qué falta

    - Retorno sobre el capital de las adquisiciones (ROIC/ROCE publicado) y los múltiplos pagados por operación (ROFA ≈17–18x EBITA según la respuesta).
    - EBITDA de las sociedades compradas aún no consolidadas (≈698 mm ya en la deuda) y umbral vigente del covenant a junio de 2026.
    - Control maestro cita una «decisión del inversor (15-nov-2026)» posterior a la fecha de la hoja (2026-11-07); además, el precio de 44,54 € es del 6-nov-2026 y debe actualizarse.

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

