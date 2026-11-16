# Estado único de Munger V2

Corte: 2026-11-16 ~21:05 Europe/Amsterdam; consulta remota del coordinador Claude (arranque).

Cierre en preparación: entregas parciales y revisiones pendientes; sin aptitud económica global acreditada.

**Fuente:** CONTROL.json. Este panel resume evidencia registrada; no observa sesiones privadas, no ejecuta agentes y no acredita por sí solo aptitud económica.

Candidata integrada: {'repositorio': 'jluisplagos/munger-v2', 'rama': 'integracion/candidata-cierre-v2', 'base': '957af652cdc3bef3d67e8623c9572138bac685e9', 'head': '957af652cdc3bef3d67e8623c9572138bac685e9', 'estado': 'Binarios materializados y manifiesto 7762/7762; verificación completa en curso; nada integrado'}. Mantenedor: Claude coordinador, único escritor.

| ID | Dueño | Entregado | Revisado | Integrado | Pruebas autor / externas | Origen |
|---|---|---|---|---|---|---|
| F1-W | Claude | ENTREGADO | CONFORME_CON_LIMITES | NO | EJECUTADAS / PARCIALES | d519eb0 |
| C20 | Claude | ENTREGADO | CONFORME_CON_LIMITES | NO | EJECUTADAS / PARCIALES | bf0d5c2 |
| CSV | Claude | ENTREGADO | CONFORME_CON_LIMITES | NO | EJECUTADAS / PARCIALES | 77ff89f |
| A-CTX | Mistral A | ENTREGADO | CORRECCIONES | NO | DECLARADAS / REPRODUCIDAS | 9d676ce |
| D-HARNESS | Mistral D | ENTREGADO | CORRECCIONES | NO | DECLARADAS / NO_EJECUTADAS | 1ac661b |
| D-36 | Mistral D + Claude runtime | PARCIAL | CORRECCIONES | NO | DECLARADAS / NO_EJECUTADAS | 1ac661b |
| E-ELIS | Antigua Mistral B, nueva E | ENTREGADO | CORRECCIONES | NO | DECLARADAS / PARCIALES | 93a9780 |
| B-PM1 | Mistral B (autor previo) | PARCIAL | CONFORME_CON_LIMITES | NO | DECLARADAS / REPRODUCIDAS | daa7478 |
| C-C2 | Mistral C (autor previo) | ENTREGADO | CONFORME_CON_LIMITES | NO | DECLARADAS / REPRODUCIDAS | 1ec4f18 |
| F-REV | Antigua Mistral C, nueva F | PENDIENTE | PENDIENTE | NO | NO_EJECUTADAS / NO_EJECUTADAS | — |
| F-B3 | Mistral C/F prepara; Claude orquesta | PARCIAL | CORRECCIONES | NO | DECLARADAS / NO_EJECUTADAS | 52fb120 |
| F-C1 | Mistral C/F prepara; Claude orquesta | PARCIAL | CORRECCIONES | NO | DECLARADAS / NO_EJECUTADAS | 52fb120 |
| G-MANUAL | Mistral A cuando termine bloqueA (cola G) | PENDIENTE | PENDIENTE | NO | NO_EJECUTADAS / NO_EJECUTADAS | — |
| T-CAND | Claude coordinador | PARCIAL | PENDIENTE | NO | NO_EJECUTADAS / NO_EJECUTADAS | 957af65 |
| T-EXP | Claude runtime + extractores/revisores reales | PENDIENTE | PENDIENTE | NO | NO_EJECUTADAS / NO_EJECUTADAS | — |
| T-CAMBIOS | Claude runtime + Mistral D | PENDIENTE | PENDIENTE | NO | NO_EJECUTADAS / NO_EJECUTADAS | — |
| T-TRASPASO | Claude + receptor sin historial | PENDIENTE | PENDIENTE | NO | NO_EJECUTADAS / NO_EJECUTADAS | — |
| H-DEC | Usuario | PENDIENTE | PENDIENTE | NO | NO_EJECUTADAS / NO_EJECUTADAS | — |
| F1-IMPL | Claude | PENDIENTE | PENDIENTE | NO | NO_EJECUTADAS / NO_EJECUTADAS | — |
| CIERRE | Claude + usuario | PENDIENTE | PENDIENTE | NO | NO_EJECUTADAS / NO_EJECUTADAS | — |

## Próxima acción y dependencias por tarea

- **F1-W · F1 W1–W3 entregada y contrastada por Mistral C/F; propuesta no adoptada**: Nada en esta tarea. La implementación de W1 en el producto depende de las decisiones (1a)–(5b) (F1-IMPL, H-DEC); no se integra en la candidata porque no es software del producto.
- **C20 · C20: U1–U6 del verificador respondidas; contraste pendiente**: Nada en esta tarea. No es software del producto: no se integra en la candidata; queda en la rama F1.
- **CSV · Cifras [LECTURA] al CSV verificado (bloque CSV de ENCARGO_C20_CSV.md, f5775dc)**: Nada en esta tarea. No es software del producto: no se integra en la candidata; queda en la rama F1.
  Dependencias: C20.
- **A-CTX · Evidencia contextual A v3**: Mistral A responde a CORRECCION_A2.md (A2-R1…R5) sobre 160faf9; las entradas REVISADO acreditadas con las reglas defectuosas deben regenerarse. El coordinador revisa solo lo afectado cuando haya respuesta.
- **D-HARNESS · Arnés D v2 y paquetes íntegros**: Mistral D corrige D2-R1…R7 (CORRECCION_D2.md): aserciones que aceptan resultados vacíos o forjados, Q1-026 incoherente con el banco, relevos vacíos de Q1-028/032, correspondencia de criterios, manifiesto. Se conserva D-R2 y la detección de las sondas de d375d80.
- **D-36 · Aceptación completa de 36 casos Qwen**: Ningún caso del personaje ejecutado (0/36). Recuento del revisor: 29 componentes con precondiciones del arnés, 1 bloqueo de entorno (Q1-026), 2 observación compartida, 2 pendientes de agente, 2 de decisión del usuario. El runtime del coordinador ejecuta el personaje cuando D2-R4 dé relevos completos.
  Dependencias: D-HARNESS, T-CAND.
  Bloqueo/límite: Parte del entorno Mistral no expone agentes/pdftotext/soffice según su declaración; transferir al runtime comprobado.
- **E-ELIS · Fuentes M1/M2/M6/N2 de Elis**: Mistral E corrige E-R1…E-R9 (CORRECCION_E1.md). Tras la corrección, N2 y M6 quedan ABIERTOS; M1 y M2, ABIERTOS. Elis sigue pendiente_de_datos. El almacén duradero de los 11 PDF lo decide el usuario.
  Bloqueo/límite: Los 11 PDF nuevos están en PROVISIONAL, solo en el sandbox del autor (subida a la Release con HTTP 401); sin copia duradera accesible. El acceso del coordinador a fr.elis.com no se usa: el programa prohíbe contactar con terceros.
- **B-PM1 · Dossier P-M1 corregido; contraste documental pendiente**: Dato de las nueve altas aceptado con límites (revisión del coordinador sobre daa7478 y contraste 223f16d). P-M1 sigue bloqueado: no se identifica θ/λ ni se adopta política. Nada que integrar en el producto sin decisión.
  Bloqueo/límite: P-M1 no delimitada con evidencia disponible; 4 PDF nuevos con preservación pendiente.
- **C-C2 · Guarda de perímetros C2**: Integrador registra uso/incorporación limitada; no otra ronda matemática por C2.
- **F-REV · Contraste independiente de cambios Claude**: Cuando exista nuevo SHA W/C20/CSV, fijar y revisar diff. Mientras tanto B-PM1/F-B3/F-C1.
- **F-B3 · Tercer B real fuera de muestra**: Mistral C/F corrige F2-D1, D2 y D4–D7. Bloqueo real: el Excel de la etapa 1 de Ahold y sus fuentes, u otra empresa fuera de muestra designada por la persona responsable.
  Bloqueo/límite: Datos de la persona responsable: el Excel evaluado de la etapa 1 de Ahold con su respuesta y sus fuentes, u otra empresa fuera de muestra designada (la lista de las 116 no está conservada).
- **F-C1 · Primer recorrido C real y contrato específico**: Mistral C/F corrige F2-D3 (contrato C frente al motor real) y F2-D1/D2/D5/D6. Bloqueo real: un banco o aseguradora designados y sus informes oficiales.
  Bloqueo/límite: Datos de la persona responsable: un banco o aseguradora concretos, sus informes oficiales (cuentas, Pilar 3 o SFCR) con huellas y, si existe, el Excel de la etapa 1.
- **G-MANUAL · Manual, instalación y recuperación desde contexto limpio**: Preparación puede avanzar antes; prueba operativa depende de candidata y runtime comprobado.
  Dependencias: T-CAND.
- **T-CAND · Candidata única de integración técnica**: Binarios materializados en el worktree de la candidata (1008 copiados desde la base 4.14 verificada, ninguno sobrescrito); manifiesto propio 7762/7762, 0 ausentes, 0 de más. verificar_paquete.sh completa: primer intento interrumpido por reinicio del contenedor (todo PASA hasta test_integracion_v64.py); segundo intento en curso sobre copia nueva, con flock. Después, integrar solo lo aceptado.
- **T-EXP · Expedientes nuevos regenerados y auditados**: Regenerar entradas/fuentes/derivados, sin sustituir hipótesis o ausencias; auditoría del material nuevo.
  Dependencias: T-CAND, A-CTX.
- **T-CAMBIOS · Vigencia, invalidación, recuperación y H9**: Ensayar cambio anterior y punto real de reanudación; no reintroducir límites I19/I20 ya corregidos.
  Dependencias: T-CAND, D-HARNESS.
- **T-TRASPASO · Traspaso sin historial y revisión de manual**: Reproducir desde documentación y fuente fijadas; registrar lo no ejecutable.
  Dependencias: T-CAND, G-MANUAL.
- **H-DEC · Decisiones económicas pendientes con fundamento**: Presentar solo opciones nuevas/reales; aprobación no suple M1/M2/M6/N2 ni P-M1.
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
- E-ELIS: RESPONDIDA; revisor asignado: Claude coordinador (subagente de revisión); SHA: 93a97801f8c4f6a4dc5cabd4540248390cf113d0.

## Cómo se decide el cierre

PROGRAMA.md fija los criterios: candidata trazable; datos/derivados y decisiones vigentes; pruebas y recorrido real; alcance por motor; manual, recuperación y traspaso. No se calcula porcentaje global. Un bloqueo económico puede permitir continuar trabajo técnico sin convertir el expediente en apto.

Las pruebas antiguas solo se conservan cuando sus dependencias no cambian. Ninguna marca del plan de la interfaz sustituye la evidencia de un commit, prueba o revisión.
