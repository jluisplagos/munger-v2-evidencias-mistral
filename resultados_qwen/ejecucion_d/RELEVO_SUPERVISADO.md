# Relevo supervisado · frente D (bloque 1)

Casos o partes de casos que **no** se pueden ejecutar automáticamente en esta sesión y quedan preparados para un agente/persona. No se ha simulado ningún agente: no se ha respondido uno mismo los prompts del banco.

## Qué falta y por qué

- **Runtime de agente del producto:** el recorrido real (extracción V6.3, fase A, fase B, fase C ×2, verificación, auditoría del paso 13) lo resuelven agentes LLM con los prompts generados (`prompts_generados/NN_*.md`) según `GUIA_RECORRIDO_SUPERVISADO.md`. En esta sesión no hay canal de agente; además el pipeline completo necesita LibreOffice (recálculo del libro), ausente aquí.
- Por tanto, en **todos los casos** la parte "entrada_usuario pegada al personaje y respuesta completa" queda en relevo. Lo ejecutado es el componente mecánico real (registro de entradas, vigencia, salidas ficha/informe).

## Paquetes de relevo por caso (entrada exacta)

Para cada caso Q1-001…036: `entrada_usuario` íntegra de `banco_revisado/casos_aceptacion.jsonl`, los archivos de `archivos_sinteticos` materializados como fuentes de prueba (TXT/CSV/JSON, nunca como aprobaciones), y los observables pedidos en `criterios_observables` mapped a: `verificacion_entradas.json`, salida de `verificacion_entradas.py comprobar --json`, `estado_pipeline.json`, `ficha.json`/`informe.md` (oficiales solo tras auditoría APROBADO), `auditoria.md`, recuentos del resumen.

Casos con paquete específico preparado:

- **Q1-026:** CAMBIO.json (caja 95→90, evidencia f5_026_nota.txt v2, deuda 300 de la nota) → `python3 -I scripts/cambiar_base.py preparar CAMBIO.json` en copia nueva; después actualizar registro y **auditoría nueva** del material final (agente auditor distinto). Falta: ejecución con fase 1 completa + LibreOffice y la auditoría real.
- **Q1-028 / Q1-027 (aprobaciones):** tras el cambio de material, el pipeline repite paso 12 y pide auditoría nueva (I19); el auditor debe ser un agente nuevo que responda a la solicitud vigente (SA-…) con la línea `Material auditado: <id>`. Falta: agente auditor real.
- **Q1-031/033:** precio histórico vs actual en `fase1_v63.json` (fechas separadas); falta recorrido de fase A/objetivo con agente.
- **Q1-034/035:** decisiones de política (rango acotado; validación de motor) — responsable humano, no el banco.

## Reglas del relevo (del producto, no negociables)

Agente por relevo con el modelo/esfuerzo de la config; escribe solo su salida; sin internet ni memoria; no ejecuta pipeline ni LibreOffice; no abre Excel; fase C con el mismo agente dos turnos; cada auditoría con agente nuevo; nunca copiar salidas de otro expediente a uno real.
