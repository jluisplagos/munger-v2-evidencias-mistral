# Revisión independiente · `producto/redondeo-exacto` (redondeo exacto de la Historia en `fase1_historia.py`)

- **Rama revisada:** `producto/redondeo-exacto` @ `2bafba2`. El código y la prueba están en `a86944b` y el manifiesto en `2bafba2`. La base es `examen/expedientes-f1` @ `c0bbf5c`. Diff revisado: `git diff c0bbf5c..2bafba2` (3 archivos).
- **Revisor:** agente Claude distinto del autor (Opus, esfuerzo alto), 19-nov-2026. No modifiqué la rama ni hice commit en el producto.
- **Copias:** las pruebas se ejecutaron en `/dev/shm/rv/copia`, una copia limpia (`git archive 2bafba2`) con los 1059 binarios del manifiesto. Los binarios se copiaron de `wt_expedientes` solo cuando su huella coincidía. El manifiesto de la copia da 9538 archivos, 0 modificados, 0 ausentes y 0 de más. También usé `/dev/shm/rv/{old,new}_scripts` (`git archive` de `c0bbf5c` y de `2bafba2`) para comparar el antes y el después. Borré todas las copias al terminar.
- **Evidencia:** `evidencia/`. Contiene la comparación de `construir` antes y después en los 48 expedientes con `fase1_partes`, las sondas de `numero`/`numero_exacto`/`redondear` y las salidas de las baterías.
- Experimental supervisado. **No es apto para dinero real.** Esta revisión se limita al redondeo. No acredita aptitud económica.

## Veredicto: **CONFORME CON CORRECCIONES** (documentales y de procedimiento; el código es correcto)

La aritmética es correcta. El importe sale exacto de la cifra impresa, con su signo y su escala. Se redondea una vez en la Historia con ROUND de la hoja (mitad lejos de cero). `numero()` no cambia. Ninguna tolerancia ni decisión cambia, y en los 48 expedientes reales no hay diferencias fuera de los empates y del cero negativo.

Hay que corregir tres cosas, ninguna en la aritmética:

1. La descripción del efecto está incompleta (C1).
2. L14 obliga a rehacer la entrada sellada en un expediente nuevo (C2).
3. La prueba nueva no entra en ninguna batería del paquete (C3).

## 1. Corrección del cálculo

**Rutas de importes (`construir.leer`).** El valor es una `Fraction`:

- `numero_exacto(impreso) × signo`, sumado con `Fraction(0)` inicial;
- `× ESCALA_EXACTA[unidad]`, o la regla de acciones con `10**6`/`10**3` enteros y los mismos umbrales `> 10**5`/`> 10**3`;
- después `ajustar` (signo, `abs` o `−v`, todo con fracciones) y un único `redondear(…, 4)` al escribir la serie.

No hay mezcla de float y fracción en el importe. El único paso a float es el umbral de los comparativos (`float(v2)`, `float(v)`), hecho a propósito. Las decisiones humanas (`valor_mm`) se siguen copiando tal cual, sin redondear, igual que antes.

**Derivados.** Todos parten de valores de la Historia ya redondeados a 4 decimales, como hace la hoja con sus celdas:

- tipo impositivo;
- caja + otros activos financieros;
- medias C46–C50 (3 decimales);
- capitalización (1 decimal).

Para esas entradas, `exacto(repr(float))` es adecuado. El `repr` de un float que salió de un redondeo a 4 decimales, o de un número de JSON, es la cifra decimal escrita, y es el mismo criterio que `verificacion_entradas._frac`. La sonda `evidencia/sonda_numero_redondear.py` lo confirma: en 20.000 fracciones aleatorias, `redondear` coincide con `verificacion_entradas._round_frac`. En `calcular_entrada`, la suma y la media son exactas y se redondean una sola vez.

Límite (no es defecto): `exacto(repr)` no sirve para un float que ya arrastra error binario (`redondear(2.0004999999999997, 3) = 2.0`). El cambio lo evita porque nunca pasa a `redondear` un resultado de aritmética float. Conviene dejarlo escrito en el docstring de `exacto`.

**Doble redondeo en C46–C50.** Existe (exacto → 4 decimales en la Historia → media → 3 decimales). Es intencionado, porque reproduce lo que hace la hoja con las celdas de la Historia. La frase «redondean una sola vez» vale para la Historia y para `calcular_entrada`, no para estas medias.

**Signo, escala y cero.** Los paréntesis, los negativos con guion, las escalas de miles y de unidades, y la regla de acciones con y sin unidad declarada dan el mismo resultado que antes salvo en los empates. `test_acciones_unidad_examen` da 10/10. Ahold (acciones con `unidad`), Zoetis, Elis, Vidrala y Viscofan reconstruyen la Historia idéntica. El cero negativo desaparece: `redondear` devuelve `float(Fraction(0)) = 0.0` (ver C1).

**`numero()` para `motor_a_f1.py`.** Solo cambia de forma: ahora pasa por `_cifra_impresa`, pero construye los mismos textos y aplica el mismo `float`. Comparé el viejo y el nuevo en 20.029 cadenas (aleatorias y límite: guiones, espacios, «4 573,7», «(130,8)», «12a», «1.234.567,89»…). Los resultados son idénticos, incluido el tipo de error, y `float(numero_exacto(s)) == numero(s)` en todos los casos. `motor_a_f1._valor_en_la_fila` sigue usando `FH.numero` y `FH.ESCALA`, que no cambian. `test_motor_a_f1_usgaap` da 290/290.

## 2. Otras reglas

- **Tolerancia de comparativos:** sigue en `max(0,0005·max(|v|,1), 0,0005)`. En los 48 expedientes, las líneas de reexpresión de `historia_revision.md` salen idénticas.
- **EBIT derivado frente a impreso:** el umbral (0,5 % / 0,001) no cambia. Los mensajes usan ahora `redondear(…, 3)` y en los 48 expedientes salen idénticos.
- **Decisiones (`fase1_decisiones.json`), ceros pendientes (H1), propagación a Análisis, `independiente`:** no se tocan.
- **Comprobación del valor declarado en `calcular_entrada`** (1e-9 relativo): no cambia. Ningún expediente real falla con el valor calculado nuevo.
- **`valor_sin_redondear`:** ahora es `float(suma exacta)` en lugar de la suma float. Cambia en el último dígito binario (ver C1). Ningún script lo lee (`grep` en `scripts/`): es solo informativo y aparece en el texto de `fuente`.

## 3. Pruebas

`test_redondeo_historia.py` da **38/38** con el código nuevo. Con el código de `c0bbf5c` da **4/34**: las comprobaciones sobre `construir` y `calcular_entrada` fallan, así que la prueba detecta el defecto.

Cobertura:

| Caso | Cubierto |
|---|---|
| empates positivos y negativos (2,5, −2,5, 1,0005, −1,0005, 2,675…) | sí |
| no empates a ambos lados (1,00049 / 1,00051) | sí |
| paréntesis y negativo con guion | sí |
| unidades y miles | sí |
| millones | **no** (la escala es 1; riesgo bajo) |
| sumas y medias de `calcular_entrada`, con signo | sí |
| cero negativo | sí |
| NaN, booleano y texto rechazados | sí |
| `numero_exacto ≡ numero` (13 cadenas) | sí |
| `construir` real sobre jumbo_f (I17, L14, ≤ 4 decimales) | sí |
| acciones (regla por tamaño y `unidad`), tipo impositivo, caja + otros, medias C46–C50 y capitalización por `construir` | **no** directamente; cubierto por la comparación de los 48 expedientes y por `test_acciones_unidad_examen` |
| umbral de comparativos | no |

La parte de jumbo_f se omite, con aviso y código 0, si falta el expediente. Es aceptable porque lo dice.

Baterías relacionadas sobre la copia limpia con binarios (LibreOffice en secuencia con `flock`): ver §6 y `evidencia/bateria.txt`.

## 4. Manifiesto

Comprobado:

- `2bafba2` lista 9538 archivos: los 8479 archivos de Git (todos con su huella de blob) más los 1059 binarios, que son los mismos y con las mismas huellas que en `c0bbf5c`.
- Respecto de `c0bbf5c` hay **648 altas**: 647 archivos de texto de expedientes del examen (zoetis_t1c 194, ahold_f3 171, jumbo_e 155, jumbo_f 123, configuracion 4) y la prueba nueva. Hay **una modificación** (`fase1_historia.py`) y **ninguna baja**.
- El manifiesto anterior estaba desfasado. Se regeneró por última vez en `a9dff6a`, y los 28 commits del examen hasta `c0bbf5c` añadieron expedientes sin regenerarlo.

**¿Es coherente con el procedimiento?** Sí, en lo técnico. `verificar_paquete.sh` exige que el manifiesto describa el árbol completo, sin «de más». El README pide usar «el MANIFIESTO_SHA256.txt de esta rama para contrastar su árbol». Sin las 647 altas, la verificación de esta rama fallaría. La cabecera del manifiesto dice que incluye los expedientes del examen tal como están en `c0bbf5c`.

**Corrección de procedimiento (C4, menor).** El manifiesto lista el árbol, pero no acredita que su contenido se haya revisado. Las 647 altas son material del examen, no de este cambio, y esta revisión no las cubre. Dos recomendaciones:

1. Regenerar el manifiesto en `examen/expedientes-f1` (o en su integración) en un commit propio. Así el diff del manifiesto de un cambio de producto muestra solo sus 2 entradas.
2. Al incorporar el cambio (INTEGRACION.md, «Incorporación controlada»), declarar como aceptados solo `personaje_v2/scripts/fase1_historia.py` (manifiesto de `2bafba2`) y `personaje_v2/pruebas/test_redondeo_historia.py`, nunca «el manifiesto» entero.

## 5. Efecto en los expedientes y cifra de L14

Ejecuté `construir` con el código de `c0bbf5c` y con el de `2bafba2` sobre copias de los 48 expedientes con `fase1_partes`. 12 no construyen con ninguna de las dos versiones (texto/ ausente o sin metadatos) y dan el mismo error. Las diferencias son estas:

| Expedientes | Cambio |
|---|---|
| jumbo, jumbo_b | `intereses_financiacion` 2022 (I17 antes del cruce J3) 7,0351 → 7,0352; `circulante` 2025 (L14) 61,1585 → 61,1586 |
| jumbo_c, jumbo_d, jumbo_e, jumbo_f | `arrendamientos_principal` 2022 (I17) 7,0351 → 7,0352; L14 61,1585 → 61,1586 |
| jumbo_b | `analisis.C46.valor_sin_redondear` 307.1729666666667 → 307.17296666666664, y el mismo número en el texto de `fuente`; el valor 307,173 no cambia |
| 15 copias de Vidrala, 2 de Viscofan y las 6 de Jumbo | adquisiciones con cero: `-0.0` → `0.0` en `fase1_v63.json` (y «-0.000» → «0.000» en `historia_revision.md`); numéricamente igual |
| Ahold (6), Elis (4), Zoetis (3) | ninguno |

**C1 (documental).** La afirmación de que «solo cambian I17 y L14» es cierta para los valores de la Historia. No lo es para los bytes:

- el cero negativo desaparece;
- `valor_sin_redondear` y el texto de `fuente` cambian en jumbo_b;
- la tabla de `historia_revision.md` muestra 61,159.

Ahora `v63_xml._texto_numero(-0.0)` escribía «-0» en la celda y pasa a escribir «0». Un libro regenerado tendrá otra huella aunque sea numéricamente igual. Basta con declararlo en el mensaje y en el registro del cambio.

**Los expedientes en curso no cambian solos.** `pipeline.py` (paso 2) solo llama a `construir` si falta `fase1_v63.json`. jumbo_f, que espera la fase A, conserva 7,0351 y 61,1585 mientras no se reconstruya. El cambio se aplicará a un expediente nuevo, como pide CLAUDE.md.

### L14: ¿61,1585 o 61,1586?

Datos (AR2025, p. 209, nota 5.30; el estado de flujos solo trae el agregado):

- cinco líneas: (49.627.440) + 1.798.445 + (19.492.757) + 1.450.000 + 4.713.202 = **(61.158.550)**;
- subtotal impreso: **(61.158.549)**, 1 € menos por el redondeo del emisor.

Con la convención de la fila 14 (+ consume caja):

- por las líneas: 61,15855 mm → ROUND a 4 decimales = **61,1586** (empate exacto, mitad lejos de cero);
- por el subtotal: 61,158549 → **61,1585**.

**Según las reglas del producto, la cifra correcta es 61,1586.** Tres motivos:

1. La regla del producto está escrita en tres sitios:
   - el docstring de `fase1_historia.py`, línea 18: «circulante = −(suma de las líneas de variación del circulante del estado de flujos)»;
   - la nota que `construir` escribe en la propia Historia: «Aumento del circulante = −(suma de las líneas…): convención del ejercicio»;
   - `prompts/historia_anio.md`, línea 19: `circulante_lineas` = «TODAS las líneas de variación».

   El producto nunca lee el subtotal y lo aplica igual a todas las empresas y a los diez años. Con aritmética exacta y ROUND de la hoja, esa regla da 61,1586.
2. El 61,1585 anterior no salió del subtotal. Salió del error binario: 61,15855 se guardaba como 61,1585499…, el mismo defecto que en I17. Que coincidiera con el redondeo del subtotal fue casualidad.
3. La entrada sellada `Historia!L14` del registro de jumbo_f se eligió para «reproducir exactamente el libro» con el subtotal. Así lo dicen su derivación `round(-o[aux …subtotal_2025], 4)`, la nota del extractor («el subtotal publicado reproduce el libro») y `examen/jumbo/revision_registro/REVISION.md`, línea 29. El subtotal es una cifra publicada y económicamente defendible. Pero esa derivación no describe lo que hace el producto, y mantenerla para conservar el 61,1585 sería legitimar un resultado antiguo con otra fuente (CLAUDE.md).

La diferencia es de 1 € (0,000001 mm) y es inmaterial en cualquier tolerancia. La cuestión es de coherencia, no económica.

**C2 (procedimiento).** Con el código nuevo, un expediente reconstruido tendrá Historia!L14 = 61,1586. La entrada sellada (`valor_modelo` 61,1585, fórmula sobre el subtotal) quedará «desactualizada» por vigencia exacta (`verificacion_entradas`, línea 1277), y su fórmula no reproducirá el libro. Lo que hay que hacer:

- **No** editar el registro sellado de jumbo_f.
- **No** cambiar el producto al subtotal para salvar el sello. Ese sería otro cambio de regla, para todas las empresas, que necesita decisión humana registrada.
- En el expediente nuevo, derivar L14 de los cinco componentes (orígenes auxiliares por línea, p. 209, con su cita), con `round(-(Σ), 4) = 61,1586`, y volver a revisarlo. La conciliación debe mencionar el subtotal impreso (61.158.549) y la diferencia de 1 € del emisor.
- I17 (`valor_modelo` 7,0351, cuyo revisor ya dijo que el exacto es 7,0352) se resuelve también con un sello nuevo en ese expediente.

Mejora opcional, fuera de este cambio: un aviso en `historia_revision.md` cuando la suma de líneas difiera del subtotal impreso.

## 6. Baterías (copia limpia `2bafba2` con binarios)

Ver `evidencia/bateria.txt` y `evidencia/t_*.txt`.

| Batería | Resultado |
|---|---|
| `verificar_paquete.sh` (rápido: manifiesto 9538 · 0/0/0, entorno, contraste del piloto Vidrala 2025 con `numero()` (salida idéntica), comprobadores 114/114, F1-SERIES 80/80, P-FOSO 66/66) | **PASA** (83 s) |
| `test_redondeo_historia.py` | 38/38 |
| `test_acciones_unidad_examen.py` | 10/10 |
| `test_f1_series_escala.py` | 80/80 |
| `test_entrada_efectiva_415.py` (LibreOffice) | PASA |
| `test_verificacion_entradas_415.py` (LibreOffice) | PASA (527 s) |
| `test_verificacion_entradas_414.py` | PASA |
| `test_motor_a_f1.py` | 163/163 |
| `test_motor_a_f1_usgaap.py` | 290/290 |
| `test_pieza1.py` | 17/17 |
| `test_v631_f1.py` | 29/29 |

No ejecuté el modo `completa` de `verificar_paquete.sh` (30–45 min con LibreOffice). Las baterías de cierre, resumen, estados, auditorías, trazabilidad e integración V6.4 no llaman a `construir` con informes reales, y ese modo no cubre este cambio mejor que la comparación de los 48 expedientes.

Un primer intento sobre una copia sin binarios falló en `test_entrada_efectiva_415`, `test_verificacion_entradas_414/415`, `test_comprobadores`, `test_pieza1` y una prueba de `test_motor_a_f1` porque faltaban los `.xlsx` de la base. No era una regresión. Se repitió sobre la copia con los 1059 binarios.

## Correcciones pedidas

| # | Gravedad | Qué |
|---|---|---|
| C1 | menor, documental | Declarar todos los efectos: el cero negativo desaparece en adquisiciones (`-0.0` → `0.0` en `fase1_v63.json` y «-0» → «0» en el libro), `valor_sin_redondear` y `fuente` cambian en el último dígito (jumbo_b C46), y la tabla de `historia_revision.md` cambia. Precisar que las medias C46–C50 redondean dos veces, como la hoja. |
| C2 | media, procedimiento | L14 = 61,1586 es la cifra del producto. En el expediente nuevo, rehacer y volver a sellar L14 (componentes) e I17 (7,0352). No tocar el registro sellado de jumbo_f ni cambiar la regla al subtotal sin decisión humana. |
| C3 | menor | Añadir `test_redondeo_historia.py` a `verificar_paquete.sh` (y a `ejecutar_pruebas_reparacion.sh` si procede), con su mínimo de comprobaciones. Ahora no lo ejecuta ninguna batería del paquete. Añadir casos de millones y uno de acciones por `construir`. |
| C4 | menor, procedimiento | Regenerar el manifiesto del examen en su propia rama o commit. Al integrar, aceptar solo los dos archivos de este cambio. |

Observación sin corrección: la tabla de `historia_revision.md` (`f"{v:,.3f}"`) sigue mostrando con el redondeo de Python, no con ROUND (61,1585 se vería «61,158»). Es solo de presentación.
