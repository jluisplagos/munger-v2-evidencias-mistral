# Conectar Mistral mediante el plan Vibe

La documentación oficial permite usar una clave de **Code → Vibe CLI** con
`MISTRAL_API_KEY` para automatizar el CLI. Las sesiones web no ofrecen modo
desatendido. Es una vía distinta de suponer crédito disponible en una API general.

Preparación entregada: `vibe_connection.py`, versión fijada `mistral-vibe==3.1.2`.
Sin `--execute` nunca lanza inferencia, aunque exista la clave. La comprobación
de CI instala el CLI y verifica esta preparación; eso no prueba autenticación.

Paso pendiente de la persona responsable:

1. Crear una clave en **Mistral → Code → Vibe CLI**, correspondiente a su plan.
2. Guardarla en el auxiliar, Settings → Secrets and variables → Actions →
   New repository secret, nombre `MISTRAL_VIBE_CLI_KEY`. No pegarla en el chat.
3. Comunicar que el secreto está guardado. ChatGPT prepara entonces la ejecución
   única de autenticación y su reserva durable antes de lanzarla.

La persona responsable ya comunicó que el secreto está guardado. Se ha preparado
`run_vibe_auth.py` y `vibe-auth.yml`: una reserva create-only en la rama de
registro, tarea `vibe-auth-001`, precede a una única invocación del CLI. Si existe
reserva, no se vuelve a ejecutar. El resultado se publica en
`automation/coordination/reviews/vibe-auth-001/`; hasta recibirlo no se declara
autenticación. La comprobación horaria no activa este trabajo: es la conexión
interactiva solicitada por el usuario.

No activar pago por uso para esta conexión. El acceso y la imputación al plan
se comprobarán con la cuenta; la salida del CLI no demuestra por sí sola qué
saldo pagó la petición.

La prueba preparada, todavía no ejecutada con credenciales, pide una sola línea,
deshabilita herramientas y no entrega credenciales de GitHub/Anthropic al CLI.
Usa un directorio vacío, un turno, salida de 512 tokens, 90 segundos y límites
acumulados de 8192 tokens / USD 0,05. Según la documentación de Vibe, los límites
acumulados impiden la siguiente llamada después de alcanzar el límite: **no son
un techo de facturación previo a la primera llamada**. Las interrupciones no
autorizan reintentos. El arnés también tiene comportamiento interno que debe
verificarse con credenciales antes de abrir una cola desatendida.

Una respuesta correcta comprobaría únicamente conexión e identidad del CLI;
no valida ninguna empresa, valoración ni entrega del producto. El trabajador
de tareas y su integración siguen pendientes después de esta comprobación.

Fuentes oficiales consultadas el 17-nov-2026:

- https://docs.mistral.ai/vibe/code/cli/install-setup
- https://docs.mistral.ai/vibe/code/cli/api-keys-profiles
- https://docs.mistral.ai/vibe/code/cli/work-with-cli
- https://docs.mistral.ai/vibe/code/choose-cli-vscode-web-sessions
- https://github.com/mistralai/mistral-vibe/blob/v3.1.2/docs/programmatic-mode.md
