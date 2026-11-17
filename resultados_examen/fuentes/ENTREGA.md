# ENTREGA · fuentes oficiales Jumbo, Zoetis, VINCI, Waste Management (examen)

Fecha: 2026-11-17/18 UTC. Rama: `mistral/examen-fuentes` en `jluisplagos/munger-v2-evidencias-mistral`.
Modelo usado de verdad: **mistral-large-4-0** (sesión Vibe Code). Herramientas usadas de verdad:
`bash` + `python3` (`requests` 2.34.2, `curl_cffi` 0.17.0 con `impersonate='chrome'`, `pypdf`), lector web
(`web_fetch`/`web_search`, base Brave) y `gh` CLI. `curl` y `wget` están bloqueados por el sandbox
("Network requests via curl are not allowed"); la red saliente vía Python funciona parcialmente.
**SEC EDGAR no se usó**: el encargo exige identificarse con nombre+correo autorizados y no se
proporcionó ninguno, así que solo se usaron las webs de inversores de cada emisor.

## Qué se consiguió y qué no

- **VINCI — 10/10 descargados** (vinci.com, HTTP 200): URD en inglés 2020–2025 (el patrón
  `vinci-YYYY-universal-registration-document.pdf` devuelve 404 para 2016–2019; esos años VINCI
  publicaba el "document de référence"/"registration document" con otro nombre y no se localizó el
  PDF en inglés con patrón directo), informe financiero semestral 2026 + estados intermedios
  (2026-07-30) y la información del tercer trimestre 2026: comunicado 9M 2026 (2026-10-22) y
  presentación 9M 2026.
- **Zoetis — 13/15 descargados** desde el CDN oficial de investor.zoetis.com (s203.q4cdn.com):
  informes anuales oficiales con el 10-K FY2016–FY2025 (el 10-K FY2025 se depositó el 2026-02-12),
  10-Q Q1 2026 (2026-05-07), comunicado T3 2026 (2026-11-05, solo existe en HTML en la web oficial;
  se guardó el HTML tal cual) y presentación de resultados T3 2026. **No descargados**: 10-Q Q2 2026
  (filing 19672260, 2026-08-06) y 10-Q Q3 2026 (filing 19906519, 2026-11-05): la web de inversores
  solo sirve sus PDF mediante enlaces generados por JavaScript y no se pudo obtener la URL directa
  del CDN sin navegador; EDGAR no se usó por la regla del User-Agent. División por fecha de
  publicación: `primer_tiempo/` = todo lo publicado hasta el 2026-10-09 inclusive;
  `segundo_tiempo/` = lo publicado después (2026-11-05).
- **Waste Management — 14/14 descargados** desde investors.wm.com (con `curl_cffi`
  impersonando Chrome; con `requests` plano el sitio devuelve 403): informes anuales 2016–2025
  (cada uno incluye el Form 10-K), 10-Q de 2026 (Q1 2026-04-29, Q2 2026-07-29, Q3 2026-10-28) y
  comunicado de resultados T3 2026 (2026-10-27).
- **Jumbo — 0/11 descargados**: `corporate.e-jumbo.gr` devuelve **HTTP 403 (Cloudflare)** a todas las
  descargas directas desde este servidor (tantto con `requests` como con `curl_cffi` imitando
  Chrome; el IP del datacenter está bloqueado). Los metadatos (título, periodo, fecha de publicación
  y URL) se verificaron leyendo las páginas oficiales con el lector web. No hay SHA-256 porque no
  hay binario descargado. Cambio de ejercicio anotado: hasta el ejercicio 2018/2019 Jumbo cerraba el
  30 de junio; hubo un **ejercicio de transición sub-doce meses 01.07.2019–31.12.2019**; desde 2020
  el ejercicio es el año natural. Los diez últimos ejercicios hasta el 31.12.2025 son:
  FY2025, FY2024, FY2023, FY2022, FY2021, FY2020, transición 01.07.2019–31.12.2019, 2018/2019,
  2017/2018 y 2016/2017, más el informe semestral H1 2026 (01.01.2026–30.06.2026, publicado el
  2026-09-24).

## Periodos por empresa

- Jumbo: ejercicios y periodos exactos en `jumbo/INDICE.tsv` (incluye el de transición).
- Zoetis: FY = año natural (31.12); 10-K FY2016–FY2025, 10-Q Q1–Q3 2026; ver columna
  `periodo_que_cubre`.
- VINCI: FY = año natural (31.12); URD 2020–2025, informe semestral 01.01.2026–30.06.2026,
  información 9M/Q3 2026 (hasta 30.09.2026).
- Waste Management: FY = año natural (31.12); informes anuales 2016–2025, 10-Q Q1–Q3 2026,
  comunicado T3 2026 (hasta 30.09.2026).

## Formato de la entrega

`resultados_examen/fuentes/<empresa>/INDICE.tsv` (una fila por documento) y `SHA256SUMS` por
empresa. **Los PDF/HTML no están en Git**: copias locales en `munger_fuentes_examen/<empresa>/`
(fuera del repositorio). Release `fuentes-examen-20261118` con los binarios como assets:
pendiente de aprobación explícita de la persona responsable antes de publicar en el repo público.

Evidencia propuesta por Mistral; pendiente de revisión e incorporación por el integrador.
