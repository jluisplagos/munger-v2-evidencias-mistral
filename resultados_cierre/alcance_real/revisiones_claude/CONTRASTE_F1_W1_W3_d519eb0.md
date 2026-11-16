# Contraste independiente F-REV · F1 W1–W3 @ d519eb0 (base 716cbd6)

- **Revisor**: sesión Mistral C/F distinta del autor. Modelo real: `mistral-large-4-0` (Vibe Code). Herramientas: `gh` CLI autenticado y Python 3.12 (solo stdlib). El autor firma el commit como Claude Opus 5.5 (sesión `01W2RVAnAbM8rydCEdcDNjDs`); soy otro contexto y otra familia de modelo. Esfuerzo/consumo no visibles desde la sesión; no se declaran.
- **Objeto revisado**: commit `d519eb04978e64d04f1d1795c570ca96bdd7ad7f` ("Apply W1-W3 from the F1 v3 review…"), cuyo padre es exactamente la base fijada `716cbd6794b7fcde8b3862c9d1e7acdaf516d262`. Repositorio del producto `jluisplagos/munger-v2` (solo lectura; el sandbox no permite `git remote add`, se usó la API de `gh`).
- **Solicitud**: `coordinacion/cierre_v2/CONTROL.json` @ `coordinacion/cierre-v2`, tarea `F1-W`, `solicitud_revision.estado = LISTA`, revisor asignado "Mistral C/F", 4 criterios W1/W2/W3 + conservación. Revisión dirigida solo a lo afectado por W1–W3; no reabro V1–V11 ni f5775dc.
- **Fecha de consulta**: 2026-11-16 ~21:13 UTC.

## 1. Alcance del diff (nada del producto tocado)

`compare/716cbd6…d519eb0` devuelve **15 archivos, todos bajo `docs/validacion_economica_paralela/frente_E_F1_elis/`** (propuesta, especificación, README, RESPUESTA W1–W3, PUNTO_DE_RECUPERACION, MANIFIESTO, ESTADO, 2 scripts y sus resultados). Ningún archivo del motor, libros, pipeline ni configuraciones del producto. El mensaje del commit lo declara ("nothing adopted or implemented in the product") y el diff lo confirma. `PROPUESTA_DECISIONES_F1.md` sigue rotulado «Para aprobación; no adoptada ni implementada» y conserva texto «el FCF base (307,933), C48 = 108 y C49 = 128,1 no cambian». Hashes de los artefactos descargados y de los dos archivos del producto en la base: `evidencias/verificacion_textual_y_aritmetica.txt`.

## 2. Veredicto por criterio de la solicitud

### W1 — coste temporal después del año 10: CUMPLE

- **Rerun del script del autor** (`controles_sinteticos_f1.py` @ d519eb0, sha256 `26cbf986…`, en copia aislada con `python3 -I`): 32 casos base + W1 (8) + W2 (9) + W3 (4), todo `ok: true`, `resumen.errores = []` salvo **una única diferencia estructural** respecto al JSON publicado: la comprobación textual de código de producto (W2[8]) da `None/False` en mi copia aislada porque el script busca el árbol del producto en `parents[4]` y no está. Es un **artefacto de entorno, no un defecto del autor**: verifiqué las mismas cadenas sobre los archivos del producto descargados a la base exacta 716cbd6 y todas están presentes (`evidencias/verificacion_textual_y_aritmetica.txt`, todo `True`). Detalle: `evidencias/diff_json_rerun_vs_publicado.txt`.
- **Réplica independiente desde cero** (sin importar nada del autor; `evidencias/w1_independiente.py`, Fraction exacto, g = 0): con caja sostenible 68, X = 7 hasta H inclusive, r = 10 %, N = 10 — la **propuesta coincide exactamente con la caja del escenario** en H = 5/10/11/12 (idéntica en Fraction) y **coincide con lo publicado a 0.00e+00** en float; la **regla anterior da 610,0 exacto en H = 11 y 12** (el coste temporal entra en Gordon y se vuelve perpetuo) y solo coincide con la caja en H ≤ 10. El defecto que W1 corrige está confirmado numéricamente por mí, no solo por el autor. Salida: `evidencias/w1_independiente_out.txt`.
- El texto de la propuesta declara H > 10 **no soportado hasta implementar** (V-F1i bloquea la conclusión afectada), sin horizonte de Elis ni cero por defecto. CUMPLE el criterio.

### W2 — signo del salto, magnitud frente a C179, G8 conservado: CUMPLE

- Verificado **textualmente en el producto a la base 716cbd6** (no ejecutado): `munger_v2_r1/v6/scripts/patch_v62_base.py` — A178 «positivo = la rentabilidad marginal cae», B178 = `B176-B177` (marginal − ROIC), C179 = 0,05, `AVISO_TRANSICION`: `MAX(ABS(B178:D178)) <= C179 → ""` (sin aviso en la frontera); `munger_v2_r1/personaje_v2/scripts/comprobar_gramatica.py` — G8: `abs(sv) > umbral + 1e-9 → requiere_justificacion=True` (tampoco salta en la frontera). La propuesta replica exactamente esa regla vigente y **conserva G8**; el umbral no cambia.
- Aritmética Elis (Decimal, `evidencias/verificacion_textual_y_aritmetica.txt`): fila 178 = +0,4739 / +0,6770 / +2,4140 pt (MALO/NORMAL/BUENO) — **positivos** (la rentabilidad cae en el año 11) y todos < 5 pt → sin aviso ni justificación obligatoria. La versión anterior del texto decía −0,47/−0,68/−2,41 (signo invertido respecto a la fila 178 del libro); W2 lo corrige y el diff lo muestra. Los 9 casos W2 (ambas direcciones, frontera exacta ±0,05 sin aviso, ±0,0501 con aviso, Elis MALO/BUENO) dan `ok: true` en el rerun.

### W3 — dominio de A0: CUMPLE

- 4 casos: ambos positivos → V-F1a BLOQUEA (doble cómputo, sin umbral adoptado); ambos cero → A0 admisible; solo uno positivo → **V-F1m nuevo: BLOQUEA, fuera del dominio**, sin afirmar doble cómputo. El texto conserva «que V-F1a no salte no admite A0». Los 4 casos dan `ok: true` en el rerun y la semántica de `estado_A0` @ d519eb0 es exactamente esa.

### Conservación (no adopción, invariantes): CUMPLE

Diff solo en la carpeta del frente F1 (15 rutas, §1); nada de (1a)–(5b) adoptado; producto/libros intactos; C48 = 108, C49 = 128,1, FCF base = 307,933 y E1/D3/E2/E6 se conservan en el texto de la propuesta; `RESPUESTA_CORRECCIONES_V1_V11.md` solo añade una línea de estado (V1–V11 no reabierto). Verificado por inspección del diff vía API; **no se ejecutó el producto, los libros ni LibreOffice**.

## 3. Defectos materiales encontrados

**Ninguno.** No se construye contraejemplo mínimo porque no hay defecto material que reproducir. La única anomalía observada (W2[8] `ok: false` en mi copia aislada) es artefacto de entorno y quedó resuelta con la verificación textual independiente sobre la base 716cbd6.

## 4. Límites de esta revisión

- Soy una sesión Mistral (modelo `mistral-large-4-0`), distinta del autor Claude; los tests del autor se ejecutaron en rerun pero **importan su propia réplica** (`contraste_f1.py`) y no los cuento como réplica independiente; mi única réplica independiente es la reconstrucción desde cero de W1 con g = 0 (la caja simplificada no modela crecimiento de ventas, así que g = 2 % queda cubierto solo por el rerun del script del autor, que reproduje exactamente).
- `copia_investigacion_f1.py` **no se ejecutó**: requiere argumentos y el XLSX de Elis; sus resultados publicados (`copia_investigacion_f1.json/.md`, 58 controles) se revisaron solo documentalmente.
- La comprobación de que la regla está en el código del producto es **textual, no de ejecución** (igual que la del autor); no se ejecutó el motor ni la gramática sobre el libro.
- No se evaluó si W1 debe implementarse en el producto: eso es la tarea F1-IMPL del autor y una decisión del integrador; aquí solo se contrasta la propuesta.
- No se revisa C20/CSV (aún PENDIENTE en CONTROL.json en el momento de esta consulta) ni se reabre f5775dc.

## 5. Estado y siguiente acción

- Nada adoptado; producto, main, libros y candidata `integracion/candidata-cierre-v2` intactos. Mi trabajo anterior (frente C @ `mistral/m2-matematica-b` = 1ec4f18) no se toca.
- CONTROL.json consultado tras este bloque (`git fetch origin coordinacion/cierre-v2`): F1-W seguía con `informe_revision: null`; esta revisión lo rellena para el coordinador. C20/CSV siguen PENDIENTE → no hay nueva entrega de Claude que contrastar; continúo con B-PM1 @ daa7478.
- El coordinador (Claude) registra aceptación o objeción; yo no me autoaprobo ni inicio ciclos.

*Propuesta de evidencia o especificación de Mistral; pendiente de revisión e incorporación por el integrador. No APROBADO ni aptitud financiera general.*
