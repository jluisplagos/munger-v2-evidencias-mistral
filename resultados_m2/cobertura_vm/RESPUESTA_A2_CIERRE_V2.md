# Respuesta a CORRECCION A2 · Frente A M2 · cobertura VM (v4.0)

Propuesta de evidencia de Mistral; pendiente de revisión e incorporación por el integrador. No APROBADO.

## Encargo ejecutado

- Control común consultado: `git fetch origin coordinacion/cierre-v2` → `8b8c9c17481abfa3c5e94e8a7906b4bcc6897715`; leídos con `git show` (sin fusionar): `coordinacion/cierre_v2/revisiones_coordinador/A_2c41d68/CORRECCION_A2.md`, `REVISION_A_2c41d68.md`, sondas en `sondas/`. A-CTX = CORRECCIONES sobre `2c41d68` (regeneración de las entradas acreditadas con reglas defectuosas). Base de la corrección publicada: `9d676ce`.
- Rama: `mistral/m2-cobertura-vm`. Escritura solo en `resultados_m2/cobertura_vm/`. Sin PR, sin fusiones, sin tocar `main`/producto/otros frentes.

## A2-R1 · Columna estrictamente posicional — corregido (v4.0)

- `check_columna` mapea el valor por **posición** en la línea de columnas del encabezado. OK sin posición → NO_DECIDIBLE; años repetidos en la cabecera o valor repetido en la fila → NO_DECIDIBLE (salvo bloque identificado); valor ausente de la fila o posición que mapea a otra columna declarada → CONFLICTO.
- Sondas del revisor verificadas directamente: 2a → NO_DECIDIBLE, 2b → NO_DECIDIBLE, 2c → CONFLICTO, 2d (EPS 950 900) → CONFLICTO, 2e (columna de variación) → NO_DECIDIBLE, 2f → OK, 2g (sonda d375d80 #3) → CONFLICTO. Nota-ref `11.2` sigue en OK (no es grupo de 3 dígitos).
- Las entradas REVISADO con columna OK sin mapeo pasan a PENDIENTE (ver lista de cambios abajo).

## A2-R2 · Reexpresión reescrita (v4.0) — corregido

- Sin atajo de cita; la fila del original se elige por **rótulo completo** (no por prefijo); se compara misma fila, columna por posición, escala y perímetro.
- Toda declaración con «no» (no aplica / no reexpresado / igual al original) + diferencia → **CONFLICTO** (nunca OK); diferencia sin declaración documental → NO_DECIDIBLE; diferencias **solo de signo** en clase aparte (SOLO_SIGNO); afirmación + diferencia → OK.
- Sondas 3c–3h y 3j verificadas. Las 19 entradas comparadas con otra fila y las 44 solo-signo se regeneran (en la lista de cambios).
- **Control coherente con A2-R2**: `control_cobertura.py` ahora exige que el `estado_contextual` de cada derivado sea exactamente la propagación de sus orígenes (CONFLICTO se propaga); la regla antigua que rechazaba todo derivado con contexto CONFLICTO era incompatible con A2-R2 y se sustituye por la comprobación de propagación. Con v4.0: **PASS, 0 violaciones, exit 0**.

## A2-R3 · Escala — corregido (v4.0)

- La escala de la **página** manda sobre la cabecera del documento; millones (incl. «millones de euros») cuentan como escala contraria; `MILES_RE` («in thousands») solo acredita miles de **euros** (no miles de acciones). Sondas 4a/4b → CONFLICTO, 4c → NO_DECIDIBLE, 4e/4f → CONFLICTO, 4g → OK. Sin impacto negativo en datos reales (unidad 467/467 OK).

## A2-R4 · Años con límites de palabra — corregido (v4.0)

- `YEAR_RE = (?<![\d.,])20\d\d(?![\d.,])` (los importes 2045,3 / 0,2050 / 2025,4 ya no son año); `YEAR_FILE_RE` solo en nombres de archivo; la cabecera no se toma de líneas con importes (caso real Viscofan `Análisis!C37`, precios 0,2050 0,2095 0,2072); la versión no se acredita por un importe. Sondas 1b–1d verificadas.

## A2-R5 · Textos, comandos y versiones — corregido

- **Recuentos generados, no a mano**: nuevo `scripts/generar_recuentos_doc.py` → `resultados/RECUENTOS_VIGENTES.md` + bloque generado (marcadores) en `MAPA_REGENERACION.md`. Los recuentos desfasados de §v3 quedan sustituidos por el bloque generado.
- **Motivo corregido** de `aux:AR2025_p27_pagos_acciones_2024` (HALLAZGOS.md §11): CF_2024 p.9 imprime `2,001` en la **misma fila 414 y columna 2024**; en v4.0 la reexpresión queda OK como «no reexpresado» con igualdad confirmada.
- **`COMANDOS.md`** creado con los comandos exactos y versiones declaradas: Python 3.12.15, openpyxl 3.1.5, pypdf 7.1.0.
- **`asociacion_pdf.py`** declara y exige pypdf >= 6.0 (probado con 7.1.0) y falla con mensaje claro si la versión no basta o falta el paquete.

## Comandos realmente ejecutados y códigos de salida (v4.0, desde la raíz del auxiliar, `PYTHONPATH=$PWD/.trabajo/pylibs`, `python3 -B`)

| Comando | Exit |
|---|---|
| `python3 -B resultados_m2/cobertura_vm/scripts/verificar_contexto.py` | 0 |
| `python3 -B resultados_m2/cobertura_vm/scripts/derivaciones.py` | 0 |
| `python3 -B resultados_m2/cobertura_vm/scripts/construir_cobertura.py` | 0 |
| `python3 -B resultados_m2/cobertura_vm/scripts/control_negativo.py` | 0 (218 mutaciones: 149 ctx / 40 mec; **bilaterales 15/15 ok**; **sondas revisor 5/5 CONFLICTO**) |
| `python3 -B resultados_m2/cobertura_vm/scripts/control_cobertura.py` | **0 = PASS, 0 violaciones** (regla de propagación actualizada per A2-R2) |
| `python3 -B resultados_m2/cobertura_vm/scripts/cola_pendientes.py` ; `resolver_bloque2.py` ; `revisar_lote.py L00..L21` | 0 |
| `python3 -B resultados_m2/cobertura_vm/scripts/generar_recuentos_doc.py` | 0 |
| `python3 -B resultados_m2/cobertura_vm/scripts/generar_cambios_estado.py 9d676cefdfeb3771a43414fcb93f430e9340fae0 a2_v4` | 0 |
| `python3 -B resultados_m2/cobertura_vm/scripts/generar_manifiesto.py` (tras `rm -rf scripts/__pycache__`) | 0 |

Comandos exactos y versiones: `COMANDOS.md`.

## Sondas del revisor reproducidas (en `resultados/control_negativo.json` → `sondas_revisor`)

`euros_no_miles` → CONFLICTO · `escala_erronea_con_cabecera` → CONFLICTO · `columna_equivocada_aceptada` → CONFLICTO · `reexpresion_toma_otra_columna` → CONFLICTO · `contradiccion_reexpresion_devuelve_ok` → CONFLICTO — **5/5 detectadas (CONFLICTO)**, como exigía d375d80 y se conservaba. Sondas bilaterales A2/v3.1: **15/15 ok** (`bilaterales_ok: true`).

## Entradas que cambian de estado (anterior → nuevo), lista generada

`resultados/cambios_estado_a2_v4.json` (generada por `scripts/generar_cambios_estado.py` diffing `9d676ce` vs el árbol v4.0; no sustituye cifras ni fuentes):

- **230 fuentes** cambian de estado contextual: REVISADO→CONFLICTO 77 · REVISADO→PENDIENTE 135 · PENDIENTE→CONFLICTO 16 · PENDIENTE→REVISADO 2.
- **286 filas del CSV** (incluye la propagación a derivados): REVISADO→CONFLICTO 110 · REVISADO→PENDIENTE 151 · PENDIENTE→CONFLICTO 23 · PENDIENTE→REVISADO 2.
- Toda entrada que pierde acreditación queda PENDIENTE; las contradicciones documentadas quedan CONFLICTO. Ninguna cifra ni fuente sustituida para que pasen.

## Resultados vigentes (generados — `resultados/RECUENTOS_VIGENTES.md`)

- Fuentes (verificacion_contexto.jsonl, 677 entradas): **148 REVISADO / 183 PENDIENTE / 93 CONFLICTO / 43 REUTILIZADO_M1 / 210 NO_APLICA**.
- CSV 677 filas: **169 REVISADO / 209 PENDIENTE / 133 CONFLICTO / 60 REUTILIZADO_M1 / 106 NO_APLICA**.
- Dimensiones: columna 273 OK / 115 ND / 79 CONFL · fila 466 / 1 · perímetro 463 OK / 4 NA · reexpresión 51 OK / 144 ND / 248 NA / 24 CONFL · signo 448 / 19 NA · unidad 467/467 OK · versión 467/467 OK.
- Mecánicos sin cambio: 568 COINCIDE_PROPUESTO / 52 HIPOTESIS / 35 CONVENCION / 16 NO_APLICABLE / 6 DATO_AUSENTE; origen 617 M2_NUEVA / 60 M1_REUTILIZADA; derivados 101 (14 piloto / 87 nuevos), 0 ciclos, hash de entradas vigente.
- Control: `control_cobertura.py` **PASS, 0 violaciones, exit 0**; recuentos conciliados 677/60/617/101/14/87.

## Conservado (conforme según A2)

- Reproducibilidad (salidas regeneradas en un pase con el código definitivo v4.0), 60 piloto M1 REUTILIZADO_M1, 5 sondas d375d80 en CONFLICTO, universo 677, estados mecánicos, 251 insumos con sha256, diff confinado a `resultados_m2/cobertura_vm/`.

## Pendientes (honestos)

- 209 PENDIENTE + 133 CONFLICTO en el CSV: los CONFLICTO son contradicciones documentadas que requieren resolución humana (no se fuerzan); los pendientes conservan su bloqueo preciso en `resultados/resoluciones_bloque2.json` / `cola_pendientes.json` (bloque 2 del cierre sigue abierto: grupos con SIN_ORIGINAL por insumos 2016 no fijados, etc.).
- A-CTX sigue pendiente de revisión por otro contexto (Claude coordinador); G-MANUAL solo si CONTROL.json lo asigna.
- Modelo: `mistral-large-4-0`; consumo/facturación no visible desde la sesión.
