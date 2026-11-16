# Estado único de Munger V2

Corte: 2026-11-16 ~21:05 Europe/Amsterdam; consulta remota del coordinador Claude (arranque).

Cierre en preparación: entregas parciales y revisiones pendientes; sin aptitud económica global acreditada.

**Fuente:** CONTROL.json. Este panel resume evidencia registrada; no observa sesiones privadas, no ejecuta agentes y no acredita por sí solo aptitud económica.

Candidata integrada: {'repositorio': 'jluisplagos/munger-v2', 'rama': 'integracion/candidata-cierre-v2', 'base': '957af652cdc3bef3d67e8623c9572138bac685e9', 'head': '957af652cdc3bef3d67e8623c9572138bac685e9', 'estado': 'Creada y publicada sin cambios sobre la base técnica; binarios aún no materializados en su worktree; nada integrado'}. Mantenedor: Claude coordinador, único escritor.

| ID | Dueño | Entregado | Revisado | Integrado | Pruebas autor / externas | Origen |
|---|---|---|---|---|---|---|
| F1-W | Claude | ENTREGADO | CONFORME_CON_LIMITES | NO | EJECUTADAS / PARCIALES | d519eb0 |
| C20 | Claude | ENTREGADO | PENDIENTE | NO | EJECUTADAS / NO_EJECUTADAS | bf0d5c2 |
| CSV | Claude | ENTREGADO | PENDIENTE | NO | EJECUTADAS / NO_EJECUTADAS | 77ff89f |
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
| T-CAND | Claude coordinador | PARCIAL | PENDIENTE | NO | NO_EJECUTADAS / NO_EJECUTADAS | 957af65 |
| T-EXP | Claude runtime + extractores/revisores reales | PENDIENTE | PENDIENTE | NO | NO_EJECUTADAS / NO_EJECUTADAS | — |
| T-CAMBIOS | Claude runtime + Mistral D | PENDIENTE | PENDIENTE | NO | NO_EJECUTADAS / NO_EJECUTADAS | — |
| T-TRASPASO | Claude + receptor sin historial | PENDIENTE | PENDIENTE | NO | NO_EJECUTADAS / NO_EJECUTADAS | — |
| H-DEC | Usuario | PENDIENTE | PENDIENTE | NO | NO_EJECUTADAS / NO_EJECUTADAS | — |
| F1-IMPL | Claude | PENDIENTE | PENDIENTE | NO | NO_EJECUTADAS / NO_EJECUTADAS | — |
| CIERRE | Claude + usuario | PENDIENTE | PENDIENTE | NO | NO_EJECUTADAS / NO_EJECUTADAS | — |

## Próxima acción y dependencias por tarea

- **F1-W · F1 W1–W3 entregada y contrastada por Mistral C/F; propuesta no adoptada**: Nada en esta tarea. La implementación de W1 en el producto depende de las decisiones (1a)–(5b) (F1-IMPL, H-DEC); no se integra en la candidata porque no es software del producto.
- **C20 · C20: U1–U6 del verificador respondidas; contraste pendiente**: Mistral C/F contrasta solo lo afectado (solicitud LISTA); el coordinador sigue con CSV.
- **CSV · Cifras [LECTURA] al CSV verificado (bloque CSV de ENCARGO_C20_CSV.md, f5775dc)**: Mistral C/F contrasta solo lo afectado por el bloque CSV (solicitud LISTA). Seis columnas por sociedad (Lavartex y «otras adquisiciones») siguen [LECTURA] con motivo; N1 no se aplica.
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
- **T-CAND · Candidata única de integración técnica**: Materializar binarios en el worktree de la candidata por el procedimiento del producto (sin sobrescribir código 4.15) y verificar su manifiesto; después incorporar solo lo aceptado.
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
- C20: LISTA; revisor asignado: Mistral C/F; SHA: bf0d5c25d136ae9b2b1f14e4688081e1792d2363.
- CSV: LISTA; revisor asignado: Mistral C/F; SHA: 77ff89f8fe99a1b5f013243ea1ccd4b84512ac51.

## Cómo se decide el cierre

PROGRAMA.md fija los criterios: candidata trazable; datos/derivados y decisiones vigentes; pruebas y recorrido real; alcance por motor; manual, recuperación y traspaso. No se calcula porcentaje global. Un bloqueo económico puede permitir continuar trabajo técnico sin convertir el expediente en apto.

Las pruebas antiguas solo se conservan cuando sus dependencias no cambian. Ninguna marca del plan de la interfaz sustituye la evidencia de un commit, prueba o revisión.
