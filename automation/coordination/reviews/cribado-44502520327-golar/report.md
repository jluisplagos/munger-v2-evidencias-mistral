# Cribado · Golar

Estado de la ejecución: `AUDITORIA_DOCUMENTAL_PENDIENTE_ACEPTACION`

Cribado pendiente de revisión humana. No es una recomendación de compra, ni aceptación, ni aptitud para dinero real. Tasa 9 % provisional.

C-ARR (decisión de la persona responsable): los arrendamientos se cuentan una sola vez, en el flujo. El alquiler se resta de la caja libre; la deuda, deuda/EBITDA y deuda/caja libre se miden sin arrendamientos; el pasivo por arrendamientos se muestra aparte, como dato.

Cifras de la etapa 1 tal como las guardó la hoja, a su fecha de análisis; sin las decisiones posteriores (P-O1, P-O2, F1-A/F1-B, D-US1/2, D-WM) ni verificación contra la fuente oficial.

| Campo | Valor |
|---|---|
| Fecha de la hoja | 27/10/2026 |
| Tarea | cribado-44502520327-golar |
| SHA del código | 833cd50a9bba34006519119c72a29c70a1656fb7 |
| Huella del paquete (package_sha256) | b5a3a7fc0329c520165a5e0b6ed68739a8948d51c8331f37a96faf0f388c26fb |
| Huella del envío (bundle_sha256) | e917aa33437b8403c5b14b70e7572a454af06b755df0dc730da95483213bd45d |
| Huella del encargo | 32b5c7f313e61a61fb0f5e68a75b3c44004eb902e97b98720fb98fa8d383e6cf |
| Huella de la Release | 4d30f7352948fe7e7fe3b133386eabedbddcc71d997e972a1c6db7964d58b0a9 |
| Huella del libro | e42fa75e38bd4580472c0973ede811958d57a16a0bfdd453a1830830b2aab725 |
| Modelo pedido / devuelto | claude-opus-5-5 / claude-opus-5-5 |
| Esfuerzo | high |
| Gramática del servidor | True |
| Mensajes enviados | 1 |
| Cota de entrada antes de llamar | 215777 tokens |
| Reserva estimada antes de llamar | USD 1.518468 |
| Uso de tokens | entrada 95829, salida 3812 |
| Coste | CONOCIDO_ESTIMADO; estimado USD 0.459556; cota 0.459556 |

| id | ruta | sha256 | bytes |
|---|---|---|---|
| respuesta | EMPRESAS_LOTES_COMPLETOS/Golar/Golar_respuesta.md | ce74011f5e701e66b2db636ec070d18491668fabf978894879190e13944ec869 | 59619 |
| hoja_analisis | EMPRESAS_LOTES_COMPLETOS/Golar/Golar_evaluada.xlsx#Análisis | ecacc01d94296854f97167cf3be939a9d595485d1427f60a40a7bb25a9a05501 | 24822 |
| hoja_control_maestro | EMPRESAS_LOTES_COMPLETOS/Golar/Golar_evaluada.xlsx#Control maestro | 806c54c23273c12e24f79b4e79fc1ba1e27d1ad30f4c486b613e703c59e1fcf8 | 109676 |

## Salida del modelo (datos, sin acciones ejecutables)

Veredicto `descartar` · DCF de la plantilla aplica: `no`

| Filtro | Resultado |
|---|---|
| calidad | dudoso |
| caja | no_pasa |
| balance | no_pasa |
| precio | no_aplica |
| encaje | no_aplica |

### Pasivo por arrendamientos (dato aparte)

    Control maestro!M36 = 6,7 mm$ de pasivo por arrendamiento operativo (oficinas, en texto); no hay arrendamiento financiero como arrendatario. El bareboat del Hilli se elimina en consolidación y su deuda bancaria de la VIE (179,8 mm$) ya está dentro de la deuda de Análisis!C54.


### Tipo de negocio y motor

    Infraestructura energética contratada: conversión, propiedad y operación de plantas flotantes de licuefacción de gas (FLNG) alquiladas a 20 años a tarifa fija con componente ligado a materias primas, en fase de fuerte inversión de crecimiento y con alta concentración de clientes.
    Valoración por activo o suma de partes: valor descontado al 9 % de las tarifas contratadas de cada FLNG hasta su vencimiento, desde su fecha de arranque, menos la deuda de cada activo, el minoritario y el capex pendiente.

### calidad

    El negocio se entiende (alquiler de unidades FLNG a 20 años con tarifa fija), pero el ROCE del 5,63% queda por debajo del 7,50% que paga por su deuda (10,65-12,13% sin obra en curso), con dos clientes que suponen el 97,4% de los ingresos del 1S2026, el 82% del backlog en SESA y márgenes comprimiéndose del 78,1% al 59,4%; los datos apuntan en las dos direcciones.
    Dato clave: Análisis!C24 = 0.0563

### caja

    El FCF base de la plantilla es −244,04 mm$ (CFO 308 − capex 544,4 − SBC 7,64), negativo en cinco de los seis últimos periodos (TTM −310,5 mm$) y financiado con deuda: en FY2025 la financiación aportó +841,1 mm$ netos y en el 1S2026 la caja cayó 307,0 mm$; además no hay desglose de capex de mantenimiento y unos ~84 mm$/año de principal del Hilli no pasan por el FCF.
    Dato clave: Análisis!C52 = -244.04

### balance

    La deuda neta sin arrendamientos de 1.804,9 mm$ es 4,93x un EBITDA de 366,1 mm$ que ya resta el alquiler (rango 4,43x-7,93x según bases y pro forma), con caja libre negativa, por lo que deuda/caja libre no es calculable y quedan ≈3.600-3.700 mm$ de capex comprometido frente a 870,5 mm$ de caja; es demasiada deuda para un negocio concentrado y en construcción, aunque la ratio de caja a deuda corta (3,46x) no presente un vencimiento inmediato.
    Dato clave: Análisis!C33 = 4.93 (deuda sin arrendamientos Análisis!C54 = 2675.4 − caja Análisis!C53 = 870.5 = deuda neta 1804.9 ÷ EBITDA 366.1 que ya resta el alquiler operativo)

### precio

    El DCF de la plantilla da valores negativos (ponderado −32,81 $/acción y escenario bueno −48,70 $, peor que el malo −22,71 $), así que no sirve para comparar con la cotización de 45,21 $; la sensibilidad a ±2 puntos de tasa no tiene valor calculado y haría falta una valoración por unidad con tarifas, fechas de COD, deuda de cada activo y minoritario.
    Dato clave: Análisis!C83 = -32.8102517225339

### encaje

    El paquete no trae la cartera de la persona responsable y la hoja solo aporta una capitalización de 4.615,8 mm$; este filtro no elimina.
    Dato clave: Análisis!C41 = 4615.8

### Qué lo cambiaría

    - Dos ejercicios completos con FCF del accionista positivo sin deuda nueva neta, con el Hilli-SESA y el MKII operando.
    - Deuda neta sin arrendamientos por debajo de ~4x el EBITDA, con el capex comprometido ya financiado.
    - Cobro verificado de SESA durante cuatro trimestres o garantía/escrow verificables, y el cuarto FLNG contratado a tarifa comparable.

### Qué falta

    - Desglose del capex entre mantenimiento y crecimiento: sin él no se conoce la caja libre sostenible de una flota FLNG en régimen.
    - Resultados del 3T 2026 y deuda pro forma tras los 500 mm$ de notas liquidados el 08-10-2026 y el RCF de 600 mm$, que no están en la cifra de deuda de la hoja.
    - Garantías, escrow o seguro que respalden el pago de SESA (82% del backlog) y una cotización de fuente primaria (la de 45,21 $ es secundaria).

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

