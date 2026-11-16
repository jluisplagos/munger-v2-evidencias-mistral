# Punto de recuperación · Frente C (M2) · rama mistral/m2-matematica-b

Evidencia propuesta por Mistral; pendiente de revisión e incorporación por el integrador.

## Estado actual

- Repositorio auxiliar: `jluisplagos/munger-v2-evidencias-mistral` (origin verificado). Rama `mistral/m2-matematica-b` **publicada** en origin @ `f5b65f717f97f777471bc5343c6541805edcd7b4`.
- Insumos: Release `base-4.14` de `jluisplagos/munger-v2` descargada (sha256 `bb51942c…b7b93e` verificado) y `preparar_insumos.py --zip` ejecutado: 251 archivos conformes en `.trabajo/insumos_m2/` (selección parcial). Producto de referencia: commit `059f4f68dca7acf465b5f5b21de2dede84c885ff`.
- Bloque B1 terminado (commit `f9bb54b`, publicado): definiciones fijadas, demostraciones T1–T12 con bibliografía primaria, 56 casos fijados con provenance y sha256, plan finito y sensibilidad finita preanunciada.
- Bloque B2 terminado: `codigo/ejecutar_casos.py` → `resultados_casos.json`: las 10 propiedades globales pasan sobre los 56 casos (residuo F exacto 0 en trazos; bisección coincide ≤ 1e-9; P* ∈ [min V, ponderado] con k ≥ 1; k = 1 ⇒ ponderado; permutación, traslación, escala; monotonía en k). `codigo/comparar_producto.py` → `COMPARACION_IMPLEMENTACION.csv` (56 filas): esperado = oráculo propio; producto (`precio_de_si.py` sha256 `089fa5e3…aad8`, commit `059f4f68`) solo en columnas aparte; **residuo máximo oráculo-vs-producto 2,8e-14**; vs valores publicados en el paquete ≤ 5,1e-13. Casos A1–A5 dan fracciones exactas 265/3, 1330/13, 100, 380/7, 1005/13. Diferencias documentadas de contrato (no de valor): S4 desordenado → producto `sin_escalera` G19 (su `p_estrella` ordena igual que el oráculo); S5 k = 0,5 → producto se niega (guarda k ≥ 1), el oráculo da P* = 112 > ponderado 102,5; S3 precio ≤ 0 → `calcular` se niega, `p_estrella` calcula; S6 p inválidas → oráculo `DominioError`, `calcular` `sin_lectura`, pero `p_estrella` llamada directa devuelve 94,0 sin validar (hallazgo: la guarda vive en `calcular`, no en `p_estrella`); S7 n = 2 → oráculo P* = 90, `calcular` exige n = 3.

## Estado final del frente (entrega completa)

- Bloque B5 terminado: `DOSSIER_D1_D7_D11.md`, `HALLAZGOS.md`, `RESUMEN_PARA_CLAUDE.md`, `COMANDOS.md`, `MANIFIESTO_SHA256.txt`. Autocomprobación reproducible: todos los scripts de `codigo/` re-ejecutados desde cero con exit 0 (selftest PASA; 10/10 propiedades; residuo oráculo-vs-producto máx 2,8e-14; cobertura coincide 24/24). No es una revisión independiente: la revisión externa se hará sobre el commit congelado de esta rama.
- Entregas exigidas presentes en `resultados_m2/matematica_b/`: `DEFINICIONES_Y_DEMOSTRACIONES.md` (con bibliografía primaria verificable), oráculo propio + casos fijados + comandos + resultados, `COMPARACION_IMPLEMENTACION.csv` (esperado/obtenido/residuos/versión exacta comparada), `EFECTOS_PROBABILIDADES.csv`, `SENSIBILIDAD_FINITA.csv` (hipótesis explícitas), `PROTOCOLOS_COBERTURA.md/.csv`, `DOSSIER_D1_D7_D11.md`, `HALLAZGOS.md`, `RESUMEN_PARA_CLAUDE.md`, `MANIFIESTO_SHA256.txt`, `PUNTO_DE_RECUPERACION.md`, `casos_fijados.json`, `resultados_casos.json`. Todas las rutas referenciadas existen; no hay rutas AUSENTES.
- Commits publicados en origin: `f9bb54b` (B1 definiciones+casos), `4caaabd` (B2 oráculo+comparación), `bf7ca2a` (B3 probabilidades+sensibilidad), `f311593` (B4 protocolos), y el commit final de B5.

## Pendiente / siguiente acción exacta

1. **Revisión externa (integrador/Claude) sobre el commit congelado de `mistral/m2-matematica-b`**: demostraciones, residuos, descomposición de probabilidades (incluida la discrepancia +1,5478 vs +1,5386 € de D7), contrato de cobertura y dossier D1/D7/D11 antes de incorporar cualquier parte.
2. Nada más en este frente: no ampliar alcance, no PR, no fusión, no tocar el producto, main, los frentes A/B, F1/Elis ni los resultados M1 revisados. Sin rondas recursivas ni autoaprobación.

## Modelo y limitaciones

- Sesión: Vibe Code de Mistral AI, modelo `mistral-large-4-0` (único modelo expuesto; sin selector de esfuerzo). Herramientas: Python 3.12.15 stdlib; red solo para GitHub (descarga de release vía `gh`); sin LibreOffice ni pipeline; no se abrieron XLSX.
- Consumo/facturación: no visible desde la sesión; no se afirma ningún límite configurado. No se compraron créditos ni se usaron servicios de pago.
- No se ha modificado el producto ni `main`; no hay PR ni fusión; no se han tocado los frentes A/B ni F1/Elis ni los resultados M1 revisados.
