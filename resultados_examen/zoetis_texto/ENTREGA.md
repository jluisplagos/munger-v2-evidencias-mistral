# Entrega · Texto por página de los 10-K de Zoetis FY2020–FY2024

Rama: `mistral/zoetis-texto-ocr` · Carpeta: `resultados_examen/zoetis_texto/` · Fecha: 18-nov-2026.

## Fuentes y verificación

- Descargados de la Release `fuentes-examen-20261118` (`jluisplagos/munger-v2-evidencias-mistral`): `zoetis-10k-fy2020.pdf` … `zoetis-10k-fy2024.pdf`.
- SHA-256 de los 5 PDF coinciden exactamente con `coordinacion/cierre_v2/examen/RELEASE_FUENTES_EXAMEN_SHA256SUMS` (verificado con `sha256sum`).
- Ninguno de los 5 PDF tiene tabla ToUnicode (comprobado sobre el binario: 0 entradas `/ToUnicode`), por lo que todas las páginas se trataron como `ocr` en `PAGINAS.tsv`.

## Herramienta y modelo usados de verdad

- OCR: **Mistral OCR, modelo `mistral-ocr-latest`**, invocado con la herramienta de OCR de documentos de esta sesión sobre cada PDF completo (el `manifest.json` de cada trabajo lo registra). No se usó tesseract ni ningún otro motor.
- Verificación manual cifra a cifra: páginas renderizadas a PNG a 200 dpi con **PyMuPDF 1.26.x (módulo `pymupdf`, `fitz` 2.1)** y revisadas visualmente con la herramienta de análisis de imágenes. Verificadas a ojo: los estados de resultados de los 5 años, la página 2 (highlights) de fy2021 y fy2024, y el balance y el flujo de efectivo de fy2024; además comprobación aritmética interna (sumas de columnas) de los estados de resultados y de flujos de efectivo de los 5 años: 0 inconsistencias.
- Modelo de razonamiento de esta sesión (elaboración de este documento): `mistral-large-4-0`.

## Contenido

- `zoetis-10k-fy2020.txt` … `zoetis-10k-fy2024.txt`: UTF-8, una marca exacta `[PDF PAGE n]` por página. Número de marcas = número de páginas del PDF: 120, 116, 112, 112 y 108 respectivamente (comprobado con `grep -c`).
- `PAGINAS.tsv`: 568 filas (una por página), columnas `archivo, pagina, metodo, confianza`. Método `ocr` en todas. Confianza: `alta` en 551 páginas, `media` en las 5 páginas 2 (highlights con gráficos), `baja` en 12 páginas de portada/contraportada o en blanco.
- `DUDAS.tsv`: 12 dudas declaradas. En las páginas de estados financieros consolidados no hay ninguna duda pendiente: las cifras se verificaron contra la imagen y cuadran aritméticamente. Las dudas son valores leídos solo dentro de imágenes de gráficos de la página 2 de fy2022/fy2023 (el OCR de página no transcribió sus etiquetas) y rótulos dudosos.

## Páginas con problemas

- Portadas y contraportadas (solo imagen, sin texto): fy2020 p. 1 y 120; fy2021 p. 116; fy2022 p. 108, 109, 110 y 112; fy2023 p. 108, 109, 110 y 112; fy2024 p. 108. En fy2022/fy2023 las p. 108–110 dicen «(This page has been left blank intentionally.)».
- Página 2 de fy2022 y fy2023: los cinco gráficos (especie, categoría, mercados, concentración, crecimiento/margen) quedaron como `[Extracted image: …]` sin valores en el texto; los valores se leyeron a mano de las imágenes y se declaran en `DUDAS.tsv`.
- fy2020 p. 1: el logo se leyó «zgetis» (debe ser «zoetis»; no es cifra).
- fy2022 p. 2 y fy2023 p. 2: la etiqueta «Companion Animal» se leyó como «Comparison Animal» en el texto de página.
- fy2024 p. 2: la tabla resumen quedó en disposición vertical (una cifra por línea); los valores se verificaron contra la imagen y son correctos.

## Nota sobre layout

Las tablas se conservan en Markdown (filas `| … |`) tal como las devuelve el OCR; las columnas quedan separadas por espacios dentro de las celdas. No se ha corregido ni completado ninguna cifra: todo lo transcrito es lo leído por el OCR o, en su caso, lo anotado como duda en `DUDAS.tsv`.
