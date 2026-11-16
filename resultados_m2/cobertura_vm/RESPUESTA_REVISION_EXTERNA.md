# Respuesta a la revisión externa · Frente A M2 · commit base revisado `08c9799`

Revisión leída desde `9366bdd563a986cdd6907ba2187f796f96898db6` (`revision/chatgpt-m2-20261116`) con `git fetch` + `git show`, sin fusionar. Mi rama: `mistral/m2-cobertura-vm`; encargo ejecutado: `revision_externa/m2/CORRECCION_A.md`.

**Propuesta de evidencia de Mistral; pendiente de revisión e incorporación por el integrador.** No APROBADO ni aptitud financiera general.

## Respuesta numerada a A1 y al encargo de CORRECCION_A.md

1. **Conservado**: inventario, huellas (251 insumos conformes), asociaciones texto↔PDF, recálculos mecánicos y los 677 registros como universo (60 M1 + 617 nuevas). No se fijó meta de coincidencias. Los estados mecánicos no cambian: 568 COINCIDE_PROPUESTO, 52 HIPOTESIS, 35 CONVENCION, 16 NO_APLICABLE, 6 DATO_AUSENTE.
2. **Completado**: nueva verificación **contextual** (`scripts/verificar_contexto.py`) que lee encabezados de tabla, fila impresa, posición del valor respecto a las columnas de ejercicio, unidad en la página, signo impreso y perímetro **desde los bytes conservados**, no desde `registro_base.json`. Procesada por las tablas/páginas inventariadas en los 22 lotes (≤30 entradas); primer lote real publicado enseguida (L05) y commit+push tras cada lote.
3. **Documentado por entrada**: `COBERTURA_677.csv` añade `estado_contextual`, `evidencia_contextual` (fila leída, encabezado, título de página, checks por dimensión), `limites_contextuales`; `resultados/verificacion_contexto.jsonl` y `OBSERVACIONES.jsonl` (reescritas con encabezados/filas leídas por página). Una cita auténtica de otra partida no se usa: la fila se ancla por sufijo de cita + cobertura de palabras y se compara con el concepto (con sinónimos ES/EN y partidas citadas «…»).
4. **Estados separados**: `estado_mecanico` y `estado_contextual` en columnas distintas. Resultados contextuales (677): **509 REVISADO_CONTEXTUAL, 60 REUTILIZADO_M1, 2 PENDIENTE_CONTEXTUAL, 106 NO_APLICA, 0 CONFLICTO_CONTEXTUAL**. Ninguna fila se presenta como plenamente revisada sin evidencia contextual; las 60 M1 quedan `REUTILIZADO_M1` con su alcance. `MAPA_REGENERACION.md` indica qué puede reutilizar el integrador (mecánico + contextual revisado + huellas vigentes) y qué requiere fuente/revisión/decisión (los 2 pendientes, las 52 hipótesis, 35 convenciones, 16 no aplicables, 6 ausentes, y los derivados con límites propagados).
5. **Derivados**: `DERIVADOS.json` añade `estado_contextual` (86 REVISADO, 14 REUTILIZADO_M1, 1 PENDIENTE propagado de `Historia!G23`), `limites_contextuales` propagados de los orígenes y `coherencia_unidades_origenes`. Recalcular la fórmula solo demuestra aritmética: el significado económico queda aparte, como encarga la revisión.
6. **Controles negativos** (`scripts/control_negativo.py` → `resultados/control_negativo.json`): sobre 38 entradas muestreadas, 154 mutaciones en memoria (periodo/columna a 2099, perímetro a cuentas individuales, unidad a acciones, concepto/partida a «Dividends»). **Detectadas por el verificador contextual: 108/154; detectadas por el mecánico: 0/154** — reproduce y acota lo que ya demostraba `SONDA_A_SEMANTICA.json`: el mecánico no atrapa metadatos contextuales mutados. Desglose: columna 33/40, perímetro 37/40, partida 32/40, unidad 6/34. **Límites del automatismo declarados**: en páginas de nota sin frase de unidad repetida la unidad queda NO_DECIDIBLE (8 casos reales); en filas no tabulares (boletín BME) la columna queda NO_DECIDIBLE (3); en páginas sin marca de perímetro, NO_DECIDIBLE (51); 1 fila de continuación sin etiqueta propia queda pendiente (`Vidrala Historia!G23 h_arrend`, p.19 CF_2019: dos tablas con el mismo valor 1,672 — activo por derecho de uso y pasivo por arrendamiento —; la ambigüedad se documenta, no se resuelve a mano). No se automatiza comprensión general ni se toca el verificador del producto.
7. **Actualizados**: tablas, observaciones, recuentos, mapa, resumen, manifiesto; esta respuesta. Comandos realmente ejecutados (todos con `python3 -B`, `PYTHONPATH=.trabajo/pylibs`):
   - `python3 -B scripts/verificar_contexto.py` → 677 entradas, estados contextuales arriba.
   - `python3 -B scripts/derivaciones.py` → 101 nodos, 101 COINCIDE_PROPUESTO mecánico, 0 ciclos/huecos, estados contextuales propagados.
   - `python3 -B scripts/construir_cobertura.py` → `COBERTURA_677.csv` (677 filas, 19 columnas incl. `estado_mecanico`/`estado_contextual`).
   - `python3 -B scripts/control_negativo.py` → 154 mutaciones, 108 detectadas por contextual, 0 por mecánico.
   - `python3 -B scripts/control_cobertura.py` → **PASS, 0 violaciones** (exit 0), ahora también valida estados contextuales, evidencia contextual obligatoria en REVISADO_CONTEXTUAL y coherencia CSV↔verificacion_contexto.
   - `python3 -B scripts/revisar_lote.py L00..L21` → lotes regenerados con evidencia contextual; commit+push tras cada lote.
   - Previamente (entrega base): `inventario.py`, `verificar_fuentes.py`, `asociacion_pdf.py`, `generar_manifiesto.py` (sin cambios en sus salidas salvo OBSERVACIONES.jsonl reescritas con contexto).

## Pendientes que quedan (no se resuelven adoptando parámetros)

- `Vidrala Historia!G22`/`G23` (h_deuda/h_arrend 2019): fila de continuación ambigua entre la tabla de activos por derecho de uso y la de pasivos por arrendamiento (mismo valor 1,672 en ambas, CF_2019 p.19). PENDIENTE_CONTEXTUAL; requiere lectura documental de la nota 8 completa.
- 52 HIPOTESIS, 35 CONVENCION, 16 NO_APLICABLE, 6 DATO_AUSENTE: sin cambio, conservadas como tales.
- Unidad no decidible en 8 páginas de nota (sin frase de unidad); perímetro no decidible en 51 páginas sin marca; columna no decidible en 3 filas no tabulares. La transformación (escala/signo) sí está acreditada mecánicamente en todas.
- 7 PDF candidatos siguen sin asociación declarada a entradas; selección parcial de insumos (251 archivos).
- La revisión contextual automatizada es heurística (sinónimos ES/EN, anclaje de fila): los 0 conflictos mecánicamente detected no sustituyen la revisión documental por otro contexto sobre el commit congelado.

## Entrega

Rama `mistral/m2-cobertura-vm`, commit congelado final en el push de esta respuesta (ver `git log`); `MANIFIESTO_SHA256.txt` regenerado; escritura solo en `resultados_m2/cobertura_vm/`. Sin PR, sin fusiones, sin tocar `main`, el producto, M1, B/C, decisiones, libros oficiales o sellos. Sin LibreOffice/pipeline/macros. Modelo: `mistral-large-4-0`; consumo no visible desde la sesión.
