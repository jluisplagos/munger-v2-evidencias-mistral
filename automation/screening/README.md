# Cribado del universo por tandas (A5/A6)

## Para qué sirve

Pasa las empresas del universo de etapa 1 por un **cribado** corto con la API de Claude:
¿merece la empresa un estudio a fondo? Aplica el embudo corregido de
`REORIENTACION_UNIVERSO.md` §4, en este orden: **calidad del negocio → caja → balance →
precio → encaje en la cartera**, con el motor de valoración adecuado a cada tipo de
negocio. No es una recomendación de compra, ni un análisis completo, ni aptitud para
dinero real. Tasa del 9 %, provisional (decisión de la persona responsable). Sin tamaños
de posición.

**Empresas del examen fuera (decisión C-EX).** Ahold, Jumbo, Zoetis, Elis, Vinci y Waste
Management no se criban hasta después del 23-nov-2026: lista cerrada en el código
(`EXCLUIDAS`), que quedan como `NO_PREPARADA:EMPRESA_DEL_EXAMEN_EXCLUIDA_HASTA_DESPUES_DEL_23_NOV`.
Quedan 111. Volver a incluirlas es un cambio de código que se revisa.

Cada ejecución del workflow es una **tanda** de 1 a 20 empresas. **Una sola aprobación**
del environment `inferencia-aprobada` cubre la tanda. Dentro, **una llamada por
empresa**, en secuencia y **sin reintentos**.

## Qué recibe el modelo

- **El encargo fijo** (`ENCARGO_CRIBADO.md`), con el esquema de la respuesta al final. Su
  huella (`encargo_sha256`) y la del sistema enviado (`system_sha256`) quedan registradas.
- **La convención de arrendamientos** (`convencion_arrendamientos`, C-ARR) y la **fecha de
  la hoja** (`fecha_hoja`, la «Fecha de análisis» tal como figura en ella).
- **El paquete de la empresa**, que sale solo de la Release `universo-etapa1-20261118`,
  asset `universo_etapa1.zip.zip` (9.222.746 bytes, SHA-256 `4d30f735…58b0a9`, fijados en
  el código). El workflow la descarga con el token de GitHub y el código comprueba la
  huella y el tamaño antes de abrirla. Las 117 huellas de los libros coinciden con
  `coordinacion/cierre_v2/universo_etapa1/INDICE.tsv`.
  - `respuesta`: `<Empresa>_respuesta.md`;
  - `cambios_v2`: `<Empresa>_cambios_v2.md`, si existe (28 empresas): los cambios de la
    versión 1 a la 2 del libro, de la propia persona;
  - `hoja_analisis` y `hoja_control_maestro`: las hojas «Análisis» y «Control maestro» del
    `<Empresa>_evaluada.xlsx`, en CSV. El libro se lee en **solo lectura** con la
    biblioteca estándar (sin LibreOffice ni macros; un libro con `vbaProject` o binarios se
    rechaza). Se copian los valores que guardó la hoja, **sin redondear**; solo las celdas
    con formato de fecha pasan a fecha ISO. Una fórmula sin valor guardado queda como
    `#SIN_VALOR_CALCULADO`. La primera columna es el número de fila. Los porcentajes llegan
    como fracción (0.109 = 10,9 %) y algunas fechas como texto; el encargo lo avisa.
  - No se mandan «Guía Simply Wall St» (instrucciones genéricas de la plantilla) ni
    «Opciones» (listas desplegables): constan en `hojas_omitidas`.
  - Cada archivo lleva su huella; las hojas, también la del libro (`origen_sha256`).

**Lista blanca.** Dentro de `EMPRESAS_LOTES_COMPLETOS/<Empresa>/` solo se admiten esos
tres nombres. Cualquier otro archivo, ruta rara, enlace o cifrado invalida la Release
entera: no se elige a mano qué se manda. El modelo no recibe la rúbrica, el examen, el
informe crítico ni ninguna conclusión del coordinador, ni el nombre del repositorio.

**Ceguera.** Se aplican a cada texto preparado las capas del análisis directo: copia
exacta de un archivo de `examen/`, `universo/`, `traspaso/` o `pruebas_candidata/` en
cualquier rama, menciones de la rúbrica o del informe crítico, y solape de 400 caracteres
con ese material. El código de un fallo lleva la marca que saltó o **todas** las rutas
ciegas con las que solapa el texto (no solo la primera). En el universo real, fuera de las
empresas del examen, saltan dos falsos positivos, que `excepciones_ceguera.json` admite
**solo para ese archivo, con esa huella y ese código exacto**: Andina y Petsathome usan
«rúbrica» en sentido contable (partidas del patrimonio y del estado de flujos). Las dos
excepciones de Elis se retiraron al quedar Elis fuera. Borrar una entrada devuelve esa
empresa a `NO_PREPARADA`, sin coste. Las excepciones no se mandan al modelo; constan en el
informe de la tanda.

## Qué devuelve

Un JSON pequeño por empresa (9 claves; esquema de unos 2.200 caracteres, sin uniones):

- `empresa`, `tipo_negocio`, `dcf_plantilla_aplica` (`si`/`no`/`dudoso`) y
  `motor_adecuado`;
- `filtros`: `calidad`, `caja`, `balance`, `precio` y `encaje`, cada uno con `resultado`
  (`pasa`/`no_pasa`/`dudoso`/`no_aplica`), `motivo` (una frase con cifra de la hoja) y
  `dato_clave` (p. ej. `Análisis!C46 = 1250.5`);
- `veredicto_cribado`: `estudiar_a_fondo`, `vigilar`, `descartar`, `demasiado_dificil` o
  `faltan_datos`;
- `pasivo_arrendamientos`: el pasivo por arrendamientos como dato aparte, con su celda;
- `que_lo_cambiaria` y `que_falta` (como mucho tres elementos cada uno).

Reglas del encargo que conviene conocer:

- «El negocio no se entiende» (`demasiado_dificil`) no es lo mismo que «el DCF de la
  plantilla no aplica» (cambia el motor y el filtro de precio, no la calidad).
- El límite de deuda se ajusta a la estabilidad del negocio.
- **Arrendamientos (decisión C-ARR de la persona responsable): una sola vez, en el
  flujo.** El alquiler se resta de la caja libre (como ya hace la plantilla); la deuda,
  deuda/EBITDA y deuda/caja libre se miden sin arrendamientos, con el EBITDA que ya resta
  el alquiler; el pasivo por arrendamientos va aparte. Un cociente de la hoja según la
  NIIF 16 no sirve tal cual. Cada `report.md` y cada `tanda.md` lo declaran en una línea
  fija que escribe el código, junto con la fecha de la hoja y una línea de condiciones:
  cifras de la etapa 1, sin las decisiones posteriores (P-O1, P-O2, F1-A/F1-B, D-US1/2,
  D-WM) ni verificación contra la fuente oficial.
- El veredicto, los semáforos, el precio de Sí y el tamaño de posición de la hoja son de
  la etapa 1, con otro embudo: el encargo pide no heredarlos y no repetir tamaños.
- El encaje en la cartera **nunca elimina**: el paquete no trae la cartera de la persona.
- Un negocio excelente y caro es `vigilar`, no `descartar`.

**Forma.** Por defecto (`gramatica = no`) no se envía `output_config.format`: el esquema
va en el encargo y la respuesta se valida aquí con las reglas del análisis directo
(claves duplicadas rechazadas; varios bloques ```json se unen solo si no hay texto entre
ellos y no repiten claves, y se anota). Con `gramatica = si` se piden salidas
estructuradas del servidor. El esquema es pequeño y sin uniones, pero **no se ha probado
contra la API**: si responde 400, la tanda se para en esa empresa (un 400 no se cobra; su
reserva cuenta como incierta hasta reconciliarla). Conviene probarlo con una tanda de una
sola empresa.

Las **comprobaciones mecánicas** (empresa distinta de la carpeta, filtro decidido sin
cifra, celda citada vacía o inexistente, veredicto incoherente con los filtros, encaje que
elimina, pasivo por arrendamientos vacío, un texto que menciona un tamaño de posición…) son avisos para la revisión; no aceptan ni rechazan.

## Paso a paso

1. **Actions → Cribado del universo Claude API → Run workflow** desde la rama con el
   código.
2. Rellena:
   - **empresas**: de 1 a 20 nombres de carpeta de la Release, separados por comas
     (`Pandora, FW_Thorpe`). Las propuestas de tandas están en el dry-run;
   - **modelo** y **esfuerzo** (por defecto Opus 5.5, `high`);
   - **coste_maximo_por_empresa_usd** (techo del código: 2). Tiene que cubrir la reserva
     de cada empresa: con Opus 5.5 la mayor es 1,52 USD, así que `1.6` basta para todas
     (se escribe **con punto**: `1,6` se rechaza en `preparar`, sin coste);
   - **coste_maximo_tanda_usd** (techo del código: 30);
   - **gramatica**: `no` (vía probada) o `si`.
3. El job `preparar` (sin secretos de inferencia) pasa las pruebas, descarga la Release,
   comprueba su huella, arma los paquetes y deja en el resumen la tabla de empresas con su
   reserva, la fecha de la hoja y la suma de reservas. Una empresa que no se puede
   preparar queda como `NO_PREPARADA:<motivo>` y la tanda sigue con las demás. Con una
   sola lectura de la rama de registro avisa de las empresas **ya cribadas** en otra
   ejecución: un run nuevo con ellas las volvería a pagar.
4. El job `cribado` espera tu aprobación (environment `inferencia-aprobada`). **Una sola
   aprobación** cubre todas las empresas.
5. Dentro, por cada empresa y en orden:
   1. si ya no queda tiempo para su peor caso antes del timeout del job, se para;
   2. **máximo de la tanda**: lo comprometido por esta ejecución (coste conocido o cota de
      cada empresa ya llamada, más lo que había en la rama de registro de intentos
      anteriores, leído una vez al empezar) más el máximo por empresa no puede pasar del
      máximo de la tanda; si pasa, se para;
   3. `critical_review.run` de AUTO1: **tope acumulado**
      `MUNGER_TOPE_ACUMULADO_ANTHROPIC_USD` con todo lo comprometido en la rama de
      registro (de todas las tareas, incluidas las empresas anteriores de esta tanda),
      conteo de tokens, **reserva create-only** publicada antes de llamar, **una llamada**
      sin reintentos, estado de coste y publicación de `reservation.json`, `report.json`,
      `report.md` y `sources.json` en
      `automation/coordination/reviews/cribado-<ejecución>-<empresa>/`.

   **Llamadas a GitHub.** Durante la tanda, el recorrido del registro de AUTO1 se sustituye
   por uno con caché: una carpeta se vuelve a leer solo si cambia el SHA de árbol que trae
   su listado (depende del contenido; sin SHA se lee siempre). Una tanda de 20 hace unas
   333, 381 y 441 llamadas con 12, 60 y 120 carpetas en el registro (antes, unas 1.630,
   4.510 y 8.110), muy por debajo de las 1.000 por hora del `GITHUB_TOKEN`.
6. Si una empresa falla, se registra y se sigue con la siguiente. La tanda **se para**:
   - al alcanzar el máximo de la tanda o el tope acumulado (o si falta el tope);
   - si la API responde un error 4xx (400 de gramática, 401, 429…): se repetiría en las
     demás;
   - tras dos fallos seguidos después de enviar (red, stream cortado);
   - tras dos respuestas pagadas e inválidas seguidas (`RESULTADO_NO_ACEPTADO_NO_REINTENTAR`):
     apuntan a un fallo sistemático de forma;
   - si un fallo ocurre después de reservar (p. ej. no se pudo publicar): cuenta el
     máximo por empresa;
   - si un coste queda sin cota (`INCIERTO_SIN_COTA`): hay que reconciliarlo en Console.
   
   Lo que queda sin llamar figura como `NO_LLAMADA_TANDA_PARADA`.
7. **Informe de la tanda**: en el resumen del job (tabla empresa → veredicto → estado →
   coste) y en la rama de registro, en
   `automation/coordination/reviews/cribado-<ejecución>-tanda-<intento>/report.md` y
   `report.json`. Esa carpeta no lleva `reservation.json`: no cuenta como gasto. El
   artefacto del job lleva además cada empresa por separado.

Un **«Re-run»** de la misma ejecución reutiliza las tareas: las empresas ya reservadas
quedan `YA_RESERVADO_SIN_NUEVA_LLAMADA` y no se vuelven a llamar; las que quedaron sin
llamar sí se llaman (con una nueva aprobación), y cuentan para el mismo máximo de la tanda.
El `tanda.md` de un intento solo suma ese intento: el total de la ejecución se suma desde
las carpetas `cribado-<ejecución>-*` del registro.

**Lanzar las tandas de una en una.** Comparten grupo de concurrencia con el análisis
directo, y GitHub cancela la ejecución que espera en cola si llega otra.

**Reconciliar un `INCIERTO`** (p. ej. tras un 400 de gramática o un corte de red): buscar
en Claude Console la petición por la hora de la ejecución; si no se cobró, o tras anotar el
coste real, la persona responsable actualiza a mano `reservation.json` de esa carpeta en la
rama de registro (`cost_status` = `CONOCIDO_ESTIMADO` y `estimated_cost_usd`). Hasta
entonces cuenta la reserva entera.

## Tanda 0 · prueba técnica de una empresa (primero)

Antes de las tandas de 20, una tanda de una empresa que no sea del examen:
`empresas` = `Pandora` (o Inditex: ambas arrendatarias, sirven para ver C-ARR),
Opus 5.5 `high`, `coste_maximo_por_empresa_usd` = `1.6`, `coste_maximo_tanda_usd` = `2`,
`gramatica` = `si`. Preparada sin API: reserva 1,183 USD con la gramática, hoja del
2026-10-25. Comprobar el estado, `model_returned`, la facturación, los tokens reales frente
a la cota y al orientativo, lo que tarda y que se publican el informe de la empresa y el de
la tanda. Si da 400, reconciliar la reserva y repetir con `gramatica` = `no`; si funciona,
`si` en todas (la validación local se mantiene). Después, una de 3–5 empresas para medir
tiempos y llamadas a GitHub. Su veredicto no cuenta para A6 si después cambia el encargo.

## Qué cuesta (dry-run del 18-nov-2026, ronda 2, sin API)

```
python3 automation/screening/screening.py cotas --release <ZIP> --code-sha <HEAD> --output <dir>
```

Prepara las 111 empresas (sin las seis del examen) sin llamar y da por empresa los bytes del envío, la cota de
tokens y la cota en USD (la reserva de AUTO1: un token por byte + 4.096 y la salida
máxima de 32.768 tokens), más un coste **orientativo** (3,5 bytes por token y 15.000
tokens de salida; el análisis directo real gastó unos 17.000 con `high`). Con Opus 5.5,
`high` (4 / 20 USD por millón):

| | Envío | Cota USD | Orientativo USD |
|---|---|---|---|
| Por empresa | 114–210 KB | 1,13–1,52 | 0,43–0,54 |
| Por tanda de 20 | | 23,9–24,9 | 9,0–9,3 |
| Tanda 6 (11 empresas) | | 13,65 | 5,09 |
| Las 111 (5 tandas de 20 y 1 de 11) | | 135,59 | 50,74 |

La cota es lo que se reserva antes de cada llamada; al conocer el coste, la exposición
baja al coste real. El tope acumulado tiene que cubrir lo ya comprometido más 1,6 USD
(el máximo por empresa) en cada paso.

## Límites

- No se ha llamado a la API. La forma de la respuesta, la gramática (`gramatica = si`) y el
  coste real están sin comprobar; la cota sí acota lo que se puede gastar.
- El cribado lee la hoja tal como la guardó la persona: si una cifra de la hoja está mal,
  el cribado hereda el error (no hay verificación contra la fuente oficial). La fecha de
  cada hoja es la de su análisis: un precio viejo puede dar un `pasa` desfasado.
- La tasa del 9 % es provisional. C-ARR y C-EX son decisiones de la persona; C-EX vence
  después del 23-nov y requiere un cambio de código.
- La caché del registro confía en el SHA de árbol del listado; si GitHub sirviera un
  `reservation.json` atrasado justo después de cambiarlo, quedaría la reserva (mayor que el
  coste), salvo un `INCIERTO_SIN_COTA` recién escrito, que bloquea en la siguiente lectura
  sin caché (la de la próxima ejecución).
- El plazo de 15 minutos se cuenta desde que empieza la tanda, no el job (la descarga y el
  checkout tardan menos de un minuto).
- No hay revalidación fuera de línea con el validador del cribado (`revalidar.py` es del
  análisis directo).
- Cada empresa publica en la rama de registro, en un repositorio público, su `sources.json`
  (el texto de la etapa 1) y la salida del modelo.
- Las comprobaciones mecánicas no miden la calidad económica del cribado; hace falta
  revisión humana. Ningún veredicto se acepta ni se integra automáticamente.
- La exclusión mutua es con el análisis directo (mismo grupo de concurrencia). Otro
  workflow de AUTO1 que reserve a la vez podría pasar la misma comprobación del tope.
- Un job cortado por el timeout en mitad de una llamada deja la reserva publicada
  (cuenta entera) sin informe de esa empresa; el código deja de empezar empresas 15 min
  antes del timeout para evitarlo.

## Finalistas para la segunda vuelta (análisis directo)

`finalistas.py` lee los `report.json` del cribado ya publicados en la rama de registro (sin
red, con `git show` del clon) para las ejecuciones que se le declaran y aplica un criterio
mecánico fijo sobre los resultados de los filtros, sin revisarlos ni aceptarlos:

- nivel 1: calidad, caja y balance = `pasa`, y precio = `pasa` o `dudoso`;
- nivel 2: ninguno de los tres es `no_pasa` ni `no_aplica`, al menos dos son `pasa`, y
  precio = `pasa` o `dudoso`;
- solo cuentan las respuestas con formato válido; el encaje y el veredicto del cribado no
  entran (el veredicto se muestra).

```
python3 -I automation/screening/finalistas.py \
  --ejecuciones 44406828081,44413758195,44502520327,44505954250,44509331308,44512238939,44515220408 \
  --salida automation/screening/FINALISTAS_tandas_1_6_y_pandora
```

Con las seis tandas y Pandora (111 empresas): FW_Thorpe (nivel 1); Azkoyen, Betsson,
CocaCola, Moury, Spie, Strabag y Tupras (nivel 2). Fuera del criterio pese al veredicto
`estudiar_a_fondo`: Ege_Profil, Italian_Wines y Omer. Es una propuesta: decide la persona responsable. Los paquetes del
análisis directo de las finalistas los prepara `automation/direct_analysis/universo.py`.

## Probar sin gastar

```
python3 -I -m unittest discover -s automation/screening -p 'test_*.py' -v
```

Las pruebas simulan la API, la rama de registro y una Release pequeña; no abren red.
