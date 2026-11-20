# Revisión independiente de la v3 del manual operativo (G-MANUAL) · `MANUAL_OPERATIVO_3149128_v3.md`

**Revisor:** agente distinto del autor del manual, de la v2 y de su corrección. Revisión en español, **solo de lo afectado** por la corrección v2 → v3. Solo lectura: no se ha modificado ningún repositorio ni worktree, y solo se ha escrito en `<rev_manual_v3>/`. No se ha ejecutado LibreOffice, el pipeline, ningún control ni ninguna batería del producto. No se ha usado la red, salvo el `git pull --ff-only` pedido, que dio «Already up to date». Las únicas ejecuciones han sido de lectura:
- `git show`, `git diff`, `git status` (con y sin `--ignored`), `git check-ignore`, `grep`, `find`;
- `sha256sum -c` del manifiesto de la candidata;
- el script de sondeo del autor (`sondeo_literales_v3.py`, que solo hace `git show`), ejecutado con `python3 -I -B` desde otra carpeta;
- herramientas propias en `sondas/herramientas/`.

**Esta revisión no es una aprobación.** No acredita aptitud económica ni para dinero real. El producto sigue siendo experimental supervisado.

**Objeto revisado.** Repositorio auxiliar `<aux>`, rama `coordinacion/cierre-v2`:
- `coordinacion/cierre_v2/manual/MANUAL_OPERATIVO_3149128_v3.md` (SHA-256 `b0c34e9c…35eb`), escrito en `2f28dcd` y declarado final en `88144b5`, sin cambios después;
- `CAMBIOS_FRENTE_A_957af65.md` (§3 Supresiones, §4 y §5 v2→v3) y `PROPUESTA_CONTINUIDAD_2_5.md`, en `88144b5`;
- `sondeo_literales_v3/` (`34d56aab…` y `4d0bf6a0…`).

Las huellas coinciden con `manual/MANIFIESTO_SHA256.txt` (S01). Durante la revisión, la rama avanzó de `472a08e` a `a79e62d`, por trabajo de otra sesión. Ninguno de esos commits toca `manual/` ni `revisiones_coordinador/MANUAL_v2_ef36ab1/` (S01).

La v2 es `ef36ab1`, igual byte a byte que `MANUAL_OPERATIVO_3149128.md` en HEAD. La revisión de la v2 está en `<aux>/coordinacion/cierre_v2/revisiones_coordinador/MANUAL_v2_ef36ab1/`.

Candidata: worktree `<candidata>`.
- Al empezar, HEAD era `3149128`. Durante la revisión pasó a **`b129b36`** (integración de G-RAIZ, 13:46 UTC), que solo cambia `CLAUDE.md`, `README.md` y `docs/MIGRATION_STATUS.json` (S11).
- Todo lo del producto se ha leído con `git show 3149128:…`.
- Lo que se lee del disco (binarios, manifiesto e ignorados) está en `munger_v2_r1/`, que es idéntico en los dos commits (S03).

**Abreviaturas:** «v3» = el manual v3; «v3:N» = su línea N; «CAMBIOS» y «Propuesta», como en el manual; `Sxx` = archivo de `sondas/`. Se distinguen **hechos** (con su sonda), *interpretaciones* y ***propuestas***.

---

## 1. Veredicto por hallazgo de la revisión de la v2

| Hallazgo | Prueba de cierre pedida | Comprobación (hecho) | Veredicto |
|---|---|---|---|
| **M1** · el 4.8 también copia `_v64/` | C-14 y la Propuesta con `comprobar_entrega_4_8.py:60`, `:75`, `:195`; el 4.9 (`:84`) como recorrido sin efecto; frase «antes de los controles de la 4.8 y la 4.8.1»; Manual:311 prevé repetir el 4.8; `grep` sobre los 19 controles | En 3149128: `4_8.py:60` copytree de `P2` sin excluir `pruebas/`; `:54` `arbol_codigo_471`, llamada solo en `:82`; `:75` `mkdtemp(prefix="c48_")`; `:195` rmtree. `4_8_1.py:38`, `:73-77`, llamadas en `:109`, `:125` (bucle de dos), `:130`, y `:184`. `4_9.py:84`: `actuales` solo aparece en esa línea. 4.11 `:87`, 4.12 `:91` y 4.13 `:107` excluyen `_v64`; 4.13 `:55` solo recoge `__pycache__`. Los demás solo copian o recorren expedientes (4.4 `:157`, 4.7 `:111`, 4.7.1 `:142`, `:188`). El orden es `:39` (4.8) antes que `:41` (4.8.1); `resumen.md:15` da 32/36. Todo coincide con v3:129-136, 328-340, 343-345, 627, 651, 655 y 674, y con la Propuesta:9-14, 28, 34-36 y 43-45 (S02) | **CERRADO** |
| **M2** · los binarios sí están | Corregir el §13 y el §4.2.6 y la fila 5; reproducir con `--ignored` y con el manifiesto | `git status --short` da 0; con `--ignored`, 682 (591 archivos y 91 carpetas). Hay 71 PDF. `info/exclude` tiene 90 líneas: 7 comentarios y 83 rutas, iguales a los 83 JSON ignorados. Las 1008 rutas `release_asset` existen y están todas ignoradas. `tail -n +2 … \| sha256sum -c --quiet` da código 0 sobre 7762 entradas. Coincide con v3:214-217, 545 y 740-746 (S03) | **CERRADO** (residual trivial n7) |
| **M3** · *(autodeclarado)* | Añadirlo a todo «probado en el traspaso» o redefinir la marca; `grep` frente a `REVT/REVISION_TRASPASO.md:54-75` | 20 líneas con «probad… en el traspaso»; las 20 llevan «autodeclarado». La regla de v3:12 coincide con `REVT:30` («no conserva una transcripción»). Las precisiones de cada línea coinciden con su fila: códigos solo en 8 y 10, el 3 indirecto, `flock` no registrado en el 8, el código 1 del 9 no consta, el 403 no se conserva (S04) | **CERRADO** |
| **M4** · comandos sin marca | Marcar cada uno como «*literal de la fuente*, no probado» o **[NO DOCUMENTADO]**; Manual:585 como «adaptado de»; matizar Manual:13; sondeo de bloques y órdenes en línea | Los 24 bloques de comando (42 líneas) tienen marca en el párrafo anterior o en el siguiente. La herramienta señala otros 4 «sin marca» que son falsos positivos: texto sangrado de las propias marcas. La plantilla está marcada en v3:593. Las órdenes en línea `verify --git-only`, modo rápido, `plantilla` y `comprobar` llevan «literal de la fuente, no probado» (S05). v3:612 dice «*adaptado de* `HERR/README.md:40-41`», que usa `lanzador.sh`, `"$REGISTRO"` y 26 (S09b). v3:13 excluye `copiar_binarios_a_b.py`: `preparacion.json → paso4_worktree_B.copia_binarios` solo tiene `script`, `recuento`, `existentes_distintos` y `detalle` (S05) | **CERRADO**, con un residual menor (n1) |
| **m1** · supresiones | Sección «Supresiones»; ningún bloque del `diff -U0` sin fila | 80 bloques v1→v2; la tabla del §4 tiene 80 filas con las cabeceras exactas del `diff` (0 distintas). Cada bloque tiene al menos una fila (S12) | **CERRADO** (residual menor n4) |
| **m2** · «excluyendo solo» | Quitar «solo» o añadir la segunda exclusión | 0 apariciones en el manual y en la Propuesta. v3:130 y la Propuesta:10 añaden `empresas_v2_correcciones/` salvo `…_4_6_1` (`4_8_1.py:77`) (S13) | **CERRADO** |
| **m3** · «siempre con 0» | «Con su argumento, sale siempre con 0» | v3:301 lo dice así; `:52-54` `return 2`, `:78` `return 0`, `:82` `sys.exit(main())` (S13) | **CERRADO** |
| **m4** · C-16 | Tensión dentro de `GUIA:141` y frente a `HITO_2_4_15.md:92` | `GUIA:141` en 3149128 dice «no basta» y «pendiente de verificar»; `HITO_2:92` dice «habría que volver». v3:477 y v3:676 lo recogen (S13) | **CERRADO** |
| **m5** · paso 14 | Quitar el 14 de la lista o darle código 10 | Se quita el 14 (v3:537, v3:589). Ver §2.1: la propuesta alternativa de la revisión era errónea | **CERRADO** (residual menor n2) |
| **m6** · README frente a `main` | Indicar el commit de las citas o dar las de `origin/main` | v3:159: las siete equivalencias son de texto idéntico; `README.md:5` no está en `main`; `tools/base_414.py` y `.gitignore` sin `diff`; `origin/main` = `d69d483`; prefijo `d52f322a…` (S13) | **CERRADO** |
| **m7** · `/tmp` y `HOME` | `$TMPDIR`, `df -h <trabajo> "${TMPDIR:-/tmp}"`, `<root>` | Cada `/tmp` de los tres documentos y del sondeo va en la forma `${TMPDIR:-/tmp}` (0 excepciones). `HOME` = `<root>` (v3:86). La Propuesta:38 dice `control481_…` sin ruta (S10) | **CERRADO** (matiz menor n6) |
| **m8** · prefijos | Prefijar las fuentes `EVID/` de la Propuesta | Todas las citas de `INFORME_TRASPASO`, `REVISION_TRASPASO`, `MEJORAS_MANUAL`, `resumen.md` y `paso10b` llevan su ruta `EVID/…` completa, y la Propuesta:7 avisa del otro `INFORME_TRASPASO.md` del producto | **CERRADO** (residual trivial n9) |
| **m9** · método del sondeo | Describir el método y conservar el script y la salida | v3:42-47 y la Propuesta:79-83 describen los literales, la comparación y los filtros. Script y salida conservados con sus huellas. La salida se reproduce **idéntica** (S07 §1) | **CERRADO** |
| **m10** · INCIDENCIAS | Quitar la fila o restituir la cita | Restituida en v3:529 (`INCIDENCIAS_4_14.md:144-182`: I18 `:144`, I19 `:161`, I20 `:169`, I21 `:178`; 182 líneas; `bb141a50…`) (S13) | **CERRADO** |
| **m11** · `CONTROL.json` | (propuesta) por tarea y campo | En `acea175`: `candidata_integrada.head` 34 y `.estado` 35; `G-MANUAL.revisor_propuesto` 589; `T-CAND.siguiente_accion` 762, con la frase «ninguna batería lee esos documentos»; `T-CAMBIOS.siguiente_accion` 810; `T-TRASPASO` 817, 818 y 841. Cada línea está en el bloque de su tarea. Prefijo `a6e982a4…`. Entre `acea175` y `88144b5` no cambia nada de lo citado de `EVID/`, salvo `CONTROL.json` (S13) | **CERRADO** |
| **m12** · «0/0» | Repartir el código o «0 en conjunto, autodeclarado» | v3:174 y v3:181, conforme a `TRASP/INFORME_TRASPASO.md:24` (S13) | **CERRADO** |

**Además, hechos nuevos del §13 de la v3:**
- los prefijos nuevos (`INCIDENCIAS_4_14.md`, controles 4.8, 4.9, 4.11, 4.12 y 4.13, y `README.md` de `origin/main`) coinciden (S13);
- las huellas completas del sondeo coinciden;
- el bloqueo `<e_work>/libreoffice.lock` existe en esta máquina (comprobado con `ls`, sin abrirlo).

## 2. Las tres discrepancias del autor con la revisión de la v2

### 2.1 m5 · el código del paso 14 y `REG/paso_h9_pipeline.txt`: **tiene razón el autor**

**Hechos (S08):**
- En el traspaso, el paso 13 cambió `informe_provisional.md` (`REG/paso_p13_pipeline.txt:1`: «cambian: informe_provisional.md»). El paso 14 cambió `fase_c.md` (`REG/paso_h9_pipeline.txt:1`: «cambian: fase_c.md»).
- `TRASP/INFORME_TRASPASO.md:37-38` y `REVT/REVISION_TRASPASO.md:71-72` lo confirman.
- En el §10 de la v2 y de la v3:
  - la fila 13 es el ensayo con `fase_c.md`, con la fuente `REG/paso_h9_pipeline.txt:1-4`;
  - la fila 14 es el H9 con `fase_c.json`, `fase_b.json` o `entrada_efectiva.json`, que **no se ha ejecutado nunca**.

`paso_h9_pipeline.txt` respalda, por tanto, la fila 13, no la 14. Darle el código 10 a la 14, como sugería la revisión, habría asignado un resultado observado a un paso no ejecutado. Quitar el 14 es lo correcto.

**Matiz (menor, n2):** v3:537 dice «`REG/paso_h9_pipeline.txt` (código 10)». Ese archivo, de 4 líneas, no contiene el código. El 10 es autodeclarado: consta en `INFORME_TRASPASO.md:38` y `REVT:72` dice «no consta … el código». Basta con escribir «código 10, autodeclarado».

### 2.2 S-12 · `paso_pipeline.py` sigue en la guía: **tiene razón el autor**

**Hechos (S08):**
- La orden `…_4_13/scripts/paso_pipeline.py CARPETA [--config …]` «hace una pasada…» está en `GUIA_RECORRIDO_SUPERVISADO.md:34` de `957af65` y en **`:41` de `3149128`**.
- El script existe en `…_4_13/scripts/`.
- La revisión de la v2 (m1) decía «lo quitó G-DOCS de la guía»; es inexacto. G-DOCS solo movió la línea.

S-12 la registra como omisión de la v2, que ningún paso del §10 usa, y eso es correcto. *Interpretación:* la v3 cita `GUIA:41` para las órdenes V6.4 del §6.3 sin mencionar la tercera orden de esa línea. No es un error, porque S-12 lo explica.

### 2.3 Sondeo con `${TMPDIR:-/tmp}`: **tiene razón el autor**, con dos matices que no cambian la conclusión

**Hechos (S07):**
- **Reproducción.** El script del autor da código 0 y una salida idéntica a `salida.txt`. Con la Propuesta v3 aparecen 3 literales: `'$'`, `'TMP'` y `'TMPDIR'`. Con el filtro A (19 controles) y con el B (scripts que nombran CONTINUIDAD) salen 0.
- **Origen de los tres literales.** La Propuesta v2 da 0 literales nuevos, en el mismo universo ampliado del sondeo independiente (S07 §2). Los 3 salen solo del `${TMPDIR:-/tmp}` que pidió m7.
- **Sondeo independiente** (S07 §2), con universo ampliado: los 539 `*.py` y los 15 `*.sh` del árbol, 31855 literales.
  - Aparecen **4**: el cuarto es `':-'`, de una sonda de la revisión independiente del hito 2 (`…_4_15/revision_independiente/hito2/sondas4/c4_t4_documento.py:68`), que no lee CONTINUIDAD.
  - `'$'` está también en `…_4_9/auditoria_interna/material_vigencia/archivos_citados.py:21`, que nombra CONTINUIDAD. Pero ningún script ni control lo ejecuta (0 apariciones de `archivos_citados` en `*.py`/`*.sh`). Además, lee una ruta fija histórica y usa `'$'` solo para **saltar** los textos entre comillas invertidas que empiezan por `$`.
  - Con el filtro A sale 0.
- **Uso de CONTINUIDAD en los controles.** Todas las comprobaciones son de presencia (`x in cont`). No hay `re.*`, `.count` ni `.index` sobre su texto. La única restricción por sección es `comprobar_entrega_4_9.py:217` (`cont.split("## 3.")[0]`), que busca «45 de 49», «46 de 49» y «LEEME_BATERIAS_HISTORICAS.md». Ninguno de esos literales cambia con la Propuesta. Los cambios de número de apariciones (172) no afectan a ninguna comprobación, porque ningún control cuenta apariciones.

*Interpretación:* «0 relevantes» se sostiene. Que salgan 3 o 4 depende del universo, no de la conclusión. ***Propuesta*** (opcional): que la Propuesta:81-82 diga que el universo es el de los 145 scripts y que, en un universo completo, aparece además `':-'` y `'$'` coincide con `archivos_citados.py`, que no se ejecuta.

## 3. Hechos falsos, comandos sin marca y política económica (criterio 3)

- **Política económica:** ninguna línea nueva de la v3, de CAMBIOS ni de la Propuesta fija R, θ, λ, probabilidades, k, umbrales ni aptitud. La única mención de «mínimo» es «no fija un mínimo nuevo» (Propuesta:71) (búsqueda sobre el `diff`).
- **Comandos sin marca:** ninguno (S05; ver M4). Comandos nuevos de la v3:
  - la repetición del 4.8 (v3:338), **[NO DOCUMENTADO]**, *adaptado de* `controles_historicos_4_13.py:59`, con el bloqueo justificado por `4_8.py:91` y `:94`;
  - `df -h <trabajo> "${TMPDIR:-/tmp}"`, **[NO DOCUMENTADO]** (v3:610).
- **Citas:** se contrastaron las 165 citas `archivo:línea` de las 110 líneas que cambian (S09b, sobre el detalle de S09). Existen y dicen lo citado. Las no resueltas automáticamente son contextuales, como en la v2 (tabla del §5.2, columna del árbol 4.14). Una es ambigua de verdad (n5).
- **Hechos falsos introducidos por la v3:** ninguno sobre `3149128`. Hay hechos que **han dejado de ser ciertos** después de escribirla (N1), una afirmación desfasada en CAMBIOS (n3) y varias imprecisiones menores (§4).

## 4. Hallazgos nuevos

### 4.1 Medio (sobrevenido, no atribuible al autor)

**N1 · La rama candidata ya no apunta a `3149128`.**
- **Dónde:**
  - v3:198, «que hoy apunta a `3149128`»;
  - v3:544, fila 4: «HEAD `3149128`»;
  - v3:541, fila 1: «`README.md:1` y `CLAUDE.md:1` dicen “hito 1”»;
  - v3:661-662, C-01 y C-02 «Sigue»;
  - las citas de `CLAUDE.md` a partir de la línea 20 (`:22-26`, `:24`, `:28-31`, `:31`, `:35`, `:37`).
- **Evidencia (hecho, S11):**
  - `integracion/candidata-cierre-v2` (local y `origin`) = `b129b36`, de las 13:46:39 UTC, posterior a la v3 (`2f28dcd` 13:25 y `88144b5` 13:34);
  - `b129b36` cambia `README.md:1` («Candidata de integración técnica: 4.15, hito 2»), `CLAUDE.md:1`, `README.md:17` y `CLAUDE.md:10`, `:35`, y añade 2 líneas a `CLAUDE.md`. `:24` pasa a `:26`, `:28` a `:30`, `:31` a `:33`, `:35` a `:37` y `:37` a `:39`;
  - las líneas citadas de `README.md` no se mueven;
  - `munger_v2_r1/` no cambia y CONTINUIDAD §2.5 sigue con la frase original.
- *Interpretación:* un receptor que siga el §4.2.5 obtiene `b129b36`, no el HEAD que espera la fila 4. Las filas 1, C-01 y C-02 ya no describen la rama.
- **Prueba de cierre propuesta (*propuesta*):** una de dos.
  - Fijar el objeto: `git worktree add ../candidata 3149128`, o comprobar el SHA después, y decir que el manual describe `3149128`.
  - O hacer una v4 sobre `b129b36`, que actualice §0, §4.2.5, filas 1 y 4, C-01, C-02, las citas de `CLAUDE.md` y su prefijo SHA-256 en el §13.
  - En los dos casos, `grep -n '3149128\|hito 1' MANUAL…` debe cuadrar con `git -C <candidata> rev-parse integracion/candidata-cierre-v2`.

### 4.2 Menores

| Id | Dónde | Evidencia (hecho) | Prueba de cierre propuesta |
|---|---|---|---|
| n1 | v3:401, segunda orden del §6.3 (V6.4.1) | `GUIA:41` da la orden V6.4 completa y, para la V6.4.1, solo el fragmento `--config personaje_v2/config_v2_v641_experimental.json`. La línea es compuesta y se marca *literal de la fuente, no probado* («toma su `--config` de la misma línea»). Por la regla de v3:14, una orden «de una fuente con cambios» es **[NO DOCUMENTADO]**, *adaptado de* | Marcarla como *adaptada de* `:41` y **[NO DOCUMENTADO]**, o justificar en v3:9-14 que una composición dentro de la misma línea cuenta como literal |
| n2 | v3:537 | `REG/paso_h9_pipeline.txt` no contiene ningún código (4 líneas). El 10 es autodeclarado (`INFORME_TRASPASO.md:38`; `REVT:72`) (S08) | «(código 10, autodeclarado; el archivo muestra la espera)» |
| n3 | CAMBIOS:145 («No se ha cerrado aquí») | Dice que el `MANIFIESTO_SHA256.txt` de `manual/` no lista la v3 ni el sondeo y que las huellas han cambiado. En `88144b5` sí los lista y las 8 huellas coinciden (S01, S12) | Quitar la viñeta o decir que se rehízo en `88144b5` |
| n4 | CAMBIOS §4 (v1→v2) | «Si un bloque mezcla varios cambios, se dan todas sus filas» no se cumple siempre. La mejora **7d** (13 esperas: v2:456 y v2:523) no figura en los bloques 59 ni 64. **G-06** (N-12 por lectura: v2:269 y v2:618) no figura en los bloques 35 ni 69. 7d y G-06 no aparecen en ningún bloque. Cada bloque sí tiene al menos una fila: el criterio de m1 se cumple (S12) | Añadir 7d a los bloques 59 y 64 y G-06 a los 35 y 69, o rebajar la frase a «al menos una fila» |
| n5 | v3:45 | «…de una salida impresa (`:127`) y de un argumento (`:28`) de `reproducir_xa_xc.py`»: las dos citas van antes del nombre del archivo y justo después de `actualizar_documentos_version_4_13.py:94`, que tiene 115 líneas. Las líneas son de `reproducir_xa_xc.py` (`:127` `print(f"código: …")`; `:28` `default="ambos"`) (S09) | `reproducir_xa_xc.py:127` y `:28` |
| n6 | v3:121; Propuesta:28 y :36 | `tempfile.mkdtemp` consulta `TMPDIR`, `TEMP` y `TMP`, y después `/tmp`, `/var/tmp`, `/usr/tmp` y el directorio actual (biblioteca estándar de Python; *interpretación* del revisor, no ejecutado). `${TMPDIR:-/tmp}` es una simplificación. Además: v3:121 está bajo «Lo que documenta el producto», pero `CONTINUIDAD.md:141` dice «`/tmp`». Si se aplica la frase 1, `CONTINUIDAD:141` (`/tmp`) y `:143` (`${TMPDIR:-/tmp}`) quedan juntas con dos formas | Escribir «el temporal del sistema (`tempfile`: `TMPDIR`, `TEMP` o `TMP`; por defecto `/tmp`)», o decir que es una simplificación. En v3:121, distinguir la cita del producto (`/tmp`) de la precisión del manual. En la Propuesta, valorar ajustar también `:141` o avisar de la diferencia |
| n7 | v3:215 | Solo nombra los PDF y XLSX (`.gitignore:2-5`). Entre los 1008 hay también 6 PNG, 4 JPG y 1 ZIP, ignorados por `.gitignore:10`, `:11` y `:8` (843 xlsx + 83 json + 71 pdf + 6 + 4 + 1) (S03). No es falso | «Los PDF, XLSX, PNG, JPG y el ZIP… (`.gitignore:2-11`)» |
| n8 | v3:3 | Dice que «las únicas órdenes ejecutadas» son `git status`, el contraste del manifiesto y el sondeo. La v3:740-744 y el §5 de CAMBIOS usan además `find`, `git rev-parse`, `git show`, `git diff --stat`, `git ls-files` y `grep`, todas de lectura | «Solo órdenes de lectura (las del §13 y las del §5 de CAMBIOS)» |
| n9 | Propuesta:3 y :71 | `MANUAL_OPERATIVO_3149128_v3.md` sin ruta. Si la Propuesta se aplica al producto, ese archivo no está en él (es el espíritu de m8) | `EVID/coordinacion/cierre_v2/manual/MANUAL_OPERATIVO_3149128_v3.md` |

## 5. Propuesta §2.5 (criterio 4) y rutas locales (criterio 5)

**§2.5: CONFORME.**
- **Cubre el 4.8**, con su función, sus líneas (`:54-60`, `:75`, `:82`, `:195`), su resultado en el traspaso (32/36) y lo que no se ha observado: el resultado tras la limpieza, y si `reproducir_xa_xc.py` o `test_estados_v2.py` leen `_v64/`. Además, condiciona la frase: «la corrección documental lo comprueba antes … o la limita al 4.8.1».
- **Sigue sin aplicarse:** la frase 1 actual está una vez, y la nueva ninguna, en `3149128` y en `b129b36` (S06, S11).
- **Byte a byte:** las dos frases actuales de la Propuesta coinciden con `CONTINUIDAD.md:143` de `3149128`, una aparición cada una (194 y 61 bytes); también con `957af65`. Las cinco citas en bloque de la Propuesta son iguales, byte a byte, a las constantes `s1a`, `s1b`, `s2a`, `s2b` y `s2c` del script del sondeo (S06).
- Matices menores: n6 y n9.

**Rutas locales: CONFORME.**
- No hay rutas bajo `<home>`, ni de la sesión, ni de `/root`.
- Todo `/tmp` va como `${TMPDIR:-/tmp}`.
- `$HOME/e_work/…` es la variable genérica citada de `PROMPT_RECEPTOR.md:25`, y `HOME` = `<root>`.
- `salida.txt` usa `<candidata>` (S10).

## 6. Veredicto global

**CONFORME_CON_LIMITES** para la v3 como manual de `3149128`:
- **los 16 hallazgos de la revisión de la v2 (M1–M4 y m1–m12) quedan cerrados** según su prueba de cierre;
- en las tres discrepancias, el autor tiene razón;
- no hay hechos falsos sobre su objeto, comandos sin marca, política económica nueva ni rutas locales.

Los límites:
1. **N1**: la rama candidata avanzó a `b129b36` después de escribirse la v3. El manual **no se puede usar tal cual con la rama actual**: hay que fijar `3149128` o hacer una v4 (§4.1).
2. Nueve menores (n1–n9), ninguno de los cuales cambia un resultado esperado del §5.2, del §5.3 ni del §10.

## 7. Límites de esta revisión

- Solo se revisa lo afectado por la corrección v2 → v3: las 110 líneas nuevas o cambiadas de la v3, el §3, el §4 y el §5 de CAMBIOS, la Propuesta y el sondeo. El resto de la v3 se da por revisado en la revisión de la v2.
- No se ha ejecutado nada del producto. Las marcas de «probado» se contrastan solo con `TRASP/`, `REG/`, `REVT/` y `F1PREP/`.
- Los dos sondeos de literales son estáticos (constantes de texto y presencia en el texto). No prueban la lógica de cada control ni sustituyen a ejecutarlos.
- Que la limpieza de `_v64/` deje igual el resultado del 4.8, y el de los otros 17 controles, sigue sin observarse (N-16 y N-20 de la v3).
- Las líneas de `CONTROL.json` se comprobaron en `acea175`, como cita la v3. En HEAD (`a79e62d`) pueden haberse movido; no se han recalculado.
- Durante la revisión, el repositorio auxiliar y la candidata avanzaron por trabajo de otra sesión. El material revisado no cambió, salvo la rama candidata (N1).
- El revisor es de la misma familia de modelo que el autor. No vale como receptor de T-TRASPASO.
- No se ha revisado ningún contenido económico.

## 8. Sondas

En `sondas/`, con las rutas sustituidas por `<aux>`, `<candidata>`, `<home>`, `<root>` y `<tmp>`. Se regeneran con `CAND=<candidata> AUX=<aux> bash sondas/herramientas/generar_sondas.sh`.

| Sonda | Contenido |
|---|---|
| S01 | Identidad: commits, huellas del manifiesto de `manual/`, v2 = `ef36ab1`, `diff` v2→v3 (61 bloques, +110/−69) y estado de la candidata |
| S02 | M1: `copytree`, `os.walk` y `mkdtemp` en los 19 controles, y líneas citadas |
| S03 | M2: `--ignored`, PDF, `info/exclude`, los 1008 `release_asset` con su regla de exclusión, y el manifiesto |
| S04 | M3: 20 marcas «probado en el traspaso», 0 sin «autodeclarado», y `REVT:54-75` |
| S05 | M4: marcas de cada bloque de comando y órdenes en línea; datos de `F1PREP` |
| S06 | §2.5 byte a byte frente a la candidata y frente al script del sondeo |
| S07 | Reproducción del sondeo del autor; sondeo independiente con universo ampliado; uso de CONTINUIDAD en los controles |
| S08 | Discrepancias: m5 (pasos 13 y 14) y S-12 (`GUIA:41`) |
| S09 y S09b | Citas `archivo:línea`: resumen, detalle y las de las líneas cambiadas |
| S10 | Rutas locales |
| S11 | La candidata avanzada a `b129b36` (N1) |
| S12 | Correspondencia de bloques del `diff` en CAMBIOS (n4) y CAMBIOS:145 frente al manifiesto (n3) |
| S13 | Menores m2, m3, m4, m6, m10, m11 y m12, y prefijos nuevos del §13 |

Herramientas en `sondas/herramientas/`:
- `citas_v3.py`, adaptada de la de la revisión de la v2;
- `marcas_comandos.py`, `literal_2_5.py` y `sondeo_independiente.py`, propias;
- `generar_sondas.sh`.

## 9. Resumen

1. Veredicto global: CONFORME_CON_LIMITES para la v3 como manual de `3149128`. No es una aprobación ni acredita aptitud.
2. M1–M4 y m1–m12, cerrados según su prueba de cierre; las líneas citadas se comprobaron en `3149128`.
3. M1: solo el 4.8 (`:60`) y el 4.8.1 (`:76-77`) copian `_v64/`; el 4.9 (`:84`) lo recorre sin efecto.
4. M2: 682 ignorados, 71 PDF, 83 en `info/exclude`, 1008/1008 binarios y el manifiesto 7762 con código 0.
5. M3: 20 de 20 «probado en el traspaso» llevan «autodeclarado». M4: todos los comandos llevan marca.
6. m5: tiene razón el autor; `paso_h9_pipeline.txt` es el ensayo de `fase_c.md`, la fila 13 del §10.
7. S-12: tiene razón el autor; `paso_pipeline.py` sigue en `GUIA:41` de `3149128`.
8. Sondeo: tiene razón el autor; se reproduce idéntico, y el sondeo ampliado da 4 literales, 0 relevantes.
9. Propuesta §2.5: cubre el 4.8, no está aplicada y sus frases actuales coinciden byte a byte.
10. No hay política económica nueva, comandos sin marca ni rutas locales.
11. N1 (medio, sobrevenido): la candidata pasó a `b129b36` (G-RAIZ); hay que fijar `3149128` o hacer una v4.
12. Nueve menores (n1–n9), entre ellos la orden V6.4.1 compuesta, el «código 10» de `REG` y CAMBIOS:145 desfasado.
