# Entrega · Ventana 2 (Zoetis Inc.) · Historia de diez años independiente

- **Empresa / años:** Zoetis Inc., ejercicios 2016–2025 (diez años, año natural terminado el 31-dic).
- **Fuentes usadas:** solo los diez 10-K `zoetis-10k-fy2016.pdf` … `zoetis-10k-fy2025.pdf` del release `fuentes-examen-20261118` de `jluisplagos/munger-v2-evidencias-mistral`. SHA-256 de los diez archivos comprobados contra `coordinacion/cierre_v2/examen/RELEASE_FUENTES_EXAMEN_SHA256SUMS` (rama `coordinacion/cierre-v2`): los diez coinciden. No abrí ningún 10-Q, comunicado ni presentación posterior al 9-oct-2026, ni ninguna carpeta del expediente en `munger-v2`.
- **Regla de informe:** para el año N usé la columna comparativa del 10-K de N+1 (p. ej. 2016 desde `zoetis-10k-fy2017.pdf`); 2025 desde el propio `zoetis-10k-fy2025.pdf` (no existe N+1). Se anota en la columna `informe_usado`. Páginas citadas = página del PDF (la del visor). Unidad impresa: millones de USD (acciones: millones de acciones).
- **Resultado:** `HISTORIA.csv`, 304 filas (23 partidas × 10 años, con componentes). 251 `encontrado`, 43 `cero_con_evidencia`, 10 `no_encontrado`.

## Lo que no encontré y por qué

- **`ebit` impreso (10 filas `no_encontrado`):** la cuenta de resultados consolidada de Zoetis no imprime en ningún año un subtotal de resultado de explotación/operating income; las líneas saltan de los gastos a `Income before provision for taxes on income`. Por eso el EBIT de la historia sale solo como `ebit_derivado` (= BAI − `Interest expense, net of capitalized interest`; `Other (income)/deductions—net` queda dentro del EBIT derivado según la plantilla).

## Ceros con evidencia (43)

- `intereses_financiacion` = cero en los diez años: bajo US GAAP los intereses pagados se clasifican en actividades de explotación (se declaran en el cuadro complementario del propio estado de flujos); la sección de financiación no tiene línea de intereses.
- `arrendamientos` = cero en balance en 2016–2018 (pre-ASC 842; los arrendamientos operativos solo eran compromisos). Desde 2019: pasivos ASC 842 (operativos + financieros desde 2023), corriente y no corriente según la nota de arrendamientos.
- `arrendamientos_principal` = cero en 2016–2023. **US GAAP: los arrendamientos operativos no tienen «principal» en financiación** (sus pagos son flujos de explotación). Solo hay principal de arrendamiento financiero desde 2023: 2024 = 1, 2025 = 2 (nota de arrendamientos, "Financing cash flows – finance leases").
- `otros_activos_financieros` = cero salvo 2018 (`Short-term investments` 99, p. 73 del 10-K fy2019).
- `deuda`: componente `Short-term borrowings` cero en 2016 (nota de deuda: "no commercial paper outstanding… no other short-term borrowings", p. 89 de fy2017), 2017, 2019, 2021, 2024, 2025; `Current portion of long-term debt` cero en 2016–2018, 2021, 2023, 2025. La deuda financiera declarada excluye los pasivos por arrendamiento (líneas aparte en el balance).
- `minoritarios` = cero (—) en 2018, 2019, 2024, 2025.

## Dudas de definición / decisiones tomadas

- `circulante_lineas`: las seis líneas impresas del bloque «Other changes in assets and liabilities» cada año, incluida `Other tax accounts, net` (línea de impuestos dentro del bloque de circulante; no hay línea separada de «impuestos pagados» en el bloque).
- `adquisiciones`: pagos por adquisiciones (neto de caja adquirida) menos cobros por venta de negocios (2023: (155) − 96; 2024: (8) − 293; 2025: (24) − (4)). Las líneas «Net proceeds from sales of assets» (venta de activos, no de negocios) no se incluyen; quedan anotadas.
- Reclasificación de presentación detectada y anotada: 2016 `Other liabilities` (295) en fy2017 vs (290) en fy2018/fy2019, y 2017 (57) en fy2017 vs (38) en fy2018/fy2019, por mover 5/19 de «Restructuring». Uso N+1 según la regla y lo dejo en `nota`.
- `pensiones`: déficit neto (funded status) de los planes de pensiones dedicados según la nota de pensiones; el balance no desagrega pensiones.
- 2025 `deuda` (9,042) incluye el bono convertible de 2,000 emitido en 2025 (está en la línea de deuda a largo plazo).

## Modelo y herramientas usadas de verdad

- Modelo: `mistral-large-4-0`. Herramientas: `gh` CLI (descarga del release y verificación SHA-256 con `sha256sum`), extracción OCR de los PDF a texto por página (herramienta `ocr_document` del entorno, sobre los archivos descargados en local), `grep`/`read_file` sobre ese texto por páginas, y `python3` (csv) para generar `HISTORIA.csv`. Sin internet, sin memoria externa: todas las cifras salen de los diez 10-K verificados.
