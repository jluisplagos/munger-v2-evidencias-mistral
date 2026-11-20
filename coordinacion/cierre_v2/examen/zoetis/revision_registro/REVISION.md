# Revisión del registro de entradas de Zoetis, primer tiempo (examen)

- **Revisor:** «Claude revisor registro», un agente Claude distinto del extractor Mistral `mistral-large-4-0`. Fecha: 2026-11-18. **No se sella nada**: el sellado se hará sobre `zoetis_t1c`.
- **Material revisado:** rama `mistral/examen-zoetis-entradas` @ `790a8f0`: `verificacion_entradas.json` (315 entradas + 169 aux), `ENTREGA.md` y `fuentes_mercado/`. Se contrastó con el expediente `zoetis_t1b/Zoetis` (repo producto, rama `examen/ahold-f1` @ `1c73f22`): textos `[PDF PAGE n]`, `cambio_zoetis_t1.json`, `fase1_partes`, `datos_v63.md`, y con la segunda lectura OCR de Mistral (`mistral/zoetis-texto-ocr`).
- **Detalle:** `REVISION.tsv` tiene una fila por entrada del alcance (285; las 30 hipótesis no se revisan) y una por auxiliar (169).

## Recuentos

| | verificado | discrepancia | duda | total |
|---|---|---|---|---|
| universo (sin hipótesis) | 237 | 33 | 15 | 285 |
| auxiliares | 152 | 16 | 1 | 169 |
| **total** | **389** | **49** | **16** | **454** |

`comprobar` sobre una copia de `zoetis_t1b` con este registro da 0 discrepancias y 36 errores (30 hipótesis y 6 sin resolver), como declara la entrega. Las columnas y los años son correctos en todas las cifras: el comparativo del 10-K siguiente o el 10-K 2025, y en el 10-Q la columna del 30-jun-2026. Las acciones van en millones con escala real 1, y C55 = 424.927.535 × 1e-6 (P-O2). De 2020 a 2024 (OCR), las 141 cifras citadas coinciden en su posición con la segunda lectura. Las de 2023 que alimentan C46, C47 y C50 coinciden además con el 10-K 2025, que no es OCR.

## Discrepancias materiales y corrección propuesta

1. **EBIT mal calculado en los diez años (`Historia!C7:L7`, valor).** El libro calcula BAI − intereses, cuando debe ser BAI + intereses. `fase1_partes` declara «EBIT derivado = BAI + gasto por intereses neto», pero pone signo −1 al gasto por intereses. Ese gasto se imprime en positivo, como coste dentro de «Costs and expenses» (10-K 2025 p. 66, comprobado también con `pdftotext` sobre el PDF de huella igual a la Release). El registro reproduce el error: los 10 aux de intereses llevan signo −1 «al signo del modelo». **Valores correctos** (2016→2025): 1.394, 1.700, 1.896, 2.024, 2.227, 2.712, 2.877, 3.175, 3.358 y **3.582** (el libro tiene 3.138). El margen de 2025 sale 37,8 %, no 33,1 %. Afecta a los márgenes, al ROIC medio y a las medidas del foso; la base del FCF (CFO − capex) no cambia.
2. **Adquisiciones netas con cobros convertidos en pagos (`D13`, `J13`, signo).** D13 = 119 suma los 37 de «Net proceeds from sales of assets»: debería ser 82, o 45 si se restan. J13 = 251 suma los 96 de «Proceeds from sale of businesses»: debería ser **59**. Con el mismo concepto, K13 sí va con signo +1.
3. **Minoritarios negativos presentados en positivo (`I26`, `J26`).** El balance imprime (2) y (6). El valor correcto es −2 y −6, o 0 con nota. Es inmaterial.
4. **`L17` vacío pese a estar publicado.** 10-K 2025 p. 89 imprime «Financing cash flows – finance leases 2 1 —». Corrección: L17 = 2. C49 ya usa ese 2.
5. **Ceros con evidencia forzada (22: el valor es correcto, la cita no prueba el cero).** Afecta a las filas 16 (2016–2025), 17 (2016–2021), 23 (2016–2017) y a 4 aux. Las citas no tienen relación con el dato: la carta a los accionistas, «Proceeds from maturities…», «Principal payments on long-term debt (1,350)», «Proceeds from sale of businesses 293 96». Con frecuencia hay **una cifra distinta de cero en la propia columna**. **Corrección:**
   - Fila 16: `no_aplicable` o convención US GAAP, citando la línea suplementaria «Interest, net of capitalized interest».
   - Fila 17: no hay arrendamientos financieros hasta 2023 (10-K 2023 p. 87 «…finance leases (years) 30.27 0.00»; 10-K 2024 p. 86 «… finance leases 1 — —»).
   - Fila 23: anterior a ASC 842 (10-K 2019 p. 73 «Operating lease liabilities 164 —»).
   - El aux de 2023 de C49 tiene la línea correcta en su misma página.

## ¿Exigen C24, C26, C33, C40 y C42 el 10-Q T2-2025?

**Solo en parte.** El 10-Q T2 2026 trae los seis meses de 2025 ya reexpresados por la *Fiscal Year Alignment* (p. 3 y 8). En las p. 10–11 da además ingresos, BAI, impuesto, beneficio y CFO «as previously reported», pero no el capex ni los intereses en la base antigua.

- **C26 (1,058)** no necesita ningún 10-Q: es ΣCFO / Σbeneficio de 2021–2025 de la Historia, 12.335 / 11.654 = 1,0584. Se puede registrar ya como derivado.
- **C40:** sale 2.363 (CFO antiguo + capex reexpresado) o 2.316 (todo reexpresado), frente a 2.365 en el libro.
- **C33:** sale 1,88–1,90x frente a 1,92x. Deuda neta 7.572; EBITDA TTM 3.992–4.019, calculado con BAI + intereses + D&A.
- **C42:** sale 9,61–9,68x frente a 9,57x (EV 38.626).
- **C24:** sale ≈ 26,2–26,9 % según se resten o no las inversiones a corto, frente a 26,6 %.

Son **aproximables con el expediente, pero no exactos**. Para el valor exacto hace falta el 10-Q T2-2025 o la fórmula de la etapa 1, que no está documentada.

**C60** se reproduce exacto ((443,835/478,569)^(1/5) − 1 = −1,50 %), pero el formato no admite la potencia.

## Otras dudas (16)

- **`E26`:** el libro está vacío, pero 10-K 2018 p. 73 imprime «—» para 2018. Debería ser 0 comprobado.
- **`C14`:** 10-K 2018 reexpresa «Other liabilities» de 2016 de −295 a −290, así que el circulante de 2016 sería 434, no 439.
- **`C48`:** 0 correcto, pero sus orígenes tienen las citas espurias del punto 5.
- **`A31/B31` y `A33/B33`:** la agrupación geográfica es dudosa. «Other emerging markets» se cuenta como Asia; «Other developed markets» y la fabricación por contrato, como Australia y Nueva Zelanda. Esto fija la r mínima.
- **`C38` y `C88`:** son de terceros, sin bytes; no son verificables.

## Datos de mercado

- **Precio de 73,08 USD:** «October 08, 2026 $73.08» en `Zoetis_IR_XNYS_ZTS_historico_acciones_20261118.txt` (`7a8d45f2…`).
- **Treasury a 10 años, 5,22 %:** fila 10/08/2026, columna «10 Yr» = 5.22, en `US_Treasury_…txt` (`c6e8af2f…`).
- **Damodaran:** «Drugs (Pharmaceutical)» (`cead05cd…`).

Las tres huellas coinciden con `HUELLAS.txt`. Pero son **transcripciones o extractos hechos por el extractor**, no los bytes originales de investor.zoetis.com ni el CSV íntegro del Tesoro. Esos hosts y nyse.com no son accesibles desde esta revisión: el proxy los rechaza.

## Límites

La revisión se hizo con scripts (página, posición de columna, informe siguiente frente al más reciente, signo, OCR) y a mano en los puntos señalados. La comprobación del OCR se apoya en otra lectura del mismo extractor, aunque independiente del tesseract del expediente; en 2023 y 2024 se cruzó además con el 10-K 2025. No se descargó la Release: el PDF local del 10-K 2025 tiene la huella de `RELEASE_FUENTES_EXAMEN_SHA256SUMS`. Las hipótesis no se revisan. Esto no acredita aptitud para dinero real.
