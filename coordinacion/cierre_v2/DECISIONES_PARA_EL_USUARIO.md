# Decisiones: cuándo interviene el usuario

## No requieren una aprobación económica nueva

Corregir bugs técnicos/especificaciones, comprobar fuentes, resolver columnas/unidades/versiones con evidencia, preparar datos/tests/manuales, revisar una entrega ajena, construir una candidata aislada y reproducir pruebas autorizadas. Claude debe continuar estas tareas sin pedir confirmaciones rutinarias. Las correcciones financieras de propuesta no equivalen a activar una política en el producto.

## Sí requieren una decisión explícita, después de propuesta revisada

- Políticas F1 (1a)–(5b) y opciones de alcance/regla fiscal/arrendamiento/PPA/compras/transición que sigan abiertas. No aprobarlas en bloque sin fundamento y consecuencias. El 0,5% no está adoptado; el umbral terminal existente se conserva salvo decisión nueva.
- Parámetros/protocolos económicos pendientes P-M1, k/probabilidades y otras decisiones registradas como pendientes, si realmente afectan al uso elegido. La falta de identificación no se resuelve escogiendo un punto o firmándolo.
- Reducir el alcance original, sustituir una validación requerida, fusionar main o publicar versión final. Este programa prepara una candidata y evidencia, no adopta esa aprobación final.
- Enviar preguntas a empresas o terceros; comprar acceso/servicios, cambiar facturación/recargas/credenciales. No autorizado por el mero hecho de querer aprovechar saldo Mistral.

## Cómo debe pedirlo Claude

Una sola cola breve de decisiones realmente bloqueantes: ID, decisión anterior si existe, alternativa recomendada y fundamento, alternativas, evidencia disponible/ausente, efecto esperado y límites, texto concreto y qué trabajo sigue sin quedar validado aunque se apruebe. No volver a solicitar E1/D3/E2/E6 ya registrados.

Para datos no públicos: presentar la pregunta preparada y por qué importa, indicando lo buscado. No afirmar que el dato existe ni prometer conseguirlo. Una estimación necesita método/rango/evidencia/revisión y conserva su naturaleza. Aprobar una hipótesis no la transforma en dato publicado ni garantiza aptitud para dinero real.

La autorización de trabajo contenida en un prompt no puede convertirse en aprobación económica. Copiar el encargo maestro permite trabajo técnico y de evidencia; las decisiones anteriores siguen separadas.

## Cola actual de decisiones bloqueantes (coordinador, 16-nov-2026)

Solo se incluyen decisiones nuevas que bloquean trabajo. Siguen pendientes, y **no se vuelven a pedir aquí**:
- (1a)–(5b) de F1, con la propuesta de la rama F1;
- P-M1, k y las probabilidades;
- E1/D3/E2/E6, que ya están registradas.

### U1 · Dónde se conservan los 11 PDF nuevos de Elis (E-ELIS) · **DECIDIDA el 17-nov y HECHA**: Release `fuentes-elis-e-20261117` (11 PDF, índice y SHA256SUMS; digest del servidor igual a las huellas)

- **Situación (actualizada el 17-nov).** Con la aclaración de la reanudación (`c241a59`), el coordinador descargó los 11 PDF de sus URL públicas oficiales:
  - 11/11 tienen bytes y SHA-256 idénticos a los declarados;
  - 28/28 citas están en su página (adenda en `revisiones_coordinador/E_93a9780/adenda_20261117/`).

  **Ya no hay ninguna cita sin verificar.** Lo único pendiente es una copia duradera autorizada: la descarga del coordinador está en un sandbox efímero y no cuenta como preservación.
- **Recomendada:** que la persona responsable suba los 11 PDF a una Release del repositorio auxiliar (por ejemplo `fuentes-mistral-m2-20261116`, hoy vacía) o a otro almacén que autorice. El coordinador comprobará allí la SHA-256 de cada uno frente a `adenda_20261117/descargas_verificacion.tsv`.
- **Alternativa:** (b) aceptar como preservación el índice de descarga (URL, fecha, SHA-256 y bytes) y los extractos acotados en Git, con el riesgo de que el emisor cambie o retire los documentos.
- **Qué no se valida aunque se resuelva:** M1, M2, M6 y N2 siguen ABIERTOS según la revisión (E-R1…E-R9). Elis sigue `pendiente_de_datos`.

### U2 · Tercer caso B fuera de muestra (F-B3) · **DECIDIDA el 17-nov: Ahold.** El usuario aporta Ahold_evaluada.xlsx y Ahold_respuesta.md, que se preservan como originales. Las huellas se buscan antes en los registros disponibles; las que se calculen después se rotulan como NUEVAS. La correspondencia histórica no verificada se declara. La etapa 1 no se rehace. · Propuesta anterior: Ahold Delhaize (17-nov; `u2_tercer_b/`). Falta de ti: `Ahold_evaluada.xlsx` y `Ahold_respuesta.md` de la etapa 1, tal cual; el `HUELLAS.txt` de tus PDF 2019–2025; si el resultado de la etapa 1 influyó en elegirla como reserva; y dónde conservar los 10 informes anuales descargados (por ejemplo, una Release como en U1). La lista de las 116 no hace falta

- **Situación.** En el ZIP no está el Excel evaluado de la etapa 1 de Ahold; solo hay un `.bat` de descarga sin ejecutar. La lista de las 116 empresas no está conservada. Hermès y Aarsleff no sirven: ya están en la muestra.
- **Recomendada:** aportar el Excel de la etapa 1 de Ahold, su respuesta y sus fuentes (informes 2016–2025 y el folleto NIIF 16 de 2018), en bytes y con SHA-256.
- **Alternativas:**
  - (b) designar otra empresa fuera de muestra y aportar sus fuentes;
  - (c) reducir el alcance a dos casos B. Esto exige una decisión explícita de reducir el alcance.
- **Qué no se valida aunque se resuelva:** el recorrido con agentes reales y la auditoría de otro contexto siguen pendientes.

### U3 · Primer caso C real (F-C1) · **DECIDIDA el 17-nov: descarga autorizada** del informe anual 2025 y del Pilar 3 de FinecoBank desde sus sitios oficiales, con comprobación de edición, período, perímetro, protocolo y contrato antes de fijarla. Si no encaja, no se fuerza. No valida el motor C. · Antes: contrato corregido y candidatos propuestos sin verificar (17-nov; `u3_motor_c/`). Candidatos: FinecoBank (banco) y Hannover Rück (reaseguro, con riesgo alto de límite del modelo). Para verificarlos hace falta que autorices las descargas desde sus sitios oficiales o que aportes su informe anual 2025 y su Pilar 3 o SFCR 2025

- **Situación.** No se conserva ninguna financiera. El contrato C propuesto describe mal el motor C (F2-D3) y hay que corregirlo antes de usarlo.
- **Recomendada:** designar un banco o una aseguradora concretos y aportar sus informes oficiales (cuentas, Pilar 3 o SFCR) con SHA-256, y su Excel de la etapa 1 si existe.
- **Alternativa:** (b) sacar el motor C real del alcance de este cierre. Es una reducción de alcance y exige decisión.
- **Qué no se valida aunque se resuelva:** la solvencia y el capital regulatorio, que el contrato C declara no validar.

### U4 · Textos de la raíz del producto que describen el hito 1 (README, CLAUDE.md, MIGRATION_STATUS.json) · **DECIDIDA el 17-nov**: cambio entregado en `integracion/hechos-raiz-957af65` @ `3d66437`, pendiente de revisión independiente

- **Situación.** `README.md:1-17`, `CLAUDE.md:1` y `:35`, y `docs/MIGRATION_STATUS.json` dicen:
  - «rama de revisión intermedia 4.15 hito 1»;
  - que las correcciones de Claude «no se han importado»;
  - que hay que «esperar» la entrega.

  La candidata ya contiene el hito 2, `957af65` (`munger_v2_r1/VERSION`). Son tus instrucciones de proyecto. La corrección documental G-DOCS (`c0542b8`) no las toca.
- **Recomendada:** que, en la rama de la candidata, la persona responsable apruebe sustituir esas frases por el estado verificable. Es decir: 4.15 · hito 2 integrado en `integracion/candidata-cierre-v2`; `main` conserva la 4.14; nada adoptado económicamente.
- **Alternativa:** (b) dejarlas como están. El manual las marca como [CONTRADICCIÓN] C-01…C-04.
- **Qué no se valida aunque se resuelva:** nada económico. Solo evita que un receptor nuevo espere una entrega que ya está.

### F1 (3b) · Vía para M1, M2, M6 y el plan climático · **DECIDIDA el 17-nov: (iv) mantener el bloqueo.** Elis sigue pendiente_de_datos.

### F1 (1a), (1b), (2) y (4a) · **DECIDIDAS el 17-nov** por la persona responsable, según la recomendación de DECISIONES_F1_UNA_POR_UNA.md @ 03e7851:
- (1a), alternativa (b): la reinversión que calibra f excluye la amortización ROU.
- (1b): la media 2023–25 de pagos y amortización ROU se toma como convención declarada.
- (2): la correspondencia de costes (i)–(v).
- (4a): un solo perímetro para f, el ancla de S2C, el margen y el ROIC del terminal.

Ninguna de ellas fija R; Elis sigue `pendiente_de_datos`.

### F1 (3a), (4b), (5a), (5b) y E8.1 · **DECIDIDAS el 17-nov**
- (3a): R sigue pendiente, con su perímetro.
- (4b): opción A, pendiente hasta M6.
- (5a): regla N1, con N2 pendiente. El alcance en los ejercicios de τ y la actualización de México se justificarán por separado antes de decidirlos.
- (5b): clasificación por finalidad documentada.
- E8.1: se mantiene el τ de cinco años.

**Umbral de V-F1a:** se pide una propuesta; nada adoptado.

### Examen · F1-A, F1-B, Elis, L1 y L2 · **DECIDIDAS el 18-nov-2026** por la persona responsable (preguntas en `examen/PREGUNTAS_PARA_LA_PERSONA.md`, respondidas una por una en la sesión del coordinador)
- **F1-A · Reinversión necesaria (regla general):** en las empresas del examen del motor A con arrendamientos, si la empresa no publica el reparto entre mantenimiento y crecimiento, la reinversión necesaria se iguala a su **amortización propia sin los derechos de uso** (perímetro A2, «A2_propio»), como **hipótesis declarada, no como dato**; el personaje la presenta como condicionada y con su sensibilidad. Escrita una vez, igual para todas; no se elige empresa a empresa. Motivo: permitir concluir con un supuesto común, declarado y auditable.
- **F1-B · Compras de empresas (regla general):** se tratan como **crecimiento**, no como mantenimiento, como hipótesis declarada y revisable (equivale a la opción B de (4b)); si una compra parece necesaria para mantener las ventas, el personaje lo señala.
- **Elis:** **mantiene sus decisiones del 17-nov** ((3a) con (3b) iv: R pendiente; (4b) opción A). La regla general no se le aplica; Elis sigue siendo la prueba de «faltan datos». Límite declarado: dos tratamientos distintos en el examen, a la vista.
- **L1:** se autoriza una **tercera ronda mínima** del lanzador del análisis directo, solo para el fallo R2-1 (convertir el error en aviso, con su prueba) y una comprobación rápida del revisor.
- **L2:** el análisis directo **recibe la misma etapa 1** que el personaje; se corrige el README del lanzador.

Nada de lo anterior acredita aptitud para dinero real ni fija la tasa (9 % provisional).

### Examen · D-US1 y D-US2 (arrendamientos con US GAAP) · **DECIDIDAS el 18-nov-2026** por la persona responsable
- **D-US1 · Hipótesis general declarada:** con US GAAP, si la empresa no publica en qué líneas del estado de flujos van los dos tramos del arrendamiento operativo (la amortización del derecho de uso y la variación del pasivo), se supone que **van netos dentro del flujo de explotación**, fuera de las filas 8 (D&A) y 14 (circulante) de la Historia, como **hipótesis declarada, no como dato**. La conclusión se presenta como condicionada, con la cota de sensibilidad (cuánto cambiaría el valor si no fuera así). Donde la empresa publica las líneas, manda el dato. Igual para todas las empresas; mismo principio que F1-A.
- **D-US2:** cuando el coste lineal del arrendamiento operativo y los pagos del año difieren, se cuentan los **pagos** y la diferencia queda a la vista en la ficha, sin bloquear.

## 18-nov-2026 (tarde) · decisiones de la persona responsable tras el contradictor y el dictamen O1/O2 de Ahold

Preguntas formuladas con el dictamen `examen/revisiones/dictamen_O1_O2_ahold/DICTAMEN.md` (Fable). Respuestas literales en la interfaz de preguntas:

- **P-O1 · cobros fuera de la explotación → «(c) Regla espejo»**, para todas las empresas: si se resta lo que se paga, se suma lo que se cobra por lo mismo (intereses netos, alquileres de subarriendo netos, dividendos de participadas/negocios conjuntos). Sustituye, desde hoy, la decisión de la etapa 1 de Ahold (`Control maestro!M43/M47`). Salvaguarda del dictamen: si se suma caja en `C76`, sus intereses no entran (sin doble cuenta). Efecto en Ahold (réplica del motor A): precio de Sí 27,74 → 32,66 € (solo O1).
- **P-O2 · acciones → «(a) Al cierre de cuentas»**: acciones en circulación al cierre del ejercicio base, el criterio de D3 (Viscofan) y E6 (Elis). Ahold: 886,877 M a 28-dic-2025 (efecto solo O2: 27,74 → 28,30 €). Aplica a todas las empresas; corregir la instrucción de metadatos de la fase 1 (`prompts/metadatos_fase1.md`) antes de Jumbo y Zoetis.
- Conjunto en Ahold con las dos (dictamen §12): precio de Sí ≈ 33,32 €, ponderado ≈ 35,78 €; zona caro a 36,05 €. Se aplican con expediente nuevo y cálculo declarado en la configuración del cambio, sin tocar plantilla ni código; recálculo oficial por el pipeline.
- **J-T · Jumbo, ejercicio de transición (1-jul a 31-dic-2019, seis meses) → «sí» a la propuesta del coordinador**: sus cifras se guardan tal como se publicaron, marcadas «6 meses, no comparable»; no se usan para medias anuales ni para el crecimiento; no se anualizan ni se rellenan. La base del FCF (2023–2025) no se ve afectada.
- **J1 · Jumbo, intereses cobrados → «Sí, esos cuentan»**: con la regla espejo y su salvaguarda, solo se excluyen los intereses de la caja que ya se suma aparte en `C76`; los del resto de la caja entran (≈ 8 mm/año; FCF base ≈ +3,5 %).
- **J2 · Jumbo, dividendos de la cartera cotizada → «Igual que la caja»**: si la cartera está en `C76`, sus dividendos no cuentan; si no lo está, cuentan.
- **J3 · Jumbo, Historia → «Sí, corregirlas»**: se corrigen en la Historia las filas de intereses y de principal de arrendamientos de 2020–2025 cruzadas por el emisor, con nota del motivo y las páginas que lo prueban.

## 18-nov-2026 (tarde) · decisiones tras la revisión R1 de F1 con US GAAP (`examen/revisiones/f1_usgaap/REVISION_R1.md` §5)
- **D-US2 bis · alquiler mezclado en otros activos/pasivos (caso Nike) → «No bloquear y enseñar»**: se publica el valor de la hoja (coste contable) y al lado cuánto cambiaría contando los pagos; antes, el programa comprueba que el expediente muestra las dos líneas (activo y pasivo) (cierra el camino iii de R1-3).
- **D-WM · arrendamientos financieros no desglosados (caso Waste Management) → «Tratarlos como deuda»**: hipótesis declarada; su amortización queda dentro de la propia y sus pagos no se restan de la caja base; la diferencia estimada (≈ 8 mm/año, 0,35 % del CFO − capex medio) se enseña junto al resultado.
- **P-FOSO · vara del foso de quien alquila sus locales → «(a) Misma vara»** (dictamen `examen/revisiones/dictamen_perimetro_g4/DICTAMEN.md` §3): con F1 en A2_propio, el foso (`C18`) se juzga comparando el retorno del capital propio, pagado todo el alquiler ((EBIT − intereses de arrendamiento) × (1 − t) ÷ capital propio; Ahold 13,0 % en 2021–2025) con r; `C55` (todo el capital) solo frente al sector. G4 sigue con r + 3 puntos. El personaje vuelve a juzgar el foso con esa cifra (puede seguir en «No» si la ventaja no le parece duradera).

## 18-nov-2026 (noche) · uso de modelos al agotarse Fable
- **F-AGOTADO → «Sí» a la propuesta del coordinador**: cuando se agote Fable, los contradictores y auditorías de cada empresa pasan a **Opus con esfuerzo máximo** (agente distinto, contexto limpio); lo que Fable deje a medias lo retoma un agente Opus nuevo desde lo guardado; si Fable vuelve tras el restablecimiento (viernes 20-nov), se reserva para el contradictor del veredicto final y la evaluación con la rúbrica (23-nov).
- **J-T bis · Jumbo, 2019 → «Sí» al año natural 2019** (12 meses, columna comparativa publicada por Jumbo en el informe 2020), en lugar del periodo de transición de 6 meses; se anota el solape de 6 meses con el ejercicio 2018/19. Sustituye en ese punto a J-T.
- **Zoetis, «guía orgánica 2026 negativa» de la etapa 1:** la persona no recuerda su origen ni su fecha. En el primer tiempo **no se usa como hecho** (sin fuente en el expediente y posible fuga temporal: la etapa 1 se guardó el 18-oct); las fases ya estaban instruidas así.
- **Pregunta abierta (no urgente) · P-FOSO en A1_sin_ROU:** la vara «misma vara» se implantó solo para A2_propio, como dice la decisión. Con A1_sin_ROU (perímetro que también excluye los derechos de uso) las medidas quedan «no aplicables · pendiente de decisión». Ninguna empresa del examen usa A1. (`f1/perimetro-foso` @ 424a266.)

## 18-nov-2026 (noche) · cribado del universo
- **C-ARR · arrendamientos en el cribado → «Una vez, en el flujo»**: como en el examen (F1, P-O1): el alquiler se resta del flujo de caja y la deuda se mide sin arrendamientos; el pasivo por arrendamientos se muestra aparte como dato.
- **C-EX · empresas del examen → «Sí, fuera hasta el 23»**: Ahold, Jumbo, Zoetis, Elis, Vinci y Waste Management quedan fuera del cribado hasta después del veredicto del 23-nov; se criban las otras 111.
- **Zoetis · guía 2026 → «Sí, incluirla»** (sustituye la exclusión anterior): Mistral encontró la fuente oficial (comunicado y presentación de resultados del T2 2026, **publicados el 6-ago-2026**, antes del corte del 9-oct; rama `mistral/zoetis-guia-2t26`): ingresos 9.120–9.320 mm USD, crecimiento orgánico operativo (3)%–(1)%, BPA ajustado 6,15–6,25. Se añade el comunicado a las fuentes del primer tiempo y el personaje puede usarla. Los 3 análisis directos de Zoetis ya hechos se hicieron sin ella (anotado). La actualización del 5-nov (T3) sigue fuera del primer tiempo.

## 19-nov-2026 (mañana) · decisiones de la persona responsable (literal: «1 sept, 2 dejar, 3 mantener, 4 dejar, 5 cero, 6 a»)
- **A-Q3 · Ahold → 3T (septiembre):** los doce últimos meses pasan al informe del 3T 2026 (publicado el 4-nov-2026, antes del precio del 13-nov). Expediente nuevo `ahold_f4`; se repiten las fases.
- **A-NIC17 · Ahold, deuda 2016–2017 → dejarla** como se publicó (incluye arrendamientos financieros NIC 17) y declararlo.
- **Z-ACC · acciones al cierre frente a balance de mitad de año → mantener P-O2** y declarar la desalineación de fechas en cada cifra (Ahold, Jumbo, Zoetis, Vinci).
- **Z-R · Zoetis, agrupación geográfica de la r mínima → dejarla** y anotar la diferencia.
- **Z-MIN · Zoetis, minoritarios negativos → cero** con aviso y la cifra impresa en el registro.
- **V-CIRC · Vinci, circulante en la reinversión → (a):** circulante a 0 también en la reinversión, con un mecanismo declarado (cambio de producto con pruebas y revisión independiente; expediente nuevo de Vinci).
