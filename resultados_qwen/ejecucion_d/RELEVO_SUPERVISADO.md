# Relevo supervisado · frente D · v2 (CORRECCION_D)

Nada de agente simulado: los registros de extractor/revisor del arnés están marcados como
**precondiciones simuladas** (D-R4). Lo que falta, con paquete exacto.

## Bloqueos de entorno (error concreto)

- Sin `soffice`: pipeline con recálculo del libro no corre. Sin `pdftotext`: Q1-026 —
  `cambiar_base.py preparar` exit 1, "«archivo» ausente o inexistente en texto/: 'AR_2021.txt'…".
  Paquete listo: `evidencias/Q1-026/CAMBIO_Q1-026.json` (caja 45.054→45.000 con evidencia v2;
  deuda 82.019 presente; deuda neta resultante 37.019). Se verificó que nunca sobrescribe.
- Sin runtime de agente LLM: extracción, fase A/B/C, verificación y auditoría (agente nuevo
  por solicitud SA-…) según `GUIA_RECORRIDO_SUPERVISADO.md`.

## Por caso pendiente

- **Q1-030 / Q1-035 (DECISION_PENDIENTE):** política del responsable (caducidad temporal;
  validación de motores). No ejecutar como obligación.
- **Q1-031 / Q1-033:** precio histórico etiquetado vs actual ausente en `fase1_v63.json`;
  requiere fase A/objetivo con agente. `precio_de_si.py --autotest` PASA vía entorno.
- **Q1-026:** con pdftotext+soffice: preparar CAMBIO, actualizar registro, recalcular
  dependientes, **auditoría nueva** del material final.
- **Q1-032 / Q1-036:** los recuentos 4/1/5 y 3/2/5 del fixture **no son observables** con el
  universo real (321 celdas; se observó 1/321 y 4/321 en parcial). No forzar universo reducido:
  preparar el relevo con un expediente de 5 entradas soportado o registrar NO_OBSERVABLE.
- **Q1-028:** la retirada de aprobación al cambiar material se observó (compartida con Q1-036);
  falta crear y aprobar una **nueva** de prueba por vías soportadas (agente auditor real).
- **Todos:** `entrada_usuario` íntegra del banco + fixtures como fuentes de prueba +
  observables mapeados a `verificacion_entradas.json`, `comprobar --json`, `estado_pipeline.json`,
  `ficha.json`/`informe.md`, `auditoria.md`.

## Reglas del relevo (del producto)

Agente por relevo con modelo/esfuerzo de la config; solo su salida; sin internet ni memoria;
sin pipeline/LibreOffice/Excel; fase C dos turnos con el mismo agente; auditoría con agente
nuevo; nunca copiar salidas entre expedientes reales.

## Paquetes por caso para el runtime del coordinador

`relevo/PAQUETES_RELEVO.json` (36 paquetes, generado por `scripts/generar_relevo.py` desde banco + evidencias + matriz): comando exacto de re-ejecución, criterios cubiertos por componente, entrada_usuario íntegra y lo que falta de agente/runtime/política por caso. Q1-026 incluye `paquete_runtime` (CAMBIO + pasos + artefactos esperados + bloqueo actual).
