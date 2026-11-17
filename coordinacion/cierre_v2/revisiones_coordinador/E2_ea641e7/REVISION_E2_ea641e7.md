# Revisión E2 · E-ELIS · `ea641e7` (respuesta a CORRECCION_E2)

- **Revisor:** contexto distinto del autor (Claude, revisión independiente). El autor es Mistral E (`Vibe Nuage Agent`, `mistral-large-4-0`).
- **Objeto:** `mistral/e-fuentes-elis` @ `ea641e77523c7833f67b56f8fd7f1f90577e7add`, un commit sobre `f00c5dd64cb956b93ebb199389ce748e9d218f6c`. Carpeta `resultados_cierre/elis_fuentes/`.
- **Encargo:** `origin/coordinacion/cierre-v2` @ `fcbf345`, `coordinacion/cierre_v2/revisiones_coordinador/E1_23718fb/CORRECCION_E2.md` (E2-D1…D9). Se usan también la revisión E1 y sus sondas de esa carpeta.
- **Modo de trabajo:** solo lectura. Las únicas operaciones de red fueron `git fetch` de las dos ramas y la descarga de la Release `fuentes-elis-e-20261117`. Escribí solo en `rev_E2/`. Las rutas de las sondas usan variables (`AUX`, `REV`, `PDF`, `URD`, `ZIP`, `LIBS`).

## Veredicto

**CERRADO_CON_LIMITES. Queda una corrección acotada (CORRECCION_E3).**

El defecto central **E2-D1 está corregido y verificado en la fuente**. La clasificación por sociedad de URD 2025 p.341/p.342 coincide con mi lectura independiente: poppler en modo `-layout`, Decimal y la página renderizada.

E2-D4…D9 están cerrados, y los negativos D4/D5 se reproducen con sus códigos reales. El manifiesto verifica 56/56. La lectura es idempotente. Los 44 archivos que decían «PROVISIONAL» están actualizados.

Siguen abiertos dos hallazgos nuevos que el autor no podía conocer por el encargo:

1. La cita del factsheet **«4-year contracts: Monthly fixed fee»** casa por un artefacto del extractor. Lo impreso es «4-year contracts: Volume-based **or** Monthly fixed fee».
2. La reproducción sin red **sobrescribió la procedencia** del índice de descargas publicado en Git. Los campos `fecha_descarga`, `http` y `url_final` ahora son sintéticos.

Hay además residuos menores en D1, D2, D3 y D5.

M1, M2, M6 y N2 siguen **ABIERTOS** y Elis sigue `pendiente_de_datos`. No se elige R, θ, λ, k, probabilidad ni ningún umbral.

## Material y verificaciones previas

| Comprobación | Resultado | Prueba |
|---|---|---|
| `git fetch` de las dos ramas | `origin/mistral/e-fuentes-elis` = `ea641e7`; `f00c5dd` es ancestro directo (1 commit) | `git rev-list --count f00c5dd..ea641e7` = 1 |
| Ámbito del commit | 57 archivos, **0 fuera** de `resultados_cierre/elis_fuentes/` | `git diff --name-only f00c5dd ea641e7` |
| Release `fuentes-elis-e-20261117` | `gh release download` falla en este entorno (GraphQL 403). Descargué los 13 assets uno a uno con la API REST (`gh api …/releases/assets/<id>`). `sha256sum -c SHA256SUMS` → **11/11 OK** | `sondas/release_assets.tsv` |
| URD 2025 | La copia local de base-4.14 tiene sha256 `04bfd087…` (igual al índice) | `s01`, `s09` |
| ZIP base-4.14 | sha256 `bb51942c…` | `s01` (verificar_base_4_14 → exit 0) |

## Clasificación de E2-D1…D9

| | Estado | Evidencia (archivo:línea · página del PDF) |
|---|---|---|
| **E2-D1** (central) | **CERRADO_CON_LIMITES** | Núcleo correcto y verificado (detalle en la sección siguiente). Queda un residuo de rótulo: LECTURA l.57 (cita 45) sigue diciendo «37,3 = compras pequeñas 2025», en el mismo registro que ya separa 3,6 de earnouts (→ E3-3) |
| **E2-D2** | **CERRADO_CON_LIMITES** | Las cinco afirmaciones tienen cita atómica registrada: [3] l.16 comunicado FY2025 p.6; [4] l.18–19 presentación FY2025 p.29; [20] l.36 factsheet p.1; [23] l.40 Q3 2026 p.3; [24] l.42–43 URD p.313. Límites: (a) en [20], «de ventas» se infiere de la maquetación. El bloque se titula «Our activity» y no dice «revenue»; el hallazgo lo reconoce («maquetación»). (b) La cita base de [20] (l.35) lee mal la página (→ E3-1) |
| **E2-D3** | **CERRADO_CON_LIMITES** | HALLAZGOS l.7, LECTURA l.20 y PREGUNTAS M1 lo rotulan como corroboración de base, y `verificar_base_4_14.py` da exit 0 (semestral 2026 EN `3919657f…`, p.10). Residuo: `PUNTO_DE_RECUPERACION.md` l.17 conserva «H1-2026 19,5% **nuevo**», que es uno de los tres sitios originales de f00c5dd (l.16). Además, `tipo_evidencia` = «nueva» en LECTURA l.14 (brochure p.15, capex 823,9/887,4/890,2 = URD p.312) y l.20, sin rótulo de corroboración en el hallazgo de l.14 (→ E3-4) |
| **E2-D4** | **CERRADO** | Reproducido en una copia desechable (`s12`). Con 1 PDF ausente, exit 1 y el índice de Git queda idéntico (`74cbae82…` antes y después). Con sha256 vacío, la lectura falla con exit 1. Con un PDF alterado en `.trabajo`, la lectura falla con exit 1 (sha recalculado). Problema nuevo relacionado: una reproducción **correcta** en modo local reescribe el índice con procedencia sintética (→ E3-2) |
| **E2-D5** | **CERRADO** | Exit reales reproducidos (`s12`): `descargar` sin fitz → 3; `lectura` sin fitz → 3; `verificar_segundo_extractor` sin pypdf → 3; `inventario` sin `716cbd6` → 2, con el `git fetch` exacto impreso. `requirements.txt` declara `pymupdf==2.1` y `pypdf==7.1.0`. La docstring de `inventario_bloque1.py` l.9–13 declara la red y `base414.zip`. Residuo documental: `pruebas_e2/NEGATIVOS_E2.txt` l.19 y l.24 registran «exit=0 (esperado 3)», lo que contradice la propia respuesta (→ E3-5) |
| **E2-D6** | **CERRADO** | `PUNTO_DE_RECUPERACION.md` l.11 → `23718fb`, l.12 → `f00c5dd`, y l.13/l.26 «este commit» solo para el bloque 6. `ENTREGA.json` l.6, l.12, l.25 y l.152 citan `f00c5dd`; l.7 dice que el commit no se autorreferencia |
| **E2-D7** | **CERRADO** | `grep -rniE 'sin cifra publicada\|no publica la tasa\|ninguna tasa ni importe publicado'` solo encuentra meta-menciones de la corrección (ENTREGA l.39, lectura_bloque2.py l.344, RESPUESTA_E2) (`s14`) |
| **E2-D8** | **CERRADO** | La cabecera del índice y la de `FUENTES_Y_BUSQUEDA.csv` ya no tienen `version`, y 0 apariciones de `93a9780` (`s14`). La fecha del documento sigue en `fecha` |
| **E2-D9** | **CERRADO** | 0 apariciones de «Warts cherei»/«Wärtscherei» fuera de las meta-menciones de la corrección (RESPUESTA_E2 l.60/63, ENTREGA l.41, adenda de RESPUESTA_E1 l.97) (`s14`) |

### E2-D1 en detalle: prueba de cierre contra URD 2025 p.341/p.342

Leí la tabla «CASH FLOWS FROM ACQUISITIONS» con poppler `-layout`, que es distinto de PyMuPDF y de pypdf. Sumé con Decimal (`sondas/s09_d1_tabla_p341.py`, `.out`) y la comprobé contra la página renderizada (`sondas/img/urd2025_p341_tabla2025.png`, pie de página impreso 339 = p.341 del PDF).

| Criterio de CORRECCION_E2 | Fuente | Entrega `ea641e7` | ¿Conforme? |
|---|---|---|---|
| Seis importantes de 2025 que suman 60,8 | p.306 lista Bodensee, Bugadería Neutral, Larosé, **Acquaflash**, JP Muller y Adrett. p.341 NET CASH FLOW: 8,9 + 13,2 + 10,2 + 7,0 + 11,8 + 9,7 = **60,8** | HALLAZGOS l.22–23; LECTURA l.53 (cita 41), l.58 (cita 46) y l.57 (cita 45); `comprobar_clasificacion_m6.py` exit 0 | Sí |
| Lavartex, solo earnout 19,7 | p.341: desembolso «-», earnout (19,7), neto (19,7). p.342 (2024): desembolso «-», earnout (83,2) | HALLAZGOS l.22; LECTURA l.59 (cita 47) y l.60 (cita 48) | Sí |
| Other 37,3, de los que 3,6 son earnouts | p.341: Other: caja 4,9, desembolso (38,5), earnout (3,6), neto (37,3). Earnouts totales 23,3 = 19,7 + 3,6 | HALLAZGOS l.23; LECTURA l.60 (cita 48); RESUMEN l.8 y l.16 | Sí (residuo en cita 45, E3-3) |
| Total 117,6 | Suma de columnas 117,8 frente al impreso (117,6); la diferencia de 0,2 es redondeo (también la fila de desembolsos da 112,5 frente a 112,6) | HALLAZGOS l.23 y RESPUESTA l.14 lo declaran como redondeo de 0,2 | Sí |
| Carsan y Ernst, importantes de 2024 | p.341 «Acquisitions during the previous financial year» → «Major acquisitions»: Carsan (28-nov-2024; 9,7 M€) y Ernst (18-dic-2024; 19,0 M€). p.342: columnas propias en las dos tablas de 2024 (neto 8,1 y 20,6) | HALLAZGOS l.22; LECTURA citas 49–54 | Sí |

Corroboración que la entrega no usa: la nota 5 de la presentación FY2025 p.29, que va unida a la línea (117,6), dice «Final earn-out related to the 2022 Mexican acquisitions paid in 2025 (€20m vs. €83m in 2024)». Esa nota identifica la compra anterior a la que corresponde el 19,7. LECTURA l.60 (cita 48) dice «No identifica a qué compra anterior corresponden los 19,7». Es cierto para p.341, pero la fuente ya está entre las descargadas. No la exijo; queda como mejora opcional (E3-6).

## Hallazgos nuevos

### E3-1 (media) · Factsheet 2026 p.1: la cita casa por un artefacto del extractor y el hallazgo lee mal la página

- **Registrado:** LECTURA l.35 (cita 23), con patrón `4-year contracts: Monthly fixed fee` y hallazgo «contratos de 4 años con tarifa fija mensual (workwear = 37% de ventas)». Se repite en PREGUNTAS l.3 (M2), HALLAZGOS l.15 y `lectura_bloque2.py` l.134.
- **Impreso** (página renderizada, `sondas/img/factsheet_p1_actividad.png`): «**4-year contracts:** Volume-based **or** Monthly fixed fee». Es una banda horizontal bajo las tres actividades (Flat Linen 47%, Workwear 37%, Hygiene & well-being 16%), no una característica de Workwear.
- **Por qué pasa la verificación:** PyMuPDF y pypdf sacan «Volume-based» fuera de orden, así que «4-year contracts:» queda pegado a «Monthly fixed fee». poppler, sin `-layout`, da «4-year contracts: Volume-based … or Monthly fixed fee» y el patrón no casa (`s07`, cita 23).
- **Efecto:** M2 sigue ABIERTO y no hay cifra afectada. Pero la afirmación registrada no es lo que dice la fuente, y es el mismo tipo de defecto de lectura de maquetación que D1.

### E3-2 (media) · La reproducción local reescribe en Git la procedencia de las descargas

- En `f00c5dd`, el índice `fuentes_descargadas/INDICE_DESCARGAS.csv` registraba la descarga real desde fr.elis.com: `fecha_descarga = 2026-11-17T08:43:57Z` en las 12 filas.
- En `ea641e7` las 12 filas dicen `2026-11-17T13:22:28Z`, con `http = 200`, `content_type = application/pdf` y `url_final` = URL de fr.elis.com. Esa ejecución fue **sin red** (RESPUESTA l.6 y l.72: `ELIS_PDF_DIR=/tmp/pdf_elis`). Los PDF salieron de la Release, y el URD de la copia de base-4.14.
- **Causa:** en `descargar_fuentes_elis.py`, `descargar_local` (l.92–99) devuelve `200, url, "application/pdf"` sintéticos. La l.113 pone `fecha_descarga = now()`, y la l.169–172 escribe el índice de Git aunque el modo sea local. Ninguna columna registra el modo.
- **Efecto:** el mismo valor pasa a LECTURA (registros de documento), `FUENTES_Y_BUSQUEDA.csv` y la cabecera de los 33 extractos. Las huellas no cambian, así que el contenido sigue siendo el mismo. Pero el índice publicado afirma descargas a las 13:22 que no ocurrieron, y la marca real solo queda en el historial de Git.
- **No es idempotente:** dos ejecuciones seguidas de `descargar` dan índices con sha256 distintos (`d3e82353…` y `7818ab34…`, `s04`). Lo idempotente es lectura + extractos (`c5e42451…` ×2, `s04`).

### E3-3 (menor) · Rótulo «37,3 = compras pequeñas 2025»

LECTURA l.57 (cita 45) y `lectura_bloque2.py` l.224 dicen «37,3 = compras pequeñas 2025». Según p.341, 37,3 es la columna «Other acquisitions»: 33,6 de compras (caja 4,9 menos desembolso 38,5) más 3,6 de earnouts y aplazados. El mismo registro, la cita 48 y HALLAZGOS l.23 ya hacen esa separación, así que el rótulo de la cita 45 la contradice.

Nota para el integrador, sin pedir cambio a E: la media de 31,5 M€/año de F1 (35,3/22,0/37,3, que HALLAZGOS l.21 atribuye a F1 V1) incluye earnouts. En 2024 son 10,7 de los 22,0 (p.342) y en 2025 son 3,6 de los 37,3. La parte de 2023 no la comprobé. No elijo cifra ni tratamiento; queda como dato para M6 y la propuesta 4b.

### E3-4 (menor) · Residuos de D3

- `PUNTO_DE_RECUPERACION.md` l.17: «H1-2026 19,5% nuevo».
- LECTURA l.14 (cita 2, brochure p.15): el capex 823,9/887,4/890,2 tiene `tipo_evidencia` = «nueva» y el hallazgo no dice que es corroboración de URD p.312. HALLAZGOS l.7 sí lo dice.

### E3-5 (menor) · El registro de negativos contradice lo que prueba

`pruebas_e2/NEGATIVOS_E2.txt` l.19 (D5a) y l.24 (D5b) dicen «exit=0 (esperado 3)» seguido de «SystemExit 3». Parece que el arnés atrapó el `SystemExit`. Los scripts dan exit 3 de verdad (`s12`), pero la prueba publicada dice lo contrario.

### E3-6 (opcional) · Cita de la nota 5 de la presentación p.29

La nota 5 identifica la compra anterior del earnout de Lavartex: «Final earn-out related to the 2022 Mexican acquisitions paid in 2025 (€20m vs. €83m in 2024)».

### Observaciones (sin corrección exigida)

- `RESUMEN_PARA_INTEGRADOR.md` l.21 («Para el control») conserva recuentos de E1: «64 registros, 52 citas». Los actuales son 80 y 68.
- `CHECKPOINT_RELEVO.md` l.31, del bloque 5, se editó en el sitio además de llevar adenda. El original sigue en `f00c5dd`. Es aceptable porque el encargo pedía actualizar los 44 archivos.
- `PREGUNTAS_Y_RESULTADOS.csv`: las columnas `estado_tras_bloque2` y `estado_tras_revision_e1` se recalculan con el estado actual (incluido el texto E2-D1). No conservan el estado histórico. Viene de antes y no lo introduce este commit.
- Presentación FY2025 p.29, cita 6 (LECTURA l.18): como en la cita 40, hay un marcador de nota impreso («1») entre «As a % of revenue» y «-18.2%». La cita lo omite y, a diferencia de la cita 40, no lo declara. La nota 1 («Favorable linen price trends combined with effective linen purchasing management») corrobora además [3].

## Comprobaciones 2 y 3 del encargo

| Punto | Resultado | Prueba |
|---|---|---|
| M1, M2, M6 y N2 ABIERTOS | Las cuatro filas de PREGUNTAS (`estado_tras_revision_e2`) empiezan por «ABIERTO». No hay ningún «CERRADO/RESUELTO» aplicado a las preguntas | `s15` |
| Elis `pendiente_de_datos` | En ENTREGA l.142, HALLAZGOS l.40, RESUMEN l.22, PUNTO l.41 y RESPUESTA_E2 l.85 | `s15` |
| Sin R, θ, λ, k ni umbrales | 0 asignaciones. ENTREGA l.142 dice «No se elige R (ni en 736,0-867,2), theta, lambda, k ni probabilidad». `apto_dinero_real` = «No se declara». C48 = 108 se conserva | `s15` |
| Manifiesto | `sha256sum -c` → rc 0. 56 entradas = 56 archivos, sin sobrantes ni faltantes | `s05` |
| Reproducción del pipeline | `descargar` (local) 12/12 exit 0. `lectura` exit 0 (80 registros, 68 citas). 33 extractos. `comprobar_clasificacion_m6` exit 0. `verificar_base_4_14` exit 0. `verificar_preservacion_release --dir` exit 0 (11/11). Todas las salidas son **idénticas a las publicadas salvo la marca de tiempo**, excepto VERIFICACION (por la versión de pypdf) | `s01`, `s03` |
| Idempotencia | Lectura y extractos: sí (2 ejecuciones, mismo sha256 de árbol). Descarga: no, por E3-2 | `s04` |
| Segundo extractor | No pude instalar pypdf 7.1.0 sin red. Con pypdf 6.17.0 local, 65/68: las 3 que fallan son espacios ante puntuación propios de 6.17 («bolt -on», «2025 )», «M&A ,») y el texto está presente (`s02`). Tercer extractor (poppler): 61/68 automáticas, más 7 confirmadas a mano en `-layout` o en la página renderizada (`s07`, `s08`). Con esa misma comprobación salió E3-1 | `s01`, `s02`, `s07`, `s08` |
| Rutas locales | Ningún script tiene rutas fijas (vienen de `ELIS_PDF_DIR`, `--dir` o `RAIZ`). Solo aparecen rutas `/tmp/...` como registro de comandos en NEGATIVOS_E2 l.1/4/5, RESPUESTA_E2 l.72/78 y ENTREGA l.47/113. Es aceptable como documentación | `s11` |
| 44 «PROVISIONAL» | Los 44 archivos que lo decían en `f00c5dd` cambiaron todos. En `ea641e7` quedan 4 apariciones en 3 archivos: dos históricos con adenda (RESPUESTA_E1 l.42/90 y CHECKPOINT l.31, en pasado) y la meta-mención de RESPUESTA_E2 l.67. Índice, LECTURA, FUENTES y los 33 extractos dicen «DESCARGADO_Y_PRESERVADO_EN_RELEASE» | `s06` |

## Lo conforme

- La corrección central de D1: lista, columnas, sumas, earnouts y clasificación 2024, con página y prueba ejecutable.
- Las 68 citas tienen huella correcta (`sha256_doc` = sha recalculado) y casan en su página con PyMuPDF. Además casan con un extractor distinto, salvo E3-1, que casa con dos extractores pero no con lo impreso.
- Las guardas de D4/D5 funcionan, el índice de Git queda intacto ante fallos y las dependencias están declaradas.
- La preservación en la Release está verificada (11/11), y el URD 2025 es el de base-4.14.
- Ámbito respetado: no toca control, producto, main, B/P-M1 ni `integrado_en_producto`.

## Límites de esta revisión

- `gh release download` no funciona en este entorno (GraphQL bloqueado). Usé la API REST de assets, con las mismas huellas.
- Sin red no pude instalar pypdf 7.1.0, así que no reproduje el «68/68» del autor con esa versión. Lo sustituí por pypdf 6.17.0, poppler y la página renderizada.
- PyMuPDF 2.1 se tomó de una instalación local ya existente en esta sesión de coordinación, y no de un venv propio.
- No revisé DEU 2024 p.288 (2023) ni las páginas ajenas a E2-D1…D9 y a los hallazgos nuevos. Revisé solo lo afectado.
- La revisión no aprueba nada económico ni cambia ningún estado de pregunta.
