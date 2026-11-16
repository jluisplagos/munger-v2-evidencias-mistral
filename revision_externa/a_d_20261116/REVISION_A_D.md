# Revisión externa dirigida · Mistral A y D · 16-nov-2026

## Dictamen

**A: corrección parcialmente conforme; cierre bloqueado por divergencia entre código y resultados y por falsas acreditaciones de reexpresión/columna. D: ejecuciones de componentes reproducidas; sus veredictos de aceptación no están acreditados por el arnés.** No se modifica el producto ni se adoptan políticas. Esta revisión es externa a las sesiones autoras; no es una auditoría económica completa de los expedientes.

Commits remotos consultados y fijados: A `0224b7182dd05d1e396223781d6f5db8b325ce2e`; D `b42f453caf0ca777b5fa56e6542ad0cc49130b9f`. Banco `4745f3887f7fd86bb3052f5d5e32285862df18e3`. Código del producto ensayado: `957af652cdc3bef3d67e8623c9572138bac685e9`. Revisión de Claude F1, B y C fuera de esta pasada.

| Plano | A | D |
|---|---|---|
| Entregado | Corrección contextual v2 publicada | 27 especificaciones y resultados por ID, matriz de 36, arnés y relevo |
| Revisado aquí | Diff, reglas, reproducción, sondas y propagación | Arnés, matriz, especificaciones, evidencias, comparación con banco y reproducción |
| Integrado | No | No |
| Probado aquí | Regeneración contextual, derivados, CSV, negativos y control | 27 especificaciones; 48 JSON comparados en campos de control; sondas de fallo del arnés y artefactos obsoletos |
| Resultado | Control reproducido exit 1 | Ejecuciones de componentes reproducidas; cero casos completos del personaje acreditados |

## Preparación y límites de la reproducción

Descarga única del ZIP base-4.14: 1.130.912.246 bytes; SHA256 `bb51942cefb848e409a4828e3faeb70f94aa4d29af39cda6d90cd0a97cb7b93e`. A: `preparar_insumos.py --zip` verificó y extrajo los 251 insumos seleccionados. D: copia limpia del código de la candidata, expediente plantilla 4.13 y dos plantillas XLSX requeridas, extraídos del mismo ZIP y comprobados contra el índice 4.14; se conservaron los archivos versionados de la candidata. **Selección parcial**, no materialización/verificación de los 6.798 archivos.

Se leyó código antes de ejecutar. Los ensayos escribieron solo en copias locales aisladas. Python, openpyxl y dependencias disponibles; no se contrató ningún proveedor de IA. El entorno de esta revisión sí expone pdftotext y soffice, pero no se ejecutaron el pipeline completo, LibreOffice ni un agente/personaje. Que Mistral careciera de esas herramientas es un límite de su entorno, no del producto.

Integridad antes de ejecutar: A 50/50 huellas coinciden. D 174 coinciden y faltan dos `.pyc` de `scripts/__pycache__/` incluidos indebidamente en el manifiesto. No se han releído todos los PDF ni acreditado semánticamente las 677 entradas: esta pasada comprueba las correcciones afectadas. Las sondas sintéticas ilustran defectos del verificador/arnés; no son datos de empresas.

## A · hallazgos y partes conservables

### A-R1 · material · el código final no reproduce los resultados publicados

Ejecutados sin cambios de código, en orden: `verificar_contexto.py`, `derivaciones.py`, `construir_cobertura.py`, `control_negativo.py`, `control_cobertura.py`. Los originales se conservaron en otro worktree.

| Estado en COBERTURA_677.csv | Publicado | Reproducido |
|---|---:|---:|
| REVISADO_CONTEXTUAL | 315 | 307 |
| PENDIENTE_CONTEXTUAL | 196 | 183 |
| CONFLICTO_CONTEXTUAL | 0 | 21 |
| REUTILIZADO_M1 | 60 | 60 |
| NO_APLICA | 106 | 106 |

El control termina **exit 1**, con conflicto propagado a Vidrala `Historia!I22`. Se modifican seis salidas respecto de los blobs publicados; hashes en A_REPRODUCCION.json. El negativo del autor no detecta esta incoherencia de entrega.

La diferencia nace de 20 conflictos de reexpresión en la regeneración: 18 celdas `Historia!C5` a `K5` (años), Vidrala `Historia!I23` y Viscofan `Palancas!C48`. El código final convierte `reexpresado="no aplica"` en conflicto por ser año comparativo; los resultados conservados no aplicaban esa regla. **No son 20 errores financieros demostrados.** El año de una columna es un metadato y no se reexpresa como un importe. La regla también necesita separar comparativo, cambio de importe, cambio de perímetro y no aplicabilidad.

Ejemplo de falso alcance incluso en la salida publicada: Vidrala `Historia!I5` figuraba REVISADO_CONTEXTUAL, con «reexpresado confirmado y declarado: el original CF_2022.txt imprime ['2021'] y el comparativo cita 2022». Eso no acredita una reexpresión monetaria.

Corrección: reconciliar primero la semántica y después regenerar todas las salidas dependientes con el código definitivo. No actualizar solo recuentos a mano ni forzar una meta de coincidencias.

### A-R2 · material · reexpresión y columna aún pueden acreditar la columna equivocada

Sondas ejecutadas con el módulo publicado, sin cambiarlo (SONDAS.json):

1. Original 2024: encabezado `2024 2023`, fila `Revenue 10000 9000`; comparativo 2024 del informe 2025 declara 9000. `check_reexpresion` devuelve «igual al original / no reexpresado» porque encuentra 9000 en **otra columna**. El 2024 original de la sonda es 10000.
2. Original con fila `Revenue 10000 8000`, comparativo declara 9000 y metadato «no reexpresado; igual al original». Devuelve **OK / reexpresado confirmado y declarado**, aunque el metadato contradice el cambio. La rama `contradice(..., True)` devuelve OK, no conflicto.
3. En columna actual: encabezado `2025 2024`, fila `Revenue 10000 9000`, período declarado 2024, columna textual «2024 (columna comparativa del informe 2025)», valor 10000. `check_columna` devuelve **OK**: considera tanto 2024 como 2025 años declarados. No separa año del informe de año de la columna.

Corrección: emparejar concepto/fila y columna inequívoca del mismo ejercicio y perímetro en ambos extremos. Comparar importes ya alineados; no cualquier número de la fila ni cualquier año de la descripción. Una contradicción explícita no puede etiquetarse OK. Ambigüedad → pendiente. Revisar solo los registros y derivados alcanzados por estas reglas; no rehacer el piloto conforme sin una dependencia concreta.

### A-R3 · alcance menor · escala en cabecera no comprueba la transformación

La sonda anterior euros/miles queda correctamente rechazada. Pero `check_unidad` con página sin frase de unidad, `doc={'miles': True}` y escala declarada **1** devuelve OK para miles, aunque la transformación requerida por este registro es 0,001. El control mecánico puede detectar otras inconsistencias; este check contextual no acredita la escala por sí solo. Aplicar la misma validación de escala en página y cabecera, y justificar el alcance de la cabecera a esa tabla.

### Lo conforme que se conserva

La regla v2 exige todas las dimensiones OK/NO_APLICA; la sonda euros→miles ya no pasa. Se conservan universo 677, 60 reutilizadas, estados mecánicos y cálculo de los 101 derivados. Las carencias reales, hipótesis y convenciones siguen separadas. Se debe corregir la acreditación contextual afectada, no reabrir toda la matemática o el alcance económico.

## D · hallazgos y evidencia conservable

### D-R1 · material · el arnés no determina cumplimiento a partir de resultados

`ejecutar_caso.py` no comprueba los esperados de los pasos; las especificaciones no contienen aserciones operativas. `Caso.ejecutar()` solo anota un AVISO si se usa `exit_esperado`, y el ejecutor no lo aplica a los pasos de estas especificaciones. `ejecutar_todo.sh` continúa tras errores. `generar_matriz.py` copia etiquetas estáticas de adaptaciones.json y escribe `preserva_sentido="sí"` sin evaluarlo.

Sondas reales del arnés (SONDAS.json):

- Con carpeta scripts de candidata vacía (entorno deliberadamente incompleto), los cinco comandos de Q1-001 salen con código **2**. El arnés devuelve **exit 0** e imprime **OK Q1-001**.
- En una copia sin carpeta de evidencias, el generador produce las 36 filas y mantiene **29 CUMPLE**.

Esto no demuestra fallo de Munger. Demuestra que el arnés no acredita esos veredictos ni detecta una regresión nueva. Añadir aserciones por criterio, códigos esperados (los negativos pueden necesitar exit 1/3), campos/estados esperados y artefactos. Un fallo inesperado debe propagarse. Separar resultado de componente y resultado de caso; no afirmar CUMPLE del caso completo cuando quedan criterios sin observar. La revisión manual de un resultado debe identificarse como tal.

### D-R2 · material · puede presentar artefactos heredados como salida de un comando fallido

`nuevo_expediente()` copia también las salidas preexistentes del expediente histórico. `copiar_artefacto` solo comprueba existencia. En la sonda con el producto real y una plantilla binaria temporalmente ausente, ficha/informe provisionales salieron con **exit 2**, indicando que no escribían ninguna salida. El arnés siguió con exit 0 y copió ambos artefactos: **idénticos byte a byte a los preexistentes de la plantilla**. Evidencia D_SALIDA_OBSOLETA.json. La dependencia se restauró después.

Corrección: expediente de prueba con estado inicial declarado, salidas previas retiradas/archivadas sin dañar los históricos, y comprobación de que cada artefacto pertenece a la ejecución y material actuales. Nunca usar la mera existencia como éxito. La invalidación de una aprobación histórica observada conserva valor como ensayo limitado; no sustituye crear y revisar una aprobación nueva de prueba por las vías soportadas.

### D-R3 · material · recuentos, reutilización y Q1-034

- Hay **27 especificaciones y 27 resultado_ejecucion.json**, no 31 ejecuciones independientes por ID ni 23 especificaciones como dice el resumen. Los 31 PARCIAL_COMPONENTE incluyen reutilizaciones de otros casos y Q1-026 con error de entorno; no equivalen a 31 recorridos propios.
- Q1-028, Q1-032 y Q1-035 referencian patrones de Q1-036. Pueden reutilizar una observación, pero no acreditan precondiciones o criterios no ensayados. El recuento 1/321 no prueba los 4/1/5 de Q1-032 ni los 3/2/5 de Q1-036. No hay que forzar un universo reducido si no está soportado: registrar qué criterio falta.
- Q1-034 es **CONTRATO_REFERENCIADO** en el banco. Rango acotado no implica elegir un punto ni esperar una nueva política para observar preservación del rango, ausencia de punto inventado y continuación del análisis permitido. Mantener separado lo que sí dependa de una decisión. No cambiar su naturaleza ni usar la falta de política para saltarse todo el caso.
- Q1-035 figura como PARCIAL_COMPONENTE en la matriz y entre los cinco no ejecutados en el resumen. El apartado «3 sin veredicto ... uno más sin ejecutar» también contradice el detalle de estados. Generar todos los recuentos desde una única fuente validada.

Corrección: matriz por criterio y precondición; distinguir ejecución propia, observación compartida, no ejecutado, entorno y relevo. Conservar 31 contractuales/3 propuestas/2 decisiones del banco, sin transformar propuestas en exigencias ni omitir el suelo contractual.

### D-R4 · material para la afirmación de independencia · comprobaciones preescritas

`comprobacion="verificada"` se transforma automáticamente en un registro con extractor y «revisor independiente de prueba D» escritos por el mismo arnés, fecha y fuente, antes del sellado. Son **precondiciones simuladas de un test de componentes**, no evidencia de extracción/revisión independiente realizadas. No deben contarse como haber completado las precondiciones semánticas o la auditoría del banco.

Corrección: identificar explícitamente estas precondiciones como simuladas y su alcance. Para casos cuya aceptación exige revisión/auditoría efectiva, ejecutar la vía soportada con actores/procedencia reales de prueba o dejar el criterio pendiente. No hace falta un proveedor de pago para conservar la parte mecánica de estas pruebas; no inventar identidades adicionales para cerrar la aceptación.

### D-R5 · menor · manifiesto y preparación

El manifiesto incluye dos `.pyc` ausentes en Git. Excluir cachés y regenerar sobre archivos entregados. La preparación debe comprobar el SHA real del código y del banco utilizados, dependencias y fallos de materialización; no basta una constante en CONFIGURACION.json. Documentar correctamente BANCO_DIR (el preparador y el ejecutor esperan niveles de directorio diferentes al sobrescribir esa variable).

### Lo reproducido y conservable

Se ejecutaron las **27 especificaciones** sobre código 957af65 y copias de prueba. Tras completar las dependencias binarias verificadas, coinciden las secuencias de códigos de salida de **27/27** y los campos de control de **48/48 JSON** comparables con lo publicado (D_REPRODUCCION.json). Se compararon universo, clases, comprobadas/pendientes/desactualizadas, errores/discrepancias y aptitud por entradas donde existían. No se comparó cada byte dependiente de fecha, ruta o material; no es una revisión de todas las decisiones semánticas.

Se conserva evidencia mecánica de rechazo/registro, vigencia, clases y bloqueo de publicación por interfaces concretas bajo esas precondiciones. No se observaron en esta pasada defectos nuevos del producto: los hallazgos D-R1–R5 afectan a su arnés, interpretación y entrega. La ausencia de defectos observados no acredita todos los criterios. **Cero casos completos del personaje aceptados por esta revisión.** No se ejecutó Q1-026 de extremo a extremo ni los 17 esperados numéricos a través de todo el producto.

## Siguiente acción finita

1. Mistral A: una corrección dirigida A-R1–R3, con reproducción desde insumos fijados y salida final coherente; no una investigación nueva de 677 registros.
2. Mistral D: corregir arnés, precondiciones, limpieza/procedencia de artefactos y matriz D-R1–R5. Repetir los componentes afectados y demostrar que controles negativos del arnés fallan correctamente. Conservar los logs válidos previos. Preparar relevo de los criterios sin agente/runtime; no fingir completarlos.
3. Revisión posterior limitada a estos cambios y sus dependencias; integración a cargo del integrador. No fusionar ni cambiar política económica por inferencia. No solicitar decisiones para corregir errores del arnés.

Encargos completos en CORRECCION_A.md y CORRECCION_D.md. No se han enviado mensajes a las sesiones ni a terceros. El saldo/consumo no es visible. No se estiman fechas ni porcentajes globales.
