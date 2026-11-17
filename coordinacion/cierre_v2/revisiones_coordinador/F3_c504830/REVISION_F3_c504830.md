# Revisión independiente de la respuesta de Mistral F a CORRECCION_F3 · de `98bdf8f` a `c504830`

- **Revisor:** subagente Claude (Opus 5.5), lanzado por el coordinador. No soy autor del material revisado; su autor es Mistral F (relevo `mistral-large-4-0`). **Límite de independencia:** el coordinador que me lanza también es Claude y es autor del contrato y del protocolo de U3 con los que se compara el de F. Doy hechos reproducibles; no decido la aceptación.
- **Fecha:** 2026-11-17.
- **Objeto:** rama `mistral/f-alcance-real` de `<repo>` (`munger-v2-evidencias-mistral`), de `98bdf8f` a `c504830` (`27c5931`, `c4d918f`, `52eca91`, `c504830`), carpeta `resultados_cierre/alcance_real/`. `git fetch` de `mistral/f-alcance-real` (= `c504830`) y de `coordinacion/cierre-v2` (= `a79e62d` al terminar).
- **Encargo aplicado:** `CORRECCION_F3.md` (`677c6cfa…7c2a`), solo los puntos abiertos R3–R15, con `REVISION_F2_195766f_98bdf8f.md` (`6325fa2b…f670`) y sus sondas. Contrato y protocolo de U3: `CONTRATO_C_DESDE_EL_MOTOR.md` (`cc9efb21…2ad7`, sin cambios desde `95d9e46`) y `PROTOCOLO_SELECCION_C.md` (`3e28d9c0…7855`). Contexto nuevo: `VERIFICACION_FINECO.md` (`245a2e6b…b6839`).
- **Material local:**
  - copia de la entrega: `git worktree add --detach <rev_F3>/wt c504830`;
  - `<zip>`: ZIP base-4.14 en `<e_work>/dl_base414/`, SHA-256 `bb51942cefb848e409a4828e3faeb70f94aa4d29af39cda6d90cd0a97cb7b93e`, recalculado (**encontrado**);
  - `<candidata>`: `<home>/wt/candidata` @ `3149128`; `git diff 957af65 HEAD -- munger_v2_r1/v6` vacío. `build_v6.py` `500c8d3a…b133146` y `test_fill.py` `bd9e5850…49feac`, iguales a los que cita F (@ `957af65`).
- **Cómo reejecuté los comandos de ENTREGA tal cual:** cada `comando` se pasa **byte a byte** a `bash -c` desde la raíz del worktree, con `ZIP_414=<zip>`. Para no escribir fuera de `<rev_F3>`, lo ejecuté en un espacio de montaje propio (`unshare -m`) con `/tmp` montado sobre `<rev_F3>/sondas/tmp_ns1/`. Así el texto del comando no cambia (`sondas/sonda_entregas_tal_cual.py`; la huella de cada comando está en `sondas/entregas_tal_cual/*.txt`).
- **No hice:** commit, push, cambios en ramas, red (salvo `git fetch`), LibreOffice ni el pipeline. Escribí solo en `<rev_F3>/`, más el registro del worktree que crea `git worktree add`.

## Veredicto

**CORRECCIONES MENORES. No hay defecto material.**

- **Lo técnico del motor C queda bien:** motor en `Análisis!C62`, citas, quiebra, descenso de g_t, excedente limpio y ROE de cierre frente a apertura. El inventario es correcto: `.bat` con huella y alcance negativo, reproducible byte a byte.
- **Siguen abiertos R12, R14 y R15:**
  - R12: el protocolo de F conserva criterios propios de admisión y desempate de C, distintos de los de U3;
  - R14 y R15: dos afirmaciones que F2 señalaba siguen sin corregir, y la prueba de horas no cubre lo que dice cubrir.
- **Hallazgos nuevos menores:** una prueba atribuye a un script lo que el script no comprueba, un comando de `COMANDOS.md` no se ejecuta y una prueba no discrimina.
- **Textos desfasados por el contexto de hoy** (§«Contexto nuevo»): la entrega es anterior a la decisión U3. No es un defecto del autor, pero hay que actualizarlos.

| Punto | Estado en `c504830` | Motivo principal |
|---|---|---|
| **R3** `.bat` de Ahold | **CERRADO** | Fila propia con `04feebd4…d53d88`; README y SELECCION corregidos. Los 4 `.bat` del ZIP tienen fila y huella. |
| **R4** alcance negativo | **CERRADO** | 6799 = 6476 + 323, con un desglose que coincide con mi `awk` independiente; 0 PDF y 0 `.bat` fuera |
| **R5** elección del motor | **CERRADO** | `Análisis!C62` en el contrato §1, el protocolo §2.1.1 y el MAPA; contraejemplo recogido |
| **R6** citas de línea | **CERRADO CON LÍMITES** | Contrato, protocolo, MAPA, RESPUESTA_F2/F3 y la evidencia r6: correctos (26/26 líneas). Quedan las citas viejas en `COMANDOS.md:164`, y el comando de verificación de `COMANDOS.md:193` falla. |
| **R7** quiebra y g_t | **CERRADO** | `BJ = (1−p)·BI + p·rec` con C22/C23 y g_t lineal (`:926`); 105,5532 reproducido |
| **R8** excedente limpio y ROE | **CERRADO** | Contrato §3–4: condición de excedente limpio (1025/75/50) y ROE de cierre 9,434 % frente a 10 % de apertura |
| **R9** comandos de ENTREGA | **CERRADO CON LÍMITES** | Los tres señalados se ejecutan tal cual, con código 0 y resultado idéntico byte a byte. Otros dos «comandos» siguen siendo descriptivos (código 2). La prueba de `tablas_vidrala` pasa aunque el script no haga nada. |
| **R10** | **CERRADO** (ya en `98bdf8f`) | Sin cambios |
| **R11** restos de antes de F2 | **CERRADO CON LÍMITES** | Lo señalado está corregido. Quedan `.trabajo` y la siguiente acción F2 en `ENTREGA_B3_C1`, y «6798/6798» en el protocolo §3 |
| **R12** dos contratos y protocolos | **ABIERTO** | Contrato alineado. El protocolo §2.1.1–5 mantiene criterios propios de C (sin C2, C3, C4 ni X1–X4; otro desempate): admitiría a FinecoBank, que U3 no admite |
| **R13** cosmético | **CERRADO CON LÍMITES** | Texto suelto eliminado y acentos de las dos filas restaurados. Se tocan otras 4 filas B que nunca tuvieron tilde, y se dice «restaurados» |
| **R14** afirmaciones de F2 | **ABIERTO** | `ENTREGA_F2.json:22` sigue con «sin cambios posteriores» y `COMANDOS.md:164`, con «933-945» |
| **R15** ENTREGA_F2 y COMANDOS | **ABIERTO** | La prueba 4, con rango fijo, ya no muestra las horas que dice cubrir. La hora final sigue en 09:44 en dos sitios. El patrón se repite en F3: dice 13:16, y el último commit es de las 13:18:19 |
| **Política económica / motor C** | **CONFORME** | No se fija ningún número ni umbral. El motor C figura como «no ejecutado, no validado» |
| **Manifiesto** | **CONFORME** | `sha256sum -c` da 0; 53 entradas = 53 archivos; sin rutas locales |

---

## Hallazgos con prueba de cierre

| Id | Gravedad | Dónde (@ `c504830`) | Defecto | Evidencia | Prueba de cierre |
|---|---|---|---|---|---|
| **H1 (R12)** | Medio | `PROTOCOLO_CONGELADO.md:24-39`; también `:16-22` y `:67-73`; `SELECCION.csv:6` | Se dice «No se mantiene un segundo protocolo paralelo» (`:43`), pero §2.1.1–5 conserva criterios propios de admisión y desempate para C.<br>- **Admisión:** tipo, fuente con huella y método posible. **Faltan** C2 (cotizada), C3 (idioma), C4 (10 años) y X1–X4 de U3.<br>- **Desempate:** «primero la mejor fuente documental; después el negocio». U3 §5 desempata por familias, luego R2, luego R3/R5/R6, luego AT1, luego euro y por último idioma.<br>- `:26` repite «antes de nombrar ninguna candidata» sin la salvedad de R12: U3 había nombrado candidatas a las 09:36:01Z. | **Contraejemplo de hoy:** FinecoBank es un banco fuera de muestra, con informe anual, ESEF y Pilar 3 descargados con SHA-256, y el motor es aplicable (`VERIFICACION_FINECO.md` §1, §6). Pasa los criterios 1–3 de F. Según U3 **no encaja**: falla C4 (9 consolidados, no 10) y C3 es dudoso (§6.1, §10). | §2.1 no contiene criterios propios de admisión ni de desempate de C. Remite a `u3_motor_c/PROTOCOLO_SELECCION_C.md` con su SHA-256, o los copia literalmente, con la misma fuente. `:26` lleva la salvedad. Comprobación: ningún texto de F admite un caso que U3 rechaza (Fineco). |
| **H2 (contexto)** | Menor (no imputable: la entrega es anterior) | `CONTRATO_C_PROPUESTA.md:3-4` y `:100-105`; `PROTOCOLO_CONGELADO.md:40-43` y `:71-73`; `ENTREGA_F3.json:79` y `:91`; `RESPUESTA_F3.md:53`; `PUNTO_DE_RECUPERACION.md:34-37` y `:57-59`; `SELECCION.csv:2` y `:6`; `README.md` (Hallazgos C) | Textos desfasados:<br>- dicen que las descargas de FinecoBank fueron «denegadas por permisos» y presentan U3 como una lista Fineco/Hannover pendiente de descarga;<br>- llaman al contrato U3 «de la persona responsable», cuando es una propuesta del coordinador, no adoptada (U3 l. 3: «No es una decisión ni una aprobación»);<br>- dicen «Ahold sin Excel de etapa 1 (insumo no entregado)»;<br>- `PUNTO:37` y `ENTREGA_F2.json:110` dicen que la candidata la fija el coordinador, y el protocolo, que la elige la persona responsable. | Decisión U3 registrada en `72c49e5` (13:25:07Z); Fineco verificado y «no encaja» en `472a08e`/`cefc77f` (13:41–13:42Z); segundo candidato en curso en `a79e62d`; U2 (Ahold) en `3b07d89` (13:28:16Z). Todo es posterior a `c504830` (13:18:19Z): `sondas/sonda_horas_out.txt`. | Reflejan el estado: Fineco descargado y verificado, no encaja tal como está escrito (C4; C3 dudoso; `245a2e6b…`), y se busca otro candidato. La elección es de la persona responsable sobre U3, que no está adoptado. Se nombra la aportación U2 de Ahold. Ningún texto da por elegida una candidata. |
| **H3 (R14)** | Menor | `ENTREGA_F2.json:22`; `COMANDOS.md:164` | R14 nombraba las dos afirmaciones y siguen:<br>- «coordinacion/cierre_v2 @57b34a6 (…, **sin cambios posteriores**)»; solo se corrigió en `RESPUESTA_F2.md:3`;<br>- citas viejas «`build_v6.py:147,…,444-453,933-945,1136-1147`; `test_fill.py:…,93-99`». El flujo y el terminal están en 929-934, no en 933-945. | `grep -n 'sin cambios posteriores'`; `sondas/sonda_citas_out.txt` | Las dos líneas, corregidas como en `RESPUESTA_F2`. `grep -n '933-945\|sin cambios posteriores'` sobre `alcance_real/` solo devuelve el registro histórico, y marcado como tal. |
| **H4 (R15)** | Menor | `ENTREGA_F2.json:92` y `:96`; `ENTREGA_F2.json:17`; `RESPUESTA_F2.md:4` y `:35`; `RESPUESTA_F3.md:4`; `ENTREGA_F3.json:13`; `COMANDOS.md:179` | - La prueba 4 dice cubrir «90329a1 21:16:13Z … 868f448 22:07:42Z», pero el rango `868f448..98bdf8f` **excluye** esos commits. Ejecutada tal cual, solo lista `195766f…98bdf8f`.<br>- La hora final del bloque F2 se corrigió en `COMANDOS.md:139`, pero sigue en «09:24–09:44» en ENTREGA_F2 y RESPUESTA_F2.<br>- En F3 se repite el patrón: «13:05–13:16» frente al último commit, a las 13:18:19Z (COMANDOS dice «~13:20»). | `sondas/entregas_tal_cual/correccion_f2_ENTREGA_F2.json_p4.txt`; `sondas/sonda_horas_out.txt` | La prueba 4 lista exactamente los commits cuyas horas declara: por ejemplo, `git show -s --format=… 90329a1 e94ee7c c7716a0 223f16d 52fb120 868f448`, o un rango que los incluya. Las horas finales coinciden con el último commit de cada bloque en todos los archivos. |
| **H5 (R9)** | Menor | `ENTREGA_B3_C1.json:63` (prueba 2); `ENTREGA_B_PM1.json:69` (prueba 3) | Siguen siendo descripciones («`gh api contents ... (E62) @ …`», «`git show …json (conclusion_frente_B, …); gh release view …`»). Llevan `EJECUTADO` y código 0, y `RESPUESTA_F3`/`ENTREGA_F3` dicen «comandos de ENTREGA ejecutables tal cual». | Tal cual: `syntax error near unexpected token '('`, código 2 (`sondas/entregas_tal_cual/preparacion_b3_c1_ENTREGA_B3_C1.json_p2.txt`, `…ENTREGA_B_PM1.json_p3.txt`) | Una de dos: se convierten en comandos que se ejecutan tal cual con código 0, o se declaran como consulta descriptiva con `exit_observado` null y el resultado de la plantilla. La afirmación de RESPUESTA_F3 se ajusta a lo que hay. |
| **H6 (R9)** | Menor | `ENTREGA_F3.json` prueba 2; `ENTREGA_B_PM1.json` prueba 1 | La prueba no discrimina. `git archive` ya extrae `VIDRALA_REPOSICION_CAPACIDAD.csv` de `daa7478`, así que el `cmp` pasa aunque `tablas_vidrala.py` no escriba nada. | Control A, con `python3 -I -c pass` en lugar del script: código 0. Control B, borrando antes el CSV y ejecutando el script: código 0, CSV idéntico (**el resultado de F es cierto**). Control C, borrando el CSV y sin script: código 2 (`sondas/sonda_r9_control_tablas_out.txt`) | El comando borra el CSV extraído antes de ejecutar el script (`rm -f resultados_m2/pm1/VIDRALA_REPOSICION_CAPACIDAD.csv && …`), y se registra un control negativo. |
| **H7 (nuevo)** | Menor | `ENTREGA_F3.json:41` (prueba 1, `criterios_cubiertos`) | Atribuye a `verificar_contrato_c.py` la cobertura de «F3-R5: motor en Análisis!C62» y de «F3-R6: citas reales verificadas». El script no lee el producto ni ningún archivo: solo importa `sys` y `fractions` y hace aritmética interna (`verificar_contrato_c.py:15-84`). | Lectura del script. R5 y R6 sí son ciertos, pero los acreditan mis sondas (`sonda_r5_r7_ref_out.txt`, `sonda_r6_evidencia_out.txt`), no esa prueba. | Se quitan R5 y R6 de esa prueba, o se añade una prueba que los compruebe contra el producto. Por ejemplo, extraer `build_v6.py:581-582,588-590,1102-1103,1132-1133` y comparar con `cmp` contra la evidencia r6, o leer `REF["Diagnóstico V6!C5"]` y comprobar que no contiene `Palancas`. |
| **H8 (R6/R15)** | Menor | `COMANDOS.md:183` y `:193` | El bloque F3 da como comando de verificación de citas `sed -n '581p;926,937p;960-963p;…'`. `960-963p` no es sintaxis de `sed`. Además, `<clon_producto>` no se define. | `sed: -e expression #1, char 18: unknown command: '-'`, código 1 (`sondas/sonda_comandos_f3_bloque_out.txt`) | `960,963p`, y la variable definida al inicio del bloque, igual que `$ZIP_414`. Al ejecutar el comando, la salida coincide con la evidencia r6. |
| **H9 (R11)** | Menor | `ENTREGA_B3_C1.json:22` y `:99`; `PROTOCOLO_CONGELADO.md:47` | Restos:<br>- «verificado por mi en .trabajo/insumos_m2», aunque `RESPUESTA_F3` dice que ya no es así;<br>- la siguiente acción de B3_C1 sigue en F2;<br>- «6798/6798 verificados». | `grep` (§R11) | Los tres textos, alineados con `ENTREGA_B_PM1` y `PUNTO`: el ZIP, 6799 = 6798 + manifiesto, y la siguiente acción vigente. |
| **H10 (R13)** | Cosmético | `MAPA_ENTRADAS.jsonl`, filas B 1, 5, 10 y 13 | Restaura los acentos de las dos filas tocadas en `e9f76a9`, pero cambia otras cuatro filas B que en `195766f` no tenían tilde. `RESPUESTA_F3` lo presenta como «restaurados» («variación», «valoración»). | `diff` de las filas B entre `195766f` y `c504830` | Las filas B, idénticas a `195766f`, o el cambio declarado como ortográfico nuevo, no como restauración. |

## Comprobación por punto (R3–R15)

### R3 · `.bat` de Ahold — CERRADO (`27c5931`)

- **Inventario** (`INVENTARIO_Y_HUECOS.csv`, filas `descargar_*.bat`): 4 filas. La de Ahold es `…/descargas_bat,…,conservado en el ZIP; SHA-256 04feebd409754a91e509dfde1e8dd63a1e8534695d05cb75fffca6a97bd53d88; NO ejecutado`.
- **Comprobación independiente** (`sondas/sonda_r3_r4_alcance.sh`, `unzip -p | sha256sum`, sin el script del autor):
  - el ZIP tiene exactamente 4 `.bat`, y las cuatro huellas coinciden con las filas;
  - la única ruta con «ahold» es ese `.bat`.
- **Textos:**
  - `README.md` (Hallazgos B): «su `.bat` … **sí está conservado** … pero **no se ha ejecutado**»;
  - `SELECCION.csv:2`: «.bat conservado en el ZIP (SHA-256 04feebd4…d53d88) pero NO ejecutado»;
  - el hueco de Ahold: «el .bat de descargas SÍ está conservado».
- **Prueba 0 de ENTREGA_F3, tal cual:** código 0. El `.bat` da `04feebd4…d53d88`, y el `cmp` del inventario sale idéntico.

### R4 · alcance negativo — CERRADO (`27c5931`)

- **Fila del ZIP:** «6799 archivos en el ZIP; dentro del alcance: 6476; fuera (declarado): 323». Desglose: `documentacion_reparacion` 45, `empresas_v2_correcciones` suelto 1, `kit_pipeline_munger` 26, `personaje_v2` otros 152, raíz 8, `v6` 91.
- **Recuento independiente** (`awk` sobre `unzip -Z1`):
  - 7462 entradas = 663 directorios + 6799 archivos;
  - 0 archivos fuera de `munger_v2_r1/`;
  - la misma partición, número a número;
  - fuera del alcance: 0 PDF y 0 `.bat`.
- Los 152 de `personaje_v2` se reparten así: 21 sueltos, `corpus/` 28, `esquema/` 5, `prompts/` 8, `pruebas/` 48 y `scripts/` 42.
- El docstring (`inventario_desde_zip.py:5-16`) y el README declaran los dos alcances.
- La prueba 0 de ENTREGA_F2, tal cual, da código 0 con los dos `cmp`. El inventario se sigue reproduciendo byte a byte.

### R5 · motor en `Análisis!C62` — CERRADO (`c4d918f`)

- **Dónde está corregido:**
  - `CONTRATO_C_PROPUESTA.md:18-25`;
  - `PROTOCOLO_CONGELADO.md:30-32`;
  - la fila «Elección de motor» de `MAPA_ENTRADAS.jsonl`.
- **Sobre `REF` y el código:**
  - `Diagnóstico V6!C5` no contiene `Palancas`;
  - con C62 = «Sí» y C6 = Financiera, la fase A elige el motor A; salen REVISAR (`:589-590`) y V11 NOA (`:1133`). El contraejemplo de F es correcto (`sondas/sonda_r5_r7_ref_out.txt`).
- **Matiz menor (no lo cuento como defecto):** el contrato §1 cita solo «No · banco o aseguradora». C5 acepta también la etiqueta antigua «No · banco, aseguradora o regulada» (`:582`), que U3 §1 sí menciona.

### R6 · citas — CERRADO CON LÍMITES (`c4d918f`, `52eca91`)

- **Volcado de las líneas reales** (`sondas/sonda_citas.py`, sobre 9 textos y 116 citas; salida en `sonda_citas_out.txt`): son correctas todas las del contrato, el protocolo, el MAPA, `RESPUESTA_F3`, `RESPUESTA_F2` (ya corregida) y el docstring del script. Por ejemplo:
  - `:169-170` es Lista C62; `:581-582` es C5; `:588-590` es REVISAR; `:1102-1103` es V01; `:1132-1133` es V11; `:426` es la nota;
  - `:926` es g_t; `:927` es L_t; `:928` es m_t; `:929-930` es el flujo; `:931` es BE; `:932-934` es el terminal; `:935` es BI; `:936` es BJ; `:937` es BK;
  - `:960-962` son τ, f y ajuste; `:963` es r; `:964` es C55; `:971` es S2C; `:972` es g∞; `:919-922` es BS; `:507-509` son C22/C23;
  - `TF:79,84,86-88,93-95,99-104`; `P62:255-257`.
- **Evidencia `r6_citas_reales_957af65.txt`:** sus 26 líneas son idénticas al código de la candidata (`sonda_r6_evidencia_out.txt`).
- **Límites:** `COMANDOS.md:164` (H3) y el comando de `COMANDOS.md:193` (H8).

### R7 · quiebra y g_t — CERRADO (`c4d918f`)

- **Contrato:**
  - §2, fila `C22/C23`;
  - §5: «`BJ = (1−p)·BI + p·rec`… `BK = BJ / Análisis!C55`… El valor por acción es **BJ ÷ nº acciones**»;
  - X14: «en los años 6–10 g_t baja en línea recta hasta g∞».
- **`REF`:** `Motor!BJ7 = (1-$N7)*BI7+$N7*$O7`, `N7 = N(Palancas!$C22)`, `O7 = N(Palancas!$C23)` y `Q7 = …$E7-($E7-$H7)*(Q$3-5)/5`.
- **Réplica propia:** BI = 115,0592 y BJ = 105,5532, como declara F.

### R8 · excedente limpio y ROE de cierre/apertura — CERRADO (`c4d918f`)

- **Contrato §4 (`:57-60`):** el flujo es igual al reparto «solo si el patrimonio cambia únicamente por beneficio y reparto». Variante: 1025, 75 frente a 50, diferencia 25 = −OCI.
- **Contrato §3 (`:45-47`):** 9,434 % (cierre) frente a 10,000 % (apertura), como convención del producto y propuesta pendiente de decisión. Coincide con U3 §3, §6 y §7.2.
- **Salida de `verificar_contrato_c.py`:** tal cual, idéntica a la evidencia `r5_r8` (sin contar las líneas vacías).

### R9 · comandos de ENTREGA — CERRADO CON LÍMITES (`52eca91`)

- **Lo que pasa tal cual:**
  - `ENTREGA_B_PM1`: prueba 0 (29/29), prueba 1 (`tablas_vidrala`, `cmp` idéntico) y prueba 2 (extractor, `cmp` idéntico);
  - `ENTREGA_B3_C1`: prueba 0 (inventario y huellas) y prueba 1 (29/29);
  - `ENTREGA_F3`: pruebas 0–4;
  - `ENTREGA_F2`: pruebas 0–4.

  Todas dan código 0 (`sondas/sonda_entregas_tal_cual_out.txt`).
- **Lo que queda:** H5 (dos descripciones con código 2) y H6 (prueba no discriminante).

### R11 · restos de antes de F2 — CERRADO CON LÍMITES (`52eca91`)

- **Corregido:**
  - `fuentes_y_preservacion` de las dos ENTREGA, con el SHA completo y 6799 = 6798 + manifiesto;
  - `cambios_respecto_entrega_anterior`, que menciona F2 y F3;
  - `ENTREGA_B_PM1.siguiente_accion_exacta`, que ya no dice «Cola 2»;
  - `PUNTO_DE_RECUPERACION.md:31`, con 6799 y el desglose.
- **Queda:** H9.

### R12 · dos contratos y protocolos — ABIERTO (`c4d918f`)

- **Contrato: alineado.** Comparado tema a tema con U3:
  - elección del motor, palancas X14–X18, g∞, quiebra, ROE de cierre y apertura, flujo, terminal, BS, τ/f/ajuste, r, C55, puente con AT1 y «otros con nombre», excedente limpio, E62 y PD-1 a PD-6: **coinciden**, sin contradicción;
  - U3 añade cosas que F no repite, como C37/C41/V06/V22, BL, la sensibilidad y §7.3. No contradicen nada; F remite a U3.
- **Protocolo: no alineado** (H1).

### R13 · cosmético — CERRADO CON LÍMITES (`c4d918f`)

- `grep -n ibral` sobre el contrato no devuelve nada.
- Las filas B 9 y 11 vuelven a su texto de `195766f`.
- Límite: H10.

### R14 · afirmaciones de RESPUESTA_F2, ENTREGA_F2 y COMANDOS — ABIERTO (`52eca91`)

- **Corregido:**
  - `RESPUESTA_F2.md:19`: citas;
  - `RESPUESTA_F2.md:39`: «comandos tal cual», con el reenvío a F3;
  - `RESPUESTA_F2.md:3`: la rama avanzó después de `57b34a6`.
- **Queda:** H3.

### R15 · ENTREGA_F2 — ABIERTO (`52eca91`)

- **Corregido:**
  - el resultado de la prueba 2, que ahora es simplemente `EJECUTADO`, con el límite en `criterios_sin_cubrir`;
  - la prueba 3, con la ruta definida y código 0 tal cual;
  - `tareas_control`, que ahora incluye B-PM1;
  - `$ZIP_414` y `$RUTA_TEXTOS`, definidos en `COMANDOS.md:141-145`;
  - la hora final del bloque F2 en `COMANDOS.md:139`.
- **Queda:** H4, y H8 para el bloque F3.

## 2. Política económica y motor C — CONFORME

- **Ningún número de política.** Ningún archivo nuevo o cambiado fija r, g∞, ROE, probabilidades, tolerancias ni umbrales. Las cifras que aparecen son de dos tipos:
  - el ejemplo «ilustrativo, no propuesto para ningún caso» (`CONTRATO:62`);
  - las palancas de los fixtures sintéticos del producto (`:8-9`).
- **Pendiente de decisión, sin número:** la tolerancia del puente y el cambio de convención del ROE (`:47`, `:56`).
- **Motor C sin validar:**
  - estado «no ejecutada, no validada» (`CONTRATO:3-4`);
  - E62: «el motor C **NO valida la solvencia ni el capital regulatorio**» (`:88-89`);
  - `PROTOCOLO:63`: «No se declara validado un caso C por el mero hecho de que la plantilla acepte cifras».
- **ENTREGA:** `integrado_en_producto` = false; `apto_dinero_real` = «No se declara por este formulario»; ningún «APROBADO».
- **Plantilla:** las cuatro ENTREGA tienen exactamente las claves y los tipos de `PLANTILLA_ENTREGA.json` (`05bf1081…2a5`), también en cada prueba (`sondas/sonda_plantilla_out.txt`).
- **Límite:** decir «contrato U3 **de la persona responsable**» puede leerse como una adopción que no existe (H2).

## 3. Manifiesto y rutas — CONFORME

- `sha256sum -c MANIFIESTO_SHA256.txt` en `<rev_F3>/wt` da código 0.
- 53 entradas = 53 archivos; la lista coincide con la carpeta.
- Ninguna ruta absoluta ni local en el manifiesto (`sondas/sonda_manifiesto_out.txt`).
- `git diff --name-only 98bdf8f c504830`: 22 rutas, todas bajo `resultados_cierre/alcance_real/`.
- Ningún binario en `--numstat` y ningún patrón de secreto en las líneas añadidas.
- `/workspace` solo aparece como texto («ningún `/workspace` fijo»).
- `/tmp/...` aparece en comandos de ENTREGA como directorio de trabajo, no como ruta del autor.

## Contexto nuevo: ¿da el contrato «alineado con U3» de `c4d918f` por elegido a FinecoBank?

**No.**
- El contrato (`:104-105`) y el protocolo (`:40-43`) dicen expresamente que F no nombra candidatas y que la elección es de la persona responsable sobre U3.
- FinecoBank solo aparece como ejemplo de la lista de U3 «con descargas bloqueadas por permisos».
- `SELECCION.csv` no nombra ninguna entidad financiera.
- Nada en el contrato depende de las cifras ni del perímetro de Fineco.

**Lo que asume y ya no vale** (todo es posterior a `c504830`, 13:18:19Z):
1. **Que las descargas de Fineco están denegadas** (`CONTRATO:102-103`; `PROTOCOLO:42-43`; `ENTREGA_F3.json:79,91`; `RESPUESTA_F3.md:53`). La persona responsable autorizó U3 (`72c49e5`, 13:25:07Z). Fineco se descargó con SHA-256, se verificó y **no encaja en la letra del protocolo C**: falla C4 y C3 es dudoso (`VERIFICACION_FINECO.md` §10; `472a08e`/`cefc77f`). Ya hay un segundo intento de selección en curso (`a79e62d`, 13:51:05Z).
2. **Que la lista vigente de U3 es «Fineco/Hannover»** (`PROTOCOLO:42`). Fineco queda descartado tal como está escrito el protocolo, y U3 reaplica el protocolo para otro candidato.
3. **Que el contrato U3 es «de la persona responsable»** (`CONTRATO:3-4`). Es una propuesta del coordinador sobre el encargo U3, y la decisión U3 dice: «La autorización no valida el motor C ni adopta política económica».
4. **Que el protocolo propio de F es inocuo** (H1). Con los datos de hoy, sus criterios 1–3 admitirían a Fineco, que U3 rechaza. Es la prueba concreta de que siguen existiendo dos protocolos.
5. **Que Ahold no tiene Excel de etapa 1 («insumo no entregado»)** (`SELECCION.csv:2`; `PUNTO:57`; hueco del inventario). La persona responsable aportó `Ahold_evaluada.xlsx` y `Ahold_respuesta.md` (`3b07d89`, 13:28:16Z), conservados en `fuentes/ahold-etapa1-20261117`. El inventario del ZIP sigue siendo correcto: esos archivos no están en el ZIP. Lo desfasado es la frase de bloqueo.

**Lo que sigue valiendo:**
- la descripción del motor, que no depende de la entidad;
- las PD-1 a PD-6 sin números.

La verificación de Fineco confirma que hacen falta, sin resolverlas: AT1 dentro del patrimonio atribuible (PD-3), «changes in reserves» con nombre en el puente, OCI de −12 319 en 2024 y años sin dividendo (excedente limpio).

## Lo conforme

- Inventario reproducible byte a byte con `.bat` y alcance negativo, comprobado de forma independiente.
- Contrato C fiel al motor en todo lo que R5–R8 pedía, sin contradicciones con U3.
- Citas del contrato, el protocolo y el MAPA verificadas una a una.
- Cuatro ENTREGA conformes con la plantilla.
- Los tres comandos señalados por R9 se ejecutan tal cual y el resultado es correcto, comprobado con un control propio.
- Sin política económica, sin validación del motor C, sin autoaprobación.
- Se mantiene, sin cambios en esta entrega:
  - 71 PDF con huella: `cmp` de `huellas_todas_las_fuentes.csv`, código 0;
  - puente 1060/1170;
  - X14/X15/X16/X18/B68;
  - ROE de cierre;
  - 29/29 de `daa7478`.

## Límites de esta revisión

- **Independencia:** soy Claude, como el coordinador, que es autor de U3 y de `VERIFICACION_FINECO.md` (por un subagente). La comparación de F con U3 la hace, por tanto, la misma familia que escribió U3.
- **Sin recálculo de la hoja:** no recalculé con LibreOffice ningún fixture. Las fórmulas las leo de `referencia_V6.3.json` y del código, y replico la aritmética en Python.
- **Lo que no verifiqué:** los datos de `VERIFICACION_FINECO.md`, que tomo como hecho registrado por el coordinador. Tampoco abrí los originales de Ahold de U2.
- **Pruebas descriptivas:** las pruebas 2 de `B3_C1` y 3 de `B_PM1` no se pueden ejecutar tal cual. No intenté su intención con `gh api`: sin red.
- **Directorios temporales:** `sondas/tmp_ns1/` y `sondas/tmp_ns2/` son el `/tmp` de las ejecuciones. Contienen textos extraídos del ZIP y un `git archive` de `daa7478`, y **no deben versionarse**. Hay que borrar `sondas/tmp_ns/` (un archivo de prueba vacío).
- **Worktree:** `<rev_F3>/wt` queda registrado en `<repo>` (`git worktree list`). Se puede quitar con `git worktree remove <rev_F3>/wt`.

## Comandos principales

```bash
git -C <repo> fetch origin mistral/f-alcance-real coordinacion/cierre-v2
git -C <repo> worktree add --detach <rev_F3>/wt c504830
sha256sum <zip>
unshare -m bash -c 'mount --bind <rev_F3>/sondas/tmp_ns1 /tmp && python3 -I <rev_F3>/sondas/sonda_entregas_tal_cual.py <rev_F3>/wt <zip> <rev_F3>/sondas/entregas_tal_cual'
bash sondas/sonda_r3_r4_alcance.sh <zip> <rev_F3>/wt/…/INVENTARIO_Y_HUECOS.csv
python3 -I sondas/sonda_citas.py <rev_F3>/wt/resultados_cierre/alcance_real <candidata>/munger_v2_r1
python3 -I sondas/sonda_r5_r7_ref.py <candidata>/munger_v2_r1/v6/referencia/referencia_V6.3.json
unshare -m bash -c 'mount --bind <rev_F3>/sondas/tmp_ns2 /tmp && cd <rev_F3>/wt && ZIP_414=<zip> bash <rev_F3>/sondas/sonda_r9_control_tablas.sh'
(cd <rev_F3>/wt/resultados_cierre/alcance_real && sha256sum -c --quiet MANIFIESTO_SHA256.txt)
```

## Huellas del material revisado (@ `c504830`)

| SHA-256 | Archivo |
|---|---|
| `c7a1f520bc72338611ddc4f322c4115e2fa5d550b4a86263dbb38afc654924eb` | `MANIFIESTO_SHA256.txt` |
| `c58f728c7ac5d39f3850dacfa19107db1a23147993875e22fbd6f04d37404c89` | `correccion_f3/ENTREGA_F3.json` |
| `6147274c252db55f66192a6bb01c81b518ea7ad41ae1566dcc4677b5f7e5a47b` | `correccion_f3/RESPUESTA_F3.md` |
| `db12bca49c2438bc293562efd4a4e6523987bdc3ca87c45763d468f0d4469177` | `preparacion_b3_c1/CONTRATO_C_PROPUESTA.md` |
| `27194caf4e2e02c48b7607dd75197f28917bace62e24f26cea8c6fdedbf333b4` | `preparacion_b3_c1/PROTOCOLO_CONGELADO.md` |
| `e30f587415add16080237abb4a2dc5e10538b143a55bc8adf66ecff497e62375` | `preparacion_b3_c1/MAPA_ENTRADAS.jsonl` |
| `66b1684f8f70ed36912f95f54ccd609ad1a3fef0759868d9fcd67b4093719428` | `preparacion_b3_c1/INVENTARIO_Y_HUECOS.csv` |
| `0d0400cf3789bdbf6708f166d8ee0b87952a89c4b3d7b9c1c328e4c90c9e1f94` | `preparacion_b3_c1/scripts/inventario_desde_zip.py` |
| `336fb6db0630494bf9bc1625dce8aa0c17b29cd6996b6cd1bab22d7ddd76bc13` | `preparacion_b3_c1/ENTREGA_B3_C1.json` |
| `7cad19fbcaf66d7721d0f759473826f7d90fc48b56328e0a37c715636539bdad` | `revisiones_b_pm1/ENTREGA_B_PM1.json` |
| `833e518e8de11abb8a01fa1528efcb421ab07f9157d6417459af12b951f10ad4` | `correccion_f2/ENTREGA_F2.json` |
| `3cf4bf2f22be557b3ee69c065548afe5bdcde685223fac8cf12f4e6656c47431` | `correccion_f2/RESPUESTA_F2.md` |
| `0a8e56f6eacd1f0c5820cce2dc27056f37a37dc95793b603e07439338a637b54` | `correccion_f2/scripts/verificar_contrato_c.py` |
| `911583e87fb5a0dff40713dbe43b98f810818803d982ed36a58d94c46692a54f` | `COMANDOS.md` |
| `d251585cd8e9b0db670a028f0d3380e4f6b01cb33dc7532896101d9ed572bf4d` | `PUNTO_DE_RECUPERACION.md` |
| `bb51942cefb848e409a4828e3faeb70f94aa4d29af39cda6d90cd0a97cb7b93e` | `<zip>` |
| `500c8d3a28b3775e1b5307d712380ed49346726c5d5b153502cd40ae5b133146` | `<candidata>/…/V6.1/build_v6.py` |
| `bd9e58500b9d5e495a8d5a5e2471e3f11442730460dcaf3eb49321538b49feac` | `<candidata>/…/V6.1/test_fill.py` |
| `677c6cfa06c75eb48aa25449479d2dc0ea55660e2b478f8fcc71bb4659d37c2a` | `CORRECCION_F3.md` |
| `cc9efb212e98c172bf60e0f24dc7b656bd3fd0d8f21ca2af32ab6a7926bf2ad7` | `u3_motor_c/CONTRATO_C_DESDE_EL_MOTOR.md` |
| `3e28d9c0456a9a3197e9a9430e988cde5cbde06b8cfa79e1608f52f836317855` | `u3_motor_c/PROTOCOLO_SELECCION_C.md` |
| `245a2e6bd226350183fa3611412205b37941fdde2583d9eb517a46be2f7b6839` | `u3_motor_c/verificacion_fineco_20261117/VERIFICACION_FINECO.md` |

**Sondas:** las huellas están en `sondas/SHA256SUMS.txt`.

*Revisión independiente con límites declarados. No es una aprobación ni acredita aptitud económica. La aceptación la registra el coordinador.*
