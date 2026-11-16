# Punto de recuperación · frente B (P-M1) · rama mistral/m2-fundamento-pm1

Propuesta de evidencia o especificación de Mistral; pendiente de revisión e incorporación por el integrador.

## Estado actual

- Repositorio auxiliar `jluisplagos/munger-v2-evidencias-mistral` (origin verificado). Rama `mistral/m2-fundamento-pm1` @ `f5b65f717f97f777471bc5343c6541805edcd7b4`, traída de origin y publicada.
- Insumos: `preparar_insumos.py --download` ejecutado; ZIP base-4.14 (1.130.912.246 bytes, sha256 `bb51942c…b7b93e` verificado) y 251 insumos conformes en `.trabajo/insumos_m2/`; 29 PDF candidatos. Selección parcial (`producto_completo_verificado: false`).
- Inventario, alcance y plan finito entregados en `INVENTARIO_Y_ALCANCE.md` (bloque B1, este commit).

## Terminado

- B1 (commit `cb39dc0`): inventario, alcance, plan finito y fuentes disponibles/faltantes con estado de acceso medido.
- B2+B3 (commit `44b4b91`): `INVERSION_VISCOFAN_2016_2025.csv` y `PUENTE_CAPEX_DA_ROU.csv` generados por `scripts/tablas_viscofan.py` (cada operando verificado por cita en su línea/página; `scripts/extraer_pdfs_viscofan.py` extrae IA_2016/2021/2023 de los PDF conservados tras comprobar SHA-256 contra el índice). Desglose por tipo verificado en bytes conservados para 2016, 2018, 2019, 2020, 2021, 2022, 2023 y 2025; 2017 solo total (107,2 M€, comparativo en IA_2018 p135); 2024 solo total (71,0 M€, comparativo en AR_2025 p143/impresa 123), desglose pendiente de fuente nueva. Puente recalculado: Σcapex caja 2021–2025 = 443.945k€, Σaltas ROU = 24.110k€, ΣD&A = 403.132k€, Σamort ROU = 27.051k€, exceso NIIF 16 = 64.923k€, exceso «Caja» = 40.813k€ (coinciden con la conciliación de la base). Hallazgos del puente: 2022 publicada 125,6 M€ vs capex caja 115.566k€ vs adiciones PP&E brutas 120.362k€; 2025 CapEx taxonomía 90,6 M€ = gestión 84,1 + altas ROU 6,494 (APM Capex p146 excluye ROU; taxonomía p275 lo incluye); en CF_2021 p8 la etiqueta inglesa de la línea de pagos está intercambiada con la de dependientes (la columna comparativa de CF_2022 p25 l337 lo fija).

- B4 (commit `ca1d8b4`): fuentes oficiales nuevas descargadas el 2026-11-16 con TLS verificado: informe de gestión 2024 (EN 167 págs. sha256 `1dc3ef18…`, ES 168 págs. `195fa418…`, text layer roto → OCR p.8 EN), página HTML oficial EN de la Memoria Anual 2024 (49.563 B, sha256 `bd139bde…`, conservada en Git en `fuentes_nuevas/` con el desglose 2024: 34/35/14/17 sobre €71,0M), presentación Beat'30 CNMV 27-feb-2026 (58 págs., sha256 `8549db83…`: capex 2026-2030 €600M, ~50% recurrente / €300M crecimiento, p.27/31/35/53), y CCAA 2024 del micrositio oficial (sha256 `14b61868…` = idéntico al CF_2024.pdf de base-4.14). Release auxiliar `fuentes-mistral-m2-20261116` creada con notas; los PDF NO pudieron subirse como assets (uploads.github.com → 401 en el sandbox) → cobertura provisional declarada con URL/SHA/bytes/páginas en `FUENTES_NUEVAS.csv`; el HTML y el índice sí van a Git (no prohibidos). `FUENTES_CONSERVADAS.csv` (196 filas de la selección base-4.14). El desglose 2024 entra en `INVERSION_VISCOFAN_2016_2025.csv` desde la fuente nueva; 2017 sigue sin desglose en bytes conservados.

- B5 (commit `fa14e5e`): `VIDRALA_REPOSICION_CAPACIDAD.csv` desde citas verificadas: adiciones PP&E brutas 2017-2025, pagos de inmovilizado (EFE), vida útil hornos 8-16 años (todos los años), renovación de hornos 2024-2025 (España/Portugal/UK), PERTE descarbonización hornos (10.298+6.316 k€), altas ROU activo/pasivo con sus diferencias (2.165 vs 2.133 en 2022; 1.485 vs 1.429 en 2024), 46.123 por «The Park» en 2023, amortización ROU, sale&leaseback 2022. Capacidad añadida NO publicada en bytes conservados. Discrepancia registrada: comparativo 2023 de adiciones PP&E = 102.795 en CF_2024 vs 100.655 en CF_2023.
- B6 (commit `fc23eca`): `CALCULOS_PM1.json` con `scripts/calculos_pm1.py` (Decimal). θ sobre el desglose por tipo 2021-2025 (ya con 2024 en bytes conservados): estrecha ΣM=108.207 θ=−4,5427; media ΣM=218.478 θ=−2,8442; amplia ΣM=304.460 θ=−1,5198; contraste amplia sobre total publicado θ=−2,3649 (exceso sobre publicado 47.068). Sensibilidad: θ=0 → 60,3% de la capacidad declarada; θ=0,2 → 68,3%; θ=0,5 → 80,2%; θ=1 → 100%. λ (Vidrala) como rango condicionado: Eurostat sts_inpp_a ES I21 NSA (series primarias en `indices/` con SHA-256 y metadatos): C23 λ∈[1,3299, 1,3743]; C28 (maquinaria) λ∈[1,2037, 1,2810] para L∈[8,16] y t=2025. NO se adopta θ ni λ.

## Terminado (entrega final, este commit)

- B7: `DOSSIER_D2.md` (identificado / no identificado / opciones condicionadas / evidencia ausente / consecuencias / decisión para la persona responsable), `HALLAZGOS.md`, `RESUMEN_PARA_CLAUDE.md`, `MANIFIESTO_SHA256.txt`. Entrega completa en `resultados_m2/pm1/`: CSV de inversión y puente, CSV de Vidrala, FUENTES_NUEVAS/CONSERVADAS, `CALCULOS_PM1.json`, scripts en `scripts/`, fuentes nuevas en `fuentes_nuevas/` e índices Eurostat en `indices/`.

## Pendiente / siguiente acción exacta

1. Revisión externa (otro contexto) sobre el commit congelado de esta rama; correcciones materiales se aplican o quedan como bloqueo.
2. Subir como assets de la Release `fuentes-mistral-m2-20261116` los PDF registrados en `FUENTES_NUEVAS.csv` (uploads.github.com dio 401 en esta sesión) y verificar sus SHA-256 al subir.
3. D2/D5/D6: decisiones de la persona responsable; este frente no adopta θ/λ/estructura ni emite objetivo.
4. Nada más en este frente: no PR, no fusión, no tocar M1 ni el producto.

## Límites

- Informes antiguos = índices de búsqueda, no evidencia nueva. Sin LibreOffice ni pipeline; XLSX solo lectura; PDF/XLSX/ZIP fuera de Git.
- No se adopta θ/λ/k/probabilidades/políticas; no se convierte categoría contable en mantenimiento económico; sin recomendaciones de inversión ni autoaprobación; D2 queda para la persona responsable.
- `www.viscofan.com`/`public.viscofan.com` no verifican TLS en el proxy del sandbox: sus bytes no se usarán como conservados salvo declaración de cobertura provisional.

## Modelo y herramientas

- Vibe Code de Mistral AI, modelo `mistral-large-4-0`; consumo no visible desde la sesión. Python 3.12.15 + pypdf 7.1.0 + openpyxl 3.1.5 + PyMuPDF 2.1; urllib para red (curl bloqueado por el sandbox). Sin LibreOffice ni pipeline.
