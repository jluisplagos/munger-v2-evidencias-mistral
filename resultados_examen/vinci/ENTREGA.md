# ENTREGA — registro de entradas de VINCI SA (examen del personaje)

- **Expediente:** `vinci/Vinci` en `jluisplagos/munger-v2`, rama `examen/expedientes-f1` (solo lectura). Entrega en `jluisplagos/munger-v2-evidencias-mistral`, rama `mistral/examen-vinci-entradas`, carpeta `resultados_examen/vinci/`. Fecha de extracción: **2026-11-19**.
- **Modelo y herramientas reales:** extractor **Mistral (mistral-large-4-0)** como agente Vibe Code. Herramientas: `python3` (`requests`, `hashlib`, `json`; `pypdf` instalado con pip para lecturas puntuales; `curl`/`wget` bloqueados por el sandbox), `gh` CLI, y funciones de lectura del producto en modo lectura (sin ejecutar el pipeline ni macros; XLSX solo en lectura). Las citas se contrastaron contra las páginas `[PDF PAGE n]` de los textos del expediente con mi propio código.
- **Autocomprobación:** 315 entradas de la plantilla presentes, sin repetir ni sobrar, más 162 auxiliares `aux:` (477 en total). Cada `cita` está en su página `[PDF PAGE n]`; cada sha256 de texto coincide con `FUENTES.tsv`; `signo × escala × valor_fuente = valor_modelo` en toda entrada con fuente; toda fórmula reproduce el valor del libro (fracciones exactas). Las 30 hipótesis de la plantilla se dejan sin tocar. Todas las comprobaciones quedan `pendiente`, `revisor: null`, sin `vinculo`: no sello nada.

## Fuentes documentales

Los 12 PDF oficiales VINCI (informes anuales 2016–2019, URD 2020–2025, semestral e intermedios a 30-jun-2026) se descargaron de la Release `fuentes-examen-20261118`: **12/12 con SHA-256 coincidente** con `RELEASE_FUENTES_EXAMEN_SHA256SUMS` (ver `DESCARGAS.tsv`). No se usan los PDF de 9M-2026 (22-oct-2026, fuera del corte del 10-oct-2026). No se commitean PDFs. Los URD 2021–2023 son de doble página: `pagina` es la del visor (marca `[PDF PAGE n]`), el texto va por mitades.

## Datos de mercado (oficiales, en `fuentes_mercado/` con `HUELLAS.txt`)

- **Precio C37 = 107,05 €:** cierre **no ajustado** oficial de Euronext Live (FR0000125486-XPAR, `adjusted=N`), fila **09/10/2026;…;107.05;107.05;…** — coincide con el libro. En esa fecha hay dividendo a cuenta de 1,10 € pendiente (ex 13-oct-2026, según la etapa 1): cotizaba con derecho.
- **Bund 10 a (C57):** el libro trae **3,486 %** (etapa 1, Investing.com). Fuentes oficiales conservadas: **Bundesbank** (UMU 9–10 a, BBSIS) da **3,46 %** el 2026-10-09; **BCE** (curva AAA euro, spot 10Y) da **3,5112 %**. Ninguna da 3,486 % → **C57 queda sin resolver** (no se pone otra fuente sin avisar).
- **Sector Damodaran (Palancas!C7):** página `mgnroc.html` (enero 2026) conservada; fila «Engineering/Construction».

## Cómputo por clase (285 entradas del alcance = 315 − 30 hipótesis; + 162 auxiliares)

| clase | entradas (285) | auxiliares |
|---|---|---|
| dato_publicado | 153 | 162 |
| derivado | 74 | 0 |
| dato_ausente | 30 | 0 |
| no_aplicable | 10 | 0 |
| convencion | 8 | 0 |
| hipotesis (C85, capa F1) | 1 | 0 |
| **sin resolver (clase null, declaradas abajo)** | **9** | 0 |

## Entradas sin resolver (no se forzó ninguna cita)

- `Análisis!C40` (7.228): el libro guarda el FCF LTM de la etapa 1; con la definición C46–C52 declarada la mejor fórmula da exactamente **4.132** (diferencia 3.096).
- `Análisis!C57` (3,486 %): Bund oficial 3,46 % (Bundesbank) / 3,5112 % (BCE) el 9-oct-2026; no coincide.
- `Análisis!C26` (2,31): no se reproduce exacto (2025: 11.886/4.903 = 2,424; media 2021–25 = 2,407).
- `Análisis!C60` (−0,002): CAGR 2022–25 = (L20/I20)^(1/3)−1; la potencia no está admitida en el formato de fórmula.
- `Análisis!C38` (111,79 €): Simply Wall St, lectura externa sin bytes (no cuenta como comprobada, R2).
- `Análisis!C28, C31, C34` («Estable»/«No»/«Sí»): veredictos de texto de la etapa 1, no cifras publicables en una línea.
- `Análisis!C88` (9,7x): P/FCF histórico de la etapa 1 (texto URD 2019–2025), sin línea única que lo contenga.

## Dudas y convenciones declaradas

- **EBIT derivado** (fila 7, los 10 años): la cuenta no imprime el BAI; cada componente se registra con su signo impreso (aux `…_ebit`): EBIT = NI − impuesto − coste deuda neta − otros financieros; coincide con «Operating income» salvo ±1 de redondeo.
- **Ceros 2016–2018** de arrendamientos (fila 23), principal (fila 17) e intereses de arrendamiento (fila 16): `no_aplicable` (antes de la NIIF 16), con cita de respaldo de la norma aún no aplicada; la cita no imprime un 0, así que no es `cero_comprobado`.
- **Deuda (fila 22)** imprime en negativo: `signo −1` la pasa a la magnitud positiva del libro. **Circulante (fila 14)**, **adquisiciones (fila 13)** y **SBC (fila 18)** igual con su signo.
- **Acciones diluidas (fila 20):** aux en unidades (escala 1e-6), fórmula `round(aux, 4)` (el libro redondea a 4 decimales; declarado en la fórmula).
- **C55:** 555.967.094 acciones en circulación a 31-dic-2025 (URD 2025 PDF p. 346), P-O2 (a), sin dilución.
- **Desalineación de fechas declarada** (Z-ACC): precio 9-oct-2026 (C37/C41/C42) con balance y EBITDA LTM a 30-jun-2026 (C32/C33/C42/C53/C54) y acciones a 31-dic-2025 (C55).
- Folios en `null` (no se infieren; `pagina` es la del visor). Perímetro: consolidado.

Esto no acredita aptitud para dinero real.
