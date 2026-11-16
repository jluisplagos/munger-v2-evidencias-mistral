# Encargo dirigido · cierre de la revisión F1 V1–V11

Pegar en la sesión autora «Conciliación económica Elis/F1». Este texto está preparado, no enviado.

Continúa en `jluisplagos/munger-v2`, rama `auditoria/economica-f1-frente-e`. Consulta remoto y conserva trabajo posterior. Base revisada `716cbd6794b7fcde8b3862c9d1e7acdaf516d262` (código/documentos sustantivos de fd474d3).

Lee REVISION_F1_V3.md y SONDAS.json en esta carpeta de la rama externa. La revisión ha reproducido tus tres scripts, 374/374 huellas y cinco salidas idénticas, el recálculo separado y los pasajes de PDF. **No repitas toda la investigación ni encargues otra revisión general.** Conserva lo ya conforme de V1–V11.

Corrige solo W1–W3 y sus dependencias:

1. **W1, temporal más allá del año 10.** La resta de X11 al flujo de Gordon no especifica correctamente la terminación de un coste en H=11/12. La tabla de transición del año 11 tampoco casa con E3. Define una propuesta de tratamiento de la caja temporal pendiente separada de la base sostenible del terminal, con valor presente comprobable, o declara expresamente el caso no soportado y bloquea únicamente su conclusión hasta especificarlo. No inventes un horizonte de Elis, no pongas cero por defecto ni implementes una nueva política. Añade H=5/10/11/12: 1–11 correctos no bastan si el valor posterior es incorrecto. Conserva positivos existentes.
2. **W2, terminal.** Haz coincidir el signo y rótulo de «salto del libro» con fila 178 = rentabilidad marginal − ROIC. El aviso usa magnitud/valor absoluto y C179 vigente; no cambies el umbral. Reconcílialo con G8 (`requiere_justificacion=True` por encima del umbral): no elimines una obligación técnica existente al decir que no creas una nueva. Si propones cambiarla, déjala como decisión separada. Prueba ambas direcciones y la frontera del umbral.
3. **W3, A0.** E2/(1a) solo admiten ambos ceros; V-F1a requiere ambos positivos. Especifica los cuatro casos y sus estados coherentes. No sustituyas AND por OR sin interpretar ni declares doble cargo demostrado donde la evidencia no lo demuestra. Una combinación fuera del dominio no puede admitirse solo porque V-F1a no salta; puede requerir aclaración, conflicto o límite de aplicabilidad.

Esta corrección es de propuesta/especificación y herramientas de investigación: no adopta (1a)–(5b), no implementa en el producto ni cambia libros/decisiones. Conserva C48=108, C49=128,1, FCF base=307,933 y E1/D3/E2/E6. Elis continúa pendiente_de_datos.

Entrega respuesta numerada W1–W3, evidencia, cambios de documentos/salidas afectados, comandos/códigos reales, manifiesto y recuperación. Commit/push por bloque sustantivo, SHA congelado final. No te autoapruebes ni encargues otra ronda automática: se contrastará externamente solo lo afectado. No esperes otra confirmación para comenzar las correcciones independientes de datos o políticas.
