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
