# Resumen para el integrador · frente D · cierre de la sesión

## Entregado / revisado / integrado / probado

| Plano | Estado |
|---|---|
| Entregado | `resultados_qwen/ejecucion_d/` en rama `mistral/d-qwen-aceptacion` del auxiliar: arnés, 23 especificaciones ejecutables (4 piloto + 19 bloque 2), MATRIZ_EJECUCION.csv (36 filas), evidencias por caso, docs |
| Revisado | banco: 57/57 SHA256 OK + `comprobar_banco.py` exit 0 (36 casos, 17 esperados, 9 controles negativos). Candidata: HEAD remoto = SHA fijado `957af65`; ZIP base-4.14 sha256 OK y materializado 6798/6798 |
| Integrado en el producto | **No** (encargo: no fusionar ni PR al producto; `jluisplagos/munger-v2` solo se leyó) |
| Probado contra el producto | 31/36 casos con componente real ejecutado (PARCIAL_COMPONENTE); 5 sin ejecutar (Q1-030, Q1-031, Q1-033, Q1-034, Q1-035) |

## Recuentos (casos, no comandos)

- Estados de ejecución: **31 PARCIAL_COMPONENTE** · **5 NO_EJECUTADO** · 0 EJECUTADO_COMPLETO (la capa de agente no existe en esta sesión).
- Veredictos: **29 CUMPLE** (componente real, evidencia en `evidencias/`) · **3 DECISION_PENDIENTE** (Q1-030, Q1-034, Q1-035) · **1 NO_OBSERVABLE** (Q1-026, bloqueo de entorno con error concreto) · **3 sin veredicto** (Q1-031, Q1-033 y uno más sin ejecutar).
- Naturaleza conservada: 31 contrato / 3 propuesta (Q1-019, Q1-022, Q1-029) / 2 decisión pendiente (Q1-030, Q1-035). Ninguna propuesta se convirtió en obligación; los criterios propuestos dentro de casos contractuales conservan su distinción.
- Los 17 esperados numéricos del banco **no** se ejecutaron como componente del producto: la aritmética de derivados del producto (fracciones exactas, U2/U4) se probó con los derivados de los casos (Q1-005, Q1-018); recalcular los esperados en otro script no ejecutaría el producto, y el recálculo del libro necesita LibreOffice (ausente).

## Criterios cubiertos vs pendientes

- Cubiertos (componente real): cero/absencia/N-A, unidad/escala, signo, columna/período, perímetro, moneda, versiones/reexpresión, conflicto con/sin resolución, instrucción embebida, firma≠publicación, fuente sin bytes, recuentos parciales, vigencia por sha256 y por fundamento, invalidación de aprobaciones, bloqueo de exportación manual.
- Pendientes: capa completa de agente/personaje (entrada del usuario, fases A/B/C, auditoría APROBADO), pipeline con recálculo (LibreOffice), Q1-026 completo (pdftotext), Q1-031/033 (precio actual/objetivo con agente), las 3 decisiones de política.

## Lo que esto no dice

No declara aptitud para dinero real ni cumplimiento global: 31 casos a nivel de componente mecánico, ninguno completo con agente; el estado inicial 0/36 pasa a 31 con componente real ejecutado.
