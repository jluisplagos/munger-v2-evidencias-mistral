# Coordinación asistida de Munger V2 · ampliación del 17-nov-2026

Encargo nuevo de la persona responsable: aprovechar sus créditos y trabajar en
conjunto. La automatización pasa a formar parte del programa y debe revisarse;
dejarla «fuera de alcance» por ser una rama nueva no cierra esta asignación.
No se adopta ninguna política económica ni se reduce el alcance original.

## Autoridad y roles

- Claude coordinador conserva CONTROL/ESTADO y la integración de la candidata.
- Mistral conserva las correcciones de sus frentes. D3, E2 y F3 siguen vigentes
  hasta respuesta y revisión; terminar una sesión no equivale a cerrar la tarea.
- Claude API produce informes/contrastes en ramas del auxiliar. No acepta sus
  propios informes, no cambia el producto ni sustituye las fases reales Qwen.
- ChatGPT consulta fuentes/commits y contrasta resultados. Su comprobación
  programada informa novedades, y no declara una llamada de modelo como prueba
  ejecutada del producto.
- La cuenta de Mistral está en Vibe/Le Chat. Su documentación admite Vibe CLI
  programático con clave del plan; su funcionamiento en esta cuenta está pendiente
  de comprobar. No comprar ni activar pay-as-you-go para suplirlo por inferencia.

## Primer trabajo API de esta ampliación

audit-pilot-code-001: auditoría documental crítica del código de automatización,
sus pruebas, el workflow y este contrato. Modelo Claude Fable 5.2, esfuerzo max
explícito. Es una ejecución distinta del autor ChatGPT. No ejecuta pruebas ni
parches. Las 49 pruebas del piloto se conservan y se repiten solo por cambios
en el código. La autenticación/modelo y resultado efectivos se registran.

Una sola petición Messages, reserva previa calculada <= USD 2. Tarifas oficiales
consultadas el 17-nov: entrada USD 8/MTok, salida USD 40/MTok; salida máxima 32768.
Sin reintento automático. Un timeout conserva reserva y consumo incierto. Salida
estructurada, citas literales verificadas y texto conservado incluso si se rechaza.
El crédito promocional aplicado se comprueba en Console, no se inventa desde uso.

La reserva e informe van a la rama automatizacion/claude-api-piloto-registro,
carpeta automation/coordination/reviews/audit-pilot-code-001/. Una reserva previa
bloquea otra inferencia. Las observaciones quedan pendientes de revisión humana.
Ningún resultado se convierte en «aceptado» o «integrado» por terminar el workflow.

## Cola por prioridad y sin duplicación

1. El coordinador recoge la PR #1 y el informe parcial Q1-028/Q1-032 del piloto.
   Registra su naturaleza documental, el SHA d032691 y sus límites. Ese contraste
   apoya D3-R4 y no repite ni reemplaza la revisión D3 completa ya registrada.
2. El coordinador lee la auditoría audit-pilot-code-001, verifica sus hallazgos y
   devuelve al autor únicamente lo afectado. La automatización continua con gasto
   no se considera desplegada hasta tener un resultado revisado.
3. Mistral A termina G-RAIZ si sigue sin respuesta y responde solo lo que deje
   abierto la revisión de A3. El inventario de A3 ya entregado no se reinicia.
4. Mistral D responde D3 sobre su HEAD vigente con invariantes generales, no solo
   las sondas literales: todas las rutas e id antes de mutar, evidencia del producto,
   reevaluación real y relevos completos. No hay casos completos Qwen por ello.
5. Mistral E responde E2; conserva lo cerrado en E1. Mistral F responde F3 y alinea
   el contrato C con el código/U3. No mantener contratos incompatibles.
6. El coordinador sigue mejoras del manual, CONTINUIDAD y tareas técnicas
   independientes. T-TRASPASO conserva sus límites y no acredita pasos con agentes.

Si aparece una entrega posterior, fijar su SHA y revisar el diff antes de reiterar
un encargo. No se pisan ramas de otros autores. Cada autor publica checkpoint,
pruebas realmente hechas y recuperación. Ninguno espera globalmente a todos.

## Comprobación de ChatGPT

Se prepara una tarea de comprobación horaria, independiente del proceso API.
Su estado real solo es ACTIVA si la herramienta de tareas lo confirma. La
programación no implica que ya haya corrido con éxito. Compara los HEAD del
producto/auxiliar y el control común. Actualiza exclusivamente su fichero propio
automation/coordination/observations/ESTADO_CHATGPT.json en esta rama; no CONTROL.
Notifica cambios sustantivos o un bloqueo real, no cada hora sin novedades.
No despierta las ventanas privadas y no gasta créditos de Anthropic/Mistral.

## Conexión de Mistral pendiente

Vibe CLI es la vía oficial para scripting/CI; Vibe Code Web no ofrece modo
desatendido según la documentación. Hace falta conectar la clave de Code > Vibe CLI
en esta cuenta y probar identidad/plan/límites antes de declarar un enlace activo.
No se comparten claves en chats. No se presupone que una clave de plan equivalga
a la de Studio. No se programa un agente escritor ni se ejecutan D3/E2/F3 por API
sin probar esta conexión y el aislamiento de cada tarea.

## Aceleración: medición, no promesa

Registrar por bloque: publicación, inicio de revisión, fin de revisión, corrección,
aceptación e integración; consumo de tokens/modelo, comandos ejecutados y reabiertos.
Medir la espera y el retrabajo que se eliminan antes de calcular ahorro global.
El piloto de dos casos (dos inferencias y postprocesamiento, USD 0,164726 estimados)
no mide velocidad de desarrollo ni coste de terminar el personaje.
Más concurrencia no consigue datos privados ni demuestra validez económica.

## Límites que se conservan

E1/D3/E2/E6, C48=108, C49=128,1 y FCF base=307,933. Elis pendiente_de_datos.
No se elige R, theta, lambda, k, probabilidades o umbrales. U2 exige historia previa
de Ahold si existe; U3 exige documentos accesibles y selección fundada. No se
inventa la historia que falta ni se fuerza B o C. No se fusiona main ni se publica
aptitud para dinero real. Mantener entregado/revisado/integrado/probado separados.

## Fuentes de interfaz y coste verificadas

- https://docs.mistral.ai/vibe/code/cli/install-setup
- https://docs.mistral.ai/vibe/code/cli/api-keys-profiles
- https://docs.mistral.ai/vibe/code/cli/work-with-cli
- https://docs.mistral.ai/vibe/code/choose-cli-vscode-web-sessions
- https://platform.claude.com/docs/en/models/overview
- https://platform.claude.com/docs/en/build-with-claude/structured-outputs
