# Punto de recuperación · frente M · rama mistral/fuentes-vm-01

Evidencia propuesta por Mistral; pendiente de revisión e incorporación por el integrador.

## Estado actual

- Repositorio auxiliar: `jluisplagos/munger-v2-evidencias-mistral` (origin verificado). Rama: `mistral/fuentes-vm-01`. Base: `main` @ `e137b854dc592bcad9ed3e51275f7b80d35d210e`.
- Insumos: `python3 docs/mistral_fuentes_vm/herramientas/preparar_insumos.py --download` ejecutado; ZIP base-4.14 (1.130.912.246 bytes, sha256 `bb51942c…b7b93e` verificado) descargado una vez y 15 insumos copiados a `.trabajo/insumos/` con sha256 conformes al índice. `producto_completo_verificado: false` (selección parcial, no materialización de los 6.798 archivos).
- Asociaciones texto↔PDF verificadas con pypdf (cobertura 100% de tokens numéricos en cada página citada): CF_2025.txt↔2355_en-2025 (p.4,7); CF_2024.txt↔2145_en-2024 (p.7); ES_2025.txt↔2308_es (p.67); AR_2025.txt↔AR_2025.pdf (p.23,27,28,76,83); CF_2024.txt(Viscofan)↔CF_2024.pdf (p.9).

## Terminado

- Bloque 1 (10 objetivos iniciales: Historia L6/L7/L8/L12 y Análisis C55 de Vidrala y Viscofan) + sus 6 dependencias: primera lectura registrada en `resultados/lectura_fuentes.jsonl` (16 observaciones) ANTES de comparar con valores heredados.
  - Hash de esa primera lectura (bloque 1): sha256 `5571ee7f9a5b021da59f99d6ac61f9feb3a4723af92a240556f3e1ef20c90f51`.

## Pendiente / siguiente acción exacta

1. Bloque 2: leer en los PDF conservados los 16 objetivos restantes (Vidrala C46–C50, K14, L14, L15, J12, K12; Viscofan C46–C50, J12, J15, K14, K15, L14, L15) y las 28 dependencias restantes; añadir observaciones a `resultados/lectura_fuentes.jsonl` (bloque2) y registrar su hash.
2. Comparar con `entrada/declaraciones_historicas.json` y con las celdas reales de los XLSX (openpyxl, solo lectura; distinguir valor almacenado y fórmula; huella del libro ya registrada).
3. Recalcular los 34 derivados desde dependencias verificadas (expresión, operandos, unidad, signo, redondeo).
4. Entregables: `resultados/contraste_objetivos.csv` (26 filas), `HALLAZGOS.md`, `RESUMEN_PARA_CLAUDE.md`, actualizar este archivo, `MANIFIESTO_SHA256.txt`; ejecutar `python3 docs/mistral_fuentes_vm/herramientas/comprobar_entrega.py`; commit y push por bloque.

## Modelo y limitaciones

- Sesión: Vibe Code de Mistral AI, modelo `mistral-large-4-0` (único modelo expuesto por esta sesión; no se declara nivel de esfuerzo porque la interfaz no lo ofrece). Herramientas deterministas usadas para huellas/extracción/aritmética: Python stdlib + pypdf 7.1.0 + openpyxl 3.1.5 (instaladas vía pip en el sandbox).
- Consumo/facturación: no visible desde la sesión; se declara que no se está limitando ni afirma límite alguno. Presupuesto recomendado por el encargo (25 EUR) configurado externamente, no por mí.
- Límites de acceso: red disponible para GitHub (descarga de la release verificada); `curl` bloqueado por política del sandbox (se usó urllib). Sin LibreOffice ni pipeline (prohibidos por el encargo). PDF/XLSX/ZIP permanecen fuera de Git (`.trabajo/` excluido).
- No se han abierto PR, no se ha tocado `munger-v2`, ni ramas/PR/issues del original.
