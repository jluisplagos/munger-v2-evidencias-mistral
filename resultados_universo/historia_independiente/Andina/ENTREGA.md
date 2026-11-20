# Entrega · Bloque 2 (Andina) · Historia de diez años independiente

- **Empresa / años:** Embotelladora Andina S.A. (Coca-Cola Andina; NYSE: AKO/AKO.B; CIK SEC 925261). Ejercicio natural: cierra el **31 de diciembre**, así que los diez últimos ejercicios cerrados son **2016 … 2025** (la columna `anio` es el año de cierre). Estados financieros consolidados bajo **NIIF/IFRS**, moneda **peso chileno**, unidad impresa **miles de CLP** (`ThCh$` en los 20-F en inglés, `M$` en los 20-F en español).
- **Fuentes usadas:** los informes anuales oficiales (Form 20-F "as filed") descargados el **2026-11-20** de la web de inversores de la empresa (`www.koandina.com`, documentos alojados en su bucket oficial `koandina-prod-files-bucket.s3…amazonaws.com`; mismo documento que el del regulador SEC). Ningún PDF se sube a Git; se anota URL, fecha de descarga y SHA-256:

| Ejercicio | Archivo descargado | URL oficial | SHA-256 |
|---|---|---|---|
| 2016 | andina-fy2016.pdf | https://koandina-prod-files-bucket.s3.us-east-1.amazonaws.com/en/finantial-docs/20F%202016%20EN.pdf | 90e8317c10e4b7c45e7b8036c87c9c2dd9218871586bf193b6b0aa4648a82bf1 |
| 2017 | andina-fy2017.pdf | https://koandina-prod-files-bucket.s3.us-east-1.amazonaws.com/en/finantial-docs/20-F%202017%20ES_1.pdf | 73a76d4b68a8528e863ee87e567a9b0a0cd0062bf04618291c2c82b2ee6a88a1 |
| 2018 | andina-fy2018.pdf | https://koandina-prod-files-bucket.s3.us-east-1.amazonaws.com/en/finantial-docs/20-F%20V.%20As%20Filed.pdf | e58a7bc80f5648555e6b011acc01cf9885c1f01fcab6d951b31c9bc1c66a6b46 |
| 2019 | — no disponible como PDF — | (en la web oficial y en EDGAR solo figura en HTM; no se encontró PDF del 20-F FY2019) | — |
| 2020 | andina-fy2020.pdf | https://koandina-prod-files-bucket.s3.us-east-1.amazonaws.com/reportes_financieros/2020%2020-F%20As%20Filed%20%28ES%29.pdf | ac1c2e327cd0aa422f77d3fa9ed9e17a351d029570cb6277fa240f05f03e0175 |
| 2021 | andina-fy2021.pdf | https://koandina-prod-files-bucket.s3.us-east-1.amazonaws.com/reportes_financieros/2021%2020-F%20As%20Filed%20%28ES%29.pdf | abecbd34ae63cc5304cd5670959a81e6dd143ff4f3bebb1dd018157017926bfb |
| 2022 | andina-fy2022.pdf | https://koandina-prod-files-bucket.s3.us-east-1.amazonaws.com/reportes_financieros/2022%2020-F%20As%20Filed%20%28ES%29.pdf | a03f3fc7de171bf20e984d16db06e55620a97e62760ffa5f7c8adf301155e452 |
| 2023 | andina-fy2023.pdf | https://koandina-prod-files-bucket.s3.us-east-1.amazonaws.com/reportes_financieros/2023%2020-F%20As%20Filed%20%28ES%29.pdf | 795df2c387a2a6fc0f5c51f2e7a60b14c17cd0f9283cab7026f1e17a0c25cb94 |
| 2024 | andina-fy2024.pdf | https://koandina-prod-files-bucket.s3.amazonaws.com/wp-content/uploads/2025/03/26203039/20F-2024-As-filed-EN.pdf | 819c45f1ee22b9a6ac57090c6737825ca146ffbeef357d9ebdd5c2cd49e49d87 |
| 2025 | andina-fy2025.pdf | https://koandina-prod-files-bucket.s3.amazonaws.com/wp-content/uploads/2026/04/01203229/20-F-2025-As-Filed.pdf | 71f6c1f79638109a5d31f1f8d452c501d2d226abab9ee422225312d3ce399ee2 |

Cada URL se re-descargó y se comprobó que su SHA-256 coincide exactamente con el del PDF usado (verificación doble).

- **Regla de informe (cifra más reciente publicada):** para el año N se usa la **columna comparativa del informe de N+1** cuando existe: 2016←20-F 2017; 2017←20-F 2018; **2018←20-F 2020 (3.ª columna; el 20-F FY2019 no está como PDF, así que el 20-F 2020 es el informe más reciente que imprime 2018)**; 2019←20-F 2020; 2020←20-F 2021; 2021←20-F 2022; 2022←20-F 2023; 2023←20-F 2024; 2024←20-F 2025; 2025←20-F 2025 propio. El **balance de 2018** sale del propio 20-F FY2018 porque el balance del 20-F FY2020 solo muestra 2020/2019. Se anota en `informe_usado`. **Páginas = página del PDF (la del visor)**, 1-indexadas.
- **Resultado:** `HISTORIA.csv`, **333 filas** (24 partidas × 10 años, con componentes): **260 `encontrado`, 31 `cero_con_evidencia`, 42 `no_encontrado`**.

## Ceros con evidencia (principales)

- `adquisiciones` = 0 los diez años: la sección de inversión del estado de flujos (método directo) no tiene línea de adquisición de negocios/dependientes (solo compras de inmovilizado, de activos financieros y, en 2016–2018, «Investment/Aportes a empresas asociadas», que no es combinación de negocios).
- `intereses_financiacion` = 0 los diez años: los intereses pagados figuran **en actividades de explotación** («Interest payments» / «Intereses pagados»); el bloque de financiación no tiene línea de intereses.
- `arrendamientos` (pasivo NIIF 16) y `arrendamientos_principal` = 0 en **2016, 2017 y 2018**: NIIF 16 obligatoria recién desde el 1-ene-2019 (cita en los 20-F FY2017/FY2018: "IFRS 16 will be mandatory for annual periods beginning after January 1, 2019"). Los «Leasing agreements / Financial lease liability payments» de esos años son arrendamientos financieros **NIIF 17**, que se incluyen en `deuda`.
- `capex` (intangibles) impreso como «—» en 2016, 2018 y 2022; `deuda` componente «Bank loans» no corriente impreso «—» en 2024.

## No encontrados (42 filas)

- `ebit` (impreso): la cuenta de resultados **por función** no imprime subtotal de resultado de explotación (el primer subtotal impreso es «Gross Profit / Ganancia Bruta»).
- `circulante_lineas`: el estado de flujos es de **método directo**, sin líneas de variación del capital circulante.
- `sbc`: no hay ningún plan de pagos basados en acciones en resultados ni notas (la compensación de directivos es «fixed remuneration and a performance bonus» / solo sueldos y beneficios en la nota de gastos de empleados).
- `id`: el 20-F declara que los gastos de I+D «are not meaningful / no son significativos»; no se imprime cifra.
- `capex` intangibles en 2024 y 2025: los 20-F FY2024/FY2025 ya no imprimen esa línea en la sección de inversión.

## Dudas de definición / decisiones tomadas

- `ebit_derivado` (siempre): BAI con signo +1 y, con signo −1, cada línea del resultado financiero entre explotación y BAI: ingresos financieros, costos financieros, diferencias de cambio y resultados por unidades de reajuste. **No** resto «Participación en ganancias de asociadas» ni «Other (losses) gains»: quedan dentro del EBIT derivado.
- `deuda` = deudas financieras con coste, corriente + no corriente, **sin** pasivos NIIF 16: componentes de la nota de «Otros pasivos financieros» (bancos + bonos/obligaciones con el público; en 2016–2018 se añaden los «Leasing agreements» NIIF 17). Se excluyen depósitos en garantía por envases y obligaciones por derivados (sin coste financiero), anotado en `nota`.
- `arrendamientos` = «Pasivos por arrendamientos / Lease liabilities» NIIF 16 de la nota 17, corriente + no corriente (desde 2019).
- `pensiones` = provisión neta post-empleo: línea no corriente de beneficios a empleados («Post-employment benefit liabilities» / «Provisiones no corrientes por beneficios a los empleados», nota 12/13).
- `patrimonio` = patrimonio atribuible a los propietarios de la controladora al cierre; `minoritarios` = participaciones no controladoras (balance); `beneficio_neto` = ganancia atribuible a los propietarios de la controladora.
- `acciones_diluidas` = número promedio ponderado de acciones (nota de BPA), total 946.570.604 (Serie A 473.289.301 + Serie B 473.281.303) **todos los años**; básica y diluida iguales.
- `da` = depreciación y amortización de la nota de gastos por naturaleza / segmentos.
- `caja` y `otros_activos_financieros` del balance (corrientes); `otros_activos_financieros` = «Otros activos financieros, corrientes».
- 2018: cuenta de resultados, flujos y `da` de la 3.ª columna del 20-F FY2020 (coinciden con el 20-F FY2018 propio); balance y `deuda` del 20-F FY2018 propio. 2019: todo desde la columna comparativa del 20-F FY2020 (no hay 20-F FY2019 en PDF en la web oficial ni en EDGAR).

## Modelo y herramientas usadas de verdad

- Modelo: `mistral-large-4-0`. Herramientas: `gh` CLI (clon del repo), `web_search`/`web_fetch` (localizar las URLs oficiales de los 20-F en el bucket S3 de koandina.com), herramienta `code_interpreter` (descarga server-side de los PDF vía parámetro `files`, cálculo de SHA-256 y extracción de texto por página con PyPDF2; re-descarga de las 9 URLs para verificar SHA-256), y `python3` (csv) para generar `HISTORIA.csv`. No abrí ningún dato de `coordinacion/cierre_v2/universo_etapa1/` salvo el propio encargo M10.
