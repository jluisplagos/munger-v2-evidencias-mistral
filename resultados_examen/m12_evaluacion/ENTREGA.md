# Entrega M12 · borrador de evaluación con la rúbrica · Ahold (f4) y Zoetis T1 (t1d)

**Rama:** `mistral/m12-evaluacion` · **Carpeta:** `resultados_examen/m12_evaluacion/` · **Fecha:** 19-nov-2026 · **Autor:** Mistral (borrador de evaluador independiente; no valora empresas ni recomienda nada; revisa y decide un evaluador Claude distinto, Fable si hay cuota).

**Encargo ejecutado:** `coordinacion/cierre_v2/examen/evaluacion/ENCARGO_MISTRAL_M12_BORRADOR_EVALUACION.md` (rama `coordinacion/cierre-v2`, repo `jluisplagos/munger-v2-evidencias-mistral`).

**Material y huellas.**
- Rúbrica congelada: `coordinacion/cierre_v2/examen/RUBRICA_EXAMEN.md`; SHA-256 comprobado = `07dd459752815e4cb225ac44c532290e15b2852c41c12253b0fb27696a330579`, coincide con `RUBRICA_EXAMEN.sha256`. Secciones usadas: 0, 1 (Ahold), 3 (Zoetis, solo T1), 7, 8, 9, 10.
- Expedientes cerrados (solo lectura): repo `jluisplagos/munger-v2`, rama `examen/expedientes-f1`, `munger_v2_r1/personaje_v2/empresas_v2_correcciones/2026-11_examen_universo/ahold_f4/Ahold/` y `zoetis_t1d/Zoetis/` (`fase_a/b/c.*`, `ficha.json`, `informe.md`, `precio.json`, `resultados.json`, `auditoria.md`, `extracto_v63.md`, `datos_v63.md`, `verificacion_entradas.json`). Ambos con auditoría `APROBADO` y entradas aptas (Ahold 308/309; Zoetis 313/315).
- Contradictor: `coordinacion/cierre_v2/examen/contradictor/{ahold_f4,zoetis_t1d}/OBJECIONES.{json,md}`; encargo fijo e independencia en `coordinacion/cierre_v2/examen/CONTRADICTOR.md` §3 (contexto limpio, solo la carpeta del expediente).
- Análisis directo (§10): rama `automatizacion/claude-api-piloto-registro`, `automation/coordination/reviews/analisis-directo-ahold-44290314915/report.json` (revalidado en `coordinacion/cierre_v2/examen/analisis_directo/ahold_44290314915/`; repeticiones `-44381043620`, `-44381146484`) y `analisis-directo-zoetis-{44399614319,44402575472,44405210664}/report.json`.

## Tabla §7 rellena (las dos filas de este encargo)

| Caso | Salida (estado · cubo · acción) | ¿Correcta? (C/aceptable/no) | S | E | G (n) | m (n) | K6 (%) | Hechos † (n de N) | Sensibilidad 7–11 % y prueba del 10 % | Contradictor (§9) | Resultado del caso |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Ahold | `concluido · Vigilar · esperar` · P* 33,79 € emitido (zona `caro`, precio 36,05 €) | **C** | 0 | 0 | 0 confirmados (duda en K4) | 1 (K5 parcial) | 10/12 claras (83 %) | 5/5 | Sin tabla 7–11 %; tornado ±1 pt = ±5,94 €; g impl. 3,31 %; prueba del 10 % no escrita | 2 válidas (1↓ O1 −2,0 €, 1↑ O2 +0,9–1,4 €), no rebatidas, se compensan; acción sin cambio | **PASA** (con m anotado; duda K4 para el revisor) |
| Zoetis T1 | `concluido · Demasiado difícil · demasiado_dificil` · sin objetivo; P* 73,27 USD calculado (zona `cumple_regla_k`, precio 73,08 USD) | **No** (§3 T1 admite Vigilar/pendiente_*; duda si el descalificador C12 lo admite) | 0 (K10 ok) | — | 1 (cubo distinto, acción sin cambio) | 1 (K5 parcial) | 11/11 (100 %) | 2/2 | Sin tabla 7–11 %; tornado ±1 pt = ±22,5 USD; g impl. 1,26 % | 2 válidas, las dos ↑ (O1 → P* 75,42; O2 → 73,66/75,81), **rebatidas**; movimiento: ninguno | **No PASA** en esta pasada (salida no correcta; G sin corregir → SUSPENDE-G si persiste tras 2 rondas) |

El detalle casilla por casilla con citas `archivo:línea` está en `EVALUACION_AHOLD.md` y `EVALUACION_ZOETIS_T1.md`.

## §10 · personaje frente a análisis directo (ambos casos)

| Medida | Ahold | Zoetis T1 |
|---|---|---|
| Veredicto vs rúbrica | Personaje `Vigilar·esperar` = correcta (sí); directo 44290314915 `vigilar·esperar` = correcta (sí). Coinciden. | Personaje `Demasiado difícil` = no correcta; directo `vigilar·esperar` (P* 68,94–69,58 en 3 ejecuciones) = correcta. Difieren. |
| Precio de Sí | Personaje 33,79 € vs directo 31,61 € (repeticiones 31,07/31,60): **+6,9 %**. Causa principal: base FCF 2.312 (regla espejo + F1 A2_propio) vs 2.000 estricto del directo, que incluye la devolución fiscal belga de 367 M€ sin normalizar (mismo sesgo que O1). | Personaje 73,27 USD vs directo ≈ 69,0–69,6 USD: **+5,3–6,2 %**. Motor B con deuda neta 31-dic-2025 y p 0,3/0,5/0,2 vs FCF base 1.994 y escenarios −2/5/8 %. |
| Trampa de Zoetis (¿«Sí» en T1?) | n/a | Ninguno de los dos dice «Sí» en T1 (K10 cumplido en ambos). |
| Errores económicos materiales | Personaje: duda K4 (motor B sin zona). Directo: base con devolución belga no normalizada (G leve, no sostiene conclusión favorable); no aplicó F1 aunque el paquete lo traía; sin doble cómputo (no suma pasivo de arrendamientos a la deuda). | Personaje: G(1) de cubo. Directo: ninguno S/G visible en el report; sí trae la tabla de sensibilidad 7–11 % completa (7 % → P* 98,91; 8 % → 81,66; 10 % → 60,63 `caro`; 11 % → 53,73), que al personaje le falta. |
| K6 con esta rúbrica | Personaje 10/12 claras (83 %). Directo: ~12 «lo que no sé» listados → menor. | Personaje 11/11 (100 %). Directo: incógnitas declaradas (fechas de exclusividad, cuotas, Librela, guía retirada) → menor. |
| Coste y tiempo | Directo: 1,923 USD, 388.375 tokens in / 18.475 out, una pasada (+2 repeticiones ≈ 1,92–1,95 USD; variación P* < 2 %). Personaje: sin registro de coste en el expediente. | Directo: 3 ejecuciones × ≈ 1,87–1,97 USD, 369.300 tokens in cada una. Personaje: sin registro de coste. |

**«Claramente mejor» (§10, fijado de antemano):** no se cumple ninguna de las tres condiciones de forma demostrable con este material: (1) ninguno de los dos evitó una trampa S en la que cayera el otro (no hubo S en ninguno); (2) no se pueden contar «dos errores materiales menos» de forma robusta (el personaje tiene la duda K4 en Ahold y el G de cubo en Zoetis; el directo tiene la base con devolución en Ahold) → **duda**; (3) +20 puntos de K6 no cuantificables exactamente para el directo → **duda**. Con dos casos esto es un indicio, no una prueba, y **no cambia el veredicto final** (§10).

## Dudas que dejo al revisor (donde no pude decidir)

1. **Ahold · K4:** el expediente compara flujos sin crecimiento por perímetro (A0/A1/A2/B_cota) pero no calcula el motor B completo ni compara zonas. Si eso no suple a «dos motores» (§1 G: «un solo motor sin justificar por qué no hace falta el otro»), hay un G sin corregir en Ahold y el caso dejaría de ser PASA.
2. **Zoetis T1 · salida:** si el descalificador C12 (no sabe juzgar la duración del foso, con fechas de exclusividad y competidor de dermatología declarados datos ausentes materiales) se admite como justificación de `Demasiado difícil` en T1, la salida sería aceptable y el G(1) desaparecería; §3, sin embargo, no lista `Demasiado difícil` entre las correctas de T1 (la reserva para el límite del modelo de Vinci, §5).
3. **K5 en ambos casos:** falta la tabla de precio de Sí y zona al 7–11 % y la prueba del 10 % escrita (hay tornado ±1 punto y g implícita). Puntué m; si el revisor lo trata como incumplimiento con efecto, sube a G.
4. **K7 en Zoetis T1:** no demostrable — las otras corridas T1 (t1 `pendiente_de_datos`, t1c `no_entregable`, t1b sin ficha cerrada) no repiten cubo/acción/P*.
5. **Análisis directo de Ahold usado:** la ejecución 44290314915 (revalidada fuera de línea, con huella en `analisis_directo/ahold_44290314915/revalidacion.json`), no las repeticiones A4 aceptadas en línea (44381043620, 44381146484), que cito como variación < 2 %. Para Zoetis uso la última (44405210664) con las otras dos como repeticiones (variación < 1 %).

## Notas de método

- Solo lectura sobre `munger-v2` (rama `examen/expedientes-f1`); no se escribió nada en el repo del producto.
- La rúbrica se verificó por SHA-256 antes de usarla; no se tocó.
- No se emiten tamaños de posición, no se cambia la tasa del 9 % y no se afirma aptitud para dinero real (reglas del repo y §11 de la rúbrica).
