# Entrega · M4 ventana 4 · Waste Management, Inc. (2016–2025)

**Modelo:** mistral-large-4-0 (agente Vibe Code). **Herramientas usadas de verdad:** `gh` CLI (descarga del release `fuentes-examen-20261118` y push), `python3` + `pypdf 7.1.0` (extracción de texto página a página de los 10 PDF, con marcadores de página del visor), `sha256sum` (verificación contra `coordinacion/cierre_v2/examen/RELEASE_FUENTES_EXAMEN_SHA256SUMS`: los 10 `wm-annual-report-2016…2025.pdf` dan OK), y scripts propios de verificación (cada `cita_literal` está en su `pagina_pdf` del `archivo` citado; cada `valor_impreso` está en su cita; 334 filas, 0 errores). No se sube ningún PDF a Git (regla de `AGENTS.md`); los PDF se quedan fuera del repo.

## Qué hice

- Extraje las 24 partidas de la plantilla (`01_historia_2016.md` de `examen/ahold-f1`) para cada año 2016–2025, **una fila por partida, año y componente**, en `HISTORIA.csv` (334 filas, millones USD salvo acciones diluidas en millones de acciones). Valores tal como impresos (con separadores y paréntesis), unidad declarada, página = página del visor PDF.
- **Regla de informe:** para el año N usé la columna comparativa del informe N+1 (`wm-annual-report-(N+1).pdf`), que recoge reexpresiones (p. ej. en el informe 2018 la columna 2017 reclasifica «Loss on early extinguishment» dentro de «Other, net», y el circulante 2017 sale reexpresado). Para 2025 usé el informe 2025 (no hay informe 2026 entre las fuentes). Se indica en `informe_usado`.
- Verifiqué SHA-256 de cada fila contra el archivo citado (`sha256_archivo`).

## Lo que no encontré y por qué

- **`id` (I+D): `no_encontrado` en los 10 años.** WM no publica gasto de I+D como partida separada en ningún informe (solo menciones en factores de riesgo).
- **`arrendamientos_principal` 2016–2018: `no_encontrado`.** Bajo US GAAP (ASC 840) los arrendamientos operativos —la inmensa mayoría— no tienen principal en financiación; el principal de los arrendamientos de capital no se desagrega en el estado de flujos. Desde 2019 (ASC 842) sí se publica: «Cash paid during N for our operating and financing leases…» y tomo la parte de financiación.
- **`intereses_financiacion`: `cero_con_evidencia` en los 10 años.** La sección de financiación del estado de flujos no tiene línea de intereses pagados: bajo US GAAP los intereses pagados van en actividades de explotación. `intereses` sale de la tabla suplementaria «Interest, net of capitalized interest».
- **`otros_activos_financieros`: `cero_con_evidencia` en los 10 años.** El activo corriente solo tiene caja, deudores, existencias y otros activos; no hay inversiones financieras corrientes (el *restricted cash* es caja y va aparte en la conciliación; *restricted funds* es no corriente).
- **`arrendamientos` 2016–2018: `cero_con_evidencia`.** ASC 842 se adoptó el 1-ene-2019 con método de transición opcional: a 31-dic-2016/17/18 no hay pasivos por arrendamiento en balance.

## Dudas de definición (cómo lo resolví)

- **EBIT derivado:** en el bloque «Other income (expense)» de WM solo resto `Interest expense, net` y `Loss on early extinguishment of debt` (signo −1); `Equity in net (income) losses of unconsolidated entities` y `Other, net` **no** se restan, per la definición de la plantilla (participadas y «Other» quedan dentro del EBIT derivado). Así el derivado difiere del impreso exactamente en esas dos líneas (p. ej. 2025: 4.338 vs 4.308 impreso).
- **`deuda` post-2019:** las líneas de balance «Current portion of long-term debt» y «Long-term debt, less current portion» **incluyen** los arrendamientos financieros ASC 842; los resto como componentes con signo −1 (citados en la nota de leases) para dejar deuda sin pasivos por arrendamiento. Pre-2019 los arrendamientos de capital quedan **dentro** de deuda, per la plantilla (no son NIIF 16).
- **`arrendamientos` post-2019:** total de *lease liabilities* de la nota de leases (operativos + financieros).
- **`pensiones`:** uso los pasivos reconocidos por prestaciones a empleados (*accrued benefit liabilities*, cuando se imprimen) o sus componentes (unfunded DB + post-jubilación); los planes multiemployer se declaran «not material» en la nota.
- **`adquisiciones`:** componente principal «Acquisitions of businesses, net of cash acquired» más «Proceeds from divestitures…» con signo −1; aviso de que esa línea incluye también «other assets».
- **Citas:** están copiadas del texto extraído con pypdf y normalizadas en espacios (pypdf a veces parte palabras con un espacio, p. ej. «pensi on»); los números y rótulos son los del PDF.

## Notas

- No abrí ninguna carpeta del expediente de WM en `munger-v2`; solo leí la plantilla indicada en el encargo. No aprobé mi propio trabajo ni hice valoraciones: solo extracción literal.
