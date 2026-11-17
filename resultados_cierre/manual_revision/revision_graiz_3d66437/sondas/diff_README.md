--- /tmp/graiz_s02.stVK4d/base_README.md	2026-11-17 13:10:35.951697266 +0000
+++ /tmp/graiz_s02.stVK4d/head_README.md	2026-11-17 13:10:36.586697170 +0000
@@ -1,10 +1,10 @@
-# Rama de revisión: 4.15, hito 1
+# Candidata de integración: 4.15, hito 2
 
-Entrega intermedia recibida de Claude, con una revisión externa en curso. No fusionada con main. El hito no contiene el cierre económico F1 ni los expedientes regenerados. Hay un contraejemplo nuevo del control de signos; consultar docs/revision_externa_4_15_hito1/.
+Rama `integracion/candidata-cierre-v2`, creada desde 957af65 (entrega 4.15 · hito 2, corrección técnica tras la revisión externa del hito 1; `munger_v2_r1/VERSION`). No fusionada con main. No contiene el cierre económico F1 ni los expedientes regenerados. La revisión externa del hito 1 está en docs/revision_externa_4_15_hito1/ y el registro del hito 2 en `munger_v2_r1/personaje_v2/empresas_v2_correcciones/2026-11_Vidrala_ensayo_4_15/hito2/HITO_2_4_15.md`.
 
 La base 4.14 completa sigue conservada en main y en su Release. Para ejecutar este hito: clonar main, recuperar y verificar sus binarios con tools/base_414.py y después cambiar a esta rama. La verificación de la 4.14 no debe aplicarse al código modificado de la 4.15; usar el MANIFIESTO_SHA256.txt de esta rama para contrastar su árbol.
 
-El trabajo actual de Claude continúa aparte. Esta rama conserva exactamente el código recibido, sin incorporar correcciones propias al producto.
+Esta rama conserva el código recibido del hito 2. Solo se incorporan en ella archivos revisados por un contexto distinto del autor, con su origen, revisión y destino registrados en el control del programa de cierre (`jluisplagos/munger-v2-evidencias-mistral`, rama `coordinacion/cierre-v2`).
 
 ---
 
@@ -14,7 +14,7 @@
 
 Repositorio público por indicación de la persona responsable: https://github.com/jluisplagos/munger-v2
 
-Las correcciones que Claude está preparando no están incorporadas todavía. Su trabajo debe continuar sin interrupción. La 4.14 mantiene su condición experimental supervisada y las incidencias documentadas en la revisión externa. Esta migración comprueba conservación de bytes, no aptitud financiera.
+Las correcciones de los hitos 1 y 2 de la 4.15 están en la candidata; main conserva la 4.14 sin cambios. El trabajo en otras sesiones debe continuar sin interrupción. La 4.14 mantiene su condición experimental supervisada y las incidencias documentadas en la revisión externa. Esta migración comprueba conservación de bytes, no aptitud financiera.
 
 ## Estructura
 
