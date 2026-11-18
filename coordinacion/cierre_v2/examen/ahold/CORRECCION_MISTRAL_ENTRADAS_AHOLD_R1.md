# Corrección para Mistral · Registro de entradas de Ahold · ronda 1 de 2

**Para pegar en la misma ventana de Mistral que hizo el registro** (rama `mistral/examen-ahold-entradas`, commit `c0231a0`). Fecha: 18-nov-2026.

## Lo que el coordinador comprobó

- `verificacion_entradas.py comprobar` sobre una copia del expediente con tu registro da **41 errores, todos esperados**: tus 11 entradas sin resolver (clase `null`) y las 30 hipótesis, que no eran de tu encargo. **Ninguna de tus 247 entradas resueltas tiene un error de formato.**
- Las huellas de los 5 archivos de `fuentes_mercado/` coinciden. La página de dividendos, descargada de nuevo por el coordinador, da el mismo SHA-256. Las filas del 13-nov (36,05) y del 17-nov (35,14) de Euronext y el Bund del 17-nov (3,34 %) están en sus archivos.
- Una muestra de 8 entradas de la Historia tiene la columna, el signo y la escala correctos.

Buen trabajo. Quedan tres cosas.

## Lo que tienes que corregir

1. **`Historia!F7` (EBIT 2019 = 2.663).** No es un dato publicado, es un **derivado**. La Historia define el EBIT de los diez años como *resultado antes de impuestos − resultado financiero* (lo dice `fase1_v63.json` y la nota de la partida). Regístralo como `derivado`:
   - con sus orígenes `aux:` publicados (BAI de 2019 y las líneas del resultado financiero, de la columna comparativa del informe que da el valor del libro: mira `fase1_partes/AR_2020.json`, partida `ebit_derivado`, columna `anterior`);
   - con una fórmula que dé exactamente 2.663;
   - y con la conciliación frente al «Operating income» impreso (2.662), que explique la diferencia de redondeo.
2. **`Análisis!C24, C26, C32, C33, C42, C60, C88, C96`.** Son valores que vienen de la etapa 1 o que calcula la fase 1 a partir de la Historia. Para cada uno:
   - **(a)** si una fórmula sobre celdas de la Historia o sobre `aux:` publicados **reproduce exactamente** el valor del libro, regístralo como `derivado`, con la fórmula y la conciliación (mira `scripts/fase1_historia.py`, `DEP_ANALISIS` y las celdas C24/C26/C28/C33, para ver cómo se calculan);
   - **(b)** si no lo reproduce, déjalo sin resolver y di en `nota` **qué valor da tu mejor fórmula y en cuánto difiere**. No fuerces ninguna cita.
3. **`Palancas!C45, C46` (fechas en formato de serie de Excel).** Regístralas como `convencion`, con `hipotesis` = {`fundamento`: la fecha del precio (13-nov-2026, fila de Euronext) y la fecha de la base (28-dic-2025, cierre del ejercicio 2025), con documento y página; `alternativas`; `limites`} y `justificacion_clase` («el libro guarda la fecha como número de serie de Excel; el texto de la fuente no puede contener ese número»).

## Cómo entregas

- El mismo archivo `resultados_examen/ahold/verificacion_entradas.json` en la misma rama, más una sección «Ronda 1» al final de `ENTREGA.md` (máximo 15 líneas) con lo que resolviste y lo que no.
- No cambies las 247 entradas que ya están bien, salvo que encuentres un error tuyo; si lo encuentras, dilo.
- Las comprobaciones siguen en `pendiente`, con `revisor: null` y sin `vinculo`. Commit y push.

Es la primera de como máximo dos rondas. Después, un agente Claude distinto revisará las entradas en la fuente y las sellará.
