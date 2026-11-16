# Punto de recuperación · frente B (P-M1) · rama mistral/m2-fundamento-pm1

Propuesta de evidencia o especificación de Mistral; pendiente de revisión e incorporación por el integrador.

## Estado actual

- Repositorio auxiliar `jluisplagos/munger-v2-evidencias-mistral` (origin verificado). Rama `mistral/m2-fundamento-pm1` @ `f5b65f717f97f777471bc5343c6541805edcd7b4`, traída de origin y publicada.
- Insumos: `preparar_insumos.py --download` ejecutado; ZIP base-4.14 (1.130.912.246 bytes, sha256 `bb51942c…b7b93e` verificado) y 251 insumos conformes en `.trabajo/insumos_m2/`; 29 PDF candidatos. Selección parcial (`producto_completo_verificado: false`).
- Inventario, alcance y plan finito entregados en `INVENTARIO_Y_ALCANCE.md` (bloque B1, este commit).

## Terminado

- B1 (este commit): inventario de fuentes conservadas (12 PDF y 9 textos de Viscofan, 11 textos de Vidrala, PDF de Vidrala 2016–2025 y BORME/CNMV), fuentes faltantes con estado de acceso medido (CNMV/BOE/Eurostat/INE/informeanual*.viscofan.com OK con TLS; www/public.viscofan.com sin verificación TLS en el proxy), alcance finito B2–B7 y límites.

## Pendiente / siguiente acción exacta

1. B2: extraer inversión por tipo de Viscofan 2016–2025 de los textos/PDF conservados (`grep` sobre `.trabajo/insumos_m2/.../viscofan_decisiones/Viscofan/texto/*.txt` y extracción PyMuPDF de `IA_2016_es.pdf`, `IA_2021_es.pdf`, `IA_2023_es.pdf`), generar `INVERSION_VISCOFAN_2016_2025.csv` con script, commit+push.
2. B3: conciliación capex de caja / D&A / altas ROU 2021–2025 (puente 2022: 125,6 M€ publicados frente a 115,566 M€ de capex de caja; perímetro 2025 con ROU), `PUENTE_CAPEX_DA_ROU.csv`, commit+push.
3. B4: fuentes oficiales nuevas (informe de gestión/anual 2024 y Beat'30) — descargar con TLS verificado, conservar en Release auxiliar `fuentes-mistral-m2-20261116` con índice SHA-256 o declarar provisional; `FUENTES_NUEVAS.csv`/`FUENTES_CONSERVADAS.csv`, commit+push.
4. B5: Vidrala reposición/capacidad/ROU desde `texto/CF_2017..CF_2025.txt`; `VIDRALA_REPOSICION_CAPACIDAD.csv`, commit+push.
5. B6: recalcular tablas de θ (script `Decimal`) y rangos de λ condicionados; `CALCULOS_PM1.json`, commit+push.
6. B7: `DOSSIER_D2.md` + entregas finales (`HALLAZGOS.md`, `RESUMEN_PARA_CLAUDE.md`, `MANIFIESTO_SHA256.txt`), commit+push final.

## Límites

- Informes antiguos = índices de búsqueda, no evidencia nueva. Sin LibreOffice ni pipeline; XLSX solo lectura; PDF/XLSX/ZIP fuera de Git.
- No se adopta θ/λ/k/probabilidades/políticas; no se convierte categoría contable en mantenimiento económico; sin recomendaciones de inversión ni autoaprobación; D2 queda para la persona responsable.
- `www.viscofan.com`/`public.viscofan.com` no verifican TLS en el proxy del sandbox: sus bytes no se usarán como conservados salvo declaración de cobertura provisional.

## Modelo y herramientas

- Vibe Code de Mistral AI, modelo `mistral-large-4-0`; consumo no visible desde la sesión. Python 3.12.15 + pypdf 7.1.0 + openpyxl 3.1.5 + PyMuPDF 2.1; urllib para red (curl bloqueado por el sandbox). Sin LibreOffice ni pipeline.
