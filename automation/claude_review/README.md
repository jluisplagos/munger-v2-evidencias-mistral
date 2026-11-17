# Piloto de revisión documental con Claude API

Este piloto entrega **una revisión asistida y parcial** de los relevos Q1-028 y
Q1-032 publicados por Mistral D. No es un coordinador autónomo de las tres
plataformas. No ejecuta el personaje ni sus pruebas, no acepta entregas, no
modifica CONTROL/ESTADO y no escribe en el repositorio producto.

## Estado de arranque

- Rama aislada: `automatizacion/piloto-claude-api`, desde el main del auxiliar.
- `request.json` empieza en `mode: dry-run`: recopila los textos reales fijados,
  prepara el informe y **no llama a Anthropic**.
- Las pruebas usan respuestas ficticias, claramente separadas de la ejecución
  real. Que pasen no acredita que la API o el crédito promocional ya funcionen.
- La ejecución real requiere configurar la credencial y cambiar a `mode: api`
  en un commit de esta rama. No hay reloj, bucle de espera ni ejecución periódica.
- Cada revisión posterior requeriría otro diseño/encargo: este piloto tiene un
  identificador único y no permite una segunda llamada cobrable.

## Qué entrega

1. Lee cuatro fuentes del auxiliar en SHA completos fijados. Del JSON de los 36
   paquetes incluye solo Q1-028 y Q1-032 y sus metadatos; declara los casos omitidos.
2. Conserva tamaño y SHA256 del original y huella de la representación incluida.
   No trunca silenciosamente: un paquete excesivo bloquea la ejecución.
3. En modo API, comprueba acceso al modelo y cuenta tokens antes de reservar.
4. Reserva el piloto de forma durable en una rama separada **antes** de la llamada.
5. Hace una sola petición Messages, sin herramientas y sin reintentos automáticos.
6. Valida el JSON recibido y las citas literales contra las fuentes incluidas.
   Una cita literal no acredita por sí misma una interpretación correcta.
7. Publica paquete, informe y reserva en
   `automatizacion/claude-api-piloto-registro`, bajo
   `automation/claude_review/results/munger-d-relevos-001/`.
   El informe siempre lleva `accepted:false`, `integrated:false` y
   `product_executed:false`. Lo revisa el coordinador.

El modelo no recibe credenciales, no dispone de herramientas y su salida no se
ejecuta. Tampoco se ejecutan scripts de las entregas de Mistral. Su texto se trata
como dato, aunque contenga instrucciones.

## Conectar la cuenta (única intervención con una credencial)

En el repositorio auxiliar, una persona con permiso para gestionar secretos debe
crear este secreto de Actions:

- Nombre: `ANTHROPIC_API_KEY`
- Valor: una clave de la organización/workspace de Claude Console que contiene
  el crédito promocional. No pegarla en el chat, commits o issues.

Acceso directo:
https://github.com/jluisplagos/munger-v2-evidencias-mistral/settings/secrets/actions/new

No se requiere instalar la aplicación Claude GitHub: usamos la API directamente.
El `GITHUB_TOKEN` temporal de Actions permite publicar solo en este repositorio.
La elegibilidad efectiva del modelo/crédito se comprueba al ejecutar; el informe
de tokens **no** permite saber si el proveedor descontó saldo promocional o
comprado. Eso se confirma en Claude Console.

Después de guardar la clave, cambiar únicamente `mode` de `dry-run` a `api` y
publicar el commit en `automatizacion/piloto-claude-api`. El evento push ejecuta
el workflow, incluso sin fusionar main. No cambiar SHA de fuentes para este ensayo.
El botón workflow_dispatch puede requerir que el workflow haya sido registrado
o exista en la rama predeterminada; no se depende de él ni se fusiona main para
activar este piloto.

## Consumo y duplicados

- Modelo de ensayo: `claude-sonnet-5-5`, sin fallback automático.
- Tarifas estándar verificadas el 17-nov-2026: USD 2 / millón de entrada y
  USD 10 / millón de salida. No se solicita Priority, herramientas o caché.
- Máximo de salida: 4096 tokens.
- Se calcula una reserva conservadora desde el conteo y los bytes; el programa
  rechaza una reserva mayor de **USD 0,25**. No es una promesa de tarifa inmutable:
  la facturación y límites efectivos los administra Anthropic. Revisar las tarifas
  si se activa en otra fecha. Un límite del workspace en Console es un control
  adicional de cuenta, que este programa no modifica.
- La reserva es create-only: una carrera o relanzamiento no puede sobrescribirla
  para volver a llamar al modelo. También hay exclusión mutua de workflows.
- Un timeout puede haberse cobrado. Se guarda como resultado no aceptado e incierto
  y **no se reintenta**. Si la publicación final falla, permanece la reserva.
- El coste del informe se estima con los tokens devueltos y las tarifas fijadas;
  no se presenta como factura. Un consumo no previsto exige revisión.
- Los minutos/artefactos de GitHub Actions se rigen por el plan de GitHub y no por
  los créditos de Anthropic.

Sonnet se usa para comprobar este mecanismo documental. Este piloto no sustituye
las revisiones críticas ni las configuraciones de agentes del personaje.

## Pruebas reproducibles

Desde la raíz del checkout:

```bash
python3 -m unittest discover -s automation/claude_review -p test_pilot.py -v
python3 automation/claude_review/pilot.py \
  --request automation/claude_review/request.json \
  --output /tmp/munger-api-dry-run \
  --code-sha "$(git rev-parse HEAD)"
```

El segundo comando en el modo inicial lee GitHub y no llama a Anthropic. Si el
repositorio está sujeto a un límite de consultas públicas, puede usarse GH_TOKEN
del entorno; nunca escribir su valor en la orden. El CLI verifica los bytes del
script y de request.json frente al HEAD observado, incluso con skip-worktree.
La carpeta de salida se mantiene fuera del repositorio.

En GitHub, el workflow primero prueba sin API. Solo si pasa ejecuta la preparación
o la llamada, según el modo versionado. Publica resumen y artefacto también si el
resultado no fue aceptado. Los artefactos de prueba caducan a los 30 días; un informe
de API publicado se conserva en la rama de registro, sin PDF/XLSX/ZIP en Git.

## Operación y límites

- Único escritor del control global e integrador: Claude coordinador existente.
- El piloto escribe únicamente su rama de registro del auxiliar.
- No hay firmas, aprobaciones, adopción económica ni aptitud financiera implícita.
- Se conservan E1/D3/E2/E6, C48=108, C49=128,1, FCF base=307,933 y Elis pendiente.
- Un cambio de fuente no actualiza automáticamente este ensayo: sus SHA son fijos.
- Para desactivar, mantener `mode: dry-run`. Si ya se reservó, no borrar la reserva
  para reintentar una petición cuyo consumo sea incierto; revisar primero Console.
- No se incluyen tus conversaciones privadas. No despierta las ventanas actuales.

## Fuentes oficiales consultadas

- Modelos y precios: https://platform.claude.com/docs/en/models/sonnet-5-5/overview
- Precios: https://platform.claude.com/docs/en/about-claude/pricing
- Conteo previo (gratuito): https://platform.claude.com/docs/en/build-with-claude/token-counting
- Versión de API: https://platform.claude.com/docs/en/api/versioning
- Créditos: https://support.claude.com/en/articles/8977456-how-do-i-pay-for-my-claude-api-usage
- Eventos Actions: https://docs.github.com/en/actions/reference/workflows-and-actions/events-that-trigger-workflows
