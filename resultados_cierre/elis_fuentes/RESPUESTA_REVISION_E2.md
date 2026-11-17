# Respuesta a la revisión E2 · E-ELIS · sobre `f00c5dd` (bloque 6)

- **Rama:** `mistral/e-fuentes-elis` (auxiliar `jluisplagos/munger-v2-evidencias-mistral`). Base revisada: `f00c5dd64cb956b93ebb199389ce748e9d218f6c` (sobre la respuesta E1 `23718fb`, base `93a9780`).
- **Encargo ejecutado:** `coordinacion/cierre_v2/revisiones_coordinador/E1_23718fb/CORRECCION_E2.md` (E2-D1…D9), según `REVISION_E1_23718fb.md`, en el control vigente `coordinacion/cierre-v2` @ `b257dfd` (tarea E-ELIS, `siguiente_accion`: «Mistral E corrige E2-D1…D9 y actualiza el estado de preservación a la Release»).
- **Ámbito de escritura:** solo `resultados_cierre/elis_fuentes/`. No toco control, producto, main, otros frentes ni B/P-M1 (`mistral/m2-fundamento-pm1` @ `daa7478`, intacta). Sin LibreOffice, pipeline ni macros.
- **Entorno de ejecución:** venv Python 3.12 con `pymupdf==2.1` y `pypdf==7.1.0` (`scripts/requirements.txt`). Reproducción **sin red** con `ELIS_PDF_DIR` apuntando a los 11 PDF descargados de la Release `fuentes-elis-e-20261117` + el URD 2025 de base-4.14 (sha256 `04bfd087…`), la misma técnica que las sondas del revisor (s04). Los 12 sha256 de salida son idénticos a los de `f00c5dd`.

## E2-D1 (media, M6) — CERRADO

Clasificación por sociedad con página, corregida en `CITAS` de `lectura_bloque2.py` y regenerada en `LECTURA_FUENTES.jsonl`/`PREGUNTAS_Y_RESULTADOS.csv`:

- Las **seis** importantes de 2025 son **Wäscherei Bodensee, Bugadería Neutral, Larosé, Acquaflash, JP Muller, Adrett** (URD p.306; antes se omitía Acquaflash y se incluía a Lavartex).
- **Lavartex no es compra de 2025:** en p.341 su columna tiene `-` en «Cash outflows» y solo `(19.7)` en «Earnouts and deferred consideration» (p.342: ya figuraba en 2024 con earnout (83,2)). Citas nuevas atómicas en p.341 (filas de desembolsos y earnouts).
- **117,6 = 60,8 + 19,7 + 37,3:** 8,9+13,2+10,2+7,0+11,8+9,7 = **60,8** (seis importantes) + 19,7 (Lavartex) + 37,3 (Other, de los que **3,6** son earnouts/aplazados) = 117,8; el total impreso es (117,6), diferencia de redondeo 0,2. 117,6 y 37,3 no cambian; cambia lo que se dice que contiene el 117,6.
- **Carsan (9,7 M€ de ingresos 2024) y Ernst (19,0 M€) clasificadas como importantes de 2024** (p.341 «Acquisitions during the previous financial year», columna propia en la tabla de 2024 p.342): su efecto en Q1 2025 es crecimiento externo de operaciones de 2024.
- **Prueba ejecutada:** `python3 scripts/comprobar_clasificacion_m6.py` → exit 0 (Decimal sobre el URD 2025 base-4.14 `04bfd087…`: p.306 contiene Acquaflash y no Lavartex; p.341 NET CASH FLOW suma 60,8/117,8 con redondeo 0,2; p.341/p.342 Carsan 9,7 / Ernst 19,0). Las 68 citas re-verifican en su página con PyMuPDF y con pypdf (`verificar_segundo_extractor.py` → 68/68, exit 0). M6 sigue **ABIERTO**.

## E2-D2 (cinco hallazgos por encima de su cita) — CERRADO

Cada afirmación añadida queda cubierta por una cita atómica nueva (sin `.*` ni `|`, guarda interna):

- [3] lino: `resulted from a better management of linen investment` (comunicado FY2025 p.6).
- [4] 18,2%/19,2% y FCF: `As a % of revenue -?
18.2% -?
19.2%` y `Free cash flow 358.6 346.3` (presentación FY2025 p.29; el patrón admite el espacio tras el guion que mete pypdf).
- [20] 37%: `Workwear 37%` (factsheet 2026 p.1).
- [23] disciplina de precios: `maintains its pricing discipline and takes a selective approach to acquiring new customers` (Q3 2026 p.3).
- [24] perímetro y divisa: `changes in the scope of consolidation of “major acquisitions” and “major disposals”` y `the impact of exchange rate fluctuations` (URD p.313).
- **Prueba:** `lectura_bloque2.py` exit 0 con 68 citas (antes 52); `verificar_segundo_extractor.py` 68/68 exit 0; 33 extractos regenerados (`publicar_extractos.py` exit 0).

## E2-D3 («ancla nueva» / «19,5% nuevo» de cifras ya en la base) — CERRADO

- H1-2026 19,5% releído como **corroboración de base**: el informe semestral 2026 EN de base-4.14 (sha256 `3919657f…`) ya dice en su p.10 «the ratio stood at 19.5% in H1 2026 (versus 18.4% in H1 2025)…». El brochure CGM p.15 repite el capex de URD p.312: también corroboración con documento nuevo.
- **Prueba ejecutada:** `python3 scripts/verificar_base_4_14.py` → exit 0 (extrae del ZIP base-4.14, sha256 `bb51942c…`, el URD `04bfd087…` y el semestral `3919657f…`, y verifica la frase en p.10). Textos actualizados en `HALLAZGOS_ELIS.md`, `ESTADOS_E1`/CSV de `lectura_bloque2.py` y `PUNTO_DE_RECUPERACION.md`.

## E2-D4 (fallo de descarga reescribía el índice de Git; lectura pasaba con `sha256_doc=''`) — CERRADO

- `descargar_fuentes_elis.py`: el índice publicado en Git **solo se reescribe si no hay fallos**; con fallos escribe solo `.trabajo/` y sale exit 1.
- `lectura_bloque2.py`: exige `http==200` y `sha256` no vacío para **todos** los documentos del índice y **recalcula el sha256 del PDF** de `.trabajo/pdf/` comparándolo con el índice; falla (exit 1) si falta o difiere.
- **Negativos ejecutados** (copia desechable, log en `pruebas_e2/NEGATIVOS_E2.txt`): D4a — 1 PDF ausente → exit 1 y el `INDICE_DESCARGAS.csv` de Git queda byte-idéntico (sha256 `74cbae82…` antes y después); D4b — índice de `.trabajo` con `sha256=''` → `AssertionError: E2-D4: q1_2025_revenue sin descarga valida…` exit 1.

## E2-D5 (exit 0 sin PyMuPDF; inventario necesitaba red y `base414.zip` sin declararlo) — CERRADO

- `requirements.txt` fija `pymupdf==2.1` y `pypdf==7.1.0`. `descargar` y `lectura` comprueban `fitz` al arrancar (exit 3 si falta); `verificar_segundo_extractor` comprueba `pypdf` (exit 3). `inventario_bloque1.py` declara red (`git ls-remote origin`) y `.trabajo/base414.zip` (sha256 registrada) con exit 2 y comando exacto ante `IndexError`/`FileNotFoundError`.
- **Negativos ejecutados** (log `pruebas_e2/NEGATIVOS_E2.txt`): D5a sin fitz → `SystemExit 3`; D5b sin pypdf → `SystemExit 3`; D5c sin el commit `716cbd6` → exit 2 con `git fetch https://github.com/jluisplagos/munger-v2.git 716cbd6…` impreso.

## E2-D6 («este commit» contradictorio; ENTREGA sin `f00c5dd`) — CERRADO

- `PUNTO_DE_RECUPERACION.md`: bloque 4 → `23718fb`, bloque 5 → `f00c5dd` (SHAs explícitos; el bloque 6 se anota «este commit; el coordinador toma el SHA remoto», único caso permitido por INTEGRACION.md). `ENTREGA.json` reescrito para el bloque 6 e incluye `f00c5dd`/`CHECKPOINT_RELEVO.md` en el historial.

## E2-D7 (residuos absolutos) — CERRADO

- «sin cifra publicada» → «sin cifra en esta página»; «No publica la tasa…» → «No da la tasa… en esta página; no localizado en esta búsqueda»; «ninguna tasa ni importe publicado» → «ninguna tasa ni importe localizado en la búsqueda previa» (cita 18 de LECTURA, fila M2 de PREGUNTAS bloque 1 y `inventario_bloque1.py`).
- **Prueba:** `grep -rniE 'sin cifra publicada|No publica la tasa|ninguna tasa ni importe publicado'` sobre los textos regenerados → 0 resultados salvo la meta-mención de esta respuesta y de `CORRECCION_E2` en los textos de corrección.

## E2-D8 (`version` = HEAD del auxiliar) — CERRADO

- Columna `version` eliminada de `CAMPOS` en `descargar_fuentes_elis.py`, del índice publicado y de `FUENTES_Y_BUSQUEDA.csv` (la fecha/edición del documento ya está en `fecha`). Regenerado: `INDICE_DESCARGAS.csv` sin `version`.

## E2-D9 (errata «Warts cherei»/«Wärtscherei») — CERRADO

- Corregido a **Wäscherei** en los hallazgos de `lectura_bloque2.py` (regeneran LECTURA/PREGUNTAS), `HALLAZGOS_ELIS.md` y `RESPUESTA_REVISION_E1.md` (con adenda). Los patrones `W\S*scherei` ya casaban con lo impreso.
- **Prueba:** `grep -rn 'Warts cherei\|Wärtscherei'` → 0 resultados.

## Estado de preservación (hecho nuevo que la entrega no conocía) — ACTUALIZADO

Los 11 PDF nuevos **ya no son provisionales**: están preservados en la Release `fuentes-elis-e-20261117` del repositorio auxiliar (decisión U1 del usuario, 2026-11-17). Verificado en esta sesión: `gh release download` de la Release → `sha256sum -c SHA256SUMS` 11/11 OK, y los 11 sha256 coinciden con `INDICE_DESCARGAS.csv` (`scripts/verificar_preservacion_release.py --dir …` → exit 0); URD 2025 = base-4.14 (`04bfd087…`). Los 44 textos que decían «PROVISIONAL» se han actualizado (los históricos `RESPUESTA_REVISION_E1.md`/`CHECKPOINT_RELEVO.md` llevan adenda). Los PDF siguen fuera del Git del auxiliar por norma del repo.

## Comandos y resultados ejecutados (bloque 6)

```
ELIS_PDF_DIR=/tmp/pdf_elis python3 scripts/descargar_fuentes_elis.py   -> exit 0, 12/12, sha256 identicos a f00c5dd
python3 scripts/lectura_bloque2.py                                     -> exit 0, 80 registros, 68 citas (2 ejecuciones: sha256 identicos)
python3 scripts/publicar_extractos.py                                  -> exit 0, 33 extractos
python3 scripts/verificar_segundo_extractor.py                         -> exit 0, pypdf 7.1.0: 68/68 con huella recalculada
python3 scripts/comprobar_clasificacion_m6.py                          -> exit 0 (E2-D1, Decimal sobre URD base-4.14)
python3 scripts/verificar_base_4_14.py                                 -> exit 0 (E2-D3, sha256 3919657f... p.10)
python3 scripts/verificar_preservacion_release.py --dir /tmp/pdf_elis  -> exit 0, Release 11/11 == indice 11/11
negativos D4a/D4b/D5a/D5b/D5c                                          -> exit 1 / 1 / 3 / 3 / 2 (pruebas_e2/NEGATIVOS_E2.txt)
grep residuos absolutos / errata                                       -> 0 / 0
```

## Lo que no cambia

- **M1, M2, M6 y N2 siguen ABIERTOS**; Elis sigue `pendiente_de_datos`. Nada desbloquea R, θ, λ, k, probabilidades ni umbrales; C48=108, C49=128,1, FCF base=307,933 y las decisiones E1/D3/E2/E6 se conservan.
- B/P-M1 intacta en `mistral/m2-fundamento-pm1` @ `daa7478`. Nada integrado en el producto (`integrado_en_producto: false`); la revisión corresponde al coordinador (Claude) sobre este commit. Sin ciclos recursivos ni autoaprobación.
- Sin contacto con empresas, sin uploads repetidos ni tokens; las URLs oficiales públicas se consultan solo para lectura.

## Modelo y herramientas

Vibe Code de Mistral AI, modelo `mistral-large-4-0`; Python 3.12 + venv (`pymupdf==2.1`, `pypdf==7.1.0`, `scripts/requirements.txt`); `gh release download` (solo lectura) para verificar la Release; git. Consumo no visible desde la sesión.
