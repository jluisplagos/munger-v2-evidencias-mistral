# Cribado · Vidrala

Estado de la ejecución: `AUDITORIA_DOCUMENTAL_PENDIENTE_ACEPTACION`

Cribado pendiente de revisión humana. No es una recomendación de compra, ni aceptación, ni aptitud para dinero real. Tasa 9 % provisional.

C-ARR (decisión de la persona responsable): los arrendamientos se cuentan una sola vez, en el flujo. El alquiler se resta de la caja libre; la deuda, deuda/EBITDA y deuda/caja libre se miden sin arrendamientos; el pasivo por arrendamientos se muestra aparte, como dato.

Cifras de la etapa 1 tal como las guardó la hoja, a su fecha de análisis; sin las decisiones posteriores (P-O1, P-O2, F1-A/F1-B, D-US1/2, D-WM) ni verificación contra la fuente oficial.

| Campo | Valor |
|---|---|
| Fecha de la hoja | 2026-10-10 |
| Tarea | cribado-44515220408-vidrala |
| SHA del código | 833cd50a9bba34006519119c72a29c70a1656fb7 |
| Huella del paquete (package_sha256) | 2df02d8f324d0fccd1ea4961254e859baf34679baa2ae7b30d3a846c70623a78 |
| Huella del envío (bundle_sha256) | c5ca10db705474b509caa1f1714949290d0c8b3f55370120b6736d95a4181fdf |
| Huella del encargo | 32b5c7f313e61a61fb0f5e68a75b3c44004eb902e97b98720fb98fa8d383e6cf |
| Huella de la Release | 4d30f7352948fe7e7fe3b133386eabedbddcc71d997e972a1c6db7964d58b0a9 |
| Huella del libro | 6aed21169576aa444a3b5d46a2c5906a7548e63ee45f23b9c60a78e4a22b2675 |
| Modelo pedido / devuelto | claude-opus-5-5 / claude-opus-5-5 |
| Esfuerzo | high |
| Gramática del servidor | True |
| Mensajes enviados | 1 |
| Cota de entrada antes de llamar | 136938 tokens |
| Reserva estimada antes de llamar | USD 1.203112 |
| Uso de tokens | entrada 61969, salida 4893 |
| Coste | CONOCIDO_ESTIMADO; estimado USD 0.345736; cota 0.345736 |

| id | ruta | sha256 | bytes |
|---|---|---|---|
| respuesta | EMPRESAS_LOTES_COMPLETOS/Vidrala/Vidrala_respuesta.md | e080936a9f8f722fdf6b8e69dac7eaa98f5774bc8506c3bb050081bf4df79a7c | 34338 |
| cambios_v2 | EMPRESAS_LOTES_COMPLETOS/Vidrala/Vidrala_cambios_v2.md | c6cdb0514e4740c22c4a17aaca3fa187444339b1cab9202f2a188f193207862c | 4969 |
| hoja_analisis | EMPRESAS_LOTES_COMPLETOS/Vidrala/Vidrala_evaluada.xlsx#Análisis | 7a33710487de938ef5d717109a64943cd83b00af6071fe9183b220057f74513b | 23240 |
| hoja_control_maestro | EMPRESAS_LOTES_COMPLETOS/Vidrala/Vidrala_evaluada.xlsx#Control maestro | f59a5bf205c3b64acee8306843b7c7a6fbbf02a2099e44498da357bf5758b720 | 53418 |

## Salida del modelo (datos, sin acciones ejecutables)

Veredicto `vigilar` · DCF de la plantilla aplica: `dudoso`

| Filtro | Resultado |
|---|---|
| calidad | pasa |
| caja | pasa |
| balance | pasa |
| precio | no_pasa |
| encaje | no_aplica |

### Pasivo por arrendamientos (dato aparte)

    47,9 mm a 30-jun-2026: Análisis!C54 = 409.6 (con arrendamientos) menos 361,7 sin NIIF 16 (Control maestro!N51).


### Tipo de negocio y motor

    Fabricante industrial cíclico de envases de vidrio para alimentación y bebidas (Iberia, Reino Unido e Irlanda, Brasil y Chile), intensivo en energía, con un margen que sigue al coste de la energía y a su traslado al precio.
    Caja libre de ciclo medio: el DCF de la plantilla con una base normalizada que incluya un año de margen bajo, como la media de 5 años (129,5 mm con 2022), en lugar de la media 2023-25 (161,2 mm) con margen de máximo.

### calidad

    Negocio comprensible: ROIC después de impuestos del 13 %, ROCE antes de impuestos estable del 16,3-19,8 % en 2019-2025 y más de 1.600 clientes, ninguno por encima del 10 %; el foso es estrecho y el margen del 30,1 % está en máximos ligado a la energía, y este filtro discrepa del «DESCARTAR · demasiado difícil» de A6, que nace de C13 = No (precio) y no de falta de comprensión.
    Dato clave: Análisis!C24 = 0.13

### caja

    El CFO agregado de 2021-2025 es 1,35 veces el beneficio neto y la caja libre de la plantilla es positiva salvo en 2022, con 161,2 mm de media 2023-25 y 129,5 mm de media de 5 años, aunque los doce meses a 30-jun-2026 caen a 94,6 mm por un circulante de −130,9 mm, con existencias +17,8 % frente a ventas +0,5 %.
    Dato clave: Análisis!C26 = 1.35

### balance

    Sin arrendamientos, la deuda neta es de 252,3 mm (361,7 − 109,4), unas 0,57-0,59x el EBITDA sin NIIF 16 según la sensibilidad de Control maestro!N36; el 0,69x de Análisis!C33 incluye arrendamientos y no sirve tal cual, pero el nivel es holgado incluso para un negocio cíclico, con la salvedad de los vencimientos: la caja solo cubre 0,46 de una deuda corriente de 240,1 mm (C34) y las líneas no dispuestas de 258 mm son de 31-dic-2025.
    Dato clave: Control maestro!N51 = Sin NIIF 16: 361,7 (deuda neta sin arrendamientos 361,7 − 109,4 = 252,3 mm)

### precio

    A 88,7 € la cotización está claramente por encima del precio de Sí de etapa 1 (≈48 €, igual al escenario malo de 48,06 € en Análisis!B78), del ponderado de 76,54 € (C83) y del normal de 74,0 €; además, el DCF inverso exige un 5,4 % de crecimiento (C86) y, aunque a r del 7 % el ponderado sube a 108,6 €, el precio de Sí seguiría por debajo de la cotización, mientras que una base de ciclo medio de 129,5 mm rebajaría los valores.
    Dato clave: Análisis!C37 = 88.7

### encaje

    El paquete no trae la cartera y la hoja no dice nada concreto del encaje a 2026-10-10, así que este filtro no aplica y no elimina.
    Dato clave: No consta la cartera de la persona responsable en el paquete (fecha de la hoja: Análisis!D4 = 2026-10-10)

### Qué lo cambiaría

    - Una cotización por debajo de 48,06 € (escenario malo, Análisis!B78) con el negocio sin cambios lo llevaría a estudiar_a_fondo.
    - Un margen EBITDA de 2026 por debajo del 22 % sin choque de energía, o una caja libre de 2026-2027 por debajo de 150 mm, lo llevaría a descartar.
    - Una deuda neta sin arrendamientos por encima de 2x EBITDA por compras en emergentes, o vencimientos a corto plazo sin líneas que los cubran, haría fallar el balance.

### Qué falta

    - Desglose y vencimientos de la deuda a 30-jun-2026 y líneas comprometidas no dispuestas verificadas a esa fecha (las de 258 mm son de 31-dic-2025).
    - EBITDA de los doce meses a 30-jun-2026 sin NIIF 16 como cifra exacta: la hoja solo da el cociente en un rango de 0,57-0,59x.
    - Series de volumen y precio por unidad y cuotas de los competidores: los pares de C42 son de fuente secundaria y no traen cuotas.

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

