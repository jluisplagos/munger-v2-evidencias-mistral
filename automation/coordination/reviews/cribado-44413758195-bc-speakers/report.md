# Cribado · BC_Speakers

Estado de la ejecución: `AUDITORIA_DOCUMENTAL_PENDIENTE_ACEPTACION`

Cribado pendiente de revisión humana. No es una recomendación de compra, ni aceptación, ni aptitud para dinero real. Tasa 9 % provisional.

C-ARR (decisión de la persona responsable): los arrendamientos se cuentan una sola vez, en el flujo. El alquiler se resta de la caja libre; la deuda, deuda/EBITDA y deuda/caja libre se miden sin arrendamientos; el pasivo por arrendamientos se muestra aparte, como dato.

Cifras de la etapa 1 tal como las guardó la hoja, a su fecha de análisis; sin las decisiones posteriores (P-O1, P-O2, F1-A/F1-B, D-US1/2, D-WM) ni verificación contra la fuente oficial.

| Campo | Valor |
|---|---|
| Fecha de la hoja | 2026-10-30 |
| Tarea | cribado-44413758195-bc-speakers |
| SHA del código | 833cd50a9bba34006519119c72a29c70a1656fb7 |
| Huella del paquete (package_sha256) | f8b84d03a9e1491cefcbef1163ba7ae14c9ab55e4e537055e0dd0a428d967ce8 |
| Huella del envío (bundle_sha256) | f6bbd7afac80cd7076851726d782fed6166a60d0a491b97476bd9d815c418e0d |
| Huella del encargo | 32b5c7f313e61a61fb0f5e68a75b3c44004eb902e97b98720fb98fa8d383e6cf |
| Huella de la Release | 4d30f7352948fe7e7fe3b133386eabedbddcc71d997e972a1c6db7964d58b0a9 |
| Huella del libro | 6dec0358147a22ccb869956237ff420bdd780605420350a63a1597fad309cf59 |
| Modelo pedido / devuelto | claude-opus-5-5 / claude-opus-5-5 |
| Esfuerzo | high |
| Gramática del servidor | True |
| Mensajes enviados | 1 |
| Cota de entrada antes de llamar | 123655 tokens |
| Reserva estimada antes de llamar | USD 1.14998 |
| Uso de tokens | entrada 56435, salida 3837 |
| Coste | CONOCIDO_ESTIMADO; estimado USD 0.30248; cota 0.30248 |

| id | ruta | sha256 | bytes |
|---|---|---|---|
| respuesta | EMPRESAS_LOTES_COMPLETOS/BC_Speakers/BC_Speakers_respuesta.md | 43ce9998e15daba6d076204249d85fcfc174b4aad333dcedbfeaf36b0eb4f6d9 | 30813 |
| hoja_analisis | EMPRESAS_LOTES_COMPLETOS/BC_Speakers/BC_Speakers_evaluada.xlsx#Análisis | a1416321c52c8aa70b4807dbca8681bda357824e8bd85a1d6f70293973c2f0e1 | 22990 |
| hoja_control_maestro | EMPRESAS_LOTES_COMPLETOS/BC_Speakers/BC_Speakers_evaluada.xlsx#Control maestro | 02361893890abc1f51b4435dee1a61fae7a2bffbc82081ba594fe7e8acf3fb31 | 48848 |

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

    Control maestro!M51 = 4.783 (pasivo por arrendamientos a 30-jun-26, incluido en la deuda total de Análisis!C54 = 25.362)


### Tipo de negocio y motor

    Fabricante industrial cíclico de componentes (transductores de audio profesional) que vende a pocos fabricantes OEM, con un solo segmento y plantas en Italia, EE. UU. y China.
    DCF de la plantilla alimentado con caja libre de ciclo medio tras arrendamientos (entre la media de cinco años, 6,6 mm, y el normalizado sin circulante, ≈9,15 mm), porque el FCF base cambia mucho según la ventana en un fabricante cíclico.

### calidad

    El ROCE del 25,4 % (serie 10–46 %) y el goodwill del 2,54 % apuntan a calidad, pero el margen EBIT cae del 22,1 % al 16,4 %, dos clientes OEM sin contrato pesan el 21 % y el 10 % y no se nombran competidores; el negocio se entiende, la duración de la ventaja no está demostrada (la etapa 1 lo llevó a demasiado difícil; aquí queda como duda que el estudio puede resolver).
    Dato clave: Análisis!C24 = 0.254

### caja

    La caja libre tras arrendamientos es positiva en el periodo LTM (7,479 mm, C52), pero la conversión CFO/beneficio es de 0,811 (<0,9), la media de cinco años (6,637 mm) no creció en una década, el flujo fue de ≈0 y −0,37 mm en 2021–22 por el circulante, y el inventario sube un +11,8 % con ventas a −7,2 %.
    Dato clave: Análisis!C26 = 0.811

### balance

    La deuda/EBITDA de 0,27x (Análisis!C33) incluye arrendamientos; sin ellos, la deuda bancaria de 20,579 mm frente a caja de 14,245 mm y valores de 6,384 mm deja una caja neta de unos 0,05 mm (≈0x sobre un EBITDA tras alquiler aproximado de 15,67 mm, o 0,40x contando solo la caja), sin covenants y con vencimientos hasta dic-2030; pasa incluso para un negocio cíclico, aunque parte de los valores está pignorada.
    Dato clave: Control maestro!N51 = 20.579 (deuda bancaria sin arrendamientos)

### precio

    La cotización de 11,5 € casi duplica el precio de Sí de referencia (≈5,7 €, escenario malo, C78 = 5,67) y apenas está por debajo del ponderado de 11,92 € (margen del 3,5 %); aunque con r del 7 % el ponderado sube a 17,05 € y con un FCF de ciclo medio de ≈9,15 mm quedaría cerca de 14,6 €, sigue claramente por encima de cualquier precio de Sí razonable.
    Dato clave: Análisis!C37 = 11.5

### encaje

    El paquete no trae la cartera de la persona responsable y la hoja solo aporta datos de la empresa (capitalización de 125,25 mm), así que este filtro no se aplica y no elimina.
    Dato clave: Análisis!C41 = 125.25

### Qué lo cambiaría

    - Una cotización en la zona de ≈5,7–8,9 € (escenario malo o ¾ del ponderado) haría pasar el precio y llevaría a estudiar a fondo.
    - Una caja libre tras arrendamientos superior a 9 mm dos años seguidos con ventas planas resolvería la duda de caja.
    - La pérdida o el recorte confirmado de un cliente grande, o un margen EBIT por debajo del 14 % un año completo, llevaría a descartar.

### Qué falta

    - Identidad, antigüedad y riesgo de integración vertical de los dos clientes OEM principales (21 % y 10 %), y el competidor más relevante con su cuota.
    - EBITDA sin NIIF 16 verificado (la hoja da ≈15,67 mm como aproximación) e importe de los valores pignorados, que afecta a la caja neta.
    - Evolución del inventario y del circulante en el 2S26 (la hoja llega a jun-26).

### Comprobaciones mecánicas y normalizaciones

    {
      "comprobaciones": {
        "avisos": [
          "Filtro balance: motivo de más de 400 caracteres."
        ],
        "nota": "Comprobaciones mecánicas informativas: no acreditan la calidad económica."
      },
      "normalizaciones": []
    }

