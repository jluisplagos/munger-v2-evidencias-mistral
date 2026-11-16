# Resumen para Claude · Frente C (M2) · matemática independiente · rama mistral/m2-matematica-b

**Declaración:** Propuesta de evidencia o especificación de Mistral; pendiente de revisión e incorporación por el integrador. No APROBADO ni aptitud financiera general.

## Qué se hizo

Oráculo independiente del precio de Sí derivado de las ecuaciones (no copiado): `G(P) = Σ p_i max(V_i−P,0)`, `L(P) = Σ p_i max(P−V_i,0)`, `P* = max{P : G(P) ≥ k·L(P)}`, `precio_si = min(P*, V_N)`. Dos soluciones propias — forma cerrada por tramos con `Fraction` (exacta) y bisección — en `codigo/oraculo_precio_si.py` (selftest PASA). Demostraciones T1–T12 en `DEFINICIONES_Y_DEMOSTRACIONES.md`: existencia/unicidad de P*, `min V ≤ P* ≤ E[V]` para k ≥ 1 (k = 1 ⇒ P* = ponderado), forma cerrada, equivariancia (permutación/traslación/escala), monotonía en k, masas cero, degeneraciones, y **P* = expectil τ = 1/(k+1)** (k = 3 → τ = 0,25, convención Newey–Powell 1987) — no percentil (Koenker–Bassett 1978), no nivel de confianza/VaR (Rockafellar–Uryasev 2000), con enlaces verificables. La regla no demuestra límite de pérdidas: en P = P* la peor pérdida realizada posible es P* − min V (T12).

## Resultados principales (todos de script, una salida por tabla)

- **Comparación:** 57 casos fijados (5 Anexo C, 7 sintéticos, 6 históricos 4.12/4.13/4.14 — H6 Caja 4.13 añadido tras la revisión externa C1 — y 39 variantes 4.14) → `COMPARACION_IMPLEMENTACION.csv`. Esperado = oráculo propio; el producto (`precio_de_si.py` sha256 `089fa5e3…aad8`, commit `059f4f68`) solo en columnas aparte. Residuo máx oráculo-vs-producto **2,8e-14**; vs paquete ≤ 5,1e-13; fracciones exactas 265/3, 1330/13, 100, 380/7, 1005/13 en el Anexo C; 10/10 propiedades pasan (`resultados_casos.json`).
- **Probabilidades (D7), corregido tras C1:** `EFECTOS_PROBABILIDADES.csv` etiqueta cada comparación por entrega y **perímetro**. La pregunta de D7 es la de **Caja**: 2×2 Caja 4.12→4.13 = 39,2877008705 / 40,9481993309 / 39,1920496243 / 40,8263467773 €, total **+1,5386459068 € = «+1,5386 €» de D7, reproducido exactamente** (efecto p +1,6605 o +1,6343 € según orden; coincide con `SONDA_C_D7_CAJA.json` al 1e-12). La activa NIIF 16 (+1,5477811279 €) es otra pregunta válida, no discrepancia; guarda nueva detecta comparaciones cruzadas de perímetro. 4.13→4.14 (activa, p fijo) = −0,3658 €.
- **Seguimiento C2 (commit `6049513`, sobre `ba46ea5`):** la guarda de perímetros ahora compara `(empresa, perímetro)` canónicos de ambos extremos (identidad estructurada con fuente+sha256); la generación deriva de ella todas las etiquetas y se ejecutan 6 controles (3 positivos, 3 negativos incl. la sonda de la revisión) — todos pasan (exit 0). C1 se conserva intacta (Caja +1,5386459068 €).
- **Revisión externa atendida (commit `9366bdd`, CORRECCION_C):** respuesta en `RESPUESTA_REVISION_EXTERNA.md`; la falsa discrepancia de 0,0092 € retirada de todos los informes; el hallazgo de `p_estrella` matizado (la vía pública `calcular` rechaza p inválidas; se documentan precondiciones, no se declara fallo material).
- **Sensibilidad finita preanunciada:** `SENSIBILIDAD_FINITA.csv` (192 puntos; rejilla fijada antes en `INVENTARIO_Y_PLAN.md` §4). Rangos precio_si: A1 71,54–100,00; Vidrala 48,81–60,19; Viscofan 33,58–43,77.
- **Cobertura/materialidad (`objetivo_v64.py`):** `PROTOCOLOS_COBERTURA.md/.csv`. Re-derivación independiente coincide 24/24 con lo publicado. Condiciones del tratamiento en tabla (acción final, S-19 manda, comprar sin objetivo, zona por encima del precio de Sí, protocolo declarado, sostén en el ámbito). Ejemplos E1–E4: acción conservada (todo «caro») con objetivo material (rangos 51,26–65,72 € / 38,13–42,98 €); aisladas aditivas y conjunta no atribuible; sin_cobertura + sin fundamento ⇒ no determinada ⇒ condiciona; el rango no cubre hipótesis no calculadas y la variante de p sale exacta sin LibreOffice.
- **Dossier:** `DOSSIER_D1_D7_D11.md` (datos/derivaciones/políticas por decisión, qué garantiza cada regla y qué no, alternativas, pendientes; D2 vinculado sin invadir el frente B; «conclusión sin objetivo» solo como propuesta no implementada).

## Hallazgos materiales (detalle en HALLAZGOS.md)

- `p_estrella` del producto, llamada directamente con probabilidades inválidas, devuelve un número (94,0) sin negarse: la guarda vive en `calcular()`. Contraejemplo mínimo entregado; propuesta separada, sin tocar el producto.
- Diferencias de contrato documentadas (G19 en desordenados, k ≥ 1, precio > 0, n = 3 en `calcular`), ninguna de valor.
- D7 reproducido; la cifra «+1,5386 €» de D7 no se reproduce con los vectores publicados (+1,5478 €).

## Límites y pendientes

- Nada aquí es precio objetivo vigente ni recomendación de k, probabilidades o protocolo; no se eligió ningún parámetro por el resultado. No se ejecutó LibreOffice ni el pipeline; no se modificó el producto; no hay PR ni fusión; no se han tocado A, B, F1/Elis ni los resultados M1.
- Bloqueos del frente: ninguno (todos los insumos necesarios estaban en el índice verificado).
- Modelo/herramientas: Vibe Code de Mistral AI, `mistral-large-4-0`; Python 3.12.15 stdlib; red solo GitHub (Release base-4.14, sha256 `bb51942c…b7b93e` verificada, 251 insumos conformes). Consumo no visible desde la sesión; no se afirma ningún límite.

## Reproducibilidad

`COMANDOS.md` lista los comandos exactos; `MANIFIESTO_SHA256.txt` las huellas de todo `resultados_m2/matematica_b/`.
