# Dossier D1 / D7 / D11 · Frente C (M2) · matemática independiente

**Declaración:** Propuesta de evidencia o especificación de Mistral; pendiente de revisión e incorporación por el integrador. No APROBADO ni aptitud financiera general. Ningún precio objetivo vigente se emite aquí; los importes históricos son solo contraste aritmético. D2 se vincula pero no se invade (es del frente B).

Nota de nomenclatura: «D11» se usa en dos sitios del paquete — en el Anexo C como la **escalera experimental del precio de Sí** (k = 3, tope NORMAL) y en `DECISIONES_PENDIENTES_4_14.md` como **D411-TERMINAL-R1** (terminal prudente de R1). Aquí se trata la escalera (ámbito de este frente) y se incluye un apartado para D411-TERMINAL-R1; se distingue cada uso.

---

## D1 · D413-FUNDAMENTO — criterio de materialidad para el objetivo

**Datos (publicados, con huella).** `fase_c.json` 4.14 de Vidrala y Viscofan (`configuracion_v64.parametros`: fundamento_suficiente, material_para_accion, material_para_objetivo, bases); `contraste_objetivo_v64.{md,json}` (cobertura y Δ €/% por variante); contrato 4.14 en `objetivo_v64.py` (`validar_juicio_objetivo`, reglas V1–V8, S3, S11); `DECISIONES_PENDIENTES_4_14.md` §2.1.

**Derivaciones (propias, reproducibles).** El contraste del objetivo es aritmética exacta sobre `precio_si = min(P*(V,p,k), V_N)`, que depende **solo** de (V, p, k, V_N): el oráculo propio reproduce todos los `precio_si` publicados del paquete (residuo ≤ 5,1e-13 en 57 casos) y por tanto todos los Δ del contraste. Ejemplos 4.14 (activa → variante): Vidrala estructura_SR2 56,0020 → 57,0263 (+1,0243 €), activa_sin_N1 +1,7482 €, parametro_maximo 51,2602 (−4,7418 €), heredado +8,7502 €; Viscofan estructura_SR2 +0,5726 €, parametro_maximo −1,6717 €, heredado +3,1785 € (todas las variantes, zona «caro»). Propiedad relevante: el contraste del objetivo **no necesita LibreOffice** (a diferencia del valor de los escenarios, que sí viene de la hoja recalculada).

**Políticas vigentes.** V4: base «calculada» exige contraste aislado o variación conjunta necesaria. V5/S11: un criterio propio del agente (p. ej. los 1,5 € de un agente) es `juicio_propio_del_agente`, base «juicio_economico», nunca «calculada». V6: declarar «no material» un parámetro sin fundamento suficiente cuyo contraste mueve el precio de Sí exige `comparado_con` con valor en €; sin él, «no determinada» y condiciona. V7: `politica_adoptada` exige registro con decisión, fecha y firma humana. R-a (con «comprar», toda hipótesis activa va a D10) y R-b (sin evidencia propia del objetivo, un contraste que mueve el precio de Sí al redondeo declarado no puede quedar fuera) son **propuestas** de D1, no adoptadas.

**Qué garantiza la regla actual y qué no.** Garantiza: coherencia mecánica (V1–V8), trazabilidad del contraste, que «no determinado» no se convierta en «no material», y que ninguna frase sin contenido excluya (V6) una hipótesis que el cálculo muestra que mueve el objetivo. No garantiza: que un Δ € sea «material» en sentido económico — no hay umbral matemático; la línea material/no material es juicio (con contrato) o política (con firma humana). Con dos empresas no hay base empírica para un umbral numérico (opciones 3–4 de D1); R-b es coherente con V6 ya implementada.

**Alternativas (de D1, no adoptadas):** (1) statu quo; (2) juicio con contrato propio + R-a/R-b (recomendada por el frente B del paquete); (3) umbral relativo común; (4) umbral absoluto por empresa. **Decisión pendiente:** adopción humana de política. **Vínculo con D2:** si la incertidumbre de P-M1 no está delimitada (D2), la abstención del objetivo prima sobre cualquier lista de condicionantes; D1 no se resuelve sin esa evidencia económica (frente B).

---

## D7 · D414-VARIACION-AGENTES — variación de juicio entre agentes (probabilidades)

**Datos (publicados, con huella).** `fase_b.json` de Viscofan 4.12 (`antecedentes/fase_b.json.4_12` y `ejecucion_1_4_13/fase_b.json`): desviación de la referencia mecánica 0,20/0,60/0,20 a **0,25/0,60/0,15** (desviacion ±0,05, clase «fundamentada», argumento escrito); `fase_b.json` de 4.13 y 4.14 (ambas empresas): vuelven a 0,20/0,60/0,20 con `desviacion = 0`. Vectores de escenarios en los `configuracion_v64_variantes.json` correspondientes (H1–H6 en `casos_fijados.json`). Precios de mercado usados solo para la zona: 90,10 € (Vidrala), 54,70 € (Viscofan).

**Derivaciones (propias, en `EFECTOS_PROBABILIDADES.csv`; corregido tras la revisión externa C1, commit `9366bdd`).** Cada comparación va etiquetada por empresa, entrega, **perímetro**, V y p; una guarda marca como PREGUNTA_DISTINTA cualquier «cambio total» que mezcle perímetros.

- **La pregunta de D7 es la de perímetro Caja** (variante `perimetro_alternativo` en 4.12 y 4.13). Tabla 2×2 Caja (k = 3), calculada con el oráculo propio desde los vectores publicados (H5, H6; sha256 en `casos_fijados.json`) y contrastada con `SONDA_C_D7_CAJA.json` de la revisión (residuo ≤ 1e-12 en las cuatro celdas):

  | Celda (perímetro Caja) | p 4.12 (0,25/0,60/0,15) | p referencia (0,20/0,60/0,20) |
  |---|---:|---:|
  | V Caja 4.12 (H5) | 39,2877008705 | 40,9481993309 |
  | V Caja 4.13 (H6) | 39,1920496243 | 40,8263467773 |

  Cambio total Caja 4.12→4.13: **+1,5386459068 €**, que redondea a **+1,5386 € como D7**: la cifra de D7 se reproduce exactamente y **ya no se declara ninguna discrepancia**. Efecto de p según orden: +1,6604984604 € (sobre V Caja 4.12) o +1,6342971529 € (sobre V Caja 4.13); media Shapley +1,6473978067 €. Efecto de V: −0,0956512462 € o −0,1218525537 € según orden.
- **La otra pregunta, también válida:** la misma descomposición sobre la activa (perímetro NIIF 16, H4→H3) da **+1,5477811279 €** = efecto p (Shapley) +1,6412 € + efecto V −0,0934 €. No refuta ni sustituye a la de Caja: son perímetros distintos. (Antes de C1 se presentó la diferencia 0,0092 € entre ambas como «discrepancia no reproducible»; era un error de identificación de la comparación, ya retirado de todos los informes.)
- Con V fijo de la activa 4.13, p desviación 4.12: 40,164007 → 38,536370 €. 4.13→4.14 (activa, p fijo en referencia): **−0,3658136463 €** (efecto puro de V). Contrafactuales (solo para medir el efecto de p, no propuestas): 4.14 con p 4.12 → 38,1914 €; Vidrala 4.14 → 54,0848 €.

**Matemática.** P* es el expectil τ = 1/(k+1) de la distribución de valores (k = 3 → τ = 0,25 en convención Newey–Powell); dentro de cada tramo es cociente de lineales en p y lineal en V, continua en (V, p): el efecto de las probabilidades es continuo, acotado y sin saltos (T2, T6, T7). No es un percentil ni un nivel de confianza (T10).

**Qué garantiza la regla y qué no.** Si se calcula la variante «probabilidades de referencia», entra **exacta** en el rango calculado y en la cobertura (precio_si depende solo de V, p, k, V_N; el oráculo la da sin LibreOffice: 38,536370 € en la celda de D7). No garantiza: que la referencia mecánica sea el juicio correcto (los dos agentes argumentan; D7 no elige), ni que las desviaciones no calculadas estén cubiertas (hasta que se calculen). Alternativas (de D7): (1) declarar el límite (statu quo); (2) contraste calculado de probabilidades (recomendada); (3) dos fases B independientes. Pendiente: convención + reparación de software (añadir la variante al cálculo de variantes y a la cobertura).

---

## D11 · escalera experimental del precio de Sí (Anexo C, «Decisión D11»; k = 3)

**Datos.** Anexo C §C.1–C.7 (sha256 `36497345…bdc54`); `precio_de_si.py` (sha256 `089fa5e3…aad8`); `precio.json` 4.14 de Vidrala (P* = 56,002005168244615, precio_si = 56,0020, ponderado = 60,6741, zona «caro», precio 90,10 €) y Viscofan (P* = 39,79819353512519, ponderado = 43,8056, zona «caro», precio 54,70 €); k = `k_asimetria` = 3 (convención del ejercicio).

**Derivaciones (propias, `DEFINICIONES_Y_DEMOSTRACIONES.md`).** T4: P* existe y es único (F_k continua y estrictamente decreciente). T5: min V ≤ P* ≤ E[V] para k ≥ 1, con P* = E[V] si k = 1. T6: forma cerrada por tramos (exacta con fracciones: 265/3, 1330/13, 100, 380/7, 1005/13 en los casos del Anexo C). T7/T8: equivariancia por permutación/traslación/escala y monotonía decreciente en k. T10: P* = expectil τ = 1/(k+1) (k = 3 → τ = 0,25, convención Newey–Powell 1987) — **no** un percentil (Koenker–Bassett 1978) **ni** un nivel de confianza (VaR/CVaR, Rockafellar–Uryasev 2000). T11: precio_si = min(P*, V_N) ∈ [min V, V_N]; el tope NORMAL es convención económica, no teorema. T12: en P = P* la peor pérdida realizada posible es P* − min V, **no acotada** por la regla; G(P*) = k·L(P*) acota solo el cociente de esperanzas.

**Verificación empírica.** Oráculo propio (traza exacta + bisección) vs producto (`precio_de_si.py` leído de `.trabajo`, sha256 y commit registrados): residuo máximo **2,8e-14** en 56 casos; vs valores publicados del paquete ≤ 5,1e-13; residuos F exactos 0 en fracciones. Las 10 propiedades globales pasan en los 56 casos (`resultados_casos.json`). Sensibilidad finita preanunciada (`SENSIBILIDAD_FINITA.csv`, 192 puntos): rangos de precio_si A1 71,54–100,00; H1 48,81–60,19; H2 33,58–43,77; k = 1 ⇒ P* = ponderado; el tope NORMAL se aplica en los extremos de la rejilla.

**Políticas.** k = 3 es convención del ejercicio; la zona dice si el precio cumple la regla matemática con los valores introducidos, **no** es la conclusión (D10 fundamento y D17 bloqueos mandan). El precio del escenario MALO no es un suelo de valor (V_MALO ≤ 0 ⇒ «sin precio del escenario MALO»).

**Qué garantiza y qué no.** Garantiza: existencia/unicidad de P*, acotación aritmética, reproducibilidad exacta, invariancia de contrato (salvo las guardas anotadas: G19 en desordenados, k ≥ 1, precio > 0, p válida — el producto valida en `calcular`, no en `p_estrella` llamada directa: con p inválidas devuelve 94,0; véase HALLAZGOS). No garantiza: límite de pérdidas (T12), que k = 3 sea buena política inversora (ninguna identidad lo prueba), que el expectil sea percentil o nivel de confianza, ni capacidad predictiva. **Alternativas:** k distinto (cuantificado en la sensibilidad, no recomendado), sin tope NORMAL, regla antigua de la hoja (`Diagnóstico V6!C156`, solo informada). **Pendiente:** mantener o cambiar la convención es decisión humana; D2 condiciona cualquier uso del objetivo.

### D411-TERMINAL-R1 (apartado aparte, mismo número en el otro documento)

Según `DECISIONES_PENDIENTES_4_14.md` §2.10: terminal prudente de R1, convención, recomendación «mantener», efecto del orden de 1 € en el MALO de Vidrala según su fase C (no calculado en el libro). Este frente no re-deriva el motor B completo (eso es del producto y requiere la hoja recalculada), así que ese efecto queda como **dato publicado**, no contrastado aquí. Lo que sí aporta la matemática de este frente: el MALO de Vidrala 4.14 es 44,3217 €/acción y el precio del escenario MALO no es un suelo (T12).
