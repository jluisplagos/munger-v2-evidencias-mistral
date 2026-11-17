# Revisión crítica independiente · F1-IMPL (motor A con el perímetro F1)

- **Material:** rama `f1/implantacion` @ `2e9442f` (commits `cbb482a`, `eb193f8`, `2e9442f` sobre la candidata `b129b36`), en `/home/user/e_work/wt_f1impl` (no modificado).
- **Contrato:** `DECISIONES_F1_UNA_POR_UNA.md`, tabla única de `PROPUESTA_DECISIONES_F1.md`, `ESPECIFICACION_F1_PROPUESTA.md` (rama `auditoria/economica-f1-frente-e` @ `9cad78d`) y `DECISIONES_PARA_EL_USUARIO.md`:68–83.
- **Revisor:** agente distinto del autor (Fable, esfuerzo máximo). 17-nov-2026. Trabajo sobre una copia en `/tmp/claude-0/revision_f1impl/`. LibreOffice solo con `flock`, en secuencia.
- **Evidencia reproducible:** `evidencia/scripts/` y `evidencia/salidas/`, junto a este informe.
- Marcas: **hecho** (lo he ejecutado o leído), *interpretación*, ***propuesta***.
- **Ceguera del examen:** este informe y su carpeta de evidencia citan criterios del examen (K1, K3, K4, salidas aceptadas) y cifras de Ahold leídas por el revisor. No deben entrar en ningún expediente ni en el material de los agentes del personaje.

## Veredicto: CORRECCIONES

La capa **calcula bien y bloquea bien allí donde se evalúa**: todas las cifras cuadran con un cálculo propio y no toca el libro ni adopta ninguna cifra sin decidir. Se puede integrar ya **como cerrojo**: frente a la candidata solo añade bloqueos.

No se puede dar F1 por implantada ni usar su «utilizable» como garantía, por cinco motivos:

1. el bloqueo solo se hace cumplir en los pasos 7 y 12: el cierre, la ficha y el informe no lo comprueban (obtuve un `concluido · Sí · comprar` oficial con la propia ficha diciendo «F1: no utilizable»);
2. F1 solo se exige si existe uno de dos archivos: una empresa NIIF con arrendamientos llega a `Sí` con el valor A0 sin rastro de F1;
3. `F1-LIBRO` no salta con términos explícitos en A0: el libro omite un coste declarado y F1 dice «utilizable»;
4. falta la guarda simétrica de V-F1m: con A1/A2/A3 y C49 a cero o vacío, el alquiler se **omite** (hoy lo tapa `F1-LIBRO`; deja de taparlo en cuanto se resuelva);
5. K3 es una identidad: cuadra con cualquier dato y no descubre un doble cómputo.

Además, hoy **el motor A no puede concluir para casi ninguna empresa real** (cualquier arrendamiento, cualquier PPA, toda US GAAP): es el límite `F1-LIBRO`, tratado al final.

## Lo que está bien (hechos reproducidos)

| Qué | Resultado propio (`repro_independiente.py`, sin código del autor; libro `d2593777…` y CSV verificado `6cb33b9d…`) |
|---|---|
| A1 − A0, Elis 2025 | **+139,381721** (= V₀ · ROU media ÷ ventas medias) |
| (1b) sensibilidad | pagos **−16,778** · ROU **+10,118** · total **−6,660** (pesos 3,04 % → 3,30 % → 3,71 %) |
| Escala PPA / ROU | **+4,206** / −10,118 (las dos en A2: −5,913) |
| T16 (N1) | τ 0,2619 / 0,2806 / 0,2559 · τ5 0,28234 · m0 0,131379 · **f 0,044900433** · flujo 236,891 (**−11,605**) · año 11 NORMAL **−18,609**; variantes −11,190 / −12,396 / −11,980; igual en A1 y A2 |
| Puente K3 de Elis A0 | 307,933 + 39,600 − 7,965 − 9,872 + 136,767 − 132,500 − 85,467 = 248,496 (residuo 0) |
| E9 T1–T3b | f, flujo sin crecimiento y C53 de A0, A1, A2 y B; los 33 flujos del Motor replicados (desviación 9·10⁻¹³) |
| Batería y regresión en la copia | `103/103 pruebas del motor A F1 (4.15) PASAN` · regresión de Elis `36/36 PASAN` |
| Muestra de `verificar_paquete.sh` (rápido) en `2e9442f` | manifiesto 7784 · modificados 0 · ausentes 0 (36 «de más» de mis propias pruebas); entorno, piloto 35 y comprobadores 114/114 PASAN. No repetí `completa` |
| Procedencia | `elis_cifras_f1.json`: 4 huellas de origen y 32 cifras iguales a las del CSV verificado |

**Ninguna cifra descuadra.**

## Hallazgos

### Materiales

**H1 · El cierre, la ficha y el informe no hacen cumplir el bloqueo F1.**
- *Evidencia* (`sondas_pipeline2.py`, PC): empresa sintética con la declaración completa; F1 pasa en el paso 7; la declaración cambia a un estado que bloquea; el paso 12 termina en `no_entregable` (`F1-LIBRO`). Relanzado con `--desde 13`: auditoría APROBADO y **ficha oficial `concluido · cubo Sí · acción comprar`, con `cierre: APROBADO`**, mientras su bloque `motor_a_f1` dice `utilizable_para_conclusion: false`. El informe imprime las dos cosas seguidas.
- Causa: `ficha.py` copia el bloque sin usarlo; `cierre_v2.motivo_rechazo_cierre` y los pasos 13–14 no miran F1.
- ***Corrección:*** con motor A y F1 exigible, sin resultado vigente (huellas del libro y de la declaración) y utilizable: `ficha.py` no escribe `concluido` ni decisión, y el cierre se rechaza. Repetir el gancho antes de fijar el material (paso 13).

**H2 · La exigencia de F1 queda abierta por defecto.**
- *Evidencia* (`sondas_pipeline.py`, PA): empresa sintética NIIF, motor A, C49 = 3,71, pasivo por arrendamientos 50, sin `entrada_efectiva.json` ni `motor_a_f1.json` → **`concluido · Sí · comprar`, auditoría APROBADO**, valor A0, sin bloque F1 en la ficha ni línea en el informe.
- `exigido()` da `False` también en un expediente de la 4.15 que declara el modo en `alcance_v2.json` (forma del hito 1, que `modo_entrada_efectiva` admite) y si se borra `entrada_efectiva.json` después del paso 2 (S11). Es un criterio más débil que el que el hito 2 fijó para lo mismo (`ficha._declara_modo`, N1).
- F1_IMPL §5 afirma «no hay resultado silencioso»: solo es cierto con ese archivo.
- ***Corrección:*** exigir F1 en todo expediente de motor A; la línea de base sintética v2.2 y los cierres históricos, con una exención explícita y registrada, no por la ausencia de un archivo. Como mínimo: el criterio de N1 más el modo registrado en `estado_pipeline.json`, y exigir siempre que el propio libro muestre arrendamientos (C49 o filas 17 y 23 de la Historia).

**H3 · `F1-LIBRO` no salta con términos explícitos en A0 (vivo, sobrevalora).**
- *Evidencia* (`sondas_capa3.py`, S14): empresa sin arrendamientos ni PPA, perímetro A0 (el único que hoy puede concluir). Con una transición de 7 al año durante 5 años como término explícito, o con compras de reposición del 0,9 % de las ventas, la capa cobra esos importes (−7 en los años 1–5; 9,3 crecientes y 12,0 en el año 11) y el libro no. `F1-LIBRO` no salta, `utilizable_para_conclusion: true`, y el pipeline sigue con el valor del libro.
- Causa: la condición es `per != "A0_total" or aj_ok`.
- ***Corrección:*** `F1-LIBRO` salta siempre que los flujos del perímetro declarado difieran de los del Motor (comparación numérica) o haya términos explícitos.

**H4 · Falta la guarda simétrica de V-F1m: alquiler omitido con A1/A2/A3 (latente).**
- *Evidencia* (`sondas_capa.py`, S1): NIIF 16 con los pagos de principal fuera del FCF base (C49 = 0 o vacío). Caja verdadera 68. A0 da 68; **A1 da 78** y no bloquea nada salvo `F1-LIBRO`. V-F1a y V-F1m solo se evalúan con A0.
- Excluir la ROU de D_X solo es coherente si los pagos están dentro del FCF base. Es también un hueco de E5: W3 solo analizó A0.
- ***Corrección*** (antes de resolver `F1-LIBRO`): con A1/A2/A3, ROU > 0 y C49 no positivo (cero o vacío) → BLOQUEA, fuera del dominio. *Sube a la persona como adición a E5.*

**H5 · K3 no es falsable.**
- *Evidencia* (S10): con 500 libros de datos aleatorios, sin relación entre FCF base, EBIT, D&A y capex, «cuadra» en 500 de 500 y en los cuatro perímetros. Con un FCF base que resta el alquiler dos veces (56 frente a 68): cuadra, ninguna partida sin explicar, `utilizable: true`. La mutación m16 del autor lo confirma.
- La etiqueta «doble cómputo» sale de la misma condición que V-F1a (ROU declarada > 0 y C49 > 0): K3 no añade detección. `F1-K3` nunca bloquea por un doble cómputo, y la ficha muestra `K3_cuadra: true` también con A0 y V-F1a saltando: se lee como «K3 pasa».
- Solo cubre la tercera parte de K3 (flujo sin crecimiento frente a caja base), como presentación; no la caja base por dos vías.
- ***Propuesta*** (tres comprobaciones que los datos pueden hacer fallar):
  1. **Caja base por dos vías:** `C70` frente a la media de la ventana de la fila 35 de la Historia (CFO − capex − intereses − principal − SBC, por año). La diferencia solo puede explicarse con partidas declaradas con fuente. Elis: 323,0 frente a 307,933; los 15,067 son 25,067 de interés de arrendamientos en C48 menos 10,0 de diferencia de capex (C47 = 857,167 frente a 867,167 en la fila 12). Detecta el caso de S10.
  2. **Cuenta del alquiler:** amortización en el margen + pagos en el FCF base − ROU devuelta por D_X tiene que dar exactamente uno. Dos: V-F1a. Cero: H4.
  3. **Reposición frente a su caja:** media de (capex − D_X + circulante) negativa con ventas que no bajan → D_X devuelve más amortización de la que el capex pudo reponer. Elis A0: −81,2 (A1 +51,3; A2 +136,8). Ahold A0: **−1.295,3**. Sin justificación, bloquea.
  - Cada una con su caso negativo y su mutación. El puente actual queda como presentación (E6) y `K3_cuadra` se sustituye por «alquiler contado: una / dos / ninguna vez».

### Medios

**H6 · La declaración y el resultado F1 no forman parte del material auditado.** `motor_a_f1.json` y `motor_a_f1_resultado.json` no están en `cierre_v2.MATERIAL_FIJO` (sí lo está `configuracion_economica.json`, su análogo del motor B): cambiarlos tras el cierre no retira la aprobación. La ficha no comprueba que `libro_sha256` y `declaracion_sha256` sean los vigentes, y un resultado antiguo se muestra aunque el motor cambie. Si `Diagnóstico V6!C5` no dice «A» (caché vacía), la capa responde «no aplica» con código 0 y el gancho sigue (S9). ***Corrección:*** añadir los dos al material fijo, comprobar huellas y pasar el motor desde el pipeline.

**H7 · La batería obligatoria no protege el punto que hace cumplir F1.** Mutaciones propias (`mutaciones_revisor.py`): gancho desactivado (R1) y gancho que deja pasar el código 4 (R2) → **103/103 PASAN**. Tampoco se detectan el ancla E4 sin restar X^v (R9) ni V-F1c sin la transición (R6). La prueba de extremo a extremo `prueba_pipeline_f1.py` no está en `verificar_paquete.sh`. T15 no se ejecuta sobre los 32 casos (lo declara el autor). ***Corrección:*** registrar la prueba de extremo a extremo como obligatoria y añadir los casos V2b y V2g.

**H8 · La cabecera de la ficha y del informe sigue dando valores A0 sin rótulo cuando F1 bloquea.** Elis (copia de la regresión): «zona caro · precio de Sí 7,30 · ponderado 7,99», y debajo la línea F1. Con los flujos F1 de la propia capa y la cola del libro replicada (10⁻¹¹ en A0), el ponderado sería 17,37 (A1) o 23,42 (A2) con precio 24,18. *Es un diagnóstico, no una valoración: palancas sin anclar y R pendiente.* En `no_entregable` por F1 (PC-1) también se imprime «precio de Sí 19,82». ***Corrección:*** con F1 bloqueando, retirar o rotular «A0 · no usable» la escalera, la zona y los valores por acción.

**H9 · N1: el alcance aplazado se puede elegir por omisión.** Si la declaración solo lista los ajustes de la ventana y pone `actualizacion_financiera_earnout_declarada: false`, `F1-PARAM` no salta y queda «solo ventana, sin actualización» (la batería lo fija como comportamiento esperado en T16). Además N1 acepta cualquier partida con la etiqueta N1 (probado con «gastos de reestructuración» con su caja en el FCF base) y no exige registro, que el texto aprobado sí pide (S4). Hoy lo tapa `F1-LIBRO`. ***Corrección:*** `F1-PARAM` siempre que se use N1 mientras el alcance no esté decidido; declaración expresa, con fuente, de cada ejercicio del τ fuera de la ventana; N1 solo para ajustes de earnout; registro.

**H10 · Términos explícitos: ceros por defecto y año 11 sin cargo.** Compras de reposición «con importes por año»: los años sin importe y un importe no numérico («nueve») se cobran como 0, y el año 11 queda en 0 a perpetuidad, sin que V-F1j salte (S5). `ancla_s2c_excluye_terminos: true` es solo una afirmación: el ancla calculada no cambia (1,655 frente a 2,0) salvo con una clave no documentada, `importes_historicos` (S6). ***Corrección:*** exigir importes de 1 a 10 y el del año 11 (o la proporción); calcular X^v con importes históricos obligatorios; vacío no es cero.

**H11 · A0 se admite con C49 vacío y sin mirar el propio libro.** C49 vacío se trata como cero, y las filas 17 (principal) y 23 (pasivo) de la Historia no se contrastan (la 17 se lee y no se usa): con ROU declarada a cero y esas filas positivas, «utilizable» (S2). Tampoco exigen registro «no hay transición conocida» (S7) ni la normalización. ***Corrección:*** C49 vacío bloquea (vacío ≠ 0); ROU = 0 declarada con filas 17 o 23 positivas bloquea; registro en esas dos declaraciones.

**H12 · Las series nuevas no están verificadas.** Respuesta a la pregunta 7, más abajo. Además T9 no es exigible en la capa: «(149,5)» declarado como +149,5 con signo 1 pasa, igual que un documento y una página inventados (S12, S13).

**H13 · Generalidad.**
- Menos de diez años de historia (la V6.3 admite cinco) → `ErrorDeclaracion`, que el pipeline convierte en `no_entregable · fallo_de_implementacion` (S3).
- La tolerancia de los flujos es absoluta (10⁻⁹): con ventas del orden de 10⁹ en la unidad del modelo, `F1-REPLICA` salta en falso (`sondas_capa2.py`). No afecta a euros o dólares en millones.
- `F1-NORMA` busca «ifrs|niif|ias» en cualquier parte de L4: «US GAAP (no IFRS)» pasa como NIIF (S8).

### Menores

- El mensaje de `pendiente_de_datos` cita «R: M1, M2, M6», que son de Elis, para cualquier empresa.
- V-F1f no informa con `A3_estimado`, que es el perímetro de Elis.
- La extensión de V-F1b debería llevar identificador propio: E5 la define con C49 > 0.
- La regresión reescribe archivos del manifiesto, con una ruta absoluta, cada vez que se ejecuta.
- En la regresión, los registros de margen, compras y transición los rellena el agente citando el registro de decisiones. No es una firma; en un expediente real debe hacerlo la persona.
- La sensibilidad de (1b) solo se calcula si se declaran los pagos y no llega a la ficha.
- Agotamiento de la PPA: 3,21 años (275,1 ÷ 85,7) frente a «unos 3,3» de la propuesta (÷ 83,5).

## 1 · Fidelidad a las decisiones

Cada decisión está implantada como se decidió; el libro y las entradas registradas no cambian (C48 = 108, C49 = 128,1, C70 = 307,933). Interpretaciones del autor:

| Interpretación | Juicio | ¿Sube a la persona? |
|---|---|---|
| `F1-2i`: A0 y A1 con PPA > 0 bloquean | Correcta: es la consecuencia de (2)(i); la tabla de costes ya no admite «cobrarla como reposición (A1) sin dato» | **Sí:** deja A1 sin uso, bloquea a empresas sin arrendamientos con intangibles comprados y lo hace con cualquier importe. Decidirla junto con el umbral de V-F1a |
| A0 sin arrendamientos y con PPA | Bien parado y reportado | Sí (la misma decisión) |
| V-F1b ampliada (ROU vacía con C49 = 0) | Correcta (vacío ≠ 0). Falta lo mismo para C49 vacío (H11) | No |
| Transición `en_R` ⇒ `A3_estimado` | Correcta: la D&A no la contiene | No |
| `F1-REGISTRO` | Correcta según E2; cobertura incompleta (H9, H11). La norma contable es un hecho: mejor fuente y página que registro | No |
| Perímetro de Elis = `A3_estimado` sin estimación | Lógico, y honesto: lo deja sin persona y bloquea | **Sí:** la declaración de Elis |
| Guarda simétrica (H4) y exigencia (H2) | No están en E5 | **Sí** |

**Decisiones aplazadas.** El umbral de V-F1a no se elige: bloquea con cualquier importe y rechaza uno declarado. El alcance de N1 y la actualización del earnout se calculan como variantes, pero pueden quedar elegidos por omisión (H9).

**Carga operativa.** Cada expediente del motor A necesita una declaración de la persona responsable (norma, cuatro perímetros, compras, transición), con fecha, persona y motivo. Sin ella, el paso 7 termina en `pendiente_de_datos`. Para Ahold hay que pedirla ya.

## 5 · Generalidad

- **US GAAP: el bloqueo es correcto como medida de seguridad; no es suficiente ni el final del camino.**
  - La demostración US1/US2 del autor es válida: el perímetro correcto depende de si la amortización no monetaria del arrendamiento está en la fila 8 y la variación del pasivo en la 14.
  - Es más amplio de lo necesario. Con arrendamientos operativos, lo habitual es que la fila 8 no lleve esa amortización: A0 sería coherente. Lo que queda igual que en NIIF son los arrendamientos financieros y la PPA. Con dos datos declarados más (importe de esa amortización dentro de la fila 8 y dónde está la variación del pasivo) habría regla.
  - No protege si F1 no se exige (H2) o si L4 contiene «IFRS» en otro contexto (H13).
  - Consecuencia: toda empresa US GAAP con motor A termina en `no_entregable · límite del modelo`. K11 no se puede cumplir en su parte de Estados Unidos por el motor A.
  - *Fuera de alcance, para la persona:* el motor B resta «deuda + arrendamientos»; con US GAAP el alquiler operativo ya está entero en el EBIT, así que restar además ese pasivo lo contaría dos veces.
- **Sin arrendamientos:** A0 solo pasa con ROU y PPA declaradas a cero año a año con documento y página, C49 no positivo, compras clasificadas (cualquier adquisición en cinco años impide «sin_compras») y siete declaraciones con registro. Falla en cerrado, salvo H3 y H11.
- **¿Puede un expediente nuevo saltarse F1 sin querer?** Sí (H2): preparado a mano, con la forma del hito 1, o reanudado tras borrar `entrada_efectiva.json`. El de Ahold (`2026-11_examen_universo/ahold_4_15`, paso 5) sí lo tiene: F1 se le exigirá en el paso 7.

## 6 · ¿Hay un camino a un objetivo o un «Sí» del motor A con el valor A0 y arrendamientos materiales?

Sí. Uno demostrado con arrendamientos, otro demostrado como mecanismo y uno derivado:

1. **F1 no exigido** (H2, PA): `concluido · Sí · comprar` con C49 > 0. Es el comportamiento de la línea de base.
2. **Bloqueo en el paso 12 y `--desde 13`** (H1, PC): `Sí` oficial con la ficha diciendo «no utilizable». Exige un relanzamiento manual contra la indicación del diagnóstico. Lo demostré con una empresa sin arrendamientos (prueba del mecanismo: el cierre no mira F1); con arrendamientos hace falta además que el paso 7 hubiera pasado antes (declaración errónea, camino 3) o que el expediente ya estuviera más allá del paso 7 al integrar F1.
3. **Derivado:** una declaración «A0, ROU = 0» con C49 vacío pasa (H11); si después se corrige, queda el camino 2.

Con arrendamientos no encontré camino cuando F1 se exige, se evalúa y la declaración es veraz: A0 bloquea (V-F1a, V-F1m, V-F1b) y los demás perímetros bloquean (`F1-LIBRO`). Sin arrendamientos sí hay uno, por los términos explícitos (H3). Saltarse el gancho del paso 7 con `--desde 8` no llegó a la fase B en mi prueba (falta `referencias_mecanicas.json`); no lo exploré más.

*A0 no es prudente por construcción:* infravalora el flujo, pero infla el ancla de S2C (Elis: 9,04 frente a 2,45 o 1,61), y en Ahold `C53` queda vacío.

## 7 · Series sin `verificacion_entradas.py`: ¿bloquea K1?

- **Hoy no:** nada se concluye con ellas.
- **Lo bloqueará en cuanto F1 dé valor.** Son las entradas más materiales del motor activo (Elis: +139 sobre 248; Ahold: unos +1.390 sobre 1.042) y quedarían fuera del universo: el registro diría «apto por entradas» sin cubrirlas.
- En Elis proceden del CSV del frente E, que tiene su propio verificador («sin incoherencia detectada», no «acreditada»); para la regresión basta.
- ***Propuesta:*** meterlas en el universo. Con la salida (a), D_X es una celda del libro y entra como «derivado» con sus orígenes auxiliares (D&A total, ROU, PPA), cada uno con fuente, página, cita y signo: el registro actual ya admite esa forma.

## Recomendación sobre `F1-LIBRO`

**Qué hay en juego en Ahold.** *Ilustración del revisor sobre el libro de datos real del expediente (paso 5, solo lectura) y cifras leídas en los informes anuales, sin pasar por la verificación de entradas* (`ilustracion_ahold.py`):

- FCF base 1.999,3; **flujo sin crecimiento del libro (A0) 1.041,6**; reinversión neta media de la ventana −1.295,3; `C53` vacío.
- Amortización de derechos de uso: 1.336 / 1.333 / 1.400 (AR2023 p. 262, AR2024 p. 321, AR2025 p. 272 del PDF) → A1 − A0 ≈ **+1.389,5**, el 68 % del FCF base. El libro valoraría Ahold con menos de la mitad del flujo.
- «Repayment of lease liabilities» (1.944 en 2025) **incluye principal e intereses** en una sola línea (AR2025, p. 260 del PDF): C49 = 1.834 son pagos totales.

| Salida | Qué exige | Riesgo | Coste | Prueba que la validaría |
|---|---|---|---|---|
| **(a) Plantilla V6.3.1 F1 por guion** | Fila D_X por año y perímetro en la Historia; tres grupos de fórmulas (fila 30, C58, C76); referencia y verificador nuevos; configuración propia; aplicar la declaración al libro; D_X en el universo de entradas | Medio: toca la integridad de la plantilla y el paso 2. Acotado: la V6.3 no cambia, el patrón es el de la V6.4.1 y la capa ya da el oráculo | **≈ 2 días** con revisión; punto de control al final del día 1 | (1) Selector vacío: 0 celdas distintas de la V6.3 y casos de referencia sin cambio. (2) Elis A1/A2 recalculado: f = 0,012624225323285 / −0,006118601744165; C53 = 2,445331695332 / 1,612524303305; 33 flujos de E9 a 10⁻⁹; control negativo del año 11 (205,4). (3) `F1-REPLICA` sobre el perímetro declarado: capa y libro coinciden. (4) T5/T6 por LibreOffice; ROU vacía → f vacía, no cero. (5) `verificar_paquete.sh completa` con la prueba de extremo a extremo |
| **(b) La capa calcula también el valor** | La cola es trivial (replicada aquí en 20 líneas, 10⁻¹¹). Lo caro es que todo lo demás lee el libro: referencias mecánicas (ancla C53), `resultados.json`, escalera, gramática, comprobación conjunta (recalcula el libro), sensibilidades, ficha y auditoría | **Alto:** dos verdades (libro A0, valor F1); cualquier consumidor sin parchear filtra A0. Rompe (4a) en la práctica | Diagnóstico: horas. Para concluir: **≥ 3 días** | Réplica de B71:D78 en A0 y contraste de cada consumidor; la auditoría de 16 puntos compara con el libro |
| **(c) Motor B V6.4.1 «NIIF 16»** | Solo si la fase A elige B; configuración experimental con trazabilidad, altas de derechos de uso de cinco años con fuente | Bajo en lo técnico. Económico: es un ensayo, no una adopción; el perímetro es decisión humana por empresa; y **C63 en Ahold es 1,35 %** (261 de intereses sin los 465 de arrendamientos, AR2025 p. 212, ÷ deuda media con arrendamientos). Con ellos sería 3,75 % y la r operativa pasaría de 6,14 % a 6,82 % (fórmula de `Diagnóstico V6!C15` con la capitalización del expediente): sesgo al alza | **0,5–1 día** | Réplica de las bases, variante Caja ↔ NIIF 16 y sensibilidad a C63 con el interés de arrendamientos |

**Recomiendo (a), en su forma mínima, con (b) solo como oráculo de prueba y (c) como segunda pata.**

- (a) es la única que mantiene un solo perímetro para f, el ancla que ve la fase B, el Motor, las sensibilidades y la auditoría, porque todo sale del libro. No incluye N1 ni términos explícitos: para ellos `F1-LIBRO` sigue bloqueando.
- (c) no sustituye a (a): K4 pide los dos motores, «A con F1 y B con el perímetro declarado». (c) da la pata B, o la conclusión principal solo si la fase A elige B por sus criterios, y entonces hay que declarar o tratar C63.
- **Antes de habilitar ningún valor fuera de A0:** H4 (guarda simétrica), H1, H2, H3 y K3 falsable (H5).
- **Si (a) no supera sus pruebas en el punto de control:** Ahold por el motor A termina en `no_entregable · límite del modelo`, que no es una salida aceptable del examen. Queda (c) si la fase A justificó B, con la conclusión declarada condicionada por faltar la pata A.

***Orden propuesto.***
1. Hoy (medio día): H1, H2, H3, H4, H6 y H7; integrar como cerrojo; pedir a la persona la declaración de Ahold y las series de ROU y PPA con fuente.
2. Días 1–2: (a), K3 falsable y D_X en el universo de entradas.
3. Después: Ahold por A (V6.3.1) y por B (V6.4.1) para K4.

## Qué ejecuté

| Orden (sobre la copia) | Resultado |
|---|---|
| `python3 -B pruebas/test_motor_a_f1.py` | 103/103 PASAN |
| `python3 -I …/f1_impl/scripts/regresion_elis_f1.py <copia>` | 36/36 PASAN |
| `repro_independiente.py`, `cola_valor.py` | cifras del cuadro; cola del libro replicada |
| `sondas_capa.py`, `sondas_capa2.py`, `sondas_capa3.py` | S1–S14 |
| `flock … sondas_pipeline.py`, `sondas_pipeline2.py` | PA, PB-1, PC-1, PC-2 |
| `mutaciones_revisor.py` | 4 de 10 no detectadas (R1, R2, R6, R9) |
| `flock … bash verificar_paquete.sh` (rápido) | manifiesto: 0 modificados y 0 ausentes (el bloque marca FALLA por 36 archivos «de más» de mis propias pruebas en la copia); entorno, piloto y comprobadores PASAN |
| `ilustracion_ahold.py` | órdenes de magnitud de Ahold |

**No verifiqué:** `verificar_paquete.sh completa`; las 18 mutaciones del autor; P3 (US GAAP de extremo a extremo); los 32 casos de T15; la cifra de PPA de Ahold. `sondas_pipeline.py` se interrumpió en PB-2: `--desde 8` no llega a la fase B porque el paso 7 no dejó `referencias_mecanicas.json`.

**Aptitud:** uso supervisado experimental. No apto para decisiones con dinero real. Superar estas pruebas no la acredita.
