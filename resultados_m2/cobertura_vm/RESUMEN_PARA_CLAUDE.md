# Resumen para Claude · Frente A M2 · cobertura integral Vidrala/Viscofan

**Propuesta de evidencia o especificación de Mistral; pendiente de revisión e incorporación por el integrador.** No APROBADO ni aptitud financiera general.

## Qué se entrega

Universo fijado cubierto completo en `resultados_m2/cobertura_vm/` (rama `mistral/m2-cobertura-vm`, escritura exclusiva en esa carpeta):

- `COBERTURA_677.csv` — 677 filas (una por empresa/celda; Vidrala 347, Viscofan 330) con clase, materialidad, estado propuesto, evidencia, límites, documento/sha256/página/columna, transformación, comparación con el libro, dependencia, lote y `origen_revision` (`M1_REUTILIZADA` en las 60 del piloto).
- `OBSERVACIONES.jsonl` — 123 observaciones reutilizables por empresa/archivo/página (cita localizada en los bytes, no el registro como prueba de sí mismo).
- `DERIVADOS.json` — 101 nodos (14 reutilizados del piloto, 87 nuevos) con origen de cada operando, fórmula, expresión evaluada, unidad, redondeo, significado, estado, resultado y hash de entradas.
- `scripts/` — pipeline reproducible (inventario, verificación de fuentes, derivaciones con `Decimal`, construcción de la cobertura, revisión por lote, control, asociación texto↔PDF).
- `resultados/` — inventario, verificación por entrada, 22 lotes (`lotes/lote_L00..L21.json`), asociación PDF, recuentos y control.
- `INVENTARIO.md`, `HALLAZGOS.md`, `MAPA_REGENERACION.md`, `MANIFIESTO_SHA256.txt`, `PUNTO_DE_RECUPERACION.md`.

## Recuentos (conciliados con 677 y con las 60 reutilizadas)

**Estados mecánicos** (sin cambios respecto a la entrega base `08c9799`): 568 COINCIDE_PROPUESTO, 52 HIPOTESIS, 35 CONVENCION, 16 NO_APLICABLE, 6 DATO_AUSENTE.

**Estados contextuales** (tras revisión A1 y corregidos por el seguimiento `63e366b`, columnas separadas en el CSV): 315 REVISADO_CONTEXTUAL, 196 PENDIENTE_CONTEXTUAL, 60 REUTILIZADO_M1, 106 NO_APLICA, 0 CONFLICTO_CONTEXTUAL.

| Concepto | n |
|---|---|
| Entradas totales | 677 (Vidrala 347 / Viscofan 330) |
| Piloto reutilizado (`M1_REUTILIZADA`) | 60 (26/34) |
| Nuevas (M2) | 617 (321/296) |
| Por clase | dato_publicado 454 · derivado 101 · cero_comprobado 13 · dato_ausente 6 · hipótesis 52 · convención 35 · no_aplicable 16 |
| Derivados | 101 = 14 piloto + 87 nuevos |
| Estados propuestos | COINCIDE_PROPUESTO 568 · HIPOTESIS 52 · CONVENCION 35 · NO_APLICABLE 16 · DATO_AUSENTE 6 · DIFERENCIA 0 · NO_ACREDITADO 0 |

## Método y reproducibilidad

1. Insumos: `python3 docs/programa_mistral_m2/herramientas/preparar_insumos.py --download` → 251 archivos conformes con sha256 verificada en `.trabajo/insumos_m2` (selección parcial; ZIP base-4.14 verificado). No se pidió nada más al usuario.
2. `scripts/verificar_fuentes.py`: sobre los bytes conservados, 467/467 entradas con fuente localizan página `[PDF PAGE n]`, cita literal y valor; `valor_modelo = valor_fuente × escala × signo` con `Decimal` cuadra en 467/467; comparación con el libro (XLSX solo lectura / registro oficial para `aux:`) coincide en 677/677 (24 vacíos declarados, vacíos en ambos lados).
3. `scripts/derivaciones.py`: grafo de 101 derivados, 0 huecos, 0 ciclos; recálculo con `Decimal`: 71 exactos, 30 dentro del redondeo a 3 decimales (≤0,0005 mm).
4. `scripts/asociacion_pdf.py`: 21 textos ↔ PDF candidato con offset 0; 426 valores en muestra (≤60 páginas/grupo) encontrados en la página PDF alineada (100%).
5. `scripts/control_cobertura.py` → **PASS, 0 violaciones**: rechaza duplicadas/faltantes, fuentes inexistentes o de huella no conforme presentadas como examinadas, operandos incoherentes y reutilización tras cambio sin recalcular. **Es autocomprobación del propio frente, no revisión independiente.**

Comandos: `python3 resultados_m2/cobertura_vm/scripts/{inventario,verificar_fuentes,derivaciones,construir_cobertura,control_cobertura,asociacion_pdf}.py` y `revisar_lote.py L00..L21` (con `PYTHONPATH=.trabajo/pylibs`; openpyxl 3.1.5 + pypdf 7.1.0 solo para lectura de XLSX/PDF).

## Pendientes honestos (conservados como tales)

- 52 hipótesis, 35 convenciones, 16 no aplicables y 6 datos ausentes (Vidrala `Análisis!C48` + `aux:intereses_financiacion_2023-2025`; Viscofan `Historia!H26`/`I26`) siguen sin decidir o sin fuente; no se declararon datos verificados.
- 13 ceros comprobados con fundamento en `fuente.tratamiento`; un cero no se acreditó por ausencia de la palabra.
- 7 PDF candidatos conservados sin asociación declarada a entradas (BORME 2026-5696, CNMV OIR, 1279_en-2016, 2275, IA_2016, IA_2021, IA_2023).
- Selección parcial de insumos (no producto completo). Asociación texto↔PDF verificada por muestra, no por documento completo.
- «COINCIDE_PROPUESTO» no acredita significado económico ni aptitud para invertir; no se fijó 677 coincidencias como objetivo.

## Corrección de la revisión externa (commit `9366bdd`, rama `revision/chatgpt-m2-20261116`)

Se ejecutó `CORRECCION_A.md`: verificación contextual por entrada leyendo encabezados/filas/columnas/unidad/signo/perímetro de los bytes conservados (`scripts/verificar_contexto.py`), estados mecánico y contextual en columnas separadas, límites propagados a los 101 derivados, controles negativos (`scripts/control_negativo.py`: 154 mutaciones, 108 detectadas por el contextual, 0 por el mecánico) y respuesta numerada en `RESPUESTA_REVISION_EXTERNA.md`. Lotes L00–L21 republicados con commit+push cada uno. Control PASS con 0 violaciones.

## Seguimiento externo `63e366b` (apartado A de SEGUIMIENTO.md)

Corregido el sobrealcance de estados contextuales (REVISADO de 509 → 315; las dimensiones no comprobadas pasan a PENDIENTE), la acreditación de unidad (la sonda «euros» vs «miles» del revisor ahora es CONFLICTO) y la de versión/reexpresión (contraste con el texto original del año comparativo). Negativos ampliados: 198 mutaciones, 151 detectadas por el contextual. Respuesta numerada en `RESPUESTA_SEGUIMIENTO_20261116.md`. Control PASS 0 violaciones.

## Estado de la rama y recuperación

Rama `mistral/m2-cobertura-vm` publicada en origin; primer punto de recuperación tras el inventario (commit `32bb45d`), lotes de la entrega base y lotes de la corrección A1 publicados con commit+push cada uno y commit+push tras cada uno de los 22 lotes (hasta `6dc3e74`, verificado con `git ls-remote`). `PUNTO_DE_RECUPERACION.md` recoge hecho/evidencia/pendiente/siguiente acción y límites. Sin PR, sin fusión, sin tocar `main`, el producto `munger-v2`, los frentes B/C, `resultados/` del piloto ni ningún registro oficial; no se ejecutó LibreOffice ni el pipeline.

## Modelo, herramientas y consumo

Sesión Vibe Code de Mistral AI, modelo **`mistral-large-4-0`** (único modelo expuesto; sin selector de esfuerzo). Herramientas: Python 3.12 stdlib + openpyxl 3.1.5 + pypdf 7.1.0 (en `.trabajo/pylibs`), git/gh, sha256. **Consumo/facturación no visible desde la sesión**: se declara que no se conoce; no se afirma ningún tope ni se compraron créditos.
