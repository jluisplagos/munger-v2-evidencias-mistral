# Punto de recuperación · revisión G-DOCS (relevo Mistral A/G)

- Rama: `mistral/g-manual-traspaso` (worktree `/workspace/wt-g`), base `78ba1ca` (revisión G-MANUAL aceptada con límites, conservada intacta en `resultados_cierre/manual_revision/`).
- Trabajo hecho: revisión independiente de G-DOCS sobre el producto `jluisplagos/munger-v2`, rama `integracion/docs-operativos-957af65` @ `c0542b83` (padre `957af65`), solo lectura vía `gh api`. Veredicto: **CONFORME CON LÍMITES** en los 4 criterios (ver `INFORME_REVISION_GDOCS.md`, `verificacion_criterios.json`). Publicada en `resultados_cierre/manual_revision/revision_gdocs_c0542b8/` con sondas s01–s06 (+ `.out` + 4 diffs), ENTREGA.json, MANIFIESTO_SHA256.txt.
- Ejecutado realmente: `gh api` (lectura), `sh s01..s06`, `diff`, `sha256sum`, `grep/sed`. **No ejecutado:** nada del producto (sin verificar_paquete.sh, LibreOffice, pipeline, agentes).
- Estado del control: `coordinacion/cierre-v2` @ `57b34a60` (HEAD remoto, sin cambios posteriores sobre `coordinacion/cierre_v2`); G-DOCS estaba ENTREGADO/PENDIENTE de revisión (commit_revisado null) → este informe la responde. G-MANUAL ya aceptada (78ba1ca) — no repetida. T-TRASPASO lanzado por Claude con otro receptor (788f25c) — no duplicado.
- Rama A intacta: `mistral/m2-cobertura-vm` @ `8b88fab` en worktree `/workspace/wt-a` (limpio).
- Siguiente acción exacta: commit+push de esta carpeta en `mistral/g-manual-traspaso`; después, en `/workspace/wt-a`, leer `coordinacion/cierre_v2/revisiones_coordinador/A2_8b88fab/CORRECCION_A3.md` y `REVISION_A2_8b88fab.md` (vía `git show origin/coordinacion/cierre-v2:…`) y responder A3-R1…R8 en `resultados_m2/cobertura_vm/` con commit por punto.
- Modelo: `mistral-large-4-0`; consumo no visible. Sin escribir en CONTROL/ESTADO ni en el producto.
