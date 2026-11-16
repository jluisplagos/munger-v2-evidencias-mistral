# Punto de recuperación · rama mistral/f-alcance-real · bloque F-REV

- **Base de la rama**: `ff0c60c` (paquete de coordinación `coordinacion/cierre_v2`, contiene el encargo
  `ec707a5ba2bd684381a63ce0f6f6c143aa59f4c0`). Rama creada desde ese commit; escribe solo en
  `resultados_cierre/alcance_real/`.
- **Bloques F-REV (Cola 1)**: (1) contraste de F1 W1–W3 @ `d519eb0` (base `716cbd6`): CUMPLE los 4
  criterios, sin defecto material. (2) contraste de **C20 (U1–U6 del verificador) @ `bf0d5c2`**
  (base `d519eb0`): **CUMPLE los 5 criterios**, sin defecto material; rerun propio de las 752 filas
  (736/752 byte-idénticas, 0 diferencias en tabla; 16 filas texto solo por falta de poppler raw en el
  sandbox) + sondas U1–U6 sobre ambas versiones del código + end-to-end en páginas exportadas
  hash-ligadas. Evidencias en `revisiones_claude/` + `evidencias/c20/`.
  Nada adoptado; producto/libros/candidata intactos; frente C (`mistral/m2-matematica-b` @ 1ec4f18) intacto.
- **Estado de las colas tras consultar CONTROL.json** (`git fetch origin coordinacion/cierre-v2`):
  - Cola 1: F-REV (W1–W3) y C20 hechos por mí (informes en `revisiones_claude/`). CSV sigue
    **POR_PREPARAR** → pendiente. Siguiente independiente: **B-PM1 @ daa7478** (contraste documental
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
