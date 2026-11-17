# Hallazgos del frente D · v3 (respuesta D2-R1…R7 sobre 1ac661b)

## Defectos del producto reproducidos

Ninguno. En los 29 casos con componente real ejecutado y aserciones (harness 3.0), el
producto se comportó conforme al contrato del banco en el componente probado.

## Defectos del arnés corregidos en esta respuesta (D2, sobre 1ac661b)

- **D2-R1 (material):** spec vacía o criterio sin aserciones daban COMPONENTE_OK; una aserción
  podía leer evidencia de otro caso (`../`); la matriz daba CUMPLE con un resultado forjado de
  dos campos; `json_lista_no_contiene` pasaba con salida vacía. Corregido en arnés v3:
  ERROR_ESPECIFICACION / ERROR por ruta / recálculo desde criterios+aserciones+`spec_sha256` /
  negativo exige `universo>0`. Prueba: sondas P1–P9 re-ejecutadas (`sondas/sondas_d2.json`):
  todas DETECTA; `pruebas_arnes.py` 16/16 PASA.
- **D2-R2 (material):** Q1-026 C1 aceptaba cualquier exit 1 con la subcadena «ausente o
  inexistente en texto/». Ahora exige las líneas exactas de AR_2021..AR_2024 y separa en
  `errores_bloqueo.json` los errores de ipal/AR_2019/AR_2020 (el bloqueo no es solo pdftotext).
  Q1-027: C2 discrimina (desactualizada por sha256, no comprobada); `apto=false` quedó en C4
  etiquetado como no discriminante. Control negativo por aserción: prueba 15 (todas las
  aserciones de todas las specs fallan sobre estado previo vacío).
- **D2-R3 (material):** Q1-026 usaba cifras que no están en su fixture (45.000/82.019/37.019).
  Alineado al banco: caja 95→90, deuda 300, deuda neta esperada 210, cita exacta de
  `f5_026_nota.txt`, bloque `evidencia` restaurado; queda **BLOQUEO_ENTORNO** en la matriz y no
  cuenta como componente CUMPLE. Q1-027 usa las cifras del fixture (80 millones, deuda 300).
- **D2-R4 (material):** los relevos de Q1-028/Q1-032 decían «nada pendiente». Ahora cada paquete
  nombra qué falta, quién lo hace y qué necesita; se incluye el recorrido del personaje
  (pasos 5/6/8/10/13, modelos de config_v2.json, fase C dos turnos mismo agente, verificación con
  agente nuevo, código 10) y el mapa por criterio del banco.
- **D2-R5:** mapa de los **109 criterios del banco** a aserciones/observables
  (`MAPA_CRITERIOS_BANCO.csv`: 59 con aserción, 50 sin aserción con relevo); `preserva_sentido`
  justificado por caso como dato; textos caducados corregidos; `pruebas_arnes.log` regenerado
  sobre el código entregado (16/16).
- **D2-R6:** `MANIFIESTO_SHA256.txt` regenerado; `sha256sum -c` exit 0 (antes fallaba
  RESUMEN_PARA_INTEGRADOR.md).
- **D2-R7:** marca `_simulada`/`[SIMULADO]` en toda comprobación escrita por el arnés (incl.
  diccionarios y `--revisor` del sellar); un log por ejecución (evidencias limpias); SHA
  observado de la candidata + árbol sin cambios sin commit exigido; banco desde SHA fijado;
  `base_414.py verify` sin `|| true`.

## Bloqueos de entorno (error concreto; no defectos del producto)

- Sin `soffice`: el pipeline con recálculo no corre aquí (deuda neta 210 de Q1-026 y esperado 220
  de Q1-027 quedan en relevo). Sin `pdftotext`: Q1-026 se detiene en AR_2021..AR_2024; además hay
  errores de ipal/AR_2019/AR_2020 (`evidencias/Q1-026/errores_bloqueo.json`).

## Decisiones pendientes (responsable de política; no decididas aquí)

Q1-030 (caducidad temporal), Q1-035 (validación de motores).

## No afirmado

29 CUMPLE son de **componente** (mecánico, con aserciones; precondiciones de extractor/revisor
SIMULADAS y rotuladas). **0/36 casos completos del personaje** (sin runtime de agente aquí).
Pasar controles de software no acredita aptitud económica ni para dinero real.
