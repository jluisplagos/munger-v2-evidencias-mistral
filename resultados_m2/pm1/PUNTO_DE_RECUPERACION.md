# Punto de recuperación · frente B (P-M1) · rama mistral/m2-fundamento-pm1

Propuesta de evidencia o especificación de Mistral; pendiente de revisión e incorporación por el integrador.

## Estado actual

- Repositorio auxiliar `jluisplagos/munger-v2-evidencias-mistral` (origin verificado). Rama `mistral/m2-fundamento-pm1` @ `f5b65f717f97f777471bc5343c6541805edcd7b4`, traída de origin y publicada.
- Insumos: `preparar_insumos.py --download` ejecutado; ZIP base-4.14 (1.130.912.246 bytes, sha256 `bb51942c…b7b93e` verificado) y 251 insumos conformes en `.trabajo/insumos_m2/`; 29 PDF candidatos. Selección parcial (`producto_completo_verificado: false`).
- Inventario, alcance y plan finito entregados en `INVENTARIO_Y_ALCANCE.md` (bloque B1, este commit).

## Terminado

- B1 (commit `cb39dc0`): inventario, alcance, plan finito y fuentes disponibles/faltantes con estado de acceso medido.
- B2+B3 (este commit): `INVERSION_VISCOFAN_2016_2025.csv` y `PUENTE_CAPEX_DA_ROU.csv` generados por `scripts/tablas_viscofan.py` (cada operando verificado por cita en su línea/página; `scripts/extraer_pdfs_viscofan.py` extrae IA_2016/2021/2023 de los PDF conservados tras comprobar SHA-256 contra el índice). Desglose por tipo verificado en bytes conservados para 2016, 2018, 2019, 2020, 2021, 2022, 2023 y 2025; 2017 solo total (107,2 M€, comparativo en IA_2018 p135); 2024 solo total (71,0 M€, comparativo en AR_2025 p143/impresa 123), desglose pendiente de fuente nueva. Puente recalculado: Σcapex caja 2021–2025 = 443.945k€, Σaltas ROU = 24.110k€, ΣD&A = 403.132k€, Σamort ROU = 27.051k€, exceso NIIF 16 = 64.923k€, exceso «Caja» = 40.813k€ (coinciden con la conciliación de la base). Hallazgos del puente: 2022 publicada 125,6 M€ vs capex caja 115.566k€ vs adiciones PP&E brutas 120.362k€; 2025 CapEx taxonomía 90,6 M€ = gestión 84,1 + altas ROU 6,494 (APM Capex p146 excluye ROU; taxonomía p275 lo incluye); en CF_2021 p8 la etiqueta inglesa de la línea de pagos está intercambiada con la de dependientes (la columna comparativa de CF_2022 p25 l337 lo fija).

## Pendiente / siguiente acción exacta

1. B4: fuentes oficiales nuevas (informe de gestión/anual 2024 y presentación Beat'30 de Viscofan) — descargar con TLS verificado (informeanual2024.viscofan.com / CNMV), conservar en Release auxiliar `fuentes-mistral-m2-20261116` con índice SHA-256 o declarar provisional; `FUENTES_NUEVAS.csv`/`FUENTES_CONSERVADAS.csv`, commit+push.
2. B5: Vidrala reposición/capacidad/ROU desde `texto/CF_2017..CF_2025.txt`; `VIDRALA_REPOSICION_CAPACIDAD.csv`, commit+push.
3. B6: recalcular tablas de θ (script `Decimal` sobre el desglose por tipo) y rangos de λ condicionados a supuestos explícitos; `CALCULOS_PM1.json`, commit+push.
4. B7: `DOSSIER_D2.md` + entregas finales (`HALLAZGOS.md`, `RESUMEN_PARA_CLAUDE.md`, `MANIFIESTO_SHA256.txt`), commit+push final.

## Límites

- Informes antiguos = índices de búsqueda, no evidencia nueva. Sin LibreOffice ni pipeline; XLSX solo lectura; PDF/XLSX/ZIP fuera de Git.
- No se adopta θ/λ/k/probabilidades/políticas; no se convierte categoría contable en mantenimiento económico; sin recomendaciones de inversión ni autoaprobación; D2 queda para la persona responsable.
- `www.viscofan.com`/`public.viscofan.com` no verifican TLS en el proxy del sandbox: sus bytes no se usarán como conservados salvo declaración de cobertura provisional.

## Modelo y herramientas

- Vibe Code de Mistral AI, modelo `mistral-large-4-0`; consumo no visible desde la sesión. Python 3.12.15 + pypdf 7.1.0 + openpyxl 3.1.5 + PyMuPDF 2.1; urllib para red (curl bloqueado por el sandbox). Sin LibreOffice ni pipeline.
