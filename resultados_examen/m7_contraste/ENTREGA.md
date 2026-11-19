# ENTREGA — M7 · Contraste independiente de las cifras que cambió la orquestación (extractor: Mistral)

- **Encargo**: `coordinacion/cierre_v2/examen/mistral_m7/ENCARGO_MISTRAL_M7_CONTRASTE.md` (rama `coordinacion/cierre-v2`). Entrega en esta rama `mistral/m7-contraste`, carpeta `resultados_examen/m7_contraste/` (`CONTRASTE.csv` + esta `ENTREGA.md`).
- **Modelo y herramientas realmente usados**: extractor **Mistral (mistral-large-4-0)** actuando como agente Vibe Code; `python3` estándar (json/csv/re) y `gh`. Lectura de `jluisplagos/munger-v2` rama `examen/expedientes-f1` **sin escribir en él**; sin LibreOffice, sin ejecutar el pipeline, sin macros; no se sube ningún PDF/XLSX a Git. Fecha: 2026-11-19.
- **Método**: para cada cifra cambiada (registros `resultados/` de los cuatro expedientes, más los orígenes con fuente impresa de las celdas derivadas cambiadas, más las series de Vinci de `motor_a_f1.json` y todas las partidas de `fase1_partes/AR_2016-2025`) se abrió `texto/` (o `fuentes_mercado/`) en la página `[PDF PAGE n]` declarada, se localizó la línea citada y se comprobó el **número impreso, la columna/año (cabecera de la tabla), la unidad, el signo** (paréntesis = negativo; «—» = cero) y, si es cálculo, **la cuenta rehecha con las cifras impresas** (fórmula declarada reevaluada con los valores vigentes de `verificacion_entradas.json`). En el CSV, `archivo` es relativo a la carpeta `<Empresa>/` del expediente (p. ej. `ahold_f4/Ahold/`).

## Recuento (CONTRASTE.csv: 800 filas, una por cifra cambiada)

| expediente | filas | sí | no | no_se_encuentra |
|---|---|---|---|---|
| `ahold_f4/Ahold` | 90 | 85 | **0** | 5 |
| `jumbo_g/Jumbo` | 59 | 40 | **0** | 19 |
| `zoetis_t1d/Zoetis` | 56 | 43 | **0** | 13 |
| `vinci/Vinci` | 595 | 595 | **0** | 0 |
| **total** | **800** | **763** | **0** | **37** |

**No hay ningún «no»**: ninguna cifra cambiada discrepa del número impreso en su fuente. Los 37 `no_se_encuentra` **no son discrepancias**, son filas sin fuente impresa que contrastar: convenciones/etiquetas de juicio sin `archivo/pagina` (ahold `C31`, `C34`, `C28`, `C60`; zoetis `Palancas!A31/A33`; jumbo `C31`, pendiente declarado), clases `no_aplicable`/`dato_ausente` (jumbo/zoetis `Historia!C86:G87`, `D13`, `D17`, `E17`, `C23`, `D23`, `C50`), y lecturas externas de terceros sin bytes conservados (ahold `C38`, marcada «Dato no verificable» en el registro; jumbo `C38`/`C88`, declaradas no material por la regla N1).

## Puntos de atención especial del encargo (todos coinciden)

- **Ahold, doce meses al 3T 2026** (`C24, C33, C40, C42, C53, C54`; LTM = ejercicio 2025 + 39 semanas de 2026 − 39 semanas de 2025): `C24` = 3.635/34.122 = 0,106535 → 0,107; `C33` = 16.188/7.334 = 2,207233 → 2,2073; `C40` rehecho línea a línea (CFO 6.731, capex −2.657, intereses −265, arrendamientos −1.956, dividendos JV 22, intereses cobrados 128, subarriendos 147) = **2.150**; `C42` = 47.905,925/7.334 = **6,532032**; `C53` = 3.559 (Q3-26 p.14, 1ª col. 27-sep-2026); `C54` = 19.747 (Q3-26 p.24, 1ª col.). Las 19 líneas nuevas del Q3-2026 (pp. 12, 14, 16, 24) verificadas con sus cabeceras de columnas; las 19 eliminaciones del 2T contrastadas contra su fuente del Q2-2026.
- **Jumbo, recálculo de C46/C40 con C76 = 150**: `C46` = 317,902497 → **317,902**; `C40` = 255,305398 → **255,305** (fórmulas reevaluadas con C76=150 y caja media 471,8284). Entradas impresas verificadas en fy2024 pp. 149/154/178 y fy2025 pp. 150/155/179/209 (columnas de grupo y año correctas; el subtotal de circulante impreso (61.158.549) queda 1 € por debajo de la suma de sus líneas, ya declarado por el expediente en `Historia!L14`).
- **Zoetis**: EBIT = beneficio antes de impuestos + gasto por intereses (10-K FY2025 p.66: 3.360 + 222; TTM: BAI 3.272 + intereses 238 = 3.510; EBITDA TTM = 3.992); **acciones exactas 424.927.535** (10-K FY2025 p.68, también 10-Q T2-2026 p.5) → `C41` = 73,08 × 424,927535 = 31.053,7042578; `C33` = 7.572/3.992 = 1,896794; `C40` = 2.887 − 524 − 0 = **2.363**; `C42` = 38.625,7042578/3.992 = 9,675778; minoritarios impresos (2)/(6)/«—» en fy2023 p.67, fy2024 p.66, fy2018 p.73 (2022/2023 deficitarios → 0 por decisión Z-MIN).
- **Vinci, series**: `da_rou` 605/623/668/714/817 (URD 2022 p.168, 2023 p.171, 2024 p.350, 2025 p.372 — prosa de la nota 4.3); `da_ppa` 0/128/128/108/38 (el 0 de 2021 por lectura: la frase «…Cobra IS on 31 December 2021» aparece literal en URD 2021 p.150); `intereses_arrendamiento` (43)/(48)/(67)/(91)/(110) (URD 2022 p.168, 2023 p.172, 2024 p.351, 2025 p.373). Las 595 filas de Vinci (series + componentes de `C40/C42/C46-C50` + todas las partidas impresas de `fase1_partes/AR_2016-2025`) coinciden línea a línea; los cálculos declarados de `C40` (4.132), `C42` (6,279640), `C46` (9.327,333), `C47` (3.799,667), `C48` (89,333), `C49` (675,333), `C50` (343,667) se reevaluaron y cuadran.

## Límites

- No apruebo mi propio trabajo: no firmo como revisor ni sello comprobaciones; la revisión corresponde a un agente Claude distinto.
- No valoro ni recomiendo: este documento solo contrasta cifras contra sus fuentes impresas; no emite juicio de inversión, aptitud ni recomendación alguna.
- Las desalineaciones de fechas declaradas por el expediente (p. ej. precio reciente × acciones al cierre del ejercicio) se constatan, no se juzgan.
