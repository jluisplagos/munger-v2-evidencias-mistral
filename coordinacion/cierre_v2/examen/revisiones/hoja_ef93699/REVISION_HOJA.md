# Revisión crítica independiente · hoja resumen en lenguaje llano (`hoja_resumen.py`)

**Veredicto: CORRECCIONES.**

- **Las cifras están bien.** La sensibilidad a la tasa se calcula correctamente, solo cambia la tasa y el 9 % reproduce exactamente el precio de Sí oficial. Lo he recalculado por dos caminos propios en todos los motores y plantillas disponibles.
- **La hoja no cuenta lo mismo que la ficha oficial cuando la ficha no concluye o concluye con condiciones.** Pone un «precio de Sí» en el veredicto aunque la ficha diga que no hay precio objetivo o que esa cifra «no es utilizable», y calla el motivo (hallazgo 1).
- **La hoja se genera con material que el sistema oficial ya no da por vigente**: aprobación retirada, F1 bloqueando, `fase_c.json` cambiado después de la auditoría, ficha sin cierre registrado. En esos casos devuelve «OK» y `--comprobar` dice «HOJA VIGENTE» (hallazgos 2 y 4).
- **Calla la aptitud por entradas y F1**, y afirma algo falso sobre la ficha («es anterior a ese bloque») (hallazgo 3).
- **No es lenguaje llano**: es el texto del personaje, con su jerga, más una tabla sin definiciones (hallazgo 6).

No debe entregarse como material de estudio hasta corregir los hallazgos 1 a 4. Los demás se pueden corregir en la misma ronda.

- **Revisado:** rama `examen/hoja-resumen` @ `ef93699` (sobre `1694f08`): `scripts/hoja_resumen.py`, `scripts/README_hoja_resumen.md` y `pruebas/test_hoja_resumen.py`. Sus huellas son las del manifiesto.
- **Revisor:** agente distinto del autor (Fable 5.2, esfuerzo máximo). 18-nov-2026.
- **Método:** copias bajo `/tmp/claude-0/revision_hoja/`, borradas al terminar. Ningún repositorio modificado: `wt_hoja` sigue en `ef93699` sin cambios. LibreOffice siempre bajo `flock /home/user/e_work/libreoffice.lock`.
- **Evidencia:** `/home/user/e_work/revision_hoja/evidencia/` (archivos de texto, unos 600 KB; índice en el apartado 7).

El documento de la reorientación (§7, criterios K5 y K9) no está en el repositorio. He medido la hoja contra el encargo del coordinador y contra las reglas del propio paquete (Anexo C §C.6–C.7, `cierre_v2.py`, `ficha.py`, `informe.py`).

---

## 1. Lo que está bien (comprobado)

1. **Batería del autor**: `python3 -B pruebas/test_hoja_resumen.py` en una copia → **60/60 pasan** en 54 s (`evidencia/01_bateria_test_hoja_resumen.txt`). No la envolví en `flock`: cada llamada a LibreOffice ya va bajo el cerrojo común dentro del script (envolverla la bloquea, hallazgo 11).
2. **Solo cambia la tasa.** La copia que hace la hoja difiere del libro evaluado en una sola parte del `.xlsx` y, dentro de ella, en una sola celda: `Análisis!C56` (0,09 → 0,1). Comprobado en siete libros: V6.3 motor A y B, V6.4, V6.4.1 y V6.3.1 F1 (`cifras/copia_solo_C56.txt`).
3. **La tabla 7–11 % es correcta.**
   - Recálculo propio con LibreOffice (herramienta mía, sin `v63_xml.py`, `recalc.sh`, `leer_resultados.py` ni `precio_de_si.py`; precio de Sí por bisección): **18 casos**, incluidas las cinco tasas de Vidrala 4.14 (V6.4) y de Viscofan 4.14 (V6.4.1). Diferencia máxima con la hoja: 2,3·10⁻¹³ (`cifras/indep_comparacion.txt`).
   - Cálculo sin LibreOffice, descontando yo los flujos del libro oficial: **10 libros × 5 tasas = 50 filas** (V6.3 motor A y B, V6.3.1 F1). Diferencia relativa máxima 4,9·10⁻¹⁵ (`cifras/dcf_puro.txt`).
   - El libro de Hermès trae su propia tabla «tu r ±2 puntos»: 1.207,74 al 7 % y 651,39 al 11 %. Son las cifras de la hoja.
4. **El 9 % reproduce exactamente el precio de Sí oficial** en los 11 expedientes reales y en los 7 sintéticos en que la hoja se genera con código 0.
5. **F1 no se rompe al recalcular.** En un libro V6.3.1 F1 con perímetro declarado (A1_sin_ROU), la copia conserva el perímetro y las 24 guardas de `motor_a_f1.py` dan lo mismo al 7, al 9 y al 11 % (`cifras/f1_guardas_por_tasa.txt`). El problema con F1 está en otra parte: hallazgo 2.
6. **No toca el expediente** (solo añade sus dos archivos) y **no altera la vigencia oficial**: con la hoja dentro del expediente, `cierre_v2.motivo_vigencia` sigue dando «vigente» (`vigencia/vigencia_A6_A7.txt`, paso 2).
7. Rechaza bien: expediente sin terminar, ficha provisional, libro distinto del de la ficha, ficha distinta de la del cierre vigente, `no_entregable` sin cierre previo y `modelo_no_aplicable`.
8. `--comprobar` detecta el cambio de cualquier archivo leído (ficha, informe, precio, resultados, fase C, estado, libro).

Expedientes usados (copias):

| Expediente | Plantilla · motor | Estado oficial | Resultado de la hoja |
|---|---|---|---|
| Hermès, Aarsleff, Nike, Rational, Vidrala (`empresas_v2`) | V6.3 · A | concluido · Vigilar · esperar | código 0 |
| Viscofan (`empresas_v2`) | V6.3 · B | concluido · Vigilar · esperar | código 0 · «no firme» |
| Vidrala 4.14, Viscofan 4.14 | V6.4 / V6.4.1 · B | concluido · esperar · objetivo condicionado | código 0 |
| Elis 4.14 | V6.3 · A | **pendiente_de_datos** | código 0 (hallazgo 1) |
| Vidrala 4.12 y 4.13 «bloqueo» | V6.4 · B | **pendiente_de_datos** (objetivo bloqueado) | código 0 (hallazgo 1) |
| EmpresaX_sobrevive (sintético) | V6.3 · A | **concluido · Sí · comprar** | código 0 |
| EmpresaX_favorable y _sin_base (sintéticos) | V6.3 · A | **pendiente_de_investigacion** | código 0 (hallazgo 1) |
| EmpresaX_sin_C34 (sintético) | V6.3 · A | **pendiente_de_datos** | código 0 (hallazgo 1) |
| EmpresaX_repetir, _limite (sintéticos) | V6.3 · A | no_entregable, modelo_no_aplicable | código 3 (bien) |
| P6 (sintético) | **V6.3.1 F1** · A, A1_sin_ROU | concluido · esperar | código 0 |
| P8 y P10 (sintéticos) | V6.3.1 F1 · A | **no_entregable, F1 bloquea, aprobación retirada** | código 5 con hoja escrita / **código 0** (hallazgo 2) |

Los sintéticos los produce el pipeline real con los agentes simulados de las baterías del paquete (`test_pipeline_sintetico.py`, `prueba_pipeline_v631.py`); no he escrito a mano ninguna de sus fichas. Las únicas alteraciones a mano son las de las pruebas A1 a A9 de los hallazgos 2, 3 y 4, que lo dicen en cada caso. En el repositorio no hay ningún expediente real con conclusión favorable ni ninguno cerrado con la V6.3.1 F1: por eso los sintéticos. Detalle de cada estado oficial: `sinteticos/fichas_oficiales_resumen.txt`.

---

## 2. Hallazgos

### 1 · ALTA · Sin conclusión oficial, la hoja pone un «precio de Sí» en el veredicto y calla el motivo

La línea de veredicto toma el precio de Sí y la zona de `precio.json` (líneas 466 y 482–483), no de la decisión de la ficha. Nunca lee `causa_si_no_concluido`, `decision.precio_objetivo`, `decision.condicion`, `objetivo`, `insumos_decision_cartera.fundamento` ni `alcance`. El informe oficial sí los pone en su primer párrafo.

Evidencia:

- **Elis 4.14 (real, auditoría APROBADO).** Ficha: `pendiente_de_datos`, acción `null`, `precio_objetivo` `null`. Causa: «…frente a 7,30 € de la hoja, que por el supuesto F1 **no es utilizable**». Fundamento: «…su precio de Sí **no es una conclusión utilizable**; la escalera se informa como zona».
  Hoja: «**Veredicto del personaje** — pendiente de datos · cubo **Vigilar** · acción **sin acción (estado pendiente de datos)** · precio de Sí **7,30 €** (precio actual 24,18 €, caro…)», tabla con precios de Sí del 7 al 11 %, «Conclusión **firme**» y «reproduce exactamente el precio de Sí **oficial**: sí». La causa no aparece. La frase del personaje que lo avisa (tesis, frase 4: «…así que ese precio no es utilizable…») queda fuera por la regla de selección.
- **Vidrala 4.13 y 4.12 «bloqueo» (reales).** Ficha: `objetivo.estado_del_objetivo = bloqueado`, `precio_objetivo_emitido = null`. Hoja: «precio de Sí **56,02 €**».
- **EmpresaX_favorable (sintético).** Ficha: `pendiente_de_investigacion`, causa «incertidumbre_no_acotada» (la comprobación conjunta no se supera). Hoja: «precio de Sí **18,12 €** (precio actual 16,00 €, **cumple: en el precio de Sí o por debajo**)». El Anexo C §C.7 manda decir aquí «Sin conclusión de compra: …».
- **EmpresaX_sin_C34 (sintético).** Causa oficial: «sin la liquidez no puedo descartar que la deuda apriete». Hoja: «cumple…»; la causa no aparece.
- **Objetivo condicionado.** Vidrala 4.14: `objetivo.provisional = true` y `decision.condicion` = «…objetivo condicionado (provisional)… sin fundamento suficiente». La línea de veredicto dice «precio de Sí **56,00 €**» sin más. En Viscofan 4.14 la única frase del personaje que lo dice (tesis, frase 4) tampoco entra.
- Con una ficha «No · descartar» y zona favorable, la línea saldría «cubo **No** · acción **descartar** · precio de Sí 18,12 € (…**cumple**…)» (simulación de presentación con `componer`: `texto/presentacion_No_descartar.txt`).

Corrección:

1. El veredicto sale solo de la ficha. Precio de compra = `decision.precio_objetivo` (y `objetivo.precio_objetivo_emitido`). Si es `null`: «la ficha no da precio de compra».
2. Si el estado no es `concluido`: primera línea «**Sin conclusión**: {estado en llano}» y debajo `causa_si_no_concluido.detalle` y `que_lo_resolveria`, limpios de referencias. La tabla de la tasa pasa a llamarse «lectura de la hoja de cálculo (no es una conclusión)» y no se usa la palabra «firme».
3. Siempre que existan: `decision.condicion`, `objetivo` (bloqueado, condicionado, provisional), `fundamento`, `alcance.aviso` y la marca «con datos de etapa 1 incompletos».
4. Quitar «oficial» de la línea de comprobación cuando la ficha no emite precio.

### 2 · ALTA · La hoja se genera con material que el sistema oficial no da por vigente (incluido F1 bloqueando)

`leer_expediente` (líneas 310–348) usa una comprobación propia, más débil que la oficial (`cierre_v2.motivo_vigencia`). No mira la auditoría, el material auditado, `aprobaciones_retiradas.json`, `ficha.cierre` ni F1. Su señal de «cerrado» es `estado_pipeline.json → fin`, que el pipeline escribe en el paso 14 y **no borra nunca** (`pipeline.py`, línea 1232 es su única escritura).

Evidencia:

- **P10 · F1 bloquea y la aprobación está retirada → código 0.** Expediente V6.3.1 F1 cerrado (P6). Cambio la declaración F1 después del cierre (el mismo cambio que la prueba P8 del paquete) y relanzo con `--desde 12`. Estado oficial: `no_entregable`, cubo y decisión vacíos, causa «motor A · F1: el resultado del motor A no se usa para una conclusión · F1-LIBRO», `motor_a_f1.utilizable_para_conclusion = false`, `aprobaciones_retiradas.json` presente, salidas archivadas.
  Hoja: «OK», «precio de Sí **19,61 €**», fila «8 % | 23,25 € | … | **cumple**», «reproduce exactamente el precio de Sí oficial: **sí**». `--comprobar` → «**HOJA VIGENTE**» (`hojas/V631_P10_desde12.*`, `vigencia/v631_p10_salida.txt`).
- **P8** (lo mismo con `--desde 7`): la puerta también se abre; acaba en código 5, pero deja la hoja escrita con «precio de Sí 19,61 €», que es el del cierre retirado.
- **A1/A6 · `fase_c.json` cambiado después de la auditoría (Vidrala 4.14).** Vía oficial: «el material cambió después de la auditoría (fase_c.json): la aprobación no vale para la versión nueva». Hoja: código 0 y texto alterado en la página («Pasaría a **No**: Nada me haría pasar a No…», «Pasaría a **Sí**: … compraría hoy a cualquier precio por debajo de 120 €», predicción 1 cambiada). Solo deja un aviso al pie para la predicción. Después, `--comprobar` → «HOJA VIGENTE» (`vigencia/vigencia_ataques.txt`, `vigencia/vigencia_A6_A7.txt`).
- **A9 · tesis cambiada (Hermès).** La hoja abre con «Hermès es una compra clara a cualquier precio. La compraría hoy mismo. No veo riesgos.», código 0, y un aviso en la última línea.
- **Los expedientes originales de `empresas_v2/` no son vigentes para la vía oficial.** Comprobados Hermès, Nike y Viscofan: «no consta la respuesta de auditoría aprobada…; hace falta una auditoría nueva». Los otros tres tampoco tienen `cierre_vigente.json`. La hoja se genera igual en los seis, y la batería usa a Hermès como ejemplo de «expediente cerrado».
- **A4** · una ficha provisional sin la clave `provisional`, sin `cierre` y sin `cierre_vigente.json` se acepta.
- **Hoja huérfana.** Cuando la vía oficial retira la aprobación archiva `ficha.json`, `informe.md` y `cierre_vigente.json`; `hoja_resumen.md` se queda en la carpeta diciendo «concluido · Vigilar · esperar · 56,00 €». `--comprobar` lo detecta (código 4), pero nadie lo ejecuta solo, y su consejo («Regenerarla») no vale: lo correcto es retirarla.
- La cabecera dice «si la ficha cambia, esta hoja se regenera»: no se regenera sola.

Corrección:

1. Puerta única: `cierre_v2.motivo_vigencia(...)` tiene que dar «vigente», con `cierre_vigente.json` y `ficha.cierre.auditoria = APROBADO`. Si F1 se exige (`motor_a_f1.vigencia`), tiene que estar vigente; si no es utilizable, la hoja es de «sin conclusión» (hallazgo 1) o no se genera.
2. Leer los textos de material ligado a la aprobación: `cambiaria_de_cubo`, `condiciones_revision` y predicciones de la **ficha**; tesis y tesis inversa del **libro evaluado**. Si `fase_c.json` difiere, no generar (código 3), no un aviso al pie.
3. Expedientes sin cierre registrado: no generar por defecto; como mucho con una opción expresa y un rótulo arriba «ANTECEDENTE · sin cierre vigente».
4. `--comprobar` repite la puerta completa, no solo las huellas. Si faltan las salidas oficiales, dice «retirar la hoja».
5. Que la retirada oficial se lleve la hoja al historial (o escribir la hoja fuera del expediente). Tocar `cierre_v2.py` es una decisión aparte: la dejo señalada.
6. Cabecera: «Vale solo mientras la ficha {huella} siga siendo la oficial. Compruébalo con `--comprobar`.»

### 3 · ALTA · Aptitud: calla «apto por entradas: no» y F1, afirma algo falso y puede proclamar «apto para dinero real»

`aptitud()` (líneas 412–421) solo mira `ficha.aptitud_de_uso`. Ese bloque solo existe en las plantillas V6.4 y V6.4.1 (`ficha.py`, líneas 464–480). En V6.3 y V6.3.1 F1 la ficha lleva `verificacion_entradas` y `motor_a_f1`, que la hoja no lee.

Evidencia:

- **EmpresaX_sobrevive (concluido · Sí · comprar).** Ficha: `apto_por_entradas = false`, «ninguna entrada financiera está verificada», 258 entradas materiales sin comprobar. El informe oficial lo pone arriba: «Entradas financieras: apta por entradas: no… Apta para dinero real: no». La hoja dice solo: «experimental; no apto para dinero real — la ficha no declara la aptitud de uso, **es anterior a ese bloque**: no se presume ninguna». La ficha se generó en el momento, con el pipeline actual: la frase es falsa.
- Lo mismo en P6 (V6.3.1 F1): la ficha lleva `motor_a_f1` (perímetro A1_sin_ROU, aviso V-F1k) y la nota «motor A sin validar: F1»; la hoja solo dice «plantilla V6.3.1 F1» en la última línea.
- La ficha real de Ahold (4.15) tiene esa forma: sin `aptitud_de_uso`, con `apto_por_entradas = false`. Es la que tendrán los expedientes F1 en curso.
- **A3** · en un expediente sin cierre registrado, una ficha editada a mano produce: «cubo **Sí** · acción **comprar** · … (…caro…) · **la ficha declara apto para dinero real**», código 0 y «HOJA VIGENTE».

Es el mismo defecto que la revisión externa señaló en las salidas V6.3 («aptitud por entradas omitida»), ahora en la hoja.

Corrección:

1. La aptitud se compone de los tres bloques. Texto fijo: «**Experimental: no vale para decidir con dinero real.**» Y debajo, cuando existan: «Datos de entrada verificados: no ({resumen})» y «Motor A · F1: {rótulo de la ficha}».
2. Quitar «es anterior a ese bloque». Si no hay ningún bloque: «la ficha no dice nada sobre la aptitud; no se presume ninguna».
3. Quitar la rama que imprime «la ficha declara apto para dinero real». Hoy `ficha.py` fija ese valor en `false`; una hoja no debe convertir un `true` en un titular. Si algún día hay una decisión humana registrada, que se lea de ese registro.

### 4 · ALTA · La hoja se escribe aunque falle su propia verificación, y después `--comprobar` la da por vigente

`generar` escribe los dos archivos (línea 624) y solo después devuelve 4 (frase sin origen) o 5 (no reproduce el oficial).

Evidencia:

- **A2** · `precio.json` alterado en Vidrala 4.14 (precio 90,10 → 50,00; zona → cumple). Código 5, pero la hoja queda escrita con «(precio actual **50,00 €**, **cumple: en el precio de Sí o por debajo**)» en el veredicto y el «**NO**» en la línea 38. Después `--comprobar` → «HOJA VIGENTE», código 0.
- **P8** · queda escrita la hoja de un expediente `no_entregable`.

Corrección: con código 4 o 5 no escribir (y borrar una hoja anterior, o apartarla con otro nombre). `--comprobar` debe fallar si `reproduce_oficial` no es verdadero en el `.json`.

### 5 · MEDIA · La selección mecánica de frases deja fuera las salvedades y a veces elige frases vacías

Regla (líneas 244–271): de la tesis, frases 1, 2 y última; de la tesis inversa, la primera de 6 palabras o más y la última; de «a No», la primera.

Evidencia (`texto/seleccion_frases.txt`, diez expedientes reales):

- De la tesis entran 3 de 4–5 frases; de la tesis inversa, 2 de 6–11.
- La frase que se salta en la tesis suele ser la salvedad. Hermès, frase 3: «Pero el capital invertido crece más que el beneficio… y Asia-Pacífico… se ha frenado». Elis, frase 4: «…ese precio no es utilizable». Viscofan 4.14, frase 4: «…objetivo condicionado…».
- La «última frase de la tesis» no siempre es el veredicto (Aarsleff, Viscofan 4.14).
- La «primera frase de la tesis inversa» a veces no dice nada: «El No es más fuerte de lo que parece.» (Aarsleff), «El foso puede no ser el que fue.» (Nike). Los riesgos concretos que siguen no entran: deuda +1.629 en nueve meses y solvencia bajo objetivo (Aarsleff); dividendos por encima de la caja y metas incumplidas (Nike).
- La hoja no dice cuántas frases omite.
- No exige contenido mínimo. Con los textos sintéticos, una hoja «**Sí · comprar**» sale con «Pasaría a **No**: …» (tres puntos). Con `fase_c.json = {}` devuelve «OK», código 0, sin porqué, sin «lo que lo haría falso» y con «1. **no consta** — None» (`vigencia/robustez_entradas_y_cerrojo.txt`).

En los expedientes de hoy (todos «esperar») el sesgo no empuja a comprar. En uno favorable, tres frases de tesis frente a dos de riesgo, una de ellas quizá vacía, sí leería como «compra».

Corrección:

1. Mostrar la **tesis inversa entera**, en lista. Es lo que una hoja de estudio no debe recortar.
2. De la tesis, todas las frases, o como mínimo no saltarse ninguna que empiece por «Pero» ni la que lleva el precio.
3. Si se recorta algo: «se omiten N de M frases; están en el informe, §8».
4. Contenido mínimo o código 4 sin escribir: tesis y tesis inversa no vacías, «a No» con texto real, tres predicciones con fecha y probabilidad.

La solución de fondo es otra y no es mía decidirla: que el personaje escriba en la fase C un resumen llano propio, auditado con el resto del material, y que la hoja lo copie.

### 6 · MEDIA · No es lenguaje llano

Medido en las 11 hojas reales (`texto/jerga.txt`):

- 1.019–1.334 palabras cada una: dos o tres páginas, no una.
- El párrafo «En pocas palabras» tiene 183–301 palabras, con frases de hasta 82.
- 46–72 apariciones por hoja de términos sin explicar: «valor ponderado» (77 en total), EBIT (63), «precio de Sí» (59), ROIC (36), «heredada» (33), cubo (22), capex, EBITDA, MALO/NORMAL/BUENO, zona, foso, orgánico, λ, S2C, p(MALO), cst, CDI.
- Quedan referencias a celdas: «(C33 = −1,35)», «C18 a 0,12», «(Historia filas 29 y 33)», «(D78 = 1.144,9 €)».
- Los textos fijos también tienen jerga: «cubo», «tasa heredada», «zona», «la prueba del 10 % es información, no condición», «fase_c.json», «Análisis!C56».
- En la misma página conviven «757.05 €» (texto del personaje) y «757,05 €» (tabla).

Una persona sin formación financiera no puede leer la línea de veredicto ni la tabla. La cabecera dice «en lenguaje llano» y no lo es. Propuesta concreta en el apartado 4.

### 7 · MEDIA · Faltan los avisos oficiales que acompañan a la escalera y a la tasa

- **«La zona no es la conclusión.»** `precio.json` lo dice («no mide riesgo ni fundamento») y el Anexo C §C.7 obliga a decirlo. La hoja pone «cumple: en el precio de Sí o por debajo» sin más; «cumple» se lee como aprobado.
- **«El escenario MALO no es un suelo de valor ni la pérdida máxima posible.»** La hoja dice «bajo el MALO: por debajo del valor del escenario MALO», también en el caso «comprar» (EmpresaX_sobrevive), donde suena a «más barato que lo peor».
- **«Convención experimental, k = 3.»** No aparece.
- **Aviso A2 de la ficha: el 9 % está por debajo de la tasa mínima de la propia hoja de cálculo.** Está en 5 de las 11 fichas reales (tasa mínima: Hermès 9,9 %, Nike 10,2 %, Viscofan 9,5 % en sus dos expedientes, Rational algo por encima del 9,0 %). La sección de la tasa no lo menciona. Peor: en Viscofan la fila del 7 % sale «**cumple**» y es justo una tasa que el libro marca «⚠ REVISAR · tu r (7,0 %) < r mínima (9,5 %)» (`cifras/tasa_avisos_y_roic.txt`).
- **Motor B: la tasa de la tabla no es la tasa con que se descuenta.** Con 7 % el libro descuenta al 6,8 % (Vidrala) o al 6,5 % (Viscofan); con 10 %, al 9,6 % o al 9,2 %. Es correcto, pero no se dice.
- **Lo demás se queda quieto.** El límite que el README declara (el ROIC de largo plazo fijado mirando la tasa) no está en la hoja. En Vidrala 4.14 el personaje puso ese ROIC en 0,09 («el capital nuevo rinde la tasa»). Si siguiera a la tasa, el precio de Sí cambiaría −3,4 % al 7 % y +1,5 % al 11 %. Poco, pero la tabla exagera algo la dependencia y no lo avisa.

Corrección: frases fijas del Anexo C §C.7 junto a la tabla; guardar en cada fila `r_vs_minima_C18` y `r_operativa_C15` y mostrarlos; pasar el límite del README a la hoja en una frase.

### 8 · MEDIA · «Precio actual» no es el precio de hoy

La hoja dice «precio actual» en el veredicto, en la sección de la tasa y en la cabecera de la tabla. Es el precio usado en el análisis. En **Vidrala 4.14 es el cierre del 31-dic-2025** (90,10 €), diez meses anterior al análisis (14-nov-2026). La fecha solo aparece al final, en «Fechas». La hoja tampoco imprime cuándo se generó.

Corrección: «precio usado en el análisis: 90,10 € (31 de diciembre de 2025)» en las tres apariciones; «Hoja generada el …» en la cabecera; aviso si el precio es anterior al análisis en más de 90 días (la ficha ya tiene un aviso parecido, A3).

### 9 · MEDIA · La página que se lee no está protegida por huella

`hoja_resumen.json` guarda las huellas de lo leído, no la de `hoja_resumen.md`. Cambié a mano el veredicto («cubo **Sí** · acción **comprar** · … **apto para dinero real**»), una fila de la tabla y una predicción: `--comprobar` → «HOJA VIGENTE» y `--verificar-origen` → «ORIGEN COMPROBADO», ambos código 0 (`vigencia/md_manipulado.txt`).

Corrección: guardar el SHA-256 del `.md` en el `.json` y comprobarlo; o que `--comprobar` recomponga la página y la compare.

### 10 · BAJA · Un recálculo que no recalculase no se detectaría

La única comprobación es que la celda de entrada tenga la tasa escrita. `leer_resultados.py --exigir-recalculo-forzado` mira celdas que no dependen de la tasa. Simulando una conversión que devuelve el libro sin recalcular, la hoja acepta cinco filas idénticas (757,05 € con cualquier tasa), «firme» y «reproduce el oficial: sí» (`cifras/sin_recalculo_y_etiquetas.txt`). Hoy LibreOffice recalcula bien; es una defensa que falta.

Corrección: `borrar_caches()` en la copia antes de recalcular, o exigir que `Motor!J7` valga la tasa y que el precio de Sí baje al subir la tasa.

### 11 · BAJA · Cerrojo: bloqueo si se envuelve en `flock`, y ruta fija de esta máquina

- Lanzada como el resto del repositorio enseña (`flock CERROJO python3 …`), la hoja se queda bloqueada: llama a `flock` por dentro sobre el mismo cerrojo. Comprobado con un cerrojo privado: seguía parada a los 40 s. Esperaría 900 s por tasa. El README no lo avisa.
- `LOCK_DEFECTO = "/home/user/e_work/libreoffice.lock"` (línea 47). En otra máquina falla con código 6.

Corrección: avisarlo en el README y en la ayuda; usar `flock -w` con mensaje claro; cerrojo por defecto relativo al paquete o al directorio temporal.

### 12 · BAJA · Rótulos y mensajes

- Tasa heredada no entera: 0,085 sale «8 % (heredada)» junto a otra fila «8 %»; 0,095 sale «10 % (heredada)» y «El 10 % es provisional».
- «pendiente de investigacion» sin tilde (se quita el guion bajo del código interno).
- «Conclusión **firme**» se lee como «análisis seguro». Solo significa que la zona no cambia entre el 8 y el 10 %. Además se calcula siempre en 8–10 % aunque la heredada sea otra.
- «no utilizable» (Elis, última columna) sin explicación.
- «Origen de cada frase», «Comprobación:» y los nombres de archivo interrumpen la lectura: van mejor al final.

### 13 · BAJA · Entradas mal formadas

Un JSON truncado o con otra forma (ficha, estado, precio, metadatos) acaba en traza de Python y código 1, que no está entre los códigos documentados. No escribe hoja, así que el lado es el seguro. Corrección: capturar y devolver 3 con mensaje.

### 14 · BAJA · La batería no cubre lo anterior

- Sus dos expedientes son «concluido · Vigilar · esperar · caro · firme». No hay caso sin conclusión, favorable, «no firme», V6.3.1 F1, aprobación retirada, `fase_c.json` cambiado, página manipulada ni códigos 4 y 5 con hoja escrita.
- Su «recálculo independiente al 10 %» usa el mismo camino que la hoja (`LibroV63` y `recalc.sh`); solo la lectura es distinta.
- Hermès, su ejemplo V6.3, no es vigente para la vía oficial (hallazgo 2): al endurecer la puerta habrá que cambiarlo, por ejemplo por Vidrala 4.10.1 (V6.3 con cierre vigente).
- No está en `verificar_paquete.sh` (el README lo declara).

---

## 3. Respuesta a las cinco preguntas del encargo

1. **Verdad y omisiones.** Sí puede contar algo distinto de la ficha. Con ficha sin conclusión o con objetivo bloqueado o condicionado, pone un precio de Sí en el veredicto, puede decir «cumple» y «firme», y calla la causa (1). Calla la aptitud por entradas y F1 (3). La selección de frases deja fuera las salvedades (5). Faltan los avisos oficiales de la escalera (7). Con una conclusión favorable leería como «compra», con «experimental; no apto» como único freno y sin decir que ninguna entrada está verificada.
2. **Cifras.** Conforme: solo cambia la tasa, el cálculo es correcto en V6.3 (A y B), V6.4, V6.4.1 y V6.3.1 F1, y el 9 % reproduce el oficial. F1 no se salta **al recalcular** (el perímetro se conserva y las guardas no dependen de la tasa). Sí se salta **en la puerta**: la hoja no consulta F1, y con F1 bloqueando genera una hoja completa con código 0 (2). No probado: motor C (no hay expediente).
3. **Vigencia.** No conforme. La huella detecta cambios en lo que la hoja leyó, pero la puerta no es la oficial: genera con aprobación retirada, con `fase_c.json` cambiado y con fichas sin cierre; la página no tiene huella (9); una hoja fallida queda escrita y luego «vigente» (4).
4. **Llano.** No (6). Propuesta en el apartado 4.
5. **Batería.** 60/60 en 54 s. No cubre los casos de los hallazgos (14).

---

## 4. Propuesta de redacción

Regla que respeto: la hoja no añade hechos de la empresa. Todo lo que propongo es texto fijo (igual para todas las empresas) o campos de la ficha copiados tal cual.

### 4.1 Cabecera

Ahora:
> Material de estudio en lenguaje llano, generado después del cierre a partir de las salidas oficiales. No es una salida oficial ni la sustituye; si la ficha cambia, esta hoja se regenera (`hoja_resumen.py`). Ficha leída: `93a880c4d718550f…`.

Propuesta:
> **Resumen para estudiar. No es una recomendación de compra ni un documento oficial.** Lo escribe un programa a partir del análisis de un analista simulado (el «personaje»). **Experimental: no vale para decidir con dinero real.** Hecho el {fecha}. Deja de valer si el análisis oficial cambia.

La huella, el nombre del programa y el origen de las frases, al pie.

### 4.2 Veredicto

Ahora (Hermès):
> **Veredicto del personaje** — concluido · cubo **Vigilar** · acción **esperar** · precio de Sí **757,05 €** (precio actual 1.312,50 €, caro: por encima del valor ponderado) · **experimental; no apto para dinero real** — la ficha no declara la aptitud de uso, es anterior a ese bloque: no se presume ninguna.

Propuesta (tres líneas; lo que va entre llaves sale de la ficha):
> **Qué concluye el análisis:** no comprar ahora; esperar a mejor precio (categoría «Vigilar»).
> **A qué precio compraría:** a 757,05 € por acción o menos. {fundamento de la ficha: «precio objetivo provisional: 4 hipótesis sin fundamento suficiente…»}
> **Precio usado en el análisis:** 1.312,50 € (3 de noviembre de 2026): más caro que el valor medio de sus tres escenarios.

Frases fijas por estado:

| Ficha | Texto |
|---|---|
| concluido · Sí · comprar | «Compraría al precio del análisis. Es la conclusión del personaje, no una recomendación.» |
| concluido · Vigilar · esperar | «No comprar ahora; esperar a mejor precio.» |
| concluido · No · descartar | «La descarta.» |
| concluido · Demasiado difícil | «No sabe valorarla y la deja.» |
| pendiente_de_datos | «**Sin conclusión: falta un dato.**» + causa de la ficha. «La ficha no da precio de compra.» |
| pendiente_de_investigacion | «**Sin conclusión de compra:** una hipótesis no se puede acotar con lo que hay.» + causa. |

Ejemplo (Elis):
> **Qué concluye el análisis: sin conclusión; falta un dato.** Motivo, según la ficha: «Reparto del capex entre mantenimiento y crecimiento: no publicado…».
> **A qué precio compraría:** la ficha no da ninguno. La hoja de cálculo arroja 7,30 €, pero la ficha dice que esa cifra «no es una conclusión utilizable».

### 4.3 Lo que lo haría falso

Cambiar los rótulos: «Lo descartaría si…», «Lo compraría si…», «Lo dejaría por demasiado difícil si…», «Bajaría el precio de compra si…», «Subiría el precio de compra si…».

### 4.4 La tasa

Título: «Cuánto cambia el resultado si se le pide más o menos rentabilidad».

Texto fijo antes de la tabla:
> La **tasa** es la rentabilidad anual mínima que el análisis le pide a la inversión. Cuanto más alta, menos vale la empresa en el cálculo. El análisis usó el **9 %**: es una cifra heredada de la primera etapa y **todavía no está decidida**. Por eso se repite el cálculo con el 7, 8, 10 y 11 %, cambiando solo esa cifra. Todo lo demás se deja igual, también las hipótesis que el personaje fijó pensando en el 9 %.

Cabeceras: «Si se le pide un…» · «Compraría a este precio o menos» · «Valor medio de sus tres escenarios» · «El precio del análisis queda…» · «Para justificar ese precio, las ventas tendrían que crecer al año (cinco años)».

Zonas:

| Ahora | Propuesta |
|---|---|
| caro: por encima del valor ponderado | más caro que el valor medio de los tres escenarios |
| vigilar: entre el precio de Sí y el valor ponderado | por encima del precio de compra y por debajo del valor medio: aún no compraría |
| cumple: en el precio de Sí o por debajo | en el precio de compra o por debajo (cumple la regla de precio; no basta para comprar: ver la conclusión) |
| bajo el MALO: por debajo del valor del escenario MALO | por debajo de lo que valdría en su escenario malo (que no es un suelo: puede ir peor) |

Notas:
> - **El 9 % es provisional.**
> - **La fila del 10 % es solo una prueba** para ver cuánto cambia el resultado. No es un requisito.
> - **Frente a la tasa, el resultado {no cambia / cambia}**: con el 8, el 9 y el 10 % el precio del análisis queda {en el mismo sitio / en sitios distintos}. Esto solo habla de la tasa; no dice que el análisis sea seguro.
> - {Aviso de la ficha, si existe: «la hoja de cálculo avisa de que el 9 % queda por debajo de su tasa mínima de referencia (9,9 %)».}
> - El precio de compra sale de una regla experimental: la ganancia esperada debe ser al menos el triple de la pérdida esperada.

### 4.5 Glosario fijo

Al pie, solo con los términos que aparezcan en la página. Definiciones iguales para todas las empresas. Ejemplos:

- **Precio de Sí:** el precio por acción al que el personaje compraría, o menos.
- **Escenarios MALO, NORMAL y BUENO:** tres historias posibles del negocio, con un valor por acción cada una.
- **Valor ponderado:** la media de los tres escenarios según la probabilidad que el personaje da a cada uno.
- **ROIC:** lo que gana el negocio al año por cada euro invertido en él.
- **Margen EBIT:** de cada 100 € de ventas, lo que queda antes de intereses e impuestos.
- **Capex:** lo que la empresa invierte en instalaciones y equipos.
- **Foso:** la ventaja que protege a la empresa de sus competidores.
- **Crecimiento orgánico:** el de las ventas sin contar compras de empresas ni divisas.

---

## 5. Límites de esta revisión

- No he podido leer el documento de la reorientación (§7, K5, K9): no está en el repositorio.
- No hay expediente real favorable ni cerrado con la V6.3.1 F1; esos casos son sintéticos, hechos con el pipeline real y los agentes simulados del paquete.
- La vigencia oficial la he comprobado en copias completas de Hermès, Nike, Viscofan (`empresas_v2`), Vidrala 4.10.1, Vidrala 4.13 bloqueo, Vidrala 4.14 y Viscofan 4.14. No en Elis.
- Motor C sin probar: no hay expediente.
- No he revisado `cierre_v2.py`, `ficha.py` ni `motor_a_f1.py` como tales; los he usado como referencia.
- Las correcciones que tocan el pipeline (borrar `fin` al relanzar, archivar la hoja al retirar una aprobación, un campo de resumen llano en la fase C) son propuestas: decide la persona responsable.

---

## 6. Qué haría falta para pasar a CONFORME

1. Hallazgos 1 a 4 corregidos, con pruebas nuevas en la batería: un expediente sin conclusión (Elis 4.14 o Vidrala 4.13 bloqueo), uno favorable y uno con F1 bloqueando tras un cierre (los sintéticos sirven), `fase_c.json` cambiado, y códigos 4 y 5 sin hoja escrita.
2. Hallazgos 5 a 9 corregidos o aceptados expresamente como límites por la persona responsable, con el límite escrito en la propia hoja.
3. Nueva revisión por un agente distinto del autor.

---

## 7. Evidencia (`/home/user/e_work/revision_hoja/evidencia/`)

| Archivo | Qué contiene |
|---|---|
| `01_bateria_test_hoja_resumen.txt` | Batería del autor en la copia: 60/60 |
| `02_lote_expedientes_reales.txt` | Generación sobre diez expedientes reales |
| `hojas/*.hoja_resumen.md`, `*.salida.txt` | Hojas generadas y salida del programa en cada caso |
| `sinteticos/fichas_oficiales_resumen.txt` | Estado oficial de cada expediente frente a lo que hizo la hoja |
| `sinteticos/sintetico_*.txt` | Salida de las baterías sintéticas del paquete que produjeron los expedientes |
| `cifras/indep_comparacion.txt`, `indep_*.json` | 18 recálculos independientes con LibreOffice |
| `cifras/dcf_puro.txt` | 50 filas calculadas sin LibreOffice |
| `cifras/copia_solo_C56.txt` | La copia solo difiere en `Análisis!C56` |
| `cifras/f1_guardas_por_tasa.txt` | Guardas F1 al 7, 9 y 11 % |
| `cifras/tasa_avisos_y_roic.txt` | Avisos del libro por tasa, aviso A2 de las fichas, ROIC anclado a la tasa |
| `cifras/sin_recalculo_y_etiquetas.txt` | Recálculo no forzado simulado; rótulos de tasas no enteras |
| `vigencia/vigencia_ataques.txt` | A1, A2, A3, A4, A9 y vigencia oficial de Hermès y Vidrala |
| `vigencia/vigencia_A6_A7.txt` | Hoja dentro del expediente, material alterado y retirada oficial |
| `vigencia/vigencia_oficial_otros.txt` | Vigencia oficial de otros cinco expedientes |
| `vigencia/v631_cerrado_salida.txt`, `v631_p10_salida.txt` | Pipeline V6.3.1 F1: cierre (P6), bloqueo tras el cierre (P8, P10) |
| `vigencia/md_manipulado.txt` | Página alterada a mano que pasa las dos comprobaciones |
| `vigencia/robustez_entradas_y_cerrojo.txt` | Entradas mal formadas, `fase_c.json` vacío, cerrojo |
| `texto/seleccion_frases.txt` | Frases de tesis y tesis inversa que entran y que se omiten |
| `texto/limpieza_fragmentos.txt` | Qué quita la limpieza en 450 frases reales |
| `texto/jerga.txt` | Longitud, referencias a celdas y jerga por hoja |
| `texto/presentacion_No_descartar.txt` | Simulación de presentación «No · descartar» con zona favorable |
| `herramientas/` | Mis scripts (`indep.py`, `dcf_puro.py`, `v631_cerrado.py`, `v631_p10.py`, …) |
