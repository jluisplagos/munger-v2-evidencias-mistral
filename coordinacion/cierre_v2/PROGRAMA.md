# Programa y prioridades

## Objetivo y criterios comunes

Entregar una herramienta reproducible y con límites verificables para apoyar análisis; toda conclusión para un uso concreto exige fuentes/derivados acreditados, motor económicamente defendible, hipótesis justificadas y revisión vigente. No se promete ausencia de errores o pérdidas. No basta pasar tests de software.

Se conservan las decisiones E1/D3/E2/E6, C48=108, C49=128,1 y FCF base=307,933. Ningún agente elige R, θ, λ, probabilidades, k, ventanas fiscales o umbrales para desbloquear un caso. No volver a pedir decisiones ya registradas. Una firma o política no subsana un dato ausente. El doble coste de arrendamientos está fundamentado bajo sus premisas; el doble coste de PPA no está demostrado como hecho general: prevalece el informe F1 posterior sobre frases históricas más fuertes.

## Prioridad 0 · arranque y control (Claude)

1. Leer continuidad fijada 8d82c8f, revisión F1 f5775dc y A/D d375d80, este paquete y recuperaciones actuales. Consultar HEAD remotos y cambios posteriores; fijar cada revisión en un SHA. No atribuir a los autores trabajo todavía no publicado.
2. Mantener un worktree por frente. La sesión Claude F1 pasa a coordinadora general; conserva su rama F1 y prepara una **candidata técnica nueva** en `integracion/candidata-cierre-v2` desde 957af65. La rama técnica original se consulta como fuente. No interrumpir otro trabajo activo ni sobrescribir cambios; si hay otro autor, usar una rama propia y registrar procedencia.
3. Verificar entorno por comandos: acceso a binarios, Python/bibliotecas, pdftotext, soffice y capacidad de agentes reales configurados. No inferir capacidades por el nombre del modelo. Materializar/verificar los insumos por el procedimiento del producto antes de pipeline; distinguir base histórica completa de selección parcial y del código 4.15 modificado. No sobrescribir la candidata con la base 4.14.
4. Publicar el primer checkpoint del control común, con lo disponible y lo bloqueado. No esperar a terminar todos los frentes.

## Prioridad 1 · frentes que pueden avanzar en paralelo

| ID | Dueño | Trabajo | Condición de salida |
|---|---|---|---|
| F1-W | Claude autor; Mistral C/F revisor distinto | W1–W3: horizonte temporal, salto/G8, A0/guarda | Cambios y pruebas dirigidos, sin volver a auditar todo F1; revisión registrada |
| C20 | Claude autor; revisor distinto | U1–U6 del verificador | Respuesta y pruebas afectadas con límites explícitos |
| CSV | Claude autor; revisor distinto | Cifras [LECTURA] al procedimiento CSV, después de estabilizar verificador | Fuente/edición/fila/columna/unidad/perímetro y huellas acreditadas; salidas regeneradas; no adopta N1 |
| A-CTX | Mistral A; Claude revisor | Revisar respuesta d2419e5 y cerrar acreditación de las fuentes/derivados alcanzados | Estados reproducibles, evidencia contextual defendible y pendientes honestos |
| D-QWEN | Mistral D; Claude revisor | Revisar bdcbba7, cerrar arnés, evidencias y paquetes pendientes | Criterios y precondiciones observables; cero CUMPLE completos sin cubrir todo el caso |
| E-ELIS | Antigua sesión B, nueva etapa E; Claude revisor | Fuentes oficiales nuevas para M1/M2/M6/N2 | Cada pregunta con hallazgo o búsqueda delimitada, sin estimar R por conveniencia |
| F-REAL | Antigua sesión C, nueva etapa F; Claude revisor | Contrastes independientes y preparación de tercer B/primer C real | Protocolo previo al resultado, recursos y entradas revisables o bloqueos precisos |

No confundir B/P-M1 con E/Elis. El dossier B anterior se preserva. C2 matemática permanece conforme en su alcance; no necesita otra ronda por este programa.

## Prioridad 2 · cola de Claude cuando un frente espere

El coordinador elige la **primera tarjeta ejecutable**. No se queda esperando una decisión económica para hacer trabajo independiente:

1. Revisar nuevas entregas A/D por sus diffs y reproducciones; no dar por corregido algo porque lo diga el resumen. Señales concretas iniciales: en A, no confundir importes 20xx con metadatos de año; en D, verificar integridad del relevo Q1-026, resultado Q1-027 y cobertura compartida por criterio.
2. Completar W1–W3 y C20; publicar candidatos de revisión. Si aún no hay resultado de otro revisor, continuar con la siguiente tarjeta, no autoaprobar.
3. Preparar e importar a la candidata evidencia/documentación aceptada, sin aplicar políticas financieras no adoptadas. Preparar cambios técnicos reversibles con pruebas; separar propuesta de comportamiento vigente.
4. Regenerar **expedientes nuevos de prueba** con la evidencia aceptada y las decisiones vigentes. Conservar históricos, retirar aprobaciones sustituidas mediante vías soportadas y revisar el significado de cada derivado material. Si no se puede cerrar una conclusión, el expediente debe decirlo.
5. Preparar/ejecutar la parte accesible de Qwen y los relevos reales: no simular agentes ni firmas. LibreOffice en secuencia cuando comparte máquina/perfil. Cada auditoría exige actor/contexto distinto de quien produjo el material; fase C conserva sus dos turnos con el mismo agente.
6. Revisar paquetes E/F, comprobar fuentes y completar datos que sí estén publicados. No escoger un parámetro cuando solo se dispone de una categoría contable o rango sin identificar.
7. Preparar manual actual, instalación/recuperación y traspaso limpio. Leer la guía histórica junto con Hito2; no reintroducir límites I19/I20 ya corregidos. H9/I19 (volver siempre a paso12) sigue pendiente de verificar por cambio afectado.
8. Preparar el expediente de decisiones para el usuario, con alternativas concretas, fundamento y consecuencias. No preguntar por un paquete de nueve aprobaciones sin revisar ni inventar un dato para reducir la lista.

Si hay fallo de entorno: conservar error exacto, probar una alternativa soportada y trasladar al runtime adecuado. No reiterar el mismo acceso fallido ni pedir tokens en el chat. Puede transferirse un paquete de prueba a Claude sin cambiar quién lo escribió ni qué se ejecutó.

## Prioridad 3 · integración, aceptación y alcance

La candidata se integra por entregas aceptadas, con origen/destino/evidencia, según INTEGRACION.md. Los cambios económicos de motor solo se implementan tras decisión explícita; se puede preparar un parche propuesto sin activarlo. No fusionar main ni publicar la versión final por inferencia.

La aceptación cubre los 36 Qwen por criterio, pruebas de vigencia/cambio/recuperación/traspaso y expedientes reales regenerados. Un cambio invalida solo pruebas materialmente afectadas; el integrador debe justificar esa dependencia, no repetir toda la batería por redacción ni conservar resultados caducados.

Mantener el alcance original a la vista: tercer B real fuera de muestra, motor C real si sigue incluido, motor A con validación económica propia. Elis es A y no sustituye un tercero B. Ahold de reserva no tenía insumos suficientes; no forzar la elección. Preparar los casos puede avanzar ahora; ejecutarlos exige candidata, contrato aplicable y precondiciones verdaderas. No declarar universalidad tras dos casos ni capacidad predictiva tras fixtures.

## Criterios de cierre

1. Versión fijada con cambios trazables y sin defectos materiales abiertos para el uso declarado.
2. Evidencia y decisiones vigentes; registros nuevos y revisión semántica de derivados, sin aprobaciones falsas/heredadas de otro material.
3. Pruebas técnicas y aceptación del recorrido real, distinguiendo completas/parciales/no observables/políticas.
4. Alcance por motor y casos representativos, con lo pendiente explícito. No se considera completado el alcance original si un componente obligatorio sigue sin validar; cualquier reducción requiere decisión explícita del usuario.
5. Manual/recuperación/traspaso comprobados y paquete de entrega revisable. La declaración de aptitud tiene alcance concreto; experimental supervisado no equivale a apto para dinero real.

El control informa posición por estos criterios, no un porcentaje agregado. No se garantiza fecha. Las fuentes faltantes pueden requerir información que ninguna cantidad de horas de agentes produzca.
