# Revisión independiente · G-RAIZ · corrección e813fe6

- **Cambio revisado:** `origin/integracion/hechos-raiz-957af65` @ `e813fe66b0210a698398d4f9a4d84788f9dda8e3`. Su padre es `3d66437`, y la base es `957af652cdc3bef3d67e8623c9572138bac685e9`.
- **Archivos:** `CLAUDE.md`, `README.md` y `docs/MIGRATION_STATUS.json`, los mismos tres que en 3d66437.
  - Frente a 3d66437: 14 líneas añadidas y 11 suprimidas.
  - Frente a 957af65: 18 añadidas y 13 suprimidas.
- **Referencias:**
  - la revisión anterior, `REVISION_G-RAIZ_3d66437.md`, con G1–G5;
  - la candidata `origin/integracion/candidata-cierre-v2` = `3149128`, cuyo padre es 957af65;
  - el contrato del programa, `coordinacion/cierre_v2/INTEGRACION.md`, en el auxiliar @ `cefc77f`. Es idéntico al de `ec707a5`.
- **Revisor:** agente distinto del autor. He trabajado en solo lectura: sin commits ni push, sin pipeline y sin LibreOffice. Alcance: solo lo afectado por la corrección.
- **Fecha:** 17-nov-2026.
- **Sondas** (en `sondas/`, cada una con su `.salida.txt`; las rutas aparecen como `<producto>` y `<auxiliar>`):
  - `01_cierre_G1_G5.sh`: pruebas de cierre de G1–G5;
  - `02_respaldo_fuentes.sh`: archivo:línea de cada afirmación nueva;
  - `03_json_mergetree_rutas_protegidas.sh`: JSON, merge-tree, rutas e instrucciones protegidas.

Abreviaturas de las fuentes (todas en 957af65, salvo INT):
- `H1` = `munger_v2_r1/personaje_v2/empresas_v2_correcciones/2026-11_Vidrala_ensayo_4_15/HITO_1_4_15.md`
- `H2` = `…/hito2/HITO_2_4_15.md`
- `PR` = `…/hito2/PUNTO_DE_RECUPERACION.md`
- `REC` = `docs/RECEPCION_ENTREGA_CLAUDE.md`
- `INT` = `coordinacion/cierre_v2/INTEGRACION.md`, en el auxiliar

## Veredicto

| G | Gravedad anterior | Veredicto | Motivo breve |
|---|---|---|---|
| G1 | MATERIAL | **CONFORME** | Ya no dice «1–6 corregidos». Separa lo que corrige el código de lo que sigue abierto, con todas las partidas de `H2:219-220` |
| G2 | MEDIO | **CONFORME** | Vuelven «no se han importado» y «Esperar su entrega final y conservarla», en CLAUDE, README y JSON |
| G3 | MEDIO | **CONFORME_CON_LIMITES** | (b) se cumple al pie de la letra. (a) se atribuye al contrato del programa (`INT:26`, `:31`), que es lo que admite el encargo; no se presenta como hecho de 957af65. Ver N1 |
| G4 | MEDIO | **CONFORME** | La revisión externa pendiente del hito 2 figura en `CLAUDE.md:1`, `README.md:1`, `README.md:3` y al frente de `next_action` |
| G5 | MENOR | **CONFORME** | Dice «sobre 957af65». La rama candidata tiene fuente en `INT:7` y en las referencias Git. Ya no aparecen «(commit 957af65)» ni «creada desde» |

| Comprobación pedida | Resultado |
|---|---|
| 1. G1–G5 cerrados según su prueba, con respaldo | Conforme. G3, con límites (N1) |
| 2. Ninguna instrucción sustantiva suprimida o debilitada frente a 3d66437 y 957af65 | Conforme. Las 22 líneas protegidas de CLAUDE.md son literales; ver la tabla de supresiones |
| 3. JSON válido | Conforme: 26 claves y recuentos sin cambios (5790, 352638783, 1008, []) |
| 4. `git merge-tree --write-tree 3149128 e813fe6` | Limpio: rc=0, árbol `ea3e804…`. Los tres blobs coinciden con los de e813fe6 y el resto del árbol es igual a 3149128 |
| 5. Rutas locales | Ninguna en las líneas añadidas. Tampoco hay correos ni rutas de usuario (rc=1) |

**Veredicto global: CONFORME_CON_LIMITES.** No queda ninguna corrección pendiente que bloquee. Se puede integrar en la candidata con los límites de abajo. N1 es una precisión de redacción recomendable, pero no bloquea.

## Comprobación por G

### G1 (`CLAUDE.md:20`, nueva línea «Situación en esta candidata»)

- **Prueba de cierre:** `grep -n 'regeneración' CLAUDE.md` da la línea 20 (sonda 01). «1–6 corregidos» ya no aparece (rc=1).
- **Lo que dice que corrige el código, con su respaldo:**

| Punto | Afirmación | Respaldo |
|---|---|---|
| 1–3 | Corrige las verificaciones | `H1:16`, `H1:24`, `H1:30` (R1–R3) |
| 4 | Corrige la derivación de C48 en la vía 4.15 (108) | `H1:134-153`, `H2:214-215` |
| 5 | Corrige la vigencia, la cobertura del juicio y los recuentos | `H1:42-72` (I13, I8, I9) |
| 6 | Corrige la aptitud por entradas en las salidas y la detección del relevo caducado | `H2:82-93` (I20, I19) |

- **Lo que dice que no está cerrado, con su respaldo:**
  - expedientes «no aptos por entradas», y C48 y C50 no reproducibles en los expedientes 4.14 hasta su regeneración: `H2:194-196`;
  - extractor y revisor reales: `H2:195`, `H2:219`;
  - U1, U6 (a), los límites del §5, el control 29/35 e I19/H9: `H2:219-220` y `PR:33-42`;
  - F1 «en otra tarea y pendiente de decisión»: `H2:9`, `H2:192`, `PR:40`, `PR:52`.
- **Coherencia con el README:** coincide con `README.md:3` («No contiene … los expedientes regenerados») y con `README.md:17` («los expedientes siguen sin regenerar»). La incoherencia entre los dos archivos raíz queda resuelta.
- *Observación (no es hallazgo):* «hasta su regeneración **y auditoría** con extractor y revisor reales» une `H2:196` con `H2:194-195`. Es más exigente que la fuente, no menos, así que no debilita nada.

### G2 (`CLAUDE.md:37`, `README.md:17`, JSON)

- `CLAUDE.md:37`: «Otras correcciones aún en curso no se han importado: F1 sigue en otra tarea […]. Esperar su entrega final y conservarla; después importarla como nueva versión sobre una copia completa, nunca sobrescribirla con la base histórica». Recupera, adaptada, la frase de 957af65.
  - «Otras correcciones … no se han importado» se apoya en `H2:20-21`.
  - «F1 sigue en otra tarea» se apoya en `H2:9` y `PR:40`.
- `README.md:17`: «Otras correcciones aún en curso, como F1 en otra tarea, no están incorporadas todavía: esperar su entrega final y conservarla».
- JSON:
  - `note` dice «Otras correcciones aún en curso, como F1 en otra tarea, todavía no importadas»;
  - `next_action` y `ongoing_claude_work` vuelven a decir «Esperar … y conservarla» e «importarla en otra rama».
- «No interrumpir el encargo que ya corre en otra sesión» pasa a «los encargos que corran en otras sesiones». Generaliza la protección y no la reduce. La revisión anterior ya lo aceptó.

### G3 (`README.md:7`, `next_action`)

- **(b), se cumple.** Las dos restricciones aparecen con la redacción propuesta en la prueba de cierre:
  - «sin incorporar correcciones propias al código del producto salvo decisión registrada»;
  - «Cada nueva entrega de Claude se importa en una rama nueva con su manifiesto (docs/RECEPCION_ENTREGA_CLAUDE.md)».

  Esto coincide con `REC:10` («Crear una rama nueva…»), y `REC` no cambia. `next_action` también vuelve a decir «incorporarla en otra rama con su propio manifiesto».
- **(a), se cumple con límites.** La regla de admisión ya no se presenta como hecho de 957af65. Se presenta como el contrato del programa, citado así: «su contrato (`jluisplagos/munger-v2-evidencias-mistral`, rama `coordinacion/cierre-v2`, `INTEGRACION.md`:26 y :31)».
  - La paráfrasis es fiel. `INT:26` dice «un revisor distinto revisa cambios de Claude» y «La misma sesión no revisa independientemente su cambio». `INT:31` dice «Importar los archivos/propuestas aceptados […] con lista de archivos, huellas, SHA origen, referencia de revisión y SHA destino».
  - La autoridad del contrato consta en `INT:5`: «Este paquete es el nuevo encargo de programa».
  - El encargo de esta revisión admite citar INTEGRACION.md como contrato del programa. Aun así, el texto no dice «decisión de la persona responsable», como sugería la prueba de cierre. No he verificado fuera de `INT:5` que la persona responsable lo dictara: es un límite, no un hallazgo.

### G4 (revisión externa pendiente)

- `CLAUDE.md:1`: «intermedia y pendiente de revisión externa (`…/hito2/PUNTO_DE_RECUPERACION.md`, «Siguiente paso exacto»)».
- `README.md:1`: «(pendiente de revisión externa)».
- `README.md:3`: «la revisión externa del hito 2 está pendiente».
- `next_action` empieza por «Revisión externa del hito 2 y decisiones de la persona responsable sobre F1, la regeneración de expedientes e I19/H9». Respaldo: `PR:49-53`.
- Ni el control ni 957af65 registran que esa revisión se haya hecho: `grep` en CONTROL.json solo devuelve el veredicto anterior. «Pendiente» sigue siendo cierto.

### G5 (hechos de rama)

- «sobre 957af65» aparece en `CLAUDE.md:1`, `CLAUDE.md:37` y `README.md:3`.
- `INT:7` dice: «candidata en `integracion/candidata-cierre-v2`».
- Referencias Git: `origin/integracion/candidata-cierre-v2` = `31491289…`, con padre `957af652…` (sondas 01 y 03).
- El JSON añade `candidate_source` con la misma cita. `candidate_base_commit` es un commit existente.

## Supresiones frente a 3d66437 y 957af65

| Texto suprimido | Lo sustituye | Juicio |
|---|---|---|
| 3d66437 `CLAUDE.md:1` «candidata de integración … (commit 957af65)» | «candidata de integración técnica … sobre 957af65 … intermedia y pendiente de revisión externa» | Conforme (G4, G5) |
| 3d66437 `CLAUDE.md:11` paréntesis «1–6 corregidos …» | La línea 11 vuelve a ser casi la de 957af65 (+ «de la 4.14»); la situación pasa a `:20` | Conforme (G1) |
| 3d66437 `CLAUDE.md:35` «Las entregas posteriores se conservan y se importan igual…» | `:37`, con «no se han importado», «Esperar su entrega final y conservarla» y el resto literal de 957af65 | Conforme (G2); recupera lo que 3d66437 había debilitado |
| 3d66437 `README.md:7`, regla sin fuente | Restricciones (b) + contrato citado | Conforme con límites (G3, N1) |
| 3d66437 `README.md:17`, `note`, `next_action`, `ongoing_claude_work` | Versiones con la espera, «otra rama» y la revisión externa | Conforme (G2, G3, G4) |
| 957af65 `README.md:3` «Hay un contraejemplo nuevo del control de signos» | Remite a docs/revision_externa_4_15_hito1/ | Conforme: R415-SIGNO está corregido (`H2:23-49`); ya lo dio por bueno la revisión anterior |
| 957af65 `README.md:7` «El trabajo actual de Claude continúa aparte.» | `README.md:17` «Otras correcciones aún en curso … El trabajo en otras sesiones debe continuar sin interrupción» | Conforme: el contenido se conserva |

- **Instrucciones protegidas:** las 22 líneas de `CLAUDE.md` de 957af65 que contienen las instrucciones de la lista son idénticas en e813fe6 (sonda 03). Son el idioma, el orden de lectura, 5790/1008/6798 con `base_414.py verify`, no declarar la migración completa, los puntos 1–7 (con C48 = 108), originales, fuentes y huellas, LibreOffice en secuencia, aprobaciones, firmas y política, Opus y Fable, el revisor distinto, la prevalencia del encargo y la recuperación con la 4.14.
- **README:** solo cambian las líneas 1, 3, 7 y 17. `README.md:5` conserva «La base 4.14 completa sigue conservada en main».
- **Main:** 957af65 no es antecesor de `origin/main`, y `VERSION` de main es la 4.14.

## Hallazgos nuevos

### N1 · MENOR · «salvo decisión registrada» no dice de quién

- **Dónde:** `README.md:7`, «sin incorporar correcciones propias al código del producto salvo decisión registrada».
- **Problema:** la redacción es la que proponía la propia prueba de cierre de G3, así que no es un incumplimiento del autor. Pero frente a 957af65 («sin incorporar correcciones propias al producto», sin excepciones) abre una excepción sin decir de quién es la decisión. `INT:7` hace del coordinador el «único escritor del control común y único integrador del producto». Una lectura literal permitiría que el coordinador registre su propia decisión en CONTROL.json y con ella incorpore correcciones al código. Eso choca con «No inventar … política económica» (`CLAUDE.md:28`) y con la prevalencia del encargo de la persona responsable (`CLAUDE.md:35`).
- **Mitigación:** la misma línea exige la revisión de un contexto distinto (`INT:26`, `:31`).
- **Propuesta (no bloquea):** «salvo decisión registrada de la persona responsable». Se comprueba con `grep -n 'decisión registrada de la persona responsable' README.md`.

### N2 · OBSERVACIÓN · «integración técnica» no está en INTEGRACION.md

- **Dónde:** `CLAUDE.md:1`, `CLAUDE.md:37`, `README.md:1`, `README.md:7` y `note`.
- **Hecho:** `INT` no contiene «técnica» (rc=1). La expresión sale de `CONTROL.json:752` (T-CAND, «Candidata única de integración técnica») y concuerda con `H2:9` («Alcance: frente técnico») y con `VERSION:1` («corrección técnica»).
- **Valoración:** es una etiqueta descriptiva, no una instrucción, y no requiere cambio.

### N3 · OBSERVACIÓN (procedimiento, fuera del diff) · la solicitud de esta revisión no está registrada con todos sus campos

- **Hecho:** en `CONTROL.json`, `G-RAIZ.solicitud_revision` sigue con `sha_autor` = 3d66437 y estado `RESPONDIDA`. La nueva solicitud solo consta en `commit_origen` (`:711`), en `siguiente_accion` (`:722`) y en el registro (`:1466`).
- **Lo que falta:** la base, las rutas, los criterios y el revisor asignado de e813fe6, que `INT:26` exige.
- **Valoración:** no afecta al contenido del cambio. Antes de integrar, el coordinador debería registrar la solicitud de e813fe6 y apuntar a este informe.

## Límites

- Solo he comprobado los hechos contra los registros de 957af65 y contra el contrato del auxiliar. No he ejecutado baterías, pipeline ni LibreOffice. Las 190 pruebas y la reconstrucción de C48 se toman de `H2:99` y `H2:213-216`.
- No he verificado que INTEGRACION.md sea una decisión de la persona responsable más allá de lo que declara `INT:5`. G3 (a) queda cerrado como «contrato del programa», según lo admite el encargo.
- `next_action` pone la revisión externa del hito 2 en primer lugar, pero no condiciona la integración de documentación como esta a que esa revisión se haya hecho. Es coherente con `INT` y con el programa. Su orden lo decide la persona responsable, no esta revisión.
- La cifra «119 tests repetidos» no cambia y sigue sin fuente localizada en `docs/`. Queda fuera del alcance, como en la revisión anterior.
- Las gravedades (menor u observación) son mías. La revisión anterior la hizo otro contexto, y la acepto como referencia sin reabrir lo que dio por conforme.
- Las sondas llevan rutas locales por defecto, sobreescribibles con `REPO` y `AUX`. Son herramientas de la revisión, no forman parte del cambio, y sus salidas están anonimizadas.
