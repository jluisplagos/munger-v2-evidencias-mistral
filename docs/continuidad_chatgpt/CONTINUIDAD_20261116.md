# Continuidad de ChatGPT · Munger V2 · 16-nov-2026

Este documento conserva el estado conocido para otra conversación. Es una referencia, no una autorización para adoptar políticas financieras. Antes de informar novedades, consultar las ramas remotas: los autores pueden haber publicado después. No confundir entregado, revisado, integrado, probado y apto para un uso concreto.

## Objetivo y preferencias

El usuario quiere terminar cuanto antes sin rebajar calidad y utilizar el sistema para apoyar decisiones con dinero real. No acepta que se cierre con verificaciones financieras insuficientes. Quiere instrucciones concretas, prompts completos y poca carga manual. Los ZIP de ChatGPT le han dado problemas; usar GitHub y textos copiables. Los repositorios públicos están autorizados. No pedir otra vez las decenas de partes ya conservadas en la Release.

No garantizar ausencia de errores o pérdidas. No inventar probabilidades, firmas, resultados de pruebas, porcentajes globales o fechas de finalización. Los anteriores porcentajes orientativos no son una medida de validación. Una auditoría APROBADO o una batería PASA no demuestra por sí sola aptitud económica o predictiva.

El proyecto es un sistema de análisis con código, plantillas Excel, prompts, agentes y controles; no un modelo de pesos entrenado sobre 116 empresas. Requiere su entorno y orquestación. La guía actual sigue describiendo relevos supervisados: no prometer una aplicación universal totalmente autónoma ya terminada.

## Repositorios y responsables

- Producto: https://github.com/jluisplagos/munger-v2
- Evidencias separadas: https://github.com/jluisplagos/munger-v2-evidencias-mistral
- Claude: integración técnica y F1/Elis. Sus propuestas no se adoptan automáticamente.
- Mistral Code: tres sesiones A/B/C, cada una en su rama y carpeta del auxiliar. Modelo comunicado por esas sesiones: mistral-large-4-0. Consumo no visible; no suponer saldo actual ni intentar gastar créditos por gastarlos.
- Qwen: chat con archivos, sin acceso al repositorio. Declaró honestamente no poder ejecutar Python en su sesión. ChatGPT ejecutó, revisó y publicó su banco; no atribuir esas ejecuciones a Qwen.
- ChatGPT: revisión externa, comprobación reproducible y coordinación; propuestas de corrección en ramas propias. No fusionar ni adoptar decisiones humanas por inferencia.

## Estado publicado contrastado al preparar este archivo

### Claude · técnico

Rama `claude/hopeful-bardeen-qap6y0`, HEAD `957af652cdc3bef3d67e8623c9572138bac685e9`. Código final del bloque: `0a0020b9e213e1de77f9d384374fb1c054643b7d`.

Hito 2 declarado cerrado. Regresión registrada PASA: entradas 190/190, entrada efectiva 62/62, relevo 5/5, entre otras baterías. El cierre del autor no equivale a aceptación final externa del producto.

Pendientes declarados: regeneración y auditoría real de expedientes, revisión semántica de derivados U1, H9/I19 (el relevo vuelve siempre al paso 12 aunque un cambio anterior pueda requerir otro punto), U6(a) y límites del documento; control histórico 4.14 29/35, no presentado como superado. Aptitud vigente: experimental supervisada.

Referencia:
https://github.com/jluisplagos/munger-v2/blob/957af652cdc3bef3d67e8623c9572138bac685e9/munger_v2_r1/personaje_v2/empresas_v2_correcciones/2026-11_Vidrala_ensayo_4_15/hito2/HITO_2_4_15.md

### Claude · F1/Elis

Rama `auditoria/economica-f1-frente-e`, HEAD `b83803cd1c42c52c6ced6a538f5ae03ef706a644`: propuesta de decisiones F1 sin implementar. Revisión del verificador número 9 incorporada (`6d799c6`); U1–U6 pendientes de respuesta C20. Ninguna de esas observaciones afecta a las 752 filas reales según el revisor. Eso no revisa las recomendaciones económicas nuevas.

ChatGPT revisó la propuesta: manifiesto 349/349, contraste 292 comprobaciones y cero fallos, salidas idénticas. Fuentes consultadas en PDF con huellas. Se conservan C48=108, C49, FCF base=307,933 y decisiones E1/D3/E2/E6. R de Elis no está identificada: no elegir un punto entre 736,0 y 867,2 para liberar una valoración.

Último encargo que se dio al usuario para esta sesión: leer y ejecutar el prompt de revisión en rama `auditoria/revision-propuesta-f1`, commit `1a071881c65a191056ca3c6b41a20a965825cf12`:
https://github.com/jluisplagos/munger-v2/blob/1a071881c65a191056ca3c6b41a20a965825cf12/docs/validacion_economica_paralela/revision_propuesta_f1_20261116/PROMPT_PARA_CLAUDE.md

P1: inversión climática separada debe conservar su salida de caja y horizonte; no excluirla por etiqueta. P2: mapear gasto comercial ya en EBIT, R, adquisiciones de reposición y crecimiento sin omisiones/duplicados; aclarar PPA constante. P3: normalización con regla fiscal y efecto conjunto; diagnóstico 27,936 no es ajuste universal aprobado. P4: sincronizar bloqueos/avisos, media de arrendamientos como hipótesis (sensibilidad 16,8), umbral 0,5 % no adoptado y coherencia terminal/ROIC. Se ejecutaron nueve ilustraciones sintéticas, no estimaciones de costes de Elis. No se autoriza implementar políticas financieras en ese encargo.

Importante: el doble coste de arrendamientos está sustentado bajo sus premisas. El doble coste de PPA **no está demostrado** como hecho general. La matriz histórica 4.14 tiene una redacción más fuerte; usar el informe F1 posterior para esta distinción.

### Mistral · A cobertura

Rama `mistral/m2-cobertura-vm`, último HEAD contrastado `08c9799e0534e8968b5670060db612941f02ecf9`.

677 entradas: 347 Vidrala y 330 Viscofan; 60 reutilizadas del piloto y 617 nuevas; 101 derivados (14 piloto, 87 nuevos). Los recuentos y controles mecánicos pasan. Falta demostrar revisión contextual independiente de concepto, fila, columna, ejercicio, unidad y perímetro: el script copiaba metadatos y encontraba números, sin acreditar ese significado. No tratar las 568 coincidencias mecánicas como 568 datos económicamente acreditados.

Encargo correctivo ya entregado:
https://github.com/jluisplagos/munger-v2-evidencias-mistral/blob/9366bdd563a986cdd6907ba2187f796f96898db6/revision_externa/m2/CORRECCION_A.md

### Mistral · B P-M1

Rama `mistral/m2-fundamento-pm1`, último HEAD contrastado `b5a07e007785f0cd194cb6437fcb5cd7029cb79f`.

Errores materiales detectados: nueve años de altas de intangibles de Vidrala etiquetadas como PP&E (2025: 45.173 k€ intangibles frente a 177.848 k€ de PP&E). Conclusión de «aceptar desglose → θ acotado a cero» no justificada: θ negativo diagnostica incompatibilidad/identificación, no estima θ=0. Porcentajes de inversión publicada aplicados a caja+ROU requieren justificar el perímetro. P-M1 sigue pendiente; no adoptar θ/λ.

Encargo correctivo ya entregado:
https://github.com/jluisplagos/munger-v2-evidencias-mistral/blob/9366bdd563a986cdd6907ba2187f796f96898db6/revision_externa/m2/CORRECCION_B.md

Cuatro PDF nuevos descargados de fuentes oficiales: SHA/tamaño coinciden; subida de assets a Release auxiliar `fuentes-mistral-m2-20261116` falló con HTTP401 tanto en Mistral como en ChatGPT. El HTML oficial sí está en Git. No afirmar PDF preservados en esa Release ni pedir tokens al chat.

### Mistral · C matemática

Rama `mistral/m2-matematica-b`, HEAD corregido `ba46ea51a33a87dc8f2a03668b0e44dd79735d09`.

C1 aritmético resuelto: 57 casos, diez propiedades, residuo máximo producto/oráculo 2,842e-14; 192 sensibilidades y 24/24 correspondencias de cobertura reproducidas. D7 Caja 4.12→4.13 = +1,5386459068 €; activa NIIF16 = +1,5477811279 €, otra comparación válida. No hay discrepancia de 0,0092 €. La llamada interna p_estrella con entradas fuera de contrato no prueba fallo de la vía pública, que rechaza el caso ensayado.

C2 pendiente: guarda anti-perímetros era un texto OK escrito a mano; cambiar H6 de Caja a NIIF16 manteniendo H5 Caja sigue devolviendo OK. Corrección dirigida solicitada: comparar empresa/perímetro canónicos en los extremos reales y probar casos positivos/negativos; no reabrir toda la matemática ni adoptar D1/D7/D11.

Último encargo dado al usuario para esa sesión:
https://github.com/jluisplagos/munger-v2-evidencias-mistral/blob/604951346bea1a487206a76519c3bb22e724bece/revision_externa/m2/SEGUIMIENTO_C_ba46ea5.md

### Qwen · aceptación

Banco Q1 v2 recibido, revisado y ajustado por el integrador. Propuesta estructuralmente comprobada: 36 casos, seis familias, 12 positivos y 24 conflictos/carencias; 50 fixtures; 17 resultados con aritmética exacta; nueve controles negativos detectados. 31 casos contractuales, tres propuestas y dos políticas pendientes. Originales conservados. No otra ronda de Qwen necesaria para esa entrega.

**Ejecución contra el producto: 0/36.** Antes de probar, fijar candidata y adaptar precondiciones por vías soportadas, sin convertir los JSON sintéticos en auditorías auténticas. Pendiente de adaptación no es fallo del producto.

Rama `revision/qwen-q1-v2`, commit `4745f3887f7fd86bb3052f5d5e32285862df18e3`:
https://github.com/jluisplagos/munger-v2-evidencias-mistral/tree/4745f3887f7fd86bb3052f5d5e32285862df18e3/resultados_qwen/q1_v2

## Pendientes globales que no deben perderse

1. Cerrar las propuestas/correcciones de arriba sin ampliar indefinidamente las revisiones.
2. Adoptar explícitamente las políticas económicas que estén fundamentadas; la carencia de datos no se subsana con una firma humana. Implementar solo lo autorizado sobre candidata técnica fijada.
3. Regenerar expedientes nuevos con los registros finales y revisión independiente de fuentes/derivados, conservando históricos y retirando aprobaciones sustituidas.
4. Validar alcance por motor y casos representativos. Dos casos B no demuestran uso universal; el tercer contraste B fuera de muestra sigue sin completarse. Elis salió A y no sustituye un tercer B. Ahold de reserva carecía en la base de Excel/respuesta/fuentes suficientes. El motor C (bancos/aseguradoras) tiene pruebas sintéticas y carece de recorrido real: si sigue en el alcance original, falta validarlo.
5. Ejecutar aceptación del producto, pruebas de vigencia/cambios/recuperación y traspaso desde contexto limpio. Integrar resultados aceptados; que existan en ramas no significa que main los incorpore.
6. Entregar una versión con manual, límites por tipo de empresa y evidencia de qué conclusiones puede soportar. La gestión del tamaño de posiciones/cartera y el riesgo de mercado no se validan pasando baterías de software.

La matriz histórica de alcance y la guía de recorrido están en la base 4.14. Consultarlas junto con los cambios posteriores: no aplicar como vigentes límites ya corregidos de I20/I19. No afirmar que el conjunto ha terminado por cerrar uno de los frentes.

## Ejemplo de uso nuevo · L'Oréal

Ya figura entre las 116 empresas analizadas del usuario. Reutilizar, cuando estén disponibles, Excel evaluado y respuesta de etapa 1, extracción financiera anterior y PDF/fuentes. Verificar su procedencia/vigencia y completar entradas que el modelo realmente necesite. No afirmar que haber pasado por el personaje anterior acredita los datos.

Fijar entidad/acción/moneda, base de cuentas, fecha de precio y acciones. La fase A elige método por hechos; no asignar motor A o B a L'Oréal sin examinar su situación ni arrastrar parámetros de empresas piloto. Si el método cae fuera del alcance validado, se declara límite. Extracción y revisión documental, fases A/B/C, cálculo y variantes, auditoría y cierre son pasos separados. Presentar hipótesis y sensibilidad, no probabilidades inventadas o bandas como intervalos estadísticos.

La confianza para decisiones reales requiere evidencia para ese expediente, motor aplicable y económicamente validado, hipótesis defendibles y límites materiales tratados. Escenario malo no es pérdida máxima; k=3 no es garantía ni probabilidad empírica. Este proyecto aún no ha acreditado esas condiciones globalmente.

## Arranque de otra conversación

Leer este documento; consultar HEAD de las ramas relevantes; leer recuperaciones y las respuestas nuevas a los encargos. Informar qué cambió desde los commits aquí fijados. Continuar revisando lo afectado sin repetir comprobaciones ya conformes por cambios solo de redacción. Si no hay acceso a una fuente o herramienta, declararlo; no fingir ejecución ni recuperar datos desde memoria.
