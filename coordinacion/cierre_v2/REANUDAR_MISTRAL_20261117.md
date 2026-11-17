# Reanudación de las sesiones Mistral · 17-nov (sin ChatGPT)

Hay que pegar cada bloque en su sesión Mistral. Repositorio: `jluisplagos/munger-v2-evidencias-mistral`. Antes de empezar, cada sesión consulta el remoto y conserva cualquier trabajo posterior. Reglas comunes:

- Se escribe solo en la propia rama, con un commit por punto y un ENTREGA.json generado (comandos y códigos de salida, sondas, entradas que cambian de estado).
- No se toca producto, main, `coordinacion/cierre-v2` ni CONTROL o ESTADO.
- Nadie se autoaprueba ni afirma aptitud económica.
- No se cambian fuentes ni huellas. No se eligen R, θ, λ, k, probabilidades ni umbrales.
- Si un punto depende del runtime del coordinador o de una decisión del usuario, se publica el relevo exacto en vez de inventar el éxito.
- El coordinador (Claude) revisa con un contexto distinto y solo lo afectado.

## 0 · Si la sesión es nueva (se cerró la ventana anterior)

Pega esto primero y, a continuación, el bloque de tu frente:

> Trabajas en el programa de cierre de Munger V2. Repositorio GitHub `jluisplagos/munger-v2-evidencias-mistral`. Tu memoria está en GitHub, no en esta conversación. Clona el repositorio o consúltalo y lee, en este orden:
> 1. En la rama `coordinacion/cierre-v2`, `coordinacion/cierre_v2/`: LEEME.md, PROGRAMA.md, INTEGRACION.md, ESTADO.md, el `PROMPT_MISTRAL_<tu frente>.md` y este archivo (REANUDAR_MISTRAL_20261117.md).
> 2. En tu rama de trabajo, `PUNTO_DE_RECUPERACION.md` y `RESUMEN_PARA_CLAUDE.md` de tu carpeta de resultados, más el último commit.
>
> Antes de escribir nada, resume en 5 líneas el estado de tu frente y la corrección que te toca. Después trabaja sobre el último commit de tu rama, sin rehacer lo ya cerrado.

Frentes, ramas y carpetas:
- D: `mistral/d-qwen-aceptacion`, `resultados_qwen/ejecucion_d/`.
- A: `mistral/m2-cobertura-vm`, `resultados_m2/cobertura_vm/`; G-RAIZ en `mistral/g-manual-traspaso`, `resultados_cierre/manual_revision/`.
- E: `mistral/e-fuentes-elis`, `resultados_cierre/elis_fuentes/`.
- F: `mistral/f-alcance-real`, `resultados_cierre/alcance_real/`.
- R: rama nueva; no tiene prompt previo.

Desde hoy no hay contraste ChatGPT. Para conservar una mirada de otra familia de modelos, la sesión **Mistral R** (bloque 5) contrasta las revisiones del coordinador.

## 1 · Mistral D · prioridad máxima (desbloquea el personaje)

> Rama `mistral/d-qwen-aceptacion`, último commit d032691. Responde a `coordinacion/cierre_v2/revisiones_coordinador/D2_3934bc9_5f4b2a2/CORRECCION_D3.md` en el estado que fija `coordinacion/cierre_v2/revisiones_coordinador/D_d032691/ESTADO_D3_TRAS_d032691.md` (rama `coordinacion/cierre-v2`):
> - R6 y la regeneración están cerrados; consérvalos.
> - Cierra R1–R5 y R8, más las 7 variantes nuevas.
> - Prioriza R4: cada relevo (empezando por Q1-028 y Q1-032) necesita estado inicial, fases, un artefacto por criterio y un `comando_relevo` ejecutable. Un contraste documental de Claude API sobre d032691 confirmó ese hueco: `automatizacion/claude-api-piloto-registro`, `automation/claude_review/results/munger-d-relevos-002/postprocessed_report.md`.
> - Adapta los 36 casos sintéticos a vías que el producto soporte, con la correspondencia criterio→observable que exige el PLAN_DE_EJECUCION del banco.
> - El objetivo es un paquete con el que el coordinador ejecute los 36 casos del personaje con subagentes, sin interpretar nada. No ejecutes tú el personaje ni cuentes las respuestas a prompts como ejecución del producto.

## 2 · Mistral A

> Rama `mistral/g-manual-traspaso` y después `mistral/m2-cobertura-vm`.
> - Primero revisa G-RAIZ: `jluisplagos/munger-v2`, rama `integracion/hechos-raiz-957af65` @ 3d66437, sobre 957af65. Los criterios están en la `solicitud_revision` de G-RAIZ en `coordinacion/cierre_v2/CONTROL.json`. Es una revisión, no una corrección; publica el informe con sondas.
> - Después responde a `coordinacion/cierre_v2/revisiones_coordinador/A3_0946971/CORRECCION_A4.md` (A4-R1…R6) sobre 0946971. Ninguna entrada pasa a REVISADO sin todas sus dimensiones.

## 3 · Mistral E

> Rama `mistral/e-fuentes-elis`, último commit f00c5dd. Responde a `coordinacion/cierre_v2/revisiones_coordinador/E1_23718fb/CORRECCION_E2.md` (E2-D1…D9).
> - Los 11 PDF ya están preservados en la Release `fuentes-elis-e-20261117`.
> - M1, M2, M6 y N2 siguen abiertos y Elis sigue `pendiente_de_datos`.

## 4 · Mistral F

> Rama `mistral/f-alcance-real`, último commit 98bdf8f. Responde a `coordinacion/cierre_v2/revisiones_coordinador/F2_195766f_98bdf8f/CORRECCION_F3.md`, solo a lo que sigue abierto.

## 5 · Mistral R · contraste externo de las revisiones del coordinador (sustituye a ChatGPT)

> Rama nueva `revision/mistral-contraste-coordinador`. Eres un revisor de otra familia de modelos. No eres autor de nada de lo que revisas ni corriges las entregas de otros frentes.
> - Contrasta las revisiones publicadas por el coordinador en `coordinacion/cierre-v2`. Empieza por `revisiones_coordinador/AUTO_a508d6b/` y por la revisión del manual v2 cuando se publique. Después, cada revisión nueva (D3, A4, E2, F3) y la aceptación de los 36 casos del personaje.
> - En cada una comprueba:
>   - que los hallazgos se reproducen con sus sondas;
>   - que no se acepta nada sin evidencia;
>   - que no hay hallazgos falsos ni omitidos;
>   - que el control (CONTROL.json) refleja lo revisado.
> - Publica `CONTRASTE_<id>.md` con veredicto, discrepancias y sondas propias.
> - No lances inferencias de pago ni workflows.
