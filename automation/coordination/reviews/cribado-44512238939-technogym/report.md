# Cribado · Technogym

Estado de la ejecución: `AUDITORIA_DOCUMENTAL_PENDIENTE_ACEPTACION`

Cribado pendiente de revisión humana. No es una recomendación de compra, ni aceptación, ni aptitud para dinero real. Tasa 9 % provisional.

C-ARR (decisión de la persona responsable): los arrendamientos se cuentan una sola vez, en el flujo. El alquiler se resta de la caja libre; la deuda, deuda/EBITDA y deuda/caja libre se miden sin arrendamientos; el pasivo por arrendamientos se muestra aparte, como dato.

Cifras de la etapa 1 tal como las guardó la hoja, a su fecha de análisis; sin las decisiones posteriores (P-O1, P-O2, F1-A/F1-B, D-US1/2, D-WM) ni verificación contra la fuente oficial.

| Campo | Valor |
|---|---|
| Fecha de la hoja | 2026-10-26 |
| Tarea | cribado-44512238939-technogym |
| SHA del código | 833cd50a9bba34006519119c72a29c70a1656fb7 |
| Huella del paquete (package_sha256) | 60b7669479893766c17c94da834e2a780e7bb7f92e08584f907601fa61e55686 |
| Huella del envío (bundle_sha256) | 8d3caad08709ec75d78218fa4bedec1275ed87c976fcce0f9b3778410155cbc9 |
| Huella del encargo | 32b5c7f313e61a61fb0f5e68a75b3c44004eb902e97b98720fb98fa8d383e6cf |
| Huella de la Release | 4d30f7352948fe7e7fe3b133386eabedbddcc71d997e972a1c6db7964d58b0a9 |
| Huella del libro | 5c6facdd5bdc2ca55b8b8d40c69c863b348d5a77a32ed6c630214426c7f51c76 |
| Modelo pedido / devuelto | claude-opus-5-5 / claude-opus-5-5 |
| Esfuerzo | high |
| Gramática del servidor | True |
| Mensajes enviados | 1 |
| Cota de entrada antes de llamar | 170851 tokens |
| Reserva estimada antes de llamar | USD 1.338764 |
| Uso de tokens | entrada 76705, salida 3845 |
| Coste | CONOCIDO_ESTIMADO; estimado USD 0.38372; cota 0.38372 |

| id | ruta | sha256 | bytes |
|---|---|---|---|
| respuesta | EMPRESAS_LOTES_COMPLETOS/Technogym/Technogym_respuesta.md | 496af3c19b6b1b28b280b5504120c2d8749eb0f8101978c63fcf86a1fbcb1b71 | 35769 |
| hoja_analisis | EMPRESAS_LOTES_COMPLETOS/Technogym/Technogym_evaluada.xlsx#Análisis | 608a8249d99ee496a952a7f3b6d81041418691ad4320234130aa9c839bd3f5bd | 23996 |
| hoja_control_maestro | EMPRESAS_LOTES_COMPLETOS/Technogym/Technogym_evaluada.xlsx#Control maestro | a322de66d5b9e818798af9412bc4a9d990296912b3db2d0a83d6d249c3dcfac6 | 89714 |

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

    Control maestro!M51 = 55.42 (mm a 30-06-2026; dato aparte, fuera del cociente de deuda)


### Tipo de negocio y motor

    Fabricante de equipos de fitness de marca, con software conectado y servicios, que vende sobre todo a operadores profesionales (BtoB 80,8 %); bien de equipo discrecional con circulante negativo y caja neta.
    El DCF de caja libre del accionista de la plantilla, partiendo de una caja libre normalizada de ciclo medio (no del LTM ni de un solo año), porque el producto es discrecional y algo cíclico.

### calidad

    El ROI publicado del 88,3 % está inflado por el cambio contable (el par homogéneo es 71,3 %, y la serie anterior va del 36,7 % al 52,5 %), pero con márgenes operativos del 11-17 % durante diez años, ingresos ≈7 % anual, el 80,8 % de las ventas a clientes profesionales y ningún cliente por encima del 10 % el negocio se entiende y es de calidad; las reservas son el producto discrecional (−24 % en 2020), el gobierno controlado por el fundador y el riesgo de crédito retenido de clientes, que la «bandera» de C20 en la hoja refleja más como precio que como negocio.
    Dato clave: Análisis!C24 = 0.883

### caja

    La caja libre base, ya neta de alquileres y de SBC, es de 85,2 mm y positiva en todos los años con dato, con una conversión CFO/beneficio de 1,59x (C26); el LTM de 70,27 mm (C40) baja por un acopio de inventario y un capex en pico que la hoja documenta como transitorios.
    Dato clave: Análisis!C52 = 85.182

### balance

    Sin arrendamientos, la deuda es de 69,27 mm frente a una caja de 210,9 mm (C53), lo que da una caja neta de 141,65 mm y −0,71x sobre el EBITDA aproximado tras restar el alquiler (199,4 mm); el −0,40x de C33 incluye arrendamientos y no se usa tal cual, y la única vigilancia son los 65 mm de revolving a corto con vencimiento en 2026.
    Dato clave: Control maestro!M51 = 69.27 (deuda financiera sin arrendamientos, mm; Análisis!C54 = 124.69 sí los incluye)

### precio

    A 12,39 € la cotización duplica el precio de Sí (≈6,0 €), supera el valor ponderado de 8,97 € (margen −38 %) y equivale al escenario bueno (12,54 €), con un crecimiento implícito del 10,6 % (C86) por encima del bueno; aunque a r del 7 % el ponderado sube a 13,30 € (C90), el precio de Sí seguiría muy por debajo de la cotización.
    Dato clave: Análisis!C37 = 12.39 frente a un precio de Sí ≈ 6,0 (Análisis!C104) y un ponderado Análisis!C83 = 8.97

### encaje

    El paquete no trae la cartera de la persona responsable y la hoja solo aporta un plan de etapa 1 (con precio de 12,39 €) que no se hereda, así que este filtro no aplica ni elimina.
    Dato clave: Análisis!C37 = 12.39

### Qué lo cambiaría

    - Una cotización en torno a 6 € o por debajo, con el margen y la caja intactos.
    - Un margen operativo por debajo del 12 % dos años seguidos, o una caja libre FY2026 por debajo de 70 mm sin que se descargue el inventario.
    - Que las revolving de 65 mm pasen a ser deuda permanente para pagar dividendos, o que las garantías a clientes resulten materiales.

### Qué falta

    - Ingresos del tercer trimestre de 2026, publicados el 28-10-2026, después de la fecha de corte; además, las notas de C46-C49 citan una decisión del 01-11-2026, posterior a la fecha de la hoja, y la fila 90 sigue describiendo el bloque DCF como aplazado.
    - Importe máximo de las garantías financieras dadas a clientes y riesgo real de las cláusulas de recompra (39,6 + 7,6 mm).
    - P/FCF histórico homogéneo para contrastar el múltiplo terminal (C88 está vacía).

### Comprobaciones mecánicas y normalizaciones

    {
      "comprobaciones": {
        "avisos": [
          "Filtro calidad: motivo de más de 400 caracteres."
        ],
        "nota": "Comprobaciones mecánicas informativas: no acreditan la calidad económica."
      },
      "normalizaciones": []
    }

