# Cribado · Carriage

Estado de la ejecución: `AUDITORIA_DOCUMENTAL_PENDIENTE_ACEPTACION`

Cribado pendiente de revisión humana. No es una recomendación de compra, ni aceptación, ni aptitud para dinero real. Tasa 9 % provisional.

C-ARR (decisión de la persona responsable): los arrendamientos se cuentan una sola vez, en el flujo. El alquiler se resta de la caja libre; la deuda, deuda/EBITDA y deuda/caja libre se miden sin arrendamientos; el pasivo por arrendamientos se muestra aparte, como dato.

Cifras de la etapa 1 tal como las guardó la hoja, a su fecha de análisis; sin las decisiones posteriores (P-O1, P-O2, F1-A/F1-B, D-US1/2, D-WM) ni verificación contra la fuente oficial.

| Campo | Valor |
|---|---|
| Fecha de la hoja | 2026-10-26 |
| Tarea | cribado-44413758195-carriage |
| SHA del código | 833cd50a9bba34006519119c72a29c70a1656fb7 |
| Huella del paquete (package_sha256) | 4b8a3cccab7074d7837198978e3158c78ac4aa8b6ae5c3989e60ab607356fe76 |
| Huella del envío (bundle_sha256) | 1ad46924be71eb536a6fd63b4710f043d903c6ed1f64bfad00725e2c7d01431f |
| Huella del encargo | 32b5c7f313e61a61fb0f5e68a75b3c44004eb902e97b98720fb98fa8d383e6cf |
| Huella de la Release | 4d30f7352948fe7e7fe3b133386eabedbddcc71d997e972a1c6db7964d58b0a9 |
| Huella del libro | 8dc185856dcfb40afe1b21cdbe3045b6c4642fb9d10dfb2ae52d67cece81585d |
| Modelo pedido / devuelto | claude-opus-5-5 / claude-opus-5-5 |
| Esfuerzo | high |
| Gramática del servidor | True |
| Mensajes enviados | 1 |
| Cota de entrada antes de llamar | 144400 tokens |
| Reserva estimada antes de llamar | USD 1.23296 |
| Uso de tokens | entrada 64899, salida 4478 |
| Coste | CONOCIDO_ESTIMADO; estimado USD 0.349156; cota 0.349156 |

| id | ruta | sha256 | bytes |
|---|---|---|---|
| respuesta | EMPRESAS_LOTES_COMPLETOS/Carriage/Carriage_respuesta.md | c1473ba8cec0eae2c6a11ff2a3a6a27879cdda615e540bc9fe970817229c9e94 | 40759 |
| hoja_analisis | EMPRESAS_LOTES_COMPLETOS/Carriage/Carriage_evaluada.xlsx#Análisis | f25f6ef5ae6847edc38093bf48858c2159d0b2fd16d03bcd49efa6ccf71c51cf | 24419 |
| hoja_control_maestro | EMPRESAS_LOTES_COMPLETOS/Carriage/Carriage_evaluada.xlsx#Control maestro | ce69c22e6e0721e756f3dc8024f01ed1818498f8c74ba33c9262a4adf3812cbd | 58352 |

## Salida del modelo (datos, sin acciones ejecutables)

Veredicto `descartar` · DCF de la plantilla aplica: `dudoso`

| Filtro | Resultado |
|---|---|
| calidad | dudoso |
| caja | pasa |
| balance | no_pasa |
| precio | no_pasa |
| encaje | no_aplica |

### Pasivo por arrendamientos (dato aparte)

    ≈22,5 mm: arrendamientos financieros ≈9,6 (Control maestro!M51) más arrendamientos operativos ≈12,9 (552,7 − 539,8, Control maestro!N51); fuera del cociente de deuda.


### Tipo de negocio y motor

    Servicios funerarios y cementerios en EE. UU. (155 funerarias, 28 cementerios): negocio local, maduro y de demanda estable, con cartera preneed, crecimiento por adquisiciones y apalancamiento elevado.
    DCF de caja libre, pero con el gasto financiero tras refinanciar las notas de 2029 estresado (o un DCF a nivel empresa restando la deuda neta), porque la caja del accionista de la plantilla supone una financiación estable que aquí no lo es.

### calidad

    Es un negocio comprensible, con márgenes estables (operativo 21–23 %) y un foso local visible en el ROIC sin goodwill del 17,1 %. Sin embargo, el ROIC con goodwill es del 8,1 %, por debajo del 9 % exigido, y los contratos funerarios caen un 6,0 % en el primer semestre de 2026 con la cremación en el 60,8 %; por eso la calidad queda en duda y no se confirma como alta.
    Dato clave: Análisis!C24 = 0.081

### caja

    La caja libre base es positiva y recurrente, 36,2 mm netos de SBC y de arrendamientos, con una conversión CFO/beneficio de 1,73x (Análisis!C26). Pero lleva cinco años plana (37,9 de media a 5 años) y cae a 28,4 mm en LTM según Control maestro.
    Dato clave: Análisis!C52 = 36.2

### balance

    Sin arrendamientos, la deuda neta es ≈527,7 mm, unas 4,45x el EBITDA LTM de 118,5 mm (que ya resta la renta) y unas 14,6 veces la caja libre base de 36,2 mm. Eso deja ≈11 % de holgura frente al covenant de 5,00x y 400 mm de notas que vencen en mayo de 2029: demasiado para un negocio estable pero con volumen a la baja. La hoja da 4,53x (Análisis!C33) porque incluye los arrendamientos financieros, y por eso se recalcula.
    Dato clave: Análisis!C54 = 539.8 (menos ~9,6 de arrendamientos financieros y 2,55 de caja = deuda neta sin arrendamientos ≈ 527,7; ≈ 4,45x EBITDA de 118,5 y ≈ 14,6x la caja libre base)

### precio

    La cotización de 35,41 USD queda muy por encima del precio de Sí de ≈23 USD (escenario malo de 23,29 en Análisis!C78) y deja solo un 7,6 % de margen frente al ponderado de 38,31. Con r = 11 % el ponderado baja a 29,5 (Análisis!C92), y el DCF depende además del cupón de la refinanciación de 2029.
    Dato clave: Análisis!C37 = 35.41

### encaje

    El paquete no trae la cartera de la persona responsable; la capitalización de 562,4 mm solo sirve de contexto y este filtro no elimina.
    Dato clave: Análisis!C41 = 562.4

### Qué lo cambiaría

    - Refinanciación de los 400 mm de notas de 2029 a un cupón conocido (≤5,5 %) sin recortar materialmente la caja libre.
    - Deuda neta sin arrendamientos por debajo de ~3,5x el EBITDA, o de ~10 veces la caja libre.
    - Caja libre por acción creciendo tres años seguidos con el ROIC con goodwill por encima del 9 %, y cotización en torno o por debajo de 23 USD.

### Qué falta

    - Resultados del tercer trimestre de 2026 (publicación el 4-nov-2026, posterior a la fecha de la hoja) y condiciones de la nueva línea de 300 mm.
    - Ratio de apalancamiento según la definición del covenant: la empresa comunica 4,0x, que no es reproducible con la hoja.
    - Cobertura de los fideicomisos preneed frente a los precios garantizados, y holgura (headroom) del test de deterioro del goodwill tras agregar las unidades funerarias.

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

