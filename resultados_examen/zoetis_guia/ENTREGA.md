# ENTREGA · ¿la guía de 2026 de Zoetis se publicó antes del 9-oct-2026?

Fecha: 2026-11-18 UTC. Rama: `mistral/zoetis-guia-2t26` en `jluisplagos/munger-v2-evidencias-mistral`.
Encargo: `coordinacion/cierre_v2/examen/zoetis/ENCARGO_MISTRAL_GUIA_2T26.md` (rama `coordinacion/cierre-v2`).
Modelo usado de verdad: **mistral-large-4-0** (sesión Vibe Code). Herramientas usadas de verdad: `bash` +
`python3` (`requests` 2.34.2; `pypdf` 7.1.1 instalado con `pip` en esta sesión; `curl`/`wget` bloqueados por
el sandbox), lector y buscador web (`web_fetch`/`web_search`, base Brave) y `gh` CLI. Solo se usó la web oficial
de inversores de Zoetis (investor.zoetis.com y su CDN s203.q4cdn.com); no terceros ni SEC EDGAR.

## Respuesta

**Sí: la guía oficial FY2026 de Zoetis se publicó el 2026-08-06**, con el comunicado de resultados del T2 2026,
su presentación y el evento (08:30 AM ET) — antes del 9-oct-2026, así que es información legítima del primer
tiempo. La «guía orgánica 2026 negativa» es el crecimiento orgánico operacional de ingresos de **(3)% a (1)%**
(revenue $9.120–$9.320B; adjusted diluted EPS $6.15–$6.25; FX a 21-jul-2026). Entre el 9-oct y el 5-nov-2026 hubo
una actualización: el comunicado del T3 2026 (**2026-11-05**) estrecha ingresos a $9.220–$9.320B (orgánico
(2)%–(1)%) y sube BPA ajustado a $6.25–$6.35 (FX a 20-oct-2026). Citas literales con documento y página/sección
en `GUIA_LITERAL.md`.

## Descargas

7 documentos oficiales, todos HTTP 200, descargados el 2026-11-18 (21:31:06Z–21:31:07Z UTC), con URL, fecha de
publicación que muestra la web, bytes y SHA-256 en `INDICE.tsv`. La ventana 01-jul..09-oct-2026 se enumeró con el
sitemap oficial (Sitemap.ashx) y la web IR: el **único** comunicado de resultados en esa ventana es el del T2 2026
(06-ago-2026); el resto de noticias 2026 de la ventana (dividendos, aprobaciones FDA/EMA, M&A, nombramientos,
conferencias) no contienen guía.

## Lo que no se encontró / límites

- La página «Zoetis Investor Overview October» (presentation-details/2026; lastmod 2026-10-27 en el sitemap)
  devuelve **404** al consultarla y su PDF no se localiza en el CDN: no se pudo comprobar si repetía la guía.
- No hay ningún otro comunicado con guía entre el 9-oct-2026 y el 5-nov-2026 aparte del T3 (05-nov-2026).

## Binarios (no van a Git)

Los PDF/HTML descargados están en local, fuera del repositorio: `/workspace/zoetis_guia_local/`
(junto con `HUELLAS.txt` y `descarga_meta.json`). **Esta herramienta no puede subirlos a una Release**
(`gh release create` está bloqueado: "Creating GitHub releases is not allowed"); la persona responsable deberá
subirlos desde esa carpeta usando los nombres y SHA-256 de `INDICE.tsv`.
