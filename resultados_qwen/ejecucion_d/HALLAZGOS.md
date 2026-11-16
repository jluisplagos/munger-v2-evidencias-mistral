# Hallazgos del frente D (cierre de la sesión)

Solo lo reproducido con comandos del producto sobre la candidata `957af652cdc3bef3d67e8623c9572138bac685e9`. Defectos, límites y decisiones pendientes, separados.

## Defectos reproducidos del producto

Ninguno. En los 31 casos con componente real ejecutado, el producto se comportó conforme al contrato del banco en el componente probado (registro de entradas, vigencia, salidas). No se declara cumplimiento global: 5 casos quedan sin ejecutar y toda la capa de agente/personaje queda en relevo supervisado.

## Comportamientos conformes observados (muestra; evidencia en `evidencias/<caso>/`)

- **Clases de entrada distinguidas:** cero_comprobado verificado y sellado (Q1-001); cero sin fuente → pendiente y `sellar` rechazado (Q1-006); dato_ausente sobre celda con valor en el libro → error del contrato (Q1-003, Q1-006); no_aplicable justificado listado aparte (Q1-002); dato como hipótesis sin `justificacion_clase` → error N2, con ella → listado en `datos_como_hipotesis` (Q1-024, Q1-004).
- **Unidad/escala/signo/período/perímetro/columna:** escala no declarada no se asume (Q1-007); equivalencia miles/millones con escala declarada (Q1-010); gasto entre paréntesis y signo −1 con tratamiento (Q1-008, Q1-011); moneda no reconocida → pendiente U7 (Q1-016); período que no corresponde a la columna → error (Q1-023); perímetro de segmento sin justificación → error, con justificación pasa (Q1-012); cita de otra columna no acredita (Q1-009).
- **Conflictos y fuentes:** discrepancia registrada con ambas fuentes, sin elegir por favorabilidad; resuelto con evidencia → verificado (Q1-015); petición de omisión queda en incidencia y el universo no se reduce (Q1-022); lectura externa sin bytes no cuenta como comprobada (Q1-017); 3 fuentes presentes se reexaminan y 2 ausentes quedan pendientes (Q1-029).
- **Derivados:** origen pendiente → derivado no comprobado; fórmula con operando que no influye (o[x]−o[x]+o[y]) → error U4 (Q1-005); reexpresión cuantificada 210−190=20 con versión v2 vigente y v1 histórica (Q1-018); reexpresado declarado con histórico conservado (Q1-014).
- **Vigencia y aprobaciones:** fuente mutada tras sellar → `desactualizada` (sha256 distinto), ya no comprobada, re-sellar rechazado (Q1-027); cambio de fundamento de hipótesis → la comprobación sellada deja de valer (Q1-020); cambiar el material auditado retira la aprobación sola ("aprobación retirada antes de leer el material") (Q1-036); ficha oficial `--estado concluido` sin auditoría APROBADO → exit 3; provisionales marcan "apta por entradas: no" con recuentos y `apto_para_dinero_real: false` (Q1-036, Q1-019, Q1-032).
- **Instrucción embebida:** el párrafo de la página 3 no permite marcar verificado sin contraste; la tabla de la página 1 sí verifica (Q1-021).

## Bloqueos de entorno (con error concreto; no son defectos del producto)

- **Q1-026 (cambio en copia nueva):** `cambiar_base.py preparar` se detiene con exit 1: "«archivo» ausente o inexistente en texto/: 'AR_2021.txt' … 'AR_2024.txt'" — los textos de esos años son PDF y falta `pdftotext` en el sandbox (sin root). Se confirmó además que nunca sobrescribe: con destino existente responde "ya existe … no se sobrescribe" (exit 1). El CAMBIO de relevo queda en `evidencias/Q1-026/CAMBIO_Q1-026.json`. Hace falta también LibreOffice para el recálculo del libro y la auditoría nueva del material final.
- **Pipeline completo y agentes:** sin `soffice` no corre el recálculo del libro; sin runtime de agente LLM no corren las fases del personaje. Ambas partes quedan en `RELEVO_SUPERVISADO.md`.

## Decisiones pendientes (no decididas aquí)

- Q1-030 caducidad temporal por antigüedad; Q1-034 tratamiento del rango acotado 0–200; Q1-035 política de validación de motores. Van como DECISION_PENDIENTE al responsable de política; el banco no las convierte en obligación.

## No afirmado

Pasar estos controles de software no acredita aptitud económica ni predictiva ni aptitud para dinero real (`apto_para_dinero_real: false` en las salidas del producto observed).
