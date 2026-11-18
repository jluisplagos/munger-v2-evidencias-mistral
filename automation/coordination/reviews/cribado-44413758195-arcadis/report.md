# Cribado · Arcadis

Estado de la ejecución: `AUDITORIA_DOCUMENTAL_PENDIENTE_ACEPTACION`

Cribado pendiente de revisión humana. No es una recomendación de compra, ni aceptación, ni aptitud para dinero real. Tasa 9 % provisional.

C-ARR (decisión de la persona responsable): los arrendamientos se cuentan una sola vez, en el flujo. El alquiler se resta de la caja libre; la deuda, deuda/EBITDA y deuda/caja libre se miden sin arrendamientos; el pasivo por arrendamientos se muestra aparte, como dato.

Cifras de la etapa 1 tal como las guardó la hoja, a su fecha de análisis; sin las decisiones posteriores (P-O1, P-O2, F1-A/F1-B, D-US1/2, D-WM) ni verificación contra la fuente oficial.

| Campo | Valor |
|---|---|
| Fecha de la hoja | 2026-11-04 |
| Tarea | cribado-44413758195-arcadis |
| SHA del código | 833cd50a9bba34006519119c72a29c70a1656fb7 |
| Huella del paquete (package_sha256) | 10fdda37b4b66464819ee0f1f37d4e7aae3c45c1608aee8ba1ec579c20a0ce09 |
| Huella del envío (bundle_sha256) | 677ed80ba6734a5d9c2adaf0ead9484621802c4a47ed64b7e7bebde41c22d3c3 |
| Huella del encargo | 32b5c7f313e61a61fb0f5e68a75b3c44004eb902e97b98720fb98fa8d383e6cf |
| Huella de la Release | 4d30f7352948fe7e7fe3b133386eabedbddcc71d997e972a1c6db7964d58b0a9 |
| Huella del libro | af5c58a7f93a775dc0f507f4d003819da142b07695ad8b37db59d84f9d1bb0f6 |
| Modelo pedido / devuelto | claude-opus-5-5 / claude-opus-5-5 |
| Esfuerzo | high |
| Gramática del servidor | True |
| Mensajes enviados | 1 |
| Cota de entrada antes de llamar | 130105 tokens |
| Reserva estimada antes de llamar | USD 1.17578 |
| Uso de tokens | entrada 58730, salida 3930 |
| Coste | CONOCIDO_ESTIMADO; estimado USD 0.31352; cota 0.31352 |

| id | ruta | sha256 | bytes |
|---|---|---|---|
| respuesta | EMPRESAS_LOTES_COMPLETOS/Arcadis/Arcadis_respuesta.md | c8ce6042e6acefd97ff1451f653fc2cac45db5b12b99b3eb7021cf4e098d3fb4 | 30983 |
| hoja_analisis | EMPRESAS_LOTES_COMPLETOS/Arcadis/Arcadis_evaluada.xlsx#Análisis | cab45ab991320bd0188d0140c5d00d40a143e024aaece1bf3e74dd86e2ea53f5 | 22966 |
| hoja_control_maestro | EMPRESAS_LOTES_COMPLETOS/Arcadis/Arcadis_evaluada.xlsx#Control maestro | 568ac776953de8e6af080775c68b585ad37866cbf0640752023216e2b2b4678a | 55376 |

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

    Control maestro!M51 = 238 (pasivo por arrendamientos a 30/06/2026, incluido en la deuda total de 1.324 de Análisis!C54)


### Tipo de negocio y motor

    Servicios profesionales de consultoría de ingeniería, diseño y gestión de proyectos: de poco capital, cobra por avance, con demanda pública y privada (agua, movilidad, edificios) y está en una reestructuración con CEO nueva.
    El DCF de caja libre de la plantilla, sobre un FCF normalizado que trate como gasto los costes de reestructuración recurrentes, porque es un negocio de servicios de poco capital con flujo positivo y financiación estable (Análisis!C62 = Sí).

### calidad

    El negocio se entiende (vende horas técnicas a más de 9.000 clientes, ninguno por encima del 10 %) y el ROIC sin fondo de comercio es del 34 %, pero el ROIC con fondo de comercio es de solo el 11,7 %, el margen tras costes no operativos recurrentes ronda el 9 %, no hay foso demostrado (C18 = No) y la asignación de capital es dudosa (IBI/Places); los datos apuntan en las dos direcciones.
    Dato clave: Análisis!C24 = 0.117

### caja

    El FCF base, después de arrendamientos y SBC, es de 226,9; la caja operativa es 1,82 veces el beneficio (Análisis!C26), el FCF fue positivo todos los años de 2016 a 2025 y el capex es de unos 37, aunque el FCF sin circulante está plano en 192-275 desde 2021.
    Dato clave: Análisis!C52 = 226.9

### balance

    Sin arrendamientos, la deuda neta de 804 sobre un EBITDA que ya resta el alquiler da unos 2,25x (frente al 2,42x de Análisis!C33, que incluye la NIIF 16) en el pico estacional de junio, unos 3,5 años de FCF base. Es asumible para un negocio de poco capital y clientes diversificados, con covenant de 3,5x, el Schuldschein de 225 refinanciado con el Eurobono de 300 y un RCF de 600 sin disponer.
    Dato clave: Control maestro!M36 = deuda neta 1042 con arrendamientos 238 → deuda neta sin arrendamientos 804 (préstamos brutos sin arrendamientos 1086, Control maestro!N51); ÷ EBITDA tras alquiler ≈ 430 − 73 = 357 → 2,25x (Control maestro!N36)

### precio

    A 47 € la cotización está claramente por encima del precio de Sí, de unos 31,2 € (el menor entre el escenario malo, 31,2, y 0,75 × el ponderado de 48,0 = 36,0); el ponderado solo deja un margen del 2 % y, con r + 2 puntos, el valor ponderado cae a 36,8 €. Incluso a r 7 %, el precio de Sí que estima la etapa 1 (unos 41 €) sigue por debajo de 47 €.
    Dato clave: Análisis!B78 = 31.2348853088268 (precio de Sí, frente a Análisis!C37 = 47)

### encaje

    El paquete no trae la cartera de la persona responsable y la hoja solo da un tamaño de posición del 0 %, que es una decisión de cartera que no corresponde a este cribado.
    Dato clave: Análisis!C104 = 0% · No (decisión de cartera de la etapa 1, no usada como conclusión)

### Qué lo cambiaría

    - Una cotización igual o inferior a unos 31 € (Análisis!B78), que llevaría el precio a pasa y el veredicto a estudiar_a_fondo.
    - Dos o tres años de margen EBITA reportado de al menos el 11 % después de los costes no operativos y un ROIC con fondo de comercio por encima del 15 %, que resolverían la duda de calidad.
    - Un deterioro del fondo de comercio de Places, o una compra con deuda que lleve la deuda neta sin arrendamientos por encima de unas 3x el EBITDA tras alquiler, que llevaría a descartar.

### Qué falta

    - El saldo vivo del factoring sin recurso a 30/06/2026 (hasta 34 cedidos en 2025), que afecta a la deuda neta y al FCF LTM.
    - El peso de los contratos a precio fijo en los ingresos y su historial de pérdidas (asunto clave de auditoría sin cifra).
    - La deuda neta sin arrendamientos y el EBITDA tras alquiler fuera del pico de junio (solo consta 2,09x con arrendamientos a 30/09/2026); el precio de 47 € viene de una fuente secundaria.

### Comprobaciones mecánicas y normalizaciones

    {
      "comprobaciones": {
        "avisos": [
          "Un texto menciona un tamaño de posición o un porcentaje de cartera."
        ],
        "nota": "Comprobaciones mecánicas informativas: no acreditan la calidad económica."
      },
      "normalizaciones": []
    }

