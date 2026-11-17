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
