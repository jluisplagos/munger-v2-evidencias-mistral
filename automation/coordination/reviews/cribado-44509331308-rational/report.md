# Cribado · Rational

Estado de la ejecución: `AUDITORIA_DOCUMENTAL_PENDIENTE_ACEPTACION`

Cribado pendiente de revisión humana. No es una recomendación de compra, ni aceptación, ni aptitud para dinero real. Tasa 9 % provisional.

C-ARR (decisión de la persona responsable): los arrendamientos se cuentan una sola vez, en el flujo. El alquiler se resta de la caja libre; la deuda, deuda/EBITDA y deuda/caja libre se miden sin arrendamientos; el pasivo por arrendamientos se muestra aparte, como dato.

Cifras de la etapa 1 tal como las guardó la hoja, a su fecha de análisis; sin las decisiones posteriores (P-O1, P-O2, F1-A/F1-B, D-US1/2, D-WM) ni verificación contra la fuente oficial.

| Campo | Valor |
|---|---|
| Fecha de la hoja | 2026-10-08 |
| Tarea | cribado-44509331308-rational |
| SHA del código | 833cd50a9bba34006519119c72a29c70a1656fb7 |
| Huella del paquete (package_sha256) | bc1ac3473a5db3ee42cf4a4f0e55343db1924079c48cdb25a7cde8285b1ea146 |
| Huella del envío (bundle_sha256) | 8b9fc85fa0a2ee46421efc712872e3dcf10340bf7f3e2c13489c00a8f9f41462 |
| Huella del encargo | 32b5c7f313e61a61fb0f5e68a75b3c44004eb902e97b98720fb98fa8d383e6cf |
| Huella de la Release | 4d30f7352948fe7e7fe3b133386eabedbddcc71d997e972a1c6db7964d58b0a9 |
| Huella del libro | 8ec3c42f0ac8e618946f0a9aef896697d37a439695ca10bcf31617993e1af069 |
| Modelo pedido / devuelto | claude-opus-5-5 / claude-opus-5-5 |
| Esfuerzo | high |
| Gramática del servidor | True |
| Mensajes enviados | 1 |
| Cota de entrada antes de llamar | 137513 tokens |
| Reserva estimada antes de llamar | USD 1.205412 |
| Uso de tokens | entrada 62404, salida 2966 |
| Coste | CONOCIDO_ESTIMADO; estimado USD 0.308936; cota 0.308936 |

| id | ruta | sha256 | bytes |
|---|---|---|---|
| respuesta | EMPRESAS_LOTES_COMPLETOS/Rational/Rational_respuesta.md | 2862d98ea3608b73798069e916d13d2636f6d3b9e3375ed16c95b637ad9e4c06 | 32103 |
| cambios_v2 | EMPRESAS_LOTES_COMPLETOS/Rational/Rational_cambios_v2.md | d1e26b17e4702abff5781b3b89c5842e1deb320b45ad0f5e18fb97f8b293a050 | 5028 |
| hoja_analisis | EMPRESAS_LOTES_COMPLETOS/Rational/Rational_evaluada.xlsx#Análisis | 8b1e931fbb98cc60b073e1eb450d5814a21b2c2a576812a5dd02053bdc6d3b4c | 23333 |
| hoja_control_maestro | EMPRESAS_LOTES_COMPLETOS/Rational/Rational_evaluada.xlsx#Control maestro | daa856580ed1034e596a8b873971d3712a1271fdae86703a2c6ffe3394184ebf | 55808 |

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

    Análisis!C54 = 27.631 (solo arrendamientos: 9,8 corrientes + 17,8 no corrientes; Control maestro!M51); fuera del cociente de deuda.


### Tipo de negocio y motor

    Fabricante de sistemas de cocción para cocinas profesionales (aparatos + 31 % de posventa); compounder estable, sin deuda financiera.
    El DCF de caja libre de la plantilla con escenarios: es un fabricante estable de bienes de equipo sin deuda, con flujos positivos y un 31 % de posventa recurrente.

### calidad

    El negocio se entiende y muestra ventaja en las cifras: ROCE del 36,7 %, margen EBIT estable en torno al 26 % y mayor cliente en torno al 1 %; el «DESCARTAR · demasiado difícil» de Análisis!A6 viene de C13 = No (precio) y no de la calidad, y quedan como dudas el volumen plano de 2023–2024, China −29 % en 2025 y competidores sin nombre.
    Dato clave: Análisis!C24 = 0.367

### caja

    Caja libre base de 219,2 m (media FY2023–25, ya restados intereses y arrendamientos), positiva todos los años de la serie, con CFO/beneficio neto de 1,097 (C26), capex de 33,3 m cercano a la amortización y 250,1 m en los últimos doce meses (C40).
    Dato clave: Análisis!C52 = 219.2

### balance

    Sin arrendamientos, la deuda financiera es 0 frente a 205,98 m de caja, una caja neta de unos −0,55x el EBITDA ya restado el alquiler (variante de Control maestro!N36); la Análisis!C33 = −0,4624 incluye 27,6 m de arrendamientos y EBITDA NIIF 16, así que no sirve tal cual, aunque la conclusión es la misma.
    Dato clave: Control maestro!M51 = deuda financiera 0 (sin arrendamientos); caja Análisis!C53 = 205.98

### precio

    La cotización de 566,5 € (C37) casi duplica el precio de Sí de unos 288 € (escenario malo, C78), queda un 34 % por encima del ponderado de 422,3 € (C83) e implica un crecimiento del 10,3 % (C86), por encima del escenario bueno; ni con r del 7 % el ponderado (617,3 €, C90) baja a 0,75 × 617 ≈ 463 €, que sigue por debajo de 566,5 €.
    Dato clave: Análisis!C78 = 288.204720059155

### encaje

    El paquete no trae la cartera y la hoja no dice nada concreto sobre encaje más allá de una capitalización de 6.441,1 m, así que el filtro no aplica y no elimina.
    Dato clave: Análisis!C41 = 6441.1

### Qué lo cambiaría

    - Una cotización en torno a 288 € o por debajo (Análisis!C78) con la tesis intacta pasaría el filtro de precio (estudiar_a_fondo).
    - Un margen EBIT sin extraordinarios sostenido por debajo del 22 %, o un competidor con nombre que iguale la tecnología a menor precio, rebajaría la calidad (descartar).
    - Que aparezca deuda financiera relevante o una adquisición grande fuera del núcleo cambiaría el balance.

### Qué falta

    - Competidores con nombre y su cuota: la cuota del 50 % es cifra de la propia empresa.
    - Una cotización posterior al 7-oct-2026: Control maestro!N38 pide actualizarla antes de decidir.
    - El EBITDA sin arrendamientos publicado: el −0,55x es una aproximación de la hoja; además, la auditoría del modelo (Control maestro filas 90–97) sigue marcada como «Pendiente» aunque los escenarios ya están rellenos.

### Comprobaciones mecánicas y normalizaciones

    {
      "comprobaciones": {
        "avisos": [],
        "nota": "Comprobaciones mecánicas informativas: no acreditan la calidad económica."
      },
      "normalizaciones": []
    }

