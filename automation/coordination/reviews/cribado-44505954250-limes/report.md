# Cribado · Limes

Estado de la ejecución: `AUDITORIA_DOCUMENTAL_PENDIENTE_ACEPTACION`

Cribado pendiente de revisión humana. No es una recomendación de compra, ni aceptación, ni aptitud para dinero real. Tasa 9 % provisional.

C-ARR (decisión de la persona responsable): los arrendamientos se cuentan una sola vez, en el flujo. El alquiler se resta de la caja libre; la deuda, deuda/EBITDA y deuda/caja libre se miden sin arrendamientos; el pasivo por arrendamientos se muestra aparte, como dato.

Cifras de la etapa 1 tal como las guardó la hoja, a su fecha de análisis; sin las decisiones posteriores (P-O1, P-O2, F1-A/F1-B, D-US1/2, D-WM) ni verificación contra la fuente oficial.

| Campo | Valor |
|---|---|
| Fecha de la hoja | 2026-10-09 |
| Tarea | cribado-44505954250-limes |
| SHA del código | 833cd50a9bba34006519119c72a29c70a1656fb7 |
| Huella del paquete (package_sha256) | becbff94fd5fd8993c27fe44e078e119ac673c515817837e446b6463cf3b36d7 |
| Huella del envío (bundle_sha256) | f0a38408fc9ed9eddd69769d2cca2e4d417734e05ce4ed7fe1cafa9aa34790bb |
| Huella del encargo | 32b5c7f313e61a61fb0f5e68a75b3c44004eb902e97b98720fb98fa8d383e6cf |
| Huella de la Release | 4d30f7352948fe7e7fe3b133386eabedbddcc71d997e972a1c6db7964d58b0a9 |
| Huella del libro | 1179a16bbe6ee07362183e6004b6b73c7af005f592533286b389bd8a3b5fa02b |
| Modelo pedido / devuelto | claude-opus-5-5 / claude-opus-5-5 |
| Esfuerzo | high |
| Gramática del servidor | True |
| Mensajes enviados | 1 |
| Cota de entrada antes de llamar | 145842 tokens |
| Reserva estimada antes de llamar | USD 1.238728 |
| Uso de tokens | entrada 66086, salida 3175 |
| Coste | CONOCIDO_ESTIMADO; estimado USD 0.327844; cota 0.327844 |

| id | ruta | sha256 | bytes |
|---|---|---|---|
| respuesta | EMPRESAS_LOTES_COMPLETOS/Limes/Limes_respuesta.md | 7c4ed6bbed2ce78f5625a91a4f91226aab80b68696365e531b0d10e55ac0157f | 37206 |
| cambios_v2 | EMPRESAS_LOTES_COMPLETOS/Limes/Limes_cambios_v2.md | b38968e15e522e351a3833753d25ff4453febea5daa0eb3ff14280fe2ff60995 | 4867 |
| hoja_analisis | EMPRESAS_LOTES_COMPLETOS/Limes/Limes_evaluada.xlsx#Análisis | 00b39fbee95ab08e87c9105be4da5592ffaafac29ea9c37ecbcee79c90e7f8ef | 24222 |
| hoja_control_maestro | EMPRESAS_LOTES_COMPLETOS/Limes/Limes_evaluada.xlsx#Control maestro | 7ddfe01888908e0b1fcef3dec49e0dec9129e1c4e04c10b6c97f16a1ecbc575e | 58488 |

## Salida del modelo (datos, sin acciones ejecutables)

Veredicto `vigilar` · DCF de la plantilla aplica: `si`

| Filtro | Resultado |
|---|---|
| calidad | dudoso |
| caja | dudoso |
| balance | pasa |
| precio | no_pasa |
| encaje | no_aplica |

### Pasivo por arrendamientos (dato aparte)

    No consta en la hoja: con HGB no hay pasivo por arrendamientos (Análisis!C49 = 0); el alquiler LTM es de 7,0 mm y las obligaciones a largo plazo no se publican desde 2021 (16,4 M€ nominales en 2020; Control maestro, fila 47).


### Tipo de negocio y motor

    Operador de clínicas privadas premium de psiquiatría, psicoterapia y psicosomática (Alemania, Suiza y Liechtenstein), negocio de servicios sanitarios en expansión por aperturas y adquisiciones, con filiales con minoritarios y cuentas en HGB.
    DCF de caja libre de la plantilla para un negocio de servicios estable con poca deuda, contrastado con un FCF normalizado con capex de mantenimiento y atribuible tras minoritarios (≈0,805), porque el FCF base está deprimido por la expansión.

### calidad

    El negocio se entiende (estancias psiquiátricas privadas con demanda creciente), pero el ROCE del 26 % antes de impuestos baja al 7,8–14,3 % con los alquileres capitalizados, el margen EBIT cae del 20,0 % (2022) al 16,5 % en H1-2026, el crecimiento viene por adquisiciones y la hoja no demuestra foso.
    Dato clave: Análisis!C24 = 0.26

### caja

    El CFO supera al beneficio (1,57x) y sale positivo, pero el FCF base es de solo 2,027 mm, irregular (CFO menos inversión entre −1,0 y 6,7 mm en 2019-2025), con un estado de flujos no auditado y un DSO que sube a ≈63 días; con capex de mantenimiento estimado de 1,35–1,50 mm sería mucho mayor, pero no está demostrado.
    Dato clave: Análisis!C52 = 2.027

### balance

    Sin arrendamientos (HGB, el alquiler ya se resta en EBITDA y CFO), la deuda con coste es 9,28 mm frente a una caja de 8,24 mm, es decir, 1,03 mm de deuda neta sobre un EBITDA LTM de 13,56 mm (0,076x; 0,11x sin los otros ingresos atípicos), y toda vence a más de un año: holgura amplia incluso para un negocio menos estable.
    Dato clave: Análisis!C54 = 9.28

### precio

    A 535 € la cotización está muy por encima del valor ponderado de 156,5 € e incluso del escenario bueno de 262,8 €; el precio exige un crecimiento del FCF del 25,4 % anual, y con r al 7 % el máximo es 247,9 €, de modo que no cambia en ±2 puntos (el precio de Sí de la etapa 1, ≈76 €, no es operativo y no lo heredo).
    Dato clave: Análisis!C83 = 156.503037336133

### encaje

    El paquete no trae la cartera; solo consta como dato una capitalización de 159,4 mm con liquidez muy baja (18.617 acciones negociadas en 2025), que no elimina en el cribado.
    Dato clave: Análisis!C41 = 159.4

### Qué lo cambiaría

    - Una cotización cerca o por debajo del valor ponderado de la hoja (≈157 €), con el negocio intacto.
    - Un ejercicio 2026 completo con margen EBITDA ≥ 22 % sin ingresos atípicos, FCF creciente y DSO de vuelta por debajo de 50 días.
    - Que la compra de Villa Boccella se financie con deuda relevante o con capital emitido barato, o que la deuda neta supere claramente 1x el EBITDA.

### Qué falta

    - Ocupación real, márgenes por clínica, crecimiento orgánico y competidores: la empresa no los publica, así que no se puede juzgar la duración de la ventaja.
    - Explicación de los 3,9 mm de otros ingresos de 2025 y estado de flujos auditado: hoy no está auditado en ningún año.
    - Importe actual de las obligaciones de alquiler y precio de compra de Villa Boccella y su financiación.

### Comprobaciones mecánicas y normalizaciones

    {
      "comprobaciones": {
        "avisos": [],
        "nota": "Comprobaciones mecánicas informativas: no acreditan la calidad económica."
      },
      "normalizaciones": []
    }

