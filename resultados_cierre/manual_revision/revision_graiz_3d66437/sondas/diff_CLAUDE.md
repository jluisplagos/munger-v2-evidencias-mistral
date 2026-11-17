--- /tmp/graiz_s02.stVK4d/base_CLAUDE.md	2026-11-17 13:10:34.725697452 +0000
+++ /tmp/graiz_s02.stVK4d/head_CLAUDE.md	2026-11-17 13:10:35.316697363 +0000
@@ -1,4 +1,4 @@
-Esta es la rama de revisión intermedia 4.15 hito 1. El código contiene las correcciones técnicas de ese hito, sin cierre económico ni aprobación final. Leer docs/revision_externa_4_15_hito1/ y el encargo correctivo vigente. Mantener en main la base histórica 4.14. No sobrescribir el trabajo en curso de la sesión de Claude.
+Esta es la candidata de integración del programa de cierre: rama `integracion/candidata-cierre-v2`, entrega 4.15 · hito 2 (commit 957af65; `munger_v2_r1/VERSION`). El código contiene las correcciones técnicas de los hitos 1 y 2, sin cierre económico ni aprobación final. Leer docs/revision_externa_4_15_hito1/, el registro del hito 2 (`munger_v2_r1/personaje_v2/empresas_v2_correcciones/2026-11_Vidrala_ensayo_4_15/hito2/HITO_2_4_15.md`) y el encargo correctivo vigente. Mantener en main la base histórica 4.14. No sobrescribir el trabajo en curso de ninguna sesión de Claude.
 
 # Instrucciones de continuidad
 
@@ -7,8 +7,8 @@
 La base histórica está completa: 5790 archivos de texto en Git y los 1008 binarios dentro del ZIP original de la Release base-4.14. La descarga y los 6798 archivos del manifiesto se verificaron. Confirmar la materialización local con tools/base_414.py verify antes de ejecutar el pipeline.
 No declarar completa la migración ni iniciar el pipeline financiero por el mero hecho de poder leer este repositorio.
 
-La versión de referencia es 4.14, experimental supervisada; no apta para dinero real.
-La revisión externa parcial encontró:
+La base histórica de referencia es la 4.14 (main); esta candidata es la 4.15 · hito 2. Las dos son experimentales supervisadas; no aptas para dinero real.
+La revisión externa parcial de la 4.14 encontró (situación en esta candidata: 1–6 corregidos en los hitos 1 y 2 de la 4.15, con el límite H9 del relevo caducado todavía abierto; 7, F1, sigue abierto y pendiente de decisiones):
 1. página inexistente aceptada por verificacion_entradas;
 2. fuente local ausente aceptada si no lleva huella;
 3. redondeo aceptado como si fuera la cifra exacta;
@@ -17,7 +17,7 @@
 6. relevo caducado y aptitud por entradas omitida en salidas V6.3;
 7. F1: el modelo A requiere conciliación y validación propias.
 
-Los contraejemplos y la revisión externa están en docs/. Los 119 tests repetidos no cubren los tres huecos nuevos.
+Los contraejemplos y la revisión externa están en docs/. Los 119 tests repetidos de la 4.14 no cubrían los tres huecos nuevos; desde la 4.15 los cubre `test_verificacion_entradas_415.py` (190 pruebas en el hito 2).
 
 Mantener originales y decisiones humanas registradas. Trabajar en ramas y expedientes nuevos.
 No cambiar fuentes ni huellas para legitimar un resultado antiguo.
@@ -32,6 +32,6 @@
 
 El encargo correctivo vigente pegado por la persona responsable prevalece sobre propuestas antiguas de continuidad.
 
-No interrumpir el encargo que ya corre en otra sesión de Claude. Las correcciones aún en curso no se han importado. Esperar su entrega final y conservarla; después importar como nueva versión sobre una copia completa, nunca sobrescribirla con la base histórica.
+No interrumpir los encargos que corran en otras sesiones de Claude. La entrega del hito 2 de la 4.15 ya está importada en esta candidata (957af65). Las entregas posteriores se conservan y se importan igual: como nueva versión sobre una copia completa, nunca sobrescribiéndolas con la base histórica.
 
 Para recuperar los binarios históricos, leer la sección de archivos pesados del README. Para una nueva entrega, seguir docs/RECEPCION_ENTREGA_CLAUDE.md. Usar el ZIP original completo de la Release base-4.14; la alternativa de recuperación parcial quedó sustituida. Las herramientas de recuperación son exclusivas de la base histórica 4.14.
