# Revisión del registro de entradas de Jumbo (examen)

- **Revisor:** «Claude revisor registro» (agente Claude distinto del extractor Mistral `mistral-large-4-0`). Fecha 2026-11-18. **No se sella nada** (el sellado se hará sobre `jumbo_e`).
- **Material revisado:** rama `mistral/examen-jumbo-entradas` @ `fced486`, `resultados_examen/jumbo/verificacion_entradas.json` (313 + 246 aux), `ENTREGA.md`, `fuentes_mercado/`. Contraste con el expediente `jumbo_c/Jumbo` (repo producto, rama `examen/ahold-f1` @ `1c73f22`): textos `[PDF PAGE n]`, PDF del expediente (huella de AR2020 = la de la Release), `cambio_jumbo_c.json`, `datos_v63.md`.
- **Detalle:** `REVISION.tsv`, una fila por entrada del alcance (283; las 30 hipótesis no se revisan) y por auxiliar (246).

## Recuentos

| | verificado | discrepancia | duda | total |
|---|---|---|---|---|
| universo (sin hipótesis) | 243 | 19 | 21 | 283 |
| auxiliares | 243 | 3 | 0 | 246 |
| **total** | **486** | **22** | **21** | **529** |

Comprobación mecánica: los 231 orígenes de la Historia están en el informe y la columna esperados (comparativo del informe siguiente, o 2025; columna del **grupo**, no de la sociedad; «2019» = año natural de AR2020 según **J-T bis**, que sustituye a J-T; «2018» = ejercicio 2018/19 del informe de transición). Escalas (euros → mm), signos y fórmulas reproducen el libro.

**Lo que no cuadra con `ENTREGA.md`:** `comprobar` sobre una copia de `jumbo_c` con este registro da **1 discrepancia** (no 0) y 40 errores de contrato (30 hipótesis + 10 sin resolver). La huella de la cabecera (`21ee49…`, la de la plantilla) no es la del libro actual de `jumbo_c` (`653ad0…`), aunque los 313 valores siguen vigentes.

## Discrepancias materiales y corrección propuesta

1. **Cruce J3 también en 2019 (valor).** `Historia!F15/F16/F17`. AR2020 p. 59 imprime para 1-ene–31-dic-2019 «Lease repayments (1.488.677)» e «Interest paid for leases (4.312.789)». La nota de costes financieros, p. 86, da «Interest expense on lease liabilities … 1.488.678»: las etiquetas vienen cruzadas igual que en 2020–2025. Comprobado también en el PDF con `pdftotext`. `jumbo_c` dejó 2019 «como se publicó» porque J3 cubría 2020–2025, cuando 2019 era la transición, que rotula bien. Con J-T bis, 2019 sale de esa columna cruzada. **Corrección:** F15 = 7,124703 + 1,488677 = **8,6134** (libro 11,4375); F16 = **1,4887** (libro 4,3128); F17 = **4,3128** (libro 1,4887). Los dos aux de AR2020 p. 59 llevan mal el concepto: el tratamiento dice «el informe rotula bien». **No toca la base del FCF 2023–2025** (C48/C49 correctos).
2. **Acciones (mecánica).** El aux de AR2025 p. 142 tiene escala 1 con valor_modelo 134,365561. Es la discrepancia que da `comprobar`. **Corrección:** escala 1e-6. La cifra, la fecha, la ausencia de autocartera y P-O2 están bien.
3. **`Análisis!C42` desfasado (vigencia).** 6,4458 sale del precio de la etapa 1 (24,72 €): (24,72 × 134,365561 + 62,247 − 546,140) ÷ 440,24 = 6,446. Con el precio activo de 27,28 € da **7,227x**. Hay que recalcularlo en `jumbo_e`.
4. **Evidencia forzada en ceros y años (15; el valor es correcto, la cita no lo prueba).** Las citas no tienen relación con el dato: cartas de garantía, dividendos, «available for sale», «Tax paid», «Proceeds from investments held to maturity 4.220.000» (no es cero en 2021). Cuatro años salen de dígitos sueltos: «Law 4449/2017», «Regulation 2020/1989»… Afecta a C16, C17, C23, D13, D16, D17, D23, E16, E17, F13, H13, D5, E5, G5 e I5. **Corrección:** las filas 16/17/23 anteriores a la NIIF 16 (1-jul-2019) pasan a `no_aplicable`, citando AR2018-19 p. 52 o la nota de la transición p. 48. F13 se cita en AR2020 p. 59 y H13 en AR2022 p. 68 («Share Capital Change of Subsidiaries … –»). Los años se citan en la cabecera de columnas o se declaran convención.

## Dudas (21) y lo que propongo

- **Resolubles con lo publicado:**
  - `L14`: la cita es el subtotal «(61.158.549)» de AR2025 p. 209, que reproduce exactamente el libro.
  - `C33`: (62,247015 − 546,140091) ÷ (435,66 + 169,93 − 165,35) = −1,0992. Los EBITDA vienen de AR2025 p. 19 y H1 2026 p. 11.
  - `C60`: es una potencia; el formato no la admite.
  - `I17`: empate de redondeo, diferencia de 50 €.
- **Clase:**
  - SBC de 2019, 2020, 2023 y 2025 y `C50`: el texto prueba la inexistencia, así que la clase es `cero_comprobado`, no `no_aplicable`.
  - `E23` y `F5`: citas débiles.
- **Significado:**
  - `J14`: el Δcirculante 2023 y el CFO, y con él `C46`, incluyen −9,6 mm de «Non-short-term restricted bank deposits», una colocación en depósito y no circulante. Supone ≈ −2,7 mm/año en la media 2023–2025.
  - `J13`: compra bruta de 1,2 mm frente a 0,301 neta de la caja adquirida. En 2025 la cifra ya va neta.
- **Sin fuente:**
  - `C96`: 16,63 % frente al 16,42 % impreso en AR2025 p. 143.
  - `C32`: 0 plausible (compra con «bargain purchase», p. 189).
  - `C28`, `C31` y `C34`: veredictos de texto de la etapa 1.
- **Mercado:**
  - `C57` (Bund 3,35 %): sin bytes oficiales. Bundesbank y BCE tampoco son accesibles desde esta revisión.
  - `C38` y `C88`: terceros sin bytes.

## Datos de mercado

- **Precio de 27,28 €:** `fuentes_mercado/JUMBO_BELA_20261118.md` tiene sha256 `18767da2…`, igual a `HUELLAS.txt` y a la copia de `coordinacion/…/precios/`. Dice «Previous Close: 27,2800 EUR», cierre del 17-nov-2026 y ex distribución de 1,00 €. Coincide, pero es la captura de la persona responsable: sigue siendo lectura externa (R2).
- **Bund:** no hay texto guardado, así que no hay nada que contrastar.
- **Damodaran:** coincide con su extracto (`05fc9122…`), que no he podido cotejar con la página original.

## Límites

Se revisó cada entrada con scripts (cita en su página, posición de columna, informe, escala y signo) y a mano en los casos señalados. No se volvió a descargar la Release; para el punto 1 se usó el PDF del expediente, con huella igual a `RELEASE_FUENTES_EXAMEN_SHA256SUMS`. Ruptura de serie que no es error del registro: la caja de 2016–2017 incluye depósitos a más de 3 meses, y desde el comparativo de 30-jun-2019 ya no (506,6 → 88,2 mm, transición p. 52). Las hipótesis, C76 incluida, no se revisan. Esto no acredita aptitud para dinero real.
