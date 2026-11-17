# ENTREGA — registro de entradas Ahold Delhaize (extractor: Mistral)

- **Expediente**: `ahold_4_15` (rama `examen/ahold` de `jluisplagos/munger-v2`). Entrega en `jluisplagos/munger-v2-evidencias-mistral`, rama `mistral/examen-ahold-entradas`, carpeta `resultados_examen/ahold/`.
- **Modelo y herramientas reales**: extractor **Mistral (mistral-large-4-0)** actuando como agente Vibe Code. Herramientas: `python3` + `urllib` (descarga de PDF y datos de mercado; `curl` está bloqueado en el sandbox), `hashlib` (SHA-256), `gh` (GitHub), y las funciones de `munger_v2_r1/personaje_v2/scripts/verificacion_entradas.py` (`_cita_cifra`, `_eval_formula_exacta`, `_validar_formula`/`_sensibilidad`/`_constantes_no_admitidas` y `comprobar` con el universo reconstruido desde la plantilla, porque el xlsx no está en Git). Sin LibreOffice ni ejecución del pipeline. Fecha de extracción: **2026-11-17**.
- **Autocomprobación**: cada cita se contrastó con `_cita_cifra` (con signo) contra la página `[PDF PAGE n]` del texto conservado; `comprobar` sobre una copia del expediente con este registro da: 288 entradas presentes, 0 repetidas/sobrantes/sin entrada, **0 discrepancias, 0 desactualizadas, 0 errores** salvo los 11 sin resolver declarados abajo y las 30 hipótesis de la plantilla ( intactas, las escriben las fases del personaje). Todas las comprobaciones quedan `resultado: "pendiente"`, `revisor: null`, sin `vinculo`: el extractor no aprueba su propio trabajo.

## Fuentes documentales

Los 10 informes anuales oficiales se descargaron de `media.aholddelhaize.com` (URLs de `INDICE_FUENTES.csv`): **HTTP 200 y SHA-256 coincidente con el índice 10/10** (ver `DESCARGAS.tsv`). No se commitean PDFs (AGENTS.md). Cada fuente local cita `texto/<informe>.txt` con su sha256; las citas son líneas literales de la página citada.

## Datos de mercado (oficiales, conservados en `fuentes_mercado/` con `HUELLAS.txt`)

- **Precio**: Euronext Live, histórico **no ajustado** de NL0011794037 (XAMS), sesión más reciente **17/11/2026, cierre 35,14 EUR**; la fila que usa el libro (C37 = 36,05) es **13/11/2026**. En esa fecha **no hay dividendo pendiente de pago**: los dividendos 2026 (ex-dates 10/04/2026 y 07/08/2026; pagos 23/04/2026 y 27/08/2026, interino 0,51 EUR) ya se pagaron (página oficial de dividendos, conservada).
- **Bund 10 años**: Deutsche Bundesbank (BBSIS), Umlaufrendite 9–10 años diaria: **2026-11-17 = 3,34 %** (fila usada por C57: 0,01 × 3,34 = 0,0334). Complemento conservado: estructura de plazos Svensson punto 10,0 y = 3,42 % el mismo día. No se usó el ECB (su data-api pedía verificación de bot para series diarias; no se sustituyó en silencio).

## Cómputo por clase (258 entradas del alcance = 288 de la plantilla − 30 hipótesis intactas; + 166 auxiliares `aux:`)

| clase | entradas (258) | auxiliares |
|---|---|---|
| dato_publicado | 165 | 166 |
| derivado | 55 | 0 |
| cero_comprobado | 12 | 0 |
| dato_ausente | 13 | 0 |
| no_aplicable | 2 | 0 |
| **sin resolver (declaradas abajo)** | **11** | 0 |

## Entradas sin resolver (clase null, declaradas; no se forzó cita)

- `Historia!F7` (ebit 2019 = 2.663 en el libro): todos los informes imprimen **2.662**; no aparece 2.663 en ninguna fuente → posible errata del pipeline; no se fuerza.
- `Análisis!C24, C26, C32, C33, C42, C60, C88, C96` (juicio numérico): valores del libro con apoyo narrativo en `datos_v63.md` pero sin una línea publicada única que los contenga; no se encontrá cita → se declaran sin resolver.
- `Palancas!C45, C46` (46339, 46019): son fechas como seriales de Excel (2026-11-13, 2025-12-28); ningún texto de fuente puede contener el serial → sin resolver.

## Dudas de concepto/columna resueltas con criterio declarado

- Años 2020–2022 (`Historia!G5:H5:I5`): las cabeceras del estado de resultados usan etiquetas de fecha ("53 weeks ended January 3, 2021"), no el año; se citó la columna del año en tablas plurianuales del mismo informe (AR2021 p.114, AR2022 p.53, AR2023 p.214).
- Minoritarios 2018–2020 (ceros): AR2018/2019/2020 no imprimen línea de NCI con guion; se citó el estado de cambios en patrimonio (guiones; resultado atribuible íntegramente a comunes) junto a la frase de política "does not have subsidiaries with non-controlling interests that are material".
- Arrendamientos 2016–2017 (ceros): NIIF 16 aún no vigente; se citan los guiones de `Finance lease liabilities` (NIIF 17) y las notas de norma futura.
- `Palancas!B30`: residual `round(1 - B28 - B29, 4)` porque el libro fuerza que los pesos sumen 1,0000 (la razón publicada 19.371/92.352 redondearía a 0,2098).
- `Análisis!C40` (FCF LTM 1.821): derivado exacto con 12 orígenes publicados (Q2-2026 p.15 y AR2025 p.216): 6.598 − 2.566 − 271 − 1.940.
- `Análisis!C57`: serie UMU 9–10 y (3,34 %); la ZST 10,0 y da 3,42 % el mismo día y se conserva como complemento.
