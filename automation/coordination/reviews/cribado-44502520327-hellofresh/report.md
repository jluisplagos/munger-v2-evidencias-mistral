# Cribado · HelloFresh

Estado de la ejecución: `AUDITORIA_DOCUMENTAL_PENDIENTE_ACEPTACION`

Cribado pendiente de revisión humana. No es una recomendación de compra, ni aceptación, ni aptitud para dinero real. Tasa 9 % provisional.

C-ARR (decisión de la persona responsable): los arrendamientos se cuentan una sola vez, en el flujo. El alquiler se resta de la caja libre; la deuda, deuda/EBITDA y deuda/caja libre se miden sin arrendamientos; el pasivo por arrendamientos se muestra aparte, como dato.

Cifras de la etapa 1 tal como las guardó la hoja, a su fecha de análisis; sin las decisiones posteriores (P-O1, P-O2, F1-A/F1-B, D-US1/2, D-WM) ni verificación contra la fuente oficial.

| Campo | Valor |
|---|---|
| Fecha de la hoja | 2026-10-25 |
| Tarea | cribado-44502520327-hellofresh |
| SHA del código | 833cd50a9bba34006519119c72a29c70a1656fb7 |
| Huella del paquete (package_sha256) | 7b4e4df28e38a7fdbe7040353b77de5d22de3abf390b85bb1e2e0cfa00e41105 |
| Huella del envío (bundle_sha256) | 6d0ecfd98d8fa866f7230e28695544177ed256b59825ab37de7deefdcfee37f0 |
| Huella del encargo | 32b5c7f313e61a61fb0f5e68a75b3c44004eb902e97b98720fb98fa8d383e6cf |
| Huella de la Release | 4d30f7352948fe7e7fe3b133386eabedbddcc71d997e972a1c6db7964d58b0a9 |
| Huella del libro | f92c0a2380c1042a8107d7dcff57bfecac4ebea5521dd3bd5cde0cf8a9fce3ff |
| Modelo pedido / devuelto | claude-opus-5-5 / claude-opus-5-5 |
| Esfuerzo | high |
| Gramática del servidor | True |
| Mensajes enviados | 1 |
| Cota de entrada antes de llamar | 162559 tokens |
| Reserva estimada antes de llamar | USD 1.305596 |
| Uso de tokens | entrada 74282, salida 3577 |
| Coste | CONOCIDO_ESTIMADO; estimado USD 0.368668; cota 0.368668 |

| id | ruta | sha256 | bytes |
|---|---|---|---|
| respuesta | EMPRESAS_LOTES_COMPLETOS/HelloFresh/HelloFresh_respuesta.md | b2f5987db4a143e88cc46872dfcf6ad87714846602e4fd5a14ec0c0abfe4fae8 | 48493 |
| hoja_analisis | EMPRESAS_LOTES_COMPLETOS/HelloFresh/HelloFresh_evaluada.xlsx#Análisis | 037ce820023e3dadbc5e0f8c16ab3875734e44c926bdece943013716dd717b34 | 24849 |
| hoja_control_maestro | EMPRESAS_LOTES_COMPLETOS/HelloFresh/HelloFresh_evaluada.xlsx#Control maestro | 43a8291cc6890ec7472526ff002771ad6d2f3a37140013971ddf7cb182c0a2b8 | 68286 |

## Salida del modelo (datos, sin acciones ejecutables)

Veredicto `descartar` · DCF de la plantilla aplica: `no`

| Filtro | Resultado |
|---|---|
| calidad | no_pasa |
| caja | no_pasa |
| balance | pasa |
| precio | no_aplica |
| encaje | no_aplica |

### Pasivo por arrendamientos (dato aparte)

    Control maestro!M51 = 571.3 (pasivo por arrendamientos a 30-jun-2026, MEUR; principal pagado LTM 122,1 según Control maestro!M46)


### Tipo de negocio y motor

    Consumo discrecional: kits de comida y platos preparados por suscripción online directa al consumidor (D2C), con plantas propias y en situación de turnaround.
    Poder de ganancia y caja normalizados: FCF después de arrendamientos con capex de mantenimiento separado y un AEBITDA según la guía rebajada a 350-370 MEUR, contrastado con el EV sin arrendamientos, en lugar de un DCF de crecimiento sobre una base negativa.

### calidad

    El negocio se entiende, pero no muestra ventaja en las cifras: ROCE pre-impuestos del 1,6% frente a un WACC propio del 9,9-10,6%, márgenes comprimiéndose (AEBITDA del 13,5% en FY20 al 5,5% LTM), pedidos de 125,13 a 100,53 millones y un turnaround declarado.
    Dato clave: Análisis!C24 = 0.016

### caja

    La caja libre base de la plantilla (media FY23-25, después de arrendamientos y SBC) es de −89,4 MEUR y la LTM de −140,5 (Análisis!C40), con FCF del accionista negativo o casi nulo en FY22-LTM; el ✓ de conversión de 10,97x (Análisis!C26) es mecánico, porque el denominador es casi cero, y no lo hago mío.
    Dato clave: Análisis!C52 = -89.4

### balance

    El 1,71x de Análisis!C33 incluye 571,3 de arrendamientos y no sirve tal cual; sin ellos, el préstamo de 179,4 frente a 246,9 de caja deja una caja neta de unos 67,5 MEUR, así que el balance pasa hoy, aunque el FCF LTM de −94,0 consume caja, el RCF de 400 vence en abril de 2027 y el bono de 350 al 5,5% de julio de 2026 eleva la deuda bruta sin arrendamientos a unos 529 MEUR.
    Dato clave: Control maestro!M51 = 179.4 (deuda financiera sin arrendamientos a 30-jun-2026) frente a Análisis!C53 = 246.9 de caja

### precio

    Con una base de FCF negativa el DCF degenera: el valor ponderado sale en −8,10 EUR por acción frente a una cotización de 3,087 EUR, no existe precio de Sí positivo, y para concluir haría falta un FCF normalizado (capex de mantenimiento más principal de arrendamientos) frente a un EV/EBITDA sin arrendamientos de 2,15x; además, la hoja es anterior a los resultados del tercer trimestre de 2026.
    Dato clave: Análisis!C43 = -8.10175686829977

### encaje

    El paquete no trae la cartera de la persona responsable; la capitalización de 447,5 MEUR es solo contexto y no uso el tamaño de posición que figura en la hoja.
    Dato clave: Análisis!C41 = 447.5

### Qué lo cambiaría

    - FCF del accionista positivo y por encima de 150 MEUR dos ejercicios seguidos, con capex por debajo de 150 MEUR y principal de arrendamientos a la baja.
    - ROCE sostenido por encima del 10% con pedidos estables o al alza a tipo constante y margen de contribución por encima del 27%.
    - Un deterioro adicional del fondo de comercio o una deuda neta sin arrendamientos que pase a positiva por la quema de caja confirmaría el descarte.

### Qué falta

    - Reparto del capex entre mantenimiento y crecimiento, y retención por cohortes y coste de adquisición de clientes (no publicados).
    - Resultados del tercer trimestre de 2026 (publicación el 05-nov-2026) y test anual de fondo de comercio (31-oct-2026), ambos posteriores a la fecha de la hoja; texto y umbral de los covenants no divulgados.
    - Inconsistencia de fechas: Control maestro fecha la decisión del inversor sobre la ventana del FCF el 28-oct-2026, posterior a la fecha de la hoja (25-oct-2026).

### Comprobaciones mecánicas y normalizaciones

    {
      "comprobaciones": {
        "avisos": [
          "Un texto menciona un tamaño de posición o un porcentaje de cartera."
        ],
        "nota": "Comprobaciones mecánicas informativas: no acreditan la calidad económica."
      },
      "normalizaciones": []
    }

