# Encargos dirigidos · no enviados

## Claude F1/Elis · pegar en la sesión autora

Continúa en `auditoria/economica-f1-frente-e`. Consulta primero el HEAD remoto: base conocida d5188bb0396a429f86b7a896e7b8f17cf039e049. Lee íntegramente la revisión económica ya terminada en `auditoria/economica-f1-frente-e-revision`, commit 8fcc7fd792f065cf29e2dc915bda92faeff1d45a, archivo `docs/validacion_economica_paralela/frente_E_F1_elis/revision/REVISION_PROPUESTA_P1_P4.md`, y sus sondas/resultados. No encargues otra revisión general.

Responde V1–V11 en una sola corrección dirigida. V1: contrasta en las fuentes primarias la definición de crecimiento orgánico, umbrales de adquisiciones importantes y compras pequeñas; corrige fundamento y sensibilidad de (4b), sin inferir reposición cero ni adoptar la hipótesis. V2: evita que un coste cobrado como término explícito permanezca también en el ancla de S2C; añade ventana→ancla→proyección→terminal con crecimiento positivo y cero. Reproduce las contrapruebas del revisor, también con tus propias funciones. V3–V11: verifica earnout y regla fiscal, alcance 2021–22, arrendamientos (pagos y amortización ROU), fórmula/aviso terminal, términos explícitos y horizonte, cota de R_propia, controles y sincronización de textos/dependencias. No repitas lo ya conforme salvo impacto concreto.

Conserva C48=108, C49=128,1, FCF base=307,933 y E1/D3/E2/E6. Elis sigue pendiente_de_datos; no elijas R ni adoptes políticas o umbrales. No implementes cambios financieros en producto/libros. Actualiza el estado de revisión: ya existe informe, no sigue solo encargada. C20/U1–U6: registra si hay respuesta posterior y trata únicamente lo afectado en su frente; no lo confundas con revisión económica. Entrega respuesta numerada, diff, comandos y resultados realmente ejecutados, límites y commit congelado, con recuperación y manifiesto. Si falta un dato/política, conserva el bloqueo afectado y termina ese punto. Sin mensajes a terceros ni rondas recursivas.

## Mistral A · pegar en la sesión A

Continúa en `mistral/m2-cobertura-vm`; consulta HEAD remoto, base revisada 54c8ddc7bcbdf0dbb1029fdd08f85c41cfbd4367. Lee SEGUIMIENTO.md de esta carpeta, apartado A. No reabras las 677 entradas completas.

Corrección dirigida: las 509 REVISADO_CONTEXTUAL incluyen 423 fuentes y 86 derivados. Entre las fuentes, 70 tienen dimensiones pendientes, y las 423 marcan versión OK aunque su detalle dice no decidible desde una página. No presentes una entrada como plenamente revisada si falta una dimensión pertinente; distingue no aplicable de no comprobado. `check_unidad` acepta miles de euros/escala 0,001 ante una página que solo dice euros: elimina esa aceptación sin evidencia de escala. Versión/reexpresión necesita evidencia independiente de documento/notas/fecha, no copiar metadatos.

Conserva el universo, huellas, estados mecánicos, M1 y evidencia contextual válida. Relee solo entradas afectadas, con cabeceras/notas suficientes o segunda extracción cuando proceda; si no se resuelve, deja pendiente. Propaga límites/estados a derivados y mapa de regeneración. Incluye negativos de euros frente a miles, año/columna, perímetro, partida y versión/reexpresión; no uses solo la ausencia de conflictos como prueba. No fuerces recuentos ni cierres económicos. Entrega respuesta numerada, evidencia por dimensión, comandos/resultados, manifiesto, recuperación y commit. Escribe solo en tu carpeta auxiliar, sin fusionar, producto, libros oficiales ni políticas.

## Mistral B · pegar en la sesión B

Continúa en `mistral/m2-fundamento-pm1`; consulta HEAD remoto, base daa74783d2708fcd46ca7c24ae1ffbb327c35784. El seguimiento externo reproduce CALCULOS_PM1.json y acepta la retirada de θ=0 como identificación; no repitas la investigación ni intentes desbloquear P-M1.

Conserva la separación PP&E/intangibles, base publicada/hipótesis NIIF16 y el bloqueo económico. Facilita para revisión dirigida las ventanas de la nota PP&E, fila/columna/año y comparativos de las nueve altas corregidas, con huellas y controles negativos. Comprueba que combinaciones de negocio se describen según su columna de la tabla, sin confundirlas con subconjunto de Additions. Revisa solo las conclusiones dependientes. El revisor no ha vuelto a ejecutar el extractor ni abierto los PDF y por eso no declara cierre documental propio.

La Release fuentes-mistral-m2-20261116 continúa sin assets en la consulta externa. No reiteres intentos fallidos idénticos ni pidas tokens al chat; conserva URL oficial, huella, tamaño y estado provisional. No digas preservado hasta verificar assets. Entrega una respuesta finita con qué está acreditado y qué sigue pendiente; sin θ/λ adoptados, políticas ni fusión. Si la evidencia ya está íntegra y no hay cambio material que hacer, referencia lo existente sin fabricar una nueva corrección.

## Mistral C · texto de cierre del punto C2

La revisión externa sobre 1ec4f18f950aecdda10c0e48c946c71cedcd644e reprodujo las 37 filas, seis controles y el fallo exit 1 al mutar el extremo real H6 a NIIF16. C2 queda conforme dentro del auxiliar. No reabrir matemática ni lanzar otra revisión por este punto. C1 se conserva, D1/D7/D11 siguen pendientes y esto no implica integración ni guarda del producto. Entregar referencia del commit al integrador, sin nueva política ni fusión.

## Claude técnico/integrador · preparación de aceptación Qwen

Consulta HEAD remoto de `claude/hopeful-bardeen-qap6y0`; base conocida 957af652cdc3bef3d67e8623c9572138bac685e9. Usa ese commit como candidata técnica de prueba propuesta si no ha cambiado, registrando SHA exacto, entorno y dependencias; no lo presentes como versión final aceptada. Lee banco revisado y PLAN_DE_EJECUCION.md en `jluisplagos/munger-v2-evidencias-mistral`, rama revision/qwen-q1-v2, commit 4745f3887f7fd86bb3052f5d5e32285862df18e3, carpeta resultados_qwen/q1_v2/banco_revisado.

Los 36 casos todavía no se han ejecutado contra el producto. Adapta los fixtures y precondiciones por vías soportadas, sin cargar JSON sintéticos como auditorías o aprobaciones auténticas. Genera aprobaciones reales de prueba para vigencia/cambios/recuperación. Ejecuta los casos contractuales observables sin esperar decisiones financieras ajenas; conserva separadas tres propuestas y dos políticas pendientes. No adoptes políticas para convertirlos en PASA. Si un caso requiere relevo supervisado, registra prompts, estado, respuesta y artefacto completos; un test de script aislado no equivale a ese recorrido.

Por caso registra versión, adaptador/precondiciones, comando o interacción, observables en todos los artefactos relevantes, resultado esperado, resultado obtenido y evidencia. Usa los veredictos del plan; ADAPTACION_PENDIENTE no es fallo ni éxito, y NO_OBSERVABLE requiere instrumentación. Conserva positivos para detectar bloqueos excesivos. Q1-036 exige observar artefactos/aprobaciones vivas, no solo la palabra bloqueado. No inventes firmas, ejecución ni resultados. Entrega matriz 36 filas y recuentos que separen ejecutados, pendientes, propuestas/políticas; fija todo con commit y recuperación. No declares aptitud económica por pasar aceptación técnica. No fusionar sin revisión ni sustituir expedientes históricos.
