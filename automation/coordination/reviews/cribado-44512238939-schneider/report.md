# Cribado · Schneider

Estado de la ejecución: `AUDITORIA_DOCUMENTAL_PENDIENTE_ACEPTACION`

Cribado pendiente de revisión humana. No es una recomendación de compra, ni aceptación, ni aptitud para dinero real. Tasa 9 % provisional.

C-ARR (decisión de la persona responsable): los arrendamientos se cuentan una sola vez, en el flujo. El alquiler se resta de la caja libre; la deuda, deuda/EBITDA y deuda/caja libre se miden sin arrendamientos; el pasivo por arrendamientos se muestra aparte, como dato.

Cifras de la etapa 1 tal como las guardó la hoja, a su fecha de análisis; sin las decisiones posteriores (P-O1, P-O2, F1-A/F1-B, D-US1/2, D-WM) ni verificación contra la fuente oficial.

| Campo | Valor |
|---|---|
| Fecha de la hoja | 2026-10-11 |
| Tarea | cribado-44512238939-schneider |
| SHA del código | 833cd50a9bba34006519119c72a29c70a1656fb7 |
| Huella del paquete (package_sha256) | 7f0b1c718d4b568a7fda8e14bfc36ca88ec91b0af9fe593e02fece04e97455a5 |
| Huella del envío (bundle_sha256) | 0ef73d873ccf8b49457ce01b3a4cf6a7039a0042ccd8ce17d8a0f5a56707cddb |
| Huella del encargo | 32b5c7f313e61a61fb0f5e68a75b3c44004eb902e97b98720fb98fa8d383e6cf |
| Huella de la Release | 4d30f7352948fe7e7fe3b133386eabedbddcc71d997e972a1c6db7964d58b0a9 |
| Huella del libro | fa4b43fdfc7fe9b03a4c188b1d52775a61a474151edc3e22e86e8b324daa910a |
| Modelo pedido / devuelto | claude-opus-5-5 / claude-opus-5-5 |
| Esfuerzo | high |
| Gramática del servidor | True |
| Mensajes enviados | 1 |
| Cota de entrada antes de llamar | 144780 tokens |
| Reserva estimada antes de llamar | USD 1.23448 |
| Uso de tokens | entrada 66222, salida 4883 |
| Coste | CONOCIDO_ESTIMADO; estimado USD 0.362548; cota 0.362548 |

| id | ruta | sha256 | bytes |
|---|---|---|---|
| respuesta | EMPRESAS_LOTES_COMPLETOS/Schneider/Schneider_respuesta.md | 7b76975609efbb706742cac8cc29930fd61e58d469aa637051e20db55ec07c1e | 34089 |
| cambios_v2 | EMPRESAS_LOTES_COMPLETOS/Schneider/Schneider_cambios_v2.md | 94ceefc0d93117cb604bc11d481a6fa0b447652df4f22202cc2971247e7f46a1 | 3637 |
| hoja_analisis | EMPRESAS_LOTES_COMPLETOS/Schneider/Schneider_evaluada.xlsx#Análisis | fd23c42bc674cc81fe391dc98e5eff414afc17d505a73fb6092a38db8c25ff5a | 23091 |
| hoja_control_maestro | EMPRESAS_LOTES_COMPLETOS/Schneider/Schneider_evaluada.xlsx#Control maestro | 49a38c84f8361ea04dd4ee3d8b28bf9c8936be79c2a5d623e17476c2a1fd09cf | 62702 |

## Salida del modelo (datos, sin acciones ejecutables)

Veredicto `vigilar` · DCF de la plantilla aplica: `dudoso`

| Filtro | Resultado |
|---|---|
| calidad | pasa |
| caja | pasa |
| balance | dudoso |
| precio | no_pasa |
| encaje | no_aplica |

### Pasivo por arrendamientos (dato aparte)

    Control maestro!M36 = 1554 (proxy a 31/12/2025; no publicado a 30/06/2026)


### Tipo de negocio y motor

    Industrial de equipos eléctricos: distribución eléctrica y gestión de la energía (≈83% de las ventas), automatización industrial y software, vendidos sobre todo por canal; negocio bastante estable con exposición creciente a centros de datos y en plena compra grande (PTC, Cognite).
    DCF de caja libre al accionista, pero sobre el perímetro pro forma con PTC y Cognite: FCF por acción tras intereses de la deuda nueva y con las acciones de la ampliación, o bien el DCF de la plantilla restando la deuda neta incremental hasta tener dos ejercicios consolidados.

### calidad

    El núcleo eléctrico se entiende (Análisis!C11 = Sí) y muestra ventaja en las cifras —ROCE del 12,1% al 15,1% y margen EBITA ajustado del 15,1% al 18,7% en FY18–FY25—, aunque la asignación de capital es dudosa (Uplight ≈627 M€ deteriorados a cero, PTC a 21x EBITA 2027e) y el 30% de los pedidos viene de centros de datos; discrepo del «demasiado difícil» de la etapa 1 porque PTC (EV 23,7 bn$, ≈14% de la capitalización) cambia el perímetro pero no hace ininteligible el negocio.
    Dato clave: Análisis!C24 = 0.151

### caja

    Convierte bien el beneficio en caja: caja operativa/beneficio de 1,29x (Análisis!C26), FCF normalizado que sube todos los años de 3.332 a 4.819 mm (FY21–FY25) y FCF base de 3.886 mm ya neto de arrendamientos (331) y SBC (214), con capex ≈3,7% de ventas; la única duda es el aumento de cobros en H1 2026 (DSO 84,8 → 94,2 días).
    Dato clave: Análisis!C52 = 3886

### balance

    Sin arrendamientos, la deuda neta de 15.360 mm sobre un EBITDA sin NIIF 16 de ≈8.344 mm da ≈1,84x, holgado para un negocio bastante estable (el 1,93x de Análisis!C33 incluye arrendamientos y no sirve tal cual); pero el pro forma con PTC y Cognite sube a ≈3,6–3,8x (estimación con arrendamientos, no recalculable sin ellos), la caja cubre solo 0,82x la deuda a corto y la exposición del 30% de los pedidos a centros de datos no justifica ese nivel sin más estudio.
    Dato clave: Control maestro!M36 = 15360 (deuda financiera neta sin arrendamientos, 30/06/2026; ÷ EBITDA sin NIIF 16 ≈8.344 = 1,84x según Control maestro!N36)

### precio

    A 266,4 € la cotización supera el precio de Sí (≈107 €, escenario malo Análisis!B78 = 106,9), el ponderado (158,4 €), el escenario bueno (232,7 €) y aun el ponderado con r al 7% (237,1 €), y el DCF inverso exige un 14,5% anual, por encima del bueno (12%); la duda sobre la aplicabilidad del DCF no rescata el precio, porque el modelo no resta la deuda neta (≈27 €/acción) ni la ampliación para PTC, y el rendimiento del FCF LTM (3,6%) apenas supera al Bund (3,47%).
    Dato clave: Análisis!C37 = 266.4

### encaje

    El paquete no trae la cartera de la persona responsable y la hoja solo da datos de la empresa (capitalización de 150.097 mm), así que no hay base para juzgar el encaje.
    Dato clave: Análisis!C41 = 150097

### Qué lo cambiaría

    - Una cotización por debajo de ≈158 € (valor ponderado, Análisis!C83) y acercándose al precio de Sí de ≈107 € pasaría a estudiar_a_fondo.
    - Una deuda neta sin arrendamientos sobre EBITDA por encima de ≈3,5x durante más de dos años tras cerrar PTC, o una segunda ampliación de capital, llevaría a descartar.
    - Deterioros en PTC, AVEVA u OSIsoft o una caída de la cartera de pedidos de centros de datos dos años seguidos rebajarían calidad y caja.

### Qué falta

    - Negocio y cuentas de PTC y Cognite (FCF, márgenes, clientes): la hoja solo da precio, múltiplos y calendario.
    - Concentración de clientes de centros de datos (peso en ventas y cartera) y deuda neta pro forma sin arrendamientos tras PTC.
    - Resultados del 3T 2026 (16/10/2026) y pasivo por arrendamientos a 30/06/2026: posteriores a la hoja o no publicados.

### Comprobaciones mecánicas y normalizaciones

    {
      "comprobaciones": {
        "avisos": [
          "Filtro calidad: motivo de más de 400 caracteres.",
          "Filtro balance: motivo de más de 400 caracteres.",
          "Filtro precio: motivo de más de 400 caracteres."
        ],
        "nota": "Comprobaciones mecánicas informativas: no acreditan la calidad económica."
      },
      "normalizaciones": []
    }

