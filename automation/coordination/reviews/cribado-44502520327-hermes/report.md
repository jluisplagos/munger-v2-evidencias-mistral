# Cribado · Hermes

Estado de la ejecución: `AUDITORIA_DOCUMENTAL_PENDIENTE_ACEPTACION`

Cribado pendiente de revisión humana. No es una recomendación de compra, ni aceptación, ni aptitud para dinero real. Tasa 9 % provisional.

C-ARR (decisión de la persona responsable): los arrendamientos se cuentan una sola vez, en el flujo. El alquiler se resta de la caja libre; la deuda, deuda/EBITDA y deuda/caja libre se miden sin arrendamientos; el pasivo por arrendamientos se muestra aparte, como dato.

Cifras de la etapa 1 tal como las guardó la hoja, a su fecha de análisis; sin las decisiones posteriores (P-O1, P-O2, F1-A/F1-B, D-US1/2, D-WM) ni verificación contra la fuente oficial.

| Campo | Valor |
|---|---|
| Fecha de la hoja | 2026-10-08 |
| Tarea | cribado-44502520327-hermes |
| SHA del código | 833cd50a9bba34006519119c72a29c70a1656fb7 |
| Huella del paquete (package_sha256) | 1c7cdf356345d394201b60f7cf81ab27c24edcb6eb448f0df4d8111bbb536a5b |
| Huella del envío (bundle_sha256) | 9fac3dcb11cc11a58aa6bb9dc1b0be426e1ebc8fa0e6eda5f4c4c9a9143fe1e8 |
| Huella del encargo | 32b5c7f313e61a61fb0f5e68a75b3c44004eb902e97b98720fb98fa8d383e6cf |
| Huella de la Release | 4d30f7352948fe7e7fe3b133386eabedbddcc71d997e972a1c6db7964d58b0a9 |
| Huella del libro | 58a588dc54b8077a0f326c75d1601a3b0561b84b1b3d56f5724d6f7b2afbdd67 |
| Modelo pedido / devuelto | claude-opus-5-5 / claude-opus-5-5 |
| Esfuerzo | high |
| Gramática del servidor | True |
| Mensajes enviados | 1 |
| Cota de entrada antes de llamar | 123659 tokens |
| Reserva estimada antes de llamar | USD 1.149996 |
| Uso de tokens | entrada 56361, salida 3039 |
| Coste | CONOCIDO_ESTIMADO; estimado USD 0.286224; cota 0.286224 |

| id | ruta | sha256 | bytes |
|---|---|---|---|
| respuesta | EMPRESAS_LOTES_COMPLETOS/Hermes/Hermes_respuesta.md | 179ad694e610a95c4ab1d77597c96d4165a6c97d879c1ed7ca3d00362d1fc08c | 26522 |
| hoja_analisis | EMPRESAS_LOTES_COMPLETOS/Hermes/Hermes_evaluada.xlsx#Análisis | 877d4da445bba796e4b9ab92f4d07e807586bafd35da514036cdc832da396953 | 22999 |
| hoja_control_maestro | EMPRESAS_LOTES_COMPLETOS/Hermes/Hermes_evaluada.xlsx#Control maestro | 8e9c75b18b454f57177ec4ff62c2ce04389166253769a4b527ac68abbe8094b5 | 53214 |

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

    Control maestro!M51 = 2279 (pasivos por arrendamiento NIIF 16 a 30-jun-2026; incluidos en Análisis!C54 = 2284)


### Tipo de negocio y motor

    Lujo personal de marca (marroquinería, ropa, seda, joyería) con fabricación artesanal propia y venta en tiendas propias al contado; compounder estable sin deuda financiera.
    El DCF de caja libre de la plantilla, porque es un negocio estable que genera caja con flujo predecible, sin deuda y con el exceso de caja tratado aparte (C76).

### calidad

    Es un negocio comprensible de marca y escasez con margen operativo recurrente estable en torno al 40,5–42,1 % (FY21–25) y un ROIC del 22 % con toda la caja (50,6 % sin caja según Control maestro!M29), sin clientes concentrados, sin deuda y con gestión prudente; la dependencia de Asia sin Japón (42 % de las ventas) es la duda principal.
    Dato clave: Análisis!C24 = 0.22

### caja

    La caja libre del accionista ya resta capex, principal de arrendamientos y SBC; es positiva todos los años (2.661 → 3.881 M€ en FY21–25, 4.216 M€ LTM), con una base normalizada de 3.487,3 M€ y una conversión caja operativa/beneficio de 1,16x (C26); los baches de 2023 y 2025 se deben al circulante y al impuesto extraordinario.
    Dato clave: Análisis!C52 = 3487.3

### balance

    La Análisis!C33 = −1,35x incluye arrendamientos y no sirve tal cual; recalculada sin ellos, la deuda financiera es de 5 M€ frente a una caja de 12.310 M€, lo que da una caja neta de 12.305 M€ (−1,75x sobre el EBITDA aproximado previo a la NIIF 16 de 7.029 M€), sin bonos, préstamos ni covenants; el veredicto coincide con el semáforo de la hoja.
    Dato clave: Control maestro!N51 = 5 (deuda financiera sin arrendamientos, M€; deuda neta sin arrendamientos 5 − 12310 = −12305)

### precio

    La cotización de 1.280 € está muy por encima del valor ponderado de 818,7 €, del escenario bueno de 1.191,9 € (D78) y del precio de Sí ≈ 523 € (mínimo entre el escenario malo B78 = 523,3 y 0,75 × 818,7); incluso con r al 7 % el valor ponderado es de 1.194 € (C90), y el DCF inverso exige un 13,7 % de crecimiento (C86), por encima del escenario bueno.
    Dato clave: Análisis!C83 = 818.664803288254 (frente a Análisis!C37 = 1280)

### encaje

    El paquete no trae la cartera de la persona responsable y la hoja solo aporta datos de la empresa, como una capitalización de 134.069,7 M€, sin nada concreto sobre encaje; este filtro no elimina.
    Dato clave: Análisis!C41 = 134069.7

### Qué lo cambiaría

    - Una cotización por debajo de unos 523 € (el escenario malo, Análisis!B78) con el negocio igual pasaría el filtro de precio.
    - Un crecimiento a tipos constantes por debajo del 3 % durante dos años, o un margen bruto por debajo del 67 % sin causa de divisas, pondría en duda la calidad.
    - Que Asia sin Japón (42 % de las ventas) quede plana dos años seguidos rebajaría el escenario normal y el valor ponderado.

### Qué falta

    - El precio de Sí no figura como celda numérica en la hoja: solo aparece el texto estimado ≈ 520 € en Análisis!C104; aquí se recalcula como mín(B78; 0,75×C83) ≈ 523 €.
    - El EBITDA sin NIIF 16 (7.029 M€) es una aproximación etiquetada en Control maestro!N36, no una cifra publicada.
    - La auditoría de Control maestro (filas 88–97) sigue marcada como «Pendiente» aunque los escenarios ya están rellenos, y el precio es del cierre del 7-oct-2026, que la propia hoja pide actualizar.

### Comprobaciones mecánicas y normalizaciones

    {
      "comprobaciones": {
        "avisos": [],
        "nota": "Comprobaciones mecánicas informativas: no acreditan la calidad económica."
      },
      "normalizaciones": []
    }

