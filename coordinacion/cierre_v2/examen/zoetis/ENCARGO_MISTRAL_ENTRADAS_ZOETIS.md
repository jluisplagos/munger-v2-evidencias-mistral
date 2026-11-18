# Encargo para Mistral · Registro de entradas de Zoetis Inc., primer tiempo (examen del personaje)

**Para pegar en una ventana nueva de Mistral.** Fecha: 18-nov-2026. Encarga: el coordinador Claude. Revisa y sella: un agente Claude distinto. **Tú no sellas ni marcas nada como «verificado».**

Es el mismo trabajo que hiciste con Ahold. **Lee primero el encargo de Ahold** (`coordinacion/cierre_v2/examen/ahold/ENCARGO_MISTRAL_ENTRADAS_AHOLD.md`, rama `coordinacion/cierre-v2`) y su corrección (`…/ahold/CORRECCION_MISTRAL_ENTRADAS_AHOLD_R1.md`): reglas, clases, formato y aceptación **idénticos**. Aquí solo cambia lo que sigue.

## 1. Dónde está todo (Zoetis)
- **Expediente (solo lectura):** repo `jluisplagos/munger-v2`, rama **`examen/ahold-f1`**, carpeta `munger_v2_r1/personaje_v2/empresas_v2_correcciones/2026-11_examen_universo/zoetis_t1b/Zoetis/`: `texto/` (10-K 2016–2025 y 10-Q del T1 y T2 de 2026), `fase1_partes/AR_AAAA.json`, `fase1_v63.json`, `fase1_metadatos.json`, y la configuración del cambio `../../configuracion/cambio_zoetis_t1.json` (C46, C47, C49 y C50 con cálculo declarado: regístralos como `derivado`).
- **Textos de 2020–2024:** salen de OCR (tesseract; ver `../../zoetis_t1/ocr_400dpi/LEEME.md`). Tú hiciste una segunda lectura OCR verificada contra la imagen (rama `mistral/zoetis-texto-ocr`): **úsala para comprobar** cada cifra de esos años; pero la `cita` y la `pagina` del registro tienen que ser las del archivo de `texto/` del expediente. Si el texto del expediente tiene una cifra mal leída que tu lectura corrige, regístrala con `incidencia` explicándolo, sin forzar la cita.
- **PDF oficiales:** Release `fuentes-examen-20261118` (huellas en `coordinacion/cierre_v2/examen/RELEASE_FUENTES_EXAMEN_SHA256SUMS`).
- **Plantilla:** `coordinacion/cierre_v2/examen/zoetis/verificacion_entradas.plantilla.json` (**315 entradas**). Lista: `zoetis/LISTA_ENTRADAS.csv`.

## 2. Alcance
Las **285 entradas** con `en_este_encargo` = «sí». Las 30 hipótesis las escriben las fases del personaje: no las toques.

## 3. Lo que tienes que vigilar especialmente en Zoetis
- **Corte del primer tiempo:** solo documentos publicados **hasta el 9-oct-2026** (los del expediente ya lo cumplen). Nada del T3 de 2026.
- **US GAAP:** los arrendamientos operativos no tienen principal en financiación; los financieros (≈ 1 mm/año) van en deuda o en C49 según la configuración del cambio.
- **Notación de EE. UU.:** «470.385» son 470,385 millones de acciones. La partida de acciones declara «miles» por una limitación del programa (nota en cada `AR_AAAA.json`): registra la cifra impresa y su escala reales en tu entrada.
- **Precio (C37) y capitalización (C41):** 73,08 USD, cierre NYSE del 8-oct-2026. Guarda tú el histórico oficial de esa sesión (página de la bolsa o de la empresa) como texto con SHA-256 en `fuentes_mercado/`; si no puedes, dilo.
- **Tasa sin riesgo:** Treasury a 10 años del 8-oct-2026, de fuente oficial (U.S. Department of the Treasury, «Daily Treasury Par Yield Curve Rates»). Hoy figura 5,22 % de un resultado de búsqueda, **sin verificar**: verifícalo o dilo.

## 4. Qué entregas
Rama nueva **`mistral/examen-zoetis-entradas`**, carpeta `resultados_examen/zoetis/`: `verificacion_entradas.json` (315 entradas), `fuentes_mercado/` con `HUELLAS.txt`, `DESCARGAS.tsv` y `ENTREGA.md` (máximo una página). Commit y push al terminar cada bloque grande.

---

### Frase para pegar en la ventana nueva
> Lee `coordinacion/cierre_v2/examen/zoetis/ENCARGO_MISTRAL_ENTRADAS_ZOETIS.md` en la rama `coordinacion/cierre-v2` del repositorio `jluisplagos/munger-v2-evidencias-mistral` y hazlo entero. Entrega en la rama `mistral/examen-zoetis-entradas`.
