# Encargo para Mistral · Registro de entradas de Jumbo S.A. (examen del personaje)

**Para pegar en una ventana nueva de Mistral.** Fecha: 18-nov-2026. Encarga: el coordinador Claude. Revisa: un agente Claude distinto, que es quien sella. **Tú no sellas ni marcas nada como «verificado».**

Es el mismo trabajo que hiciste con Ahold. **Lee primero el encargo de Ahold** (`coordinacion/cierre_v2/examen/ahold/ENCARGO_MISTRAL_ENTRADAS_AHOLD.md`, rama `coordinacion/cierre-v2`) y su corrección (`…/ahold/CORRECCION_MISTRAL_ENTRADAS_AHOLD_R1.md`): las reglas, las clases, el formato y la forma de aceptación son **idénticos**. Aquí solo cambia lo que sigue.

## 1. Dónde está todo (Jumbo)

- **Expediente (solo lectura):** repo `jluisplagos/munger-v2`, rama **`examen/ahold-f1`**, carpeta `munger_v2_r1/personaje_v2/empresas_v2_correcciones/2026-11_examen_universo/jumbo_c/Jumbo/`:
  - `texto/*.txt`: los diez informes anuales (2016/17 … 2025) y el semestral H1 2026, con marcas `[PDF PAGE n]`;
  - `fase1_partes/AR_AAAA.json`: lo que extrajeron los extractores, con `impreso`, `pagina` y `linea` literal (tu mejor punto de partida). **Atención:** en este expediente, 33 componentes de 2020–2025 se corrigieron porque el propio emisor cruzó las etiquetas «Lease repayments» (es el interés) e «Interest paid for leases» (es el principal) en el estado de flujos. Los originales están en `antecedentes/fase1_partes_original/` y el rastro en `resultados/cambio_de_base.json`. Registra la cifra **como está impresa**, y explica el cruce de etiquetas en `tratamiento` con la página de la nota de costes financieros que lo prueba;
  - `fase1_v63.json`, `fase1_metadatos.json`, `historia_revision.md`, y la configuración del cambio en `../../configuracion/cambio_jumbo_c.json` (cálculos declarados de C46, C48 y C49 según las decisiones de la persona responsable J1–J3; léela para registrar esos tres como `derivado`).
- **PDF oficiales:** Release `fuentes-examen-20261118` del auxiliar (`gh release download`), con huellas en `coordinacion/cierre_v2/examen/RELEASE_FUENTES_EXAMEN_SHA256SUMS`. **2022 y 2023** son conversiones registradas de los XHTML oficiales (huellas y método en `RELEASE_FUENTES_EXAMEN_VERIFICACION.md`, anexo): para esos dos años, `version` = el XHTML original y su SHA-256, y anota en `tratamiento` que la página es la de la conversión.
- **Plantilla del registro:** `coordinacion/cierre_v2/examen/jumbo/verificacion_entradas.plantilla.json` (**313 entradas**; `valor_modelo` es el valor del libro). Lista resumida: `jumbo/LISTA_ENTRADAS.csv`.

## 2. Alcance

Las **283 entradas** con `en_este_encargo` = «sí». Las 30 hipótesis las escriben las fases del personaje: no las toques.

## 3. Lo que tienes que vigilar especialmente en Jumbo

- **Cambio de ejercicio:** «2016» = 1-jul-2016 a 30-jun-2017, «2017» = 2017/18, «2018» = 2018/19; **«2019» = transición de seis meses (1-jul a 31-dic-2019)**, no comparable (decisión J-T); desde 2020, año natural. El `periodo` lleva las fechas exactas.
- **Unidades:** los estados de Jumbo están en **euros enteros**; el libro trabaja en millones. `escala` y `unidad` tienen que decirlo.
- **Acciones:** 134.365.561 en circulación al 31-dic-2025, sin autocartera ni dilutivos (decisión P-O2: acciones al cierre).
- **Precio (C37) y capitalización (C41):** el precio de 27,28 € del 17-nov-2026 está verificado por la persona responsable en la página oficial de Euronext Athens (`coordinacion/cierre_v2/examen/precios/JUMBO_BELA_20261118.md`). Guarda tú el histórico oficial de Euronext Athens de esa sesión como texto con SHA-256 en `fuentes_mercado/` si puedes; si no, dilo.
- **Tasa sin riesgo:** Bund a 10 años de la misma fecha, de fuente oficial (Bundesbank o BCE), guardada igual. Si no puedes, dilo; no pongas otra fuente sin avisar.
- **Caja y depósitos:** separa efectivo, depósitos a plazo y depósitos restringidos; la cartera de acciones y bonos cotizados no es caja.

## 4. Qué entregas

Rama nueva **`mistral/examen-jumbo-entradas`**, carpeta `resultados_examen/jumbo/`: `verificacion_entradas.json` (las 313 entradas, las 30 hipótesis sin tocar), `fuentes_mercado/` con `HUELLAS.txt`, `DESCARGAS.tsv` y `ENTREGA.md` (máximo una página). Commit y push al terminar cada bloque grande.

---

### Frase para pegar en la ventana nueva

> Lee `coordinacion/cierre_v2/examen/jumbo/ENCARGO_MISTRAL_ENTRADAS_JUMBO.md` en la rama `coordinacion/cierre-v2` del repositorio `jluisplagos/munger-v2-evidencias-mistral` y hazlo entero. Entrega en la rama `mistral/examen-jumbo-entradas`.
