# ENTREGA — Zoetis, segundo tiempo (publicado el 5-nov-2026) · extractor: Mistral

Encargo: `coordinacion/cierre_v2/examen/zoetis/ENCARGO_MISTRAL_ZOETIS_T2.md` (rama `coordinacion/cierre-v2`). Entrega en rama `mistral/examen-zoetis-t2`, carpeta `resultados_examen/zoetis_t2/`. Fecha de extracción: **2026-11-18** (reloj del sistema, UTC). No se valora ni recomienda nada; no se aprueba este trabajo (revisión pendiente por un agente distinto).

## Qué hice

- **Fuentes**: descargué de la Release `fuentes-examen-20261118` (`gh release download`) el 10-Q T3 2026, el comunicado y la presentación del T3; **SHA-256 coincidente 3/3** con `RELEASE_FUENTES_EXAMEN_SHA256SUMS`. Ningún PDF se commitea (AGENTS.md).
- **Bloque A — `CIFRAS_T3.csv`** (55 filas): partidas del 10-Q T3 en las columnas «nueve meses terminados el 30-sep-2026» y «… 2025» y el balance al 30-sep-2026 (acciones diluidas/básicas también del trimestre), cada una con valor impreso, signo, página del visor PDF, cita literal y estado. Cifras clave 9M-2026: ventas 7.121, beneficio antes de impuestos 2.353, neto atribuible 1.883, D&A (CFO) 357 + amortización de intangibles 93, CFO 1.880, capex (334), adquisiciones (155), intereses pagados 258, SBC 78, I+D 527, recompras (1.690), dividendos pagados (666); balance 30-sep-2026: caja 1.333, inversiones CP 200, deuda CP 750 / LP 8.299 (principal 9.150), patrimonio 3.303, arrendamiento operativo no corriente 188, acciones en circulación 406.316.147 (portada, 30-oct-2026).
- **Bloque B — `GUIA_2026.md`**: guía del 5-nov-2026 comparada línea a línea con la del 6-ago-2026 (la tabla del propio comunicado trae ambas columnas): ingresos $9.220–$9.320 (antes $9.120–$9.320), orgánico operacional (2)%–(1)% (antes (3)%–(1)%), BPA ajustado $6.25–$6.35 (antes $6.15–$6.25), renta neta ajustada $2.600–$2.640 (antes $2.570–$2.620), BPA reportado $5.50–$5.60, tipo de cambio de la guía «as of October 20, 2026»; con las frases literales de ambas fechas y citas de recompras/dividendo/deuda/reestructuración sin opinar.
- **Bloque C — `fuentes_mercado/`**: precio de cierre ZTS (NYSE) del **5-nov-2026 = $82.11** y del **6-nov-2026 = $79.4** (página oficial de la empresa, tabla «XNYS:ZTS historical stock data»; nyse.com bloquea el acceso automatizado, como permite el encargo) y **Treasury 10 años: 4,84 % (5-nov) y 4,86 % (6-nov)** (CSV oficial «Daily Treasury Par Yield Curve Rates» de home.treasury.gov). Conservados como texto con SHA-256 en `HUELLAS.txt` y `DESCARGAS.tsv`.
- Commit y push tras cada bloque (A, B, C) a `mistral/examen-zoetis-t2`.

## Qué no encontré y por qué

- **Beneficio operativo**: el 10-Q no lo imprime como línea (los gastos van línea a línea) → `no_encontrado` con nota.
- **Arrendamiento operativo corriente y arrendamiento financiero (pasivo)**: el 10-Q condensado no trae nota de arrendamientos ni líneas separadas en el balance; solo «Operating lease liabilities 188» (no corriente, p. 5) y los flujos «Operating cash flows - operating leases 51» / «Financing cash flows - finance leases 1» (p. 8) → `no_encontrado`, declarado; no se mezclan partidas.
- **Pensiones**: sin línea en el balance ni nota de pensiones en el 10-Q (solo OCI «Benefit plans» y la mención litigiosa) → `no_encontrado`.
- **Minoritarios**: guion «—» impreso en PyG, comprehensive income y balance → `cero_con_evidencia`.

## Dudas

- El 10-Q aplica el «Fiscal Year Alignment» (nota 2, p. 10): los comparativos 2025 están reexpresados; las cifras de 2025 de este segundo tiempo no son las «as previously reported».
- D&A: Zoetis publica por separado «Depreciation and amortization expense» (CFO) y «Amortization of intangible assets» (PyG); registro ambas partidas sin sumarlas.
- El comunicado es HTML (sin páginas); en `GUIA_2026.md` se cita por sección, y en la presentación por página del visor PDF.

## Modelo y herramientas realmente usados

Extractor **Mistral (mistral-large-4-0)** actuando como agente Vibe Code. Herramientas: `gh` (clone, release download, ramas, push), `python3` + `pypdf 7.1.1` (extracción de texto del 10-Q y la presentación, con marcas `[PDF PAGE n]`) + `hashlib` (SHA-256), `web_fetch` (investor.zoetis.com y home.treasury.gov), y shell. Sin LibreOffice ni XLSX. No se ejecutó ningún pipeline del producto ni se autoaprobó nada.

## Segundo encargo · LTM a 30-sep-2026 (`ENCARGO_MISTRAL_ZOETIS_T2_LTM.md`, rama `coordinacion/cierre-v2`)

- **Fuentes**: de la Release `fuentes-examen-20261118`, `zoetis-10k-fy2025.pdf` (sha256 `517a8d74…81efb`) y `zoetis-10q-2026-q3.pdf` (sha256 `f797be28…242bf`); ambos verificados contra `coordinacion/cierre_v2/examen/RELEASE_FUENTES_EXAMEN_SHA256SUMS`. Ningún PDF se commitea.
- **Entrega**: `LTM_3T.csv` (22 filas) con `partida, valor_ltm, unidad, cuenta (componentes con su valor), archivos, paginas, citas_literales, nota_base`. Fórmula usada en cada flujo: **LTM = FY2025 (10-K) + 9M2026 (10-Q) − 9M2025 (10-Q)**. Cifras LTM (mm USD): ventas **9.494**; beneficio antes de impuestos **3.142**; gasto por intereses **242**; EBIT **3.384**; D&A línea flujos **479** + amortización de intangibles (PyG) **124** = **603**; EBITDA **3.987**; CFO **2.728**; capex **(493)**; FCF **2.235**; intereses pagados **294**; beneficio neto atribuible **2.507**. Saldos al 30-sep-2026 (10-Q): caja 1.333; deuda CP 750 / LP 8.299 (principal 9.150, nota 9); arrendamiento operativo no corriente 188; patrimonio 3.303; minoritarios guion «—» (cero con evidencia, **no negativo**); acciones en circulación (portada, 30-oct-2026) 406.316.147.
- **Fiscal Year Alignment (nota 2 del 10-Q, p. 10-11)**: los nueve meses de 2025 del 10-Q T3 están **reexpresados (recast)** (p. ej. Revenue 9M2025: 7.080 as previously reported → 7.094 as recast; CFO 2.011 → 2.056); el FY2025 del 10-K está **as previously reported** (base con lag de un mes al 30-nov en filiales internacionales; Zoetis dice que recastará el FY2025 en futuros informes). Por eso cada fila de flujo lleva en `nota_base` que el LTM mezcla bases (FY2025 con lag vs 9M2025 recast): avisado, no mezclado en silencio.
- **No encontrado en el 10-Q** (declarado, no se inventa): pasivo por arrendamiento financiero en el balance (solo flujos «Financing cash flows - finance leases 1 2», p. 8) y arrendamiento operativo corriente (dentro de «Other current liabilities 113», p. 5). El CFO del 10-Q imprime además «Amortization of cloud computing implementation costs 13 8» (p. 8) como línea aparte; el 10-K FY2025 no la imprime separada, así que no entra en el LTM de D&A.
- **D&A**: las dos líneas que publica Zoetis («Depreciation and amortization expense» del CFO y «Amortization of intangible assets» de la PyG) se dan por separado y se suman una sola vez para el EBITDA (479 + 124 = 603).
- Sin valoración ni recomendación; revisión pendiente por un agente distinto. Mismo modelo y herramientas que arriba (`gh`, `python3` + `pypdf 7.1.1`, `hashlib`, shell). Commit y push a `mistral/examen-zoetis-t2`.
