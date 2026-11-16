# Punto de recuperación · Frente C (M2) · rama mistral/m2-matematica-b

Evidencia propuesta por Mistral; pendiente de revisión e incorporación por el integrador.

## Estado actual

- Repositorio auxiliar: `jluisplagos/munger-v2-evidencias-mistral` (origin verificado). Rama `mistral/m2-matematica-b` **publicada** en origin @ `f5b65f717f97f777471bc5343c6541805edcd7b4`.
- Insumos: Release `base-4.14` de `jluisplagos/munger-v2` descargada (sha256 `bb51942c…b7b93e` verificado) y `preparar_insumos.py --zip` ejecutado: 251 archivos conformes en `.trabajo/insumos_m2/` (selección parcial). Producto de referencia: commit `059f4f68dca7acf465b5f5b21de2dede84c885ff`.
- Bloque B1 terminado (commit `f9bb54b`, publicado): definiciones fijadas, demostraciones T1–T12 con bibliografía primaria, 56 casos fijados con provenance y sha256, plan finito y sensibilidad finita preanunciada.
- Bloque B2 terminado: `codigo/ejecutar_casos.py` → `resultados_casos.json`: las 10 propiedades globales pasan sobre los 56 casos (residuo F exacto 0 en trazos; bisección coincide ≤ 1e-9; P* ∈ [min V, ponderado] con k ≥ 1; k = 1 ⇒ ponderado; permutación, traslación, escala; monotonía en k). `codigo/comparar_producto.py` → `COMPARACION_IMPLEMENTACION.csv` (56 filas): esperado = oráculo propio; producto (`precio_de_si.py` sha256 `089fa5e3…aad8`, commit `059f4f68`) solo en columnas aparte; **residuo máximo oráculo-vs-producto 2,8e-14**; vs valores publicados en el paquete ≤ 5,1e-13. Casos A1–A5 dan fracciones exactas 265/3, 1330/13, 100, 380/7, 1005/13. Diferencias documentadas de contrato (no de valor): S4 desordenado → producto `sin_escalera` G19 (su `p_estrella` ordena igual que el oráculo); S5 k = 0,5 → producto se niega (guarda k ≥ 1), el oráculo da P* = 112 > ponderado 102,5; S3 precio ≤ 0 → `calcular` se niega, `p_estrella` calcula; S6 p inválidas → oráculo `DominioError`, `calcular` `sin_lectura`, pero `p_estrella` llamada directa devuelve 94,0 sin validar (hallazgo: la guarda vive en `calcular`, no en `p_estrella`); S7 n = 2 → oráculo P* = 90, `calcular` exige n = 3.

## Pendiente / siguiente acción exacta

1. Bloque B3: `codigo/efectos_probabilidades.py` → `EFECTOS_PROBABILIDADES.csv` (Viscofan 4.12/4.13/4.14: efecto puro de p separado del cambio total, 2×2 con ambos órdenes) y `codigo/sensibilidad_finita.py` → `SENSIBILIDAD_FINITA.csv` (rejilla anunciada en `INVENTARIO_Y_PLAN.md` §4). Commit y push.
2. Bloque B4: `PROTOCOLOS_COBERTURA.md` + ejemplos sintéticos del contrato de `objetivo_v64.py`. Commit y push.
3. Bloque B5: `DOSSIER_D1_D7_D11.md`, `HALLAZGOS.md`, `RESUMEN_PARA_CLAUDE.md`, `MANIFIESTO_SHA256.txt`. Commit y push final. Sin PR ni fusión.

## Modelo y limitaciones

- Sesión: Vibe Code de Mistral AI, modelo `mistral-large-4-0` (único modelo expuesto; sin selector de esfuerzo). Herramientas: Python 3.12.15 stdlib; red solo para GitHub (descarga de release vía `gh`); sin LibreOffice ni pipeline; no se abrieron XLSX.
- Consumo/facturación: no visible desde la sesión; no se afirma ningún límite configurado. No se compraron créditos ni se usaron servicios de pago.
- No se ha modificado el producto ni `main`; no hay PR ni fusión; no se han tocado los frentes A/B ni F1/Elis ni los resultados M1 revisados.
