# Punto de recuperación · frente D · v2 (CORRECCION_D)

- Rama: `mistral/d-qwen-aceptacion` (auxiliar), base revisada por CORRECCION_D: `b42f453`;
  HEAD de la corrección en el push de cierre (ver `git log`).
- Producto (solo lectura): `claude/hopeful-bardeen-qap6y0` @ `957af652cdc3bef3d67e8623c9572138bac685e9`
  (SHA verificado en ejecución por el arnés); copia `/workspace/base_414_main` (main d69d483 +
  base 4.14 materializada, ZIP sha256 `bb51942c…7b93e`, 6798/6798). Residuo local de prueba:
  `munger_v2_r1/pruebas_d/` (Q1-026), no commiteado.
- Banco: `revision/qwen-q1-v2` @ `4745f3887f7fd86bb3052f5d5e32285862df18e3`; `BANCO_DIR` =
  `/workspace/banco_q1_v2/resultados_qwen/q1_v2/banco_revisado` (nivel banco_revisado).
- Reproducir: `bash scripts/preparar_entorno.sh && bash scripts/ejecutar_todo.sh &&
  python3 -B scripts/pruebas_arnes.py && python3 scripts/generar_matriz.py`.
- Estado (bloque 1 del programa de cierre): 30/36 con ejecución propia COMPONENTE_OK;
  veredicto de componente CUMPLE en esos 30; veredicto de caso pendiente de agente en 29;
  1 NO_OBSERVABLE (Q1-026, bloqueo de entorno documentado con paquete restaurado),
  2 DECISION_PENDIENTE (Q1-030, Q1-035). Q1-027 cerrado con resultado (hueco b);
  paquete Q1-026 restaurado con procedencia verificable (hueco a).
- Siguiente comando exacto (reanudar desde contexto limpio):
  bash scripts/preparar_entorno.sh && bash scripts/ejecutar_todo.sh && python3 -B scripts/pruebas_arnes.py && python3 scripts/generar_matriz.py && python3 scripts/generar_relevo.py
- Runtime del coordinador: ejecutar relevo/PAQUETES_RELEVO.json (36 paquetes) con agentes reales y registrar SHA por ejecución.
- Expedientes de prueba: `/workspace/ejecucion_d_run/<caso>/Viscofan` + `_heredados/`.
- Sin secretos; sin pycache en el manifiesto.
