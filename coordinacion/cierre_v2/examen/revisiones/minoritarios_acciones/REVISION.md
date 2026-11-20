# Revisión independiente · `producto/minoritarios-acciones` (acciones exactas de los metadatos, Análisis!C55)

- **Rama revisada:** `producto/minoritarios-acciones` @ `fd03369` sobre `examen/expedientes-f1` @ `f02f7b1`.
  - `1fa300b`: solo el manifiesto del árbol del examen.
  - `fd03369`: el cambio (`fase1_historia.py`, `prompts/metadatos_fase1.md`, prueba nueva, bloque en `verificar_paquete.sh` y manifiesto).
- **Revisor:** agente Claude distinto del autor (Opus, esfuerzo alto), 19-nov-2026. No modifiqué la rama.
- **Copias:**
  - copia limpia `git archive fd03369` en `/dev/shm/rm/copia`, con los 1059 binarios del manifiesto (copiados de `wt_expedientes` solo si la huella coincidía): 9675 archivos, 0 modificados, 0 ausentes, 0 de más;
  - `git archive` de los scripts de `f02f7b1` y de `fd03369` para comparar antes y después.

  Borré todas las copias al terminar.
- **Evidencia:** `evidencia/`.
- Experimental supervisado. **No apto para dinero real.** Esta revisión no acredita aptitud económica.

## Veredicto: **CONFORME CON CORRECCIONES**

Lo que el cambio hace, lo hace bien:

- es aditivo;
- con `impreso`, la comparación es exacta (fracciones);
- se detiene antes de escribir `fase1_v63.json`;
- sin `impreso`, nada cambia: 49 expedientes dan resultados idénticos byte a byte.

Hay que corregir dos cosas antes de usarlo en un expediente nuevo:

- **C1:** el nombre `unidad` choca con el uso que ya tiene.
- **C2:** la regla choca con la dilución que el propio prompt permite sumar.

También conviene corregir el respaldo de la capitalización a 1 decimal (C3) en este mismo cambio.

La decisión de no tocar los minoritarios negativos es correcta y su análisis también (§6).

## 1. Corrección

`defecto_acciones_meta(ac)` hace esto:

1. Si no hay `impreso`, no comprueba nada.
2. Exige que `impreso` sea texto y que `unidad` (por omisión «unidades») esté en `ESCALA_EXACTA`.
3. Lee `impreso` con `numero_exacto`, la misma lectura que `numero()`, y exige que sea positivo.
4. Exige `exacto(valor) == impreso × escala` con fracciones.

El defecto se suma a `inc_acc`. Por eso aparece en «BLOQUEA» de `historia_revision.md` y `construir` devuelve 1 sin escribir `fase1_v63.json`, igual que las incoherencias de acciones que ya existían. El orden no cambia: decisiones inválidas, luego faltantes y luego acciones.

`exacto(repr(float))` es adecuado aquí, porque `valor` viene de JSON: 424.927535 se lee como 424927535/10⁶.

Sondas (`evidencia/sonda_acciones.py`):

| Caso | Resultado | Juicio |
|---|---|---|
| «424.927.535» / «424,927,535», valor 424,927535 | sin defecto | correcto |
| valor 424,928 con «424.927.535» | defecto | correcto (el caso Zoetis) |
| «886,877» miles → 886,877; «905» millones; «424,9» millones | sin defecto | correcto |
| valor como texto, booleano, ausente; impreso vacío, «-», «(1)» | defecto | correcto |
| `unidad: None` explícita | defecto («None no es una de…») | aceptable |
| «424.928» en **millones** (3 decimales) | defecto, porque se lee 424.928 **millones** = 424928 | ambigüedad heredada de `numero()`: un número con tres decimales se toma por separador de miles. Bloquea en vez de aceptar, así que es seguro, pero el mensaje confunde. **Límite (C4)** |
| `unidad` «millones de acciones» (la que llevan hoy ahold_f2 y ahold_f3) **con** `impreso` | defecto («no es una de…») | ver **C1** |
| valor = en circulación + dilución (lo que el prompt permite) con `impreso` de las acciones en circulación | defecto | ver **C2** |

## 2. Metadatos sin `impreso` y otras reglas

- Ejecuté `construir` con el código de `f02f7b1` y con el de `fd03369` sobre copias de los **49** expedientes con `fase1_partes` (`evidencia/comparacion_49_expedientes.txt`). Comparé `fase1_v63.json`, `historia_revision.md` y la salida del programa. **No hay ninguna diferencia.** Los 11 expedientes que no construyen dan el mismo error con las dos versiones. Ninguno lleva `impreso`.
- `incoherencias_acciones` (factor 10), la serie de la Historia, la regla de unidad de las partidas (`AR_*.json`), la capitalización, `rellenar_fase1_v63.py` y `v63_xml` no se tocan.
- El prompt cambia en dos sitios: `acciones_diluidas` (pide `impreso`, `unidad` y el valor exacto) y `capitalizacion` («con el valor exacto de las acciones, sin redondearlas antes»).

## 3. Correcciones

### C1 · MEDIA · `unidad` ya significa otra cosa en `acciones_diluidas`

Hoy `acciones_diluidas.unidad` es la **unidad de `valor`**:

- ahold_f2 y ahold_f3 traen `"unidad": "millones de acciones"`;
- `rellenar_fase1_v63.py`, línea 283, la escribe en `Control maestro!H` de la fila de Análisis!C55 (comprobado en `Ahold_v63_datos.xlsx`, fila 52: H = «millones de acciones»).

El cambio le da otro significado: la unidad **de `impreso`**. Con el prompt nuevo, el agente escribirá `"unidad": "unidades"` para Zoetis y `rellenar` pondrá «unidades» como unidad de un C55 de 424,927535 **millones**. Es una etiqueta de evidencia falsa en el Control maestro. Al revés, unos metadatos como los de Ahold con `impreso` se detienen por la unidad.

**Corrección:** usar una clave propia para la escala de la cifra impresa (por ejemplo `unidad_impreso` o `escala_impreso`) y dejar `unidad` como unidad de `valor`. Hay que actualizar el prompt, la función y la prueba, y añadir un caso con `unidad: "millones de acciones"` y `impreso`.

### C2 · MEDIA · dilución sumada frente a «valor = impreso»

El mismo párrafo del prompt pide `valor` = `impreso` en millones y, a la vez: «si hay instrumentos dilutivos materiales …, suma la dilución que publique la empresa al cierre». Con dilución, `valor` no es ninguna cifra impresa y `construir` se detiene. El agente solo puede salir de ahí omitiendo `impreso`, y entonces se pierde la comprobación sin que nadie lo vea.

**Corrección.** Decir qué se hace en ese caso. Hay dos opciones:

- (a) `impreso` = acciones en circulación, y un `dilucion_impresa` (con su cita) que se suma de forma exacta;
- (b) componentes `[{impreso, unidad, pagina}]` sumados como en `fase1_partes`.

Mientras no se elija, el prompt debe pedir que no se sume la dilución en `valor` con `impreso`. Además, conviene que `historia_revision.md` avise cuando los metadatos no traen `impreso`, para que la falta de comprobación quede a la vista. No hace falta bloquear: los expedientes anteriores no lo traen.

### C3 · MENOR · respaldo de la capitalización a 1 decimal: sí, corregirlo ya

`construir` (línea 756) calcula `capitalizacion = redondear(precio × acciones, 1)` cuando los metadatos no la traen. Es el mismo tipo de defecto que corrige esta rama:

- 0,1 mm es un redondeo de importe más basto que el del libro;
- U2/N4 de `verificacion_entradas` admite en un importe el resultado exacto o su redondeo a 3 decimales (±0,0005). 31.053,7 frente a 31.053,7042578 no cumple, y la derivación C41 = C37 × C55 quedaría en discrepancia.

Hoy está inactivo: los 49 expedientes traen `capitalizacion` en sus metadatos. Pero el prompt nuevo dice cómo calcular las acciones, no que no se redondee el producto, y los metadatos de Zoetis ya traían 31.053,7.

**Corrección:** es una línea. Guardar el producto exacto (`float(exacto(precio) × exacto(acciones))`) o redondearlo a 3 decimales, con una prueba. En el prompt, añadir «sin redondear el resultado». Opcional: avisar si la `capitalizacion` declarada no es `precio × acciones` dentro de la regla U2.

### C4 · MENOR · pruebas

- Con el código de `f02f7b1` la prueba da **9/17** en mi ejecución, no 8/17. Varias comprobaciones de «defecto» pasan con el código antiguo por el motivo equivocado: `defectos()` convierte el `AttributeError` en una lista de un defecto, y `len(...) == 1` se cumple. Pasa con «impreso no texto», «no numérico», «booleano/ausente», «cero/guion» y «unidades como millones». Hay que comprobar el texto del defecto, o que el envoltorio devuelva un centinela que falle.
- Las dos comprobaciones de `v63_xml` y de C41 prueban lo que ya existía. Están bien como documentación, pero no prueban el cambio.
- Faltan dos casos: el de C1 (`unidad` del valor junto con `impreso`) y el límite de los 3 decimales en millones (C4 de la tabla).

## 4. Pruebas ejecutadas (copia limpia de `fd03369` con binarios)

LibreOffice en secuencia con `flock`. Salidas en `evidencia/bateria.txt` y `evidencia/t_*.txt`.

| Batería | Resultado |
|---|---|
| `verificar_paquete.sh` rápido: manifiesto 9675 · 0/0/0, entorno, piloto, comprobadores, F1-SERIES, redondeo exacto, **acciones exactas (bloque nuevo)**, P-FOSO | **PASA GLOBAL** (89 s) |
| `test_acciones_metadatos_exactas.py` | 17/17 (9/17 con el código de `f02f7b1`; ver C4) |
| `test_redondeo_historia.py` | 44/44 |
| `test_acciones_unidad_examen.py` | 10/10 |
| `test_entrada_efectiva_415.py` (LibreOffice) | PASA |
| `test_verificacion_entradas_414.py` | PASA |
| `test_motor_a_f1.py` | 177/177 |
| `test_pieza1.py` | 17/17 |
| `test_v631_f1.py` | 29/29 |

No ejecuté `test_verificacion_entradas_415` (≈ 9 min con LibreOffice): no usa `construir` con metadatos y el cambio no toca `verificacion_entradas`.

## 5. Manifiesto

- **`1fa300b`:** 9674 entradas. Frente a `f02f7b1` (9547) hay 127 altas (jumbo_g 123, ahold_f3 3, configuracion 1), 2 modificaciones (`verificacion_entradas.json` de ahold_f3 y de zoetis_t1c, los sellados) y ninguna baja. Ningún archivo de producto cambia.
- **`fd03369`:** solo cambian `fase1_historia.py`, `metadatos_fase1.md` y `verificar_paquete.sh`, y se añade la prueba.
- La copia limpia con binarios verifica 9675 / 0 / 0 / 0.

Esto aplica la recomendación C4 de la revisión del redondeo: el manifiesto del examen va en un commit aparte y el diff del cambio de producto solo muestra sus cuatro archivos. Lo ideal sería que ese commit estuviera en `examen/expedientes-f1`. Estar en la rama de producto, como commit aparte y sin cambios de producto, es aceptable. Al integrar se aceptan solo los cuatro archivos de `fd03369`.

## 6. Minoritarios negativos: la decisión de no cambiarlos

**El análisis del autor es correcto.** Lo comprobé en `Zoetis_v63_evaluada.xlsx` (zoetis_t1c):

- `Historia` C26:L26 tiene una validación «decimal ≥ 0» con el mensaje «no admite negativos».
- `Motor!E234` (V37) da «INV|Minoritarios negativos en Historia fila 26 … ≥ 0».
- Convenciones V6.3 §8 incluye a los minoritarios en los dominios que no admiten negativos.
- La única fórmula que usa la fila 26 es el puente `Historia!C65 = MAX(0,L25)+L26`, y solo con el **último** año.
- Los 10-K imprimen «Equity attributable to noncontrolling interests (2)» en 2022 (p. 66) y «(6)» en 2023 (p. 67). `ajustar` toma `abs` porque `minoritarios` no está en `CON_SIGNO`, así que la Historia guarda +2 y +6. L26 (2025) es 0 («—»).

El efecto económico en Zoetis es nulo, porque el puente solo usa 2025.

**No cambiarlo en esta rama es lo correcto.** Las tres salidas son cambios de regla del producto o de la plantilla y necesitan la decisión de la persona (Z-MIN está pendiente):

- (a) 0 con aviso;
- (b) aceptar el negativo, que cambia la validación y el puente;
- (c) dejar el valor absoluto.

Mezclarlo con el arreglo de C55 haría pasar una política por una corrección de datos.

La opción (a) que recomienda el autor es razonable: un déficit de minoritarios no es valor de los accionistas de la matriz, y tratarlo como 0 es prudente. Pero la analogía con las pensiones solo vale en parte. Allí la plantilla conserva el negativo publicado y lo anula en la fórmula (`MAX(0,L25)`). Aquí la validación impide guardarlo, así que (a) obliga a transformar la cifra en la fase 1 y a dejar la publicada en el registro.

**Observación general (fuera del alcance, para un cambio aparte):** `ajustar` convierte en positivo, sin aviso, cualquier negativo impreso de las partidas que no son `CON_SIGNO`. En zoetis_t1c, `historia_revision.md` muestra 2 y 6 sin ninguna nota. Mientras se decide Z-MIN, conviene que `construir` avise en `historia_revision.md` cada vez que cambia el signo de una cifra impresa, en minoritarios o en cualquier otra partida que la plantilla quiera ≥ 0.

## Resumen de las correcciones

| # | Gravedad | Qué |
|---|---|---|
| C1 | media | Clave propia para la escala de `impreso`; `unidad` sigue siendo la unidad de `valor`, porque `rellenar` la escribe en Control maestro!H. |
| C2 | media | Resolver la dilución sumada frente a `impreso` (componentes o `dilucion_impresa`) y avisar cuando falte `impreso`. |
| C3 | menor | Capitalización de respaldo exacta o a 3 decimales, no a 1; en el prompt, «sin redondear el resultado». |
| C4 | menor | Que las pruebas fallen con el código anterior por el motivo correcto; casos de C1 y del límite de los 3 decimales en millones. |

---

# Ronda 2 · `2a323b8` (sobre `fd03369`) e integración

- **Revisado:** `2a323b8`, con las correcciones C1–C4 y el aviso de signo, frente a mi ronda 1.
- **Revisor:** el mismo agente de la ronda 1, distinto del autor. 19-nov-2026.
- **Copias:** copia limpia `git archive 2a323b8` con los 1059 binarios (huellas del manifiesto): 9675 archivos, 0 modificados, 0 ausentes, 0 de más. Borrada al terminar.
- **Evidencia:** `evidencia_r2/`.

## Veredicto: **CONFORME**

### Correcciones

| # | Estado | Comprobación |
|---|---|---|
| C1 | **hecha** | La escala de la cifra impresa tiene clave propia, `escala_impreso`, y `unidad` sigue siendo la unidad de `valor`. Nunca se usa para leer `impreso`. Prueba: con `unidad` «millones de acciones» (como Ahold) e `impreso`, `construir` construye, conserva la unidad y da el valor por comprobado. Con `unidad` «millones» e `impreso` en unidades, la escala no se toma de `unidad`. |
| C2 | **hecha** | `dilucion: [{impreso, escala_impreso, pagina, concepto}]`. Cada componente se lee con su escala y se suma de forma exacta a las acciones en circulación. Detiene: la dilución sumada sin declarar sus componentes, la dilución redondeada, un componente mal formado y un valor de `dilucion` que no es una lista. Si los metadatos no traen `impreso`, `historia_revision.md` lo avisa en la sección nueva «Acciones de los metadatos (Análisis!C55)», sin bloquear. Límite menor: `pagina` y `concepto` no se validan (son documentales). |
| C3 | **hecha** | La capitalización de respaldo es `float(exacto(precio) × exacto(acciones))`, sin redondear (73,08 × 424,927535 = 31.053,7042578). El prompt añade «sin redondear el resultado». |
| C4 | **hecha** | Con el código de `f02f7b1` la prueba da **3/30** (lo reproduje). Las tres que pasan son comportamiento que no cambia: `v63_xml` escribe el repr, y zoetis_t1c construye con el valor exacto y con sus metadatos de hoy. Ninguna comprobación de defecto pasa ya por el motivo equivocado. Hay casos nuevos para C1 y para «424.928» en millones, que ahora explica el separador de miles. |
| Extra | **hecho** | `SALDOS_SIN_SIGNO` = deuda, arrendamientos, caja, otros activos financieros, minoritarios, acciones. Un negativo impreso se avisa en `historia_revision.md` y la conversión no cambia. En los 49 expedientes solo salta en Zoetis: minoritarios 2022 (−2) y 2023 (−6), en sus tres copias. |

**Observación sin corrección.** Pensiones queda fuera del aviso a propósito: en el estado de financiación el déficit suele imprimirse en negativo («funded status»). Pero esa misma ambigüedad es la razón para avisar. `ajustar` toma el valor absoluto de la fila 25, y un superávit impreso en negativo, como activo neto, pasaría a déficit sin aviso. Para un cambio aparte: un aviso neutro también para pensiones («impreso negativo: confirmar si es déficit o superávit»).

### Comprobaciones de esta ronda

- **Diagnóstico de expedientes.** Ejecuté `construir` con `f02f7b1` y con `2a323b8` sobre los 49 expedientes con `fase1_partes` (`evidencia_r2/comparacion_49_expedientes_r2.txt`).
  - `fase1_v63.json` y la salida del programa son **idénticos en los 38 que construyen**.
  - Los 11 que no construyen dan el mismo error con las dos versiones.
  - `historia_revision.md` solo **añade** dos secciones: «Acciones de los metadatos» (en los 38, con el aviso de `impreso` ausente) y «Signo de saldos impresos en negativo» (solo en las 3 copias de Zoetis).
- **Baterías** (`evidencia_r2/bateria.txt`):

| Batería | Resultado |
|---|---|
| `verificar_paquete.sh` rápido (manifiesto 9675 · 0/0/0; acciones exactas 30/30; redondeo 44/44; F1-SERIES; P-FOSO; piloto) | **PASA GLOBAL** |
| `test_acciones_metadatos_exactas.py` | 30/30 (3/30 con `f02f7b1`) |
| `test_redondeo_historia.py` | 44/44 |
| `test_acciones_unidad_examen.py` | 10/10 |
| `test_entrada_efectiva_415.py` (LibreOffice) | PASA |
| `test_verificacion_entradas_414.py` | PASA |
| `test_motor_a_f1.py` | 177/177 |
| `test_pieza1.py` | 17/17 |
| `test_v631_f1.py` | 29/29 |

- **Manifiesto de la rama:** respecto de `fd03369` solo cambian los 4 archivos del cambio.

## Integración en `examen/expedientes-f1`

- **Base:** `aaa2802`. Es `f02f7b1` más 3 commits del examen: ahold_f3 sellado, y fase A y fase B escrita de jumbo_g. Ninguno toca código.
- **`f55754c`**, `merge --no-ff` de `producto/minoritarios-acciones` (`2a323b8`):
  - Solo entran los 4 archivos aceptados: `personaje_v2/scripts/fase1_historia.py`, `personaje_v2/prompts/metadatos_fase1.md`, `personaje_v2/pruebas/test_acciones_metadatos_exactas.py` y `verificar_paquete.sh`.
  - Los 4 son idénticos byte a byte a `2a323b8`.
  - El manifiesto de la rama no se fusionó: se conservó el de `aaa2802`.
  - No se tocó ningún expediente, no se ejecutó el pipeline y no se tocó jumbo_g.
- **`1fc9359`**, manifiesto regenerado en su propio commit. Lo generé sobre una copia limpia de `f55754c` con los 1059 binarios: 9687 archivos.
  - Respecto del manifiesto anterior, que estaba desfasado: los 4 archivos aceptados más 141 entradas del árbol del examen (jumbo_g 135, ahold_f3 4, zoetis_t1c 1, configuracion 1).
  - Esas 141 entradas solo se listan; esta integración no las acredita, y la cabecera y el mensaje del commit lo dicen.
- **`verificar_paquete.sh` rápido sobre esa copia con el manifiesto nuevo:** **RESULTADO GLOBAL PASA** (9687 · 0/0/0). Salida en `evidencia_r2/verificar_paquete_rapida_integracion_1fc9359.txt`.
- **Push:** `origin/examen/expedientes-f1` = `1fc9359` (avance rápido desde `aaa2802`).

Los expedientes en curso no cambian solos: el paso 2 del pipeline solo llama a `construir` si falta `fase1_v63.json`. Para que C55 de Zoetis salga exacto (424,927535) hace falta un expediente nuevo con `impreso` en sus metadatos.
