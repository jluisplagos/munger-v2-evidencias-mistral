# Cribado · Thales

Estado de la ejecución: `AUDITORIA_DOCUMENTAL_PENDIENTE_ACEPTACION`

Cribado pendiente de revisión humana. No es una recomendación de compra, ni aceptación, ni aptitud para dinero real. Tasa 9 % provisional.

C-ARR (decisión de la persona responsable): los arrendamientos se cuentan una sola vez, en el flujo. El alquiler se resta de la caja libre; la deuda, deuda/EBITDA y deuda/caja libre se miden sin arrendamientos; el pasivo por arrendamientos se muestra aparte, como dato.

Cifras de la etapa 1 tal como las guardó la hoja, a su fecha de análisis; sin las decisiones posteriores (P-O1, P-O2, F1-A/F1-B, D-US1/2, D-WM) ni verificación contra la fuente oficial.

| Campo | Valor |
|---|---|
| Fecha de la hoja | 2026-10-11 |
| Tarea | cribado-44515220408-thales |
| SHA del código | 833cd50a9bba34006519119c72a29c70a1656fb7 |
| Huella del paquete (package_sha256) | f8d94239ba3f76b63406f950ce0f4652201db78c2c6b1ba4685bac4b62b2800f |
| Huella del envío (bundle_sha256) | 345ade3e3404b45a3cfbfec15ea748e919fb4b619138dbdf14cc52ad670d6f8d |
| Huella del encargo | 32b5c7f313e61a61fb0f5e68a75b3c44004eb902e97b98720fb98fa8d383e6cf |
| Huella de la Release | 4d30f7352948fe7e7fe3b133386eabedbddcc71d997e972a1c6db7964d58b0a9 |
| Huella del libro | 8564132aac1964e98004d743eeb3819894b7befde55ad822e13365bc622021c5 |
| Modelo pedido / devuelto | claude-opus-5-5 / claude-opus-5-5 |
| Esfuerzo | high |
| Gramática del servidor | True |
| Mensajes enviados | 1 |
| Cota de entrada antes de llamar | 141878 tokens |
| Reserva estimada antes de llamar | USD 1.222872 |
| Uso de tokens | entrada 63639, salida 4152 |
| Coste | CONOCIDO_ESTIMADO; estimado USD 0.337596; cota 0.337596 |

| id | ruta | sha256 | bytes |
|---|---|---|---|
| respuesta | EMPRESAS_LOTES_COMPLETOS/Thales/Thales_respuesta.md | 73d1e2c2029e1e042c3153bde5830d404048b98c06c3679dc6c47cce4a2aca3a | 36629 |
| cambios_v2 | EMPRESAS_LOTES_COMPLETOS/Thales/Thales_cambios_v2.md | 96bb95381f6c9a49efa0d16769b5c079082b1387c3b65220afeaf4229fbfc8c1 | 3293 |
| hoja_analisis | EMPRESAS_LOTES_COMPLETOS/Thales/Thales_evaluada.xlsx#Análisis | 2e7f11e51fd061d816d4a60e27aaa32a00dabf9f5b37fb351d13b5cdbc4a8139 | 23371 |
| hoja_control_maestro | EMPRESAS_LOTES_COMPLETOS/Thales/Thales_evaluada.xlsx#Control maestro | a2e4226fb840ef10124c60321d9991bf15fcea1b0c310b2ee9e19b8665fc1713 | 57654 |

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

    Control maestro!M51 = 1400.6 (pasivo por arrendamientos a 30-06-2026)


### Tipo de negocio y motor

    Contratista industrial de defensa, aeroespacial y ciberseguridad con clientes mayoritariamente estatales, contratos largos de precio fijo y anticipos de clientes (núcleo estable de Defensa más segmentos más flojos).
    El DCF de caja libre de la plantilla, con base normalizada a varios años y contraste sin capital circulante, porque los anticipos de clientes mueven mucho la caja anual.

### calidad

    Negocio comprensible con un núcleo de Defensa de calidad y un ROIC propio del 14,7 % en FY2025 (10,9-12,9 % en 2021-2024), con lastres visibles (fondo de comercio del 21,6 % del activo, Cyber & Digital y Espacio flojos, control del Estado y Dassault, investigaciones PNF/SFO); discrepo del «DESCARTAR · demasiado difícil» de Análisis!A6, que nace de la bandera de precio C13 y no de que el negocio no se entienda (C11 y C12 = Sí).
    Dato clave: Análisis!C24 = 0.147

### caja

    La caja libre base normalizada es positiva (1.598,7 M€, ya restados alquileres y SBC), el flujo operativo multiplica por 2,15 el beneficio neto en 2021-2025 y el FOCF fue positivo todos los años 2018-2025, aunque 724 M€ del de 2025 vinieron del capital circulante (anticipos) y pueden revertir.
    Dato clave: Análisis!C52 = 1598.7

### balance

    El cociente de la hoja (Análisis!C33 = 0,15x) incluye arrendamientos y no sirve tal cual; sin ellos, la deuda bruta de 4.174,7 M€ queda por debajo de la caja de 4.997,2 M€, lo que da caja neta (≈ −0,28x sobre un EBITDA sin NIIF 16 que la propia hoja marca como aproximado), y aguanta de sobra el bono de 1.000 M€ de agosto de 2026 y la compra de Exail (≈0,7x pro forma 2027 según la empresa, con arrendamientos) en un negocio de contratos largos prefinanciados.
    Dato clave: Control maestro!M51 = 4174.7 (deuda bruta sin arrendamientos a 30-06-2026) frente a Análisis!C53 = 4997.2 de caja: caja neta ≈ 822.5

### precio

    A 218,3 € la cotización duplica el precio de Sí (≈109 €, el valor del escenario malo) y supera el ponderado de 170,4 € y casi el bueno de 227,6 €; el DCF inverso exige un 10,2 % anual (más que el escenario bueno) y con r al 7 % el ponderado (253 €) tampoco deja la cotización por debajo de 0,75 veces su valor, así que el resultado no cambia con ±2 puntos de tasa.
    Dato clave: Análisis!C37 = 218.3 frente a Análisis!B78 = 108.935854859439

### encaje

    El paquete no trae la cartera de la persona responsable y la hoja solo recoge un plan de etapa 1 ligado al precio de Sí de ≈109 €, que no se hereda; este filtro no elimina.
    Dato clave: No consta cartera en el paquete

### Qué lo cambiaría

    - Una cotización en torno o por debajo de 109 € (valor del escenario malo, Análisis!B78), que llevaría a estudiar a fondo.
    - Un book-to-bill de Defensa por debajo de 1 dos años seguidos o un margen de Defensa sostenido por debajo del 12 %, que rebajaría la calidad.
    - Una deuda sin arrendamientos tras cerrar Exail que pase de caja neta a varias veces el EBITDA, o sanciones graves de las investigaciones PNF/SFO.

### Qué falta

    - Deuda bruta sin arrendamientos pro forma tras el bono de 1.000 M€ de agosto de 2026 y la compra de Exail (valor de empresa ≈3.900 M€): la hoja solo da el pro forma con arrendamientos (≈0,7x).
    - EBITDA sin NIIF 16 verificado: la hoja solo da una aproximación (−269,3 M€ sobre 3.411,4 M€).
    - Precio de Sí exacto (la respuesta da ≈109 € como estimación pendiente del script) y alcance de las investigaciones PNF/SFO, que el informe dice que no se puede evaluar.

### Comprobaciones mecánicas y normalizaciones

    {
      "comprobaciones": {
        "avisos": [
          "Filtro calidad: motivo de más de 400 caracteres.",
          "Filtro balance: motivo de más de 400 caracteres."
        ],
        "nota": "Comprobaciones mecánicas informativas: no acreditan la calidad económica."
      },
      "normalizaciones": []
    }

