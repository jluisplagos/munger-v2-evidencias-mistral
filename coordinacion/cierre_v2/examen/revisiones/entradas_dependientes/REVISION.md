# Revisión independiente · `producto/entradas-dependientes` (entradas que dependen de una celda de juicio: recálculo determinista tras la fase B)

- **Rama revisada:** `producto/entradas-dependientes` @ `084d2e4` sobre `1fc9359`. El cambio está en `90572af` y el manifiesto en `084d2e4`. Diff revisado: `git diff 1fc9359..084d2e4`, 6 archivos más el manifiesto:
  - nuevos: `scripts/entradas_dependientes.py` y `pruebas/test_entradas_dependientes.py`;
  - modificados: `pipeline.py`, `cierre_v2.py`, `cambiar_base.py` y `verificar_paquete.sh`.
- **Revisor:** agente Claude distinto del autor (Opus 5.5), 19-nov-2026. No toqué la rama del autor, `jumbo_g` ni ningún otro expediente. De `jumbo_g` solo hice copias, y sus 158 archivos tienen las mismas huellas antes y después de la revisión. No leí la rúbrica ni `contradictor/`.
- **Copias** (en `/dev/shm`, borradas al terminar):
  - `nuevo`: `git archive 084d2e4` con los 1059 binarios del manifiesto, copiados de `wt_expedientes` solo cuando su huella coincidía;
  - `mixto`: la prueba nueva con los `pipeline.py`, `cierre_v2.py` y `cambiar_base.py` de `1fc9359` y sin `entradas_dependientes.py`;
  - varias copias de `jumbo_g`.
- **LibreOffice:** siempre con `flock /home/user/e_work/libreoffice.lock`, una ejecución cada vez.
- **Evidencia:** `evidencia/`.
- Experimental supervisado. **No es apto para dinero real.** Esta revisión no acredita aptitud por entradas ni aptitud económica.

## Veredicto: **CONFORME** (sin correcciones pendientes)

El recálculo hace lo que dice y nada más:

- toma la fórmula registrada, sus orígenes publicados y la celda de juicio que acaba de escribir la fase B;
- calcula con aritmética exacta y guarda según U2;
- escribe el mismo número en las seis copias, más un rastro auditado;
- no toca fuentes, comprobaciones, vínculos, fórmulas ni orígenes.

Cuando hay un valor nuevo, los sellos del revisor de esas entradas dejan de valer y hay que volver a sellar. Sin declaraciones, el pipeline no hace nada distinto. Es idempotente. La fase C y la auditoría ven el rastro.

Las cifras de `jumbo_g` las reproduje con un cálculo propio y con el paso 9 de verdad, con LibreOffice, en copias:

| Cifra | Antes | Después |
|---|---|---|
| C46 | 317,617 | 317,902 |
| C40 | 255,108 | 255,305 |
| Partida F1-K3a | 10,444 | 10,729 |
| Precio de Sí | 33,3838 | 33,4209 |

Al final dejo siete observaciones que no bloquean y el resultado de la integración. Integré la rama en `examen/expedientes-f1` (`e031edb` y `23be5de`, con push). En la copia limpia, la `rapida` falla solo en el manifiesto, por 128 archivos de vinci que ya estaban fuera de él antes de integrar.

## 1. ¿Abre una vía para alterar entradas o legitimar resultados? No

Comparé instantáneas justo antes y justo después de `recalcular_dependientes`, en el paso 9 de verdad sobre una copia de `jumbo_g` con la declaración añadida a C46 y C40 (`evidencia/e2e_diff_recalculo.txt`). Solo cambia esto:

| Archivo | Qué cambia |
|---|---|
| `verificacion_entradas.json` | `valor_modelo` de C46 y C40, más la clave nueva `recalculo_dependiente`. Ni la comprobación, ni el vínculo, ni la fuente, ni la derivación, ni ninguna otra de las 566 entradas. |
| `fase1_v63.json` y `fase1_metadatos.json` | `analisis.C46/C40.valor`, más su `recalculo_dependiente`. |
| `motor_a_f1.json` | Solo la partida `conciliacion_fcf_base[0]` (componente C46): `importe` 10,444 → 10,729, una marca añadida al final de su texto y `recalculo_dependiente`. |
| Los dos libros | Análisis C46 y C40, y una nota añadida en Control maestro N43 y N40, iguales en los dos libros. Ninguna otra celda de ninguna hoja. |
| Nuevos | `recalculo_dependientes.json` y su copia en `../resultados/`. |

`fase_a.json` y `fase_b.json` no cambian.

**Las barreras están en el código, y las pruebas las ejercitan.**

- Solo se recalcula una entrada declarada en el registro (`derivacion.recalculo`) que cumpla todo esto:
  - es una celda numérica de datos de Análisis que declara la fase 1 (sin las de texto), es de clase `derivado` y no es una fórmula del libro;
  - su fórmula no escribe cifras, usa todos sus orígenes y solo ellos, y cada origen influye;
  - toda celda de juicio de la fórmula está declarada y la escriben la fase A o la B (nunca la C, que escribe después);
  - sus demás orígenes son auxiliares del registro con número o celdas de datos del libro, nunca fórmulas;
  - no forma cadenas: ninguna derivada del registro usa una entrada dependiente sin declararse también;
  - no tiene a la vez un `calculo` de `fase1_historia`;
  - declara `regla`;
  - si hay partida K3a del componente, declara `conciliacion_f1`, y con `true` hay una sola partida.
- La fórmula se evalúa con el evaluador AST de `verificacion_entradas` (sin `eval`).
- Antes de escribir:
  - las copias tienen que coincidir con el valor actual o con el nuevo;
  - los libros se escriben en temporales con la lista blanca de entradas de la plantilla (una fórmula no se puede escribir) y pasan su verificador.
- Ante cualquier defecto se detiene sin escribir nada. Hay 19 casos de prueba, todos «se detiene sin escribir nada».
- Una partida K3a tocada a mano después de un recálculo detiene el siguiente.

**F1-K3a no queda «legitimada».** Con `conciliacion_f1`, la partida cambia exactamente lo que cambia C46, y el componente de K3a (C46 menos la media de la fila 11) cambia lo mismo. El residuo de K3a no cambia: si fallaba, sigue fallando; si pasaba, sigue pasando. Con `conciliacion_f1: false`, K3a juzga la partida tal como está, y una diferencia nueva bloquearía.

**La declaración no la puede poner una fase.** Vive en el registro, que es material auditado, y forma parte de la huella de la entrada (§5). Añadirla invalida cualquier sello anterior de esa entrada (comprobado: al añadirla solo cambia la huella de C46). La fase B solo influye en C46 a través de C76, por la fórmula J1 registrada, que es el acoplamiento que la decisión J1 manda y que antes no se aplicaba.

## 2. Expedientes sin declaraciones: no cambia nada

- `hay_declaraciones` falso (sin registro, registro ilegible o sin `recalculo`): el pipeline no lanza el programa ni en el paso 2 ni en el paso 9, ni anota nada en el historial. Lo dice la prueba, y lo confirmé con el paso 9 de verdad sobre una copia de `jumbo_g` sin declaración: no hay línea de `entradas_dependientes`, C46 sigue en 317,617 y el precio de Sí es 33,3838, el de antes.
- Ninguno de los 13 registros de los expedientes declara `derivacion.recalculo` (`evidencia/expedientes_sin_declaraciones_y_material.txt`).
- `MATERIAL_FIJO` gana `recalculo_dependientes.json`, pero `material()` solo cuenta los archivos que existen. El identificador de material de `ahold_f3`, `jumbo_e` y `zoetis_t1c` es el mismo con el `cierre_v2` actual y con el de la rama. Ninguna auditoría pendiente cambia de material por esto.
- `cambiar_base.py comprobar` y las entradas de la fase C solo cambian si existe el rastro.

## 3. Idempotencia

Una segunda aplicación con la misma fase B, sobre la copia real de `jumbo_g` ya recalculada, no cambia ningún archivo: las huellas de todo el expediente son idénticas. Tampoco reescribe el rastro.

La prueba cubre además dos cosas:

- ir de 150 a 140 y volver a 150 deja los mismos archivos que ir a 150 directamente;
- la recuperación de una aplicación interrumpida: las copias admiten el valor actual o el nuevo, y el valor declarado y el importe declarado de K3a se conservan del primer rastro.

## 4. La fase C y la auditoría ven el rastro

- `recalculo_dependientes.json` (antes y después, C76 usado, orígenes con su procedencia y huellas de los archivos escritos) va en `MATERIAL_FIJO`. La auditoría del paso 13 lee además toda la carpeta.
- La fase C lo recibe entre sus entradas, con la advertencia de que `datos_v63.md` da los valores anteriores.
- Las notas N43 y N40 del Control maestro dicen el valor nuevo, el exacto, el valor declarado, la celda de juicio y su valor, y dónde está el rastro.
- Copia legible en `../resultados/recalculo_dependientes_<E>.md`.

## 5. Los sellos del revisor siguen siendo honestos

La huella del vínculo (`huella_fundamento`, I13) incluye:

- `valor_modelo` y la `derivacion` completa, con `recalculo`;
- la fila de evidencia del Control maestro;
- la declaración de la entrada en `fase1_v63.json` (FCF base).

El recálculo cambia las tres. En la copia de `jumbo_g`, de las 566 entradas solo cambia la huella de C46 y C40.

Lo comprobé emulando un sello de C46 como lo escribiría `sellar`, y repitiendo la fase B con C76 = 140 (`evidencia/sello_emulado.txt`):

- el programa no toca la comprobación ni el vínculo;
- la huella sellada y la vigente ya no coinciden, y `comprobar` la da por «desactualizada»;
- un valor recalculado nunca queda sellado sin una revisión nueva;
- sin valor nuevo no se escribe nada, así que un sello vigente sigue vigente.

## 6. Pruebas

| Batería | Resultado |
|---|---|
| `test_entradas_dependientes.py` (copia limpia, sin libros de `jumbo_g`) | **51/51**; la parte de `jumbo_g` se omite y lo dice |
| Ídem con una copia de `jumbo_g` (`MUNGER_JUMBO_G`) | **57/57** |
| Ídem con el código de `1fc9359` (`mixto`) | **8/58**: fallan 50 (el autor dice 49). Las 8 que pasan son controles que no dependen del programa o que no deben cambiar nada |
| `verificar_paquete.sh rapida` sobre `084d2e4` (copia limpia) | **RESULTADO GLOBAL: PASA** (manifiesto 9689 · 0/0/0; F1-SERIES 80/80, redondeo 44/44, acciones 30/30, P-FOSO 72/72, comprobadores 114/114, entradas dependientes 51/51) |
| Sin LibreOffice: `test_auditorias_v2`, `test_estados_v2`, `test_integridad_auditoria_v2`, `test_juicio_objetivo_414`, `test_resumen_v2` | 55/55 · 28/28 · 103/103 · 27/27 · 45/45 |
| Con LibreOffice (una cada vez): `test_cierre_v2`, `test_verificacion_entradas_414` | 55/55 · 33/33 |
| Con LibreOffice: resto | todas pasan (sección «Baterías con LibreOffice») |

**Comprobaciones propias** (`evidencia/`):

- `calculo_independiente_J1.txt`: el cálculo de J1 con fracciones da C46 = 317,902497082 → 317,902, C40 = 255,305397764 → 255,305 y K3a = 10,729. Con C76 = 200 y 160 reproduce también los valores de partida.
- `precio_paso9_libreoffice.txt`: el paso 9 de verdad hasta el precio, con LibreOffice:

  | Copia | Precio de Sí | Ponderado |
  |---|---|---|
  | con declaración | 33,4209 | 36,3394 |
  | sin declaración | 33,3838 | 36,2995 |
- `e2e_diff_recalculo.txt`: lo que se escribe (§1).
- `sello_emulado.txt`: los sellos (§5).
- `expedientes_sin_declaraciones_y_material.txt`: §2.

## Observaciones (no bloquean)

1. **Celdas de juicio de la fase A.** Se admiten (las numéricas son Análisis C56 y Palancas C10), pero el recálculo solo corre en el paso 9. Con una dependencia de la fase A, la fase B y la F1 del paso 7 verían el valor anterior hasta el paso 9. Hoy no hay ninguna: la única es C76, de la fase B. Conviene limitar `celdas_de_juicio` a la fase B o recalcular también tras la fase A antes de que alguien declare una.
2. **Textos que quedan descritos con el valor anterior.** La `derivacion.conciliacion` del registro, la `fuente` de `fase1_v63.json`, el texto original y la `fuente` de la partida K3a siguen describiendo C76 = 160. El estado nuevo está en la marca añadida y en `recalculo_dependiente`. Es transparente, pero quien vuelva a sellar tiene que leer el rastro.
3. **`cambiar_base.py comprobar` confía en el rastro** (`vigente`) para esperar el valor recalculado; no lo recalcula. No es una vía abierta, porque `verificacion_entradas` sí vuelve a calcular la derivación con la C76 del libro y daría una discrepancia, pero el informe de concordancia por sí solo no lo prueba.
4. **El libro de datos.** Recibe C46 y C40 recalculados con la C76 de la fase B mientras su propia C76 sigue siendo la de la preparación. Es así por diseño, para que `comprobar_celdas_v2` siga exigiendo los dos libros iguales fuera de las celdas de juicio, y queda dicho en el rastro.
5. **`datos_v63.md` no se regenera** tras el paso 9. La fase C lo sabe por su entrada; la fase B decide siempre con los valores anteriores a su propio C76, cosa inherente a una dependencia de su propia celda.
6. **La C76 del registro.** En `jumbo_g` la entrada de C76 (hipótesis) sigue con 160 y el fundamento de `jumbo_e`. Tras el paso 9 hay que actualizarla con la fase B y volver a sellar C76, C46 y C40 para la aptitud por entradas. Es tarea del registro, no de este cambio.
7. **Recuento con el código anterior:** 50 de 58 fallan, no 49. No cambia la conclusión.

## Baterías con LibreOffice

Cada una con su propio `flock`, en secuencia, sobre la copia limpia de `084d2e4`. Salidas en `evidencia/baterias/`.

| Batería | Resultado |
|---|---|
| `test_cierre_v2.py` | 55/55 |
| `test_verificacion_entradas_414.py` | 33/33 |
| `test_verificacion_entradas_415.py` | 190/190 |
| `test_entrada_efectiva_415.py` | 62/62 |
| `test_relevo_i19_415.py` | 5/5 |
| `test_vigencia_h5.py` | 59/59 |
| `test_trazabilidad_v2.py` | 78/78 |
| Pruebas de la reparación en modo completo (`test_comprobadores.py`, y `test_pipeline_sintetico.py` con los mismos 30 nombres que la línea de base v2.2) | 114/114 · 30/30 |
| `test_integracion_v64.py` (incluye el cambio de base, que usa `cambiar_base.py`) | 199/199 |

Junto con las seis sin LibreOffice y las tres de la tabla de §6, cubren todas las baterías que importan `pipeline.py`, `cierre_v2.py` o `cambiar_base.py`. No falla ninguna.

## Integración en `examen/expedientes-f1`

Hecha en `/home/user/e_work/wt_expedientes` sobre `origin/examen/expedientes-f1` @ `ee1ca6a`. Antes comprobé que la rama local coincidía con origin y que no había cambios sin confirmar en archivos con seguimiento.

1. **`e031edb`**: `git merge --no-ff 084d2e4`, sin conflictos, conservando el manifiesto del objetivo. Entran solo los seis archivos del cambio.
2. **`23be5de`**: el manifiesto, en un commit propio. Parte del manifiesto anterior y solo cambian las entradas de los seis archivos, con las huellas del contenido confirmado. Son exactamente las del manifiesto de `084d2e4`; solo cambia la cabecera, que describe esta integración.
3. **Push**: `ee1ca6a..23be5de` a `examen/expedientes-f1`.

`git diff --name-only ee1ca6a 23be5de` da solo los seis archivos y el manifiesto: **ningún expediente cambia**. `jumbo_g` tiene las mismas 158 huellas al principio de la revisión y después de integrar.

**`rapida` en copia limpia de `23be5de`** (`git archive` con los 1059 binarios del manifiesto, comprobados por huella; `evidencia/baterias/verif_rapida_23be5de.txt`):

- **Todas las baterías dan PASA**: entorno, piloto, comprobadores 114/114, F1-SERIES 80/80, redondeo 44/44, acciones 30/30, P-FOSO 72/72 y entradas dependientes 51/51 (`jumbo_g` omitido: sus libros no están en Git).
- El manifiesto da 9689 archivos, 0 modificados y 0 ausentes, pero 128 «de más». Por eso **RESULTADO GLOBAL: FALLA (1 bloque)**.
- **Los 128 son los archivos de vinci** que entraron en `examen/expedientes-f1` sin manifiesto entre `4a39e6b` y `ee1ca6a`: `configuracion/cambio_vinci.json` y `vinci/`. Ninguno es de otra carpeta. `ee1ca6a` ya fallaba igual antes de integrar: 9687 entradas y los mismos 128 de más.
- Como el encargo era aceptar solo los archivos del cambio, no los añadí. Aceptarlos en el manifiesto corresponde a quien lleva vinci o a la coordinación.