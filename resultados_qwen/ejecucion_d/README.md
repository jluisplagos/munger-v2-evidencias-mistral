# Ejecución D · aceptación del banco Qwen Q1 v2 contra Munger V2 · v2 (CORRECCION_D)

Frente D del encargo `ENCARGO_MISTRAL_D_QWEN.md`, corregido según
`revision_externa/a_d_20261116/CORRECCION_D.md` (base revisada `b42f453`).
Candidata fijada: `jluisplagos/munger-v2@957af652cdc3bef3d67e8623c9572138bac685e9`.
Banco normativo: `resultados_qwen/q1_v2/banco_revisado/` en `revision/qwen-q1-v2@4745f3887f7fd86bb3052f5d5e32285862df18e3`.

## Reproducción (lo automatizado)

```bash
bash scripts/preparar_entorno.sh          # verifica SHA de candidata y banco en ejecución
# deja exportado: CANDIDATA_DIR=... BANCO_DIR=.../banco_revisado RUN_DIR=...
bash scripts/ejecutar_todo.sh             # 28 casos; exit != 0 si alguno no queda COMPONENTE_OK
python3 -B scripts/pruebas_arnes.py        # 8 pruebas del propio arnés (deben dar 8/8 PASA)
python3 scripts/generar_matriz.py          # deriva MATRIZ_EJECUCION.csv SOLO de evidencias validadas
```

Variables: `CANDIDATA_DIR` (copia del producto), `BANCO_DIR` (**nivel `banco_revisado`**, el que
contiene `casos_aceptacion.jsonl`; el preparador lo fija así), `RUN_DIR` (expedientes de prueba),
`EVIDENCIAS_DIR` (dónde escribe el arnés; por defecto `evidencias/` junto al arnés).

## Cómo se acredita un veredicto (v2)

- Cada especificación declara `esperado` (exits válidos; los rechazos esperados como
  `sellar` exit 1 o `ficha.py` oficial exit 3 se declaran y no son fallo) y `criterios`
  con aserciones sobre los JSON/artefactos producidos.
- `resultado_ejecucion.json` (harness 2.0) guarda `estado_caso` (COMPONENTE_OK /
  COMPONENTE_FALLA / ERROR / ERROR_ENTORNO), los criterios evaluados, los artefactos
  copiados con su huella y la marca de precondiciones **simuladas** de extractor/revisor.
- Las salidas heredadas del expediente plantilla se archivan en `_heredados/` antes de
  ejecutar; un artefacto solo se copia si su comando productor terminó con exit esperado
  y su sha256 difiere del heredado.
- `MATRIZ_EJECUCION.csv` y `evidencias/recuentos.json` se derivan solo de esas evidencias
  (fuente única): sin evidencia no hay veredicto positivo. Se distingue `veredicto_componente`
  (CUMPLE = lo ejecutado por el arnés) de `veredicto_caso` (el caso completo queda sin
  veredicto si falta algún criterio, p. ej. la capa de agente).
- Observaciones compartidas (Q1-028/Q1-032 sobre Q1-036) se declaran en la matriz y no
  se cuentan como ejecución propia. Q1-032/Q1-036: el recuento 1/321 del universo real no
  prueba 4/1/5 ni 3/2/5; queda registrado como no observable y en relevo.

## Requisitos y límites

- Python 3.12 con openpyxl, lxml, pypdf, jsonschema. Sin LibreOffice ni pdftotext en este
  entorno (sin root): el pipeline con recálculo no corre aquí (Q1-026 bloqueado por ello,
  error exacto conservado); la capa de agente del personaje queda en `RELEVO_SUPERVISADO.md`.
- Los fixtures se materializan como fuentes de prueba; no son expedientes reales ni
  auditorías auténticas. Estado inicial del banco: 0/36 contra el producto; no se declara
  aptitud para dinero real.

## Contenido

- `CONFIGURACION.json`, `MATRIZ_EJECUCION.csv` (36 filas), `scripts/` (arnés v2 + especificaciones + pruebas),
  `evidencias/` (por caso: log, JSON de control, resultado_ejecucion.json; `recuentos.json`;
  `pruebas_arnes.log`), `HALLAZGOS.md`, `RELEVO_SUPERVISADO.md`, `RESUMEN_PARA_INTEGRADOR.md`,
  `PUNTO_DE_RECUPERACION.md`, `MANIFIESTO_SHA256.txt` (sin pycache).
