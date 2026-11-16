# Hallazgos del frente D · v2 (tras CORRECCION_D D-R1–R5)

## Defectos del producto reproducidos

Ninguno. En los 27 casos con componente real ejecutado y aserciones (harness 2.0), el
producto se comportó conforme al contrato del banco en el componente probado. La revisión
externa (REVISION_A_D.md apartado D) no encontró defectos nuevos del producto tampoco.

## Hallazgos del arnés corregidos (D-R1–R5) — con la corrección aplicada y probada

- **D-R1 (material):** el arnés v1 daba exit 0 y "OK" con la candidata vacía (los 5 comandos
  salían 2) y la matriz copiaba CUMPLE de adaptaciones.json sin evidencia. Corregido: exits
  esperados por paso, aserciones por criterio, propagación de errores al exit global, matriz
  derivada solo de `resultado_ejecucion.json` validados. Prueba: candidata incompleta →
  rc=2, ERROR_ENTORNO (pruebas_arnes.log #3); evidencias ausentes → 0 CUMPLE (#5); resultado
  mutado → aserción FALLA (#6).
- **D-R2 (material):** se podía copiar un artefacto heredado byte a byte tras un fallo de
  generación (ficha/informe exit 2 con plantilla ausente). Corregido: salidas heredadas
  archivadas en `_heredados/` antes de ejecutar y `copiar_artefacto` exige exit esperado del
  productor + huella distinta. Prueba #4: con plantilla ausente en candidata aislada, ficha
  sale 2 (inesperado), el caso queda ERROR y el artefacto NO se copia. Los binarios oficiales
  no se tocaron.
- **D-R3 (material):** recuentos desde fuente única (`evidencias/recuentos.json` == CSV).
  27 ejecuciones propias (28 especificaciones; Q1-026 sin spec ejecutable por el bloqueo de
  entorno). Q1-028/Q1-032 declaran observación compartida con Q1-036 y no se cuentan como
  propias. Q1-032/Q1-036: 1/321 no prueba 4/1/5 ni 3/2/5 → no observable aquí, en relevo.
  Q1-035 coherente entre matriz y recuentos (DECISION_PENDIENTE en ambos). Naturaleza
  conservada desde el banco: 31 contrato / 3 propuestas / 2 decisiones pendientes.
- **D-R4 (material):** los registros de extractor/revisor preescritos por el arnés son
  precondiciones SIMULADAS de test de componentes; cada resultado lo declara
  (`precondiciones_simuladas`). No se cuentan como revisión independiente ejecutada; los
  criterios que la exigen quedan pendientes para el relevo (no se inventan firmas).
- **D-R5 (menor):** dos `.pyc` excluidos del árbol y del manifiesto (`.gitignore`);
  SHA de candidata y banco verificados en ejecución (`verificar_entorno`, preparar_entorno.sh);
  BANCO_DIR documentado al nivel `banco_revisado` en preparador y ejecutor.
- **Q1-034:** ejecutado como CONTRATO_REFERENCIADO (naturaleza del banco intacta): el rango
  0–200 queda preservado como hipótesis acotada y el punto medio inventado (100) como dato
  sin fuente se rechaza (evidencias/Q1-034). No se adoptó política; la valoración puntual apta
  y el tratamiento de sensibilidad quedan en relevo/política.

## Bloqueos de entorno (error concreto; no defectos del producto)

- Sin `soffice` (sin root): pipeline con recálculo no corre. Sin `pdftotext`: Q1-026 —
  `cambiar_base.py preparar` exit 1: "«archivo» ausente o inexistente en texto/:
  'AR_2021.txt'…'AR_2024.txt'" (son PDF). CAMBIO de relevo en `evidencias/Q1-026/`.
  Se comprobó que nunca sobrescribe el origen ("ya existe … no se sobrescribe", exit 1).

## Decisiones pendientes (responsable de política; no decididas aquí)

Q1-030 (caducidad temporal), Q1-035 (validación de motores). Q1-034 conserva contrato; su
parte de política va separada.

## No afirmado

27 CUMPLE son de **componente** (mecánico, con aserciones). Ningún caso completo de personaje
está acreditado (capa de agente sin runtime aquí): el veredicto de caso queda pendiente en los
27 ejecutados. Pasar controles de software no acredita aptitud económica ni para dinero real.
