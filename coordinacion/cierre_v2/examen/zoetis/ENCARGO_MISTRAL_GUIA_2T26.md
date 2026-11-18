# Encargo corto para Mistral · Zoetis: ¿la guía de 2026 se publicó antes del 9-oct-2026?

**Para pegar en una ventana nueva de Mistral.** Fecha: 18-nov-2026. Lee antes `AGENTS.md`.

## Por qué
La etapa 1 de Zoetis de la persona responsable habla de un «recorte de guía de agosto de 2026» y de una «guía orgánica 2026 negativa». Ningún documento del expediente la contiene (los 10-Q no traen guía). Si la guía oficial se publicó el **6-ago-2026** (resultados del T2) o en cualquier fecha **anterior al 9-oct-2026**, es información legítima del primer tiempo del examen; si se publicó después, no.

## Qué hacer
1. Busca en la **web de inversores de Zoetis** (no en terceros) los comunicados de resultados y presentaciones publicados entre el **1-jul y el 9-oct-2026**, en especial el comunicado de resultados del **segundo trimestre de 2026** y su presentación.
2. Descárgalos tal cual (PDF o HTML), con URL, fecha de publicación que muestre la web, fecha de descarga, bytes y SHA-256.
3. Transcribe **literalmente** la guía para 2026 que contengan (ingresos, crecimiento orgánico/operativo, BPA ajustado), con página o sección.
4. Di también si encuentras alguna actualización de guía entre el 9-oct y el 5-nov-2026 (solo para saberlo; no forma parte del primer tiempo).

## Qué entregas
Rama nueva **`mistral/zoetis-guia-2t26`**, carpeta `resultados_examen/zoetis_guia/`: `INDICE.tsv` (archivo, título, fecha_publicacion, url, fecha_descarga_utc, bytes, sha256), `GUIA_LITERAL.md` (citas literales con su documento y página) y `ENTREGA.md` (máximo media página). Los PDF/HTML no van a Git: guárdalos en local y, si tu herramienta no puede subirlos a una Release, dilo. Commit y push.

### Frase para pegar
> Lee `coordinacion/cierre_v2/examen/zoetis/ENCARGO_MISTRAL_GUIA_2T26.md` en la rama `coordinacion/cierre-v2` del repositorio `jluisplagos/munger-v2-evidencias-mistral` y hazlo entero. Entrega en la rama `mistral/zoetis-guia-2t26`.
