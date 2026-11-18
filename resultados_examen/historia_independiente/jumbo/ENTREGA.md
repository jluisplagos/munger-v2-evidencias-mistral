# Entrega · Ventana 1 (Jumbo S.A.) · Historia de diez años independiente

- **Empresa / periodos:** Jumbo S.A. (JUMBO GROUP, Atenas; IFRS-UE, EUR). Diez periodos: ejercicios jul–jun 2016/17, 2017/18 y 2018/19; **periodo de transición de seis meses 01.07.2019–31.12.2019** (cambio a año natural, tratado como periodo propio, `anio=2019T`); y años naturales 2020–2025.
- **Fuentes usadas:** los informes de Jumbo del release `fuentes-examen-20261118` de `jluisplagos/munger-v2-evidencias-mistral`: 8 PDF (`jumbo-annual-report-fy2017-18/fy2018-19/transition-2019/fy2021/fy2024/fy2025.pdf` y `9a9c_jumboannualreport_31122020_en.pdf` = FY2020) y los XHTML `jumbo-annual-report-fy2022.xhtml` / `-fy2023.xhtml`. Los 10 archivos jumbo descargados se verificaron con SHA-256 contra `coordinacion/cierre_v2/examen/RELEASE_FUENTES_EXAMEN_SHA256SUMS` (rama `coordinacion/cierre-v2`): los 10 coinciden. `jumbo-annual-report-fy2016-17.pdf` quedó descargado y verificado pero **no usado**: su columna actual se sustituye por el comparativo de fy2017-18 según la regla. No abrí ninguna carpeta `jumbo/` del expediente en `munger-v2`.
- **Regla de informe:** para el periodo N usé la columna comparativa del informe de N+1 (anotado en `informe_usado`): 2016/17 desde fy2017-18; 2017/18 desde fy2018-19; 2018/19 (P&L, flujos y balance 30.06.2019) desde el informe de transición; 2019T (P&L y flujos de 6 meses) desde el informe de transición y su balance 31.12.2019 desde el comparativo de FY2020; 2020 desde fy2021; 2021 desde el XHTML fy2022; 2022 desde el XHTML fy2023; 2023 desde fy2024; 2024 desde fy2025; 2025 desde fy2025 (no hay N+1). **Unidad impresa: euros** (no miles) en los diez informes; `acciones_diluidas` en acciones. Páginas = página del PDF (visor); en los XHTML no hay páginas de PDF y se cita la sección y la página impresa (pie).
- **Resultado:** `HISTORIA.csv`, 328 filas (24 partidas × 10 periodos, con componentes): 260 `encontrado`, 68 `cero_con_evidencia`, 0 `no_encontrado`. Todas las filas llevan archivo, SHA-256, página, cita literal y estado.

## Lo que no encontré y por qué

- Nada quedó `no_encontrado`: las 24 partidas existen (como cifra o como cero con evidencia) en los diez periodos.

## Ceros con evidencia (68)

- `minoritarios` = 0 ('-') en los diez periodos (balance y cuenta de resultados).
- `sbc` e `id` = 0 en los diez periodos: el desglose completo de gastos (nota 5.3 de cada informe) no tiene línea de pagos basados en acciones ni de I+D.
- `intereses_financiacion` = 0 en los diez periodos: los intereses pagados figuran en actividades de explotación ('Interest paid'/'Interest payable'); en financiación solo constan los intereses de arrendamientos, que son parte de `arrendamientos`.
- `arrendamientos` (pasivo NIIF 16) = 0 a 30.06.2017, 30.06.2018 y 30.06.2019, y `arrendamientos_principal` = 0 en 2016/17–2018/19: IFRS 16 se adoptó el 01.07.2019 con enfoque modificado **sin reexpresar comparativos** (nota impresa en el informe de transición).
- `adquisiciones` = 0 en 2016/17–2022 y 2024 (sin línea de adquisición de negocios en el estado de flujos); 2023: pago (1.200.000) y caja adquirida 898.919 (neto (301.081)); 2025: (1.200.000) + (10.705.577).
- `otros_activos_financieros` = 0 a 30.06/2017 y 30.06/2018: en esos balances no hay línea de activos financieros corrientes distintos de caja; la reclasificación de depósitos >3 meses a 'Other current financial assets' solo se publicó desde el informe de transición (30.06.2019: 418.460.513). De 2019 a 2025 la partida = 'Other current financial assets' + depósitos restringidos a corto plazo.
- `deuda` = 0 a 31.12.2023 y 31.12.2025 (nota de préstamos: revolving/bono = '-'; sin préstamos a largo plazo esos años). En los demás cierres, deuda = bono no convertible (largo plazo) + porción corriente del bono + préstamos a corto plazo; **excluye** los pasivos NIIF 16 (líneas aparte).
- Ceros parciales en componentes: 'Other financial results' = 0 en 2017/18–2024 (en 2016/17 y 2025 sí hay cifra), y líneas de circulante puntuales ('Other', 'Non-short-term restricted bank deposits') = 0 en 2021 y 2022.

## Dudas de definición / decisiones tomadas

- `ebit` impreso existe en los diez periodos ('Profit before tax, interest and investment results'); además `ebit_derivado` = BAI − (finance costs + finance income + other financial results), con signo −1 en el bloque financiero. En 2019–2024 el estado no imprime línea separada de 'Other financial results': usé el subtotal impreso del bloque, que cuadra con la suma de costs+income. Cuadra con el EBIT impreso en todos los años (diferencias de redondeo de 1–2 € en 2016/17 y 2017/18, anotadas).
- `da` se tomó de la nota de flujos de explotación (5.30/5.31, 'Depreciation of tangible/intangible assets'), no del estado principal, que en estos informes no desagrega D&A.
- `circulante_lineas` = todas las líneas del bloque 'Changes in working capital' de la nota de flujos (incluidas 'Non-short-term restricted bank deposits' y 'Other' cuando aparecen).
- Reexpresiones anotadas: 2017/18 con comisiones de tarjetas reclasificadas a 'Finance costs' (nota bajo la cuenta de fy2018-19, p.41); ajuste IFRS 9 de (1.815.501) en el patrimonio inicial 01.07.2018 según el estado de cambios (p.44 de fy2018-19) — el balance comparativo imprime 1.058.468.883, que es el que uso; depósitos >3 meses reclasificados en 30.06.2019.
- En fy2025 la nota 5.23 imprime 7.630.467 de lease corriente a 31.12.2024 frente a 7.630.869 en el balance; usé el balance (el total impreso 75.183.110 cuadra con las líneas del balance).
- `acciones_diluidas`: no hay instrumentos dilutivos en ningún año ('no titles/securities potentially convertible into shares'), así que diluido = básico (media ponderada 136.059.759 acciones en los diez periodos).

## Modelo y herramientas usadas de verdad

- Modelo: `mistral-large-4-0`. Herramientas: `gh` CLI (descarga del release y verificación SHA-256 con `sha256sum`), `python3` + `pypdf` (instalado con pip) para extraer el texto por página de los 8 PDF con marcadores `[PDF PAGE n]`, `beautifulsoup4` (ya presente) para los XHTML, `grep`/`read_file` sobre esos textos, y `python3` (módulo `csv`) para generar `HISTORIA.csv`. Solo lectura del repo auxiliar `jluisplagos/munger-v2` (rama `examen/ahold-f1`, plantilla `01_historia_2016.md`); no escribí allí. Los PDF no se suben a Git.
