# Cribado del universo por tandas (A5/A6)

## Para qué sirve

Pasa las empresas del universo de etapa 1 por un **cribado** corto con la API de Claude:
¿merece la empresa un estudio a fondo? Aplica el embudo corregido de
`REORIENTACION_UNIVERSO.md` §4, en este orden: **calidad del negocio → caja → balance →
precio → encaje en la cartera**, con el motor de valoración adecuado a cada tipo de
negocio. No es una recomendación de compra, ni un análisis completo, ni aptitud para
dinero real. Tasa del 9 %, provisional (decisión de la persona responsable). Sin tamaños
de posición.

Cada ejecución del workflow es una **tanda** de 1 a 20 empresas. **Una sola aprobación**
del environment `inferencia-aprobada` cubre la tanda. Dentro, **una llamada por
empresa**, en secuencia y **sin reintentos**.

## Qué recibe el modelo

- **El encargo fijo** (`ENCARGO_CRIBADO.md`), con el esquema de la respuesta al final. Su
  huella (`encargo_sha256`) y la del sistema enviado (`system_sha256`) quedan registradas.
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
    `#SIN_VALOR_CALCULADO`. La primera columna es el número de fila.
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
con ese material. En el universo real saltan cuatro falsos positivos, que
`excepciones_ceguera.json` admite **solo para ese archivo, con esa huella y ese código**:

- Andina y Petsathome: la hoja usa «rúbrica» en sentido contable (partidas del
  patrimonio y del estado de flujos);
- Elis (respuesta y hoja «Análisis»): la ficha provisional del traspaso cita como «antes»
  la celda B101 de la hoja de la persona; la copia va de la etapa 1 al traspaso.

Son **propuestas del autor, pendientes de revisión**. Borrar una entrada devuelve esa
empresa a `NO_PREPARADA`, sin coste. Las excepciones no se mandan al modelo; constan en el
informe de la tanda.

## Qué devuelve

Un JSON pequeño por empresa (8 claves; esquema de unos 2.200 caracteres, sin uniones):

- `empresa`, `tipo_negocio`, `dcf_plantilla_aplica` (`si`/`no`/`dudoso`) y
  `motor_adecuado`;
- `filtros`: `calidad`, `caja`, `balance`, `precio` y `encaje`, cada uno con `resultado`
  (`pasa`/`no_pasa`/`dudoso`/`no_aplica`), `motivo` (una frase con cifra de la hoja) y
  `dato_clave` (p. ej. `Análisis!C46 = 1250.5`);
- `veredicto_cribado`: `estudiar_a_fondo`, `vigilar`, `descartar`, `demasiado_dificil` o
  `faltan_datos`;
- `que_lo_cambiaria` y `que_falta` (como mucho tres elementos cada uno).

Reglas del encargo que conviene conocer:

- «El negocio no se entiende» (`demasiado_dificil`) no es lo mismo que «el DCF de la
  plantilla no aplica» (cambia el motor y el filtro de precio, no la calidad).
- El límite de deuda se ajusta a la estabilidad del negocio. **Los arrendamientos se
  cuentan siempre**, de forma coherente en deuda, EBITDA y caja libre. Es la convención que
  propone el autor para cumplir «siempre o nunca»; si la persona responsable prefiere
  «nunca», hay que cambiar el encargo (y su huella).
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
elimina…) son avisos para la revisión; no aceptan ni rechazan.

## Paso a paso

1. **Actions → Cribado del universo Claude API → Run workflow** desde la rama con el
   código.
2. Rellena:
   - **empresas**: de 1 a 20 nombres de carpeta de la Release, separados por comas
     (`Ahold, Pandora, FW_Thorpe`). Las propuestas de tandas están en el dry-run;
   - **modelo** y **esfuerzo** (por defecto Opus 5.5, `high`);
   - **coste_maximo_por_empresa_usd** (techo del código: 2). Tiene que cubrir la reserva
     de cada empresa: con Opus 5.5 la mayor es 1,51 USD, así que **1,6** basta para todas;
   - **coste_maximo_tanda_usd** (techo del código: 30);
   - **gramatica**: `no` (vía probada) o `si`.
3. El job `preparar` (sin secretos de inferencia) pasa las pruebas, descarga la Release,
   comprueba su huella, arma los paquetes y deja en el resumen la tabla de empresas con su
   reserva y la suma de reservas. Una empresa que no se puede preparar queda como
   `NO_PREPARADA:<motivo>` y la tanda sigue con las demás.
4. El job `cribado` espera tu aprobación (environment `inferencia-aprobada`). **Una sola
   aprobación** cubre todas las empresas.
5. Dentro, por cada empresa y en orden:
   1. si ya no queda tiempo para su peor caso antes del timeout del job, se para;
   2. **máximo de la tanda**: lo comprometido por esta ejecución (coste conocido o cota de
      cada empresa ya llamada, y lo que haya en la rama de registro de intentos
      anteriores) más el máximo por empresa no puede pasar del máximo de la tanda; si
      pasa, se para;
   3. `critical_review.run` de AUTO1: **tope acumulado**
      `MUNGER_TOPE_ACUMULADO_ANTHROPIC_USD` con todo lo comprometido en la rama de
      registro (de todas las tareas, incluidas las empresas anteriores de esta tanda),
      conteo de tokens, **reserva create-only** publicada antes de llamar, **una llamada**
      sin reintentos, estado de coste y publicación de `reservation.json`, `report.json`,
      `report.md` y `sources.json` en
      `automation/coordination/reviews/cribado-<ejecución>-<empresa>/`.
6. Si una empresa falla, se registra y se sigue con la siguiente. La tanda **se para**:
   - al alcanzar el máximo de la tanda o el tope acumulado (o si falta el tope);
   - si la API responde un error 4xx (400 de gramática, 401, 429…): se repetiría en las
     demás;
   - tras dos fallos seguidos después de enviar (red, stream cortado);
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

## Qué cuesta (dry-run del 18-nov-2026, sin API)

```
python3 automation/screening/screening.py cotas --release <ZIP> --code-sha <HEAD> --output <dir>
```

Prepara las 117 empresas sin llamar y da por empresa los bytes del envío, la cota de
tokens y la cota en USD (la reserva de AUTO1: un token por byte + 4.096 y la salida
máxima de 32.768 tokens), más un coste **orientativo** (3,5 bytes por token y 15.000
tokens de salida; el análisis directo real gastó unos 17.000 con `high`). Con Opus 5.5,
`high` (4 / 20 USD por millón):

| | Envío | Cota USD | Orientativo USD |
|---|---|---|---|
| Por empresa | 114–210 KB | 1,13–1,51 | 0,43–0,54 |
| Por tanda de 20 | | ≈ 24 | ≈ 9 |
| Las 117 (6 tandas: 5 de 20 y 1 de 17) | | 142,19 | 53,27 |

La cota es lo que se reserva antes de cada llamada; al conocer el coste, la exposición
baja al coste real. El tope acumulado tiene que cubrir lo ya comprometido más 1,6 USD
(el máximo por empresa) en cada paso.

## Límites

- No se ha llamado a la API. La forma de la respuesta, la gramática (`gramatica = si`) y el
  coste real están sin comprobar; la cota sí acota lo que se puede gastar.
- El cribado lee la hoja tal como la guardó la persona: si una cifra de la hoja está mal,
  el cribado hereda el error (no hay verificación contra la fuente oficial). La fecha de
  cada hoja es la de su análisis: un precio viejo puede dar un `pasa` desfasado.
- La convención de arrendamientos («siempre») y la tasa del 9 % son provisionales.
- Las comprobaciones mecánicas no miden la calidad económica del cribado; hace falta
  revisión humana. Ningún veredicto se acepta ni se integra automáticamente.
- La exclusión mutua es con el análisis directo (mismo grupo de concurrencia). Otro
  workflow de AUTO1 que reserve a la vez podría pasar la misma comprobación del tope.
- Un job cortado por el timeout en mitad de una llamada deja la reserva publicada
  (cuenta entera) sin informe de esa empresa; el código deja de empezar empresas 15 min
  antes del timeout para evitarlo.

## Probar sin gastar

```
python3 -I -m unittest discover -s automation/screening -p 'test_*.py' -v
```

Las pruebas simulan la API, la rama de registro y una Release pequeña; no abren red.
