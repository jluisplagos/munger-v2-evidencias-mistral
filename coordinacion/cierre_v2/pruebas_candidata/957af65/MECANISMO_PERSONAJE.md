# Mecanismo real de ejecución del personaje · candidata 957af65 · comprobación del coordinador (17-nov-2026)

**Alcance.** Comprobar con comandos cómo ejecuta el producto las fases de agente y qué necesita, antes de afirmar que pueden correrse los 36 casos Qwen (reanudación `c241a59`, §1.7). No se ha lanzado ningún agente ni se ha simulado ninguna respuesta. Esto no es uno de los 36 casos ni un expediente nuevo.

## 1. Lo que dice el producto

- `personaje_v2/scripts/pipeline.py:7-14`: los pasos de agente no se ejecutan dentro del pipeline:
  - paso 5, extracción;
  - paso 6, fase A;
  - paso 8, fase B;
  - paso 10, fase C en dos turnos;
  - paso 13, verificación.

  El pipeline deja el prompt en `prompts_generados/` y `ESPERANDO.md` y sale con **código 10**. Cuando existe la salida del agente, se vuelve a lanzar y continúa. `--agentes-simulados` solo vale para pruebas técnicas (`GUIA_RECORRIDO_SUPERVISADO.md:49`).
- La sesión que orquesta lanza un subagente por cada relevo, con el modelo y el esfuerzo de `config_v2.json → modelos` (`PROMPT_CLAUDE_CODE.md:28-31`; `GUIA_RECORRIDO_SUPERVISADO.md:45-49`):
  - extracción: sonnet, esfuerzo medio;
  - fases A, B y C: opus, esfuerzo alto;
  - verificación: opus, esfuerzo medio, con un agente **nuevo**;
  - la fase C, turno 2, la hace **el mismo agente** que el turno 1.
- **No hace falta ninguna API ni credencial:** el procedimiento soportado no la exige.

## 2. Capacidades de esta sesión, comprobadas

- Lanzar subagentes con un modelo elegido, en contexto separado: sí. Es la herramienta que usan las revisiones de este programa.
- Continuar el mismo agente para el turno 2 de la fase C: sí, con `SendMessage` a su id.
- Lanzar un agente nuevo para la auditoría: sí.
- LibreOffice 24.2.7.2 en secuencia (`flock -x`), pdftotext 24.02.0 y Python 3.13.18: sí. La verificación completa de la candidata pasó (`README.md` de esta carpeta).

## 3. Ensayo del mecanismo

- **Preparación:** una copia nueva del árbol materializado de 957af65. Réplica `empresas_v2/Rational_rep/` solo con las entradas, según el procedimiento de réplica (`PROMPT_CLAUDE_CODE.md:36`).
- **Comando:** `flock -x … python3 scripts/pipeline.py empresas_v2/Rational_rep`.
- **Resultado:** código **10** tras los pasos mecánicos 0–4, en 15 s. Espera al agente `extraccion_v63` (paso 5). El prompt indica `{"modelo": "sonnet", "esfuerzo": "medio"}` (`mecanismo_prompt_05_cabecera.txt`).
- **Registro:** `mecanismo_pipeline_Rational_rep.log`, con las rutas sustituidas por `<copia>`.
- **Límite encontrado:** los seis expedientes de `empresas_v2/` no conservan `pdf/` ni `texto/` en el árbol materializado. La extracción de una réplica de Rational no tendría fuentes y no se continúa. Los expedientes de decisiones de la 4.14 (Vidrala, Viscofan y Elis) sí conservan `texto/`; su regeneración es T-EXP.

## 4. Conclusión para los 36 casos Qwen (D-36)

- **No falta capacidad de agentes, configuración ni credenciales.**
- **Lo que falta es la adaptación.** El banco (`revision/qwen-q1-v2` @ `4745f38`, `PLAN_DE_EJECUCION.md` §2) define mini-expedientes sintéticos (fixtures TXT, CSV y JSON). Su propio plan exige prepararlos por las vías soportadas y mapear sus observables a los del producto antes de evaluar; sin eso, el resultado es ADAPTACION_PENDIENTE. Hoy no está:
  - qué expediente o paso del producto corresponde a cada caso;
  - qué entrada se carga;
  - qué fases se recorren;
  - qué artefacto se observa por criterio.

  Es D2-R4/R5 (relevos íntegros y correspondencia de los 109 criterios del banco con observables), encargado a Mistral D.
- **No se sustituye el producto por respuestas libres de subagentes.** Un caso se ejecuta cuando su relevo dice qué estado del producto preparar, qué pasos recorrer con agentes reales y qué artefacto mirar por criterio.
