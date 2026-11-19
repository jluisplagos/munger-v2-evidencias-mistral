# Cribado · Sony

Estado de la ejecución: `AUDITORIA_DOCUMENTAL_PENDIENTE_ACEPTACION`

Cribado pendiente de revisión humana. No es una recomendación de compra, ni aceptación, ni aptitud para dinero real. Tasa 9 % provisional.

C-ARR (decisión de la persona responsable): los arrendamientos se cuentan una sola vez, en el flujo. El alquiler se resta de la caja libre; la deuda, deuda/EBITDA y deuda/caja libre se miden sin arrendamientos; el pasivo por arrendamientos se muestra aparte, como dato.

Cifras de la etapa 1 tal como las guardó la hoja, a su fecha de análisis; sin las decisiones posteriores (P-O1, P-O2, F1-A/F1-B, D-US1/2, D-WM) ni verificación contra la fuente oficial.

| Campo | Valor |
|---|---|
| Fecha de la hoja | 2026-11-08 |
| Tarea | cribado-44512238939-sony |
| SHA del código | 833cd50a9bba34006519119c72a29c70a1656fb7 |
| Huella del paquete (package_sha256) | 4c9e01b88b82d64cfbbe55c8f0d55b2e32f091c4f57b27d2d948bf1974d49c2f |
| Huella del envío (bundle_sha256) | 0bd85eb34db1c9bfa7be8763c48dd154fcb46e303d3ccce58d149e55ea6fb2b0 |
| Huella del encargo | 32b5c7f313e61a61fb0f5e68a75b3c44004eb902e97b98720fb98fa8d383e6cf |
| Huella de la Release | 4d30f7352948fe7e7fe3b133386eabedbddcc71d997e972a1c6db7964d58b0a9 |
| Huella del libro | dee037401f2a77c33f9147f8fb880594f8870361a08776d531cdb79af882e07e |
| Modelo pedido / devuelto | claude-opus-5-5 / claude-opus-5-5 |
| Esfuerzo | high |
| Gramática del servidor | True |
| Mensajes enviados | 1 |
| Cota de entrada antes de llamar | 157494 tokens |
| Reserva estimada antes de llamar | USD 1.285336 |
| Uso de tokens | entrada 69277, salida 4119 |
| Coste | CONOCIDO_ESTIMADO; estimado USD 0.359488; cota 0.359488 |

| id | ruta | sha256 | bytes |
|---|---|---|---|
| respuesta | EMPRESAS_LOTES_COMPLETOS/Sony/Sony_respuesta.md | d06e6fafd0c0b3040fde02d0be049d407911fd1bcec7f613c17adafcea97d14f | 45413 |
| hoja_analisis | EMPRESAS_LOTES_COMPLETOS/Sony/Sony_evaluada.xlsx#Análisis | 62b33a92608b78d9deb10ba7337f709cad5e8f2b5e2a5e86f51cae5d6d488cba | 24914 |
| hoja_control_maestro | EMPRESAS_LOTES_COMPLETOS/Sony/Sony_evaluada.xlsx#Control maestro | 4203f263c46dcf40b2d14046c2be3512e29a89fdb6ee807c7a4da1f8b079476e | 66259 |

## Salida del modelo (datos, sin acciones ejecutables)

Veredicto `vigilar` · DCF de la plantilla aplica: `dudoso`

| Filtro | Resultado |
|---|---|
| calidad | dudoso |
| caja | dudoso |
| balance | pasa |
| precio | no_pasa |
| encaje | no_aplica |

### Pasivo por arrendamientos (dato aparte)

    Control maestro!M36 = 638980 mm (97.956 corrientes + 541.024 no corrientes según Control maestro!M51); no entra en el cociente de deuda.


### Tipo de negocio y motor

    Conglomerado de entretenimiento y tecnología: PlayStation (hardware, contenido digital y servicios de red), música, cine y televisión, electrónica de consumo y sensores de imagen CMOS; la hoja lo clasifica como cíclica/commodity (C14).
    Suma de partes: múltiplos o DCF por segmento para Music y los servicios de red de PlayStation, caja de ciclo medio para sensores, hardware y electrónica, y Pictures por cartera de contenidos; el DCF de grupo de la plantilla solo como contraste.

### calidad

    El negocio se entiende con el paquete y las cifras muestran calidad (ROIC del 15,6% y margen operativo de 9,2% a 11,6% en FY2024-FY2026), pero la ventaja a diez años no se puede verificar (C18 = No: sin cuotas, sin concentración de clientes de sensores y con deterioros como el de Bungie), así que queda en duda; discrepo del «demasiado difícil» de la etapa 1, porque esto es incertidumbre sobre el foso, no un negocio ininteligible.
    Dato clave: Análisis!C24 = 0.156

### caja

    La caja libre base normalizada es positiva (765.306 mm) y la conversión CFO/beneficio es de 1,36x (C26), pero la serie es errática (−174.847 mm en FY2023), el capex en caja de FY2026 (457.681 mm) está muy por debajo del devengado (804.900 mm) y las compras de catálogos (185.000-314.000 mm al año) no pasan por capex ni por CFO, así que no está claro cuánto es recurrente.
    Dato clave: Análisis!C52 = 765306

### balance

    La C33 = 0,026x de la hoja incluye 638.980 mm de arrendamientos y no sirve tal cual; sin ellos, la deuda financiera de 1.447.870 mm queda por debajo de la caja de 2.009.334 mm (caja neta de unos 561.464 mm), así que el cociente es negativo con cualquier EBITDA después de alquiler, sin covenants financieros y con 789,6 bn de líneas no dispuestas.
    Dato clave: Control maestro!N51 = 1447870 (deuda financiera sin arrendamientos, frente a caja Análisis!C53 = 2009334)

### precio

    A 4.142 ¥ la cotización está por encima del valor ponderado de 2.475,6 ¥ (margen de −67%), del escenario bueno de 3.619,2 ¥ e incluso del ponderado con r del 7% (3.549,5 ¥); el DCF inverso exige un 12,4% anual, más que el escenario bueno, aunque la conclusión depende de la base de FCF elegida y el motor de suma de partes no se ha hecho.
    Dato clave: Análisis!C83 = 2475.56429614244

### encaje

    El paquete no trae la cartera de la persona responsable y la hoja solo da datos de la empresa (capitalización de 24.188.642 mm), sin nada concreto sobre concentración o correlación; este filtro no elimina.
    Dato clave: Análisis!C41 = 24188642

### Qué lo cambiaría

    - Una cotización por debajo del valor ponderado de unos 2.476 ¥ (Análisis!C83) con calidad y caja confirmadas llevaría a estudiar a fondo.
    - Que el capex de mantenimiento resulte ser el devengado (unos 804.900 mm) y la caja libre recurrente quede estructuralmente por debajo de la media de cinco años (612.773 mm) haría que la caja no pasara y llevaría a descartar.
    - La publicación de cuotas y de la concentración de clientes de sensores, con una base diversificada, resolvería la duda de calidad.

### Qué falta

    - Concentración de clientes y cuotas de mercado de sensores (I&SS), y unidades de consola y suscriptores de PS Plus posteriores a FY2023.
    - Capex de mantenimiento real (en caja 457.681 frente a 804.900 devengado) y tratamiento de las compras de catálogos fuera de CFO y capex, que decide qué base de FCF es repetible (de 612.773 a 1.483.672 mm).
    - Las decisiones de la base del FCF figuran fechadas el 15-nov-2026, después de la fecha de la hoja (2026-11-08), y la auditoría del modelo (Control maestro filas 90-97) sigue marcada como pendiente aunque el DCF ya está calculado.

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

