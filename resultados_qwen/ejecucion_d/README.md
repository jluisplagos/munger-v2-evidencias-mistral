# Ejecución D · aceptación del banco Qwen Q1 v2 contra Munger V2

Frente D del encargo `revision_externa/seguimiento_20261116/ENCARGO_MISTRAL_D_QWEN.md`.
Candidata fijada: `jluisplagos/munger-v2@957af652cdc3bef3d67e8623c9572138bac685e9` (rama `claude/hopeful-bardeen-qap6y0`).
Banco normativo: `resultados_qwen/q1_v2/banco_revisado/` en `revision/qwen-q1-v2@4745f3887f7fd86bb3052f5d5e32285862df18e3`.

## Reproducción (lo automatizado)

```bash
# 0. entorno (una sola vez; descarga el ZIP base-4.14 una vez y lo verifica)
bash scripts/preparar_entorno.sh

# 1. ejecutar los casos con especificación ejecutable (piloto del bloque 1)
bash scripts/ejecutar_todo.sh
# o caso a caso:
python3 scripts/ejecutar_caso.py scripts/especificaciones/piloto/Q1-001.json

# 2. regenerar la matriz de los 36 casos
python3 scripts/generar_matriz.py
```

Variables de entorno: `CANDIDATA_DIR` (copia de trabajo del producto, por defecto `/workspace/base_414_main`),
`BANCO_DIR` (copia del banco, por defecto `/workspace/banco_q1_v2/resultados_qwen/q1_v2/banco_revisado`),
`RUN_DIR` (directorio de expedientes de prueba aislados, por defecto `/workspace/ejecucion_d_run`).

Cada caso copia el expediente plantilla del producto (`empresas_v2_correcciones/2026-11_Vidrala_ensayo_4_13/viscofan/Viscofan`)
a un directorio limpio, materializa los fixtures como fuentes locales con marcas `[PDF PAGE n]`, escribe el
registro `verificacion_entradas.json` y ejecuta los **comandos documentados del producto**
(`verificacion_entradas.py plantilla|comprobar --json|sellar`, `ficha.py`, `informe.py`) sobre esa copia.
Todo comando ejecutado queda con exit/stdout/stderr en `evidencias/<caso>/ejecucion.log` y los JSON en `evidencias/<caso>/`.
El producto no se modifica: solo se leen sus scripts; todo se escribe en copias aisladas.

## Requisitos y límites

- Python 3.12 con openpyxl, lxml, pypdf, jsonschema. **Sin LibreOffice ni pdftotext** en este entorno
  (sin root): el pipeline completo con recálculo de libros no corre aquí; se ejecutan las vías del producto
  que no necesitan recálculo (registro de entradas, ficha, informe, lógica de cierre vía ficha.py).
- No hay runtime de agente LLM del producto en esta sesión: las partes de personaje (entrada del usuario,
  fases A/B/C, auditoría) quedan como **relevo supervisado** (`RELEVO_SUPERVISADO.md`), no se simulan.
- Los fixtures sintéticos se materializan como fuentes de prueba; no se presentan como expedientes reales
  ni como auditorías auténticas. Los revisores del arnés se declaran como tales ("de prueba D").
- Estado inicial conocido del banco: 0/36 contra el producto. Esta ejecución no declara aptitud para dinero real.

## Contenido

- `CONFIGURACION.json`: SHA de producto y banco, entorno, alcance de la copia materializada.
- `MATRIZ_EJECUCION.csv`: 36 filas, una por caso, con estado y veredicto separados.
- `scripts/`: arnés (lib_arnes.py, ejecutar_caso.py, generar_matriz.py, preparar_entorno.sh, ejecutar_todo.sh) y especificaciones.
- `evidencias/`: logs y observables acotados por caso (sin XLSX/PDF/ZIP originales).
- `HALLAZGOS.md`, `RELEVO_SUPERVISADO.md`, `RESUMEN_PARA_INTEGRADOR.md`, `PUNTO_DE_RECUPERACION.md`, `MANIFIESTO_SHA256.txt`.
