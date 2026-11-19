# Cribado · Kongsberg

Estado de la ejecución: `AUDITORIA_DOCUMENTAL_PENDIENTE_ACEPTACION`

Cribado pendiente de revisión humana. No es una recomendación de compra, ni aceptación, ni aptitud para dinero real. Tasa 9 % provisional.

C-ARR (decisión de la persona responsable): los arrendamientos se cuentan una sola vez, en el flujo. El alquiler se resta de la caja libre; la deuda, deuda/EBITDA y deuda/caja libre se miden sin arrendamientos; el pasivo por arrendamientos se muestra aparte, como dato.

Cifras de la etapa 1 tal como las guardó la hoja, a su fecha de análisis; sin las decisiones posteriores (P-O1, P-O2, F1-A/F1-B, D-US1/2, D-WM) ni verificación contra la fuente oficial.

| Campo | Valor |
|---|---|
| Fecha de la hoja | 2026-10-17 |
| Tarea | cribado-44505954250-kongsberg |
| SHA del código | 833cd50a9bba34006519119c72a29c70a1656fb7 |
| Huella del paquete (package_sha256) | b215eb217ba50860bbaf7dc1f303a8e316a2b176d7f60c49c3fb9e90df5d1c08 |
| Huella del envío (bundle_sha256) | 7633ce44874f01012fe446fa93904ac13a4a257b39302197a1bd9e0c36585ced |
| Huella del encargo | 32b5c7f313e61a61fb0f5e68a75b3c44004eb902e97b98720fb98fa8d383e6cf |
| Huella de la Release | 4d30f7352948fe7e7fe3b133386eabedbddcc71d997e972a1c6db7964d58b0a9 |
| Huella del libro | 463a9dcb6de872a72b9c675747b1be2fd91b4f16b30494891db2b044e2b60257 |
| Modelo pedido / devuelto | claude-opus-5-5 / claude-opus-5-5 |
| Esfuerzo | high |
| Gramática del servidor | True |
| Mensajes enviados | 1 |
| Cota de entrada antes de llamar | 140434 tokens |
| Reserva estimada antes de llamar | USD 1.217096 |
| Uso de tokens | entrada 63088, salida 4751 |
| Coste | CONOCIDO_ESTIMADO; estimado USD 0.347372; cota 0.347372 |

| id | ruta | sha256 | bytes |
|---|---|---|---|
| respuesta | EMPRESAS_LOTES_COMPLETOS/Kongsberg/Kongsberg_respuesta.md | e4b38a767cd04c5bc83ca73bd537783fc2a9cf4cf9585acd0f39cea8e604803f | 32992 |
| cambios_v2 | EMPRESAS_LOTES_COMPLETOS/Kongsberg/Kongsberg_cambios_v2.md | c76dcdebe09ba8333044136e8f0480cb9377c0c92058fbd19b9691d35a410642 | 4352 |
| hoja_analisis | EMPRESAS_LOTES_COMPLETOS/Kongsberg/Kongsberg_evaluada.xlsx#Análisis | 0ee54ac88db285e18e6b79270d7f0c51cc023259f2ccdb2493e7ddc4e61f0570 | 23320 |
| hoja_control_maestro | EMPRESAS_LOTES_COMPLETOS/Kongsberg/Kongsberg_evaluada.xlsx#Control maestro | 3f0389c45708c76fe4cd2a6e8610d03685eee9fec1a6fe4cc5fd0c3b24523bf1 | 58687 |

## Salida del modelo (datos, sin acciones ejecutables)

Veredicto `vigilar` · DCF de la plantilla aplica: `dudoso`

| Filtro | Resultado |
|---|---|
| calidad | pasa |
| caja | dudoso |
| balance | pasa |
| precio | no_pasa |
| encaje | no_aplica |

### Pasivo por arrendamientos (dato aparte)

    Control maestro!M51 = 2054 (a 30/06/2026; 417 a corto plazo según Control maestro!M37)


### Tipo de negocio y motor

    Contratista de defensa y aeroespacial (más tecnología marítima y espacial en Discovery) que vende a gobiernos con contratos a precio fijo, anticipos y cartera plurianual; la demanda depende del ciclo de gasto público en defensa.
    Caja normalizada de ciclo medio sin anticipos (antes de variaciones de circulante) o beneficio normalizado sobre la entrega de la cartera, contrastado con el DCF de la plantilla.

### calidad

    El negocio se entiende (sistemas de defensa a gobiernos con anticipos y una cartera de 152.756 MNOK) y muestra un margen EBITDA de Defence & Aerospace del 19-21 % desde 2020 y un ROCE del 57,6 %, aunque ese ROCE está inflado por los anticipos y la demanda depende del ciclo de gasto público y de un Estado con el 50 %.
    Dato clave: Análisis!C24 = 0.576

### caja

    El FCF base de 5.205 MNOK se apoya en anticipos: antes de circulante, la opción C da solo 1.100 MNOK, el FCF del grupo fue −676 en 2022 y el CFO continuado del 1S2026 fue negativo (≈5,2 bn de circulante deshecho); por eso no heredo el ✓ de la hoja en C25 y C26 (1,75, que baja a 0,92 sin saldo contractual).
    Dato clave: Control maestro!N43 = 1100 (FCF normalizado antes de circulante, opción C, frente a Análisis!C52 = 5205)

### balance

    Sin arrendamientos, la deuda es 1.100 MNOK frente a una caja de 4.859, lo que da una deuda neta de unos −3.759 MNOK y unas −0,58x el EBITDA aproximado sin NIIF 16 de 6.482 (el −0,24x de C33 incluye arrendamientos y no se usa tal cual), con covenant de ≤4,75x: holgado incluso para un negocio con algo de ciclo, aunque esa caja es solo el 14 % de los pasivos de contrato (33.879 MNOK).
    Dato clave: Control maestro!N51 = 1100 (deuda sin arrendamientos: bono 1.000 + préstamo 100; caja Análisis!C53 = 4859)

### precio

    A 315,3 NOK, la cotización supera los tres escenarios (50,3 / 121,5 / 202,2 NOK) y el ponderado de 123,4 NOK incluso con r al 7 % (184,0), el DCF inverso exige un 18,7 % anual y el precio de Sí estimado (≈50 NOK) queda unas seis veces por debajo; con una base sin anticipos (1.100 MNOK) estaría aún más cara, así que la duda sobre el motor no cambia la conclusión.
    Dato clave: Análisis!C37 = 315.3 frente a Análisis!B78 = 50.2521447315899 (precio de Sí estimado ≈50)

### encaje

    El paquete no trae la cartera de la persona responsable; la hoja solo aporta datos de mercado, como una capitalización de 277.341 MNOK, sin nada concreto sobre el encaje, y este filtro no elimina.
    Dato clave: Análisis!C41 = 277341

### Qué lo cambiaría

    - Una cotización cerca o por debajo del valor ponderado de unos 123 NOK (más aún hacia el precio de Sí de ≈50 NOK) pasaría el veredicto a estudiar a fondo.
    - Que la caja antes de circulante de la actividad continuada crezca desde 1.770 MNOK hacia unos 3.000 MNOK confirmaría el filtro de caja.
    - Que en el 3T el circulante siga deshaciéndose o el margen EBITDA de defensa caiga por debajo del 17 % haría no pasar el filtro de caja o el de calidad (descartar).

### Qué falta

    - Resultados del 3T 2026 (29/10/2026), posteriores a la fecha de la hoja: indicarán si el circulante sigue deshaciéndose.
    - Precio de Sí exacto: la hoja solo trae la estimación de ≈50 NOK de la respuesta, y el EBITDA sin NIIF 16 (6.482) es una aproximación.
    - Competidores y crecimiento orgánico por programa, que la empresa no publica.

### Comprobaciones mecánicas y normalizaciones

    {
      "comprobaciones": {
        "avisos": [],
        "nota": "Comprobaciones mecánicas informativas: no acreditan la calidad económica."
      },
      "normalizaciones": []
    }

