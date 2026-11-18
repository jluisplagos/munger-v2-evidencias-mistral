# Entrega M5 · Inventario bloque 3 (39 empresas) · rama `mistral/m5-inventario-b3`

Fecha: 18-nov-2026. Encargo: `coordinacion/cierre_v2/universo_etapa1/ENCARGO_MISTRAL_M5_INVENTARIO.md` (bloque 3). Entrega en `resultados_universo/inventario/INVENTARIO_b3.tsv` (39 filas + cabecera) y este `ENTREGA_b3.md`. Commit y push tras cada 10 empresas (4 commits en la rama).

## Modelo y herramientas usados de verdad
- Modelo: `mistral-large-4-0` (Mistral), en esta sesión de Vibe Code.
- Herramientas: lectura de los XLSX de etapa 1 solo en lectura con `openpyxl` (sin macros ni LibreOffice), desde la Release `universo-etapa1-20261118` (asset `universo_etapa1.zip.zip`, SHA-256 `4d30f7352948fe7e7fe3b133386eabedbddcc71d997e972a1c6db7964d58b0a9`); búsqueda web (Brave) y lectura de páginas oficiales de inversores de cada empresa para los datos de web, con URL oficial en la columna `fuentes`. No se usó SEC EDGAR (sin datos de contacto autorizados), salvo referencias cruzadas en resultados de búsqueda.

## Qué no encontré y por qué
- **ISIN no verificado en fuente oficial para algunas empresas**: los ISIN se tomaron de las páginas oficiales de acción/IR listadas en `fuentes` cuando aparecían en ellas (p. ej. BAM, Salzgitter, Strabag, Euronext Live). Para las que no mostraron el ISIN en el fragmento cargado (Quanta, Rentokil, Rovi, SQM, Spectra, TE Connectivity, Valeura, Volution, Vitec, Upsales, WEG, Tupras, Sony, WM, Zoetis, Sulzer, Sweco, Technogym, Vossloh) se consignó el ISIN estándar de la línea cotizada principal; si el coordinador lo considera insuficiente, se marca como pendiente de verificación contra el registro oficial (CNMV/BME, Companies House, SIX, etc.).
- **SQM**: ISIN de la línea chilena (Bolsa de Santiago) no confirmado en fuente oficial; se consigna el ISIN del ADR NYSE (US8336341083) y los tickers locales SQM-A/SQM-B.
- **Informes anuales en inglés 2016–2025**: el recuento se basa en el archivo de informes de la web oficial de cada empresa. Para **Puig** solo hay 2 (2024–2025; salió a bolsa en mayo-2024). Para **Upsales** hay 5 (desde su salida a bolsa en 2021) y el informe anual 2025 se publicó primero en sueco (la web IR está en inglés). Para **Quanta** la página oficial lista 8 informes anuales (2018–2025); los 10-K en inglés cubren más años pero no son «informes anuales» como tal. Para el resto se contó 10 cuando el archivo oficial en inglés abarca 2016–2025.
- **Upsales**: el informe anual 2025 tuvo un retraso administrativo (publicado el 21/04/2026, según su comunicado oficial).
- **Tupras**: la moneda de los estados es TRY con IAS 29 (hiperinflación); la hoja de etapa 1 ya flags la provisionalidad de la moneda del DCF (TRY IAS 29 vs USD), que se conserva en `moneda_precio`.
- **Datos de etapa 1**: `fecha_etapa1` = celda D4 de «Análisis»; `precio_etapa1`/`moneda_precio` y `veredicto_etapa1` de la hoja y la respuesta. Incidencias: 11 empresas del bloque tienen `_cambios_v2.md` (Quanta, Rational, Rheinmetall, Salzgitter, Schneider, Sika, TE_Connectivity, Thales, Vidrala, Vinci, Viscofan, Zoetis); no hubo archivos que no abran ni datos contradictorios ni deslistados.

## Notas
- Este documento es un inventario, no un juicio: no valora ni recomienda.
- Los XLSX no se suben a Git (regla del repositorio); se leyeron desde la Release.
