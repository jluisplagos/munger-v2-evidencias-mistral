# Cribado · Roche

Estado de la ejecución: `AUDITORIA_DOCUMENTAL_PENDIENTE_ACEPTACION`

Cribado pendiente de revisión humana. No es una recomendación de compra, ni aceptación, ni aptitud para dinero real. Tasa 9 % provisional.

C-ARR (decisión de la persona responsable): los arrendamientos se cuentan una sola vez, en el flujo. El alquiler se resta de la caja libre; la deuda, deuda/EBITDA y deuda/caja libre se miden sin arrendamientos; el pasivo por arrendamientos se muestra aparte, como dato.

Cifras de la etapa 1 tal como las guardó la hoja, a su fecha de análisis; sin las decisiones posteriores (P-O1, P-O2, F1-A/F1-B, D-US1/2, D-WM) ni verificación contra la fuente oficial.

| Campo | Valor |
|---|---|
| Fecha de la hoja | 2026-10-26 |
| Tarea | cribado-44512238939-roche |
| SHA del código | 833cd50a9bba34006519119c72a29c70a1656fb7 |
| Huella del paquete (package_sha256) | 46a0419547d8fd8ad9af5bce83977ee048be3149cc7ad85c99dc090280cf0123 |
| Huella del envío (bundle_sha256) | 24d59bc449724f74dca17903c23fb738cbfe4e714771fc2343764dd786dfdaa7 |
| Huella del encargo | 32b5c7f313e61a61fb0f5e68a75b3c44004eb902e97b98720fb98fa8d383e6cf |
| Huella de la Release | 4d30f7352948fe7e7fe3b133386eabedbddcc71d997e972a1c6db7964d58b0a9 |
| Huella del libro | 245b39fd1c99f6630ebaa9a6697d2d1c2a075201419022ef20106020690ec1d4 |
| Modelo pedido / devuelto | claude-opus-5-5 / claude-opus-5-5 |
| Esfuerzo | high |
| Gramática del servidor | True |
| Mensajes enviados | 1 |
| Cota de entrada antes de llamar | 179020 tokens |
| Reserva estimada antes de llamar | USD 1.37144 |
| Uso de tokens | entrada 80695, salida 4650 |
| Coste | CONOCIDO_ESTIMADO; estimado USD 0.41578; cota 0.41578 |

| id | ruta | sha256 | bytes |
|---|---|---|---|
| respuesta | EMPRESAS_LOTES_COMPLETOS/Roche/Roche_respuesta.md | b123f99c4124ae7169f310653bcecaa19d6a17b38a8b9ce5641ab4a20155a348 | 35070 |
| hoja_analisis | EMPRESAS_LOTES_COMPLETOS/Roche/Roche_evaluada.xlsx#Análisis | c2eb7307bdc7494788b2e9c7b13f5bee9435f31a37bd303ffe8b471365e5f9c5 | 23412 |
| hoja_control_maestro | EMPRESAS_LOTES_COMPLETOS/Roche/Roche_evaluada.xlsx#Control maestro | 93b6b46b79a3acd1a22ee54a3a4f21535834559f1c7288ce7f4c9315940724c4 | 99486 |

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

    Control maestro!N46 = 1503 (pasivo por arrendamientos a 30-06-2026; 1.555 a 31-12-2025), fuera del cociente de deuda


### Tipo de negocio y motor

    Farmacéutica innovadora con patentes (77,5 % de las ventas) y diagnóstico in vitro (22,5 %); negocio estable pero dependiente de renovar exclusividades
    El DCF de caja libre de la plantilla, con escenarios construidos producto a producto según las fechas de pérdida de exclusividad y la conversión de la tubería en ventas.

### calidad

    El ROIC después de impuestos es del 28,9 % (serie 25-32 % en 2021-2025), con márgenes IFRS estables en un rango de 2,9 puntos y once años de crecimiento a tipos constantes; el paquete permite entender el negocio, así que discrepo del «demasiado difícil» de la etapa 1, aunque la renovación de las patentes de Ocrevus, Hemlibra y Vabysmo (un tercio de Pharma) es una duda que tendría que resolver el estudio a fondo.
    Dato clave: Análisis!C24 = 0.289

### caja

    El FCF base neto de SBC es de 11.886 mm, con un CFO estable entre 16.095 y 20.976 y una conversión de 1,47x (1,38x si se reclasifican intereses y arrendamientos), aunque el FCF no crece (C25 = No) y los minoritarios de Chugai le restarían entre un 5 % y un 8 %.
    Dato clave: Análisis!C52 = 11886

### balance

    La deuda neta sin arrendamientos de 22.071 mm, frente a un EBITDA LTM de 22.710 menos unos 406 de pagos por arrendamiento (≈22.300; Roche no publica el EBITDA previo a la NIIF 16), da ≈1,0x, y frente al FCF base de 11.886 da ≈1,9x, holgado para un negocio estable con rating AA; el 1,04x de C33 incluye arrendamientos y no se usa tal cual, y queda por vigilar que la deuda neta subió un 36,6 % en el semestre y que la caja cubre solo 0,83x la deuda a corto (6.583), con una línea comprometida de 7.500 M USD como respaldo.
    Dato clave: Análisis!C54 = 31805 (deuda bruta sin arrendamientos; deuda neta sin arrendamientos 31.805 − 5.448 − 4.286 = 22.071)

### precio

    La cotización de 390,9 está muy por encima del valor ponderado de 239,1 y del escenario bueno de 351,9, e incluso con r al 7 % y g + 0,5 puntos el valor (365,2) sigue por debajo; el DCF inverso exige un crecimiento del 10,0 % frente al 3 % histórico, lo que coincide con la etapa 1.
    Dato clave: Análisis!C83 = 239.07980483204

### encaje

    El paquete no trae la cartera; la hoja solo recoge un plan de cartera de la etapa 1 (C104), que no se hereda, y el valor ponderado de 239,1 no cambia nada en este filtro.
    Dato clave: Análisis!C104 = 0% · Demasiado difícil · sin posición (dato de la etapa 1, no se usa)

### Qué lo cambiaría

    - Una cotización por debajo del valor ponderado de la hoja (≈239 CHF), que llevaría el precio a cerca o a pasa.
    - Fechas de exclusividad de Ocrevus o Hemlibra anteriores a 2030, o ventas de Pharma a tipos constantes a la baja dos años seguidos tras los biosimilares de Xolair (pondría en duda la calidad).
    - Una deuda neta sin arrendamientos por encima de unas 2x el EBITDA, o que siga subiendo para pagar el dividendo y las adquisiciones.

### Qué falta

    - Fechas de pérdida de exclusividad por producto y región de Ocrevus, Hemlibra y Vabysmo; la hoja las marca como no verificadas.
    - Un EBITDA previo a la NIIF 16 publicado: el cociente sin arrendamientos (≈1,0x) es una aproximación propia que resta los pagos de arrendamiento.
    - FCF atribuible a Roche sin los minoritarios de Chugai (38,9 %): solo hay una horquilla de entre un -5 % y un -8 %.

### Comprobaciones mecánicas y normalizaciones

    {
      "comprobaciones": {
        "avisos": [
          "Filtro calidad: motivo de más de 400 caracteres.",
          "Filtro balance: motivo de más de 400 caracteres."
        ],
        "nota": "Comprobaciones mecánicas informativas: no acreditan la calidad económica."
      },
      "normalizaciones": []
    }

