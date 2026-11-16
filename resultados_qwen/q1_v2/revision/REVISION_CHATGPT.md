# Revisión externa del banco Qwen Q1 v2 · 16-nov-2026

## Dictamen

**Banco de aceptación propuesto, estructuralmente comprobado y revisado en el alcance aquí descrito; pendiente de adaptar, ejecutar y revisar contra el producto.** No se declara aptitud para dinero real. No se ha ejecutado ninguno de los 36 casos contra Munger V2.

Qwen corrigió los problemas sustantivos de v1: equivalencia miles/millones, inventario sin agregado ambiguo, deuda 300 aportada en los casos aislados, derivado neutro sin definición falsa de EBITDA, rechazo de booleanos/no finitos y constante simple, delimitación del rango del litigio y distinción entre conflicto resuelto y bloqueo vigente. Su declaración de no ejecución se conserva intacta.

La copia recibida y su comprobador dieron código 0: 36 casos, seis por familia, dos positivos por familia, 17 esperados numéricos y siete controles negativos detectados. Se materializaron 50 fixtures y un manifiesto real de 57 archivos. Ese resultado no bastaba para aceptar sin revisar los criterios y el comprobador.

## Debilidad residual del comprobador y corrección local

El comprobador recibido usa un conjunto de nombres visitados por el AST. Para Q1-005, `[1200, 1050]`, esperado 150, acepta:

```text
op0 * 0 + op1 * 0 + 150
```

Los nombres aparecen pero no intervienen en el resultado. `SONDA_COMPROBADOR_V2.json` conserva el contraejemplo real ejecutado sobre la copia recibida. No se atribuye este resultado al producto.

En la copia revisada se restringe **la gramática de este banco finito**: números declarados como operandos, nombres opN sin constantes literales y cada operando una sola vez. Las 17 operaciones actuales ya cumplen esta forma. Se añade rechazo de la constante disfrazada y de `op0 - op0 + op1`, con sus respectivos controles negativos.

Esto no es una regla para los derivados financieros de Munger ni una prueba universal de dependencia o corrección económica. Una fórmula financiera legítima podría repetir operandos; no está siendo evaluada por este comprobador del banco.

## Precisiones del integrador para evitar falsos fallos

Los siete originales se conservan; `CAMBIOS_INTEGRADOR_CASOS.json` identifica los ocho casos ajustados:

- **Q1-002:** el fixture incluye ahora el texto examinable de la Nota 2 sintética que justifica el N/A. Una mera referencia a una nota no adjunta no sirve de evidencia completa.
- **Q1-006:** ausencia de fuente para un cero no equivale por sí misma a contradicción con un valor publicado distinto. Se exige la incidencia correcta.
- **Q1-007:** la escala de una tabla puede seguir pendiente sin impedir usar directamente los 2,5 millones de la nota con unidad explícita y fuente examinada.
- **Q1-023:** admite usar un período ya documentado y declarado, además de pedir aclaración; no fuerza otra pregunta si ya está identificado.
- **Q1-025 y Q1-030:** no inventar caducidad temporal; tampoco penalizar una política temporal realmente adoptada y aplicable. Una política pendiente no se decide en el banco.
- **Q1-034:** un punto elegido sigue siendo hipótesis con fundamento y límites; no se transforma en dato comprobado mediante firma.
- **Q1-035:** una política puede permitir cálculo experimental etiquetado, pero no demuestra por sí misma validación del motor ni aptitud para dinero real.

El plan aclara que los fixtures son descripciones sintéticas: deben adaptarse por vías soportadas, no inyectarse como sellos o aprobaciones oficiales. `ADAPTACION_PENDIENTE` se distingue de un fallo del producto. Las propuestas contenidas en criterios individuales tampoco se convierten automáticamente en obligaciones contractuales.

## Verificación ejecutada por el integrador

- Revisión estática: scripts de biblioteca estándar, sin red, procesos externos o ejecución del producto. Las 50 rutas de fixtures son locales TXT/CSV/JSON; los JSON sintéticos son legibles.
- Materialización de la copia revisada: **50/50**.
- Comprobador revisado con autocontroles: **código 0; nueve de nueve controles negativos detectados**.
- Distribución: **36 casos, 12 positivos y 24 conflictos/carencias**, seis por familia; **31 contractuales, tres propuestas y dos decisiones pendientes**.
- Aritmética independiente con fracciones exactas: **17/17** resultados conformes. Se revisaron los operandos contra los archivos de cada caso; el factor 1000 de conversión miles/millones es una transformación de unidad declarada.
- Sondas directas sobre la copia revisada: constante simple, constante disfrazada y cancelación de operando repetido, **tres de tres rechazadas**.
- Manifiesto de la copia revisada: **57 huellas reales**, excluyendo el propio manifiesto. Los resultados de ejecución y fecha constan en `banco_revisado/resultado_comprobacion.json`.

La autoría de los cambios del integrador se separa de Qwen y de su declaración de no ejecución. Ni las pruebas del comprobador ni los esperados numéricos demuestran que el producto cumplirá los casos. La siguiente evidencia necesaria es su ejecución sobre una candidata fijada con los observables y precondiciones correctamente preparados.

## Siguiente paso

No es necesaria otra ronda de Qwen para esta entrega. Conservarla en el auxiliar para preparar la aceptación del personaje; no fusionarla automáticamente con la rama de producción. Claude mantiene su trabajo técnico/económico y Mistral sus correcciones M2. La adaptación y ejecución de los casos requieren un encargo separado sobre una versión concreta, sin confundir un banco ya preparado con un producto ya validado.
