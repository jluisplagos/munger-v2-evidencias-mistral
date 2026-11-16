# Resumen para el integrador · frente D · v2 (CORRECCION_D) · recuentos desde evidencias/recuentos.json (fuente única)

## Planos

| Plano | Estado |
|---|---|
| Entregado | arnés v2 + 28 especificaciones + evidencias reejecutadas + matriz 36 filas, rama `mistral/d-qwen-aceptacion` |
| Revisado | banco 57/57 SHA + comprobar exit 0; candidata SHA verificado en ejecución = `957af65` |
| Integrado en el producto | **No** (encargo) |
| Probado | 27 casos con componente real y aserciones (COMPONENTE_OK); 8/8 pruebas del arnés PASA |

## Recuentos (de recuentos.json, igual que el CSV)

- Casos: 36. Estados: **27 PARCIAL_COMPONENTE** (ejecución propia COMPONENTE_OK) · **9 NO_EJECUTADO**
  (Q1-026 con bloqueo de entorno documentado; Q1-030/031/033/035 y los que no tienen spec ejecutable).
- Veredicto de **componente**: **27 CUMPLE** · 9 sin veredicto (sin evidencia no hay positivo).
- Veredicto de **caso**: 27 "sin veredicto de caso" (pendiente de agente) · 6 sin veredicto ·
  **1 NO_OBSERVABLE** (Q1-026, entorno) · **2 DECISION_PENDIENTE** (Q1-030, Q1-035).
- Naturaleza (del banco, intacta): **31 CONTRATO_REFERENCIADO / 3 PROPUESTA_ACEPTACION / 2 DECISION_PENDIENTE**.
  Q1-034 sigue contrato y se ejecutó como tal. Ninguna propuesta se convirtió en obligación.
- Observaciones compartidas declaradas: Q1-028 y Q1-032 (sobre Q1-036), no contadas como propias.
- Precondiciones de extractor/revisor: SIMULADAS (D-R4), declaradas en cada resultado.
- Los 17 esperados numéricos del banco no se ejecutaron vía producto (requiere recálculo con
  LibreOffice, ausente); la aritmética de derivados del producto se probó en Q1-005/Q1-018.

## No dicho

Ningún caso completo de personaje acreditado; no aptitud para dinero real. 27 CUMPLE son de
componente mecánico con aserciones, no de aceptación completa.
