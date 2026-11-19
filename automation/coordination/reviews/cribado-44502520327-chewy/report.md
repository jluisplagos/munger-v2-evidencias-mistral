# Cribado · Chewy

Estado de la ejecución: `AUDITORIA_DOCUMENTAL_PENDIENTE_ACEPTACION`

Cribado pendiente de revisión humana. No es una recomendación de compra, ni aceptación, ni aptitud para dinero real. Tasa 9 % provisional.

C-ARR (decisión de la persona responsable): los arrendamientos se cuentan una sola vez, en el flujo. El alquiler se resta de la caja libre; la deuda, deuda/EBITDA y deuda/caja libre se miden sin arrendamientos; el pasivo por arrendamientos se muestra aparte, como dato.

Cifras de la etapa 1 tal como las guardó la hoja, a su fecha de análisis; sin las decisiones posteriores (P-O1, P-O2, F1-A/F1-B, D-US1/2, D-WM) ni verificación contra la fuente oficial.

| Campo | Valor |
|---|---|
| Fecha de la hoja | 2026-10-10 |
| Tarea | cribado-44502520327-chewy |
| SHA del código | 833cd50a9bba34006519119c72a29c70a1656fb7 |
| Huella del paquete (package_sha256) | 75d17d96ca5f32099c7501fea7354b10a390fc549d7a7bcb40011c8ecb990a95 |
| Huella del envío (bundle_sha256) | e6880ad60a2366aaaed599ae25b199d2bcaa8b8bf9ee00ef9e7b5b5549a558c9 |
| Huella del encargo | 32b5c7f313e61a61fb0f5e68a75b3c44004eb902e97b98720fb98fa8d383e6cf |
| Huella de la Release | 4d30f7352948fe7e7fe3b133386eabedbddcc71d997e972a1c6db7964d58b0a9 |
| Huella del libro | 7e800850c14e3ddd85b78bf731b68dcabb96c10adb786978f9fd0d6429a6225a |
| Modelo pedido / devuelto | claude-opus-5-5 / claude-opus-5-5 |
| Esfuerzo | high |
| Gramática del servidor | True |
| Mensajes enviados | 1 |
| Cota de entrada antes de llamar | 140317 tokens |
| Reserva estimada antes de llamar | USD 1.216628 |
| Uso de tokens | entrada 63509, salida 4074 |
| Coste | CONOCIDO_ESTIMADO; estimado USD 0.335516; cota 0.335516 |

| id | ruta | sha256 | bytes |
|---|---|---|---|
| respuesta | EMPRESAS_LOTES_COMPLETOS/Chewy/Chewy_respuesta.md | 4bbcd7418f5c562a73056aeab161a5df7ed9ea596d7d7340a8aa426b5392f300 | 34213 |
| cambios_v2 | EMPRESAS_LOTES_COMPLETOS/Chewy/Chewy_cambios_v2.md | 7ec05d60a9bf31f96f4ff18bfaa3393ce880515d136fdabb673de3a83f7fcd84 | 4201 |
| hoja_analisis | EMPRESAS_LOTES_COMPLETOS/Chewy/Chewy_evaluada.xlsx#Análisis | 1de5e15b135da9e5cebc5caac262dec7916f3127515a4607f33f974f56248bfa | 23397 |
| hoja_control_maestro | EMPRESAS_LOTES_COMPLETOS/Chewy/Chewy_evaluada.xlsx#Control maestro | 57790f656d2aff5c942c054c08d58a1eca1c0b4e46c21cfcda22755dd9eaae69 | 57423 |

## Salida del modelo (datos, sin acciones ejecutables)

Veredicto `vigilar` · DCF de la plantilla aplica: `si`

| Filtro | Resultado |
|---|---|
| calidad | dudoso |
| caja | pasa |
| balance | pasa |
| precio | no_pasa |
| encaje | no_aplica |

### Pasivo por arrendamientos (dato aparte)

    Control maestro!N36 = 569.5 (pasivos por operating leases; deuda con arrendamientos 1.169,5 en Control maestro!N51, solo como contexto)


### Tipo de negocio y motor

    Comercio minorista online de consumibles recurrentes para mascotas (comida, salud y farmacia), con suscripción Autoship y circulante negativo; un solo segmento en EE. UU. y Canadá.
    El DCF de caja libre al accionista de la plantilla (tras SBC), con el FCF base normalizado por impuestos en caja e intereses del term loan.

### calidad

    Es un negocio entendible de consumibles recurrentes (Autoship 83 %) con un margen bruto al alza siete años seguidos y un ROIC LTM del 16 %, pero el margen operativo GAAP no ha pasado del 2,0 % en diez años, el ROIC medio de cinco años es del 3,8 %, la SBC (297,9) supera al resultado operativo (254,3) y los tres mayores proveedores suponen el 39 % de las ventas, así que la ventaja no se ve todavía en las cifras.
    Dato clave: Análisis!C24 = 0.16 (ROIC LTM; media de cinco años ≈3,8 % según la nota de Control maestro!N29)

### caja

    La caja libre tras SBC es positiva y creciente (FCF base de 171,5 con la media FY23–25 y 270,2 LTM, frente a -38,6 en FY22), pero la SBC consume el 62 % del FCF, hay pocos años de historial positivo y la ayudan unos impuestos casi nulos (23,3 en FY25) y unos intereses del term loan (unos 25 netos al año) que aún no recoge.
    Dato clave: Análisis!C52 = 171.5

### balance

    Sin arrendamientos, la deuda es el term loan de 600 frente a 611 de caja, lo que da una caja neta de unos 11 y una deuda neta/EBITDA GAAP LTM (472,1, que ya resta el alquiler) de -0,02x, con vencimiento en 2033 y el ABL de 800 sin disponer; ojo: esa caja existe solo porque el préstamo de junio de 2026 financió 552,8 de adquisiciones y 400 de recompras (sin él sería de unos 19).
    Dato clave: Análisis!C54 = 600 (deuda sin arrendamientos: term loan) frente a Análisis!C53 = 611 de caja; Análisis!C33 = -0.023

### precio

    La cotización de 18,95 está muy por encima del valor ponderado de 10,72 y del escenario bueno de 18,15, no hay precio de Sí (la referencia de la etapa 1 es de unos 5,1) y el DCF inverso exige un crecimiento del 16,3 % frente al 15 % del escenario bueno; ni con r al 7 % (16,16 ponderado) llega al precio, así que el resultado no cambia con ±2 puntos de tasa.
    Dato clave: Análisis!C83 = 10.7167830079001 frente a Análisis!C37 = 18.95

### encaje

    El paquete no trae la cartera de la persona responsable y la hoja solo recoge un tamaño de etapa 1 (0 %) que no se hereda, así que no se puede juzgar el encaje.
    Dato clave: Análisis!C104 = 0% · No · sin precio de Sí (dato de la etapa 1, no usado)

### Qué lo cambiaría

    - Una cotización igual o inferior al valor ponderado de la hoja (unos 10,7 USD), o en la zona de ¾ de ese valor (unos 8), con las mismas hipótesis, que llevaría el veredicto a estudiar_a_fondo.
    - Tres años con un margen del dueño (FCF tras SBC, con impuestos e intereses normales) de al menos el 3 % de las ventas, que haría pasar el filtro de calidad.
    - Más deuda para recompras o adquisiciones, o un FCF tras SBC LTM por debajo de 171,5 con ventas creciendo, que llevaría a descartar.

### Qué falta

    - Impuestos en caja normalizados: cuándo se agotan las pérdidas fiscales federales de 82,8 y el efecto de la OBBBA (el ajuste de unos 50 al año es una estimación).
    - Competidores y cuota de mercado: el paquete no nombra a ningún rival, y eso es clave para juzgar la ventaja competitiva.
    - Economía y precio pagado por Modern Animal (goodwill de 221,6), y retorno de las adquisiciones de H1 FY26 (552,8).

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

