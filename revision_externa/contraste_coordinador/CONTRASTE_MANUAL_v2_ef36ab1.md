# CONTRASTE_MANUAL_v2_ef36ab1 · revisión del coordinador sobre G-MANUAL v2 (`ef36ab1`)

- **Revisión contrastada:** `coordinacion/cierre_v2/revisiones_coordinador/MANUAL_v2_ef36ab1/` (rama `coordinacion/cierre-v2` @ `30c314c`): `REVISION_MANUAL_v2_ef36ab1.md`, `CORRECCION_MANUAL_v3.md`, `sondas/` (herramientas `citas.py`, `cita.sh`, `sonda_literales.py`).
- **Veredicto del contraste: LA REVISIÓN SE SOSTIENE, con una discrepancia de control.** Hallazgos M1–M4 y m1–m12 reproducen; nada aceptado; pero `CONTROL.json` no refleja fielmente el veredicto en el campo `revision` de G-MANUAL (ver §Discrepancias).

## Sondas propias (reproducción)

Aux = este repo @ `ef36ab1`; candidata = `jluisplagos/munger-v2` @ `3149128` (clon aislado aparte, solo lectura):

| Sonda | Resultado mío | Publicada |
|---|---|---|
| S01: `git diff --stat 6889b02 ef36ab1`; huellas del manifiesto | ef36ab1 añade solo los 4 archivos (3 docs + manifiesto); sha256 coinciden: `894caa2e…`, `cc19014f…`, `38cc5c0b…`, `6ed65dce…`, `88e69671…` | Idéntica |
| S02/S03: `citas.py` sobre Manual, CAMBIOS, Propuesta (con `CAND`/`AUX`) | Manual: **603 citas, 24 problemas**; CAMBIOS: **139 citas, 2 problemas** (AMBIG L18); Propuesta: **37 citas, 0 problemas**; detalle idéntico al publicado salvo sustitución de `<home>` | Idéntica |
| `sonda_literales.py` | 145 scripts / 13129 literales; frase1 y frase2 aparecen **1 vez** cada una en `CONTINUIDAD.md`; cambios 1+2 → 0 literales; `957af65→3149128` → 3 fragmentos (`2. Adjuntar \``, `ambos`, `código: `); 1207 presentes | Idéntica a S04 |
| S10: `git diff --no-index --stat` v1→v2 | **476 inserciones / 274 supresiones**; tabla m1: las 11 claves buscadas dan v1=1, v2=0, CAMBIOS=0; `INCIDENCES_4_14.md` sigue en «Fuentes leídas» (L689) | Idéntica |
| S13: líneas de `CONTROL.json` @ `ef36ab1` (31-32, 582, 754, 802, 809-810, 833) y @ `b257dfd` (34, 589) | Coinciden con S13 (m11) | Idéntica |
| L635 «FUERA DE RANGO» de la herramienta | Falso positivo de la heurística: el `:375` de esa fila remite a `munger_v2_r1/CONTINUIDAD.md:375` (archivo de 397 líneas; frase del ZIP completo). La afirmación del informe «todas existen y en rango» se sostiene | — |

## Hallazgos verificados

- **M1:** `comprobar_entrega_4_8.py:60` (producto @3149128) hace `copytree` excluyendo solo `empresas_v2`, `empresas_v2_correcciones`, `.lo_perfil`, `__pycache__`, `sintetico` → **copia `pruebas/_v64/`**; `:75` `mkdtemp(prefix="c48_")`, `:195` borrado; `comprobar_entrega_4_9.py:84` `os.walk(RAIZ)` sin excluir `_v64/`; en `controles_historicos_4_13.py` hay 19 controles y el 4.8 (:39) va antes que el 4.8.1 (:41). Confirmado.
- **M2:** en un clon nuevo de `3149128`: `.gitignore:2 = *.pdf`; el manifiesto tiene **7762 entradas, de las que 6726 están en git** (1036 no: 83 `.json`, 843 `.xlsx`, 71 `.pdf`, …) y `git status --short` da 0 líneas. Es decir, `git status` sin `--ignored` no detecta los binarios ignorados; en el worktree del revisor estaban materializados (7762/7762, 682 con `--ignored` según S12 publicada). La afirmación del §13 del manual («no tiene los binarios materializados») es falsa o engañosa. Confirmado.
- **M3:** Manual L88, L155, L196, L224, L269, L282, L323 dicen «comando probado en el traspaso del 17-nov» **sin** `(autodeclarado)`, mientras L160, L167, L188, L219, L311, L476 sí lo llevan; la tabla de `REVT/REVISION_TRASPASO.md` da «—»/«I» en comando/código para esos pasos (flock paso 8, código 1 paso 9, 403 paso 2a). La regla del propio Manual:12 no se aplica uniformemente. Confirmado.
- **Criterio 3 (S05):** `resumen.md` del registro: 4.10 «39 de 44», 4.11 «33 de 38», 4.12 CUMPLE miembro a miembro (txt:14); en el producto, `comprobar_entrega_4_10.py:181-182` comprueba `.PARTES.txt` y `PROMPT_NUEVA_VENTANA.md` lo contiene 1 vez en `origin/main`, 0 en `957af65` y 0 en `3149128`. Confirmado.

## Control (CONTROL.json) · DISCREPANCIA

- `tareas[G-MANUAL].solicitud_revision.informe_revision.veredicto` = «**CORRECCIONES**: 4 medios y 12 menores, sin hallazgos materiales…», y `registro_eventos` (2026-11-17) dice «Manual v2 (ef36ab1) revisado … **CORRECCIONES**, con 4 medios … y 12 menores».
- Pero `tareas[G-MANUAL].revision` = **`CONFORME_CON_LIMITES`**, valor que también muestra la tabla de `ESTADO.md`, mientras que el texto de «Próxima acción» de ese mismo ESTADO dice «v2 (ef36ab1) revisado: **CORRECCIONES (M1–M4 y 12 menores)**».
- **Discrepancia D-MANUAL-1:** el campo `revision` de G-MANUAL no refleja el veredicto del informe enlazado (parece residuo de la revisión anterior del manual v1, `78ba1ca`, que sí fue CONFORME_CON_LÍMITES). No hay aceptación indebida (`integracion=NO`, `alcance_aceptado=[]`), pero el control no refleja fielmente lo revisado en ese campo. Sugerencia: alinear `revision` a `CORRECCIONES`, como en T-AUTO/A-CTX/E-ELIS.

## Otros puntos

- Nada aceptado sin evidencia: `integracion=NO`, `alcance_aceptado=[]`, pruebas `NO_EJECUTADAS/PARCIALES`. OK.
- Límite mío: no reejecuté el pipeline del producto ni las marcas «probado» más allá de contrastarlas con lo publicado en `TRASP/`, `REG/`, `REVT/`, `PRUEBAS/`, `F1PREP/` (igual que el revisor).
