# Estado diario del examen (cinco líneas, sin jerga)

## 17-nov-2026 (noche)
1. Preparado: base y candidata comprobadas; rúbrica congelada; contradictor escrito; Ahold con historia de 10 años, trimestres de 2026 y extracto, parado antes de la fase A.
2. F1-IMPL (alquiler contado una vez) programado y con sus pruebas en verde; ahora lo revisa Fable. Límite: con el motor A, Ahold no podrá concluir hasta que el valor se calcule con el criterio nuevo.
3. Corregido un fallo del producto (acciones de Ahold mil veces más pequeñas), revisado en dos rondas.
4. Recibidas las etapa 1 de Jumbo, Zoetis, Vinci y Waste Management; sus webs bloquean la nube, así que Mistral descarga las fuentes desde el ordenador de la persona.
5. Lanzador del análisis directo por API: corregido tras la primera revisión; falta la segunda ronda. No se ha gastado nada de API.

## 18-nov-2026 (madrugada)
1. F1-IMPL cerrado tras dos rondas (conforme con límites); la plantilla V6.3.1, que calcula el valor con el alquiler contado una vez, está hecha y revisada, con correcciones acotadas en curso.
2. Ahold recorre ya la V6.3.1: la fase A eligió el motor A y da «No» provisional; parado antes del paso 7, que necesita la decisión F1-A.
3. Lanzador de API: dos rondas de revisión cerradas con límites; quedan las preguntas L1 y L2.
4. Hubo un reinicio del contenedor sin pérdida de trabajo.
5. Fable: 1 sesión usada de 6. Gasto de API: 0.

## 18-nov-2026, 11:30 (hora de la persona) · frente API preparado
- 0.4 hecho por la persona: environment `inferencia-aprobada` con revisora obligatoria `jluisplagos`; secreto `ANTHROPIC_API_KEY` solo en el environment; variable `MUNGER_TOPE_ACUMULADO_ANTHROPIC_USD = 180`; sin clave de Anthropic a nivel de repositorio (solo `MISTRAL_VIBE_CLI_KEY`).
- A1: autorización literal de la persona («Autorizo fusionar el lanzador del análisis directo en main del repositorio auxiliar»). `main` avanza sin fusión (fast-forward) 422a6f3 → 69f0385 (= `automatizacion/analisis-directo`; revisión tercera ronda en 74fe0cf «conforme con límites»; después solo datos del paquete de Ahold). Pruebas como en CI: 49 + 95 + 37, todas OK.
- A3 intento 1 (ejecución 44285698464, Ahold, Opus 5.5 high, tope 5): `ANTHROPIC_HTTP_400` a los 14 s, una llamada, sin causa registrada. Saldo de la consola sin cambio (198,75 USD): no cobrado. La reserva (4,498 USD) queda contada como coste incierto en el tope acumulado hasta reconciliar.
- Cambio `error-api-visible` (2df48f3 + 4ff75ab: guarda tipo y mensaje del error de la API, acotados; sin cambio de coste), revisado por agente distinto (CONFORME CON LÍMITES), fusionado en `main` del auxiliar por avance rápido 69f0385 → 4ff75ab con autorización literal de la persona («Autorizo fusionar el cambio error-api-visible en main del repositorio auxiliar»).
- A3 intento 2 (ejecución 44288081039): 400 `invalid_request_error` «The compiled grammar is too large…» (salidas estructuradas con el esquema de 79 propiedades). No cobrado.
- Cambio `esquema-sin-gramatica` (08fa48f + 3300424: sin `output_config.format`, esquema en el encargo, validación local reforzada), revisado por agente distinto (CONFORME CON LÍMITES), fusionado en `main` 4ff75ab → 3300424 con autorización literal de la persona («Autorizo fusionar el cambio esquema-sin-gramatica en main del repositorio auxiliar»). Prueba en seco: reserva 4,505884 USD.
- A3 intento 3 (ejecución 44290314915): pagada, 1,923 USD (388 375 tokens de entrada, 18 475 de salida); rechazada en línea por `JSON_INVALIDO` (objeto partido en dos bloques); revalidada fuera de línea: válida (vigilar · esperar · precio de Sí 31,61 · zona caro). `analisis_directo/ahold_44290314915/`.
- Cambio `varios-bloques-json` (une bloques sin texto intermedio ni claves repetidas; `revalidar.py` solo para rechazos de forma con el paquete enviado), revisado por agente distinto (CONFORME CON LÍMITES, R1/R2 corregidos), fusionado en `main` con autorización literal de la persona («Autorizo fusionar el cambio varios-bloques-json en main del repositorio auxiliar»).
- Gasto de API acumulado conocido: 1,923 USD (+ dos 400 no cobrados, contados como incierto en el tope hasta reconciliar).
