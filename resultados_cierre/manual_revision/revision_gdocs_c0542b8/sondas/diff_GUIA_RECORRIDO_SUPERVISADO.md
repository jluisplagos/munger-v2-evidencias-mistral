--- material/base/munger_v2_r1_personaje_v2_GUIA_RECORRIDO_SUPERVISADO.md	2026-11-17 09:21:38.805715234 +0000
+++ material/head/munger_v2_r1_personaje_v2_GUIA_RECORRIDO_SUPERVISADO.md	2026-11-17 09:21:39.459715138 +0000
@@ -1,4 +1,6 @@
-# Guía breve del recorrido supervisado · plantillas V6.4 y V6.4.1 experimentales (motor B) · entregas 4.13 y 4.14
+# Guía breve del recorrido supervisado · plantillas V6.4 y V6.4.1 experimentales (motor B) · entregas 4.13 y 4.14, puesta al día para la 4.15 · hito 2
+
+> **Puesta al día para la 4.15 · hito 2 (programa de cierre v2).** Se corrigen los textos que dejaron de ser ciertos con los hitos 1 y 2: arranque desde el repositorio, registro de las entradas (R1–R3, I8/I9, I13, signo publicado), entrada efectiva en modo «estricta», aptitud por entradas también en la V6.3 (I20) y relevo caducado (I19). **Sigue abierto H9:** el relevo caducado vuelve siempre al paso 12. No cambia ninguna regla económica ni ninguna configuración.
 
 **Para qué sirve.** Explica cómo se recorre un expediente con agentes reales bajo la supervisión de la persona responsable, qué se mira en cada relevo y cómo se lee el resultado. Un recorrido así produce un **análisis experimental**: no es una decisión de inversión, no aprueba ningún parámetro y no sustituye a la evaluación de aptitud del informe de la entrega (`…/2026-11_Vidrala_ensayo_4_13/INFORME_INTEGRACION_4_13.md`, apartado de aptitud de uso).
 
@@ -11,7 +13,12 @@
 
 ## 1. Antes de empezar
 
-1. Comprobar el paquete en una descompresión limpia: `bash verificar_paquete.sh completa` (≈ 25–45 min, 36 en la prueba de traspaso de la 4.14; tiene que dar PASA). Espacio en disco: CONTINUIDAD §2, punto 5.
+1. Comprobar el árbol en una copia limpia. Desde la 4.15 no hay un ZIP completo:
+   - se clona `main` y se recuperan y verifican los binarios de la base 4.14 con `tools/base_414.py`, solo sobre la base 4.14 (README de la raíz, sección de archivos pesados);
+   - se pasa a la rama 4.15 y su árbol se contrasta con su propio `munger_v2_r1/MANIFIESTO_SHA256.txt`; nunca con las herramientas de la 4.14 (`PROMPT_NUEVA_VENTANA.md`);
+   - en una copia de ese árbol, `bash verificar_paquete.sh completa`, que tiene que dar PASA: ≈ 25–45 min en la 4.14 y 60 min en la verificación de la candidata 4.15 · hito 2.
+
+   Espacio en disco: CONTINUIDAD §2, punto 5.
 2. Una sola tarea con LibreOffice a la vez: el pipeline, las baterías y los controles que recalculan van siempre en secuencia. `comprobar_entorno.sh`, que el pipeline ejecuta al empezar, también llama a LibreOffice. Las lecturas sin recálculo pueden ir en paralelo.
 3. No se modifica nada de `personaje_v2/empresas_v2/` ni de los expedientes de entregas anteriores: se trabaja en un expediente nuevo.
 
@@ -41,6 +48,7 @@
 | 3 | límite del modelo (motor fuera de la cobertura, financiera, otro método) | es un resultado legítimo; se documenta |
 | 5 | retirada de una aprobación pendiente de registrar | volver a ejecutar cuando el resumen sea escribible |
 | 6 | estado del pipeline o registro de auditorías ilegible | restaurar desde una copia o relanzar con `--reiniciar`; nunca se sigue como aprobado |
+| 0, terminado en el paso 2 | (4.15) entrada efectiva: `entrada_efectiva.json` ilegible o con errata (`no_entregable`), o relleno en modo «estricta» detenido (`rellenar_fase1_v63.py --estricta`, código 7: `pendiente_de_datos`) | leer `diagnostico.md`; completar la entrada efectiva con su cálculo o corregir el archivo, sin rebajar el modo (`…_4_15/HITO_1_4_15.md`, C48; `…_4_15/hito2/HITO_2_4_15.md`, U6) |
 
 **Cada relevo** se resuelve con un agente real:
 - el prompt generado (`prompts_generados/NN_<fase>.md`), con el modelo y el esfuerzo de `config_v2_v64_experimental.json → modelos` (extracción: Sonnet, esfuerzo medio; fases A, B y C: Opus, esfuerzo alto; verificación: Opus, esfuerzo medio);
@@ -62,7 +70,7 @@
 ## 5. Cómo se lee el resultado
 
 - **Estado, acción y cubo** (ficha e informe, línea 1).
-- **Aptitud de uso** (`ficha.json → aptitud_de_uso`; informe §1, debajo de la línea de estado; columna del resumen V6.4): es la evaluación de la entrega, separada de la auditoría. Mientras diga «experimental», ni el estado «concluido» ni una auditoría APROBADO hacen el resultado apto para decidir con dinero real.
+- **Aptitud de uso** (`ficha.json → aptitud_de_uso`; informe §1, debajo de la línea de estado; columna del resumen V6.4): es la evaluación de la entrega, separada de la auditoría. Mientras diga «experimental», ni el estado «concluido» ni una auditoría APROBADO hacen el resultado apto para decidir con dinero real. Desde el hito 2 de la 4.15 hay además un bloque `verificacion_entradas` en todas las plantillas. Un modo de la entrada efectiva aplicado distinto del declarado impide «apto por entradas» también en `aptitud_de_uso` (`…_4_15/hito2/HITO_2_4_15.md`, I20).
 - **Objetivo** (`ficha.json → objetivo`; informe §1 y §14):
   - `objetivo_emitido`: nada material lo condiciona;
   - `objetivo_condicionado`: hay hipótesis sin fundamento que lo condicionan, pero la acción se sostiene en todo el ámbito calculado: el precio de Sí se da como **valor calculado condicional, provisional**, con la lista de hipótesis;
@@ -92,14 +100,28 @@
    - *Ejemplos de entrada y salida:* Viscofan y Vidrala (Excel) y Elis (PDF e instrucciones), en `empresas_v2_correcciones/2026-11_Vidrala_ensayo_4_14/`.
    - Cada expediente lleva en su carpeta la entrada (`etapa1/`, `fase1_*`, `texto/`) y la salida (`ficha.json`, `informe.md`, `auditoria.md` y los libros).
 2. **Registro de las entradas.** `python3 -B scripts/verificacion_entradas.py plantilla CARPETA` crea el registro. Para no tocar el expediente, hágase en una copia.
-   - **El extractor** rellena cada entrada: fuente con archivo, página, cita que contenga la cifra, escala y signo; o una derivación con orígenes y fórmula; o una hipótesis con fundamento, alternativas y límites; o un cero comprobado, un dato ausente o no aplicable, cada uno con su justificación.
-   - **Un revisor distinto** rellena `comprobacion` en cada entrada: revisor, resultado, fuente examinada y nota.
+   - **El extractor** rellena cada entrada: fuente con archivo, página, cita que contenga la cifra, escala y signo; o una derivación con orígenes y fórmula; o una hipótesis con fundamento, alternativas y límites; o un cero comprobado, un dato ausente o no aplicable, cada uno con su justificación. Desde la 4.15:
+     - `pagina` es la página del PDF, un entero, y el folio impreso va aparte;
+     - la fuente local tiene que existir y llevar su sha256 vigente;
+     - la cita tiene que contener la cifra equivalente, sin redondeo;
+     - `valor_fuente` es la cifra publicada con su signo, y la transformación (`signo`, `escala`) se declara;
+     - las cifras de juicio también entran en el registro.
+
+     Fuentes: `…_4_15/HITO_1_4_15.md`, R1–R3 e I8/I9; `…_4_15/hito2/HITO_2_4_15.md`, R415-SIGNO.
+   - **Un revisor distinto** rellena `comprobacion` en cada entrada (revisor, resultado, fuente examinada y nota) y la **sella**: `python3 -B scripts/verificacion_entradas.py sellar CARPETA --revisor NOMBRE --fecha AAAA-MM-DD CELDA [CELDA …]`, con la fecha de hoy.
+     - Sin ese vínculo con huella, la entrada queda pendiente.
+     - Si cambia lo vinculado, queda desactualizada.
+
+     Fuente: `…_4_15/HITO_1_4_15.md`, I13.
    - `python3 -B scripts/verificacion_entradas.py comprobar CARPETA` dice si el registro es apto. El pipeline lo vuelve a comprobar en el paso 12.
-   - Un registro no apto no impide recorrer el pipeline, y ninguna salida se presenta como apta para dinero real. Con la V6.4 y la V6.4.1, la ficha y el informe dicen «apta por entradas: no». Con la V6.3 (motor A) no lo dicen: el resultado está en `estado_pipeline.json → verificacion_entradas` y en el registro del pipeline (INCIDENCIAS I20).
+   - Un registro no apto no impide recorrer el pipeline, y ninguna salida se presenta como apta para dinero real. Con la V6.4 y la V6.4.1, la ficha y el informe dicen «apta por entradas: no». Desde el hito 2 de la 4.15, la ficha y el informe de **todas** las plantillas, también la V6.3 (motor A), llevan el bloque `verificacion_entradas`: apto o no por entradas, el recuento, `apto_para_dinero_real: false` y el modo de la entrada efectiva. Las salidas históricas sin registro ni modo no cambian (`…_4_15/hito2/HITO_2_4_15.md`, I20 corregido).
 3. **Cambio de base o corrección de datos de un expediente cerrado.**
    - Se escribe un `CAMBIO.json`, con los ejemplos de `…_4_14/configuracion/cambio_decisiones_*.json`, y se ejecuta `python3 -I scripts/cambiar_base.py preparar CAMBIO.json`. Nunca sobrescribe: crea un expediente nuevo y el origen no se toca.
    - Una corrección de la Historia va en `correcciones_fase1_partes`, con el valor impreso que se espera encontrar.
-   - Si el CAMBIO perdería una entrada `analisis` del origen, la preparación se detiene.
+   - Si el CAMBIO perdería una entrada `analisis` del origen, la preparación se detiene. Desde la 4.15:
+     - las entradas `analisis` se declaran con su cálculo;
+     - las heredadas se reconocen o se descartan, con motivo (`analisis_que_se_conservan` / `analisis_que_se_descartan`);
+     - el expediente nuevo lleva `entrada_efectiva.json`, por defecto en «estricta». Si falta un cálculo, el relleno se detiene y el pipeline termina en el paso 2 (`…_4_15/HITO_1_4_15.md`, C48).
    - Después se actualiza el registro de las entradas que cambian. Primero escribe el extractor y después revisa el revisor; también se actualizan los fundamentos de las hipótesis que reescriban las fases.
 4. **Regla de rama para los agentes.** Cada agente parte de la salida del expediente anterior (`../antecedentes/heredados/`) y cambia solo lo que se invalida, con una sección «Cambios frente al expediente anterior».
 5. **Configuración por motor.**
@@ -111,6 +133,11 @@
    - Si el pipeline se corta, se vuelve a ejecutar con el mismo comando: retoma en el paso guardado en `estado_pipeline.json`, y un agente que no terminó se vuelve a lanzar con el mismo `prompts_generados/NN_*.md`.
    - `--desde N` repite desde el paso N cuando cambia una entrada de ese paso, por ejemplo `--desde 12` para el registro de las entradas.
    - Si el material cambia después de una auditoría, la aprobación se retira sola: el pipeline emite una solicitud nueva, y una auditoría anterior no responde a ella.
-   - **Relevo caducado.** Si, mientras el paso 13 espera, cambia o aparece un archivo del material (`cierre_v2.MATERIAL_FIJO`), la solicitud pendiente ya no se puede aprobar: el pipeline no vuelve a fijar el material mientras espera (INCIDENCIAS I19). Se usa `--desde 12`, que emite una solicitud nueva.
+   - **Relevo caducado.** Si, mientras el paso 13 espera, cambia o aparece un archivo del material (`cierre_v2.MATERIAL_FIJO`), la solicitud pendiente ya no se puede aprobar. Desde el hito 2 de la 4.15 (I19 corregido), al relanzar el **mismo comando, sin `--desde`**, el paso 13:
+     - lo detecta y lo registra en `estado_pipeline.json → relevos_caducados`;
+     - repite la verificación del paso 12;
+     - pide la auditoría del material vigente. La solicitud antigua queda «sustituida», y su aprobación no cierra nada (`…_4_15/hito2/HITO_2_4_15.md`; `pruebas/test_relevo_i19_415.py`).
+
+     **Límite abierto (H9):** la vuelta es siempre al paso 12. Si lo cambiado son salidas de fases anteriores (fases A, B o C, o la entrada efectiva), volver al paso 12 no basta, y el procedimiento para ese caso no está documentado: está pendiente de verificar por cambio afectado.
    - **Relevo de un expediente anterior o sustituido:** en una copia hermana a la misma profundidad, nunca en su sitio. Se relanza primero con el mismo comando para regenerar los prompts con las rutas actuales (CONTINUIDAD §2, punto 6).
    - Una retirada o una publicación pendiente se resuelve con el mismo pipeline; ver `scripts/cierre_v2.py` y `documentacion_cierre_4_14/hito1/REGISTRO_REPARACION_4_13_1.md`.
