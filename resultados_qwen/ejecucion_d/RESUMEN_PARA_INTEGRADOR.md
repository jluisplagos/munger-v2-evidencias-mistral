# Resumen para el integrador · frente D · bloque 1

## Entregado / revisado / integrado / probado

| Plano | Estado |
|---|---|
| Entregado | arnés + 4 especificaciones ejecutables + MATRIZ_EJECUCION.csv (36 filas) + evidencias del piloto, en `resultados_qwen/ejecucion_d/` de la rama `mistral/d-qwen-aceptacion` |
| Revisado | banco verificado (57/57 SHA, comprobar exit 0); candidata verificada (ZIP base 4.14 sha256 OK, 6798/6798; HEAD remoto = SHA fijado) |
| Integrado en el producto | **No**: no se fusiona ni se abre PR al producto (encargo) |
| Probado contra el producto | 4 casos piloto a nivel de componente real (Q1-001, Q1-006, Q1-027, Q1-036) + patrones reutilizados en Q1-025/028/032/035; 29 casos mapeados pero NO_EJECUTADO |

## Recuentos (no confundir comandos con casos)

- Casos del banco: **36**. Ejecutados a nivel de componente: **4** (piloto). Mapeados con componente/interfaz identified pero sin ejecutar: **29**. Con veredicto propio: **6 CUMPLE** (Q1-001, Q1-006, Q1-027, Q1-028, Q1-032, Q1-036 — los 4 piloto + 2 por patrón ejecutado), **3 DECISION_PENDIENTE** (Q1-030, Q1-034, Q1-035), **27 sin veredicto** (no ejecutados).
- Estados de ejecución: `PARCIAL_COMPONENTE` 7 · `NO_EJECUTADO` 29.
- Naturaleza conservada: 31 contrato / 3 propuesta (019, 022, 029) / 2 decisión pendiente (030, 035). Ninguna propuesta se convirtió en obligación.
- Criterios cubiertos en los piloto: cero publicado vs ausencia, cero sin fuente, vigencia por sha256, bloqueo de exportación manual con pendientes. Pendientes: los 17 numéricos como ejecución del componente derivado real, y toda la capa de agente/personaje.

## Lo que esto no dice

No declara aptitud para dinero real ni cumplimiento global del producto: 32/36 casos sin ejecutar y sin capa de agente. El estado inicial 0/36 pasa a 4 casos con componente real ejecutado; el resto queda mapeado y en relevo.
