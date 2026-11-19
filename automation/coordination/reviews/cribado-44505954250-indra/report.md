# Cribado · Indra

Estado de la ejecución: `AUDITORIA_DOCUMENTAL_PENDIENTE_ACEPTACION`

Cribado pendiente de revisión humana. No es una recomendación de compra, ni aceptación, ni aptitud para dinero real. Tasa 9 % provisional.

C-ARR (decisión de la persona responsable): los arrendamientos se cuentan una sola vez, en el flujo. El alquiler se resta de la caja libre; la deuda, deuda/EBITDA y deuda/caja libre se miden sin arrendamientos; el pasivo por arrendamientos se muestra aparte, como dato.

Cifras de la etapa 1 tal como las guardó la hoja, a su fecha de análisis; sin las decisiones posteriores (P-O1, P-O2, F1-A/F1-B, D-US1/2, D-WM) ni verificación contra la fuente oficial.

| Campo | Valor |
|---|---|
| Fecha de la hoja | 2026-10-17 |
| Tarea | cribado-44505954250-indra |
| SHA del código | 833cd50a9bba34006519119c72a29c70a1656fb7 |
| Huella del paquete (package_sha256) | f5b3dc2311b1cef0600317701ae11a74ee903f737d3c902c4df3eb75e4a764ff |
| Huella del envío (bundle_sha256) | 4770e8464a17bec87be1f4a2a9b8bb6575a45b54dcd2f9e86d7d84238747808b |
| Huella del encargo | 32b5c7f313e61a61fb0f5e68a75b3c44004eb902e97b98720fb98fa8d383e6cf |
| Huella de la Release | 4d30f7352948fe7e7fe3b133386eabedbddcc71d997e972a1c6db7964d58b0a9 |
| Huella del libro | 706c77fc3a66321eac0e8c9c136800e85f161d356477662af3b1a58be489c1af |
| Modelo pedido / devuelto | claude-opus-5-5 / claude-opus-5-5 |
| Esfuerzo | high |
| Gramática del servidor | True |
| Mensajes enviados | 1 |
| Cota de entrada antes de llamar | 137085 tokens |
| Reserva estimada antes de llamar | USD 1.2037 |
| Uso de tokens | entrada 63234, salida 5284 |
| Coste | CONOCIDO_ESTIMADO; estimado USD 0.358616; cota 0.358616 |

| id | ruta | sha256 | bytes |
|---|---|---|---|
| respuesta | EMPRESAS_LOTES_COMPLETOS/Indra/Indra_respuesta.md | d1c3007e59a61a25e481144fe1af52aa1ca5a416c730242bd8dd048f22807b38 | 31064 |
| cambios_v2 | EMPRESAS_LOTES_COMPLETOS/Indra/Indra_cambios_v2.md | 5453e1cb7b95072269045a1c39e7f6a47e4f32043cf64bf63412c75291830f83 | 4029 |
| hoja_analisis | EMPRESAS_LOTES_COMPLETOS/Indra/Indra_evaluada.xlsx#Análisis | dee8da4bc1c4d67145cafd9c017e069f351650c314834dd1b5f557b14c6e07a0 | 23100 |
| hoja_control_maestro | EMPRESAS_LOTES_COMPLETOS/Indra/Indra_evaluada.xlsx#Control maestro | 6bbdbf61450d280ff0b1528cb23abeca575e9ef3d5de14a827a08106dbb0ba82 | 57911 |

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

    Control maestro!M51 = 168.1 (pasivo por arrendamientos a 30/06/2026; de ellos 30.9 a corto plazo según Control maestro!M37)


### Tipo de negocio y motor

    Contratista de defensa, tráfico aéreo, espacio y movilidad, con servicios de TI (Minsait), que trabaja por proyectos sobre todo para administraciones públicas; ligado al ciclo de gasto en defensa y con un perímetro en transformación por adquisiciones.
    DCF de caja libre con el FCF recurrente del nuevo perímetro (Hispasat, Tess) separando los anticipos PEM, o suma de partes Defensa/Espacio/Minsait, contrastado con una caja de ciclo medio del gasto en defensa.

### calidad

    El negocio se entiende y el margen EBIT sube del 6,4 % al 9,5 %, con un ROCE después de impuestos de 0,17, pero este baja a 0,115/0,09 si los anticipos MINETUR se tratan como deuda; además Minsait (57 % de las ventas) gana un 6,6 %, no hay foso ni competidores identificados, el valor depende del gasto público en defensa y el gobierno corporativo está en relevo.
    Dato clave: Análisis!C24 = 0.17

### caja

    El FCF base es de 252,6 M€ y la serie 2021-2025 sube de 289 a 364 M€, pero la conversión de 1,63 (C26, ✓ PASA en la etapa 1) se apoya en anticipos de clientes (34 % del CFO; 1,08 sin ellos) y el FCF LTM sin PEM y con factoring constante es de −16,3 M€ con un capex de 305,3 M€ ligado a Hispasat, así que la caja recurrente del nuevo perímetro está por demostrar.
    Dato clave: Análisis!C52 = 252.6

### balance

    Sin arrendamientos, la deuda financiera es de 1.459,2 M€ frente a una caja de 2.473,5 M€, es decir, caja neta; aun tratando los anticipos PEM (1.909,1 M€) como deuda, la deuda neta sería de unos 894,8 M€, ≈1,1x el EBITDA pre-NIIF 16 estimado de 788,2 M€ (no publicado), por debajo del 1,28 de C33, que incluye arrendamientos; los vencimientos se concentran en 2029 (680,2 M€) y la caja cubre 2,2x la deuda a corto plazo en lectura conservadora, aunque sumando los anticipos TESS y PAZ el cociente subiría a ≈3,2x.
    Dato clave: Control maestro!M51 = 1459.2 (deuda financiera sin arrendamientos; Análisis!C54 = 1627.3 incluye 168.1 de arrendamientos)

### precio

    A 63,68 € la cotización supera incluso el escenario bueno (58,46 €), el ponderado (35,47 €) y el malo (20,25 €, en línea con el precio de Sí de ≈20,3 € de la respuesta); con r al 7 % el ponderado solo llega a 51,9 €, el precio exige un crecimiento del 16,8 % anual y cotiza a 41,8x FCF frente a una mediana histórica de 10,2x, de modo que, aunque el DCF de la plantilla sea dudoso por los PEM, todas las medidas apuntan a caro.
    Dato clave: Análisis!D78 = 58.4641861537762

### encaje

    El paquete no trae la cartera de la persona responsable y la hoja solo da datos de la empresa (capitalización de 11.152 M€), así que no se puede juzgar el encaje.
    Dato clave: Análisis!C41 = 11152

### Qué lo cambiaría

    - Una cotización por debajo del valor ponderado de la hoja (≈35,5 €), y más aún cerca del escenario malo (≈20,2 €), con el negocio intacto.
    - Un FCF de 2026 sin PEM y con factoring constante por debajo de los 364 M€ de 2025, que haría no pasar la caja y llevaría a descartar.
    - El cierre de la operación con EM&E en términos favorables a consejeros en conflicto, o un ROCE ≥15 % sostenido con los anticipos tratados como deuda.

### Qué falta

    - EBITDA pre-NIIF 16 publicado: el 788,2 M€ es una estimación, y también falta el calendario de compensación de los 3.516,1 M€ de anticipos MINETUR (PEM, TESS y PAZ).
    - FCF recurrente del nuevo perímetro (Hispasat, Tess) sin anticipos PEM y crecimiento orgánico separado de las adquisiciones.
    - Competidores y cuotas por segmento para juzgar el foso; la etapa 1 concluyó «demasiado difícil», pero por su propia respuesta el negocio sí se entiende, así que aquí se trata como duda de calidad.

### Comprobaciones mecánicas y normalizaciones

    {
      "comprobaciones": {
        "avisos": [
          "Filtro balance: motivo de más de 400 caracteres.",
          "Filtro precio: motivo de más de 400 caracteres."
        ],
        "nota": "Comprobaciones mecánicas informativas: no acreditan la calidad económica."
      },
      "normalizaciones": []
    }

