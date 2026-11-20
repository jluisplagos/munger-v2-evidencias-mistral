# ENTREGA — M11 · Contraste independiente del expediente de Zoetis, segundo tiempo (extractor: Mistral)

- **Encargo**: `coordinacion/cierre_v2/examen/zoetis_t2/ENCARGO_MISTRAL_M11_CONTRASTE_T2.md` (rama `coordinacion/cierre-v2`). Entrega en la rama `mistral/m11-contraste-t2`, carpeta `resultados_examen/m11_contraste_t2/` (`CONTRASTE.csv` + esta `ENTREGA.md`). Método igual que M7 (`coordinacion/cierre_v2/examen/mistral_m7/ENCARGO_MISTRAL_M7_CONTRASTE.md`). Fecha: 2026-11-19.
- **Modelo y herramientas realmente usados**: extractor **Mistral (mistral-large-4-0)** actuando como agente Vibe Code; `gh` (clonar repos/ramas, leer ramas sin escribir en `jluisplagos/munger-v2`), `python3` estándar (json/csv/datetime) y shell para buscar líneas en `texto/`. Sin LibreOffice, sin ejecutar el pipeline ni macros, sin XLSX; no se sube ningún PDF/XLSX a Git.
- **Ámbito**: las **34 entradas pendientes con extractor «Claude orquestación»** de `zoetis_t2/Zoetis/verificacion_entradas.json` (las mismas 34 de `resultados/registro_cambios_zoetis_t2.json`: 20 auxiliares nuevos del 10-Q T3 2026 y las celdas C24, C31, C32, C33, C34, C37, C40, C41, C42, C53, C54, C55, C57 y `Palancas!C45`), más los **7 orígenes impresos del 10-K FY2025** usados por las celdas derivadas cambiadas, más la **guía del 5-nov-2026** y la **demanda colectiva (10-Q T3 p. 24)** del encargo.
- **Método**: para cada cifra se abrió `texto/` (o `fuentes_mercado/`) en la página `[PDF PAGE n]` declarada, se comprobó la **cabecera de columnas**, el **número impreso**, la **columna/año**, la **unidad**, el **signo** (paréntesis = negativo; «—» = cero) y, si es cálculo, **se rehizo la cuenta con las cifras impresas**. En el CSV, `archivo` es relativo a `zoetis_t2/Zoetis/`.

## Recuento (CONTRASTE.csv: 43 filas)

| filas | sí | no | no_se_encuentra |
|---|---|---|---|
| 43 | **41** | **0** | 2 |

**No hay ningún «no»**: ninguna cifra cambiada discrepa del número impreso en su fuente. Los 2 `no_se_encuentra` son `Análisis!C31` y `Análisis!C34` («Sí»), convenciones de juicio sin archivo/página que contrastar (igual que en M7), no discrepancias.

## Puntos de atención especial del encargo (todos coinciden)

- **Doce meses al 30-sep-2026** (`C24, C33, C40, C42`): cuentas rehechas con cifras impresas y cuadran al dígito: BAI LTM = 3.360 − 2.599 + 2.353 = 3.114 (10-K p. 66; nota 2 p. 10 «as previously reported»; 10-Q p. 3); intereses LTM = 222 − 165 + 185 = 242; impuestos LTM = 687 − 529 + 470 = 628; D&A (línea de flujos) LTM = 487 − 365 + 357 = 479; EBITDA LTM = 3.835; CFO LTM = 2.904 − 2.011 + 1.880 = 2.773 (nota 2 p. 11); capex LTM = 493; `C33` = 7.716/3.835 = 2,011994784876141; `C24` = 3.356×(1−628/3.114)/11.019 = 0,24314328791461562; `C40` = 2.773−493−1 = 2.279; `C42` = 42.606,79989885/3.835 = 11,109986935814863. Bases «as previously reported» (BAI 2.599, impuestos 529, CFO 2.011, nota 2 pp. 10–11) frente a reexpresadas (intereses 165, D&A 365, capex 462, arrendamientos financieros 2, pp. 3/8): todo impreso como se declara; la mezcla de bases queda declarada en el expediente como APROXIMACIÓN.
- **C53 = 1.333** (caja, 10-Q p. 5, columna 30-sep-2026) y **C54 = 9.049** = 750 + 8.299 (p. 5) ✓. **C32** = 2.888/15.088 = 0,1914103923647932 ✓.
- **C37 = 82,11** (5-nov-2026): fila «November 05, 2026 | $82.11» de `fuentes_mercado/Zoetis_IR_XNYS_ZTS_historico_acciones_20261118_mistral_examen_zoetis_t2.txt` ✓ (transcripción; falta captura/CSV, ya declarado). **C41** = 82,11 × 424.927535 = 34.890,79989885 exacto ✓. **C55** = 424.927.535 acciones (10-K FY2025 p. 68) ✓. **C57 = 4,84 %**: fila 11/05/2026 del CSV del Tesoro, 13ª columna (10 Yr) = 4.84 ✓. `Palancas!C45` = 46331 = serial Excel 1900 de 2026-11-05 (comprobado) ✓.
- **Guía del 5-nov-2026**: ingresos $9.220–$9.320 (antes $9.120–$9.320), orgánico (2)%–(1)%, BPA ajustado $6.25–$6.35, neto ajustado $2.600–$2.640, reportado $5.50–$5.60, FX «as of October 20, 2026» — texto y tabla «2026 GUIDANCE» del comunicado del T3 coinciden línea a línea con la sección 5 del extracto ✓.
- **Demanda colectiva**: 10-Q T3 p. 24 — presentada el 27-may-2026, modificada el 23-oct-2026, *City of Ann Arbor Retiree Health Care Benefit Plan & Trust v. Zoetis Inc., et al.*, Case No. 1:26-cv-04401 (S.D.N.Y.), clase 14-ene-2025 a 6-may-2026; derivadas 1:26-cv-04709 (S.D.N.Y.) y 2:26-cv-07479 (D.N.J.); coincide con la sección 10.5 del extracto ✓.

## Comparación con mi entrega anterior (`mistral/examen-zoetis-t2`) y explicación de cada diferencia

- **EBITDA LTM**: mi `LTM_3T.csv` daba **3.987** = EBIT 3.384 + D&A 603, donde los 603 sumaban la línea de flujos «Depreciation and amortization expense» (479 LTM) **y** la línea de la PyG «Amortization of intangible assets» (124 LTM). La línea de flujos del CFO ya es la D&A total (la PyG solo desglosa aparte la amortización de intangibles; la depreciación de PP&E va dentro de cost of sales/SG&A/R&D, 10-K p. 66), así que mi entrega **contaba dos veces la amortización de intangibles** (124 LTM), como detectó el coordinador. El expediente (C33/C42) usa solo la línea de flujos: EBITDA LTM = EBIT 3.356 + 479 = **3.835**; diferencia 3.987 − 3.835 = 152 = 124 (doble cómputo) + 28 (base del BAI 9M-2025, ver abajo).
- **Base del 9M-2025**: mi entrega usaba las columnas reexpresadas de los estados principales (BAI 2.571, CFO 2.056, p. 3/8); el expediente usa, para casar con el 10-K 2025 (base antigua), el 9M-2025 «as previously reported» de la nota 2 (BAI 2.599, impuestos 529, CFO 2.011) y solo reexpresados los intereses/D&A/capex/arrendamientos (165/365/462/2). Resultado: BAI LTM 3.114 (yo 3.142), EBIT LTM 3.356 (yo 3.384), CFO LTM 2.773 (yo 2.728). La mezcla de bases está declarada en el expediente como aproximación.
- **FCF (C40)**: el expediente da 2.279 = CFO LTM 2.773 − capex 493 − principal de arrendamientos financieros 1; mi entrega daba FCF 2.235 = CFO 2.728 − capex 493 (no descontaba los arrendamientos financieros). Misma partida, base y perímetro distintos.
- **Iguales en ambas entregas**: precio 82,11 $ (5-nov), acciones 424.927.535, capitalización 34.890,79989885, Treasury 10 años 4,84 % (5-nov), y la guía del 5-nov (9.220–9.320 / (2)%–(1)% / 6,25–6,35 / 2.600–2.640 / 5,50–5,60 / FX 20-oct) — en mi `GUIA_2026.md` ya estaban esos mismos valores.

## Límites

- No apruebo mi propio trabajo: no firmo como revisor ni sello comprobaciones; la revisión corresponde a un agente Claude distinto.
- No valoro ni recomiendo: este documento solo contrasta cifras contra sus fuentes impresas; no emite juicio de inversión, aptitud ni recomendación alguna.
- El precio del 5-nov-2026 sigue siendo una transcripción sin captura/CSV original (ya declarado en el expediente); las desalineaciones de fechas (precio 5-nov × acciones 31-dic-2025) se constatan, no se juzgan.
