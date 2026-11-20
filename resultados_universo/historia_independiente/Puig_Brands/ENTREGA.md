# Entrega · Bloque 8 (Puig Brands) · Historia de diez años independiente · M10

- **Empresa / años:** Puig Brands, S.A. (BME: PUIG; antes Puig, S.L.), Barcelona. Ejercicio **natural** (cierre 31-dic). Los diez últimos ejercicios cerrados a la fecha del encargo son **2016–2025**.
- **Disponibilidad en la web oficial (dicho explícitamente, como pide el encargo):**
  - **2016, 2017 y 2018: no hay informe anual oficial en la web de inversores (puig.com; sus publicaciones empiezan en 2019) ni en el regulador (la CNMV solo recoge informes de Puig Brands desde 2023).** Por eso no hay filas para esos años.
  - **2019 y 2020:** existe el "Annual Report" oficial (memoria + Estado de Información No Financiera), pero **no incluye los estados financieros consolidados** y no hay cuentas anuales consolidadas publicadas en la web oficial para esos años → 24 partidas `no_encontrado` por año (filas incluidas con el informe como archivo y su SHA-256).
  - **2021–2025:** estados consolidados completos disponibles en la web oficial: *Special Purpose Consolidated Financial Statements 2023/2022/2021* (publicados para la OPV de 2024) y las *Cuentas Anuales Consolidadas* de Puig Brands 2023, 2024 y 2025 (tambiién dentro de los informes anuales integrados 2024/2025).
- **Fuentes usadas:** descargadas de la web de inversores (puig.com / uploads.puig.com) el **20-nov-2026** (UTC): URL, fecha y SHA-256 de cada PDF en `FUENTES.csv` (y el SHA por fila en `HISTORIA.csv`). Ningún PDF se sube a Git. No abrí `coordinacion/cierre_v2/universo_etapa1/` ni ningún expediente de `munger-v2` salvo la plantilla genérica indicada en el encargo M4.
- **Regla de informe:** 2021 desde la columna 2021 del documento SP 2021–2023 (única publicación oficial con estados de 2021); **2022** desde la columna comparativa de las cuentas anuales 2023; **2023** desde la comparativa de las cuentas 2024; **2024** desde la comparativa de las cuentas 2025; **2025** desde las propias cuentas 2025 (no existe N+1). Se anota en `informe_usado`. Reexpresiones recogidas: BPA 2023 y 2024 reexpresados según IAS 33 (OPV) en los informes siguientes. Unidad impresa: **miles de euros** en todos los estados; acciones 2021/2022 impresas en **miles** (9,340 / 133,124) y 2023–2025 en **unidades**. Páginas citadas = página del PDF (la del visor).
- **Resultado:** `HISTORIA.csv`, 183 filas (2021–2025 × 27 filas con componentes; 2019–2020 × 24). 123 `encontrado`, 2 `cero_con_evidencia`, 58 `no_encontrado`.

## Lo que no encontré y por qué

- **2016–2018:** sin informe anual oficial en web/regulador (dicho arriba); sin filas.
- **2019–2020:** el informe anual oficial no trae estados financieros consolidados → 48 filas `no_encontrado`.
- **`intereses` e `intereses_financiacion` (2021–2025):** el estado de flujos no desglosa los intereses pagados; la línea de financiación es combinada ("Repayment of bank borrowings and interests"). El gasto financiero del P&L sí está en la nota de Financial result (va en `ebit_derivado`), pero no los intereses pagados en efectivo → `no_encontrado` honesto.
- **`adquisiciones` = 0 con evidencia en 2023 y 2025:** línea "Business Combinations (net of cash)" con guion en el estado de flujos.

## Dudas de definición / decisiones tomadas

- `ebit` impreso = **"Operational profit"** (subtotal inmediato al resultado financiero); el informe imprime también "Operating profit" antes de "Other operational income and expenses" (anotado en `nota`).
- `ebit_derivado` = BAI − **"Financial result"** (única línea impresa entre resultado operativo y BAI); la línea de participadas ("Result from associates and joint ventures...") queda **dentro** del EBIT derivado según la plantilla.
- `da` = línea "Depreciation and Amortization" del estado de flujos (incluye derecho de uso).
- `capex` = "Purchases of property, plant and equipment and intangible".
- `circulante_lineas` = la única línea impresa de circulante ("Changes in working capital", neto de perímetro y partidas sin caja).
- `adquisiciones` = "Business Combinations (net of cash)"; la línea aparte "Acquisition of non-controlling interests" no se incluye.
- `deuda` = "Bank borrowings" corriente + no corriente (sin pasivos NIIF 16).
- `arrendamientos` = pasivos por arrendamiento NIIF 16 de la nota de Leases (no corriente dentro de "Provisions and other liabilities"; corriente dentro de "Other current liabilities"); `arrendamientos_principal` = "Repayment of lease debt".
- `otros_activos_financieros` = línea del balance "Other current assets" (la nota de activos financieros clasifica como financieros corrientes a trade receivables + other current assets; la línea incluye anticipos e impuestos según su desglose).
- `pensiones` = "Employee pension plans" (neto) de la nota de provisiones.
- `sbc` = "multiannual employee remuneration" (planes SARs) dentro de gastos de personal; en 2024 hubo además un premio excepcional de OPV de 94.340 miles (no incluido, anotado).
- `id` = "Research and development expenses" de la nota de gastos operativos.
- `acciones_diluidas` = número medio de acciones para el BPA de la nota de BPA; sin diferencia diluido/básico. 2021/2022 impresos en miles; 2023/2024 reexpresados (IAS 33) en los informes siguientes.

## Modelo y herramientas usadas de verdad

- Modelo: `mistral-large-4-0`. Herramientas: `python3` + `urllib` (descarga de los PDF desde puig.com/uploads.puig.com; `curl`/`wget` bloqueados en el entorno), `hashlib` (SHA-256), `pypdf` (texto por página con marcas `[PDF PAGE n]`), `grep`/`read_file` sobre ese texto y `python3`+`csv` para los CSV. Todas las cifras salen de los PDF oficiales descargados; sin memoria externa.
