# Respuesta a la revisión externa E1 · E-ELIS · sobre `93a9780`

- **Rama:** `mistral/e-fuentes-elis` (auxiliar `jluisplagos/munger-v2-evidencias-mistral`). Base revisada: `93a97801f8c4f6a4dc5cabd4540248390cf113d0`.
- **Encargo ejecutado:** `coordinacion/cierre_v2/revisiones_coordinador/E_93a9780/CORRECCION_E1.md` (control de referencia de la reanudación `99adbbf`, rama `coordinacion/cierre-v2`; el archivo no ha cambiado en el HEAD consultado durante esta corrección, `57b34a6`; la adenda del coordinador verificó 11/11 PDF y 28/28 citas desde sus URL oficiales). Apartado asignado: §4 Mistral E de `revision_externa/reanudacion_20261117/REANUDACION.md` (`c241a59`).
- **Ámbito de escritura:** solo `resultados_cierre/elis_fuentes/`. No se toca control, producto, main, otros frentes ni B/P-M1 (`mistral/m2-fundamento-pm1` @ `daa7478`, intacta). Sin LibreOffice, pipeline ni macros.

Cada punto E-R1…E-R9 con su prueba de cierre **realmente ejecutada** (comandos al final). Todas las citas quoted verifican en documento + página PDF con PyMuPDF (extractor primario) **y** con pypdf 7.1.0 (segundo extractor): 52/52.

## E-R1 (material, N2) — CERRADO

- **Hecho:** retirada la afirmación falsa de que el +25,7 es «concepto monetario» de la «sección operativa». En la nota 4.6 (URD 2025 p.350) la ganancia por bajas va en su **propia línea** (`Net gain (loss) related to retirement of fixed assets 25.7 (1.5)`), **separada** de `of which monetary items (28.2) (22.2)`; figura además como sublínea `of which net gain (loss) on disposal of non-current assets 25.7 (1.5)`.
- **EFE (p.327):** `Net gains and losses on disposal of property, plant and equipment and intangible assets (23.1)` aparece en la sección **operativa** (antes de `NET CASH FROM OPERATING ACTIVITIES 1,510.6 1,452.1`) y se resta como partida no monetaria; `Proceeds from disposal of property, plant and equipment 15.3 7.3` va en **inversión** (antes de `NET CASH FLOWS FROM INVESTING ACTIVITIES (991.5) (1,060.3)`).
- **Nota 4.4 (p.349):** `Change in receivables on disposal of fixed assets 16.9 (0.1)` — 16,9 M€ a cobrar por bajas a cierre 2025.
- **Dos medidas separadas:** +23,1 M€ (EFE p.327, todas las bajas de PP&E e intangibles; es la que F1 usa para `f`, informe `716cbd6` l317/l328) vs +25,7 M€ (nota 4.6 p.350, bajas de inmovilizado; la que eleva m0 +0,54 pp). **N2 queda ABIERTO** en cobro, fiscalidad y reposición, con las tres páginas citadas (327/349/350). La narrativa de seguros (URD p.309, comunicado FY2025 p.4, presentación FY2025 p.25) sigue **sin igualarse** con el +25,7.
- **Prueba:** `python3 scripts/lectura_bloque2.py` → exit 0, 52 citas verificadas (incl. las 7 nuevas de p.327/349/350); registros con `tipo_evidencia=corroboracion_base` en `LECTURA_FUENTES.jsonl`; `python3 scripts/verificar_segundo_extractor.py` → 52/52 con pypdf 7.1.0.

## E-R2 (material, M6) — CERRADO

- **Clasificación por sociedad con página:** URD 2025 p.306 (§4.1.2 «Major acquisitions») y p.312 cuentan **seis adquisiciones importantes** en 2025, incl. **Wäscherei Bodensee** (Suiza), Bugaderia Neutral (España), Larosé y Adrett (Alemania). En Note 2.4 (p.341) cada importante tiene **columna propia** (Bodensee, Bugaderia Neutral, Larosé, JP Muller, Adrett, Lavartex) y `Other acquisitions` es columna aparte. Bodensee deja de presentarse como compra pequeña.
- **117,6 ≠ 37,3:** fila `NET CASH FLOW` de p.341: total 2025 **(117,6)** = suma de las columnas de las importantes + `Other acquisitions` **(37,3)** (última columna). 117,6 es el M&A total 2025 en caja (igual en EFE p.327 y presentación FY2025 p.29; en la p.29 impresa hay un marcador de nota «5» entre rótulo y cifra, precisión ya registrada en la adenda). 37,3 son las compras pequeñas 2025. F1 V1 ya citaba 35,3/22,0/37,3 en 2023–25 (media 31,5) [informe `716cbd6` l550; URD 2025 p.341–342; DEU 2024 p.288].
- **Prueba:** citas `urd2025 p306/p312/p341/p327` verificadas (PyMuPDF + pypdf); la tabla p.341 además comprobada visualmente (imagen de página renderizada) para fijar la columna de (37,3); extracto publicado en `extractos/urd2025_p341.txt`.

## E-R3 (M6, perímetro) — CERRADO

- El perímetro del orgánico (URD 2025 p.313: >5,0 M€ ingresos/año en Francia, >3,0 M€ en otros países, Note 2.4) **ya lo tenía F1 V1** [informe `716cbd6` l550: «P: URD 2025 p. 313; DEU 2024 p. 259; URD 2023 p. 267»]. Se declara **corroboración** (`tipo_evidencia=corroboracion_base`) y se retira la lectura de que el umbral «confirma» el 31,5 M€/año: esa media sale de los flujos de adquisiciones pequeñas (p.341–342; DEU 2024 p.288), no del umbral. **M6 queda ABIERTO**; la finalidad reposición/crecimiento no localizado en esta búsqueda.
- **Prueba:** `git show 716cbd6:...INFORME_CONCILIACION_F1.md` (l550) ejecutado; cita p.313 en `LECTURA_FUENTES.jsonl` con `tipo_evidencia=corroboracion_base`.

## E-R4 (M1, corroboración vs evidencia nueva) — CERRADO

- Las cifras de capex (URD 2025 p.311–312: bruto 823,9/887,4/890,2; neto 874,7 = 18,2%; identidad con cesiones 15,3 + subvenciones 0,2) y de taxonomía (p.215: CapEx 1.160,0; 86,0% elegible; 842,0 = 72,6% alineado) **ya estaban en el URD 2025 de la base**: declaradas `corroboracion_base`, no evidencia nueva.
- **Perímetro de la taxonomía añadido (p.217):** incluye altas IAS 38 (26,2), derechos de uso IFRS 16 (183,9), PP&E IAS 16 (887,1) y altas por combinaciones (62,7) = 1.159,9 ≈ 1.160,0; perímetro distinto del capex propio 890,2. El alineado es casi todo **economía circular** (70,7 pp de 72,6%; clima 1,9 pp) y **no mide el plan climático**: no se presenta como importe del plan climático.
- **Prueba:** citas `urd2025 p215 (×2), p217 (×4), p311 (×2), p312` verificadas en ambos extractores.

## E-R5 (citas defectuosas) — CERRADO

- Cita 20 (q1_2025 p.1) y cita 21 (q3_2026 p.1) reescritas **sin `.*` codicioso ni alternativas**, split en citas atómicas: Q1 2025 p.1 (3 adquisiciones Carsan/Ernst/Bodensee, c. 55 M€, +2,1% externo en dos citas separadas); Q3 2026 p.1 (+1,5 pp y pipeline), p.2 (Muller +0,5 pp), p.3 (RS10 +1,3 pp desde 1-jun-2026). Cada afirmación del hallazgo queda cubierta por su cita registrada. Además, todas las citas viejas con `.*` (capex bruto, 19,5% H1 2026, etc.) se han reescrito con texto exacto.
- **Prueba:** `lectura_bloque2.py` incluye una guarda que **falla** si algún patrón contiene `.*` o `|`; exit 0 con 52 citas; negativo real durante el desarrollo: patrón desplazado → exit 1 (`AssertionError: cita no verificada`).

## E-R6 (preservación de los 11 PDF) — CERRADO (cobertura provisional declarada)

- Publicado en Git, solo texto: `fuentes_descargadas/INDICE_DESCARGAS.csv` (por archivo: url_solicitada, url_final, http, content-type, bytes, sha256, fecha_descarga, versión = HEAD del auxiliar en la ejecución, estado) y `extractos/` con **32 extractos acotados de las páginas citadas** (ventana de 400 caracteres alrededor de cada coincidencia), cada uno con la **huella sha256 del PDF** en la cabecera.
- **Cobertura provisional declarada:** los bytes de los PDF **no** están en el Git del auxiliar (upload a `uploads.github.com` → HTTP 401, ya documentado; no se reintenta ni se piden tokens). Siguen **PROVISIONAL** hasta una copia duradera autorizada (decisión del usuario). Re-descarga el 2026-11-17: 12/12 HTTP 200 y los 12 sha256 **idénticos** a los registrados en `93a9780` (y URD 2025 = `04bfd087…` = base-4.14), coherente con la adenda del coordinador.
- **Prueba:** `descargar_fuentes_elis.py` exit 0 (12/12); comparación sha256 12/12 iguales frente a `git show 93a9780:...FUENTES_Y_BUSQUEDA.csv`; `publicar_extractos.py` exit 0 (32 extractos).

## E-R7 (frases absolutas) — CERRADO

- Eliminados «no publicada» / «sigue sin publicarse» de ENTREGA.json, RESUMEN, HALLAZGOS, PREGUNTAS_Y_RESULTADOS.csv y textos de citas de `LECTURA_FUENTES.jsonl`; sustituidos por «**no localizado en esta búsqueda**» con su alcance (12 documentos oficiales nuevos + base ya examinada).
- **Prueba:** `grep -rniE "no publicad|sin publicar"` sobre los textos de evidencia regenerados (HALLAZGOS_ELIS.md, RESUMEN, README, PUNTO_DE_RECUPERACION, PREGUNTAS_Y_RESULTADOS.csv, FUENTES_Y_BUSQUEDA.csv, LECTURA_FUENTES.jsonl) → 0 resultados; las únicas coincidencias restantes son las meta-menciones de esta respuesta y de ENTREGA.json que describen la corrección.

## E-R8 (textos desfasados) — CERRADO

- README ya no dice «pendiente» (bloques 1–3 publicados; bloque 4 = esta corrección E1). Títulos «bloque 2» actualizados a «bloque 2 + corrección E1». Control citado: `99adbbf` (referencia de la reanudación `c241a59`) con HEAD remoto anotado en ejecución (`57b34a6` en esta corrección); ya no se cita `ff0c60cd` como vigente. «Bloque 2 (este commit)» eliminado de ENTREGA.json.
- **Prueba:** textos regenerados y releídos; `inventario_bloque1.py` imprime ambos HEAD (referencia + remoto actual).

## E-R9 (reproducibilidad) — CERRADO

- **Idempotencia:** `lectura_bloque2.py` reescribe `LECTURA_FUENTES.jsonl` desde cero y recalcula (sin duplicar columnas ni filas) `PREGUNTAS_Y_RESULTADOS.csv` y `FUENTES_Y_BUSQUEDA.csv`. Ejecutado 2 veces seguidas: sha256 de las 3 salidas **idénticos** (`diff` de los listados = vacío).
- **Carpetas y exit ≠ 0:** `descargar_fuentes_elis.py` crea `.trabajo/elis_fuentes/{pdf,texto}` y `fuentes_descargadas/`; valida HTTP 200 **y** magic `%PDF` (fr.elis.com devuelve 200 con HTML de error para rutas inexistentes); sale **exit 1** si falla alguna descarga. Negativo ejecutado: URL inexistente → `FALLO ... text/html` → exit 1.
- **Dependencias declaradas:** `inventario_bloque1.py` comprueba con `git cat-file -e` los commits `716cbd6` (producto), `f5775dc` y `99adbbf` (auxiliar) y sale **exit 2** imprimiendo el `git fetch` exacto si falta alguno (negativo ejecutado: commit ausente → exit 2 + comando).
- **Segundo extractor ejecutado:** `verificar_segundo_extractor.py` con **pypdf 7.1.0** re-verifica las 52 citas en sus páginas (normalizando ligaduras y espacios) → **52/52**, informe en `VERIFICACION_SEGUNDO_EXTRACTOR.json`, exit 0.

## Comandos y resultados realmente ejecutados

```
python3 resultados_cierre/elis_fuentes/scripts/inventario_bloque1.py
  -> exit 0 | control ref 99adbbf6; HEAD remoto coordinacion/cierre-v2: 57b34a6 (en ejecución)
     | versiones fijadas OK | zip base-4.14 sha256 OK
python3 resultados_cierre/elis_fuentes/scripts/descargar_fuentes_elis.py
  -> exit 0 | 12/12 HTTP 200, PDF validados (magic %PDF); sha256 12/12 iguales a 93a9780
     | indice Git: fuentes_descargadas/INDICE_DESCARGAS.csv
  -> NEGATIVO (URL inexistente): FALLO 200 text/html -> exit 1
python3 resultados_cierre/elis_fuentes/scripts/lectura_bloque2.py   (ejecutado 2 veces)
  -> exit 0 | 64 registros (12 docs + 52 citas) | segunda ejecución: sha256 idénticos (idempotente)
  -> NEGATIVO (desarrollo, patrón desplazado): AssertionError cita no verificada -> exit 1
python3 resultados_cierre/elis_fuentes/scripts/publicar_extractos.py
  -> exit 0 | 32 extractos acotados en extractos/ con sha256 del PDF en cabecera
python3 resultados_cierre/elis_fuentes/scripts/verificar_segundo_extractor.py
  -> exit 0 | pypdf 7.1.0: 52/52 citas verifican | VERIFICACION_SEGUNDO_EXTRACTOR.json
python3 -c asegurar_commit('0'*40, ...) en inventario_bloque1.py
  -> NEGATIVO: DEPENDENCIA AUSENTE + comando git fetch -> exit 2
git show 716cbd6:.../INFORME_CONCILIACION_F1.md | sed -n '550p'   (V1: p.313 + 35,3/22,0/37,3)
  -> ejecutado, cita confirmada
comparación sha256 12/12 vs git show 93a9780:FUENTES_Y_BUSQUEDA.csv -> TODOS IGUALES
```

## Lo que no cambia

- **Elis sigue `pendiente_de_datos`.** Nada de esto elige R (ni en 736,0–867,2), θ, λ, k, probabilidades, fiscalidad ni umbrales, y no desbloquea la valoración. C48=108, C49=128,1, FCF base=307,933 y las decisiones vigentes (E1/D3/E2/E6) se conservan.
- M1, M2, M6 y N2 quedan **ABIERTOS** (ver `PREGUNTAS_Y_RESULTADOS.csv`, columna `estado_tras_revision_e1`); donde la evidencia no identifica un parámetro se demuestra el límite y queda pendiente.
- Los 11 PDF nuevos siguen **PROVISIONAL**: el almacén duradero lo decide el usuario (§2 de CORRECCION_E1); no bloquea las correcciones de esta entrega.
- Sin ciclos recursivos de revisión ni autoaprobación: la revisión corresponde al coordinador (Claude) sobre el control.

---

## Adenda E2 (2026-11-17, bloque 6)

Esta respuesta queda corregida por `CORRECCION_E2.md` en dos puntos: E2-D1 (la lista de importantes de 2025 es Bodensee, Bugadería Neutral, Larosé, **Acquaflash**, JP Muller y Adrett; **Lavartex no es de 2025**, solo earnout (19,7); Carsan y Ernst son importantes de 2024) y el estado de preservación (los 11 PDF ya están en la Release `fuentes-elis-e-20261117`, decisión U1). Ver `RESPUESTA_REVISION_E2.md`. La errata ortográfica (Wärtscherei → Wäscherei, E2-D9) también queda corregida aquí.
