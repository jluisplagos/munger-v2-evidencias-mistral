# Revisión independiente · G-RAIZ · 3d66437

- **Cambio:** `origin/integracion/hechos-raiz-957af65` @ `3d66437e797b6b0bf137b42fa62b561f39121722`, sobre `957af652cdc3bef3d67e8623c9572138bac685e9`.
- **Archivos tocados:** `CLAUDE.md`, `README.md` y `docs/MIGRATION_STATUS.json`. Son 15 líneas añadidas y 13 suprimidas.
- **Candidata de destino:** `3149128` (957af65 + G-DOCS), en `<candidata>`.
- **Revisor:** agente distinto del autor del cambio. He trabajado en solo lectura: sin commits ni push, sin ejecutar el pipeline y sin LibreOffice.
- **Fecha:** 17-nov-2026.
- **Sondas:** `sondas/01_diff_y_supresiones.sh`, `sondas/02_respaldo_957af65.sh` y `sondas/03_json_aplicacion_rutas.sh`, cada una con su `.salida.txt`. En las salidas, las rutas aparecen como `<producto>` y `<candidata>`.

Abreviaturas de las fuentes citadas (todas en 957af65):
- `VERSION` = `munger_v2_r1/VERSION`
- `H1` = `munger_v2_r1/personaje_v2/empresas_v2_correcciones/2026-11_Vidrala_ensayo_4_15/HITO_1_4_15.md`
- `H2` = `…/2026-11_Vidrala_ensayo_4_15/hito2/HITO_2_4_15.md`
- `PR` = `…/2026-11_Vidrala_ensayo_4_15/hito2/PUNTO_DE_RECUPERACION.md` (fuera de los cuatro archivos pedidos, pero en 957af65)
- `T415` = `munger_v2_r1/personaje_v2/pruebas/test_verificacion_entradas_415.py`
- `REC` = `docs/RECEPCION_ENTREGA_CLAUDE.md` (no cambia)

## Veredicto por criterio

| # | Criterio | Veredicto |
|---|---|---|
| 1 | Solo cambian hechos verificables en 957af65, cada uno con su archivo:línea | **CORRECCIONES** (G1, G3, G5) |
| 2 | Se conservan todas las instrucciones sustantivas y las decisiones | **CORRECCIONES** (G2, G3, G4). Las instrucciones de la lista se conservan sin cambios; las supresiones afectan a otras instrucciones sustantivas |
| 3 | No se declara aptitud ni se adopta nada; main sigue con la 4.14 | **CONFORME_CON_LIMITES**. No se declara aptitud y main no cambia, pero «1–6 corregidos» (G1) se lee como un cierre y G3 introduce una regla de proceso nueva |
| 4 | JSON válido y recuentos; aplicación limpia sobre 3149128; sin rutas locales ni datos personales | **CONFORME** |

**Dictamen global: ACEPTABLE CON CORRECCIONES.** Bastan correcciones de texto en las tres raíces; no hay que tocar ningún archivo del producto. No recomiendo integrar 3d66437 tal como está.

## Hallazgos

### G1 · MATERIAL · «1–6 corregidos» exagera el estado y contradice el registro del hito 2

- **Dónde:** `CLAUDE.md:11` (3d66437): «situación en esta candidata: 1–6 corregidos en los hitos 1 y 2 de la 4.15, con el límite H9 del relevo caducado todavía abierto; 7, F1, sigue abierto».
- **Evidencia en 957af65:**
  - `H2:194-196`: «Regeneración y auditoría de los expedientes Viscofan, Vidrala y Elis: sus registros siguen “no aptos por entradas” con las reglas 4.15 […] C48 y C50 siguen no reproducibles en los expedientes 4.14 hasta su regeneración».
  - `H2:219-220`: «No cerrado: F1; regeneración y auditoría de los expedientes […]; I19/H9; U1; U6 (a); los límites del §5; el control de la entrega 4.14 (29/35)».
  - `H1:181`: la reconstrucción de C48 marca `reproduce: false` con código 1. «La prueba con el código 0 solo existirá con el expediente de Elis regenerado».
  - `H1:205-211`: los expedientes 4.14 son «no apto por entradas»: no tienen vínculos, les faltan las cifras de juicio y C48 y C50 no son reproducibles.
  - `PR:39`: la regeneración y la auditoría de los expedientes siguen pendientes.
- **Qué está respaldado:** la corrección **del código**.
  - Puntos 1, 2 y 3: `H1:16-40` y `T415:8-13`.
  - Punto 4: `H1:134-153`, `H2:45-49` y `H2:213-216`.
  - Punto 5: `H1:42-72`.
  - Punto 6: `H2:82-93`.
- **Qué no está respaldado:** que los puntos 4 y 5 estén corregidos en la candidata. El punto 4 exige expresamente «corregir la derivación/reconstrucción», y 957af65 dice que la reconstrucción con código 0 y la reproducibilidad de C48 en el expediente siguen pendientes. Además, el paréntesis cita solo H9 y F1 como abiertos. Omite la regeneración y la auditoría, U1, U6 (a) y el control 4.14 (29/35), que `H2:219-220` enumera como «no cerrado». El README sí conserva «No contiene […] los expedientes regenerados» (`README.md:3`), así que los dos archivos raíz quedan incoherentes entre sí.
- **Por qué es material:** `CLAUDE.md` es la instrucción de arranque de toda sesión, y el punto 4 (C48) es una decisión protegida. Un agente que lea «corregidos» puede dar por cerrada la reconstrucción de C48 o la vigencia de los registros reales.
- **Prueba de cierre:** el paréntesis debe decir, por ejemplo: «situación en esta candidata: 1–6 corregidos en el código (hitos 1 y 2 de la 4.15); siguen abiertos el límite H9 del relevo caducado, la regeneración y auditoría de los expedientes Viscofan, Vidrala y Elis —sus registros siguen “no aptos por entradas” y C48 y C50 no son reproducibles en los expedientes 4.14 hasta su regeneración— y los demás puntos no cerrados de `HITO_2_4_15.md` §9; 7, F1, sigue abierto y pendiente de decisión». Se comprueba con `grep -n 'regeneración' CLAUDE.md` en la nueva revisión.

### G2 · MEDIO · Se suprime que hay correcciones en curso sin importar y se debilita la instrucción de esperar a la entrega final

- **Dónde:**
  - `CLAUDE.md:35`. Antes decía: «Las correcciones aún en curso no se han importado. Esperar su entrega final y conservarla; después importar…». Ahora dice: «La entrega del hito 2 de la 4.15 ya está importada en esta candidata (957af65). Las entregas posteriores se conservan y se importan igual…».
  - `README.md:17`: se suprime «Las correcciones que Claude está preparando no están incorporadas todavía».
  - `docs/MIGRATION_STATUS.json`: `note` pierde «Correcciones actuales de Claude todavía no importadas» y `next_action` pierde «Esperar a que Claude termine».
- **Evidencia en 957af65:**
  - `H2:9`: «La conciliación económica F1 se hace en otra tarea, sobre una copia independiente».
  - `H2:20-21`: «Los trabajos que pudieran seguir en la conversación anterior de Claude **no** se han incorporado».
  - `PR:40` y `PR:52`: F1 sigue en otra tarea, pendiente de decisión.

  Que la entrega del hito 2 está importada es cierto (`VERSION:1`, `H2:211-220`). Pero el propio registro dice que hay trabajo en otra tarea sin incorporar, y el cambio borra esa frase.
- **Instrucción debilitada:** se pierde «Esperar su entrega final». La frase nueva («se importan igual») no exige esperar a que el trabajo termine. Queda un respaldo indirecto en `REC:5` («Cuando termine:»), al que remite `CLAUDE.md:37`. Por eso lo clasifico como medio y no como material.
- **Prueba de cierre:** `CLAUDE.md:35` conserva las dos ideas, por ejemplo: «… ya está importada en esta candidata (957af65). Otras correcciones en curso, como F1 en otra tarea, no se han importado: esperar su entrega final y conservarla; después importarla como nueva versión sobre una copia completa, nunca sobrescribiéndola con la base histórica». `README.md:17` y `note` del JSON dicen lo mismo.

### G3 · MEDIO · Regla de integración nueva, sin respaldo en 957af65, que sustituye dos restricciones

- **Dónde:**
  - `README.md:7`. Antes: «Esta rama conserva **exactamente** el código recibido, **sin incorporar correcciones propias al producto**». Ahora: «Esta rama conserva el código recibido del hito 2. Solo se incorporan en ella archivos revisados por un contexto distinto del autor, con su origen, revisión y destino registrados en el control del programa de cierre (…)».
  - `docs/MIGRATION_STATUS.json`, `next_action`. Antes: «… incorporarla **en otra rama** con su propio manifiesto». Ahora: «Integrar en la candidata solo archivos revisados…». `ongoing_claude_work` también pierde la rama aparte.
- **Evidencia:**
  - La regla no sale de 957af65: `git grep` de `candidata-cierre`, `evidencias-mistral` y «programa de cierre» en 957af65 no devuelve nada (sonda 02, rc=1).
  - Contradice `REC:10` («Crear una rama nueva e importar su código…»), que sigue vigente y al que remite `CLAUDE.md:37`. También es menos clara que `CLAUDE.md:22` («Trabajar en ramas y expedientes nuevos»), que no cambia.
  - Ya no excluye las correcciones al **código del producto**, solo exige que estén revisadas. G-DOCS (3149128) era «no code».
  - *Interpretación:* que se quite «exactamente» se entiende, porque 3149128 ya cambió 4 archivos de documentación. Lo que falta es acotar qué se admite.
  - El siguiente paso que registra 957af65 es otro: «Revisión externa del hito 2» y «Lo que decida la persona responsable» (`PR:49-53`). Ver G4.
- **Prueba de cierre:** dos cambios.
  - (a) Marcar la regla como decisión de la persona responsable, con referencia al registro de coordinación que la contiene. No debe presentarse como un hecho de 957af65.
  - (b) Conservar las dos restricciones: «sin incorporar correcciones propias al código del producto salvo decisión registrada» y «cada nueva entrega de Claude se importa en una rama nueva con su manifiesto (docs/RECEPCION_ENTREGA_CLAUDE.md)».

### G4 · MEDIO · Desaparece la revisión externa pendiente

- **Dónde:**
  - `README.md:1-3`: se pierde «Entrega intermedia […] con una revisión externa en curso».
  - `CLAUDE.md:1`: se pierde «rama de revisión intermedia».
  - `MIGRATION_STATUS.json`: el nuevo `next_action` no menciona ninguna revisión externa.
- **Evidencia:** `PR:49-53` fija como «Siguiente paso exacto» la revisión externa del hito 2 y las decisiones de la persona responsable. `PR:53` añade: «Este frente no inicia ninguno por su cuenta». Ningún archivo de 957af65 dice que esa revisión se haya hecho.
- **Prueba de cierre:** `CLAUDE.md:1` o `README.md:3` dicen que la 4.15 · hito 2 está pendiente de revisión externa (`PUNTO_DE_RECUPERACION.md` §«Siguiente paso exacto»), y `next_action` la recoge antes de cualquier integración.

### G5 · MENOR · Hechos de rama y programa que no están en 957af65

- **Dónde:**
  - `CLAUDE.md:1`: «candidata de integración del programa de cierre: rama `integracion/candidata-cierre-v2`».
  - `README.md:3`: «creada desde 957af65».
  - `README.md:7`: control `jluisplagos/munger-v2-evidencias-mistral`, rama `coordinacion/cierre-v2`.
  - JSON: `candidate_branch` y `candidate_base_commit`.
- **Evidencia:** son ciertos según las referencias Git, que he comprobado:
  - `origin/integracion/candidata-cierre-v2` = `3149128`, cuyo padre es 957af65;
  - `3149128:munger_v2_r1/CONTINUIDAD.md:6`;
  - el repositorio de control existe y es público.

  Pero no hay ningún archivo:línea de 957af65 que los respalde, como pide el criterio 1. Además, `CLAUDE.md:1` llama a la candidata «(commit 957af65)», cuando su cabeza es 3149128. Sería más exacto «sobre 957af65».
- **Prueba de cierre:** citar la fuente (referencia Git o `CONTINUIDAD.md:6` de la candidata) en el registro de G-RAIZ, y escribir «sobre 957af65» en `CLAUDE.md:1`.

## Comparación frase a frase de las líneas suprimidas

| Línea suprimida (957af65) | Línea nueva (3d66437) | Juicio |
|---|---|---|
| CLAUDE:1 «rama de revisión intermedia 4.15 hito 1 … correcciones técnicas de ese hito, sin cierre económico ni aprobación final … Leer docs/revision_externa_4_15_hito1/ y el encargo correctivo vigente. Mantener en main la base histórica 4.14. No sobrescribir el trabajo en curso de la sesión de Claude» | Hito 2 (`VERSION:1`); «sin cierre económico ni aprobación final» (`H2:9-10`, `H2:219-220`); se añade la lectura de HITO_2 (la ruta existe); main 4.14 se conserva; «de ninguna sesión» amplía la protección | Conforme, salvo G4 (se pierde «intermedia») y G5 |
| CLAUDE:10 «La versión de referencia es 4.14, experimental supervisada; no apta para dinero real» | «base histórica de referencia es la 4.14 (main); […] 4.15 · hito 2. Las dos son experimentales supervisadas; no aptas para dinero real» | Conforme (`VERSION:1` «aptitud: uso supervisado experimental, no apto…»; `H2:8`) |
| CLAUDE:11 «La revisión externa parcial encontró:» | Se añade la situación | **G1** (H9 `H2:92`, F1 `H2:192-193` y «pendiente de decisión» `PR:40,52`, todos respaldados; «1–6 corregidos» no) |
| CLAUDE:20 «Los 119 tests repetidos no cubren los tres huecos nuevos» | «…de la 4.14 no cubrían…; desde la 4.15 los cubre `test_verificacion_entradas_415.py` (190 pruebas en el hito 2)» | Conforme: 190 en `H2:99`, `PR:12`, `verificacion_completa_0a0020b.txt:30` y mínimo `-ge 190` en `verificar_paquete.sh:152`; R1–R3 con sus contraejemplos en `T415:8-13` |
| CLAUDE:35 «Las correcciones aún en curso no se han importado. Esperar su entrega final y conservarla; …» | «Entrega del hito 2 ya importada; las posteriores se importan igual» | **G2** |
| README:1 «Rama de revisión: 4.15, hito 1» | «Candidata de integración: 4.15, hito 2» | Conforme (`VERSION:1`) con G5 |
| README:3 «Entrega intermedia … revisión externa en curso … contraejemplo nuevo del control de signos» | Hito 2; «No contiene el cierre económico F1 ni los expedientes regenerados» se conserva | El contraejemplo de signos está corregido (R415-SIGNO, `H2:23-49`). **G4** por la revisión externa pendiente |
| README:7 «conserva exactamente el código recibido, sin incorporar correcciones propias al producto» | Regla de integración nueva | **G3** |
| README:17 «Las correcciones que Claude está preparando no están incorporadas todavía. Su trabajo debe continuar sin interrupción» | «Las correcciones de los hitos 1 y 2 … están en la candidata; main conserva la 4.14 sin cambios. El trabajo en otras sesiones debe continuar sin interrupción» | **G2** (se pierde la parte en curso); «main sin cambios» es conforme (sonda 03) |
| JSON `note`, `next_action`, `ongoing_claude_work` | Ver G2 y G3 | **G2 y G3**; se conserva «Continuar sin interrupción» y «versión nueva con manifiesto propio» |

**Instrucciones protegidas: todas se conservan sin cambios en 3d66437.**

| Instrucción | Dónde |
|---|---|
| Originales y decisiones humanas | `CLAUDE.md:22` |
| Fuentes y huellas | `CLAUDE.md:23` |
| LibreOffice en secuencia | `CLAUDE.md:24` |
| Aprobaciones retiradas y auditoría de material distinto | `CLAUDE.md:25` |
| Firmas, política económica y aptitud | `CLAUDE.md:26` |
| Opus y Fable | `CLAUDE.md:28-30` |
| Revisor distinto del autor | `CLAUDE.md:31` |
| Prevalencia del encargo vigente | `CLAUDE.md:33` |
| Recuperación con la 4.14 (README, `RECEPCION_ENTREGA_CLAUDE.md`, ZIP completo, herramientas exclusivas de la 4.14) | `CLAUDE.md:37` |
| `base_414.py verify` y recuentos 5790/1008/6798 | `CLAUDE.md:7` |
| No declarar completa la migración ni iniciar el pipeline | `CLAUDE.md:8` |
| Main conserva la 4.14 | `CLAUDE.md:1` y `README.md:5`, `README.md:17` |
| C48 = 108, sin sustituir por 82.933 | `CLAUDE.md:15` |
| Los 7 hallazgos de la revisión externa | `CLAUDE.md:12-18` |
| Sección del README de archivos pesados y `base_414.py` | Sin cambios fuera de las líneas 1-17 |

## Lo conforme

- **JSON:** es válido. No cambia ningún recuento (5790, 352638783, 1008, 0). `candidate_base_commit` es un commit existente y coincide con la base. `candidate_branch` existe en el remoto.
- **Cifras modificadas:** 190 pruebas, hito 2, aptitud experimental, F1 abierto y H9 abierto están respaldadas en 957af65 (ver tabla).
- **Aplicación sobre la candidata:**
  - `git merge-tree --write-tree 3149128 3d66437` da rc=0, sin conflictos. Los tres blobs fusionados son idénticos a los de 3d66437.
  - `git apply --cached --check` sobre un índice temporal de 3149128 da rc=0.
  - G-DOCS no toca ninguno de los tres archivos.
- **Main:** sigue con la 4.14. 957af65 no es antecesor de `origin/main`, el `VERSION` de main es la 4.14 y el árbol del producto (`munger_v2_r1`, `baselines`, `tools`) no ha cambiado desde la base común.
- **Rutas y datos:** no hay rutas locales, correos ni datos personales en las líneas añadidas. La única referencia nueva es `jluisplagos/munger-v2-evidencias-mistral`, un repositorio público del mismo propietario que ya figura en `remote_url`.
- **Aptitud y adopciones:** no se declara aptitud ni se adopta ninguna opción económica.

## Límites de esta revisión

- He comprobado los hechos contra los registros de 957af65. No he ejecutado las baterías: el 190/190 se toma de `verificacion_completa_0a0020b.txt` y del mínimo de `verificar_paquete.sh`. El recuento estático de llamadas `paso(` en `T415` es 182; el resto se genera en bucles, y no lo he ejecutado.
- La cifra «119 tests repetidos» es anterior al cambio, que no la modifica, y no he encontrado su origen en `docs/` de 957af65. Queda fuera del alcance.
- No he verificado si G3 responde a una decisión de la persona responsable registrada en el repositorio de control. Si existe, G3 se cierra citándola y conservando las restricciones del punto (b).
- La clasificación material, medio o menor es mía.
