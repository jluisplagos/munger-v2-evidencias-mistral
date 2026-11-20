# Entrega · Bloque 8 (Rational) · Historia de diez años independiente · M10

- **Empresa / años:** RATIONAL AG (ETR: RAA, Landsberg am Lech). Ejercicio **natural** (cierre 31-dic). Los diez últimos ejercicios cerrados a la fecha del encargo son **2016–2025**.
- **Fuentes usadas:** los diez informes anuales oficiales en inglés descargados de la web de inversores (`https://www.rational-online.com/.../annual-reports...`, archivo oficial "annual reports archive" y publicaciones por ejercicio) el **20-nov-2026** (UTC). URL, fecha y SHA-256 de cada PDF en `FUENTES.csv` (y el SHA por fila en `HISTORIA.csv`). Ningún PDF se sube a Git. No abrí `coordinacion/cierre_v2/universo_etapa1/` ni ningún expediente de `munger-v2` salvo la plantilla genérica indicada en el encargo M4.
- **Regla de informe:** para el año N usé la **columna comparativa del informe de N+1** (p. ej. 2016 desde `rational-ar-2017.pdf`); 2025 desde el propio `rational-ar-2025.pdf` (no existe N+1). Se anota en `informe_usado`. Reexpresiones recogidas: **2021** reexpresado según IAS 8.14 en el informe 2022 (CFO 172,101; circulante y intereses pagados ajustados) y **2023** reexpresado según IAS 8 (impuestos diferidos) en el informe 2024 (beneficio 213,968; patrimonio 760,789). Unidad impresa en todos los informes: **miles de euros (kEUR)**; acciones en **unidades**. Páginas citadas = página del PDF (la del visor).
- **Resultado:** `HISTORIA.csv`, 318 filas (24 partidas × 10 años, con componentes). 276 `encontrado`, 42 `cero_con_evidencia`, 0 `no_encontrado`.

## Ceros con evidencia (42)

- `sbc` = 0 en los diez años: nota "Share-based payment" de cada informe: «There was no share-based payment agreement in YYYY…» (plan de opciones de 2000 liquidado en efectivo en 2002 y 2006).
- `minoritarios` = 0 en los diez años: el patrimonio se compone solo de subscribed capital, capital reserves, retained earnings y other components (suman el total); no hay línea de NCI en el balance ni en el estado de cambios en patrimonio.
- `adquisiciones` = 0 en los diez años: la sección de inversión del estado de flujos no incluye línea de adquisiciones/ventas de negocios.
- `arrendamientos` (NIIF 16) = 0 en 2016–2018 (pre-NIIF 16, fuera de balance; aplicada desde 1-ene-2019 sin reexpresar comparativos); desde 2019, corriente + no corriente de la nota 19 ("Lease liabilities" dentro de "Other financial liabilities").
- `arrendamientos_principal` = 0 en 2016–2018 (sin línea en financiación); desde 2019, línea "Payments for lease liabilities".
- `deuda` = 0 en 2023–2025: línea "Financial debt" con guion en el balance (deuda bancaria devuelta en 2024; AR 2025: «As a Group without financial debt»).
- `ebit_derivado`: línea "Other financial result" con guion en 2016–2017 (cero con evidencia como componente).

## Dudas de definición / decisiones tomadas

- `ebit` impreso existe todos los años ("Earnings before financial result and taxes (EBIT)"; en 2016 "Earnings before interest and taxes"). `ebit_derivado` = BAI − resultado financiero, incluyendo "Other financial result" y, desde 2022, la línea IAS 29 (hiperinflación Turquía), que quedan entre el EBIT y el EBT.
- `da` = línea "Depreciation and amortisation" del estado de flujos.
- `capex` = "Capital expenditures in intangible assets and property, plant and equipment" (única línea de inversión en inmovilizado).
- `circulante_lineas` = las cuatro líneas del bloque "Changes in" (inventories, trade receivables and other assets, provisions, trade payables and other liabilities); los impuestos pagados van aparte (no se incluyen).
- `intereses` = "Interest paid" (financiación); por tanto `intereses_financiacion` = el mismo importe.
- `deuda` = "Financial debt" / "liabilities to banks" corriente + no corriente (préstamos inmobiliarios); **sin** los pasivos por arrendamiento NIIF 16.
- `otros_activos_financieros` = activos financieros corrientes no caja: "Deposits" (2016, en AR 2017) / "Other financial assets" corriente.
- `pensiones` = línea del balance "Provisions for pensions" / "Pension plans and similar commitments" / "Pension and similar obligations" (provisión neta IAS 19).
- `id` = línea "Research and development expenses" de la cuenta de resultados (impresa negativa).
- `acciones_diluidas` = "Average number of shares (undiluted/diluted)" = 11,370,000 todos los años, en unidades.

## Modelo y herramientas usadas de verdad

- Modelo: `mistral-large-4-0`. Herramientas: `python3` + `urllib` (descarga de los PDF desde rational-online.com; `curl`/`wget` están bloqueados en el entorno), `hashlib` (SHA-256), `pypdf` (extracción de texto por página con marcas `[PDF PAGE n]`), `grep`/`read_file` sobre ese texto y `python3`+`csv` para generar los CSV. Todas las cifras salen de los diez PDF oficiales descargados; sin memoria externa.
