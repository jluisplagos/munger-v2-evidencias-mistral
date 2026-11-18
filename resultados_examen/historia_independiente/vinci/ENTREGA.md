# Entrega · Ventana 3 (VINCI SA) · Historia de diez años independiente

## Qué hice
- Ventana 3 del encargo M4: **VINCI SA, ejercicios 2016–2025**, extracción literal e independiente de las 24 partidas de la plantilla (`01_historia_2016.md` de `munger-v2`, rama `examen/ahold-f1`).
- Fuentes: los 10 PDF de VINCI de la release `fuentes-examen-20261118` (`vinci-annual-report-2016…2019.pdf`, `vinci-urd-2020…2025.pdf`). **SHA-256 verificados OK** contra `coordinacion/cierre_v2/examen/RELEASE_FUENTES_EXAMEN_SHA256SUMS`. No usé los PDF de 2026 ni ninguna carpeta del expediente en `munger-v2`.
- Regla de informe: para cada año N uso la **columna comparativa del informe N+1** (recoge reexpresiones: NIIF 15/9 en el informe 2018, NIIF 16 desde 1-ene-2019, interpretación IFRS IC dic-2019 reflejada en el URD 2020, IFRS IC mayo-2021 en el URD 2021, asignación final del precio de Cobra IS en el URD 2022). El año **2025 usa el informe 2025** (no hay informe 2026 en las fuentes de la ventana). Cada fila de `HISTORIA.csv` lo anota en `informe_usado`.
- Documento usado: **cuentas consolidadas** de cada informe (cuenta de resultados, balance, estado de flujos y notas 7.2, 8 y 21). Página = página del PDF (la del visor). Unidad: millones de EUR, salvo `acciones_diluidas` (unidades).
- `HISTORIA.csv`: 318 filas (partida × año × componente), con valor impreso, signo, archivo, SHA-256, página, cita literal, estado y nota. Verifiqué con script que cada `valor_impreso` aparece en la página citada del archivo citado.

## Lo que no encontré y por qué
- `id` (I+D): `no_encontrado` en los 10 años. VINCI no publica línea de gasto de I+D ni en la cuenta ni en las notas; solo menciones cualitativas y un presupuesto de unos €50 M (URD 2020–2025; URD 2025 p. 24: «R&D spending was approximately €50 million in 2024 and 2023», dato aproximado no reconocido como partida de resultados).
- `resultado_antes_impuestos`: la cuenta de resultados de VINCI **no imprime subtotal de BAI**. Tomo la nota 7.2 («Income before tax and income/(loss) of companies accounted for under the equity method»), que excluye el resultado de participadas; en `nota` doy el BAI estricto de la cara (nota + participadas).

## Dudas de definición y cómo las resolví
- `ventas` = línea «Revenue (*)» (excluye obras de concesiones hechas por no-Grupo); «Total revenue» queda en nota.
- `ebit` = subtotal impreso «Operating income» (también impresos «Operating income from ordinary activities» y «Recurring operating income», en nota).
- `ebit_derivado` = BAI (nota 7.2) + resultado de participadas (suma +1, porque en la cuenta de VINCI va dentro de la explotación) − cada línea del resultado financiero (signo −1; no uso el subtotal «Cost of net financial debt» para no duplicar). Resultado = «Operating income» impreso.
- `capex` = compras brutas «Purchases of PP&E and intangible assets» (el neto «Operating investments (net of disposals)» en nota).
- `adquisiciones` = subtotal neto impreso en la cara del estado de flujos: «Net effect of changes in scope of consolidation» (2016–2017) y «Net financial investments» (2018–2025; desde 2021 se desglosa aparte «Cash and cash equivalents of acquired companies»). Cambio de rótulo anotado en `nota`.
- `deuda` = Bonds + Other loans and borrowings + Current borrowings (componentes, corriente + no corriente), **sin** pasivos NIIF 16 (líneas aparte desde 2019) ni derivados.
- `arrendamientos` = cero con evidencia antes de 2019 (NIIF 16 desde 1-ene-2019; el balance del informe 2019 muestra «-» en 31/12/2018); desde 2019, «Non-current lease liabilities» + «Current lease liabilities».
- `arrendamientos_principal` = principal según la nota 21 de cada informe («repayments of lease liabilities: decrease of €X million»); la cara del estado de flujos imprime principal + gasto financiero combinados (anotado en nota). Cero antes de 2019.
- `intereses` = «Net interest paid» (en explotación) → `intereses_financiacion` = cero con evidencia en los 10 años.
- `otros_activos_financieros` = «Other current financial assets» + «Cash management financial assets» (sin derivados corrientes, que no son depósitos ni inversiones temporales).
- `circulante_lineas` = la única línea de variación del circulante impresa en el estado de flujos («Changes in operating working capital requirement and current provisions»); el desglose está en la nota 19.1.

## Modelo y herramientas usadas de verdad
- Modelo: **mistral-large-4-0** (agente Vibe Code). Herramientas: `gh` CLI (descarga de la release y API), Python 3.12 + **PyMuPDF 2.1** (extracción de texto por página de los PDF), `sha256sum`, `grep`/`rg` y scripts propios de verificación. Sin LibreOffice. PDF fuera de Git.
