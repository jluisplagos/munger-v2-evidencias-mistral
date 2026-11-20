# Respuesta del autor · ronda 1 de la revisión crítica de la hoja resumen (`hoja_resumen.py`)

- **Revisión respondida:** `/home/user/e_work/revision_hoja/REVISION_HOJA.md` (Fable, veredicto CORRECCIONES), sobre `ef93699`.
- **Autor de las correcciones:** Claude (Opus 5.5), el mismo autor de `ef93699`. No me he revisado a mí mismo: la segunda ronda la hace
  otro agente.
- **Rama:** `examen/hoja-resumen` (worktree `/home/user/e_work/wt_hoja`). Commit final: `6406a99` (sobre `ef93699`), publicado en `origin/examen/hoja-resumen`. No se ha fusionado en main.
- **Archivos cambiados:** `personaje_v2/scripts/hoja_resumen.py` (reescrito, versión 2.0), `personaje_v2/pruebas/test_hoja_resumen.py`
  (batería nueva), `personaje_v2/scripts/README_hoja_resumen.md`, `personaje_v2/scripts/cierre_v2.py` (archivo de la hoja al retirar
  una aprobación), `personaje_v2/scripts/pipeline.py` (archivo de la hoja y de `fin` al relanzar), `verificar_paquete.sh` (registro de
  la batería) y `MANIFIESTO_SHA256.txt`. Ninguna fuente, huella de expediente, ficha, auditoría ni aprobación se ha tocado.
- **Decisiones del coordinador aplicadas:** al relanzar el pipeline se invalida la hoja anterior; al retirar una aprobación la hoja se
  archiva como no vigente; nunca se reactiva una aprobación retirada. El «resumen llano escrito por el personaje» no se hace (fuera de
  alcance).

## Resultados de las pruebas

Salidas completas en `/home/user/e_work/revision_hoja/respuesta_ronda1/`.

| Prueba | Código | Resultado |
|---|---|---|
| `pruebas/test_hoja_resumen.py` (batería nueva) con `6406a99` | 0 | **85/85 PASAN** (2 min 20 s con el cerrojo tomado; `bateria_hoja_resumen_6406a99.txt`) |
| La misma batería contra el código de `ef93699` (cambios apartados con `git stash` y restaurados después) | 1 | **25/85; fallan 60** (`bateria_nueva_contra_ef93699.txt`) |
| `pruebas/test_cierre_v2.py` (toca `archivar_salidas`) | 0 | 55/55 PASAN |
| `pruebas/test_vigencia_h5.py` | 0 | 59/59 PASAN |
| `pruebas/test_estados_v2.py` | 0 | 28/28 PASAN |
| `v6/v631_f1/scripts/prueba_pipeline_v631.py` (toca `--desde`) | 0 | 9/9 PASAN |
| `bash verificar_paquete.sh` (rápida) sobre una extracción limpia de `6406a99` (`git archive` + los 1.059 archivos fuera de Git copiados con su huella del manifiesto) | 0 | **RESULTADO GLOBAL: PASA** (manifiesto 8.052 archivos, 0 modificados, 0 ausentes, 0 de más; entorno, piloto 35/35, comprobadores 114/114) |

Contra `ef93699` fallan todos los casos nuevos de los hallazgos ALTA y MEDIA (por hallazgo: H1 11, H2 11, H3 6, H4 5, H5 6, H6 4, H7 5, H8 1,
H9 1; y de los BAJA: H10 1, H11 1, H12 4, H13 1). El único caso con etiqueta de hallazgo que pasa con `ef93699` es «H2 · si la ficha
cambia, --comprobar dice que la hoja ya no vale», que ya cubría la versión revisada y se conserva como regresión. Los 24 casos sin
etiqueta que también pasan con `ef93699` son de regresión (limpieza de frases, cifras de la tabla, recálculo independiente al 10 %,
predicciones, originales intactos…).

La batería completa del paquete (`verificar_paquete.sh completa`, ≈ 80 min) no la he repetido: he ejecutado los bloques que tocan
los cambios (arriba) y la rápida. `verificar_paquete.sh completa` exige ahora la batería de la hoja con al menos 85 pruebas.

**Sobre el cerrojo:** durante el trabajo, otra sesión tuvo el cerrojo común 77 min (`verificar_paquete.sh completa`); todas mis
ejecuciones con LibreOffice fueron en secuencia, bajo `flock` del cerrojo común (o, en la ejecución contra `ef93699`, con el cerrojo que
el propio programa toma en cada recálculo).

## Hallazgo por hallazgo

Formato: qué cambié (archivo · función) → prueba que lo cubre (texto del caso en `test_hoja_resumen.py`) → resultado.

### 1 · ALTA · Sin conclusión oficial, «precio de Sí» en el veredicto y la causa callada

- **Cambio** (`hoja_resumen.py` · `veredicto`, `componer`): el veredicto sale solo de la ficha. Frase fija por estado (§4.2 de la
  revisión). Sin `concluido` (o con `motor_a_f1` no utilizable): «**Sin conclusión: falta un dato.**», «**Sin conclusión de compra:**
  una hipótesis no se puede acotar…» u otro estado en llano, más «Motivo, según la ficha» (`causa_si_no_concluido.detalle`) y «Qué lo
  resolvería» (`que_lo_resolveria`), limpios de referencias. «A qué precio compraría» = `decision.precio_objetivo` /
  `objetivo.precio_objetivo_emitido`; si es nulo (o el objetivo está bloqueado, o no hay conclusión): «**la ficha no da precio de
  compra.**» y, si hay cifra en la hoja de cálculo, por qué no lo es («la ficha dice que el objetivo está bloqueado», «la ficha dice
  que esa cifra no es utilizable para una conclusión»). Objetivo condicionado: «Es un precio provisional: el objetivo está
  condicionado». «Salvedades de la ficha»: `decision.condicion`, `objetivo`, `insumos_decision_cartera.fundamento`, marca de etapa 1 y
  `alcance.aviso`. Sin conclusión, la tabla es «una lectura de la hoja de cálculo, no una conclusión» y su columna «Precio de Sí de la
  hoja de cálculo (no es un precio de compra)». Desaparecen «firme» y «oficial» de la comprobación.
- **Pruebas:** «H1 · pendiente_de_investigacion con el precio por debajo del precio de Sí…», «H1 · «No · descartar» con zona
  favorable…», «H1 · objetivo bloqueado…», «H1/H3 · ficha concluido con motor_a_f1 no utilizable…» (sin LibreOffice); «H1 · V6.3:
  «Qué concluye: No comprar ahora…»», «H1 · objetivo condicionado…», «H1 · Vidrala 4.14: se copian el fundamento y el alcance…»,
  «H1 · sin conclusión: «Sin conclusión: falta un dato»…» (Elis), «H1 · Elis: el 7,30 € … no aparece como precio de compra…»,
  «H1 · Elis: la tabla se presenta como «lectura de la hoja de cálculo…»», «H1 · objetivo bloqueado: sin conclusión…» (Vidrala 4.13
  bloqueo).
- **Resultado:** corregido; 11 casos, todos pasan con `6406a99` y fallan con `ef93699`.

### 2 · ALTA · La hoja se genera con material que el sistema oficial no da por vigente

- **Cambio** (`hoja_resumen.py` · `vigencia_oficial`, `leer_expediente`, `comprobar`): puerta única = `cierre_v2.motivo_vigencia`
  (la del cierre oficial: auditoría y material, aprobación retirada, F1 con `motivo_f1`) + `cierre_vigente.json` presente +
  `ficha.cierre.auditoria = APROBADO` + F1 (`motor_a_f1.vigencia`) vigente y utilizable salvo en `pendiente_de_datos` (que ya es «sin
  conclusión») + las comprobaciones anteriores (`fin`, estado, libro, ficha e informe del cierre). Si no: código 3, sin hoja.
  `--antecedente` permite generarla rotulada arriba «NO VIGENTE · ANTECEDENTE» (y `--comprobar` nunca la da por vigente).
  `--comprobar` repite la puerta completa además de las huellas y aconseja **retirar** la hoja. Las frases siguen saliendo de
  `fase_c.json`, pero ahora la puerta garantiza que es el material auditado (si cambia: código 3, no un aviso al pie). Cabecera:
  «Deja de valer si el análisis oficial cambia» y, al pie, «Vale solo mientras la ficha {huella} siga siendo la oficial y vigente.
  Compruébalo con --comprobar» (ya no dice «se regenera»).
- **Decisiones del coordinador:** `cierre_v2.py` · nueva `archivar_hoja_resumen` y su llamada en `archivar_salidas`: al retirar una
  aprobación (por cualquier vía) la hoja se mueve a `historial_cierres/NN_…/hoja_resumen.NO_VIGENTE.*` con
  `HOJA_RESUMEN_NO_VIGENTE.json` y queda anotada en `RETIRADA.json` (`hoja_resumen_no_vigente`). `pipeline.py` · `main`: al relanzar
  (`--desde N` o `--reiniciar`) la hoja se archiva en `historial_hojas_resumen/NN_relanzamiento_…/` y, con `--desde`, `fin` pasa a
  `fin_anterior`. Nada reactiva una aprobación retirada: restaurar archivos sigue dando código 3.
- **Pruebas:** «H2 · si la ficha cambia, --comprobar…», «H2/H4 · con una ficha que no es la del cierre…», «H2 · fase_c.json cambiado
  después de la auditoría…» (A1/A6), «H2 · retirada oficial de la aprobación (asegurar_vigencia): la hoja se archiva…», «H2 ·
  restaurar fase_c.json no reactiva la aprobación retirada…», «H2 · A4: sin cierre_vigente.json…», «H2/H5 · fase_c.json = {}…»,
  «H2 · Hermès (no vigente para la vía oficial)…», «H2 · --antecedente…», «H2 · F1 cambiada después del cierre: --comprobar…», «H2 ·
  decisión del coordinador: al relanzar el pipeline (--desde 12)…», «H2 · P10: con F1 bloqueando tras el relanzamiento no hay hoja».
  La V6.3.1 F1 se prueba con una empresa sintética cerrada por el pipeline real con los agentes simulados (como P6/P10 del revisor).
- **Resultado:** corregido; 11 casos fallan con `ef93699` (y el de regresión «si la ficha cambia» pasa en las dos). Con el expediente F1 sintético: la hoja anterior se archiva al relanzar con `--desde 12`, `fin` pasa a `fin_anterior` y con F1 bloqueando no hay hoja (código 3).

### 3 · ALTA · Aptitud: calla «apto por entradas: no» y F1; frase falsa; podía proclamar «apto para dinero real»

- **Cambio** (`hoja_resumen.py` · `aptitud`): texto fijo «**¿Sirve para decidir con dinero real?** No. **Experimental: no vale para
  decidir con dinero real.**» y debajo, si existen: «Datos de entrada verificados contra sus fuentes: sí/no ({n} de {universo}…;
  motivo)» (`verificacion_entradas` o `aptitud_de_uso.verificacion_entradas`), «Motor A · F1: {rótulo}; bloquean …» (`motor_a_f1`),
  «Motor A · F1 hoy: no vigente o no utilizable» (`motor_a_f1.vigencia` actual) y la evaluación de la entrega (`aptitud_de_uso`).
  Sin bloques: «La ficha no dice nada sobre la aptitud; no se presume ninguna.» Se quitan «es anterior a ese bloque» y la rama
  «la ficha declara apto para dinero real»: una marca `apto_para_dinero_real = true` no se repite («haría falta una decisión humana
  registrada fuera de esta hoja»).
- **Pruebas:** «H3 · aptitud: dice «no vale…», «datos de entrada verificados: no» y F1; nunca afirma «apto para dinero real»» (ficha
  con `apto_para_dinero_real = true`, el caso A3), «H3 · sin ningún bloque de aptitud…», «H3 · V6.3 sin bloques de aptitud…», «H3 ·
  V6.4 con aptitud_de_uso…», «H3 · V6.3.1 F1: la hoja dice «Datos de entrada verificados contra sus fuentes: no»… y «Motor A · F1»».
- **Resultado:** corregido; 6 casos pasan con `6406a99` y fallan con `ef93699`.

### 4 · ALTA · La hoja se escribía aunque fallara su propia verificación

- **Cambio** (`hoja_resumen.py` · `generar`, `apartar_hoja`, `comprobar`): todo se compone y se verifica antes de escribir; con
  cualquier código ≠ 0 (3, 4, 5, 6) no se escribe nada y la hoja anterior se aparta como `hoja_resumen.NO_VIGENTE.md/.json`.
  `--comprobar` falla si el `.json` no registra `reproduce_oficial = true` o si la hoja es un antecedente.
- **Pruebas:** «H4 · código 5 (no reproduce el precio de Sí): no queda hoja_resumen.md y la anterior se aparta…», «H4 · después de un
  código 5, --comprobar no encuentra hoja vigente», «H4 · código 4 (frase sin origen): no se escribe hoja», «H4 · --comprobar falla
  (código 4) si la hoja registra que no reproducía…», «H2/H4 · con una ficha que no es la del cierre…». Los códigos 4 y 5 se provocan
  en el proceso de la batería sustituyendo la sensibilidad (no hace falta LibreOffice para eso). El caso A2 del revisor (`precio.json`
  alterado) hoy lo para antes la puerta (material cambiado: código 3).
- **Resultado:** corregido; 5 casos pasan con `6406a99` y fallan con `ef93699`.

### 5 · MEDIA · Selección mecánica de frases

- **Cambio** (`hoja_resumen.py` · `seleccionar_por_que`, `contenido_minimo`, `componer`): la tesis va **entera** (párrafo) y la tesis
  inversa **entera** (lista); no hay selección, así que no se omite ninguna frase (no hace falta el «se omiten N de M»). Contenido
  mínimo o código 4 sin hoja: tesis y tesis inversa con al menos 6 palabras, «a No» con texto real (salvo cubo No) y tres predicciones
  con texto, fecha y probabilidad.
- **Pruebas:** «H5 · la tesis y la tesis inversa se muestran ENTERAS…», «H5 · contenido mínimo: «a No» con «…», tesis vacía…»,
  «H5 · V6.3: la tesis y la tesis inversa están enteras…», «H5 · contenido mínimo incumplido: código 4 y no se escribe hoja».
- **Resultado:** corregido en lo que toca al programa; 6 casos (uno es real: los textos del expediente sintético V6.3.1 F1 —tesis inversa y «a No» casi vacíos— ya no dan hoja: código 4).
- **No hecho:** el resumen llano escrito por el personaje en la fase C (decisión del coordinador: fuera de alcance).

### 6 · MEDIA · No es lenguaje llano

- **Cambio** (`hoja_resumen.py` · `componer`, `GLOSARIO`, `glosario`, `ZONA_LLANA`, `ROTULO_FALSO`): la redacción del §4 de la
  revisión: cabecera nueva, «Qué concluye el análisis» en tres líneas, rótulos «Lo descartaría si…», «Lo compraría si…», «Lo dejaría
  por demasiado difícil si…», «Bajaría/Subiría el precio de Sí si…», título y texto fijo de la tasa, cabeceras y zonas de la tabla en
  llano, glosario fijo con los términos que aparecen. Las referencias técnicas (Análisis!C56, fase_c.json, huellas, origen de las
  frases) pasan al pie («Para comprobar esta hoja»). La limpieza quita también «(Historia filas 29 y 33)».
- **Pruebas:** «H6 · limpiar: «(Historia filas 29 y 33)»…», «H6 · cabecera llana…», «H6 · rótulos llanos…», «H6 · glosario con los
  términos de la página…».
- **Resultado:** corregido en los textos fijos y los rótulos; 4 casos pasan con `6406a99` y fallan con `ef93699`. Queda el límite de la longitud (abajo).
- **Límite, no corregido:** la hoja **no es más corta** (unas 2.000 palabras frente a 1.000–1.300): la tesis inversa entera (hallazgo
  5) pesa más que la brevedad, y el texto del personaje conserva su jerga, sus referencias que no están entre paréntesis
  («Historia C58») y su formato de cifras («757.05 €»). Solo un resumen llano escrito por el personaje lo resolvería (fuera de
  alcance). Queda escrito en el README.

### 7 · MEDIA · Faltan los avisos oficiales de la escalera y de la tasa

- **Cambio** (`hoja_resumen.py` · `sensibilidad`, `componer`): cada fila guarda `r_operativa_C15`, `r_minima_C17` y `r_vs_minima_C18`;
  la columna «Aviso de la hoja de cálculo» dice «la tasa queda por debajo de la mínima de la hoja (9,5 %)» y, en el motor B,
  «descuenta al 6,5 %». Notas fijas: el aviso A2 de la ficha («queda por debajo de su tasa mínima de referencia»), «no es la
  conclusión: no mide el riesgo ni el fundamento», «el escenario malo no es un suelo de valor ni la pérdida máxima posible», «regla
  experimental (k = 3)», que la tasa con que descuenta el motor B se ajusta y que lo demás (también el ROIC fijado mirando la tasa) se
  deja quieto.
- **Pruebas:** «H7 · avisos junto a la tabla…», «H7 · motor B: la tabla dice con qué tasa descuenta…», «H7 · Vidrala 4.14 al 8 %…»,
  «H7 · aviso A2…» y «H7 · la fila del 7 % lleva el aviso…» (Viscofan 4.14).
- **Resultado:** corregido; 5 casos (Vidrala 4.10.1, Vidrala 4.14 y Viscofan 4.14).

### 8 · MEDIA · «Precio actual» no es el precio de hoy

- **Cambio** (`hoja_resumen.py` · `componer`, `fecha_precio`): «Precio usado en el análisis: 90,10 € (31 de diciembre de 2025)» en la
  conclusión y en la cabecera de la tabla («El precio del análisis (90,10 €) queda…»); «No es el precio de hoy» y, si es de más de 90
  días antes del análisis, «**Ojo:** es un precio de N días antes del análisis»; «Hecho el …» en la cabecera y en las fechas.
- **Pruebas:** «H8 · «Precio usado en el análisis: 90,10 € (31 de diciembre de 2025)»…», «H6 · cabecera llana… y la fecha de la hoja».
- **Resultado:** corregido; 1 caso propio y la fecha de la hoja en el caso de la cabecera.

### 9 · MEDIA · La página no estaba protegida por huella

- **Cambio** (`hoja_resumen.py` · `componer`, `comprobar`, `verificar_origen`): `hoja_resumen.json → md_sha256`; `--comprobar` y
  `--verificar-origen` lo comprueban.
- **Prueba:** «H9 · una edición a mano de hoja_resumen.md se detecta (--comprobar y --verificar-origen, código 4)».
- **Resultado:** corregido; 1 caso.

### 10 · BAJA · Recálculo que no recalculase

- **Cambio** (`hoja_resumen.py` · `comprobar_recalculo`): el precio de Sí y el valor medio tienen que bajar al subir la tasa y la tasa
  con que descuenta la hoja (C15), si es numérica, tiene que cambiar; si no, código 6.
- **Prueba:** «H10 · un «recálculo» que no recalcula… se detecta». **Resultado:** corregido; 11 casos, todos pasan con `6406a99` y fallan con `ef93699`.0

### 11 · BAJA · Cerrojo

- **Cambio** (`hoja_resumen.py` · `sensibilidad`, `main`, `LOCK_DEFECTO`): `flock -w` (900 s por recálculo, `--espera-cerrojo`) con
  mensaje claro y código 6; `--cerrojo-ya-tomado` / `HOJA_RESUMEN_CERROJO_YA_TOMADO=1`; cerrojo por defecto el común si existe su
  carpeta y, si no, uno en el directorio temporal. Aviso en la ayuda y en el README.
- **Prueba:** «H11 · con el cerrojo ocupado… código 6 con mensaje claro y sin hoja». **Resultado:** corregido; 11 casos, todos pasan con `6406a99` y fallan con `ef93699`.1

### 12 · BAJA · Rótulos y mensajes

- **Cambio:** `tasa_txt` (0,085 → «8,5 %»); `ESTADO_LLANO` («pendiente de investigación» con tilde); «firme» sustituido por «Frente a
  la tasa, el resultado (no) cambia … no dice que el análisis sea seguro», calculado siempre con la tasa del análisis ± 1 punto (que se
  añaden a las tasas pedidas); «no utilizable» → «no se puede calcular» con su nota; origen y nombres de archivo al pie.
- **Pruebas:** «H12 · una tasa no entera…», «H12 · sin «Conclusión firme»…», «H12 · las tasas vecinas…», «H12 · el crecimiento «no
  utilizable» se explica». **Resultado:** corregido; 11 casos, todos pasan con `6406a99` y fallan con `ef93699`.2

### 13 · BAJA · Entradas mal formadas

- **Cambio** (`hoja_resumen.py` · `cargar_dict`, `leer_expediente`): JSON ilegible o con otra forma → código 3 con mensaje.
- **Prueba:** «H13 · un JSON truncado del expediente da código 3 con mensaje, sin traza de Python». **Resultado:** corregido; 11 casos, todos pasan con `6406a99` y fallan con `ef93699`.3

### 14 · BAJA · La batería no cubría lo anterior

- **Cambio:** batería nueva (ver arriba), con Vidrala 4.10.1 como ejemplo V6.3 vigente en lugar de Hermès, casos sin conclusión,
  condicionado, bloqueado, A2, motor B, no vigente, antecedente, F1 sintético, retirada y relanzamiento, página editada y códigos 4 y 5
  sin hoja; el recálculo independiente al 10 % se hace con `recalc.sh` y openpyxl (la lectura no es la del programa; el recálculo
  sigue siendo LibreOffice, no hay otro motor disponible). Registrada en `verificar_paquete.sh completa` (al menos 85 pruebas).
- **Resultado:** corregido; 11 casos, todos pasan con `6406a99` y fallan con `ef93699`.4

## Lo que queda sin hacer, con su motivo

- **Resumen llano escrito por el personaje** (fondo de los hallazgos 5 y 6): fuera de alcance por decisión del coordinador.
- **Brevedad** (hallazgo 6): ver el límite del apartado 6.
- **«Lo demás se queda quieto»** (hallazgo 7): se avisa en una frase; no se recalcula con el ROIC siguiendo a la tasa (sería cambiar
  un juicio del personaje).
- **Hoja escrita con `--salida` fuera del expediente:** ni la retirada ni el relanzamiento la archivan (no saben dónde está);
  `--comprobar` sí la da por no vigente.
- **Limpieza de un corchete de fuente dentro de un paréntesis:** deja «cálculo propio con)» (Elis); es texto del personaje y no se
  reescribe.
- **Motor C:** sigue sin probar (no hay expediente).
- **`verificar_paquete.sh` en el propio worktree:** el bloque del manifiesto falla allí (50 ausentes y 10.819 de más: binarios que no
  están en Git y carpetas ignoradas como `.lo_perfil/` y las descargas de `contrastes/`), con 0 modificados; por eso la verificación
  rápida se hizo, como en `1694f08`, sobre una extracción limpia (PASA).
- **Batería completa del paquete:** no repetida (ver «Resultados»).
- **Cambios en `cierre_v2.py` y `pipeline.py`:** son mínimos y solo actúan si hay una hoja (archivo) o con `--desde` (`fin` →
  `fin_anterior`), pero tocan la vía oficial: conviene que la segunda ronda los mire expresamente.
