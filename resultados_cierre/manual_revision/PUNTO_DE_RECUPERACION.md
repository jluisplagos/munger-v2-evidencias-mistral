# Punto de recuperación · revisión G-MANUAL (Mistral A)

- Rama: `mistral/g-manual-traspaso` (worktree separado `/workspace/wt-gmanual-2df0cd`), base `cdec2f5dab654a9149ed510475feae3ed2f0662f` (control vigente con el manual; manual idéntico a `341831f`).
- Rama A intacta: `mistral/m2-cobertura-vm` @ `8b88fab28261506c60bc7631fd24894e225099d2` (respuesta A2 v4.0 entregada; rutas RESPUESTA_A2_CIERRE_V2.md / ENTREGA.json / COMANDOS.md confirmadas en ese SHA; pendiente de revisión por Claude — no repetir ni autoaprobar).
- Trabajo hecho: revisión documental de `MANUAL_OPERATIVO_957af65.md` + `CONTRADICCIONES_GUIA.md` (@341831f) contra producto @957af65 y auxiliar @9871f59, cinco criterios de la solicitud → **CONFORME CON LÍMITES** (ver `INFORME_REVISION_GMANUAL.md` y `verificacion_criterios.json`, 11 hallazgos CONFORME).
- Ejecutado realmente: `git show/ls-tree/diff` (lectura) + `python3 -B scripts/verificar_manual.py` (exit 0). **No ejecutado:** nada del producto (sin pipeline, sin LibreOffice, sin red, sin agentes); T-TRASPASO pendiente.
- Entrega: `INFORME_REVISION_GMANUAL.md`, `verificacion_criterios.json`, `scripts/verificar_manual.py`, `ENTREGA.json`, `MANIFIESTO_SHA256.txt`, este archivo — todo en `resultados_cierre/manual_revision/`.
- Siguiente acción exacta: el coordinador registra el informe en CONTROL.json (G-MANUAL `informe_revision`/`commit_revisado` = SHA remoto de esta rama), corrige textos desfasados en copia aislada de la candidata y prepara T-TRASPASO con receptor sin historial. Si Claude devuelve corrección sobre A2, atenderla después en `mistral/m2-cobertura-vm` desde `8b88fab`.
- Modelo: `mistral-large-4-0`; consumo no visible. Sin escribir en el control común ni en el producto.
