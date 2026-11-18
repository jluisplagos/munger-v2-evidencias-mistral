# Cribado · Betsson

Estado de la ejecución: `AUDITORIA_DOCUMENTAL_PENDIENTE_ACEPTACION`

Cribado pendiente de revisión humana. No es una recomendación de compra, ni aceptación, ni aptitud para dinero real. Tasa 9 % provisional.

C-ARR (decisión de la persona responsable): los arrendamientos se cuentan una sola vez, en el flujo. El alquiler se resta de la caja libre; la deuda, deuda/EBITDA y deuda/caja libre se miden sin arrendamientos; el pasivo por arrendamientos se muestra aparte, como dato.

Cifras de la etapa 1 tal como las guardó la hoja, a su fecha de análisis; sin las decisiones posteriores (P-O1, P-O2, F1-A/F1-B, D-US1/2, D-WM) ni verificación contra la fuente oficial.

| Campo | Valor |
|---|---|
| Fecha de la hoja | 2026-10-25 |
| Tarea | cribado-44413758195-betsson |
| SHA del código | 833cd50a9bba34006519119c72a29c70a1656fb7 |
| Huella del paquete (package_sha256) | b61b4e938e28bac1721ba7b19e1dcb932c2d7f4723b8dd78c22dde2ccdf65ba2 |
| Huella del envío (bundle_sha256) | 4167e792a8d973dc1035d024662f6437d147a433d784d4745cf8976a87a3d6cf |
| Huella del encargo | 32b5c7f313e61a61fb0f5e68a75b3c44004eb902e97b98720fb98fa8d383e6cf |
| Huella de la Release | 4d30f7352948fe7e7fe3b133386eabedbddcc71d997e972a1c6db7964d58b0a9 |
| Huella del libro | faf7c5ae94fc10a757e4a4632f5f132199380481cdf4183dcacf533b74cd45da |
| Modelo pedido / devuelto | claude-opus-5-5 / claude-opus-5-5 |
| Esfuerzo | high |
| Gramática del servidor | True |
| Mensajes enviados | 1 |
| Cota de entrada antes de llamar | 166926 tokens |
| Reserva estimada antes de llamar | USD 1.323064 |
| Uso de tokens | entrada 74312, salida 4325 |
| Coste | CONOCIDO_ESTIMADO; estimado USD 0.383748; cota 0.383748 |

| id | ruta | sha256 | bytes |
|---|---|---|---|
| respuesta | EMPRESAS_LOTES_COMPLETOS/Betsson/Betsson_respuesta.md | a637521a9b8d5de0c31b535a496053b5b9414649c86789ab835344b08e01c331 | 50977 |
| hoja_analisis | EMPRESAS_LOTES_COMPLETOS/Betsson/Betsson_evaluada.xlsx#Análisis | 2334efd015826843243656d07a81b6994b4dd90511a853a8a18e5c4f3a5b94a1 | 24973 |
| hoja_control_maestro | EMPRESAS_LOTES_COMPLETOS/Betsson/Betsson_evaluada.xlsx#Control maestro | 93c36358990165f8b3ab1e7c0e88f458bd4c162d890f252d75a235e67f7d2ced | 69828 |

## Salida del modelo (datos, sin acciones ejecutables)

Veredicto `estudiar_a_fondo` · DCF de la plantilla aplica: `si`

| Filtro | Resultado |
|---|---|
| calidad | dudoso |
| caja | pasa |
| balance | pasa |
| precio | dudoso |
| encaje | no_aplica |

### Pasivo por arrendamientos (dato aparte)

    Control maestro!M36 = 27.9 (arrendamientos 4,2 corrientes + 23,7 no corrientes, según Control maestro!M51)


### Tipo de negocio y motor

    Operador de juego online regulado (casino y apuestas B2C, más plataforma B2B), con márgenes condicionados por impuestos al juego y licencias país por país.
    El DCF de caja libre de la plantilla con base LTM y escenarios regulatorios explícitos (impuestos al juego y cierres de mercado), contrastado con el P/FCF histórico de 8,6x.

### calidad

    El negocio se entiende y el ROCE del 17 % sigue por encima del 15 %, pero ha bajado desde el 25,9 %. Además, el margen bruto se comprime del 65,3 % al 55,5 %, la etapa 1 no ve foso (C18 = No), el B2B depende de un cliente y la base fiscal la fijan los Estados. Es una duda que debe resolver el estudio; no la convierto en «demasiado difícil» como hizo la etapa 1.
    Dato clave: Análisis!C24 = 0.17

### caja

    La caja libre base después de alquileres y SBC es positiva, 111,8, con una conversión de caja operativa sobre beneficio de 1,374x (Análisis!C26). La serie normalizada ha sido positiva todos los años (103,0/119,4/186,8/200,4/185,9/111,1), pero cae casi un 45 % desde el pico de 2024 mientras el capex sube a 72,3 (frente a 52,0 de media a tres años).
    Dato clave: Análisis!C52 = 111.8

### balance

    Sin arrendamientos, la deuda son los bonos (173,8) frente a una caja de 284,7 (Análisis!C53), es decir, caja neta de unos 110,9 y −0,48x sobre el EBITDA preNIIF 16 aproximado de 232,4 (Control maestro!N36). El bono de 2027 (99,6) está cubierto 2,74x por la caja, sin test de mantenimiento. Conviene vigilar que la matriz emisora solo tenga 28,6 de caja.
    Dato clave: Control maestro!M51: bonos 99,6 + 74,2 = 173.8 sin arrendamientos (Análisis!C54 = 201.7 incluye 27,9 de arrendamientos)

### precio

    La cotización de 8,8986 está un 32 % por encima del valor del escenario malo de la hoja, 6,73, que es la referencia de Sí de la etapa 1 (la respuesta da 6,75; manda la hoja). En cambio, está por debajo del ponderado, 12,55, incluso con r al 11 % (9,71, Análisis!C92), y el DCF inverso implica −1,9 % de crecimiento. Las señales apuntan en las dos direcciones.
    Dato clave: Análisis!B78 = 6.73485391230823

### encaje

    El paquete no trae la cartera de la persona responsable. La hoja solo aporta datos de propiedad (insiders con el 11,2 % del capital), que no sirven para juzgar el encaje.
    Dato clave: Análisis!C96 = 0.112

### Qué lo cambiaría

    - Un margen bruto trimestral que siga cayendo por debajo del 55,5 % o un ROCE por debajo del 15 % pasaría la calidad a no_pasa.
    - Una cotización por debajo de 6,73 EUR (el valor del escenario malo de la hoja) pasaría el precio a pasa.
    - Un deterioro del goodwill de 484,9 MEUR en el test de 2026, o una caja libre por debajo de 100 MEUR, cambiaría la caja o la calidad.

### Qué falta

    - Margen por mercado o región: la empresa publica un solo segmento, y sin ese dato no se sabe si el escalón fiscal es de nivel o compuesto.
    - Parte restringida de la caja de 284,7 (saldos de jugadores 48,5 con reserva no publicada) y efecto cuantificado de la prohibición de Brasil.
    - La hoja no fija precio de Sí (C104 «sin precio de entrada»); solo da la referencia del escenario malo, de 6,73.

### Comprobaciones mecánicas y normalizaciones

    {
      "comprobaciones": {
        "avisos": [],
        "nota": "Comprobaciones mecánicas informativas: no acreditan la calidad económica."
      },
      "normalizaciones": []
    }

