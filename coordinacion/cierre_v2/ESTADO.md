# Estado único de Munger V2

Corte: 2026-11-17 ~09:50 UTC; consulta remota del coordinador (F hasta c761cc8, D hasta 5f4b2a2).

Cierre en preparación: entregas parciales y revisiones pendientes; sin aptitud económica global acreditada.

**Fuente:** CONTROL.json. Este panel resume evidencia registrada; no observa sesiones privadas, no ejecuta agentes y no acredita por sí solo aptitud económica.

Candidata integrada: {'repositorio': 'jluisplagos/munger-v2', 'rama': 'integracion/candidata-cierre-v2', 'base': '957af652cdc3bef3d67e8623c9572138bac685e9', 'head': '31491289a9a13a670dd563c1b2df85dad54eb74a', 'estado': '957af65 + G-DOCS (3149128; 4 archivos documentales revisados). Código sin cambios; manifiesto 7762/7762'}. Mantenedor: Claude coordinador, único escritor.

| ID | Dueño | Entregado | Revisado | Integrado | Pruebas autor / externas | Origen |
|---|---|---|---|---|---|---|
| F1-W | Claude | ENTREGADO | CONFORME_CON_LIMITES | NO | EJECUTADAS / PARCIALES | d519eb0 |
| C20 | Claude | ENTREGADO | CONFORME_CON_LIMITES | NO | EJECUTADAS / PARCIALES | bf0d5c2 |
| CSV | Claude | ENTREGADO | CONFORME_CON_LIMITES | NO | EJECUTADAS / PARCIALES | 77ff89f |
| A-CTX | Mistral A | ENTREGADO | CORRECCIONES | NO | DECLARADAS / REPRODUCIDAS | 0946971 |
| D-HARNESS | Mistral D | ENTREGADO | CORRECCIONES | NO | DECLARADAS / PARCIALES | d032691 |
| D-36 | Mistral D + Claude runtime | PARCIAL | CORRECCIONES | NO | DECLARADAS / PARCIALES | d032691 |
| E-ELIS | Antigua Mistral B, nueva E | ENTREGADO | CORRECCIONES | NO | DECLARADAS / REPRODUCIDAS | f00c5dd |
| B-PM1 | Mistral B (autor previo) | PARCIAL | CONFORME_CON_LIMITES | NO | DECLARADAS / REPRODUCIDAS | daa7478 |
| C-C2 | Mistral C (autor previo) | ENTREGADO | CONFORME_CON_LIMITES | NO | DECLARADAS / REPRODUCIDAS | 1ec4f18 |
| F-REV | Antigua Mistral C, nueva F | ENTREGADO | CONFORME_CON_LIMITES | NO | EJECUTADAS / NO_EJECUTADAS | c7716a0 |
| F-B3 | Mistral C/F prepara; Claude orquesta | PARCIAL | CORRECCIONES | NO | DECLARADAS / REPRODUCIDAS | 98bdf8f |
| F-C1 | Mistral C/F prepara; Claude orquesta | PARCIAL | CORRECCIONES | NO | DECLARADAS / REPRODUCIDAS | 98bdf8f |
| G-MANUAL | Claude coordinador (borrador por un subagente de redacción) | PARCIAL | CONFORME_CON_LIMITES | NO | NO_EJECUTADAS / PARCIALES | 341831f |
| G-DOCS | Claude coordinador | ENTREGADO | CONFORME_CON_LIMITES | SI | EJECUTADAS / REPRODUCIDAS | c0542b8 |
| G-RAIZ | Claude coordinador | ENTREGADO | PENDIENTE | NO | EJECUTADAS / NO_EJECUTADAS | 3d66437 |
| T-CAND | Claude coordinador | ENTREGADO | PENDIENTE | NO | EJECUTADAS / NO_EJECUTADAS | 957af65 |
| T-EXP | Claude runtime + extractores/revisores reales | PENDIENTE | PENDIENTE | NO | NO_EJECUTADAS / NO_EJECUTADAS | — |
| T-CAMBIOS | Claude runtime + Mistral D | PENDIENTE | PENDIENTE | NO | NO_EJECUTADAS / NO_EJECUTADAS | — |
| T-TRASPASO | Claude + receptor sin historial | ENTREGADO | CONFORME_CON_LIMITES | NO | EJECUTADAS / PARCIALES | 788f25c |
| H-DEC | Usuario | PENDIENTE | PENDIENTE | NO | NO_EJECUTADAS / NO_EJECUTADAS | — |
| F1-IMPL | Claude | PENDIENTE | PENDIENTE | NO | NO_EJECUTADAS / NO_EJECUTADAS | — |
| CIERRE | Claude + usuario | PENDIENTE | PENDIENTE | NO | NO_EJECUTADAS / NO_EJECUTADAS | — |

## Próxima acción y dependencias por tarea

- **F1-W · F1 W1–W3 entregada y contrastada por Mistral C/F; propuesta no adoptada**: Nada en esta tarea. La implementación de W1 en el producto depende de las decisiones (1a)–(5b) (F1-IMPL, H-DEC); no se integra en la candidata porque no es software del producto.
- **C20 · C20: U1–U6 del verificador respondidas; contraste pendiente**: Nada en esta tarea. No es software del producto: no se integra en la candidata; queda en la rama F1.
- **CSV · Cifras [LECTURA] al CSV verificado (bloque CSV de ENCARGO_C20_CSV.md, f5775dc)**: Nada en esta tarea. No es software del producto: no se integra en la candidata; queda en la rama F1.
  Dependencias: C20.
- **A-CTX · Evidencia contextual A v3**: Mistral A: primero la revisión de G-RAIZ (3d66437); después A4-R1…R6 (CORRECCION_A4.md) en la rama A. T-EXP sigue bloqueado por A-CTX.
- **D-HARNESS · Arnés D v2 y paquetes íntegros**: D3 sigue vigente (d032691 es anterior a CORRECCION_D3). Tras d032691: R6 cerrado, la regeneración cerrada y el MAPA publicado; R1–R5 y R8 abiertos, con 7 variantes nuevas (ESTADO_D3_TRAS_d032691.md). Mistral D responde a D3 sobre d032691.
- **D-36 · Aceptación completa de 36 casos Qwen**: 0/36 casos del personaje (correcto). No se ejecutan con un arnés sin aceptar; el runtime del coordinador los ejecutará cuando D3-R1…R4 estén cerrados.
  Dependencias: D-HARNESS, T-CAND.
  Bloqueo/límite: No falta capacidad: el personaje se ejecuta con código 10 y subagentes de la sesión orquestadora (modelo y esfuerzo de config_v2.json, fase C con el mismo agente, auditoría con agente nuevo; sin API). Comprobado en 957af65: réplica hasta el código 10, paso 5. Bloqueo real: la adaptación de los 36 casos sintéticos a vías soportadas y la correspondencia criterio→observable (D2-R4/R5, Mistral D), que exige el propio PLAN_DE_EJECUCION del banco.
- **E-ELIS · Fuentes M1/M2/M6/N2 de Elis**: Mistral E corrige E2-D1…D9 (CORRECCION_E2.md) y actualiza el estado de preservación a la Release. M1/M2/M6/N2 ABIERTOS; Elis pendiente_de_datos.
- **B-PM1 · Dossier P-M1 corregido; contraste documental pendiente**: Dato de las nueve altas aceptado con límites (revisión del coordinador sobre daa7478 y contraste 223f16d). P-M1 sigue bloqueado: no se identifica θ/λ ni se adopta política. Nada que integrar en el producto sin decisión.
  Bloqueo/límite: P-M1 no delimitada con evidencia disponible; 4 PDF nuevos con preservación pendiente.
- **C-C2 · Guarda de perímetros C2**: Decisión del integrador: no se incorpora a la candidata. Es herramienta de contraste del auxiliar, no software del producto, y conserva C1 y D1/D7/D11 pendientes. Se conserva el enlace (1ec4f18, SEGUIMIENTO.md @ b049777); se usa como oráculo de contraste solo dentro de su alcance.
- **F-REV · Contraste independiente de cambios Claude**: Siguiente contraste de Mistral C/F sobre entregas de Claude: G-MANUAL (solicitud LISTA), además de responder a CORRECCION_F2.
- **F-B3 · Tercer B real fuera de muestra**: Inventario reproducible aceptado con límites (F2-D1 cerrado; 71 PDF con huella). Mistral C/F corrige F3-R3 (.bat de Ahold), R4 y textos. La ejecución depende de U2 (etapa 1 de Ahold).
  Bloqueo/límite: Historia irrecuperable de la persona responsable: Ahold_evaluada.xlsx (V5.3) y Ahold_respuesta.md de la etapa 1 (sin ellos el pipeline se detiene en el paso 1 y la r heredada C56 no puede reconstruirse sin elegirla); huellas de sus PDF 2019–2025 (HUELLAS.txt del .bat); y si el resultado de la etapa 1 influyó en elegir a Ahold como reserva.
- **F-C1 · Primer recorrido C real y contrato específico**: Contrato C de F con un defecto medio (F3-R5: el motor se elige en Análisis!C62, comprobado en build_v6.py). Se alinea con el de u3_motor_c o se retira (F3-R12). La elección de candidato es de la persona responsable sobre U3.
  Bloqueo/límite: Documentos oficiales de los candidatos sin verificar: descarga de FinecoBank denegada por el control de permisos de la sesión; Hannover Re responde 403 a curl. Hace falta que la persona responsable autorice esas descargas o deje ella los documentos (informe anual 2025 y Pilar 3 o SFCR 2025 de cada candidato).
- **G-MANUAL · Manual, instalación y recuperación desde contexto limpio**: Manual aceptado con límites (78ba1ca) y probado en T-TRASPASO. Pendiente: aplicar MEJORAS_MANUAL.md (disco y _v64, pasos 12–14 y H9, resultado esperado de los controles históricos sobre 4.15, flock, registro del receptor, comandos que faltan) con revisión de un contexto distinto.
  Dependencias: T-CAND.
- **G-DOCS · Corrección documental de la guía del recorrido y de CONTINUIDAD en una rama aislada de la candidata (sin cambios de código)**: Integrado en la candidata (3149128). Nada más en esta tarea.
  Dependencias: G-MANUAL.
- **G-RAIZ · U4: hechos desfasados de README, CLAUDE.md y docs/MIGRATION_STATUS.json de la raíz, en una rama aislada (instrucciones sustantivas conservadas)**: Revisión independiente (solicitud LISTA). Si es conforme, se incorpora a la candidata con origen, revisión y destino.
- **T-CAND · Candidata única de integración técnica**: Candidata con su primera integración (G-DOCS, 3149128): solo documentos; manifiesto 7762/7762. La verificación completa de 957af65 sigue valiendo para el código, que no ha cambiado; ninguna batería lee esos documentos. Integrar lo siguiente aceptado por archivo, con origen, revisión, destino y pruebas afectadas.
- **T-EXP · Expedientes nuevos regenerados y auditados**: Regenerar entradas/fuentes/derivados, sin sustituir hipótesis o ausencias; auditoría del material nuevo.
  Dependencias: T-CAND, A-CTX.
- **T-CAMBIOS · Vigencia, invalidación, recuperación y H9**: Ensayar cambio anterior y punto real de reanudación; no reintroducir límites I19/I20 ya corregidos.
  Dependencias: T-CAND, D-HARNESS.
- **T-TRASPASO · Traspaso sin historial y revisión de manual**: Aceptado con límites (sin pasos de agentes; el registro no guarda transcripción ni la mayoría de códigos; receptor de la misma familia de modelo). Pasos con agentes reales: runtime del coordinador. Mejoras del manual en MEJORAS_MANUAL.md (G-MANUAL).
  Dependencias: T-CAND, G-MANUAL.
- **H-DEC · Decisiones económicas pendientes con fundamento**: Decisiones económicas F1 (1a)–(5b), E8.1 y umbral de V-F1a presentadas una por una (03e7851) a la persona responsable. Nada adoptado. F1-IMPL espera esas decisiones.
  Dependencias: F1-W.
  Bloqueo/límite: No hay adopción de políticas económicas nuevas en este programa.
- **F1-IMPL · Implementación económica F1 autorizada**: Puede preparar parche propuesto separado; no activar cambios económicos antes de decisión explícita.
  Dependencias: F1-W, H-DEC, T-CAND.
  Bloqueo/límite: Datos/políticas económicos pendientes; Elis sigue pendiente_de_datos.
- **CIERRE · Entrega final por alcance declarado**: Evaluar criterios de cierre, no porcentaje; no reducir alcance original por inferencia.
  Dependencias: D-36, T-EXP, T-CAMBIOS, T-TRASPASO, F-B3, F-C1, H-DEC, B-PM1, C20, CSV, A-CTX, F1-IMPL.

## Solicitudes de revisión

- F1-W: RESPONDIDA; revisor asignado: Mistral C/F; SHA: d519eb04978e64d04f1d1795c570ca96bdd7ad7f.
- C20: RESPONDIDA; revisor asignado: Mistral C/F; SHA: bf0d5c25d136ae9b2b1f14e4688081e1792d2363.
- CSV: RESPONDIDA; revisor asignado: Mistral C/F; SHA: 77ff89f8fe99a1b5f013243ea1ccd4b84512ac51.
- A-CTX: RESPONDIDA; revisor asignado: Claude coordinador (subagente de revisión); SHA: 0946971e1e4cf10cb85ed4c757968a4bd060d6a7.
- E-ELIS: RESPONDIDA; revisor asignado: Claude coordinador (subagente de revisión); SHA: f00c5dd64cb956b93ebb199389ce748e9d218f6c.
- G-MANUAL: RESPONDIDA; revisor asignado: Mistral A, en rama propia mistral/g-manual-traspaso, carpeta resultados_cierre/manual_revision/ (reanudación c241a59); SHA: 341831fd8b4c9081c09f1ebe7b31799042402d0f.
- G-DOCS: RESPONDIDA; revisor asignado: Mistral A, en mistral/g-manual-traspaso (antes de A3), u otro contexto distinto; SHA: c0542b83b9923f98124d3c72e48b7fc7245284d2.
- G-RAIZ: LISTA; revisor asignado: Mistral A, en mistral/g-manual-traspaso (siguiente tras G-DOCS), u otro contexto distinto; SHA: 3d66437e797b6b0bf137b42fa62b561f39121722.

## Cómo se decide el cierre

PROGRAMA.md fija los criterios: candidata trazable; datos/derivados y decisiones vigentes; pruebas y recorrido real; alcance por motor; manual, recuperación y traspaso. No se calcula porcentaje global. Un bloqueo económico puede permitir continuar trabajo técnico sin convertir el expediente en apto.

Las pruebas antiguas solo se conservan cuando sus dependencias no cambian. Ninguna marca del plan de la interfaz sustituye la evidencia de un commit, prueba o revisión.
