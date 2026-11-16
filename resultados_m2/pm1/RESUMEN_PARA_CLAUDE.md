# Resumen para Claude · frente B (P-M1) · M2 · 2026-11-16

Propuesta de evidencia de Mistral; pendiente de revisión e incorporación por el integrador. No APROBADO; no aptitud financiera general. Rama `mistral/m2-fundamento-pm1`; solo se escribió en `resultados_m2/pm1/`. Sin PR, sin fusión, sin tocar el producto, M1, F1/Elis o los otros frentes.

## Qué se hizo

1. **Inversión por tipo Viscofan 2016–2025** (`INVERSION_VISCOFAN_2016_2025.csv`, script `scripts/tablas_viscofan.py` con verificación de cada cita en su línea/página): desglose verificado en bytes para 2016, 2018–2025; 2017 solo total (107,2 M€). El desglose de 2024 (34/14/35/17 sobre €71,0M) entró con la fuente nueva: HTML oficial de la Memoria Anual 2024 conservado en Git (sha256 `bd139bde…`).
2. **Conciliación capex/D&A/ROU** (`PUENTE_CAPEX_DA_ROU.csv`): 2021–2025 recalculado con `Decimal` — capex caja 443.945 k€, altas ROU 24.110, D&A 403.132, amort ROU 27.051, **exceso NIIF 16 64.923 k€** (Caja 40.813); coincide con la conciliación de la base. Puente 2022 documentado (publicada 125,6 vs caja 115.566 vs PP&E bruto 120.362 k€); puente 2025: CapEx taxonomía 90,6 = 84,1 + ROU 6,494, y APM CapEx excluye ROU (dos definiciones en el mismo informe).
3. **Fuentes oficiales nuevas** (`FUENTES_NUEVAS.csv`, `FUENTES_CONSERVADAS.csv`, `fuentes_nuevas/`): informe de gestión 2024 (EN/ES), página HTML oficial, presentación Beat'30 (CNMV 27-feb-2026: €600M capex 2026–2030, 50/50 recurrente/crecimiento) y CCAA 2024 (sha256 idéntico al CF_2024.pdf de base-4.14). Release `fuentes-mistral-m2-20261116` creada; los PDF no pudieron subirse como assets (uploads.github.com → 401 en el sandbox) → **cobertura provisional** con URL/SHA/bytes/páginas registrada; pendiente de subida.
4. **Vidrala** (`VIDRALA_REPOSICION_CAPACIDAD.csv`): vida útil hornos 8–16 (todos los años), renovación de hornos 2024–2025, adiciones PP&E por país 2018–2023, adiciones brutas 2017–2025, ROU activo/pasivo con diferencias (2.165/2.133; 1.485/1.429), 46.123 «The Park» 2023, amort ROU. Capacidad añadida no publicada en bytes.
5. **Límites de θ/λ** (`CALCULOS_PM1.json`, `scripts/calculos_pm1.py`, Decimal): θ con el desglose por tipo 2021–2025 = **−4,54 / −2,84 / −1,52** (estrecha/media/amplia); M < D&A en los cinco años; θ≥0 exige 60–100% de reclasificación de la «capacidad». λ (Vidrala) como rango condicionado a series primarias Eurostat (`indices/`, con SHA-256 y metadatos): C23 [1,330–1,374], C28 [1,204–1,281] para L∈[8,16], t=2025.

## Conclusión para D2 (decisión de la persona responsable, no adoptada aquí)

- **Viscofan:** P-M1 delimitable solo si se acepta el método replicable del desglose por tipo → θ acotado a 0 (extremo inferior), con la sensibilidad demostrada; sin aceptarlo, θ sin delimitar.
- **Vidrala:** no delimitada con lo disponible → abstención del objetivo (igual que el expediente `vidrala_bloqueo` existente). λ solo condicionado a estructura aceptada + serie + vida útil explícitas.
- Pendientes demostrados: desglose 2017; desglose reposición/capacidad de hornos de Vidrala; familia Λ en Viscofan; estructura de P-M1 en ambas.

## Verificación

- `python3 resultados_m2/pm1/scripts/extraer_pdfs_viscofan.py` (SHA-256 de IA_2016/2021/2023 contra el índice antes de extraer).
- `python3 resultados_m2/pm1/scripts/tablas_viscofan.py` → regenera ambos CSV (falla si alguna cita no está en su línea).
- `python3 resultados_m2/pm1/scripts/tablas_vidrala.py`, `scripts/fuentes_csv.py`, `scripts/calculos_pm1.py`.
- Push verificado: `git ls-remote origin mistral/m2-fundamento-pm1` coincide con HEAD local.

## Modelo y herramientas

Vibe Code de Mistral AI, modelo `mistral-large-4-0`; consumo no visible desde la sesión. Python 3.12.15 + pypdf 7.1.0 + openpyxl 3.1.5 + PyMuPDF 2.1 + OCR (herramienta del sandbox) para el PDF de gestión 2024 con text layer roto. Red con TLS verificado: GitHub (API; uploads bloqueado 401), CNMV, BOE, informeanual*.viscofan.com, Eurostat. Sin LibreOffice ni pipeline. `www/public.viscofan.com` sin verificación TLS en el proxy → no se usaron sus bytes.
