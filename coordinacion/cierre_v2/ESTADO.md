# Estado único de Munger V2

Corte: 2026-11-16; consulta remota al preparar este programa.

Cierre en preparación: entregas parciales y revisiones pendientes; sin aptitud económica global acreditada.

**Fuente:** CONTROL.json. Este panel resume evidencia registrada; no observa sesiones privadas, no ejecuta agentes y no acredita por sí solo aptitud económica.

Candidata integrada: todavía no registrada. Mantenedor: Claude coordinador, único escritor.

| ID | Dueño | Entregado | Revisado | Integrado | Pruebas autor / externas | Origen |
|---|---|---|---|---|---|---|
| F1-W | Claude | PARCIAL | CORRECCIONES | NO | DECLARADAS / REPRODUCIDAS | 716cbd6 |
| C20 | Claude | PENDIENTE | PENDIENTE | NO | NO_EJECUTADAS / NO_EJECUTADAS | — |
| CSV | Claude | PENDIENTE | PENDIENTE | NO | NO_EJECUTADAS / NO_EJECUTADAS | — |
| A-CTX | Mistral A | ENTREGADO | PENDIENTE | NO | DECLARADAS / NO_EJECUTADAS | d2419e5 |
| D-HARNESS | Mistral D | ENTREGADO | PENDIENTE | NO | DECLARADAS / NO_EJECUTADAS | bdcbba7 |
| D-36 | Mistral D + Claude runtime | PARCIAL | PENDIENTE | NO | DECLARADAS / NO_EJECUTADAS | bdcbba7 |
| E-ELIS | Antigua Mistral B, nueva E | PENDIENTE | PENDIENTE | NO | NO_EJECUTADAS / NO_EJECUTADAS | — |
| B-PM1 | Mistral B (autor previo) | PARCIAL | LIMITADA | NO | DECLARADAS / REPRODUCIDAS | daa7478 |
| C-C2 | Mistral C (autor previo) | ENTREGADO | CONFORME_CON_LIMITES | NO | DECLARADAS / REPRODUCIDAS | 1ec4f18 |
| F-REV | Antigua Mistral C, nueva F | PENDIENTE | PENDIENTE | NO | NO_EJECUTADAS / NO_EJECUTADAS | — |
| F-B3 | Mistral C/F prepara; Claude orquesta | PENDIENTE | PENDIENTE | NO | NO_EJECUTADAS / NO_EJECUTADAS | — |
| F-C1 | Mistral C/F prepara; Claude orquesta | PENDIENTE | PENDIENTE | NO | NO_EJECUTADAS / NO_EJECUTADAS | — |
| G-MANUAL | Mistral A cuando termine bloqueA (cola G) | PENDIENTE | PENDIENTE | NO | NO_EJECUTADAS / NO_EJECUTADAS | — |
| T-CAND | Claude coordinador | PENDIENTE | PENDIENTE | NO | NO_EJECUTADAS / NO_EJECUTADAS | — |
| T-EXP | Claude runtime + extractores/revisores reales | PENDIENTE | PENDIENTE | NO | NO_EJECUTADAS / NO_EJECUTADAS | — |
| T-CAMBIOS | Claude runtime + Mistral D | PENDIENTE | PENDIENTE | NO | NO_EJECUTADAS / NO_EJECUTADAS | — |
| T-TRASPASO | Claude + receptor sin historial | PENDIENTE | PENDIENTE | NO | NO_EJECUTADAS / NO_EJECUTADAS | — |
| H-DEC | Usuario | PENDIENTE | PENDIENTE | NO | NO_EJECUTADAS / NO_EJECUTADAS | — |
| F1-IMPL | Claude | PENDIENTE | PENDIENTE | NO | NO_EJECUTADAS / NO_EJECUTADAS | — |
| CIERRE | Claude + usuario | PENDIENTE | PENDIENTE | NO | NO_EJECUTADAS / NO_EJECUTADAS | — |

## Próxima acción y dependencias por tarea

- **F1-W · F1 v3 entregada; corrección W1-W3 pendiente**: Corregir horizonte temporal posterior al año10, signo/G8 y dominio A0; conservar lo conforme.
- **C20 · Responder U1-U6 del verificador**: Leer plan C20 en b83803c y revisión9; corregir solo lo afectado.
- **CSV · Acreditar cifras LECTURA por procedimiento CSV**: Fijar verificador/CSV y acreditar filas nuevas con fuentes y edición; no aplicar N1.
  Dependencias: C20.
- **A-CTX · Evidencia contextual A v3**: Revisar diff v3 y reproducir; comprobar importe20xx frente a metadato de año.
- **D-HARNESS · Arnés D v2 y paquetes íntegros**: Revisar aserciones/artefactos/recuentos; cerrar Q1-027 y paquete Q1-026 referenciado.
- **D-36 · Aceptación completa de 36 casos Qwen**: Separar criterios propios/compartidos, componentes y recorrido real; no hay 36 casos completos acreditados.
  Dependencias: D-HARNESS, T-CAND.
  Bloqueo/límite: Parte del entorno Mistral no expone agentes/pdftotext/soffice según su declaración; transferir al runtime comprobado.
- **E-ELIS · Fuentes M1/M2/M6/N2 de Elis**: Leer encargo nuevo; inventario de lo ya leído y búsqueda finita de fuentes oficiales.
- **B-PM1 · Dossier P-M1 corregido; contraste documental pendiente**: Contrastar nueve altas corregidas con notas/cabeceras; conservar no identificación de θ/λ.
  Bloqueo/límite: P-M1 no delimitada con evidencia disponible; 4 PDF nuevos con preservación pendiente.
- **C-C2 · Guarda de perímetros C2**: Integrador registra uso/incorporación limitada; no otra ronda matemática por C2.
- **F-REV · Contraste independiente de cambios Claude**: Cuando exista nuevo SHA W/C20/CSV, fijar y revisar diff. Mientras tanto B-PM1/F-B3/F-C1.
- **F-B3 · Tercer B real fuera de muestra**: Inventario existente, elegibilidad y selección previa a resultados; no forzar motor.
- **F-C1 · Primer recorrido C real y contrato específico**: Preparar banco/aseguradora con fuentes y contrato propuesto, no declarar validado por plantilla.
- **G-MANUAL · Manual, instalación y recuperación desde contexto limpio**: Preparación puede avanzar antes; prueba operativa depende de candidata y runtime comprobado.
  Dependencias: T-CAND.
- **T-CAND · Candidata única de integración técnica**: Crear integracion/candidata-cierre-v2 desde957af65 y fijar componentes; conservar main/históricos.
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

- F1-W: POR_PREPARAR; revisor asignado: Mistral C/F; SHA: aún sin nueva entrega fijada.
- C20: POR_PREPARAR; revisor asignado: Mistral C/F; SHA: aún sin nueva entrega fijada.
- CSV: POR_PREPARAR; revisor asignado: Mistral C/F; SHA: aún sin nueva entrega fijada.

## Cómo se decide el cierre

PROGRAMA.md fija los criterios: candidata trazable; datos/derivados y decisiones vigentes; pruebas y recorrido real; alcance por motor; manual, recuperación y traspaso. No se calcula porcentaje global. Un bloqueo económico puede permitir continuar trabajo técnico sin convertir el expediente en apto.

Las pruebas antiguas solo se conservan cuando sus dependencias no cambian. Ninguna marca del plan de la interfaz sustituye la evidencia de un commit, prueba o revisión.
