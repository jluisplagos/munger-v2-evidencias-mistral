# Cribado · Rovi

Estado de la ejecución: `AUDITORIA_DOCUMENTAL_PENDIENTE_ACEPTACION`

Cribado pendiente de revisión humana. No es una recomendación de compra, ni aceptación, ni aptitud para dinero real. Tasa 9 % provisional.

C-ARR (decisión de la persona responsable): los arrendamientos se cuentan una sola vez, en el flujo. El alquiler se resta de la caja libre; la deuda, deuda/EBITDA y deuda/caja libre se miden sin arrendamientos; el pasivo por arrendamientos se muestra aparte, como dato.

Cifras de la etapa 1 tal como las guardó la hoja, a su fecha de análisis; sin las decisiones posteriores (P-O1, P-O2, F1-A/F1-B, D-US1/2, D-WM) ni verificación contra la fuente oficial.

| Campo | Valor |
|---|---|
| Fecha de la hoja | 2026-11-07 |
| Tarea | cribado-44512238939-rovi |
| SHA del código | 833cd50a9bba34006519119c72a29c70a1656fb7 |
| Huella del paquete (package_sha256) | 91944cbedb989312a33223c5c0baeb0f378974b5ac7f816242d5cbb525eeeaec |
| Huella del envío (bundle_sha256) | c3052db7037f6fe45ce98c4a8da37ee0d17c083c4eaf4877140710114b7d3113 |
| Huella del encargo | 32b5c7f313e61a61fb0f5e68a75b3c44004eb902e97b98720fb98fa8d383e6cf |
| Huella de la Release | 4d30f7352948fe7e7fe3b133386eabedbddcc71d997e972a1c6db7964d58b0a9 |
| Huella del libro | dcdbd0c000c4f108dd2c6da35e378597db7be3a37df52c89fe330421b8950ad8 |
| Modelo pedido / devuelto | claude-opus-5-5 / claude-opus-5-5 |
| Esfuerzo | high |
| Gramática del servidor | True |
| Mensajes enviados | 1 |
| Cota de entrada antes de llamar | 140050 tokens |
| Reserva estimada antes de llamar | USD 1.21556 |
| Uso de tokens | entrada 63199, salida 3320 |
| Coste | CONOCIDO_ESTIMADO; estimado USD 0.319196; cota 0.319196 |

| id | ruta | sha256 | bytes |
|---|---|---|---|
| respuesta | EMPRESAS_LOTES_COMPLETOS/Rovi/Rovi_respuesta.md | 4f08c8c600742a7b586921ee58fc9bcac7722704d751f59d967e659e6611e45f | 36563 |
| hoja_analisis | EMPRESAS_LOTES_COMPLETOS/Rovi/Rovi_evaluada.xlsx#Análisis | 76aa41e7f901a3aa59e26e401f34b34ecf0cd064e6d5b9b417c9218dd66620bc | 24051 |
| hoja_control_maestro | EMPRESAS_LOTES_COMPLETOS/Rovi/Rovi_evaluada.xlsx#Control maestro | 1a204ba4b9fd78fcdef904fdda50ab66bff59412c62b37157b08a8afe3051aa6 | 58540 |

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

    Control maestro!M51 = 11.1 (pasivo por arrendamientos NIIF 16 incluido en la deuda financiera de 100,9 a 30/09/2026)


### Tipo de negocio y motor

    Farmacéutica de especialidades (heparinas, Okedi®) más fabricación de inyectables a terceros (CDMO), con ingresos por contratos de 3–5 años.
    El DCF de la plantilla, pero sobre una caja libre normalizada de ciclo medio (sin anticipos de Moderna ni subvenciones) y con escenarios ligados al llenado de la capacidad CDMO.

### calidad

    La mecánica se entiende (C11 = Sí), pero el ROCE del 23,5 % TTM viene de una etapa pandémica (8–16 % antes de la COVID), los márgenes se comprimen y un cliente llegó al 38 % de la facturación, así que la durabilidad de la ventaja queda por demostrar; por eso no lo trato como «no se entiende», a diferencia del cubo de la etapa 1.
    Dato clave: Análisis!C24 = 0.235

### caja

    La caja libre base es positiva (103,22 M€ de media 2021–25, 108,3 M€ TTM) y el CFO equivale a 1,03 veces el beneficio, aunque la serie está movida por los anticipos de Moderna y el capex sube de 55,5 a 79,7 M€ TTM.
    Dato clave: Análisis!C52 = 103.22

### balance

    Sin arrendamientos, la deuda neta es de unos 18,9 M€ (89,8 − 70,9 de caja, Análisis!C53 = 70.9), unas 0,08x el EBITDA ex-badwill neto de alquiler (≈224 M€) y unas 0,18x el FCF base de 103,22 M€. Es holgado incluso para un negocio con ingresos irregulares; el 0,13x de Análisis!C33 incluye arrendamientos y no se usa tal cual.
    Dato clave: Control maestro!N51 = deuda sin arrendamientos 89,8 (Análisis!C54 = 100.9 menos 11,1 de arrendamientos); deuda neta sin arrendamientos ≈18,9

### precio

    Con una cotización de 68,6 € frente a un valor ponderado de 42,90 €, un escenario malo de 21,20 € y un bueno de 68,96 €, está claramente por encima. Ni con r al 7 % (63,92 €, Análisis!C90) llega al precio, y el precio exige un crecimiento del FCF del 12,7 % anual.
    Dato clave: Análisis!C83 = 42.8975802327312

### encaje

    El paquete no trae la cartera; la hoja solo valora el precio actual en 68,6 € (Análisis!C37) y no dice nada concreto sobre el encaje.
    Dato clave: Análisis!C104 = sin dato de cartera utilizable (decisión de cartera de la etapa 1, no se hereda)

### Qué lo cambiaría

    - Una cotización por debajo de ≈21 € (escenario malo, Análisis!B78 = 21.2) o cerca del valor ponderado de ≈43 €.
    - Autorización y arranque del contrato de jeringas con un EBIT sin badwill ni subvención ≥23 % en 2026–2027.
    - Pérdida de un cliente CDMO grande sin reponerlo, o FCF repetible claramente inferior a 100 M€.

### Qué falta

    - Separar el margen CDMO del de heparinas propias, y las condiciones económicas de los contratos (Moderna, BMS, Roche, jeringas).
    - Una serie de FCF normalizada sin anticipos ni subvenciones, y el reparto del capex entre mantenimiento y crecimiento.
    - Control maestro cita decisiones del inversor del 11-nov-2026, posteriores a la fecha de la hoja (07/11/2026): hay que confirmar qué cifras son definitivas.

### Comprobaciones mecánicas y normalizaciones

    {
      "comprobaciones": {
        "avisos": [],
        "nota": "Comprobaciones mecánicas informativas: no acreditan la calidad económica."
      },
      "normalizaciones": []
    }

