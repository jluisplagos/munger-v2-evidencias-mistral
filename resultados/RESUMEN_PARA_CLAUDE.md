# Resumen para Claude · frente M · evidencia de fuentes Vidrala/Viscofan

**Evidencia propuesta por Mistral; pendiente de revisión e incorporación por el integrador.** No es auditoría aprobada ni aptitud para dinero real.

## Objetivo
Preparar evidencia verificable de los 26 objetivos (y 34 dependencias) de los expedientes finales `…/2026-11_Vidrala_ensayo_4_14/vidrala_decisiones/Vidrala` y `…/viscofan_decisiones/Viscofan`, contrastando fuentes conservadas, declaraciones históricas y celdas reales de los XLSX, sin modificar el producto.

## Commits y huellas (publicados en la rama `mistral/fuentes-vm-01`)
- Base: `main` @ `e137b854dc592bcad9ed3e51275f7b80d35d210e`. Rama publicada en `jluisplagos/munger-v2-evidencias-mistral`:
  - `5641bec` bloque 1 (primera lectura de 16 entradas, antes del contraste),
  - `b278727` bloque 2 (60 entradas en total),
  - `6b53ef9` entrega completa (commit de entrega: [6b53ef9](https://github.com/jluisplagos/munger-v2-evidencias-mistral/commit/6b53ef9f67dc4519cfd9a64bcf21e40f08baa120)),
  - commit superior de **correcciones dirigidas** tras la revisión externa de `6b53ef9` (ver `git log` de la rama; las correcciones están documentadas en `HALLAZGOS.md`).
- Insumos: ZIP release `base-4.14` (1.130.912.246 bytes, sha256 `bb51942c…b7b93e`) descargado una vez con `preparar_insumos.py --download`; 15 archivos en `.trabajo/insumos/` con sha256 conformes. Selección parcial: **no** es materialización de los 6.798 archivos.
- PDF conservados (sha256 verificados): VIDRALA_EN2025 `c548c2fa…`, VIDRALA_ES2025 `29fd6a29…`, VIDRALA_EN2024 `c2d4c12e…`, VISCOFAN_2025 `e997bc7d…`, VISCOFAN_2024 `14b61868…`. XLSX: Vidrala `82ff7fb8…`, Viscofan `95a78291…`.
- Asociaciones texto↔PDF verificadas con pypdf (100% tokens numéricos por página citada) y verificación visual (PyMuPDF) en EN2025 p.52 y ES2025 p.14.
- `resultados/lectura_fuentes.jsonl`: 60 observaciones. Hashes: bloque 1 `5571ee7f…90f51`; bloque 2 `8a7a518f…29c2c`; tras correcciones `3d81d01b…fdf42f` (la primera lectura se conserva en el historial, commits `5641bec`/`b278727`).
- Auditoría aritmética determinista de sumas, medias y conversiones: **sin problemas** tras corregir C49 (20.292 miles, no 20.492).

## Recuento por estado (26 objetivos)
- `COINCIDE_EN_REVISION_MISTRAL`: **23**
- `HIPOTESIS_O_AUSENCIA`: **3** (Vidrala `Análisis!C48` dato ausente E4; `C49` y `C50` hipótesis)
- `DIFERENCIA`: 0 · `NO_ACREDITADO`: 0

Todos los recalculados coinciden con el libro a 3 decimales (E1): Vidrala C46 335,413333→335,413; C47 169,667667→169,668; C55 35,182858 exacto. Viscofan C46 192,300333→192,3; C47 77,533333→77,533; C48 8,294 exacto; C49 5,547333→5,547; C50 3,707333→3,707; C55 45,993399 exacto (D3, de Viscofan). Datos publicados L6/L7/L8/L12/K14/L14/L15 de ambas empresas verificados en los PDF.

## Fuentes examinadas
- Vidrala: EN 2025 (80 p.) p.4, 7, 52; EN 2024 (85 p.) p.7, 56; ES 2025 original (372 p.) p.14, 67, 357 (verificación visual en p.14).
- Viscofan: AR_2025 (470 p.) p.23, 27, 28, 76, 83; CF_2024 (107 p.) p.9.
- XLSX de ambos expedientes leídos en solo lectura (openpyxl): celdas objetivo hardcodeadas; Vidrala C48 = vacío.

## Hallazgos materiales (detalle en `HALLAZGOS.md`)
1. Traducción EN de Vidrala invierte rótulos: «Payments from sale of…» = pagos **por adquisición**; «Cash used in operating activities» = «Efectivo generado por las operaciones» (ES original p.14).
2. EN imprime «106,417)» sin paréntesis (col. 2024); ES original «(106.417)»; aritmética del subtotal lo confirma (P1).
3. Viscofan K14 usa el comparativo 2024 **reexpresado** en AR_2025 (acreedores −2.953 vs −2.639 en CF_2024) → 8,862 (no 8,548). Resuelto por la regla «cifra más reciente».
4. Vidrala C48: sin línea de intereses en financiación en 2023-2025 (verificado visualmente en ES p.14) → dato ausente (E4); alternativa 2,254 mm no adoptada.
5. Vidrala C49/C50: el principal de arrendamientos no se publica (pago total 20.292 miles, media 6,764 mm; interés devengado 6.762 miles, media 2,254 mm; diferencia media 4,510 mm ≈ principal, no acreditado); SBC=0 solo está cubierto para consejeros → hipótesis, no datos.
6. E2 preservado: K14 = 84,994 publicado; reserva plusvalía Italia (50,547) aparte, no descontada. L7 (EBIT 292,068) incluye el deterioro de 2,362; L8 lo excluye.

## Correcciones dirigidas aplicadas (revisión externa de `6b53ef9`)
C49 (valor_leido 20.292; medias 6,764/2,254/4,510), L7 (EBIT incluye deterioro 2.362; sin él 294.430), L14 («−799 miles = −0,799 millones»), C55 de Vidrala sin atribución a D3, y textos de recuperación/resumen actualizados. Detalle con valores antiguos→nuevos en `HALLAZGOS.md`.

## Pendientes y rutas
- Revisión externa (integrador/Claude) de citas, datos, derivaciones y compatibilidad antes de incorporar cualquier parte (`resultados/` en la rama; sin PR ni fusión).
- Consumo/facturación no visible desde la sesión (se declara; no se afirma límite). El encargo recomienda un presupuesto inicial de 25 EUR configurado externamente; **no se ha podido comprobar desde la sesión que esté configurado**, se presenta como recomendación. Modelo real: `mistral-large-4-0` (Vibe Code).
- No se tocaron Elis/F1, P-M1, probabilidades, k, motor C, precios objetivo ni políticas; no se abrió PR ni se fusionó nada; no se ejecutó LibreOffice ni el pipeline; no hay PDF/XLSX/ZIP en Git.
