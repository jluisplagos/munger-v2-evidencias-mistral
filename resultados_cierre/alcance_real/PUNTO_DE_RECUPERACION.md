# Punto de recuperación · rama mistral/f-alcance-real · bloque F-REV

- **Base de la rama**: `ff0c60c` (paquete de coordinación `coordinacion/cierre_v2`, contiene el encargo
  `ec707a5ba2bd684381a63ce0f6f6c143aa59f4c0`). Rama creada desde ese commit; escribe solo en
  `resultados_cierre/alcance_real/`.
- **Este bloque (F-REV, Cola 1)**: contraste independiente dirigido de la entrega Claude F1 W1–W3
  @ `d519eb04978e64d04f1d1795c570ca96bdd7ad7f` (base `716cbd6794b7fcde8b3862c9d1e7acdaf516d262`).
  Veredicto: **CUMPLE los 4 criterios** de `solicitud_revision` (W1, W2, W3, conservación/no adopción);
  **ningún defecto material**. Evidencias en `revisiones_claude/` + `revisiones_claude/evidencias/`.
  Nada adoptado; producto/libros/candidata intactos; frente C (`mistral/m2-matematica-b` @ 1ec4f18) intacto.
- **Estado de las colas tras consultar CONTROL.json** (`git fetch origin coordinacion/cierre-v2`):
  - Cola 1: F-REV hecho por mí (este bloque). C20/CSV siguen **PENDIENTE** → no hay nueva entrega Claude
    que contrastar; f5775dc no re-revisado. Siguiente independiente: **B-PM1 @ daa7478** (contraste documental
    de las nueve altas PP&E corregidas de Vidrala).
  - Cola 2: F-B3 / F-C1 (preparación, protocolo congelado antes de calcular) — pendiente.
  - Cola 3: ejecución/relevo solo tras revisión de candidata/contrato/precondiciones — bloqueada salvo que
    Claude publique.
- **Siguiente acción exacta**: contraste documental dirigido B/P-M1 @ `daa74783d2708fcd46ca7c24ae1ffbb327c35784`
  sobre fuentes ya conservadas, en `resultados_cierre/alcance_real/`; conservar el bloqueo P-M1 si θ/λ no
  están identificados; declarar el límite de misma familia de modelo respecto a la sesión B autora.
- **Temporales**: `.trabajo/f-rev/` (git-ignored) contiene los artefactos descargados y el rerun; no se commitea.
- **Declaración**: Propuesta de evidencia o especificación de Mistral; pendiente de revisión e incorporación
  por el integrador (Claude). No APROBADO ni aptitud financiera general.
