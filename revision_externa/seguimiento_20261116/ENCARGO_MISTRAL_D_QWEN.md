# Mistral D · adaptación y ejecución de aceptación Qwen Q1

## Objetivo

Convertir el banco Qwen ya revisado en pruebas ejecutables de Munger V2 sobre una candidata técnica fijada. Construir adaptadores y observables, ejecutar las partes disponibles por las vías reales del producto y dejar preparado el relevo supervisado del resto. El resultado útil son ejecuciones reproducibles y una matriz de cobertura honesta, no otra revisión general del banco.

Este es un encargo nuevo, independiente de Mistral A/B/C y de Claude F1. No reemplaza sus correcciones. La aceptación completa aún no se ha ejecutado: estado inicial conocido **0/36 casos contra el producto**. El saldo y consumo actuales no son visibles para ChatGPT; registra solo lo que tu sesión pueda comprobar. No gastes créditos por agotarlos.

## Repositorios, rama y permiso de trabajo

- Evidencias y código de prueba: https://github.com/jluisplagos/munger-v2-evidencias-mistral
- Producto como fuente: https://github.com/jluisplagos/munger-v2
- Trabaja en una sesión nueva y rama propia `mistral/d-qwen-aceptacion`, creada desde `revision/chatgpt-seguimiento-20261116`. Guarda entregables únicamente en `resultados_qwen/ejecucion_d/` del auxiliar.
- No cambies ramas A/B/C ni archivos de otros frentes. No fusionar ni abrir PR de integración al producto. No cambiar políticas, fuentes o libros oficiales.
- Está autorizado construir un arnés externo y ejecutar comandos documentados del producto **en copias locales de prueba aisladas**, incluidos los pasos de pipeline/LibreOffice que de verdad necesiten esos casos, si están disponibles y después de inspeccionar qué ejecutan. Esta ampliación se limita a este frente D; las prohibiciones del encargo histórico M1 no deben interpretarse como prohibición de estas pruebas locales ahora solicitadas. No publicar expedientes sintéticos como expedientes reales. No ejecutar macros de archivos de procedencia desconocida ni activar servicios de pago.
- Si para resolver un defecto hace falta cambiar el producto, entrega reproducción y propuesta separada; no corrijas la candidata para hacer pasar los tests.

## Lectura inicial y versiones

1. Lee íntegramente la continuidad:
   https://github.com/jluisplagos/munger-v2-evidencias-mistral/blob/8d82c8fea43b55fbd167eef8738aba1f64f3e426/docs/continuidad_chatgpt/CONTINUIDAD_20261116.md
2. Lee SEGUIMIENTO.md en `revision_externa/seguimiento_20261116/` de la rama de seguimiento y las instrucciones del repositorio. Las decisiones registradas se conservan.
3. Consulta los HEAD remotos de la rama técnica y del banco antes de trabajar. Candidata técnica propuesta: `claude/hopeful-bardeen-qap6y0`, SHA `957af652cdc3bef3d67e8623c9572138bac685e9`. Banco fijado: `revision/qwen-q1-v2`, SHA `4745f3887f7fd86bb3052f5d5e32285862df18e3`.
4. Usa esos SHA en copias aisladas. Si hay cambios posteriores, registra diff y relación con este encargo; no mezcles silenciosamente revisiones ni declares los resultados aplicables al HEAD nuevo. No es necesario volver a preguntar para ensayar la candidata fijada; señala la diferencia de vigencia.
5. Usa exclusivamente `resultados_qwen/q1_v2/banco_revisado/` como banco normativo de esta ejecución. Lee README, revisión externa y PLAN_DE_EJECUCION completos. Conserva sin cambios los originales y el manifiesto recibido; comprueba el banco en una copia de trabajo.
6. En la candidata, localiza guía de recorrido, HITO_2_4_15.md, contrato de entradas, vías manuales/pipeline, esquemas, generación/verificación de auditorías y recuperación. Lee lo pertinente para elegir interfaces soportadas. No supongas nombres de CLI ni que exista una API de chat autónoma.

## Bloque 1 · adaptación y piloto real

Publica primero este bloque antes de continuar el resto; no esperes al final de todo para guardar trabajo.

### Mapa de los 36 casos

Crea MATRIZ_EJECUCION.csv con exactamente una fila por ID y estas distinciones:

- naturaleza original: contrato, propuesta o política pendiente;
- precondiciones que realmente necesita;
- componente e interfaz real de la candidata;
- parte automatizable y parte que exige agente/relevo supervisado;
- observable de cada criterio y artefacto/estado donde se comprueba;
- adaptación necesaria y si preserva el sentido del caso;
- estado de ejecución y veredicto, separados;
- evidencia y comandos o interacción reproducible;
- qué queda sin comprobar.

No conviertas tres propuestas y dos políticas pendientes en requisitos obligatorios. Si un criterio individual es propuesto dentro de un caso contractual, conserva también esa distinción.

### Piloto

Adapta primero un positivo de entradas (Q1-001 o Q1-002), un conflicto/carencia de entradas (Q1-006), un caso de cambio posterior a revisión (Q1-026 o Q1-027) y el intento de exportación manual Q1-036. Revisa en el banco las precondiciones exactas; no improvises otras.

Ejecuta las partes respaldadas por interfaces reales; verifica tanto respuesta como estado persistido y artefactos de salida. Incluye controles que demuestren que el arnés también detectaría una salida incorrecta. No uses solo búsquedas de palabras como «bloqueado» o «APROBADO».

Para vigencia/cambios, no cargues una aprobación ficticia del fixture como si fuera auténtica: crea un expediente **de prueba** mediante las vías soportadas y completa la revisión de prueba exigida. Registra quién/herramienta intervino y con qué independencia. Si no puedes satisfacerla, deja esa parte pendiente y prueba solo lo realmente observable. No fabriques firmas ni suplantes a otro revisor.

Si no existe ejecución del agente/personaje disponible, no te respondas a ti mismo los prompts del banco y lo llames prueba del producto. Puedes ejecutar sus componentes accesibles y preparar el paquete exacto de relevo: configuración, instrucciones oficiales, entrada íntegra del usuario, fixtures y observables requeridos. Distingue prueba de componente de aceptación completa.

Haz commit y push al terminar el mapa y el piloto, con resultados obtenidos y límites. Continúa el bloque siguiente sin esperar confirmación rutinaria.

## Bloque 2 · cobertura restante

1. Extiende los adaptadores a los casos restantes que permitan las interfaces de la candidata, reutilizando infraestructura del piloto.
2. Ejecuta cada caso en un directorio o estado limpio. Captura código de salida, stdout/stderr relevantes, versión, entradas/huellas y artefactos producidos. No reutilices una aprobación tras mutación sin verificar su vigencia.
3. En los 17 casos numéricos, los esperados del banco sirven como oráculo; la respuesta observada tiene que proceder de una ejecución del componente real. Recalcular el esperado en otro script no ejecuta el producto.
4. Verifica positivos para detectar rechazo excesivo, no solo negativos para detectar aprobación indebida. Una carencia afecta a su conclusión dependiente, no obliga a bloquear toda actividad.
5. Trata expresamente confusión cero/ausencia/N/A, unidad/periodo/perímetro, derivados, instrucciones incrustadas en fuentes, vigencia/cambio/reversión, contexto limpio y exportación manual. Cubre solo lo que los casos realmente exigen; no amplíes indefinidamente el banco.
6. Q1-036: examina el artefacto exportado y cualquier aprobación vigente que el producto exponga, no solo el chat. Si no existe una vía manual ejecutable, documenta la ausencia o el relevo necesario según el contrato; no inventes un fallo de una interfaz inexistente.
7. Mantén políticas pendientes como pendientes. No elijas R, θ, λ, k, probabilidades, umbrales o caducidad para hacer pasar un caso. Los escenarios sintéticos conservan sus parámetros expresos sin convertirse en política real.

Estados de ejecución: NO_EJECUTADO, ADAPTACION_PENDIENTE, PARCIAL_COMPONENTE o EJECUTADO_COMPLETO. Veredictos según el plan: CUMPLE, FALLA_IMPLEMENTACION, REQUISITO_NO_IMPLEMENTADO, DECISION_PENDIENTE o NO_OBSERVABLE; deja sin veredicto definitivo lo no ejecutado. Un criterio observado puede tener resultado propio, pero no presentes el caso completo como CUMPLE si faltan criterios.

## Bloque 3 · defectos y relevo

Por cada fallo observado:

- requisito aplicable y criterio exacto;
- mínima precondición y reproducción desde estado limpio;
- esperado frente a observado, con artefactos;
- por qué no es un error del adaptador o una propuesta no adoptada;
- efecto limitado y componente responsable;
- propuesta de corrección separada, sin modificar el producto.

Si el bloqueo es del entorno, intenta la alternativa soportada más directa y registra el error concreto. No pidas tokens ni vuelques secretos. Si no hay un runtime, dependencia o canal necesario, entrega adaptadores funcionales de lo accesible y paquetes de relevo listos para lo restante; no dediques el resto de la sesión a reiterar la misma descarga o acceso fallidos. La ausencia de observables no prueba cumplimiento.

## Entrega finita

Todo bajo `resultados_qwen/ejecucion_d/`:

- README.md: un comando de reproducción para lo automatizado, requisitos y límites.
- CONFIGURACION.json: SHA producto/banco, fecha, entorno, herramientas/modelo realmente expuestos, alcance de la copia materializada; distinguir selección parcial de base completa.
- MATRIZ_EJECUCION.csv: 36 filas, estados y evidencias por caso.
- scripts/: adaptadores/ejecutor/comprobación de resultados, sin modificar producto.
- evidencias/: logs y observables acotados; no subir PDF/XLSX/ZIP originales ni secretos. Si un binario de salida es necesario para reproducir, conserva su huella y el comando que lo genera; no afirmes que está preservado en Git si no lo está.
- HALLAZGOS.md: solo defectos reproducidos, límites y decisiones pendientes separados.
- RELEVO_SUPERVISADO.md: entradas y pasos exactos para los casos no ejecutables automáticamente; indica quién/componente falta, sin atribuirle trabajo ya realizado.
- RESUMEN_PARA_INTEGRADOR.md: entregado/revisado/integrado/probado, recuentos de casos completos y parciales, criterios cubiertos y pendientes. No confundas cantidad de comandos con cantidad de casos.
- PUNTO_DE_RECUPERACION.md y MANIFIESTO_SHA256.txt.

Haz commit y push tras cada bloque, sin fusiones ni ciclos recursivos de revisión. Al acabar da enlaces y SHA congelado. No declares aptitud para dinero real: pasar software no identifica parámetros económicos ni valida capacidad predictiva. La revisión externa y la integración son posteriores y separadas.

Este encargo termina con la entrega trazable de los 36 casos mapeados y las ejecuciones/relevos honestamente disponibles, incluso si quedan bloqueos concretos. No termina con una promesa de ejecutarlos ni con otro simple pase del comprobador del banco.
