# Entrega · Bloque 3 (FW Thorpe) · Historia de diez años independiente · M10

- **Empresa / años:** FW Thorpe plc (LSE AIM: TFW). Ejercicio **no natural**: termina el **30 de junio**. Por la regla del encargo ("los diez últimos cerrados si el ejercicio no es natural"), los diez últimos ejercicios cerrados a la fecha del encargo (19-nov-2026) son los terminados el **30-jun-2017 … 30-jun-2026** (el informe 2026, aprobado el 1-oct-2026, ya estaba publicado). Se anota `periodo_exacto` = ejercicio terminado el 30-jun-20XX en cada fila.
- **Fuentes usadas:** los diez informes anuales oficiales `annual-report-2017.pdf` … `annual-report-2026.pdf` descargados de la web de inversores (`https://www.fwthorpe.co.uk/pdf/fw-thorpe-annual-report-YYYY.pdf`) el 20-nov-2026. URL, fecha y SHA-256 de cada PDF en `FUENTES.csv` (y el SHA por fila en `HISTORIA.csv`). Ningún PDF se sube a Git. No abrí `coordinacion/cierre_v2/universo_etapa1/` ni ningún expediente de `munger-v2`.
- **Regla de informe:** para el año N usé la **columna comparativa del informe de N+1** (p. ej. 2017 desde `annual-report-2018.pdf`); 2026 desde el propio `annual-report-2026.pdf` (no existe N+1). Se anota en `informe_usado`. Páginas citadas = página del PDF (la del visor). Unidad impresa: **miles de GBP (£'000)**; acciones en unidades.
- **Resultado:** `HISTORIA.csv`, 336 filas (24 partidas × 10 años, con componentes). 305 `encontrado`, 31 `cero_con_evidencia`, 0 `no_encontrado`.

## Lo que no encontré / ceros con evidencia (31)

- `minoritarios` = cero en los diez años: el grupo no presenta NCI en patrimonio; las obligaciones contractuales de compra a minoritarios (Zemper, SchahlLED/Lumen) se reconocen como **pasivo financiero** (redemption liability) según la política contable "Non-controlling interests" (citada por fila).
- `arrendamientos` (NIIF 16) = cero en balance en 2017 y 2018 (bajo IAS 17, fuera de balance; NIIF 16 adoptada el 1-jul-2019); desde 2020, corriente + no corriente según balance.
- `arrendamientos_principal` = cero en 2017–2019 (pre-NIIF 16); desde 2020, línea de pagos de arrendamiento en financiación.
- `intereses_financiacion` = cero en 2017–2019 y 2021 (sin línea de pago de intereses en financiación); 2020 y 2022–2026: línea "Payment of (lease) interest".
- `deuda` = cero en 2017 (sin línea "Financial liabilities"; préstamo Spuiweg nil). En 2018–2021 el balance no trae línea "Financial liabilities": la deuda es el **préstamo de Spuiweg Holding B.V.** (1% sobre base del Banco de Inglaterra) dentro de "otras partidas a pagar" (2018: 2.336; 2019: 2.139; 2020: 1.971; 2021: 899, en £'000), citado de la nota. Desde 2022 la línea "Financial liabilities" del balance incluye sobre todo **redemption liabilities** a valor razonable (pasivo por canje de participaciones a minoritarios), no deuda bancaria; se anota en `nota`.
- `adquisiciones`: ceros con guion/impresos en 2019, 2020, 2021, 2024, 2026; pagos en 2017 (240), 2018 (6.313, Famostar), 2022 (14.625 subsidiaries + 4.958 JV + 15.219 depositary receipts, Zemper), 2023 (12.602, Lumen), 2025 (813 contraprestación diferida; cobro 287 por venta de filial).

## Dudas de definición / decisiones tomadas

- `ebit` impreso = "Operating profit" (existe todos los años). `ebit_derivado` = BAI − (finance income + finance costs/expense); la línea "Share of (profit)/loss of joint ventures" queda **dentro** del EBIT derivado según la plantilla (no se resta).
- `da` = componentes de la nota "Cash generated from operations" (depreciación PPE + depreciación inversión inmobiliaria + amortización/deterioro de intangibles).
- `capex` = compras de PPE + intangibles; la compra de **inversión inmobiliaria** va en línea aparte y se anota como componente separado con nota.
- `circulante_lineas` = las tres líneas de "Changes in working capital" de la nota (inventarios, deudores, acreedores y provisiones); el impuesto pagado va aparte (no se incluye).
- `id` = "Research and development expenditure credit" de la nota: en todos los años es un **crédito** (valor negativo impreso entre paréntesis); se registra tal como está impreso.
- `sbc` = "Share-based payment charge" de la nota de flujos (2017–2021, 2025, 2026); en 2022–2024 se toma de la nota de pagos basados en acciones / estado de cambios en patrimonio (2022: (348) por share appreciation rights; 2023: guion; 2024: 152).
- `pensiones` = "Surplus in the scheme" de la nota 22 (neto obligación−activos; superávit positivo). El activo no se reconoce en balance por techo de activo (asset ceiling); se anota en `nota`.
- `otros_activos_financieros` = short-term financial assets + otros activos financieros corrientes a VR + activos financieros corrientes a coste amortizado (pagarés, p. ej. Ratio EV).
- `acciones_diluidas` = número medio ponderado diluido de la nota de BPA, en **unidades** (no miles).

## Modelo y herramientas usadas de verdad

- Modelo: `mistral-large-4-0`. Herramientas: `python3` + `urllib` (descarga de los PDF desde fwthorpe.co.uk; `curl` está bloqueado en el entorno), `hashlib`/`sha256sum` (SHA-256), `pypdf` (extracción de texto por página con marcas `[PDF PAGE n]`), `grep`/`read_file` sobre ese texto y `python3`+`csv` para generar `HISTORIA.csv`. Todas las cifras salen de los diez PDF oficiales descargados; sin memoria externa.
