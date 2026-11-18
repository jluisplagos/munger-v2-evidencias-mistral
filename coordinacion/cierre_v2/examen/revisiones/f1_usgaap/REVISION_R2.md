# Revisión crítica independiente · F1 con US GAAP (ASC 842) · ronda 2 (y última)

- **Revisor:** agente distinto del autor (Claude, modelo Fable 5.2, esfuerzo máximo), 18-nov-2026. No modifiqué la rama ni ningún repositorio. No hice commit.
- **Material:** `jluisplagos/munger-v2`, rama `f1/usgaap` @ `bcb6dc3` (código y pruebas en `a6fc300`; después solo cambian documentos, el manifiesto y el guion de mutaciones: `git diff --stat a6fc300 bcb6dc3`), worktree `/home/user/e_work/wt_usgaap`. Sigue limpio y en `bcb6dc3`.
- **Dónde trabajé:** una copia ligera en `/home/user/e_work/revision_usgaap/copia2/` y carpetas temporales propias (borradas al terminar; la carpeta temporal de la sesión es compartida y solo borré lo mío). LibreOffice siempre con `flock /home/user/e_work/libreoffice.lock`. El expediente real de Zoetis y las declaraciones del examen, solo en lectura.
- **Evidencia:** carpeta `evidencia_r2/` junto a este informe: mis guiones (`*.py`, `*.sh`) y sus salidas (`*.txt`). Los guiones se pueden repetir sobre otro árbol con `COPIA_REVISION=<…>/munger_v2_r1`.
- **Aptitud:** uso supervisado experimental. No apto para decisiones con dinero real. Que pase estas pruebas no lo acredita.

Distingo **hechos** (los reproduje), *interpretaciones* y ***propuestas***.

## Veredicto: CORRECCIONES (acotadas)

**Lo que se pidió en la ronda 1 está hecho y lo he comprobado por mi cuenta.** Las cinco ALTAS quedan resueltas o aplazadas como se dijo: R1-1 y los tres caminos de R1-3 ya no llegan a `concluido` sin condición; D-US2 bis y D-WM hacen lo que decidió la persona; R1-2 se resuelve en la otra rama (lo comprobé en el código fusionado). No hay regresión de valor con NIIF.

**Por qué no es «conforme»:** buscando caminos nuevos encontré **dos por los que un expediente US GAAP llega de extremo a extremo a `concluido`, sin condición y con el valor sobrestimado**. Ninguno lo introdujo el autor en esta ronda:

- **R2-1** sale de la regla que yo propuse en la ronda 1 («fuera» se prueba con una línea del estado de flujos que nombre el arrendamiento). Una línea que nombra el arrendamiento **sin ser el tramo** (deterioro del derecho de uso, resultado por cancelar un contrato) vale como prueba. Y con esa misma línea presente, la declaración veraz queda bloqueada.
- **R2-2** ya existía en la ronda 1 y no lo exploré: un tramo declarado dentro de la fila 14, contrastado con su línea, admite un importe declarado de **cero**.

Son cambios pequeños y dejo guiones que sirven de prueba de aceptación (§5). Añado una regresión NIIF acotada que afecta a una declaración real del examen (Jumbo, §4) y una observación sobre la interpretación 8 (§5, R2-3).

**No afecta a Zoetis ni a Waste Management.** Lo comprobé con el expediente real de Zoetis y con el estado de flujos real de WM (§8): ninguno de los dos tiene esas líneas. Para esas dos empresas la rama sirve tal como está.

No hace falta otra ronda completa de revisión: basta con que quien integre repita los guiones del §5 después de corregir.

---

## 1. Pruebas reproducidas (copia de `bcb6dc3`)

| Prueba | Declarado | Reproducido |
|---|---|---|
| `test_motor_a_f1_usgaap.py` | 246/246 | **246/246** |
| `test_motor_a_f1.py` (NIIF) | 163/163 | **163/163** |
| `test_v631_f1.py` | 29/29 | **29/29** |
| `prueba_pipeline_usgaap.py` (LibreOffice) | 22/22 | **22/22** |
| `probar_libro_v631_usgaap.py` (LibreOffice) | 15/15 | **15/15** |
| `prueba_pipeline_f1.py` (gancho; LibreOffice) | 8/8 | **8/8** |
| `mutaciones_usgaap.py` | 84 de 84 | **84 de 84** |
| `regresion_elis_f1.py` (NIIF, libro real) | 39/39 | **39/39** |
| Fusión con `f1/series-escala` @ `b3998a8` | solo conflicto en el manifiesto | **confirmado** (5 archivos comunes; `git merge-file` a tres bandas limpio en los otros 4). En el código fusionado: 246/246, 163/163 y 55/55 (`test_f1_series_escala.py`) |

No repetí `verificar_paquete.sh completa`: uso el registro del autor (`resultados/verificacion_completa_a6fc300.txt`, RESULTADO GLOBAL: PASA).

**Mis guiones de la ronda 1, sin cambios, contra la capa nueva** (mismo montaje que describe el autor, repetido por mí: `r1_*_contra_r2.txt`): B1–B6 y C1 bloquean (`F1-US-FILAS`); B7 sale condicionado con cota ±12; E6 ya no salta; N1–N3 bloquean; el patrón de la página ve 14 de 14 rótulos (antes 4); 3.000 declaraciones mal formadas, 0 excepciones (antes 326).

---

## 2. Las ALTAS de la ronda 1

### R1-1 · motor B con US GAAP sin declaración · **resuelto**

- **Lectura de L4.** Libro real de Zoetis recalculado por LibreOffice: el lector ligero devuelve `'1165'` (índice de texto compartido) y `_l4_del_libro` devuelve `'US GAAP'` (`capa_r2.txt`, A0).
- **Exigencia** (grupo A, 14 expedientes mínimos): se exige con L4 «US GAAP»; no se exige con «IFRS»; con L4 vacío, «Otro», «U.S. GAAP» o sin libro se exige **solo** en expedientes de la 4.15 (falla en cerrado). Los anteriores a la 4.15 no cambian.
- **De extremo a extremo** (`pipeline_r2.txt`, Y8; el XB3 de la ronda 1): `pendiente_de_datos` en el paso 7 (`F1-NORMA`, `F1-US-DESGLOSE`), sin fase B. Antes: `concluido`. `vigencia()` dice exigido y no utilizable, y el cierre objeta un «concluido».
- **Control NIIF** (Y10): empresa NIIF con el motor B en un expediente de la 4.15 → `concluido`, F1 no se ejecuta.

Resto menor: en un expediente del motor B bloqueado en el paso 7, la línea del informe sigue diciendo «Motor A · F1 … caja base por dos vías sin explicar; perímetro declarado: sin declarar» (Y8, Y9). La ficha no lleva aún el motor y la línea cae en el texto antiguo. Es de presentación.

### R1-3 · ubicación falsa con cita real · **los tres caminos de la ronda 1, cerrados**

Empresa de referencia: caja correcta 68.

| Camino | Capa (`capa_r2.txt`, grupo B) | De extremo a extremo (`pipeline_r2.txt`) |
|---|---|---|
| (i) pasivo dentro de la fila 14, declarado «fuera» citando su línea | DATOS INVÁLIDOS («contradicha»). También con la etiqueta partida de Nike, con la línea solo en el lado «anterior» y con el año como texto | — (lo cubre el PU5 del autor, que reproduje) |
| (i) lo mismo sin `fase1_partes` (mi X1) | utilizable **condicionado**, cota −12/+12 (error +10) | Y1: `concluido` **CONDICIONADA**; cota −3,449/+3,557 mm en el rótulo y en el informe; error +2,695, dentro. Antes: sin condición |
| (ii) «fila_8» falsa con cita genérica (mi X2) | INCOMPLETO («la cita no nombra el arrendamiento») | Y2: `pendiente_de_datos` en el paso 7. Antes: `concluido` |
| (ii) con una frase real de una nota | condicionado, cota −10 (error +10) | — (PU6 del autor) |
| (iii) solo el pasivo en la fila 14 y los dos declarados dentro | bloquea; sin `fase1_partes`, también | Y3: `pendiente_de_datos` en el paso 7 |

**Matriz nueva** (`matriz_r2.txt`): 6 situaciones reales × 20 declaraciones, en tres pasadas (la verdad se ve en las líneas; no se ve; sin `fase1_partes`). El declarante falso prueba cinco formas de citar, todas con texto que está en el expediente.

| Pasada | Utilizables | Con error y **sin condición** | Condicionados con el error fuera de la cota |
|---|---|---|---|
| A · la verdad se ve | 11 de 120 | 2 | 1 |
| B · ninguna línea nombra los tramos | 36 de 120 | 1 | 3 |
| C · sin `fase1_partes` | 24 de 120 | 0 | 2 |

En la ronda 1 eran 6 sin condición (sin `fase1_partes`) y 2 (con ella). **Los 9 que quedan vienen todos de los dos mecanismos nuevos del §5** (línea que no es el tramo; importe cero). Con declaraciones veraces la cota cubre el error en todos los casos, como en la ronda 1.

### R1-4 · D-US2 bis · **aplicada como se decidió**

Pagos 13 y coste 12, los dos tramos dentro de la fila 14 (grupo F; PU7 del autor):

- Se publica el valor de la hoja (69, coste contable) y al lado «contando los pagos, el flujo sin crecimiento cambiaría en −1,000 mm (−1,45 %)». Signo y cifra correctos. No bloquea ni condiciona.
- Vale con dos líneas propias (F1), con las etiquetas mezcladas y partidas de Nike (F2) y con una sola línea neta (F6).
- Si no puede comprobar las dos líneas, bloquea (F4, sin `fase1_partes`).

Dos observaciones menores están en el §7 (R2-5).

### R1-5 · D-WM · **aplicada como se decidió**

- Con las cifras de Waste Management (caja pagada 60/90/101, gasto total 58/73/96): diferencia estimada **8,0 mm al año, 0,349 %** de CFO − capex medio. Es la cifra de la decisión (grupo G).
- La conclusión sale CONDICIONADA (D-US1 + D-WM). Exige C49 = 0.
- **De extremo a extremo** (Y7; el autor no tenía esta prueba): `concluido` CONDICIONADA; la diferencia estimada está en la ficha y en la línea del informe.
- Si se declara «no_publicado» en una empresa cuya Historia sí lleva el principal (fila 17), bloquea `F1-K3a` (G2).

### R1-2 · el cero publicado · aplazado a `f1/series-escala`, **comprobado en el código fusionado**

Zoetis real, principal de 2023 impreso «—»: en `bcb6dc3` sigue inválido; en el código fusionado se acepta (queda «pendiente» la columna, que no bloquea) (`fusion_r2.txt`, M1).

---

## 3. Medias y bajas de la ronda 1

| Hallazgo | Estado | Comprobación propia |
|---|---|---|
| R1-6 · «no_publicada» frente a la página | resuelto | J1, J1b (las dos trampas de la ronda 1 bloquean), J1c (página que no es el estado de flujos → INCOMPLETO) |
| R1-7 · coste y pagos con distinto perímetro (WM) | resuelto | J2: declarado «no comparable», la diferencia no se calcula y la cota se rotula holgada |
| R1-8 · la cota en el informe | resuelto | J3; Y1 y Y7 (dos cifras: % del flujo y % del valor presente en el escenario normal) |
| R1-9 · motor B: avisar del ancla | resuelto | J4 (`F1-US-ANCLA`); PU10 del autor. Resto de presentación: ver R1-1 |
| R1-10 · salida del límite `F1-LIBRO` | **no tocado** (declarado) | sigue abierto: un solo tramo dentro de la fila 14 con su importe veraz termina en `no_entregable · límite del modelo` (D1) |
| R1-11 · vocabulario cerrado de la norma | resuelto | PU11; grupo I. Todos los `fase1_v63.json` del árbol y del examen llevan valores de la lista |
| R1-12 · claves nulas en la ficha NIIF | resuelto | ficha de Elis regenerada: el bloque F1 no lleva `condicionada` ni `us_gaap` |
| R1-13 · tolerancia y mensaje de `F1-US-C49` | resuelto | E6 no salta. Ver R2-6 |
| R1-14 · excepción con series mal formadas | resuelto | tres campañas al azar (3.000 + 3.000 + 3.000, las dos últimas con `fase1_partes` estropeados): 0 excepciones. Efecto lateral: R2-4 |
| R1-15 · K3b no es comprobación independiente | resuelto | J5: «según la hipótesis…», `conforme` vacío; el informe lo dice. Ver R2-3 |
| R1-16 · financieros fuera de la D&A | resuelto | E3; Z2 (Zoetis real: condicionado, +1 mm) |

---

## 4. Regresiones NIIF

| Comprobación | Resultado |
|---|---|
| Diferencial de 424 casos con declaración NIIF (421 sintéticos, incluidas las variantes de L4, + el libro real de Elis con sus 3 declaraciones) | ronda 1 ↔ ronda 2: **424 idénticos**. Base ↔ ronda 2: 13 distintos, los mismos de la ronda 1 (lista cerrada de L4) |
| Declaraciones NIIF **reales** del examen sobre sus libros (Ahold ×3, Elis, Jumbo) | 4 idénticas con los tres códigos (dos de ellas utilizables). **Jumbo cambia** (abajo) |
| `vigencia()` de los expedientes existentes | 38 del árbol y 12 del examen: 0 distintos entre base, ronda 1 y ronda 2 |
| De extremo a extremo, NIIF con el motor B (Y10) | `concluido`; F1 no se ejecuta |
| Elis: regresión, ficha y línea del informe | 39/39; ficha sin claves nuevas; línea del informe idéntica a la registrada |
| 135 formas mal construidas de una declaración NIIF utilizable (`formas_niif_r1_vs_r2.txt`) | 87 idénticas; 41 ya bloqueaban y siguen; 4 pasan de excepción a DATOS INVÁLIDOS; **3 pasan de utilizable a bloqueada** (`normalizacion` con `[]`, `""` o `0`) |

### R2-4 · MEDIA · La comprobación de forma nueva bloquea una declaración real de Jumbo

**Hecho** (`jumbo_real_base_r1_r2.txt`, `examen_real_niif_base_r1_r2.txt`). La declaración F1 de `jumbo_d` (NIIF) lleva dentro de `series` una nota en texto:

```
"pagos_arrendamiento_sin_declarar": "vacío: el estado de flujos los publica en dos líneas (…)"
```

| Código | Resultado |
|---|---|
| base y ronda 1 | bloquea solo `F1-SERIES` (la escala, que arregla `f1/series-escala`) |
| ronda 2 | bloquea `F1-DECLARACION`: «series.pagos_arrendamiento_sin_declarar no es un objeto por año (str)» |
| ronda 2 sin esa clave | como antes |

**Causa.** La corrección de R1-14 no se limitó a evitar excepciones: ahora cualquier entrada de `series` que no sea un objeto es DATOS INVÁLIDOS, también con NIIF. Antes se ignoraba.

**Efecto.** No cambia ningún valor. Pero cuando se integre la otra rama, Jumbo no concluirá hasta que alguien mueva esa nota. El documento del autor dice que NIIF no cambia; para declaraciones bien formadas es cierto.

***Propuesta.*** Mantener el rigor (es coherente con «las claves no reconocidas no se ignoran en silencio») y **mover la nota de `jumbo_d` al campo `nota`**; decirlo en el §1 del documento. Es tarea del examen, no del producto.

---

## 5. Caminos nuevos a `concluido` sobrevalorado

### R2-1 · ALTA (acotada) · Una línea que nombra el arrendamiento sin ser el tramo sirve de prueba de «fuera», y bloquea la declaración veraz

**Situación.** La empresa no publica los tramos. La variación del pasivo va dentro de «Accrued and other liabilities» (fila 14): el libro da 78 y lo correcto es 68. El estado de flujos lleva además, entre los ajustes, una línea como «Loss on lease termination» o «Impairment of operating lease right-of-use assets». *Interpretación:* son líneas habituales en empresas con muchos locales alquilados (comercio, restauración); no lo he medido.

**Hechos** (`capa_r2.txt`, grupo C; `pipeline_r2.txt`):

| Declaración | Capa | De extremo a extremo |
|---|---|---|
| **Veraz**: los dos tramos «no_publicada» | bloquea: «la página muestra una línea del arrendamiento operativo (…): donde la empresa publica la línea manda el dato; **declara su ubicación**» (C1) | Y4h: `pendiente_de_datos`, paso 7 |
| Los dos «fuera» citando esa línea | utilizable, **sin condición**, 78 (+14,7 %); contraste «contrastada/contrastada»; K3b «una vez (contrastado)» (C3, C4) | **Y4: `concluido` sin condición**; flujo +2,695 sobre el control; valor ponderado 22,919 frente a 22,562 (+1,6 %) |
| Amortización «fuera» con la línea de deterioro; pasivo «no_publicada» | condicionado; la cota del pasivo cubre el error (C2) | — |

El error también puede ir a la baja (C5: −10, sin condición).

De 14 rótulos habituales que **no** son un tramo (los escribí yo), la capa acepta 10 como línea del tramo (C6): deterioros, cancelaciones, modificaciones, incentivos, abandono, costes de salida.

**Causa.** El contraste comprueba que la línea citada nombra el arrendamiento y que la fase 1 no la sumó. No puede saber si esa línea **es** el tramo. El mismo patrón hace las dos cosas: bloquea el «no_publicada» veraz (el autor lo declara como límite 3, «el lado seguro») y acredita el «fuera» falso (no declarado). El mensaje del bloqueo empuja al declarante hacia la segunda.

*Interpretación.* Es el mismo efecto que R1-3 (i), con un disparador más estrecho: hace falta que el estado de flujos tenga una de esas líneas. La regla la propuse yo; el autor la implantó tal cual.

***Corrección propuesta*** (mínima):
1. Tratar como **ajenas a los tramos** las líneas que nombran el arrendamiento junto a un término de otra cosa: *impairment, write-off, termination, modification, abandonment, exit, incentive, sale-leaseback, gain, loss* (y sus equivalentes en español).
2. Una línea ajena no hace saltar «manda el dato» frente a «no_publicada» (cierra el límite 3 en los casos habituales) y **no vale como cita de una ubicación**.
3. Más robusta, si se quiere: con los dos tramos «fuera» en líneas propias, comprobar que sus cifras impresas suman coste − pagos; si no, «sin contrastar».

**Aceptación:** `capa_r2.py C` (C1 utilizable y condicionado; C2–C4 ya no «contrastada»); `pipeline_r2.py Y4 Y4h` (Y4h `concluido` CONDICIONADA; Y4 no `concluido` sin condición).

### R2-2 · MEDIA · Un tramo contrastado dentro de la fila 14 admite un importe declarado de cero

**Situación.** «Operating lease liabilities» es una línea propia que la fase 1 sumó en la fila 14 (10 al año). Es el caso frecuente.

**Hechos** (`capa_r2.txt`, grupo D; `pipeline_r2.txt`; `fusion_r2.txt`):

| Declaración | Resultado |
|---|---|
| «fila_14» con su importe (10): veraz | `no_entregable · límite del modelo` (`F1-LIBRO`): ningún libro lo retira (R1-10) |
| «fila_14» con importe **0** | utilizable, **sin condición**, 78 (+14,7 %); «contrastada»; K3b «contrastado» (D2). **Y5: `concluido` sin condición**, +1,6 % de valor |
| lo mismo sin `fase1_partes` | condicionado, pero la cota por abajo es 0 y no cubre el error (D2b) |
| lo mismo en el código fusionado, con el cero declarado por `cero_comprobado` y una frase cualquiera de la página (el cero queda «pendiente», que no bloquea) | utilizable, sin condición, 78 (M2) |

**Causa.** La ubicación se contrasta con la línea; el importe no. La capa tiene a mano la cifra impresa de esa línea (`fase1_partes`, campo `impreso`) y no la compara. Con importe cero no se retira nada, `F1-LIBRO` no salta y la variación del pasivo se queda en la reinversión.

*Interpretación.* Hoy hace falta que un «0» suelto esté en una página, cosa rara en un 10-K. Al integrar `f1/series-escala` basta una frase de ocho palabras: por eso conviene cerrarlo **antes de fusionar**. Y como la declaración veraz no tiene salida, hay incentivo.

***Corrección propuesta.*** Si la línea contrastada es propia (solo nombra el arrendamiento), el importe declarado tiene que ser su cifra impresa en cada año; si no, DATOS INVÁLIDOS. Si es una línea mezclada, el importe no se puede comprobar: condicionar, con el pago o el coste como cota.

**Aceptación:** `capa_r2.py D` (D2 bloquea; D1 igual que hoy); `pipeline_r2.py Y5`; `fusion_r2.py` (M2 bloquea); `matriz_r2.py` (0 «ERROR SIN CONDICIÓN» y 0 «FUERA DE COTA»).

Del mismo tipo y sin remedio sencillo: un importe inflado dentro de la D&A (D3: 15 declarados, 10 de verdad → +5 sin condición). La línea es mezclada y no hay cifra con que comparar. Es el mismo límite que tiene NIIF con `da_rou`; debería constar entre los límites.

### R2-3 · MEDIA · Interpretación 8: la amortización financiera «dentro de la fila 8» por omisión no mira una línea contraria que está a la vista

**Hechos** (grupo E). Principal financiero 5 en C49; la D&A (20) **no** lleva esa amortización; se declara `da_rou` = 5 sin decir ubicación:

- E1: utilizable, sin condición, 73 frente a 68 (+5). K3b: «contrastado con las líneas que la fase 1 sumó».
- E2: igual **aunque el estado de flujos muestre** «Amortization of finance lease right-of-use assets» como línea propia que la fase 1 no sumó.
- E3 (declarada «fuera_de_la_fila_8» con esa línea): 68, correcto.

*Interpretación.* El caso por omisión es razonable: la norma pide presentar esa amortización como la de activos similares (lo cito de memoria, 842-20-45-4(a); no lo he vuelto a contrastar). Lo que no encaja con «manda el dato» es E2, y que K3b diga «contrastado» de algo que no se contrastó. En el examen pesa poco: Zoetis, 1 mm sobre 2.795.

***Propuesta.*** Si una línea de la conciliación nombra la amortización de arrendamientos financieros y no está sumada en la fila 8, DATOS INVÁLIDOS («declárala fuera»). Y no decir «contrastado» mientras haya `da_rou` financiero sin línea que lo nombre.

---

## 6. Las interpretaciones del §9 del autor, frente a lo que decidió la persona

| Nº | Interpretación | Juicio |
|---|---|---|
| 1 | D-US2 bis también con dos líneas propias | **Se ajusta.** La decisión era no bloquear y enseñar; el libro no puede retirar nada. Comprobado (F1) |
| 2 | Si no se pueden comprobar las dos líneas, bloquea | **Se ajusta.** La decisión pone la comprobación como condición previa (F4, B-iii3) |
| 3 | D-WM se declara por expediente; exige C49 = 0 y las dos series | **Se ajusta.** Reproduce los 8 mm y el 0,35 % de la decisión. No comprueba que la empresa de verdad no desglose, pero el resultado sale condicionado y con la diferencia a la vista |
| 4 | Lo que no se puede contrastar se usa y condiciona, con la cota del caso contrario | **Se ajusta** (es lo que pedí). Salvedad: con importe cero la cota vale cero (R2-2) |
| 5 | «Otro» cuenta como norma sin determinar | Razonable; es un límite (§7) |
| 6 | Tolerancia de `F1-US-C49` | **Se ajusta.** Ver R2-6 |
| 7 | A0 con amortización operativa en la fila 8 bloquea siempre, etc. | Sin objeción. No la ataqué más allá de la batería del autor |
| 8 | La amortización financiera por omisión no se condiciona | **No viene de ninguna decisión.** Razonable como omisión; corregir lo de R2-3 |

---

## 7. Los límites nuevos, y otras observaciones menores

**«Otro» en L4 no concluye** (grupos A e I; Y9). Confirmado: con los motores A y B un expediente de la 4.15 con «Otro» termina en `pendiente_de_datos` en el paso 7. Fallar en cerrado es lo correcto: F1 no tiene regla para otras normas. Dos reparos:
- El estado sugiere que falta un dato, y no hay dato que lo arregle sin mentir sobre la norma. Sería más exacto `no_entregable · límite del modelo`.
- Con el motor B esto es nuevo (antes concluía). Ningún expediente del examen lleva «Otro» (todos dicen IFRS o US GAAP). Si entra una empresa así, hará falta una decisión de la persona.

**Falsos positivos del patrón amplio** (límite 3). Confirmados (C1, Y4h). No son «el lado seguro»: la misma línea abre el camino contrario (R2-1). La propuesta del autor (declarar las líneas que no son tramo, condicionando) va en la dirección de mi corrección; con una lista de términos no hace falta declaración.

**Otras, de gravedad baja:**

- **R2-5 · D-US2 bis.** (a) Si se declara la línea neta, «cuánto cambiaría» usa esa cifra aunque contradiga pagos − coste: declarada a 0 con pagos 17 y coste 12, enseña «+0,000 mm» cuando son −5 (D4). Bastaría comparar las dos. (b) Si no se puede calcular (coste no comparable y sin línea neta), publica igual, sin condición, con el texto «NO se puede calcular» (F5); la decisión pedía enseñar la diferencia.
- **R2-6 · `F1-US-C49` «explicado».** Una partida declarada en `conciliacion_fcf_base` explica cualquier diferencia, también por defecto: C49 = 0,01 con principal publicado de 10 pasa con un AVISO (H2; +9,99 sin condición). El aviso dice «compruébese que no son pagos operativos», que es el riesgo contrario. Es el mismo criterio que K3a ya aplicaba; pido solo que el texto distinga el sentido.
- **Límite 5 del autor.** El resultado guarda la huella de las líneas examinadas pero `vigencia()` no la mira, y `fase1_partes` no está en el material fijo del cierre. Convendría comprobarla.

---

## 8. Zoetis y Waste Management, con sus datos reales

**Zoetis** (`zoetis_real_r2.txt`; expediente real del examen `zoetis_t1b`, con su `fase1_partes`, su texto y su libro recalculado; solo lectura):

- La capa lee bien las líneas reales. Ninguna de las filas 8 y 14 nombra el arrendamiento.
- Los dos tramos «no_publicada» (página 70) → hipótesis D-US1, **condicionada, cota −64,2/+63,5 mm (±2,3 % del flujo)**. C49 = 1 coincide con el principal publicado (2/1/—).
- Citar por error la página de la nota (89) da INCOMPLETO, como debe.
- **Lo que hoy le impide concluir no es de esta rama:**
  1. `F1-K3a`: la fase 1 real dejó vacía la fila 17 de 2025 (la nota dice 2). Diferencia sin explicar: −0,666.
  2. `F1-LIBRO`: el libro aún no lleva la declaración (se relanza desde el paso 2).
  3. El «—» de 2023, hasta integrar `f1/series-escala`.
- **Si la fase A eligiera el motor B** (`zoetis_real_motor_b_r2.txt`): con el libro tal cual, F1 termina en `no_entregable · límite del modelo` (`F1-US-PUENTE`). La fila 23 lleva 248 de pasivo por arrendamiento **operativo** y el puente lo restaría además del EBIT (deuda del libro 9.297; coherente 9.049). Declarar que la fila 23 no lo lleva no cuela: lo contradicen las líneas reales de la fase 1 (DATOS INVÁLIDOS). La salida es corregir la fase 1 para que la fila 23 no lleve el pasivo operativo (el financiero, 7, ya está en la deuda). Sin declaración F1: `pendiente_de_datos`.

**Waste Management.** Su estado de flujos real de 2025 (texto extraído del informe anual: página 161 del PDF, la 78 impresa) no tiene ninguna línea de arrendamiento en la explotación: irá por D-US1 más D-WM, condicionada. No hay expediente todavía; no he ejecutado su fase 1.

Ninguna de las dos tiene líneas del tipo de R2-1 ni un tramo propio en la fila 14 (R2-2).

---

## 9. Lo que no hice, y límites de esta revisión

- No repetí `verificar_paquete.sh` (ni `rapida` ni `completa`); me apoyo en el registro del autor para lo que no es de F1.
- En el código fusionado solo probé la capa (baterías y dos casos), no el pipeline.
- R2-3 no lo llevé de extremo a extremo: nada posterior a la capa lo examina.
- Mis rótulos de líneas «que no son un tramo» los escribí yo; no los saqué de informes concretos.
- No probé Excel real ni la fase 1 de WM.
- No he revisado `f1/series-escala` (lo hace otro agente); solo su efecto sobre esta rama.
- La cita de 842-20-45-4(a) en R2-3 es de memoria.

## Anexo · Evidencia (`evidencia_r2/`)

| Archivo | Qué es |
|---|---|
| `capa_r2.py` → `capa_r2.txt` | casos propios sobre la capa: A (R1-1), B (R1-3), C (R2-1), D (R2-2), E (R2-3), F (D-US2 bis), G (D-WM), H (C49), I («Otro»), J (medias) |
| `pipeline_r2.py` → `pipeline_r2.txt` | 11 casos de extremo a extremo (Y0–Y10), 10 min con LibreOffice |
| `matriz_r2.py` → `matriz_r2.txt` | verdad × declaración × forma de citar, tres pasadas |
| `zoetis_real_r2.py`, `zoetis_real_motor_b_r2.py` → `zoetis_real_r2.txt`, `zoetis_real_motor_b_r2.txt` | la capa sobre el expediente real de Zoetis (motor A y, por si acaso, motor B) |
| `fusion_r2.py` → `fusion_r2.txt` | código fusionado con `f1/series-escala`: M1 (Zoetis «—») y M2 (importe cero) |
| `examen_real_worker.py`, `jumbo_real_worker.py` → `examen_real_niif_base_r1_r2.txt`, `jumbo_real_base_r1_r2.txt` | declaraciones NIIF reales del examen con los tres códigos |
| `formas_niif_worker.py` → `formas_niif_r1_vs_r2.txt` | 135 formas mal construidas de una declaración NIIF |
| `diferencial_niif_*.txt`, `vigencia_expedientes_base_r1_r2.txt`, `declaraciones_existentes_bien_formadas.txt` | diferenciales NIIF y vigencia |
| `fuzz_r2.py` → `fuzz_r2.txt`; `r1_fuzz_contra_r2.txt` | declaraciones y `fase1_partes` mal formados al azar |
| `correr_guion_r1.py` → `r1_*_contra_r2.txt` | mis guiones de la ronda 1, sin cambios, contra la capa nueva |
| `test_*.txt`, `prueba_pipeline_*.txt`, `probar_libro_v631_usgaap.txt`, `mutaciones_usgaap.txt`, `regresion_elis_f1.txt`, `lo_resumen.txt` | baterías del autor reproducidas |
| `ayudas2.py`, `correr_lo_r2.sh` | carga de las ayudas de la batería del autor; orden de las pruebas con LibreOffice |

Los diferenciales usan además el código antiguo, sacado con `git archive 1694f08` y `git archive 34b68fc` (carpeta `personaje_v2/scripts`), y los guiones de la ronda 1 están en `evidencia/`.

Para repetir un guion sobre un árbol corregido: `COPIA_REVISION=<árbol>/munger_v2_r1 python3 -B capa_r2.py SALIDA.txt C D E` (los de LibreOffice, con `flock /home/user/e_work/libreoffice.lock`).
