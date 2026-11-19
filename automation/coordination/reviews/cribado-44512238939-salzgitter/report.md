# Cribado · Salzgitter

Estado de la ejecución: `AUDITORIA_DOCUMENTAL_PENDIENTE_ACEPTACION`

Cribado pendiente de revisión humana. No es una recomendación de compra, ni aceptación, ni aptitud para dinero real. Tasa 9 % provisional.

C-ARR (decisión de la persona responsable): los arrendamientos se cuentan una sola vez, en el flujo. El alquiler se resta de la caja libre; la deuda, deuda/EBITDA y deuda/caja libre se miden sin arrendamientos; el pasivo por arrendamientos se muestra aparte, como dato.

Cifras de la etapa 1 tal como las guardó la hoja, a su fecha de análisis; sin las decisiones posteriores (P-O1, P-O2, F1-A/F1-B, D-US1/2, D-WM) ni verificación contra la fuente oficial.

| Campo | Valor |
|---|---|
| Fecha de la hoja | 2026-10-11 |
| Tarea | cribado-44512238939-salzgitter |
| SHA del código | 833cd50a9bba34006519119c72a29c70a1656fb7 |
| Huella del paquete (package_sha256) | 7500627a98ee2b9619a240784f45154b12947f3ad6be8489facc0e8cedd2b578 |
| Huella del envío (bundle_sha256) | e54cfbd0b0ed7c63f71d65c2382ab1134b17b7fcb607e7a14ecb4d13ea119621 |
| Huella del encargo | 32b5c7f313e61a61fb0f5e68a75b3c44004eb902e97b98720fb98fa8d383e6cf |
| Huella de la Release | 4d30f7352948fe7e7fe3b133386eabedbddcc71d997e972a1c6db7964d58b0a9 |
| Huella del libro | 52897b79d4f83cb4c2feb07c392b83ce6a0b78df1c3b3de8fe77b105aec1f9e1 |
| Modelo pedido / devuelto | claude-opus-5-5 / claude-opus-5-5 |
| Esfuerzo | high |
| Gramática del servidor | True |
| Mensajes enviados | 1 |
| Cota de entrada antes de llamar | 139587 tokens |
| Reserva estimada antes de llamar | USD 1.213708 |
| Uso de tokens | entrada 63189, salida 3580 |
| Coste | CONOCIDO_ESTIMADO; estimado USD 0.324356; cota 0.324356 |

| id | ruta | sha256 | bytes |
|---|---|---|---|
| respuesta | EMPRESAS_LOTES_COMPLETOS/Salzgitter/Salzgitter_respuesta.md | 929c2b98de73217c4ef619f1c45f2ee5cf409d8649115a4c3e097eaedac02935 | 33549 |
| cambios_v2 | EMPRESAS_LOTES_COMPLETOS/Salzgitter/Salzgitter_cambios_v2.md | 47d57fbbbab545ca31f4619f8c8c851bc7541952e909f8152dfad01489da742b | 4090 |
| hoja_analisis | EMPRESAS_LOTES_COMPLETOS/Salzgitter/Salzgitter_evaluada.xlsx#Análisis | 357fabc33d09e479c7c8f17942cc7dec16269594478bca5507f1f65a4da53d02 | 23849 |
| hoja_control_maestro | EMPRESAS_LOTES_COMPLETOS/Salzgitter/Salzgitter_evaluada.xlsx#Control maestro | d31dd2ac09236e6a49c7645a6dca4aa6570643d8ae02fbbc3c6a780a8bec29d1 | 57109 |

## Salida del modelo (datos, sin acciones ejecutables)

Veredicto `descartar` · DCF de la plantilla aplica: `no`

| Filtro | Resultado |
|---|---|
| calidad | no_pasa |
| caja | no_pasa |
| balance | dudoso |
| precio | no_aplica |
| encaje | no_aplica |

### Pasivo por arrendamientos (dato aparte)

    Control maestro!M51 = 131.1 (arrendamientos incluidos en la deuda total de 2.127,4 m; también en Control maestro!M36)


### Tipo de negocio y motor

    Siderúrgica integrada alemana cíclica, de materias primas, con comercio de acero, un fabricante de maquinaria de envasado (KHS) y una participación del 29,99 % en Aurubis por puesta en equivalencia.
    Caja o beneficio normalizados a lo largo del ciclo del acero, combinados con una suma de partes (Aurubis a mercado, KHS y negocio de acero) menos la deuda neta sin arrendamientos, las pensiones y los compromisos de SALCOS.

### calidad

    El negocio se entiende (C11 = Sí), pero no muestra ventaja en las cifras: ROCE LTM del 6,1 % (con Aurubis como el 71 % del numerador, 2,5 % sin ella) y media de 7 años del 4,2 % frente a una tasa del 9 %, con pérdidas antes de impuestos en 4 de 8 años y dependencia del ciclo del acero, la energía y la protección comercial.
    Dato clave: Análisis!C24 = 0.061

### caja

    La caja libre base, que ya resta intereses y arrendamientos, es de −141,6 m y sale negativa en las ocho variantes que probó la hoja (de −35,1 m LTM neto de subvenciones a −598,4 m LTM bruto), con inversión obligada en SALCOS y HKM por delante: no convierte el beneficio en caja libre de forma recurrente.
    Dato clave: Análisis!C52 = -141.6

### balance

    Sin arrendamientos, la deuda neta es de unos 792,2 m y la hoja da unos 1,12x sobre el EBITDA previo a la NIIF 16 (el 1,23x de Análisis!C33 incluye arrendamientos y no sirve tal cual), un nivel cómodo incluso para una cíclica; pero ese EBITDA incluye Aurubis por puesta en equivalencia (sin ella, 2,04x con arrendamientos), la deuda/caja libre no se puede medir porque la caja libre es negativa y fuera del cociente quedan 1.393,1 m de pensiones (3,10x si se cuentan como deuda), así que no basta para decidir.
    Dato clave: Control maestro!M36 = 792.2 (deuda neta 923.3 − arrendamientos 131.1)

### precio

    Con una caja base negativa, el DCF de la plantilla da −38,8 € ponderado (de −25,3 € a −56,5 € por escenario) frente a una cotización de 49,94 €, sin precio de Sí; ese número no sirve para concluir porque el método no aplica y la hoja es del 11-oct-2026, anterior al informe de 9M; haría falta una suma de partes (Aurubis a mercado 2.162,6 m, KHS y acero) menos deuda neta y pensiones.
    Dato clave: Análisis!C83 = -38.8082274497115

### encaje

    El paquete no trae la cartera de la persona responsable y la hoja no dice nada concreto sobre el encaje, más allá de una capitalización de 2.853,6 m; este filtro no elimina.
    Dato clave: Análisis!C41 = 2853.6

### Qué lo cambiaría

    - Un ROCE por encima del 9 % a lo largo de un ciclo completo con SALCOS ya produciendo (hoy es del 6,1 % LTM).
    - Caja libre después de inversión, intereses y arrendamientos positiva tres años seguidos a partir de 2027.
    - Una suma de partes (Aurubis 2.162,6 m más KHS, menos los 792,2 m de deuda neta sin arrendamientos y los 1.393,1 m de pensiones) que supere con margen claro la capitalización de 2.853,6 m.

### Qué falta

    - Precio y pasivos de la toma del 100 % de HKM (julio de 2026), que aún no están ni en la deuda ni en el EBITDA de la hoja; el informe de 9M (12-nov-2026) es posterior a la fecha de corte.
    - EBITDA LTM exacto después de restar el alquiler, con y sin Aurubis: la hoja solo da un 1,12x aproximado sin arrendamientos.
    - Cifras de KHS por separado (margen, cartera, competidores) para valorar la suma de partes.

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

