# Contraste Mistral del banco Qwen solicitado por el usuario

## Qué resuelve

El usuario pregunta si los recorridos Qwen son fiables y si Mistral puede
repetirlos. El banco revisado 4745f38 es una propuesta de aceptación, ya revisada
estructuralmente: 36 casos, 17 esperados y 9 controles negativos. Eso no equivale
a cumplimiento del producto. Los recorridos completos siguen en 0/36.

La repetición contra el producto espera el cierre de D3 del ejecutor y requiere
agentes, entradas, observables y artefactos reales sobre un SHA fijado. Ni usar
otro proveedor ni volver a generar respuestas del banco sustituye ese recorrido.

## Trabajo de Mistral preparado

Tarea qwen-bank-review-001: contraste documental de coherencia interna de los
36 casos, sus fixtures, el plan y los resultados esperados. Preserva las siete
correcciones del integrador; no reabre decisiones ni modifica el banco. No es
una revisión ciega: los esperados están visibles. No se incluye el contrato
primario completo ni el código del producto; se limita lo que puede concluir.

Paquete fijo en requests/qwen-bank-review-001.json: 58 archivos del banco
@4745f3887f7fd86bb3052f5d5e32285862df18e3. Se comprobaron tamaño y hash Git de
los 58 originales, y los SHA-256 de las 57 entradas del manifiesto. Se conserva
el manifiesto original, excluido de su propio inventario. No se ejecuta el
Python de Qwen al verificar esa integridad.

Una reserva create-only precede al CLI. Preflight con límite cero para resolver
el modelo efectivo sin generación; después, una sola generación, sin herramientas,
en directorio vacío y sin credenciales GitHub/Anthropic en el entorno del CLI.
Versión mistral-vibe 3.1.2. Se fija el modelo resuelto y el esfuerzo más alto que
anuncia su configuración entre max/high/medium/low/minimal/off. Se registra como
configurado, sin inventar observación directa del parámetro en el proveedor.

Salida máxima 16384 tokens, un turno y 300 segundos; límites acumulados del CLI
120000 tokens / USD 1, que no son un techo de facturación previo a la llamada.
No se activa pago por uso. La imputación al plan no se presupone de un coste
reportado como cero. Un fallo conserva reserva y no se reintenta automáticamente.

El informe exige 36 ids distintos y citas literales verificadas. Una validación
de formato no prueba que sus interpretaciones sean correctas. Estado de salida:
pendiente de aceptación por otro contexto; accepted=false, integrated=false,
product_executed=false y complete_product_cases=0. Si falla, se conserva el texto
visible recibido. Las pruebas con respuestas simuladas son del ejecutor, no son
resultados de los casos Qwen.

## Recogida por el coordinador

Rama automatizacion/claude-api-piloto-registro, carpeta
automation/coordination/reviews/qwen-bank-review-001/. Consultar resultado real,
modelo, esfuerzo, límites y consumo; no atribuir un resultado antes de publicarse.
ChatGPT examina las observaciones y Claude decide qué correcciones concretas
proceden. El banco original se conserva y ninguna política económica se adopta.

La conexión Vibe sí se comprobó en vibe-auth-001: una respuesta correcta,
versión 3.1.2, una generación. Eso prueba conexión, no este trabajo ni el producto.

Preparación inicial (4725f30, Actions 44079249084): falló al validar la configuración
completa de Vibe sin inicializar HarnessFilesManager. Ocurrió después de acreditar
preflight token_limit con cero uso/coste y antes de iniciar la generación. Se
conservó preparation_failure_44079249084.json y la reserva; no hubo respuesta de
revisión. Se corrige leyendo únicamente metadatos del catálogo exportado.
La reanudación explícita de la misma tarea exige esa evidencia exacta de cero
generaciones, el mismo SHA de paquete y una transición con SHA esperado. No borra
la reserva ni abre otra tarea para repetir una inferencia de consumo incierto.

El intento completo sí generó después una vez (ed9d3c5, Actions 44080061002):
modelo configurado mistral-large-4-0, esfuerzo high, uso informado 42992 entrada /
16384 salida, 1024 entrada en caché. Terminó por límite de salida, sin texto
visible y sin revisión entregada. Coste CLI 0; imputación al plan no comprobada.
La reserva y el fallo se conservan; la tarea completa no se vuelve a ejecutar.

Nuevo alcance por tandas: qwen-bank-group-01…06, seis casos cada una. La proyección
conserva las líneas originales de esos casos, todos sus fixtures íntegros, el plan
y el resumen. Declara expresamente la selección de líneas y conserva el hash del
paquete íntegro original. Las seis tandas cubren exactamente 36 ids sin solaparse.
Una generación máxima por tanda, 32768 tokens de salida, mismo esfuerzo alto
anunciado por el modelo y 300 segundos. Primero se activa solo la tanda 01; las
demás esperan un informe utilizable y comprobado. No cambia la clasificación del
banco ni cuenta como un recorrido del producto. Se preserva el consumo anterior.

Tanda 01: Mistral entregó seis casos y cinco observaciones (12424 entrada / 11781
salida, 1024 caché; coste CLI 0, saldo aplicado no comprobado). El control original
rechazó una cita de Markdown que unía líneas. postprocessed_report.json conserva
el texto visible original y registra la cita recompuesta con los saltos literales
del archivo, su ubicación y la regla aplicada; cero inferencias añadidas. Los
caracteres permanecen iguales y no se permite cruzar párrafos ni corregir números.

Siguiente contraste: qwen-peer-group-01, Claude Sonnet 5.5/high, entrada USD 2/MTok,
salida USD 10/MTok, máximo 16384 salida y reserva calculada <= USD 0,50. Fuentes
fijadas a un commit de la rama de registro y a la proyección exacta del banco;
rechaza casos incompletos, fuentes alteradas o atribuciones de pruebas del producto.
Sin herramientas, una llamada como máximo, streaming, sin reintentos; dictamen
documental pendiente de aceptación. No se activa esta llamada desde el chequeo
horario: forma parte de la prueba operativa solicitada de colaboración.
