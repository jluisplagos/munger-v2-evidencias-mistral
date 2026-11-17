# Punto de recuperación — revisión G-RAIZ (3d66437)

- **Rama**: `mistral/g-manual-traspaso` (worktree `/workspace/wt-g` en la sesión)
- **Entrega anterior de esta rama**: `a0524d9` (revisión G-DOCS, aceptada por el coordinador en `289c796`); antes `78ba1ca` (G-MANUAL). Conservadas intactas.
- **Esta entrega**: subcarpeta `resultados_cierre/manual_revision/revision_graiz_3d66437/` (informe + sondas + criterios + ENTREGA + manifiesto). Un solo commit encima de `a0524d9`.
- **Objeto revisado (solo lectura)**: `jluisplagos/munger-v2` rama `integracion/hechos-raiz-957af65` @ `3d66437e797b6b0bf137b42fa62b561f39121722`, base `957af652cdc3bef3d67e8623c9572138bac685e9`.
- **Control vigente consultado**: `origin/coordinacion/cierre-v2` @ `30c314c3210c7f8eda5c3b632d98ce55fafef9db` (G-RAIZ solicitud LISTA).
- **Para reproducir las sondas**: `cd resultados_cierre/manual_revision/revision_graiz_3d66437/sondas && sh s01…s06*.sh` (usan `gh api` de solo lectura; las salidas quedan en `*.out`). Los archivos descargados van a un `mktemp -d` (no versionados); los hashes quedan fijados en `s02.out`.
- **Veredicto**: CONFORME CON LÍMITES en los 3 criterios. Nada integrado en el producto; la aceptación es del coordinador.
- **Siguiente paso previsto**: A4 (CORRECCION_A4.md, A4-R1…R6) en `mistral/m2-cobertura-vm` desde `0946971`, en worktree separado (`/workspace/wt-a`).
- **Entorno declarado**: modelo `mistral-large-4-0`; herramientas `gh api`, `sh`, `diff`, `sha256sum`, `grep`, `python3`; nada del producto ejecutado (sin LibreOffice ni pipeline).
- **Fecha**: 2026-11-17 UTC.
