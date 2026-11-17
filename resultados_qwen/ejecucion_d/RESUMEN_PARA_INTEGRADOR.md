# Resumen para el integrador · frente D · respuesta D2 sobre 1ac661b · fuente única: evidencias/recuentos.json

## Planos

| Plano | Estado |
|---|---|
| Entregado | arnés v3 + 28 especificaciones ejecutadas + evidencias + matriz 36 + mapa 109 criterios + relevo 36 paquetes + ENTREGA.json + RESPUESTA_D2.md, rama `mistral/d-qwen-aceptacion` |
| Revisado | banco 57/57 SHA + comprobar exit 0 (desde SHA fijado 4745f38); candidata 957af65 con SHA observado en ejecución y 0 cambios sin commit; base 4.14 6798/6798 (ZIP sha256 OK) |
| Integrado en el producto | **No** (Claude integra; este frente no modifica el producto) |
| Probado | 29/36 con componente real + aserciones (harness 3.0); arnés 16/16 PASA; sondas D2 P1–P9 DETECTA; **0/36 casos completos del personaje** |

## Matriz de 36 (cierre por categoría, recalculada desde evidencia validada)

- Estados: **29 PARCIAL_COMPONENTE** · **1 BLOQUEO_ENTORNO** (Q1-026; no cuenta como CUMPLE) · **6 NO_EJECUTADO** (Q1-028, Q1-030, Q1-031, Q1-032, Q1-033, Q1-035; Q1-028/Q1-032 con observación compartida de Q1-036 declarada).
- Veredicto de **componente**: **29 CUMPLE** (criterios no vacíos, todos CUMPLE_COMPONENTE, `spec_sha256` coincidente) · 7 sin veredicto.
- Veredicto de **caso**: 29 pendiente de agente · **1 NO_OBSERVABLE** (Q1-026) · 4 sin veredicto · **2 DECISION_PENDIENTE** (Q1-030, Q1-035 → usuario). **0 casos completos.**
- Criterios del banco: 109 mapeados en `MAPA_CRITERIOS_BANCO.csv` (59 con aserción, 50 sin aserción + relevo).
- Naturaleza del banco intacta: **31 contrato / 3 propuestas / 2 decisiones pendientes**.

## Tareas restantes concretas

1. **Runtime del coordinador (Claude)**: ejecutar `relevo/PAQUETES_RELEVO.json` (36 paquetes con qué/quién/necesita y recorrido del personaje) con agentes reales.
2. **Q1-026**: con pdftotext+soffice seguir `paquete_runtime` (CAMBIO alineado al banco: caja 95→90, deuda 300, deuda neta 210; origen intacto verificado; OJO: errores de ipal/AR_2019/AR_2020 además de pdftotext).
3. **Q1-027**: esperado 300−80=220 con recálculo (soffice); nuevo contraste con agente.
4. **Q1-028**: reaprobación nueva con auditor real + derivado 245. **Q1-032**: recuento 4/1/5 sobre universo de 5 soportado.
5. **Q1-031/Q1-033**: fase A con agente real. **Q1-030/Q1-035**: decisión del usuario.
6. **Revisión externa** de este bloque por Claude antes de marcar revisado.

## No dicho

Ningún caso completo del personaje acreditado; los CUMPLE son de componente mecánico con
aserción. Sin aptitud para dinero real. Las precondiciones de extractor/revisor del arnés son
simuladas y están rotuladas (`_simulada`/`[SIMULADO]` en cada registro).
