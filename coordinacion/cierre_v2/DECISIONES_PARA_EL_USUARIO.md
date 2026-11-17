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
