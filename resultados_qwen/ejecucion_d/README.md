# Ejecución D · aceptación del banco Qwen Q1 v2 contra Munger V2 · v3 (respuesta D2 sobre 1ac661b)

Frente D del programa de cierre. Candidata fijada:
`jluisplagos/munger-v2@957af652cdc3bef3d67e8623c9572138bac685e9`.
Banco normativo: `resultados_qwen/q1_v2/banco_revisado/` en `revision/qwen-q1-v2@4745f3887f7fd86bb3052f5d5e32285862df18e3`
(extraído del SHA fijado, no de la punta de la rama).

## Reproducción

```bash
bash scripts/preparar_entorno.sh          # candidata 957af65 + base 4.14 verificada + banco @4745f38
bash scripts/ejecutar_todo.sh             # 28 casos + generar_matriz + generar_correspondencia + generar_relevo
python3 -B scripts/pruebas_arnes.py        # 16 pruebas del arnés (16/16 PASA) -> evidencias/pruebas_arnes.log
python3 -I sondas/sondas_d2.py . "$BANCO_DIR" sondas/sondas_d2.json   # sondas D2 (stubs): P1-P9 DETECTA
sha256sum -c MANIFIESTO_SHA256.txt        # exit 0
```

Variables: `CANDIDATA_DIR` (copia del producto), `BANCO_DIR` (nivel `banco_revisado`),
`RUN_DIR` (expedientes de prueba), `EVIDENCIAS_DIR` (por defecto `evidencias/` junto al arnés).

## Cómo se acredita un veredicto (v3)

- Especificación con `pasos` y `criterios.afirma` no vacíos; cada aserción se resuelve dentro de
  `evidencias/<caso>/` o de su RUN_DIR (`run:`); fuera → ERROR.
- `resultado_ejecucion.json` (harness 3.0) guarda `estado_caso`, criterios evaluados, artefactos
  con huella, `spec_sha256`, `candidata_sha` **observado**, `banco_casos_sha256` y la marca de
  precondiciones **simuladas** (`_simulada`/`[SIMULADO]` en cada registro escrito por el arnés).
- Una ejecución = evidencias limpias (un log por ejecución); el árbol de la candidata debe estar
  sin cambios sin commit y con el SHA esperado, o el caso sale ERROR_ENTORNO.
- `MATRIZ_EJECUCION.csv` y `evidencias/recuentos.json` se derivan solo de esas evidencias:
  CUMPLE exige criterios no vacíos todos CUMPLE_COMPONENTE **y** huella de spec coincidente
  (un resultado forjado no pasa). Sin evidencia no hay veredicto positivo; sin carpeta de
  evidencias, 36 filas y 0 CUMPLE con exit 0. `BLOQUEO_ENTORNO` (Q1-026) no cuenta como CUMPLE.
- `MAPA_CRITERIOS_BANCO.csv` mapea los 109 criterios observables del banco a aserciones del
  arnés o a «sin aserción» con su relevo. `relevo/PAQUETES_RELEVO.json` lleva los 36 paquetes
  con qué falta, quién lo hace y qué necesita, más el recorrido del personaje (fases en orden).

## Requisitos y límites

- Python 3.12 con openpyxl, lxml, pypdf, jsonschema. Sin LibreOffice ni pdftotext en este
  entorno: el recálculo de libros no corre (Q1-026 queda BLOQUEO_ENTORNO con paquete listo y
  errores de bloqueo separados); la capa de agente del personaje queda en
  `RELEVO_SUPERVISADO.md` / `relevo/`. Las sondas de `sondas/` usan stubs y miden la lógica
  del arnés, no el producto.
- Estado inicial del banco: 0/36 contra el producto; no se declara aptitud para dinero real.

## Contenido

- `CONFIGURACION.json`, `MATRIZ_EJECUCION.csv` (36 filas), `MAPA_CRITERIOS_BANCO.csv` (109),
  `scripts/` (arnés v3 + especificaciones + pruebas + sondas D2), `evidencias/` (por caso:
  log único por ejecución, JSON de control, resultado_ejecucion.json; recuentos.json;
  pruebas_arnes.log), `relevo/PAQUETES_RELEVO.json`, `sondas/sondas_d2.{py,json,stdout}`,
  `HALLAZGOS.md`, `RELEVO_SUPERVISADO.md`, `RESUMEN_PARA_INTEGRADOR.md`, `RESPUESTA_D2.md`,
  `PUNTO_DE_RECUPERACION.md`, `MANIFIESTO_SHA256.txt` (sin pycache).
