# U2 · tercer caso B fuera de muestra · recursos, fuentes públicas y propuesta · BORRADOR para revisión

- **Autoría:** un subagente del coordinador, el 17-nov-2026, por encargo de la persona responsable (U2). Antes de aceptarlo hace falta la revisión de un contexto distinto.
- **Comprobado por el coordinador:**
  - el único recurso de Ahold que existe es `…_4_14/documentacion_cierre_4_14/descargas_bat/descargar_fuentes_ahold.bat`, con SHA-256 `04feebd4…d53d88`, la misma que en el manifiesto 4.14;
  - el `.bat` dice: «La carpeta tiene los informes 2019-2025»;
  - los 10 informes anuales descargados pasan `sha256sum -c SHA256SUMS_pdf.txt` (10/10).
- **Fuentes públicas recopiladas:** los informes anuales oficiales 2016–2025 de Ahold Delhaize. Están en un sandbox efímero, fuera de Git. Este directorio guarda solo el índice (`INDICE_FUENTES.csv` y `descargas.tsv`) y las huellas.
  - El folleto de reexpresión NIIF 16 de 2018 da 404 en su URL. Lo cubre la nota 36 del informe 2019 (PDF pp. 188–192).
  - **No hay preservación duradera** mientras no se decida dónde guardarlos.
- **Propuesta (`PROPUESTA_TERCER_B.md`):**
  - Ahold Delhaize, con la etapa 1 de la persona responsable;
  - si no, otra empresa de las 116 que designe ella;
  - si no, una reducción de alcance, que exige su decisión.

  No se decide el motor: lo hace la fase A. Si sale A, el caso puede terminar en el límite del modelo, y ese resultado se conserva.
- **Corrige al paquete de Mistral C/F @ `52fb120`:** el `.bat` sí está conservado.
- **Rutas:** las locales se sustituyen por `<scratchpad>`, `<e_work>` y `<home>`.
