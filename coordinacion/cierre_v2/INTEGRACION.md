# Contrato común de trabajo e integración

## Autoridad y propiedad

Este paquete es el nuevo encargo de programa. Amplía de forma explícita B/C a E/F y permite pruebas locales del producto en copias aisladas; no reinterpreta el encargo M1 como autorización económica. Sus reglas prevalecen sobre alcances antiguos incompatibles para estos trabajos nuevos. No modifica las decisiones financieras registradas ni autoriza cambiar credenciales, facturación o límites de gasto.

- **Claude coordinador**: único escritor del control común y único integrador del producto. Rama auxiliar `coordinacion/cierre-v2`; F1 en su rama; candidata en `integracion/candidata-cierre-v2`. No fusiona a main ni publica producción en este programa.
- **Mistral A**: `mistral/m2-cobertura-vm`, `resultados_m2/cobertura_vm/`.
- **Mistral D**: `mistral/d-qwen-aceptacion`, `resultados_qwen/ejecucion_d/`.
- **Antigua B, nueva E**: `mistral/e-fuentes-elis`, `resultados_cierre/elis_fuentes/`.
- **Antigua C, nueva F**: `mistral/f-alcance-real`, `resultados_cierre/alcance_real/`. Sus revisiones independientes de Claude van en subcarpeta `revisiones_claude/`, sin tocar archivos del autor.

E/F nacen desde el commit de este paquete, o una base del auxiliar registrada que lo contenga. A/D lo leen con `git show` sin fusionar toda la rama de coordinación. Cada autor conserva los cambios locales y trabaja solo en su carpeta; no fuerza pushes. Ningún Mistral escribe en el repositorio producto.

## Entrega estándar

Cada bloque sustantivo publica: ENTREGA.json (modelo en PLANTILLA_ENTREGA.json), resultados/evidencia acotada, scripts, MANIFIESTO_SHA256.txt y PUNTO_DE_RECUPERACION.md con siguiente acción exacta. Commit/push al cerrar bloque; un commit de autor no puede incluir su propio SHA en su contenido, por eso el coordinador toma el SHA remoto y lo fija en el control. Se excluyen cachés/secretos; PDF/XLSX/ZIP no van al Git del auxiliar. Conservar URL+SHA no equivale a haber preservado bytes de forma duradera.

Si un asset no puede conservarse en Release por error de autorización, registrar provisional, URLs oficiales, hashes, tamaños y descarga reproducible. No reiterar uploads fallidos ni pedir tokens; aprovechar fuentes ya preservadas. Si hay otra conservación autorizada, verificarla antes de afirmar preservación.

## Recepción y revisión

1. Leer HEAD y ENTREGA del autor; fijar SHA, comprobar manifiesto y procedencia. Un resumen no sustituye los resultados.
2. Leer diff respecto de la versión revisada. Identificar dependencias afectadas. Pruebas de fallo relevante y positivos necesarios, sin reabrir todo lo conforme.
3. Reproducir comandos/salidas y revisar el significado de las fuentes y derivaciones cuando corresponda. No aceptar sello programático como revisión independiente, ni una mera coincidencia numérica como concepto/ejercicio acreditado.
4. Registrar autor y revisor/contexto reales. La misma sesión no revisa independientemente su cambio. Claude revisa a Mistral; un revisor distinto revisa cambios de Claude (Mistral C/F puede producir contraste independiente, sujeto a reproducibilidad y a los requisitos del producto). No afirmar independencia total solo por cambiar el nombre de un actor. Cada solicitud se registra en CONTROL.json con SHA autor, base, diff/rutas, criterios y revisor asignado; el informe del revisor cita esa solicitud y su SHA. No inferir encargos de conversaciones privadas ni duplicar una revisión asignada a otro.
5. Clasificar: conforme para alcance concreto, conforme con límites, correcciones materiales o no verificable. No bloquear partes independientes por una carencia ajena. Una revisión limitada no acredita aptitud económica global.

## Incorporación controlada

Nunca fusionar indiscriminadamente ramas completas auxiliares en el producto. Importar los archivos/propuestas aceptados al lugar que corresponda, con lista de archivos, huellas, SHA origen, referencia de revisión y SHA destino. Si no procede incorporar un artefacto, conservar enlace y decisión de uso. Describir si es documentación, dato, prueba o cambio de software.

Los datos pendientes quedan pendientes en los registros finales. Los cambios económicos no adoptados permanecen como propuestas/parches separados sin activar. No elegir políticas para hacer pasar pruebas ni para clasificar un caso de aceptación como éxito.

Verificar la candidata real, no solo una constante escrita en un log. Materialización de base, código 4.15 y binarios deben corresponder al conjunto fijado. Al integrar cambios, regenerar lo dependiente y volver a auditar el material nuevo; no reactivar aprobación vieja.

## Validación y límites

Pruebas: fecha, SHA código/banco/configuración, datos de entrada/huellas, comando, código de salida, esperado, observado, artefactos y criterio. Positivos y negativos. Distinguir resultado esperado de un rechazo y un error de entorno. Un archivo existente puede ser antiguo; comprobar procedencia de esta ejecución.

El runtime del personaje debe ejecutar sus fases y modelos configurados o una sustitución explícitamente declarada como experimento. Mistral respondiendo por sí mismo no equivale a haber ejecutado el producto. Las precondiciones simuladas sirven para pruebas de componente y se rotulan; no sustituyen revisión/auditoría real exigida. LibreOffice en una máquina compartida exige exclusión mutua verificable (lock con `flock` o mecanismo equivalente) y perfiles de prueba aislados; si no existe esa garantía, un único proceso propietario del recálculo y ninguna ejecución concurrente. No basta escribir «en secuencia» mientras se lanzan trabajos en paralelo.

Consultas entre sesiones se hacen leyendo commits al terminar bloques; no asumir mensajes privados compartidos ni mantener bucles infinitos de espera. El programa no autoriza mensajes a empresas o personas fuera de estas sesiones.

## Control y checkpoint

Solo el coordinador actualiza CONTROL.json y genera ESTADO.md. Cada fila mantiene por separado entrega/revisión/integración/pruebas, commit y próximo dueño. Registrar cada decisión de aceptación o devolución. No usar marcas del plan de la interfaz como prueba.

Checkpoint al terminar un bloque, cambiar de candidata, encontrar bloqueo o antes de agotar contexto: qué se hizo y evidencia; qué no; commits local/remoto; cambios sin publicar; siguiente comando exacto; bloqueos materiales; tarea independiente siguiente. Ninguna sesión promete seguir ejecutándose si su proveedor la pausa. El usuario debe poder reanudar con «continúa desde tu recuperación» sin reconstruir la conversación.
