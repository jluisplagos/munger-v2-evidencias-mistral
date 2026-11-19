# Revisión independiente · `f1/usgaap-replica` (margen de partida de la capa F1 según Palancas C8)

- **Rama revisada:** `f1/usgaap-replica` @ `5a525e0`. Commits: `7bf8bd2` (código y pruebas), `5f52734` (manifiesto), `8652620` (registro en `F1_IMPL.md` §11, guion de mutaciones y resultados) y `5a525e0` (manifiesto, 9416 archivos).
- **Base real: `15c4ccf`, no `c0bbf5c`.** `git diff c0bbf5c..5a525e0` (137 archivos) arrastra, invertidos, los tres commits de `examen/expedientes-f1` que la rama no tiene: `cdf1b6f` y `909d279` (sellado de los registros de `jumbo_e` y `ahold_f3`) y `c0bbf5c` (expediente `jumbo_f`). Esas «eliminaciones» no son del autor. El cambio del autor es `git diff 15c4ccf..5a525e0`: 11 archivos, `motor_a_f1.py`, dos baterías, `probar_libro_v631_usgaap.py`, `verificar_paquete.sh`, `F1_IMPL.md`, `F1_USGAAP.md`, el guion de mutaciones, dos archivos de resultados y el manifiesto. Eso es lo que reviso.
- **Revisor:** agente Claude distinto del autor (Opus 5.5), 19-nov-2026. No toqué la rama del autor ni los expedientes. No leí la rúbrica ni `contradictor/`.
- **Copias (en `/dev/shm`, borradas al terminar):**
  - `nuevo`: árbol de `5a525e0` con los binarios del árbol del autor.
  - `viejo`: los 11 archivos de `15c4ccf`.
  - `mixto`: `5a525e0` con el `motor_a_f1.py` de `15c4ccf`, para correr las pruebas nuevas contra la capa vieja.
  - `limpio`: `5a525e0` con los 106 binarios del manifiesto que faltan en el árbol del autor. Los copié de `wt_expedientes` solo cuando su huella coincidía (106 de 106).
  - Expedientes: `zoetis_t1c`, `ahold_f3`, `jumbo_e`, `jumbo_f`, `ahold_f2` y `zoetis_t1b` (de `wt_expedientes`) y `elis_f1` (de `wt_examen`).
- **LibreOffice:** siempre con `flock /home/user/e_work/libreoffice.lock`, una ejecución cada vez.
- **Evidencia:** `evidencia/`. Contiene las salidas de las baterías, las mutaciones, la comparación de las dos capas sobre los expedientes, las variantes de C8 del libro de Zoetis y los guiones usados.
- Experimental supervisado. **No es apto para dinero real.** Esta revisión no acredita aptitud económica.

## Veredicto: **CONFORME CON CORRECCIONES**

Las correcciones son de integración y de una etiqueta informativa. El código es correcto y no debilita ninguna guarda.

El diagnóstico es correcto. La plantilla calcula `Diagnóstico V6!C10 = IF(Palancas!C8="Media del ciclo"; Historia!C49; Historia!C48)`, y el Motor parte de C10 (`D6:D8`). La capa tomaba siempre C48. La corrección hace que la capa use el m0 del libro. Además, la réplica contrasta ese m0 con C10 y con D6:D8, también en el paso 7, sin flujos. Con eso las guardas quedan más estrictas o iguales, nunca más laxas. Ninguna otra palanca del libro entra en el motor A sin que la capa la lea o la contraste.

En NIIF (`ahold_f3`, `jumbo_e`, `jumbo_f`, `ahold_f2`, `elis_f1` y la regresión de Elis) no cambia ninguna cifra, ninguna guarda ni ningún código de salida. En `zoetis_t1c`, la réplica y `F1-LIBRO` quedan conformes y la conclusión pasa a «utilizable CONDICIONADA (D-US1)». El flujo sin crecimiento es 2.484,631, que es exactamente el del Motor del libro (`BL7 × r`). La cota de D-US1 queda en −2,6 % / +2,6 %. Las fases A, B y C no usaron ninguna cifra de la capa antigua, así que basta con repetir el paso 12.

**Correcciones:**

- **C1 · Integración (obligatoria antes de fusionar).** La rama no está sobre `c0bbf5c` ni sobre el `examen/expedientes-f1` actual (`origin` @ `a9c42b9`, que ya trae `producto/redondeo-exacto`). `git merge-tree` da conflicto solo en `MANIFIESTO_SHA256.txt`; `verificar_paquete.sh` se fusiona solo y conserva los umbrales 176/294/18 y la batería nueva del redondeo. Después de fusionar hay que hacer dos cosas:
  - regenerar el manifiesto en su propio commit;
  - repetir sobre el resultado `verificar_paquete.sh rapida`, `test_motor_a_f1.py`, `test_motor_a_f1_usgaap.py` y `probar_libro_v631_usgaap.py` (este con LibreOffice).
- **C2 · Etiqueta de P-FOSO (recomendada; no bloquea esta integración).** `perimetro_f1.desde_libro` y `desde_datos` toman C48 («margen_ultimo») como «margen de partida» del ROIC terminal neutro. Ese texto va en `datos_v63.md`, que leen las fases B y C. Con «Media del ciclo» mostraría un margen que no es el m0 del libro. Hoy no afecta a nadie: con US GAAP no se calcula, y todos los libros NIIF del motor A en curso tienen «Último año» (`evidencia/c8_libros_examen.txt`). El autor lo deja escrito como límite en §11. Conviene corregirlo, usando C10 o C48/C49 según C8, antes de que un expediente NIIF con A2 elija «Media del ciclo».
- **C3 · Hueco de prueba (opcional).** Ninguna batería sin LibreOffice comprueba que `leer_libro` lea `Palancas!C8`. Las sintéticas construyen el diccionario a mano. Si se quita la lectura (mutación r13), las baterías sintéticas no lo detectan; solo lo detecta la prueba L8 con LibreOffice, que va en el modo «completa». No es un riesgo, porque sin C8 la capa toma C48, el contraste con C10 y D6:D8 bloquea y el sistema falla cerrado. Aun así, una prueba barata de `leer_libro` lo cubriría en el modo rápido.

## 1. ¿Es correcto el diagnóstico?

Sí. Lo comprobé en una copia del libro evaluado (`Zoetis_v63_evaluada.xlsx`, `7cb988d0…`; recálculo `532504ee…`). Las fórmulas y valores están en `evidencia/zoetis_t1c/formulas_motor_a.txt`.

**Qué hace el libro con C8:**

- `Palancas!C8` tiene validación de lista `Lista_Base` = `Opciones!M3:M4` = {«Último año», «Media del ciclo»} y admite vacío. Fase A escribió «Media del ciclo».
- `Diagnóstico V6!C10 = IF(Palancas!$C8="Media del ciclo";Historia!$C$49;Historia!$C$48)`. Con el motor A, `Motor!D6:D8 = IF(C5="C"; C14; C10)`.
- `Historia!C48 = L29` (último año).
- `Historia!C49 = IF(AND(COUNT(C29:L29)>0; COUNT(C29:L29)=C43); AVERAGE(C29:L29); "")`. Es la media de EBIT ÷ ventas de todos los años con ventas, y queda vacía si a alguno le falta el margen.
- `margen_de_partida()` reproduce exactamente esa regla, incluido el vacío (ventas cero o EBIT vacío → `None`). La media exacta difiere de C49 en 1,8·10⁻¹⁶.

| Valor de C8 | Celda que usa la plantilla | Comprobado con LibreOffice sobre el libro de Zoetis |
|---|---|---|
| «Media del ciclo» | C49 | C10 = D6 = 0,340556331 |
| «Último año» | C48 | C10 = 0,378366959 |
| vacío | C48 | C10 = 0,378366959 |
| «media del ciclo» (minúsculas; fuera de la lista) | C49: LibreOffice compara sin distinguir mayúsculas | C10 = 0,340556331 |
| «Media del ciclo» con un año sin EBIT | C49 vacía → C10 y D6 vacías → el Motor no calcula (`BS6` FALSO) | C10 vacía |

**La misma fórmula está en todas las plantillas** (V6.1, V6.2, V6.3, V6.3.1 F1). La excepción son las V6.4 y V6.4.1 experimentales, que anteponen `Configuración V6.4!B21` cuando `B76` es verdadero (`evidencia/plantillas_c10_c8.txt`). En ese caso la capa no seguiría a B21, pero el contraste con C10 la hace bloquear. Hoy no se llega ahí: la V6.4 solo cubre el motor B y el paso 7 para antes al motor A.

**Cuenta del bloqueo en Zoetis (MALO, año 1).**

| Capa | m0 | m₁ | AU6 |
|---|---|---|---|
| Libro (Motor) | C49 = 0,340556 | 0,336445 | 2.453,483 |
| Capa vieja (réplica) | C48 = 0,378367 | 0,366694 | 2.682,659 |

La diferencia es 229,18 = 9.467 × 0,8003 × (C48 − C49) × 4/5. Se reduce a cero en el año 5, cuando el margen llega a m_obj. En el paso 7 no había flujos y la réplica vieja no contrastaba m0, así que no lo vio. Lo reproduje con una variante «paso 7», sin palancas ni g: la capa vieja da 2.771,10 sin bloquear; la nueva da 2.484,63 y contrasta m0 con C10 y D6:D8, que existen aunque no haya palancas (`evidencia/variantes_c8_zoetis.txt`).

**¿Hay otras palancas que la capa ignore del mismo modo?** No. Repasé todas las entradas de las filas 6–8 del Motor con el motor A:

| Entrada del Motor | De dónde sale | Cómo la usa la capa |
|---|---|---|
| L0 (C) | C9 = Historia C44 | la lee |
| m0 (D) | C10 | **corregido**: la elige por C8 y la contrasta con C10 y D6:D8 |
| g años 1–5 (E), m objetivo (F), S2C (G), ROIC largo (I) | Palancas B14:D16 y B18:D18 | las lee |
| g para siempre (H) | Análisis B68:D68 + 0,0 | la lee; un desplazamiento distinto de 0 lo detectaría la comparación de flujos |
| τ (K) | C11 = C52 | la contrasta |
| f (L) | C12 = C58 | la contrasta |
| ajuste (M), quiebra (N, O) y acciones (P) | — | no entran en los flujos AU:BD ni BF; la capa no calcula el valor |
| tasa (J) | Análisis C56 | la misma que usa la cota en valor presente |

El horizonte también coincide en los dos lados: 10 años, convergencia del margen en 5 años, desvanecimiento de g entre los años 6 y 10, y un año 11 con m_obj y g∞/ROIC. Está fijo en la plantilla y en `motor()`.

Las demás palancas de Palancas no entran en la fila 6–8 o la capa ya las cubre:

- C5, C6, C7 y C9/C10 (I+D capitalizada) solo cambian anclas o diagnósticos. C9/C10 afectan a C55, C67 y P-FOSO, no al Motor.
- C43/C44 (FCF normalizado) entran por Historia C70, que la capa lee.
- La fila 9 del Motor (estudio del Panel) queda fuera de la réplica.

## 2. ¿La corrección es completa y no debilita ninguna guarda?

**Lo que cambia en las guardas** (todo en `motor_a_f1.py`):

- **Contraste de m0.** Antes se contrastaba solo con C48, solo si C48 tenía valor y solo cuando había réplica. Ahora `_replica_m0` lo contrasta siempre: con la celda que elige C8 (vacía es diferencia), con C10 y con D6:D8, a 10⁻¹². **Más estricto.**
- **Valor de C8 fuera de la lista.** `F1-REPLICA` bloquea con un mensaje explícito. **Nuevo.** Antes de la capa ya lo impiden `fase_a.esquema.json` (enum) y `comprobar_celdas_v2.py` (lista exacta), así que es una defensa más.
- **«Media del ciclo» con C49 incalculable.** La capa lanza `ErrorDeclaracion` (rc 2), y el gancho del pipeline da `no_entregable · fallo_de_implementacion`. **Nuevo.** En el pipeline lo para antes `comprobar_entrada_v63.py` del paso 7: con la variante del libro sale «motores calculables: ['C']», rc 1 y `pendiente_de_datos`.
- **K3.** La segunda partida pasa a m0 × V0 − Ē. Es una identidad: con «Último año» es exactamente la misma cifra (fracciones exactas), y con «Media del ciclo» sigue cuadrando (2.484,631 = suma de partidas).
- **V-F1f** (solo INFORMA). Calcula lo que lleva m0 de la PPA y de la ROU como media del ciclo, o da «no calculable». En Zoetis las series no cubren los diez años y sale «no calculable», que es lo honesto. Antes daba la proporción del año base, que con «Media del ciclo» no es lo que lleva m0.
- **F1-PARAM.** Con N1 y «Media del ciclo» añade una línea, pero no cambia la severidad: cualquier ajuste N1 ya hacía bloquear por el alcance sin decidir.
- **F1-LIBRO, flujos, f, τ y ancla:** sin cambio de lógica.

Lo único que deja de bloquear es el falso positivo de «Media del ciclo» con un libro coherente. Un libro que diga «Media del ciclo» y cuyo Motor parta de otro margen sigue bloqueando por C10, D6:D8 y los flujos. Las pruebas M0 lo cubren y lo confirmé en el libro real (variante en minúsculas).

**Ningún resultado «utilizable» quedó calculado con un m0 erróneo.** Revisé los 17 `motor_a_f1_resultado.json` de `wt_expedientes` y `wt_examen` (`evidencia/resultados_f1_existentes_c8.txt`). Solo `zoetis_t1c` tiene «Media del ciclo», y estaba bloqueado. Todos los demás libros dicen «Último año». Los cinco de `wt_expedientes` que no tienen el libro en su carpeta registran la misma huella de libro que su copia en `wt_examen`, donde el libro dice «Último año». Hay un caso que merece cuidado: los resultados «utilizable» con 0 flujos contrastados (los del paso 7 de `ahold_f1` y `ahold_f2`) no probaban m0 con la capa vieja. Están bien porque C8 es «Último año». Además, con «Media del ciclo» y C48 ≠ C49 la capa vieja bloqueaba siempre en el paso 12, porque los flujos de los años 1–4 difieren. Por eso no importa que `vigencia()` no mire la versión de la capa.

**Comparación de las dos capas sobre copias de los expedientes** (`evidencia/comparacion_capas_expedientes.txt`; se ignoran `version`, `fecha` y la ruta de la declaración):

| Expediente | C8 | Capa vieja → nueva | Diferencias |
|---|---|---|---|
| `zoetis_t1c` (US GAAP, A2) | Media del ciclo | rc 5, bloquean `F1-REPLICA` y `F1-LIBRO` → rc 0, CONDICIONADA | m0, F0, K3, cotas en %, V-F1f y réplica: 136 valores |
| `ahold_f3` (NIIF) | Último año | rc 0 → rc 0, utilizable | solo 6 campos informativos nuevos (base, celda y m0) y el texto de `F1-REPLICA` |
| `jumbo_e` (NIIF) | Último año | rc 0 → rc 0, utilizable | ídem |
| `jumbo_f` (libro heredado de `jumbo_e`) | Último año | rc 3 (`F1-K3a`) → rc 3 | ídem |
| `elis_f1` (`wt_examen`) | Último año | rc 3 → rc 3, las mismas 9 guardas | ídem |
| `ahold_f2` | Último año | rc 0 → rc 0 | ídem |
| `zoetis_t1b` (motor B, puente) | Último año | rc 3 → rc 3 | ninguna |
| Regresión de Elis (`regresion_elis_f1.py`) | Último año | 39/39 → 39/39 | en las tres declaraciones, solo los 6 campos y el texto |

**Observación operativa sobre `ahold_f3` y `jumbo_e`** (esperan la auditoría del paso 13): **no hay que repetir nada.** Si se repitiera el paso 12 solo por esto, cambiaría `motor_a_f1_resultado.json` (versión, fecha, campos nuevos y texto), que forma parte de `MATERIAL_FIJO`. Con eso cambiaría el material sometido a la auditoría y habría que pedirla de nuevo.

**Sobre `jumbo_f`:** sigue en el paso 6, esperando la fase A, que es la que elegirá C8. Conviene integrar la corrección antes de que llegue al paso 7. Si elige «Media del ciclo» con la capa vieja, el paso 7 daría un flujo sin crecimiento erróneo sin avisar y el paso 12 bloquearía.

## 3. Pruebas

Las repetí todas. Las de LibreOffice, una cada vez con `flock`. Salidas en `evidencia/baterias/`.

| Batería | Capa vieja con las pruebas nuevas (`mixto`) | Capa nueva |
|---|---|---|
| `test_motor_a_f1.py` | **165/176**: fallan las 11 M0 que no son controles de «Último año» | **176/176** (con las pruebas de `15c4ccf`, la capa vieja da 163/163) |
| `test_motor_a_f1_usgaap.py` | **290/294**: fallan las 4 M0 | **294/294** |
| `probar_libro_v631_usgaap.py` (LibreOffice) | **17/18**: falla L8, bloquean `F1-REPLICA` y `F1-LIBRO`, m0 0,2 = C48 | **18/18** |
| `prueba_pipeline_f1.py` (gancho, LibreOffice) | — | 8/8 |
| `prueba_pipeline_usgaap.py` (LibreOffice) | — | 26/26 |
| `probar_v631_f1.py` estructura / a0 / f1 (a0 y f1 con LibreOffice) | — | 21/21 · 22/22 · 35/35 |
| `prueba_pipeline_v631.py` (LibreOffice) | — | 9/9 |
| `test_v631_f1.py` | — | 29/29 |
| `test_perimetro_foso.py`, `test_f1_series_escala.py`, `test_comprobadores.py` (dentro de `verificar_paquete.sh rapida`) | — | 66/66 · 80/80 · 114/114 |
| `regresion_elis_f1.py` | 39/39 | 39/39 |

**Mutaciones.**

- **`mutaciones_margen_de_partida.py`.** Sus 12 mutaciones tocan cada pieza nueva: la lectura de C8, cada contraste, la tolerancia, el vacío, la parada, la media sobre todos los años, K3, V-F1f, F1-PARAM y N1. Las repetí con un guion propio (`evidencia/scripts/mutaciones_revisor.py`; salida en `evidencia/mutaciones/mut_revisor.txt`). Mi guion detecta por recuento: cuántas pruebas pasan, el total y si la batería se interrumpe. El del autor usa como clave los primeros 152 caracteres de la línea, nombre y detalle juntos, y un cambio de detalle podría contar como «deja de pasar». Resultado: **12 de 12 detectadas.** z08 se detecta porque la batería se interrumpe (TypeError), no por una aserción. El efecto es el mismo: fallo cerrado.
- **Cuatro mutaciones mías.** Detectadas por las sintéticas:
  - r18: la media con los años disponibles;
  - r22: contrastar siempre con C48;
  - r23: no contrastar C10.
  
  **No** detectada por las sintéticas:
  - r13: no leer C8.
  
  r13 sí la detecta L8 con LibreOffice (17/18, bloquean `F1-REPLICA` y `F1-LIBRO`). Ver C3.
- **`mutaciones_usgaap.py`:** 112 de 112 detectadas en `5a525e0`. Sus patrones siguen aplicando una vez.

## 4. Manifiesto y registro frente a `verificar_paquete.sh`

- **Manifiesto de `5a525e0`:** 9416 archivos; en la copia limpia, 0 modificados, 0 ausentes y 0 de más. `bash verificar_paquete.sh rapida` da **RESULTADO GLOBAL: PASA** (`evidencia/baterias/verif_rapida_5a525e0.txt`). Para que pasara tuve que quitar el perfil `personaje_v2/.lo_perfil/`, que está ignorado en el árbol del autor, y añadir los 106 binarios con su huella. El autor solo dejó la verificación sobre `5f52734` (9413); la de `5a525e0` es esta.
- **Umbrales:** `verificar_paquete.sh` exige al menos 176, 294 y 18, que son exactamente los recuentos actuales. Los comentarios conservan los anteriores (142, 290 y 16).
- **Registro:** comprobé todas las cifras de `F1_IMPL.md` §11 y de `resultados/margen_de_partida_5f52734.txt`:
  - la cuenta de AU6;
  - 165/176, 290/294 y 17/18;
  - 12/12 y 112/112;
  - el resultado de Zoetis: 2.484,631 frente a 2.771,101 y −2,6 % / +2,6 % frente a −2,3 % / +2,3 %;
  - que `ahold_f3` y `jumbo_e` tienen «Último año».
  
  «F1-SERIES-CERO (PENDIENTE)» es el efecto de esa guarda; su severidad es AVISO. `F1_USGAAP.md` §7 cita L8 correctamente. La única imprecisión está en el encargo de la revisión, no en el registro: el encargo decía «sobre c0bbf5c», y el registro dice bien `15c4ccf` (ver C1).

## 5. Efecto económico en `zoetis_t1c` y qué hay que repetir

**¿Es razonable que el flujo sin crecimiento baje de 2.771,1 a 2.484,6?**

**Mecánicamente, sí.** 2.484,631 es el flujo sin crecimiento del propio libro: `(BL7 − M7) × J7 = 2.484,631379`. El libro valora con C49 desde que la fase A eligió «Media del ciclo». El 2.771,1 era la cifra de la capa, incoherente con el libro. La diferencia es −286,47 (−10,3 %) = V0 × (1 − τ) × (C48 − C49) = 9.467 × 0,8003 × 3,78 pp. El valor del libro y `precio.json` no cambian con esta corrección.

Por la misma razón, el diagnóstico por perímetro baja 286,47 en todos (A0 2.337,42, A1 2.338,46, A2 2.484,63, B 2.152,36) y la diferencia A2 − A0 no cambia. La cota de D-US1 en mm sigue siendo la misma (−64,23 / +63,54): solo cambia su porcentaje, porque cambia el divisor.

**Económicamente, es la consecuencia de una decisión de juicio de la fase A, no del cambio.** La fase A justificó «Media del ciclo» así: 2025 (37,8 %) es el máximo de la serie y lo ayudaron la venta de MFA y menos cargos de inventario, y la guía de 2026 sube el coste de ventas a ≈29 % frente a 28,2 %. Pero la propia fase A reconoce que «no es cíclica» y que «la media de diez años puede quedarse corta». Dejo los datos para quien juzgue, sin proponer una política:

- La media de 34,06 % incluye el 28,5 % de 2016.
- En el NORMAL, el margen del año 1 es 34,24 %: un escalón de −3,6 pp frente al 37,84 % de 2025. En el MALO es −4,2 pp y en el BUENO −3,1 pp.
- La guía citada explica del orden de 0,8 pp de margen bruto, no los 3,8 pp que separan C48 de C49.
- Cada punto de m0 mueve el flujo sin crecimiento ≈ 75,8 mm (≈ 3 %). Es más que toda la cota de D-US1 (±64 mm).

**¿Usaron las fases A, B o C alguna cifra de la capa antigua? No.** Las entradas de cada fase salen de `pipeline.py`:

- **Fase A** (paso 6; lee `datos_v63.md`, los extractos y el personaje): se ejecuta **antes** de la primera evaluación F1, que es en el paso 7.
- **Fase B** (paso 8; lee `fase_a.json`, `datos_v63.md`, `referencias_mecanicas.json`, `extracto_v63.md` y `gramatica.md`):
  - `datos_v63.md` se regenera en el paso 7 después de F1. Solo lleva la declaración F1 y el bloque P-FOSO «NO APLICABLES» (US GAAP).
  - Lo único que podría heredar de `motor_a_f1_resultado.json` son las anclas de S2C (`anclas_capa`). No dependen de m0 y con US GAAP no se muestran.
  - `referencias_mecanicas.json` toma m0 del libro según C8: 0,340556 = C49, base «Media del ciclo».
- **Fase C** (paso 10; lee `fase_a/b.json`, `resultados.json`, `precio.json`, `gramatica.md`, `datos_ausentes.json`, `datos_v63.md` y los extractos):
  - `resultados.json` y `precio.json` salen de `leer_resultados.py` y `precio_de_si.py` sobre el libro recalculado. No leen la capa.
  - Ninguna fase lee `motor_a_f1_resultado.*`.
- **Búsqueda de cifras de la capa:** no encontré ni 2.771, ni ±2,3 %, ni D-US1, ni `F1-REPLICA` en esas entradas, en `fase_a/b/c.json/.md`, en `celdas_*.json` ni en los encargos de `prompts_generados/`.

**Qué hay que repetir: basta con el paso 12** (`pipeline.py --desde 12`, con la capa corregida ya integrada). No hay que repetir ninguna fase. El paso 12 hace esto:

1. recalcula el libro;
2. pasa `verificar_todo.sh`;
3. vuelve a evaluar F1: según la evaluación hecha en copia, saldrá «utilizable CONDICIONADA (D-US1)» y no bloqueará nada;
4. registra la verificación de las entradas.

Después, el paso 13 regenera `ficha_provisional.json` e `informe_provisional.md` **antes** de fijar el material. Eso importa, porque las versiones actuales (del paso 11) llevan el F1 del paso 7, con la capa vieja: cota de −2,3 % / +2,3 % y «evaluación no vigente». La `ficha.json` y el `informe.md` del cierre en `no_entregable` quedan como antecedente. Si la coordinación prefiere hacerlo en un expediente nuevo, por la norma de expedientes nuevos, tampoco cambia ninguna entrada ni salida de A, B o C.

## Otras observaciones (sin efecto en el veredicto)

- **Mayúsculas en C8.** LibreOffice trata «media del ciclo» como «Media del ciclo». La capa no lo interpreta y bloquea, que es conservador. El caso no llega a la capa porque el esquema y `comprobar_celdas_v2.py` exigen el texto exacto.
- **Parada con C49 incalculable.** `ErrorDeclaracion` da rc 2, y el gancho lo clasifica como fallo de implementación, igual que «f no calculada». Como en el pipeline `comprobar_entrada_v63.py` lo convierte antes en `pendiente_de_datos`, la clasificación del gancho no llega a usarse.

## Ronda 2 · correcciones C2 y C3 (`6f5f26a`) e integración (`7d9ab04`, `b62c284`, `a0ae904`, `6c0e678`)

- **Revisor:** el mismo agente de la ronda 1 (Opus 5.5), distinto del autor, 19-nov-2026. No toqué la rama del autor ni los expedientes.
- **Copia:** `git archive 6c0e678` con los 1059 binarios del manifiesto, copiados de `wt_expedientes` solo cuando su huella coincidía. Estaba en `/dev/shm`; la borré al terminar.
- **LibreOffice:** con `flock`, una ejecución cada vez.
- **Evidencia:** `evidencia/ronda2/`.

### Veredicto de la ronda 2: **CONFORME**

C1, C2 y C3 quedan resueltas. La integración solo toca, de los expedientes, `zoetis_t1c`, y su paso 12 da exactamente lo anticipado.

**C2 · P-FOSO.** `perimetro_f1.margen_de_partida(base, c48, c49)` aplica la regla de la plantilla:

| Palancas C8 | Margen de partida |
|---|---|
| vacía o «Último año» | C48 |
| «Media del ciclo» | C49; si C49 está vacía, ninguno (no cae en C48) |
| cualquier otro valor | ninguno, y el texto lo dice |

`desde_libro` lee `Palancas!C8` del libro. `desde_datos` la lee del volcado (`leer_v63.palancas` trae `C8`). El bloque guarda `m0`, `m0_celda` y `base_del_margen` en lugar de `C48_m0`. Ningún otro código leía `C48_m0` (`git grep`), y `_rotulo_m0` sigue entendiendo un bloque antiguo. Es informativo: ninguna guarda usa `roic_neutro_con_m0`. Con «Último año» la cifra no cambia.

- `test_perimetro_foso.py` da **72/72**. Con el `perimetro_f1.py` de `5a525e0` da **66/72**: fallan las 6 M0.
- Seis mutaciones mías del cambio, **6 de 6 detectadas** (`evidencia/ronda2/mut_pfoso_revisor.txt`):
  - «Media del ciclo» toma C48;
  - un valor fuera de la lista se toma como «Último año»;
  - `desde_datos` sin C8;
  - `desde_libro` sin C8;
  - el texto rotula siempre C48;
  - con C49 vacía cae en C48.

**C3 · `leer_libro` lee C8 sin LibreOffice.** La prueba nueva escribe en un `.xlsx` el libro sintético «Media del ciclo», lo lee con `leer_libro` y comprueba que la capa da lo mismo que con el diccionario.

- `test_motor_a_f1.py` da **177/177**.
- Con `leer_libro` sin la lectura de C8 da **176/177**, y la que falla es justo esa prueba.
- El guion de mutaciones del autor ahora detecta por recuento y añade z13 (no leer C8): **13 de 13** en la copia integrada.

**C1 · integración.**

- `7d9ab04` es un `merge --no-ff` de `6f5f26a` sobre `a9c42b9`. Los 12 archivos del cambio son idénticos a `6f5f26a`. `verificar_paquete.sh` es el de `6f5f26a` más la batería del redondeo exacto, que viene del otro lado; no hay ninguna otra diferencia.
- Los dos manifiestos dan 0 modificados, 0 ausentes y 0 de más en copia limpia: `b62c284` con 9542 archivos y `6c0e678` con 9547.
- `verificar_paquete.sh rapida` sobre `6c0e678` da **RESULTADO GLOBAL: PASA** (P-FOSO 72/72, F1-SERIES 80/80, redondeo 44/44, comprobadores 114/114).
- Sobre la copia integrada:

  | Batería | Resultado |
  |---|---|
  | `test_motor_a_f1.py` | 177/177 |
  | `test_motor_a_f1_usgaap.py` | 294/294 |
  | `probar_libro_v631_usgaap.py` (LibreOffice) | 18/18 |
  | gancho `prueba_pipeline_f1.py` (LibreOffice) | 8/8 |

- Los umbrales del script son 177, 294, 18, 72 y 44, iguales a los recuentos.

**Expedientes.** Entre `a9c42b9` y `6c0e678` solo cambian 16 archivos de `zoetis_t1c/Zoetis`, todos en `a0ae904` (`evidencia/ronda2/integracion_archivos.txt`). El merge y los dos manifiestos no tocan ningún expediente, y `ahold_f3`, `jumbo_e` y `jumbo_f` no cambian. En `wt_expedientes` hay archivos sin seguimiento de otra sesión (`jumbo_g/` y `configuracion/cambio_jumbo_g.json`): no forman parte de la integración y no los toqué.

**Paso 12 de `zoetis_t1c` (`a0ae904`): da lo anticipado.** Su `motor_a_f1_resultado.json` es idéntico al que anticipé en la ronda 1 salvo en `libro_sha256` (`evidencia/ronda2/zoetis_paso12_frente_a_lo_anticipado.txt`). Esa diferencia es esperable: el recálculo es un archivo nuevo, y el libro de origen es el mismo (`7cb988d0…`).

- La réplica es conforme: m0 = Historia C49 = 0,340556331360566, con 33 flujos. `F1-LIBRO` también es conforme y nada bloquea.
- La conclusión es **«utilizable CONDICIONADA (D-US1)»**, con los avisos `V-F1k`, `F1-US-HIPOTESIS` y `F1-SERIES-CERO`. `F1-US-BASE` y `V-F1f` solo informan.
- **El flujo sin crecimiento es 2.484,631379.** La **cota de D-US1 es −64,23 / +63,54 mm = −2,6 % / +2,6 %**; en valor presente del NORMAL, −3,1 % / +3,1 %.
- `resultados.json` y `precio.json` no cambian, porque el libro ya valoraba con C49: precio de Sí 73,31, ponderado 80,06, zona `cumple_regla_k`.
- El paso 13 regeneró `ficha_provisional.json` e `informe_provisional.md` antes de fijar el material. La ficha lleva F1 vigente y utilizable, y el informe dice −2,6 % / +2,6 % y ya no «evaluación no vigente». El material fijado es `91a9726f8fcf8982`, con el resultado F1 nuevo (`5657f787…`), y la solicitud es `SA-4456f50971f1118d`. El expediente espera la auditoría.
- Ajeno a este cambio: en `a0ae904`, la verificación de las entradas de Zoetis está en 0 de 315 celdas comprobadas (apta por entradas: no), y la ficha provisional propone `pendiente_de_datos`, como propuso la fase C. Hay un sellado del registro de entradas de `zoetis_t1c` posterior (`9938d40`, en este repositorio) que no reviso aquí.
