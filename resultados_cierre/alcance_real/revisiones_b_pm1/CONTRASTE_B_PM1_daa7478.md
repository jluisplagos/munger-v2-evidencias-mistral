# Contraste documental B-PM1 @ daa7478 (rama mistral/m2-fundamento-pm1)

- **Revisor**: sesión Mistral C/F. **Límite de independencia declarado**: el autor es «Mistral B (autor previo)» — **misma familia de modelo (Mistral), sesión distinta**. No soy un tercero de otra familia; mi aporte es método distinto (extracción por posición/slots, no por las ventanas regex del autor), hashes y re-ejecución, no una opinión de otro modelo. Modelo real: `mistral-large-4-0` (Vibe Code). Herramientas: git/gh CLI y Python 3.12 stdlib. Nada instalado; no se ejecutó LibreOffice ni el pipeline.
- **Objeto**: commit `daa74783d2708fcd46ca7c24ae1ffbb327c35784` (HEAD de `mistral/m2-fundamento-pm1`), dossier `resultados_m2/pm1/`. No toqué esa rama ni ningún otro frente.
- **Encargo (CONTROL.json B-PM1)**: contrastar las nueve altas PP&E corregidas con notas/cabeceras; conservar la no-identificación de θ/λ. No elegir θ/λ, no repetir toda la investigación.

## Veredicto

### B1 — las nueve altas PP&E vienen de la nota correcta: CONFIRMADO por extracción independiente

Mi propio extractor (`evidencias/extraccion_independiente_pm1.py`, método distinto al del autor: localiza la nota por título, la tabla del año por su línea de cabecera, la fila total de Coste tras «Work in progress» y lee el slot 1 = Additions) sobre los textos conservados **hash-verificados** (11 textos CF/ES byte-idénticos al ZIP base-4.14; 29 PDF de FUENTES_CONSERVADAS con sha256+bytes OK) obtiene exactamente los nueve valores del dossier:

| Año | PP&E Additions (k€) | Comparativo en CF siguiente |
|---|---|---|
| 2017 | 101.154 | CF_2018: 101.154 ✓ |
| 2018 | 93.148 | CF_2019: 93.148 ✓ |
| 2019 | 108.645 | CF_2020: 108.645 ✓ |
| 2020 | 134.263 | CF_2021: 134.263 ✓ |
| 2021 | 105.877 | CF_2022: 105.877 ✓ |
| 2022 | 158.234 | CF_2023: 158.234 ✓ |
| 2023 | 134.472 | CF_2024: 134.472 ✓ |
| 2024 | 171.185 | CF_2025: 171.185 ✓ |
| 2025 | 177.848 | — |

- **Origen del error antiguo confirmado por mí**: la nota de Intangible Assets de CF_2017 da Additions total **156.743** = emission 3.237 + goodwill **150.657** + otros; en 2025 la nota de intangibles da **45.173** (emission 37.661) — exactamente los valores que la revisión externa (SONDA_B_INTANGIBLES) marcó como lecturas erróneas de PP&E. Las 9 filas de intangibles (total/emission/goodwill) coinciden todas (`evidencias/extraccion_independiente_out.txt`).
- **Script del autor re-ejecutado**: `tablas_vidrala.py` @ daa7478 → exit 0, salida `VIDRALA_REPOSICION_CAPACIDAD.csv` **byte-idéntica** a la commiteada, y su control negativo pasa («las filas antiguas viven en la nota Intangible Assets y el extractor las rechaza»). No modifiqué su material; corrí una copia en `.trabajo/` y limpié el worktree.
- **Discrepancia comparativa 2023**: vista por mí en CF_2024 p.48 — combinación de negocios reexpresada 291.821 vs 262.679 (CF_2023), cierre de coste 2.131.588 vs 2.102.446, adiciones 134.472 **iguales**. Coincide con lo que el dossier registra sin resolver ni forzar.

### B2 — θ/λ no identificados; P-M1 no delimitada; bloqueo conservado: CONFIRMADO (y yo no los identifico)

- `CALCULOS_PM1.json` @ daa7478 declara en `conclusion_frente_B`: «P-M1 no delimitada con la evidencia disponible; bloqueo de la conclusión afectada (D2/D5/D6…)», y en `pendiente`: «θ y λ no identificados… no se elige valor». La extrapolación de perímetro está etiquetada `HIPÓTESIS` con los cálculos sobre la base correcta separados de los de la hipótesis. Yo no propongo ningún valor de θ/λ; el bloqueo se conserva.
- **Preservación pendiente confirmada**: `gh release view fuentes-mistral-m2-20261116 --json assets` → `assets: []` (vacío), coherente con el 401 documentado por el autor; los 4 PDF nuevos quedan en cobertura PROVISIONAL (URL+SHA-256+bytes en FUENTES_NUEVAS.csv), no presented como preservados en GitHub. Verificado, no reintentado por mí (no tengo credenciales de upload ni las pido).

## Defectos materiales

**Ninguno** en lo contrastado. No hay contraejemplo que construir: las nueve altas se reproducen con método independiente desde bytes hash-verificados, los comparativos cuadran, el error antiguo se localiza en la nota de intangibles, y el estado de no-identificación de θ/λ está correctamente declarado.

## Límites

- Misma familia de modelo que el autor (Mistral B): la independencia es de sesión/método/hashes, no de familia de modelo — declarado arriba.
- No re-ejecuté `calculos_pm1.py` completo ni `extraer_pdfs_viscofan.py`/`tablas_viscofan.py` (parte Viscofan fuera del alcance de este contraste dirigido); revisé `CALCULOS_PM1.json` documentalmente.
- Los textos conservados provienen del ZIP base-4.14 verificado (sha256 del release); no usé los PDF con poppler (no disponible en el sandbox).
- Sigue pendiente: subida de los 4 PDF nuevos a la release (401), desglose por tipo 2017 de Viscofan, desglose reposición/capacidad de los hornos de Vidrala.

## Estado

Rama `mistral/f-alcance-real`; nada modificado fuera de `resultados_cierre/alcance_real/`; la rama del frente B (`mistral/m2-fundamento-pm1`) intacta. Siguiente en la cola: **F-B3 / F-C1** (Cola 2, preparación de casos). El coordinador registra; yo no me autoaprobo.

*Propuesta de evidencia o especificación de Mistral; pendiente de revisión e incorporación por el integrador. No APROBADO ni aptitud financiera general.*
