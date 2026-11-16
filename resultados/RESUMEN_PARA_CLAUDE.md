# Resumen para Claude · frente M · evidencia de fuentes Vidrala/Viscofan

**Evidencia propuesta por Mistral; pendiente de revisión e incorporación por el integrador.** No es auditoría aprobada ni aptitud para dinero real.

## Objetivo
Preparar evidencia verificable de los 26 objetivos (y 34 dependencias) de los expedientes finales `…/2026-11_Vidrala_ensayo_4_14/vidrala_decisiones/Vidrala` y `…/viscofan_decisiones/Viscofan`, contrastando fuentes conservadas, declaraciones históricas y celdas reales de los XLSX, sin modificar el producto.

## Commits y huellas
- Rama: `mistral/fuentes-vm-01` en `jluisplagos/munger-v2-evidencias-mistral` (base `main` @ `e137b854dc592bcad9ed3e51275f7b80d35d210e`). Commits locales: `5641bec` (bloque 1), `b278727` (bloque 2), más el de entrega final (ver `git log` de la rama).
- Insumos: ZIP release `base-4.14` (1.130.912.246 bytes, sha256 `bb51942c…b7b93e`) descargado una vez con `preparar_insumos.py --download`; 15 archivos copiados a `.trabajo/insumos/` con sha256 conformes. Selección parcial: **no** es materialización de los 6.798 archivos.
- PDF conservados (sha256 verificados): VIDRALA_EN2025 `c548c2fa…`, VIDRALA_ES2025 `29fd6a29…`, VIDRALA_EN2024 `c2d4c12e…`, VISCOFAN_2025 `e997bc7d…`, VISCOFAN_2024 `14b61868…`. XLSX: Vidrala `82ff7fb8…`, Viscofan `95a78291…`.
- Asociaciones texto↔PDF verificadas con pypdf (100% tokens numéricos por página citada) y verificación visual (PyMuPDF) en EN2025 p.52 y ES2025 p.14.
- `resultados/lectura_fuentes.jsonl`: 60 observaciones (una por entrada). Hash primera lectura bloque 1: `5571ee7f…90f51`; bloque 2: `8a7a518f…29c2c`; fichero completo: `5905e415…f3d8dc`.

## Recuento por estado (26 objetivos)
- `COINCIDE_EN_REVISION_MISTRAL`: **23**
- `HIPOTESIS_O_AUSENCIA`: **3** (Vidrala `Análisis!C48` dato ausente E4; `C49` y `C50` hipótesis)
- `DIFERENCIA`: 0 · `NO_ACREDITADO`: 0

Todos los recalculados coinciden con el libro a 3 decimales (E1): Vidrala C46 335,413333→335,413; C47 169,667667→169,668; C55 35,182858 exacto. Viscofan C46 192,300333→192,3; C47 77,533333→77,533; C48 8,294 exacto; C49 5,547333→5,547; C50 3,707333→3,707; C55 45,993399 exacto (D3). Datos publicados L6/L7/L8/L12/K14/L14/L15 de ambas empresas verificados en los PDF (páginas en `lectura_fuentes.jsonl`).

## Fuentes examinadas
- Vidrala: EN 2025 (80 p.) p.4, 7, 52; EN 2024 (85 p.) p.7, 56; ES 2025 original (372 p.) p.14, 67, 357 (verificación visual en p.14).
- Viscofan: AR_2025 (470 p.) p.23, 27, 28, 76, 83; CF_2024 (107 p.) p.9.
- XLSX de ambos expedientes leídos en solo lectura (openpyxl): celdas objetivo hardcodeadas; Vidrala C48 = vacío.

## Hallazgos materiales (detalle en `HALLAZGOS.md`)
1. Traducción EN de Vidrala invierte rótulos: «Payments from sale of…» = pagos **por adquisición**; «Cash used in operating activities» = «Efectivo generado por las operaciones» (ES original p.14). Signos/conceptos correctos solo en español.
2. EN imprime «106,417)» sin paréntesis (col. 2024); ES original «(106.417)»; aritmética del subtotal lo confirma (P1).
3. Viscofan K14 usa el comparativo 2024 **reexpresado** en AR_2025 (acreedores −2.953 vs −2.639 en CF_2024) → 8,862 (no 8,548). Resuelto por la regla «cifra más reciente».
4. Vidrala C48: sin línea de intereses en financiación en 2023-2025 (verificado en ES p.14 visualmente) → dato ausente (E4); alternativa 2,254 mm no adoptada.
5. Vidrala C49/C50: principal de arrendamientos no publicado; SBC=0 solo cubierto para consejeros → hipótesis, no datos.
6. E2 preservado: K14 = 84,994 publicado; reserva plusvalía Italia (50,547) aparte, no descontada.

## Pendientes y rutas
- Pendiente de revisión externa de citas, derivaciones y compatibilidad antes de incorporar cualquier parte (`resultados/contraste_objetivos.csv`, `resultados/lectura_fuentes.jsonl`, `resultados/HALLAZGOS.md`).
- Bloqueo de entrega remoto: el push a la rama del auxiliar falla con 403 (la instalación de la GitHub App no tiene acceso de escritura al auxiliar; `gh`/API mutantes bloqueados por el sandbox). Detalle en `PUNTO_DE_RECUPERACION.md`.
- Sin consumo visible desde la sesión (no se afirma límite). Modelo real: `mistral-large-4-0` (Vibe Code).
- No se tocaron Elis/F1, P-M1, probabilidades, k, motor C, precios objetivo ni políticas; no se abrió PR ni se fusionó nada; no se ejecutó LibreOffice ni el pipeline.
