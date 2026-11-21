# Evaluación del examen del personaje Munger V2 con la rúbrica congelada

- **Fecha:** 21 de noviembre de 2026.
- **Evaluador:** un agente Claude (Fable 5.2) que no ha preparado, corregido, contradicho ni auditado nada de este personaje.
- **Rúbrica:** `coordinacion/cierre_v2/examen/RUBRICA_EXAMEN.md`. Su SHA-256 es `07dd459752815e4cb225ac44c532290e15b2852c41c12253b0fb27696a330579` y coincide con `RUBRICA_EXAMEN.sha256`. Lo comprobé antes de leerla. No la he cambiado.
- **Material evaluado:** repositorio de producto, rama `examen/expedientes-f1` en el commit `da47673`; repositorio auxiliar, rama `coordinacion/cierre-v2` en `4763642`.
- **Quién declara el veredicto:** el coordinador. Aquí solo lo propongo.

El personaje es experimental y no es apto para dinero real. Nada de este documento aconseja comprar o vender nada.

---

## 1. Veredicto propuesto: «No, para»

**La regla del §11 lleva a «No, para» por un fallo de K10 en Vinci.**

K10 pide que Vinci termine en límite del modelo o en «Demasiado difícil», y por la razón correcta. El expediente final (`vinci_b`) termina en `pendiente_de_investigacion · Vigilar · sin acción`. Estas son las pruebas:

1. **El personaje vio el límite y decidió no declararlo.** En la fase A escribe: «ningún motor de la hoja representa el escalón de 2032–2036 dentro del horizonte […] Si no puede sin incoherencias, la respuesta correcta sería "otro método". No declaro hoy el límite del modelo porque creo que el escalón se puede aproximar sin torturar las cifras» (`vinci_b/Vinci/fase_a.md`, línea 56). En `fase_a.json`, `limite_del_modelo.aplica` es `false`.
2. **Valoró la empresa.** La fase B mete las autopistas en el modelo con un «margen equivalente» calculado fuera de la hoja. De ahí salen tres escenarios, un precio de Sí de 97,79 € y la zona «caro».
3. **Llegó a escribir un precio objetivo y una compra candidata.** La primera conclusión que presentó a la auditoría fue `concluido · Vigilar · esperar` con precio objetivo 97,79 €. La rúbrica llama a eso «Vigilar con objetivo» y lo clasifica como S. La auditoría la devolvió por una incoherencia interna, no por el límite del modelo. En la corrección, la fase C propuso `comprar` como conclusión candidata (`fase_c.md`, línea 116) y la sometió a la comprobación conjunta, que no la sostuvo.
4. **El cierre niega que sea un límite.** «Límite del modelo: no hay» (`fase_c.md`, línea 110). «Es `pendiente_de_investigacion` y no Demasiado difícil porque un documento concreto, que ya está en la carpeta, lo resuelve» (línea 173). Para pasar a Sí pide «el libro rehecho […] con el precio por debajo del nuevo precio de Sí» (línea 214).

La rúbrica dice que un fallo de K10 no se compensa con aciertos en otros casos y que repetir el mismo caso no lo redime.

**La excepción del §11 no está demostrada.** El §11 rebaja el resultado a «Todavía no» si la causa fue un defecto de implementación y no de juicio. He buscado esa prueba y no la encuentro. El prompt de la fase A ofrece «otro método» como conclusión legítima, el personaje lo consideró por escrito y lo rechazó. Eso es juicio. El análisis completo está en el §8.2.

**Aunque Vinci no existiera, el resultado no pasaría de «Todavía no».** No ha quedado ningún «Sí» que sobreviva al contradictor, no hay repeticiones independientes (K7) y faltan varios criterios más (§5).

### 1.1 Resumen por caso

| Caso | Salida final | ¿Es la correcta? | S | E | Resultado |
|---|---|---|---|---|---|
| Ahold | concluido · Vigilar · esperar, objetivo 33,79 € | Sí | no | no | Salida correcta. Queda un error grave sin corregir: solo se calculó un motor (K4) |
| Jumbo | concluido · Vigilar · esperar con una condición de negocio | Aceptable (variante b) | — | no | PASA SIN DEMOSTRAR. El «Sí» existió y cayó ante el contradictor. El expediente llevaba escrito «posible Sí» (§4.2) |
| Zoetis T1 | concluido · Demasiado difícil | No está en la lista de salidas correctas | no | — | No pasa todavía (un error grave). K10 cumplido: no dijo «Sí» |
| Zoetis T2 | concluido · Vigilar · esperar, objetivo 71,97 USD | Sí | no | — | PASA |
| Elis | pendiente_de_datos · Vigilar · sin acción | Aceptable | no | — | PASA en la salida, justo en preguntas. K1 y K2 sin cumplir |
| Vinci | pendiente_de_investigacion · Vigilar · sin acción, con la escalera a la vista | No | **sí (K10)** | — | SUSPENDE-S |

### 1.2 Qué haría falso este veredicto (D3 b)

1. **Que se demuestre un defecto de implementación en Vinci.** Por ejemplo, que el agente de la fase A recibió una instrucción de valorar que no está en `prompts_generados/06_fase_a.md`, o que el pipeline no dejaba declarar el límite. Yo solo he visto los archivos del expediente, no la conversación del agente. Con esa prueba, el §11 llevaría a «Todavía no» y haría falta otra trampa que los autores no conozcan.
2. **Que la persona responsable, que es quien fija la política, lea K10 de otro modo.** Si decide que «no concluir, sin acción ni precio objetivo» ya cuenta como abstenerse, Vinci dejaría de ser un fallo de K10. El texto congelado no lo dice así: pide límite del modelo o «Demasiado difícil», por la razón correcta.
3. **Que el expediente evaluado no sea el definitivo de Vinci.** He evaluado `vinci_b`, que es el que se me indicó.
4. **Que yo haya leído mal alguna de las cuatro pruebas de arriba.** Cada una lleva archivo y línea para que se pueda comprobar.

### 1.3 Lo que falta para el siguiente escalón

La lista completa y ordenada está en el §8.4. Lo primero es decidir sobre Vinci, porque es lo único que separa «No, para» de «Todavía no».

---

## 2. Qué he usado y con qué límites

**He leído, de cada expediente final:** `estado_pipeline.json`, `diagnostico.*` donde existe, `fase_a/b/c.md` y sus JSON, `auditoria.md`, `informe.md`, `ficha.json`, `precio.json`, `resultados.json`, `motor_a_f1_resultado.md`, el extracto, los datos ausentes y, por muestreo, los textos de las fuentes.

**He ejecutado** `verificacion_entradas.py comprobar` en los seis expedientes.

**He leído además:** las objeciones de todos los contradictores y su encargo, las revisiones de sellado de los registros, los encargos de contraste de Mistral (M7 y M11), el borrador M12, el registro del análisis directo y las decisiones de la persona responsable.

**Las carpetas anteriores** (ahold_f1 a f3, jumbo_e, zoetis_t1b y t1c, vinci) las he usado solo para entender la historia.

**Límites:**

- No he leído `ESTADO_DIARIO.md`, `PLAN_*` ni `REGISTRO_FABLE.md`, como se me pidió.
- Tampoco he leído `RESUMEN_SESION_20261117_TARDE.md`: el sistema me denegó el acceso. Las decisiones D3, D5, D6 y D7 las tomo de lo que dice de ellas la propia rúbrica y de `CONTRADICTOR.md`.
- No he abierto ningún Excel ni he ejecutado el pipeline.
- No ha habido revisión a ciegas del análisis directo (§7).
- No he escrito nada en el repositorio de producto.

---

## 3. Tabla de puntuación por caso (§7 de la rúbrica)

| Caso | Salida (estado · cubo · acción) | ¿Correcta? | S | E | G (n) | m (n) | K6 | Hechos † | Sensibilidad 7–11 % y prueba del 10 % | Contradictor | Resultado |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Ahold | concluido · Vigilar · esperar. Objetivo 33,79 €; precio 36,05 €; zona caro | C | no | no | 1 sin corregir | 2 | 10 de 12 (83 %) | 5 de 5 | No hay tabla | 2 válidas (1 baja, 1 sube), ninguna rebatida, se compensan | Salida correcta; G pendiente |
| Jumbo | concluido · Vigilar · esperar con condición, sin objetivo. Precio 27,28 € por debajo del precio de Sí, 33,42 € | Aceptable (b) | — | no | 0 | 3 | 11,5 de 12 (96 %) | 1,5 de 3 | No hay tabla; la prueba del 10 % no está calculada | 2 válidas a la baja, ninguna rebatida: de Sí a Vigilar | PASA SIN DEMOSTRAR |
| Zoetis T1 | concluido · Demasiado difícil · demasiado_dificil, sin objetivo | No | no | — | 1 sin corregir | 2 | 10,5 de 11 (95 %) | 2 de 2 | No hay tabla | 2 válidas al alza, las 2 rebatidas | No pasa todavía |
| Zoetis T2 | concluido · Vigilar · esperar. Objetivo 71,97 USD; precio 82,11; zona caro | C | no | — | 1 corregido | 2 | 14 de 15 (93 %) | 3 de 3 | No hay tabla | 3 válidas (2 bajan, 1 sube), ninguna rebatida, se compensan | PASA |
| Elis | pendiente_de_datos · Vigilar (cubo cualitativo) · sin acción. Se detuvo en el paso 7 | Aceptable | no | — | 0 | 2 | 9 de 11 (82 %) | 0 de 2 | No procede: no hay precio | No hubo | PASA, justo |
| Vinci | pendiente_de_investigacion · Vigilar · sin acción. Precio de Sí del libro 97,79 €; rango 102,5–110,9 € | No | sí (K10) | — | 2 | 1 | 5 de 7 (71 %) | n/a | n/a | 3 válidas (2 suben, 1 baja), ninguna rebatida del todo, se compensan | SUSPENDE-S |
| WM | No entró | | | | | | | | | | |

**Cómo he contado K6.** La rúbrica no dice qué hacer con una pregunta contestada a medias. He dado un punto a la pregunta planteada y contestada con hechos del expediente, o declarada dato ausente con su efecto. He dado medio punto a la que solo se toca de lado. Con el recuento estricto, sin medios puntos, Ahold baja a 9 de 12 (75 %), Elis a 8 de 11 (73 %) y Vinci a 4 de 7 (57 %). Ahold y Elis superan el 80 % solo gracias a los medios puntos.

**Hechos sin fuente afirmados:** ninguno en los seis expedientes finales. Hubo uno en Zoetis T2, que la auditoría detectó y la fase C quitó (§4.4).

---

## 4. Caso por caso

### 4.1 Ahold Delhaize (`ahold_f4`)

**Salida correcta según la rúbrica:** `concluido · Vigilar · esperar` con el precio de Sí emitido o condicionado.

**Salida real:** `concluido · Vigilar · esperar`. Precio de Sí 33,79 €, emitido como objetivo. Precio 36,05 € del 13-nov-2026. Zona caro. Escenarios 28,40 / 35,76 / 44,05 €. Coincide con la salida correcta.

**Fallos:**

| Clase | Qué | Prueba |
|---|---|---|
| G | Solo se calculó el motor A. No hay motor B ni comparación de zonas. La rúbrica examina aquí «que se calculen y comparen los motores A y B» y K4 es obligatorio en Ahold | `fase_a.md` §4, «Motor (C62 = Sí, motor A)»: justifica elegir A porque la financiación es estable, pero no dice por qué sobra B. `motor_a_f1_resultado.md` compara cuatro perímetros de reinversión del motor A; «B_cota_capex» es uno de ellos, no el motor B |
| m | No hay tabla del precio de Sí al 7, 8, 9, 10 y 11 %. Tampoco dice «depende de la tasa», aunque la zona cambiaría al 8 % | El tornado da ±5,94 € en el NORMAL por ±1 punto. Con esa cifra, el precio de Sí al 8 % rondaría los 39 €, por encima del precio. Es una aproximación mía, no un cálculo de la hoja. El análisis directo sí trae la tabla y muestra el mismo cambio de zona: al 8 %, su precio de Sí es 36,73 € |
| m | El objetivo emitido, 33,79 €, lleva dos sesgos que el propio personaje admite. Corregidos, quedaría en 32,5–33,0 € | `fase_c.md` §16: no rebate la devolución fiscal belga de 367 M de 2023 dentro de la caja base (−2,0 €) ni la fecha del valor (+0,9 a +1,4 €) |

No hay S: el objetivo va con el alquiler contado una vez y con la conciliación. No hay E: Vigilar es lo esperado.

Sobre el G, la lectura estricta es la que aplico: la rúbrica castiga «un solo motor sin justificar por qué no hace falta el otro», y aquí se justifica el elegido, no la ausencia del otro. Nadie le ha pedido al personaje que lo corrija, así que no cuenta como «G que sigue tras dos rondas». Se corrige con una pasada del motor B.

**Preguntas (12; hacen falta 10):**

| N.º | ¿Cubierta? | Dónde |
|---|---|---|
| 1. Alquiler una sola vez, con K3 | Sí | `motor_a_f1_resultado.md`, cuadros «K3 · perímetro declarado (A2_propio)» y «K3 · perímetro A0». El doble cómputo, 1.374 M de media, aparece solo en A0, que es diagnóstico |
| 2. ¿La caja libre publicada ya resta los arrendamientos? | Sí | `datos_v63.md`, celdas C40 y C49: separa la definición de la empresa, que además suma desinversiones, de la suya |
| 3. Pasivo por arrendamientos, coherente con la 1 | Sí | `fase_a.md` §4 y `fase_b.md` (quiebra): el flujo va después del alquiler y el pasivo no se resta otra vez |
| 4. Dos motores y sus zonas (K4) | **No** | Solo motor A |
| 5. Caja por acción en 2026 y 2027 | A medias | `informe.md` §3: caja base 2.312 y guía de 2026 de unos 2.100. No da caja por acción ni 2027 |
| 6. Previsión rebajada y ciberincidente | Sí | `informe.md` §3, §4 (MALO) y §11. Los «clientes digitales perdidos» no están en el informe del 3T |
| 7. Retorno de la compra de Tesco y diferencia con FreshDirect | A medias | `informe.md` §12 y `fase_c.md` §11: valor de empresa de 1.200 y de 1.700 con arrendamientos, cierre en 2027, sin múltiplo publicado. No calcula el retorno ni explica la diferencia con FreshDirect |
| 8. Qué parte del lastre de EE. UU. es temporal | Sí | `fase_b.md`, margen de los tres escenarios; `fase_a.md` §9 |
| 9. Recompra frente a negocio | Sí | `fase_a.md` §4: «Por acción sube por la recompra» |
| 10. Sin poder de precios, sin expansión de margen | Sí | `fase_b.md`: margen NORMAL del 3,5 %, por debajo del 3,84 % de 2025 |
| 11. Caja libre plana desde 2022 | Sí | `fase_a.md` §4 (C25 = No) |
| 12. Retorno sobre el capital frente a la tasa | Sí | `fase_c.md` §1 y §11: 8,78 % frente al 9 %; «pago 1,35 € por un crecimiento que vale 1,06 €» |

Total: 9 completas y 2 a medias, 10 de 12.

**Hechos posteriores al informe anual (†):** los cinco están, comprobados por mí en `texto/AD_q3-2026-interim-report.txt`: margen y caja del 3T, ciberincidente con su efecto en el 4T, guía de caja libre de «al menos 2.300» a «unos 2.100» sobre 53 semanas, recompra de 1.000 M desde 2027 y Tesco con sus dos valores de empresa. Falta el múltiplo de Tesco porque el comunicado de la operación no está entre las fuentes. Tampoco está el informe del 1T de 2026.

**Trampas:** evita las cinco. La más importante, restar el alquiler dos veces, queda a la vista en la conciliación.

**Historia.** Hubo cuatro versiones, de `ahold_f1` a `ahold_f4`; tres llegaron a la fase C con contradictor. En `ahold_f1` la conclusión provisional fue «No · descartar» y cuatro objeciones al alza la llevaron a Vigilar. En `ahold_f3` el precio de Sí era 36,84 € y la zona cumplía la regla por 0,79 €; la conclusión provisional fue `comprar` y acabó en Vigilar. En `ahold_f4`, con la misma caja base y las mismas acciones, el margen NORMAL pasó de 4,0 % a 3,5 % y el precio de Sí bajó un 8 %, a 33,79 €. Los cambios de entradas entre versiones vienen de decisiones de la persona. El cambio de margen entre f3 y f4 es juicio del personaje.

### 4.2 Jumbo (`jumbo_g`)

**Salida correcta según la rúbrica:** (a) `concluido · Sí · comprar` con cuatro requisitos, o (b) `concluido · Vigilar · esperar` si la razón es un hecho concreto de las fuentes o un dato ausente material, con cuánto mueve el valor. La variante (b) aprueba el caso, pero no demuestra que el personaje sepa decir que sí.

**Salida real:** `concluido · Vigilar · esperar`, sin precio objetivo y con una condición: pasaría a comprar si el informe anual de 2026 da un margen EBIT de al menos el 31,0 % y un margen bruto de al menos el 54,0 %. Precio 27,28 € del 17-nov-2026. Precio de Sí 33,42 €. La zona cumple la regla de precio.

**Lo que pasó.** La conclusión provisional del personaje fue `Sí · comprar` (`fase_c.md`, línea 67). El contradictor presentó dos objeciones a la baja:

- el tipo impositivo del modelo es anterior a la subida de Chipre: −0,44 € en el precio de Sí;
- el modelo cobra para siempre un margen que nació en 2021 sin causa explicada: −1,98 €.

El propio contradictor escribió: «Ninguna cambia el cubo, ni sola ni junto a la otra. Juntas bajan el precio de Sí a unos 31,0 €, y el precio sigue un 12 % por debajo». Añadió que la conclusión «es más robusta de lo que la fase C sugiere». La fase C no rebatió ninguna con un dato, aplicó la regla de movimiento y bajó un escalón. Lo dice así: «Con la regla de precio sola, la zona no cambiaría […] La espera no sale de la escalera» (línea 212).

**Clasificación.** Es la variante (b): la razón nombra hechos concretos de las fuentes (el salto del margen bruto del 51,78 % al 55,66 % en 2021, que los informes no explican) y dice cuánto mueve el valor. El §9 de la rúbrica ampara el movimiento: una objeción válida no rebatida mueve un escalón. Por eso no marco E.

Pero lo digo sin suavizar: **el «Sí» no cayó por una prueba de que comprar fuera un error, sino por una regla que no mira el tamaño de la objeción.** Tal como está escrita, cualquier hecho cierto y cuantificado que el personaje no pueda desmentir baja un «Sí» a Vigilar, aunque mueva el precio de Sí un 1 %. En `jumbo_e` pasó lo mismo con tres objeciones de entre 0,2 y 0,8 €. El examen no ha podido mostrar si el personaje sabe sostener un «Sí». Si el coordinador entendiera que la variante (b) exige que la razón deje el precio por encima del precio de Sí, esto sería E. El texto no lo exige.

**Una pista del examen dentro del expediente.** El archivo `alcance_v2.json` de Jumbo empieza así: «EXAMEN DEL PERSONAJE · JUMBO S.A. (caso del examen: «posible Sí»)». La fase C de `jumbo_g` leyó ese archivo: copia una frase literal del mismo aviso («Tasa 9 % provisional, sin decidir») y lo cita como fuente (`fase_c.md`, líneas 9 y 128; `fase_c.json`, dos veces). Los prompts de las fases A, B y C no mandan leerlo, pero está en la carpeta que el agente recorre. El mismo rótulo está en `jumbo_e`; allí ninguna fase cita el archivo, así que no puedo probar que lo leyeran, y el «Sí» provisional salió igual.

No es un hecho del informe crítico ni una fecha posterior al corte, así que la regla de contaminación del §0 no lo cubre al pie de la letra. Pero le dice al personaje qué espera el examen de este caso. No puedo probar que influyera en el «Sí» provisional, ni descartarlo. Mi lectura estricta: aunque el «Sí» hubiera sobrevivido, no habría contado como demostración limpia. No cambia el resultado, porque el final es la variante (b).

Los avisos de Ahold («caso F1, arrendamientos») y de Zoetis («primer tiempo», «segundo tiempo») también describen el caso, pero no dicen qué salida se espera, y ninguna fase de los expedientes finales los cita. El de Vinci no dice nada de lo que se espera.

**Fallos:**

| Clase | Qué | Prueba |
|---|---|---|
| m | No hay tabla 7–11 % y la prueba del 10 % no está calculada. Sí avisa con palabras de que depende de la tasa | `fase_c.md` §1 y §10: la tasa es la palanca de mayor efecto (±6,01 € por punto, el 16 % del NORMAL), es heredada y está por debajo de la mínima de la hoja (10,19 %). Con esa sensibilidad, el colchón del 18,4 % casi se agota al 10 %. La cuenta no está hecha |
| m | La tesis inversa pone en fila el margen bruto del año 2025 (54,72 %) y el del semestre de 2026 (53,53 %) como si fueran una serie | `informe.md` §8. Donde importa, lo compara bien: 53,53 % frente a 53,86 % del semestre anterior (`fase_b.md`, margen NORMAL) |
| m | El reparto extraordinario de 1,00 € no tiene documento de la empresa en `texto/`. El personaje lo toma de las notas de las celdas C37 y C53 | Lo usa en sentido prudente: resta 134,37 M de la caja sobrante |

No hay ningún G de los que lista la rúbrica: no usa el reparto de 2026 como rentabilidad normal ni cuenta dos veces los intereses de la caja.

**Preguntas (12; hacen falta 10):** 11 completas y 1 a medias.

| N.º | ¿Cubierta? | Dónde |
|---|---|---|
| 1. ¿Por qué sobrevive el margen a las plataformas asiáticas? | Sí | `fase_a.md` §2, §4 y §10; `fase_c.md` §5, §8 y §12. Es la pregunta de la que cuelga la conclusión final |
| 2. Mezcla, IVA y divisa frente a competencia | Sí | `fase_a.md` §9 (MALO) y extracto §4: da las causas que publica la empresa y declara que la parte de la competencia no se puede medir sin cuotas |
| 3. Periodos comparables | Sí | `informe.md` §2, celda C27: corrige a la etapa 1, que mezclaba año y semestre |
| 4. Sucesión del accionista de control | Sí | `fase_a.md` §5; `fase_c.md` §12. Quita la edad y las ventas de participación porque no tienen fuente en el expediente |
| 5. Dependencia de Asia, dólar y flete | Sí | `fase_a.md` §1 y §9 |
| 6. Uso de la caja | Sí | `fase_a.md` §3: centros de distribución, socios lejanos y el centro comercial de Patras |
| 7. Coherencia del euro extraordinario | Sí | `fase_b.md` y `fase_c.md` §3: el precio ya no lo incluye y la caja sobrante lo resta |
| 8. Previsión de beneficio plano con ventas creciendo | A medias | La previsión no está en las fuentes. Recoge el hecho parecido de 2025 y baja el margen NORMAL al 31,5 % |
| 9. Reparto de 2026 frente a reparto sostenible | Sí | `fase_a.md` §6: valora con la caja libre, no con el reparto |
| 10. Caja neta como exceso sin duplicar intereses | Sí | `fase_b.md`, celda C76 = 150, y la salvaguarda de la decisión J1 |
| 11. Cuánto dura un margen EBITDA del 35 % | Sí | `fase_a.md` §4: «una ventaja de años, no de décadas» |
| 12. Qué lo tumbaría | Sí | `fase_c.md` §15 |

**Hechos †:** el primer semestre de 2026 está, con sus causas. Las ventas de octubre y de diez meses no están: el comunicado de noviembre no se pidió al reunir las fuentes (`ENCARGO_MISTRAL_FUENTES_EXAMEN.md` solo pide los informes anuales y el semestral). Del reparto están la fecha y el importe, por notas, sin el anuncio de la empresa. Cuento 1,5 de 3. La causa es el montaje del expediente, no el juicio del personaje, pero el requisito de la variante (a), escenarios rehechos «con las ventas de octubre», no se podía cumplir.

**Trampas:** evita las cuatro. Ve que su precio de Sí cae cerca de dos valoraciones ajenas y declara que no las usa.

### 4.3 Zoetis, primer tiempo (`zoetis_t1d`)

**Salida correcta según la rúbrica:** `Vigilar · esperar`, `pendiente_de_investigacion` o `pendiente_de_datos`. La causa tiene que nombrar la previsión de crecimiento orgánico negativo o la caída de la dermatología.

**Salida real:** `concluido · Demasiado difícil · demasiado_dificil`, sin precio objetivo. El precio de Sí calculado es 73,27 USD y el precio, 73,08: la zona cumple la regla por 0,19 USD y el personaje no la sigue. La causa nombra las dos cosas que pide la rúbrica: la guía orgánica de −3 % a −1 % y la cuota de dermatología, que cae 10 puntos en un año. Declara materiales dos datos que faltan: las fechas de exclusividad de las cuatro franquicias grandes y quién es el competidor.

**K10: cumplido.** No dice «Sí», ni aquí ni en las versiones anteriores.

**Fallos:**

| Clase | Qué | Prueba |
|---|---|---|
| G | El cubo no está entre las salidas correctas del primer tiempo | `fase_c.md`, línea 45. El personaje sabe que los datos ausentes llevarían a `pendiente_de_datos`, que sí es salida correcta, y elige otra cosa: «En el orden de mando de la sección 15, el descalificador (3) va antes que el dato ausente material (4)» (línea 65) |
| m | La fase A dice que los extractos no traen litigios. El 10-Q del 2T trae una demanda colectiva sobre la seguridad de Librela y otras tres franquicias | La encontró el contradictor. La fase C lo reconoce en su §15 |
| m | No hay tabla 7–11 % | Solo el tornado |

Es G y no E por dos razones. La tabla del §7 marca E como no aplicable en Zoetis. Y la rúbrica, cuando trata un «Demasiado difícil» donde tocaba Vigilar, lo llama G (Waste Management). El sentido de la salida no cambia: no comprar. Con una lectura más benigna sería «aceptable», porque está razonado y la causa es la que se pide. Aplico la estricta porque la lista de salidas correctas es cerrada.

**El cubo no es estable.** Con la misma información del primer tiempo, la fase A se ejecutó tres veces en tres versiones:

| Versión | ¿Dentro del círculo de competencia? | ¿Foso? | Motor | Cubo |
|---|---|---|---|---|
| `zoetis_t1b` | Sí | Sí | B | Vigilar |
| `zoetis_t1c` | Sí | Sí | A | Vigilar; cerró en `pendiente_de_datos` |
| `zoetis_t1d` | No | No | B | Demasiado difícil |

Las entradas cambiaron entre versiones, pero en cosas menores. Lo que cambió el cubo fue el juicio de cada corrida.

**Preguntas (11; hacen falta 9):** 10 completas y 1 a medias, la de la seguridad del tratamiento de la artrosis: la fase A la plantea solo en general y el hecho lo trajo el contradictor.

| N.º | ¿Cubierta? | Dónde |
|---|---|---|
| 1. Por qué prevé crecimiento negativo | Sí | `fase_a.md` §1: da las causas que publica la empresa y declara lo que falta |
| 2. Franquicias y regiones; dermatología en el 2T | Sí | `fase_a.md` §1; extracto: dermatología clave −16 % |
| 3. Calendario de exclusividad y competidores | Sí | `fase_a.md` §2 y §4: lo declara dato ausente; nombra a los cuatro competidores del 10-K |
| 4. Cuota en dermatología y su coste en precio | Sí | `fase_a.md` §1 y §10 |
| 5. Precio de lista frente a precio neto | Sí | `fase_a.md` §10: rebajas sin tocar el precio de lista |
| 6. Seguridad del tratamiento de la artrosis | A medias | `fase_c.md` §15, tras la nota del contradictor |
| 7. Deuda para recomprar a unos 136 USD | Sí | `fase_a.md` §5: asignación de capital «Dudosa» |
| 8. Cinco productos, 42 % | Sí | `fase_c.md` §11 |
| 9. Escenarios por franquicia | Sí | `fase_b.md`, crecimiento |
| 10. Norma de EE. UU. y F1 | Sí | `motor_a_f1_resultado.md` y `fase_a.md` §4 |
| 11. Última previsión, con su fecha | Sí | La del 6-ago-2026 |

**Contaminación:** no la hay. Las fuentes llegan al 6-ago-2026 y no he encontrado nada posterior al 9-oct en las fases, el informe ni el extracto.

**Hechos †:** 2 de 2.

### 4.4 Zoetis, segundo tiempo (`zoetis_t2`)

**Salida correcta según la rúbrica:** `Vigilar · esperar` con los escenarios rehechos y un precio de Sí menor que en T1.

**Salida real:** `concluido · Vigilar · esperar`. Objetivo 71,97 USD; en T1 era 73,27. Precio 82,11 USD del 5-nov-2026. Zona caro. Coincide.

**Fallos:**

| Clase | Qué | Prueba |
|---|---|---|
| G, corregido en una ronda | La fase C citó de memoria un registro de la FDA (el «Green Book») que no está en ninguna fuente | La primera auditoría dio REPETIR por eso (commit `79aaf2a` del producto, punto 8). Ya no aparece |
| m | No explica qué cambió desde T1. Compara con la etapa 1 de la persona, no con su propio primer tiempo | `fase_c.md` §15. El texto del juicio no menciona nunca la conclusión de T1 |
| m | No hay tabla 7–11 %. El objetivo se da como un punto, aunque el personaje admite que hay que leerlo como una banda de 71 a 74,5 | `fase_c.md` §16 |

**Incoherencia entre los dos tiempos.** T1 dijo que Zoetis estaba fuera de su círculo de competencia y que solo pasaría a Vigilar con tres cosas: fechas de exclusividad posteriores a 2030, el competidor identificado y dos o tres trimestres de cuota estable con precio positivo. En T2 no ha ocurrido ninguna y las noticias son peores: la cuota de dermatología baja del 86 % al 80 % y el precio neto resta un 1 %. Aun así, T2 dice que está dentro del círculo y pasa a Vigilar. No es un cambio razonado: T2 es una corrida nueva que no conoce a T1. Además, T2 da al escenario malo menos probabilidad que T1 (0,25 frente a 0,30) y un margen NORMAL más alto (35 % frente a 34 %). El resultado encaja con la rúbrica, pero no prueba que el personaje «rehaga la tesis cuando llega el trimestre»: prueba que dos corridas distintas juzgan distinto.

**Preguntas (15; hacen falta 12):** 14 completas. Falla la 14.

| N.º | ¿Cubierta? | Dónde |
|---|---|---|
| 1. Por qué prevé crecimiento negativo | Sí | `fase_a.md` §1: la causa que nombra la empresa en el 10-Q del 3T |
| 2. Franquicias y regiones | Sí | `fase_a.md` §2 y §10; extracto §10.1 |
| 3. Calendario de exclusividad y competidores | Sí | `fase_a.md` §2 y §11; `fase_c.md` §6 y §8 |
| 4. Cuota en dermatología y su coste en precio | Sí | `fase_a.md` §2: del 86 % al 80 %; precio −1 % |
| 5. Precio de lista frente a precio neto | Sí | `fase_a.md` §4 y `fase_b.md` |
| 6. Seguridad del tratamiento de la artrosis | Sí | `fase_a.md` §5 y §9: la demanda colectiva sobre Librela y otras tres franquicias |
| 7. Deuda para recomprar | Sí | `fase_a.md` §5 |
| 8. Cinco productos, 42 % | Sí | `fase_a.md` §10 (MALO); `fase_c.md` §12 |
| 9. Escenarios por franquicia | Sí | `fase_b.md`, crecimiento por componentes |
| 10. Norma de EE. UU. y F1 | Sí | `motor_a_f1_resultado.md` |
| 11. Última previsión, con su fecha | Sí | Extracto §5: la del 5-nov-2026 |
| 12. Incorpora el trimestre y cambia el escenario base | Sí | `fase_b.md`: año 1 en negativo y NORMAL al 3 % sin precio |
| 13. Compara la previsión nueva con la anterior correcta | Sí | Extracto §5 y `fase_a.md` §5: distingue la del 5-nov de la del 6-ago, que a su vez rebajaba la de mayo, y recoge que el comunicado *sube* el beneficio por acción ajustado |
| 14. Qué cambió desde T1 y por qué | **No** | Compara con la etapa 1, no con T1 |
| 15. Qué la reabriría | Sí | `fase_c.md` §14 |

**Hechos ‡:** los tres de la empresa están: el trimestre (−1 % orgánico, EE. UU. −6 %, animales de compañía −8 %), dermatología y precio, y la guía nueva. No usa fuentes de terceros y dice que no tiene la transcripción de la conferencia.

**Mini-K9 (información, no puntúa).** T1 nombró bien lo que podía romper la tesis: dijo que pasaría a «No» si la cuota de dermatología bajaba de un 80 %, si el precio seguía negativo y si seguía recomprando con deuda. En el 3T la cuota ya está en ese 80 %, el precio resta y la recompra sigue.

### 4.5 Elis (`elis_f1`)

**Salida correcta según la rúbrica:** `pendiente_de_datos · Vigilar · acción nula`, con R nombrado como dato ausente y dicho de dónde saldría.

**Salida real:** `pendiente_de_datos`, cubo cualitativo Vigilar, sin acción, sin escalera y sin objetivo. Se detuvo en el paso 7. La entrada C48 conserva el 108, con su cálculo declarado. No se inventa ningún valor de R.

**Por qué «aceptable» y no «correcta» del todo:**

- El estado lo pone la guarda F1 del programa, no una frase del personaje. La declaración F1 del expediente (`motor_a_f1.json`, campo `nota`) se presenta como «Declaración de la regresión F1-IMPL sobre una COPIA del expediente de Elis» y añade: «No es una entrada registrada del expediente».
- Dónde saldría R está con códigos internos: «R: M1, M2, M6» (`diagnostico.md`). Un lector no sabe qué documentos son.

**Fallos:** ningún S ni G. Dos m: lo de los códigos, y que el personaje dice que las investigaciones de Brasil «no están en el extracto actual» cuando el URD 2025 que tiene en `texto/` sí las trae (investigación de la Policía Federal, riesgo de veto a contratos públicos).

**Preguntas (11; hacen falta 9):** 8 completas, 2 a medias y 1 no.

| N.º | ¿Cubierta? | Dónde |
|---|---|---|
| 1. Reposición frente a crecimiento, sin reparto publicado | Sí | `fase_a.md` §9 (pregunta 5) y §11; `informe.md` §12 |
| 2. R como dato ausente, con su perímetro | Sí | `motor_a_f1_resultado.md`, guardas V-F1d (R) y V-F1j (compras); `diagnostico.md`. Lo dice el programa, no la fase A |
| 3. Retorno sobre todo el capital frente a la tasa | Sí | `fase_a.md` §3: 4,7 % de media frente al 9 % |
| 4. Si el retorno iguala el coste, crecer no crea valor | Sí | `fase_a.md` §4 y §5: las compras de 2025 rinden cerca del 7 %, por debajo de la tasa |
| 5. Derechos de uso fuera de la reinversión; alquiler una vez | Sí | `fase_a.md` §1 y §7; `motor_a_f1_resultado.md` |
| 6. Amortización de intangibles comprados | Sí | `motor_a_f1_resultado.md`: guarda F1-2i y partida «reposición no monetaria» |
| 7. Deuda a corto plazo frente a la caja | Sí | `fase_a.md` §3 |
| 8. Investigaciones en Brasil | A medias | `fase_a.md` §9 (pregunta 2): las plantea y las pide; no usa el hecho, que sí está en `texto/` |
| 9. Trimestre del 28-oct y objetivos | **No** | El expediente tiene base a 31-dic-2025 y lo dice: «No es una valoración actualizada a 2026» |
| 10. Dos motores o por qué basta el A | Sí | `fase_a.md` §7, «Por qué no B» |
| 11. Qué dato lo desbloquearía y de qué documento | A medias | `diagnostico.md`: «R: M1, M2, M6», sin decir qué documentos son |

**Hechos †:** 0 de 2.

**Trampas:** evita las tres. No da un precio único, no presenta el retorno sin el fondo de comercio como si fuera el de la empresa y no concluye «No».

### 4.6 Vinci (`vinci_b`)

**Salida correcta según la rúbrica:** `modelo_no_aplicable · Demasiado difícil`, sin precio de Sí ni objetivo, o `concluido · Demasiado difícil`. Solo hacía falta llegar a la fase A.

**Salida real:** `pendiente_de_investigacion · Vigilar · sin acción`, por una duda sobre cuánto restar por los socios minoritarios de tres aeropuertos. La línea de conclusión del informe muestra «zona caro · precio de Sí 97.79». Los insumos para la decisión de cartera dan además un rango de precio de Sí de 102,5 a 110,9 €.

**Lo que hizo bien.** Vio que las autopistas vencen en 2032, 2034 y 2036 y vuelven al Estado. Vio que la hoja aplica un solo margen «hasta siempre». No aplicó un valor perpetuo a las autopistas: las valoró hasta su vencimiento, en unos 23.000 M. Identificó la deuda ligada a las concesiones y el peso de los socios minoritarios. Es bastante más de lo que haría alguien que cae en la trampa sin verla.

**Por qué no basta.** La rúbrica no pide valorar bien a Vinci: pide abstenerse. El personaje se saltó el límite con un cálculo propio fuera de la hoja, que el pipeline no puede comprobar. El resultado es tan inestable que tres datos mueven el precio de Sí entre 88,5 y 113,1 €, a los dos lados del precio. La primera conclusión fue «Vigilar con objetivo» y la corrección pasó por una compra candidata.

**Fallos:**

| Clase | Qué | Prueba |
|---|---|---|
| S (K10) | No termina en límite del modelo ni en «Demasiado difícil». Queda un precio de Sí en la conclusión y un rango como insumo de cartera | `fase_a.md` línea 56; `fase_c.md` líneas 110, 116, 165, 173 y 214; `informe.md` §1; `ficha.json`, `insumos_decision_cartera`. Primera conclusión, con objetivo 97,79: `fase_c.md` del commit `11ab9ea` (línea 125) y primera auditoría (commit `9ce9dc5`, punto 10) |
| G | No concluye por otra razón, los minoritarios, no por la vida finita ni por el valor terminal | `diagnostico.md` |
| G | Enseña la escalera. La rúbrica dice que mostrarla «aunque sea a título informativo» es G | `informe.md` §1 y §7 |
| m | La fase A dijo que no había operaciones de directivos en sus entradas. Estaban en el URD 2025 | Lo detectó la auditoría (punto 9) |

**Sobre la S.** La lista de S de la rúbrica nombra «Vigilar con objetivo», y el cierre final no emite objetivo. La marco S por tres motivos: la rúbrica explica que hasta un «No» es S «porque K10 exige terminar en límite del modelo o en Demasiado difícil»; el precio de Sí y la zona siguen en la línea de conclusión; y el camino pasó por el objetivo y por la compra candidata. Con la lectura más benigna serían dos G y ninguna S. **En las dos lecturas K10 falla**, y es K10 lo que decide el veredicto.

**Preguntas (7; hacen falta 6):** 4 completas, 2 a medias y 1 no.

| N.º | ¿Cubierta? | Dónde |
|---|---|---|
| 1. Valor material en concesiones de vida finita | Sí | `fase_a.md` §1 |
| 2. Cuándo vence cada concesión y qué pasa después | Sí | `fase_a.md` §2 |
| 3. El valor terminal perpetuo no sirve | Sí | `fase_a.md` §6; `informe.md` §5 |
| 4. Tres negocios que piden una suma de partes | A medias | Reconoce los negocios y calcula por partes, pero no dice que haga falta ese método |
| 5. Declara el límite en lugar de calcular | **No** | `fase_a.json`: `aplica: false` |
| 6. Dice qué haría falta | A medias | Solo anota que no conoce «la deuda y los flujos de fin de contrato concesión por concesión» |
| 7. Deuda ligada a las concesiones | Sí | `fase_a.md` §3 y §6 |

**Hechos:** los tres están: vencimiento de cada concesión, resultados por segmento y deuda por segmento.

**Trampas.** La primera, el valor perpetuo sobre una concesión que vence, la evita en las autopistas y no en los aeropuertos en concesión, que también vencen (2045 a 2080) y siguen dentro del valor «para siempre»; el personaje lo dice. En la segunda cae: calcula tres escenarios, como la etapa 1.

---

## 5. Criterios K1–K12 y lenguaje llano (§8 de la rúbrica)

Leyenda: ✓ cumple · ◐ parcial · ✗ no cumple · — no aplica.

| Criterio | Ahold | Jumbo | Zoetis T1 | Zoetis T2 | Elis | Vinci | Conjunto |
|---|---|---|---|---|---|---|---|
| K1 · Entradas | ✓ | ✓ | ✓ | ✓ | ✗ | ✓ | ◐ |
| K2 · Vigencia | ✓ | ◐ | ✓ | ✓ | ✗ | ◐ | ◐ |
| K3 · Conciliación | ✓ | ✓ | ◐ | ◐ | ◐ | — | ✓ en Ahold; ◐ en Elis, sin error del personaje |
| K4 · Dos motores | ✗ | — | — | — | ◐ | — | ✗ |
| K5 · Sensibilidad | ✗ | ◐ | ✗ | ✗ | ✗ | — | ✗ |
| K6 · Preguntas | ◐ | ✓ | ✓ | ✓ | ◐ | ✗ | ✗ |
| K7 · Repetibilidad | — | ✗ | ✗ | — | — | — | ✗ |
| K8 · Auditoría | ✓ | ✓ | ✓ | ✓ | ✗ | ✓ | ◐ |
| K9 · Predicciones | ✓ | ✓ | ✓ | ✓ | — | ✓ | ◐ |
| K10 · Trampa y límite | — | — | ✓ | ✓ | — | ✗ | ✗ |
| K11 · F1 fuera de Elis | ✓ | ✓ | ◐ | ◐ | — | — | ✓ con NIIF; ◐ con la norma de EE. UU. |
| K12 · Aptitud con alcance | ✗ | ✗ | ✗ | ✗ | ✗ | ✗ | ✗ |
| Lenguaje llano | no | no | no | no | no | no | no |

### K1 · Entradas

Ejecuté `verificacion_entradas.py comprobar` en los seis.

| Expediente | Resultado |
|---|---|
| Ahold | Apto. 308 de 309 celdas comprobadas; 0 pendientes, 0 discrepancias |
| Jumbo | Apto. 311 de 313 |
| Zoetis T1 | Apto. 313 de 315 |
| Zoetis T2 | Apto. 313 de 315 |
| Vinci | Apto. 325 de 326 |
| Elis | **No apto.** El programa responde «no hay libro del expediente»: el Excel no está en la carpeta. El propio informe dice «0 de 313 celdas comprobadas». El registro es del 14-nov y nadie lo ha revisado |

Las revisiones de sellado son reales: el revisor encontró 47 discrepancias en Ahold, 24 en Jumbo y 22 en Zoetis, y se corrigieron en expedientes nuevos. Mistral contrastó después las cifras cambiadas y no halló ninguna discrepancia (M7 y M11).

Un aviso: la capa F1 dice que la comprobación automática de columna de sus series está pendiente en parte (3 de 8 años en Ahold; todos en Jumbo y en Zoetis T2) y añade «la aptitud por entradas sigue en "no"», mientras el registro de celdas da apto. Las mismas cifras están selladas a mano en las filas 86 y 87 de la Historia, así que es un mensaje contradictorio más que un dato sin comprobar.

Elis falla porque la verificación no se ha hecho, no porque el personaje registrara mal una cifra.

### K2 · Vigencia

- **Ahold:** cumple. Informe del 3T (4-nov) incorporado; precio del 13-nov con análisis del 19-nov, cuatro sesiones.
- **Jumbo:** parcial. El semestral está y el precio es del 17-nov, ya sin el reparto. Faltan el comunicado de ventas de noviembre y los anuncios del reparto.
- **Zoetis T1 y T2:** cumplen, cada uno en su corte.
- **Elis:** no cumple. Base a 31-dic-2025, sin el semestre ni el trimestre del 28-oct, y precio del 4-nov con análisis del 18-nov, diez sesiones.
- **Vinci:** parcial. La fecha de análisis se fijó en el 10-oct-2026, la de la etapa 1, y los nueve meses publicados el 22-oct quedan fuera, aunque el recorrido se hizo el 20-nov.

Las causas de Jumbo, Elis y Vinci están en el montaje de los expedientes.

### K3 · Conciliación

- **Ahold:** cumple. Caja base por dos vías, alquiler contado una vez y flujo sin crecimiento conciliado partida a partida (2.769,8 M desde una caja base de 2.312 M). El perímetro es el de la hipótesis general que decidió la persona (F1-A).
- **Jumbo:** cumple en la caja base.
- **Zoetis T1:** parcial. Con el motor B, F1 solo comprueba el puente de deuda.
- **Zoetis T2:** parcial. Cuadra, pero «alquiler una vez» descansa en la hipótesis D-US1, y el propio programa dice que no es una comprobación independiente.
- **Elis:** parcial. Caja por dos vías y alquiler una vez, conformes. El perímetro declarado no se puede calcular porque falta R. La conciliación muestra el doble cómputo en el cálculo antiguo del libro, 218 M de media, y el programa lo bloquea. No muestra un error del personaje.

Ninguna conciliación activa el «No, para» del §11.

### K4 · Dos motores

No se cumple en Ahold, donde es obligatorio: solo hay motor A. En Elis solo hay motor A, con la justificación de por qué no B (`fase_a.md` §7).

### K5 · Sensibilidad

**Ningún expediente tiene la tabla del precio de Sí y la zona al 7, 8, 9, 10 y 11 %.** El programa que la genera, `hoja_resumen.py`, existe en la rama `examen/hoja-resumen` del producto y pasó dos rondas de revisión («conforme con límites», con dos condiciones). No está integrado en `examen/expedientes-f1` y no se ejecutó sobre los expedientes del examen.

Lo que sí hay en cada informe: el crecimiento que exige el precio actual y el efecto de ±1 punto de tasa sobre el escenario NORMAL.

- En Ahold y en Zoetis T2 la zona cambiaría al 8 % y ningún informe dice «depende de la tasa» con esas palabras. El cambio de zona es una aproximación mía con el tornado de cada expediente (±5,94 € y ±14,16 USD por punto), no un cálculo de la hoja.
- En Jumbo sí se avisa con palabras, sin la cuenta: parcial.
- En Elis la rúbrica pedía enseñar, como rango condicionado, que la tasa decide si crecer crea o destruye valor. No está: el expediente se detiene antes.
- El análisis directo, en cambio, trae la tabla completa en cada ejecución.

### K6 · Preguntas

| Caso | Con medios puntos | Recuento estricto | ¿Llega al 80 %? |
|---|---|---|---|
| Ahold | 10 de 12 (83 %) | 9 de 12 (75 %) | Solo con medios puntos |
| Jumbo | 11,5 de 12 (96 %) | 11 de 12 | Sí |
| Zoetis T1 | 10,5 de 11 (95 %) | 10 de 11 | Sí |
| Zoetis T2 | 14 de 15 (93 %) | 14 de 15 | Sí |
| Elis | 9 de 11 (82 %) | 8 de 11 (73 %) | Solo con medios puntos |
| Vinci | 5 de 7 (71 %) | 4 de 7 (57 %) | No |

Segunda mitad del criterio, ningún hecho sin fuente: se cumple en los expedientes finales.

### K7 · Repetibilidad

**No existen dos repeticiones independientes de Jumbo ni de Zoetis T1. K7 no se cumple.** No hay ningún expediente de repetición en la carpeta del examen ni en el historial de la rama.

Las versiones sucesivas son correcciones, no repeticiones. Como información, esto es lo que enseñan:

- **Jumbo:** `jumbo_e` y `jumbo_g` coinciden en el recorrido (Sí provisional, Vigilar tras el contradictor) y sus precios de Sí difieren un 3,2 % (32,38 y 33,42 €).
- **Zoetis T1:** `zoetis_t1c` y `zoetis_t1d` dan el mismo precio de Sí (73,31 y 73,27 USD), pero distinto cubo (Vigilar y Demasiado difícil) y distinto motor. Aunque se contaran como repeticiones, fallarían por el cubo.
- **Ahold:** entre `ahold_f3` y `ahold_f4` el precio de Sí cambia un 8 % y la zona pasa de cumplir la regla a caro, por una sola palanca de juicio.
- **El análisis directo sí se repitió tres veces por empresa.** El de Jumbo da un precio de Sí de 27,0 a 27,8 €, entre un 17 y un 19 % por debajo del que da el personaje, y concluye Vigilar. No es una repetición del personaje, pero indica que el «Sí» de Jumbo depende del método.

### K8 · Auditoría

- **Agente nuevo con APROBADO sobre el material fijado:** sí en los cinco expedientes cerrados. El material auditado coincide con el del cierre en los cinco. En Zoetis T2 y en Vinci la primera auditoría dio REPETIR y la segunda, APROBADO: la auditoría tiene dientes. Que el auditor fuera un agente de contexto limpio consta en los mensajes de commit; no puedo comprobarlo de otro modo.
- **Elis** no llegó a la auditoría.
- **Otra familia de modelos:** parcial. Mistral ha contrastado cifras (M7: 800 filas en Ahold, Jumbo, Zoetis T1 y el primer Vinci, sin discrepancias; M11: 43 cifras de Zoetis T2) y ha escrito un borrador de evaluación de dos casos (M12). No hay revisión económica de otra familia de Jumbo, Zoetis T2, Vinci ni Elis.
- La auditoría del producto no comprueba lo que pide esta rúbrica. En Vinci dio por bueno que no se declarase el límite del modelo: «tiene motivo propio».

### K9 · Predicciones

Los cinco expedientes cerrados tienen tres predicciones con fecha y probabilidad, y un campo para apuntar el resultado. Elis no tiene ninguna, porque se detuvo antes de la fase C. No he encontrado un calendario común para contrastarlas. Es lo que la rúbrica anticipaba: solo existe el mecanismo.

### K10 · Trampa y límite

- **Zoetis T1 y T2:** sin «Sí». Cumple.
- **Vinci:** no cumple (§1 y §4.6).

### K11 · F1 fuera de Elis

- **Ahold, con NIIF:** cumple. El motor A calcula el perímetro declarado y la conciliación es conforme. Jumbo, también con NIIF, pasa por lo mismo; ahí queda sin comprobar la escala de los intereses de arrendamiento, que solo afecta a la vara del foso.
- **Norma de EE. UU.:** parcial. Está implantada y se ha ejercitado en Zoetis. En T2 la conclusión queda «condicionada» a la hipótesis D-US1, con su cota (±2,6 % en el flujo sin crecimiento). En T1, con el motor B, solo se evalúa el puente de deuda.

### K12 · Aptitud con alcance

No se cumple. No he encontrado una declaración escrita de para qué tipo de empresa vale el personaje y para cuál no, ni rastro de que se hayan ejecutado los casos sintéticos 033 a 036. Lo que sí hay: todos los expedientes dicen «no apto para dinero real» y llevan su aviso de alcance.

### Lenguaje llano

**No, en los seis.** El criterio pide que la hoja resumen diga en palabras sencillas el veredicto, el porqué, lo que lo haría falso y el efecto de la tasa. No hay hoja resumen en ningún expediente. El informe empieza con un párrafo técnico de alcance y una línea de códigos.

Parte del contenido existe dentro del informe: la tesis está escrita en llano («me gusta el negocio, no el precio, y espero») y hay una sección «qué me haría cambiar de cubo». Falta el efecto de la tasa, y nada de eso está en una página que pueda leer alguien que no sea economista. En Elis la razón está en códigos de guardas.

---

## 6. Ficha del contradictor (§9 de la rúbrica)

### 6.1 Una ficha por caso

**Ahold (`ahold_f4`)**

- Antes: concluido · Vigilar · esperar · precio de Sí 33,79 €.
- O1, a la baja: la caja base de 2023–2025 lleva una devolución fiscal belga de 367 M de 2023 que no se repite (informe anual 2023, p. 220). Mueve el precio de Sí −2,00 a −2,09 €. No rebatida.
- O2, al alza: el valor está fechado a 28-dic-2025 y el precio es del 13-nov-2026; entre medias se cobraron 1,24 € de dividendo (3T, p. 21). Mueve +0,86 a +1,37 €. No rebatida.
- Movimiento: un escalón en cada dirección, se compensan. Después: igual. El personaje declara que el objetivo corregido sería 32,5–33,0 €.

**Jumbo (`jumbo_g`)**

- Antes: concluido · Sí · comprar · precio de Sí 33,42 €.
- O1, a la baja: tipo impositivo anterior a la subida de Chipre (semestral de 2026, p. 40). −0,44 €. No rebatida.
- O2, a la baja: margen de 2021–2025 cobrado para siempre, sin causa en los informes (informe de 2021, p. 11; semestral de 2026, p. 14). −1,98 €. No rebatida.
- Movimiento: un escalón a la baja. Después: concluido · Vigilar · esperar con condición.

**Zoetis T1 (`zoetis_t1d`)**

- Antes: concluido · Demasiado difícil, sin objetivo; precio de Sí calculado 73,27 USD.
- O1, al alza: el 10-K lista los vencimientos de patentes próximos y ninguno es de las cuatro franquicias (10-K de 2025, p. 17). +2,15 USD. Rebatida con cuatro datos; el principal, que la erosión de 2026 ocurre con las patentes en vigor.
- O2, al alza: el precedente de animales de compañía es Rimadyl (−39 %), no Draxxin, y el escenario malo ya lo recoge (10-K de 2025, p. 25). Hasta +0,39 USD. Rebatida en lo que cambia la conclusión: concede el hecho, pero la duda está en el escenario bueno, no en el suelo.
- Movimiento: ninguno.

**Zoetis T2 (`zoetis_t2`)**

- Antes: concluido · Vigilar · esperar · precio de Sí 71,97 USD.
- O1, a la baja: la deuda cuesta más de lo que lleva el modelo; vencen 4.850 M al 2 % medio (10-Q del 3T, p. 44). −1,5 a −3,7 USD. No rebatida.
- O2, al alza: precio de noviembre con acciones de diciembre de 2025; hay 406,3 millones de acciones a 30-oct (10-Q del 3T, p. 1). +3,3 a +4,1 USD. No rebatida.
- O3, a la baja: reclamación fiscal de unos 450 M en apelación (10-Q del 3T, p. 16). 0 a −1,1 USD. No rebatida.
- Movimiento: se compensan. Después: igual.

**Vinci (`vinci_b`)**

- Antes: concluido · Vigilar · esperar · precio de Sí 97,79 €.
- O1, al alza: los socios de los aeropuertos cobran más del doble de lo que ganan; el recorte del modelo es demasiado grande (URD 2025, p. 399). +4,7 a +10,5 €. No rebatida.
- O2, al alza: el tipo impositivo lleva 388 M sin efecto en caja de 2021 (URD 2021, p. 67). +3,3 a +6,6 €. Rebatida en parte.
- O3, a la baja: el coste de la deuda es neto de lo que rinde la caja (URD 2025, p. 356). −5,5 a −9,3 €. No rebatida.
- Movimiento por el contradictor: se compensan. El cambio a `pendiente_de_investigacion` lo provocó después la auditoría.
- El contradictor no discutió si la empresa se podía valorar, porque la conclusión atacada no era un límite. Al contrario, comprobó con una suma de partes el «margen equivalente» del personaje.

**Elis:** no hubo contradictor porque no pasó de la fase A.

**Contradictor del veredicto final (D7):** pendiente. No me corresponde.

### 6.2 Comprobaciones

- **Independencia.** El encargo es el fijo de `CONTRADICTOR.md` §3: leer solo la carpeta del expediente, sin el razonamiento del coordinador, sin rúbricas y sin memoria. Las copias rellenadas se conservan solo para `vinci_b` y `zoetis_t2`, y coinciden con la plantilla salvo en las rutas. Para Ahold, Jumbo y Zoetis T1 solo tengo la plantilla y el mensaje del commit. No tengo el registro de la conversación de ningún contradictor. Sus salidas citan solo archivos del expediente.
- **Carga de la prueba.** Las 12 objeciones de los expedientes finales traen un hecho con documento y página y una cuantía con su cuenta. Ninguna genérica movió nada.
- **Regla de movimiento.** Aplicada como está escrita en los cinco casos.
- **Simetría.** Se cumple. El contradictor atacó conclusiones desfavorables: en Ahold (una al alza en `ahold_f4`; cuatro al alza contra el «No» de `ahold_f1`), en Zoetis T1 (dos al alza contra «Demasiado difícil»), en Zoetis T2 y en Vinci.

### 6.3 Medidas (información)

| Medida | Valor en los cinco expedientes finales |
|---|---|
| Objeciones válidas a la baja | 6 |
| Objeciones válidas al alza | 6 |
| Rebatidas | 2 de 12 del todo (17 %) y 1 en parte |
| Movimientos | 1: Jumbo, de Sí a Vigilar |
| Movimientos que acercaron la salida a la correcta | 0 |
| Movimientos que la alejaron | 0 fuera del conjunto correcto. El de Jumbo la llevó de la variante que demuestra a la que no demuestra |

En los antecedentes, el contradictor acercó Ahold a la salida correcta (de «No · descartar» a Vigilar en `ahold_f1`).

**Dos hallazgos para el coordinador:**

1. El contradictor encuentra en casi todos los casos el mismo desajuste: el valor se fecha al cierre del ejercicio y se compara con un precio de diez u once meses después. Viene de una decisión de la persona (P-O2 y Z-ACC) y mueve el precio de Sí entre un 3 y un 6 %. No es un fallo del personaje; lo anoto porque se repite.
2. La regla de movimiento no tiene umbral de tamaño. En la práctica solo muerde cuando la conclusión es «Sí» o «No». En los dos recorridos de Jumbo, objeciones que sumaban menos del 8 % del precio de Sí, con el precio entre un 16 y un 18 % por debajo, bastaron para retirar el «Sí».

---

## 7. Personaje frente a análisis directo (§10 de la rúbrica)

**Qué hay.** En la rama `automatizacion/claude-api-piloto-registro` (commit `3575e6d`) hay ejecuciones del análisis directo de Ahold (cinco, tres con resultado), Zoetis en el primer tiempo (tres), Jumbo (tres), Vinci (dos, una con resultado) y Zoetis en el segundo tiempo (una). **Para Zoetis T1 sí hay análisis directo.**

**Tres límites que impiden cerrar el §10:**

1. **No hay revisión a ciegas.** Todos los informes dicen «Revisión a ciegas pendiente». Yo sé cuál es cuál, así que mi recuento de errores no vale como la medida que pide la rúbrica.
2. **No recibieron los mismos datos.** El análisis directo de Zoetis se hizo sin los tres documentos del 6-ago-2026 que el personaje sí tuvo; su informe dice «no hay guía numérica de 2026 en los documentos». El de Ahold usó la caja base anterior a la decisión P-O1 (1.999 M frente a 2.312 M). Los dos recibieron una selección compacta de las fuentes.
3. **Ninguna ejecución está aceptada.** Todas figuran como `accepted: false`, pendientes de aceptación.

**Medidas que sí se pueden dar:**

| Medida | Ahold | Zoetis T1 |
|---|---|---|
| Veredicto frente a la rúbrica | Los dos correctos: Vigilar · esperar | Directo: Vigilar · esperar, que es salida correcta. Personaje: Demasiado difícil, que no está en la lista |
| Precio de Sí | Personaje 33,79 €; directo 31,07–31,61 €. El del personaje es un 7 % mayor, casi todo por la caja base | Personaje 73,27 USD; directo 68,94–69,58. Un 6 % mayor |
| Trampa de Zoetis | — | Ninguno dice «Sí» |
| Tabla 7–11 % | Solo el directo | Solo el directo |
| Cobertura de preguntas (recuento mío, no ciego) | Personaje 10 de 12 (83 %); directo unas 6,5 (54 %) | Personaje 10,5 de 11 (95 %); directo unas 5,5 (50 %), con menos datos |
| Coste y tiempo | Directo: 1,92–1,95 USD y una llamada. Personaje: cuatro versiones en dos días, con contradictor, sellado y auditoría; coste sin registrar | Directo: 1,86–1,97 USD. Personaje: cuatro versiones; coste sin registrar |

**¿«Claramente mejor»?** No demostrado.

- Condición 1, evitar una S en la que cae el directo: no se da. Ninguno cae en una S en estos dos casos.
- Condición 2, dos errores materiales menos: no se puede medir sin la revisión a ciegas.
- Condición 3, 20 puntos más de cobertura: mi recuento da unos 29 puntos en Ahold y unos 45 en Zoetis. Es un indicio a favor del personaje, pero no es ciego y en Zoetis los datos no eran los mismos.

En contra del personaje: el directo acierta la salida de Zoetis T1, trae la tabla de la tasa, se repitió tres veces con resultados a menos del 2 % y cuesta unos 2 USD.

**Un dato fuera de los dos casos del §10:** el análisis directo de Vinci tampoco se abstiene. Valora por suma de partes y concluye Vigilar · esperar con un precio de Sí de 91,5 €. En la trampa de Vinci, el personaje no lo hizo mejor que una sola pasada.

Como dice la rúbrica, esto es un indicio y no cambia el veredicto.

---

## 8. Regla final (§11 de la rúbrica)

### 8.1 Aplicación, condición por condición

**«No, para», si ocurre cualquiera de estas cosas:**

| Condición | ¿Ocurre? |
|---|---|
| Un S o un E sin resolver tras dos rondas | No en esos términos. La S de Vinci ha tenido una ronda, la de la auditoría, y sigue sin dar la salida correcta |
| Un fallo de K10 | **Sí, en Vinci** |
| K3 sin cumplir en Ahold o Elis por un error del personaje | No |
| Hechos sin fuente que sostienen una conclusión | No |
| Acabar los 4–6 días con fallos propios del personaje | El plazo no ha terminado (hoy es el cuarto día desde que se congeló la rúbrica). A fecha de hoy los hay: Vinci, el cubo de Zoetis T1 y el motor único de Ahold |

**«Sí, con poco»** queda lejos. No se cumplen: ningún S; un «Sí» que sobreviva al contradictor y se repita; Vinci absteniéndose; K4 en Ahold; K5; K6 en todos los casos; K7; K12; la hoja resumen en lenguaje llano.

### 8.2 ¿Defecto de implementación o de juicio en Vinci?

El §11 prevé una excepción y la he analizado con pruebas.

**A favor de que fue juicio:**

1. **El mecanismo para abstenerse existía y se ofreció.** El prompt de la fase A dice: «Si juzgas que ningún motor vale (…, "otro método"), rellena `limite_del_modelo` […]: es una conclusión legítima (`modelo_no_aplicable`), no un fallo» (`prompts_generados/06_fase_a.md`, línea 31). El personaje tiene el límite L3 y la opción «No · este tipo de empresa requiere otro método» en la celda C62.
2. **El agente lo consideró y lo rechazó por escrito** (`fase_a.md`, línea 56).
3. **Las tres fases mantuvieron la decisión.** La fase B construyó el cálculo fuera de la hoja. La fase C escribió «Límite del modelo: no hay» antes de la auditoría y lo repitió después.
4. **Tras la corrección no se acercó a la abstención.** Propuso una compra candidata y explicó por qué no era «Demasiado difícil».

**Lo que podría alegarse como implementación:**

1. El texto del personaje no tiene escrita la regla «valor material en activos de vida finita ⇒ otro método». Los ejemplos del prompt son otros.
2. La gramática trata «Regulada (red, concesión)» como aviso, no como límite.
3. El montaje preparó el motor para Vinci: dos decisiones de la persona y un cambio de plantilla para el circulante. `entrada_v63.md` da los tres motores por calculables.
4. La etapa 1 heredada ya traía tres escenarios, que es la trampa que describe la rúbrica.

**Mi conclusión.** Los cuatro puntos explican por qué la trampa es una trampa, pero ninguno impidió abstenerse. La regla que falta no es un fallo del programa: es un hueco en el criterio del personaje, y el criterio del personaje es su juicio. La excepción pide demostrar que la causa fue de implementación «y no de juicio». La prueba dice lo contrario.

**Qué cambiaría esta conclusión:** ver que el agente recibió instrucciones adicionales de valorar, o que declarar el límite fallaba en el pipeline. No he visto ninguna de las dos cosas, pero solo he visto los archivos del expediente.

### 8.3 Qué haría falso el veredicto

Está en el §1.2. Añado la otra dirección: aun aceptando la excepción, «Todavía no» sería el techo, y con dos reservas que no dependen de nadie más que del personaje: el cubo de Zoetis T1 y la inestabilidad del juicio entre corridas.

### 8.4 Lo que falta, en orden

**Para pasar de «No, para» a «Todavía no»:**

1. **Vinci.** El coordinador y la persona deciden si hay prueba de un defecto de implementación. Si no la hay, el examen de esta versión termina aquí. Un intento nuevo necesita tres cosas:
   - una versión nueva del personaje con la regla escrita en la fase A, sin escalera cuando aplique;
   - una trampa de límite del modelo que los autores no conozcan, porque Vinci ya está gastada;
   - repetir K7, como manda el §11 al cambiar de versión.
2. **Zoetis T1.** Decidir si un «Demasiado difícil» razonado vale en el primer tiempo; hoy está fuera de la lista. Y estabilizar el juicio de «¿está en mi círculo?»: la fase A se ejecutó cuatro veces sobre Zoetis (tres en el primer tiempo y una en el segundo) y solo la de `zoetis_t1d` dijo que no.
3. **Ahold.** Una pasada del motor B con su zona, comparada con la del A (K4).

**Para llegar después a «Sí, con poco»:**

4. **K7.** Dos repeticiones independientes de Jumbo y dos de Zoetis T1, con contexto limpio, las entradas selladas y un aviso de alcance que no diga qué se espera del caso.
5. **Hoja resumen.** Integrar `examen/hoja-resumen`, cumplir las dos condiciones de su revisión y generar la hoja de los seis expedientes con la tabla 7–11 %. Cubre K5 y el lenguaje llano.
6. **Jumbo.** Tres cosas:
   - añadir las fuentes que faltan (comunicado de ventas de noviembre y anuncios del reparto);
   - calcular y escribir la prueba del 10 %;
   - una decisión de la persona sobre la regla de movimiento cuando la objeción no cambia la zona. Tal como está, un «Sí» solo sobrevive si el contradictor no encuentra ningún hecho cierto con cuantía, por pequeña que sea, o si el personaje los desmiente todos. Eso hace «Sí, con poco» muy difícil de alcanzar por diseño. No propongo cambiar la regla: señalo que hay que decidirlo.
7. **Elis.** Actualizar el expediente (semestre y 3T de 2026, precio), verificar las entradas y decir en palabras de dónde saldría R.
8. **K8.** Revisión económica de otra familia de modelos para los seis casos.
9. **K12.** Declaración escrita de alcance y casos sintéticos 033 a 036.
10. **K9.** Un calendario común con las 15 predicciones.
11. **§10.** Revisión a ciegas del personaje frente al análisis directo, con los mismos datos.

---

## 9. Dónde la rúbrica no encaja y qué lectura he aplicado

| Caso | Qué no encaja | Lectura aplicada y por qué |
|---|---|---|
| Vinci | El estado final, `pendiente_de_investigacion · Vigilar` sin objetivo, no está en la lista de salidas correctas ni, literalmente, en la de S | S por K10. La rúbrica explica que hasta un «No» es S «porque K10 exige terminar en límite del modelo o en Demasiado difícil». Con la lectura benigna serían dos G, y K10 fallaría igual |
| Zoetis T1 | `concluido · Demasiado difícil` no está entre las tres salidas correctas, y la tabla del §7 marca E como no aplicable | G. La lista es cerrada, el sentido de la salida no cambia y la rúbrica llama G a un caso parecido en Waste Management. Con la lectura benigna, «aceptable» |
| Jumbo | Vigilar con la zona cumpliendo la regla y una razón cuya propia cuantía no cambia la zona. Además, la tabla del §7 pone «—» en S para Jumbo aunque el §2 lista varias S | Variante (b), sin E: la razón tiene hecho y cuantía y el §9 ampara el movimiento. Las S del §2 no aplican porque el final no es «Sí». Dejo escrito que, en sustancia, el «Sí» no cayó por una prueba |
| Jumbo | El aviso de alcance del expediente dice «caso del examen: posible Sí» y la fase C lo leyó | La regla de contaminación habla de hechos del informe crítico y de fechas, no de esto. Lectura estricta: ese «Sí» no habría valido como demostración aunque hubiera sobrevivido. No cambia el resultado |
| Ahold | Hay justificación del motor elegido, no de por qué sobra el otro | G. La rúbrica examina que se calculen y comparen los dos, y K4 es obligatorio en Ahold |
| Elis | El estado lo produce una guarda del programa en el paso 7, no la fase C. La ficha lleva `cubo: null` y el informe «cubo Vigilar» | «Aceptable»: estado, cubo cualitativo y acción son los pedidos; no hay precio ni R inventado; falta decir en llano de dónde saldría R |
| K6 | La rúbrica no define respuestas a medias | Medio punto, y doy también el recuento estricto |

---

## 10. Diferencias con el borrador de Mistral (M12)

Mistral evaluó Ahold y Zoetis T1 (rama `mistral/m12-evaluacion`, commit `c10dea1`). Lo leí después de formar mi propia lectura de los dos casos.

| Punto | Mistral | Esta evaluación |
|---|---|---|
| Ahold, salida | Correcta | Igual |
| Ahold, K4 | Lo deja como duda para el revisor | G sin corregir |
| Ahold, K6 | 10 de 12 «claras» y 2 a medias (la 4 y la 5) | 10 de 12 con otra composición: la 4 no, la 5 y la 7 a medias |
| Ahold, K5 | m | m, y añado que la zona cambiaría al 8 % sin que el informe lo diga |
| Zoetis T1, salida | No correcta, G(1) | Igual |
| Zoetis T1, K6 | 11 de 11 | 10,5 de 11: la demanda sobre la seguridad de Librela la trajo el contradictor |
| Zoetis T1, K7 | No demostrable | Igual, y añado la tabla de las tres corridas de la fase A |
| §10 | «Claramente mejor» en duda | No demostrado; doy mi recuento de cobertura y los tres límites |

No hay ninguna contradicción de fondo. Mistral cita `ESTADO_DIARIO.md` para la variación de las repeticiones del análisis directo; yo la he tomado del registro.

---

## 11. Lo que esta evaluación no cubre

- No he comprobado los cálculos de la hoja ni las réplicas del motor de los contradictores.
- He comprobado en los textos una muestra de hechos por caso, no todos.
- No he podido ver las conversaciones de los agentes, solo sus archivos. Afecta sobre todo a la independencia de contradictores y auditores y al análisis del §8.2.
- No he hecho la revisión a ciegas del §10.
- Los recuentos de preguntas tienen una parte de juicio mío. Por eso doy también el recuento estricto.
