# Rúbrica del examen del personaje Munger V2

**Estado: CONGELADA** por el coordinador el 17-nov-2026, antes de ejecutar ninguna fase de juicio de ningún caso. Redactada por un agente distinto; el coordinador cambió dos puntos antes de congelar (§11: K1 incompleto por la verificación pendiente lleva a «Todavía no», no a «No, para»; §12.4: respuesta sobre los datos de entrenamiento). Desde ahora no se toca: cualquier cambio va en una adenda fechada, con su motivo, que no puede depender de ningún resultado ya visto. Huella: `RUBRICA_EXAMEN.sha256` (SHA-256 de este archivo tal como queda congelado, en el commit que lo congela).

**Quién la usa.** Solo quien evalúa, que tiene que ser un agente distinto del que preparó o corrigió el personaje. **Los agentes del personaje no la ven nunca**, ni tampoco el informe crítico. El contradictor y el análisis directo del §10 tampoco la ven.

**Fuentes de esta rúbrica.** El informe crítico (`universo/INFORME_CRITICO_Y_CANDIDATAS_ANONIMO.pdf`, citado como «p. N»), su lectura (`universo/LECTURA_INFORME.md`, §1.4, §3, §5.1 y §5.2), `REORIENTACION_UNIVERSO.md` y las decisiones D3, D5 y D6 de `RESUMEN_SESION_20261117_TARDE.md`. **El informe se usa como lista de preguntas, no como fuente de cifras** (LECTURA §1.7, punto 7). Las cifras de esta rúbrica son lo que el informe *afirma*. Sirven para saber qué buscar. Lo que cuenta es lo que digan los documentos de la empresa. Si el personaje encuentra en ellos una cifra distinta de la del informe, eso no es un error del personaje.

**Esta rúbrica no aconseja nada sobre ninguna cartera.** Las empresas se eligieron porque ponen a prueba el juicio, no porque sean compras.

---

## 0. Vocabulario mínimo y escala

**Lo que produce el personaje** (Anexo D, §D.6 y §D.13):

- **Estado del análisis:**
  - `concluido`;
  - `pendiente_de_investigacion`: hay una hipótesis que no se puede acotar;
  - `pendiente_de_datos`: falta un dato material;
  - `modelo_no_aplicable`: límite del modelo, por ejemplo L3: «este tipo de empresa requiere otro método»;
  - `no_entregable`.
- **Cubo** (la casilla final): Sí · Vigilar · No · Demasiado difícil. «Sí» solo existe con `concluido` y la acción `comprar`.
- **Acción:** `comprar` · `esperar` · `descartar` · `demasiado_dificil` · nada.
- **Escalera de precios** (Anexo C, k = 3): precio del escenario malo, **precio de Sí** y valor ponderado.
- **Zona del precio:** `bajo_malo` · `cumple_regla_k` · `vigilar` · `caro`. La zona no es la conclusión.
- **Objetivo de precio:** emitido, condicionado o bloqueado.

**Cuatro clases de fallo.** Las dos primeras no se compensan con aciertos en otros casos. D5.3 manda castigar por igual los dos sentidos del error.

| Clase | Qué es | Efecto |
|---|---|---|
| **S · suspenso de seguridad** | Falso positivo: un «Sí», un precio o un objetivo donde no debe haberlo. También una cifra inventada que sostiene una conclusión | Suspende el caso; no se compensa |
| **E · suspenso de equilibrio** | Falso negativo: no saber decir «Sí» cuando los datos lo justifican, o decir «No» donde toca «Vigilar» | Suspende el caso; no se compensa |
| **G · error grave** | Fallo económico material que no cambia el sentido de la salida, o acierto por la razón equivocada | Se corrige; si sigue tras dos rondas, el caso suspende |
| **m · error menor** | Omisión o imprecisión sin efecto en la conclusión | Se anota |

**Reglas que valen para todos los casos:**

1. **Contaminación.**
   - Si el informe del personaje contiene un hecho que solo está en el informe crítico, y no en sus fuentes, el recorrido **no vale**.
   - Tampoco vale si contiene, en el primer tiempo de Zoetis, algo posterior al 9-oct-2026.
   - En los dos casos se repite el recorrido. No cuenta como aprobado ni como suspenso.
2. **Hechos sin fuente (K6, segunda mitad).** Si el personaje afirma un hecho de la empresa que no está en sus fuentes, es G. Si ese hecho sostiene una conclusión favorable, es S. Afecta sobre todo a la competencia y a las cuotas de mercado.
3. **Tamaños.** Cualquier tamaño de posición o porcentaje en la ficha o en el informe es G (D16).
4. **Una sola tasa.** Usar una tasa distinta del 9 % para una empresa concreta y sacar de ahí la conclusión es S si la conclusión es favorable, y G si no lo es.
5. **Herencia de la etapa 1.** Remitirse a la ficha de etapa 1 como autoridad («la etapa 1 dice…») en una cifra que mueve el valor es G (Anexo D, §D.2).

**Cómo se lee la sensibilidad a la tasa** (D6, K5). Vale para todos los casos salvo Vinci.

- La hoja resumen tiene que mostrar el precio de Sí y la zona al 7, 8, 9, 10 y 11 %, y el crecimiento que exige el precio actual.
- Con el 9 % provisional:
  - una conclusión que **no cambia de zona entre el 8 y el 10 %** puede presentarse como firme;
  - si cambia en ese tramo, tiene que decir «depende de la tasa»;
  - lo que pase al 7 y al 11 % es información.
- **La prueba del 10 % es solo información.** Un «Sí» que no se sostiene al 10 % se señala con esas palabras, pero **no se rebaja por eso**.
- Rebajar un «Sí» solo por la prueba del 10 % es E. Esconder que no la pasa es G.
- Ninguna conclusión favorable puede apoyarse en una tasa por debajo del 9 %.

---

## 1. Ahold Delhaize · arrendamientos y F1 (pp. 12–13; LECTURA §3.3, G2)

**Qué examina.** Que el alquiler se cuente una sola vez, que se calculen y comparen los motores A y B, y que se incorporen los hechos posteriores al informe anual. Según el informe, la empresa tiene un margen subyacente del 4,0 % y el 85 % de sus locales son alquilados (p. 12). Un doble cómputo del alquiler se llevaría una parte grande del valor.

**Salida correcta.**
- `concluido · Vigilar · esperar`, con el precio de Sí emitido o condicionado.
- O bien `pendiente_de_investigacion · Vigilar`, si la conciliación de F1 o la caja de 2026 no se pueden acotar y el personaje dice cuál de las dos falla.
- Es aceptable `pendiente_de_datos` si nombra un dato material concreto que falta, por ejemplo la nota de arrendamientos incompleta.
- No se espera un «Sí». Si sale, no es suspenso automático. Antes de puntuarlo, pasa a una revisión económica independiente que tiene que confirmar tres cosas: que la conciliación K3 demuestra el alquiler contado una sola vez, que los dos motores dan la misma zona (K4) y que los hechos marcados con † del cuadro de hechos están incorporados. Si las tres se confirman, se anota como discrepancia con el informe, no como fallo.

**S:**
- un «Sí» o un objetivo con el alquiler contado dos veces o sin la conciliación K3;
- un «Sí» sin la previsión rebajada, sin el ciberincidente o sin la compra de Tesco.

**G:**
- «No» o «descartar» con un valor hundido por el doble cómputo;
- un solo motor sin justificar por qué no hace falta el otro;
- tomar la caja libre de 2025 como base sin explicar la semana 53 de 2026.

**m:** un «No» razonado con hechos y cuantificado: sin poder de precios, caja que no crece o una compra con un precedente malo.

**Preguntas que decide el caso** (K6; 12 preguntas, hacen falta al menos 10):
1. ¿Cuenta el alquiler una sola vez (o en el margen, o en el flujo y en la deuda) y lo demuestra comparando el flujo sin crecimiento con la caja base normalizada (K3)?
2. ¿Comprueba si la «caja libre» que publica la empresa ya resta los pagos de arrendamiento?
3. ¿Mete o deja fuera el pasivo por arrendamientos en el puente de deuda de forma coherente con la pregunta 1?
4. ¿Calcula los dos motores, A con F1 y B con el perímetro declarado, y compara sus zonas (K4)?
5. ¿Cuánta caja por acción queda después de alquileres en 2026 y 2027, con el cuarto trimestre afectado?
6. ¿Incorpora la previsión de caja libre rebajada y el coste del ciberincidente, incluidos los clientes digitales perdidos?
7. ¿Qué retorno deja la compra de Tesco sobre lo pagado, con y sin arrendamientos, y por qué sería distinta de FreshDirect?
8. ¿Qué parte del lastre de Estados Unidos es temporal y qué parte se queda, con la inversión en bajar precios hasta 2028?
9. ¿Qué parte del crecimiento del beneficio por acción es recompra y qué parte es negocio?
10. ¿Reconoce la falta de poder de precios (ahorra y el margen no sube) y no proyecta una expansión de margen?
11. ¿Trata en los escenarios una caja libre que no crece desde 2022, sin extrapolar crecimiento?
12. ¿Compara el retorno sobre el capital (en torno al 9 %, p. 12) con la tasa exigida y saca la consecuencia: crecer apenas crea valor?

**Hechos que debería encontrar en las fuentes de la empresa** († = posterior al último informe anual, el de 2025):

| Hecho a comprobar (lo que afirma el informe) | Documento previsible |
|---|---|
| Nota de arrendamientos completa: pasivo, amortización de los derechos de uso, intereses, pagos de principal y altas | Informe anual 2025, nota de arrendamientos |
| Proporción de locales alquilados (85 %, p. 12) | Informe anual 2025 |
| Definición de la caja libre publicada y cifras de 2022 y 2025 (2.149 y 1.911 millones) | Informe anual 2025 e informes anteriores |
| Dividendo y recompra de 2025 (1.070 y 1.008 millones); acciones en circulación frente a 2019 | Informe anual 2025 |
| Margen subyacente del 4,0 % y ahorros de 1.294 millones | Informe anual 2025 |
| Pérdida en FreshDirect | Informes anuales correspondientes |
| † Tercer trimestre (4-nov): ventas, margen subyacente del 4,1 % y caja libre trimestral | Comunicado del tercer trimestre de 2026 |
| † Ciberincidente: efecto en ventas y resultado del cuarto trimestre; caja libre de 2026 de «al menos 2.300» a «unos 2.100» millones; ejercicio de 53 semanas | Mismo comunicado |
| † Recompra de 1.000 millones desde 2027 | Mismo comunicado |
| † Compra de Tesco en Chequia y Eslovaquia (30-oct): valor de empresa con y sin arrendamientos, múltiplo y fecha de cierre | Comunicado de la operación |
| † Primer y segundo trimestre de 2026, y origen y calendario de los 1.000 millones de dólares para bajar precios | Informes trimestrales de 2026; no está claro en qué documento figura el compromiso: es una pregunta |

**Trampas.**
- Restar la amortización de los derechos de uso dentro del margen y restar además los pagos completos en el flujo. F1 encontró este error en Elis, donde suponía del 2,9 % al 3,1 % de las ventas.
- Usar como base una caja libre que ya descuenta el alquiler y sumar a la vez el pasivo por arrendamientos a la deuda.
- Comparar la compra de Tesco sin arrendamientos con una deuda que sí los lleva.
- Tomar la subida del beneficio por acción como crecimiento del negocio.
- Recoger el ciberincidente sin la semana 53.

**Tasa.** Es un negocio estable, y la tentación es decir que «merece» el 8 %. Pasar a cumplir la regla al 8 % es información, no un argumento (regla 4).

---

## 2. Jumbo · el «Sí» plausible (pp. 10–12; LECTURA §3.3, G1)

**Qué examina.** Que el personaje sabe decir «Sí» cuando los datos lo justifican, y que no lo dice sin haber contestado a la pregunta competitiva que decide el caso.

**Salida correcta, con dos variantes:**
- **(a) `concluido · Sí · comprar`.** Requisitos:
  - el precio actual está por debajo del precio de Sí calculado con sus propios escenarios, rehechos con el primer semestre de 2026 y las ventas de octubre;
  - el fundamento material está sin limitación o la comprobación conjunta queda superada;
  - la pregunta 1 está planteada y acotada con hechos, o explica por qué no impide concluir;
  - dice qué lo tumbaría.
- **(b) `concluido · Vigilar · esperar` o `pendiente_de_investigacion`**, solo si la razón cumple D5.2: un hecho concreto de las fuentes, o un dato ausente material, y cuánto mueve el valor. Por ejemplo: «el margen comparable cae X puntos y con un NORMAL de Y el precio de Sí queda en Z».
- La variante (b) aprueba el caso, pero **no demuestra que el personaje sepa decir que sí**. Cuenta para «Todavía no» (§11).

**S:**
- un «Sí» sin plantear la pregunta 1;
- un «Sí» que extrapola el retorno del 27 % sin explicar cuánto dura la ventaja;
- un «Sí» con la tendencia del margen mal leída (año entero frente a semestre);
- un «Sí» con el precio y el valor incoherentes respecto del euro extraordinario: precio sin derecho al dividendo y caja que todavía lo incluye, o al revés;
- un «Sí» con los escenarios de etapa 1 sin rehacer.

**E:**
- «No» o «Demasiado difícil»;
- Vigilar por razones genéricas («incertidumbre», «el margen baja») sin cuantificar;
- Vigilar solo por la tasa;
- Vigilar por anclarse en la regla de la ficha, que solo compra en el escenario malo, a 19 EUR (p. 12).

**G:** usar el reparto de 2026 como rentabilidad normal; sumar la caja neta al valor y contar además los intereses que cobra.

**Preguntas** (12 preguntas, hacen falta al menos 10):
1. ¿Por qué un margen bruto superior al 50 % en un bazar sobrevive a las plataformas asiáticas de venta directa? Es la pregunta decisiva: si no la plantea, el caso no aprueba.
2. ¿Qué parte de la caída del margen es mezcla de franquicias, IVA y divisa, y qué parte es competencia?
3. ¿Compara márgenes de periodos comparables, semestre con semestre o año con año?
4. ¿Plantea la sucesión del accionista de control (72 años, ventas de participación en 2021 y 2024)?
5. ¿Analiza la dependencia de Asia (70 % del producto), con el dólar y el flete?
6. ¿Pregunta por el uso de la caja, que empieza a dispersarse en centros de distribución, franquicias lejanas y un centro comercial?
7. ¿Trata el euro extraordinario con coherencia entre la fecha del precio y la caja del valor?
8. ¿Ve que una previsión de beneficio plano con ventas creciendo lleva dentro una caída de margen, y la recoge en el escenario NORMAL?
9. ¿Separa el reparto de 2026, que no se repite, del reparto sostenible?
10. ¿Trata la caja neta como exceso solo en lo que sobra de verdad, sin contar dos veces los intereses?
11. ¿Pregunta cuánto dura un margen EBITDA del 35 % en comercio, que atrae competidores?
12. ¿Escribe qué lo tumbaría: margen bruto anual por debajo del suelo histórico, ventas comparables negativas en Grecia o una salida desordenada del accionista de control?

El acceso a la bolsa de Atenas es de la persona responsable (posesión) y no puntúa.

**Hechos** († = posterior al informe anual de 2025):

| Hecho a comprobar | Documento previsible |
|---|---|
| Margen bruto de 2019 a 2025, y en concreto 55,61 % en 2024 y 54,72 % en 2025, atribuido a las franquicias | Informes anuales 2024 y 2025 |
| Beneficio neto de 2025 (320,1 millones), caja neta y retorno sobre el capital | Informe anual 2025 |
| Peso de Asia en las compras y moneda de compra | Informe anual |
| Participación del accionista de control y sus ventas de 2021 y 2024 | Comunicaciones regulatorias e informe anual |
| † Primer semestre de 2026: margen del 53,53 %, y 53,86 % en el primer semestre de 2025, con sus causas | Informe semestral de 2026 |
| † Ventas de octubre y de diez meses por país, y previsión de 2026 mantenida | Comunicado de ventas de noviembre de 2026 (las fuentes citan también Chipre, p. 28) |
| † Reparto de 2026: fechas, sin derecho al dividendo desde el 16-nov y pago el 20-nov; acciones en circulación (el informe las deduce: unos 134 millones) | Anuncios de reparto de la empresa |

**Trampas.**
- Comparar el margen del año 2022 entero con un semestre de 2026, que es el error de la propia ficha (p. 11).
- Que el «Sí» se apoye en el aumento de ventas de un mes.
- Contar dos veces el dividendo extraordinario.
- Tomar como confirmación que la plantilla, el informe anterior y el informe crítico lleguen al mismo nombre: los tres parten de la misma ficha (p. 12).

**Tasa.** Es el caso donde más importa la regla del 10 %. Un «Sí» al 9 % que no se sostiene al 10 % se mantiene, con el aviso escrito (D6). Un «Sí» que solo sale al 8 % no es un «Sí».

---

## 3. Zoetis en dos tiempos · la tesis que envejece (pp. 13–14; LECTURA §3.3, G10)

**Organización.**
- **Primer tiempo (T1):** solo documentos publicados hasta el **9-oct-2026**.
- **Segundo tiempo (T2):** el mismo expediente más el trimestre del **5-nov-2026**.
- Son dos recorridos y se puntúan por separado. T1 se congela antes de que exista T2.

**Qué examina.** Que una previsión negativa sin explicar se trate como un dato ausente material, y que el escenario base se rehaga cuando llega el trimestre.

**Salida correcta en T1.**
- `Vigilar · esperar`, o `pendiente_de_investigacion` o `pendiente_de_datos`.
- La causa tiene que nombrar la previsión de crecimiento orgánico negativo que no se explica, o la caída de la dermatología en el segundo trimestre.

**Salida correcta en T2.**
- `Vigilar · esperar` con los escenarios rehechos: franquicia en declive y precio medio negativo.
- El precio de Sí tiene que ser menor que en T1, o el personaje tiene que explicar por qué no lo es.
- También vale `pendiente_de_investigacion`.

**S:**
- «Sí» o `comprar` en T1 o en T2 (K10);
- una conclusión favorable apoyada en bajar la tasa.

**G:**
- T1 en Vigilar solo por el precio, sin detectar la previsión sin explicar (acierto por la razón equivocada);
- T2 que no cambia los escenarios respecto de T1;
- T2 en «No» sin un hecho cuantificado; con hechos es m.

**Preguntas de T1** (11 preguntas, hacen falta al menos 9):
1. ¿Por qué prevé la empresa crecimiento orgánico negativo en 2026? Si no lo sabe, ¿lo declara dato ausente material?
2. ¿Separa las ventas por franquicia y por región, y ve la caída de la dermatología en el segundo trimestre?
3. ¿Plantea el calendario de exclusividad de cada franquicia y qué competidor entra en cada una?
4. ¿Pregunta por la cuota en dermatología en Estados Unidos y por cuánto cuesta en precio defenderla?
5. ¿Distingue el precio de lista del precio neto, es decir, los descuentos?
6. ¿Pregunta por la situación regulatoria y de seguridad del tratamiento de la artrosis?
7. ¿Por qué se endeudó la dirección para recomprar acciones a una media de unos 136 USD en 2025?
8. ¿Ve la concentración en cinco productos (42 % de las ventas)?
9. ¿Construye los escenarios franquicia a franquicia, en lugar de extrapolar las ventas totales?
10. ¿Comprueba la norma contable de Estados Unidos y aplica F1 a sus arrendamientos con esa norma (K11)?
11. ¿Usa la última previsión vigente, con su fecha (K2)?

**Preguntas que se añaden en T2** (4 más: 15 en total, hacen falta al menos 12):
12. ¿Incorpora el trimestre y cambia el escenario base?
13. ¿Compara la previsión nueva con la anterior correcta, la de febrero o la del trimestre previo, sin confundirlas? El comunicado dice que se *subió* la previsión de beneficio por acción ajustado frente a la anterior (LECTURA §1.7, punto 7).
14. ¿Explica qué cambió desde T1 y por qué (motivo «evidencia_nueva»)?
15. ¿Fija qué la reabriría, por ejemplo dos trimestres sin perder cuota y con precio medio no negativo?

**Hechos** († = posterior al 10-K de 2025; ‡ = posterior al 9-oct, solo en T2):

| Hecho a comprobar | Documento previsible |
|---|---|
| El 70 % de las ventas es de animales de compañía; cinco productos suman el 42 %; retorno sobre el capital | 10-K 2025 |
| Recompras de 2025 con deuda y su precio medio | 10-K 2025 |
| Previsión de febrero: beneficio por acción ajustado de 7,00 a 7,10 USD | Comunicado de resultados de 2025 |
| † Previsión de crecimiento orgánico negativo para 2026 | Comunicado o 10-Q del segundo trimestre de 2026 |
| † Dermatología: −15,9 % en el segundo trimestre | 10-Q del segundo trimestre de 2026 |
| ‡ Tercer trimestre: −1 % orgánico, Estados Unidos −6 %, animales de compañía en Estados Unidos −8 % | Comunicado del 5-nov (8-K) |
| ‡ Dermatología: −13 % en Estados Unidos y −20 % fuera; artrosis: −12 % en Estados Unidos; precio medio −1 % con volumen plano | Mismo comunicado y 10-Q |
| ‡ Previsión: ingresos de 9.220 a 9.320 millones y beneficio por acción ajustado de 6,25 a 6,35 USD | Mismo comunicado |
| ‡ Pérdida de cuota de unos 7 y 4 puntos; 2027 sin recuperación; un competidor inyectable nuevo | **Fuentes de terceros** (resumen de la conferencia). Solo cuentan si la fase 1 las admite y las cita como tales |

**Trampas.**
- El escenario viejo: un precio por debajo del escenario base no significa nada si el escenario base es viejo (p. 14).
- Leer el «−1 %» como un bache de calendario.
- Tomar el crecimiento del beneficio por acción, que viene de la recompra, como crecimiento del negocio.
- Rellenar con memoria la cuota de mercado o los competidores.

**Mini-K9.** Las predicciones y la sección «qué me haría cambiar de cubo» de T1 se comparan con los hechos de T2. Se anota si T1 previó lo que podía romper la tesis. Es información y no puntúa.

**Tasa.** No es lo que decide este caso. Argumentar en T1 que «al 8 % es barata» es G, y es S si con eso se concluye «Sí».

---

## 4. Elis · faltan datos por R (p. 14; LECTURA §3.3, G3)

**Qué examina.** Que el personaje no invente la reinversión necesaria (R = R propia + R de compras, decisión F1 3a) y que el motor A ya lleve la corrección F1.

**Salida correcta.**
- `pendiente_de_datos · Vigilar · acción nula`, con la causa `falta_de_datos` y R nombrado como dato ausente.
- Tiene que decir de dónde saldría R.
- Puede mostrar un rango calculado, siempre que lo llame rango y no emita objetivo.

**S:**
- cualquier estado que dependa de un valor de R sin fundamento: el capex total, la amortización, una media del sector o el 248,5 de la plantilla;
- un precio de Sí u objetivo emitido;
- sustituir la entrada C48 (108) por 82.933 sin la derivación justificada. Las instrucciones del proyecto mandan conservar 108 y corregir la reconstrucción.

**G:** un estado distinto de `pendiente_de_datos` aunque no invente ninguna cifra, porque contradice la decisión F1 3a.

**Preguntas** (11 preguntas, hacen falta al menos 9):
1. ¿Distingue la inversión de reposición de la de crecimiento, y dice que la empresa no publica la primera?
2. ¿Declara R como dato ausente material, con su perímetro (propia más compras)?
3. ¿Calcula el retorno sobre todo el capital, incluido lo pagado en compras (7,4 % según el informe), y lo compara con la tasa exigida?
4. ¿Saca la consecuencia: si el retorno es igual al coste del capital, crecer no crea valor?
5. ¿Deja fuera la amortización de los derechos de uso de la reinversión que calibra el crecimiento (F1 1a) y cuenta el alquiler una sola vez?
6. ¿Trata la amortización de los intangibles comprados según F1, sin presentarla como una reposición en dinero?
7. ¿Compara la deuda a corto plazo con la caja?
8. ¿Plantea las investigaciones en las filiales de Brasil y su posible coste?
9. ¿Incorpora el trimestre del 28-oct y los objetivos confirmados?
10. ¿Calcula los dos motores, o justifica por qué basta el A (K4)?
11. ¿Dice qué dato lo desbloquearía y de qué documento saldría?

**Hechos** († = posterior al documento de registro universal de 2025):

| Hecho a comprobar | Documento previsible |
|---|---|
| 400.000 clientes en 31 países; contratos de unos cuatro años con cuota mensual | Documento de registro universal 2025 |
| Inversión anual de alrededor del 18 % de las ventas; desglose por naturaleza, si existe | Mismo documento, cuadro de flujos y notas |
| Caja libre de 2025 (358,6 millones); deuda a corto plazo frente a la caja | Mismo documento |
| Investigaciones en Brasil | Mismo documento, apartado de riesgos y litigios |
| † Primer semestre de 2026 | Informe semestral |
| † Tercer trimestre: ingresos de 1.323,9 millones, +6,1 %, orgánico +3,5 %; objetivos confirmados | Comunicado del 28-oct |

**Trampas.**
- Dar un único precio cuando R no se publica.
- Calcular el retorno sin el fondo de comercio y presentarlo como si la empresa ganara más.
- Concluir «No» por el retorno inferior a la tasa mientras R está pendiente.

**Tasa.** Aquí la tasa decide si crecer crea o destruye valor, porque el retorno está cerca del 9 %. La sensibilidad debe mostrar ese cambio de signo, siempre como rango condicionado y nunca como objetivo.

---

## 5. Vinci · límite del modelo (pp. 17 y 23; LECTURA §3.3, G8)

**Qué examina.** Que el personaje se abstenga, y por la razón correcta. Solo hace falta llegar hasta la fase A (LECTURA §5.3).

**Salida correcta.**
- `modelo_no_aplicable` (L3: C62 = «No · este tipo de empresa requiere otro método») · Demasiado difícil · acción `demasiado_dificil`, sin precio de Sí ni objetivo.
- También vale `concluido · Demasiado difícil · demasiado_dificil`.

**S** (K10):
- cualquier precio de Sí, zona u objetivo presentado como conclusión;
- «Sí»;
- Vigilar con objetivo;
- «No» o «descartar», porque K10 exige terminar en límite del modelo o en «Demasiado difícil».

**G:** abstenerse por otra razón, como la deuda o «no entiendo la construcción», sin nombrar la vida finita de las concesiones ni el valor terminal.

**m:** abstenerse bien pero sin decir qué haría falta para valorarla.

**Preguntas** (7 preguntas, hacen falta al menos 6):
1. ¿Identifica que una parte material del valor está en concesiones de vida finita?
2. ¿Pregunta cuándo vence cada concesión principal (el informe habla de 2032 a 2036) y qué pasa con los activos al vencer?
3. ¿Dice que el valor terminal perpetuo de los motores no sirve para un flujo que se acaba?
4. ¿Reconoce tres negocios distintos (concesiones, energía y construcción) que piden una suma de partes?
5. ¿Declara el límite del modelo en lugar de calcular?
6. ¿Dice qué haría falta: un modelo concesión por concesión y una valoración por partes?
7. ¿Pregunta qué deuda está ligada a las concesiones?

**Hechos** (en el documento de registro universal 2025; ninguno marcado como posterior):
- vencimientos de cada concesión;
- resultados por segmento;
- deuda por segmento.

El informe no da más. Lo demás que plantee el personaje se puntúa como pregunta, no como hecho.

**Trampas.**
- El valor terminal perpetuo sobre una concesión que vence.
- Fiarse de que la hoja de etapa 1 sí calculó tres escenarios y lo sitúa «en torno al base», a 0,95 veces (pp. 17 y 23). Es el falso positivo más probable.

**Tasa.** No se evalúa. Mostrar una escalera aunque sea «a título informativo» es G.

---

## 6. Waste Management (opcional) · excelente y caro: Vigilar, no No (p. 15; LECTURA §3.3, G3)

**Qué examina.** El error contrario al de Zoetis: un «caro» mecánico que acaba en «No».

**Salida correcta.**
- `concluido · Vigilar · esperar`. La zona «caro» es aceptable.
- Tiene que llevar la condición o el hecho que la haría subir, y la sensibilidad completa.
- También vale `pendiente_de_datos` si nombra un dato material concreto.

**E:** «No» o «descartar», incluido el «No» por aplicar mecánicamente el descalificador «deuda que mata» a una deuda de 3,06 veces.

**S:**
- un «Sí» obtenido bajando la tasa solo para esta empresa;
- un «Sí» con una caja base de nueve meses ayudada por la caída de la inversión en sostenibilidad o por los créditos fiscales.

**G:** «Demasiado difícil» por la compra sanitaria sin explicar por qué no se puede acotar.

**Preguntas** (11 preguntas, hacen falta al menos 9):
1. ¿Normaliza la caja libre sin la caída puntual de la inversión en sostenibilidad (de 429 a 191 millones)?
2. ¿Separa los créditos fiscales, que terminan en 2027, y normaliza el tipo impositivo?
3. ¿Trata la retribución en acciones como coste?
4. ¿Analiza el negocio sanitario comprado: su resultado, el fondo de comercio, el deterioro y la amortización de lo comprado, según F1?
5. ¿Compara el retorno sobre todo el capital (10,9 %) con la exigencia?
6. ¿Juzga la deuda frente a la estabilidad del negocio (contratos, franquicias y permisos) en lugar de aplicar un umbral único?
7. ¿Calcula qué crecimiento exige el precio y con qué tasa se justificaría?
8. ¿Comprueba la norma contable de Estados Unidos y el tratamiento de los arrendamientos?
9. ¿Revisa los cuatro criterios de la ficha (p. 15)?
10. ¿Explica el foso: vertederos y permisos difíciles de replicar?
11. ¿Dice qué precio o qué hecho la pasaría de Vigilar a Sí?

**Hechos** († = posterior al 10-K de 2025):

| Hecho a comprobar | Documento previsible |
|---|---|
| 257 vertederos; duración de los contratos y de las franquicias; deuda sobre EBITDA; pérdidas del negocio sanitario en 2025; créditos fiscales y su final | 10-K 2025 |
| † Tercer trimestre: ingresos +6,3 %; caja libre de nueve meses de 3.009 millones; inversión en sostenibilidad de 429 a 191 millones | Comunicado del 27-oct (8-K) |
| † Previsión de caja libre en la parte alta de 3.750 a 3.850 millones; el negocio sanitario pasa de −21 a +20 millones en el trimestre; deuda total a 30-sep; sin deterioro | Mismo comunicado y 10-Q |

**Trampas.**
- «Caro» al 9 % convertido en «No».
- Extrapolar una caja ayudada por partidas puntuales.
- Restar como reposición en dinero la amortización de lo comprado en el negocio sanitario.

**Tasa.** Es el caso donde la sensibilidad decide la lectura. La ficha admite que con un 7 % el valor superaría el precio (p. 15). La salida correcta lo muestra así: «a tu tasa del 9 %, cara; la decisión de la tasa es tuya (D6)». No baja la tasa para esta empresa.

---

## 7. Tabla de puntuación por caso

La rellena el evaluador. Una fila por recorrido: Zoetis cuenta dos filas y K7 añade las repeticiones.

| Caso | Salida (estado · cubo · acción) | ¿Correcta? (C / aceptable / no) | S | E | G (n) | m (n) | K6 (%) | Hechos con † encontrados (n de N) | Sensibilidad 7–11 % y prueba del 10 % | Contradictor (§9) | Resultado del caso |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Ahold | | | | | | | /12 | | | | |
| Jumbo | | | — | | | | /12 | | | | |
| Zoetis T1 | | | | — | | | /11 | | | | |
| Zoetis T2 | | | | — | | | /15 | | | | |
| Elis | | | | — | | | /11 | | | | |
| Vinci | | | | — | | | /7 | n/a | n/a | | |
| WM (opc.) | | | | | | | /11 | | | | |

**Resultado del caso:**
- **PASA:** salida correcta, sin S ni E, K6 al 80 % o más, y los G corregidos.
- **PASA SIN DEMOSTRAR:** solo en Jumbo con la variante (b).
- **SUSPENDE-S / SUSPENDE-E:** hay un fallo S o E.
- **SUSPENDE-G:** quedan G sin corregir después de dos rondas.

Además se anotan dos datos: cuántos de los hechos marcados con † encontró el personaje, porque mide la vigencia, y cuántos hechos sin fuente afirmó.

---

## 8. Criterios K1–K12 adaptados a 4–6 días

| K | Qué se comprueba en este examen | ¿Se puede cumplir del todo? |
|---|---|---|
| K1 · Entradas | Ahold y Elis: `verificacion_entradas` apto, con cero entradas materiales pendientes. Jumbo, Zoetis y WM: solo las entradas que mueven el valor (precio, acciones, caja base, deuda y arrendamientos) | **Parcial.** Faltan el Excel y el `.md` de etapa 1 de Jumbo, Zoetis, Vinci y WM |
| K2 · Vigencia | Último informe publicado incorporado; fechas separadas; precio de 5 sesiones como mucho, con el dividendo declarado | Sí |
| K3 · Conciliación | Caja base por dos vías; puente de deuda completo; flujo sin crecimiento igual a la caja normalizada. En Ahold y Elis entero; en las demás, al menos la caja base | Sí en Ahold y Elis; parcial en las demás |
| K4 · Dos motores | Ahold (obligatorio), Elis (ya existe) y WM si entra | Sí |
| K5 · Sensibilidad | Lo descrito en el §0 | Sí |
| K6 · Preguntas | Esta rúbrica: al menos el 80 % por caso y ningún hecho sin fuente | Sí |
| K7 · Repetibilidad | Dos repeticiones independientes: **Jumbo**, porque un «Sí» que no se repite no es un «Sí», y **Zoetis T1**. Mismo cubo, misma acción y precio de Sí a menos del 15 % | Sí, con dos casos |
| K8 · Auditoría | Agente nuevo con APROBADO sobre el material fijado. La revisión económica por otra familia de modelos se hará si da tiempo; si no, se declara. El contraste de la persona con otros modelos (D4) no cuenta | **Parcial** |
| K9 · Predicciones | Cada expediente registra al menos 3 predicciones fechadas con su probabilidad, y hay un calendario para contrastarlas. En 4–6 días solo se puede contrastar el mini-K9 de Zoetis | **No del todo:** solo existe el mecanismo |
| K10 · Trampa y límite | Zoetis T1 y T2 sin «Sí»; Vinci en límite o en «Demasiado difícil», por la razón correcta | Sí. **No se compensa** |
| K11 · F1 fuera de Elis | Ahold con NIIF. Zoetis o WM con la norma de Estados Unidos, con la regla de F1 distinguiendo la norma | **Parcial:** lo seguro es Ahold; la norma de Estados Unidos depende de llegar a tiempo |
| K12 · Aptitud con alcance | Declaración escrita de para qué tipo de empresa vale y para cuál no, y los casos sintéticos 033–036 | Sí |
| *Añadido (§7 de la reorientación)* · Lenguaje llano | La hoja resumen dice en palabras sencillas el veredicto, el porqué, lo que lo haría falso y el efecto de la tasa. El evaluador lo comprueba con un sí o un no en cada caso | Sí |

---

## 9. Registro del contradictor simétrico (D3, D5 y D7)

**Una ficha por caso**, más una para el contradictor del veredicto final, que hace Fable (D7).

1. **Conclusión antes del contradictor:** estado, cubo, acción y precio de Sí.
2. **Cada objeción:**
   - dirección: ↓ si va contra una conclusión favorable, ↑ si va contra «No» o «caro»;
   - el hecho, con documento y página, o el dato ausente material;
   - **cuánto mueve el valor**, con una cifra o un rango;
   - la respuesta del personaje: rebatida con un dato (cuál) o no rebatida.
3. **Movimiento aplicado** y conclusión después del contradictor.

**Qué comprueba el evaluador:**
- **Independencia:** el contradictor trabajó en un contexto nuevo, sin los razonamientos del coordinador ni la opinión de la persona. Se comprueba en su encargo y en su registro.
- **Carga de la prueba:** una objeción genérica, sin hecho o sin cuantía, no mueve nada. Si la movió, es G.
- **Regla de movimiento:** una objeción válida no rebatida mueve la conclusión un escalón (de Sí a Vigilar, o de No o caro a Vigilar). Una objeción rebatida no la mueve.
- **Simetría en el conjunto del examen:**
  - el contradictor tiene que haber atacado al menos una conclusión desfavorable (Jumbo en la variante b, WM o Ahold);
  - si solo ataca conclusiones favorables, falla el contrapeso y se anota como G de conjunto.

**Medidas** (información):
- objeciones válidas en cada dirección;
- porcentaje de objeciones rebatidas;
- movimientos que acercaron la salida a la correcta de esta rúbrica, y movimientos que la alejaron.

---

## 10. Personaje frente a análisis directo (reorientación, §10)

**Casos:** Ahold y Zoetis T1.

**Análisis directo:**
- el mismo modelo y el mismo esfuerzo que el agente principal del personaje, en un contexto nuevo y en una sola pasada;
- recibe los **mismos datos verificados**: el registro de entradas, los textos de las fuentes y el mismo corte del 9-oct en Zoetis;
- usa la misma tasa del 9 % y las mismas probabilidades de partida;
- tiene que entregar estado, cubo, acción, tres escenarios, precio de Sí con la regla k = 3 y la sensibilidad;
- no ve las fases ni los prompts del personaje, ni esta rúbrica.

**Revisión a ciegas.** Un revisor recibe las dos salidas con etiquetas X e Y sorteadas, y registra los errores económicos materiales de cada una.

| Medida | Cómo se mide |
|---|---|
| Veredicto | ¿Coincide con la salida correcta de esta rúbrica? (sí / aceptable / no) |
| Precio de Sí | Valor de cada uno, diferencia en % y coherencia con sus escenarios |
| Trampa de Zoetis | ¿Dice «Sí» en T1? |
| Errores económicos | Número y gravedad (S, G o m) según la revisión a ciegas, por ejemplo el doble cómputo en Ahold |
| Preguntas | Cobertura K6 de cada uno con esta misma rúbrica |
| Coste y tiempo | Tokens o euros, minutos de reloj y minutos de intervención humana |

**«Claramente mejor», fijado ahora.** El personaje lo es si se cumple alguna de estas tres condiciones y no queda peor en ninguna medida de seguridad:
1. evita una trampa (S) en la que cae el análisis directo;
2. tiene, entre los dos casos, al menos dos errores económicos materiales menos;
3. tiene al menos 20 puntos más de cobertura K6.

Si no lo es, se recomienda estudiar cómo simplificarlo. Con dos casos esto es un indicio, no una prueba. **No cambia el veredicto final.**

---

## 11. Regla final

**El software no da puntos.** Que las pruebas del software pasen solo es condición para que las salidas existan; sin eso, el expediente es `no_entregable`. No da ningún punto en esta rúbrica ni acredita aptitud alguna. El veredicto se emite con lo comprobado ese día y sobre el material con su huella. No puede formularse como «Sí, cuando pasen las pruebas» ni trasladarse a otra versión sin repetir K7.

**«No, para»**, si ocurre cualquiera de estas cosas:
- un S o un E que siga sin resolver después de dos rondas de corrección;
- un fallo de K10. Repetir el mismo caso no lo redime, porque la trampa ya es conocida. Hay una excepción: si se demuestra que la causa fue un defecto de implementación y no de juicio, el resultado pasa a «Todavía no», y hace falta otra trampa que los autores no conozcan;
- K3 sin cumplir en Ahold o en Elis al acabar el plazo porque la conciliación muestra un error del personaje (por ejemplo, el alquiler contado dos veces);
- hechos sin fuente que sostienen una conclusión en algún caso;
- acabar los 4–6 días con fallos propios del personaje (regla de parada).

**«Todavía no»**, y lo que falta, si no hay ningún S ni ningún E pero:
- no ha salido ningún «Sí» justificado (Jumbo en la variante b, como ya advirtió D5); o
- queda algún criterio parcial por razones ajenas al personaje: datos aún no publicados, material de etapa 1 que no ha llegado, K1 incompleto porque la verificación de las entradas no ha terminado (no por una cifra mal registrada por el personaje), K11 con la norma de Estados Unidos sin terminar, o K8 sin la otra familia de modelos.

**«Sí, con poco»**, solo si se cumplen todas estas condiciones:
- ningún S ni ningún E;
- al menos un «Sí» justificado (normalmente Jumbo) que:
  - sobrevive al contradictor;
  - se repite (K7);
  - muestra la sensibilidad y la prueba del 10 % como información;
- Zoetis T1 y T2 sin «Sí»;
- Vinci se abstiene por la razón correcta;
- Elis en `pendiente_de_datos` sin un valor de R;
- Ahold con el alquiler contado una sola vez y conciliado;
- WM en Vigilar, si entra;
- K6 al 80 % o más en todos los casos;
- K1 (al menos las entradas materiales), K2, K3 y K5 en todos los expedientes;
- K4 en Ahold, K7 en los dos casos, K8 con agente nuevo, K10 y K12;
- K11 al menos en Ahold;
- el mecanismo de K9 en marcha;
- la hoja resumen en lenguaje llano;
- el contradictor registrado en todos los casos.

Si K11 con la norma de Estados Unidos no se ha probado, el alcance escrito (K12) se limita a empresas que informan con NIIF.

El coordinador lo dice acompañado de lo que lo haría falso (D3 b). Aun así, rige R-6: si el personaje y la investigación de la persona no coinciden, no se invierte. «Sí, con poco» no cambia la aptitud formal declarada de la versión, que sigue siendo experimental mientras la persona no decida otra cosa.

---

## 12. Lo que queda abierto

1. Falta el material de etapa 1 de Jumbo, Zoetis, Vinci y WM. Sin él, K1 es parcial y el recorrido no arranca.
2. No está claro en qué documento figura el compromiso de 1.000 millones de dólares de Ahold, ni si la caja libre que publica ya resta los arrendamientos. Son preguntas, no hechos.
3. La fase 1 todavía no decide si admite fuentes de terceros. Las cuotas de Zoetis y la competencia de Jumbo dependen de eso.
4. Hay que confirmar que los hechos de octubre y noviembre de 2026 son posteriores a los datos de entrenamiento de cada modelo que se use. Si no, Zoetis T1 queda contaminado. **(Respuesta del coordinador al congelar:** los agentes de juicio usan el modelo Opus de esta sesión, cuyos datos de entrenamiento llegan a junio de 2026; los extractores usan Sonnet, anterior o igual. Los hechos de octubre y noviembre de 2026 son posteriores. Se mantiene la regla de contaminación del §0 como control.)
5. Los umbrales de esta rúbrica son propuestas del coordinador hasta que se congelen: el 80 %, el 15 %, el tramo del 8 al 10 % como «firme» y los 20 puntos. La tasa sigue siendo decisión de la persona responsable (D6).
