# ENTREGA · M8 bloque A · datos oficiales de las 8 empresas de calidad

Fecha: 2026-11-19. Rama: `mistral/m8-calidad`. Encargo: `coordinacion/cierre_v2/universo_etapa1/m8/ENCARGO_MISTRAL_M8_CALIDAD.md` (rama `coordinacion/cierre-v2`). Solo datos con fuente; sin valoraciones ni recomendaciones.

## Qué encontré (todo con documento, página, cita literal y SHA-256)

8 empresas del bloque A, 229 filas en `DATOS.csv` ( estados: 108 `impreso`, 85 `calculado`, 16 `publicado`, 10 `verificado`, 10 `no_encontrado` ):

| Empresa | Documento anual (fuente oficial) | Intermedio más reciente | Precio 18-nov-2026 (bolsa principal) |
|---|---|---|---|
| ABB | Annual Reporting Suite 2025 (ABB Library, pub. 2026-02-20; sección financiera = Financial Report 2025) | Q3-2026 Financial Information (EQS/Nasdaq, 2026-10-20) | ABBN XSWX 67,98 CHF |
| ASML | Annual Report 2025 IFRS (pub. 2026-02-25) | Q3/9M-2026: PR Euronext CPR + 6-K estados US GAAP (SEC, pub. 2026-10-14) | ASML XAMS 1.260,80 EUR |
| Andina | Memoria Integrada 2025 + 4T25 FECU (koandina/CNMV) | 6-K estados interinos 30-sep-2026 (SEC CIK 925261) | ANDINA-B XSN 4.780,30 CLP |
| Bioventix | Annual Report FY2026 (year ended 30-jun-2026, FRS 102) | Interim Results H1 31-dic-2025 | BVXP XLON 1.950,00 GBX |
| FW_Thorpe | Annual Report FY2026 (year ended 30-jun-2026, UK IAS) | Interim Report H1 31-dic-2025 | TFW XLON 260,00 GBX |
| Ferrari | Form 20-F FY2025 (SEC CIK 1648416, filed 2026-02-19; el PDF de cdn.ferrari.com da 403, se usa la copia del regulador) | 6-K Interim Report 9M-2026 (SEC, 2026-11-03, IAS 34) | RACE XMIL 374,65 EUR (NYSE RACE: 410,91 USD) |
| Hermes | URD 2025 (AMF 2026-03-19, versión EN de finance.hermes.com) | Half-Year Financial Report June 2026 (2026-07-29) | RMS XPAR 1.278,50 EUR |
| Inditex | Cuentas anuales consolidadas FY2025 ended 31-jan-2026 (inditex.com, CNMV, Board 2026-03-10) | Informe intermedio consolidado H1-2026 to 31-jul-2026 (2026-09-09, CNMV) | ITX XBME 59,36 EUR |

Por empresa: documento anual + intermedio (título, fecha, URL, SHA-256 en `HUELLAS.txt`; los PDF/HTML no van a Git), ventas, EBIT, flujo de caja de operaciones, capex, pagos de principal de arrendamientos, compensación en acciones, caja, deuda financiera sin arrendamientos, pasivos por arrendamiento y acciones en circulación (sin autocartera) para el último ejercicio completo, el periodo intermedio y LTM (ejercicio + intermedio − comparable del año anterior), más precio de cierre del 18-nov-2026 con serie diaria 2026-10-19→2026-11-18 conservada en `fuentes_mercado/` (CSV con su SHA-256 en `HUELLAS.txt`, fuente Yahoo Finance tabla histórica del ticker de la bolsa principal, consultada el 2026-11-19).

Cifras tal como están impresas (unidad y moneda del documento: ABB USD M US GAAP; ASML € M IFRS annual / USD M US GAAP intermedio; Andina COP miles IFRS; Bioventix/FW_Thorpe £'000; Ferrari/Hermès/Inditex € M IFRS). Los `calculado` son sumas/restas de líneas impresas del mismo documento (p. ej. capex = intangibles + PP&E del flujo de caja; deuda sin arrendamientos = deuda total − arrendamientos; acciones = emitidas − autocartera; LTM = FY + intermedio − comparable; en Inditex, principal de arrendamiento = pago fijo − intereses de arrendamiento). Nada se estima.

## Qué no encontré y por qué (10 filas `no_encontrado`, con motivo en `nota`)

- **ABB** pagos de principal de arrendamientos LTM al 30-sep-2026: el informe intermedio Q3-2026 no publica el desglose de pagos de arrendamientos de los 9M (solo el anual lo tiene).
- **ASML** pagos de principal de arrendamientos 9M-2026 y pasivos por arrendamiento al 2026-09-27: los estados trimestrales US GAAP (6-K) no los desagregan; último dato publicado: pasivo por arrendamiento 251,4 al 31-dic-2025 (anual IFRS, nota 14).
- **Andina** compensación en acciones FY2025, 9M-2026 y LTM: ni los estados consolidados ni la Memoria Integrada 2025 ni el 6-K intermedio publican partida de share-based compensation.
- **Bioventix** pagos de principal de arrendamientos FY2026/H1-2026/LTM y pasivos por arrendamiento al 31-dic-2025: el flujo de caja (anual e interino) no desagrega esos pagos y el balance interino no desagrega los arrendamientos; último dato publicado: 10.970 al 30-jun-2026 (nota 20 del AR26).

## Modelo y herramientas reales

Agente **Vibe Code** con modelo **mistral-large-4-0** (Mistral AI), ejecutado en sandbox el 2026-11-19. Herramientas: shell/Python (`urllib` para descargas con SHA-256, `pypdf` para extracción de texto por página), `web_search`/`web_fetch` para localizar documentos oficiales (SEC EDGAR, webs IR de las empresas, AMF/CNMV) y las tablas históricas de Yahoo Finance, y `git`/`gh` para la rama y los push. Verificación: todas las URLs de documentos rehechas con HEAD/GET 200 y hash reproducido; `DATOS.csv` validado con `csv.DictReader` (229 filas × 13 columnas, sin campos nulos).
