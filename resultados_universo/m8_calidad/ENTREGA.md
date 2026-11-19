# ENTREGA · M8 calidad · Bloque B (rama `mistral/m8-calidad-b`)

Fecha: 19-nov-2026. Empresas del bloque B: Intuitive, LOreal, LVMH, Lifco, London_Security, Moncler, Puigbrands, Rational.

## Qué encontré

- `DATOS.csv`: 8 empresas × 22 filas = 176 filas (más cabecera). Por empresa: documento del informe anual y del informe intermedio (título, fecha de publicación, URL, SHA-256 del PDF descargado **solo para la huella — no subido a Git**, página 1 y cita), las 9 partidas del último ejercicio completo (FY2025) y de los últimos 12 meses (LTM = FY2025 + periodo intermedio 2026 − periodo comparativo 2025 del mismo intermedio, marcado `calculado` con la fórmula en la nota), acciones en circulación sin autocartera a la fecha publicada más reciente, y precio de cierre del 18-nov-2026 en la bolsa principal.
- Fuentes oficiales usadas: ISRG — 10-K FY2025 y 10-Q 3T2026 en SEC EDGAR (HTML; no hay PDF del 10-Q en el registro); L'Oréal — DEU 2025 y rapport financier semestriel 2026 en loreal-finance.com; LVMH — DEU 2025 (AMF D.26-0195) y rapport semestriel 2026 en lvmh.com; Lifco — annual report 2025 y interim 9M 2026 en lifco.com/mfn.se; London Security — Annual Report 2025 e Interim 2026 (ejercicio a 31-dic) en londonsecurity.org; Moncler — Annual Report 2025 y Half-Year Report 30-jun-2026 (eMarket Storage/Borsa Italiana); Puig — Cuentas Anuales Consolidadas 2025 (CNMV, 18-feb-2026) e informe financiero semestral 30-jun-2026 (31-jul-2026) en puig.com/uploads; Rational — Annual Report 2025 (19-mar-2026) y Statement 9M 2026 (05-nov-2026) en rational-online.com.
- Precios de cierre 18-nov-2026 (todas las bolsas cerraron ese día): ISRG 420.95 USD (Nasdaq), OR 443.05 EUR (Euronext Paris), MC 388.10 EUR (Euronext Paris), LIFCO B 285.60 SEK (Nasdaq Stockholm), LSC 3.700 GBX = 37.00 GBP (AIM London), MONC 41.20 EUR (Borsa Italiana), PUIG 20.00 EUR (BME), RAA 610.00 EUR (Xetra). Cada uno en `fuentes_mercado/<Empresa>_precio_2026-11-18.csv` con fuente y fecha de consulta; huellas SHA-256 de CSV de precios y de cada PDF fuente en `fuentes_mercado/HUELLAS.txt` (los PDF se marcan "no en Git").
- Cifras tal como están impresas (número, signo, unidad y moneda de cada documento); las sumas de partidas impresas (p. ej. deuda como suma de corriente + no corriente) van como `calculado` con la cita de las partidas sumadas.

## Qué no encontré y por qué (`no_encontrado`, con motivo en `nota`)

- **Intuitive (10-Q 3T2026):** no desglosa pagos de principal de arrendamientos (el 10-K p. 106 afirma "The Company currently does not have any finance leases"; los operating leases van en otras partidas) ni el pasivo por arrendamiento del arrendatario a 30-sep-2026 (solo en el 10-K: 170.9 M USD a 31-dic-2025).
- **LVMH, Lifco, London_Security, Rational:** no publican la compensación en acciones como línea separada (LVMH/Lifco va dentro de "non-cash items"/"autres retraitements"; Rational afirma en la nota 27 del AR 2025 que no hubo acuerdo de pago en acciones en 2025; el estado 9M 2026 de Rational no publica SBC).
- **Rational a 30-sep-2026:** el estado 9M 2026 no desglosa "Other financial liabilities" (38.388 miles EUR en total) entre arrendamientos y resto; el desglose solo está en el AR anual (nota 18: lease liabilities 27.144 miles EUR a 31-dic-2025). Rational no tiene deuda bancaria.

## Modelo y herramientas reales

- Modelo: `mistral-large-4-0` (sesión Vibe Code, 19-nov-2026).
- Herramientas: `web_search` / `web_search_finance_search` (búsqueda de documentos oficiales y tarjetas de precio con serie diaria), descarga con Python `urllib` (UA descriptivo; SHA-256 local), `ocr_document` (OCR de cada PDF a Markdown por página para localizar página y cita literal), `stockanalysis.com` historial diario (datos S&P Global) como fuente de precio cruzada con la tarjeta finance, y `git`/`gh` para commit por empresa y push a `origin` (`jluisplagos/munger-v2-evidencias-mistral`).
- 8 commits (uno por empresa) en `mistral/m8-calidad-b`. Sin PDF/XLSX/ZIP en Git; sin valorar ni recomendar (solo datos con fuente); trabajo sin autoaprobar.
