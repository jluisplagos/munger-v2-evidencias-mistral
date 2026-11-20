# Revisión independiente del resultado T-TRASPASO (17-nov-2026)

**Revisor:** agente distinto del receptor que hizo la prueba y del autor del manual. Solo ha leído. No ha ejecutado LibreOffice, el pipeline ni ningún control del producto. No ha usado la red ni ha cambiado ningún repositorio.

**Objeto revisado.** Repositorio de evidencias, rama `coordinacion/cierre-v2` @ `be6e9d5`:
- `coordinacion/cierre_v2/traspaso/resultado_20261117/`: `INFORME_TRASPASO.md`, `LEEME.md`, `registro/` y `scripts_receptor/`;
- `coordinacion/cierre_v2/traspaso/PROMPT_RECEPTOR.md`;
- `coordinacion/cierre_v2/manual/MANUAL_OPERATIVO_957af65.md`;
- como referencia, `coordinacion/cierre_v2/pruebas_candidata/957af65/`.

Para las causas se ha leído el código de la candidata en su worktree de solo lectura (HEAD `3149128` = `957af65` + cuatro documentos de G-DOCS).

**Esta revisión no es una aprobación.** No acredita aptitud económica ni para dinero real. El producto sigue siendo experimental supervisado.

Convenciones: **hecho** (comprobado aquí, con su fuente), *interpretación* y ***propuesta***.

---

## 0. Veredicto

**CONFORME CON LÍMITES.**

- Los resultados que importan están respaldados por el registro publicado y coinciden con las referencias:
  - verificación completa: PASA, código 0, idéntica byte a byte a la de las pruebas de la candidata;
  - control 4.14: 29/35, con las seis FALLA documentadas;
  - relevo caducado detectado sin `--desde`;
  - H9: vuelve al paso 12.
- No se afirma ningún paso con agentes que no se ejecutara.
- Límites:
  1. El registro no conserva una transcripción de comandos ni la mayoría de los códigos de salida. Los pasos 1–7, 11 y parte de 9, 10b y 12–14 son autodeclarados.
  2. Hay cinco imprecisiones menores (§1.3). Ninguna cambia un resultado.
- Las diferencias de 4.10 y 4.11 tienen explicación:
  - 4.10: está ligada al texto reescrito en la 4.15;
  - 4.11: es atribuible al entorno, no al código de la 4.15 (§5).

---

## 1. ¿Respalda el registro cada paso de la tabla? (pregunta 1)

### 1.1 Integridad del material publicado (hechos)

- `MANIFIESTO_SHA256.txt` del resultado: los 62 archivos dan OK. No hay ningún archivo fuera del manifiesto, salvo el propio manifiesto.
- `registro/SHA256_REGISTRO.txt` (huellas antes de sustituir las rutas): 11 FALLAN.
  - Diez son los archivos con rutas sustituidas: `resumen.json`, `resumen.md`, `4_8_1_comprobar_entrega.txt`, `paso10_salida.txt`, y los `13_verificacion.md` y `estado_pipeline.json` de las tres copias.
  - El undécimo es el propio `SHA256_REGISTRO.txt`, que se lista con la huella del archivo vacío (`e3b0c442…`): se calculó sobre sí mismo antes de escribirse. Es un defecto menor de forma.
- Manual: `MANUAL_OPERATIVO_957af65.md` `6ed65dce…` y `CONTRADICCIONES_GUIA.md` `88e69671…`. Coinciden con `manual/MANIFIESTO_SHA256.txt` y con el encabezado del informe.
  - El manual, `PROMPT_RECEPTOR.md` y `pruebas_candidata/` no cambian entre `788f25c` (instrucción del receptor) y `be6e9d5`.
- No quedan rutas absolutas del entorno del receptor. Las únicas son rutas históricas del entorno de la 4.14 dentro de `historial` de `estado_pipeline.json`, que forman parte del original copiado.

### 1.2 Respaldo paso por paso

Leyenda: **R** = en el registro · **I** = indirecto (se deduce de otro archivo del registro o del repositorio) · **—** = solo en el informe.

| # | Comando | Código | Resultado | Observación del revisor |
|---|---|---|---|---|
| 1 | — | n/a | I | Los prefijos del §13 del manual coinciden con `957af65` (hecho: comprobados 15 aquí). El informe dice que comprobó 10 |
| 2a | — | — | — | El 403 de `gh release download` no se conserva |
| 2b | — | — | I | La huella `bb51942c…` solo está en el informe. `materialize` funcionó con ese ZIP |
| 3 | — | I | **R** | `paso3_*.log`: 1008 recuperados; 6798/6798, `complete: true`. Por `tools/base_414.py:163`, eso implica código 0 |
| 4 | — | — | I | El HEAD `957af65` no tiene registro propio. Lo apoyan la línea `VERSION` del log del paso 8 y el manifiesto (7762, PASA) |
| 5 | — (script **R**) | I | **R** | Se publica `copiar_binarios.py`, que es correcto: no sobrescribe y comprueba la huella antes y después. `paso5_copia_binarios.json`: 1008·0·0·0. El conjunto de rutas es idéntico al de `copia_binarios_candidata.json` (hecho, 1008 = 1008). Los «83 JSON» de `git status` no tienen registro |
| 6 | — | n/a | — | No verificable: no hay transcripción de comandos (ver A-13) |
| 7 | — | — | — | Ni la copia ni «0 `__pycache__`, 1,5 GB» tienen registro |
| 7b | — | — | — | El script improvisado del manifiesto **no se conserva**, a diferencia del del paso 5 |
| 8 | I | **R** | **R** | `paso8_exit.txt` EXIT=0; inicio 08:44:07 y fin 09:37:27; log completo. El uso de `flock` no queda registrado |
| 9 | — | — | **R** | 29/35 en el log. Ni el código 1 ni los tiempos (09:37:42–53) tienen registro |
| 10 | I | **R** | **R** | EXIT=0, 09:38:05–10:05:57, 19 salidas y resumen. Los «8,4 GB libres» no tienen registro (no hay `df`) |
| 10b | — | — | **R** | Reintento 25/30 y limpieza (`paso10_limpieza_rutas.txt`). Ni los «13 GB», ni las horas, ni el código tienen registro |
| 11 | — | n/a | — | Sin registro. Comprobado aquí en el árbol: 13 `estado_pipeline.json` en espera, y la lista del informe es coherente |
| 12 | — | — | **R** | `paso12_pipeline_01.txt` y `relevo_copia_base/` lo respaldan, y el prompt tiene 6 rutas `<traspaso>`. El código 10 no se registra (la salida «ESPERANDO» es coherente con 10). Hay huellas «antes» (126) pero no «después», ni salida de `diff -r` |
| 13 | — | — | **R** | `paso_p13_pipeline.txt` y `relevo_copia_p13/`. No consta la línea añadida ni el código |
| 14 | — | — | **R** | `paso_h9_pipeline.txt` y `relevo_copia_h9/`. Igual que el 13 |
| 15–16 | n/a | n/a | coherente | En el registro no hay ningún `auditoria.md`: `auditoria: null` y todas las solicitudes «pendiente» o «sustituida», con veredicto nulo |
| 17 | n/a | n/a | **R** (ficha) | `ficha_provisional.json` tiene `apto_por_entradas: false`, `apto_para_dinero_real: false`, 0 de 292, `modo: registrada`, `declarado_en: null` y `aplicada_en_paso_2: null`. La «línea 9 del informe» no se puede comprobar: `informe_provisional.md` no está en el registro |
| 18 | n/a | n/a | coherente | No hay ninguna configuración económica en el registro |

**Tiempos (§2 del informe).**
- Respaldados:
  - paso 8: 53 min 20 s;
  - paso 10: 27 min 52 s;
  - relanzamientos: 15 s cada uno, por los sellos del `historial` (10:12:49→10:13:04, 10:13:32→10:13:47 y 10:13:47→10:14:02).
- Sin registro: la descarga, `materialize` + `verify`, la copia, el paso 9, el reintento del 4.8.1 y el total.

### 1.3 Afirmaciones que el registro matiza o contradice

1. **§5 del informe: cinco huellas no son las de los archivos publicados.**
   - Afectan a `resumen.json`, `resumen.md` y los tres `estado_pipeline.json`. El informe da la huella anterior a la sustitución de rutas.
   - El LEEME lo explica; el informe, no. ***Propuesta:*** una nota en §5.
2. **Paso 14 / A-15: «no se repiten los pasos que consumen la fase C».** Es inexacto.
   - Al repetir el paso 12 se ejecuta `verificar_todo.sh` (en el `historial`: «RESULTADO verificar_todo.sh: PASS»).
   - Ese script vuelve a pasar `verify_quotes_v2.py` sobre `fase_c.md` y valida el esquema de `fase_c.json` (`PV2/scripts/verificar_todo.sh:22,58-60`).
   - Lo que no se repite es la escritura de celdas desde `fase_c.json` (`fase_a_celdas.py … C`, `escribir_v63.py`) ni los turnos del agente.
   - *Interpretación:* como `fase_c.md` es texto que no se vuelca en celdas, la prueba **no discrimina el caso H9**. Lo discriminaría un cambio en `fase_c.json`, `fase_b.json` o `entrada_efectiva.json`. La conclusión del informe («H9 pendiente») sigue siendo correcta.
3. **«Iguales» en los controles históricos.** Solo coincide la última línea.
   - Hecho, por `diff` con `E414/resultados/controles_historicos_en_arbol_4_14/`:
     - son idénticos byte a byte 4.2, 4.3, 4.3.1, 4.4, 4.5, 4.6, 4.6.1, 4.7, 4.7.1, 4.8 y las dos comparaciones de baterías;
     - 4.8.1 (reintento), 4.9, 4.10.1, 4.12 y 4.13 difieren en el detalle de líneas que ya eran NO CUMPLE. Aparece `personaje_v2/pruebas/test_cierre_v2.py`, cambiado en la 4.15, y en 4.13 los archivos nuevos del expediente 4.15.
   - Las de 4.10 y 4.11 tienen además ese cambio de detalle.
   - El informe dice que compara la última línea, así que no oculta nada. Pero «Iguales» debería decir «misma última línea; detalle distinto, por los archivos de la 4.15».
4. **D-2: «775 líneas».** El archivo tiene 776: 774 `.xlsx`, la carpeta `vigencia/` y la nota del ZIP. Es trivial.
5. **Paso 12: «el original no cambia: 126 huellas iguales antes y después».** Solo se publica el «antes». La afirmación queda autodeclarada.

---

## 2. Paso 8: la verificación completa (pregunta 2)

- **Hecho:** `registro/paso8_verificar_paquete_completa.log` y `pruebas_candidata/957af65/verificar_paquete_completa.log` son **idénticos byte a byte** (`cmp` sin diferencias; SHA-256 `23fd7aa1b452df49e05ca38e9307f5492199ae0494f0e617bf70a308cedb54d4` en los dos). El log no tiene rutas ni horas, así que no hizo falta descontar ninguna sustitución.
  - *Interpretación:* la identidad es lo esperable en una salida determinista; no es por sí sola indicio de copia.
  - Hay pruebas independientes de que se ejecutó:
    - los sellos de inicio y fin (53 min);
    - `paso10_limpieza_rutas.txt`, con 774 `.xlsx` de `pruebas/_v64/` de la copia limpia, que solo existen después de `completa`;
    - el control 4.8.1, que falló al copiar `_v64/vigencia/`.
- **Recuentos** (hecho, líneas 4–59 del log): 7762·0·0·0; entorno, PASA; piloto, 35 CUMPLEN, salida idéntica; 114/114; 30/30 (30·30·0·0); 59/59; 27/27; 33/33; 190/190; 62/62; 5/5; 199/199; 78/78; 103/103; 55/55; 28/28; 45/45; 55/55; `RESULTADO GLOBAL: PASA`. Coinciden con la tabla del §5.2 del manual en los 18 bloques.
- **Código y duración:** `EXIT=0`. De 08:44:07 a 09:37:27, 53 min 20 s.
  - Queda fuera de los 25–45 min documentados (CONTINUIDAD §2.2).
  - Es coherente con la candidata (22:18–23:18, ≈60 min). El manual ya lo recoge como C-11.

## 3. Paso 9: el control de la 4.14 (pregunta 3)

- **Hecho:** 29/35 (línea 36). Las seis FALLA están en las líneas 7, 15 y 23 (verificación de entradas: «0 de 321», «0 de 311» y «0 de 292») y 10, 18 y 26 (fechas de archivo). Son exactamente las líneas que cita el manual (§5.3) para `PRUEBAS/comprobar_entrega_4_14.log`, y no hay ninguna FALLA más.
- `diff` con la referencia: solo cambian las tres marcas de tiempo (08:43:08 frente a 20:54:07). Es la hora del checkout, conservada por `cp -a`.
- Que no usa LibreOffice es correcto: el script no importa `subprocess` ni llama a `soffice` (hecho, lectura de `comprobar_entrega_4_14.py`). El código 1 no se registra.

## 4. Pasos 12–14 (pregunta 4)

### 4.1 Relevo caducado detectado sin `--desde` (hecho)

En `relevo_copia_base/estado_pipeline.json`:
- `relevos_caducados[0]`: fijado `9e1a725d6432f548`, vigente `72f855cf59b252fb`, `archivos_cambiados: ["verificacion_entradas.json"]`, refijado `4d9ee9b6e4b4bd09`, solicitud `SA-4bb1526435a31a51`;
- `SA-ed5561eac1cc5897` en estado «sustituida», con `motivo_sustitucion`;
- después del registro, la repetición del paso 12 (recálculo, `verificar_todo.sh` PASS y «0 de 292», apta: no) y la solicitud nueva.

Es el caso histórico I19 que describe CONTINUIDAD §2.6. El relanzamiento no lleva `--desde`, según el informe, y el registro lo confirma: el `historial` no registra ninguna reanudación forzada.

**Paso 13 (copia `_p13`):**
- segundo `relevos_caducados`, con cambiado `informe_provisional.md`;
- refijado `b79ad7da2f9829aa`, `SA-3419ec21eb14c04f`, y `SA-4bb…` «sustituida».
- Hecho: en el material refijado, `informe_provisional.md` tiene la misma huella que en la base, así que el paso 12 lo regeneró y la marca de prueba desapareció. Coincide con lo que dice el informe.

### 4.2 H9, vuelta al paso 12 con `fase_c.md` cambiado (hecho)

- `relevo_copia_h9`: fijado `4d9ee9b6…`, vigente `f3e1a1c00aa66553` y cambiado `fase_c.md`; refijado `af6dd549a8496c72`, `SA-cfb141cb0d97496c`, y `SA-4bb…` «sustituida».
- Comparación de `material_auditoria.json` (h9 frente a la base): `fase_c.md` cambia (`f5ce112f…` → `7d7a874c…`), además de `resultados.json` y `acreditacion_libro.json`, que cambian por el recálculo. El cambio **queda dentro del material refijado**.
- `consumidos.fase_c.json` no cambia. No se repiten los pasos 10 y 11; ver §1.3.2 sobre lo que sí repite `verificar_todo.sh`.
- Qué no prueba:
  - si el retorno al 12 basta cuando cambia una salida que se vuelca en celdas;
  - el cambio elegido no ejercita ese caso.

### 4.3 Afirmaciones sobre agentes

- **No se afirma nada que no se ejecutara.** No hay ningún `auditoria.md`, ningún veredicto ni ninguna ficha final. No se usó `--agentes-simulados`: no aparece en el `historial` posterior al 17-nov.
- Límite: la imposibilidad de lanzar agentes de contexto separado se declara, pero no se demuestra con un comando (N-07 del manual; `PROGRAMA.md:13` pide comprobarlo con comandos).

## 5. Paso 10: los controles 4.10 (39/44) y 4.11 (33/38) (pregunta 5)

### 5.1 4.10: 39/44 (40/44 en el árbol 4.14)

- **Qué falla exactamente.** Hecho, línea 41 de la salida: «NO CUMPLE · [constata] el mensaje de arranque recupera la estructura de uso: pasos, línea separadora y título del mensaje».
- **Condición del código** (`…_4_10/scripts/comprobar_entrega_4_10.py:181-182`): `"\n---\n" in prom and "# Continuación del proyecto Munger v2 · verificación inicial" in prom and ".PARTES.txt" in prom`, sobre `munger_v2_r1/PROMPT_NUEVA_VENTANA.md`.
- **Hecho (`git show`):**
  - la separadora y el título están presentes en `589ce19` (base 4.14), `957af65` y `3149128`;
  - `.PARTES.txt` aparece una vez en la 4.14 y ninguna en `957af65` ni en `3149128`;
  - el archivo lo cambiaron `de5322f`, `9975d81` y `0a0020b` (hito 2), que reescriben el mensaje para arrancar desde el repositorio en lugar de un ZIP en partes.
- **Clasificación:** atribuible a un **cambio documental de la 4.15**, deliberado. Es un control «ligado al texto de su versión» en el sentido de `LEEME_CONTROLES_HISTORICOS_4_14.md` §3. No es una regresión funcional ni depende del entorno. Persiste en HEAD `3149128`.
- Además, la línea 3, que ya era NO CUMPLE, añade `test_cierre_v2.py` a «fuera de lo declarado»: es otro cambio de la 4.15.

### 5.2 4.11: 33/38 (34/38 en el árbol 4.14)

- **Qué falla exactamente.** Hecho, línea 12 de la salida: «NO CUMPLE · [reejecuta] la reconstrucción desde la V6.3 da el mismo SHA-256 que la plantilla entregada (determinista)».
  - El detalle muestra que la reconstrucción **terminó bien**: «1240 flujos anuales envueltos · 28 comprobaciones de configuración · conciliación … · partes restauradas 6 → …/V64_reconstruida.xlsx».
  - La condición es `rc == 0 and sha(nueva) == sha(pl64)` (`…_4_11/scripts/comprobar_entrega_4_11.py:124-126`). Falla solo la igualdad de la huella **del archivo ZIP**.
- **Pruebas de que no es la 4.15 (hechos):**
  1. `git diff --name-only 589ce19 957af65` no toca nada bajo `munger_v2_r1/v6/`:
     - ni `construir_v64_experimental.py`;
     - ni `add_sliders.py`;
     - ni `v6/scripts/patch_v62_base.py`, el único módulo propio que importa.
     De los 1008 archivos cambiados o nuevos, los que no son del expediente `…_4_15/` son 47: todos de `personaje_v2/`, `docs/` o de la raíz. Ninguno está en `v6/`.
  2. En la misma ejecución CUMPLEN `V6.3: entregables y referencia con sus SHA-256` y `V6.4 experimental: plantilla y referencia con sus SHA-256` (líneas 9–10). Las entradas binarias (V6.3 y la V6.4 entregada) son las de la 4.14.
  3. En la misma pasada, el control 4.12 repite la misma reconstrucción (`comprobar_entrega_4_12.py:176-180`) y la compara **miembro a miembro** con `comparar_zip.py`. **CUMPLE** (línea 14 de `4_12_comprobar_entrega.txt`). El contenido reconstruido es idéntico; solo difiere la compresión.
  4. El propio proyecto lo documenta: «No se promete identidad binaria entre entornos: la huella del archivo depende de la compresión» (`PV2/ANEXO_D_salidas_y_formatos.md:424`; `…_4_12/INFORME_INTEGRACION_4_12.md:69`). Y `test_integracion_v64.py` (grupo A) no exige la huella («distinto (no se exige)»).
  5. No es el disco:
     - `construir_v64_experimental.py` terminó con `rc == 0`;
     - el temporal del 4.8.1, que se quedó sin espacio, se borra en su `finally` (`comprobar_entrega_4_8_1.py:184`) antes de que corran 4.9–4.13.
- **Clasificación:** **atribuible al entorno.** El control 4.11 exige identidad binaria del ZIP, y esa identidad depende de la biblioteca de compresión. La 4.12 corrigió ese criterio, y la comprobación corregida pasa.
  - *Interpretación:* el entorno del receptor comprime distinto que el que generó las referencias de la 4.14.
  - No queda probado qué componente es (zlib u otro): ni el informe ni las referencias registran la versión de zlib. Python 3.13.18 y openpyxl 3.1.5 coinciden con lo registrado en la 4.11 (`…_4_11/replica/INFORME_REPLICA.md:180`). Solo como indicio: la máquina de esta revisión da zlib 1.3, y no consta que sea la del receptor.
  - ***Propuesta*** para cerrarlo sin lugar a dudas:
    - registrar `zlib.ZLIB_RUNTIME_VERSION` en el entorno de referencia y en el del receptor;
    - pasar `comparar_zip.py` sobre la reconstrucción del 4.11.
- Además, la línea 2, que ya era NO CUMPLE, cambia su lista truncada de «de más»: entra `test_cierre_v2.py`, de la 4.15, y sale `resumen.py` por el truncado `[:5]`.

### 5.3 Resto del paso 10

- **4.8.1:**
  - el primer intento falló por `[Errno 28]` al copiar el árbol a un temporal;
  - el reintento, tras la limpieza de CONTINUIDAD §2.5, da 25/30, igual que el árbol 4.14. Solo difiere el detalle (`test_cierre_v2.py`).
- **Hecho:** `comprobar_entrega_4_8_1.py:76-77` copia `personaje_v2/` excluyendo solo `empresas_v2`, `.lo_perfil` y `__pycache__`, así que **copia `pruebas/_v64/`**. CONTINUIDAD §2.5 dice «los controles no recorren `_v64/`». Para el 4.8.1 es inexacto en cuanto al disco, aunque no en cuanto al resultado: copia `_v64/`, pero no lo evalúa. Es la causa del fallo por espacio que el informe atribuye a A-6.

## 6. Las ambigüedades y errores del manual (pregunta 6)

- **Recuento.** El encargo habla de 14, pero el informe lista **16** (A-1…A-16) y además 4 desviaciones propias (D-1…D-4). Se revisan las 16.
- Todas son ciertas en lo esencial. A-14 y A-16 no son defectos del manual, sino de su entorno de fuentes.
- Orden de gravedad para un receptor nuevo:

| Orden | Id | Gravedad | ¿Cierta? | Comprobación del revisor |
|---|---|---|---|---|
| 1 | **A-6** Disco | **Alta** | Sí | §3.1 del manual (7 GB) y N-05. El fallo se produjo con unos 8,4 GB libres (autodeclarado). Es recurrente: I17 (4.14, controles), I18/I21 (traspaso 4.14) y ahora aquí. **Añadido:** CONTINUIDAD §2.5 afirma que «los controles no recorren `_v64/`», pero el 4.8.1 sí lo copia (§5.3). El manual no traslada la limpieza de §2.5 al paso 10 |
| 2 | **A-9** Pasos 12–13 | **Alta** | Sí | El §10 (paso 12) espera «código 10, prompts regenerados». Con `elis_motor_A`, que el propio §7.4 declara caducado, el primer relanzamiento ejecuta además la detección del paso 13. CONTINUIDAD §2.6 se contradice en dos viñetas seguidas («sale con código 10 sin hacer nada más» frente a «lo detecta al relanzarlo»). El paso 13 no dice qué archivo cambiar, y `informe_provisional.md` se regenera |
| 3 | **A-7** Paso 10 | **Media-alta** | Sí | El manual cita el LEEME, pero no da el comando (`controles_historicos_4_13.py CARPETA_SALIDA`) ni dónde poner la salida. Las referencias están dentro del árbol (`E414/resultados/…`). Esperado sobre el árbol 4.15: N-04. Ahora hay dos diferencias que el manual no clasifica (§5) |
| 4 | **A-15** H9 | **Media-alta** | Sí | §7.3 y N-08 del manual. **Añadido:** el procedimiento de prueba tampoco indica qué salida cambiar. Con `fase_c.md` no se distingue el caso que importa (§1.3.2) |
| 5 | **A-2** Bloqueo LO | **Media-alta** (seguridad) | Sí | El manual no da la ruta (N-06). `PROMPT_RECEPTOR.md` regla 3 da `$HOME/e_work/libreoffice.lock`. El receptor usó otra ruta (`<e_work>`), porque `$HOME` no apuntaba al bloqueo compartido. Si dos sesiones usan bloqueos distintos, no hay exclusión mutua |
| 6 | **A-13** Registro del receptor | **Media** | Sí | El paso 6 exige comprobar «el registro del receptor», pero nadie dice qué registro. **Consecuencia observada:** el registro publicado no tiene transcripción ni códigos de la mayoría de los pasos (§1.2) |
| 7 | **A-4** Copia de binarios, copia limpia y contraste del manifiesto | **Media** | Sí | N-01, N-02 y N-03. El receptor tuvo que escribir código propio. Solo el del paso 5 se conserva |
| 8 | **A-8** `--config` del paso 12 | **Media** | Sí | §6.3 da `--config config_v2.json` (V6.3), sin la ruta `personaje_v2/`. `estado_pipeline.json` no guarda el comando original |
| 9 | **A-5** Clonado y obtención de la rama | **Media-baja** | Sí | N-11; §4.2.5 solo da la rama. El README describe otra vía: cambiar de rama en el mismo clon (`README.md:5`) |
| 10 | **A-1** EVID desfasado | **Media-baja** | Sí | Hecho: `CONTROL.json` cambia +208/−35 entre `9871f59` y `788f25c`. En `788f25c`, las líneas 503, 519, 594 y 618 ya no son las citadas (T-CAMBIOS en la 693, T-TRASPASO en la 717). Los `mecanismo_*` y `MECANISMO_PERSONAJE.md` no existían en `9871f59` |
| 11 | **A-14** `AGENTS.md` | **Baja-media** | Sí, como conflicto de fuentes | `AGENTS.md` (en `788f25c`) prohíbe LibreOffice y el pipeline a los frentes Mistral M2. Un receptor estricto podría negarse a los pasos LO. No es un error del manual |
| 12 | **A-3** `verify --report docs/…` | **Baja** | Sí | El comando de `README.md:43` escribe un JSON sin seguimiento en `docs/` del clon (`.gitignore` solo cubre `.downloads/`). No modifica la rama `main` |
| 13 | **A-10** Más esperas | **Baja** | Sí | Hecho: 13 `estado_pipeline.json` en espera en `957af65`, frente a los 4 de CONTINUIDAD §2.6. Ninguno vigente |
| 14 | **A-11** Paso 9 | **Baja** | Sí | N-12 ya está en el manual. Las marcas de tiempo distintas son esperables, aunque no se avisa |
| 15 | **A-12** Duración | **Baja** | Sí | Ya está como C-11 |
| 16 | **A-16** `python` / `python3` | **Baja** | Sí, sin efecto | `README.md:42-43` usa `python`; el mensaje de arranque usa `python3 -I` |

## 7. Desviaciones D-1…D-3 (pregunta 7)

- **D-1** (`soffice --version` sin `flock`, a las 08:43:53).
  - No afecta a ningún resultado: después, la verificación es idéntica byte a byte a la de referencia.
  - Incumple la regla 3 del prompt. Que no corriera otro LibreOffice (`ps`) no tiene registro.
- **D-2** (borrado de `_v64/*.xlsx`, de `vigencia/` y del ZIP).
  - No afecta a ningún resultado:
    - se hizo después de los pasos 8, 9 y de la primera pasada del 10;
    - CONTINUIDAD §2.5 lo autoriza, y las rutas se registran;
    - el reintento del 4.8.1 da lo mismo que la referencia;
    - los pasos 12–14 corren en otra copia.
  - Efecto lateral: sin el ZIP, la materialización ya no se puede repetir sin descargarlo otra vez.
- **D-3** (borrado de `copia_limpia_1/` y `copia_relevo/`).
  - No afecta a ningún resultado.
  - Reduce la posibilidad de reexaminar:
    - no se conservan las líneas-marcador de los pasos 13 y 14;
    - tampoco el `informe_provisional.md` regenerado;
    - ni el estado posterior de las 126 huellas.
- **Desviaciones no listadas como D:**
  - la ruta del bloqueo distinta de la regla 3 del prompt (tratada en A-2);
  - la carpeta de salida del paso 10 fuera del árbol (declarada en el paso 10).
  - Ninguna afecta a los resultados.
  - *Interpretación:* la primera es razonable si `<e_work>` es el bloqueo que comparten las demás sesiones, pero no se puede comprobar con el registro.

## 8. ¿Declara bien sus límites el informe? (pregunta 8)

**Sí, en lo esencial:**
- Pasos 15–16 y la parte AG de 13, 14 y 17: «no ejecutable por el receptor», sin simular nada.
- Ningún APROBADO, ningún `auditoria.md` y ninguna ficha final.
- «No apto para dinero real», y superar los controles no acredita aptitud.
- H9 queda pendiente.
- Pendientes que no toca: F1, la regeneración, U1, U6 (a) y el control 4.14.
- Falta la revisión por otro agente (§6 del informe).

**Lo que debería añadir:**
1. Que la incapacidad para lanzar agentes no se comprobó con un comando (N-07).
2. Que el registro no contiene transcripción ni la mayoría de los códigos, así que varios «hechos» de la tabla son autodeclarados.
3. Que la familia de modelo del receptor es la del autor del manual. Solo lo dice el LEEME, que escribió el coordinador.
4. La nota de §1.3.1 sobre las huellas de §5.

## 9. Mejoras del manual, por prioridad (propuestas)

1. **Disco y paso 10.**
   - Fijar el espacio para la vía del repositorio: el receptor llegó a ocupar ≈9,8 GB en la carpeta, más el temporal del 4.8.1.
   - Incluir en el paso 10 la limpieza de CONTINUIDAD §2.5, con registro de rutas, antes del 4.8.1.
   - Corregir en CONTINUIDAD que el 4.8.1 **sí copia** `_v64/`.
2. **Pasos 12–14.**
   - Avisar de que `elis_motor_A` ya está caducado: el primer relanzamiento registra `relevos_caducados`, repite el paso 12 y sustituye `SA-ed5561…`.
   - Para el paso 13, indicar un archivo del material que el paso 12 no regenere.
   - Para H9, indicar que se cambie una salida que se vuelque en celdas (`fase_c.json`, `fase_b.json` o `entrada_efectiva.json`).
   - Dar el comando completo con `--config personaje_v2/config_v2.json`.
3. **Resultado esperado de los controles históricos sobre el árbol 4.15.**
   - 4.10: 39/44, por el texto del mensaje de arranque (`.PARTES.txt`).
   - 4.11: 33/38 o 34/38, según el entorno de compresión. Lo vinculante es la comprobación miembro a miembro del 4.12.
   - Para el resto, misma última línea con un detalle distinto por los archivos de la 4.15.
   - Dar el comando y dónde va `CARPETA_SALIDA` (fuera del árbol verificado).
4. **Bloqueo de LibreOffice:** una ruta única y el comando `flock -x` completo, también para `soffice --version`.
5. **Registro del receptor:**
   - exigir una transcripción con el comando, el código (`$?`) y la hora de cada paso;
   - exigir conservar los scripts improvisados (también el del paso 7b) y el `df` antes de los bloques largos;
   - exigir las huellas antes y después del paso 12.
6. **Comandos de los pasos N-01, N-02, N-03 y N-11.** Se puede tomar como base `scripts_receptor/copiar_binarios.py`, tras revisarlo.
7. **Referencias:**
   - actualizar las citas de EVID a la rama vigente;
   - aclarar la precedencia de `AGENTS.md` frente a `PROMPT_RECEPTOR.md`;
   - aclarar el JSON que escribe `verify --report`, el recuento de esperas y `python` frente a `python3`.

## 10. Lo que esta revisión no ha hecho

- No ha ejecutado ningún control. Las causas de §5 se apoyan en la lectura del código, en `git diff` y en las salidas publicadas.
- No ha comprobado la versión de zlib del entorno del receptor ni del de la 4.14.
- No ha revisado el contenido económico de ningún expediente.
