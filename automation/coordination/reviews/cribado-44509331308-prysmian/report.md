# Cribado · Prysmian

Estado de la ejecución: `AUDITORIA_DOCUMENTAL_PENDIENTE_ACEPTACION`

Cribado pendiente de revisión humana. No es una recomendación de compra, ni aceptación, ni aptitud para dinero real. Tasa 9 % provisional.

C-ARR (decisión de la persona responsable): los arrendamientos se cuentan una sola vez, en el flujo. El alquiler se resta de la caja libre; la deuda, deuda/EBITDA y deuda/caja libre se miden sin arrendamientos; el pasivo por arrendamientos se muestra aparte, como dato.

Cifras de la etapa 1 tal como las guardó la hoja, a su fecha de análisis; sin las decisiones posteriores (P-O1, P-O2, F1-A/F1-B, D-US1/2, D-WM) ni verificación contra la fuente oficial.

| Campo | Valor |
|---|---|
| Fecha de la hoja | 2026-10-09 |
| Tarea | cribado-44509331308-prysmian |
| SHA del código | 833cd50a9bba34006519119c72a29c70a1656fb7 |
| Huella del paquete (package_sha256) | f3d5ac33f13068a1500131586d957402f399c987eeaa64bc901f644995a2e3e3 |
| Huella del envío (bundle_sha256) | 0bdbd4965be92e7a7c64135dd632051d3c1e7d2e2a29b33b882b2340717f838e |
| Huella del encargo | 32b5c7f313e61a61fb0f5e68a75b3c44004eb902e97b98720fb98fa8d383e6cf |
| Huella de la Release | 4d30f7352948fe7e7fe3b133386eabedbddcc71d997e972a1c6db7964d58b0a9 |
| Huella del libro | 1e078a6c75f97ef9069bd7a073a26965c87c5c1539d3cd42d341b7179629dd43 |
| Modelo pedido / devuelto | claude-opus-5-5 / claude-opus-5-5 |
| Esfuerzo | high |
| Gramática del servidor | True |
| Mensajes enviados | 1 |
| Cota de entrada antes de llamar | 139721 tokens |
| Reserva estimada antes de llamar | USD 1.214244 |
| Uso de tokens | entrada 63133, salida 5509 |
| Coste | CONOCIDO_ESTIMADO; estimado USD 0.362712; cota 0.362712 |

| id | ruta | sha256 | bytes |
|---|---|---|---|
| respuesta | EMPRESAS_LOTES_COMPLETOS/Prysmian/Prysmian_respuesta.md | 5a0df257d37214391031f843b4279a42fa162e369c1acd025ee1293581ac1088 | 35612 |
| cambios_v2 | EMPRESAS_LOTES_COMPLETOS/Prysmian/Prysmian_cambios_v2.md | c15a2fca0513b4bec5db4c7f2487f80b5e723afd72bad0aadd45ff98e2a28aef | 4671 |
| hoja_analisis | EMPRESAS_LOTES_COMPLETOS/Prysmian/Prysmian_evaluada.xlsx#Análisis | 0f870f9aafdd7558b6636f1ee95b6fbd7bc973ae063536739498e51cc6f4da28 | 22874 |
| hoja_control_maestro | EMPRESAS_LOTES_COMPLETOS/Prysmian/Prysmian_evaluada.xlsx#Control maestro | 703e0c40f9f08819f249e5785ee0ee6c4911b7fb862a2054495cf6756704c91b | 55473 |

## Salida del modelo (datos, sin acciones ejecutables)

Veredicto `vigilar` · DCF de la plantilla aplica: `dudoso`

| Filtro | Resultado |
|---|---|
| calidad | dudoso |
| caja | pasa |
| balance | dudoso |
| precio | no_pasa |
| encaje | no_aplica |

### Pasivo por arrendamientos (dato aparte)

    ≈ 399 mm a 31/12/2025: Análisis!C54 = 5208 (deuda con arrendamientos) menos 4.809 sin arrendamientos (Control maestro!M51); de ellos, 108 mm corrientes (Control maestro!M37).


### Tipo de negocio y motor

    Industrial cíclico: fabricación e instalación de cables de energía y telecomunicaciones, con una parte de proyectos plurianuales (Transmission, cartera de 15,1 mil mm) y otra ligada a la construcción y a los metales (Electrification, 55,8 % de las ventas).
    Caja libre de ciclo medio (márgenes normalizados entre el 8–9 % de 2016–2021 y el 12 % actual, sin circulante ni anticipos extraordinarios), recalculada con el perímetro proforma de Atkore (deuda, acciones y FCF a la vez), contrastada con los múltiplos de los pares.

### calidad

    El negocio se entiende (Análisis!C11 = Sí) y el ROCE es del 16,9 % antes de impuestos (≈ 13 % después); pero el margen EBITDA ajustado récord del 12,2 % en 2025 contrasta con el 6,9–9,4 % de 2016–2021, la empresa reconoce productos intercambiables y que el precio es clave, y la ventaja solo se ve en Transmission (≈ 17 % de ventas); por eso no veo calidad probada a lo largo del ciclo, aunque, a diferencia de la etapa 1, no lo trato como «demasiado difícil».
    Dato clave: Análisis!C24 = 0.169

### caja

    La caja libre base es de 767 mm después de intereses, principal de arrendamientos y SBC, y la conversión CFO/beneficio es de 2,15x (2,41x sin YOFC), con caja libre positiva todos los años 2016–2025; matiz: 857 mm de circulante a favor en 2023–2025 y anticipos de clientes inflan la cifra, y el LTM a junio de 2026 (759–772 mm) apenas supera la base.
    Dato clave: Análisis!C52 = 767

### balance

    Sin arrendamientos, la deuda neta a diciembre de 2025 es ≈ 1,23x el EBITDA que ya resta el alquiler (2.398 − 209), lo que pasaría incluso para un negocio cíclico; sin embargo, la compra de Atkore, todavía sin cerrar, lleva la deuda proforma estimada a ≈ 2,5x (no consta si esa cifra incluye arrendamientos), el LTM a junio de 2026 ya está en 1,57x con arrendamientos y hay un híbrido de 1.000 contado como patrimonio, por lo que discrepo del ✓ PASA de la hoja (1,29x con NIIF 16).
    Dato clave: Control maestro!M51 = 4809 (deuda bruta sin arrendamientos); deuda neta sin arrendamientos ≈ 2.698 / EBITDA tras alquiler 2.189 = 1,23x (Control maestro!N36)

### precio

    A 123,2 € la cotización multiplica por ≈ 2,4 el valor ponderado (51,87 €) y supera incluso el escenario bueno (72,95 €) y el ponderado con r al 7 % (74,71 €); el precio implica un crecimiento de la caja libre del 17,7 % anual y un rendimiento FCF del 2,3 %, por debajo de la tasa sin riesgo del 3,48 %, y un motor de ciclo medio, con márgenes más bajos, daría todavía menos valor.
    Dato clave: Análisis!C83 = 51.8678714229004

### encaje

    El paquete no trae la cartera de la persona responsable y la hoja solo da contexto de tamaño (capitalización de 36.870 mm), así que este filtro no elimina.
    Dato clave: Análisis!C41 = 36870

### Qué lo cambiaría

    - Una cotización cerca o por debajo del valor ponderado de ≈ 52 € (Análisis!C83), o del escenario malo de ≈ 32 € (Análisis!B78), llevaría el caso a estudiar_a_fondo.
    - Un cierre de Atkore con la deuda neta sin arrendamientos por encima de ≈ 2,5x el EBITDA tras alquiler haría que el balance no pase y llevaría a descartar.
    - Una serie de ROCE después de impuestos por encima del 13–15 % que atraviese un ciclo bajo, con márgenes que no vuelvan al 8–9 %, haría que la calidad pase.

### Qué falta

    - Cifras proforma de Atkore al cierre (deuda neta, EBITDA, FCF y acciones con el mismo perímetro), y si el ≈ 2,5x estimado incluye arrendamientos.
    - Serie de ROCE y márgenes a lo largo de un ciclo bajo, y FCF de ciclo medio sin el efecto del circulante ni de los anticipos de clientes (pasivos contractuales de 2.325 mm).
    - La respuesta v2 está fechada el 25-oct-2026, después de la fecha de la hoja (09/10/2026); además, el cupón anualizado del híbrido (52,5 mm) no está en la base, que quedaría en ≈ 715 mm.

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

