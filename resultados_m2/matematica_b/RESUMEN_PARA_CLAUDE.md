# Resumen para Claude · Frente C (M2) · matemática independiente · rama mistral/m2-matematica-b

**Declaración:** Propuesta de evidencia o especificación de Mistral; pendiente de revisión e incorporación por el integrador. No APROBADO ni aptitud financiera general.

## Qué se hizo

Oráculo independiente del precio de Sí derivado de las ecuaciones (no copiado): `G(P) = Σ p_i max(V_i−P,0)`, `L(P) = Σ p_i max(P−V_i,0)`, `P* = max{P : G(P) ≥ k·L(P)}`, `precio_si = min(P*, V_N)`. Dos soluciones propias — forma cerrada por tramos con `Fraction` (exacta) y bisección — en `codigo/oraculo_precio_si.py` (selftest PASA). Demostraciones T1–T12 en `DEFINICIONES_Y_DEMOSTRACIONES.md`: existencia/unicidad de P*, `min V ≤ P* ≤ E[V]` para k ≥ 1 (k = 1 ⇒ P* = ponderado), forma cerrada, equivariancia (permutación/traslación/escala), monotonía en k, masas cero, degeneraciones, y **P* = expectil τ = 1/(k+1)** (k = 3 → τ = 0,25, convención Newey–Powell 1987) — no percentil (Koenker–Bassett 1978), no nivel de confianza/VaR (Rockafellar–Uryasev 2000), con enlaces verificables. La regla no demuestra límite de pérdidas: en P = P* la peor pérdida realizada posible es P* − min V (T12).

## Resultados principales (todos de script, una salida por tabla)

- **Comparación:** 56 casos fijados (5 Anexo C, 7 sintéticos, 5 históricos 4.12/4.13/4.14, 39 variantes 4.14) → `COMPARACION_IMPLEMENTACION.csv`. Esperado = oráculo propio; el producto (`precio_de_si.py` sha256 `089fa5e3…aad8`, commit `059f4f68`) solo en columnas aparte. Residuo máx oráculo-vs-producto **2,8e-14**; vs paquete ≤ 5,1e-13; fracciones exactas 265/3, 1330/13, 100, 380/7, 1005/13 en el Anexo C; 10/10 propiedades pasan (`resultados_casos.json`).
- **Probabilidades (D7):** `EFECTOS_PROBABILIDADES.csv`. Con V fijo, p 0,25/0,60/0,15 vs referencia 0,20/0,60/0,20: 40,164007 → 38,536370 € (4.13) y 39,287701 → 40,948199 € (4.12 «Caja») — D7 reproducido. Total 4.12→4.13 = **+1,5478 €** = efecto p (Shapley) +1,6412 € + efecto V −0,0934 €; 4.13→4.14 = −0,3658 € (p fijo). Discrepancia anotada: D7 cita +1,5386 € (no reproducible; Δ 0,0092 €).
- **Sensibilidad finita preanunciada:** `SENSIBILIDAD_FINITA.csv` (192 puntos; rejilla fijada antes en `INVENTARIO_Y_PLAN.md` §4). Rangos precio_si: A1 71,54–100,00; Vidrala 48,81–60,19; Viscofan 33,58–43,77.
- **Cobertura/materialidad (`objetivo_v64.py`):** `PROTOCOLOS_COBERTURA.md/.csv`. Re-derivación independiente coincide 24/24 con lo publicado. Condiciones del tratamiento en tabla (acción final, S-19 manda, comprar sin objetivo, zona por encima del precio de Sí, protocolo declarado, sostén en el ámbito). Ejemplos E1–E4: acción conservada (todo «caro») con objetivo material (rangos 51,26–65,72 € / 38,13–42,98 €); aisladas aditivas y conjunta no atribuible; sin_cobertura + sin fundamento ⇒ no determinada ⇒ condiciona; el rango no cubre hipótesis no calculadas y la variante de p sale exacta sin LibreOffice.
- **Dossier:** `DOSSIER_D1_D7_D11.md` (datos/derivaciones/políticas por decisión, qué garantiza cada regla y qué no, alternativas, pendientes; D2 vinculado sin invadir el frente B; «conclusión sin objetivo» solo como propuesta no implementada).

## Hallazgos materiales (detalle en HALLAZGOS.md)

- `p_estrella` del producto, llamada directamente con probabilidades inválidas, devuelve un número (94,0) sin negarse: la guarda vive en `calcular()`. Contraejemplo mínimo entregado; propuesta separada, sin tocar el producto.
- Diferencias de contrato documentadas (G19 en desordenados, k ≥ 1, precio > 0, n = 3 en `calcular`), ninguna de valor.
- D7 reproducido; la cifra «+1,5386 €» de D7 no se reproduce con los vectores publicados (+1,5478 €).

## Límites y pendientes

- Nada aquí es precio objetivo vigente ni recomendación de k, probabilidades o protocolo; no se eligió ningún parámetro por el resultado. No se ejecutó LibreOffice ni el pipeline; no se modificó el producto; no hay PR ni fusión; no se han tocado A, B, F1/Elis ni los resultados M1.
- Pendiente: revisión externa sobre el commit congelado de esta rama. Bloqueos del frente: ninguno (todos los insumos necesarios estaban en el índice verificado).
- Modelo/herramientas: Vibe Code de Mistral AI, `mistral-large-4-0`; Python 3.12.15 stdlib; red solo GitHub (Release base-4.14, sha256 `bb51942c…b7b93e` verificada, 251 insumos conformes). Consumo no visible desde la sesión; no se afirma ningún límite.

## Reproducibilidad

`COMANDOS.md` lista los comandos exactos; `MANIFIESTO_SHA256.txt` las huellas de todo `resultados_m2/matematica_b/`.
