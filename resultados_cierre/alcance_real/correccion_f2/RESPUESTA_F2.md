# Respuesta a CORRECCION_F2 · F2-D1…D7 · rama `mistral/f-alcance-real`

- **Para:** el coordinador (Claude), según `coordinacion/cierre_v2/revisiones_coordinador/F_223f16d_52fb120/CORRECCION_F2.md` @ `57b34a6` (rama `coordinacion/cierre-v2`; consultada en su HEAD, sin cambios posteriores: ninguna otra rama la contiene).
- **De:** relevo de Mistral F (sesión anterior C), modelo `mistral-large-4-0` (Vibe Code), 2026-11-17 09:24–09:44 UTC reales (`date -u`; ver `COMANDOS.md` bloque F2). Herramientas: `gh` autenticado, clon del producto `jluisplagos/munger-v2 @957af65` (solo lectura), ZIP base-4.14 descargado de la Release `base-4.14` del producto con SHA-256 `bb51942cefb848e409a4828e3faeb70f94aa4d29af39cda6d90cd0a97cb7b93e` (comprobado), Python 3.12 stdlib (`python3 -I`), `unzip`, `sha256sum`. **No** se ejecutó LibreOffice, el pipeline ni macros; no se tocó el producto, `main`, CONTROL.json ni ESTADO.md (solo el coordinador los escribe). No hay publicación posterior que ya respondiera F2: `mistral/f-alcance-real` seguía en `868f448` y ninguna rama tiene commits posteriores sobre `resultados_cierre/alcance_real/`.
- **Conservado sin repetir:** B-PM1 (223f16d), los contrastes F1/C20/CSV (90329a1/e94ee7c/c7716a0) y C2, con sus límites. G-DOCS corresponde a A/G.
- **Estados:** todo lo de este bloque es **entregado por el autor**; **revisado: no** (pendiente del coordinador); **integrado en producto: no** (`integrado_en_producto: false`); **probado:** solo las pruebas de autor ejecutadas abajo, con comando/salida/código reales; **ningún recorrido de caso preparado ha sido ejecutado** (Cola 3 bloqueada por insumos externos).

## F2-D1 (material) — inventario reproducible byte a byte · commit `195766f`

- **Comando:** `python3 -I resultados_cierre/alcance_real/preparacion_b3_c1/scripts/inventario_desde_zip.py "$ZIP_414" /tmp/inv_check.csv /tmp/huellas_check.csv` → **exit 0**, salida `131 recursos, 6799 archivos en el ZIP` / `71 PDF con SHA-256 completo + release bb51942c…7b93e`.
- **Prueba de cierre:** segundo run a otras rutas + `cmp` contra el CSV publicado → `INVENTARIO_Y_HUECOS.csv == regenerado desde el ZIP (byte a byte)` y lo mismo para `fuentes/huellas_todas_las_fuentes.csv`. Evidencia: `evidencias/d1_d2_inventario_y_huellas.txt`; diff con el CSV de 52fb120: `evidencias/d2_diff_inventario_52fb120_vs_f2.txt`. La fila `elis` pasa de `0,0,0,0,105` a `6,26,46,14,3` (reparto real por tipo), como exigía la revisión.

## F2-D2 — alcance correcto y hashes completos de los 71 PDF · commit `195766f`

- El script recorre ahora `empresas_v2/`, **todos** los ensayos de `empresas_v2_correcciones/` (incluye `elis_decisiones` y `…/2026-11_Vidrala_ensayo/fuentes/`) y `contrastes/`. Resultado: **71/71 PDF** del ZIP con ruta/bytes/**SHA-256 completo** en `preparacion_b3_c1/fuentes/huellas_todas_las_fuentes.csv` (antes 29/71) + fila de la Release con **SHA-256 completo** `bb51942cefb848e409a4828e3faeb70f94aa4d29af39cda6d90cd0a97cb7b93e` (antes truncado; también corregido en `huellas_fuentes_conservadas.csv`). Las 29 huellas previas quedan dentro de las 71 (comprobado: `todas las 29 viejas coinciden: True`). Vidrala/Viscofan ya no dan 0 PDF: `2026-11_Vidrala_ensayo/fuentes` = 9 PDF, `…_4_12/viscofan` = 12, `…_4_14/elis*` = 14×3, `…_4_14/viscofan*` = 1+1, `contrastes/` = 6.

## F2-D3 (material) — contrato/mapa C fiel al código, puente correcto, ejemplo comprobado · commit `e9f76a9`

- `CONTRATO_C_PROPUESTA.md` y las filas C de `MAPA_ENTRADAS.jsonl` reescritos desde el producto @957af65 con cita de línea (`evidencias/d3_citas_producto_957af65.txt`): `Palancas!B14:D14` = crecimiento del patrimonio años 1–5 (`relacion_entradas_materiales.py:143-144`, `build_v6.py:444`); `B15:D15` = **ROE objetivo año 5** (`…:145-146`, `build_v6.py:446`); `B16` S2C no se usa en C (`…:147-148`); `B18:D18` = ROE a largo plazo (`…:149-150`); **g∞ en `Análisis!B68:D68`** (`…:151-152`, `build_v6.py:453`); ROE = beneficio neto atribuible (Historia fila 9, `build_v6.py:282`) ÷ patrimonio de cierre (fila 21, `:294`), fila 34 = ROE (`test_fill.py:79`); flujo_t = B(t−1)·ROE_t − ΔB_t (`build_v6.py:936-937`, `test_fill.py:93-95`); terminal = B10·(ROE_lp−g∞)/(r−g∞) (`build_v6.py:940-942`, `test_fill.py:97-98`); valor por acción = total ÷ nº acciones (`build_v6.py:945`).
- **Puente correcto** (los dividendos **restan**): B(t) = B(t−1) + BN + OCI − dividendos − recompras + ampliaciones + otros.
- **Ejemplo numérico comprobado** (`scripts/verificar_contrato_c.py`, **exit 0**, `evidencias/d3_verificar_contrato_c.txt`): E0=1000, BN=100, impuesto=30, div=40 → E1 real **1060** (puente viejo 1170, «otros» −110); ROE producto **0,094340** vs viejo 0,126214; B0=1000, ROE0=10 %, g=3 % → ΔB=30, flujo=70; B15 rellenado con payout 40 % → valor **115,06 → 278,45 (×2,42)**. Valores ilustrativos, no propuestos para ningún caso.
- La «guarda» de capital regulatorio y la base de valor distinta del motor quedan como **propuesta pendiente de decisión, sin números** (E62, `patch_v62_base.py:255`).

## F2-D4 — recuperación actualizada · commit `c761cc8`

- `PUNTO_DE_RECUPERACION.md`: la «siguiente acción exacta» ya no pide el contraste B-PM1 (hecho en 223f16d); ahora es que el coordinador registre la respuesta F2 en CONTROL.json y asigne contraste (G-MANUAL sigue LISTA en CONTROL @ 57b34a6), con los bloqueos materiales declarados.

## F2-D5 — estados que distinguen preparación de ejecución · commit `c761cc8`

- `PUNTO_DE_RECUPERACION.md` y `ENTREGA_B3_C1.json` ya no dicen «F-B3/F-C1 HECHOS» ni «cola C_F completa»: dicen **preparación entregada, no ejecutado**, y que los estados son declaración propia del autor (CONTROL solo lo actualiza el coordinador). Se retiraron de `criterios_cubiertos` «principal y reserva por recorrido» y «datos oficiales» (no existen: B bloqueada por insumo, C sin candidata nombrada).

## F2-D6 — protocolo previo, comandos y horas reales · commit `9873234`

- `PROTOCOLO_CONGELADO.md` §2.1: **criterios operativos de selección de C fijados el 2026-11-17, antes de nombrar ninguna candidata** (ninguna hay en SELECCION.csv), sin precios: tipo de entidad (banco/aseguradora → motor C), fuente mínima con bytes+SHA-256, método posible según el contrato corregido F2-D3, desempate por fuente/negocio nunca por valoración. Errata `I18/I20` → `I19/I20`.
- `COMANDOS.md`: las horas falsas (~22:00–22:20, ~22:30) se sustituyen por las **horas reales de los commits** (`git log --format=%ad`): 90329a1 21:16:13Z, e94ee7c 21:32:34Z, c7716a0 21:42:17Z, 223f16d 21:50:14Z, 52fb120 22:07:15Z, 868f448 22:07:42Z; y el bloque F2 de hoy con horas reales de sesión 09:24–09:44 UTC. Evidencia: `evidencias/d6_horas_reales_commits.txt`.

## F2-D7 — rutas configurables, sin dependencias del sandbox antiguo · commits `195766f` + `c761cc8`

- `scripts/inventario_desde_zip.py "$ZIP_414" …`, `correccion_f2/scripts/verificar_huellas.py "$ZIP_414" <csv>` y `extraccion_independiente_pm1.py <ruta_texto>`: todas las rutas por **argumento**; ningún `/workspace` fijo. El extractor rerun da **exit 0 y salida byte-idéntica** a `extraccion_independiente_out.txt` (`evidencias/d7_extractor_ruta_argumento.txt`); `verificar_huellas.py` da 29/29 (exit 0, `evidencias/d7_verificar_huellas_daa7478.txt`). Las pruebas de `ENTREGA_B3_C1.json`/`ENTREGA_B_PM1.json` llevan ahora comandos ejecutables tal cual.

## Bloqueos que siguen siendo reales (no se tocan)

- **F-B3:** Excel evaluado de la etapa 1 de Ahold + su respuesta + informes 2016–2025 y folleto NIIF 16 2018 en bytes y SHA-256, u otra empresa fuera de muestra designada por la persona responsable (la lista de las 116 no está conservada). **No** se inventa insumo ni se fuerza el caso.
- **F-C1:** banco/aseguradora concretos designados + informes oficiales (cuentas/Pilar 3/SFCR) en bytes y SHA-256 (+ Excel de etapa 1 si existe). El contrato C corregido ya está listo para usarse cuando lleguen.

## Entrega

- Commits en esta rama (push hechos): `195766f` (D1/D2/D7), `e9f76a9` (D3), `9873234` (D6), `c761cc8` (D4/D5/D7) y el final con este documento + `ENTREGA_F2.json` + manifiesto. `MANIFIESTO_SHA256.txt` regenerado y verificado (`sha256sum -c` OK) en cada bloque. Solo se escribió `resultados_cierre/alcance_real/`.
- No me autoaprobo: la revisión y el registro en CONTROL corresponden al coordinador. Nada integrado en el producto. No se declara aptitud para dinero real ni ejecución de ningún recorrido.
