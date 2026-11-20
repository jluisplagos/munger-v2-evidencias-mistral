# Revisión independiente del borrador v2 del manual operativo (G-MANUAL) · `ef36ab1`

**Revisor:** agente distinto del autor del manual, de la candidata y del receptor de T-TRASPASO. Solo lectura. No se ha ejecutado LibreOffice, el pipeline, ningún control ni ninguna batería del producto. No se ha usado la red. No se ha modificado ningún repositorio ni worktree. Las únicas ejecuciones de código ajeno han sido `--help` de copias de `tools/base_414.py` y de `comprobar_registro.py` en una carpeta temporal, con `python3 -I -B`, y una pasada de huellas, de solo lectura, sobre el manifiesto del worktree de la candidata (sonda S12).

**Esta revisión no es una aprobación.** No acredita aptitud económica ni para dinero real. El producto sigue siendo experimental supervisado.

**Objeto revisado.** Repositorio auxiliar `<aux>`, commit `ef36ab18ff485e40dbb727b1b95eb177e5346683`:
- `coordinacion/cierre_v2/manual/MANUAL_OPERATIVO_3149128.md` (SHA-256 `894caa2e…c38a`, igual que su `MANIFIESTO_SHA256.txt`);
- `coordinacion/cierre_v2/manual/CAMBIOS_FRENTE_A_957af65.md` (`cc19014f…82bf`);
- `coordinacion/cierre_v2/manual/PROPUESTA_CONTINUIDAD_2_5.md` (`38cc5c0b…b744`).

`ef36ab1` solo añade esos tres archivos y el manifiesto sobre `6889b02` (sonda S01). La candidata es el worktree `<candidata>`, HEAD `31491289a9a13a670dd563c1b2df85dad54eb74a`, limpio (`git status --short` vacío). F1PREP se leyó en `03e7851`.

**Abreviaturas.** «Manual» = `MANUAL_OPERATIVO_3149128.md`; «CAMBIOS» = `CAMBIOS_FRENTE_A_957af65.md`; «Propuesta» = `PROPUESTA_CONTINUIDAD_2_5.md`. Las de rutas (`PV2/`, `E414/`, `TRASP/`, `REG/`, `REVT/`, `HERR/`, `F1PREP/`) son las del propio manual. `Sxx` = archivo de `sondas/`.

Convenciones: **hecho** (comprobado aquí, con su sonda), *interpretación* y ***propuesta***.

---

## 1. Veredicto por criterio

| # | Criterio | Veredicto | Motivo breve |
|---|---|---|---|
| 1 | Las siete mejoras de `MEJORAS_MANUAL.md`, con fuente correcta | **CONFORME_CON_LIMITES** | Las siete están aplicadas, con fuentes que existen y dicen lo citado. Límites: el espacio mínimo y el clonado siguen **[NO DOCUMENTADO]**, sin inventar nada, lo que es correcto. La corrección de §2.5 (C-14) solo mira el 4.8.1, pero el 4.8 también copia `_v64/` (hallazgo M1) |
| 2 | Ningún comando inventado; cada uno con su marca, contrastada con los registros | **CORRECCIONES** | No hay comandos inventados. Las marcas de «probado» no son siempre exactas: falta «autodeclarado» donde el registro no conserva el comando (M3). Además, varios comandos no llevan ninguna de las marcas del criterio y nadie los ha probado (M4) |
| 3 | Controles históricos sobre 4.15 | **CONFORME** | 4.10 39/44 por `.PARTES.txt`; 4.11 33/38 por el entorno, con el 4.12 miembro a miembro CUMPLE como lo vinculante; los otros 17, «observado una vez, no fijado». Todo cuadra con `REG/` y con el código |
| 4 | H9 abierto; I19/I20 no reintroducidos; sin política económica | **CONFORME** | H9 sigue abierto y sin procedimiento (N-08). I19 e I20 figuran como corregidos. No se elige ningún valor y no se declara aptitud. Una imprecisión menor en C-16 (m4) |
| 5 | Propuesta de CONTINUIDAD §2.5 exacta y sin aplicar | **CONFORME_CON_LIMITES** | Las dos frases actuales coinciden byte a byte con la candidata (una aparición cada una). Las frases nuevas y sus fuentes están indicadas, y no se aplica nada. Límites: la justificación omite el 4.8 (M1), dice «excluyendo solo» (m2) y una cita es ambigua (m8) |
| 6 | CAMBIOS cubre todas las diferencias v1 → v2 | **CORRECCIONES** | Cubre las mejoras y los cambios generales. No recoge varias supresiones ni algunos cambios (m1) |
| 7 | Sin rutas locales ni datos personales | **CONFORME_CON_LIMITES** | No hay rutas bajo `<home>`, ni correos, ni datos personales. Quedan `/tmp` como directorio temporal del sistema, un `/tmp/control481_…` citado del registro y `HOME=/root` citado del informe (m7) |

**Veredicto global: CORRECCIONES.** Ningún hallazgo es material. Hay cuatro medios (M1–M4) y doce menores (m1–m12). Ninguno cambia un resultado esperado del §5.2 ni del §5.3. Tampoco introducen política económica ni aptitud.

---

## 2. Hallazgos

### 2.1 Materiales

Ninguno.

### 2.2 Medios

**M1 · CONTINUIDAD §2.5 (C-14) es falsa también para el control 4.8, no solo para el 4.8.1.**
- **Dónde:** Manual:124, :125 (C-14), :311 («para los demás **[NO DOCUMENTADO]**») y :644 (fila C-14). Propuesta:5 («Por qué»), :21 (frase nueva) y :35 («de los demás no hay comprobación»).
- **Evidencia contraria (hecho, S06):**
  - `…_4_8/scripts/comprobar_entrega_4_8.py:60` copia `personaje_v2/` a un temporal (`:75`, `tempfile.mkdtemp(prefix="c48_")`). Solo excluye `empresas_v2`, `empresas_v2_correcciones`, `.lo_perfil`, `__pycache__` y `sintetico`, así que copia `pruebas/_v64/`. Borra el temporal al final (`:195`).
  - `…_4_9/scripts/comprobar_entrega_4_9.py:84` recorre todo el árbol con `os.walk(RAIZ)` sin excluir `_v64/`. *Interpretación:* no afecta al resultado, porque la variable `actuales` no se usa después (S06).
  - El 4.8 va antes que el 4.8.1 en `controles_historicos_4_13.py:39` y `:41`. En el traspaso, el 4.8 pasó y el 4.8.1 se quedó sin espacio.
  - *Interpretación:* el 4.8 copia una vez y el 4.8.1 lo hace en cuatro llamadas.
  - Por tanto, «los controles no recorren `_v64/`» es inexacto al menos para tres controles.
  - La alternativa del Manual:311 («pasada completa y, si el 4.8.1 falla, limpieza y repetición solo del 4.8.1») no prevé que el 4.8 pueda fallar por el mismo motivo con menos disco.
- **Prueba de cierre:**
  - ampliar C-14 y la Propuesta («Por qué», tabla de fuentes y «Qué no dice») con `comprobar_entrega_4_8.py:60`, `:75`, `:195`, y mencionar `comprobar_entrega_4_9.py:84` como recorrido sin efecto;
  - valorar que la frase nueva diga «antes de los controles de la 4.8 y la 4.8.1»;
  - en el Manual:311, prever la repetición del 4.8 si falla por espacio;
  - el revisor lo reproduce con `git grep -n -E 'copytree|os.walk' 3149128 -- '…/*/scripts/comprobar_*.py'` sobre los 19 controles de `controles_historicos_4_13.py:28-48`.

**M2 · Un «hecho» del §13 es falso: los binarios sí están en el worktree leído de la candidata.**
- **Dónde:** Manual:705, «el worktree leído de la candidata no tiene los binarios materializados (`git status` sin archivos sin seguimiento)». Relacionado: Manual:200 y la fila 5 del §10 (Manual:516), «83 JSON sin seguimiento en `git status`».
- **Evidencia contraria (hecho, S12):**
  - en `<candidata>/munger_v2_r1/`, las 7762 entradas de `MANIFIESTO_SHA256.txt` existen y coinciden: 7762 iguales, 0 ausentes;
  - `git status --short` da 0 líneas, pero `git status --short --ignored` da 682: los PDF están ignorados por `.gitignore:2` (`*.pdf`);
  - los 83 JSON están en `info/exclude` del directorio Git común (83 entradas);
  - *interpretación:* `git status` sin `--ignored` no sirve para saber si los binarios están, y que aparezcan los 83 JSON depende de que el clon no tenga una exclusión local.
- **Prueba de cierre:**
  - corregir la observación del §13: los binarios están, ignorados; los 83 JSON están excluidos en `info/exclude`;
  - en el §4.2.6 y la fila 5, decir que los 83 JSON solo aparecen como sin seguimiento en un clon sin exclusión local;
  - reproducir con `git status --short --ignored | wc -l` y con el contraste del manifiesto.

**M3 · Las marcas «probado en el traspaso» no siguen la regla del propio manual sobre *(autodeclarado)*.**
- **Dónde:** la regla está en Manual:12: «Si el registro no lo conserva y solo consta en el informe, se añade *(autodeclarado)*». Sin esa marca, aunque el registro no conserva el comando, en:
  - Manual:88 (las dos órdenes con `flock`);
  - Manual:155 (403 de `gh release download` en el traspaso);
  - Manual:196 (`copiar_binarios.py`: código «I», indirecto);
  - Manual:224 (`flock … completa`);
  - Manual:269 (`comprobar_entrega_4_14.py`: ni el comando ni el código 1 constan);
  - Manual:282 (`controles_historicos_4_13.py` con `flock`);
  - Manual:323 (`find … -delete` / `rm -rf`, que el informe abrevia con «…»).
- **Evidencia contraria (hecho, S07):**
  - el registro no conserva ninguna transcripción de comandos (`REVT/REVISION_TRASPASO.md:30`);
  - la tabla de respaldo da «—» o «I» en la columna Comando para todos los pasos (`REVT/REVISION_TRASPASO.md:54-75`);
  - el uso de `flock` en el paso 8 no consta (`:65`);
  - el código 1 del paso 9 no consta (`:66`);
  - el 403 no se conserva (`:57`).
  - Solo los resultados de los pasos 3, 5, 8, 9, 10, 10b y 12–14 están en `REG/`, y solo los códigos de 8 y 10 (`REG/paso8_exit.txt`, `REG/paso10_exit.txt`).
  - *Interpretación:* la marca se aplica en unos pasos (160, 167, 188, 219, 311, 476) y no en otros con el mismo respaldo. El lector no puede distinguir.
- **Prueba de cierre:**
  - añadir *(autodeclarado)* a todo «comando probado en el traspaso», o redefinir la marca como «comando autodeclarado; resultado y código en `REG/` cuando consten», con la columna que corresponda de `REVT/REVISION_TRASPASO.md:54-75`;
  - comprobarlo con `grep -n 'probado en el traspaso'` frente a esa tabla (S16).

**M4 · Varios comandos no llevan ninguna marca del criterio, y la categoría «literal de la fuente» contradice la propia definición de **[NO DOCUMENTADO]**.**
- **Dónde:** Manual:9 define **[NO DOCUMENTADO]** como «lo que el material no dice **o un comando que nadie ha probado**». Sin embargo, estos comandos no se probaron ni en el traspaso ni en F1:
  - sin marca: Manual:183 (`verify --git-only`), :230 (modo rápido), :354 (`verificacion_entradas.py plantilla`), :363 (`sellar`) y :366 (`comprobar`);
  - marcados solo como *literal de la fuente*: Manual:336 (`cambiar_base.py preparar`), :348 (`configuracion_economica.py validar`) y :374-375 (pipeline V6.4 y V6.4.1);
  - Manual:585-586 se presenta como «literal de `HERR/README.md:40-42`», pero adapta los nombres (`HERR/README.md:40-41` usa `lanzador.sh`, `"$REGISTRO"` y 26).
  - Manual:13 dice que la preparación F1 tiene «su comando y su código registrados». Para `copiar_binarios_a_b.py` no es así: `preparacion.json → paso4_worktree_B.copia_binarios` solo guarda el script y el recuento, no la orden ni el código (S07). El propio script sale siempre con 0 (Manual:198 lo dice).
- **Evidencia (hecho, S16 y S07):**
  - ninguno de esos comandos aparece en `TRASP/INFORME_TRASPASO.md:20-43` ni en `F1PREP/log_base414.txt` o `F1PREP/preparacion.json`;
  - sí existen en el producto con esa forma (`PV2/GUIA_RECORRIDO_SUPERVISADO.md:27`, `:37`, `:41`, `:102`, `:111`, `:116`; `README.md:51`; `verificar_paquete.sh:3`), así que **no son inventados**.
- **Prueba de cierre:** marcar cada uno como «*literal de la fuente*, no probado (ni en el traspaso ni en F1)», o como **[NO DOCUMENTADO]** según Manual:9. Corregir la marca de Manual:585 a «adaptado de» y matizar Manual:13. Un sondeo que liste todos los bloques y comandos en línea debe encontrar en cada uno una marca de las cuatro definidas.

### 2.3 Menores

| Id | Dónde | Evidencia contraria | Prueba de cierre propuesta |
|---|---|---|---|
| m1 | CAMBIOS §1–§2 (todo el documento) | El `diff` v1 → v2 (S10) da 476 líneas añadidas y 274 suprimidas. CAMBIOS no recoge que se quitaron: el comando `…_4_13/scripts/paso_pipeline.py CARPETA [--config …]` (v1:255; lo quitó G-DOCS de la guía); el comando completo de `empaquetar_cambios_4_15.py` (§8, sigue en `E415/hito2/HITO_2_4_15.md:187`); la frase «la línea de materialidad … sin umbral adoptado» (v1:282); el primer intento de la candidata interrumpido por un reinicio (v1:144); los modelos en `config_v2*.json` (v1:273); la referencia a I18–I21 (`INCIDENCIAS_4_14.md:144-182`); el mensaje 4.14 conservado en `E415/reproduccion/codigo_4_14/`; y las filas `PV2/ESTADO.md`, `PV2/DECISIONES.md` y `CONTROL.json` del §13. Tampoco recoge el cambio de la observación del entorno de lectura ni el de las filas 1, 6 y 19 del §10 | Añadir una sección «Supresiones» con cada una y su motivo. Un `diff -U0` no debe mostrar ningún bloque sin fila en CAMBIOS |
| m2 | Manual:124; Propuesta:5 | «excluyendo **solo** `empresas_v2`, `.lo_perfil` y `__pycache__`». `comprobar_entrega_4_8_1.py:77` excluye también todo `empresas_v2_correcciones` salvo `2026-11_Vidrala_ensayo_4_6_1` (S06) | Quitar «solo» o añadir la segunda exclusión |
| m3 | Manual:284 | «El script sale **siempre** con 0 (`:78`)». Sin argumento sale con 2 (`controles_historicos_4_13.py:52-54`) | «Con su argumento, sale siempre con 0» |
| m4 | Manual:448 y :646 (C-16) | Presenta la guía («no basta») frente al programa («pendiente de verificar»). La misma línea de la guía dice también «está pendiente de verificar por cambio afectado» (`PV2/GUIA_RECORRIDO_SUPERVISADO.md:141`, S15) | Decir que la tensión está dentro de `GUIA:141` («no basta» y «pendiente de verificar») y frente a `HITO_2_4_15.md:92` («habría que») |
| m5 | Manual:508 frente a :526 | Manual:508 incluye el paso 14 entre los pasos con código esperado distinto de 0, pero la fila 14 da «—» | Quitar el 14 de :508 o darle código esperado (10, observado en `REG/paso_h9_pipeline.txt`) |
| m6 | Manual:149-183 (§4.2.1–4) | Los pasos 1–4 se hacen en el clon de `main`, pero se citan líneas del `README.md` de `3149128`. El de `main` tiene 10 líneas menos al principio: `README.md:41` de la candidata es la línea 31 de `main` (S15). Los comandos son idénticos, y `tools/base_414.py` y `.gitignore` no cambian | Indicar que las citas son de `3149128` o dar también la línea de `origin/main` |
| m7 | Manual:81, :116, :119, :124, :574; CAMBIOS:13; Propuesta:21, :28, :30 | Criterio 7. `/tmp` aparece como temporal del sistema (lo dice el producto, `CONTINUIDAD.md:141`). `df -h <trabajo> /tmp` lo usa como argumento. `/tmp/control481_…` está citado del registro. `HOME=/root` está citado de `TRASP/INFORME_TRASPASO.md:10`. Ninguna es una ruta personal del autor. *Interpretación:* el temporal real depende de `TMPDIR` (`tempfile.mkdtemp`) | Escribir «el temporal del sistema (`$TMPDIR`, por defecto `/tmp`)», `df -h <trabajo> "${TMPDIR:-/tmp}"` y `<root>` en lugar de `/root` |
| m8 | Propuesta:52 | `INFORME_TRASPASO.md:33`, `:34`, `:78` sin prefijo. La Propuesta va a aplicarse al producto, donde existe otro `INFORME_TRASPASO.md` (`E414/documentacion_cierre_4_14/traspaso/`), cuyas líneas 33, 34 y 78 dicen otra cosa (S03) | Prefijar con `EVID/coordinacion/cierre_v2/traspaso/resultado_20261117/` |
| m9 | Manual:42; Propuesta:66 | «Ningún texto literal … aparece o desaparece» no explica el método. Aquí: barrido de las constantes de texto de 145 scripts. Con los cambios 1 y 2 de la Propuesta, 0 aparecen o desaparecen: **se confirma**. Entre `957af65` y `3149128`, en cambio, cambian 3 fragmentos (`'2. Adjuntar \`'`, `'código: '`, `'ambos'`). Ninguno se busca en `CONTINUIDAD.md`: son de `actualizar_documentos_version_4_13.py`, salidas impresas y argumentos (S04). La conclusión del manual se sostiene solo con ese filtro | Describir el sondeo (qué literales y con qué filtro) y conservar su script y su salida |
| m10 | Manual:689 | `E414/documentacion_cierre_4_14/INCIDENCIAS_4_14.md` figura en «Fuentes leídas», pero v2 ya no lo cita en ningún sitio (S10) | Quitarlo de la tabla o restituir la cita de I18–I21 |
| m11 | Manual:32, :24 | Las líneas de `CONTROL.json` son las de `6889b02`. La rama ya avanzó: en `HEAD` (`b257dfd` al cerrar esta revisión) `"head"` está en la 34 (no en la 31) y `revisor_propuesto` de G-MANUAL en la 589 (no en la 582). La 754, la 802, las 809-810 y la 833 siguen coincidiendo (S13). El manual ya prevé buscar el texto | Ninguna corrección obligatoria. ***Propuesta:*** citar `CONTROL.json` por id de tarea y campo («G-MANUAL → revisor_propuesto»), además de la línea |
| m12 | Manual:155 y :167 | «códigos 0/0» del §4.2.3 sale de `TRASP/INFORME_TRASPASO.md:24`, que da «0 / 0» para tres órdenes (`gh api`, `stat` y `sha256sum`) | Decir a qué orden corresponde cada código, o «0 en conjunto, autodeclarado» |

---

## 3. Lo que está conforme (hechos, con su sonda)

- **Integridad del objeto:**
  - `ef36ab1` solo añade los tres documentos y el manifiesto sobre `6889b02`;
  - las huellas coinciden con `manual/MANIFIESTO_SHA256.txt`;
  - `MANUAL_OPERATIVO_957af65.md` conserva `6ed65dce…`, la huella que usó el traspaso (S01).
- **Citas archivo:línea** (S02 y S03, comprobación automática de existencia y rango y lectura de cada línea): de las 603 citas del Manual, todas existen y están en rango. Las 24 que la herramienta no resuelve sola son contextuales (`…log:N`, `:N` de tabla, `resumen.md`) y se comprobaron aparte. Además:
  - los mínimos de `verificar_paquete.sh:95…323` (59, 27, 33, 190, 62, 5, 199, 78, 103, 55, 28, 45, 55);
  - el log `PRUEBAS/…:4-59`;
  - `LEEME_CONTROLES_HISTORICOS_4_14.md:15-43`;
  - `resumen.md:5-23`;
  - las líneas de `CONTROL.json` en `ef36ab1` (31-32 candidata, 582 G-MANUAL, 754 T-CAND, 802 T-CAMBIOS, 809-810 y 833 T-TRASPASO).
  - CAMBIOS (139 citas) y Propuesta (todas): sin problemas, salvo la ambigüedad m8.
- **Huellas del §13:** los 38 prefijos de la candidata, los 3 de EVID y los 3 de F1PREP coinciden. También coinciden las huellas completas de `lanzador_comun.sh` (`94f45a6e…`), `comprobar_registro.py` (`1ec39613…`) y `copiar_binarios.py` (`8fb5b9bc…`) (S08, S14).
- **Rutas, scripts y opciones nombrados:** existen en `3149128` los 22 archivos comprobados (configuraciones, scripts, `baselines/4.14*.json` y `tools/*`) (S08). También existen:
  - las opciones de `pipeline.py` (`--config`, `--agentes-simulados`, `--hasta`, `--reiniciar`, `--desde`);
  - `verificacion_entradas.py plantilla|comprobar|sellar --revisor --fecha`;
  - `configuracion_economica.py validar`;
  - `rellenar_fase1_v63.py --estricta` (código 7);
  - `base_414.py {verify,materialize} --source --git-only --report` (`--help`);
  - `comprobar_registro.py --esperados --json` (`--help`).
- **Mejoras 1–7** (criterio 1):
  - **Disco:** §3.2 separa lo documentado de lo observado, con las cifras autodeclaradas marcadas; §5.4 da la limpieza con registro de rutas y sin borrar el ZIP; los pasos 10a y 10b; C-14; N-16 como límite.
  - **Pasos 12–14:**
    - el aviso de `elis_motor_A` coincide con `REG/paso12_pipeline_01.txt:1-4` (fijado `9e1a725d…`, vigente `72f855cf…`, `SA-4bb…` sustituye a `SA-ed5561…`);
    - el paso 13 cambia `fase_c.md`, que sigue en el material refijado (`REVT/REVISION_TRASPASO.md:142-143`);
    - H9 se prueba con `fase_c.json`, `fase_b.json` o `entrada_efectiva.json`, y queda **[NO DOCUMENTADO]**;
    - el comando completo con `--config personaje_v2/config_v2.json` cuadra con `TRASP/INFORME_TRASPASO.md:36`.
  - **Controles históricos:** ver el criterio 3.
  - **`flock`:** una sola ruta, `<e_work>/libreoffice.lock`, que existe (S12); `soffice --version` con `flock`, marcado **[NO DOCUMENTADO]**.
  - **Registro del receptor:** la sintaxis, los códigos 0/1/2/3, la hora de fin, la regla del nombre sin espacios y el formato `RESULTADO 1 · pasos con código distinto de 0: …` coinciden con `HERR/lanzador_comun.sh:2-20` y `HERR/comprobar_registro.py:3-11`, `:25`, `:103-111`. La plantilla está marcada **[NO DOCUMENTADO]**.
  - **N-01, N-02, N-03 y N-11:** las atribuciones al traspaso o a F1 cuadran con `REG/paso5_copia_binarios.json` (1008·0·0·0), con `preparacion.json` (`tail -n +2 … | sha256sum -c --quiet`, código 0, 7004/7004) y con `log_base414.txt:2`, `:12`, `:14`, `:23` (0/0).
  - **Referencias:** las 13 esperas (hecho: 13, 4+4+5, S09); `python3`; 53 min 20 s (`REG/paso8_inicio.txt`, `REG/paso8_fin.txt`); `verify --report` (`tools/base_414.py:151`, `:159-160`).
- **Criterio 3:**
  - `4_10…txt:41` NO CUMPLE por la condición de `comprobar_entrega_4_10.py:181-182`; `.PARTES.txt` aparece 1 vez en `origin/main` y 0 en `957af65` y en `3149128`;
  - `4_11…txt:12` NO CUMPLE solo por la huella (`comprobar_entrega_4_11.py:126`), y `v6/` no cambia entre `589ce19` y `3149128` (0 archivos);
  - `4_12…txt:14` CUMPLE miembro a miembro (`comprobar_entrega_4_12.py:176-180`);
  - el 4.8.1 da 25/30 en el reintento (`REG/paso10b_4_8_1_reintento.txt:38`);
  - las otras 17 filas coinciden con `resumen.md` y con el LEEME 4.14 (S05).
- **Criterio 4:**
  - H9 «abierto, sin procedimiento» (Manual:441-447, N-08, paso 14 con comando **[NO DOCUMENTADO]**);
  - I19 e I20 «corregidos» (Manual:433 y :411; C-09 y C-13 resueltas, conforme a `CONTINUIDAD.md:196`, `:292`, `:356-357`);
  - ningún valor de R, θ, λ, probabilidades, k ni umbrales. La única `R=` es una variable de Bash de la plantilla (Manual:570);
  - «no apto para dinero real» en Manual:5, :48, :367, :411-413, CAMBIOS:5 y Propuesta:67.
- **Criterio 5:**
  - las dos frases actuales de la Propuesta están en `CONTINUIDAD.md:143` de `3149128`, byte a byte, una vez cada una (S04);
  - las fuentes de la tabla de la Propuesta existen y dicen lo citado (`comprobar_entrega_4_8_1.py:38`, `:73-77`, `:109`, `:125`, `:130`, `:184`, `:177-180`; `CAMBIOS_ARCHIVOS.txt:1`, `:81`; `CONTINUIDAD.md:384-386`);
  - no se aplica: `ef36ab1` no toca el producto y la candidata conserva la frase original;
  - el sondeo de literales de la Propuesta se reproduce: 0 cambios con los cambios 1 y 2 y con la variante.
- **Estado de C-01…C-16 y del §12.3:**
  - las resoluciones citadas existen (por ejemplo, C-04 → `CONTINUIDAD.md:391-395`; C-08 → `:376`; C-12 → `:199`);
  - las correspondencias G-1…G-9 y O-1…O-9 de `CONTRADICCIONES_GUIA.md` apuntan a líneas de `3149128` que tratan lo mismo (muestreo de todas las filas).

---

## 4. Límites de esta revisión

- No se ha ejecutado nada del producto: ni LibreOffice, ni el pipeline, ni controles, ni baterías. Las marcas de «probado» se contrastan solo con lo publicado en `TRASP/`, `REG/`, `REVT/`, `PRUEBAS/` y `F1PREP/`. Que un comando funcione hoy en otra máquina no se ha comprobado.
- La lectura semántica de las 603 citas del manual ha sido completa en las de comandos, resultados, mejoras, controles, H9 y propuesta. En las citas de contexto (§1, §2, §6, §8) se ha comprobado la existencia y el rango, y se ha leído la línea, sin un análisis exhaustivo de su matiz.
- `CONTRADICCIONES_GUIA.md` y el §12.3 se han revisado por muestreo de filas, no línea por línea.
- La comprobación de que el 4.8 y el 4.9 tocan `_v64/` (M1) es por lectura. No se ha medido el disco que usa el 4.8.
- La rama `coordinacion/cierre-v2` avanzó durante la revisión (`5efa898` → `b257dfd`) por trabajo de otra sesión. Aquí solo se revisa `ef36ab1`. Lo posterior no se ha leído salvo `CONTROL.json` (m11).
- El revisor es de la misma familia de modelo que el autor del manual. No vale como receptor sin historial de T-TRASPASO.
- No se ha revisado el contenido económico de ningún expediente.

## 5. Sondas

En `sondas/`, con las rutas locales sustituidas por `<aux>`, `<candidata>`, `<home>` y `<tmp>`:
- S01: identidad y huellas;
- S02 y S03: citas del Manual, de CAMBIOS y de la Propuesta, en resumen y en detalle;
- S04: literal de §2.5 y sondeo de literales;
- S05: controles históricos;
- S06: copias y recorridos de `_v64/`;
- S07: marcas de «probado» frente a los registros;
- S08: existencia de rutas, opciones y `--help`;
- S09: esperas;
- S10: `diff` v1 → v2;
- S11: rutas locales;
- S12: entorno de la candidata y bloqueo;
- S13: `CONTROL.json`;
- S14: huellas del §13;
- S15: guía, H9 y README;
- S16: marcas de origen.

Las herramientas están en `sondas/herramientas/`. Leen `CAND` y `AUX` del entorno.

## 6. Resumen

1. Veredicto global: **CORRECCIONES**. No hay hallazgos materiales. Hay 4 medios y 12 menores.
2. C1 CONFORME_CON_LIMITES: las siete mejoras están aplicadas y sus fuentes son correctas.
3. C2 CORRECCIONES: no hay comandos inventados, pero las marcas no son exactas.
4. M3: falta «autodeclarado» en 7 sitios donde el registro no conserva el comando.
5. M4: varios comandos no probados van sin marca o solo como «literal de la fuente».
6. C3 CONFORME: 4.10 39/44 por `.PARTES.txt` y 4.11 33/38 por el entorno, con el 4.12 CUMPLE miembro a miembro.
7. C4 CONFORME: H9 abierto y sin procedimiento; I19 e I20 no se reintroducen; no hay política económica ni aptitud.
8. C5 CONFORME_CON_LIMITES: las dos frases actuales coinciden byte a byte y no se aplica nada.
9. M1: el 4.8 también copia `_v64/` (`comprobar_entrega_4_8.py:60`), así que C-14 y la Propuesta están incompletas.
10. C6 CORRECCIONES: CAMBIOS omite varias supresiones, entre ellas `paso_pipeline.py`, el comando de empaquetado y filas del §13.
11. C7 CONFORME_CON_LIMITES: no hay rutas bajo `<home>` ni datos personales; quedan `/tmp` del sistema y `HOME=/root` citados.
12. M2: el §13 dice que el worktree no tiene los binarios; los tiene, ignorados (7762/7762 coinciden).
13. Las 603 citas del manual existen y están en rango; los 44 prefijos SHA-256 del §13 coinciden.
14. Las 13 esperas, 1008·0·0·0 y 53 min 20 s cuadran con los registros.
15. Límites: solo lectura, sin ejecutar controles; la rama auxiliar avanzó durante la revisión; el revisor es de la misma familia de modelo que el autor.
