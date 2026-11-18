# Entrega M4 · ventana 5 (Ahold Delhaize) · contraste contra la extracción de Claude

## Qué hice
Contrasté las **210 cifras** (21 partidas × ejercicios 2016–2025) de `historia.partidas.<partida>.valores` en `fase1_v63.json` (repo `jluisplagos/munger-v2`, rama `examen/ahold-f1`, carpeta `…/2026-11_examen_universo/ahold_f1/Ahold/`) contra los textos ya extraídos de esa misma carpeta (`texto/AD_annual-report-2016.txt` … `AD_annual-report-2025.txt`, marcas `[PDF PAGE n]`), comprobando cada valor **en la página citada** en el campo `fuente` de cada partida y año (normalmente la columna comparativa del informe del año siguiente). No abrí ningún PDF ni el libro `Ahold_v63_datos.xlsx` (no está en Git) y no escribí nada en `munger-v2` (clonación sparse de solo lectura).

## Método
- Búsqueda literal del valor tokenizado (signo, paréntesis, separador de miles) en la página citada; la cita es la línea de la tabla donde aparece.
- Si el total no está impreso (partidas derivadas: `deuda`, `arrendamientos` desde 2020, `adquisiciones`, `circulante`, `tipo_impositivo`, `ebit` derivado), verifiqué **componente a componente** que la línea y el impreso están literalmente en las páginas citadas (usando `fase1_partes/AR_*.json` solo como localizador de líneas) y recalculé el agregado con la definición de la plantilla (`01_historia_2016.md`).
- Los ceros (`arrendamientos` 2016–2017, `minoritarios` 2016–2025) se verificaron con su cita literal en la página citada.

## Recuento (filas RECUENTO al final del CSV)
**210 cifras → coincide si: 199 · no: 1 · no_se_encuentra: 10**

- Único **no**: `ebit` 2019 = 2663 en fase1_v63; en la página citada (`AD_annual-report-2020.txt` p.145) el subtotal impreso *Operating income* es **2,662**. El 2663 es el EBIT derivado (BAI 2,134 − resultado financiero −529), verificado componente a componente en esa página; diferencia de 1 entre el derivado y el impreso (redondeo/definición v2.2).
- Los 10 **no_se_encuentra**: `id` (I+D) en los diez años — `null` en fase1_v63 con fuente «desconocido»; los informes no publican un gasto de I+D cifrado.

## Convenciones observadas (anotadas en `nota`, no como discrepancias)
`capex`, `intereses`, `intereses_financiacion` y `arrendamientos_principal` se guardan en positivo en fase1_v63 y se imprimen entre paréntesis en el estado de flujos (p. ej. `(1,302)`).

## Dudas de definición
En fase1_v63 `ebit` es el EBIT derivado (BAI − resultado financiero, v2.2), no siempre el subtotal impreso; `tipo_impositivo` = impuestos/BAI (derivado); `deuda` excluye los pasivos NIIF 16 (van en `arrendamientos`) e incluye los arrendamientos financieros IAS 17 de 2016–2018.

## Modelo y herramientas usadas de verdad
Modelo `mistral-large-4-0` (Mistral) vía Vibe Code. Herramientas deterministas locales: `git`/`gh` (clonación sparse de solo lectura del repo auxiliar) y `python3` sobre los `.txt`/`.json` extraídos. Sin acceso a los PDF, sin internet, sin LibreOffice ni pipeline. No aprobé mi propio trabajo; sin valoraciones ni recomendaciones.
