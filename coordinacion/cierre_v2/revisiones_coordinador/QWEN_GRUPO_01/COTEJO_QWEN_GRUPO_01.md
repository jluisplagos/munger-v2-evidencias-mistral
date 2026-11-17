# Cotejo independiente: Mistral (qwen-bank-group-01) y Claude API (qwen-peer-group-01) sobre Q1-001…Q1-006

Revisor: agente independiente, no autor de ninguno de los dos informes. Trabajo documental en solo lectura.
No se han ejecutado casos, producto, scripts del banco ni ninguna API. La única operación de red fue `git fetch`.
No se elige ninguna política económica. Las rutas locales aparecen como `<aux>`.

## 0. Material y versiones fijadas

| Elemento | Commit | Sonda |
|---|---|---|
| Rama de registro `origin/automatizacion/claude-api-piloto-registro` | 953af02c43a36b090fff5f4df3c754e1a4ad59ee | `sondas/00_fetch_y_commits.txt` |
| Rama `origin/automatizacion/coordinacion-api-v1` (`QWEN_CONTRASTE.md`, último cambio a508d6b) | 267ad18d0460c0db84db422a9c06821824bf3b54 | `sondas/QWEN_CONTRASTE.txt` |
| Banco Qwen de referencia: cabeza de `origin/revision/qwen-q1-v2` (`git cat-file -t 4745f38` = commit) | 4745f3887f7fd86bb3052f5d5e32285862df18e3 | `sondas/00_fetch_y_commits.txt` |
| `origin/preparacion/qwen-q1-aceptacion` | 96d21d5 (padre de 4745f38). Solo contiene `docs/qwen_q1/ENCARGO_LOCAL_COMPLETO.md`; 0 archivos `banco_revisado` | ídem |

Integridad (`sondas/integridad_fuentes_y_cita.txt`):
- Los 10 textos de fuente de ambos paquetes (`sources.json`) son idénticos a los blobs de 4745f38: casos líneas 1-6, PLAN, RESUMEN y 7 fixtures. Los blobs declarados por Mistral coinciden.
- La fuente `mistral_review` del contraste Claude es igual al campo `review` de `postprocessed_report.json`, es decir, a la versión con la cita recompuesta. La instantánea e5caa02 que Claude declara (`ledger_snapshot_sha`) no cambia hasta 953af02 (`sondas/snapshot_e5caa02.txt`).

### 0.1 Rechazo inicial por cita maquetada y suplemento

- Original: `qwen-bank-group-01/report.md:15` lleva `"state": "RESULTADO_NO_ACEPTADO_NO_REINTENTAR"` y `:42` lleva `"error": "CITA_NO_LITERAL"` (@953af02).
- Causa verificada: la cita del hallazgo 5 («Recoger observables: respuesta completa; artefactos exportados/publicados (el criterio…) matriz §4 si se expone;») no aparece literal en `PLAN_DE_EJECUCION.md`. En el archivo está partida en `PLAN_DE_EJECUCION.md:31-33` @4745f38. Comprobación: `cita modelo literal en plan: False`.
- Suplemento añadido en c898af7/e5caa02 (`postprocessed_report.json` y `.md`). No toca `report.json` ni `report.md` (`sondas/snapshot_e5caa02.txt`). Lo que se comprobó:
  - el corte `[1666:1830]` del PLAN coincide con `verbatim_source_quote`;
  - sin espacios en blanco, ambas citas son iguales;
  - el resto de la revisión es idéntico al texto visible original: la única diferencia es `/findings[4]/quote`;
  - `raw_visible_model_output` se conserva igual (`sondas/mistral_raw_vs_postprocesado_y_citas.txt`).
- Las demás 11 citas de Mistral son literales.
- Límite: `QWEN_CONTRASTE.md:87` (@267ad18) dice que «Los caracteres permanecen iguales». En sentido estricto no es así: la cita tiene 158 caracteres en el modelo y 164 en la fuente, porque la fuente lleva salto más tres espacios donde el modelo pone un espacio. Son iguales los caracteres no blancos. La regla se llama `SOLO_SALTOS_SUAVES_DE_LINEA_MARKDOWN`, pero también repone la sangría. No altera ninguna interpretación.
- Postprocesado por «ChatGPT» con `postprocessing_added_inference_calls: 0` (campos del JSON). No he podido verificar el código del postprocesado, del que solo consta la huella `39004579…`.

### 0.2 Hecho decisivo que no tenía ninguno de los dos revisores

El contrato primario que Mistral declara ausente está en el propio commit fijado: `docs/qwen_q1/ENCARGO_LOCAL_COMPLETO.md:69-165` @4745f38 (`sondas/encargo_local_completo_4745f38.txt`). Ninguno de los dos paquetes lo incluía, por diseño: `qwen_bank_review.py:34-35` @267ad18 dice «No se ha incluido el contrato primario completo». Las líneas que deciden varias objeciones son estas:
- §3, `:117`: «Una hipótesis conservará su identificación, fundamento, alternativas y límites. No se marcará como dato publicado…»
- §4, `:124`: «entrada → uso → fuente → comprobación → resultado → incidencia.»
- §4, `:128`: «Si se utilizan agentes, no se limitarán a aceptar su registro: examinarán las fuentes correspondientes.»
- §5, `:136`: «…impedirá presentar la conclusión afectada como apta para dinero real.»
- `:75`: SHA-256 del requisito `70c1ac8d…`. `RESUMEN_PARA_INTEGRADOR.md:72` dice «SHA-256 del requisito fuente: no verificado en esta sesión». Yo tampoco lo verifico.

Escala de severidad: `qwen_bank_review.py:44` @267ad18 solo enumera `material/media/menor/limite`, sin definir ninguna (`sondas/escala_severidad.txt`). Por eso las disputas que tratan únicamente de severidad no son decidibles.

---

## 1. Observaciones de Mistral

Referencias del informe: `qwen-bank-group-01/postprocessed_report.md` @953af02. Referencias del banco: @4745f38, salvo indicación.

### M1. «No apta para dinero real» sin operacionalizar (Q1-003, Q1-005, Q1-006; media)

| | |
|---|---|
| Texto de Mistral | `postprocessed_report.md:59`: «Los tres casos de carencia usan como criterio observable que la conclusión afectada 'no se presenta como apta para dinero real', pero ni el banco ni el plan definen qué constituye…» |
| Evidencia a favor | `casos_aceptacion.jsonl:3` (Q1-003, criterio 2): «La conclusión que usa deuda neta no se presenta como apta para dinero real mientras la ausencia no se resuelva.» Ni el PLAN ni el RESUMEN definen qué salida cuenta como «apta». Solo declaran que el banco no la acredita: `PLAN_DE_EJECUCION.md:89-91` («Este banco no declara aptitud para dinero real») y `RESUMEN_PARA_INTEGRADOR.md:86`. |
| Evidencia en contra | La fórmula literal solo está en Q1-003. Q1-005 (`jsonl:5`, criterio 3) dice «la conclusión que usa D no se presenta como apta.» Q1-006 (`jsonl:6`, criterio 3) dice «no se presenta como apta mientras no se resuelva» (`sondas/claude_api_metadatos_y_citas.txt`). Los casos de carencia de la familia son cuatro, no tres: Q1-004 también es `CONFLICTO_CARENCIA` (`jsonl:4`). El término procede del contrato §5 (`ENCARGO_LOCAL_COMPLETO.md:136`). El plan prevé que el integrador «mapear los observables del banco a los del producto» (`PLAN_DE_EJECUCION.md:22-23`) y que lo no expuesto sea NO_OBSERVABLE (`:35`). |
| Veredicto | **CONFIRMADA_CON_LIMITES**. La falta de operacionalización es real y afecta a los tres casos; en Q1-005 y Q1-006 es aún más vaga sin «dinero real». La cita, en cambio, generaliza mal la fórmula literal y omite Q1-004. La definición no puede cerrarse sin el estado que exponga el producto, de modo que corresponde a la fase de mapeo del plan. |

### M2. Q1-002: ningún observable distingue examinar la Nota 2 de copiar el registro (media)

| | |
|---|---|
| Texto de Mistral | `postprocessed_report.md:69`: «un producto que copie el registro sin examinar la nota cumpliría los criterios tal como están redactados (falso positivo).» Recomendación en `:72`: «que la salida cite la Nota 2, pág. 2». |
| Evidencia a favor | La precondición `jsonl:2` dice «El registro no sustituye el examen de esa nota.» La añadió el integrador: `sondas/diff_recibido_vs_revisado_Q1-001_006.txt` y `revision/CAMBIOS_INTEGRADOR_CASOS.json:3-7`. El original decía «Expediente ES-1 con registro de N/A justificado e hipótesis explícita (fixture JSON).» El integrador no añadió ningún criterio. El fundamento contractual está en §4 (`ENCARGO_LOCAL_COMPLETO.md:128`), pero `referencia_requisito` de Q1-002 cita solo §3 (`jsonl:2`). El criterio 1, «La matriz distingue el N/A justificado (con nota de soporte) de una línea ausente», se satisface copiando el JSON, porque el propio registro trae la nota: `fixtures/f1_002_registro.json:18-23`. |
| Límite | La recomendación de Mistral no cierra el hueco. El registro ya contiene la cita: `f1_002_registro.json:4` dice «sin operaciones en moneda extranjera (Nota 2, pag. 2)», y `:19-21` dan documento, página y nota. Exigir que la salida «cite la Nota 2, pág. 2» se cumple igualmente copiando. Solo una variante en la que el texto de la nota no respalde el N/A del registro puede discriminar entre examinar y copiar. La severidad «media» no es decidible (§0.2). |
| Veredicto | **CONFIRMADA_CON_LIMITES**. El hueco existe y está reforzado por §4:128; el remedio propuesto no discrimina. |

### M3. «El resto del expediente» sin archivos (Q1-001, Q1-002; menor)

| | |
|---|---|
| Texto de Mistral | `postprocessed_report.md:80`: «el caso solo declara un archivo sintético y el plan §2.1 ordena cargar solo los archivos del caso». |
| Evidencia | `PLAN_DE_EJECUCION.md:29`: «1. Cargar solo los archivos del caso.» Q1-001 (`jsonl:1`): «…continúa con la matriz y el resto del expediente.» Q1-002 (`jsonl:2`): «¿Puedes continuar con el expediente?» y en actividad: «Registro y contraste del resto de entradas». Ambos casos se llaman «ES-1», el mismo expediente, y Q1-002 cita otra nota del mismo informe (`f1_002_registro.json:19-21`). La frase de Q1-001 puede leerse, por tanto, como una invitación a cargar el fixture de Q1-002, en contra de `PLAN:29`. |
| Límite | En Q1-001 hay una lectura razonable: el «resto» son ingresos y EBITDA del mismo fixture (`f1_001_nota.txt:2`), cubiertos por el criterio 2 («El contraste de ingresos y EBITDA continúa…»). En Q1-002 no hay otras entradas. El mismo defecto afecta a Q1-004 y Q1-006, y Mistral no lo señala (§3). |
| Veredicto | **CONFIRMADA_CON_LIMITES**. |

### M4. «El Excel» que es un CSV (Q1-006; menor)

| | |
|---|---|
| Evidencia | Q1-006 (`jsonl:6`): «El Excel trae minoritarios 0 (fixtures/f1_006_excel.csv)». Precondición: «Excel sintético…». `RESUMEN_PARA_INTEGRADOR.md:39`: «sin XLSX». |
| Límite | Es una convención de todo el banco, no un descuido de Q1-006: hay cinco fixtures `*_excel.csv` (f1_006, f2_010, f3_015, f4_022, f5_027; `sondas/grep_q1004_apta_excel.txt`) y `RESUMEN:21` nombra `f5_027_excel.csv`. El encargo pide simular «Excel frente a extracción» (`ENCARGO_LOCAL_COMPLETO.md:25`) y permite CSV en lugar de XLSX (`:56`). El riesgo es bajo. Si se corrige, conviene hacerlo con una sola declaración en el PLAN («los CSV `*_excel.csv` representan hojas Excel sintéticas») y no solo en Q1-006. |
| Veredicto | **CONFIRMADA_CON_LIMITES**. |

### M5. Contrato primario y código del producto no incluidos (límite)

| | |
|---|---|
| Texto de Mistral | `postprocessed_report.md:105`: «no se ha incluido el contrato primario completo ni el código del producto; por tanto no se puede contrastar que la matriz exigida por §4 tenga las columnas que los criterios asumen (fuente, período, unidad, resultado verificado)». |
| Evidencia | Es correcto para su paquete: `sources.json` @953af02 contiene solo 10 fuentes del banco y el prompt lo declara (`qwen_bank_review.py:34-35`). La cita de apoyo (`PLAN:31-33`) solo muestra que el plan remite a la matriz §4, no la ausencia del contrato. |
| Límite | El contrato sí existe en 4745f38 (§0.2) y permite contrastar lo que Mistral no pudo. §4 fija como columnas «entrada → uso → fuente → comprobación → resultado → incidencia» (`ENCARGO:124`). «Período» y «unidad» son atributos del contraste de §2 (`ENCARGO:98-99`), no columnas literales de §4. Por eso el criterio 1 de Q1-001 puede exigir campos que el producto no tenga por qué mostrar en la matriz (§3, omisión O1). El código del producto sigue sin estar disponible. |
| Veredicto | **CONFIRMADA_CON_LIMITES**. Es cierta como límite del paquete, pero la carencia se puede remediar dentro del mismo commit. |

### Evaluación de casos de Mistral (complementaria)

Mistral calificó los seis casos como COHERENTE_INTERNAMENTE (`postprocessed_report.md:10-46`). Su prompt admitía AMBIGUO e INCONSISTENTE (`qwen_bank_review.py:40`).

| Caso | Veredicto del cotejo | Motivo breve |
|---|---|---|
| Q1-001 | CONFIRMADA_CON_LIMITES | Coherente, pero con riesgo de falso negativo en un control positivo (O1). |
| Q1-002 | CONFIRMADA_CON_LIMITES | Coherente. El hueco de M2 está reconocido por el propio Mistral. |
| Q1-003 | CONFIRMADA | El fixture `f1_003_tabla.txt:1-2` respalda todos los criterios. |
| Q1-004 | **NO_CONFIRMADA** | Los criterios piden conservar alternativas y límites que el fixture no tiene (C1). Debió calificarse AMBIGUO o INCONSISTENTE. |
| Q1-005 | CONFIRMADA_CON_LIMITES | La aritmética 1200-1050=150 y la regla opN (`PLAN:80-83`) son correctas, igual que la corrección v2 n.º 4 citada (`RESUMEN:23-24`). El criterio de «apta» carece de conclusión observable (O5). |
| Q1-006 | CONFIRMADA_CON_LIMITES | Coherente. Los criterios de continuación y de «apta» son vacíos (O4, O5). |

---

## 2. Objeciones de Claude API

Referencias del informe: `qwen-peer-group-01/report.md` @953af02. Modelo: `claude-sonnet-5-5`, esfuerzo pedido `high`, `stop_reason end_turn`, un mensaje (`report.json`).

### C1. El fixture de Q1-004 carece de fundamento, alternativas y límites (media)

| | |
|---|---|
| Texto de Claude | `report.md:9`: «el único fixture (f1_004_nota.txt) solo dice "Margen EBITDA estimado por el analista: 18%. Estimacion interna; no es cifra publicada". No contiene fundamento, alternativas ni límites que conservar, a diferencia de Q1-002…» |
| Evidencia | Fixture completo, `fixtures/f1_004_nota.txt:1`: «SINTETICA TRES S.A. - Pagina 3 - Nota 7: Margen EBITDA estimado por el analista: 18%. Estimacion interna; no es cifra publicada por la sociedad.» La cita de Claude es un prefijo literal. Los criterios de `jsonl:4` dicen «La salida conserva la etiqueta de hipótesis/estimación con su fundamento.» y «El registro de la hipótesis (alternativas, límites) se mantiene y la actividad continúa.» Entre las conductas inaceptables: «Eliminar alternativas y límites al reetiquetar.» En contraste, Q1-002 sí los trae: `f1_002_registro.json:10-15` (alternativas `[1, 3]`, «no extrapolable mas de 3 ejercicios»). La precondición de Q1-004 no declara ningún registro previo de la hipótesis: «Nota sintética que declara el margen 18% como estimación interna.» Mistral lo dio por bueno en `postprocessed_report.md:32`: «mantener alternativas y límites». |
| Límite | «No contiene fundamento» es demasiado absoluto. El fixture atribuye la cifra («estimado por el analista», «Estimacion interna»), que es un fundamento mínimo de procedencia, aunque no de método. El criterio tiene base contractual en §3 (`ENCARGO:117`); lo que falla es el fixture o la redacción, no el requisito. |
| Veredicto | **CONFIRMADA_CON_LIMITES**. La inconsistencia sobre alternativas, límites y registro está confirmada; la ausencia de fundamento es solo parcial. |

### C2. Mistral exageró el punto «dinero real» (menor)

| | |
|---|---|
| Texto de Claude | `report.md:16`: «Esa fórmula figura literalmente solo en Q1-003… La crítica de falta de operacionalización queda sobredimensionada para esos dos casos. Además, la recomendación de marcar el artefacto como 'limitada/pendiente de fuente' propone estados que ninguna fuente del paquete define». Corrección propuesta en `:17`: «Para Q1-005 y Q1-006 basta con que la salida no presente la conclusión como apta.» |
| Lo que se confirma | El dato literal: «dinero real» aparece en los casos solo en Q1-001 (`conclusion_afectada`, no es criterio) y en Q1-003 (criterio). Sonda en `sondas/claude_api_metadatos_y_citas.txt`. |
| Lo que no se confirma | (a) Quitar «dinero real» no hace operacional el criterio; «apta» a secas es más vaga, y la propuesta de `:17` deja el problema sin resolver. (b) «Estados que ninguna fuente define» es inexacto. Mistral los presenta como ejemplo («p. ej.») y ese vocabulario figura en el paquete: Q1-006, criterio 1, dice «ausencia/pendiente de fuente» (`jsonl:6`); `PLAN:74-75` dice «solo la conclusion afectada se limita»; Q1-005, actividad, dice «registro de D con etiqueta de pendiente» (`jsonl:5`). (c) El remedio NO_OBSERVABLE (`PLAN:35`) cubre el estado no expuesto, no la ambigüedad de un criterio cuando el estado sí se expone. |
| Veredicto | **CONFIRMADA_CON_LIMITES**. La imprecisión de la cita de Mistral es real. No se sostiene que el hallazgo deba limitarse a Q1-003. |

### C3. Mistral cita una corrección v2 inexistente (menor)

| | |
|---|---|
| Texto | Mistral, `postprocessed_report.md:32`: «coherente con §3 citado y con la corrección v2 de no reetiquetar hipótesis». Claude, `report.md:23`: «La lista de las 7 correcciones v2 del resumen no incluye ninguna sobre Q1-004…» |
| Evidencia | `RESUMEN_PARA_INTEGRADOR.md:14-31` enumera siete correcciones: (1) Q1-010/007, (2) Q1-018, (3) Q1-026/027, (4) Q1-005, (5) el comprobador, (6) Q1-034 y (7) el plan y la clasificación. Ninguna trata de Q1-004 ni de reetiquetar. Las precisiones del integrador (`revision/CAMBIOS_INTEGRADOR_CASOS.json:1-53`) afectan a 002, 006, 007, 023, 025, 030, 034 y 035, no a 004. Q1-004 es idéntico en `recibido/` y en `banco_revisado/` (`sondas/diff_recibido_vs_revisado_Q1-001_006.txt`). `git grep "reetiquet"` solo da el `riesgo_que_detecta` del propio caso (`jsonl:4`: «Reetiquetar una hipótesis como cifra publicada…»), que probablemente es el origen de la confusión. |
| Veredicto | **CONFIRMADA**. |

### C4. Mistral sobredimensiona Q1-002 (menor)

| | |
|---|---|
| Texto de Claude | `report.md:30`: «El criterio 1 ya exige que la matriz distinga el N/A "(con nota de soporte)"… y el JSON incorpora el texto de la nota en nota_soporte. El hueco existe solo en parte… La severidad 'media' resulta alta». |
| Evidencia | Es literal que el criterio 1 contiene «(con nota de soporte)» (`jsonl:2`). Pero el argumento no refuta el de Mistral, sino que lo confirma: como la nota viene dentro del mismo registro (`f1_002_registro.json:18-23`), copiar el registro satisface el criterio 1 sin examen alguno. La cuestión de la severidad no es decidible porque la escala no está definida (§0.2). Claude acierta en que exigir la cita sería una propuesta nueva (`PLAN:65-68`), pero, como se explica en M2, esa cita tampoco discrimina. |
| Veredicto | **NO_CONFIRMADA** en lo sustancial: el criterio 1 no cierra el hueco ni siquiera en parte. La rebaja de severidad es NO_DECIDIBLE. |

---

## 3. Hallazgos del banco para el integrador (propuestas; nada se aplica)

### H1. Q1-004 (C1). Corrección propuesta, a decidir por el integrador

Se proponen dos alternativas excluyentes.

- **Opción B, mínima y sin datos nuevos.** Es la que recomiendo porque no introduce cifras.
  - `precondiciones`: «Nota sintética que declara el margen 18% como estimación interna del analista, sin fundamento metodológico, alternativas ni límites; no existe registro previo de la hipótesis.»
  - `criterios_observables`:
    1. «La salida conserva la etiqueta de estimación no publicada y su atribución al analista (Nota 7, pág. 3).»
    2. «La matriz no marca el margen como publicado.»
    3. «La salida registra como incidencia que la hipótesis carece de fundamento metodológico, alternativas y límites (§3), sin inventarlos; la actividad no dependiente continúa.»
  - `conductas_inaceptables`: mantener «Marcar 18% como dato publicado.» y sustituir la segunda por «Inventar fundamento, alternativas o límites no presentes en la fuente.»
  - Qué debe hacer el producto con una hipótesis incompleta (limitar su uso, admitirla con incidencia) no está fijado en el contrato. El criterio 3 debe declararse PROPUESTA dentro del caso (`PLAN:67-68`), no como obligación.
- **Opción A, enriquecer el fixture.** Añadir a `f1_004_nota.txt` fundamento, alternativas y límites sintéticos, con el mismo formato que `f1_002_registro.json:10-15`, y regenerar el manifiesto. Hay que reproducir `MANIFIESTO_SHA256.txt` y `materializar_fixtures.py:9`, porque contiene el texto del fixture. Esto cambia una fuente del banco y exigiría nueva versión y revisión.
- En ambas opciones, `actividad_que_puede_continuar` («contraste del resto de entradas publicadas») queda vacía porque el fixture no publica ninguna entrada (O4). Hay que eliminarla o añadir una línea publicada al fixture.

### H2. Resto de propuestas

- **H2, Q1-002 (M2/C4).** Añadir §4 a `referencia_requisito` (`ENCARGO:128`). Proponer como PROPUESTA_ACEPTACION una variante en la que `nota_soporte.texto` no respalde el N/A del registro. Es la única forma de observar el examen frente a la copia; no sustituye el caso positivo.
- **H3, «apta» (M1/C2).** Vincular los criterios de Q1-003, Q1-005 y Q1-006 a §5 (`ENCARGO:136`) y remitir su definición al mapeo de observables del producto (`PLAN:21-23`), con NO_OBSERVABLE si no se expone. No inventar estados.
- **H4, Q1-001.** El criterio 1 fija «fuente (pág.2, nota 3)», pero el cero también está publicado en la Tabla 1, pág. 1 (`f1_001_nota.txt:2`). Conviene aceptar cualquiera de las dos o ambas para no producir un falso negativo en un control positivo. Además, «período» y «unidad» deben observarse como atributos del contraste (§2) y no necesariamente como columnas de la matriz §4 (`ENCARGO:124`).
- **H5, convención Excel/CSV (M4).** Hacer una única declaración en el PLAN.
- **H6.** Verificar el SHA-256 del requisito (`ENCARGO:75`), pendiente según `RESUMEN:72`.

---

## 4. Qué omitieron ambos informes en Q1-001…006

- **O1, Q1-001.** Riesgo de falso negativo en un control POSITIVO: la fuente exigida es solo «pág.2, nota 3» (`jsonl:1`), aunque `f1_001_nota.txt:2` publica también «Deuda financiera 0» en la Tabla 1, pág. 1. El criterio tampoco pide la versión del documento, «(v1)» en `f1_001_nota.txt:1`, que §2 exige (`ENCARGO:95`).
- **O2, Q1-001.** El criterio 1 exige en «la matriz exigida por §4» período y unidad, que §4 no enumera como columnas (`ENCARGO:124`). Puede exigir campos que el producto no tiene (`ENCARGO:44`, «sin inventar campos del producto»). Mistral lo intuyó como límite (M5), pero no lo concretó.
- **O3, Q1-002.** El requisito de §4 «examinarán las fuentes» (`ENCARGO:128`), del que procede la precondición del integrador, no figura en `referencia_requisito` (`jsonl:2`, «§3» solamente). Ninguno de los dos vio que la cita propuesta por Mistral ya está en el registro (`f1_002_registro.json:4`).
- **O4, Q1-004 y Q1-006.** Los criterios y las actividades de continuación no tienen objeto: Q1-004 dice «contraste del resto de entradas publicadas» (`jsonl:4`) y Q1-006 dice «el resto del contraste continúa» y «Contraste del resto de entradas» (`jsonl:6`), pero sus fixtures no contienen otras entradas (`f1_004_nota.txt:1`, `f1_006_excel.csv:1-2`, `f1_006_nota.txt:1`). Esos criterios se cumplen trivialmente o no son observables. Mistral solo lo señaló para Q1-001 y Q1-002.
- **O5, Q1-005 y Q1-006.** La entrada no pide ninguna conclusión. Q1-005 pide calcular D y marcarla como comprobada; Q1-006 pide usar el 0. Sin embargo, el criterio exige que «la conclusión que usa D/minoritarios no se presenta como apta». Sin conclusión solicitada, el criterio es probablemente NO_OBSERVABLE. Q1-003 sí pide «termina la valoración». La propuesta de Claude («basta con que la salida no presente la conclusión como apta») hereda este vacío.
- **O6, Q1-004.** La precondición no declara un registro previo de la hipótesis, pero el criterio 3 dice que «El registro… se mantiene». Claude lo rozó, pero no lo separó de la carencia del fixture.
- **O7, familia.** Mistral cuenta «tres casos de carencia», pero son cuatro (Q1-003 a Q1-006). Ninguno de los dos contrastó la cobertura de la familia 1 con el encargo (`ENCARGO:21-23`); el cotejo la encuentra completa: dos positivos y cero, ausencia, N/A, hipótesis y derivado cubiertos.
- **O8, proceso.** Claude no se pronuncia sobre M5 ni sobre la validez del suplemento de cita. La afirmación de `QWEN_CONTRASTE.md:87` sobre caracteres idénticos es inexacta en los espacios en blanco (§0.1).

## 5. Conclusiones

1. Las seis evaluaciones y cinco observaciones de Mistral son, en lo esencial, defendibles. Hay una excepción material: declaró Q1-004 COHERENTE_INTERNAMENTE apoyándose en una corrección v2 que no existe (C3, CONFIRMADA) y sin advertir que el fixture no contiene alternativas ni límites (C1, CONFIRMADA_CON_LIMITES).
2. De las cuatro objeciones de Claude API, la más útil es C1 y la más sólida es C3. C2 acierta en la literalidad, pero se equivoca al proponer limitar el hallazgo. C4 no se sostiene: su argumento refuerza el hueco que quiere minimizar.
3. Las observaciones de Mistral reciben estos veredictos: M1, M2, M3, M4 y M5, CONFIRMADA_CON_LIMITES; ninguna queda NO_CONFIRMADA.
4. El hecho que más cambia el análisis es que el contrato está en `docs/qwen_q1/ENCARGO_LOCAL_COMPLETO.md` @4745f38 y ninguno de los dos lo tuvo. Con él se resuelven M5 y el origen de M1/C2 (§5:136), se refuerza M2 (§4:128) y se fundamenta C1 (§3:117).
5. El suplemento de cita es fiel en caracteres no blancos y no añade inferencias.
6. Nada de lo anterior es ejecución del producto ni aceptación de ningún informe. El banco sigue con 0/36 recorridos y NO_EJECUTADO. Las correcciones H1 a H6 son propuestas para el integrador.
