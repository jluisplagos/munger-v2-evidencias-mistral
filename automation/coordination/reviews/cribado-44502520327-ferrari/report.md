# Cribado · Ferrari

Estado de la ejecución: `AUDITORIA_DOCUMENTAL_PENDIENTE_ACEPTACION`

Cribado pendiente de revisión humana. No es una recomendación de compra, ni aceptación, ni aptitud para dinero real. Tasa 9 % provisional.

C-ARR (decisión de la persona responsable): los arrendamientos se cuentan una sola vez, en el flujo. El alquiler se resta de la caja libre; la deuda, deuda/EBITDA y deuda/caja libre se miden sin arrendamientos; el pasivo por arrendamientos se muestra aparte, como dato.

Cifras de la etapa 1 tal como las guardó la hoja, a su fecha de análisis; sin las decisiones posteriores (P-O1, P-O2, F1-A/F1-B, D-US1/2, D-WM) ni verificación contra la fuente oficial.

| Campo | Valor |
|---|---|
| Fecha de la hoja | 2026-10-25 |
| Tarea | cribado-44502520327-ferrari |
| SHA del código | 833cd50a9bba34006519119c72a29c70a1656fb7 |
| Huella del paquete (package_sha256) | 3b4951ae65280d9f747d6a8c068148768bca953eb7378fa3135ddc27555e474f |
| Huella del envío (bundle_sha256) | 05c0cbcc0714687472de5792cdd9dba0a71d14a6d10749c35d08f33dd4f27850 |
| Huella del encargo | 32b5c7f313e61a61fb0f5e68a75b3c44004eb902e97b98720fb98fa8d383e6cf |
| Huella de la Release | 4d30f7352948fe7e7fe3b133386eabedbddcc71d997e972a1c6db7964d58b0a9 |
| Huella del libro | c586e4295e58c538571a689c4a18bc9e531647d0ec7bcabd4efd8c7178d3a714 |
| Modelo pedido / devuelto | claude-opus-5-5 / claude-opus-5-5 |
| Esfuerzo | high |
| Gramática del servidor | True |
| Mensajes enviados | 1 |
| Cota de entrada antes de llamar | 145824 tokens |
| Reserva estimada antes de llamar | USD 1.238656 |
| Uso de tokens | entrada 65204, salida 3023 |
| Coste | CONOCIDO_ESTIMADO; estimado USD 0.321276; cota 0.321276 |

| id | ruta | sha256 | bytes |
|---|---|---|---|
| respuesta | EMPRESAS_LOTES_COMPLETOS/Ferrari/Ferrari_respuesta.md | 93c6208b2578a209e8429f765bbe5459054957eee27087bbb50dec6a801361c8 | 38633 |
| hoja_analisis | EMPRESAS_LOTES_COMPLETOS/Ferrari/Ferrari_evaluada.xlsx#Análisis | 0f14232d7f0a539b8bde0206f4dc06060a88accc303882bad14a3915e94432fa | 24019 |
| hoja_control_maestro | EMPRESAS_LOTES_COMPLETOS/Ferrari/Ferrari_evaluada.xlsx#Control maestro | 1a6d2565ba2334c41965cd7fcf2973c041d9c971c3e3d6bb27d7e39fddf36b02 | 62024 |

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

    Control maestro!M51 = 157.1 (pasivo por arrendamientos a 30-jun-2026, incluido en la deuda IFRS de Análisis!C54 = 3165.6)


### Tipo de negocio y motor

    Fabricante de coches deportivos de lujo con escasez administrada (compounder de marca, un solo segmento), con un brazo de financiación a clientes.
    El DCF de caja libre de la plantilla es adecuado: se trata de un negocio industrial de un solo segmento, estable, que autofinancia su capex; conviene vigilar aparte la cartera de financiación a clientes (FFS).

### calidad

    Negocio sencillo y comprensible con ROIC del 31,7 % y margen EBIT que pasa del 15,6 % (2015) al 29,5 % (2025), así que discrepo del «DESCARTAR · demasiado difícil» de Análisis!A6, que mezcla precio con comprensión; las vigilancias son el inventario de producto terminado (+20,2 %) y China y Reino Unido a la baja.
    Dato clave: Análisis!C24 = 0.317

### caja

    La caja libre base después de capex, principal de arrendamientos y SBC es positiva (1.015,4 mm €), el FCF declarado sube cada año de 546 (2021) a 1.406 (2025) y CFO/beneficio neto es 1,41x, aunque 2025 está inflado por anticipos del F80.
    Dato clave: Análisis!C52 = 1015.4

### balance

    La 0,61x de la hoja (Análisis!C33) incluye 157,1 de arrendamientos; sin ellos, la deuda neta queda en ≈1.586 mm € frente a un EBITDA LTM de 2.846,9 menos ≈30 de alquiler, ≈0,56x (cifra que también da Control maestro), holgado para un negocio tan estable, y la deuda neta industrial es solo 131.
    Dato clave: Análisis!C54 = 3165.6 menos arrendamientos Control maestro!M51 = 157.1 → deuda sin arrendamientos 3008.5; deuda neta ≈ 1586.2 (con caja no restringida 1422.3)

### precio

    La cotización de 349,5 € es unas 4,5 veces el precio de Sí (≈77,9 €, escenario malo) y 2,9 veces el valor ponderado de 120,4 €; ni con r del 7 % (173,6 €) se acerca, y el DCF inverso exige un 21,2 % anual de crecimiento del FCF.
    Dato clave: Análisis!C78 = 77.9306896310482

### encaje

    El paquete no trae la cartera de la persona responsable; la hoja solo marca la categoría «nunca vender» (Sí), que no basta para juzgar el encaje.
    Dato clave: Análisis!C103 = Sí

### Qué lo cambiaría

    - Una cotización por debajo de unos 120 € (Análisis!C83) acercaría el precio y llevaría a estudiar a fondo; por debajo de 77,9 € (Análisis!C78), el precio pasaría.
    - Que el inventario de producto terminado no se normalice en el 3T26 o en el cierre de 2026 y que las entregas caigan dos años seguidos rebajaría la calidad.
    - Que el ROIC caiga de forma sostenida por debajo del 15 % o que el margen EBIT baje más de dos puntos frente al 30,5 % del 1S26.

### Qué falta

    - El EBITDA LTM sin arrendamientos exacto (pagos de alquiler LTM con intereses): la cifra de ≈0,56x es aproximada.
    - No constan el desglose de inventarios a jun-2025 ni el tamaño de la cartera de pedidos y de la lista de espera para contrastar la señal de demanda (inventario de producto terminado +20,2 %).
    - Fuentes: Control maestro cita una «decisión del inversor (28-oct-2026)» posterior a la fecha de la hoja (25-oct-2026), y faltan los resultados del 3T26 (3-nov-2026).

### Comprobaciones mecánicas y normalizaciones

    {
      "comprobaciones": {
        "avisos": [],
        "nota": "Comprobaciones mecánicas informativas: no acreditan la calidad económica."
      },
      "normalizaciones": []
    }

