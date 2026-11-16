# Definiciones y demostraciones · Frente C (M2) · matemática independiente del precio de Sí

**Declaración:** Propuesta de evidencia o especificación de Mistral; pendiente de revisión e incorporación por el integrador. No APROBADO ni aptitud financiera general.

Rama `mistral/m2-matematica-b`, carpeta `resultados_m2/matematica_b/`. Todo número de este frente sale de los scripts de `codigo/` (una única salida de cálculo por tabla); este documento solo enuncia y demuestra. El código del producto (`personaje_v2/scripts/`) se ha leído para fijar el contrato y se compara **después** de fijar casos y definiciones (`COMPARACION_IMPLEMENTACION.csv`); nunca se usa para generar los valores esperados del oráculo propio.

## 0. Material de partida y huellas

- Repositorio auxiliar `jluisplagos/munger-v2-evidencias-mistral` (origin verificado), rama `mistral/m2-matematica-b` @ `f5b65f7`.
- Producto de referencia: `jluisplagos/munger-v2` @ commit `059f4f68dca7acf465b5f5b21de2dede84c885ff`, recuperado de la Release `base-4.14` (`munger_v2_r1_entrega4.14_cierre_verificacion_entradas.zip`, 1.130.912.246 bytes, sha256 `bb51942cefb848e409a4828e3faeb70f94aa4d29af39cda6d90cd0a97cb7b93e`, verificado) y selección conforme de 251 archivos en `.trabajo/insumos_m2/` vía `docs/programa_mistral_m2/herramientas/preparar_insumos.py --zip` (cada archivo comprobado contra `docs/programa_mistral_m2/entrada/indice_fuentes.json`).
- Documentos leídos: `personaje_v2/ANEXO_C_precio_de_si.md` (sha256 `36497345…bdc54`), `personaje_v2/scripts/precio_de_si.py` (`089fa5e3…aad8`), `personaje_v2/scripts/configuracion_economica.py` (`247a3494…b445c4e`), `personaje_v2/scripts/objetivo_v64.py` (`bd6b09e3…7ac67`), `…_4_14/documentacion_cierre_4_14/DECISIONES_PENDIENTES_4_14.md` (`a5d529a6…b097`), fases A/B/C y configuraciones de los expedientes 4.14 de Vidrala y Viscofan y antecedentes 4.13 (4.12) de Viscofan, todos con sha256 en `casos_fijados.json`.
- No se ejecutó LibreOffice ni el pipeline; no se modificó el producto. XLSX solo en lectura (de hecho no se abrieron XLSX).

## 1. Definiciones fijadas (dominio y contrato)

**Definición 1 (escenarios).** Un caso es un par de vectores `(V, p)` con `V_i ∈ ℝ` finitos (valor por acción del escenario *i*) y `p_i ≥ 0` con `Σ p_i = 1` (probabilidades), más un parámetro `k > 0` y, para la salida recortada, el valor del escenario NORMAL `V_N`. El producto usa n = 3 con la convención de orden `B78 ≤ C78 ≤ D78` (MALO ≤ NORMAL ≤ BUENO) y `k = k_asimetria = 3` (convención del ejercicio, `config_v2.json`); el oráculo propio es general en n y en el orden (la permutación no cambia nada, T7 abajo). Las guardas del producto (`k ≥ 1`, `|Σp − 1| ≤ 1e-3`, `p_i ≥ 0`, precio actual > 0, valores numéricos, orden fijo) son **política del contrato**, no matemáticas; se listan en `oraculo_precio_si.guardas_producto` y se distinguen en cada tabla.

**Definición 2 (ganancia y pérdida esperadas).** Para un precio `P`:

```
G(P) = Σ_i p_i · max(V_i − P, 0)        L(P) = Σ_i p_i · max(P − V_i, 0)
F_k(P) = G(P) − k · L(P)
```

**Definición 3 (precio límite P*).** `P*(V, p, k) = max { P ∈ ℝ : F_k(P) ≥ 0 }`, es decir, el precio más alto que cumple `G(P) ≥ k·L(P)`.

**Definición 4 (salida del contrato D11).** `precio_de_si = min(P*, V_N)`; `precio_escenario_malo = min(V)` si `min(V) > 0` y `None` en otro caso; `ponderado = Σ p_i V_i`; la zona del precio actual es `bajo_malo` si `precio ≤ precio_escenario_malo`, `cumple_regla_k` si `precio ≤ precio_de_si`, `vigilar` si `precio ≤ ponderado`, y `caro` en otro caso.

## 2. Demostraciones

**T1 (identidad fundamental).** `G(P) − L(P) = E[V] − P` para todo `P`, donde `E[V] = Σ p_i V_i`.
*Prueba.* `max(v−P,0) − max(P−v,0) = v − P` (comprobar los tres casos `v > P`, `v = P`, `v < P`). Sumar con pesos `p_i`. ∎

**T2 (F es continua, lineal a trozos y estrictamente decreciente).** `F_k` es continua en ℝ (suma de continuas) y lineal en cada intervalo entre valores distintos de `V`. Si `P` no coincide con ningún `V_i`, sea `A = {i : V_i > P}`, `B = {i : V_i < P}`; entonces `G′(P) = −Σ_{i∈A} p_i`, `L′(P) = Σ_{i∈B} p_i` y `F′_k(P) = −(Σ_A p_i + k·Σ_B p_i)`. Como `Σ_A p_i + Σ_B p_i = 1`, la pendiente es `≤ −min(1, k) < 0`. En los quiebros (P = V_j) las pendientes izquierda y derecha siguen siendo negativas, así que `F_k` es estrictamente decreciente en todo ℝ. ∎

**T3 (límites).** `F_k(P) → +∞` cuando `P → −∞` (para `P < min V`, `L = 0` y `G = E[V] − P`) y `F_k(P) → −∞` cuando `P → +∞` (para `P > max V`, `G = 0`, `L = P − E[V]`). ∎

**T4 (existencia y unicidad de P*).** Por T2–T3, existe un único `P*` con `F_k(P*) = 0`, y `{P : F_k(P) ≥ 0} = (−∞, P*]`; por tanto `P* = max{P : G(P) ≥ k·L(P)}` está bien definido. ∎

**T5 (acotación).** `min V ≤ P* ≤ max V`. En concreto `F_k(min V) = G(min V) ≥ 0` (pues `L(min V) = 0`) y `F_k(max V) = −k·L(max V) ≤ 0`. Además, si `k ≥ 1`, `P* ≤ E[V]`, porque por T1 `F_k(E[V]) = (1−k)·L(E[V]) ≤ 0`; la igualdad `P* = E[V]` se da si y solo si `L(E[V]) = 0`, es decir, en el caso degenerado (toda la masa en un punto). Para `k = 1`, `P* = E[V]` exactamente. Para `0 < k < 1`, `P* > E[V]`. ∎

**T6 (forma cerrada por tramos).** Sean `v_(1) < … < v_(m)` los valores distintos de `V` con masas `q_j = Σ_{i : V_i = v_(j)} p_i`. En el tramo `[v_(j), v_(j+1)]`:

```
F_k(P) = Σ_{l>j} q_l (v_(l) − P) − k Σ_{l≤j} q_l (P − v_(l)) = 0
⇒  P_j = ( Σ_{l>j} q_l v_(l) + k Σ_{l≤j} q_l v_(l) ) / ( Σ_{l>j} q_l + k Σ_{l≤j} q_l )
```

`P*` es el único `P_j` que cae dentro de su tramo (si cae justo en un quiebro `v_(j)`, los dos tramos adyacentes lo dan). Si `m = 1` (todos los valores con masa iguales a `v`), `P* = v`. *Prueba.* Despeje directo de la ecuación lineal del tramo; la unicidad viene de T4. ∎

**T7 (equivariancias).** (a) Permutación: `P*` depende solo del multiconjunto `{(V_i, p_i)}`. (b) Traslación: `P*(V + c, p, k) = P*(V, p, k) + c`. (c) Escala positiva: `P*(aV, p, k) = a·P*(V, p, k)` para `a > 0`. *Prueba.* (a) las sumas no cambian. (b) `max(v + c − (P + c), 0) = max(v − P, 0)`. (c) `max(av − aP, 0) = a·max(v − P, 0)` para `a > 0`. ∎

**T8 (monotonía en k).** Si `0 < k₁ < k₂`, entonces `P*(k₂) ≤ P*(k₁)`, con desigualdad estricta salvo que `L(P*(k₁)) = 0`. *Prueba.* `F_{k₂}(P) = F_{k₁}(P) − (k₂−k₁)·L(P) ≤ F_{k₁}(P)`; como `F_{k₂}` es decreciente y `F_{k₂}(P*(k₁)) ≤ 0 = F_{k₂}(P*(k₂))`, se sigue `P*(k₂) ≤ P*(k₁)`. ∎

**T9 (masas cero y degeneraciones).** Los escenarios con `p_i = 0` no afectan a `G`, `L` ni `P*`; el acotamiento relevante es sobre los valores con masa positiva: `min{V_i : p_i > 0} ≤ P* ≤ max{V_i : p_i > 0}`. Si toda la masa está en un único valor `v`, `P* = v`. Si `p` tiene algún negativo o no suma 1, la Definición 3 no aplica (no hay distribución de probabilidad) y el oráculo lanza `DominioError`; el producto se niega con `sin_lectura` (guarda `|Σp−1| ≤ 1e-3`). ∎

**T10 (P\* es un expectil, no un percentil ni un nivel de confianza).** Newey y Powell definen el expectil `e_τ` como el minimizador de `E[ |τ − 1{V ≤ m}| · (V − m)² ]`; la condición de primer orden es

```
τ · E[(V − m)⁺] = (1 − τ) · E[(m − V)⁺]      ⇔      τ · G(m) = (1 − τ) · L(m)
```

Igualando con `G(P*) = k·L(P*)`: `(1−τ)/τ = k`, es decir, **`P* = e_τ(V)` con `τ = 1/(1+k)`** en la convención de Newey–Powell (el peso `τ` cae sobre las desviaciones positivas). Con `k = 3`, `τ = 0,25`: P* es el expectil 0,25 de la distribución de valores de escenario (en la convención contraria, que pesa las pérdidas con `τ`, es el expectil 0,75). El expectil `τ = 0,5` es la media. Un **percentil** (cuantil) es otra cosa: minimizador de la pérdida-check `E[ρ_τ(V−m)]` con `ρ_τ(u) = u·(τ − 1{u<0})`, cuya condición de primer orden es `P(V ≤ q_τ) = τ`; es un nivel de la distribución (un estadístico de orden), no una media ponderada. Un **nivel de confianza** pertenece a la semántica VaR (Rockafellar–Uryasev): `VaR_β` es el cuantil β de la pérdida, «la pérdida no supera `VaR_β` con probabilidad β». La ecuación `G = k·L` compara dos esperanzas; **no asigna probabilidad a ningún suceso**, así que P* no es «un 75 % de nada»: con k = 3 el número 3 es un cociente de esperanzas, no una probabilidad ni un nivel de confianza. Expectil y percentil coinciden solo en casos simétricos (o en τ = 0,5, donde ambos son la media); en general `e_τ ≠ q_τ`. ∎

**T11 (propiedades de P\* frente a la salida recortada).** De T4–T8: `P* ∈ [min V, E[V]]` para `k ≥ 1`; `P*` decrece con `k`; `P*` es invariante por permutación y equivariante por traslación y escala positiva. La salida recortada `precio_de_si = min(P*, V_N)` hereda la equivariancia y la monotonía en k, y además cumple `min V ≤ precio_de_si ≤ V_N` y `precio_de_si = V_N` (tope NORMAL aplicado) exactamente cuando `P* > V_N`. La comprobación del DCF inverso (interpolar la tabla `Análisis!A108:B188` en `Palancas!C14` y comparar con `C78` al 1 %) es una **verificación de coherencia interna de la hoja**, no parte de la matemática de P*; el tope `V_N` es una convención económica de D11 («no pagar más que el escenario central»), no un teorema. ∎

**T12 (qué NO demuestra la regla).** (a) En `P = P*` la pérdida realizada en el escenario *i* es `max(P* − V_i, 0)`; la peor pérdida realizada posible es `P* − min V`, que la regla no acota salvo por T5. `G(P*) = k·L(P*)` acota solo el **cociente de esperanzas**, no ningún cuantil de la pérdida. (b) `P* ≥ V_MALO` (con V_MALO = min V) es aritmética (T5), no una afirmación de que el escenario MALO acote la pérdida real: MALO es una historia elegida y la quiebra está modelada como un único recorte (`Palancas!C22`); la realidad puede ser peor. (c) Ninguna identidad matemática valida `k = 3` como política inversora. (d) Que P* sea un expectil no lo convierte en percentil ni en nivel de confianza (T10), ni demuestra capacidad predictiva. ∎

## 3. Dos soluciones independientes y tolerancias

1. **Cerrada por tramos (T6)** con aritmética exacta (`fractions.Fraction`): para entradas racionales (los cinco casos del Anexo C lo son) da `P*` exacto (p. ej. `265/3`, `1330/13`, `100`, `380/7`, `1005/13`) con residuo `F(P*) = 0` exacto.
2. **Bisección** sobre `F_k` en `[min V, max V]` (200 iteraciones, muy por debajo del épsilon de float64), con residuo `|F(P)|` informado.

Las dos se contrastan en cada caso (`dif_trazos_biseccion`, `residuo_F_*`) y con el producto en `COMPARACION_IMPLEMENTACION.csv`. Tolerancia justificada: con float64 el residuo de bisección queda en ~1e-13 relativo; se informa el residuo real en cada fila en lugar de exigir un umbral arbitrario. Los casos históricos tienen V con 16 dígitos (floats del paquete); ahí se usa `Fraction(float)` (valor binario exacto del float publicado), así que el oráculo calcula sobre exactamente los bytes/valores publicados.

## 4. Bibliografía primaria (enlaces verificables; acceso anotado el 16-nov-2026)

1. Newey, W. K., & Powell, J. L. (1987). *Asymmetric Least Squares Estimation and Testing*. Econometrica, 55(4), 819–847. [DOI 10.2307/1911031](https://doi.org/10.2307/1911031) · [JSTOR 1911031](https://www.jstor.org/stable/1911031) · [RePEc/IDEAS](https://ideas.repec.org/a/ecm/emetrp/v55y1987i4p819-47.html). Definición original del expectil (pérdida cuadrática asimétrica) y su condición de primer orden. Acceso: resumen público; texto completo de pago (JSTOR). Verificado por búsqueda bibliográfica en esta sesión.
2. Koenker, R., & Bassett, G. (1978). *Regression Quantiles*. Econometrica, 46(1), 33–50. [DOI 10.2307/2290993](https://doi.org/10.2307/2290993). Definición del cuantil/percentil por pérdida-check (contraste con el expectil: `|u|` frente a `u²` asimétrica). Acceso: resumen público; texto de pago.
3. Rockafellar, R. T., & Uryasev, S. (2000). *Optimization of Conditional Value-at-Risk*. Journal of Risk, 2(3), 21–41. [DOI 10.21314/JOR.2000.038](https://doi.org/10.21314/JOR.2000.038) · [PDF público (Univ. de Washington)](https://sites.math.washington.edu/~rtr/papers/rtr179-CVaR1.pdf). Semántica de VaR (cuantil β de la pérdida) y CVaR (esperanza condicionada más allá del cuantil): por qué un nivel de confianza es un cuantil y no una esperanza, y por qué `G = k·L` no es ni VaR ni CVaR. Acceso: PDF público. Verificado en esta sesión.

Estas tres fuentes primarias bastan para la relación estadística relevante (T10): expectil (N&P 1987) ≠ percentil (Koenker–Bassett 1978) ≠ nivel de confianza/VaR (Rockafellar–Uryasev 2000). No se usa bibliografía secundaria. Límite de acceso: los textos completos de N&P y Koenker–Bassett son de pago; la condición de primer orden del expectil se cita de la definición estándar (loss `ρ_τ(u) = |τ − 1{u<0}| u²`) y se contraste con la del cuantil (`ρ_τ(u) = u(τ − 1{u<0})`).

## 5. Límites de este documento

- Demuestra propiedades de la regla definida; **no** demuestra que la regla sea buena política, que k = 3 sea adecuado, o que las probabilidades de los expedientes sean correctas.
- Los casos históricos son importes publicados en el paquete 4.14; se usan solo para contraste aritmético, nunca como objetivo vigente de inversión. No se emite ningún precio objetivo vigente.
- La descomposición en efectos de probabilidades (sección 2 del encargo) está en `EFECTOS_PROBABILIDADES.csv`; la sensibilidad finita preanunciada, en `SENSIBILIDAD_FINITA.csv`; la revisión de protocolos de cobertura, en `PROTOCOLOS_COBERTURA.md`; el dossier D1/D7/D11, en `DOSSIER_D1_D7_D11.md`.
