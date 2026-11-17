# Manual operativo de Munger V2 · candidata `integracion/candidata-cierre-v2` @ b129b36 · BORRADOR (revisión 4)

**Estado de este documento:** borrador para revisión (tarea G-MANUAL), **revisión 4**. Sustituye, para la candidata `b129b36`, a `MANUAL_OPERATIVO_957af65.md`, a la revisión 2 (`MANUAL_OPERATIVO_3149128.md`, commit `ef36ab1`) y a la revisión 3 (`MANUAL_OPERATIVO_3149128_v3.md`, commit `88144b5`), que se conservan en Git. La revisión 2 aplicó las mejoras 1–7 de `REVT/MEJORAS_MANUAL.md`, que salieron de la prueba de traspaso del 17-nov (T-TRASPASO) y de su revisión independiente. La revisión 3 corrige los hallazgos medios M1–M4 y menores m1–m12 de la revisión independiente de la v2 (`EVID/coordinacion/cierre_v2/revisiones_coordinador/MANUAL_v2_ef36ab1/REVISION_MANUAL_v2_ef36ab1.md`, §2.2 y §2.3; lista en `CORRECCION_MANUAL_v3.md`, en la misma carpeta). La revisión 4 corrige el hallazgo medio N1 (la candidata pasó de `3149128` a `b129b36`) y los menores n1–n9 de la revisión independiente de la v3 (`EVID/coordinacion/cierre_v2/revisiones_coordinador/MANUAL_v3_88144b5/REVISION_MANUAL_v3.md`, §4), que la dio por CONFORME_CON_LIMITES como manual de `3149128`. No es un documento del producto, no está integrado y **esta revisión 4 no la ha revisado nadie distinto de quien la escribe**. Se ha preparado leyendo archivos: no se ha ejecutado ningún comando del producto, ni LibreOffice, ni el pipeline, ni la red (salvo `git pull --ff-only` y `git fetch` del repositorio de evidencias). Solo se han ejecutado órdenes de lectura: las del §13 de este manual (`git status`, `git rev-parse`, `find`, `wc` y el contraste del manifiesto sobre el worktree de la candidata), las del §5 y el §7 de `CAMBIOS_FRENTE_A_957af65.md` (`git show`, `git diff --stat`, `git ls-files`, `grep`, `sha256sum`) y el sondeo de literales (§0). Los cambios frente a la versión 1 y a las revisiones 2 y 3 están en `CAMBIOS_FRENTE_A_957af65.md`.

**Aptitud:** el producto es experimental supervisado y **no es apto para dinero real**. Este manual no adopta ninguna política económica ni ningún valor.

**Cómo leerlo.**
- Cada afirmación operativa lleva su fuente como `archivo:línea` (o un intervalo de líneas).
- **[NO DOCUMENTADO]** señala lo que el material no dice, o un comando que este borrador propone o adapta sin que conste probado. **[CONTRADICCIÓN]** señala dos fuentes incompatibles. Los dos se recopilan en el §12.
- **Origen de cada comando.** Cada comando lleva una de estas cuatro marcas:
  - *literal de la fuente*: copiado del documento o del script del producto que se cita. Si no consta ejecutado ni en el traspaso ni en la preparación F1, se escribe *literal de la fuente, no probado*: existe con esa forma en el producto, pero ninguna de las pruebas que cita este manual lo ha ejecutado;
  - **«comando probado en el traspaso del 17-nov» *(autodeclarado)***: lo ejecutó el receptor de T-TRASPASO sobre `957af65`. El registro no conserva ninguna transcripción de comandos (`REVT/REVISION_TRASPASO.md:30`): el comando consta solo en el informe, así que **esta marca lleva siempre *(autodeclarado)***. Junto a ella se dice qué hay en `REG/` según la columna que corresponda de `REVT/REVISION_TRASPASO.md:54-75`: el resultado, cuando consta, y el código, que solo consta en los pasos 8 y 10 (`REG/paso8_exit.txt`, `REG/paso10_exit.txt`);
  - **«comando probado en la preparación F1 del 15-nov»**: lo ejecutó la preparación del frente E (F1), fuera del traspaso, con su comando y su código registrados (`F1PREP/log_base414.txt`; `F1PREP/preparacion.json`). La copia de binarios con `copiar_binarios_a_b.py` **no cuenta**: de ella solo constan el script y el recuento, no la orden ni el código (`F1PREP/preparacion.json`, `paso4_worktree_B.copia_binarios`);
  - **[NO DOCUMENTADO]**: comando que propone este borrador y que no consta probado. Si sale de una fuente con cambios, se dice *adaptado de* esa fuente. No se ejecuta como si fuera un procedimiento validado.
- Los marcadores `<…>` son de la fuente o designan una ruta propia del receptor.

**Abreviaturas de rutas.** Las rutas son relativas a la raíz del repositorio del producto (`jluisplagos/munger-v2`, candidata en `b129b36`), salvo las que empiezan por `EVID/` o `F1PREP/`.

| Abreviatura | Ruta |
|---|---|
| `PV2/` | `munger_v2_r1/personaje_v2/` |
| `E414/` | `munger_v2_r1/personaje_v2/empresas_v2_correcciones/2026-11_Vidrala_ensayo_4_14/` |
| `E415/` | `munger_v2_r1/personaje_v2/empresas_v2_correcciones/2026-11_Vidrala_ensayo_4_15/` |
| `EVID/` | raíz del repositorio de evidencias `jluisplagos/munger-v2-evidencias-mistral`, **rama vigente `coordinacion/cierre-v2`**, leída en `acea175` (la v2 se escribió sobre `6889b02`; entre los dos, de lo que cita este manual solo cambia `CONTROL.json`). Lo que la v4 cita de la candidata vigente y de G-RAIZ se lee en `2c988b8` |
| `PRUEBAS/` | `EVID/coordinacion/cierre_v2/pruebas_candidata/957af65/` |
| `TRASP/` | `EVID/coordinacion/cierre_v2/traspaso/resultado_20261117/` |
| `REG/` | `TRASP/registro/` |
| `REVT/` | `EVID/coordinacion/cierre_v2/traspaso/revision_20261117/` |
| `HERR/` | `EVID/coordinacion/cierre_v2/herramientas/` |
| `F1PREP/` | repositorio del producto, rama `auditoria/economica-f1-frente-e` @ `03e7851`, carpeta `docs/validacion_economica_paralela/frente_E_F1_elis/evidencias/preparacion/` |

**Citas a `EVID/`.** Se citan en la rama vigente. Si la rama avanza y una línea se mueve, se busca el texto citado; no se usa el commit `9871f59` de la versión 1 de este manual, porque `CONTROL.json` cambió desde entonces (`REVT/REVISION_TRASPASO.md:216`). `CONTROL.json` es el archivo que más cambia: se cita por tarea y campo (por ejemplo, `CONTROL.json` → `T-CAND.siguiente_accion`), con la línea que tiene en `acea175`; las citas nuevas de la v4, con la línea que tiene en `2c988b8`.

---

## 0. Objeto: qué es `b129b36` y qué vale del traspaso

- **`b129b36` = `3149128` + G-RAIZ.** G-RAIZ cambia tres archivos de la raíz y ningún código: `CLAUDE.md`, `README.md` y `docs/MIGRATION_STATUS.json`, tomados de `e813fe6` (`git diff --stat 3149128 b129b36`; `EVID/coordinacion/cierre_v2/CONTROL.json` → `G-RAIZ.commit_origen` y `.commit_destino`, líneas 717-718 en `2c988b8`). Su revisión, por un contexto distinto del autor, es CONFORME_CON_LIMITES (`EVID/coordinacion/cierre_v2/revisiones_coordinador/G-RAIZ_e813fe6/REVISION_G-RAIZ_e813fe6.md`). La rama candidata apunta a `b129b36` (`CONTROL.json` → `versiones_fijadas.candidata` y `candidata_integrada`, líneas 11 y 30 en `2c988b8`; `git rev-parse integracion/candidata-cierre-v2` en el worktree leído, §13).
- **Ningún archivo de `munger_v2_r1/` cambia con G-RAIZ**: ni el código, ni el manifiesto, ni los documentos del paquete (las huellas del §13 son iguales en los dos commits, salvo las tres de la raíz). Donde este manual dice «en `3149128`» de un archivo de `munger_v2_r1/`, vale igual para `b129b36`. Las citas de `CLAUDE.md`, `README.md` y `docs/MIGRATION_STATUS.json` son las de `b129b36`.
- `3149128` = `957af65` + la corrección documental G-DOCS. Cambia cuatro archivos y ningún código: `munger_v2_r1/CAMBIOS_ARCHIVOS.txt`, `munger_v2_r1/CONTINUIDAD.md`, `munger_v2_r1/MANIFIESTO_SHA256.txt` y `PV2/GUIA_RECORRIDO_SUPERVISADO.md` (`git diff --stat 957af65 3149128`; `EVID/coordinacion/cierre_v2/CONTROL.json` → `candidata_integrada.head` y `.estado`, líneas 34-35 en `acea175`).
- El manifiesto sigue teniendo 7762 entradas, todas salvo él mismo (`munger_v2_r1/MANIFIESTO_SHA256.txt:1`).
- `VERSION` no cambia: «entrega 4.15 · hito 2» (`munger_v2_r1/VERSION:1`).
- **La prueba de traspaso se hizo sobre `957af65`** (`TRASP/INFORME_TRASPASO.md:1`; `TRASP/LEEME.md:8`). Como el código es el mismo, sus resultados de código valen para `3149128` y para `b129b36`. El coordinador registra que «ninguna batería lee esos documentos» (`EVID/coordinacion/cierre_v2/CONTROL.json` → `T-CAND.siguiente_accion`, línea 762 en `acea175`).
- Los controles históricos sí leen `CONTINUIDAD.md` (por ejemplo, `E414/../2026-11_Vidrala_ensayo_4_10/scripts/comprobar_entrega_4_10.py:176-180`). **Sondeo de literales de este borrador** (solo lectura con `git show`; script y salida en `EVID/coordinacion/cierre_v2/manual/sondeo_literales_v3/`, a partir de la herramienta `sondas/herramientas/sonda_literales.py` de la revisión de la v2):
  - *qué literales:* todas las constantes de texto (las `ast.Constant` de tipo `str`; en una f-string, cada trozo fijo) de los 145 scripts `*.py` de `personaje_v2/empresas_v2_correcciones/*/scripts/`, `personaje_v2/pruebas/` y `contrastes/*/scripts/` de `3149128` (iguales en `b129b36`): 13129 distintos;
  - *qué se mira:* cuáles están en el texto de `CONTINUIDAD.md` de un commit y no en el del otro;
  - *resultado sin filtro:* entre `957af65` y `3149128` cambian 3: `` '2. Adjuntar `' ``, `'código: '` y `'ambos'`. El primero es de `actualizar_documentos_version_4_13.py:94`, un script que reescribe documentos y que ningún control nombra; los otros dos, de una salida impresa (`reproducir_xa_xc.py:127`) y de un argumento (`reproducir_xa_xc.py:28`) de `E414/../2026-11_Vidrala_ensayo_4_8/scripts/reproducir_xa_xc.py`, que el control 4.8 ejecuta (`comprobar_entrega_4_8.py:84-85`) y que no nombra `CONTINUIDAD.md`;
  - *filtro:* constantes de los 19 controles que lanza `controles_historicos_4_13.py:28-48`. Con él, 0 aparecen o desaparecen.
  - *Interpretación:* por eso no se espera que cambie su última línea. La conclusión depende de ese filtro, y el sondeo no prueba la lógica de cada control. Sobre `3149128` y `b129b36` los controles **no se han ejecutado**.

## 1. Qué es y qué no es

- Munger V2 analiza empresas con una plantilla Excel (V6.3 y, solo con selección expresa, las V6.4 y V6.4.1 experimentales del motor B) y un personaje de juicio. Su pipeline tiene los pasos 0 a 14 y combina scripts deterministas con agentes (`munger_v2_r1/CONTINUIDAD.md:156`).
- **Versión:** entrega 4.15 · hito 2, la corrección técnica tras la revisión externa del hito 1 (`munger_v2_r1/VERSION:1`). Más las correcciones documentales G-DOCS y G-RAIZ (§0).
- **Aptitud:** uso supervisado y experimental. **No es apto para decisiones con dinero real** (`munger_v2_r1/VERSION:1`, `E415/hito2/HITO_2_4_15.md:8`, `CLAUDE.md:10`).
- Superar los controles de software no acredita aptitud (`E415/hito2/HITO_2_4_15.md:8`, `EVID/coordinacion/cierre_v2/PROGRAMA.md:5`, `PRUEBAS/README.md:26`).
- La verificación de las entradas es una condición necesaria, no suficiente (`munger_v2_r1/PROMPT_NUEVA_VENTANA.md:36-37`, `E415/HITO_1_4_15.md:299`).
- Un recorrido produce un **análisis experimental**. No es una decisión de inversión ni aprueba ningún parámetro (`PV2/GUIA_RECORRIDO_SUPERVISADO.md:5`). El resultado no se lee como una orden de compra o de venta (`PV2/GUIA_RECORRIDO_SUPERVISADO.md:95`).
- **No cerrado** en la candidata:
  - F1: el motor A no está validado. Su ancla f cuenta dos veces los arrendamientos NIIF 16 y los intangibles adquiridos (`E415/hito2/HITO_2_4_15.md:192-193`).
  - Los expedientes Viscofan, Vidrala y Elis no se han regenerado ni auditado con extractor y revisor reales. Sus registros siguen «no aptos por entradas» (`E415/hito2/HITO_2_4_15.md:194-196`).
  - H9, U1 y U6 (a), y los límites declarados (`E415/hito2/HITO_2_4_15.md:219-220`; `munger_v2_r1/CONTINUIDAD.md:356`).
  - El alcance original no está completado (`E414/documentacion_cierre_4_14/HITO_2.md:68-72`).
- Poder leer el repositorio no autoriza a declarar completa la migración ni a iniciar el pipeline financiero (`CLAUDE.md:8`). Ningún trabajo de alcance nuevo empieza sin encargo (`munger_v2_r1/CONTINUIDAD.md:361`).
- **Configuraciones económicas.** Las de demostración o de ensayo no están adoptadas (`munger_v2_r1/CONTINUIDAD.md:69-70`, `munger_v2_r1/CONTINUIDAD.md:74`). `configuracion_economica.json` «no es una adopción» (`PV2/GUIA_RECORRIDO_SUPERVISADO.md:10`). Ninguna convención de la V6.4 está adoptada (`munger_v2_r1/CONTINUIDAD.md:374`). Este manual no adopta ni propone ningún valor: ni R, θ, λ, probabilidades, k ni umbrales. Ningún agente los elige para desbloquear un caso (`EVID/coordinacion/cierre_v2/PROGRAMA.md:7`).

## 2. Reglas que rigen toda la operación

- Idioma: español claro, en tercera persona respecto de la persona responsable. Se distinguen hechos, interpretaciones y propuestas (`munger_v2_r1/PROMPT_NUEVA_VENTANA.md:32`).
- Modelos (`CLAUDE.md:30-33`, `munger_v2_r1/PROMPT_NUEVA_VENTANA.md:33-35`):
  - Opus, con esfuerzo alto, para la coordinación y la implementación.
  - Fable, con esfuerzo máximo, de forma selectiva, con aviso y registro.
  - La revisión la hace un agente distinto del autor del cambio.
- No se modifican originales, fuentes ni huellas para legitimar un resultado. No se reactivan aprobaciones retiradas, no se aceptan auditorías de material distinto y no se inventan firmas ni política económica (`CLAUDE.md:24-28`, `munger_v2_r1/PROMPT_NUEVA_VENTANA.md:38-40`).
- Se trabaja en ramas y expedientes nuevos. No se modifican `PV2/empresas_v2/` ni los expedientes anteriores (`munger_v2_r1/CONTINUIDAD.md:374`, `PV2/GUIA_RECORRIDO_SUPERVISADO.md:23`).
- La IA no confirma ceros ni rellena los campos humanos (`decision`, `fecha`, `confirmado_por`) (`munger_v2_r1/CONTINUIDAD.md:381`).
- Un resultado que no se ha ejecutado no se presenta como ejecutado (`munger_v2_r1/CONTINUIDAD.md:380`).
- **Qué instrucción manda en una prueba de traspaso** (mejora 7).
  - `AGENTS.md` del repositorio de evidencias prohíbe ejecutar LibreOffice y el pipeline. Va dirigido a los frentes del programa Mistral M2 (`EVID/AGENTS.md:1`, `EVID/AGENTS.md:7-15`).
  - `PROMPT_RECEPTOR.md` manda ejecutar LibreOffice en secuencia, con `flock -x` (`EVID/coordinacion/cierre_v2/traspaso/PROMPT_RECEPTOR.md:25`).
  - *Interpretación:* el receptor de T-TRASPASO no es un frente Mistral M2, así que para él rige `PROMPT_RECEPTOR.md`. Así lo hizo el receptor del 17-nov (`TRASP/INFORME_TRASPASO.md:88`). Un receptor que dude lo consulta al coordinador antes de ejecutar nada; no elige por su cuenta. La precedencia formal entre los dos textos **[NO DOCUMENTADO]**.

### 2.1 LibreOffice: siempre en secuencia, con un único bloqueo (mejora 4)

- Nunca dos tareas con LibreOffice a la vez: ni el pipeline, ni las baterías, ni los controles que recalculan. `comprobar_entorno.sh` también lo llama (`CLAUDE.md:26`, `munger_v2_r1/CONTINUIDAD.md:133`, `PV2/GUIA_RECORRIDO_SUPERVISADO.md:22`). En una máquina compartida hace falta exclusión mutua verificable, por ejemplo con `flock`, y perfiles aislados (`EVID/coordinacion/cierre_v2/INTEGRACION.md:41`).
- **Una sola ruta de bloqueo: `<e_work>/libreoffice.lock`.**
  - Es la que usó el receptor del traspaso. `<e_work>` sustituye en el registro al directorio de trabajo compartido de la máquina (`TRASP/INFORME_TRASPASO.md:10`; `TRASP/LEEME.md:10`).
  - **No** se usa `$HOME/e_work/libreoffice.lock`, la ruta por defecto de `PROMPT_RECEPTOR.md:25`: en el entorno del traspaso, `HOME` era el directorio personal del superusuario (`<root>`; `TRASP/INFORME_TRASPASO.md:10`) y esa ruta no es el bloqueo compartido (`TRASP/INFORME_TRASPASO.md:71`; `REVT/REVISION_TRASPASO.md:211`). Si dos sesiones usan archivos distintos, no hay exclusión mutua.
  - Hecho comprobado al escribir este borrador, y de nuevo al escribir la revisión 3: en la máquina del coordinador el archivo existe en `<e_work>/libreoffice.lock`, y `<e_work>` es la raíz de trabajo de la preparación F1 (`F1PREP/PREPARACION.md:3`). Que sea el bloqueo que comparten **todas** las sesiones lo confirma el coordinador antes de cada prueba: **[NO DOCUMENTADO]** en el producto.
- **Forma del comando.** Toda orden que pueda arrancar LibreOffice va precedida de `flock -x <e_work>/libreoffice.lock`. Comandos con esa forma probados en el traspaso, autodeclarados (`TRASP/INFORME_TRASPASO.md:31-36`):

      flock -x <e_work>/libreoffice.lock bash verificar_paquete.sh completa
      flock -x <e_work>/libreoffice.lock python3 -I -B personaje_v2/empresas_v2_correcciones/2026-11_Vidrala_ensayo_4_14/scripts/comprobar_entrega_4_14.py

  «comando probado en el traspaso del 17-nov» *(autodeclarado)*: son los pasos 8 y 9 (`TRASP/INFORME_TRASPASO.md:31-32`); el uso de `flock` no queda registrado (`REVT/REVISION_TRASPASO.md:65`); el código del paso 8 y los resultados de los dos están en `REG/` (§5.1, §5.3). Los demás del §10 siguen la misma forma.
- **También `soffice --version`.** El receptor lo ejecutó una vez sin `flock` para anotar la versión (desviación D-1, `TRASP/INFORME_TRASPASO.md:95`; `REVT/REVISION_TRASPASO.md:226-228`). Se hace así:

      flock -x <e_work>/libreoffice.lock soffice --version

  **[NO DOCUMENTADO]**: es la forma probada aplicada a la orden que ejecuta `comprobar_entorno.sh` (`PV2/scripts/comprobar_entorno.sh:7`), pero esta combinación no consta ejecutada.

## 3. Requisitos y comprobación del entorno

### 3.1 Requisitos

- Python 3.10 o posterior y GitHub CLI, para descargar la Release y materializar la base (`README.md:39`).
- **`python` frente a `python3`** (mejora 7). `README.md:42-43` usa `python`; el mensaje de arranque usa `python3 -I` (`munger_v2_r1/PROMPT_NUEVA_VENTANA.md:17`); los scripts del producto llaman a `python3` (`munger_v2_r1/verificar_paquete.sh:39`). El traspaso usó `python3` (`TRASP/INFORME_TRASPASO.md:25`) y la preparación F1, `python3 -I` (`F1PREP/log_base414.txt:2`, `F1PREP/log_base414.txt:14`). Este manual escribe `python3`. En el entorno del traspaso los dos nombres eran Python 3.13 (`TRASP/INFORME_TRASPASO.md:92`).
- Comprobados por `PV2/scripts/comprobar_entorno.sh`:
  - módulos de Python `openpyxl`, `lxml`, `pypdf` y `jsonschema` (`PV2/scripts/comprobar_entorno.sh:5-8`);
  - binarios `soffice` (LibreOffice) y `pdftotext` (`PV2/scripts/comprobar_entorno.sh:7`);
  - las rutas `plantilla.*` y `kit_v1.*` de la configuración activa: `MUNGER_CONFIG` o `config_v2.json` (`PV2/scripts/comprobar_entorno.sh:9-14`);
  - el autotest de `precio_de_si.py` (`PV2/scripts/comprobar_entorno.sh:20`).
  - El corpus Damodaran solo da AVISO si falta (`PV2/scripts/comprobar_entorno.sh:15-16`).
- Versiones registradas: Python 3.13.18, LibreOffice 24.2.7.2, pdftotext 24.02.0 y openpyxl 3.1.5, en las pruebas de la candidata (`PRUEBAS/README.md:4`) y en el traspaso, con Bash 5.2.21 (`TRASP/INFORME_TRASPASO.md:10`). Versiones mínimas de LibreOffice y de las bibliotecas **[NO DOCUMENTADO]**. La versión de zlib no se ha registrado en ningún entorno (§5.3, control 4.11).
- Para los recorridos reales hace falta una sesión que pueda lanzar agentes nuevos de contexto separado. Si no puede, se declara que la auditoría no es independiente (`munger_v2_r1/CONTINUIDAD.md:153`). La capacidad se comprueba con comandos, no por el nombre del modelo (`EVID/coordinacion/cierre_v2/PROGRAMA.md:13`). El comando para comprobarla **[NO DOCUMENTADO]**: el receptor del traspaso declaró que no podía, pero no lo comprobó con un comando (`REVT/REVISION_TRASPASO.md:152`).
- No se añaden credenciales al repositorio (`README.md:60`).

### 3.2 Disco (mejora 1)

- **Lo que documenta el producto** (medido en la 4.14, sobre un ZIP) (`munger_v2_r1/CONTINUIDAD.md:138-143`):
  - la descompresión ocupa unos 1,9 GB;
  - la verificación completa deja unos 1,7 GB en `PV2/pruebas/_v64/`;
  - el control de la 4.8.1 usa unos 2 GB temporales «en `/tmp`» (`munger_v2_r1/CONTINUIDAD.md:141`). *Precisión de este manual, no del producto:* los controles usan `tempfile.mkdtemp`, que toma `TMPDIR`, `TEMP` o `TMP` si están definidas y, si no, `/tmp` (y, si no puede, `/var/tmp`, `/usr/tmp` o la carpeta actual; biblioteca estándar de Python, `tempfile._candidate_tempdir_list`). Este manual lo abrevia como `${TMPDIR:-/tmp}`: es una simplificación del caso habitual;
  - conviene tener al menos 7 GB libres después de descomprimir.
- **Lo observado en el traspaso por la vía del repositorio** (sobre `957af65`, una sola vez; las cifras de espacio son autodeclaradas, porque no se registró ningún `df`: `REVT/REVISION_TRASPASO.md:67-68`):
  - **pico de ≈9,8 GB ocupados en la carpeta de trabajo**: clon de `main` con la base materializada, worktree de la candidata con los binarios, copia limpia y copia de relevos (`TRASP/INFORME_TRASPASO.md:78`; `REVT/REVISION_TRASPASO.md:267`). A eso se suma el temporal del control 4.8.1, en `${TMPDIR:-/tmp}`;
  - la copia limpia ocupaba 1,5 GB antes de verificar (`TRASP/INFORME_TRASPASO.md:29`);
  - el ZIP de la Release ocupa 1130912246 bytes (`README.md:33`);
  - con unos **8,4 GB libres** al empezar los controles históricos, el 4.8.1 se quedó sin espacio (`[Errno 28]`) (`TRASP/INFORME_TRASPASO.md:33`; `REG/paso10_controles_historicos/resumen.md:17`);
  - tras la limpieza del §5.4 quedaban unos **13 GB libres** y el 4.8.1 terminó (`TRASP/INFORME_TRASPASO.md:34`; `REG/paso10b_4_8_1_reintento.txt:38`).
- **Qué controles copian `pruebas/_v64/`** (lectura del código de los 19 controles de `controles_historicos_4_13.py:28-48`, buscando `copytree` y `os.walk`):
  - **4.8.1.** Copia `personaje_v2/` en `${TMPDIR:-/tmp}` (`tempfile.mkdtemp(prefix="control481_")`, `E414/../2026-11_Vidrala_ensayo_4_8_1/scripts/comprobar_entrega_4_8_1.py:38`). Excluye `empresas_v2`, `.lo_perfil` y `__pycache__` y, dentro de `empresas_v2_correcciones/`, todo salvo `2026-11_Vidrala_ensayo_4_6_1`; así que **copia también `pruebas/_v64/`** (`:76-77`). Lo hace en cuatro llamadas (`:109`, dos en el bucle de `:124-125` y `:130`) y no borra el temporal hasta el final (`:184`).
  - **4.8.** Copia `personaje_v2/` una vez, en `${TMPDIR:-/tmp}` (`tempfile.mkdtemp(prefix="c48_")`, `E414/../2026-11_Vidrala_ensayo_4_8/scripts/comprobar_entrega_4_8.py:75`). Excluye `empresas_v2`, `empresas_v2_correcciones`, `.lo_perfil`, `__pycache__` y `sintetico`, así que **también copia `pruebas/_v64/`** (`:60`, función `arbol_codigo_471`, llamada en `:82`). Borra el temporal al final (`:195`). En el traspaso, el 4.8 se ejecutó antes que el 4.8.1 (`controles_historicos_4_13.py:39`, `:41`) y no falló (32 de 36, `REG/paso10_controles_historicos/resumen.md:15`).
  - **4.9.** Recorre todo el árbol con `os.walk`, sin excluir `_v64/` (`E414/../2026-11_Vidrala_ensayo_4_9/scripts/comprobar_entrega_4_9.py:84`), pero el conjunto que obtiene (`actuales`) no se usa después: es un recorrido sin efecto en el resultado ni en el disco. El 4.13 también recorre el árbol entero en `comprobar_entrega_4_13.py:55`, pero solo recoge archivos de `__pycache__`.
  - Los demás no copian `_v64/`: el 4.11, el 4.12 y el 4.13 lo excluyen al recorrer el árbol (`comprobar_entrega_4_11.py:87`, `comprobar_entrega_4_12.py:91`, `comprobar_entrega_4_13.py:107`), y el resto solo copia o recorre carpetas de expedientes, o no usa esas funciones.
  - *Interpretación:* el 4.8 copia `_v64/` una vez y el 4.8.1 cuatro. Con menos disco libre, el 4.8 podría fallar por el mismo motivo. No se ha observado.
- **[CONTRADICCIÓN] del producto (C-14):** `munger_v2_r1/CONTINUIDAD.md:143` (§2.5) dice que «los controles no recorren `_v64/`». El 4.8.1 lo copia (`comprobar_entrega_4_8_1.py:76-77`), y por eso se quedó sin espacio (`REVT/REVISION_TRASPASO.md:197`). El 4.8 también lo copia (`comprobar_entrega_4_8.py:60`), y el 4.9 lo recorre sin efecto (`comprobar_entrega_4_9.py:84`). Para el resultado del 4.8.1 la frase es cierta (copia `_v64/`, pero no lo evalúa, `REVT/REVISION_TRASPASO.md:197`); para el del 4.8 no se ha comprobado; para el disco, no lo es en ninguno de los dos. **Este manual no corrige el producto:** el texto que se propondría está en `PROPUESTA_CONTINUIDAD_2_5.md`, para una corrección documental aparte.
- **Espacio mínimo por la vía del repositorio: [NO DOCUMENTADO].** Ninguna fuente lo fija. Este manual no inventa una cifra. Lo que hay son los hechos de arriba: con 8,4 GB libres falló el 4.8.1 y con 13 GB pasó. El receptor registra el espacio libre antes de los pasos 8 y 10 (§10.1) y aplica la limpieza del §5.4 antes de los controles históricos, que incluyen el 4.8 y el 4.8.1.

### 3.3 Comprobación

- En una sesión nueva, comprobar el acceso al repositorio, Python, LibreOffice y la descarga de la Release antes del pipeline (`README.md:58`).
- El comprobador es `PV2/scripts/comprobar_entorno.sh` (`README.md:58`). Se ejecuta desde `personaje_v2/` (`PV2/README_v2.md:24`, documento histórico). También es el paso 0 del pipeline (`PV2/scripts/comprobar_entorno.sh:2`) y el segundo bloque de `verificar_paquete.sh` (`munger_v2_r1/verificar_paquete.sh:65-69`).
  - Resultado esperado: código 0. Código 1 si falta algo (`PV2/scripts/comprobar_entorno.sh:2`).
  - **Llama a LibreOffice** (`soffice --version`, `PV2/scripts/comprobar_entorno.sh:7`): va con el bloqueo del §2.1.

## 4. Instalación y recuperación de los binarios

### 4.1 Principio

- La base histórica 4.14 tiene dos partes (`CLAUDE.md:7`, `README.md:13`):
  - 5790 archivos de texto en Git;
  - 1008 binarios, dentro del ZIP original de la Release `base-4.14`.
- **Las herramientas de recuperación son exclusivas de la base histórica 4.14** (`CLAUDE.md:39`). La verificación de la 4.14 no se aplica al código modificado de la 4.15. El árbol de la 4.15 se contrasta con el `MANIFIESTO_SHA256.txt` de su rama (`README.md:5`, `README.md:56`; `munger_v2_r1/CONTINUIDAD.md:109-112`; `PV2/GUIA_RECORRIDO_SUPERVISADO.md:16-18`).
- No se usan `base_414.py` ni `restore_assets_414.py` para una entrega posterior (`docs/RECEPCION_ENTREGA_CLAUDE.md:9`).
- La alternativa parcial (`baselines/4.14_assets.json`, `tools/restore_assets_414.py`) quedó sustituida por el ZIP completo (`README.md:62`, `CLAUDE.md:39`).
- `main` y el ZIP no se modifican (`munger_v2_r1/PROMPT_NUEVA_VENTANA.md:18`). La candidata no se sobrescribe con la base 4.14 (`EVID/coordinacion/cierre_v2/PROGRAMA.md:13`, `CLAUDE.md:37`).

### 4.2 Paso a paso (mejoras 6 y 7)

**Citas del `README.md` en los pasos 1–4.** Estos pasos se hacen en el clon de `main`, pero las líneas del `README.md` que se citan son las de `b129b36`, iguales que en `3149128` (G-RAIZ solo cambia `README.md:1`, `:3`, `:7` y `:17`, que no son de estos pasos). En `origin/main` (`d69d483`) el mismo texto está 10 líneas antes: `:33-35` → `:23-25`, `:39` → `:29`, `:41` → `:31`, `:42-43` → `:32-33`, `:45` → `:35`, `:46` → `:36` y `:51` → `:41` (`git show origin/main:README.md`). `README.md:5` solo está en la candidata. Los comandos son idénticos, y `tools/base_414.py` y `.gitignore` no cambian entre `origin/main` y `b129b36`.

1. **Clonar `main`** en una carpeta nueva y vacía (`EVID/coordinacion/cierre_v2/traspaso/PROMPT_RECEPTOR.md:17`). Recuperar y verificar allí los binarios (`README.md:5`, `munger_v2_r1/PROMPT_NUEVA_VENTANA.md:15-19`).
   - El comando de clonado **[NO DOCUMENTADO]**: el traspaso clonó `main` (`d69d483`) pero no registró la orden (`TRASP/INFORME_TRASPASO.md:18`).
2. **Descargar el ZIP** de la Release `base-4.14`, desde la raíz del clon. La orden del README es *literal de la fuente* (`README.md:41`):

       gh release download base-4.14 --repo jluisplagos/munger-v2 --pattern munger_v2_r1_entrega4.14_cierre_verificacion_entradas.zip --dir .downloads

   - **En una sesión de Claude Code falla** con el código 1 y un 403 («GitHub GraphQL is not available from Claude Code sessions»).
     - En el traspaso: «comando probado en el traspaso del 17-nov» *(autodeclarado)*; el código 1 y el 403 solo constan en el informe (`TRASP/INFORME_TRASPASO.md:23`; `REVT/REVISION_TRASPASO.md:57`).
     - En la preparación F1, con otro `--dir`: «comando probado en la preparación F1 del 15-nov», código 1 en los cuatro intentos (`F1PREP/preparacion.json`, `paso2_descarga.comando_indicado` y `.resultado_comando_indicado`).
   - Alternativa por la API REST (`munger_v2_r1/PROMPT_NUEVA_VENTANA.md:15-16`, `E415/hito2/PUNTO_DE_RECUPERACION.md:55-56`):

         gh api -H "Accept: application/octet-stream" repos/jluisplagos/munger-v2/releases/assets/750814858 > .downloads/munger_v2_r1_entrega4.14_cierre_verificacion_entradas.zip

     «comando probado en el traspaso del 17-nov» *(autodeclarado)*. El informe da «0 / 0» para tres órdenes juntas (esta descarga, `stat` y `sha256sum`, §4.2.3), sin decir a cuál corresponde cada código: **0 en conjunto, autodeclarado**. Duró 41 s (`TRASP/INFORME_TRASPASO.md:24`). Nada de esto está en `REG/` (`REVT/REVISION_TRASPASO.md:58`). También probado en la preparación F1, código 0 (`F1PREP/preparacion.json`, `paso2_descarga.codigo_salida_alternativa`). La redirección exige que `.downloads/` exista; cómo la creó el receptor **[NO DOCUMENTADO]**.
   - También vale la descarga manual (`README.md:45`). `.downloads/` está en el `.gitignore` de la raíz (`.gitignore:26`).
3. **Comprobar el ZIP** (`README.md:33-35`): 1130912246 bytes y SHA-256 `bb51942cefb848e409a4828e3faeb70f94aa4d29af39cda6d90cd0a97cb7b93e`. Comandos (N-11):

       stat -c '%s %n' .downloads/munger_v2_r1_entrega4.14_cierre_verificacion_entradas.zip
       sha256sum .downloads/munger_v2_r1_entrega4.14_cierre_verificacion_entradas.zip

   «comando probado en el traspaso del 17-nov» *(autodeclarado)*: **0 en conjunto con la descarga**, porque el «0 / 0» de `TRASP/INFORME_TRASPASO.md:24` cubre `gh api`, `stat` y `sha256sum` sin repartirse entre ellas. La huella solo consta en el informe (`REVT/REVISION_TRASPASO.md:58`). `sha256sum <zip>` es también la orden de la vía ZIP (`munger_v2_r1/CONTINUIDAD.md:114`).
   - **No borrar el ZIP** después de verificarlo. El receptor lo borró para ganar espacio (D-2), y la materialización ya no se puede repetir sin descargarlo otra vez (`REVT/REVISION_TRASPASO.md:235`).
4. **Materializar y verificar la base 4.14**, en el clon de `main`. Órdenes del README, *literal de la fuente* (`README.md:42-43`):

       python tools/base_414.py materialize --source .downloads/munger_v2_r1_entrega4.14_cierre_verificacion_entradas.zip
       python tools/base_414.py verify --report docs/VERIFICACION_BASE_COMPLETA_LOCAL.json

   - **`verify --report` escribe un JSON dentro del clon de `main`** (mejora 7). `--report` es opcional (`tools/base_414.py:151`) y escribe el informe en la ruta dada (`tools/base_414.py:159-160`). La de `README.md:43` deja `docs/VERIFICACION_BASE_COMPLETA_LOCAL.json` sin seguimiento en el clon: el `.gitignore` solo cubre `.downloads/` (`TRASP/INFORME_TRASPASO.md:72`; `REVT/REVISION_TRASPASO.md:218`). No modifica la rama `main`, pero sí el árbol local.
   - Variante con el informe **fuera del clon** (en la carpeta del registro del receptor):

         python3 -I tools/base_414.py materialize --source <zip>
         python3 -I tools/base_414.py verify --report <registro>/VERIFICACION_BASE_COMPLETA_LOCAL_414.json

     «comando probado en la preparación F1 del 15-nov», códigos 0/0 (`F1PREP/log_base414.txt:2`, `:12`, `:14`, `:23`). El traspaso usó la variante del README con `python3`: «comando probado en el traspaso del 17-nov» *(autodeclarado)*. Los resultados están en `REG/paso3_materialize.log` y `REG/paso3_verify.log`, y de ellos se deduce el código 0 por `tools/base_414.py:163` (`TRASP/INFORME_TRASPASO.md:25`; `REVT/REVISION_TRASPASO.md:59`).
   - **Esperado:** código 0, `complete: true` y 6798/6798, sin ningún archivo ausente o alterado (`README.md:46`, `munger_v2_r1/PROMPT_NUEVA_VENTANA.md:18`). Obtenido en el traspaso: 1008 recuperados; 6798/6798 (`REG/paso3_materialize.log`, `REG/paso3_verify.log`).
   - El script verifica todo el origen antes de escribir y no sobrescribe un archivo distinto (`tools/base_414.py:111`, `tools/base_414.py:123`). Su código de salida es 0 solo si `complete` es verdadero (`tools/base_414.py:163`).
   - Solo lo versionado en Git: `python tools/base_414.py verify --git-only` (*literal de la fuente, no probado*: `README.md:51`).
5. **Obtener la candidata** `integracion/candidata-cierre-v2`, que hoy apunta a `b129b36` (`EVID/coordinacion/cierre_v2/CONTROL.json` → `versiones_fijadas.candidata`, línea 11 en `2c988b8`; en `acea175` era `3149128`, `candidata_integrada.head`, línea 34). Desde la raíz del clon de `main`:

       git worktree add ../candidata integracion/candidata-cierre-v2

   «comando probado en el traspaso del 17-nov» *(autodeclarado)*: el comando, el código 0 y el HEAD solo constan en el informe (`TRASP/INFORME_TRASPASO.md:26`; `REVT/REVISION_TRASPASO.md:60`). Entonces daba `957af65`; hoy debe dar `b129b36`. El comando para comprobar el HEAD **[NO DOCUMENTADO]**.
   - El README describe otra vía: cambiar de rama en el mismo clon (`README.md:5`). Con un worktree aparte, la base 4.14 de `main` queda intacta para copiar sus binarios.
   - El mensaje de arranque nombra otra rama, la de trabajo del hito 2 (`munger_v2_r1/PROMPT_NUEVA_VENTANA.md:19`). CONTINUIDAD ya aclara que la candidata es `integracion/candidata-cierre-v2` (`munger_v2_r1/CONTINUIDAD.md:6`). **[CONTRADICCIÓN]** C-03, ahora parcial.
6. **Copiar los 1008 binarios** `release_asset` de la base materializada a la candidata, sin sobrescribir ninguno (N-01). Desde la carpeta de trabajo:

       python3 -I <copia_de>/copiar_binarios.py <clon_de_main> <worktree_candidata> <registro>/paso5_copia_binarios.json

   - Script: `TRASP/scripts_receptor/copiar_binarios.py` (SHA-256 `8fb5b9bcfd242743c5d2c778215ba5961458bf781150d274332eed1d5af1735d`, `TRASP/INFORME_TRASPASO.md:125`). Uso en `TRASP/scripts_receptor/copiar_binarios.py:7`.
   - «comando probado en el traspaso del 17-nov» *(autodeclarado)*: el comando y el código 0 solo constan en el informe (`TRASP/INFORME_TRASPASO.md:27`). El resultado, 1008 copiados · 0 existentes iguales · 0 distintos · 0 fallos, está en `REG/paso5_copia_binarios.json`, y el script está publicado (`REVT/REVISION_TRASPASO.md:61`: «Comando» «— (script R)», «Código» I). El revisor lo dio por correcto: no sobrescribe y comprueba la huella antes y después; sus 1008 rutas son las de las pruebas de la candidata (`REVT/REVISION_TRASPASO.md:61`).
   - Lee `baselines/4.14.json`, toma `storage == release_asset` y antepone `archive_prefix` (`copiar_binarios.py:26-32`). Sale con 1 si hay fallos o binarios distintos (`copiar_binarios.py:52`), así que su código sirve para el registro del §10.1.
   - Alternativa: `F1PREP/scripts/copiar_binarios_a_b.py` (uso `python3 -I copiar_binarios_a_b.py <baseline.json> <A/munger_v2_r1> <B/munger_v2_r1> <salida.json>`, *literal de la fuente*: `copiar_binarios_a_b.py:2`). La preparación F1 del 15-nov lo usó sobre el árbol del hito 1, con 1008·0·0·0·0 (`F1PREP/copia_binarios_A_a_B.json`; `F1PREP/PREPARACION.md:10`), pero **no registró la orden ni el código**: `F1PREP/preparacion.json` → `paso4_worktree_B.copia_binarios` solo guarda el script y el recuento. Por eso no lleva la marca «probado en la preparación F1». **No informa del resultado por su código de salida**: no llama a `sys.exit` (`copiar_binarios_a_b.py:38-41`), así que sale con 0 aunque haya fallos. Para el registro del §10.1 se prefiere `copiar_binarios.py`.
   - **Si un binario de la 4.14 ya existe distinto en la candidata:** ninguno de los dos scripts lo sobrescribe; lo listan como «distintos». Qué hacer entonces **[NO DOCUMENTADO]**: el receptor se detiene y lo comunica. En la candidata no ocurre (0 distintos).
   - Después, **en un clon sin exclusión local**, `git status` en la candidata muestra 83 JSON sin seguimiento: son binarios de la 4.14 que el `.gitignore` no cubre. Están en el manifiesto y no se versionan (`PRUEBAS/README.md:12`, `E415/hito2/HITO_2_4_15.md:21`; observado en el traspaso, sin registro: `REVT/REVISION_TRASPASO.md:61`).
     - Los demás binarios copiados no aparecen, porque los cubre el `.gitignore`: 843 XLSX y 71 PDF (`.gitignore:2-5`), 1 ZIP (`:8`), 6 PNG (`:10`) y 4 JPG (`:11`). Con los 83 JSON suman los 1008 (`baselines/4.14.json`, `storage == release_asset`).
     - Si el directorio Git común tiene esas 83 rutas en `info/exclude`, como el clon que leyó este borrador (§13), `git status --short` sale vacío aunque los 1008 binarios estén.
     - Por tanto, **`git status` sin `--ignored` no sirve para saber si los binarios están**: para eso está el contraste con el manifiesto (paso 7).
7. **Verificar con el manifiesto propio de la candidata** (N-02).
   - `munger_v2_r1/MANIFIESTO_SHA256.txt` tiene 7762 entradas, todas salvo él mismo, y una línea 1 de cabecera (`munger_v2_r1/MANIFIESTO_SHA256.txt:1`).
   - La comprobación del producto es el primer bloque de `verificar_paquete.sh`, antes de las pruebas (`munger_v2_r1/verificar_paquete.sh:28-29`, `:38-63`). Cuenta modificados, ausentes **y de más** (`:53-56`).
   - Comprobación independiente, desde `munger_v2_r1/` del worktree de la candidata:

         tail -n +2 MANIFIESTO_SHA256.txt | sha256sum -c --quiet

     «comando probado en la preparación F1 del 15-nov», código 0, sobre el manifiesto del hito 1 (7004/7004) (`F1PREP/preparacion.json`, `paso4_worktree_B.manifiesto_B`). **No consta en el traspaso:** allí el contraste se hizo con un Python propio que no se conservó (paso 7b; `TRASP/INFORME_TRASPASO.md:30`; `REVT/REVISION_TRASPASO.md:64`). Límite: `sha256sum -c` no detecta los archivos **de más**. Cómo los contó la preparación F1 **[NO DOCUMENTADO]** (solo constan sus listas, `F1PREP/preparacion.json`, `manifiesto_B.listas`).
   - Esperado: 7762 · 0 modificados · 0 ausentes · 0 de más (`PRUEBAS/README.md:11`; `TRASP/INFORME_TRASPASO.md:30`, sobre `957af65`).

## 5. Verificación del paquete y resultados esperados

### 5.1 Cómo

- **Sobre una copia limpia** de `munger_v2_r1/`, sin `personaje_v2/.lo_perfil/` ni `__pycache__` (`munger_v2_r1/PROMPT_NUEVA_VENTANA.md:22`). Comando (N-03), desde la carpeta de trabajo:

      mkdir copia_limpia_1 && cp -a candidata/munger_v2_r1 copia_limpia_1/

  «comando probado en el traspaso del 17-nov» *(autodeclarado)*: el comando, el código 0 y «0 `__pycache__` y 0 `.lo_perfil`» solo constan en el informe (`TRASP/INFORME_TRASPASO.md:29`; `REVT/REVISION_TRASPASO.md:63`). `cp -a` conserva las fechas del checkout, que aparecen en el control 4.14 (`REVT/REVISION_TRASPASO.md:121`).
- Ejecutar desde la raíz `munger_v2_r1/` de la copia, con el bloqueo del §2.1 (`munger_v2_r1/verificar_paquete.sh:2-4`, `munger_v2_r1/CONTINUIDAD.md:115`):

      flock -x <e_work>/libreoffice.lock bash verificar_paquete.sh completa

  «comando probado en el traspaso del 17-nov» *(autodeclarado)*: el uso de `flock` no queda registrado (`REVT/REVISION_TRASPASO.md:65`). El código 0 está en `REG/paso8_exit.txt`; las horas, en `REG/paso8_inicio.txt` y `REG/paso8_fin.txt`.
- **Una sola vez por carpeta.** Las pruebas escriben dentro del árbol (`PV2/pruebas/`, `PV2/.lo_perfil/` y `.pyc`) y fuera (temporales y `~/.cache` de LibreOffice). Para repetir, hace falta una copia nueva (`munger_v2_r1/CONTINUIDAD.md:137`, `munger_v2_r1/verificar_paquete.sh:28-29`).
- **Duración** (mejora 7): **53–60 min en la 4.15**.
  - Traspaso: de 08:44:07 a 09:37:27 UTC, 53 min 20 s (`REG/paso8_inicio.txt`, `REG/paso8_fin.txt`).
  - Pruebas de la candidata: de 22:18 a 23:18 UTC (`PRUEBAS/README.md:21`). La guía corregida da «60 min en la verificación de la candidata 4.15 · hito 2» (`PV2/GUIA_RECORRIDO_SUPERVISADO.md:19`).
  - **[CONTRADICCIÓN]** C-11: `munger_v2_r1/CONTINUIDAD.md:115` sigue diciendo «unos 25–45 minutos».
- **Modo rápido** (`bash verificar_paquete.sh`, sin `completa`; *literal de la fuente, no probado*): manifiesto, entorno, piloto y `test_comprobadores.py` (`munger_v2_r1/verificar_paquete.sh:3`). Su PASA solo cubre lo que lista (`munger_v2_r1/verificar_paquete.sh:26`). Ningún modo sustituye a los controles de los expedientes reales ni a sus auditorías (`munger_v2_r1/verificar_paquete.sh:27`).

### 5.2 Resultado esperado de `completa`

- Valores de referencia: `munger_v2_r1/PROMPT_NUEVA_VENTANA.md:23-26`, `munger_v2_r1/CONTINUIDAD.md:116-131` y `E415/hito2/PUNTO_DE_RECUPERACION.md:10-13`.
- Obtenido sobre `957af65`, con código 0, dos veces: en las pruebas de la candidata (`PRUEBAS/verificar_paquete_completa.log:4-59`) y en el traspaso, con un registro **idéntico byte a byte** (SHA-256 `23fd7aa1b452df49e05ca38e9307f5492199ae0494f0e617bf70a308cedb54d4`, `REVT/REVISION_TRASPASO.md:107`). Sobre `3149128` y `b129b36` no se ha ejecutado; el código es el mismo (§0).

| Bloque | Esperado | Mínimo exigido | Obtenido en 957af65 |
|---|---|---|---|
| Manifiesto | 0 modificados · 0 ausentes · 0 de más | — | 7762 · 0 · 0 · 0 (`PRUEBAS/verificar_paquete_completa.log:4-5`) |
| Entorno | PASA | — | PASA (`…log:7-8`) |
| Piloto Vidrala 2025 | 35 CUMPLEN, salida idéntica a la de referencia | — | PASA (`…log:10-11`) |
| `test_comprobadores.py` | 114/114 | — | 114/114 (`…log:14`) |
| `test_pipeline_sintetico.py` | 30/30, con los nombres de la línea de base v2.2 | — | 30/30 · faltan 0 · nuevas 0 (`…log:16-19`) |
| Vigencia H5 | 59/59 | 59 (`verificar_paquete.sh:95`) | 59/59 |
| Juicio sobre el objetivo | 27/27 | 27 (`:114`) | 27/27 |
| Entradas 4.14 | 33/33 | 33 (`:133`) | 33/33 |
| Entradas 4.15 | 190/190 | 190 (`:152`) | 190/190 |
| Entrada efectiva | 62/62 | 62 (`:171`) | 62/62 |
| Relevo caducado (LibreOffice) | 5/5 | 5 (`:190`) | 5/5 |
| Integración V6.4 | 199/199 | 199 (`:209`) | 199/199 |
| Trazabilidad | 78/78 | 78 (`:228`) | 78/78 |
| Integridad de la auditoría | 103/103 | 103 (`:247`) | 103/103 |
| Solicitudes de auditoría | 55/55 | 55 (`:266`) | 55/55 |
| Estados | 28/28 | 28 (`:285`) | 28/28 |
| Resumen | 45/45 | 45 (`:304`) | 45/45 |
| Cierre | 55/55 | 55 (`:323`) | 55/55 |
| **Global** | `RESULTADO GLOBAL: PASA`, código 0 | — | PASA (`…log:59`; `PRUEBAS/README.md:21`; `REG/paso8_exit.txt`) |

- En «completa», las quince baterías son obligatorias. Si una falla, no se ejecuta o tiene menos pruebas que el mínimo, el resultado es FALLA (`munger_v2_r1/CONTINUIDAD.md:135`, `munger_v2_r1/verificar_paquete.sh:332-333`). Las trece que siguen a la sintética solo se ejecutan en «completa» (`munger_v2_r1/CONTINUIDAD.md:135`).
- Usan LibreOffice: `test_comprobadores.py`, la sintética, `test_integracion_v64.py`, `test_estados_v2.py`, `test_cierre_v2.py`, `test_resumen_v2.py` (`munger_v2_r1/CONTINUIDAD.md:133`) y `test_relevo_i19_415.py` (`munger_v2_r1/verificar_paquete.sh:24-25`, `PV2/pruebas/test_relevo_i19_415.py:10`).

### 5.3 Después, sobre la misma copia: control de la 4.14 y controles históricos (mejora 3)

**Control de la 4.14.**
- Comando (`munger_v2_r1/CONTINUIDAD.md:136`), desde `munger_v2_r1/` de la copia limpia:

      flock -x <e_work>/libreoffice.lock python3 -I -B personaje_v2/empresas_v2_correcciones/2026-11_Vidrala_ensayo_4_14/scripts/comprobar_entrega_4_14.py

  «comando probado en el traspaso del 17-nov» *(autodeclarado)*: ni el comando ni el código 1 constan en el registro; el resultado, 29/35, sí (`REG/paso9_comprobar_entrega_4_14.log:36`; `TRASP/INFORME_TRASPASO.md:32`; `REVT/REVISION_TRASPASO.md:66`). Por lectura, no llama a LibreOffice: no usa `subprocess` ni `soffice` (`REVT/REVISION_TRASPASO.md:122`). Ir con el bloqueo es prudencia, no requisito (N-12, cerrado por lectura).
- **Esperado sobre un clon Git: 29/35, código 1** (`munger_v2_r1/CONTINUIDAD.md:136`, `E415/hito2/HITO_2_4_15.md:122-123`). Obtenido dos veces: `PRUEBAS/comprobar_entrega_4_14.log:36` y `REG/paso9_comprobar_entrega_4_14.log:36`. Las seis FALLA esperadas:
  - tres verificaciones de las entradas de los expedientes finales de la 4.14 («0 de 321», «0 de 311» y «0 de 292»), «no apto por entradas» por diseño con las reglas de la 4.15 (`REG/paso9_comprobar_entrega_4_14.log:7,15,23`; `E415/HITO_1_4_15.md:211`);
  - tres fechas de archivo que Git no conserva, con el contenido idéntico al manifiesto (`REG/paso9_comprobar_entrega_4_14.log:10,18,26`, `munger_v2_r1/CONTINUIDAD.md:136`). **Su hora cambia en cada máquina**: es la del checkout, conservada por `cp -a` (`REVT/REVISION_TRASPASO.md:121`). No es una discrepancia.
- El código 1 no se registró en el traspaso (`REVT/REVISION_TRASPASO.md:66`): el registro del §10.1 lo recoge.
- **No se da por superado** (`E415/hito2/HITO_2_4_15.md:123`). Sobre una descompresión del ZIP se esperaba 32/35 (`munger_v2_r1/CONTINUIDAD.md:136`); la 4.15 no tiene un ZIP completo (`E415/hito2/HITO_2_4_15.md:183-187`).

**Controles de las entregas anteriores.**
- Ahora se ejecutan con la limpieza previa del §5.4. Comando, desde `munger_v2_r1/` de la copia limpia, con la carpeta de salida **fuera del árbol verificado**:

      flock -x <e_work>/libreoffice.lock python3 -I -B personaje_v2/empresas_v2_correcciones/2026-11_Vidrala_ensayo_4_13/scripts/controles_historicos_4_13.py <registro>/paso10_controles_historicos

  - La forma `controles_historicos_4_13.py CARPETA_SALIDA` es *literal de la fuente* (`E414/resultados/LEEME_CONTROLES_HISTORICOS_4_14.md:5`; `E414/../2026-11_Vidrala_ensayo_4_13/scripts/controles_historicos_4_13.py:6`).
  - Con el bloqueo y la carpeta fuera del árbol: «comando probado en el traspaso del 17-nov» *(autodeclarado)*: el informe lo abrevia como `flock -x … python3 -I -B …` (`TRASP/INFORME_TRASPASO.md:33`). El código 0 está en `REG/paso10_exit.txt`, y las 19 salidas y el resumen, en `REG/paso10_controles_historicos/` (`REVT/REVISION_TRASPASO.md:67`). Las referencias de la 4.14 están dentro del árbol (`E414/resultados/controles_historicos_en_arbol_4_14/`); escribir la salida allí añadiría archivos al árbol verificado (`TRASP/INFORME_TRASPASO.md:79`).
  - Duración observada: de 09:38:05 a 10:05:57, 27 min 52 s (`REG/paso10_inicio.txt`, `REG/paso10_fin.txt`).
  - **Su código 0 no dice que los controles cumplan.** Con su argumento, el script sale siempre con 0 (`controles_historicos_4_13.py:78`, `:82`); sin argumento, imprime su ayuda y sale con 2 (`:52-54`). El código de cada control está en la columna «Código» de `resumen.md` (`controles_historicos_4_13.py:69`, `:75-77`).
  - La columna «¿Igual que en el árbol 4.12?» compara con las salidas del árbol 4.12, no con las del 4.14 (`controles_historicos_4_13.py:20-21`, `:66-68`). Para compararlas con las del árbol 4.14 hace falta un `diff` con `E414/resultados/controles_historicos_en_arbol_4_14/` (así lo hizo el revisor, `REVT/REVISION_TRASPASO.md:95`); el comando **[NO DOCUMENTADO]**.
- **Resultado esperado sobre el árbol 4.15.** Por la última línea de cada salida. El detalle de las líneas que ya eran NO CUMPLE cambia en varios controles por los archivos que añade o cambia la 4.15, por ejemplo `personaje_v2/pruebas/test_cierre_v2.py` (`REVT/REVISION_TRASPASO.md:94-99`).

| Control | Esperado sobre el árbol 4.15 | Árbol 4.14 (`E414/resultados/LEEME_CONTROLES_HISTORICOS_4_14.md`) | Clasificación | Fuente |
|---|---|---|---|---|
| **4.10** | **39 de 44**, código 1 | 40 de 44 (`:38`) | **Cambio documental de la 4.15.** Falla «el mensaje de arranque recupera la estructura de uso…» (`REG/paso10_controles_historicos/4_10_comprobar_entrega.txt:41`): el control exige `.PARTES.txt` en `PROMPT_NUEVA_VENTANA.md` (`E414/../2026-11_Vidrala_ensayo_4_10/scripts/comprobar_entrega_4_10.py:181-182`). La cadena está en la 4.14 (`origin/main`) y no en `957af65`, `3149128` ni `b129b36`; el mensaje se reescribió para arrancar desde el repositorio. Lo comprobó el coordinador. No es una regresión: es un control ligado al texto de su versión (`LEEME_CONTROLES_HISTORICOS_4_14.md:27`) | `REVT/MEJORAS_MANUAL.md:15`; `REVT/REVISION_TRASPASO.md:156-165` |
| **4.11** | **33 de 38**, código 1. En otro entorno de compresión podría dar 34 de 38 | 34 de 38 (`:40`) | **Atribuible al entorno (compresión).** Falla la igualdad de la huella del ZIP reconstruido (`REG/paso10_controles_historicos/4_11_comprobar_entrega.txt:12`; condición en `E414/../2026-11_Vidrala_ensayo_4_11/scripts/comprobar_entrega_4_11.py:124-126`). La reconstrucción termina bien, y `v6/` no cambia entre la 4.14 y `957af65`. **Lo vinculante es la comparación miembro a miembro del 4.12, que CUMPLE** (`REG/paso10_controles_historicos/4_12_comprobar_entrega.txt:14`; `E414/../2026-11_Vidrala_ensayo_4_12/scripts/comprobar_entrega_4_12.py:176-180`). Queda por cerrar: la versión de zlib (`zlib.ZLIB_RUNTIME_VERSION`) en los dos entornos y `comparar_zip.py` sobre la reconstrucción del 4.11 | `REVT/MEJORAS_MANUAL.md:16`; `REVT/REVISION_TRASPASO.md:167-190` |
| 4.2 | todas las comprobaciones esperadas se cumplen, código 0 | igual (`:15`) | observado una vez, no fijado | `REG/paso10_controles_historicos/resumen.md:5` |
| 4.3 | 217 de 217, código 0 | igual (`:16`) | observado una vez, no fijado | `…/resumen.md:6` |
| 4.3.1 | 43 de 43, código 0 | igual (`:17`) | observado una vez, no fijado | `…/resumen.md:7` |
| 4.4 | 72 de 72, código 0 | igual (`:18`) | observado una vez, no fijado | `…/resumen.md:8` |
| 4.5 | 60 de 60, código 0 | igual (`:19`) | observado una vez, no fijado | `…/resumen.md:9` |
| 4.6.1 | 23 de 23, código 0 | igual (`:20`) | observado una vez, no fijado | `…/resumen.md:10` |
| 4.6 | 23 de 24, código 1 (Z-1) | igual (`:25`) | observado una vez, no fijado | `…/resumen.md:11` |
| 4.8.1, comparación de baterías de la 4.7.1 | «HAY DIFERENCIAS», código 1 | igual (`:33`) | observado una vez, no fijado | `…/resumen.md:12` |
| 4.7 | 45 de 49, código 1 | igual (`:30`) | observado una vez, no fijado | `…/resumen.md:13` |
| 4.7.1 | 38 de 44, código 1 | igual (`:31`) | observado una vez, no fijado | `…/resumen.md:14` |
| 4.8 | 32 de 36, código 1 | igual (`:32`) | observado una vez, no fijado | `…/resumen.md:15` |
| 4.8, comparación de baterías de la 4.7.1 | «HAY DIFERENCIAS», código 1 | igual (`:33`) | observado una vez, no fijado | `…/resumen.md:16` |
| 4.8.1 | 25 de 30, código 1, **después de la limpieza del §5.4**. Sin ella, en el traspaso se interrumpió por falta de espacio | 25 de 30 (`:36`) | observado una vez, no fijado | `REG/paso10b_4_8_1_reintento.txt:38`; `…/resumen.md:17` (el intento fallido) |
| 4.9 | 34 de 39, código 1 | igual (`:37`) | observado una vez, no fijado | `…/resumen.md:18` |
| 4.10.1 | 38 de 43, código 1 | igual (`:39`) | observado una vez, no fijado | `…/resumen.md:20` |
| 4.12 | 59 de 63, código 1 | igual (`:41`) | observado una vez, no fijado | `…/resumen.md:22` |
| 4.13 | 83 de 89, código 1 | igual (`:43`) | observado una vez, no fijado | `…/resumen.md:23` |

- «Observado una vez, no fijado» quiere decir: es lo que dio el traspaso sobre `957af65`, en un entorno; ningún documento del producto lo fija como esperado. Si sale distinto, se registra la diferencia y su detalle, sin calificarla, y se comunica.
- En el traspaso, la limpieza se hizo **después** de la primera pasada, y solo se repitió el 4.8.1 (`TRASP/INFORME_TRASPASO.md:34`; `REVT/REVISION_TRASPASO.md:229-234`). Con la limpieza **antes** de la pasada completa, el resultado de los otros 18 controles no se ha observado (N-16).
  - Por lectura del código de los 19 controles (§3.2): solo el 4.8 y el 4.8.1 copian `pruebas/_v64/`; el 4.9 lo recorre sin efecto; el 4.11, el 4.12 y el 4.13 lo excluyen (`comprobar_entrega_4_11.py:87`, `comprobar_entrega_4_12.py:91`, `comprobar_entrega_4_13.py:107`); los demás no copian ni recorren el árbol entero. *Interpretación:* la limpieza no debería cambiar el resultado de los otros 17, pero no se ha observado.
  - Si un receptor prefiere no correr ese riesgo, puede repetir la secuencia observada: pasada completa y, **si el 4.8 o el 4.8.1 fallan por espacio**, limpieza y repetición solo de los que hayan fallado. En el traspaso, el 4.8 pasó (32 de 36, `REG/paso10_controles_historicos/resumen.md:15`), pero con menos disco podría fallar por el mismo motivo (§3.2).
  - Repetición del 4.8.1, desde `munger_v2_r1/` de la copia limpia:

        flock -x <e_work>/libreoffice.lock python3 -I -B personaje_v2/empresas_v2_correcciones/2026-11_Vidrala_ensayo_4_8_1/scripts/comprobar_entrega_4_8_1.py

    «comando probado en el traspaso del 17-nov» *(autodeclarado)*: el informe lo abrevia con «…» (`TRASP/INFORME_TRASPASO.md:34`); el código 1 y las horas son autodeclarados; el resultado, 25 de 30, está en `REG/paso10b_4_8_1_reintento.txt:38` (`REVT/REVISION_TRASPASO.md:68`).
  - Repetición del 4.8, desde el mismo sitio:

        flock -x <e_work>/libreoffice.lock python3 -I -B personaje_v2/empresas_v2_correcciones/2026-11_Vidrala_ensayo_4_8/scripts/comprobar_entrega_4_8.py

    **[NO DOCUMENTADO]**, *adaptado de* la llamada de `controles_historicos_4_13.py:59` (`python3 -I -B <script>`, desde `munger_v2_r1/`) y de la orden anterior: no consta ejecutado suelto (N-20). Va con el bloqueo porque ejecuta `test_estados_v2.py` (`comprobar_entrega_4_8.py:91`, `:94`), que arranca LibreOffice (`munger_v2_r1/CONTINUIDAD.md:133`). Lo observado es lo de la tabla: 32 de 36, código 1.
- `E414/resultados/LEEME_CONTROLES_HISTORICOS_4_14.md` describe el árbol 4.14 (`:1-3`). CONTINUIDAD ya reconoce que «el resultado esperado de esos controles sobre el árbol 4.15 no está documentado» (`munger_v2_r1/CONTINUIDAD.md:136`). Esta tabla es la propuesta del manual para cubrir ese hueco; no es un documento del producto.

### 5.4 Limpieza de `pruebas/_v64/` antes de los controles 4.8 y 4.8.1 (mejora 1)

- **Cuándo:** en la copia limpia, después de `verificar_paquete.sh completa` (§5.2) y del control de la 4.14 (§5.3), y **antes** de los controles históricos, que incluyen el 4.8 y el 4.8.1, los dos que copian `_v64/` (§3.2).
- **Qué autoriza el producto:** terminada la verificación, borrar los `*.xlsx` y `vigencia/` de `personaje_v2/pruebas/_v64/`, **registrando las rutas** (`munger_v2_r1/CONTINUIDAD.md:143`; regla 11.10).
- **Comando**, desde la carpeta de trabajo:

      find <copia>/munger_v2_r1/personaje_v2/pruebas/_v64 -name '*.xlsx' -not -path '<copia>/munger_v2_r1/personaje_v2/pruebas/_v64/vigencia/*' -delete
      rm -rf <copia>/munger_v2_r1/personaje_v2/pruebas/_v64/vigencia

  «comando probado en el traspaso del 17-nov» *(autodeclarado)*: el informe da las dos órdenes juntas, con `;`, y abrevia las rutas con «…» (`TRASP/INFORME_TRASPASO.md:34`); `<copia>` es `copia_limpia_1`, como muestran las rutas registradas en `REG/paso10_limpieza_rutas.txt`). Las rutas borradas sí están en el registro: 774 `.xlsx`, la carpeta `vigencia/` y la nota del ZIP, 776 líneas (`REVT/REVISION_TRASPASO.md:100`). El comando exacto con que se escribió esa lista y el código de salida no se conservan (`REVT/REVISION_TRASPASO.md:68`).
- **Registrar las rutas antes de borrar:** el mismo `find` con `-print` en lugar de `-delete`, redirigido a `<registro>/paso10_limpieza_rutas.txt`. **[NO DOCUMENTADO]**: no consta así en el traspaso.
- **No** se borra el ZIP de la Release (§4.2.3) ni nada fuera de `_v64/`.
- La limpieza solo se hace en la copia limpia ya verificada. Nunca en el worktree de la candidata ni en una copia que aún no haya pasado la verificación.

## 6. Recorrido supervisado de una empresa

> Requiere encargo expreso (`CLAUDE.md:8`, `munger_v2_r1/CONTINUIDAD.md:361`). Se hace en un expediente nuevo y con agentes reales (`PV2/GUIA_RECORRIDO_SUPERVISADO.md:23`, `PV2/GUIA_RECORRIDO_SUPERVISADO.md:93`). **La guía ya está puesta al día para la 4.15 · hito 2** desde `3149128`, igual en `b129b36` (`PV2/GUIA_RECORRIDO_SUPERVISADO.md:1-3`). `CONTRADICCIONES_GUIA.md` se escribió para `957af65`; su estado en `b129b36` está en el §12.3.

### 6.1 Preparar el expediente

- **Nueva base económica o corrección de datos de un expediente cerrado:** se escribe un `CAMBIO.json` (`PV2/GUIA_RECORRIDO_SUPERVISADO.md:27`, `PV2/GUIA_RECORRIDO_SUPERVISADO.md:119`) y se ejecuta (*literal de la fuente, no probado*: `PV2/GUIA_RECORRIDO_SUPERVISADO.md:27`):

      python3 -I personaje_v2/scripts/cambiar_base.py preparar CAMBIO.json

  - Crea un expediente nuevo y nunca sobrescribe el origen (`PV2/GUIA_RECORRIDO_SUPERVISADO.md:119`, `PV2/scripts/cambiar_base.py:4-5`).
  - Una corrección de la Historia va en `correcciones_fase1_partes` (`PV2/GUIA_RECORRIDO_SUPERVISADO.md:120`).
  - Si se perdiera una entrada `analisis` del origen, la preparación se detiene (`PV2/GUIA_RECORRIDO_SUPERVISADO.md:121`).
  - Desde la 4.15: las entradas `analisis` se declaran con su cálculo; las heredadas se reconocen o descartan (`analisis_que_se_conservan` / `analisis_que_se_descartan`); el expediente nuevo lleva `entrada_efectiva.json`, por defecto en «estricta» (`PV2/GUIA_RECORRIDO_SUPERVISADO.md:121-124`; `E415/HITO_1_4_15.md:145-151`; `munger_v2_r1/CONTINUIDAD.md:16`).
- **Parada en el paso 2** (`PV2/GUIA_RECORRIDO_SUPERVISADO.md:51`; `PV2/scripts/pipeline.py:659-669`):
  - un `entrada_efectiva.json` ilegible, con errata o con un modo distinto del declarado termina en `no_entregable`;
  - el relleno «estricta» detenido (`rellenar_fase1_v63.py --estricta`, código 7) termina en `pendiente_de_datos`;
  - qué se hace: leer `diagnostico.md`; completar la entrada efectiva con su cálculo o corregir el archivo, **sin rebajar el modo** (`PV2/GUIA_RECORRIDO_SUPERVISADO.md:51`). Sin ningún rastro del modo, se aplica «registrada» (límite U6 (a)) (`E415/hito2/HITO_2_4_15.md:74-76`).
- **Configuración económica (motor B):** la escribe la orquestación, nunca un agente de juicio (`PV2/GUIA_RECORRIDO_SUPERVISADO.md:10`). Lleva su trazabilidad (`PV2/GUIA_RECORRIDO_SUPERVISADO.md:30-36`) y se valida con (*literal de la fuente, no probado*: `PV2/GUIA_RECORRIDO_SUPERVISADO.md:37`):

      python3 -B personaje_v2/scripts/configuracion_economica.py validar configuracion_economica.json

  Ningún parámetro, protocolo ni perímetro queda adoptado (`PV2/GUIA_RECORRIDO_SUPERVISADO.md:33-36`).

### 6.2 Registro de las entradas (verificación de las entradas financieras)

- Plantilla del registro: `python3 -B scripts/verificacion_entradas.py plantilla CARPETA` (*literal de la fuente, no probado*), desde `personaje_v2/`. Se hace en una copia (`PV2/GUIA_RECORRIDO_SUPERVISADO.md:102`). Escribe `verificacion_entradas.plantilla.json` (`PV2/scripts/verificacion_entradas.py:83`).
- **El extractor** rellena cada entrada (`PV2/GUIA_RECORRIDO_SUPERVISADO.md:103-110`):
  - `pagina` es la página del PDF, un entero; el folio impreso va aparte. Una página inexistente es una discrepancia (`E415/HITO_1_4_15.md:19-21`);
  - una fuente local tiene que existir y llevar su sha256 vigente; si no, la entrada queda pendiente (`E415/HITO_1_4_15.md:26-27`). Una lectura externa no cuenta como comprobada (`E415/HITO_1_4_15.md:28`);
  - las cifras tienen que ser numéricamente equivalentes, sin redondeo (`E415/HITO_1_4_15.md:32-37`);
  - `valor_fuente` es la cifra **publicada, con su signo**; `signo` y `escala` son la transformación. Un signo −1 exige su `tratamiento` (`E415/hito2/HITO_2_4_15.md:30`, `:42-43`);
  - el universo incluye las cifras de juicio (`ambito = "juicio"`) (`munger_v2_r1/CONTINUIDAD.md:15`).
- **El revisor, distinto del extractor**, comprueba cada entrada y la **sella** (`PV2/GUIA_RECORRIDO_SUPERVISADO.md:111-115`; `PV2/scripts/verificacion_entradas.py:84`). *Literal de la fuente, no probado* (`PV2/GUIA_RECORRIDO_SUPERVISADO.md:111`):

      python3 -B scripts/verificacion_entradas.py sellar CARPETA --revisor NOMBRE --fecha AAAA-MM-DD CELDA [CELDA …]

  - Con la fecha de hoy. Sin vínculo, la comprobación queda pendiente; si cambia lo vinculado, desactualizada (`E415/HITO_1_4_15.md:53-54`). El vínculo detecta cambios, pero no acredita autoría (`E415/HITO_1_4_15.md:63`).
- Comprobación: `python3 -B scripts/verificacion_entradas.py comprobar CARPETA` (*literal de la fuente, no probado*). El pipeline la repite en el paso 12 (`PV2/GUIA_RECORRIDO_SUPERVISADO.md:116`).
- Un registro no apto no impide recorrer el pipeline, y ninguna salida se presenta como apta para dinero real (`PV2/GUIA_RECORRIDO_SUPERVISADO.md:117`).
- Las firmas no se simulan. La revisión del significado económico de cada derivado (U1) la hace un revisor independiente (`E415/hito2/HITO_2_4_15.md:194-196`, `:66-68`).

### 6.3 Ejecutar el pipeline

- Comandos por plantilla. La selección es siempre explícita (`PV2/GUIA_RECORRIDO_SUPERVISADO.md:41`, `:127-129`). Marcas: la primera línea es *literal de la fuente, no probado* (`:41`). La segunda es **[NO DOCUMENTADO]**, *adaptada de* `:41`: esa línea da la orden V6.4 completa y, para la V6.4.1, solo el fragmento `--config personaje_v2/config_v2_v641_experimental.json`; la orden entera la compone este manual. La tercera es **[NO DOCUMENTADO]** en esta forma general, *adaptada de* `:129`; con la ruta de un expediente concreto y `flock`, es la orden «probada en el traspaso del 17-nov» *(autodeclarado)* del §7.4:

      python3 personaje_v2/scripts/pipeline.py CARPETA --config personaje_v2/config_v2_v64_experimental.json     (V6.4, motor B)
      python3 personaje_v2/scripts/pipeline.py CARPETA --config personaje_v2/config_v2_v641_experimental.json    (V6.4.1)
      python3 personaje_v2/scripts/pipeline.py CARPETA --config personaje_v2/config_v2.json                      (V6.3, motor A)

  - La tercera línea completa la ruta de `--config config_v2.json` (`PV2/GUIA_RECORRIDO_SUPERVISADO.md:129`) con `personaje_v2/`, como las dos primeras (mejora 2). Con esa ruta completa la ejecutó el traspaso (§7.4).
  - Opciones: `[--config …] [--agentes-simulados DIR] [--hasta N] [--reiniciar] [--desde N]` (`PV2/scripts/pipeline.py:4`).
  - `--agentes-simulados` solo vale para pruebas técnicas, nunca en un expediente real (`PV2/GUIA_RECORRIDO_SUPERVISADO.md:57`, `:93`).
  - Con el bloqueo del §2.1: el pipeline recalcula y su paso 0 llama a LibreOffice (`PV2/GUIA_RECORRIDO_SUPERVISADO.md:22`).
- Códigos de salida (`PV2/GUIA_RECORRIDO_SUPERVISADO.md:43-51`):

| Código | Qué significa | Qué se hace |
|---|---|---|
| 0 | terminado: concluido, pendiente o no entregable, con su diagnóstico | leer la ficha, el informe y `diagnostico.md` |
| 0, terminado en el paso 2 | (4.15) entrada efectiva ilegible o con errata (`no_entregable`), o relleno «estricta» detenido (código 7: `pendiente_de_datos`) | leer `diagnostico.md`; completar la entrada efectiva o corregir el archivo, sin rebajar el modo |
| 10 | espera a un agente (`ESPERANDO.md`, `prompts_generados/`) | lanzar el agente y volver a ejecutar |
| 2 | parada sin escribir: selección, configuración o material incoherentes | corregir la causa; no forzar |
| 3 | límite del modelo | es un resultado legítimo; se documenta |
| 5 | retirada de una aprobación pendiente de registrar | volver a ejecutar cuando el resumen sea escribible |
| 6 | estado del pipeline o registro de auditorías ilegible | restaurar desde una copia o relanzar con `--reiniciar`; nunca seguir como aprobado |

### 6.4 Relevos (código 10) con agentes reales en contextos separados

- Cada relevo se resuelve con un agente real (`PV2/GUIA_RECORRIDO_SUPERVISADO.md:53-57`):
  - el agente recibe el prompt generado, `prompts_generados/NN_<fase>.md`;
  - modelo y esfuerzo, según `modelos` de la configuración: extracción, Sonnet medio; fases A, B y C, Opus alto; verificación, Opus medio (`PV2/GUIA_RECORRIDO_SUPERVISADO.md:54`);
  - reglas: escribe solo su salida; sin internet ni memoria; no ejecuta el pipeline ni LibreOffice; no abre Excel (`PV2/GUIA_RECORRIDO_SUPERVISADO.md:55`).
- **La fase C tiene dos turnos con el mismo agente**: se continúa su conversación (`PV2/GUIA_RECORRIDO_SUPERVISADO.md:56`, `EVID/coordinacion/cierre_v2/PROGRAMA.md:38`).
- **Cada auditoría la hace un agente nuevo, de contexto separado** (`PV2/GUIA_RECORRIDO_SUPERVISADO.md:68`, `munger_v2_r1/CONTINUIDAD.md:153`):
  - sin contexto del trabajo y sin que se le diga qué se espera (`PV2/PROMPT_CLAUDE_CODE.md:30`, documento histórico);
  - el actor y el contexto tienen que ser distintos de quien produjo el material (`EVID/coordinacion/cierre_v2/PROGRAMA.md:38`);
  - si no se puede lanzar, se declara que la auditoría no es independiente (`munger_v2_r1/CONTINUIDAD.md:153`).
- Orden habitual: extracción → fase A → fase B → recálculo y variantes (paso 10) → fase C, turno 1 → turno 2 → verificación y auditoría → cierre. Puede haber vueltas (`PV2/GUIA_RECORRIDO_SUPERVISADO.md:59`).
- Qué mira la persona responsable en cada relevo: `PV2/GUIA_RECORRIDO_SUPERVISADO.md:61-68`. APROBADO solo vale para el material fijado (`PV2/GUIA_RECORRIDO_SUPERVISADO.md:68`).

### 6.5 Leer el resultado

- Estado, acción y cubo: ficha e informe, línea 1 (`PV2/GUIA_RECORRIDO_SUPERVISADO.md:72`).
- **Aptitud por entradas (I20, hito 2).** La ficha y el informe de todas las plantillas, también la V6.3, muestran el bloque `verificacion_entradas` (`E415/hito2/HITO_2_4_15.md:82-88`, `PV2/scripts/ficha.py:383-391`, `PV2/GUIA_RECORRIDO_SUPERVISADO.md:117`): si es apto o no, el recuento, `apto_para_dinero_real: false` y el modo de la entrada efectiva, aplicado y declarado, con su procedencia. Las salidas históricas sin registro ni modo no cambian (`E415/hito2/HITO_2_4_15.md:85-87`).
  - Observado en el traspaso, en la ficha **provisional** de la copia del paso 12: `apto_por_entradas: false`, `apto_para_dinero_real: false`, «0 de 292», modo `registrada`, `declarado_en: null` (`REG/relevo_copia_base/ficha_provisional.json`; `REVT/REVISION_TRASPASO.md:74`).
- `aptitud_de_uso` (V6.4): mientras diga «experimental», ni «concluido» ni APROBADO hacen el resultado apto para dinero real. Un modo aplicado distinto del declarado impide «apto por entradas» (`PV2/GUIA_RECORRIDO_SUPERVISADO.md:73`).
- Objetivo, rango calculado, avisos de dominio, acción final y fechas: `PV2/GUIA_RECORRIDO_SUPERVISADO.md:74-83`. El rango **no es un intervalo de confianza** (`PV2/GUIA_RECORRIDO_SUPERVISADO.md:80`).

## 7. Vigencia, cambios, invalidación y reanudación

### 7.1 Vigencia e invalidación

- Cualquier cambio del material auditado retira la aprobación en la **primera** llamada de cualquier herramienta, y el pipeline repite lo afectado. También la retira una estructura JSON incorrecta en un campo de control. Las salidas cerradas no se editan a mano (`PV2/GUIA_RECORRIDO_SUPERVISADO.md:87`).
- El material fijado incluye, entre otros, `fase_a.json`/`.md`, `fase_b.json`/`.md`, `fase_c.json`/`.md` y `extracto_v63.md` (`PV2/scripts/cierre_v2.py:31`), `verificacion_entradas.json` (`:448`) y, desde el hito 2, `entrada_efectiva.json` (`:451`; `E415/hito2/HITO_2_4_15.md:88`).
- Una comprobación de entradas cuyo vínculo ya no coincide queda desactualizada (`E415/HITO_1_4_15.md:53`).
- Un defecto del código que escribe el material provisional se corrige en el código y se relanza `pipeline.py … --desde 13`. El material se regenera y se fija de nuevo, y hace falta una auditoría nueva (`PV2/GUIA_RECORRIDO_SUPERVISADO.md:68`).
- **Pruebas:** un cambio invalida solo las pruebas materialmente afectadas, y el integrador justifica esa dependencia (`EVID/coordinacion/cierre_v2/PROGRAMA.md:49`).

### 7.2 Reanudación

- Si el pipeline se corta, se vuelve a ejecutar con el mismo comando. Retoma en el paso guardado en `estado_pipeline.json`. Un agente que no terminó se relanza con el mismo `prompts_generados/NN_*.md` (`PV2/GUIA_RECORRIDO_SUPERVISADO.md:133`).
- `--desde N` repite desde el paso N cuando cambia una entrada de ese paso. Por ejemplo, `--desde 12` para el registro de las entradas (`PV2/GUIA_RECORRIDO_SUPERVISADO.md:134`).
- Si el material cambia después de una auditoría, la aprobación se retira sola y se emite una solicitud nueva. Una auditoría anterior no responde a ella (`PV2/GUIA_RECORRIDO_SUPERVISADO.md:135`).
- `estado_pipeline.json` no guarda el comando original (`REVT/REVISION_TRASPASO.md:214`): «el mismo comando» se toma del LEEME del expediente (§7.4).

### 7.3 Relevo caducado (I19, corregido en el hito 2) y límite H9

- **Comportamiento vigente.** Mientras el paso 13 espera, el pipeline compara el material fijado con el vigente. Si difieren (`E415/hito2/HITO_2_4_15.md:89-92`, `munger_v2_r1/CONTINUIDAD.md:152`, `PV2/GUIA_RECORRIDO_SUPERVISADO.md:136-139`, `PV2/scripts/pipeline.py:1060-1084`):
  - lo registra en `estado_pipeline.json → relevos_caducados`, con el material fijado, el vigente y los archivos cambiados;
  - repite el paso 12;
  - pide la auditoría del material vigente, y la solicitud antigua queda «sustituida».
- **Basta relanzar el pipeline con el mismo comando, sin `--desde`** (`munger_v2_r1/CONTINUIDAD.md:152`, `PV2/pruebas/test_relevo_i19_415.py:33-37`). Una aprobación de la solicitud antigua no cierra nada (`PV2/pruebas/test_relevo_i19_415.py:73-77`). Con el código anterior al hito 2 se usaba `--desde 12`: **no es el procedimiento vigente** (`munger_v2_r1/CONTINUIDAD.md:152`).
- Lo cubre la batería `test_relevo_i19_415.py`, 5/5, con agentes simulados (`PV2/pruebas/test_relevo_i19_415.py:10`). El traspaso lo observó además con LibreOffice sobre un expediente real copiado, sin `--desde` (`REVT/REVISION_TRASPASO.md:126-138`).
- **Límite H9: abierto, sin procedimiento.** No se reintroduce I19 ni I20; lo único abierto es H9.
  - El relevo caducado vuelve **siempre al paso 12** (`E415/hito2/HITO_2_4_15.md:92-93`; `PV2/GUIA_RECORRIDO_SUPERVISADO.md:141`). Si cambian salidas de fases anteriores, haría falta volver al paso que las consume; hay una propuesta sin aplicar (`E415/hito2/PUNTO_DE_RECUPERACION.md:33-34`, `munger_v2_r1/CONTINUIDAD.md:11`).
  - El programa lo deja **pendiente de verificar por cambio afectado** (`EVID/coordinacion/cierre_v2/PROGRAMA.md:40`). La tarea T-CAMBIOS pide ensayar un cambio anterior y el punto real de reanudación (`EVID/coordinacion/cierre_v2/CONTROL.json` → `T-CAMBIOS.siguiente_accion`, línea 810 en `acea175`).
  - **Para probarlo hay que cambiar una salida que se vuelque en celdas: `fase_c.json`, `fase_b.json` o `entrada_efectiva.json`** (`REVT/MEJORAS_MANUAL.md:12`; `REVT/REVISION_TRASPASO.md:93`). Las fases se vuelcan en el libro con `fase_a_celdas.py` y `escribir_v63.py` (`PV2/scripts/pipeline.py:587-592`), y la entrada efectiva se lee en el paso 2 (`PV2/scripts/pipeline.py:642`, `:659-669`).
  - **Con `fase_c.md` no se distingue el caso que importa.** Es texto que no se vuelca en celdas. Al repetir el paso 12, `verificar_todo.sh` vuelve a pasar las citas de `fase_c.md` y el esquema de `fase_c.json` (`PV2/scripts/verificar_todo.sh:22`, `:58-60`), pero no reescribe celdas desde `fase_c.json` (`REVT/REVISION_TRASPASO.md:89-93`).
  - **Qué cambio concreto hacer, cómo comprobar si llega a las celdas y cuál sería el resultado correcto: [NO DOCUMENTADO].** Este manual no lo inventa. Hasta que T-CAMBIOS lo resuelva, el operador registra `relevos_caducados[].archivos_cambiados`, el paso al que vuelve y lo que se repite, y lo comunica a la persona responsable. No lo da por resuelto.
  - *Cautelas, por lectura del código:* un cambio que rompa el JSON o su esquema prueba otra cosa: la validación de `fase_c.json` (`PV2/scripts/verificar_todo.sh:22`) o la parada por `entrada_efectiva.json` ilegible (`PV2/scripts/pipeline.py:76-105`). Cualquier cambio se hace solo en una copia desechable; no es un valor económico ni se adopta, y su salida no es un análisis.
- **[CONTRADICCIÓN] menor (C-16):** la tensión está dentro de la misma línea de la guía corregida, que dice a la vez que, si cambian salidas de fases anteriores, «volver al paso 12 no basta» y que el caso «está pendiente de verificar por cambio afectado» (`PV2/GUIA_RECORRIDO_SUPERVISADO.md:141`). Y está frente a `E415/hito2/HITO_2_4_15.md:92`, que lo da en condicional («habría que volver al paso que las consume»), como el programa («pendiente de verificar», `EVID/coordinacion/cierre_v2/PROGRAMA.md:40`). Este manual sigue al programa: no consta que baste ni que no baste.

### 7.4 Relevos de expedientes anteriores o sustituidos (pasos 11–13 del §10; mejora 2)

- **Relevos pendientes del paquete** (`munger_v2_r1/CONTINUIDAD.md:144-147`). Ninguno pertenece a un expediente vigente:
  - `E414/elis_motor_A/Elis`, paso 13: caducado y sustituido;
  - las ramas `viscofan/` y `vidrala/` de la 4.14, paso 13: no se auditan;
  - `vidrala_decisiones_INVALIDO_perdio_analisis`, paso 6: inválido; no se reanuda.
- **Hay 13 esperas, no 4** (mejora 7). En `3149128` hay 13 `estado_pipeline.json` con `esperando` (lectura de este borrador; el mismo número en `957af65`, `REVT/REVISION_TRASPASO.md:219`). Además de los cuatro de CONTINUIDAD: las copias `antecedentes/heredados/` de cuatro expedientes de la 4.14 y cinco esperas en expedientes de la 4.10, la 4.10.1 y la 4.12 (`TRASP/INFORME_TRASPASO.md:35`, `:84`). Ninguna es vigente y ninguna se reanuda en su sitio. Solo se cuentan para dejar constancia; no se resuelven.
- **Reglas** (`munger_v2_r1/CONTINUIDAD.md:149-153`):
  - se resuelve en una **copia hermana, a la misma profundidad (`cp -a`)**, nunca en su sitio;
  - se relanza primero el pipeline con el mismo comando, que regenera los prompts con las rutas actuales;
  - las plantillas de relevo de la 4.13 son históricas;
  - la auditoría la hace un agente nuevo, de contexto separado.
- **Dónde:** en una copia de `munger_v2_r1/` distinta de la copia limpia, para no tocar el árbol en el que se hizo el control de la 4.14. El traspaso usó una «copia para relevos» aparte (`TRASP/INFORME_TRASPASO.md:18`). El comando con que la hizo **[NO DOCUMENTADO]**; la forma de la copia limpia (§5.1) es la probada para una copia completa.
- **Aviso: `elis_motor_A` ya está caducado.** El primer relanzamiento no sale solo con «código 10 y prompts regenerados». Con el código 4.15 hace también la detección del relevo caducado:
  - registra `relevos_caducados` con el material fijado `9e1a725d6432f548`, el vigente `72f855cf59b252fb` y `verificacion_entradas.json` como archivo cambiado;
  - repite el paso 12 («0 de 292», apta por entradas: no);
  - registra una solicitud nueva y deja `SA-ed5561eac1cc5897` «sustituida»;
  - sale con código 10, esperando la auditoría de la solicitud nueva.

  Fuentes: `REG/paso12_pipeline_01.txt:1-4`; `REG/relevo_copia_base/estado_pipeline.json`; `REVT/REVISION_TRASPASO.md:126-133`; `munger_v2_r1/CONTINUIDAD.md:145`. En el traspaso, la solicitud nueva fue `SA-4bb1526435a31a51`, del material `4d9ee9b6e4b4bd09`: observado una vez; esos identificadores pueden variar.
  - **[CONTRADICCIÓN] C-15:** `munger_v2_r1/CONTINUIDAD.md:151` dice que el primer relanzamiento «sale con código 10 sin hacer nada más»; `:152` dice que el pipeline detecta el relevo caducado al relanzarlo. Para `elis_motor_A`, que `:145` declara caducado, pasan las dos cosas (`REVT/REVISION_TRASPASO.md:208`).
- **El mismo comando de `elis_motor_A`.** Su plantilla es la V6.3, `config_v2.json` (`E414/elis_motor_A/LEEME_ELIS_MOTOR_A.md:5`), y el traspaso de la 4.14 usó `--config personaje_v2/config_v2.json` (`E414/documentacion_cierre_4_14/traspaso/INFORME_TRASPASO.md:112`). Desde `munger_v2_r1/` de la copia de relevos:

      cp -a personaje_v2/empresas_v2_correcciones/2026-11_Vidrala_ensayo_4_14/elis_motor_A personaje_v2/empresas_v2_correcciones/2026-11_Vidrala_ensayo_4_14/elis_motor_A_relevo_receptor
      flock -x <e_work>/libreoffice.lock python3 personaje_v2/scripts/pipeline.py personaje_v2/empresas_v2_correcciones/2026-11_Vidrala_ensayo_4_14/elis_motor_A_relevo_receptor/Elis --config personaje_v2/config_v2.json

  «comando probado en el traspaso del 17-nov» *(autodeclarado)*: el informe abrevia la ruta con «…» (`TRASP/INFORME_TRASPASO.md:36`); el código 10 y el `diff -r` son autodeclarados; la salida está en `REG/paso12_pipeline_01.txt` y el estado, en `REG/relevo_copia_base/` (`REVT/REVISION_TRASPASO.md:70`). Duró unos 15 s (`REVT/REVISION_TRASPASO.md:81`).
- **Huellas del original antes y después** (mejora 5). El traspaso guardó las 126 huellas de `elis_motor_A` antes del relanzamiento (`REG/paso12_original_antes.sha256`), con el formato de `sha256sum` y rutas `./Elis/…`. El «después» no se publicó (`REVT/REVISION_TRASPASO.md:101`). Cómo se calcularon y la orden de contraste posterior **[NO DOCUMENTADO]**. El receptor guarda las dos listas y su comparación en el registro.

## 8. Recepción de entregas nuevas

- No se interrumpe ni se repite un encargo en curso de otra sesión. Su entrega final se conserva y se importa como versión nueva, sobre una copia completa. Nunca se sobrescribe con la base histórica (`CLAUDE.md:37`, `docs/RECEPCION_ENTREGA_CLAUDE.md:3`). Una entrega posterior no se incorpora automáticamente (`munger_v2_r1/PROMPT_NUEVA_VENTANA.md:43-44`).
- Pasos del producto (`docs/RECEPCION_ENTREGA_CLAUDE.md:7-12`):
  1. Conservar el ZIP, su SHA-256, el manifiesto, la verificación externa y el registro de cambios. Si es un parche, también la identidad exacta de su base.
  2. Subirlo completo a una Release nueva. Antes, comprobar el tamaño: el límite es de 2 GiB por archivo.
  3. Comprobar la huella y la integridad de sus miembros. Extraerlo en una carpeta nueva y verificar el manifiesto de **esa** entrega. Sin `base_414.py` ni `restore_assets_414.py`.
  4. Importarla en una rama nueva, con los bytes exactos y los binarios registrados aparte. Comparar con la base histórica completa. Un archivo ausente no es automáticamente un alta.
  5. Ejecutar los controles de la entrega sobre la copia materializada y registrar resultados reales.
  6. Revisarla contra los contraejemplos y los bloqueos económicos. No dar por apto un resultado porque pasen los controles de software.
- Paquete de cambios de la 4.15 frente a la base 4.14 (`E415/hito2/HITO_2_4_15.md:183-187`): 17 cambiados · 964 nuevos · 0 desaparecidos, más el manifiesto sustituido; se reconstruye con `empaquetar_cambios_4_15.py`; el ZIP no se versiona.
- En el programa de cierre (`EVID/coordinacion/cierre_v2/INTEGRACION.md:23-35`): se fija el SHA del autor, se leen las diferencias, se reproducen los comandos, autor y revisor son distintos, nunca se fusionan ramas auxiliares completas y se verifica la candidata real.
- **[CONTRADICCIÓN]** C-05, ahora parcial: CONTINUIDAD ya registra que el hito 2 se entregó como rama con un paquete de cambios (`munger_v2_r1/CONTINUIDAD.md:375`), pero la misma regla sigue exigiendo «un ZIP completo», igual que `docs/RECEPCION_ENTREGA_CLAUDE.md:7-9`.

## 9. Traspaso a un contexto limpio

- La fuente de verdad es el repositorio y sus pruebas, no la memoria de conversaciones anteriores (`munger_v2_r1/PROMPT_NUEVA_VENTANA.md:11`).
- El mensaje de arranque vigente es el texto bajo la línea de `munger_v2_r1/PROMPT_NUEVA_VENTANA.md` (`:5-7`). CONTINUIDAD §12 ya arranca desde el repositorio (`munger_v2_r1/CONTINUIDAD.md:391-395`): C-04 queda resuelta en `3149128`.
- **Primera tarea del receptor:** comprobar el estado y no iniciar ningún otro trabajo (`munger_v2_r1/PROMPT_NUEVA_VENTANA.md:13-29`).
- **Puntos de recuperación:** `E415/hito2/PUNTO_DE_RECUPERACION.md:49-53`; en la coordinación, cada bloque publica el suyo (`EVID/coordinacion/cierre_v2/INTEGRACION.md:17`).
- **Precedentes:**
  - 4.14: el receptor verificó el paquete y resolvió un relevo en una copia hermana; su auditoría no fue independiente (`E414/documentacion_cierre_4_14/traspaso/LEEME_TRASPASO.md:5-17`); las dificultades quedaron en I18–I21 (`E414/documentacion_cierre_4_14/INCIDENCIAS_4_14.md:144-182`), de las que I19 e I20 están corregidas en el hito 2 (§6.5, §7.3) y no se reintroducen; la prueba quedó por repetir (`munger_v2_r1/CONTINUIDAD.md:358`).
  - 17-nov (T-TRASPASO, sobre `957af65`): conforme con límites. La verificación completa fue idéntica byte a byte; 29/35; I19 observado sin `--desde`; H9 vuelve al paso 12. Los pasos con agentes no fueron ejecutables por el receptor, y el registro no conserva transcripción ni la mayoría de los códigos (`REVT/REVISION_TRASPASO.md:19-34`; `EVID/coordinacion/cierre_v2/CONTROL.json` → `T-TRASPASO.siguiente_accion`, línea 841 en `acea175`).

## 10. Lista de comprobación de la prueba de traspaso (T-TRASPASO)

- **Para quién:** un receptor sin historial que solo dispone del repositorio, de este manual y del mensaje de arranque (`EVID/coordinacion/cierre_v2/traspaso/PROMPT_RECEPTOR.md:3`, `:12-14`).
- **Qué pide la tarea:** reconstruir y verificar la candidata y decir qué no ha podido hacer y por qué (`EVID/coordinacion/cierre_v2/traspaso/PROMPT_RECEPTOR.md:5-8`; tarea en `EVID/coordinacion/cierre_v2/CONTROL.json` → `T-TRASPASO.id` y `.tarea`, líneas 817-818 en `acea175`).
- **Requisitos de cada paso:** **S** = sin LibreOffice ni agentes; **LO** = con LibreOffice, con el bloqueo del §2.1; **AG** = con agentes reales de contexto separado; **RED** = descarga de la Release.
- **Código esperado:** el código de salida con que el paso es correcto. Varios pasos correctos salen con un código distinto de 0 (9, 10b, 12 y 13). El registro del §10.1 los marca como «fallidos», y el receptor los contrasta con esta columna. El paso 14 no tiene código esperado: no se ha ejecutado nunca. `REG/paso_h9_pipeline.txt` es del paso 14 **del traspaso**, que cambió `fase_c.md`; en esta lista, eso es el paso 13. Su código 10 es autodeclarado: consta en `TRASP/INFORME_TRASPASO.md:38`, no en el registro (`REVT/REVISION_TRASPASO.md:72`). El archivo, de 4 líneas, muestra la espera (`REG/paso_h9_pipeline.txt:4`), no el código.

| # | Paso | Requisito | Comando (§) | Código esperado | Resultado esperado | Fuente |
|---|---|---|---|---|---|---|
| 1 | Leer `README.md`, `CLAUDE.md`, `munger_v2_r1/CONTINUIDAD.md`, `munger_v2_r1/PROMPT_NUEVA_VENTANA.md`, `E415/hito2/HITO_2_4_15.md` y `PUNTO_DE_RECUPERACION.md` | S | lectura | — | Identifica la 4.15 · hito 2 con G-DOCS y G-RAIZ, la aptitud experimental y los pendientes (F1, regeneración, H9, U1, U6 (a)). Comprueba que `README.md:1` y `CLAUDE.md:1` ya dicen «hito 2», como `VERSION` (C-01 y C-02, resueltas en `b129b36`) | `munger_v2_r1/VERSION:1`; `README.md:1`; `CLAUDE.md:1`; `E415/hito2/HITO_2_4_15.md:219-220` |
| 2 | Clonar `main`, descargar el ZIP y comprobarlo | RED | §4.2.1–3 | 0 (`gh release download` da 1 en una sesión de Claude Code; entonces, la API REST) | 1130912246 bytes; SHA-256 `bb51942c…7b93e` | `README.md:33-35`; `TRASP/INFORME_TRASPASO.md:23-24` |
| 3 | `materialize` y `verify` con `tools/base_414.py`, en `main` | S | §4.2.4 | 0 / 0 | 1008 recuperados; 6798/6798, `complete: true` | `README.md:42-46`; `REG/paso3_*.log` |
| 4 | Obtener `integracion/candidata-cierre-v2` | S | §4.2.5 | 0 | HEAD `b129b36`; `VERSION` dice «4.15 · hito 2» | `EVID/coordinacion/cierre_v2/CONTROL.json` → `versiones_fijadas.candidata` (línea 11 en `2c988b8`) |
| 5 | Copiar los 1008 binarios `release_asset`, sin sobrescribir | S | §4.2.6 | 0 | 1008 copiados · 0 existentes · 0 distintos · 0 fallos; en un clon sin exclusión local, 83 JSON sin seguimiento en `git status` (§4.2.6) | `REG/paso5_copia_binarios.json`; `PRUEBAS/README.md:10-12` |
| 6 | Comprobar que no se ha ejecutado `base_414.py` sobre el árbol 4.15 | S | el script del lanzador (§10.1) | — | Ninguna orden de `base_414.py` sobre la candidata en el script del lanzador | `CLAUDE.md:39`, `README.md:56` |
| 7 | Contrastar la candidata con su manifiesto y hacer la copia limpia | S | §4.2.7 y §5.1 | 0 / 0 | 7762 · 0 · 0 · 0; copia nueva sin `.lo_perfil/` ni `__pycache__` | `PRUEBAS/README.md:11`; `TRASP/INFORME_TRASPASO.md:29-30` |
| 8 | Espacio libre y después `bash verificar_paquete.sh completa`, una vez | LO | §5.1 | 0 | La tabla del §5.2; `RESULTADO GLOBAL: PASA`; 53–60 min | `munger_v2_r1/PROMPT_NUEVA_VENTANA.md:23-26`; `REG/paso8_*` |
| 9 | En la misma copia, `comprobar_entrega_4_14.py` | S (va con bloqueo por prudencia) | §5.3 | **1** | 29/35; las seis FALLA del §5.3 y ninguna otra | `munger_v2_r1/CONTINUIDAD.md:136`; `REG/paso9_comprobar_entrega_4_14.log` |
| 10a | Espacio libre, lista de rutas y limpieza de `pruebas/_v64/` | S | §5.4 | 0 | Rutas registradas; sin `*.xlsx` ni `vigencia/` en `_v64/` | `munger_v2_r1/CONTINUIDAD.md:143`; `REG/paso10_limpieza_rutas.txt` |
| 10b | Controles históricos, salida fuera del árbol | LO (algunos) | §5.3 | 0 el script; el de cada control, en `resumen.md` | La tabla del §5.3: 4.10 39/44 (`.PARTES.txt`); 4.11 33/38 (entorno) con el 4.12 miembro a miembro CUMPLE; el resto, lo observado una vez | `REG/paso10_controles_historicos/resumen.md`; `REG/paso10b_4_8_1_reintento.txt` |
| 11 | Localizar los relevos pendientes del paquete y su regla | S | lectura | — | 13 esperas; ninguna vigente; ninguna se reanuda en su sitio | `munger_v2_r1/CONTINUIDAD.md:144-150`; §7.4 |
| 12 | Copia hermana de `elis_motor_A` (`cp -a`) en la copia de relevos, huellas del original y relanzar con el mismo comando | LO | §7.4 | **10** | Prompts con las rutas actuales; **además**, detección del relevo caducado histórico (`relevos_caducados`, paso 12 repetido, solicitud nueva, `SA-ed5561…` «sustituida»); el original no cambia (huellas antes = después) | `REG/paso12_pipeline_01.txt:1-4`; `munger_v2_r1/CONTINUIDAD.md:145`, `:150-152` |
| 13 | Relevo caducado: en otra copia del estado del paso 12, añadir una línea de prueba a **`fase_c.md`** (archivo del material que el paso 12 no regenera) y relanzar **sin `--desde`** | LO (+ AG en un expediente real) | §7.4 (mismo comando, otra copia) | **10** | `relevos_caducados` con `fase_c.md` cambiado, paso 12 repetido, solicitud nueva y la anterior «sustituida»; el cambio **sigue** en el material refijado | `REG/paso_h9_pipeline.txt:1-4`; `REVT/REVISION_TRASPASO.md:140-143` |
| 14 | H9: en otra copia, cambiar una salida que se vuelque en celdas (`fase_c.json`, `fase_b.json` o `entrada_efectiva.json`) y relanzar sin `--desde` | LO + AG | **[NO DOCUMENTADO]** (§7.3) | — | **Pendiente de verificar.** Se registra a qué paso vuelve y si el cambio llega a las celdas. No se declara resuelto | `EVID/coordinacion/cierre_v2/PROGRAMA.md:40`; `REVT/MEJORAS_MANUAL.md:12` |
| 15 | Fase C: los dos turnos con el mismo agente | AG | — | — | El turno 2 continúa la conversación del turno 1 | `PV2/GUIA_RECORRIDO_SUPERVISADO.md:56` |
| 16 | Auditoría por un agente nuevo, de contexto separado | AG | — | — | APROBADO solo del material fijado vigente. Si no se puede lanzar, se declara que la auditoría no es independiente | `PV2/GUIA_RECORRIDO_SUPERVISADO.md:68`; `munger_v2_r1/CONTINUIDAD.md:153` |
| 17 | La ficha y el informe (también V6.3) muestran `verificacion_entradas` con `apto_para_dinero_real: false` | LO + AG (la ficha final exige la auditoría) | — | — | Bloque presente con el recuento, el modo aplicado y el declarado, y su procedencia; en la ficha provisional ya se ve | `E415/hito2/HITO_2_4_15.md:82-88`; `REG/relevo_copia_base/ficha_provisional.json` |
| 18 | Comprobar que no se adopta ninguna política económica | S | — | — | Ninguna configuración de demostración se presenta como adoptada; no se fija R, θ, λ, probabilidades, k ni umbrales | `PV2/GUIA_RECORRIDO_SUPERVISADO.md:10`; `EVID/coordinacion/cierre_v2/PROGRAMA.md:7` |
| 19 | Informe del receptor y registro (§10.1) | S | §10.1 | 0 (comprobador del registro, salvo los códigos esperados ≠ 0) | Por bloques; hechos, interpretaciones y propuestas separados; lo no ejecutado se marca como no ejecutado; registro y scripts conservados con sus huellas | `EVID/coordinacion/cierre_v2/traspaso/PROMPT_RECEPTOR.md:18-24`, `:28-32` |

- **Paso 13 (mejora 2).** `informe_provisional.md` **no sirve**: el paso 12 lo regenera y el cambio desaparece, aunque se detecte (`REVT/REVISION_TRASPASO.md:138`). `fase_c.md` sí sirve: en el traspaso, su cambio se detectó y quedó dentro del material refijado (`REVT/REVISION_TRASPASO.md:142-143`). Por lectura de `PV2/scripts/cierre_v2.py:31`, otros textos del material que el pipeline no regenera son `fase_a.md`, `fase_b.md` y `extracto_v63.md`; no se han observado. El contenido de la línea de prueba del traspaso no se conservó (`REVT/REVISION_TRASPASO.md:239`). *Propuesta, no probada:* una línea de texto sin comillas ni cifras, porque el paso 12 vuelve a comprobar las citas de `fase_c.md` (`PV2/scripts/verificar_todo.sh:58-60`). Este paso **no prueba H9** (§7.3).
- **Copias de los pasos 13 y 14.** Cada una es una copia aparte (`cp -a`) del estado que dejó el paso 12, como en el traspaso (`TRASP/INFORME_TRASPASO.md:37-38`). Se conservan hasta que el revisor las haya visto: el traspaso las borró, y no se pueden reexaminar las líneas de prueba ni las huellas posteriores (D-3, `REVT/REVISION_TRASPASO.md:236-241`).
- **Qué solo puede comprobarse con LibreOffice:** pasos 8, 10b (en parte), 12, 13, 14 y 17, y el bloque de entorno (`PV2/GUIA_RECORRIDO_SUPERVISADO.md:22`).
- **Qué solo puede comprobarse con agentes reales:** pasos 13 (en un expediente real), 14, 15, 16 y 17. Con agentes simulados solo valen como prueba técnica (`PV2/GUIA_RECORRIDO_SUPERVISADO.md:57`).
- **Condición de la prueba:** el receptor no es quien escribió este manual, y un revisor distinto revisa el resultado (`EVID/coordinacion/cierre_v2/CONTROL.json` → `G-MANUAL.revisor_propuesto`, línea 589 en `acea175`; `CLAUDE.md:33`).

### 10.1 Registro del receptor: comando, código y hora por paso (mejora 5)

**Qué se exige** (`REVT/MEJORAS_MANUAL.md:19`; `REVT/REVISION_TRASPASO.md:281-284`):
- para cada paso, el comando literal, el código de salida y la hora;
- el espacio libre antes de los bloques largos (pasos 8 y 10);
- los scripts improvisados, con su huella (también el del contraste del manifiesto, si se usa uno);
- las huellas del original antes y después del paso 12;
- el informe y la lista de huellas de todo el registro.

Motivo: el registro del 17-nov no conserva transcripción ni la mayoría de los códigos, y varios pasos quedaron autodeclarados (`REVT/REVISION_TRASPASO.md:30`, `:54-75`).

**Herramientas.** `HERR/lanzador_comun.sh` y `HERR/comprobar_registro.py` (procedimiento en `HERR/README.md`; huellas en `HERR/MANIFIESTO_SHA256.txt`). Sus pruebas dan 30 de 30 (`HERR/README.md:49`; `HERR/test_herramientas.out`). Son herramientas del coordinador: no cambian ninguna prueba del producto (`HERR/README.md:55`).
- `iniciar REGISTRO N` crea el registro y su cabecera con la hora de inicio y los N pasos esperados (`HERR/lanzador_comun.sh:3`, `:11-12`).
- `paso NOMBRE SALIDA comando args…` ejecuta el comando, guarda su salida y anota el nombre, **la hora en que termina** y el código (`HERR/lanzador_comun.sh:4`, `:13-14`). La hora de inicio de un paso es la de fin del anterior, o la de la cabecera.
- `en_dir NOMBRE DIRECTORIO` anota el `cd` como paso; si falla, código 125, y los pasos siguientes siguen anotándose (`HERR/lanzador_comun.sh:5`, `:15`). Un `cd` fallido deja los pasos siguientes en otra carpeta: el receptor se detiene si lo ve.
- `terminar` escribe el resumen y sale con 0, 1 (algún paso ≠ 0) o 3 (pasos ejecutados ≠ esperados) (`HERR/lanzador_comun.sh:7`, `:17-20`).
- `comprobar_registro.py REGISTRO --esperados N` sale con 0, 1 (lista los pasos ≠ 0), 2 (registro mal formado) o 3 (recuento distinto) (`HERR/comprobar_registro.py:3-11`).

**Cómo cubre cada exigencia.**
- *Comando:* el registro anota nombre, hora y código, **no el texto del comando** (`HERR/lanzador_comun.sh:13`). La transcripción es el propio script del lanzador, que el receptor conserva con su huella en el registro. El nombre de cada paso no puede tener espacios (`HERR/comprobar_registro.py:25`).
- *Código y hora:* los anota `paso`.
- *Códigos esperados distintos de 0:* `terminar` y `comprobar_registro.py` darán 1 si un paso correcto sale con 1 o 10 (pasos 9, las repeticiones del 10b, 12 y 13; el 14 no tiene código esperado). No se cambian las herramientas para ocultarlo: `comprobar_registro.py` lista cada paso con su código (`HERR/comprobar_registro.py:103-104`), y el receptor contrasta esa lista con la columna «Código esperado» del §10. Cualquier otro código se informa tal cual (`HERR/README.md:45`).
- *Controles históricos:* el código 0 de `controles_historicos_4_13.py` no dice nada de los controles (§5.3); se lee `resumen.md`.
- *Órdenes con tuberías o con `;`* (la limpieza del §5.4, el contraste con `sha256sum -c`): `paso` ejecuta un solo comando con sus argumentos (`HERR/lanzador_comun.sh:14`). Para una tubería haría falta `bash -c '…'`, y entonces el código es el de la tubería. **[NO DOCUMENTADO]**: no probado.

**Plantilla propuesta.** **[NO DOCUMENTADO]**: aplica la sintaxis de `HERR/README.md:29-35` y de `HERR/lanzador_comun.sh:2-7` a comandos que se probaron sueltos en el traspaso (§4–§7). La combinación no se ha probado. Los `<…>` son rutas del receptor.

```bash
#!/bin/bash
# lanzador_traspaso.sh · conservar este archivo y su huella: es la transcripción de los comandos
source <evid>/coordinacion/cierre_v2/herramientas/lanzador_comun.sh
R=<trabajo>/registro
LOCK=<e_work>/libreoffice.lock
iniciar "$R/registro_lanzador.log" 5
en_dir copia_limpia <trabajo>/copia_limpia_1/munger_v2_r1
paso df_antes_p08 "$R/df_antes_p08.txt" df -h <trabajo> "${TMPDIR:-/tmp}"
paso p08_verificar_completa "$R/paso8_verificar_paquete_completa.log" flock -x "$LOCK" bash verificar_paquete.sh completa
paso p09_control_4_14 "$R/paso9_comprobar_entrega_4_14.log" flock -x "$LOCK" python3 -I -B personaje_v2/empresas_v2_correcciones/2026-11_Vidrala_ensayo_4_14/scripts/comprobar_entrega_4_14.py
paso p10_historicos "$R/paso10_salida.txt" flock -x "$LOCK" python3 -I -B personaje_v2/empresas_v2_correcciones/2026-11_Vidrala_ensayo_4_13/scripts/controles_historicos_4_13.py "$R/paso10_controles_historicos"
terminar
```

- `df -h` es **[NO DOCUMENTADO]**: el traspaso no registró ningún `df` (`REVT/REVISION_TRASPASO.md:67-68`).
- La limpieza del §5.4 va entre `p09` y `p10`, con su lista de rutas; en esta plantilla no se incluye, porque su forma dentro de `paso` no está probada.
- Comprobación del registro. **[NO DOCUMENTADO]**, *adaptado de* `HERR/README.md:40-41`, que usa `lanzador.sh`, `"$REGISTRO"` y 26 pasos; aquí lleva el nombre, el registro y los 5 pasos de esta plantilla. No se ha ejecutado:

      bash lanzador_traspaso.sh; rc_lanzador=$?
      python3 -I <evid>/coordinacion/cierre_v2/herramientas/comprobar_registro.py <trabajo>/registro/registro_lanzador.log --esperados 5; rc_registro=$?

  Con esta plantilla, lo esperado es `rc_lanzador` = 1 y `RESULTADO 1 · pasos con código distinto de 0: p09_control_4_14=1`, porque el paso 9 correcto sale con 1. Cualquier otro paso en la lista, un 2 o un 3 es una discrepancia.
- **Huellas del registro.** Se calculan al final, cuando ya no cambia ningún archivo, y la lista no se incluye a sí misma. En el traspaso, `SHA256_REGISTRO.txt` se listó con la huella del archivo vacío (`REVT/REVISION_TRASPASO.md:45`). Si se sustituyen rutas locales por marcadores, la lista se rehace después y se dice (`REVT/REVISION_TRASPASO.md:86-88`). El comando **[NO DOCUMENTADO]**.

## 11. Pendientes que el operador no puede cerrar

- **F1 (otra tarea).** Ver §1.
- **Regeneración y auditoría** de Viscofan, Vidrala y Elis con extractor y revisor reales; sin firmas simuladas (`E415/hito2/PUNTO_DE_RECUPERACION.md:39`).
- **H9**, **U1** y **U6 (a)** (`E415/hito2/PUNTO_DE_RECUPERACION.md:33-38`). H9 sin procedimiento (§7.3).
- **Control de la 4.14**, 29/35: no se da por superado (`E415/hito2/PUNTO_DE_RECUPERACION.md:42`).
- **Control 4.11:** la versión de zlib y `comparar_zip.py` sobre su reconstrucción (§5.3).
- **CONTINUIDAD §2.5:** la frase sobre `_v64/` (C-14; afecta al 4.8 y al 4.8.1), en una corrección documental aparte (`PROPUESTA_CONTINUIDAD_2_5.md`).
- Las pruebas de la candidata son del autor de la candidata, no una revisión independiente (`PRUEBAS/README.md:3`).

## 12. Registro de [NO DOCUMENTADO] y [CONTRADICCIÓN]

### 12.1 [NO DOCUMENTADO]

| Id | Qué falta | Estado en esta revisión | Dónde |
|---|---|---|---|
| N-01 | Copia de los 1008 binarios y qué hacer si uno difiere | **Comando dado** (probado en el traspaso, autodeclarado, §4.2.6). Qué hacer si uno difiere: sigue sin documentar | §4.2.6 |
| N-02 | Contraste independiente del manifiesto | **Comando dado** (probado en la preparación F1, no en el traspaso). No detecta archivos de más | §4.2.7 |
| N-03 | Copia limpia | **Comando dado** (probado en el traspaso, autodeclarado) | §5.1 |
| N-04 | Resultado esperado de los controles históricos sobre el árbol 4.15 | **Dado:** 4.10 y 4.11 explicados; el resto, observado una vez, no fijado | §5.3 |
| N-05 | Espacio en disco por la vía del repositorio | **Parcial:** observado (pico de ≈9,8 GB, fallo con 8,4 GB libres, éxito con 13 GB). Mínimo sin fijar | §3.2 |
| N-06 | Ruta del bloqueo y comando `flock` completo | **Dado** (`<e_work>/libreoffice.lock`). Falta confirmar que la comparten todas las sesiones; `soffice --version` con `flock`, no probado | §2.1 |
| N-07 | Comando que compruebe si la sesión puede lanzar agentes de contexto separado | Sin documentar | §3.1 |
| N-08 | Procedimiento de H9 | Sin documentar. Se dice qué archivos cambiar, no cómo ni qué esperar | §7.3 |
| N-09 | Cómo resolver la parada del modo «estricta» | **Cerrado por la guía corregida** (`PV2/GUIA_RECORRIDO_SUPERVISADO.md:51`) | §6.1 |
| N-10 | Versiones mínimas de LibreOffice y de las bibliotecas | Sin documentar; además, versión de zlib | §3.1 |
| N-11 | Clonado y huella del ZIP | Huella: **dada** (probada en el traspaso, autodeclarado). Clonado: sin documentar | §4.2.1, §4.2.3 |
| N-12 | Si `comprobar_entrega_4_14.py` usa LibreOffice | **Cerrado por lectura:** no lo usa | §5.3 |
| N-13 | Creación de `.downloads/` antes de la descarga por la API REST | Sin documentar | §4.2.2 |
| N-14 | Comando para comprobar el HEAD de la candidata | Sin documentar | §4.2.5 |
| N-15 | Comandos de la copia de relevos y de las huellas del original antes y después del paso 12 | Sin documentar | §7.4 |
| N-16 | Efecto de la limpieza de `_v64/` en los otros 18 controles, si se hace antes de la pasada completa | No observado. Por lectura de los 19: solo el 4.8 y el 4.8.1 copian `_v64/`; el 4.9 lo recorre sin efecto; el 4.11, el 4.12 y el 4.13 lo excluyen | §3.2, §5.3 |
| N-17 | `df`, `find … -print`, `bash -c` dentro de `paso` y la plantilla del lanzador con comandos del producto | Propuestas no probadas | §5.4, §10.1 |
| N-18 | Precedencia formal entre `AGENTS.md` y `PROMPT_RECEPTOR.md` | Sin documentar; interpretación en §2 | §2 |
| N-19 | Comando del `diff` de las salidas históricas con las referencias del árbol 4.14 | Sin documentar | §5.3 |
| N-20 | Repetición suelta del control 4.8 si falla por espacio | Forma adaptada de `controles_historicos_4_13.py:59`; no probada | §5.3 |

### 12.2 [CONTRADICCIÓN]

| Id | Fuente A | Fuente B | Estado en `b129b36` |
|---|---|---|---|
| C-01 | En `3149128`: `README.md:1-7` y `CLAUDE.md:1`: «rama de revisión 4.15, hito 1», «conserva exactamente el código recibido» | `munger_v2_r1/VERSION:1`: «4.15 · hito 2» | **Resuelta en `b129b36`** (G-RAIZ): `README.md:1` «Candidata de integración técnica: 4.15, hito 2 (pendiente de revisión externa)»; `README.md:7` «Esta rama conserva el código recibido del hito 2»; `CLAUDE.md:1` «entrega 4.15 · hito 2 (`munger_v2_r1/VERSION`)» |
| C-02 | En `3149128`: `README.md:17`, `CLAUDE.md:35`, `docs/MIGRATION_STATUS.json:9,12-13`: las correcciones «no están incorporadas» | `E415/hito2/HITO_2_4_15.md:1-10` | **Resuelta en `b129b36`** (G-RAIZ): `README.md:17` «Las correcciones técnicas de los hitos 1 y 2 de la 4.15 están en el código de la candidata»; `CLAUDE.md:37` «La entrega del hito 2 de la 4.15 ya está importada en esta candidata»; `docs/MIGRATION_STATUS.json:9` «La entrega 4.15 · hito 2 de Claude está importada». Lo que sigue sin importar es F1 y las demás correcciones en curso (`README.md:17`, `CLAUDE.md:37`, `docs/MIGRATION_STATUS.json:12-13`) |
| C-03 | `munger_v2_r1/PROMPT_NUEVA_VENTANA.md:19`: rama `claude/hopeful-bardeen-qap6y0` | `EVID/coordinacion/cierre_v2/PROGRAMA.md:12`: candidata `integracion/candidata-cierre-v2` | **Parcial:** `munger_v2_r1/CONTINUIDAD.md:6` ya nombra las dos; el mensaje de arranque no cambia |
| C-04 | CONTINUIDAD §12: adjuntar el ZIP de la 4.14 | `munger_v2_r1/PROMPT_NUEVA_VENTANA.md:3` | **Resuelta** (`munger_v2_r1/CONTINUIDAD.md:391-395`) |
| C-05 | `munger_v2_r1/CONTINUIDAD.md:375` y `docs/RECEPCION_ENTREGA_CLAUDE.md:7-9`: toda entrega es un ZIP completo | `E415/hito2/HITO_2_4_15.md:183-187`: rama y paquete de cambios | **Parcial:** `:375` registra el hecho, pero mantiene la regla |
| C-06 | CONTINUIDAD §2.1: «Descomprimir el ZIP» | `README.md:5` | **Resuelta** (`munger_v2_r1/CONTINUIDAD.md:109-114`) |
| C-07 | CONTINUIDAD §2: «las doce», «las diez» | `munger_v2_r1/verificar_paquete.sh:85-330`: trece | **Resuelta** (`munger_v2_r1/CONTINUIDAD.md:135`, `:137`) |
| C-08 | Regla 11.4: «las diez baterías … (198)» | quince; mínimo 199 | **Resuelta** (`munger_v2_r1/CONTINUIDAD.md:376`) |
| C-09 | CONTINUIDAD: I19/I20 como límites vigentes | `E415/hito2/HITO_2_4_15.md:82-93` | **Resuelta** (`munger_v2_r1/CONTINUIDAD.md:196`, `:292`, `:356-357`) |
| C-10 | El LEEME de la 4.14 «sustituye, para este árbol» | Describe el árbol 4.14 | **Reconocida** en `munger_v2_r1/CONTINUIDAD.md:136`; este manual da lo observado (§5.3) |
| C-11 | `munger_v2_r1/CONTINUIDAD.md:115`: 25–45 min | `PV2/GUIA_RECORRIDO_SUPERVISADO.md:19`: 60 min en la candidata; traspaso 53 min 20 s | **Sigue**, menor |
| C-12 | `test_integracion_v64.py` (198) | 199 | **Resuelta** (`munger_v2_r1/CONTINUIDAD.md:199`) |
| C-13 | Guía: I19 e I20 como límites | Hito 2 | **Resuelta** (`PV2/GUIA_RECORRIDO_SUPERVISADO.md:117`, `:136-141`) |
| **C-14** | `munger_v2_r1/CONTINUIDAD.md:143`: «los controles no recorren `_v64/`» | `comprobar_entrega_4_8_1.py:76-77` y `comprobar_entrega_4_8.py:60`: copian `personaje_v2/` con `pruebas/_v64/`; `comprobar_entrega_4_9.py:84` lo recorre sin efecto | **Nueva**, del producto. Propuesta en `PROPUESTA_CONTINUIDAD_2_5.md` |
| **C-15** | `munger_v2_r1/CONTINUIDAD.md:151`: el relanzamiento «sale con código 10 sin hacer nada más» | `munger_v2_r1/CONTINUIDAD.md:152` y `:145`; `REG/paso12_pipeline_01.txt:1-4` | **Nueva**, del producto, menor |
| **C-16** | `PV2/GUIA_RECORRIDO_SUPERVISADO.md:141`: volver al paso 12 «no basta» y, en la misma línea, «está pendiente de verificar por cambio afectado» | `E415/hito2/HITO_2_4_15.md:92`: «habría que volver al paso que las consume»; `EVID/coordinacion/cierre_v2/PROGRAMA.md:40`: pendiente de verificar | **Nueva**, del producto, menor |

### 12.3 Estado de `CONTRADICCIONES_GUIA.md` (escrito para `957af65`) en `b129b36`

- **G-1 a G-9** (guía histórica): corregidas por G-DOCS. G-1 → `PV2/GUIA_RECORRIDO_SUPERVISADO.md:136-141`; G-2 → `:117`; G-3 → `:111-115`; G-4 → `:103-110`; G-5 → `:121-124`; G-6 → `:73`; G-7 → `:1-3`; G-8 → `:16-21` (la copia de los binarios sigue sin comando en el producto; aquí, §4.2.6); G-9 → `:51`.
- **O-1 a O-11** (CONTINUIDAD): resueltas O-1 a O-9 (`munger_v2_r1/CONTINUIDAD.md:356`, `:357`, `:196`, `:292`, `:135`, `:137`, `:376`, `:199`, `:391-395`, `:109-114`); O-10 parcial (C-05); O-11 reconocida (C-10).
- **O-12 y O-13** (raíz): resueltas en `b129b36` por G-RAIZ, como C-01 y C-02. **O-14** (mensaje de arranque): sigue como C-03 (parcial).
- **O-15 a O-18** (documentos históricos con aviso): sin cambios; siguen valiendo como avisos.
- Ese documento no se reescribe aquí. Un receptor de `b129b36` no aplica sus filas «no es cierto» sin mirar antes este apartado.

## 13. Fuentes leídas

**Producto, candidata `b129b36`.** SHA-256 abreviados (16 hex), calculados al leerlos con `git show b129b36:<ruta>`. Los que cambiaron con G-DOCS van marcados con *; los tres que cambiaron con G-RAIZ, con † (entre paréntesis, su prefijo en `3149128`). Todos los demás son iguales en `3149128` y en `b129b36`.

| Archivo | SHA-256 (prefijo) |
|---|---|
| `README.md` † | `3a13fd25d490bd32` (`d74809472d2f239e`) |
| `CLAUDE.md` † | `dddc84fbc4985cdb` (`d41ad7a19a1afea3`) |
| `.gitignore` | `e2cad29821487bbd` |
| `docs/RECEPCION_ENTREGA_CLAUDE.md` | `c8a999643828e649` |
| `docs/MIGRATION_STATUS.json` † | `77a499802c1da894` (`cf9e7927c5427b97`) |
| `tools/base_414.py` | `56a3e62f4d186275` |
| `munger_v2_r1/CONTINUIDAD.md` * | `56e37708c24cf6bc` |
| `munger_v2_r1/MANIFIESTO_SHA256.txt` * | `1b988e3a135f4209` |
| `munger_v2_r1/CAMBIOS_ARCHIVOS.txt` * | `c8ce2f59d841c290` |
| `munger_v2_r1/verificar_paquete.sh` | `f304ededb0950be1` |
| `munger_v2_r1/VERSION` | `f92618d605ccdff8` |
| `munger_v2_r1/PROMPT_NUEVA_VENTANA.md` | `ed804aab69a5526b` |
| `PV2/GUIA_RECORRIDO_SUPERVISADO.md` * | `2861e7f1ed1ac0f9` |
| `PV2/README_v2.md` | `c5d6f2ff37c20948` |
| `PV2/PROMPT_CLAUDE_CODE.md` | `988e52c781015e49` |
| `PV2/scripts/comprobar_entorno.sh` | `a9508c32033aac1d` |
| `PV2/scripts/pipeline.py` | `3999a95afed93c76` |
| `PV2/scripts/ficha.py` | `c3ba3d86a678313b` |
| `PV2/scripts/cierre_v2.py` | `6d89a81a0f2d73e9` |
| `PV2/scripts/verificar_todo.sh` | `dc5d049820a40104` |
| `PV2/scripts/cambiar_base.py` | `2661f9baa48ed1ea` |
| `PV2/scripts/verificacion_entradas.py` | `4b00aa2a42ae4574` |
| `PV2/pruebas/test_relevo_i19_415.py` | `663a922555abbe5c` |
| `E415/HITO_1_4_15.md` | `f1697a9468730535` |
| `E415/hito2/HITO_2_4_15.md` | `8b1a19d99cb75756` |
| `E415/hito2/PUNTO_DE_RECUPERACION.md` | `cf08466e1447f0c8` |
| `E414/documentacion_cierre_4_14/HITO_2.md` | `367932cca24b4300` |
| `E414/documentacion_cierre_4_14/INCIDENCIAS_4_14.md` | `bb141a50e38ee27b` |
| `E414/documentacion_cierre_4_14/traspaso/INFORME_TRASPASO.md` | `eb6e494a7707f88b` |
| `E414/documentacion_cierre_4_14/traspaso/LEEME_TRASPASO.md` | `ef1bf2548f25e18a` |
| `E414/resultados/LEEME_CONTROLES_HISTORICOS_4_14.md` | `34212e1cefd2a010` |
| `E414/elis_motor_A/LEEME_ELIS_MOTOR_A.md` | `19f9fc8894cf6283` |
| `E414/scripts/comprobar_entrega_4_14.py` | `5fd59314910f5123` |
| `…/2026-11_Vidrala_ensayo_4_13/scripts/controles_historicos_4_13.py` | `53daa8f2fdd537b4` |
| `…/2026-11_Vidrala_ensayo_4_8/scripts/comprobar_entrega_4_8.py` | `1ed5fd6ba4e2f34a` |
| `…/2026-11_Vidrala_ensayo_4_8/scripts/reproducir_xa_xc.py` | `f848d4a9f345379b` |
| `…/2026-11_Vidrala_ensayo_4_8_1/scripts/comprobar_entrega_4_8_1.py` | `fe912957e9cfaba9` |
| `…/2026-11_Vidrala_ensayo_4_9/scripts/comprobar_entrega_4_9.py` | `ee998bbf07370987` |
| `…/2026-11_Vidrala_ensayo_4_10/scripts/comprobar_entrega_4_10.py` | `0c48ffa1033ae10f` |
| `…/2026-11_Vidrala_ensayo_4_11/scripts/comprobar_entrega_4_11.py` | `987be84638f72b0b` |
| `…/2026-11_Vidrala_ensayo_4_12/scripts/comprobar_entrega_4_12.py` | `b218619edf2c27a0` |
| `…/2026-11_Vidrala_ensayo_4_13/scripts/comprobar_entrega_4_13.py` | `8559c88c705616dd` |

**Producto, `origin/main` (`d69d483`)**, para las citas del §4.2.1–4: `README.md` `d52f322abfb0e502`. `tools/base_414.py` y `.gitignore` son iguales que en la candidata.

**Evidencias, rama `coordinacion/cierre-v2` @ `acea175`** (la v2 se escribió sobre `6889b02`; entre los dos, de lo citado solo cambia `CONTROL.json`). `PROGRAMA.md` e `INTEGRACION.md` no cambian desde `9871f59` (prefijos `03730269609b5aec` y `57ab214f5a9f0ba9`); `PRUEBAS/README.md` tampoco (`fd349e6d5ab43295`). `CONTROL.json` (`a6e982a49149b52a` en `acea175`) se cita por tarea y campo, con su línea en `acea175`. La revisión de la v2 está en `EVID/coordinacion/cierre_v2/revisiones_coordinador/MANUAL_v2_ef36ab1/` (`REVISION_MANUAL_v2_ef36ab1.md`, `CORRECCION_MANUAL_v3.md` y las sondas S01–S16). El sondeo de literales de la v3 está en `EVID/coordinacion/cierre_v2/manual/sondeo_literales_v3/`: `sondeo_literales_v3.py` (`34d56aabfb8069674494cf7a549517fea21acd5d52eed47e422e8fbc8107f226`) y `salida.txt` (`4d0bf6a066590e1c94593cfeed20deaab1521778bc0f0a5ac583c9a5971b149f`). Para la v4: `CONTROL.json` en `2c988b8` (`5be39cbc516e27d7`), la revisión de la v3 (`EVID/coordinacion/cierre_v2/revisiones_coordinador/MANUAL_v3_88144b5/REVISION_MANUAL_v3.md`, `f036bf834272258e`) y la de G-RAIZ (`EVID/coordinacion/cierre_v2/revisiones_coordinador/G-RAIZ_e813fe6/REVISION_G-RAIZ_e813fe6.md`, `3a434303a3c55a76`). El traspaso, su revisión y las herramientas tienen sus propios manifiestos: `TRASP/MANIFIESTO_SHA256.txt`, `REVT/MANIFIESTO_SHA256.txt` y `HERR/MANIFIESTO_SHA256.txt`. Huellas de los scripts que se proponen ejecutar: `TRASP/scripts_receptor/copiar_binarios.py` `8fb5b9bcfd242743…`, `HERR/lanzador_comun.sh` `94f45a6e07f737d8…` y `HERR/comprobar_registro.py` `1ec39613baa14761…`.

**Preparación F1** (`F1PREP/`, rama `auditoria/economica-f1-frente-e` @ `03e7851`, también en `origin`): `scripts/copiar_binarios_a_b.py` `0107a4d76a81c727…` (= `F1PREP/INDICE.md:26`), `log_base414.txt` `53c82e93cc2c0d74…` (= `F1PREP/INDICE.md:14`), `preparacion.json` `7a31775e0ee9f032…` (= `F1PREP/INDICE.md:12`).

**Observación del entorno de lectura (hecho, comprobado de nuevo al escribir la revisión 4).** El worktree leído de la candidata (`<candidata>`, HEAD `b129b36f0aaf7e705fd206efd743fc01a9e96c10`, igual que `integracion/candidata-cierre-v2` y `origin/integracion/candidata-cierre-v2` según `git rev-parse`) **sí tiene los binarios materializados**. Lo que lo muestra:
- desde `munger_v2_r1/`, `tail -n +2 MANIFIESTO_SHA256.txt | sha256sum -c --quiet` sale con 0 sobre las 7762 entradas (la orden «probada en la preparación F1 del 15-nov» del §4.2.7);
- `git status --short` da 0 líneas, pero `git status --short --ignored | wc -l` da 682: 591 archivos y 91 carpetas ignorados;
- hay 71 PDF en `munger_v2_r1/` (`find munger_v2_r1 -name '*.pdf' | wc -l`), ignorados por `.gitignore:2` (`*.pdf`);
- los 83 JSON están en `info/exclude` del directorio Git común (`git rev-parse --git-common-dir`): 90 líneas, de las que 83 son esas rutas y 7, comentarios. Por eso no salen como «sin seguimiento».

Estas órdenes de lectura son de este borrador: como paso del receptor, **[NO DOCUMENTADO]**, salvo el contraste del manifiesto. Son las mismas cifras que dio la revisión 3 sobre `3149128` y que obtuvieron la revisión de la v2 (`EVID/coordinacion/cierre_v2/revisiones_coordinador/MANUAL_v2_ef36ab1/sondas/S12_entorno_candidata.txt`) y la de la v3 (`EVID/coordinacion/cierre_v2/revisiones_coordinador/MANUAL_v3_88144b5/sondas/S03_M2_entorno_candidata.txt`). Este borrador no ha modificado ningún repositorio.
