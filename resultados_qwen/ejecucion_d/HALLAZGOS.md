# Hallazgos del frente D (bloque 1)

Solo lo reproducido con comandos del producto sobre la candidata `957af65`. Defectos, límites y decisiones pendientes, separados.

## Defectos reproducidos del producto

Ninguno en esta pasada. Los cuatro casos piloto ejecutados se comportaron conforme al contrato del banco en el componente probado (ver abajo). No se declara por ello cumplimiento global: 32 casos quedan sin ejecutar y las partes de agente quedan en relevo.

## Comportamientos conformes observados (con evidencia)

- **Cero publicado distinguible de ausencia (Q1-001):** `cero_comprobado` con fuente local conservada, revisor distinto del extractor y `sellar` con fecha del día → `selladas 1`, celda en `comprobadas`, `por_clase` distingue la clase. Control negativo: la misma celda como `dato_ausente` con valor en el libro → error del contrato ("dato ausente con un valor en el libro: es un dato (o un cero) que hay que contrastar") y no queda verificada. Evidencia: `evidencias/Q1-001/`.
- **Cero sin fuente no pasa (Q1-006):** `cero_comprobado` con archivo inexistente → pendiente ("la fuente local no está... su contraste no es reproducible") y `sellar` rechazado; `dato_ausente` sobre celda con valor en el libro → error del contrato. Evidencia: `evidencias/Q1-006/`.
- **Vigencia tras cambio de fuente (Q1-027):** sellada la caja, al mutar el archivo de la fuente la comprobación pasa a `desactualizada` ("la fuente cambió (sha256 distinto del registrado)"), deja de estar comprobada, `apto_por_entradas=false` y un nuevo `sellar` se rechaza. Evidencia: `evidencias/Q1-027/`.
- **Bloqueo de la vía manual (Q1-036):** `ficha.py --estado concluido` sin auditoría APROBADO → exit 3 ("no se confirma «concluido»... usa --provisional"); al cambiar `verificacion_entradas.json` (material auditado) la aprobación previa se retira sola ("aprobación retirada antes de leer el material... el material cambió después de la auditoría"); `ficha.py/informe.py --provisional` marcan "apta por entradas: no (1 de 321)", `apto_para_dinero_real: false`, aptitud `experimental`. Evidencia: `evidencias/Q1-036/`.

## Límites del entorno (no son defectos del producto)

- Sin LibreOffice (`soffice`) ni `pdftotext` en el sandbox (sin root): no se ejecuta el pipeline completo con recálculo de libros ni la re-lectura de fuentes PDF. Se ejecutaron las vías del producto que no los necesitan. Las 18 diferencias de archivos de texto de la candidata respecto a la base 4.14 son las correcciones 4.15 esperadas (la verificación 4.14 no aplica al código 4.15, según el README de la rama).
- El universo real del expediente sintético es de 321 celdas; los recuentos "3/2/5" de los fixtures Q1-019/032/036 se prueban como patrón (1 comprobada + pendientes), no con un universo de 5.

## Decisiones pendientes (no decididas aquí)

- Q1-030: caducidad temporal por antigüedad — no está en el contrato del registro; queda como DECISION_PENDIENTE del responsable de política.
- Q1-034: tratamiento del rango acotado 0–200 (punto justificado o sensibilidad documentada) — DECISION_PENDIENTE.
- Q1-035: política de validación de motores — DECISION_PENDIENTE; la ficha separa los tres planos y no declara apto para dinero real.

## No afirmado

Pasar estos controles de software no acredita aptitud económica ni predictiva ni aptitud para dinero real.
