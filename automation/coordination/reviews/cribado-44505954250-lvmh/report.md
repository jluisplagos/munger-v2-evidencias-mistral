# Cribado · LVMH

Estado de la ejecución: `AUDITORIA_DOCUMENTAL_PENDIENTE_ACEPTACION`

Cribado pendiente de revisión humana. No es una recomendación de compra, ni aceptación, ni aptitud para dinero real. Tasa 9 % provisional.

C-ARR (decisión de la persona responsable): los arrendamientos se cuentan una sola vez, en el flujo. El alquiler se resta de la caja libre; la deuda, deuda/EBITDA y deuda/caja libre se miden sin arrendamientos; el pasivo por arrendamientos se muestra aparte, como dato.

Cifras de la etapa 1 tal como las guardó la hoja, a su fecha de análisis; sin las decisiones posteriores (P-O1, P-O2, F1-A/F1-B, D-US1/2, D-WM) ni verificación contra la fuente oficial.

| Campo | Valor |
|---|---|
| Fecha de la hoja | 2026-10-25 |
| Tarea | cribado-44505954250-lvmh |
| SHA del código | 833cd50a9bba34006519119c72a29c70a1656fb7 |
| Huella del paquete (package_sha256) | 03dec4a955759b782d47bcc7fe1bfb2ab6b92d4cd945ca7624ce2cb610270106 |
| Huella del envío (bundle_sha256) | 6489ccd0e017d7ab773d39282cc027dd8402e72c84b7cb20fada764cf30afd69 |
| Huella del encargo | 32b5c7f313e61a61fb0f5e68a75b3c44004eb902e97b98720fb98fa8d383e6cf |
| Huella de la Release | 4d30f7352948fe7e7fe3b133386eabedbddcc71d997e972a1c6db7964d58b0a9 |
| Huella del libro | cd69740f08265e80eaab52f27a8d892c830695bf5a3b615adab2a10d6d2b8aff |
| Modelo pedido / devuelto | claude-opus-5-5 / claude-opus-5-5 |
| Esfuerzo | high |
| Gramática del servidor | True |
| Mensajes enviados | 1 |
| Cota de entrada antes de llamar | 156420 tokens |
| Reserva estimada antes de llamar | USD 1.28104 |
| Uso de tokens | entrada 69806, salida 4399 |
| Coste | CONOCIDO_ESTIMADO; estimado USD 0.367204; cota 0.367204 |

| id | ruta | sha256 | bytes |
|---|---|---|---|
| respuesta | EMPRESAS_LOTES_COMPLETOS/LVMH/LVMH_respuesta.md | c1b05496e35bcd5e58f9dbc8590fc004d6e023ea30b5e19aae5f964bd566059b | 43458 |
| hoja_analisis | EMPRESAS_LOTES_COMPLETOS/LVMH/LVMH_evaluada.xlsx#Análisis | 54229e800f96c202ab6c128a3f85529509e940ae4d0b1795b5d618b7844fe204 | 24263 |
| hoja_control_maestro | EMPRESAS_LOTES_COMPLETOS/LVMH/LVMH_evaluada.xlsx#Control maestro | d1e6c229ebfabbece434efd03d887c6597693320807838204378076e532ab088 | 67917 |

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

    Control maestro!M36 = 16261 (pasivos por arrendamiento a 30-jun-2026; deuda bruta con arrendamientos 36745 en Control maestro!N51)


### Tipo de negocio y motor

    Conglomerado de marcas de lujo (moda y marroquinería, vinos y licores, perfumes, relojería y joyería, distribución selectiva) de consumo discrecional, con demanda sensible al ciclo y a Asia.
    El DCF de caja libre de la plantilla, pero partiendo de una caja libre normalizada de mitad de ciclo (margen recurrente en torno al 22%) y contrastado con la caja libre normalizada de fase 1, porque la demanda de lujo y Vinos y Licores tienen componente cíclico.

### calidad

    Negocio entendible de marcas de lujo con margen bruto entre el 64,5% y el 68,8% desde 2017 y un ROIC después de impuestos del 12,5%, por encima del 9%, pero en descenso desde el 19,7% de 2021 y con el margen recurrente pasando del 26,7% al 22,0%; discrepo del «DESCARTAR · demasiado difícil» de Análisis!A6, que nace de C13 = No, una duda de precio y no de comprensión del negocio.
    Dato clave: Análisis!C24 = 0.125

### caja

    La caja libre de la plantilla, ya neta de principal de arrendamientos (2.902 mm) y de SBC, es de 9.790 mm de media y fue positiva todos los años (13.124/10.134/8.046/10.490/11.305 mm en 2021-25 y 11.352 LTM), con conversión CFO/beneficio de 1,37x, aunque no crece desde 2021 y la normalizada está plana (11.601 → 11.682).
    Dato clave: Análisis!C52 = 9790

### balance

    El 1,02x de Análisis!C33 incluye 16.261 mm de arrendamientos y no sirve tal cual; sin ellos, la propia hoja da 8.245 mm de deuda neta sobre un EBITDA sin NIIF 16 estimado en 20.354 mm (0,41x, y 1,29x con los 6.416 mm de compromisos de compra de minoritarios), unas 0,84 veces la caja libre base de 9.790 mm, con caja más activos financieros corrientes de 12.202 mm frente a 7.444 mm de deuda a corto.
    Dato clave: Control maestro!M36 = 8245 (deuda financiera neta sin arrendamientos; deuda bruta sin arrendamientos Análisis!C54 = 20484)

### precio

    La cotización de 383 € está un 64% por encima del valor del escenario malo (233,55 €), que actúa como precio de Sí, y por encima del ponderado (366,35 €); el precio exige crecer un 5,75% anual (Análisis!C86) y, aun con r al 7%, el escenario malo seguiría por debajo de 383 €.
    Dato clave: Análisis!B78 = 233.5470807223

### encaje

    El paquete no trae la cartera de la persona responsable y la hoja solo da datos de la empresa, como una capitalización de 188.328 mm, de modo que no hay base para juzgar el encaje, y este filtro no elimina.
    Dato clave: Análisis!C41 = 188328

### Qué lo cambiaría

    - Una cotización en torno a 234 € o por debajo, con el margen recurrente sostenido cerca del 22%, pasaría el veredicto a estudiar a fondo.
    - Un margen recurrente por debajo del 20% dos años seguidos, o un descenso de la caja libre normalizada con el circulante neutralizado, rebajaría calidad y caja.
    - Que Diageo ejerza su opción de venta, incluida en los 6.416 mm de compromisos de compra de minoritarios, obligaría a rehacer el perímetro y la deuda.

### Qué falta

    - Las decisiones de periodo, ROIC y caja en Control maestro (M29, M37, M43 a M48) llevan fecha 28-oct-2026, posterior a la fecha de la hoja (25-oct-2026), y la auditoría del modelo (filas 90 a 97) sigue marcada como «Pendiente».
    - El EBITDA sin arrendamientos (20.354 mm) es una estimación propia, porque LVMH no publica EBITDA, y la cotización de 383 € procede de fuentes secundarias.
    - No hay ROIC publicado por la empresa, ni cuotas de mercado fuera de Vinos y Licores, ni descomposición del crecimiento en precio y volumen.

### Comprobaciones mecánicas y normalizaciones

    {
      "comprobaciones": {
        "avisos": [],
        "nota": "Comprobaciones mecánicas informativas: no acreditan la calidad económica."
      },
      "normalizaciones": []
    }

