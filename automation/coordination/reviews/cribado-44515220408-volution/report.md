# Cribado · Volution

Estado de la ejecución: `AUDITORIA_DOCUMENTAL_PENDIENTE_ACEPTACION`

Cribado pendiente de revisión humana. No es una recomendación de compra, ni aceptación, ni aptitud para dinero real. Tasa 9 % provisional.

C-ARR (decisión de la persona responsable): los arrendamientos se cuentan una sola vez, en el flujo. El alquiler se resta de la caja libre; la deuda, deuda/EBITDA y deuda/caja libre se miden sin arrendamientos; el pasivo por arrendamientos se muestra aparte, como dato.

Cifras de la etapa 1 tal como las guardó la hoja, a su fecha de análisis; sin las decisiones posteriores (P-O1, P-O2, F1-A/F1-B, D-US1/2, D-WM) ni verificación contra la fuente oficial.

| Campo | Valor |
|---|---|
| Fecha de la hoja | 26/10/2026 |
| Tarea | cribado-44515220408-volution |
| SHA del código | 833cd50a9bba34006519119c72a29c70a1656fb7 |
| Huella del paquete (package_sha256) | 7cf54a3a04c3f47c36acad3a16f93c582b68ebc0b2e22046cb7237608052736e |
| Huella del envío (bundle_sha256) | 2b7ea22980a3e328c85c5120fa844344434083f3e58234a16581941462093c59 |
| Huella del encargo | 32b5c7f313e61a61fb0f5e68a75b3c44004eb902e97b98720fb98fa8d383e6cf |
| Huella de la Release | 4d30f7352948fe7e7fe3b133386eabedbddcc71d997e972a1c6db7964d58b0a9 |
| Huella del libro | aedfddb493940eb3ffeea7c37bbfe634063b0d30cf22333bd560667706c3a47c |
| Modelo pedido / devuelto | claude-opus-5-5 / claude-opus-5-5 |
| Esfuerzo | high |
| Gramática del servidor | True |
| Mensajes enviados | 1 |
| Cota de entrada antes de llamar | 192122 tokens |
| Reserva estimada antes de llamar | USD 1.423848 |
| Uso de tokens | entrada 85340, salida 3829 |
| Coste | CONOCIDO_ESTIMADO; estimado USD 0.41794; cota 0.41794 |

| id | ruta | sha256 | bytes |
|---|---|---|---|
| respuesta | EMPRESAS_LOTES_COMPLETOS/Volution/Volution_respuesta.md | f8fa1fe242917a7585d98513fecb2b3e603c65410f1c35e5cc67946edcee5aa3 | 33660 |
| hoja_analisis | EMPRESAS_LOTES_COMPLETOS/Volution/Volution_evaluada.xlsx#Análisis | a6df8bb4187a1c3d812ab9b1babc5bdf1c8d0fea9d4d259eefe1ceb368da7064 | 23170 |
| hoja_control_maestro | EMPRESAS_LOTES_COMPLETOS/Volution/Volution_evaluada.xlsx#Control maestro | d657100aa21f4868c758da97a14f596006cc64b4ce8ca04efa3a8ea58a6cb8c6 | 113079 |

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

    Control maestro!M51 = 51.6 (6,8 corriente + 44,8 no corriente, a 31/07/2026; fuera del cociente de deuda)


### Tipo de negocio y motor

    Fabricante industrial de ventilación y calidad del aire (ensamblaje ligero en capital), con exposición moderada al ciclo de la construcción y crecimiento reciente por adquisiciones financiadas con deuda.
    El DCF de caja libre al accionista de la plantilla, con crecimientos orgánicos y no extrapolando el crecimiento comprado, contrastado con la caja de ciclo medio por la exposición a la construcción.

### calidad

    Es un negocio comprensible, con ROIC del 25,4% y margen operativo ajustado del 23,2% en expansión, y más de 20.000 clientes sin ninguno por encima del 10%; pero el 73% del crecimiento de FY22-FY26 se compró y el fondo de comercio es el 40,4% del activo, por lo que el «DESCARTAR · demasiado difícil» de Análisis!A6 refleja C13 = No y no una falta de comprensión del negocio.
    Dato clave: Análisis!C24 = 0.254

### caja

    La caja libre del accionista, después de intereses, arrendamientos y SBC, es positiva y creciente (base de 64,8 de media FY24-FY26 y 80,0 antes de SBC en FY26, desde 28,8 en FY22), con un capex de 8,2 y una conversión CFO/beneficio neto de 1,72, aunque parte del crecimiento procede del circulante y de las compras.
    Dato clave: Análisis!C52 = 64.842

### balance

    Sin arrendamientos, la deuda neta de 184,2 equivale a unas 1,55x el EBITDA ya neto de alquiler (128,1 menos 9,1 de pagos por arrendamiento de FY26, unos 119,0; cálculo mío) y a unas 2,8 veces la caja libre base de 64,8, con covenant de 3,0x y el único préstamo, un revolving, ampliado tras el cierre hasta sep-2029; el 1,84x de Análisis!C33 incluye arrendamientos y no sirve tal cual, y no recoge los £34m dispuestos para getAir.
    Dato clave: Control maestro!N36 = 184.2 (deuda neta sin arrendamientos a 31/07/2026)

### precio

    La cotización de 6,25 está claramente por encima del precio de Sí de ~4,52 (el menor entre el escenario malo de 4,52 y 0,75 × 6,49 de ponderado = 4,87) y casi en el escenario normal de 6,33; con r ±1 punto el precio de Sí estimado (~4,0-5,2) sigue muy por debajo.
    Dato clave: Análisis!C37 = 6.25

### encaje

    El paquete no trae la cartera de la persona responsable; solo consta una capitalización de 1.237,8 £m, que no permite juzgar el encaje.
    Dato clave: Análisis!C41 = 1237.82

### Qué lo cambiaría

    - Una cotización en torno a 4,52 £ o por debajo, con la tesis intacta (pasaría a estudiar_a_fondo).
    - Un deterioro del fondo de comercio de Australasia o un orgánico negativo dos años sin recesión (pondría en duda calidad y caja).
    - Otra compra grande que lleve la deuda neta sin arrendamientos por encima de unas 2,5x el EBITDA neto de alquiler (balance no_pasa).

### Qué falta

    - No hay un EBITDA pre-NIIF 16 publicado: el EBITDA neto de alquiler (~119,0) lo calculo restando los 9,1 de pagos por arrendamiento de FY26.
    - No se publican el retorno por adquisición (ROAI) ni la sensibilidad del test de deterioro de Australasia (51% del fondo de comercio).
    - Control maestro cita decisiones del inversor del 8-nov-2026, posteriores a la fecha de la hoja (26/10/2026), y la deuda posterior a getAir no figura en el balance.

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

