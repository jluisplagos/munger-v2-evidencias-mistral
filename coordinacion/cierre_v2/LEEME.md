# Programa único de cierre de Munger V2

Preparado el 16-nov-2026. Objetivo: una candidata integrada, revisada y probada, con evidencia económica suficiente para cada uso que se declare. No es una garantía de terminar en una noche/semana ni de evitar pérdidas.

## Puesta en marcha: cinco mensajes, una vez

| Sesión que ya existe | Archivo que debe leer y ejecutar | Papel desde ahora |
|---|---|---|
| **Claude F1/Elis**, la que entregó el estado 716cbd6 | PROMPT_CLAUDE_COORDINADOR.md | **Único coordinador e integrador**; trabaja en worktrees separados de F1 y candidata técnica |
| Mistral **«M2 cobertura integral ampliada»** | PROMPT_MISTRAL_A.md | Cierra evidencia contextual y prepara regeneración |
| Mistral **«…encargo mistral/d-qwe…»** | PROMPT_MISTRAL_D.md | Dueño del banco Qwen, arnés y relevo de aceptación |
| Mistral **«M2-FRENTE B PM1 ampliación económica»** | PROMPT_MISTRAL_B_E.md | Conserva B; nueva etapa **E**, fuentes económicas faltantes de Elis |
| Mistral **«M2-FRENTE C matemática independiente»** | PROMPT_MISTRAL_C_F.md | Conserva C2; nueva etapa **F**, contraste independiente y casos reales fuera de muestra |

No abrir cinco conversaciones adicionales. B y C reciben un **encargo nuevo**; no se reabre su trabajo anterior por defecto. Cuatro sesiones Mistral es una propuesta operativa para aprovechar las que ya existen, no una medida de coste óptimo. Solo se ejecutarán las que la interfaz/plan permitan.

Estos archivos son instrucciones preparadas: **no han sido enviados a esas sesiones**. No hace falta volver a pegar los prompts anteriores para los mismos trabajos. Este programa los reúne y conserva sus criterios; cada sesión consulta las revisiones enlazadas y el remoto antes de actuar.

## Un solo lugar para saber dónde estamos

La rama del auxiliar **`coordinacion/cierre-v2`** contiene este programa y CONTROL.json. **Solo Claude coordinador actualiza el control común.** Mistral escribe sus carpetas y ramas; entrega su ENTREGA.json, manifiesto y recuperación. Claude consulta esos commits, revisa y registra su incorporación.

- PROGRAMA.md: prioridades, condiciones de salida y cola para trabajo continuo.
- CONTROL.json: estado inicial contrastado, dependencias y próximas acciones.
- ESTADO.md: vista legible generada con `python3 coordinacion/cierre_v2/estado.py`.
- INTEGRACION.md: cómo se recibe, revisa e incorpora cada entrega.
- PLANTILLA_ENTREGA.json: contrato común para un relevo trazable.
- DECISIONES_PARA_EL_USUARIO.md: qué requiere decisión y qué no.

El control separa **entregado, revisado, integrado y probado**. Las pruebas del autor no son revisión externa. Una entrega parcial no es fracaso si declara exactamente el alcance y el bloqueo; tampoco es cierre del producto.

## Qué significa avanzar esta noche y en los siguientes días

Se avanza por **bloques verificables**, sin prometer fechas: resolver los defectos concretos, aceptar evidencia reutilizable, construir la candidata y ejecutar recorridos completos. Si una tarea necesita un dato o política ausente, se registra la dependencia y se continúa la siguiente tarea independiente. No pedir decisiones rutinarias para corregir un script, documentar una fuente o preparar una prueba.

Las instrucciones no mantienen una sesión viva por sí solas. Si el proveedor pausa, agota contexto o exige reanudación, debe quedar un checkpoint con el siguiente comando. No se ha creado un servicio ni una automatización que ejecute agentes durante toda la semana.

## Situación inicial

El código técnico sigue en 957af65 y F1 en 716cbd6. Las correcciones F1 W1–W3, C20 y CSV están pendientes de nueva entrega. A y D ya han publicado respuestas a la revisión d375d80; **esas respuestas nuevas no se han aceptado externamente**. Los 36 Qwen completos no están acreditados. Los datos materiales de Elis y P-M1 no están identificados. Detalle exacto en CONTROL.json; no hay porcentaje global fiable de finalización.
