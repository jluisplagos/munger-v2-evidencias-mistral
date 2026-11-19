# Verificación de la Release `fuentes-examen-20261118` (repositorio auxiliar)

Fecha: 18-nov-2026. Comprueba: el coordinador Claude. Material: los 67 assets de la Release, descargados con `gh api …/releases/assets/<id>` (389,8 MB). Huellas de los 67 en `RELEASE_FUENTES_EXAMEN_SHA256SUMS` (misma carpeta). Se comparan con `resultados_examen/fuentes/<empresa>/INDICE.tsv` de la rama `mistral/examen-fuentes`.

## Resultado por empresa

| Empresa | Documentos | Coinciden con la huella de Mistral | Observación |
|---|---|---|---|
| Vinci | 10 de Mistral + 4 informes anuales 2016–2019 añadidos por la persona | 10/10 | Los 4 añadidos son informes anuales oficiales (portada «2016/2017/2018/2019 ANNUAL REPORT», 348–396 pp.). Con ellos hay diez ejercicios. |
| Waste Management | 14 | 12/14 | Los 10-Q del T1 y T2 de 2026 de la Release **no tienen la huella de Mistral** (otra impresión: creada el 27-oct-2026, 57 y 65 pp., frente a 56 y 81). El contenido es el correcto: «Form 10-Q … Waste Management, Inc., Commission file number 1-12154», trimestres cerrados el 31-mar y el 30-jun-2026. Se usa la versión de la Release con su propia huella. |
| Zoetis | 13 de Mistral + 10-Q T2 y T3 añadidos por la persona | 12/13 | El comunicado HTML del T3 (segundo tiempo) difiere en 1,8 kB de la copia de Mistral (página dinámica); se usa la de la Release. 10-Q T2: «quarterly period ended June 30, 2026», creado el 6-ago-2026 → **primer tiempo** (≤ 9-oct). 10-Q T3: «September 30, 2026», creado el 5-nov-2026 → **segundo tiempo**. |
| Jumbo | 11 (Mistral no pudo descargar ninguno: Cloudflare) | sin huella de Mistral | Los 11 están y la portada de cada uno dice el periodo esperado: 2016/17, 2017/18, 2018/19 (julio–junio), transición 1-jul a 31-dic-2019, 2020, 2021, 2022, 2023, 2024, 2025 y semestral 1-ene a 30-jun-2026 (creado el 24-sep-2026). Las huellas de la Release son la referencia. |

Hay copias duplicadas con otro nombre (por ejemplo `51c9_jumboannualreport_31122025_en.pdf` = `jumbo-annual-report-fy2025.pdf`, `Zoetis-2025-Annual-Report.pdf` = `zoetis-10k-fy2025.pdf`): misma huella, sin efecto.

## Dos avisos

1. **Jumbo 2022 y 2023 solo están en formato XHTML** (el formato electrónico europeo ESEF, con el código LEI `549300TGIVUUMY40MZ05` en el nombre). Son documentos oficiales, pero **no tienen páginas**, y el pipeline cita por `[PDF PAGE n]`. Si existe el PDF de esos dos informes en la web de Jumbo, conviene subirlo. Si no existe, el coordinador hará una conversión a PDF registrada (original XHTML + huella del original + huella de la conversión) y las citas de esos dos años se referirán a la conversión.
2. **Zoetis, separación por fecha:** primer tiempo = 10-K 2016–2025 + 10-Q T1 y T2 de 2026; segundo tiempo = comunicado y presentación del T3 (5-nov-2026) + 10-Q T3. Nada publicado después del 9-oct-2026 entra en el primer tiempo.

## Conclusión

Las fuentes de las cuatro empresas están completas para montar sus expedientes. Las diferencias de huella (WM T1 y T2, comunicado HTML de Zoetis) son otra copia del mismo documento oficial, no otro documento; quedan registradas y se usa la huella de la Release.

## Anexo · conversión a PDF de Jumbo 2022 y 2023 (18-nov-2026, autorizada por la persona responsable)

- Herramienta: Chromium sin interfaz (Playwright), `page.pdf()` sobre el XHTML original sin modificar; tamaño carta.
- Originales: `jumbo-annual-report-fy2022.xhtml` (872dd6a2…) y `jumbo-annual-report-fy2023.xhtml` (f84c2313…).
- Conversiones: `jumbo-annual-report-fy2022.conversion.pdf` 132 pp. `94eba6aa2a52a9b50b2e4d97882148afb0882ec8515bdc458de0cb48f26c27d5`; `jumbo-annual-report-fy2023.conversion.pdf` 135 pp. `af3a7e063e083c336aed2f0973f5efa70f7939e5dddf61edd98f72decd1bd2de`.
- Comprobación: todas las cifras etiquetadas ESEF (`ix:nonFraction`) aparecen en el texto de la conversión: 269/269 (2022) y 271/271 (2023).
- Inspección visual del balance de 2023 (p. 66): tabla entera en una página; el número de página impreso por Jumbo (66) coincide con la página del PDF.
- Las citas de esos dos años se refieren a la conversión. Contraste adicional: cada año aparece como comparativo en el informe siguiente (2023 en el PDF oficial de 2024).
- Los PDF no van a Git; se conservan junto al resto de fuentes del coordinador.

## Anexo 2 · guía de Zoetis del T2 2026 (subida por la persona el 18-nov-2026, 21:46 UTC)

| Asset de la Release | SHA-256 | Frente a Mistral (`mistral/zoetis-guia-2t26`) |
|---|---|---|
| `Q2-2026-Zoetis-Earnings-Call.pdf` | `88a61cb5ee2daa492773287fe87fac6ff8341ae596099ff130523da98e0ae843` | idéntico |
| `Zoetis_2Q26_Financial_Results.pdf` (24 pp., creado el 5-ago-2026 20:07 UTC) | `130a148ebefba6244024f8f8967acdd4ee0fbabbd21a98640dc29cf93e03d571` | idéntico |
| `Zoetis.Inc.-.Zoetis.Announces.Second.Quarter.2026.Results.html` | `8ccb57bcc445a29facfa79cf22f415485dbe0af25a7fe88ed18fe75f8c2a39b1` | distinto de la copia de Mistral (`62061c66…`): página dinámica; el texto de la sección «FINANCIAL GUIDANCE» es idéntico (ingresos 9.120–9.320 mm USD, orgánico (3)%–(1)%, BPA ajustado 6,15–6,25; tipos de cambio a 21-jul-2026) |

Publicados el 6-ago-2026, antes del corte del primer tiempo (9-oct-2026). Se añaden a las fuentes del primer tiempo de Zoetis por decisión de la persona (18-nov-2026).

## Anexo 3 · datos de mercado subidos por la persona (19-nov-2026, 08:36 UTC)

| Asset | SHA-256 | Contenido | Uso |
|---|---|---|---|
| `bund_10y_WT1010.csv` (766892543) | `fef9498ea765b89547cebb222ab8720e91c84113c8caca74a676e21e5e571967` | Bundesbank, serie BBSSY.D.REN.EUR.A630.000000WT1010.A (rendimiento diario del Bund a 10 años), última actualización 18-nov-2026 | 13-nov 3,37 % (Ahold: el expediente tenía 3,34 % de Trading Economics → se corrige en ahold_f4); 17-nov 3,35 % (Jumbo: coincide); 9-oct 3,47 % (Vinci: la etapa 1 tenía 3,486 % de Investing → se corrige en el Vinci nuevo; el 10-oct no hay valor) |
| `us_treasury_par_yield_2026.csv` (766892834) | `0707733bdc20fce9a21a1063c5b99dbfd3456acabb216f73e6d6b798f511243d` | Tesoro de EE. UU., curva par diaria 2026 | 8-oct 5,22 % (Zoetis T1: coincide); 5-nov 4,84 % y 6-nov 4,86 % (Zoetis T2: coinciden con Mistral) |
| `damodaran_margin.xls` (766892761) | `25b04fce9740d9a471d50e176bf55aa6b7608cd0621b00072508a20e7c35ed7a` | Damodaran, márgenes por sector (enero 2026) | C7 de las cuatro empresas |
| `damodaran_indname.xls` (766892588) | `a1f4d70aa2cff728d846ca0b2fbdf7ea94030d2df6e140418920d3addb22c363` | Damodaran, clasificación de empresas por sector | contraste del sector |
| `jumbo.png` (766892797) | `cd1d1c30aee4e033e993736805da8069233e48ee61a51256157c46fecef7c7a1` | Captura de Euronext Athens, BELA: «Last Traded Price 27.4000 · Previous Close 27.4000», volumen 0 (antes de la apertura) | **No prueba el 27,28 € del 17-nov**: es el cierre del 18-nov (27,40 €), sin fecha visible. Falta la prueba del precio de Jumbo. |
| `FUENTES.txt` (766892781) | `c3e69e1c43a3f95228936e21d1496d77f85810c824768efdebaf5b296b96c892` | Lista de URL de la persona | — |

Faltan: el precio de Zoetis del 8-oct-2026 (solo está la URL) y el de Vinci del 9-oct-2026 (107,05 € de la etapa 1, sin fuente oficial).

### Anexo 3 bis (19-nov, ~08:50 UTC) · entregados en el chat por la persona
- `VINCI_historical_price.xls` (SHA-256 `78eee9c5d6b1e0402ab9bf8979a5f2d19c09acf3d861bca9e9427ebe305afb9d`): exportación de Euronext «Historical Data», FR0000125486, del 2024-11-20 al 2026-11-18. Fila «2026-10-09, 107.8, 108.1, 106.75, 107.05, 107.05 …» → **cierre de VINCI del 9-oct-2026 = 107,05 €, verificado** (coincide con la etapa 1). Copia local del coordinador en `/home/user/e_work/fuentes_examen/mercado_persona/` (no va a Git: XLS); debe conservarse en `fuentes_mercado/` del Vinci nuevo con su huella.
- Captura de investor.zoetis.com «Historical Stock Quote», fecha 2026-Oct-8: «Closing Price $73.08» → coincide con C37 de Zoetis T1. Llegó pegada en el chat, sin archivo: se pide a la persona que la suba a la Release como imagen para conservar sus bytes.

### Anexo 3 ter (19-nov, 08:55 UTC) · capturas subidas a la Release
- `Jumbo_BELA_2026-11-17_EuronextAthens.jpg` (asset 766946296, SHA-256 `c6f6a4b192248837f41c69e7132f28a9c5c29f663c92ae9d16ad41e946976693`): Euronext Athens «Historical Data», fila 11/17/2026: CLOSE 27.2800, OPEN 27.0000, HIGH 27.2800, LOW 26.7200, VOLUME 369,577 → **cierre de Jumbo del 17-nov-2026 = 27,28 €, verificado**.
- `Zoetis_ZTS_cierre_2026-10-08.jpg` (asset 766946313, SHA-256 `a51f50f11664105d1a6b79c7b72d4eedbf1afa867c36798dae50d1fb54e5ec82`): investor.zoetis.com con la fecha 2026-Oct-8 seleccionada pero **«Closing Price $85.57», apertura $82.15**: no corresponde al 8-oct (la captura pegada en el chat con la misma fecha daba $73.08, apertura $71.36, volumen 6.176.469). Parece que la tabla no se actualizó tras elegir la fecha. **No vale como prueba**; se pide otra.
- `Zoetis_ZTS_2026-10-08_v2.png` (asset 766963607): vuelve a mostrar $85.57 (sin actualizar tras elegir la fecha) → no vale.
- **Captura entregada en el chat (19-nov, ~09:10 UTC)**, conservada por el coordinador como `Zoetis_ZTS_2026-10-08_chat.png` (SHA-256 `c1871f7e80e1f46015912a0cc585292bc9186e2fad95db5d8ef98bbe632c1530`): investor.zoetis.com «Historical Stock Quote», 2026-Oct-8: Day's Open $71.36, Closing Price **$73.08**, Intraday Low $71.15, High $73.75, Volume 6,176,469 → **cierre de Zoetis del 8-oct-2026 = 73,08 USD, verificado**. Copia en `/home/user/e_work/fuentes_examen/mercado_persona/`; debe conservarse en `fuentes_mercado/` de zoetis_t1d con su huella.
- **Captura entregada en el chat (19-nov)**, conservada por el coordinador como `Zoetis_ZTS_2026-11-05_chat.png` (SHA-256 `994c5be31e5fc3b51ac2df60de59a306cce723e07ac2026a29eb0268af87d9bc`): investor.zoetis.com «Historical Stock Quote», 2026-Nov-5: Day's Open $84.87, Closing Price **$82.11**, Intraday Low $81.54, High $88.74, Volume 10,087,799 → **cierre de Zoetis del 5-nov-2026 = 82,11 USD, verificado** (Zoetis T2). Copia en `/home/user/e_work/fuentes_examen/mercado_persona/`; debe conservarse en `fuentes_mercado/` de zoetis_t2 con su huella.
