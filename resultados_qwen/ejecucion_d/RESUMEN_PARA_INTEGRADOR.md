# Resumen para el integrador · frente D · cierre del programa (bloques 1–3) · fuente única: evidencias/recuentos.json

## Planos

| Plano | Estado |
|---|---|
| Entregado | arnés v2 + 30 especificaciones ejecutables + evidencias + matriz 36 + relevo 36 paquetes + ENTREGA.json, rama `mistral/d-qwen-aceptacion` |
| Revisado | banco 57/57 SHA + comprobar exit 0; candidata SHA `957af65` verificado en ejecución; base 4.14 materializada 6798/6798 (ZIP sha256 OK) |
| Integrado en el producto | **No** (Claude integra; este frente no modifica el producto) |
| Probado | 30/36 con componente real + aserciones (56/56 criterios evaluados CUMPLE_COMPONENTE); arnés 8/8 PASA; **0 casos completos del personaje** (sin runtime de agente aquí) |

## Matriz de 36 (cierre por categoría)

- Estados: **30 PARCIAL_COMPONENTE** · **6 NO_EJECUTADO** (Q1-028, Q1-030, Q1-031, Q1-032, Q1-033, Q1-035; Q1-028/Q1-032 con observación compartida de Q1-036 declarada).
- Veredicto de **componente**: **30 CUMPLE** · 6 sin veredicto (sin evidencia no hay positivo).
- Veredicto de **caso**: 29 sin veredicto de caso (pendiente de agente) · **1 NO_OBSERVABLE** (Q1-026: bloqueo de entorno con paquete listo) · 4 sin veredicto · **2 DECISION_PENDIENTE** (Q1-030, Q1-035 → política del usuario).
- Criterios: 56 evaluados en los 30 ejecutados, 56 CUMPLE_COMPONENTE; los criterios de agente no se evaluaron (no simulados).
- Naturaleza del banco intacta: **31 contrato / 3 propuestas / 2 decisiones pendientes**; Q1-034 ejecutado como contrato (rango 0–200 preservado, punto inventado rechazado).

## Tareas restantes concretas

1. **Runtime del coordinador (Claude)**: ejecutar `relevo/PAQUETES_RELEVO.json` (36 paquetes) con agentes reales — recorrido del personaje, auditorías APROBADO con agente nuevo; registrar SHA de cada ejecución y atribuir autor/ejecutor.
2. **Q1-026**: con pdftotext+soffice, seguir `paquete_runtime` en el paquete (CAMBIO listo en `evidencias/Q1-026/`; origen intacto verificado).
3. **Q1-031/Q1-033**: precio actual vs histórico con agente sobre `fase1_v63.json`.
4. **Q1-030/Q1-035**: decisiones de política del usuario (caducidad temporal; validación de motores).
5. **Revisión externa** de este bloque por Claude (D-HARNESS/D-36 en CONTROL.json) antes de marcar revisado.

## No dicho

Ningún caso completo del personaje acreditado; 30 CUMPLE son de componente mecánico con
aserciones. Sin aptitud para dinero real. Las precondiciones de extractor/revisor del arnés
son simuladas y están rotuladas como tales.
