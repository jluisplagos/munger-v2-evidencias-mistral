# Punto de recuperación · Frente C (M2) · rama mistral/m2-matematica-b

Evidencia propuesta por Mistral; pendiente de revisión e incorporación por el integrador.

## Estado actual

- Repositorio auxiliar: `jluisplagos/munger-v2-evidencias-mistral` (origin verificado). Rama `mistral/m2-matematica-b` **publicada** en origin @ `f5b65f717f97f777471bc5343c6541805edcd7b4`.
- Insumos: Release `base-4.14` de `jluisplagos/munger-v2` descargada (sha256 `bb51942c…b7b93e` verificado) y `preparar_insumos.py --zip` ejecutado: 251 archivos conformes en `.trabajo/insumos_m2/` (selección parcial). Producto de referencia: commit `059f4f68dca7acf465b5f5b21de2dede84c885ff`.
- Bloque B1 terminado (commit `f9bb54b`, publicado): definiciones fijadas, demostraciones T1–T12 con bibliografía primaria, 56 casos fijados con provenance y sha256, plan finito y sensibilidad finita preanunciada.
- Bloque B2 terminado: `codigo/ejecutar_casos.py` → `resultados_casos.json`: las 10 propiedades globales pasan sobre los 56 casos (residuo F exacto 0 en trazos; bisección coincide ≤ 1e-9; P* ∈ [min V, ponderado] con k ≥ 1; k = 1 ⇒ ponderado; permutación, traslación, escala; monotonía en k). `codigo/comparar_producto.py` → `COMPARACION_IMPLEMENTACION.csv` (56 filas): esperado = oráculo propio; producto (`precio_de_si.py` sha256 `089fa5e3…aad8`, commit `059f4f68`) solo en columnas aparte; **residuo máximo oráculo-vs-producto 2,8e-14**; vs valores publicados en el paquete ≤ 5,1e-13. Casos A1–A5 dan fracciones exactas 265/3, 1330/13, 100, 380/7, 1005/13. Diferencias documentadas de contrato (no de valor): S4 desordenado → producto `sin_escalera` G19 (su `p_estrella` ordena igual que el oráculo); S5 k = 0,5 → producto se niega (guarda k ≥ 1), el oráculo da P* = 112 > ponderado 102,5; S3 precio ≤ 0 → `calcular` se niega, `p_estrella` calcula; S6 p inválidas → oráculo `DominioError`, `calcular` `sin_lectura`, pero `p_estrella` llamada directa devuelve 94,0 sin validar (hallazgo: la guarda vive en `calcular`, no en `p_estrella`); S7 n = 2 → oráculo P* = 90, `calcular` exige n = 3.

## Estado actual (tras seguimiento C2 sobre ba46ea5, commit de revisión `6049513`)

- C2 ejecutado: la guarda de perímetros compara de verdad `(empresa, perímetro)` canónicos de ambos extremos (identidad estructurada en `casos_fijados.json`, vinculada a vector+fuente+sha256); la generación deriva de `misma_pregunta(a,b)` todas las etiquetas de los cambios totales (resultado: OK, 3/3); controles en tabla 6 de `EFECTOS_PROBABILIDADES.csv`: positivos Caja/Caja y NIIF16/NIIF16 entre años, negativos Caja/NIIF16, empresas distintas y la sonda exacta de la revisión (H6 mutado a NIIF16 vs H5 Caja) — **todos pasan, exit 0**; un negativo inesperado provocaría exit 1. Oráculo y producto sin cambios; C1 conservada (Caja +1,5386459068 € = «+1,5386 €» de D7).
- Regenerado y re-ejecutado con exit 0: 57 casos, 10/10 propiedades, residuo máx vs producto 2,842e-14, 192 puntos de sensibilidad, cobertura 24/24, `EFECTOS_PROBABILIDADES.csv` 37 filas. `RESPUESTA_REVISION_EXTERNA.md` actualizada con C1+C2. D1/D7/D11 siguen pendientes; sin PR ni ciclos.

## Estado previo (tras la revisión externa M2, commit de revisión `9366bdd`)

- Rama mantenida: `mistral/m2-matematica-b` (la rama `revision/chatgpt-m2-20261116` NO fusionada; revisión leída con `git show 9366bdd…:ruta`). Entrega revisada: `fe46f07`.
- Corrección acotada C1 ejecutada (CORRECCION_C): (i) retirada la falsa «discrepancia no reproducible de 0,0092 €» — era mezcla de perímetros; (ii) caso H6 añadido (Viscofan 4.13 `perimetro_alternativo` Caja, V = [30.6406803941772, 44.8547080140724, 59.2982622162535], sha256 `c8e7270f…913d2` verificado en fuente) → universo 57 casos; (iii) tabla 2×2 Caja recalculada con el oráculo: 39,2877008705 / 40,9481993309 / 39,1920496243 / 40,8263467773 €, total **+1,5386459068 € = «+1,5386 €» de D7** (coincide con `SONDA_C_D7_CAJA.json` al 1e-12; efecto p +1,6604984604 / +1,6342971529 € según orden); la activa NIIF 16 (+1,5477811279 €) queda como pregunta aparte etiquetada; (iv) guarda nueva detecta comparaciones cruzadas de perímetro (resultado: OK); (v) hallazgo `p_estrella` matizado: la vía pública `calcular()` rechaza p inválidas, se documentan precondiciones, no se declara fallo material.
- Salidas regeneradas y re-ejecutadas con exit 0: 57 casos, 10/10 propiedades, residuo máx oráculo-vs-producto 2,842e-14, sensibilidad 192 puntos, cobertura 24/24 coincidente. `RESPUESTA_REVISION_EXTERNA.md` responde C1 numerado con las comprobaciones ejecutadas y los límites pendientes. D1/D7/D11 quedan como políticas pendientes; no se adoptó k ni probabilidades; los precios históricos no se usan como objetivo vigente.
- Commits publicados: `f9bb54b`, `4caaabd`, `bf7ca2a`, `f311593`, `fe46f07` (entrega), y el commit de corrección de este bloque.

## Pendiente / siguiente acción exacta

1. **Comprobación del integrador sobre el commit congelado de esta rama**, limitada a la guarda C2 y sus salidas (la aritmética C1/D7 ya está confirmada). Sin nuevos ciclos por iniciativa propia.
2. Nada más en este frente: no PR, no fusión, no tocar main/producto/A/B/M1/F1-Elis.

## Modelo y limitaciones

- Sesión: Vibe Code de Mistral AI, modelo `mistral-large-4-0` (único modelo expuesto; sin selector de esfuerzo). Herramientas: Python 3.12.15 stdlib; red solo para GitHub (descarga de release vía `gh`); sin LibreOffice ni pipeline; no se abrieron XLSX.
- Consumo/facturación: no visible desde la sesión; no se afirma ningún límite configurado. No se compraron créditos ni se usaron servicios de pago.
- No se ha modificado el producto ni `main`; no hay PR ni fusión; no se han tocado los frentes A/B ni F1/Elis ni los resultados M1 revisados.
