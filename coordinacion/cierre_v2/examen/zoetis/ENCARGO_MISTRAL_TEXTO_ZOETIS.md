# Encargo para Mistral · Texto por página de cinco 10-K de Zoetis (2020–2024)

**Para pegar en una ventana nueva de Mistral.** Fecha: 18-nov-2026. Encarga: el coordinador Claude. Lee antes `AGENTS.md` del repositorio auxiliar y cumple sus reglas (no escribir en `jluisplagos/munger-v2`, no subir PDF a Git, no aprobar tu propio trabajo, no valorar).

## Por qué
Los 10-K de Zoetis de 2020, 2021, 2022, 2023 y 2024 de la Release `fuentes-examen-20261118` tienen fuentes sin tabla ToUnicode: su texto no se puede copiar. El coordinador los ha pasado por un OCR (tesseract) y ha encontrado errores de dígitos (por ejemplo «1,716» donde dice 7,776). Necesitamos **una segunda lectura independiente** para comparar página a página y cifra a cifra. Tú ya leíste estos PDF con tu herramienta de OCR para la ventana 2 de M4.

## Qué hacer
1. Descarga `zoetis-10k-fy2020.pdf` … `zoetis-10k-fy2024.pdf` de la Release (`gh release download fuentes-examen-20261118 -R jluisplagos/munger-v2-evidencias-mistral -p 'zoetis-10k-fy202[0-4].pdf'`) y comprueba su SHA-256 contra `coordinacion/cierre_v2/examen/RELEASE_FUENTES_EXAMEN_SHA256SUMS`.
2. Para cada PDF, produce un archivo de texto con **todas las páginas**, cada una precedida de la marca exacta `[PDF PAGE n]` (n = número de página del PDF, empezando en 1, una marca por página, aunque la página esté vacía). Conserva la disposición de las tablas lo mejor que puedas (columnas separadas por espacios), **sin corregir ni completar cifras**: transcribe lo que ves.
3. **Prioridad:** las páginas de los estados financieros consolidados (cuenta de resultados, balance, flujos de efectivo, cambios en el patrimonio) y de las notas de deuda, arrendamientos (leases), impuestos, beneficio por acción, pagos basados en acciones y segmentos/geografía. Comprueba a mano, mirando la imagen de la página, cada cifra de esas tablas.
4. Lista en `DUDAS.tsv` cada cifra que no lees con seguridad: `archivo, pagina, fila (rótulo), columna (año), lo_que_lees, alternativa`.

## Qué entregas
Rama nueva **`mistral/zoetis-texto-ocr`**, carpeta `resultados_examen/zoetis_texto/`:
- `zoetis-10k-fy2020.txt` … `zoetis-10k-fy2024.txt` (UTF-8, marcas `[PDF PAGE n]`);
- `PAGINAS.tsv`: `archivo, pagina, metodo (ocr | texto), confianza (alta|media|baja)`;
- `DUDAS.tsv`;
- `ENTREGA.md` (máximo una página): herramienta y modelo usados de verdad, páginas con problemas.
Commit y push al terminar cada archivo.

## Cómo se acepta
El coordinador comparará tu texto con su OCR: número de marcas = número de páginas; en las páginas de estados financieros, cada discrepancia de cifra se resolverá mirando la imagen del PDF. Prefiero una duda declarada a una cifra adivinada.
