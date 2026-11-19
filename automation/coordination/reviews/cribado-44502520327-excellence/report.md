# Cribado · Excellence

Estado de la ejecución: `AUDITORIA_DOCUMENTAL_PENDIENTE_ACEPTACION`

Cribado pendiente de revisión humana. No es una recomendación de compra, ni aceptación, ni aptitud para dinero real. Tasa 9 % provisional.

C-ARR (decisión de la persona responsable): los arrendamientos se cuentan una sola vez, en el flujo. El alquiler se resta de la caja libre; la deuda, deuda/EBITDA y deuda/caja libre se miden sin arrendamientos; el pasivo por arrendamientos se muestra aparte, como dato.

Cifras de la etapa 1 tal como las guardó la hoja, a su fecha de análisis; sin las decisiones posteriores (P-O1, P-O2, F1-A/F1-B, D-US1/2, D-WM) ni verificación contra la fuente oficial.

| Campo | Valor |
|---|---|
| Fecha de la hoja | 25.10.2026 |
| Tarea | cribado-44502520327-excellence |
| SHA del código | 833cd50a9bba34006519119c72a29c70a1656fb7 |
| Huella del paquete (package_sha256) | 2e90ff681c61c70ba6187a46bcdafc868f2873ef131c7d3141a1177d5aace547 |
| Huella del envío (bundle_sha256) | c4d2338a12eb0c6bb043de4f63d9506a9386c8a315536569e072fca03cd2c95e |
| Huella del encargo | 32b5c7f313e61a61fb0f5e68a75b3c44004eb902e97b98720fb98fa8d383e6cf |
| Huella de la Release | 4d30f7352948fe7e7fe3b133386eabedbddcc71d997e972a1c6db7964d58b0a9 |
| Huella del libro | 06233b0b69af76050bbb6a75b657a2727d0b1f84b0f9a93cca7972f4ecd3d729 |
| Modelo pedido / devuelto | claude-opus-5-5 / claude-opus-5-5 |
| Esfuerzo | high |
| Gramática del servidor | True |
| Mensajes enviados | 1 |
| Cota de entrada antes de llamar | 150140 tokens |
| Reserva estimada antes de llamar | USD 1.25592 |
| Uso de tokens | entrada 68738, salida 4103 |
| Coste | CONOCIDO_ESTIMADO; estimado USD 0.357012; cota 0.357012 |

| id | ruta | sha256 | bytes |
|---|---|---|---|
| respuesta | EMPRESAS_LOTES_COMPLETOS/Excellence/Excellence_respuesta.md | d5669a888bf1fadc1e37457a63f7cf8c2c2e0988be11f145aa17734538accebe | 42865 |
| hoja_analisis | EMPRESAS_LOTES_COMPLETOS/Excellence/Excellence_evaluada.xlsx#Análisis | 922350c5d7991bfaafc969a72f93fdc4a79413f6c356c3366eebdb75611dc56a | 23601 |
| hoja_control_maestro | EMPRESAS_LOTES_COMPLETOS/Excellence/Excellence_evaluada.xlsx#Control maestro | d35eb0b57c2793f1c3e6956cbe5422c901738eac3325a4a434f1785592e42541 | 62668 |

## Salida del modelo (datos, sin acciones ejecutables)

Veredicto `descartar` · DCF de la plantilla aplica: `dudoso`

| Filtro | Resultado |
|---|---|
| calidad | no_pasa |
| caja | dudoso |
| balance | pasa |
| precio | no_pasa |
| encaje | no_aplica |

### Pasivo por arrendamientos (dato aparte)

    Control maestro!M51 = leasing financiero ≈0,703 mm (estimado a 30.06.2026); el alquiler operativo (almacén ≈0,8 mm, Control maestro!M47) no se capitaliza (UoR sin NIIF 16) y ya se paga dentro del CFO.


### Tipo de negocio y motor

    Fabricante polaco de jarabes, concentrados, bebidas y suplementos, mayoritariamente con marca de distribuidor y para pocas cadenas; margen ligado al diferencial de materias primas (cíclico / commodity).
    Caja o beneficio de ciclo medio (margen normalizado a lo largo de un ciclo completo de insumos, con el capex ŁSSE y el nuevo coste fijo de 1,5 mm/año incluidos) en vez de proyectar desde el pico de margen de 2023-2026.

### calidad

    El ROCE LTM del 32,5% es reciente (≈7,7% en FY21-22 según Control maestro!N29) y descansa en un salto de margen EBIT del 0,4-3,6% (FY19-22) al 14,5% (FY25) que la propia dirección atribuye al ciclo de insumos; no hay foso, un cliente pesó el 42,8% de las ventas de 2024 y la gestión desvía caja al control (1,5 mm PLN/año al presidente del consejo de supervisión, frente a un beneficio neto de 8,4 mm, y warrants de hasta el 12,7% a 0,10 PLN).
    Dato clave: Análisis!C24 = 0.325

### caja

    El FCF base neto de SBC es positivo (3,119 mm, media FY23-25) y la conversión CFO/beneficio es de 1,358 (Análisis!C26), pero es inestable: −0,18 en 2022, solo 1,063 mm con la media de 5 años con SBC y un LTM de 12,592 inflado por +3,85 de circulante, con una ola de capex ŁSSE de hasta 19,165 mm antes del 31.03.2027 aún por absorber.
    Dato clave: Análisis!C52 = 3.119

### balance

    Sin arrendamientos, la deuda es de unos 0,834 mm de créditos frente a 15,051 mm de caja (Análisis!C53), así que hay caja neta de unos 14,2 mm y la deuda neta/EBITDA queda en ≈−0,82x sobre un EBITDA LTM de 17,243 que ya incluye el alquiler operativo (UoR); el −0,784 de Análisis!C33 incluye leasing, pero el resultado no cambia y pasa con holgura incluso para un negocio cíclico.
    Dato clave: Control maestro!M51 = créditos ≈0,834 (deuda sin arrendamientos; la deuda total Análisis!C54 = 1.537 incluye leasing ≈0,703)

### precio

    La cotización de 0,406 PLN (Análisis!C37) está muy por encima del valor ponderado de 0,273 y del precio de Sí de ≈0,16 que estima la respuesta (escenario malo 0,163), sigue por encima con r −2 pts (0,375) y casi alcanza el escenario bueno (0,451); un motor de ciclo medio (FCF 5a con SBC de 1,063 mm) la dejaría aún más cara.
    Dato clave: Análisis!C83 = 0.273299814804816

### encaje

    El paquete no trae la cartera; la hoja solo da un tamaño de posición del 0% (Análisis!C104), que es una decisión de la etapa 1 y no se usa aquí.
    Dato clave: Análisis!C104 = 0% · No · sin seguimiento (dato de la etapa 1, no heredado)

### Qué lo cambiaría

    - Concentración del cliente principal por debajo del 30% de las ventas o un contrato plurianual a los márgenes actuales.
    - Dos ejercicios con margen EBIT del 14-15% o más con el coste de insumos subiendo, que probarían poder de precio y no solo ciclo.
    - Retirada o reducción drástica de la retribución de 125.000 PLN/mes del presidente del consejo de supervisión y de los contratos vinculados, junto con una cotización por debajo de ≈0,16 PLN.

### Qué falta

    - Concentración de clientes de 2025 y duración y fecha de renovación del contrato con el cliente A (el dato de 2024 es del 42,8%).
    - Resultados del T3 2026 (previstos para el 13.11.2026, posteriores a la fecha de corte) y calendario real del capex ŁSSE de hasta 19,165 mm.
    - La deuda a 30.06.2026 es una estimación (no la desglosa el trimestral), y la decisión del inversor sobre las medias está fechada el 28-oct-2026, después de la fecha de la hoja (25.10.2026).

### Comprobaciones mecánicas y normalizaciones

    {
      "comprobaciones": {
        "avisos": [
          "Filtro calidad: motivo de más de 400 caracteres.",
          "Un texto menciona un tamaño de posición o un porcentaje de cartera."
        ],
        "nota": "Comprobaciones mecánicas informativas: no acreditan la calidad económica."
      },
      "normalizaciones": []
    }

