# Revisión independiente de la respuesta F2 de Mistral C/F · de `195766f` a `98bdf8f`

- **Revisor:** subagente Claude (Opus 5.5), lanzado por el coordinador. No soy autor del material revisado: su autor es Mistral C/F. **Límite:** el coordinador que me lanza también es Claude, y además es autor del contrato C paralelo (`u3_motor_c/`) con el que comparo el de F. Este informe da hechos reproducibles; no decide la aceptación.
- **Fecha:** 2026-11-17.
- **Objeto:**
  - encargo inicial: `195766f` (F2-D1, D2 y D7) sobre `868f448`, rama `origin/mistral/f-alcance-real` de `<repo>` (`munger-v2-evidencias-mistral`);
  - primera ampliación pedida por el coordinador: `e9f76a9` (D3), `9873234` (D6) y `c761cc8` (D4, D5 y D7);
  - segunda ampliación: `98bdf8f` (09:47:33Z, «respuesta completa … con ENTREGA, evidencias y manifiesto»), HEAD final de la rama. Solo añade `correccion_f2/ENTREGA_F2.json` y `RESPUESTA_F2.md`, un bloque F2 en `COMANDOS.md` y el manifiesto (§8).
  - La referencia remota avanzó mientras revisaba (reflog: `195766f` → `9873234` → `c761cc8` → `98bdf8f`). No hice ningún fetch.
- **Reglas aplicadas:** `CORRECCION_F2.md` (`80c5c166…52fe`) y `REVISION_F_223f16d_52fb120.md` (`66667315…1031`), con sus sondas; `u2_tercer_b/RECURSOS_EXISTENTES.md` y `LEEME.md`; `u3_motor_c/CONTRATO_C_DESDE_EL_MOTOR.md`; `PLANTILLA_ENTREGA.json`. Todo leído con `git show` de `origin/coordinacion/cierre-v2` (en `763d0ff` al terminar; `CORRECCION_F2.md` y `PLANTILLA_ENTREGA.json` no cambian desde `57b34a6`).
- **Material local:**
  - `<zip>`: ZIP base-4.14, SHA-256 `bb51942cefb848e409a4828e3faeb70f94aa4d29af39cda6d90cd0a97cb7b93e` (recalculado);
  - `<candidata>/munger_v2_r1/`: candidata en `3149128`. `build_v6.py`, `test_fill.py`, `relacion_entradas_materiales.py`, `patch_v62_base.py` y `referencia_V6.3.json` son idénticos a `957af65` (`git diff 957af65 HEAD` vacío), la versión que cita F.
  - Entregas extraídas con `git archive <commit> resultados_cierre/alcance_real | tar -x` en `<rev_F2>/entrega/` (`195766f`), `<rev_F2>/entrega_c761cc8/` y `<rev_F2>/entrega_98bdf8f/`. Sin checkout ni worktree.
- **Herramientas:** `python3 -I`, `unzip -Z1/-l/-p`, `sha256sum`, `awk`, `cmp`, `git show/diff/log`, `openpyxl` (solo lectura de un fixture).
- **No hice:** commit, push, cambios en repositorios, red, LibreOffice ni el pipeline.
- **Sondas:** en `<rev_F2>/sondas/`; huellas al final.

## Resumen de veredictos

| Punto | En `195766f` | En `98bdf8f` (HEAD final) | Motivo principal |
|---|---|---|---|
| **F2-D1** | **CERRADO CON LÍMITES** | **CERRADO** | El CSV se reproduce byte a byte desde el ZIP. En `195766f`, la ENTREGA conserva el comando viejo, que ya no funciona; `c761cc8` lo arregla y `ENTREGA_F2` lo vuelve a declarar. |
| **F2-D2** | **CERRADO CON LÍMITES** | **CERRADO CON LÍMITES** (sin cambios) | 71/71 PDF con huella completa y Release con SHA completo. El alcance se declara solo en positivo. El `.bat` de Ahold no se registra, y el README sigue diciendo que no existe. |
| **F2-D7** | **ABIERTO** | **CERRADO CON LÍMITES** | En `195766f` el extractor sigue con `/workspace` fijo. Se corrige en `c761cc8`. Los comandos de `ENTREGA_F2` se ejecutan (con `/tmp` y la ruta de textos sustituidas), pero dos «comandos» de `ENTREGA_B_PM1` y `B3_C1` siguen sin ejecutarse tal cual, y `RESPUESTA_F2` dice que sí. |
| **F2-D3** | — | **CERRADO CON LÍMITES** | X14/X15/X18/B68, ROE, puente, terminal y base de valor: correctos. Pero atribuye la elección del motor a `Palancas C6` (es `Análisis C62`), cita mal unas diez líneas del motor y omite la quiebra. `98bdf8f` repite esas citas en `RESPUESTA_F2` y `COMANDOS`. |
| **F2-D4** | — | **CERRADO** | La siguiente acción está al día. Los `ENTREGA_F2.json` y `RESPUESTA_F2.md` a los que remitía, ausentes en `c761cc8`, existen en `98bdf8f` (R10 resuelto). |
| **F2-D5** | — | **CERRADO CON LÍMITES** | Distingue preparación de ejecución y retira los dos criterios inexistentes. `ENTREGA_F2` está limpia. Quedan restos en `ENTREGA_B3_C1`, `ENTREGA_B_PM1` y `PUNTO` (R11), y una afirmación inexacta en `98bdf8f` (R14). |
| **F2-D6** | — | Horas: **CERRADO**. Protocolo: **CERRADO CON LÍMITES** | Las horas coinciden al segundo con los commits. El bloque F2 de `COMANDOS` (09:24–09:44) no cubre el commit final de las 09:47:33. El protocolo no nombra candidata ni usa precios, pero repite el error de `Palancas C6`. Además, el U3 del coordinador ya había publicado dos candidatas 5,5 minutos antes en el mismo repositorio. |
| **4. Pendientes y contrato C** | **No los declara** | Los responde | `195766f` no menciona D3–D6 ni `u3_motor_c`. `e9f76a9` y `9873234` rehacen el contrato y el protocolo de C en paralelo a U3, sin mencionarlo. |
| **5. Higiene** | **CERRADO** | **CERRADO** | Manifiestos válidos (46/46 en `98bdf8f`). Sin binarios, cachés ni secretos. |
| **ENTREGA frente a plantilla** | **ABIERTO** | **CERRADO CON LÍMITES** | En `98bdf8f`, `ENTREGA_F2.json` tiene exactamente las claves y los tipos de la plantilla; sus pruebas 0–3 se ejecutan con código 0 y la 5 es NO_EJECUTADO. Límites: el resultado de la prueba 2 es un valor compuesto, la prueba 4 no es reproducible y declara cubiertos D2, D3 y D7 a pesar de R3–R9 (R14, R15). |

## Defectos y contraejemplos

| Id | Gravedad | Dónde | Defecto | Contraejemplo / evidencia |
|---|---|---|---|---|
| **R1** | Material en `195766f`; resuelto en `c761cc8` | `ENTREGA_B3_C1.json` @ `195766f` | No se actualizó. La prueba 0 sigue declarando `unzip -l … \| python3 scripts/inventario_desde_zip.py /tmp/zip_list.txt INVENTARIO_Y_HUECOS.csv` con exit 0. El script nuevo pide 3 argumentos y un ZIP. | Esa forma, con 2 argumentos, da `IndexError` y exit 1 (`sondas/sonda_d1_comando_entrega_195766f_out.txt`). |
| **R2** | Menor (D7) en `195766f`; resuelto en `c761cc8` | `revisiones_b_pm1/evidencias/extraccion_independiente_pm1.py` @ `195766f` | Ruta `/workspace/…` fija en la línea 10. Es justo el contraejemplo de F2-D7, y el mensaje del commit dice que D7 está cubierto. | Ejecutado tal cual: `FileNotFoundError` y exit 1 (`sondas/sonda_d7_extractor_195766f_out.txt`). En `c761cc8` toma `sys.argv[1]`: exit 0 y salida idéntica byte a byte a `extraccion_independiente_out.txt` (`sondas/sonda_c761cc8_comandos_out.txt`). |
| **R3** | Menor (D2) | `INVENTARIO_Y_HUECOS.csv` fila Ahold; `README.md:28`; `SELECCION.csv:2` (sin cambios hasta `c761cc8`) | El `.bat` de Ahold está en el ZIP, pero el inventario lo da por «sin conservar». El README dice «carece de Excel de etapa 1 **y .bat**», y SELECCION, «sin PDF/fuentes conservados». El `.bat` solo cuenta, sin nombre, como 1 de los 17 «otros» de `documentacion_cierre_4_14`. | `…/2026-11_Vidrala_ensayo_4_14/documentacion_cierre_4_14/descargas_bat/descargar_fuentes_ahold.bat`, SHA-256 `04feebd409754a91e509dfde1e8dd63a1e8534695d05cb75fffca6a97bd53d88`, igual que en el manifiesto 4.14. Dice: «La carpeta tiene los informes 2019-2025» (`sondas/sonda_d2_bat_ahold_out.txt`). La frase «ni .bat **ejecutado**» de la fila es cierta. |
| **R4** | Menor (D2) | `inventario_desde_zip.py` y README | El alcance se declara en positivo (docstring y README), pero no dice qué queda fuera ni cuánto. | De los 6799 archivos del ZIP, 6476 entran y 323 quedan fuera, sin aviso: `v6/` 91, `personaje_v2/` (fuera de `empresas_v2*`) 152, `documentacion_reparacion/` 45, `kit_pipeline_munger/` 26, 8 sueltos en la raíz y `empresas_v2_correcciones/ceros_heredados_H1.csv` (`sondas/sonda_d2_alcance_out.txt`). Hoy ningún PDF queda fuera. |
| **R5** | Medio (D3) | `CONTRATO_C_PROPUESTA.md` §1 y `PROTOCOLO_CONGELADO.md` §2.1.1 | Dice que el motor C se elige con `Palancas C6` = «Financiera» → `Diagnóstico C5`, y cita `build_v6.py:146-153`. En el producto, `Diagnóstico C5` solo lee `Análisis!C62`, que elige la fase A. `Palancas C6` solo produce el aviso de coherencia (Diagnóstico C6 REVISAR, V11 NOA). | `REF["Diagnóstico V6!C5"] = IF(Análisis!$C$62="Sí","A",…"No · banco o aseguradora"…,"C"…)`: no contiene `Palancas` (`sondas/sonda_d3_motor_c_out.txt`). El fixture C_orig lleva `C62` = «No · banco, aseguradora o regulada». Si alguien pone `Palancas C6` = Financiera y deja C62 = «Sí», obtiene el motor A bloqueado por V11, no el motor C. Las líneas 146-153 son constantes; la nota «Financiera → motor C» está en `build_v6.py:426`. |
| **R6** | Menor (D3: «con cita de línea») | Contrato §1–4 y `MAPA_ENTRADAS.jsonl` | Las citas de línea del motor están desplazadas. Lo citado sí es correcto. La propia evidencia de F (`d3_citas_producto_957af65.txt`, bloque «933-942») muestra BG…BP, no g_t, L_t, m_t ni el flujo. | Detalle en la tabla de abajo (`sondas/sonda_d3_lineas_reales.txt`). |
| **R7** | Menor (D3) | Contrato §4 y MAPA fila «Motor C» | El valor por acción se da como «(VP flujos + VP VT) ÷ nº acciones», sin `BJ = (1−p)·BI + p·rec`, que en C también se aplica (Palancas C22/C23). Tampoco dice que g_t baja en línea recta hasta g∞ en los años 6–10. | `REF["Motor!BJ7"]`, `N7 = N(Palancas!$C22)`, `O7 = N(Palancas!$C23)`. Con p = 10 % y rec = 20 sobre el ejemplo de F, el valor pasa de 115,06 a 105,55 (`sondas/sonda_d3_motor_c_out.txt`). |
| **R8** | Menor (D3) | Contrato §3 | «Identidad: dividendo = BN − ΔB» se da sin la condición de excedente limpio: con OCI ≠ 0 no se cumple. Tampoco registra que el ROE de partida es de cierre (L9/L21) mientras el motor aplica m_t al patrimonio de apertura. | Variante de U3: OCI −25 y recompras 10 → beneficio − ΔB = 75 frente a un reparto de 50. ROE de cierre 9,434 % frente a 10 % de apertura en el caso 1000/100/40 (reproducido en `sonda_d3_motor_c_out.txt`). |
| **R9** | Menor | `ENTREGA_B_PM1.json` prueba 2; `ENTREGA_B3_C1.json` prueba 1; `ENTREGA_B_PM1.json` prueba 1 @ `c761cc8` (igual en `98bdf8f`) | Comandos que no se ejecutan tal cual:<br>- `python3 -I evidencias/extraccion_independiente_pm1.py sobre los textos hash-verificados` no lleva el argumento que ahora exige el script;<br>- «sha256+bytes de los 29 PDF … contra .trabajo/insumos_m2» es una descripción;<br>- `tablas_vidrala.py` depende de `.trabajo/`, que no se entrega. | La prueba 2, tal cual, da `IndexError` y exit 1 (`sondas/sonda_c761cc8_comandos_out.txt`). |
| **R10** | Menor (D4/entrega); **resuelto en `98bdf8f`** | `PUNTO_DE_RECUPERACION.md` y `ENTREGA_B3_C1.json.siguiente_accion_exacta` @ `c761cc8` | Remiten a `correccion_f2/ENTREGA_F2.json` y `correccion_f2/RESPUESTA_F2.md`, que no existen. CORRECCION_F2 pedía «un commit con ENTREGA.json y F2-D1…D7». | `git ls-tree -r c761cc8` no tiene ningún `ENTREGA_F2`. `correccion_f2/` solo contiene `evidencias/` y `scripts/` (`sondas/sonda_entregas_c761cc8_vs_plantilla_out.txt`). |
| **R11** | Menor | `ENTREGA_B3_C1.json` y `ENTREGA_B_PM1.json` @ `c761cc8` (igual en `98bdf8f`; `ENTREGA_F2` ya no lo tiene) | Restos de antes de F2:<br>- `cambios_respecto_entrega_anterior` no menciona F2;<br>- `fuentes_y_preservacion` dice «SHA-256 bb51942c..., 6798/6798 verificados … por mi listado» (el SHA truncado y la sobredeclaración que ya señaló la revisión 3b);<br>- `ENTREGA_B_PM1.siguiente_accion_exacta` sigue diciendo «pasar a Cola 2»;<br>- `PUNTO_DE_RECUPERACION` repite «6798/6798». | `sondas/sonda_entregas_c761cc8_vs_plantilla_out.txt` |
| **R12** | Menor (D6) | `PROTOCOLO_CONGELADO.md` §2.1 (`9873234`, 09:41:31Z) | Dice que los criterios se fijaron «antes de nombrar ninguna candidata». Es cierto dentro del material de F. Pero en el mismo repositorio, `u3_motor_c/CANDIDATOS_C.md` (`95d9e46`, 09:36:01Z) ya nombraba candidatas (FinecoBank 1.º, …). La independencia de F frente a esa lista no es observable. Además, hay dos protocolos de C en paralelo. | `git log` (`sondas/sonda_d6_horas_out.txt`) |
| **R13** | Cosmético | Contrato, línea 4; MAPA, filas B | Texto suelto «ibraltar dos fixtures». El commit `e9f76a9` dice «filas B intactas», pero dos filas B cambian: les quita los acentos («financiación» → «financiacion», «años» → «anos», «convención» → «convencion»). | `git diff 195766f e9f76a9 -- …/MAPA_ENTRADAS.jsonl` |
| **R14** | Menor | `RESPUESTA_F2.md`, `ENTREGA_F2.json` y bloque F2 de `COMANDOS.md` @ `98bdf8f` | Dan por cerrados puntos que esta revisión deja con límites:<br>- repite las citas desplazadas: flujo en `build_v6.py:936-937`, terminal en `940-942`, «933-945»;<br>- dice que «las pruebas de ENTREGA_B3_C1/ENTREGA_B_PM1 llevan ahora comandos ejecutables tal cual», pero R9 sigue (esos archivos no cambian en `98bdf8f`);<br>- en `criterios_cubiertos` pone «F2-D3 … fiel al código» y «F2-D2 alcance completo», aunque siguen R3–R8;<br>- dice que `coordinacion/cierre-v2` @ `57b34a6` está «sin cambios posteriores», cuando hay 12 commits posteriores antes de `98bdf8f`, entre ellos U3 (`95d9e46`, 09:36Z) y U2 (`e393690`, 09:38Z, el `.bat`). `CORRECCION_F2.md` no cambió, así que el fondo se sostiene. | `sondas/sonda_98bdf8f_out.txt`; tabla de R6; `git log 57b34a6..origin/coordinacion/cierre-v2` |
| **R15** | Menor | `ENTREGA_F2.json` | - El `resultado` de la prueba 2 es «EJECUTADO (replica en Python; recálculo del xlsx NO_EJECUTADO …)», un valor compuesto, no EJECUTADO o NO_EJECUTADO como en la plantilla. El límite sí está bien declarado en `criterios_sin_cubrir`.<br>- La prueba 4 (`git log … -7` sin referencia) depende del HEAD de quien la ejecuta: hoy da otra ventana de commits.<br>- La prueba 3 usa el marcador `<ruta_textos_CF_20YY>` y el bloque de `COMANDOS` usa `$ZIP_414` y `$RUTA_TEXTOS` sin definirlos.<br>- `tareas_control` no incluye B-PM1, aunque D7 toca su extractor y su ENTREGA. | Pruebas 0–3 ejecutadas: exit 0 (`sondas/sonda_98bdf8f_comandos_out.txt`) |

**Citas de línea de F frente a las reales (R6).** Archivos idénticos en `957af65` y en la candidata.

| Lo que cita F | F dice | Real |
|---|---|---|
| Elección del motor / nota «Financiera → motor C» | `build_v6.py:146-153` | Elección en `581` (Diagnóstico C5 ← C62); nota en `426`; coherencia en `589` y `1133` |
| Palancas X16 (S2C) | `448-449` | `450-452`; forzado a 1 en `971` (F dice `970`) |
| Palancas X18 | `450-452` | `454-456` |
| L_t = L(t−1)·(1+g_t) | `934` | `927` (la 934 es BH) |
| flujo_t = B(t−1)·ROE_t − ΔB_t | `936-937` | `929-930` (936-937 son BJ, la quiebra, y BK, por acción) |
| ROE_t interpolado | `938` | `928` (la 938 es BL) |
| Valor por acción | `939-945` | `931-937` |
| Valor terminal | `940-942` | `932-934` |
| τ = 0, f = 0, ajuste = 0 / r = C56 | `966-968` / `968-969` | `960-962` / `963` (la 966 es `def put_scen`) |
| test_fill: ROE interpolado / terminal / división / τ, f, adj | `84,92` / `97-98` / `99` / `85-87` | `84,93` / `99-103` / `104` / `86-88` |

Correctas: `282`, `294`, `312`, `444`, `446`, `453`, `1136-1147`, `1142-1144`; `test_fill.py:79`, `93-95`; `relacion_entradas_materiales.py:143-152`; `patch_v62_base.py:255-257`.

---

## 1. F2-D1 · reproducción del inventario desde el ZIP

**Qué ejecuté** (`sondas/d1/`):

```
python3 -I <rev_F2>/entrega/…/preparacion_b3_c1/scripts/inventario_desde_zip.py <zip> inv.csv huellas.csv   # exit 0
cmp inv.csv          …/INVENTARIO_Y_HUECOS.csv                   # idéntico
cmp huellas.csv      …/fuentes/huellas_todas_las_fuentes.csv     # idéntico
```

- **Salida:** «131 recursos, 6799 archivos en el ZIP»; «71 PDF con SHA-256 completo + release bb51942c…7b93e».
- **Reproducción:** byte a byte: `5bc4127a…eaa5` (inventario) y `a7d174f0…d2d5` (huellas), iguales a lo publicado.
- **Recuento independiente** (`sonda_d1_recuento_awk.sh`, en `awk` sobre `unzip -Z1`, sin el script del autor): las 131 filas de recuento coinciden con las publicadas.
  - La suma de recuentos (6476) es igual al número de archivos dentro del alcance.
  - Las n_otros de `empresas_v2` bajan respecto a 52fb120 (Aarsleff 5 → 2…) porque el script viejo contaba los directorios. Lo nuevo es lo correcto.
- **Recuento total:** 6799 = 6798 del manifiesto 4.14 más el propio `MANIFIESTO_SHA256.txt`. Es coherente.
- **El script:**
  - toma la ruta del ZIP por argumento;
  - lee el ZIP con `zipfile`, sin depender de un listado previo;
  - ordena las filas;
  - las filas de hueco son literales fijas, y así se declara.
- **ENTREGA:**
  - **En `195766f`:** `ENTREGA_B3_C1.json` no se tocó (R1), así que «ENTREGA lo declara con el comando exacto» no se cumple en este commit.
  - **En `c761cc8`:** la prueba 0 declara `python3 -I …/inventario_desde_zip.py "$ZIP_414" /tmp/inv_check.csv /tmp/huellas_check.csv && cmp … && cmp …`, con exit esperado y observado 0. Lo ejecuté tal cual desde la raíz extraída, cambiando solo `/tmp/` por `<rev_F2>/sondas/c761cc8_comandos/tmp/`: exit 0.

**Veredicto:** CERRADO CON LÍMITES en `195766f` (por R1); CERRADO en `c761cc8`.

## 2. F2-D2 · alcance y huellas

- **Recorrido:** el inventario incluye `elis_decisiones` (12 xlsx / 83 json / 102 docs / **14 pdf** / 7 otros), `contrastes/` (3 recursos, 6 PDF) y `2026-11_Vidrala_ensayo/fuentes` (9 PDF).
  - Ya no da 0 PDF a Vidrala ni a Viscofan: los PDF de Vidrala están en `contrastes/` y `ensayo/fuentes`; los de Viscofan, en `4_12/viscofan` (12) y en `4_14/viscofan(_decisiones)` (1 + 1).
  - Suma de n_pdf = 71.
- **71 PDF con SHA-256 completo:** lo comprobé por mi cuenta con `unzip -p <zip> <pdf> | sha256sum` y `wc -c`, sin Python (`sonda_d2_pdf_unzip_p.sh`).
  - `unzip -Z1` da 71 rutas `.pdf`; `unzip -l`, también 71.
  - Ruta, bytes y SHA-256 coinciden en los 71 con `huellas_todas_las_fuentes.csv`.
  - Hay 42 huellas distintas, porque los PDF de Elis se repiten en tres expedientes y los de Viscofan en dos.
- **Fila de la Release:** `release/munger_v2_r1_entrega4.14_cierre_verificacion_entradas.zip,1130912246,bb51942cefb848e409a4828e3faeb70f94aa4d29af39cda6d90cd0a97cb7b93e`, con 64 hexadecimales, igual al `sha256sum` del ZIP.
  - En `huellas_fuentes_conservadas.csv` solo cambia la fila de la Release, que ahora lleva el SHA completo. Los otros cambios del diff son de fin de línea (`--ignore-cr-at-eol`): ninguna huella de PDF se tocó.
- **Las 29 de B:** `verificar_huellas.py <zip> FUENTES_CONSERVADAS@daa7478` da 29/29 y exit 0.
  - Con un SHA alterado (control negativo propio), da 28/29, «1 FALLOS» y exit 1 (`sonda_d7_verificar_huellas_out.txt`).
- **Alcance:** se declara en positivo. Lo que queda fuera no se declara (R4).
- **`.bat` de Ahold:** no está registrado (R3). Es el mismo hallazgo de U2 (`RECURSOS_EXISTENTES.md` §4: «"sin .bat": falso»), y sigue sin corregirse en `c761cc8`.

**Veredicto:** CERRADO CON LÍMITES (R3, R4), igual en `195766f` y en `c761cc8`.

## 3. F2-D7 · rutas fijas y comandos

- **En `195766f`:**
  - `inventario_desde_zip.py` y `verificar_huellas.py` toman sus rutas por argumento.
  - El extractor de B-PM1 conserva `/workspace` fijo (R2).
  - La ENTREGA tiene comandos que no se ejecutan (R1).
  - **Veredicto: ABIERTO.**
- **En `c761cc8`:**
  - Ningún `.py` ni `.sh` usa `/workspace`, salvo en un comentario.
  - El extractor, con la ruta de los textos sacados de `<zip>`, da exit 0 y salida idéntica byte a byte.
  - `ENTREGA_B_PM1` prueba 0: ejecutada con el `git show` sobre `<repo>` (la rama `m2-fundamento-pm1` = `daa7478`, CSV `0924feff…`), da 29/29 y exit 0.
  - Quedan los comandos descriptivos o incompletos de R9. `/workspace` y `/tmp` siguen en `COMANDOS.md` y en evidencias como registro histórico del entorno de F, y lo admito como tal.
  - **Veredicto: CERRADO CON LÍMITES.**

## 4. F2-D3 · contrato C y mapa frente al motor

**Comprobación independiente** (`sondas/sonda_d3_motor_c.py`):
- Comparé el texto exacto de 13 fórmulas de `referencia_V6.3.json` (Motor Q7, AA7, AK7, AU7, BE7, BF7, BG7, BH7, BJ7, BK7, N7, O7 e Historia L34): las 13 coinciden con lo que replico.
- Mi réplica está escrita desde esas fórmulas, no desde el script de F.
- Sobre el fixture `Fixture_motorC_original.xlsx` reproduce B78:D78 = 8,3362525831 / 11,9777149618 / 15,2293638877, los valores de LibreOffice del `LEEME.txt`, en sus 10 decimales (`sonda_d3_fixture_c_out.txt`).

| Afirmación de F | Comprobación | Resultado |
|---|---|---|
| X14 = crecimiento del patrimonio, años 1–5 | `build_v6.py:444`; `REF Motor!Q7` | **Correcto**. Omite el descenso lineal hasta g∞ en los años 6–10 (R7) |
| X15 = ROE objetivo en el año 5, no *payout* | `446`; `AK7 = D+(F−D)·MIN(t,5)/5` | **Correcto** |
| X16 no se usa en C | `G7 = IF(C5="C",1,…)` | **Correcto** |
| X18 = ROE a largo plazo, solo en el terminal | `BF7 = AJ7·(I7−H7)` en C | **Correcto** |
| g∞ en Análisis B68:D68 | `453`; `Palancas!B17 = Análisis!B68` (copia) | **Correcto** |
| ROE = beneficio neto atribuible ÷ patrimonio de cierre | `Historia!L34 = L9/L21`; `C60 = L34`; `test_fill.py:79` | **Correcto** |
| Puente 1000 + 100 − 40 = 1060 (antes 1170) | Recalculado | **Correcto**: 1060 y 1170; ROE de cierre 0,094340 |
| Terminal B10·(ROE_lp − g∞)/(r − g∞), descontado 10 años; r = C56; τ = f = ajuste = 0 | `BF7…BH7`, `J7`, `K7`, `L7`, `M7` | **Correcto** |
| Ejemplo 115,06 → 278,45 (×2,42) | Mi réplica: 115,0592 → 278,4507 (×2,4201) | **Correcto**. El script de F, ejecutado aquí, da exit 0 y salida idéntica a su evidencia |
| Base de valor: la del motor; guarda y otras bases, propuesta sin números | §4 | **Correcto** |
| Selección del motor por `Palancas C6` | `Diagnóstico C5` solo lee `Análisis C62` | **Incorrecto** (R5) |
| Citas de línea | Ver la tabla de R6 | **Unas diez desplazadas** (R6) |
| Valor por acción = (VP + VT) ÷ acciones | Falta `BJ` (quiebra) | **Incompleto** (R7) |

**Veredicto:** CERRADO CON LÍMITES.
- Los cinco errores de F2-D3 están corregidos: palancas, ROE, signo de los dividendos, ×2,42 y base de valor.
- R5 conviene corregirlo antes de usar el contrato: es una descripción falsa del lugar donde se elige el motor, aunque el producto la bloquea con V11, así que no daría un valor erróneo en silencio.
- R6 deja a medias la exigencia «con cita de línea».

### 4.1 Comparación con el contrato del coordinador (`u3_motor_c/CONTRATO_C_DESDE_EL_MOTOR.md`, `cc9efb21…2ad7`)

| Tema | Mistral (`c761cc8`) | U3 (coordinador) | Quién tiene razón según el código |
|---|---|---|---|
| Dónde se elige el motor C | `Palancas C6` → Diagnóstico C5 | `Análisis C62` (fase A) → C5; C6 solo da coherencia (REVISAR / V11 NOA) | **U3** (`REF["Diagnóstico V6!C5"]`, `build_v6.py:581,589,1133`) |
| X14, X15, X16, X18, B68 | Correcto | Correcto, y añade el descenso en los años 6–10 y la gramática de B16:D16 vacías | **Coinciden.** U3 es más completo |
| ROE de partida | L9/L21 de cierre | L9/L21 de cierre, y anota que m_t se aplica a la apertura (§7.2) | **Coinciden.** Solo U3 registra la diferencia de convención |
| Puente y caso numérico | 1060; «dividendo = BN − ΔB» | 1060; flujo = 40 = dividendos; excedente limpio como hipótesis (variante con OCI) | **Coinciden** en el número. U3 acierta en la condición (R8) |
| Efecto del *payout* en X15 | ×2,42 (base B0 = 100, ROE0 = 10 %, g1 = 3 %…) | ×1,81 sobre el fixture C_orig; dice que no reproduce ×2,42 | **Los dos son correctos**, con bases distintas. Reproduje ambos: ×2,4201 y 21,7086/11,9777 = ×1,8124 |
| Quiebra (C22/C23) | No aparece | `BJ = (1−p)·BI + p·rec` | **U3** (`REF Motor!BJ7`, `N7`, `O7`) |
| Terminal, r, τ/f/ajuste, acciones | Correcto | Correcto, y añade las condiciones de `BS` y BL | **Coinciden** |
| Citas de línea | Desplazadas (R6) | Coinciden con el código en las que comprobé (`927`, `929-930`, `931-937`, `960-964`, `971`, `454-456`, `581-582`) | **U3** |
| «Ventas» (Historia fila 6) bloquea C | No aparece | §7.1, PD-4 | No lo verifiqué a fondo. Es un hallazgo de U3 que F no trata |
| Guarda de capital y base alternativa | Propuesta sin números | PD-1 y PD-2, sin números | **Coinciden** |

No hay ninguna contradicción en la que F acierte y U3 falle. Las discrepancias son R5, R6, R7 y R8, y en todas el código da la razón a U3.

## 5. F2-D6 · horas y protocolo

- **Horas:** las de `COMANDOS.md` @ `9873234`/`c761cc8` coinciden al segundo con la fecha de autor y de commit de `90329a1`, `e94ee7c`, `c7716a0`, `223f16d`, `52fb120` y `868f448` (`sonda_d6_horas_out.txt`).
  - La de la evidencia de B-PM1 (21:48:58Z) también cuadra.
  - Las horas aproximadas anteriores («~22:00–22:20», «~22:30») desaparecen.
  - Límite menor: `COMANDOS.md` no añade un bloque F2; los comandos de F2 están solo en evidencias y ENTREGA.
  - **CERRADO.**
- **Protocolo antes de candidata:** **CERRADO CON LÍMITES** (R5, R12).
  - Orden de los commits: contrato (`e9f76a9`, 09:39:34Z) → protocolo (`9873234`, 09:41:31Z).
  - `SELECCION.csv` no ha cambiado desde `52fb120`: no nombra ninguna entidad financiera, solo «banco o aseguradora europea…».
  - Ningún commit de F posterior nombra candidata.
  - Los criterios no usan precios: tipo de entidad, fuente mínima con huella, método posible y desempate por fuente y después por negocio.
  - El criterio 1 repite el error de `Palancas C6` (R5).
  - U3 había publicado candidatas antes en el mismo repositorio (R12).
  - La errata I18 → I19 está corregida.

## 6. Punto 4 · pendientes y contrato C

- **En `195766f`:** ni el mensaje, ni el README, ni las evidencias, ni el `PUNTO_DE_RECUPERACION` declaran pendientes D3–D6. El `PUNTO` sigue pidiendo el contraste B-PM1, que ya está hecho. No se menciona `u3_motor_c` y no se duplica el contrato.
- **Después:** `e9f76a9` reescribe `CONTRATO_C_PROPUESTA.md` y `9873234` añade un protocolo de C. Los dos van en paralelo a `u3_motor_c/` (`95d9e46`), sin mencionarlo ni conciliarse con él. Hay, por tanto, dos contratos y dos protocolos de C. Según el encargo, no juzgo cuál prevalece; la comparación técnica está en §4.1.

## 7. Higiene

- **Manifiestos:** `sha256sum -c` da 0 en `195766f` (39 entradas), `e9f76a9` (42), `9873234` (43) y `c761cc8` (44). En los cuatro, la lista coincide con la carpeta.
- **`git diff --name-only 868f448 195766f`:** 10 rutas. **`868f448 c761cc8`:** 23 rutas. Todas bajo `resultados_cierre/alcance_real/`.
- Ningún PDF, XLSX, ZIP, pyc, caché, `.trabajo` ni `.env`. Ningún binario en `--numstat`.
- Ningún patrón de secreto (password, secret, api key, ghp_, github_pat_, sk-, AKIA, clave privada, bearer, token) en las líneas añadidas (`sonda_higiene_out.txt`, `sonda_higiene_hasta_c761cc8_out.txt`).
- **ENTREGA frente a la plantilla:** las dos ENTREGA @ `c761cc8` tienen exactamente las claves de la plantilla y de sus pruebas. `es_plantilla` es false, `commit_entrega` no se autorreferencia, `integrado_en_producto` es false, `apto_dinero_real` lleva el texto de la plantilla y no hay ningún «APROBADO». Pero falta la ENTREGA de F2 (R10) y los campos están desfasados (R11).
- **CONTROL:** F no lo toca. Dice F-B3/F-C1 = CORRECCIONES y B-PM1/F-REV = CONFORME_CON_LIMITES, coherente con lo que F declara ahora (D5).

## 8. Ampliación a `98bdf8f`

- **Qué cambia:** cuatro rutas, `COMANDOS.md`, `MANIFIESTO_SHA256.txt`, `correccion_f2/ENTREGA_F2.json` (nuevo) y `correccion_f2/RESPUESTA_F2.md` (nuevo). Ningún archivo revisado en `195766f…c761cc8` cambia: script, CSV, contrato, mapa, protocolo, `ENTREGA_B3_C1`, `ENTREGA_B_PM1`, extractor y `PUNTO` son los mismos blobs. Por eso R3–R9, R11, R12 y R13 siguen igual; R10 queda resuelto.
- **Manifiesto:** `sha256sum -c` da 0; 46 entradas = 46 archivos, y la lista coincide con la carpeta.
- **Higiene `868f448..98bdf8f`:** todo bajo `alcance_real/`. Sin binarios, cachés ni secretos.
- **`ENTREGA_F2.json` frente a la plantilla** (idéntica en `57b34a6`, `704e6bb` y HEAD):
  - no falta ni sobra ninguna clave, y tampoco en las 6 pruebas; los tipos coinciden;
  - `es_plantilla` es false, `commit_entrega` no se autorreferencia, `integrado_en_producto` es false, `apto_dinero_real` lleva el texto de la plantilla y no hay ningún «APROBADO»;
  - `base_revisada_sha` = `868f448` y `candidata_producto_sha` = `957af65`, ambos correctos;
  - `cambios_respecto_entrega_anterior` describe bien los cuatro commits;
  - límites: R14 y R15.
- **Pruebas de `ENTREGA_F2` ejecutadas por mí** desde la raíz extraída, cambiando solo `/tmp` por `<rev_F2>/sondas/c98bdf8f/tmp` y el marcador de la ruta por los textos sacados de `<zip>`:
  - prueba 0: exit 0 y los dos `cmp` iguales;
  - prueba 1: 29/29 y exit 0;
  - prueba 2: «TODO CUADRA» y exit 0;
  - prueba 3: exit 0, con la salida idéntica a la publicada.
- **`RESPUESTA_F2.md`:** responde punto por punto con comandos y códigos. Lo que dice de D1, D2 (cifras), D4, D5 y D6 (horas) coincide con lo que reproduzco. Lo que dice de D3 (citas) y D7 (ENTREGA anteriores «tal cual») no se sostiene entero (R14).

## Comandos principales

```bash
git -C <repo> archive 195766f resultados_cierre/alcance_real | tar -x -C <rev_F2>/entrega
git -C <repo> archive c761cc8 resultados_cierre/alcance_real | tar -x -C <rev_F2>/entrega_c761cc8
sha256sum <zip>
python3 -I <rev_F2>/entrega/…/scripts/inventario_desde_zip.py <zip> inv.csv huellas.csv && cmp … && cmp …
unzip -Z1 <zip> > sondas/d1/zip_Z1.txt
bash sondas/sonda_d1_recuento_awk.sh sondas/d1/zip_Z1.txt …/INVENTARIO_Y_HUECOS.csv
bash sondas/sonda_d2_pdf_unzip_p.sh <zip> …/huellas_todas_las_fuentes.csv sondas/d2
bash sondas/sonda_d2_alcance.sh sondas/d1/zip_Z1.txt …/INVENTARIO_Y_HUECOS.csv
python3 -I …/correccion_f2/scripts/verificar_huellas.py <zip> sondas/d7/FUENTES_CONSERVADAS_daa7478.csv   # y mutante
python3 -I sondas/sonda_d3_motor_c.py <candidata>/munger_v2_r1/v6/referencia/referencia_V6.3.json
python3 -I sondas/sonda_d3_fixture_c.py <candidata>/munger_v2_r1/v6/pruebas/fixtures/Fixture_motorC_original.xlsx
bash sondas/sonda_d3_citas.sh <candidata>/munger_v2_r1
python3 -I <rev_F2>/entrega_c761cc8/…/correccion_f2/scripts/verificar_contrato_c.py
(cd <rev_F2>/<árbol>/resultados_cierre/alcance_real && sha256sum -c --quiet MANIFIESTO_SHA256.txt)
# 98bdf8f: pruebas de ENTREGA_F2 (sondas/sonda_98bdf8f_comandos_out.txt); plantilla y manifiesto (sondas/sonda_98bdf8f_out.txt)
```

## Huellas

**Material revisado (blobs).** Los marcados «@ `c761cc8`» son el mismo blob en `98bdf8f`:

| SHA-256 | Archivo |
|---|---|
| `bb51942cefb848e409a4828e3faeb70f94aa4d29af39cda6d90cd0a97cb7b93e` | `<zip>` |
| `0a5e7a66797d36f0d7b19f404078ca3a1989a035807334f44177306c5eaa9325` | `inventario_desde_zip.py` (igual en `195766f` y `c761cc8`) |
| `5bc4127a71af118c8ac0f432c5232a1651ab020403c3842e5dd3b0af9284eaa5` | `INVENTARIO_Y_HUECOS.csv` (igual en `195766f` y `c761cc8`) |
| `a7d174f02d11fa465741254a89148cdf8840b839c37d8fdc0ddcf1ed660bd2d5` | `huellas_todas_las_fuentes.csv` |
| `b40ddd04535135704af061d6025b8bd0bceb02b7e81bbcabc54cb7549deb275d` | `huellas_fuentes_conservadas.csv` @ `195766f` |
| `6423cf6115e2c74ad98485db796308d14b8c19d304f6edc7e7f39ae63f242c31` | `verificar_huellas.py` |
| `02c06c74847c590d9edb1173fca82cd10304766b284c95719194d4192c3b8518` | `CONTRATO_C_PROPUESTA.md` @ `c761cc8` |
| `70cd4861ae8e7311d6448722bb49e7f1c31ea8754f780b66e3b85585c4bf930f` | `MAPA_ENTRADAS.jsonl` @ `c761cc8` |
| `8dd963dadb1a772a7969b04e91aa795cfbafd3a57c4926012ff5c33b62b27b42` | `PROTOCOLO_CONGELADO.md` @ `c761cc8` |
| `e1669e433d1a345a9e93e7920f3b379e19119735d2a5bddf087ad4b2800bea1b` | `ENTREGA_B3_C1.json` @ `c761cc8` |
| `396f13f487fa06ea6f9da7a75250b21c013863285f541970d91bf9d5263a7a3e` | `ENTREGA_B_PM1.json` @ `c761cc8` |
| `5f91768afb738aebe13535642638d29fb8addbcd467fce0f8d13e29a066754c3` | `extraccion_independiente_pm1.py` @ `c761cc8` |
| `4c742d102b366067fd57219252be99b8428dcf51cc0f380fcd5130cf81e52aac` | `verificar_contrato_c.py` |
| `a5a8818d37ff8fad25c4e736415ae45254d291b97e7ca66004e17a9fa9a9171a` | `PUNTO_DE_RECUPERACION.md` @ `c761cc8` |
| `8c195a54d83a2c26cfcfd2ce1ec86b3c44681bdaef680506872c5750618f5f43` | `COMANDOS.md` @ `c761cc8` |
| `d36a7baea90474f71e53baae65e4fd5c4097cf574df26ab1289cefa3b21c5034` | `MANIFIESTO_SHA256.txt` @ `c761cc8` |
| `717e0b669c321d08abb9debb4e88e28a4a6463c8757732e17a35325a466d224f` | `MANIFIESTO_SHA256.txt` @ `98bdf8f` |
| `86e3fa21f13ee7d5c1bda53660973925829de1f0eb0f3894a952af8ca1cf3bb8` | `correccion_f2/ENTREGA_F2.json` @ `98bdf8f` |
| `762b79a559aeb72ee6405e904fc4f5797d0507517a996fc5e4830c3dad7e98de` | `correccion_f2/RESPUESTA_F2.md` @ `98bdf8f` |
| `1dc4e4e1b109c4665b3b93822d4233d22f8fbe95bb04f4888bd9360c7252fe07` | `COMANDOS.md` @ `98bdf8f` |
| `04feebd409754a91e509dfde1e8dd63a1e8534695d05cb75fffca6a97bd53d88` | `.bat` de Ahold en `<zip>` |
| `80c5c16600e30eaeedede2ac33abc4b24aa376363ab5485a4bdce29c1c1552fe` | `CORRECCION_F2.md` |
| `666673150c9935348c7a594f889374545eebd40a9152c1d82eb38bc4d9d01031` | `REVISION_F_223f16d_52fb120.md` |
| `cc9efb212e98c172bf60e0f24dc7b656bd3fd0d8f21ca2af32ab6a7926bf2ad7` | `u3_motor_c/CONTRATO_C_DESDE_EL_MOTOR.md` |
| `cce3d69edd87ac190114b4cababcddaf29e27020d397d9cd0b4942a8eb616ecb` | `u2_tercer_b/RECURSOS_EXISTENTES.md` |
| `05bf108112d0fcfaa028b88e4da6c320f71ca96b42678b073175e6ec2dfe12a5` | `PLANTILLA_ENTREGA.json` |
| `500c8d3a28b3775e1b5307d712380ed49346726c5d5b153502cd40ae5b133146` | `<candidata>/…/V6.1/build_v6.py` |
| `bd9e58500b9d5e495a8d5a5e2471e3f11442730460dcaf3eb49321538b49feac` | `<candidata>/…/V6.1/test_fill.py` |
| `4e8d136a744fb6694be8927b407ba39275a3bf2479f414fca08942d0dc25d0d7` | `<candidata>/…/referencia_V6.3.json` |
| `6b518138a899ad83bda594031fe4b6e2ffe66a00990610676a77ce2435ccc3f7` | `<candidata>/…/Fixture_motorC_original.xlsx` |

**Sondas:** en `<rev_F2>/sondas/SHA256SUMS.txt`.

*Revisión independiente con límites declarados. No es una aprobación ni acredita aptitud económica. La aceptación la registra el coordinador.*
