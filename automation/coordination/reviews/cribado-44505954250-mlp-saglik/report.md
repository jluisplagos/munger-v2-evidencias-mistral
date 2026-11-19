# Cribado · MLP_Saglik

Estado de la ejecución: `AUDITORIA_DOCUMENTAL_PENDIENTE_ACEPTACION`

Cribado pendiente de revisión humana. No es una recomendación de compra, ni aceptación, ni aptitud para dinero real. Tasa 9 % provisional.

C-ARR (decisión de la persona responsable): los arrendamientos se cuentan una sola vez, en el flujo. El alquiler se resta de la caja libre; la deuda, deuda/EBITDA y deuda/caja libre se miden sin arrendamientos; el pasivo por arrendamientos se muestra aparte, como dato.

Cifras de la etapa 1 tal como las guardó la hoja, a su fecha de análisis; sin las decisiones posteriores (P-O1, P-O2, F1-A/F1-B, D-US1/2, D-WM) ni verificación contra la fuente oficial.

| Campo | Valor |
|---|---|
| Fecha de la hoja | 31/10/2026 |
| Tarea | cribado-44505954250-mlp-saglik |
| SHA del código | 833cd50a9bba34006519119c72a29c70a1656fb7 |
| Huella del paquete (package_sha256) | dcd0e081d0eb299dd603cce29742a3a29a47eb2cab1b537becc1c4c8b7bd552c |
| Huella del envío (bundle_sha256) | cb325ce8f1e552561caee3123a0a3247f3aba794f6c6ad416329e9ef39958790 |
| Huella del encargo | 32b5c7f313e61a61fb0f5e68a75b3c44004eb902e97b98720fb98fa8d383e6cf |
| Huella de la Release | 4d30f7352948fe7e7fe3b133386eabedbddcc71d997e972a1c6db7964d58b0a9 |
| Huella del libro | 5fc0ea4edacd6ccdba4718244ed5b9c143395ecc66aac8fa2469a7596377d908 |
| Modelo pedido / devuelto | claude-opus-5-5 / claude-opus-5-5 |
| Esfuerzo | high |
| Gramática del servidor | True |
| Mensajes enviados | 1 |
| Cota de entrada antes de llamar | 131899 tokens |
| Reserva estimada antes de llamar | USD 1.182956 |
| Uso de tokens | entrada 59771, salida 5121 |
| Coste | CONOCIDO_ESTIMADO; estimado USD 0.341504; cota 0.341504 |

| id | ruta | sha256 | bytes |
|---|---|---|---|
| respuesta | EMPRESAS_LOTES_COMPLETOS/MLP_Saglik/MLP_Saglik_respuesta.md | e2964913f66c364a1f18c733b0c09b19c4c8654edaa13e48f3599d93a28d1ff5 | 34528 |
| hoja_analisis | EMPRESAS_LOTES_COMPLETOS/MLP_Saglik/MLP_Saglik_evaluada.xlsx#Análisis | 9f90a9ec2feca6bf4367393d6e8b6b722268201f1b8bed16d6ccd022d062032d | 23283 |
| hoja_control_maestro | EMPRESAS_LOTES_COMPLETOS/MLP_Saglik/MLP_Saglik_evaluada.xlsx#Control maestro | ea5e050d43d6958724e5c62123d2b47ee8e461f2c367c3ede7162d85befb547e | 53332 |

## Salida del modelo (datos, sin acciones ejecutables)

Veredicto `faltan_datos` · DCF de la plantilla aplica: `dudoso`

| Filtro | Resultado |
|---|---|
| calidad | dudoso |
| caja | dudoso |
| balance | pasa |
| precio | dudoso |
| encaje | no_aplica |

### Pasivo por arrendamientos (dato aparte)

    Control maestro!M51 = 8313.4 (pasivo por arrendamientos a 30.06.2026, mm TL; incluido en la deuda bruta de Análisis!C54 = 21506.2)


### Tipo de negocio y motor

    Operador de hospitales privados en Turquía (servicios hospitalarios cobrados sobre todo a la SGK y a aseguradoras), con contabilidad de hiperinflación (IAS 29) y fase de expansión por capex y adquisiciones.
    Un DCF de caja libre antes de financiación en TL constantes (IAS 29), con capex de mantenimiento normalizado y la deuda sin arrendamientos restada aparte, en lugar del flujo del accionista neto de intereses nominales en hiperinflación.

### calidad

    El negocio se entiende (unos 30 hospitales privados, margen operativo estable del 17,5–19,5 % y 17,6 % LTM), pero el ROCE antes de impuestos cae del 19,4 % al 14,7 % LTM (≈11 % después de impuestos), el pagador principal es la SGK con un reparto de ingresos desconocido y los anticipos de inmovilizado a vinculadas suben de 2.163 a 4.031 mm; no lo considero ininteligible, a diferencia del «demasiado difícil» de la etapa 1, sino de calidad no demostrada.
    Dato clave: Análisis!C24 = 0.147

### caja

    La conversión CFO/beneficio es buena (1,38x en Análisis!C26) y antes de intereses la caja LTM sigue positiva (15.807 − 10.068 − 2.886 ≈ 2.853), pero el FCF del accionista pasa de 3.779 en 2023 a −3.724 en 2025 y −3.951 LTM por capex de expansión e intereses nominales en TL, sin capex de mantenimiento verificado en fuente primaria.
    Dato clave: Análisis!C40 = -3951

### balance

    El 0,7x de Análisis!C33 incluye arrendamientos (8.313,4) y no sirve tal cual; la hoja no publica el EBITDA tras alquiler, pero aproximándolo como 18.951 menos el principal de arrendamientos LTM de 2.886 da unos 16.065, de modo que la deuda neta sin arrendamientos de 4.936,9 queda en torno a 0,3x (algo más si se restaran también los intereses de arrendamientos, 1.089 solo en 6M26), muy por debajo de cualquier límite prudente; el bono de 6.000 de septiembre de 2026 eleva la cobertura de la deuda a corto de 0,75x a unos 1,29x pro forma frente al vencimiento de 7.000 en junio de 2027, aunque la deuda es TL a tipo variable.
    Dato clave: Control maestro!N36 = 4936.9 (deuda neta sin arrendamientos; deuda bruta sin arrendamientos Control maestro!N51 = 13192.8)

### precio

    Con el DCF de la plantilla, la cotización de 379 TL duplica el valor ponderado de 189,4, supera el escenario bueno (302,0) y queda por encima incluso con r al 7 % (máximo 295,8), con un DCF inverso que exige un 15,7 % de crecimiento anual; pero ese DCF mide sobre todo la financiación (C62 = «No · financiación cambia mucho») y el EV/EBITDA de 4,58x apunta en sentido contrario, así que no concluyo hasta tener un FCF real antes de financiación.
    Dato clave: Análisis!C43 = 189.403779490274

### encaje

    El paquete no trae la cartera de la persona responsable (solo la cotización de 379 TL), así que este filtro no se evalúa y no elimina.
    Dato clave: Análisis!C37 = 379

### Qué lo cambiaría

    - Memoria y notas que confirmen un capex de mantenimiento cercano al 3,9 % de las ventas y un FCF real antes de financiación claramente positivo y estable.
    - FCF del accionista de 2026 completo de nuevo negativo, o ROCE antes de impuestos que siga cayendo por debajo del 14,7 %.
    - Que los anticipos a vinculadas resulten pagos por activos por encima de mercado, o una refinanciación cara del bono de 7.000 mm que vence en junio de 2027.

### Qué falta

    - Reparto de ingresos por pagador (SGK, aseguradoras, privados) y mecanismo de tarifas de la SGK: sin memoria anual ni notas.
    - Capex de mantenimiento en fuente primaria (hoy solo el ~3,9 % de ventas de la dirección, fuente secundaria) y destino y precio de los anticipos de inmovilizado a vinculadas (2.163 → 4.031 mm).
    - EBITDA sin NIIF 16 o intereses de arrendamientos LTM completos, para cerrar la deuda neta/EBITDA sin arrendamientos, que ahora es aproximada.

### Comprobaciones mecánicas y normalizaciones

    {
      "comprobaciones": {
        "avisos": [
          "Filtro calidad: motivo de más de 400 caracteres.",
          "Filtro balance: motivo de más de 400 caracteres.",
          "Filtro precio: motivo de más de 400 caracteres."
        ],
        "nota": "Comprobaciones mecánicas informativas: no acreditan la calidad económica."
      },
      "normalizaciones": []
    }

