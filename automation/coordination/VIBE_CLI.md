# Conectar Mistral mediante el plan Vibe

La documentación oficial permite usar una clave de **Code → Vibe CLI** con
`MISTRAL_API_KEY` para automatizar el CLI. Las sesiones web no ofrecen modo
desatendido. Es una vía distinta de suponer crédito disponible en una API general.

Preparación entregada: `vibe_connection.py`, versión fijada `mistral-vibe==3.1.2`.
Sin `--execute` nunca lanza inferencia, aunque exista la clave. La comprobación
de CI instala el CLI y verifica esta preparación; eso no prueba autenticación.

Paso pendiente de la persona responsable:

1. Crear una clave en **Mistral → Code → Vibe CLI**, correspondiente a su plan.
2. Guardarla en el auxiliar como secreto `MISTRAL_VIBE_CLI_KEY`. No pegarla en el chat.
   Desde AUTO1 debe ser un *Environment secret* del environment protegido
   `inferencia-aprobada` (ver más abajo), no un secreto del repositorio.
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

## Puerta humana e instalación aislada (AUTO1-M6, M7, m7 y m9)

**Paso pendiente de la persona responsable:** crear en el auxiliar el environment
`inferencia-aprobada` (Settings → Environments) con **Required reviewers**, y guardar
en él `MISTRAL_VIBE_CLI_KEY` y `ANTHROPIC_API_KEY` como *Environment secrets*.
Después, borrar los secretos homónimos del repositorio. El procedimiento completo y
el tope acumulado están en PROGRAMA.md, «Correcciones AUTO1».

- `vibe-auth.yml`, `qwen-bank-mistral-review.yml` y `qwen-bank-mistral-groups.yml`
  solo se lanzan con `workflow_dispatch`. Cada job con secreto espera la aprobación
  de ese environment. En las tandas, el job Mistral y el job Claude se aprueban por
  separado.
- `vibe-readiness.yml` se sigue lanzando con push, pero ya sin la clave (m9). Su
  preparación nunca autentica.
- Vibe se instala en un paso sin secretos, en `$RUNNER_TEMP/vibe-venv`, con
  `--only-binary=:all:`, de modo que no se ejecuta código de construcción.
  - El script que orquesta se ejecuta con el Python del sistema, que no carga
    `.pth` del entorno virtual.
  - Solo el proceso `vibe` usa el entorno virtual, sin `GH_TOKEN` ni `ANTHROPIC_API_KEY`.
  - **Pendiente:** fijar hashes (`--require-hashes`). Sin red no se han podido obtener,
    y no se inventan.
- Las dos invocaciones del contraste, la preparatoria y la generación, arrancan con
  `cwd` en el directorio vacío. La preparatoria se cuenta en
  `preflight_invocations_started` (m7).
