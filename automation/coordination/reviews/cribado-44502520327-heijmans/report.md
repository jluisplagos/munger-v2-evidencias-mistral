# Cribado · Heijmans

Estado de la ejecución: `AUDITORIA_DOCUMENTAL_PENDIENTE_ACEPTACION`

Cribado pendiente de revisión humana. No es una recomendación de compra, ni aceptación, ni aptitud para dinero real. Tasa 9 % provisional.

C-ARR (decisión de la persona responsable): los arrendamientos se cuentan una sola vez, en el flujo. El alquiler se resta de la caja libre; la deuda, deuda/EBITDA y deuda/caja libre se miden sin arrendamientos; el pasivo por arrendamientos se muestra aparte, como dato.

Cifras de la etapa 1 tal como las guardó la hoja, a su fecha de análisis; sin las decisiones posteriores (P-O1, P-O2, F1-A/F1-B, D-US1/2, D-WM) ni verificación contra la fuente oficial.

| Campo | Valor |
|---|---|
| Fecha de la hoja | 2026-11-05 |
| Tarea | cribado-44502520327-heijmans |
| SHA del código | 833cd50a9bba34006519119c72a29c70a1656fb7 |
| Huella del paquete (package_sha256) | 9e3647d485cf67064a638868d1db25a744567abfec115193ac6ea4656c78302b |
| Huella del envío (bundle_sha256) | 030310d971d3958b9c6fc702527ca7e9dd9d87afa7dfb99abf636ec150eb7a73 |
| Huella del encargo | 32b5c7f313e61a61fb0f5e68a75b3c44004eb902e97b98720fb98fa8d383e6cf |
| Huella de la Release | 4d30f7352948fe7e7fe3b133386eabedbddcc71d997e972a1c6db7964d58b0a9 |
| Huella del libro | 99cffff707c65908429454bdcd68945fbd9ef7d3b361325ea477b09bdc761de2 |
| Modelo pedido / devuelto | claude-opus-5-5 / claude-opus-5-5 |
| Esfuerzo | high |
| Gramática del servidor | True |
| Mensajes enviados | 1 |
| Cota de entrada antes de llamar | 131635 tokens |
| Reserva estimada antes de llamar | USD 1.1819 |
| Uso de tokens | entrada 59462, salida 3961 |
| Coste | CONOCIDO_ESTIMADO; estimado USD 0.317068; cota 0.317068 |

| id | ruta | sha256 | bytes |
|---|---|---|---|
| respuesta | EMPRESAS_LOTES_COMPLETOS/Heijmans/Heijmans_respuesta.md | c7c7b783752c683c8433343800735404696b36fbc9304c8af80d88630e5c87c1 | 30627 |
| hoja_analisis | EMPRESAS_LOTES_COMPLETOS/Heijmans/Heijmans_evaluada.xlsx#Análisis | 213dcb6db1437b56ffd9dd7c6677b579d31c7e52c0301380e9683b7224671c6d | 23234 |
| hoja_control_maestro | EMPRESAS_LOTES_COMPLETOS/Heijmans/Heijmans_evaluada.xlsx#Control maestro | a999be48a4419cdc087e334bb4c8229d122078525a795e26135c4fe6f39ad075 | 56896 |

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

    Control maestro!M51: pasivos por arrendamiento = 124.1 (Análisis!C54 = 132.5 los incluye junto a 8,4 de deuda financiera)


### Tipo de negocio y motor

    Constructora, promotora residencial y de infraestructuras centrada solo en Países Bajos; negocio de proyectos cíclico, con circulante negativo por anticipos y capex bajo.
    Caja libre de ciclo medio, con margen normalizado a lo largo de un ciclo completo de vivienda y obra pública (la base antes de circulante de la plantilla es una aproximación razonable), contrastada con un escenario de reversión de los anticipos.

### calidad

    El negocio se entiende (Análisis!C11 = Sí), por lo que no comparto el «demasiado difícil» de la hoja; aun así, el ROCE del 27,9 % está inflado por el circulante negativo (≈22,6 % normalizado), no hay foso estructural (C18 = No) y el margen EBITDA subyacente del 9,1 % de 2025 puede ser pico de ciclo tras la pérdida de 110,5 de 2016.
    Dato clave: Análisis!C24 = 0.279

### caja

    La caja libre normalizada antes de circulante es positiva y recurrente (60,1 base; 56,0 de media a 5 años y 64,5 a 3 años), pero solo convierte ≈46 % del beneficio de 2025 (130). El FCF publicado salta de ≈10 en 2023 a 189,6 en 2025 por los anticipos (+113,5), así que el ratio de 2,12x de Análisis!C26 está inflado y no prueba calidad.
    Dato clave: Análisis!C52 = 60.1

### balance

    Sin arrendamientos la deuda es 8,4 frente a una caja de 190 (104,7 no restringida), lo que da caja neta y una deuda neta/EBITDA de ≈−1,00x con el EBITDA aproximado antes de NIIF 16 (≈180,9). El −0,26x de Análisis!C33 incluye los arrendamientos y no sirve tal cual. Los compromisos fuera de balance (≈392 de suelo condicionado, 169,8 de avales y 111 de responsabilidad solidaria en VOF) son la vigilancia propia de una cíclica, pero no rompen el filtro.
    Dato clave: Control maestro!M51 = 8.4 (deuda financiera sin arrendamientos, dentro de Análisis!C54 = 132.5)

### precio

    A 85,85 € la cotización supera el valor ponderado de 38,77 € (Análisis!C83) y hasta el escenario bueno de 60,80 € (Análisis!D78). Tampoco cambia con r al 7 %: el ponderado sube solo a 55,36 € (Análisis!C90). El DCF inverso exige un 15,3 % anual de crecimiento (Análisis!C86). Con el motor de ciclo medio sería aún más exigente, así que está claramente caro.
    Dato clave: Análisis!C37 = 85.85

### encaje

    El paquete no trae la cartera de la persona responsable; solo consta una capitalización de 2.359 mm, sin nada concreto sobre encaje.
    Dato clave: Análisis!C41 = 2359

### Qué lo cambiaría

    - Una cotización por debajo de ≈39 € (valor ponderado de Análisis!C83) lo acercaría a estudiar_a_fondo.
    - Un margen EBITDA subyacente por debajo del 7 % o un proyecto con pérdidas de decenas de millones llevaría a descartar.
    - Una caja libre normalizada de 2026 por encima de 80 mm sin anticipos extraordinarios reforzaría los filtros de caja y calidad.

### Qué falta

    - Serie anual de caja libre antes de circulante 2016–2025 y márgenes por proyecto a lo largo de una caída de la vivienda (solo hay medias a 3 y 5 años).
    - Cifras del H1-26 sin verificar y EBITDA antes de NIIF 16 solo aproximado (≈180,9).
    - Control maestro fecha la decisión de la base del DCF el 10-nov-2026, después de la fecha de hoja del 05-nov-2026: incoherencia de fechas en la fuente.

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

