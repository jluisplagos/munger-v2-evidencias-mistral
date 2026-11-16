# Inventario, alcance y plan finito · Frente C (M2) · matemática independiente

**Declaración:** Propuesta de evidencia o especificación de Mistral; pendiente de revisión e incorporación por el integrador. No APROBADO ni aptitud financiera general.

## 1. Inventario y verificación

| Insumo | Estado |
|---|---|
| origin = `jluisplagos/munger-v2-evidencias-mistral` | verificado (`git remote -v`) |
| Rama `mistral/m2-matematica-b` @ `f5b65f7` | publicada en origin (`git ls-remote` coincide con HEAD local) |
| ZIP base-4.14 (Release de `jluisplagos/munger-v2`) | descargado; sha256 `bb51942c…b7b93e` == `configuracion.json` |
| `.trabajo/insumos_m2/` (251 archivos) | `preparar_insumos.py --zip` → `seleccion_conforme: 251`, cada sha256 comprobado contra `indice_fuentes.json`; selección parcial (`producto_completo_verificado: false`) |
| `ANEXO_C_precio_de_si.md`, `scripts/precio_de_si.py`, `scripts/configuracion_economica.py`, `scripts/objetivo_v64.py`, `DECISIONES_PENDIENTES_4_14.md` | leídos; sha256 en `casos_fijados.json` |
| Fases A/B/C y configuraciones 4.14 de Vidrala y Viscofan; antecedentes 4.13/4.12 de Viscofan | leídos (`precio.json`, `configuracion_v64_variantes.json`, `fase_b.json`, `contraste_objetivo_v64.{md,json}`, `cambio_decisiones_*_4_14.json`) |
| Fuentes que faltan para este frente | Ninguna bloqueante. No se necesitan PDF nuevos: el frente C trabaja sobre vectores (V, p, k, precio) ya publicados en JSON. Los PDF del índice son del frente A. |
| Herramientas | Python 3.12.15 stdlib (json, csv, hashlib, fractions, decimal). Sin LibreOffice, sin pipeline, sin XLSX. Modelo de la sesión: `mistral-large-4-0` (Vibe Code de Mistral AI); consumo/facturación no visible desde la sesión. |

## 2. Alcance (universo finito del frente)

1. Definición y oráculo independiente del precio de Sí (P*, precio_de_si, zona): solución por tramos exacta + bisección; contraste con los 5 casos del Anexo C, 7 sintéticos propios y 6 históricos fijados (H6 = Viscofan 4.13 «Caja», añadido tras la revisión externa C1) + las 39 variantes calculadas 4.14 (20 Vidrala + 19 Viscofan) = 57 casos.
2. Propiedades y límites (T1–T12) como pruebas y como aserciones ejecutables (`oraculo_precio_si.py --selftest`, `ejecutar_casos.py`).
3. Relación con expectiles con bibliografía primaria (N&P 1987; Koenker–Bassett 1978; Rockafellar–Uryasev 2000).
4. Contraste de k y probabilidades en los casos históricos fijados, con el efecto puro de probabilidades separado del cambio total entre entregas (incluido 0,20/0,60/0,20 frente a 0,25/0,60/0,15 en Viscofan 4.12→4.13/4.14).
5. **Sensibilidad finita preanunciada** (ver §4): rejilla fija, anunciada aquí antes de ver resultados.
6. Revisión del contrato de cobertura/materialidad de `objetivo_v64.py` con ejemplos sintéticos.
7. Dossier D1/D7/D11 (D2 se vincula sin invadir el frente B).

Fuera de alcance: frentes A y B, F1/Elis, motor C, valores actuales nuevos, precios objetivo vigentes, cambios de software del producto, PRs y fusiones.

## 3. Plan y bloques (con puntos de recuperación)

| Bloque | Contenido | Salida |
|---|---|---|
| B1 | Definiciones, demostraciones, casos fijados, plan | este archivo + `DEFINICIONES_Y_DEMOSTRACIONES.md` + `casos_fijados.json` + `PUNTO_DE_RECUPERACION.md` → commit/push `f9bb54b` |
| B6 | Corrección acotada tras revisión externa (`9366bdd`, CORRECCION_C): caso H6 Caja 4.13, tablas 2×2 por perímetro, guarda de pregunta cruzada, retiro de la falsa discrepancia D7, matización del hallazgo `p_estrella`, `RESPUESTA_REVISION_EXTERNA.md` | regeneración de casos/resultados/CSV + respuesta + manifiesto → commit/push |
| B2 | Oráculo propio + propiedades ejecutables + comparación con el producto | `codigo/oraculo_precio_si.py`, `codigo/ejecutar_casos.py`, `codigo/comparar_producto.py`, `COMPARACION_IMPLEMENTACION.csv`, `resultados_casos.json` → commit/push |
| B3 | Efectos de probabilidades y sensibilidad finita | `EFECTOS_PROBABILIDADES.csv`, `SENSIBILIDAD_FINITA.csv` → commit/push |
| B4 | Protocolos de cobertura y ejemplos sintéticos | `PROTOCOLOS_COBERTURA.md`, `codigo/protocolos_cobertura.py`, CSV auxiliar → commit/push |
| B5 | Dossier D1/D7/D11 + entregas finales | `DOSSIER_D1_D7_D11.md`, `HALLAZGOS.md`, `RESUMEN_PARA_CLAUDE.md`, `MANIFIESTO_SHA256.txt`, `PUNTO_DE_RECUPERACION.md` final → commit/push |

## 4. Sensibilidad finita PREANUNCIADA (antes de ver resultados)

Motivo: D7 mide que el cambio de probabilidades movió el precio de Sí de Viscofan ≈ +1,63…+1,66 €; se quiere cuantificar, sobre los vectores fijados, cuánto mueven P* y precio_de_si (i) la masa de las colas y (ii) k, sin simular ninguna distribución nueva como si estuviera calibrada.

- Casos: A1 (Anexo C caso 1), H1 (Vidrala 4.14 activa), H2 (Viscofan 4.14 activa). V y precio fijos de `casos_fijados.json`.
- Rejilla de k: `k ∈ {1, 1,5, 2, 2,5, 3, 4, 5, 10}` (dominio de la guarda del producto k ≥ 1; k = 1 es el caso límite P* = ponderado).
- Rejilla de probabilidades (sobre el V fijo de cada caso): simétricas `p = (δ, 1−2δ, δ)` con `δ ∈ {0,05, 0,10, 0,15, 0,20, 0,25, 0,30}` (dominio: p_i ≥ 0, Σ = 1 ⇒ δ ≤ 0,5), más los dos vectores históricos asimétricos y su espejo `(0,25, 0,60, 0,15)` y `(0,15, 0,60, 0,25)` para no elegir el lado favorable.
- Salidas por punto: P*, G(P*), L(P*), residuo F(P*), precio_de_si, zona con el precio fijo del caso. Generado por `codigo/sensibilidad_finita.py` → `SENSIBILIDAD_FINITA.csv`. Nada de muestreo, nada de distribuciones nuevas.

## 5. Reglas de juego seguidas

- Escribir solo en `resultados_m2/matematica_b/` (temporales en `.trabajo/`); no tocar `main`, el producto, los resultados M1 ni los otros frentes.
- Separar dato publicado / derivación / hipótesis / convención / ausencia. Las guardas del producto se marcan como política, no como matemática.
- No elegir parámetros por producir resultados favorables; no emitir precio objetivo vigente; no recomendar k, p o protocolo como óptimos.
- Commit y push tras cada bloque con `PUNTO_DE_RECUPERACION.md` actualizado. Sin PR, sin fusiones, sin rondas de autoaprobación.
