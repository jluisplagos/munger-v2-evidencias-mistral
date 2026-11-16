# Mapa de regeneración · Frente A M2

Qué puede aprovechar Claude para una futura regeneración, qué debe revisarse y qué queda bloqueado. **No es una orden de modificar libros ni de adoptar decisiones.**

## Reutilizable con huella vigente (sin revisar de nuevo salvo que cambien los bytes)

| Recurso | Huella | Uso |
|---|---|---|
| 21 textos `.txt` del expediente (Vidrala `texto/CF_2017..CF_2025`, `ES_2024`, `ES_2025`; Viscofan `texto/AR_2017/2019/2020/2025`, `CA_2023_es`, `CF_2021`, `CF_2022_compilacion`, `CF_2024`, `IA_2018_es`, `fuentes_mercado/BMadrid_…txt`) | sha256 conforme verificada (`resultados/inventario.json`, `OBSERVACIONES.jsonl`) | 467 entradas con fuente: página `[PDF PAGE n]`, cita, valor, unidad/escala/signo |
| 29 PDF candidatos | sha256 en `entrada/indice_fuentes.json` | asociación texto↔PDF verificada por contenido en muestra (21 textos, 426 valores, 100%) |
| XLSX `Vidrala_v63_evaluada.xlsx` / `Viscofan_v63_evaluada.xlsx` (solo lectura) | sha256 conforme | comparación con el libro (celdas `Hoja!Celda`, valores cacheados) |
| `verificacion_entradas.json` de cada expediente | sha256 conforme | valor registrado de celdas `aux:` y contraste del registro |
| Grafo de 101 derivados (`DERIVADOS.json`) | hash de entradas por nodo | recálculo con `Decimal`; 14 nodos del piloto reutilizados, 87 nuevos |
| 60 entradas del piloto M1 | evidencia corregida en `resultados/` + `revision_externa/REVISION_CHATGPT_2.md` | `origen_revision=M1_REUTILIZADA`; revisar solo si cambia un origen |

## Debe revisarse en regeneración (no reutilizar a ciegas)

- Las 52 HIPOTESIS, 35 CONVENCION, 16 NO_APLICABLE y 6 DATO_AUSENTE: son decisiones/supuestos/ausencias, no datos verificados; cada una con su justificación en `COBERTURA_677.csv` (`limites`, `dependencia`).
- Los 30 derivados con diferencia ≤ 0,0005 mm (redondeo del libro a 3 decimales): el valor exacto sale del recálculo, no del redondeo.
- La asociación texto↔PDF es por muestra (≤60 páginas por grupo); una regeneración completa exigiría recorrer todos los PDF candidatos página a página.
- Versiones inglesas «free translation»: prevalece el español en caso de discrepancia (aviso del piloto).

## Bloqueado o pendiente de fuente/decisión

- Vidrala `Análisis!C48` y `aux:intereses_financiacion_2023/2024/2025`: dato ausente (E4); requiere consulta a Vidrala o desglose del ESEF 2025. Sigue DATO_AUSENTE.
- Viscofan `Historia!H26`/`I26` (minoritarios 2018/2019): dato ausente declarado.
- 7 PDF candidatos conservados sin asociación declarada a entradas: BORME 2026-5696, CNMV OIR Vidrala 2026, 1279_en-2016, 2275 otra información relevante, IA_2016, IA_2021, IA_2023.
- Selección parcial de insumos (251 archivos): el producto completo no está materializado ni verificado; cualquier entrada que exija un PDF no conservado queda registrada como no acreditada (en este universo no ocurrió: 0 NO_ACREDITADO).
- Las nuevas fuentes opcionales que pudieran surgir seguirán el protocolo de la Release auxiliar del frente B; este frente no gestiona su preservación.

## Reglas operativas para regenerar

1. Ejecutar en orden: `inventario.py` → `verificar_fuentes.py` → `derivaciones.py` → `construir_cobertura.py` → `revisar_lote.py <L>` → `control_cobertura.py` → `asociacion_pdf.py` (con `PYTHONPATH=.trabajo/pylibs` para openpyxl/pypdf).
2. Si cambian bytes de una fuente, recalcular todo lo dependiente: el control rechaza resultados reutilizados tras cambiar operarios sin recalcular (hash de entradas por nodo y por fuente).
3. No fijar como objetivo 677 coincidencias; los estados honestos incluyen DIFERENCIA/NO_ACREDITADO cuando aparezcan.

## Estados de las dependencias para regeneración (seguimiento 63e366b, v2)

| Grupo | n | Estado contextual | ¿Qué puede reutilizar el integrador? |
|---|---|---|---|
| Datos/ceros con fuente, todas las dimensiones acreditadas | 264 | REVISADO_CONTEXTUAL | Sí: huella vigente + fila/columna/unidad/signo/perímetro/versión/reexpresión leídos |
| Derivados cuyos orígenes están todos revisados | 51 | REVISADO_CONTEXTUAL | Sí: fórmula + hash de entradas vigente |
| Piloto M1 (datos y derivados) | 60 | REUTILIZADO_M1 | Sí, con el alcance y huellas del piloto corregido |
| Fuentes con alguna dimensión no comprobada | 160 | PENDIENTE_CONTEXTUAL | No como revisadas: reexpresión no decidible (158), perímetro (40), unidad (8), signo (7), columna (3), fila (1) — solapamientos entre filas |
| Derivados con orígenes pendientes | 36 | PENDIENTE_CONTEXTUAL | No: heredan los límites de los orígenes (`limites_contextuales`) |
| Hipótesis / convenciones / no aplicables / ausentes | 109 | NO_APLICA (clase) | No como datos: requieren decisión o fuente |

El control (`control_cobertura.py`) sigue en PASS con 0 violaciones y valida la coherencia CSV↔verificación contextual. Ver `RESPUESTA_SEGUIMIENTO_20261116.md`.

## Estados de las dependencias para regeneración (revisión d375d80, v3) — tabla vigente

| Grupo | n | Estado contextual | ¿Qué puede reutilizar el integrador? |
|---|---|---|---|
| Fuentes con todas las dimensiones OK/NO_APLICA | 241 | REVISADO_CONTEXTUAL | Sí: huella vigente + fila/columna (por posición)/unidad+escala/signo/perímetro/versión/reexpresión leídos |
| Derivados cuyos orígenes están todos revisados | 41 | REVISADO_CONTEXTUAL | Sí: fórmula + hash de entradas vigente |
| Piloto M1 | 60 | REUTILIZADO_M1 (43 fuentes + 14 derivados; 3 de clase no aplica figuran en NO_APLICA) | Sí, con el alcance y huellas del piloto corregido |
| Fuentes con alguna dimensión no decidible | 183 | PENDIENTE_CONTEXTUAL | No como revisadas: reexpresión ND 179, perímetro ND 40, unidad ND 8, signo ND 7, columna ND 4, fila ND 1 — solapamientos entre filas |
| Derivados con orígenes pendientes | 46 | PENDIENTE_CONTEXTUAL | No: heredan `limites_contextuales` (p. ej. `Vidrala Historia!I22` ← `Historia!I23`) |
| Hipótesis / convenciones / no aplicables / ausentes | 106 | NO_APLICA (clase) | No como datos: requieren decisión o fuente |

Totales CSV (677): 282 REVISADO_CONTEXTUAL / 229 PENDIENTE / 60 REUTILIZADO_M1 / 106 NO_APLICA / **0 CONFLICTO**. Control PASS exit 0 con el código definitivo v3 (coherente con los resultados, a diferencia de la reproducción del revisor sobre `0224b71`). Las 5 sondas del revisor son CONFLICTO 5/5. Ver `RESPUESTA_A_D_20261116.md`.
