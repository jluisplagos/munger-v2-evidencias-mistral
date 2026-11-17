# Recuentos vigentes · Frente A M2 · cobertura VM (GENERADO por scripts/generar_recuentos_doc.py · 2026-11-17T10:35:29Z)

**No editar a mano**: este documento lo regenera `generar_recuentos_doc.py` a partir de las salidas del pipeline.

## Estados contextuales (677 filas de COBERTURA_677.csv)

| Estado | n |
|---|---|
| REVISADO_CONTEXTUAL | 209 |
| PENDIENTE_CONTEXTUAL | 283 |
| CONFLICTO_CONTEXTUAL | 19 |
| REUTILIZADO_M1 | 60 |
| NO_APLICA | 106 |
| **total** | **677** |

## Estados contextuales por nivel

- Entradas verificadas en `verificacion_contexto.jsonl` (677): CONFLICTO_CONTEXTUAL 15 / NO_APLICA 210 / PENDIENTE_CONTEXTUAL 233 / REUTILIZADO_M1 43 / REVISADO_CONTEXTUAL 176
- Derivados (101 nodos en `DERIVADOS.json`): CONFLICTO_CONTEXTUAL 4 / PENDIENTE_CONTEXTUAL 50 / REUTILIZADO_M1 14 / REVISADO_CONTEXTUAL 33

## Dimensiones contextuales (sobre las entradas con fuente)

| Dimensión | Desglose |
|---|---|
| columna | CONFLICTO 2 / NO_DECIDIBLE 104 / OK 361 |
| fila | NO_DECIDIBLE 1 / OK 466 |
| perimetro | NO_APLICA 4 / OK 463 |
| reexpresion | CONFLICTO 14 / NO_APLICA 220 / NO_DECIDIBLE 196 / OK 37 |
| signo | NO_APLICA 19 / OK 448 |
| unidad | OK 467 |
| version | OK 467 |

## Controles

- `control_cobertura.py`: PASS=True, violaciones=0 (exit 0 si PASS).
- `control_negativo.py`: 219 mutaciones en memoria; detectadas por el contextual 140, por el mecanico 40; sondas bilaterales ok=True; sondas del revisor d375d80 en CONFLICTO: 5/5.

