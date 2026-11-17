# Estado único de Munger V2

Corte: 2026-11-17 ~12:10 UTC; consulta remota del coordinador (A 0946971, D d032691, E f00c5dd, F 98bdf8f, G a0524d9 sin cambios; automatización a508d6b, registro 953af02).

Reorientado al universo real de la persona responsable (17-nov): examen del personaje con cinco empresas reales y tope de 4–6 días; sin aptitud económica acreditada hasta el veredicto final.

**Fuente:** CONTROL.json. Este panel resume evidencia registrada; no observa sesiones privadas, no ejecuta agentes y no acredita por sí solo aptitud económica.

Candidata integrada: integracion/candidata-cierre-v2 @ b129b36 (957af65 + G-DOCS + G-RAIZ; solo documentos). Mantenedor: Claude coordinador, único escritor.

| ID | Dueño | Entregado | Revisado | Integrado | Pruebas autor / externas | Origen |
|---|---|---|---|---|---|---|
| F1-W | Claude | ENTREGADO | CONFORME_CON_LIMITES | NO | EJECUTADAS / PARCIALES | d519eb0 |
| C20 | Claude | ENTREGADO | CONFORME_CON_LIMITES | NO | EJECUTADAS / PARCIALES | bf0d5c2 |
| CSV | Claude | ENTREGADO | CONFORME_CON_LIMITES | NO | EJECUTADAS / PARCIALES | 77ff89f |
| A-CTX | Mistral A | ENTREGADO | CORRECCIONES | NO | DECLARADAS / REPRODUCIDAS | 0946971 |
| D-HARNESS | Mistral D | ENTREGADO | CORRECCIONES | NO | DECLARADAS / PARCIALES | c734ca1 |
| D-36 | Mistral D + Claude runtime | PARCIAL | CORRECCIONES | NO | DECLARADAS / PARCIALES | d032691 |
| E-ELIS | Antigua Mistral B, nueva E | ENTREGADO | CORRECCIONES | NO | DECLARADAS / REPRODUCIDAS | ea641e7 |
| B-PM1 | Mistral B (autor previo) | PARCIAL | CONFORME_CON_LIMITES | NO | DECLARADAS / REPRODUCIDAS | daa7478 |
| C-C2 | Mistral C (autor previo) | ENTREGADO | CONFORME_CON_LIMITES | NO | DECLARADAS / REPRODUCIDAS | 1ec4f18 |
| F-REV | Antigua Mistral C, nueva F | ENTREGADO | CORRECCIONES | NO | EJECUTADAS / NO_EJECUTADAS | c504830 |
| F-B3 | Mistral C/F prepara; Claude orquesta | PARCIAL | CORRECCIONES | NO | DECLARADAS / REPRODUCIDAS | 98bdf8f |
| F-C1 | Mistral C/F prepara; Claude orquesta | PARCIAL | CORRECCIONES | NO | DECLARADAS / REPRODUCIDAS | 98bdf8f |
| G-MANUAL | Claude coordinador (borrador por un subagente de redacción) | ENTREGADO | CONFORME_CON_LIMITES | NO | NO_EJECUTADAS / PARCIALES | 341831f |
| G-DOCS | Claude coordinador | ENTREGADO | CONFORME_CON_LIMITES | SI | EJECUTADAS / REPRODUCIDAS | c0542b8 |
| G-RAIZ | Claude coordinador | ENTREGADO | CONFORME_CON_LIMITES | SI | EJECUTADAS / REPRODUCIDAS | e813fe6 |
| T-CAND | Claude coordinador | ENTREGADO | PENDIENTE | NO | EJECUTADAS / NO_EJECUTADAS | 957af65 |
| T-EXP | Claude runtime + extractores/revisores reales | PENDIENTE | PENDIENTE | NO | NO_EJECUTADAS / NO_EJECUTADAS | — |
| T-CAMBIOS | Claude runtime + Mistral D | PENDIENTE | PENDIENTE | NO | NO_EJECUTADAS / NO_EJECUTADAS | — |
| T-TRASPASO | Claude + receptor sin historial | ENTREGADO | CONFORME_CON_LIMITES | NO | EJECUTADAS / PARCIALES | 788f25c |
| H-DEC | Usuario | PARCIAL | PENDIENTE | NO | NO_EJECUTADAS / NO_EJECUTADAS | — |
| F1-IMPL | Claude | PENDIENTE | PENDIENTE | NO | NO_EJECUTADAS / NO_EJECUTADAS | — |
| T-AUTO | Usuario (ramas automatizacion/*, preparadas con ChatGPT) | ENTREGADO | CORRECCIONES | NO | DECLARADAS / REPRODUCIDAS | a508d6b |
| Q-CONTRASTE | Mistral (Vibe) + contraste Claude API | PARCIAL | LIMITADA | NO | NO_EJECUTADAS / NO_EJECUTADAS | 953af02 |
| CIERRE | Claude + usuario | PENDIENTE | PENDIENTE | NO | NO_EJECUTADAS / NO_EJECUTADAS | — |

## Próxima acción y dependencias por tarea

- **F1-W · F1 W1–W3 entregada y contrastada por Mistral C/F; propuesta no adoptada**: Nada en esta tarea. La implementación de W1 en el producto depende de las decisiones (1a)–(5b) (F1-IMPL, H-DEC); no se integra en la candidata porque no es software del producto.
- **C20 · C20: U1–U6 del verificador respondidas; contraste pendiente**: Nada en esta tarea. No es software del producto: no se integra en la candidata; queda en la rama F1.
- **CSV · Cifras [LECTURA] al CSV verificado (bloque CSV de ENCARGO_C20_CSV.md, f5775dc)**: Nada en esta tarea. No es software del producto: no se integra en la candidata; queda en la rama F1.
  Dependencias: C20.
- **A-CTX · Evidencia contextual A v3**: Mistral A: primero la revisión de G-RAIZ (3d66437); después A4-R1…R6 (CORRECCION_A4.md) en la rama A. T-EXP sigue bloqueado por A-CTX.
- **D-HARNESS · Arnés D v2 y paquetes íntegros**: Revisión crítica de D3 (328fa31 y c734ca1) hecha por un contexto distinto (Fable, máximo): NO cierra D3. R4 y R8 sin tratar: generar_relevo.py sin cambios desde 5f4b2a2, lo comprobó el coordinador; en lo publicado, 0/36 paquetes con estado inicial, fases y artefacto por criterio. R1 abierto (cinco vías nuevas de autolectura) y R2 abierto (prueba 34 que no puede fallar; Q1-017). Q1-026 no tiene bloqueo de entorno. R6 empeora: el manifiesto da código 1. pruebas_arnes v4 aborta en la prueba 4. CORRECCION_D4 va a Mistral D.
- **D-36 · Aceptación completa de 36 casos Qwen**: 0/36 casos ejecutables sin interpretar: falta el relevo en los 29 con componente y en Q1-026, y todo en Q1-028/031/032/033; Q1-030 y Q1-035 esperan decisión del usuario. Los 30 componentes sí se ejecutan con ejecutar_todo.sh y SHA_CANDIDATA_ESPERADO=b129b36. El personaje no se ejecuta hasta que se cierre D4.
  Dependencias: D-HARNESS, T-CAND.
  Bloqueo/límite: No falta capacidad: el personaje se ejecuta con código 10 y subagentes de la sesión orquestadora (modelo y esfuerzo de config_v2.json, fase C con el mismo agente, auditoría con agente nuevo; sin API). Comprobado en 957af65: réplica hasta el código 10, paso 5. Bloqueo real: la adaptación de los 36 casos sintéticos a vías soportadas y la correspondencia criterio→observable (D2-R4/R5, Mistral D), que exige el propio PLAN_DE_EJECUCION del banco.
- **E-ELIS · Fuentes M1/M2/M6/N2 de Elis**: E2 (ea641e7) revisada: D1 central cerrado con límites (las seis importantes suman 60,8, verificado en p.341). D2, D3 y D5 con residuos; D4 y D6–D9 cerrados. Dos defectos nuevos medios: E3-1 (cita del factsheet que solo casa por el orden de extracción) y E3-2 (la reproducción reescribe el índice de descargas: no es idempotente). CORRECCION_E3 va a Mistral E. M1, M2, M6 y N2 siguen ABIERTOS.
- **B-PM1 · Dossier P-M1 corregido; contraste documental pendiente**: Dato de las nueve altas aceptado con límites (revisión del coordinador sobre daa7478 y contraste 223f16d). P-M1 sigue bloqueado: no se identifica θ/λ ni se adopta política. Nada que integrar en el producto sin decisión.
  Bloqueo/límite: P-M1 no delimitada con evidencia disponible; 4 PDF nuevos con preservación pendiente.
- **C-C2 · Guarda de perímetros C2**: Decisión del integrador: no se incorpora a la candidata. Es herramienta de contraste del auxiliar, no software del producto, y conserva C1 y D1/D7/D11 pendientes. Se conserva el enlace (1ec4f18, SEGUIMIENTO.md @ b049777); se usa como oráculo de contraste solo dentro de su alcance.
- **F-REV · Contraste independiente de cambios Claude**: F3 (c504830) revisada: sin defectos materiales. Cerrados R3–R5, R7, R8 y R10; R6, R9, R11 y R13 con límites; abiertos R12 (PROTOCOLO_CONGELADO conserva criterios C propios), R14 y R15. Tres menores nuevos. El contrato C de c4d918f no da Fineco por elegida, pero arrastra supuestos que U3 ha dejado atrás. CORRECCION_F4 va a Mistral F.
- **F-B3 · Tercer B real fuera de muestra**: Inventario reproducible aceptado con límites (F2-D1 cerrado; 71 PDF con huella). Mistral C/F corrige F3-R3 (.bat de Ahold), R4 y textos. La ejecución depende de U2 (etapa 1 de Ahold).
  Bloqueo/límite: No hay huellas históricas de los PDF de Ahold: 11 SIN_HISTÓRICA. El HUELLAS.txt del .bat solo habría cubierto 2016–2018 y el folleto, y el .bat no llegó a ejecutarse. Pendiente de la persona responsable: el SHA-256 (certutil) de sus PDF 2019–2025 de la carpeta KONINKLIJKE AHOLD DELHAIZE y de los dos originales aportados. Sin verificar: la edición del AR2025 (la cita L17, p.210, no casa), FS25, Q2-26 y los pkg_*.
- **F-C1 · Primer recorrido C real y contrato específico**: U3, por decisión de la persona responsable: Hannover Rück se conserva como prueba negativa de «modelo no aplicable», no como sustituto del caso C aplicable. Se busca un banco compatible con el motor y el protocolo, separando los bloqueos de acceso a documentos de los incumplimientos del protocolo. Las fuentes de Hannover se conservan en una Release.
  Bloqueo/límite: Documentos oficiales de los candidatos sin verificar: descarga de FinecoBank denegada por el control de permisos de la sesión; Hannover Re responde 403 a curl. Hace falta que la persona responsable autorice esas descargas o deje ella los documentos (informe anual 2025 y Pilar 3 o SFCR 2025 de cada candidato).
- **G-MANUAL · Manual, instalación y recuperación desde contexto limpio**: v4 (ea70e23) entregada para b129b36 por un contexto Claude autor: cierra N1 y n1–n9. Falta la revisión de lo afectado por otro contexto; se propone que la haga Mistral R, que es de otra familia de modelos. Después, la propuesta §2.5 (ampliada al 4.8) como cambio documental de la candidata, con su revisión.
  Dependencias: T-CAND.
- **G-DOCS · Corrección documental de la guía del recorrido y de CONTINUIDAD en una rama aislada de la candidata (sin cambios de código)**: Integrado en la candidata (3149128). Nada más en esta tarea.
  Dependencias: G-MANUAL.
- **G-RAIZ · U4: hechos desfasados de README, CLAUDE.md y docs/MIGRATION_STATUS.json de la raíz, en una rama aislada (instrucciones sustantivas conservadas)**: Integrado en la candidata, b129b36. Queda abierto el menor N1 (precisar «de la persona responsable» en README.md:7), para una próxima corrección documental. Mistral A revisó 3d66437 por su cuenta (e61d66d) y dio CONFORME CON LÍMITES; se conserva como contraste.
- **T-CAND · Candidata única de integración técnica**: Candidata en b129b36: G-DOCS (3149128) más G-RAIZ (tres archivos raíz). Sin cambios en el código; manifiesto del producto conforme. La verificación completa de 957af65 sigue valiendo para el código.
- **T-EXP · Expedientes nuevos regenerados y auditados**: Regenerar entradas/fuentes/derivados, sin sustituir hipótesis o ausencias; auditoría del material nuevo.
  Dependencias: T-CAND, A-CTX.
- **T-CAMBIOS · Vigencia, invalidación, recuperación y H9**: Ensayar cambio anterior y punto real de reanudación; no reintroducir límites I19/I20 ya corregidos.
  Dependencias: T-CAND, D-HARNESS.
- **T-TRASPASO · Traspaso sin historial y revisión de manual**: Aceptado con límites (sin pasos de agentes; el registro no guarda transcripción ni la mayoría de códigos; receptor de la misma familia de modelo). Pasos con agentes reales: runtime del coordinador. Mejoras del manual en MEJORAS_MANUAL.md (G-MANUAL).
  Dependencias: T-CAND, G-MANUAL.
- **H-DEC · Decisiones económicas pendientes con fundamento**: Las tres propuestas (9cad78d) están revisadas por un contexto distinto con Fable al máximo: las tres CONFORME_CON_LIMITES, sin hallazgos materiales, con 6 medios y 14 menores; ninguno cambia cifras. Alcance: presentar B (2022–25) como opción frente a A′ y A, con 2021 «no acreditada»; la decisión real es binaria y vale 0,72 en el flujo (0,23 % del FCF base). México: dos opciones, sin recomendación. Umbral: el 0,1 % es convencional y «sin umbral» está presentada con justicia. Vuelven a la persona responsable; Elis sigue bloqueada por R.
  Dependencias: F1-W.
  Bloqueo/límite: No hay adopción de políticas económicas nuevas en este programa.
- **F1-IMPL · Implementación económica F1 autorizada**: Puede preparar parche propuesto separado; no activar cambios económicos antes de decisión explícita.
  Dependencias: F1-W, H-DEC, T-CAND.
  Bloqueo/límite: Datos/políticas económicos pendientes; Elis sigue pendiente_de_datos.
- **T-AUTO · Automatización de coordinación (infraestructura: piloto Claude API, coordinación común, Vibe CLI, contrastes Qwen)**: AUTO1 (422a6f3) revisada por un contexto distinto: conforme con observaciones, sin hallazgos materiales. 95+49 pruebas, sonda SSE 25/25, 0 jobs no conformes; 41 de 44 pruebas nuevas fallan sobre a508d6b y 10 de 10 mutantes detectados. Siguen abiertos M7 (hashes), m6 (ruleset) y las observaciones N1–N6. N2: Vibe CLI puede leer el GH_TOKEN con escritura del proceso padre; hay que separarlo. Pendiente del usuario: crear el environment inferencia-aprobada con revisores, mover allí los secretos, fijar el tope y decidir si los workflows pasan a main. El autor de 422a6f3 es un contexto Claude de esta sesión. No integrado ni adoptado: la rama del usuario no cambia.
  Bloqueo/límite: Infraestructura, no producto. Ni se adopta ni se fusiona main; PR #1 queda en borrador. No hay agente API que aplique correcciones ni una cola continua autorizada. audit-pilot-code-001 no se repite. No se cambia la facturación ni se activa pay-as-you-go. Sus informes son contrastes documentales: no ejecutan el personaje, no aceptan entregas y no sustituyen correcciones (D3) ni revisiones del coordinador.
- **Q-CONTRASTE · Contraste documental del banco Qwen (Q1, 36 casos) en tandas de seis**: Tanda 01 cotejada por un contexto distinto. Mistral: M1–M5 confirmadas con límites; Q1-004 «coherente internamente», no confirmada. Claude API: C3 confirmada, C1 y C2 con límites, C4 no confirmada. Ninguno de los dos revisores tuvo el contrato §2–§7 (ENCARGO_LOCAL_COMPLETO.md:69-165). Correcciones propuestas al banco sin aplicar (Q1-004 opción B, mínima; Q1-002 §4; Q1-001 doble fuente del cero). Las aplica, si procede, el dueño del banco o Mistral D dentro de D3. Tandas 02–06 aparcadas.
  Dependencias: T-AUTO.
  Bloqueo/límite: Revisión documental del banco. No ejecuta casos del personaje (siguen 0/36) y no sustituye el banco anterior, que se conserva, ni la aceptación D-36.
- **CIERRE · Entrega final por alcance declarado**: Evaluar criterios de cierre, no porcentaje; no reducir alcance original por inferencia.
  Dependencias: D-36, T-EXP, T-CAMBIOS, T-TRASPASO, F-B3, F-C1, H-DEC, B-PM1, C20, CSV, A-CTX, F1-IMPL.

## Solicitudes de revisión

- F1-W: RESPONDIDA; revisor asignado: Mistral C/F; SHA: d519eb04978e64d04f1d1795c570ca96bdd7ad7f.
- C20: RESPONDIDA; revisor asignado: Mistral C/F; SHA: bf0d5c25d136ae9b2b1f14e4688081e1792d2363.
- CSV: RESPONDIDA; revisor asignado: Mistral C/F; SHA: 77ff89f8fe99a1b5f013243ea1ccd4b84512ac51.
- A-CTX: RESPONDIDA; revisor asignado: Claude coordinador (subagente de revisión); SHA: 0946971e1e4cf10cb85ed4c757968a4bd060d6a7.
- E-ELIS: RESPONDIDA; revisor asignado: Claude coordinador (subagente de revisión); SHA: f00c5dd64cb956b93ebb199389ce748e9d218f6c.
- G-MANUAL: RESPONDIDA; revisor asignado: Subagente Claude, contexto distinto del autor (no hay sesión Mistral libre); SHA: ef36ab18ff485e40dbb727b1b95eb177e5346683.
- G-DOCS: RESPONDIDA; revisor asignado: Mistral A, en mistral/g-manual-traspaso (antes de A3), u otro contexto distinto; SHA: c0542b83b9923f98124d3c72e48b7fc7245284d2.
- G-RAIZ: RESPONDIDA; revisor asignado: Subagente Claude, contexto distinto del autor; SHA: e813fe66b0210a698398d4f9a4d84788f9dda8e3.
- T-AUTO: RESPONDIDA; revisor asignado: Subagente Claude, contexto distinto del autor; SHA: a508d6b38168933d9e6ef480e0d23627b8d748fb.

## Cómo se decide el cierre

PROGRAMA.md fija los criterios: candidata trazable; datos/derivados y decisiones vigentes; pruebas y recorrido real; alcance por motor; manual, recuperación y traspaso. No se calcula porcentaje global. Un bloqueo económico puede permitir continuar trabajo técnico sin convertir el expediente en apto.

Las pruebas antiguas solo se conservan cuando sus dependencias no cambian. Ninguna marca del plan de la interfaz sustituye la evidencia de un commit, prueba o revisión.
