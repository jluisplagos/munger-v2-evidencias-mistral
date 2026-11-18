# ENTREGA — registro de entradas de Zoetis Inc., primer tiempo (extractor: Mistral)

- **Expediente**: `zoetis_t1b/Zoetis/` (rama `examen/ahold-f1` de `jluisplagos/munger-v2`, solo lectura). Entrega en `jluisplagos/munger-v2-evidencias-mistral`, rama `mistral/examen-zoetis-entradas`, carpeta `resultados_examen/zoetis/`: `verificacion_entradas.json` (315 entradas de la plantilla + 169 auxiliares `aux:` = 484), `fuentes_mercado/` con `HUELLAS.txt`, `DESCARGAS.tsv`, `ENTREGA.md`.
- **Modelo y herramientas reales**: extractor **Mistral (mistral-large-4-0)** actuando como agente Vibe Code. Herramientas: `python3` + `hashlib` (SHA-256), `gh` (GitHub: clone, release, ramas), `web_fetch`/`web_search` (lecturas de mercado), y las funciones de `munger_v2_r1/personaje_v2/scripts/verificacion_entradas.py` como autocomprobación (`_cita_cifra` con signo, `_validar_formula`/`_constantes_no_admitidas`/`_eval_formula_exacta`/`_sensibilidad`, `_importe_libro_exacto`, `_contiene_texto`). El xlsx del libro no está en Git, así que `comprobar` completo no se ejecuta; la autocomprobación por entrada usa las mismas funciones del producto sobre cada cita/página/sha/fórmula. Fecha de extracción: **2026-11-18**.
- **Autocomprobación**: 484 entradas, **0 errores** (cita localizada en la página citada y cifra leída con su signo; escala coherente con la unidad; signo×escala×valor_fuente = valor del libro; fórmulas con todos sus orígenes y solo ellos, cada uno influyente, sin constantes no admitidas). Las **30 hipótesis** de la plantilla quedan **intactas** (las escriben las fases del personaje). Todas las comprobaciones quedan `resultado: "pendiente"`, `revisor: null`, sin `vinculo`: el extractor no sella ni aprueba su propio trabajo.

## Fuentes documentales

Los **12 PDF oficiales** del expediente (10-K 2016–2025 y 10-Q T1/T2 2026) se descargaron de la Release `fuentes-examen-20261118` (`gh release download`): **SHA-256 coincidente 12/12 con `FUENTES.tsv` y con `RELEASE_FUENTES_EXAMEN_SHA256SUMS`** (ver `DESCARGAS.tsv`; los bytes coinciden con los assets de la release). No se commitean PDFs (AGENTS.md). Corte del primer tiempo: solo documentos publicados hasta el 9-oct-2026 — el `zoetis-10q-2026-q3.pdf` de la release queda **fuera** y no se usa. Cada fuente local cita `texto/<informe>.txt` con su sha256; las citas son líneas literales de la página `[PDF PAGE n]` citada. Textos 2020–2024 (OCR): cada cifra de esos años se comprobó contra la segunda lectura verificada (rama `mistral/zoetis-texto-ocr`); citas y páginas las del `texto/` del expediente. **1 incidencia**: `aux:...fy2021_p63_current_portion_of_long_term_debt_2020` — artefacto OCR «—_—» en p. 74 que impide leer el signo de 600; se cita la misma cifra en p. 63 del mismo texto, donde el guion de la otra columna se lee como cero y el signo de 600 es inequívoco.

## Datos de mercado (conservados en `fuentes_mercado/` con `HUELLAS.txt`)

- **Precio C37 = 73,08 USD**, cierre NYSE del 8-oct-2026: **verificado** en la página oficial de la empresa (investor.zoetis.com, tabla «XNYS:ZTS historical stock data», fila `October 08, 2026 $73.08`), conservada como texto con SHA-256. La página de la bolsa (nyse.com) bloquea el acceso automatizado; se usa la página de la empresa, como permite el encargo. En esa fecha no hay dividendo pendiente de pagar ($0.53 declarado el 8-oct-2026, ex-date 30-oct-2026). **C41** = round(73,08 × 424,928, 1) = 31.053,7 mm USD, con acciones en circulación 424.927.535 al 31-dic-2025 (10-K 2025 p. 68).
- **Tasa sin riesgo C57**: Treasury 10 años del 8-oct-2026 = **5,22 %, verificado** en el CSV oficial del U.S. Department of the Treasury («Daily Treasury Par Yield Curve Rates», home.treasury.gov, fila 10/08/2026, columna «10 Yr»), conservado como texto con SHA-256. El 5,22 % que salía de un resultado de búsqueda sin verificar queda así confirmado contra la fuente oficial.
- **Lecturas externas de terceros, no comprobadas** (conservación `externa`, 4 campos declarados, sin bytes): C38 valor intrínseco 197,36 USD (Simply Wall St) y C88 P/FCF 47,1x (Digrin) según `datos_v63.md`; la relectura del 2026-11-18 no reprodujo esos valores. C7 sector Damodaran «Drugs (Pharmaceutical)» (mgnroc.html, enero 2026), extracto conservado.

## Cómputo por clase (285 entradas del alcance + 169 auxiliares)

| clase | alcance (285) | auxiliares | total |
|---|---|---|---|
| dato_publicado | 159 | 164 | 323 |
| derivado | 64 | 0 | 64 |
| cero_comprobado | 21 | 5 | 26 |
| dato_ausente | 24 | 0 | 24 |
| convencion | 10 | 0 | 10 |
| no_aplicable | 1 | 0 | 1 |
| sin resolver (clase null, declaradas) | 6 | 0 | 6 |
| hipótesis (sin tocar) | 30 | 0 | 30 |

## Entradas sin resolver (clase null, declaradas; no se forzó cita ni fórmula)

- `Análisis!C24` ROIC TTM 26,6 %, `C26` CFO/beneficio 1,058, `C33` deuda neta/EBITDA 1,92x, `C40` FCF TTM 2.365, `C42` EV/EBITDA 9,57x: exigen el 10-Q T2-2025, que **no está en el expediente**; no reproducibles solo con la Historia FY2016–2025 y los 10-Q 2026 del expediente.
- `Análisis!C60` CAGR de acciones −0,015: la fórmula admite solo enteros 1–12, potencias de diez y `round` (no potencias); no se fuerza.

## Criterios declarados en casos especiales

- **Acciones «miles»**: la partida declara «miles» por una limitación del programa; se registra la cifra impresa con su escala real (ej. «470.385» = 470,385 millones de acciones, unidad «millones de acciones», escala 1; auxiliar de circulación 424.927.535 acciones con escala 1e-6 en C55).
- **US GAAP arrendamientos**: los operativos van en el CFO sin principal en financiación; los financieros (~1 mm/año) en deuda/C49. C48 = media 2023–2025 de ceros comprobados (intereses en financiación: US GAAP los lleva en CFO). `Historia!I17` = cero comprobado (guion en columna 2022 del 10-K 2024, p. 86); `Historia!K17` = 1 (10-K 2025, p. 89, columna 2024); `Historia!L17` = dato ausente (libro vacío). Filas 85–87 (perímetro de reinversión, D&A rou/ppa) = dato ausente: Zoetis no publica ese desglose.
- **C46/C47/C49/C50** registradas como `derivado` (media 2023–2025 de componentes publicados) según `configuracion/cambio_zoetis_t1.json`; C48 sin cálculo declarado = media de ceros.
- `Historia!E26` (minoritarios 2018): libro vacío → `dato_ausente` (vacío no es cero). `Control maestro!D5` (ratio ADR) = `no_aplicable`: el precio es el de la acción ordinaria ZTS en NYSE, no un ADR.
- Moneda/unidad/norma de texto (USD, mm, US GAAP) con `equivalencia` declarada contra la cabecera del 10-K 2025 (p. 66) y la nota 1 (p. 45).
