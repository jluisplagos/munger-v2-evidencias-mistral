# Cribado · Puigbrands

Estado de la ejecución: `AUDITORIA_DOCUMENTAL_PENDIENTE_ACEPTACION`

Cribado pendiente de revisión humana. No es una recomendación de compra, ni aceptación, ni aptitud para dinero real. Tasa 9 % provisional.

C-ARR (decisión de la persona responsable): los arrendamientos se cuentan una sola vez, en el flujo. El alquiler se resta de la caja libre; la deuda, deuda/EBITDA y deuda/caja libre se miden sin arrendamientos; el pasivo por arrendamientos se muestra aparte, como dato.

Cifras de la etapa 1 tal como las guardó la hoja, a su fecha de análisis; sin las decisiones posteriores (P-O1, P-O2, F1-A/F1-B, D-US1/2, D-WM) ni verificación contra la fuente oficial.

| Campo | Valor |
|---|---|
| Fecha de la hoja | 26/10/2026 |
| Tarea | cribado-44509331308-puigbrands |
| SHA del código | 833cd50a9bba34006519119c72a29c70a1656fb7 |
| Huella del paquete (package_sha256) | 3faaeb7c712212fb31d96c0b9a271b0109e7e54d0f252185615bb743b1b976f0 |
| Huella del envío (bundle_sha256) | 82fc41dd13c986ff3bfd3cd52474096263d5a04c71fb6ad954c3d32d7bdb3ecb |
| Huella del encargo | 32b5c7f313e61a61fb0f5e68a75b3c44004eb902e97b98720fb98fa8d383e6cf |
| Huella de la Release | 4d30f7352948fe7e7fe3b133386eabedbddcc71d997e972a1c6db7964d58b0a9 |
| Huella del libro | 8328a1b285ca007e755c82c0ad0c9c0e80e672605e26e232bac9049cff0f148f |
| Modelo pedido / devuelto | claude-opus-5-5 / claude-opus-5-5 |
| Esfuerzo | high |
| Gramática del servidor | True |
| Mensajes enviados | 1 |
| Cota de entrada antes de llamar | 184128 tokens |
| Reserva estimada antes de llamar | USD 1.391872 |
| Uso de tokens | entrada 84382, salida 4154 |
| Coste | CONOCIDO_ESTIMADO; estimado USD 0.420608; cota 0.420608 |

| id | ruta | sha256 | bytes |
|---|---|---|---|
| respuesta | EMPRESAS_LOTES_COMPLETOS/Puigbrands/Puigbrands_respuesta.md | 66efa2e7d14ca5e5992c112e548d9874bcd3dd4cb6e283d07a1c347e7900123a | 38722 |
| hoja_analisis | EMPRESAS_LOTES_COMPLETOS/Puigbrands/Puigbrands_evaluada.xlsx#Análisis | 97f478bf3901abdd3a58b62ddce787fe573c238eaf2a2aeaa530479870516606 | 24195 |
| hoja_control_maestro | EMPRESAS_LOTES_COMPLETOS/Puigbrands/Puigbrands_evaluada.xlsx#Control maestro | 1c826830900eddae6713585c8c2f7f2f321ef3239ce08d1d013aa48ea7e0a294 | 100166 |

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

    Control maestro!M51 = 399.7 mm de pasivos por arrendamiento a 30/06/2026 (Análisis!C54 = 1798.6 menos 1398.9 de deuda bancaria), fuera del cociente de deuda.


### Tipo de negocio y motor

    Grupo de marcas de belleza de consumo (fragancias de marca 72 % de las ventas, maquillaje y cuidado de la piel), estable y con crecimiento en parte comprado.
    El DCF de caja libre al accionista de la plantilla, adecuado para un negocio de marcas estable, restando aparte los 558,2 mm de put/call y earn-outs sobre minoritarios e incorporando Isdin con su EBITDA y su deuda.

### calidad

    Negocio de marcas comprensible: margen bruto del 75 %, margen operativo estable del 14,8-16,1 % (FY2022-FY2025) y ningún cliente por encima del 10 % de las ventas; el ROIC con intangibles es solo del 9,1 % (13-14 % sin fondo de comercio) porque el crecimiento se ha comprado caro, y Makeup y Skincare caen al 1,8 % y al 1,5 % de margen en H1-26, dudas que el estudio puede resolver.
    Dato clave: Análisis!C24 = 0.091

### caja

    El FCF al accionista, ya neto de intereses y principal de arrendamientos, creció de 186,0 a 520,8 mm entre FY2022 y FY2025 con 434,6 mm UDM y CFO/beneficio de 1,24x (Análisis!C26), aunque cerca del 45 % de la mejora vino del circulante y el CFO de H1-26 fue −118,6 mm.
    Dato clave: Análisis!C40 = 434.6

### balance

    El 1,48x de Análisis!C33 incluye 399,7 mm de arrendamientos y no sirve tal cual; sin ellos la deuda neta es ≈1.189,5 mm, ≈1,22x el EBITDA que resta el alquiler (aproximación de la hoja), con 924 mm de líneas no dispuestas, holgado para un negocio de marca estable, aunque el ~82 % de vencimientos en 2026-2027, Isdin (900 mm al cierre, ≈2,2x pro forma sin arrendamientos según mi recálculo de los 2.789 mm) y los 558,2 mm de put/call piden vigilancia.
    Dato clave: Análisis!C54 = 1798.6 con arrendamientos; sin ellos, deuda bancaria bruta 1398.9 (Control maestro!N51) y deuda neta sin arrendamientos ≈ 1189.5 (1398.9 − caja Análisis!C53 = 205.1 − 4.3 de préstamos a vinculadas), ≈ 1.22x un EBITDA UDM que resta el cargo de arrendamientos (≈ 977.8)

### precio

    A 19,14 € la cotización duplica el precio de Sí (≈9,3 €, escenario malo, inferior a ¾ del ponderado de 12,79 €) y supera incluso el escenario bueno (18,43 €) y el ponderado a r = 7 % (18,39 €, Análisis!C90); el precio exige un 11,1 % de crecimiento anual (Análisis!C86) y la hoja ya incorpora el avance de 9M-26 del 21/10/2026; la base de 373,5 mm de la hoja (la respuesta redondea a 374) no cambia la conclusión.
    Dato clave: Análisis!C37 = 19.14 frente a Análisis!C78 (malo) = 9.30739242610205 y Análisis!C83 = 12.7939992042131

### encaje

    El paquete no trae la cartera; la hoja solo registra un plan de cartera de la etapa 1 a 19,14 €, que no es un dato de encaje.
    Dato clave: Análisis!C104 = 0% · Watchlist (dato de la etapa 1, no usado como conclusión)

### Qué lo cambiaría

    - Una cotización en torno a 9,3 € o menos con el negocio intacto llevaría el precio a pasar (estudiar a fondo); hacia 12,8 € quedaría cerca.
    - Un FCF de FY2026 de 480 mm o más con circulante neutro subiría el FCF base y el valor; uno por debajo de ~420 mm haría fallar la caja.
    - Que tras el cierre de Isdin la deuda neta sin arrendamientos supere ~2,5x el EBITDA, o un deterioro relevante de Charlotte Tilbury, haría fallar el balance o la calidad (descartar).

### Qué falta

    - El umbral del covenant y el calendario de vencimientos actualizado a 30/06/2026 (el último es de 31/12/2025, con ~82 % en 2026-2027); tampoco hay un EBITDA anterior a la NIIF 16 publicado: el 1,22x es una aproximación.
    - Las cifras de beneficio, caja y deuda de Isdin y de Charlotte Tilbury, y cómo se financiarán los 900 mm de Isdin.
    - Duda sobre las fuentes: la hoja está fechada el 26/10/2026, pero cita decisiones del inversor del 01-nov-2026 (C24, C46-C50); la cotización de 19,14 € es del 23/10 y la lectura de 19,41 € del 26/10 no está confirmada.

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

