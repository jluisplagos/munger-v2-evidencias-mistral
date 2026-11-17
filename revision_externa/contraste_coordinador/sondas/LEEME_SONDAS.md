# Sondas propias del contraste (Mistral R)

- `control_consistency.py`: consistencia de `CONTROL.json` (rama `coordinacion/cierre-v2` @ `30c314c`) con los `informe_revision.veredicto` enlazados. Ejecutada con:
  `git show coordinacion/cierre-v2:coordinacion/cierre_v2/CONTROL.json > /tmp/CONTROL_cierre_v2.json`
  `python3 -I control_consistency.py /tmp/CONTROL_cierre_v2.json`
  Salida en `resultados_control_consistency.log`: la única DISCREPANCIA real es **G-MANUAL** (`revision=CONFORME_CON_LIMITES` vs veredicto «CORRECCIONES: 4 medios y 12 menores…»).
- Las demás sondas (reproducción de las del coordinador) se ejecutaron sobre copias `git archive` de cada commit revisado en `/workspace` (fuera del repo) y se describen con comandos y resultados en cada `CONTRASTE_*.md`:
  - AUTO: 6×unittest (100 OK), `sonda_sse.py` (salida idéntica, 25/16/9), `sonda_workflows.sh` (idéntica), diff `a508d6b..267ad18` (solo `observations/`).
  - MANUAL: `citas.py` (603/139/37 citas; 24/2/0 problemas), `sonda_literales.py` (idéntica), `git diff --no-index --stat` (476/274), líneas de CONTROL.json, `sha256sum -c` del manifiesto aux (coincide), manifiesto vs `git ls-files` en clon de `3149128` (7762 entradas, 6726 trackeadas), lecturas de `build`/`comprobar_*` del producto @ `3149128`/`957af65`.
  - D3/d032691: `sha256sum -c` (4 fallos @3934bc9; 11+1 @5f4b2a2; banco 57/57; 204/204 @d032691), `sondas_arnes_d2.py` (idéntica salvo rutas temporales/hash del stub), `comprobaciones_d2.sh` (log idéntico), `sondas_arnes_d3.py` (JSON idéntico, cero diferencias), recuento de `MATRIZ_EJECUCION.csv` (30 CUMPLE, «sí» 36/36).
  - A4: `sha256sum -c` (196/196), recuento de `COBERTURA_677.csv` (209/283/19), polaridad en `verificacion_contexto.jsonl` (5 celdas), sha256 de `ENTREGA.json` vs `control_cobertura.json` real, `cola_pendientes.json` (233/50/88).
  - E2: manifiestos (2 .pyc en 23718fb; 49/49 en f00c5dd), 32 extractos, URD p.306/p.312/p.341 en `extractos/` (sha del PDF `04bfd087…`).
  - F3: manifiesto 46/46 @98bdf8f; `build_v6.py` @957af65 (motor en `Análisis!C62`, V01 :1102-1103, V11 :1133).

No si ejecuta red, API de pago, workflows, LibreOffice ni el producto.
