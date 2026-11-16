# Relevo supervisado · frente D (cierre de la sesión)

No se ha simulado ningún agente: no se ha respondido uno mismo los prompts del banco. Lo que falta, con el paquete exacto.

## Bloqueos de entorno (con error concreto)

- **LibreOffice (`soffice`) ausente** (sin root en el sandbox): el pipeline con recálculo del libro (`recalc.sh`) no corre. Vías afectadas: recorrido completo del expediente, variantes calculadas, Q1-026 recálculo de dependientes.
- **`pdftotext` ausente:** los textos de los PDF de la base no se re-leen; `cambiar_base.py preparar` se detiene con "«archivo» ausente o inexistente en texto/: 'AR_2021.txt'…'AR_2024.txt'" (evidencia `evidencias/Q1-026/cambiar_base_preparar.txt`, exit 1). Paquete de relevo listo: `evidencias/Q1-026/CAMBIO_Q1-026.json` (corrección caja 45.054→45.000 con evidencia v2; deuda 82.019 presente; deuda neta resultante 37.019).
- **Sin runtime de agente LLM del producto:** extracción V6.3, fase A, fase B, fase C (2 turnos, mismo agente), verificación y auditoría (agente nuevo por solicitud SA-…) según `GUIA_RECORRIDO_SUPERVISADO.md`.

## Paquetes de relevo por caso restante

- **Q1-030 / Q1-034 / Q1-035 (DECISION_PENDIENTE):** decisión del responsable de política (caducidad temporal; tratamiento del rango acotado 0–200; validación de motores). No ejecutar como obligación.
- **Q1-031 / Q1-033:** precio histórico etiquetado vs precio actual ausente en `fase1_v63.json` (fechas separadas); requiere fase A/objetivo con agente real. El autotest `precio_de_si.py --autotest` pasó (PASA) vía `comprobar_entorno.sh`.
- **Q1-026:** con pdftotext+soffice: `python3 -I scripts/cambiar_base.py preparar CAMBIO_Q1-026.json` (copia nueva, origen intacto — verificado: no sobrescribe), actualizar registro de entradas de la copia, recalcular dependientes, **auditoría nueva** del material final (agente auditor distinto).
- **Q1-027/028 (aprobaciones):** tras cambiar material, el pipeline repite paso 12 y exige auditoría nueva (I19); el auditor responde a la solicitud vigente con `Material auditado: <id>`.
- **Todos los casos:** la `entrada_usuario` íntegra del banco + fixtures materializados como fuentes de prueba + observables mapeados a `verificacion_entradas.json`, `comprobar --json`, `estado_pipeline.json`, `ficha.json`/`informe.md`, `auditoria.md`.

## Reglas del relevo (del producto)

Agente por relevo con modelo/esfuerzo de la config; escribe solo su salida; sin internet ni memoria; no ejecuta pipeline ni LibreOffice; no abre Excel; fase C dos turnos con el mismo agente; cada auditoría con agente nuevo; nunca copiar salidas entre expedientes reales.
