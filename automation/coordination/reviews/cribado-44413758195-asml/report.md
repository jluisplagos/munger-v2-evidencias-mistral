# Cribado · ASML

Estado de la ejecución: `AUDITORIA_DOCUMENTAL_PENDIENTE_ACEPTACION`

Cribado pendiente de revisión humana. No es una recomendación de compra, ni aceptación, ni aptitud para dinero real. Tasa 9 % provisional.

C-ARR (decisión de la persona responsable): los arrendamientos se cuentan una sola vez, en el flujo. El alquiler se resta de la caja libre; la deuda, deuda/EBITDA y deuda/caja libre se miden sin arrendamientos; el pasivo por arrendamientos se muestra aparte, como dato.

Cifras de la etapa 1 tal como las guardó la hoja, a su fecha de análisis; sin las decisiones posteriores (P-O1, P-O2, F1-A/F1-B, D-US1/2, D-WM) ni verificación contra la fuente oficial.

| Campo | Valor |
|---|---|
| Fecha de la hoja | 2026-10-17 |
| Tarea | cribado-44413758195-asml |
| SHA del código | 833cd50a9bba34006519119c72a29c70a1656fb7 |
| Huella del paquete (package_sha256) | 3d081e62104076f7134024f8ec1ec54a0065d7a4e2050cf519ebe0a12633396d |
| Huella del envío (bundle_sha256) | e8e37ba6a56225c9784c4da1ffce8315b6f1766897d422a1b6b80e877ef373d3 |
| Huella del encargo | 32b5c7f313e61a61fb0f5e68a75b3c44004eb902e97b98720fb98fa8d383e6cf |
| Huella de la Release | 4d30f7352948fe7e7fe3b133386eabedbddcc71d997e972a1c6db7964d58b0a9 |
| Huella del libro | d7befe8aa9823091712fe0181869a85dbb3854f4ae2a455269273abc741aa61c |
| Modelo pedido / devuelto | claude-opus-5-5 / claude-opus-5-5 |
| Esfuerzo | high |
| Gramática del servidor | True |
| Mensajes enviados | 1 |
| Cota de entrada antes de llamar | 136993 tokens |
| Reserva estimada antes de llamar | USD 1.203332 |
| Uso de tokens | entrada 61644, salida 2869 |
| Coste | CONOCIDO_ESTIMADO; estimado USD 0.303956; cota 0.303956 |

| id | ruta | sha256 | bytes |
|---|---|---|---|
| respuesta | EMPRESAS_LOTES_COMPLETOS/ASML/ASML_respuesta.md | e98ef6e025f39803072cfab53b385b9c309273b8cba608dc018bda92f0c3d64a | 33131 |
| cambios_v2 | EMPRESAS_LOTES_COMPLETOS/ASML/ASML_cambios_v2.md | 793bc064b79f95c802484bd7588564f791400b86ee5d15c146cfb6148088c1ba | 3788 |
| hoja_analisis | EMPRESAS_LOTES_COMPLETOS/ASML/ASML_evaluada.xlsx#Análisis | 55c06bad78267a0f4cf64119d7e46d002768b77553da1f3ded56902239ac9e1f | 22729 |
| hoja_control_maestro | EMPRESAS_LOTES_COMPLETOS/ASML/ASML_evaluada.xlsx#Control maestro | 3f85503938788341f2e61d9ade95c2b795e4ebeefe7af0b5a29dd485f4a3c78b | 56378 |

## Salida del modelo (datos, sin acciones ejecutables)

Veredicto `vigilar` · DCF de la plantilla aplica: `dudoso`

| Filtro | Resultado |
|---|---|
| calidad | pasa |
| caja | pasa |
| balance | pasa |
| precio | no_pasa |
| encaje | no_aplica |

### Pasivo por arrendamientos (dato aparte)

    Control maestro!M51 = 234,9 mm de arrendamientos operativos (dic-25); además, 16,5 mm de arrendamiento financiero incluidos en Análisis!C54 y excluidos del cociente.


### Tipo de negocio y motor

    Fabricante de bienes de equipo para semiconductores (litografía EUV/DUV y servicio sobre la base instalada): monopolio tecnológico en EUV, pero cíclico y dependiente del capex de pocos clientes.
    Caja libre de ciclo medio (normalizar la caja libre a lo largo de un ciclo completo de capex de semiconductores, separando anticipos y factoring) descontada al 9%; el DCF de la plantilla, con base media FY2023–25, sirve como aproximación.

### calidad

    Es el único fabricante de EUV y tiene un ROCE antes de impuestos LTM del 62,8% (99,3% sin caja) con márgenes brutos en expansión hasta el 52,8%, aunque concentra el 61,2% de las ventas en cuatro clientes y el 29,1% en China; el negocio se entiende con el paquete, así que discrepo del «DESCARTAR · demasiado difícil» de Análisis!A6, que nace de C13 (precio) y no de la calidad.
    Dato clave: Análisis!C24 = 0.628

### caja

    La caja libre base (media FY2023–25 neta de SBC) es positiva, con 7.615,9 mm, y la conversión caja/beneficio es de 1,33x (0,96x sin anticipos); aun así es muy cíclica (3.247 mm en 2023 frente a 11.027 mm en 2025) y el CFO de 2025 incluye 6.212 mm de factoring.
    Dato clave: Análisis!C52 = 7615.9

### balance

    Sin arrendamientos, la deuda de 2.707,9 mm frente a caja e inversiones a corto de 12.735,1 mm deja una caja neta de unos 10.027 mm (≈ −0,62x el EBITDA LTM de 16.242,2 mm, que en US GAAP ya resta el alquiler, coherente con Análisis!C33 = −0,62); el único vencimiento relevante, el bono de 750 mm de mayo de 2027, lo cubre la caja unas 10,8 veces.
    Dato clave: Análisis!C54 = 2724.4 (incluye 16,5 de arrendamiento financiero; sin él, 2.707,9)

### precio

    La cotización de 1.477,2 € está muy por encima del precio de Sí (240,97 €), del valor ponderado (447,8 €) y del escenario bueno (678,5 €); incluso con r del 7% el ponderado ronda 669–732 €, y el precio exige un 23,2% de crecimiento anual de la caja libre (Análisis!C86), así que el resultado no depende de la tasa ni de la base cíclica (con una base de ~13.000 mm, la respuesta estima un precio de Sí de ~410 €).
    Dato clave: Análisis!C37 = 1477.2

### encaje

    El paquete no trae la cartera de la persona responsable, y lo que dice Análisis!C104 (precio de Sí de 241 €) es un plan de la etapa 1, no un dato de encaje.
    Dato clave: Análisis!C104 = plan de cartera de la etapa 1 (no se usa)

### Qué lo cambiaría

    - Una cotización cerca o por debajo del valor ponderado de la hoja (447,8 €) con la tesis intacta pasaría el veredicto a estudiar_a_fondo.
    - Una restricción nueva de exportación de EUV a China o la aparición de un competidor creíble en EUV rebajarían la calidad.
    - Una caja libre de ciclo medio documentada muy por encima de 13.000 mm que eleve el valor ponderado hacia la cotización.

### Qué falta

    - Una caja libre de ciclo medio limpia de anticipos y del factoring (6.212 mm en 2025): la base de 7.615,9 mm y el LTM sin circulante de 13.122,5 mm difieren un 72%.
    - Dónde clasifica la empresa los intereses cobrados, para decidir si el exceso de caja (3.300–5.300 mm) se puede sumar sin contarlo dos veces.
    - Si las 10 ventas de directivos (≈14 mm EUR) son discrecionales o están ligadas a planes de retribución o a impuestos.

### Comprobaciones mecánicas y normalizaciones

    {
      "comprobaciones": {
        "avisos": [
          "Filtro precio: motivo de más de 400 caracteres."
        ],
        "nota": "Comprobaciones mecánicas informativas: no acreditan la calidad económica."
      },
      "normalizaciones": []
    }

