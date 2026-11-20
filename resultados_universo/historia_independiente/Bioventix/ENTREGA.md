# Entrega · Bloque 2 (Bioventix) · Historia de diez años independiente

- **Empresa / años:** Bioventix plc (AIM: BVXP). Ejercicio no natural: cierra el **30 de junio**, así que los "diez últimos ejercicios cerrados" son **FY2016 (1-jul-2015 a 30-jun-2016) … FY2025 (1-jul-2024 a 30-jun-2025)**; la columna `anio` usa el año de cierre (junio).
- **Fuentes usadas:** los diez informes anuales oficiales (Annual Report and Financial Statements) descargados el **2026-11-20** de la web de inversores de la empresa, `www.bioventix.com` (sección Investors / Accounts & AGM; los PDF viven en `/wp-content/uploads/`). Ningún PDF se sube a Git; se anota URL, fecha de descarga y SHA-256:

| Ejercicio | Archivo descargado | URL oficial (bioventix.com) | SHA-256 |
|---|---|---|---|
| FY2016 | bvx-fy2016.pdf | https://www.bioventix.com/wp-content/uploads/final-report-and-accounts-june-2016.pdf | 1d8361f8148ba2830f90189832405acf631e2831f8d32b328fe814ad335e8c9b |
| FY2017 | bvx-fy2017.pdf | https://www.bioventix.com/wp-content/uploads/finres300617.pdf | 390a8a6148f20434f3f9627a20302ac09cf27c34705380c7e6f71555a29a08d8 |
| FY2018 | bvx-fy2018.pdf | https://www.bioventix.com/wp-content/uploads/BVXP-FinRes-30062018.pdf | fa5b6ba494a926d89253578de9159bbf7e5e1a4e0a9a9046db8a693fad0b3615 |
| FY2019 | bvx-fy2019.pdf | https://www.bioventix.com/wp-content/uploads/accounts-30062019.pdf | b593b9742f7587f9ab90d6c179c8246db97d935247221d4b14a95bc8d049f6a5 |
| FY2020 | bvx-fy2020.pdf | https://www.bioventix.com/wp-content/uploads/finres30062020.pdf | 7f38a2d4292c7bc0b816244b04650f10e97fc0673fd23e37405fb7d03c7694a0 |
| FY2021 | bvx-fy2021.pdf | https://www.bioventix.com/wp-content/uploads/bvx-online-accounts.pdf | 2e6d1845139f231a7dae72a86f495d5f0f22d6049e0acfe33e088de7aa2e87e9 |
| FY2022 | bvx-fy2022.pdf | https://www.bioventix.com/wp-content/uploads/ks_bvx_ra22_online.pdf | 3577a1c7c54455cd762261f80b323e94b548fdbc9128710b732babf8c1a91980 |
| FY2023 | bvx-fy2023.pdf | https://www.bioventix.com/wp-content/uploads/BVX_RA23.pdf | 4508378fc33a384ceffd16066d531cbbc2e3217e6bb356700292cc0f442b12b8 |
| FY2024 | bvx-fy2024.pdf | https://www.bioventix.com/wp-content/uploads/KS_BVX_AR24_Online.pdf | 5269dbcf84f310b4391bba78b6667e6a41cba44117504fcdf5789063daaebb8e |
| FY2025 | bvx-fy2025.pdf | https://www.bioventix.com/wp-content/uploads/KS_BVX_AR25_PagesCover_10Nov-DIGITAL.pdf | d92013dc30604ebc8d45c28ceb104becf0fd22df3ae04df517c4e9886ad412f1 |

- **Regla de informe (cifra más reciente publicada):** para el año N se usa la **columna comparativa del informe de N+1** (p. ej. FY2016 desde el AR FY2017); FY2025 sale de su propio AR (no existe N+1). Se anota en `informe_usado`. **Páginas = página del PDF (la del visor)**, 1-indexada. Unidad impresa: **libras esterlinas en unidades (£)**; acciones en unidades. Moneda: GBP. FRS 102 (UK GAAP).
- **Resultado:** `HISTORIA.csv`, **274 filas** (24 partidas × 10 ejercicios, con componentes): **190 `encontrado`, 84 `cero_con_evidencia`, 0 `no_encontrado`**.

## Ceros con evidencia (principales)

- `deuda` = 0 en los diez años: la empresa no tiene borrowings (p. ej. AR FY2021 p. 11: "Due to the lack of borrowing within the company…"; balances sin líneas de deuda).
- `arrendamientos` (pasivo NIIF 16) y `arrendamientos_principal` = 0 en los diez años: el balance no muestra pasivos por arrendamiento y el bloque de financiación del estado de flujos no tiene pagos de arrendamiento (la compañía no reconoce arrendamientos; no hay nota de arrendamientos).
- `adquisiciones` = 0: el bloque de inversión solo tiene compra/venta de inmovilizado y de "unlisted and other investments" (participadas), nunca adquisición de negocios.
- `intereses`/`intereses_financiacion` = 0 salvo FY2016 (164), FY2018 (15) y FY2022 (303); esos años van íntegramente en financiación.
- `otros_activos_financieros` = 0 (activos corrientes = stocks, deudores y caja; la inversión en participadas es no corriente), `pensiones` = 0 (plan de aportación definida, nota de "Pension commitments"), `minoritarios` = 0 (no hay NCI; capital and reserves agota el net assets).

## Dudas de definición / decisiones tomadas

- `ebit` impreso existe ("Operating profit"); `ebit_derivado` se da igualmente con BAI (+1) y cada línea entre explotación y BAI (−1): intereses a cobrar, intereses a pagar y, en FY2024, el deterioro de la inversión en CardiNor ("Amounts written off investments" 183,306, línea impresa entre "Operating profit" y BAI, incluida con signo −1). "Difference on foreign exchange" va **antes** de "Operating profit", queda dentro del EBIT derivado.
- `ventas` FY2018 = "Total turnover" 8,751,608, que incluye "Back dated royalty income" 772,391 (línea separada en el AR FY2018; en N+1 se reexpresa como total).
- `da`: FY2021 estado de flujos 135,103 vs nota 5 135,104 (redondeo de 1); uso el estado de flujos y lo anoto.
- `circulante_lineas`: las tres líneas impresas de variación de stocks/deudores/acreedores; se excluyen impuestos pagados y ajustes no monetarios según la plantilla.
- Los AR FY2016–FY2020 son PDF escaneados (sin capa de texto): se extrajeron con OCR por página; las páginas son las del PDF. Los AR FY2021–FY2025 tienen capa de texto.

## Modelo y herramientas usadas de verdad

- Modelo: `mistral-large-4-0`. Herramientas: `gh` CLI (clon del repo), `web_search`/`web_fetch` (localizar URLs oficiales en bioventix.com), herramienta `code_interpreter` (descarga server-side de los PDF vía parámetro `files`, cálculo de SHA-256 y extracción de texto por página con PyPDF2 para FY2021–FY2025), herramienta `ocr_document` del entorno (OCR por página de los PDF escaneados FY2016–FY2020), y `python3` (csv) para generar `HISTORIA.csv`. No abrí ningún dato de `coordinacion/cierre_v2/universo_etapa1/` salvo el propio encargo M10.
