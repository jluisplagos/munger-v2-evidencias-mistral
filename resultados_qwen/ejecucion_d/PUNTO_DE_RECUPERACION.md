# Punto de recuperación · frente D · v3 (respuesta D2-R1…R7 sobre 1ac661b)

- Rama: `mistral/d-qwen-aceptacion` (auxiliar). Base revisada: `1ac661b`; bloques de esta
  respuesta: arnés v3 + specs + generadores (ver `git log`).
- Producto (solo lectura): `claude/hopeful-bardeen-qap6y0` @ `957af652cdc3bef3d67e8623c9572138bac685e9`;
  copia `/workspace/base_414_main` (main `d69d483` + base 4.14 materializada, ZIP sha256
  `bb51942c…7b93e`, verify complete=true 6798/6798; checkout 957af65, 0 cambios sin commit).
- Banco: `revision/qwen-q1-v2` @ `4745f3887f7fd86bb3052f5d5e32285862df18e3`, extraído con
  `git archive` del SHA fijado; `BANCO_DIR` = `.../resultados_qwen/q1_v2/banco_revisado`.
- Reproducir: `bash scripts/preparar_entorno.sh && bash scripts/ejecutar_todo.sh &&
  python3 -B scripts/pruebas_arnes.py && python3 -I sondas/sondas_d2.py . "$BANCO_DIR" sondas/sondas_d2.json &&
  (cd resultados_qwen/ejecucion_d && sha256sum -c MANIFIESTO_SHA256.txt)`.
- Estado: 29/36 PARCIAL_COMPONENTE CUMPLE · 1 BLOQUEO_ENTORNO (Q1-026) · 6 NO_EJECUTADO ·
  2 DECISION_PENDIENTE (Q1-030/Q1-035) · **0/36 casos completos del personaje**;
  arnés 16/16 PASA; sondas D2 P1–P9 DETECTA; mapa 109 criterios (59 con aserción).
- Siguiente comando exacto (reanudar desde contexto limpio): el de «Reproducir» de arriba.
- Runtime del coordinador: ejecutar `relevo/PAQUETES_RELEVO.json` (36 paquetes) con agentes
  reales y registrar SHA por ejecución. Detalle por punto D2-R1…R7 en `RESPUESTA_D2.md`.
- Expedientes de prueba: `/workspace/ejecucion_d_run/<caso>/` (incl. `pruebas_d/` de Q1-026,
  bajo RUN_DIR; la candidata queda limpia). Sin secretos; sin pycache en el manifiesto.
