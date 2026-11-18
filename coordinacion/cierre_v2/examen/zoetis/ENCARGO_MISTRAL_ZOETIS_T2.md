# Encargo para Mistral · Zoetis, segundo tiempo (trimestre del 5-nov-2026)

**Para pegar en una ventana nueva de Mistral.** Fecha: 19-nov-2026. Encarga: el coordinador Claude. Revisa: un agente Claude distinto. Lee antes `AGENTS.md` del repositorio auxiliar y cumple sus reglas: no escribir en `jluisplagos/munger-v2`, no subir PDF a Git, no aprobar tu propio trabajo, **no valorar ni recomendar**.

## 1. Para qué sirve

El examen analiza Zoetis dos veces. El **primer tiempo** usa lo publicado hasta el 9-oct-2026 (ya tienes su registro de entradas en `mistral/examen-zoetis-entradas`). El **segundo tiempo** es el mismo expediente **más** lo publicado el **5-nov-2026**: el 10-Q del tercer trimestre de 2026 y el comunicado y la presentación de resultados del T3. Necesito las cifras nuevas, literales y con página, para actualizar los doce últimos meses (TTM) y la guía.

## 2. Fuentes (Release `fuentes-examen-20261118` del auxiliar)

- `zoetis-10q-2026-q3.pdf` (10-Q, trimestre cerrado el 30-sep-2026);
- `zoetis-3q2026-press-release.html` (comunicado) y `zoetis-3q2026-financial-results.pdf` (presentación).

Las huellas de los tres están en `coordinacion/cierre_v2/examen/RELEASE_FUENTES_EXAMEN_SHA256SUMS` (rama `coordinacion/cierre-v2`).

Descarga con `gh release download` y comprueba el SHA-256 de cada archivo contra ese fichero. Si la huella no coincide, dilo y no sigas con ese archivo.

## 3. Qué extraer

**A. Del 10-Q T3** (columnas «nueve meses terminados el 30-sep-2026» **y** «… 2025», y el balance al 30-sep-2026), las mismas partidas que en el registro del primer tiempo: ventas, beneficio operativo (si se imprime), amortizaciones (D&A), beneficio neto atribuible, impuestos, beneficio antes de impuestos, flujo de caja de las operaciones (CFO), capex, adquisiciones, intereses pagados (si se publican en la nota de flujos), pagos de principal de arrendamientos financieros, compensación en acciones (SBC), I+D, acciones diluidas medias (trimestre y nueve meses), acciones en circulación en la fecha más reciente que dé la portada, patrimonio, deuda financiera (corto y largo plazo, por separado), pasivos por arrendamiento (operativo y financiero, por separado), caja y equivalentes, otras inversiones financieras, pensiones, minoritarios, recompras y dividendos pagados en los nueve meses.

**B. Del comunicado y la presentación del T3:** la **guía de 2026 actualizada** (ingresos, crecimiento orgánico operativo, BPA ajustado y lo que digan del tipo de cambio), **comparada línea a línea** con la guía del 6-ago-2026 (ingresos 9.120–9.320 mm USD, orgánico (3)%–(1)%, BPA ajustado 6,15–6,25). Si la guía cambia, cita las dos frases literales. Anota también cualquier cambio que la empresa declare sobre recompras, dividendo, deuda o reestructuración, solo como cita literal y sin opinar.

**C. Mercado:** precio de cierre de ZTS en NYSE del **5-nov-2026** y del **6-nov-2026**, y Treasury a 10 años de esos dos días (CSV oficial «Daily Treasury Par Yield Curve Rates» de home.treasury.gov). Guárdalos como texto con SHA-256 en `fuentes_mercado/`, igual que hiciste en el primer tiempo (la página de la empresa sirve si nyse.com bloquea el acceso). Si no puedes, dilo.

Reglas de siempre: cifra **tal como está impresa** (número, signo y unidad); página del PDF (la del visor); cita literal corta; **cero con evidencia** o `no_encontrado`, nunca un cero sin prueba. Si una línea del 10-Q mezcla arrendamientos operativos y financieros, sepáralos con la nota de arrendamientos y dilo.

## 4. Qué entregas

Rama nueva **`mistral/examen-zoetis-t2`**, carpeta `resultados_examen/zoetis_t2/`:

1. `CIFRAS_T3.csv`: `partida, periodo_exacto, valor_impreso, unidad, signo_en_el_documento, archivo, sha256_archivo, pagina_pdf, cita_literal, estado (encontrado | cero_con_evidencia | no_encontrado), nota`.
2. `GUIA_2026.md`: guía del 6-ago frente a la del 5-nov, con citas y páginas.
3. `fuentes_mercado/` con `HUELLAS.txt` y `DESCARGAS.tsv`.
4. `ENTREGA.md` (máximo una página): qué hiciste, lo que no encontraste y por qué, dudas, y el modelo y las herramientas que usaste de verdad.

Haz commit y push al terminar cada bloque (A, B, C).

---

### Frase para pegar en la ventana nueva

> Lee `coordinacion/cierre_v2/examen/zoetis/ENCARGO_MISTRAL_ZOETIS_T2.md` en la rama `coordinacion/cierre-v2` del repositorio `jluisplagos/munger-v2-evidencias-mistral` y hazlo entero. Entrega en la rama `mistral/examen-zoetis-t2`.
