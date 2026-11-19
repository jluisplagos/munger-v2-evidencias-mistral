# Cribado · Quanta

Estado de la ejecución: `AUDITORIA_DOCUMENTAL_PENDIENTE_ACEPTACION`

Cribado pendiente de revisión humana. No es una recomendación de compra, ni aceptación, ni aptitud para dinero real. Tasa 9 % provisional.

C-ARR (decisión de la persona responsable): los arrendamientos se cuentan una sola vez, en el flujo. El alquiler se resta de la caja libre; la deuda, deuda/EBITDA y deuda/caja libre se miden sin arrendamientos; el pasivo por arrendamientos se muestra aparte, como dato.

Cifras de la etapa 1 tal como las guardó la hoja, a su fecha de análisis; sin las decisiones posteriores (P-O1, P-O2, F1-A/F1-B, D-US1/2, D-WM) ni verificación contra la fuente oficial.

| Campo | Valor |
|---|---|
| Fecha de la hoja | 2026-10-17 |
| Tarea | cribado-44509331308-quanta |
| SHA del código | 833cd50a9bba34006519119c72a29c70a1656fb7 |
| Huella del paquete (package_sha256) | 4aeefebb52bf335c7a41013c496d465ade6fe113e597be08bf2283b31f8ee4aa |
| Huella del envío (bundle_sha256) | f543f0e8e6f9dc42878c6c55c09c3a8db76ca76cc34a93f2945e12298316ecbc |
| Huella del encargo | 32b5c7f313e61a61fb0f5e68a75b3c44004eb902e97b98720fb98fa8d383e6cf |
| Huella de la Release | 4d30f7352948fe7e7fe3b133386eabedbddcc71d997e972a1c6db7964d58b0a9 |
| Huella del libro | d8c040cc53da46de9db21f8a6bb0c03cfbe0a4f7c2bcff10e003bf75d129ec61 |
| Modelo pedido / devuelto | claude-opus-5-5 / claude-opus-5-5 |
| Esfuerzo | high |
| Gramática del servidor | True |
| Mensajes enviados | 1 |
| Cota de entrada antes de llamar | 144637 tokens |
| Reserva estimada antes de llamar | USD 1.233908 |
| Uso de tokens | entrada 66111, salida 4063 |
| Coste | CONOCIDO_ESTIMADO; estimado USD 0.345704; cota 0.345704 |

| id | ruta | sha256 | bytes |
|---|---|---|---|
| respuesta | EMPRESAS_LOTES_COMPLETOS/Quanta/Quanta_respuesta.md | 0be1cd01244c6ca8be215552445ef88b368ce02fe1a4f277efde812047afe1ac | 36438 |
| cambios_v2 | EMPRESAS_LOTES_COMPLETOS/Quanta/Quanta_cambios_v2.md | a09651d353be710c1a74ecdbd80e3d5bdcaa9c71f32b99d0bf05a16bb73b4509 | 5272 |
| hoja_analisis | EMPRESAS_LOTES_COMPLETOS/Quanta/Quanta_evaluada.xlsx#Análisis | 170c9fc2dcf4165a5e9702da2f28bb9911bdee5af14a1a27455a8f54c818ed13 | 23708 |
| hoja_control_maestro | EMPRESAS_LOTES_COMPLETOS/Quanta/Quanta_evaluada.xlsx#Control maestro | d9a4b84532dbcf17ec2f4ccc5488c0e6340d194447cda5c28a354ee005685525 | 58058 |

## Salida del modelo (datos, sin acciones ejecutables)

Veredicto `vigilar` · DCF de la plantilla aplica: `dudoso`

| Filtro | Resultado |
|---|---|
| calidad | dudoso |
| caja | pasa |
| balance | pasa |
| precio | no_pasa |
| encaje | no_aplica |

### Pasivo por arrendamientos (dato aparte)

    Arrendamientos operativos ≈ 498,3 M USD (Control maestro!N36; 6.603,1 − 6.104,9 según Control maestro!N51) más finance leases de 38,9 M USD (Control maestro!M51), fuera del cociente de deuda.


### Tipo de negocio y motor

    Contratista especializado de infraestructura eléctrica y subterránea (transmisión, distribución, subestaciones, gas, centros de datos), cíclico y por contratos, en gran parte a precio fijo, con crecimiento apoyado en adquisiciones.
    Caja libre de ciclo medio normalizada (con años de bache como 2015 y 2020) y restando el gasto recurrente en adquisiciones que alimenta el crecimiento, contrastada con el DCF de la plantilla.

### calidad

    El negocio se entiende (C11 = Sí, así que no lo trato como «demasiado difícil», a diferencia de la etiqueta A6 de la hoja), pero la ventaja no se ve clara: el ROIC con fondo de comercio es de 11,2 %, apenas por encima del 9 %, con margen operativo del 5-6 % y la empresa admite pocas barreras de entrada, frente a un ROIC tangible del 35,8 % y una cartera de 53.440 M USD que apuntan a lo contrario.
    Dato clave: Análisis!C24 = 0.112

### caja

    La caja libre base tras SBC es positiva, de 1.251,7 M USD, la conversión CFO/beneficio es de 2,04x (C26) y el capex ronda el 2 % de las ventas, aunque 2021-2025 gastó 8.096 M USD en adquisiciones frente a 5.138 M USD de caja libre, de modo que parte del crecimiento está comprado.
    Dato clave: Análisis!C52 = 1251.7

### balance

    Sin arrendamientos la deuda neta es ≈ 1,81x el EBITDA LTM US GAAP, que ya resta el alquiler operativo (1,83x en C33 con 38,9 de finance leases), razonable para un contratista cíclico, aunque la caja no cubre la deuda a corto (0,74x en C34) y tras el balance hubo notes por 2.000 M USD y la operación de Enerfab, de importe no verificado.
    Dato clave: Análisis!C54 = 6104.9 (menos 38,9 de finance leases según Control maestro!M51 → deuda sin arrendamientos ≈ 6.066,0; deuda neta ≈ 5.559,6 ÷ EBITDA LTM 3.066,2 ≈ 1,81x; Análisis!C33 = 1.83)

### precio

    La cotización de 631,86 USD está unas 5,5 veces por encima del precio de Sí (≈115,26 = mín(115,26; 0,75 × 211,24)) y unas 3 veces por encima del ponderado, por lo que queda claramente por encima incluso con r = 7 % (318,46 en C90), aunque el DCF de la plantilla sea discutible para un cíclico: el precio exige un 23,6 % anual de crecimiento (C86).
    Dato clave: Análisis!C37 = 631.86 frente a Análisis!B78 = 115.26 y Análisis!C83 = 211.24

### encaje

    El paquete no trae la cartera de la persona responsable y la hoja solo da datos de la empresa (capitalización de 94.996 M USD), así que este filtro no aplica ni elimina.
    Dato clave: Análisis!C41 = 94996

### Qué lo cambiaría

    - Una cotización cercana o inferior al valor ponderado de la hoja (~211 USD) llevaría el caso a estudiar a fondo.
    - Que el importe de Enerfab u otras compras eleve la deuda neta sin arrendamientos por encima de ~2,5x el EBITDA, lo que haría fallar el balance.
    - Que los 983,6 M USD de reclamaciones no aprobadas acaben en pérdidas relevantes, lo que rebajaría calidad y caja.

### Qué falta

    - Importe de la operación de Enerfab y su efecto en deuda y EBITDA tras el balance de 30/06/2026, junto con las notes de 2.000 M USD.
    - Resultados del 3T2026, previstos el 29/10/2026 y posteriores a la fecha de la hoja, para actualizar LTM, deuda y precio.
    - Serie larga de retorno sobre capital tangible y de crecimiento orgánico que muestre el comportamiento en los baches (2015, 2020).

### Comprobaciones mecánicas y normalizaciones

    {
      "comprobaciones": {
        "avisos": [],
        "nota": "Comprobaciones mecánicas informativas: no acreditan la calidad económica."
      },
      "normalizaciones": []
    }

