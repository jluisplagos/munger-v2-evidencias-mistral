# Relevo supervisado · frente D · v3 (respuesta D2-R4)

Nada de agente simulado: los registros de extractor/revisor del arnés llevan `_simulada` /
`[SIMULADO]` (D2-R7a). Lo que falta, con paquete exacto y responsable en
`relevo/PAQUETES_RELEVO.json` (36 paquetes; ninguno dice «nada pendiente» salvo la decisión
del usuario, que también se nombra).

## Bloqueos de entorno (error concreto)

- Sin `soffice`: recálculo del libro no corre (Q1-026 deuda neta 210; Q1-027 esperado 220). Sin
  `pdftotext`: Q1-026 se detiene en AR_2021..AR_2024; **además** hay errores de ipal/AR_2019/AR_2020
  separados en `evidencias/Q1-026/errores_bloqueo.json` (pdftotext solo no basta).
  Paquete listo: `evidencias/Q1-026/CAMBIO_Q1-026.json` alineado al banco (caja 95→90, deuda 300,
  deuda neta 210, cita exacta de `f5_026_nota.txt`, bloque `evidencia` restaurado). Origen intacto
  verificado (`origen_estado.txt`: `intacto=true`, `candidata_escribe_el_arnes=false`).
- Sin runtime de agente LLM: extracción, fases A/B/C, verificación y auditoría según
  `GUIA_RECORRIDO_SUPERVISADO.md`; mecanismo comprobado en 957af65 (código 10 + ESPERANDO.md;
  pasos 5/6/8/10/13 con los modelos de `config_v2.json`; fase C dos turnos con el mismo agente;
  verificación con agente nuevo; sin API ni credencial).

## Por caso pendiente

- **Q1-030 / Q1-035 (DECISION_PENDIENTE):** política del responsable (caducidad temporal;
  validación de motores). Decisión del usuario, no del banco ni del arnés.
- **Q1-031 / Q1-033:** precio histórico etiquetado vs actual ausente en `fase1_v63.json`;
  requiere fase A/objetivo con agente real.
- **Q1-028:** la retirada de aprobación al cambiar material se observó (compartida con Q1-036);
  falta la **reaprobación nueva con auditor real** y documentar la deuda neta vigente
  300+40−95=245 como transformación pendiente de verificar (fixture `f5_028_aprobacion.json`).
- **Q1-032:** el recuento 4/1/5 del fixture `f6_032_matriz.json` no es observable con el universo
  real (321); preparar expediente de 5 entradas soportado o registrar NO_OBSERVABLE.
- **Todos los ejecutados (29):** recorrido del personaje con agente real (entrada_usuario del
  banco, fases en orden, artefacto por criterio según `MAPA_CRITERIOS_BANCO.csv`).

## Reglas del relevo (del producto)

Agente por relevo con el modelo/esfuerzo de la config; solo su salida; sin internet ni memoria;
sin pipeline/LibreOffice/Excel en los relevos de agente; fase C dos turnos con el mismo agente;
auditoría con agente nuevo; nunca copiar salidas entre expedientes reales; LibreOffice en
secuencia con `flock` y perfil aislado cuando se recalcule.
