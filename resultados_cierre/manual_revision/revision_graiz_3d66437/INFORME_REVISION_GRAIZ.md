# Informe de revisión independiente G-RAIZ (U4)

- **Tarea**: G-RAIZ, `solicitud_revision` estado LISTA en `coordinacion/cierre_v2/CONTROL.json` (control vigente consultado en `origin/coordinacion/cierre-v2` @ `30c314c`; la solicitud no ha cambiado desde `b257dfd`/`6370d21`).
- **Objeto revisado**: `jluisplagos/munger-v2`, rama `integracion/hechos-raiz-957af65` @ `3d66437e797b6b0bf137b42fa62b561f39121722`, base `957af652cdc3bef3d67e8623c9572138bac685e9`. **Solo lectura** vía `gh api`; no clonado, no modificado, no ejecutado nada del producto.
- **Autor del cambio**: Claude coordinador (commit message: "U4: update outdated facts in root README, CLAUDE.md and MIGRATION_STATUS… For independent review before acceptance"). Esta revisión es de un contexto distinto del autor.
- **Revisor**: sesión Vibe Code de Mistral AI, modelo `mistral-large-4-0`. Herramientas realmente usadas: `gh api` (lectura), `sh`, `diff`, `sha256sum`, `grep`, `python3` (JSON). Sin LibreOffice, sin pipeline, sin red propia.
- **Fecha**: 2026-11-17 (UTC).

## Veredicto: **CONFORME CON LÍMITES** en los 3 criterios

## Alcance verificado (s01, s03)

- Rama `integracion/hechos-raiz-957af65` HEAD == `3d66437e…` ✔
- `3d66437` tiene un único parent == `957af652…` ✔
- `compare 957af65...3d66437`: `ahead_by=1`, `total_commits=1`, y **exactamente** los 3 `diff_rutas`: `CLAUDE.md` +5/−5, `README.md` +4/−4, `docs/MIGRATION_STATUS.json` +6/−4. Ningún otro archivo tocado ✔
- Hashes de los 6 archivos descargados (3 en base, 3 en head) en `sondas/s02.out`; diffs completos en `sondas/s03.out` y `sondas/diff_*.md` / `diff_MIGRATION_STATUS.json`.

## Criterio 1 — Solo cambian hechos verificables en 957af65: **CONFORME** (s04)

Cada hecho nuevo declarado en head quedó contrastado contra `957af65`:

| Hecho declarado en 3d66437 | Verificación en 957af65 | Evidencia |
|---|---|---|
| Rama `integracion/candidata-cierre-v2`, creada desde 957af65 | `compare 957af65...integracion/candidata-cierre-v2` → `ahead`, `behind_by=0` (957af65 es ancestro) | s04 [H2] |
| Entrega 4.15 · hito 2 (commit 957af65; `munger_v2_r1/VERSION`) | `VERSION@957af65` empieza "entrega 4.15 · hito 2" | s04 [H1] |
| Correcciones técnicas de los hitos 1 y 2 | Existen `…/2026-11_Vidrala_ensayo_4_15/HITO_1_4_15.md` y `…/hito2/HITO_2_4_15.md` en el árbol de 957af65 | s04 [H4], [H5], [H6] |
| Hallazgos 1–6 corregidos en los hitos 1 y 2 | HITO_1 §R1 (página inexistente), §R2 (fuente local ausente), §R3 (redondeo), hallazgo 4 (HITO_1:182), hallazgo 5 (HITO_1:38); HITO_2 §3 I19/I20 (hallazgo 6, HITO_2:80-92) | s04 [H5], [H6] |
| Límite H9 del relevo caducado todavía abierto | HITO_2:92 "Límite (H9)", HITO_2:147, HITO_2:219 "No cerrado: … I19/H9" | s04 [H6] |
| 7 / F1 sigue abierto | CLAUDE.md:18; HITO_2:192 "F1 (bloqueo económico, otra tarea)", HITO_2:219 | s04 [H6] |
| `test_verificacion_entradas_415.py` cubre los huecos (190 pruebas en el hito 2) | El archivo existe en 957af65 (`munger_v2_r1/personaje_v2/pruebas/…`, 1214 líneas / 113051 bytes); HITO_2:99 declara **190/190** | s04 [H7] |
| `docs/revision_externa_4_15_hito1/` y registro del hito 2 | Existen en el árbol de 957af65 | s04 [H4], [H8] |
| Entrega del hito 2 ya importada en la candidata (957af65) | La rama revisada cuelga directamente de 957af65 y la candidata lo tiene de ancestro | s01, s04 [H2] |
| Referencia al control del programa de cierre (`jluisplagos/munger-v2-evidencias-mistral`, rama `coordinacion/cierre-v2`) | La rama existe en el auxiliar (@ `30c314c`) | s04 [H9] |
| `docs/MIGRATION_STATUS.json` | Sigue siendo JSON válido (25 claves); solo cambian `note`, `next_action`, `ongoing_claude_work` y se añaden `candidate_branch` + `candidate_base_commit=957af65`; todos los campos numéricos/de integridad idénticos | s06 |

**Límite declarado**: la batería `190/190` no se ejecutó aquí (sin pipeline ni LibreOffice; no se ejecuta nada del producto). El archivo de test existe en 957af65 y el recuento 190 es el registrado por el autor en `HITO_2_4_15.md:99`; el conteo estático de llamadas `paso(` en el archivo es 182 directas más las generadas en bucles. La verificación de este hecho es documental, no ejecutiva.

## Criterio 2 — Se conservan todas las instrucciones sustantivas y decisiones: **CONFORME** (s05)

Solo 5 líneas de `CLAUDE.md` y 4 de `README.md` cambian, y todas son hechos de estado (identidad de rama, versión, estado de hallazgos, prueba, importación hecha). Las instrucciones sustantivas quedan **byte a byte idénticas** en head:

- Originales, fuentes y huellas: CLAUDE.md:22-23, README:60 ✔
- LibreOffice en secuencia: CLAUDE.md:24, README:60 ✔
- Aprobaciones: CLAUDE.md:25, README:60 ✔
- Política económica: CLAUDE.md:26 ✔
- Modelos (Opus/Fable): CLAUDE.md:28-30 ✔
- Separación de revisor: CLAUDE.md:31 ("agente distinto del autor del cambio"); además README:7 (nuevo) refuerza que solo se integran archivos "revisados por un contexto distinto del autor" ✔
- Recuperación con la 4.14: CLAUDE.md:37, README:5, 28-47, 55-56, 60; la línea cambiada 35 conserva la regla "nunca sobrescribiéndolas con la base histórica" ✔

La línea 10 nueva conserva la condición "experimentales supervisadas; no aptas para dinero real" para **ambas** versiones. Ninguna instrucción sustantiva se elimina ni debilita (s05.out: todas las palabras clave presentes con el mismo recuento en base y head).

## Criterio 3 — No se declara aptitud ni se adopta nada; main sigue con la 4.14: **CONFORME** (s06)

- Todas las menciones de aptitud en head son negativas: CLAUDE.md:10 ("no aptas para dinero real"), CLAUDE.md:26, README:17 ("comprueba conservación de bytes, no aptitud financiera") ✔
- Nada adoptado: README:3 "No fusionada con main"; MIGRATION_STATUS `next_action` nuevo termina en "no fusionar main"; el commit declara "For independent review before acceptance" ✔
- main sigue con la 4.14: `VERSION@main` = "entrega 4.14 …" (main @ `d69d4837f0e99ce30f38d3461f15cceee9a58730` en el momento de la revisión); HITO_2 §0 registra "main y el ZIP no se han modificado" ✔

## Límites de esta revisión

1. Nada del producto ejecutado (sin pipeline, LibreOffice, tests ni agentes); la verificación es documental vía API de lectura + diffs + hashes.
2. El recuento "190 pruebas" se toma del registro del hito 2 (HITO_2:99); el test no corrió aquí.
3. "main sin cambios" se comprueba por `VERSION@main` en el momento de la revisión, no por un diff histórico completo de main.
4. Esta revisión no integra nada en el producto ni aprueba nada: solo informa al coordinador.

## Evidencias

- `sondas/s01…s06_*.sh` + `s01…s06.out` (ejecutadas, rc=0)
- `sondas/diff_CLAUDE.md`, `sondas/diff_README.md`, `sondas/diff_MIGRATION_STATUS.json`
- `verificacion_criterios.json`, `ENTREGA.json`, `MANIFIESTO_SHA256.txt`, `PUNTO_DE_RECUPERACION.md`
