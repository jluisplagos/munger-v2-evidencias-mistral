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
