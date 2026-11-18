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
