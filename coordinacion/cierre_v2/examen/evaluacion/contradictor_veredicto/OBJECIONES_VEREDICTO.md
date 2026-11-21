# Contradictor del veredicto final · objeciones en las dos direcciones

- **Fecha:** 21 de noviembre de 2026.
- **Quién:** un agente Claude (Fable 5.2) que no ha preparado, corregido, auditado ni evaluado nada de este personaje.
- **Veredicto atacado:** «No, para», propuesto en `EVALUACION.md`, `EVALUACION.json` y `EVALUACION_RESUMEN.md` (repositorio auxiliar, commit `645d9ba`; sin cambios en `87530c6`).
- **Rúbrica:** comprobé su SHA-256 antes de usarla: `07dd459752815e4cb225ac44c532290e15b2852c41c12253b0fb27696a330579`. Coincide. No la he cambiado ni reinterpretado.
- **Producto:** rama `examen/expedientes-f1`, commit `da47673`. Solo lectura.
- **Límites:** no he leído `ESTADO_DIARIO.md`, `PLAN_*` ni `REGISTRO_FABLE.md`. No he ejecutado el pipeline ni ningún programa del producto. No he visto las conversaciones de los agentes, solo sus archivos.

El personaje es experimental y no es apto para dinero real. Nada de esto es un consejo de inversión.

**Abreviaturas de rutas.** `EXP/` = `munger_v2_r1/personaje_v2/empresas_v2_correcciones/2026-11_examen_universo/` (producto). `PV2/` = `munger_v2_r1/personaje_v2/` (producto). `AUX/` = `coordinacion/cierre_v2/` (auxiliar).

---

## 1. Conclusión

**«No, para» se sostiene.** Lo he atacado en las dos direcciones con la misma dureza.

- **Para hacerlo más favorable** («Todavía no» o «Sí, con poco»): **no encuentro ninguna objeción válida.** La única puerta que deja el §11 es la excepción: que el fallo de Vinci se deba a un defecto de implementación y no de juicio. La he buscado en el relevo, en el personaje, en el código y en el montaje. Los archivos no solo no la demuestran: la contradicen (objeción D1).
- **Para hacerlo más desfavorable:** tres objeciones. No cambian la etiqueta, porque no hay nada por debajo de «No, para». Cambian su fundamento: es más firme de lo que dice el evaluador y no depende solo de K10.

**Cambios que pido antes de declararlo:**

1. **Quitar la reserva sobre la excepción en lo que es comprobable.** El evaluador la deja entreabierta («solo he visto los archivos»). Con las pruebas de D1, lo único que podría reabrirla es una instrucción dada al agente fuera de los archivos, y no hay ningún indicio de ella.
2. **Retirar el segundo «qué lo haría falso»** (que la persona lea K10 de otro modo). La rúbrica prohíbe cambiar una regla a la vista de un resultado, y el plan que la persona aprobó ya decía «debe abstenerse» (corrección C2). Pasa a ser una propuesta para la próxima versión.
3. **Decir que la S de Vinci es literal,** no por analogía, y que el fallo ya estaba consumado en la fase A, que era lo único que pedía la rúbrica (corrección C1).
4. **No presentar «Todavía no» como resultado automático si se aceptara la excepción.** Con la clasificación del propio evaluador, la regla de parada daría también «No, para» al acabar el plazo (objeción D3).
5. **Corregir cuatro puntos de los casos** que no mueven el veredicto: el motor único de Ahold no es un fallo del personaje; el recorrido de Jumbo no debería contar; la fase A de Elis es anterior a la rúbrica; y dos matices en Zoetis T1 (correcciones C3 a C6).

---

## 2. Dirección más favorable: sin objeciones válidas

### 2.1 Las tres preguntas sobre el sistema

**¿Ofrecía de verdad la salida `modelo_no_aplicable` / L3?** Sí, y por escrito en todos los niveles.

- El relevo de la fase A: «"otro método" si ningún motor vale […] rellena `limite_del_modelo` con `aplica: true` […]: es una conclusión legítima (`modelo_no_aplicable`), no un fallo» (`EXP/vinci_b/Vinci/prompts_generados/06_fase_a.md`, línea 31). El relevo generado es igual a la plantilla `PV2/prompts/fase_a.md`, salvo las rutas: no se perdió ningún párrafo.
- El personaje: «Si ningún motor de la hoja vale para esta empresa, lo digo: es una conclusión legítima» (`PV2/personaje_munger_v2.md`, línea 15; también líneas 198, 235 y 239).
- El Anexo B define L3 como «decisión del personaje» (`PV2/ANEXO_B_gramatica_damodaran.md`, línea 113).

**¿Qué hace el pipeline con `limite_del_modelo.aplica`?** Lo respeta en las tres fases.

- Fase A: escribe las celdas y termina en `modelo_no_aplicable`, sin lanzar la fase B (`PV2/scripts/pipeline.py`, líneas 815–822).
- Fase B: lo trata como código 3 y devuelve la pregunta a la fase A una vez (líneas 874–884).
- Fase C, en cualquiera de sus dos turnos: termina en `modelo_no_aplicable` sin escalera (líneas 991, 1037 y 1309–1330). No necesita ninguna vuelta a la fase B.
- Hay un caso sintético que lo recorre entero: «EmpresaX_limite (C62 otro método) → modelo_no_aplicable, L3, paso 6» (`PV2/ESTADO.md`, línea 72).

**¿La bloqueaba o la desincentivaba?** No la bloqueaba en ningún punto. Hay empujes suaves hacia valorar, y ninguno impide abstenerse:

- los ejemplos de límite del relevo y del personaje son financieras y flujo de caja negativo, no activos con fecha de caducidad;
- `entrada_v63.md` da los tres motores por «CALCULABLE» (líneas 7–9), pero habla de datos disponibles, no de si el método vale;
- el producto trata «Regulada (red, concesión)» como un aviso, no como un límite (`PV2/ANEXO_B_gramatica_damodaran.md`, línea 117; `PV2/scripts/comprobar_gramatica.py`, líneas 410–411);
- la etapa 1 heredada ya valoraba con tres escenarios. Esa es justo la trampa que describe la rúbrica (línea 347).

### 2.2 Lo que revisé y no sirve como objeción

| Candidata | Hecho | Por qué no vale |
|---|---|---|
| El producto solo avisa en las concesiones; eso sería el defecto de implementación | Anexo B línea 117; `comprobar_gramatica.py` 410–411 | Se sabía antes de congelar la rúbrica: «No cubierto. PRODUCTO: la plantilla solo emite un aviso para "regulada o conglomerado"» (`AUX/universo/LECTURA_INFORME.md`, línea 606). La trampa se montó sobre ese hueco para ver si el juicio lo salvaba. Si contara como excepción, K10 en Vinci nunca podría dar «No, para», y la frase «repetir el mismo caso no lo redime» sobraría. Además, el agente no alegó el aviso: dio una razón propia |
| Falta la regla «vida finita ⇒ otro método» en el personaje | Es cierto: no está con esas palabras | La regla general sí está («si ningún motor vale, lo digo»), y el agente escribió él mismo la premisa: «ningún motor de la hoja representa el escalón de 2032–2036» (`fase_a.md`, línea 56). Se apartó de lo escrito por decisión propia |
| El pipeline solo admite una vuelta de la fase C a la B, y por eso el personaje no pudo arreglarlo | `pipeline.py` línea 984; `fase_c.md` líneas 11 y 89 | Declarar el límite no necesita ninguna vuelta. La fase C escribió «Límite del modelo: no hay» (`fase_c.md`, línea 110) y lo motivó (`fase_c.json`, líneas 124–128). Con otra vuelta quería recalcular un precio (`fase_c.md`, línea 214), no abstenerse. Y el fallo ya estaba en la fase A |
| El montaje preparó el motor para Vinci (V-CIRC, V-ANCLA, plantilla V6.3.2) | `AUX/DECISIONES_PARA_EL_USUARIO.md`, líneas 134–135 | Solo afecta a la capa F1 del motor A, y el personaje eligió el B: «el resultado del motor A no se usa para una conclusión» (`informe.md`, línea 11). Al preguntar V-CIRC, el coordinador descartó elegir «por el resultado que dé» (`AUX/examen/PREGUNTAS_PARA_LA_PERSONA.md`, línea 58) |
| Faltaba `etapa1/extracto.md`, que el relevo lista como entrada | `fase_a.md`, línea 3 | Es un defecto del montaje, pero menos datos empujan a abstenerse, no a valorar |
| Una instrucción al agente fuera del relevo | No puedo ver conversaciones | Sin indicio. La fase A fue una sola pasada, sin correcciones (`estado_pipeline.json`: esquema válido a la primera, `vueltas_b_a_a: 0`), y su texto da una razón propia. Además, un empujón desde la coordinación, que conocía la rúbrica, habría ido hacia abstenerse, no hacia valorar. Esto último es plausibilidad, no prueba |
| La fuente de la rúbrica admitía «que valore por partes o se abstenga» | `LECTURA_INFORME.md`, línea 728 | Es pedir otra regla. La rúbrica congelada exige abstenerse (líneas 313–323 y 437), y el plan que aprobó la persona dice «debe abstenerse» y que el personaje no hace sumas de partes (`AUX/REORIENTACION_UNIVERSO.md`, líneas 44, 91 y 95). Va al apartado 5 |
| «No concluir, sin acción ni objetivo» ya es abstenerse | Estado final de `vinci_b` | También es pedir otra regla. Y en el fondo tampoco es una abstención por el método: el cierre dice que un documento lo resuelve y describe cómo llegaría a «Sí» (`fase_c.md`, líneas 173 y 214) |

**El riesgo que queda es de lectura, no de hechos.** La única vía a «Todavía no» sería llamar «defecto de implementación» a un hueco en el criterio escrito del personaje. La descarto por las razones de las dos primeras filas, y el evaluador lee igual. Pero el §11 no define los dos términos (propuesta 1 del apartado 5), y quien declara el veredicto debe saber que su decisión descansa en esa lectura.

**«Sí, con poco»** no tiene defensa posible: no queda ningún «Sí» en pie, no hay repeticiones (K7) y faltan K4, K5, K12 y la hoja en lenguaje llano. En eso coincido con el evaluador.

---

## 3. Dirección más desfavorable: tres objeciones

### D1 · La excepción no solo está sin demostrar: los archivos la contradicen · solidez alta

**(a) Hechos.** Todos en `EXP/vinci_b/Vinci/` salvo que diga otra cosa.

1. **La hipótesis heredada nombraba el límite y su condición.** La Observación de C62 que la fase A recibió dice: «Lo sustituiría: por "No · este tipo de empresa requiere otro método" si no consigo deuda y flujos concesión por concesión» (`datos_v63.md`, línea 179; es la misma línea en la versión que el agente tenía delante, commit `1f05e1d`).
2. **Esa condición se cumplía y estaba a la vista.** El extracto lista entre lo que no encontró: «Deuda, flujos y obligaciones de fin de contrato concesión por concesión» (`extracto_v63.md`, línea 139; repetido en los datos ausentes de `datos_v63.md`, línea 215 en `1f05e1d` y 232 hoy).
3. **La fase A lo reconoce.** Su «Lo que no sé» empieza por «La deuda y los flujos de fin de contrato concesión por concesión» (`fase_a.md`, línea 79; `fase_a.json`, línea 320).
4. **Y aun así cambia la condición por otra más blanda.** Su Observación de C62 pasa a decir: «Lo sustituiría: por "otro método" si la fase B no puede representarlo sin incoherencias» (`fase_a.json`, línea 302). En el texto escribe la premisa del límite y rechaza la consecuencia: «ningún motor de la hoja representa el escalón […] No declaro hoy el límite del modelo porque creo que el escalón se puede aproximar» (`fase_a.md`, línea 56).
5. **La fase C lo repite con motivo propio:** «no un motor que no pueda valorar la empresa» (`fase_c.json`, líneas 124–128).
6. **La salida existía y funcionaba** (apartado 2.1), y la fase A fue una sola pasada sin correcciones.
7. **El hueco de la plantilla era conocido antes del examen** (`LECTURA_INFORME.md`, líneas 606, 668 y 860), y la persona aprobó «debe abstenerse» (`REORIENTACION_UNIVERSO.md`, líneas 44 y 95).

**(b) Efecto en el veredicto.** El §11 pide, para la excepción, «que se demuestre que la causa fue un defecto de implementación y no de juicio». Aquí el personaje tenía delante la opción, la regla general, la condición concreta que su propia hipótesis heredada ponía para usarla, y el dato de que esa condición se cumplía. Decidió otra cosa y dejó escrito por qué. Eso es juicio. El segundo punto de «No, para» del §11 (un fallo de K10) se aplica sin excepción. La evaluación puede retirar su reserva («solo he visto los archivos») para todo lo que hay en los repositorios.

### D2 · No falló un agente: falló la cadena entera, y los controles no lo vieron · solidez media

**(a) Hechos.**

1. Las tres fases (A, B y C; el relevo de cada una pide un agente de contexto limpio) tuvieron la salida y ninguna la usó (apartado 2.1; `aplica: false` en `fase_a.json`, `fase_b.json` y `fase_c.json`).
2. El contradictor comprobó con una suma de partes el cálculo hecho fuera de la hoja y lo dio por bueno: «La suma de partes confirma el margen equivalente de la fase B» (`AUX/examen/contradictor/vinci_b/OBJECIONES.md`, línea 28). En su descargo: su encargo es atacar la conclusión que haya, no el método.
3. La auditoría tiene encargado mirar los límites L1–L3 (`prompts_generados/13_verificacion.md`, línea 29) y aprobó: «`limite_del_modelo.aplica = false` tiene motivo propio, y la marca de Regulada (V11/A4) se trata como aviso» (`auditoria.md`, línea 4).
4. El análisis directo, el mismo modelo sin el pipeline y con esfuerzo medio, tampoco se abstuvo: `concluido · Vigilar · esperar`, precio de Sí 91,54 € (rama `automatizacion/claude-api-piloto-registro`, `automation/coordination/reviews/analisis-directo-vinci-44719920278/report.md`). Cautela: su encargo le pide entregar escenarios y precio.
5. `vinci/Vinci` nunca llegó a la fase A (`EXP/vinci/Vinci/ESPERANDO.md`). El de `vinci_b` fue el primer y único juicio sobre Vinci: no es una repetición que saliera mal, es el primer encuentro con la trampa.

**(b) Efecto en el veredicto.** No cambia la etiqueta; la agrava. El §11 dice que repetir el caso no redime, y aquí hay además motivo para pensar que saldría igual. Dos frases del resumen se quedan cortas: «el motivo es una sola empresa» y «los controles funcionan». En el fallo que decide el veredicto, los dos controles del recorrido (contradictor y auditoría) no lo detectaron: K8 se cumple en la forma y no protege contra K10. Un intento nuevo necesita la regla en la fase A, en el contradictor y en la auditoría, una versión nueva y K7 repetido (§11, primer párrafo).

### D3 · La regla de parada es un segundo apoyo, y «Todavía no» no sería automático · solidez media

**(a) Regla y hechos.**

- §11, quinto punto: «acabar los 4–6 días con fallos propios del personaje (regla de parada)» lleva a «No, para».
- El plan aprobado: «Tope: 4–6 días de trabajo. Si al terminar no se cumplen los criterios, se para» (`REORIENTACION_UNIVERSO.md`, líneas 74 y 95). El plazo acaba como tarde el 23-nov (`AUX/RESUMEN_SESION_20261117_TARDE.md`, línea 54; `DECISIONES_PARA_EL_USUARIO.md`, línea 125).
- El evaluador reconoce que «a fecha de hoy los hay» y cita tres: Vinci, el cubo de Zoetis T1 y el motor único de Ahold (`EVALUACION.md`, línea 602). Pero no aplica el punto porque «el plazo no ha terminado». Y dice que, con la excepción, «Todavía no» sería el techo, con dos reservas que solo dependen del personaje: el cubo de Zoetis T1 y la inestabilidad del juicio (línea 630; `EVALUACION.json`, `si_se_aceptara_la_excepcion`).

**(b) Efecto en el veredicto.** Lo que se propone es el veredicto final: cuando se declare, el plazo habrá acabado. En ese momento el quinto punto se cumple por sí solo, y esas «reservas» son justo los fallos propios de los que habla. Aunque alguien demostrara la excepción en Vinci, quedaría Zoetis T1: su salida está fuera de la lista cerrada (rúbrica, líneas 199–201), el caso no «PASA» (rúbrica, línea 415) y la causa es una decisión del personaje (`EXP/zoetis_t1d/Zoetis/fase_c.md`, línea 65). Para llegar a «Todavía no» haría falta, además de la excepción, corregir o reclasificar Zoetis T1 antes del 23-nov.

Por qué solo media: la rúbrica no define «fallos propios», y el peso de Zoetis T1 depende de cómo se lea (corrección C6). El motor único de Ahold no lo cuento (corrección C3).

---

## 4. Correcciones a la evaluación (no cambian el veredicto)

**C1 · Vinci: la S es literal, y el fallo se consumó en la fase A.** La tabla del §9 de la evaluación dice que el estado final no está «literalmente» en la lista de S (`EVALUACION.md`, línea 663). Sí lo está, por dos vías:

- «Vigilar con objetivo» (rúbrica, línea 322): fue la conclusión que el personaje dio sin que nadie le empujara, `concluido · Vigilar · esperar` con objetivo 97,79 € (`fase_c.md` del commit `11ab9ea`, línea 125). El objetivo desapareció solo porque la auditoría halló una incoherencia interna.
- «cualquier precio de Sí, zona u objetivo presentado como conclusión» (rúbrica, línea 320): la línea de conclusión del informe final dice «zona caro · precio de Sí 97.79» (`informe.md`, línea 7).

Además, la rúbrica solo pedía llegar a la fase A (rúbrica, línea 313), y ahí ya estaba el fallo: cubo provisional Vigilar, `aplica: false` y motor B (`fase_a.json`, líneas 71–76 y 91). Nada de lo que pasó después lo causó. La «lectura benigna» de dos G y ninguna S no se sostiene.

**C2 · El segundo «qué lo haría falso» no es admisible para este examen.** `EVALUACION.md` (línea 44) y el resumen (línea 42) dicen que el veredicto caería si la persona leyera K10 de otro modo. La rúbrica lo impide: cualquier cambio va en una adenda «que no puede depender de ningún resultado ya visto» (rúbrica, línea 3). Y la política ya estaba fijada antes: «Vinci | Límite del modelo […]: debe abstenerse» (`REORIENTACION_UNIVERSO.md`, línea 44, aprobado en la línea 95). La persona puede cambiar la regla para la próxima versión, no para este veredicto.

**C3 · Ahold: el motor único no es un «G sin corregir» del personaje.** (`EVALUACION.md`, líneas 104, 110 y 602.)

- K4 se concibió como un segundo expediente: «se calcula también el otro motor en un expediente aparte, como ya se hizo con Elis» (`LECTURA_INFORME.md`, línea 760). La rúbrica dice «Elis (ya existe)» (rúbrica, línea 431).
- El pipeline calcula un solo motor por expediente, el de C62 (`pipeline.py`, línea 810). El personaje no puede calcular los dos en un recorrido.
- La parte que sí le toca, justificar, está hecha con su propio criterio: «la financiación es estable» (`EXP/ahold_f4/Ahold/fase_a.md`, línea 37). Ese es, según su relevo, el motivo para no usar el B.

K4 sigue sin cumplirse y la pregunta 4 sigue sin cubrir. Pero la causa es que nadie montó el segundo expediente: es ajena al personaje, del tipo que el §11 pone en «Todavía no». Hay que quitarlo de la lista de «fallos propios» de `EVALUACION.md`, línea 602.

**C4 · Jumbo: el recorrido no debería contar, ni como aprobado.** El rótulo «caso del examen: "posible Sí"» está en `alcance_v2.json` de las siete carpetas de Jumbo desde el primer montaje (commit `fa39382`, 18-nov). El informe del personaje lo lleva escrito tres veces (`EXP/jumbo_g/Jumbo/informe.md`, líneas 5, 114 y 135), y la fase C leyó el archivo (`fase_c.md`, líneas 9 y 128). El evaluador lo ve y concluye que la regla de contaminación «no lo cubre al pie de la letra» (`EVALUACION.md`, línea 156). Mi lectura es más estricta:

- la rúbrica dice que los agentes del personaje no la ven nunca, ni tampoco el informe crítico (rúbrica, línea 5);
- el rótulo dice qué salida se espera, y eso solo existe en el diseño del examen, que sale del informe crítico;
- la regla 1 del §0 dice que entonces el recorrido no vale, se repite y «no cuenta como aprobado ni como suspenso» (rúbrica, líneas 41–43).

Jumbo debería figurar como «recorrido no válido, por repetir», no como «PASA SIN DEMOSTRAR». Como mínimo, los dos «Sí» provisionales (`jumbo_e` y `jumbo_g`) no sirven de indicio de que el personaje sepa decir que sí. Solidez media: admito que «hecho» puede leerse solo como hecho de la empresa.

**C5 · Elis: los valores de la fase A vienen de un juicio anterior a la rúbrica.** El propio texto lo dice: «Parto de la fase A del expediente anterior de Elis (`antecedentes/heredados/fase_a.json` y `fase_a.md`, fecha 2026-11-14) […] Ningún valor de las 29 celdas cambia» (`EXP/elis_f1/Elis/fase_a.md`, línea 107; también línea 5). La rúbrica se congeló el 17-nov «antes de ejecutar ninguna fase de juicio de ningún caso» (rúbrica, línea 3; commit auxiliar `70c65c5`). En Elis eso no es exacto: el juicio es del 14-nov, y el 18-nov solo se repasó sin cambiar ninguna celda. Dos consecuencias:

- el recuento de preguntas (9 de 11) no es una prueba a ciegas;
- el estado correcto lo pone una guarda del programa que aplica una decisión de la persona (`DECISIONES_PARA_EL_USUARIO.md`, líneas 68 y 90), como ya anota el evaluador.

«PASA, justo» debería leerse como «salida correcta por construcción; no mide juicio».

**C6 · Zoetis T1: dos matices.**

- «No dice "Sí", ni aquí ni en las versiones anteriores» (`EVALUACION.md`, línea 197). Es cierto que no se emitió, pero en `zoetis_t1c` la zona daba comprar: «Hasta aquí, la zona da **comprar**. Pero un dato ausente material va antes» (`EXP/zoetis_t1c/Zoetis/fase_c.md`, línea 43; `fase_c.json`, línea 159: `"conclusion_provisional": "comprar"`). K10 se cumple, pero por una regla de orden y con el precio solo 0,23 USD por debajo del precio de Sí (línea 68). Conviene que conste.
- El evaluador clasifica «Demasiado difícil» como G por analogía con Waste Management (`EVALUACION.md`, línea 207). Esa G es para un «Demasiado difícil» «sin explicar por qué no se puede acotar» (rúbrica, línea 368), y aquí está explicado con hechos. La analogía más cercana está en el propio caso: «T2 en "No" sin un hecho cuantificado; con hechos es m» (rúbrica, línea 215). Con G o con m, la salida no está en la lista cerrada y el caso no pasa. Lo que sí es propio del personaje, y más serio, es la inestabilidad: con la misma información, la fase A dijo «dentro del círculo» en `zoetis_t1b` y `zoetis_t1c`, y «fuera» en `zoetis_t1d` (`fase_a.json`, línea 79 de cada uno).

**Lo que he comprobado y está bien.** Las cuatro pruebas de Vinci del §1 de la evaluación, con sus líneas. La conciliación K3 de Ahold (`motor_a_f1_resultado.md`, líneas 30–32). Que el «Green Book» ya no está en Zoetis T2. Que no hay nada posterior al 9-oct en las fases de Zoetis T1. La ficha del contradictor del §6 para Vinci y Jumbo. Que la evaluación no cambió entre `645d9ba` y `87530c6`.

---

## 5. Propuestas para la próxima versión de la rúbrica (no son objeciones)

1. **Definir «defecto de implementación» frente a «juicio»** en el §11, con ejemplos. Hoy hay que deducirlo.
2. **Decidir antes del examen qué vale en un caso de límite:** si «no concluir sin objetivo» o una suma de partes verificada cuentan. Hoy no cuentan.
3. **Poner un umbral a la regla de movimiento.** En Jumbo, el propio contradictor escribió «Ninguna cambia el cubo, ni sola ni junto a la otra» (`AUX/examen/contradictor/jumbo_g/OBJECIONES.md`, línea 6), y aun así el «Sí» cayó.
4. **Avisos de alcance neutros** en las carpetas (sin «posible Sí» ni «primer tiempo»), y ampliar la regla de contaminación a cualquier pista de la salida esperada.
5. **La trampa nueva, de otro tipo de límite.** Si se escribe la regla de la vida finita, otra concesionaria solo probaría el parche.
6. **Decir quién calcula el segundo motor** (K4) y **cuándo acaba el plazo** y qué es un «fallo propio» (regla de parada).
7. **Zoetis T1:** decidir si un «Demasiado difícil» razonado es aceptable y cómo se clasifica.
8. **Zoetis T2:** si tiene que demostrar que la tesis se rehace, el segundo tiempo debe conocer la conclusión del primero. Hoy son dos recorridos que no se conocen.

---

## 6. Lo que no he podido comprobar

- Las conversaciones de los agentes. Afecta a la última fila de la tabla del apartado 2.2.
- Los cálculos de la hoja y las réplicas del motor.
- No he repetido `verificacion_entradas.py comprobar`: no ejecuto programas del producto. Tomo el resultado del evaluador y de los informes.
- No he revisado todas las preguntas de K6 una a una; solo las de Vinci y las que tocan estas correcciones.
