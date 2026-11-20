# Informe de la prueba de traspaso (T-TRASPASO) · candidata `integracion/candidata-cierre-v2` @ 957af65

**Receptor:** agente sin historial del proyecto (Claude Code, Opus 5.5), sesión del 17-nov-2026. No ha escrito el manual ni la candidata. **No es una valoración ni una aprobación.** El producto es experimental supervisado y **no es apto para dinero real**. Superar los controles de software no acredita aptitud.

**Instrucción seguida:** `coordinacion/cierre_v2/traspaso/PROMPT_RECEPTOR.md` de `jluisplagos/munger-v2-evidencias-mistral`, rama `coordinacion/cierre-v2`, commit `788f25c73af698709d9b550b132780c86f7e203d`.
**Manual usado:** `coordinacion/cierre_v2/manual/MANUAL_OPERATIVO_957af65.md` (SHA-256 `6ed65dce0753ed4a298e451d0f25979843214a0bb35cc58f722eaef0c888aeb9`) y `CONTRADICCIONES_GUIA.md` (`88e69671141b585d8bdfcb5e2e5ba8221463c37fbe1032f4e763680b93814425`). Las dos huellas coinciden con `manual/MANIFIESTO_SHA256.txt`.

**Carpeta de trabajo:** `<traspaso>/`, creada vacía a las 08:41:22 UTC. No se ha usado ninguna otra carpeta de `<home>` como fuente. Registros en `registro/` y huellas de todos ellos en `registro/SHA256_REGISTRO.txt`.

**Entorno (hechos):** Python 3.13.18, LibreOffice 24.2.7.2, pdftotext 24.02.0, openpyxl 3.1.5, Bash 5.2.21 y `gh` autenticado. `HOME=/root`. Bloqueo de LibreOffice: `<e_work>/libreoffice.lock`, con `flock -x`. **No se han modificado repositorios remotos**: ni commit, ni push, ni subidas. Tampoco se han cambiado credenciales.

Convenciones: se separan **hechos**, *interpretaciones* y ***propuestas***. Se habla de la persona responsable en tercera persona.

---

## 1. Tabla por paso (lista del §10 del manual)

Raíces: `MAIN` = `<traspaso>/munger-v2` (clon de `main`, `d69d483`) · `CAND` = worktree `…/candidata` · `CL1` = copia limpia `…/copia_limpia_1/munger_v2_r1` · `CR` = copia para relevos `…/copia_relevo/munger_v2_r1` · `E414` = `personaje_v2/empresas_v2_correcciones/2026-11_Vidrala_ensayo_4_14`.

| # | Comando literal (cwd) | Código | Resultado (hecho) | ¿Coincide con el manual? |
|---|---|---|---|---|
| 1 | Lectura con `git show 957af65:<archivo>` de `README.md`, `CLAUDE.md`, `munger_v2_r1/VERSION`, `CONTINUIDAD.md`, `PROMPT_NUEVA_VENTANA.md`, `HITO_2_4_15.md` y `PUNTO_DE_RECUPERACION.md` | — | `VERSION`: «entrega 4.15 · hito 2», «no apto para decisiones con dinero real». Pendientes: F1, regeneración y auditoría de Viscofan, Vidrala y Elis, H9/I19, U1, U6 (a) y control 4.14 29/35. `README.md:1` y `CLAUDE.md:1` dicen «hito 1». Los 10 prefijos SHA-256 del §13 que se comprobaron coinciden | **Sí** |
| 2a | `gh release download base-4.14 --repo jluisplagos/munger-v2 --pattern munger_v2_r1_entrega4.14_cierre_verificacion_entradas.zip --dir .downloads` (MAIN) | 1 | 403: «GitHub GraphQL is not available from Claude Code sessions» | Sí: el manual prevé que falle |
| 2b | `gh api -H "Accept: application/octet-stream" repos/jluisplagos/munger-v2/releases/assets/750814858 > .downloads/munger_v2_r1_entrega4.14_cierre_verificacion_entradas.zip` (MAIN) y después `stat -c '%s %n'` y `sha256sum` | 0 / 0 | 1130912246 bytes; SHA-256 `bb51942cefb848e409a4828e3faeb70f94aa4d29af39cda6d90cd0a97cb7b93e`. Duración: 41 s | **Sí**. La huella se calculó con `sha256sum`, el comando de CONTINUIDAD; en esta vía **[NO DOCUMENTADO]** (N-11) |
| 3 | `python3 tools/base_414.py materialize --source .downloads/…zip` y `python3 tools/base_414.py verify --report docs/VERIFICACION_BASE_COMPLETA_LOCAL.json` (MAIN) | 0 / 0 | «Archivos recuperados: 1008»; `verified 6798 · expected 6798 · missing 0 · changed 0 · complete true` | **Sí**. Se usó `python3` en lugar de `python`; aquí los dos son 3.13. Ver A-3 sobre el informe escrito en `docs/` |
| 4 | `git worktree add ../candidata integracion/candidata-cierre-v2` (MAIN) | 0 | HEAD `957af652cdc3bef3d67e8623c9572138bac685e9`; `VERSION` «4.15 · hito 2»; `origin/integracion/candidata-cierre-v2` = 957af65 | **Sí**. El comando **[NO DOCUMENTADO]**: se improvisó un worktree, como en las pruebas de la candidata |
| 5 | `python3 -I scripts_receptor/copiar_binarios.py munger-v2 candidata registro/paso5_copia_binarios.json` (script propio, **improvisado**) | 0 | `copiados 1008 · existentes_iguales 0 · distintos 0 · fallos 0`. Después, `git status` en CAND da 83 JSON sin seguimiento y ningún cambio versionado | **Sí**. Procedimiento **[NO DOCUMENTADO]** (N-01). El script lee `baselines/4.14.json`, `storage == release_asset` y el prefijo `munger_v2_r1/`. Comprueba el SHA-256 del origen, no sobrescribe nunca y comprueba el SHA-256 del destino |
| 6 | Revisión del propio registro de comandos | — | `base_414.py` solo se ejecutó en MAIN. En CAND, ninguna orden. `git diff` vacío en MAIN y CAND | **Sí** |
| 7 | `mkdir copia_limpia_1 && cp -a candidata/munger_v2_r1 copia_limpia_1/` | 0 | 0 `__pycache__` y 0 `.lo_perfil`; 1,5 GB | Sí. El comando **[NO DOCUMENTADO]** (N-03): `cp -a`, improvisado |
| 7b | Contraste independiente de CAND con `munger_v2_r1/MANIFIESTO_SHA256.txt`, en Python propio con la misma lógica que `verificar_paquete.sh` (**improvisado**, N-02) | 0 | 7762 en el manifiesto · 0 modificados · 0 ausentes · 0 de más | **Sí** |
| 8 | `flock -x <e_work>/libreoffice.lock bash verificar_paquete.sh completa` (CL1) | **0** | **RESULTADO GLOBAL: PASA**. Recuentos: 7762·0·0·0; entorno, PASA; piloto, 35 CUMPLEN; 114/114; 30/30 (faltan 0, nuevas 0); 59/59; 27/27; 33/33; 190/190; 62/62; 5/5; 199/199; 78/78; 103/103; 55/55; 28/28; 45/45; 55/55. De 08:44:07 a 09:37:27 UTC (53 min 20 s). El registro es **idéntico byte a byte** al de las pruebas de la candidata: el SHA-256 de los dos es `23fd7aa1…57d4ac` | **Sí**, en los 18 bloques. La duración queda fuera de los 25–45 min de la documentación (C-11) |
| 9 | `flock -x <e_work>/libreoffice.lock python3 -I -B personaje_v2/empresas_v2_correcciones/2026-11_Vidrala_ensayo_4_14/scripts/comprobar_entrega_4_14.py` (CL1, después del 8) | 1 | **29/35**. Las seis FALLA son las esperadas: tres verificaciones de entradas, «0 de 321/311/292», y tres fechas de archivo. El `diff` con `PRUEBAS/comprobar_entrega_4_14.log` solo difiere en las 3 marcas de tiempo del checkout (08:43:08 en lugar de 20:54:07) | **Sí**. Por lectura del script, no llama a LibreOffice (no usa `subprocess` ni `soffice`). Aun así se ejecutó con `flock` por prudencia (N-12) |
| 10 | `flock -x … python3 -I -B personaje_v2/empresas_v2_correcciones/2026-11_Vidrala_ensayo_4_13/scripts/controles_historicos_4_13.py <traspaso>/registro/paso10_controles_historicos` (CL1). El comando sale del LEEME de la 4.14, no del manual. Carpeta de salida fuera del árbol, por decisión propia | 0 (el script) | De 09:38:05 a 10:05:57 (27 min 52 s). **El control 4.8.1 se interrumpió por falta de espacio** (`[Errno 28] No space left on device` al copiar el árbol en `/tmp/control481_*`). Al empezar quedaban unos 8,4 GB libres | Resultado esperado **[NO DOCUMENTADO]** (N-04). Se registra sin calificarlo. El fallo de espacio no lo prevé el manual: ver A-6 |
| 10b | Limpieza según `CONTINUIDAD.md` §2.5: `find …/pruebas/_v64 -name '*.xlsx' -not -path '…/vigencia/*' -delete; rm -rf …/_v64/vigencia`, y borrado del ZIP local ya verificado. Rutas en `registro/paso10_limpieza_rutas.txt`. Después, `flock -x … python3 -I -B …/2026-11_Vidrala_ensayo_4_8_1/scripts/comprobar_entrega_4_8_1.py` (CL1) | 1 | Espacio libre: 13 GB. 4.8.1: **25 de 30**. De 10:07:09 a 10:12:21 | **Improvisado.** 25/30 es lo mismo que el LEEME 4.14 da para el árbol 4.14 |
| 11 | Lectura de los `estado_pipeline.json` (`esperando`) de CAND | — | En `E414`: `elis_motor_A/Elis`, paso 13; `viscofan/Viscofan`, paso 13; `vidrala/Vidrala`, paso 13; `vidrala_decisiones_INVALIDO…/Vidrala`, paso 6. Los tres finales (`*_decisiones`) están en el paso 14. Hay más esperas que no menciona el manual: copias `antecedentes/heredados` de la 4.14 y expedientes de la 4.10, 4.10.1 y 4.12 | **Sí**: ninguno es vigente y ninguno se reanuda en su sitio. Ver A-10 |
| 12 | `cp -a elis_motor_A elis_motor_A_relevo_receptor` (CR/E414; `diff -r`, diferencia 0) y después `flock -x … python3 personaje_v2/scripts/pipeline.py personaje_v2/…/elis_motor_A_relevo_receptor/Elis --config personaje_v2/config_v2.json` (CR) | **10** | Prompts regenerados con las rutas actuales: las 6 rutas `/home/claude/trabajo_4_14/…` pasan a ser `<traspaso>/copia_relevo/…`. El original `elis_motor_A` no cambia: las 126 huellas son iguales antes y después. **Además**, el código 4.15 detecta el relevo caducado histórico: `relevos_caducados` con fijado `9e1a725d…`, vigente `72f855cf…` y cambiado `verificacion_entradas.json`; repite el paso 12 («0 de 292», apta: no); solicitud nueva `SA-4bb1526435a31a51` del material `4d9ee9b6…`; `SA-ed5561…` queda «sustituida» | **Sí**: código 10, prompts regenerados, original sin cambios. «El mismo comando» **[NO DOCUMENTADO]**: `--config personaje_v2/config_v2.json` se dedujo del LEEME del expediente (V6.3) y del §6.3 |
| 13 | `cp -a` del estado anterior a `…_p13`; con la auditoría pedida (`SA-4bb…`), se añade una línea a `informe_provisional.md` (archivo del material) y se relanza el mismo comando **sin `--desde`** | **10** | `relevos_caducados` con fijado `4d9ee9b6…`, vigente `88ccc612…` y cambiado `informe_provisional.md`; paso 12 repetido; solicitud nueva `SA-3419ec21eb14c04f` (material `b79ad7da…`); `SA-4bb…` «sustituida». El paso 12 regenera `informe_provisional.md` y el cambio de prueba desaparece | **Sí** en la parte que solo exige LibreOffice. La parte con agentes en un expediente real: **no ejecutable por el receptor** |
| 14 | Lo mismo en `…_h9`, cambiando `fase_c.md`, una salida de una fase anterior | **10** | Vuelve al **paso 12**: cambiado `fase_c.md`; solicitud `SA-cfb141cb0d97496c` (material `af6dd549…`). El `fase_c.md` cambiado **queda dentro del material refijado** y no se repiten los pasos que consumen la fase C. *Interpretación:* no consta que el consumo de ese cambio quede cubierto | Coincide en lo que se registra: vuelve al 12. **H9 sigue pendiente; no se declara resuelto.** La parte AG: **no ejecutable por el receptor** |
| 15 | — | — | No ejecutado | **No ejecutable por el receptor**: hace falta continuar la conversación de un agente real de fase C, y el receptor no puede lanzar agentes de contexto separado |
| 16 | — | — | No ejecutado. No se ha escrito ningún `auditoria.md`: las solicitudes `SA-4bb…`, `SA-3419…` y `SA-cfb1…` quedan pendientes y las copias se han borrado | **No ejecutable por el receptor**: hace falta un auditor nuevo de contexto separado, y el receptor no lo puede lanzar. No se simula. Precedente: en la 4.14 el receptor se auditó a sí mismo; aquí no se ha repetido |
| 17 | Lectura de `ficha_provisional.json` e `informe_provisional.md` regenerados por el código 4.15 en la copia del paso 12 (V6.3, motor A) | — | **Parcial:** el bloque `verificacion_entradas` existe, con `apto_por_entradas: false`, `apto_para_dinero_real: false`, recuento «0 de 292» y `entrada_efectiva.declarada.modo: registrada`, `declarado_en: null`, `aplicada_en_paso_2: null`; el informe lo muestra en su línea 9. La ficha **final** exige completar la auditoría | Parcial. La ficha final: **no ejecutable por el receptor** (AG) |
| 18 | Revisión del propio trabajo | — | No se ha creado ni modificado ninguna `configuracion_economica.json` ni ningún parámetro: ni R, θ, λ, probabilidades, k ni umbrales. Los únicos cambios de contenido fueron dos líneas-marcador de prueba en copias desechables (pasos 13 y 14), ya borradas | **Sí** |
| 19 | Este informe | — | Por bloques; hechos, interpretaciones y propuestas separados; lo no ejecutado se marca como tal | Sí |

### Resultado de los controles históricos (paso 10, registrado sin calificar)

Se compara la última línea con las salidas de referencia del árbol 4.14 (`E414/resultados/controles_historicos_en_arbol_4_14/`):
- **Iguales:** 4.2 (todas), 4.3 217/217, 4.3.1 43/43, 4.4 72/72, 4.5 60/60, 4.6.1 23/23, 4.6 23/24, 4.7 45/49, 4.7.1 38/44, 4.8 32/36, las dos comparaciones de baterías («HAY DIFERENCIAS»), 4.8.1 25/30 (en el reintento), 4.9 34/39, 4.10.1 38/43, 4.12 59/63 y 4.13 83/89.
- **Distintas del árbol 4.14:**
  - **4.10: 39/44** (40/44 en la 4.14). Pasa a NO CUMPLE «el mensaje de arranque recupera la estructura de uso: pasos, línea separadora y título del mensaje». *Interpretación:* `PROMPT_NUEVA_VENTANA.md` se reescribió en la 4.15; sería un control ligado al texto.
  - **4.11: 33/38** (34/38 en la 4.14). Pasa a NO CUMPLE «la reconstrucción desde la V6.3 da el mismo SHA-256 que la plantilla entregada (determinista)», que es una comprobación que **reejecuta**. La causa no se ha investigado.

## 2. Tiempos de los bloques largos

| Bloque | Inicio–fin (UTC) | Duración |
|---|---|---|
| Descarga del ZIP (API REST) | 08:41:47–08:42:28 | 41 s |
| `materialize` + `verify` | 08:42:34–08:42:59 | 25 s |
| Copia de los 1008 binarios | 08:43:31–08:43:35 | 4 s |
| `verificar_paquete.sh completa` | 08:44:07–09:37:27 | 53 min 20 s |
| `comprobar_entrega_4_14.py` | 09:37:42–09:37:53 | 11 s |
| Controles históricos (19) | 09:38:05–10:05:57 | 27 min 52 s |
| Reintento del control 4.8.1 | 10:07:09–10:12:21 | 5 min 12 s |
| Relanzamientos del pipeline (pasos 12, 13 y 14) | 10:12:48–10:14:02 | unos 15 s cada uno |
| Prueba completa | 08:41:22–≈10:20 | ≈1 h 40 min |

## 3. Ambigüedades y errores del manual (y desviaciones del receptor)

**Del manual o de sus fuentes:**
- **A-1 · Referencias a EVID desfasadas.** El manual cita EVID «leído en el commit `9871f59`», pero el receptor debe usar la rama `coordinacion/cierre-v2` (`788f25c`). Entre los dos commits, `CONTROL.json` cambió (+208/−35 líneas), así que las líneas citadas (`CONTROL.json:503-519`, `:594`, `:618`) ya no apuntan al texto que se cita. Ese texto existe, en otras líneas (T-CAMBIOS, línea 693; T-TRASPASO, línea 717). `PRUEBAS/` ganó además archivos `mecanismo_*` que el manual no menciona.
- **A-2 · Bloqueo de LibreOffice (N-06).** El manual no da la ruta. `PROMPT_RECEPTOR.md` dice «`$HOME/e_work/libreoffice.lock`», pero aquí `HOME=/root` y el bloqueo compartido real es `<e_work>/libreoffice.lock`. Se usó este, según los datos del entorno.
- **A-3 · `verify --report docs/…` escribe dentro del clon de `main`.** Deja `docs/VERIFICACION_BASE_COMPLETA_LOCAL.json` sin seguimiento. El manual dice que «`main` … no se modifica»: ¿vale escribir en el árbol local? Es ambiguo. No se ha versionado nada.
- **A-4 · Copia de los binarios (N-01), copia limpia (N-03) y contraste del manifiesto (N-02):** sin comando. Se improvisaron (script propio, `cp -a` y Python). El resultado coincide con el esperado.
- **A-5 · Comando de clonado y obtención de la rama (N-11):** sin comando. Se usó `git worktree`.
- **A-6 · Espacio en disco (N-05) — error práctico.**
  - El §3.1 pide «al menos 7 GB libres después de descomprimir». Con unos 8,4 GB libres al empezar los controles históricos, el control 4.8.1 se quedó sin espacio. Copia el árbol en `/tmp` y el árbol incluye `pruebas/_v64/` (más de 2 GB tras la verificación).
  - El manual no traslada la salida de `CONTINUIDAD.md` §2.5: borrar los `*.xlsx` y `vigencia/` de `_v64/` y registrar las rutas. El receptor la aplicó y repitió solo ese control.
  - ***Propuesta:*** que el manual diga esto en el paso 10 y fije el espacio para la vía del repositorio. En esta prueba hubo hasta unos 9,8 GB ocupados en la carpeta: clones, copia limpia y copia de relevos.
- **A-7 · Paso 10.** El manual no da el comando, que está en el LEEME 4.14 (`controles_historicos_4_13.py CARPETA_SALIDA`). Tampoco dice dónde va `CARPETA_SALIDA`. Si va dentro del árbol, como la referencia en `resultados/`, añade archivos al árbol verificado. Se puso fuera. El esperado sobre el árbol 4.15 sigue **[NO DOCUMENTADO]** (N-04); hay dos diferencias frente al árbol 4.14 (§1).
- **A-8 · Paso 12: «el mismo comando».** El manual no da el `--config` del expediente. Se dedujo `personaje_v2/config_v2.json` del LEEME del expediente.
- **A-9 · Orden de los pasos 12 y 13.**
  - El único relevo del paquete con precedente (`elis_motor_A`) ya está caducado. Con el código 4.15, el primer relanzamiento del paso 12 dispara también la detección del paso 13: registra el relevo caducado, repite el paso 12 y emite una solicitud nueva. El manual no lo avisa. Quien espere solo «código 10 y prompts regenerados» puede sorprenderse.
  - El paso 13 no dice qué archivo cambiar. Si se cambia uno que el paso 12 regenera (`informe_provisional.md`), el cambio desaparece aunque se detecte.
- **A-10 · Paso 11.** El manual lista cuatro relevos (de CONTINUIDAD), pero en el árbol hay más esperas: copias `antecedentes/heredados` y expedientes de la 4.10, la 4.10.1 y la 4.12. Ninguno es vigente; el manual no dice si deben contarse.
- **A-11 · Paso 9.** El manual no aclara si usa LibreOffice (N-12). Por lectura, no. La salida difiere de la referencia en las fechas de checkout; el manual no lo avisa (detalle menor).
- **A-12 · Duración.** 53 min, por encima de los 25–45 min documentados (C-11). Coincide con la hora de la candidata (≈1 h).
- **A-13 · Requisito S del paso 6:** «Ninguna orden de `base_414.py` … en el registro del receptor». Depende de que el receptor lleve un registro; el manual no dice cuál.
- **A-14 · `AGENTS.md` del repositorio de evidencias.** Dice «No ejecutar LibreOffice, el pipeline ni macros», pero va dirigido a los frentes Mistral M2. Choca en apariencia con los pasos LO del §10. Se siguió `PROMPT_RECEPTOR.md`, que manda ejecutar LibreOffice en secuencia.
- **A-15 · H9 (paso 14).**
  - Se confirma el comportamiento descrito: cambiar `fase_c.md` hace volver al paso 12 y el cambio queda en el material refijado, sin repetir los pasos que consumen la fase C.
  - El procedimiento correcto sigue **[NO DOCUMENTADO]** (N-08) y no se da por resuelto.
- **A-16 · Comandos con `python`.** README y manual usan `python`; el mensaje de arranque usa `python3 -I`. Aquí son equivalentes (los dos son 3.13). Sin efecto en esta máquina.

**Desviaciones del receptor (hechos):**
- **D-1:** a las 08:43:53 ejecutó `soffice --version` **sin `flock`**, para registrar la versión. En ese momento no corría ningún proceso de LibreOffice (`ps`). Todo lo demás con LibreOffice fue bajo `flock -x`.
- **D-2:** borró el ZIP local (ya verificado) y los `*.xlsx` y `vigencia/` de `_v64/` de la copia limpia, después de la verificación completa y del control 4.14 y antes de repetir el 4.8.1. Lo hizo según CONTINUIDAD §2.5, con las rutas registradas (775 líneas).
- **D-3:** al terminar borró `copia_limpia_1/` y `copia_relevo/`. Las evidencias de los relevos quedan en `registro/relevo_copia_{base,p13,h9}/`: estado, solicitud, material, ficha provisional, ESPERANDO y prompt del paso 13. Se conservan los dos clones (`munger-v2` con la base materializada, `candidata` con los binarios).
- **D-4:** `registro/paso10_controles_historicos/resumen.md` conserva la fila del 4.8.1 fallido. El reintento está aparte, en `registro/paso10b_4_8_1_reintento.txt`.

## 4. Lo que el receptor no ha podido hacer, y por qué

- **Pasos 15 y 16, y la parte AG de los pasos 13, 14 y 17:** no ejecutables por el receptor. No puede lanzar agentes de contexto separado y la regla 5 prohíbe simularlos. Por tanto, ninguna auditoría independiente; ningún APROBADO; ninguna ficha final del código 4.15.
- **H9:** solo se ha observado a qué paso vuelve (12). Si el cambio queda consumido no se ha verificado, y H9 queda **pendiente**.
- **Siguen sin cerrar:** F1, regeneración y auditoría de los expedientes, U1, U6 (a) y control 4.14 29/35. El receptor no los toca.

## 5. SHA-256 de las salidas citadas (en `registro/`)

| Archivo | SHA-256 |
|---|---|
| `paso3_materialize.log` | `86e853a0737b29408754e7edb6f5bcfa1de6755e14d194f846b8a493a8c1b31a` |
| `paso3_verify.log` | `496990947f8f396e88662f844ac77e3208873052dc81d4be68f7b54d02e46802` |
| `paso5_copia_binarios.json` | `c8cccada1941c9350cd9520c1e7c3f559cb295137ce9065cc57d60a82ae9ef20` |
| `paso8_verificar_paquete_completa.log` | `23fd7aa1b452df49e05ca38e9307f5492199ae0494f0e617bf70a308cedb54d4` (igual que el de `PRUEBAS/`) |
| `paso9_comprobar_entrega_4_14.log` | `afc6147a8751b094a4cc7a0f60a2c536e1a7fa9284b3274e58f5f36fef41e794` |
| `paso10_controles_historicos/resumen.json` | `5030f0fad13f6f1a0eb1ac2a50647f365283a96af25c7fbf7c1fabd75197249f` |
| `paso10_controles_historicos/resumen.md` | `8235bd7260dbd880f267bbb672debb8fd3f0b6e94f1dd71acde00af7e23068bf` |
| `paso10b_4_8_1_reintento.txt` | `8665fadd7ca440e418ce3ba9a58a0def86550b51e6b69472cbb065ac1402ab22` |
| `paso12_pipeline_01.txt` | `1effd8d5a19e79271c5ef7d14d422344b3cd2e5c89638f5e7e6d717daf929809` |
| `paso_p13_pipeline.txt` | `7a42fb7ddb50833b6a1f3e2ed26c907f07e842c42417c46ba2da44d37be5ef9b` |
| `paso_h9_pipeline.txt` | `f27fe8d4a3d1c456a505a7f1bbf0627871f57996c8ebdfaad394745a2bae3e25` |
| `relevo_copia_base/estado_pipeline.json` | `3c2b1d6894662fbcb7ea53e5eb21529076f8e965db0e8d33cbda02ab8744f211` |
| `relevo_copia_base/ficha_provisional.json` | `ec43b10da7c710a62db7c4024f11b6e07cc5ceb95d4c73f5b1ad31cd1e13aea1` |
| `relevo_copia_p13/estado_pipeline.json` | `6f694e68dd94f65716c41879174612e85e9fc622eba8f60c168e658965d38a7f` |
| `relevo_copia_h9/estado_pipeline.json` | `36d0b985fd7d2a9e732ee49b105a2811bf8712c406def32684ace7f2ed3c7a32` |
| `../scripts_receptor/copiar_binarios.py` | `8fb5b9bcfd242743c5d2c778215ba5961458bf781150d274332eed1d5af1735d` |
| ZIP `base-4.14` (descargado y luego borrado) | `bb51942cefb848e409a4828e3faeb70f94aa4d29af39cda6d90cd0a97cb7b93e` |

Lista completa: `registro/SHA256_REGISTRO.txt`.

## 6. Condición de la prueba

El receptor no escribió el manual. **Este informe no lo ha revisado nadie más**: la revisión por un agente distinto queda pendiente (`CLAUDE.md:31`). Nada de lo anterior acredita aptitud económica ni para dinero real.
