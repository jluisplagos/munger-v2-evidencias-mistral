# Cribado · Pandora

Estado de la ejecución: `AUDITORIA_DOCUMENTAL_PENDIENTE_ACEPTACION`

Cribado pendiente de revisión humana. No es una recomendación de compra, ni aceptación, ni aptitud para dinero real. Tasa 9 % provisional.

C-ARR (decisión de la persona responsable): los arrendamientos se cuentan una sola vez, en el flujo. El alquiler se resta de la caja libre; la deuda, deuda/EBITDA y deuda/caja libre se miden sin arrendamientos; el pasivo por arrendamientos se muestra aparte, como dato.

Cifras de la etapa 1 tal como las guardó la hoja, a su fecha de análisis; sin las decisiones posteriores (P-O1, P-O2, F1-A/F1-B, D-US1/2, D-WM) ni verificación contra la fuente oficial.

| Campo | Valor |
|---|---|
| Fecha de la hoja | 2026-10-25 |
| Tarea | cribado-44406828081-pandora |
| SHA del código | 833cd50a9bba34006519119c72a29c70a1656fb7 |
| Huella del paquete (package_sha256) | 689b65bf3b6a1ce201b24dc9e5e4bc74332006213a9f6402da10773ab57e2a6f |
| Huella del envío (bundle_sha256) | 61e334480fefd28cb02d329e74fbc0b246dea4a6bb3028f64e21d65ca9369e27 |
| Huella del encargo | 32b5c7f313e61a61fb0f5e68a75b3c44004eb902e97b98720fb98fa8d383e6cf |
| Huella de la Release | 4d30f7352948fe7e7fe3b133386eabedbddcc71d997e972a1c6db7964d58b0a9 |
| Huella del libro | 174f383005695e411f22b300e2fa505abee0ecc2dcc7b3c35dbb1b2af3dd8334 |
| Modelo pedido / devuelto | claude-opus-5-5 / claude-opus-5-5 |
| Esfuerzo | high |
| Gramática del servidor | True |
| Mensajes enviados | 1 |
| Cota de entrada antes de llamar | 131937 tokens |
| Reserva estimada antes de llamar | USD 1.183108 |
| Uso de tokens | entrada 59931, salida 5188 |
| Coste | CONOCIDO_ESTIMADO; estimado USD 0.343484; cota 0.343484 |

| id | ruta | sha256 | bytes |
|---|---|---|---|
| respuesta | EMPRESAS_LOTES_COMPLETOS/Pandora/Pandora_respuesta.md | bf39fabd4d3a3eda50ccaf9f46b129c094bb0e7cc1d7be122e7114544059fa53 | 33525 |
| hoja_analisis | EMPRESAS_LOTES_COMPLETOS/Pandora/Pandora_evaluada.xlsx#Análisis | a849c40a3d2d0d9791ce42fef534547b4ca1a9305f3d86b59783c85149c8efe6 | 23504 |
| hoja_control_maestro | EMPRESAS_LOTES_COMPLETOS/Pandora/Pandora_evaluada.xlsx#Control maestro | be783ff4152d438c517e172af4874ab93d569776911c829013535fd166ea8616 | 53912 |

## Salida del modelo (datos, sin acciones ejecutables)

Veredicto `vigilar` · DCF de la plantilla aplica: `si`

| Filtro | Resultado |
|---|---|
| calidad | dudoso |
| caja | pasa |
| balance | pasa |
| precio | no_pasa |
| encaje | no_aplica |

### Pasivo por arrendamientos (dato aparte)

    Control maestro!M51 = 6291 (pasivos por arrendamiento a 30/06/2026; fuera del cociente de deuda)


### Tipo de negocio y motor

    Marca de joyería de consumo accesible con fabricación propia y venta minorista en tiendas propias alquiladas, cuyo margen depende de la plata como materia prima.
    DCF de caja libre de la plantilla, pero con una trayectoria explícita del FCF (bache de margen en 2027 por la plata ya cubierta y recuperación con el chapado en platino) en lugar de una base plana de 4.828 mm.

### calidad

    El negocio se entiende (joyería de marca con margen bruto ~80 % y ROIC del 39 %, nunca por debajo del 20 % en 2015–25), pero el margen EBIT cae del 36,5 % (2016) al 23,9 % (2025), la empresa planifica ≥12–14 % para 2027 por la plata, el EBIT lleva nueve años plano (7.404 → 7.783), Moments (61 % de las ventas) tiene like-for-like negativo y la dirección es nueva; discrepo del «demasiado difícil» de la etapa 1, porque la incertidumbre es de valoración y no de comprensión del negocio.
    Dato clave: Análisis!C24 = 0.39

### caja

    El FCF al accionista, después de capex, de arrendamientos y de SBC, fue positivo todos los años 2021–25 (4.652 / 2.175 / 4.789 / 5.880 / 4.190; LTM 4.896), con una conversión CFO/beneficio neto de 1,4 (Análisis!C26) y una base normalizada de 4.828 mm; no crece y 2027 se estima más bajo, pero la conversión es recurrente.
    Dato clave: Análisis!C52 = 4828

### balance

    Sin arrendamientos, la deuda neta de 9.352 mm (10.260 − 908) equivale a unas 1,08x el EBITDA LTM después de alquiler (10.420 − 1.333 de principal − 431 de intereses de arrendamientos ≈ 8.656, en línea con el 1,08–1,10x aproximado de la hoja) y a 1,9x la caja libre base de 4.828, con 6.721 mm de líneas comprometidas sin disponer; es holgado para una marca de consumo aunque con el FCF estimado para 2027 (2.400–2.900) subiría a ~3,5x, y el 1,5x de Análisis!C33 no sirve tal cual porque incluye arrendamientos.
    Dato clave: Control maestro!M51: deuda financiera sin arrendamientos = 10260 (menos caja Análisis!C53 = 908 → deuda neta 9352)

### precio

    La cotización de 822 DKK está claramente por encima del escenario malo (530,5) y de ¾ del ponderado (≈763 sobre 1.017,5); el DCF inverso exige solo un 0,24 % de crecimiento, pero con r al 11 % el ponderado baja a 784 y con el FCF estimado para 2027 el P/FCF sería de 21–25x, así que no hay margen suficiente.
    Dato clave: Análisis!C37 = 822 frente a Análisis!B78 = 530.543538038958

### encaje

    El paquete no trae la cartera de la persona responsable y la hoja solo recoge un tamaño de posición de etapa 1 (0 %), que no se usa como conclusión.
    Dato clave: Análisis!C104 = 0% · Demasiado difícil · sin posición (dato de etapa 1, no heredado)

### Qué lo cambiaría

    - Una cotización en torno a 530 DKK o por debajo (escenario malo, Análisis!B78) llevaría a estudiar a fondo.
    - Que la actualización del 04/11/2026 o los datos de 2027 muestren un margen EBIT por debajo del 12 %, o un like-for-like de Core negativo con el platino ya en tienda (pérdida de marca), llevaría a descartar.
    - Que la deuda financiera siga subiendo para pagar recompras hasta superar ~2,5x el EBITDA después de alquiler haría que el balance no pasara.

### Qué falta

    - Resultados del tercer trimestre de 2026 y actualización estratégica del 04/11/2026 con el margen EBIT de 2027: son posteriores a la fecha de corte y la hoja pide revisarla tras ellos.
    - El EBITDA después de alquileres no figura como cifra en la hoja (solo la aproximación de 1,08–1,10x) y falta el calendario completo de vencimientos de la deuda financiera de 10.260 mm.
    - Dudas sobre las fuentes: Control maestro (C43–C46) cita una «decisión del inversor (1-nov-2026)», posterior a la fecha de la hoja (25/10/2026), y el FCF de 2027 (2.400–2.900) es una estimación de la fase 1, no un dato publicado.

### Comprobaciones mecánicas y normalizaciones

    {
      "comprobaciones": {
        "avisos": [
          "Filtro calidad: motivo de más de 400 caracteres.",
          "Filtro balance: motivo de más de 400 caracteres.",
          "Un texto menciona un tamaño de posición o un porcentaje de cartera."
        ],
        "nota": "Comprobaciones mecánicas informativas: no acreditan la calidad económica."
      },
      "normalizaciones": []
    }

