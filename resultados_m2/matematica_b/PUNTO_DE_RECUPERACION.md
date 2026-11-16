# Punto de recuperación · Frente C (M2) · rama mistral/m2-matematica-b

Evidencia propuesta por Mistral; pendiente de revisión e incorporación por el integrador.

## Estado actual

- Repositorio auxiliar: `jluisplagos/munger-v2-evidencias-mistral` (origin verificado). Rama `mistral/m2-matematica-b` **publicada** en origin @ `f5b65f717f97f777471bc5343c6541805edcd7b4`.
- Insumos: Release `base-4.14` de `jluisplagos/munger-v2` descargada (sha256 `bb51942c…b7b93e` verificado) y `preparar_insumos.py --zip` ejecutado: 251 archivos conformes en `.trabajo/insumos_m2/` (selección parcial). Producto de referencia: commit `059f4f68dca7acf465b5f5b21de2dede84c885ff`.
- Bloque B1 terminado (commit `f9bb54b`, publicado): definiciones fijadas, demostraciones T1–T12 con bibliografía primaria, 56 casos fijados con provenance y sha256, plan finito y sensibilidad finita preanunciada.
- Bloque B2 terminado: `codigo/ejecutar_casos.py` → `resultados_casos.json`: las 10 propiedades globales pasan sobre los 56 casos (residuo F exacto 0 en trazos; bisección coincide ≤ 1e-9; P* ∈ [min V, ponderado] con k ≥ 1; k = 1 ⇒ ponderado; permutación, traslación, escala; monotonía en k). `codigo/comparar_producto.py` → `COMPARACION_IMPLEMENTACION.csv` (56 filas): esperado = oráculo propio; producto (`precio_de_si.py` sha256 `089fa5e3…aad8`, commit `059f4f68`) solo en columnas aparte; **residuo máximo oráculo-vs-producto 2,8e-14**; vs valores publicados en el paquete ≤ 5,1e-13. Casos A1–A5 dan fracciones exactas 265/3, 1330/13, 100, 380/7, 1005/13. Diferencias documentadas de contrato (no de valor): S4 desordenado → producto `sin_escalera` G19 (su `p_estrella` ordena igual que el oráculo); S5 k = 0,5 → producto se niega (guarda k ≥ 1), el oráculo da P* = 112 > ponderado 102,5; S3 precio ≤ 0 → `calcular` se niega, `p_estrella` calcula; S6 p inválidas → oráculo `DominioError`, `calcular` `sin_lectura`, pero `p_estrella` llamada directa devuelve 94,0 sin validar (hallazgo: la guarda vive en `calcular`, no en `p_estrella`); S7 n = 2 → oráculo P* = 90, `calcular` exige n = 3.

## Pendiente / siguiente acción exacta

- Bloque B3 terminado (pendiente de commit en este push): `EFECTOS_PROBABILIDADES.csv` — con V fijo, pasar de p referencia 0,20/0,60/0,20 a la desviación 4.12 0,25/0,60/0,15 baja el precio de Sí de Viscofan 4.13 de 40,164007 a 38,536370 (−1,6276 €; D7 cita 38,5364 ✓) y sube el de la 4.12 «Caja» de 39,287701 a 40,948199 (+1,6605 €; D7 cita 40,9482 ✓). Descomposición 4.12→4.13 (activa): cambio total +1,5478 € = efecto p (Shapley, dos órdenes) +1,6412 € + efecto V −0,0934 €; los dos órdenes dan efecto p entre +1,6276 y +1,6547 (D7: «+1,63 a +1,66» ✓). 4.13→4.14: −0,3658 € con p fijo (efecto puro de V). **Discrepancia documentada:** D7 cita «+1,5386 €» como cambio total; con los vectores publicados el total activa 4.12→4.13 es +1,5478 € (diferencia 0,0092 € no reproducible con los datos del paquete). `SENSIBILIDAD_FINITA.csv`: 192 puntos (3 casos × 8 k × 8 p), rejilla la anunciada en `INVENTARIO_Y_PLAN.md` §4; rangos de precio_si: A1 71,54–100,00; H1 48,81–60,19; H2 33,58–43,77; todos los residuos F exactos 0.

## Pendiente / siguiente acción exacta

- Bloque B4 terminado (pendiente de commit en este push): `PROTOCOLOS_COBERTURA.md` + `PROTOCOLOS_COBERTURA.csv` + `codigo/protocolos_cobertura.py`. Re-derivación independiente de la cobertura: coincide con lo publicado en `contraste_objetivo_v64.md` en los 24 parámetros presentes (Vidrala 12 + Viscofan 12). Condiciones necesarias/sucias del tratamiento documentadas en tabla. Ejemplos: E1 acción conservada (todas las variantes 4.14 en «caro») con objetivo material (rangos 51,26–65,72 € Vidrala, 38,13–42,98 € Viscofan; mpa=false ∀, mpo=true en varios); E2 aisladas +0,1333 € c/u y conjunta +0,2667 € = suma (linealidad en V dentro del tramo, T6; P* continua sin saltos) y conjunta no atribuible; E3 sin_cobertura + fs=false ⇒ no determinada ⇒ condiciona (real: PM1.familia Viscofan, PM1.roic_terminal Vidrala); E4 rango calculado cubre solo variantes calculadas y la variante de probabilidades sale exacta sin LibreOffice (40,164007 / 38,536370).

## Pendiente / siguiente acción exacta

1. Bloque B5: `DOSSIER_D1_D7_D11.md`, `HALLAZGOS.md`, `RESUMEN_PARA_CLAUDE.md`, `MANIFIESTO_SHA256.txt`, `COMANDOS.md`; commit y push final. Sin PR ni fusión.
## Modelo y limitaciones

- Sesión: Vibe Code de Mistral AI, modelo `mistral-large-4-0` (único modelo expuesto; sin selector de esfuerzo). Herramientas: Python 3.12.15 stdlib; red solo para GitHub (descarga de release vía `gh`); sin LibreOffice ni pipeline; no se abrieron XLSX.
- Consumo/facturación: no visible desde la sesión; no se afirma ningún límite configurado. No se compraron créditos ni se usaron servicios de pago.
- No se ha modificado el producto ni `main`; no hay PR ni fusión; no se han tocado los frentes A/B ni F1/Elis ni los resultados M1 revisados.
