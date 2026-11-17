# Encargo para Mistral · Registro de entradas de Ahold Delhaize (examen del personaje)

**Para pegar en una ventana nueva de Mistral.** Fecha: 17-nov-2026. Encarga: el coordinador Claude. Revisa: un agente Claude distinto, que es quien sella. **Tú no sellas ni marcas nada como «verificado».**

## 1. Qué es esto

Munger V2 es un sistema de análisis de empresas. Se está examinando con cinco casos reales; Ahold Delhaize es el primero. Antes de que el sistema juzgue la empresa, **cada cifra que usa tiene que llegar a una página de un documento oficial**. Tu trabajo es el del *extractor* del registro de entradas: para cada cifra, decir de dónde sale exactamente.

Lee antes `AGENTS.md` del repositorio auxiliar y respeta sus reglas: no escribir en `jluisplagos/munger-v2`, no subir PDF/XLSX/ZIP a Git, no aprobar tu propio trabajo, no declarar aptitud para dinero real.

## 2. Dónde está todo

- **Expediente (solo lectura):** repo `jluisplagos/munger-v2`, rama `examen/ahold`, carpeta `munger_v2_r1/personaje_v2/empresas_v2_correcciones/2026-11_examen_universo/ahold_4_15/Ahold/`:
  - `texto/AD_annual-report-AAAA.txt`: los diez informes anuales 2016–2025 en texto, con marcas `[PDF PAGE n]` (n es la página del PDF);
  - `fase1_partes/AR_AAAA.json`: lo que extrajeron los extractores de la Historia, con `impreso`, `pagina` y `linea` literal de cada componente (es tu mejor punto de partida);
  - `fase1_v63.json`, `fase1_metadatos.json`, `historia_revision.md`: la Historia construida y los metadatos.
- **PDF oficiales:** descárgalos tú de sus URL de `coordinacion/cierre_v2/u2_tercer_b/INDICE_FUENTES.csv` (rama `coordinacion/cierre-v2` del auxiliar) y comprueba que su SHA-256 es el de la columna `sha256`. Si alguno no coincide, **para y dilo**: no sigas con otra edición.
- **Plantilla del registro:** `coordinacion/cierre_v2/examen/ahold/verificacion_entradas.plantilla.json` (288 entradas, una por celda; `valor_modelo` es el valor del libro). La lista resumida está en `LISTA_ENTRADAS.csv`.
- **Modelo de formato:** el registro ya revisado de Elis, en el repo del producto, rama `integracion/candidata-cierre-v2`, `munger_v2_r1/personaje_v2/empresas_v2_correcciones/2026-11_Vidrala_ensayo_4_14/elis_motor_A/Elis/verificacion_entradas.json`. Las reglas completas están en la cabecera de `munger_v2_r1/personaje_v2/scripts/verificacion_entradas.py` (R1–R3, R415-SIGNO, N2, N4, T1–T5). **Léelas: la máquina las comprueba.**

## 3. Qué tienes que hacer

**Alcance: las 258 entradas cuya `clase_propuesta` no es `hipotesis`** (Historia, Análisis y Control maestro). Las 30 hipótesis las escriben las fases del personaje; no las toques.

Para cada entrada, rellena:
1. `clase`: `dato_publicado`, `derivado`, `cero_comprobado`, `dato_ausente` o `no_aplicable`. Nunca `hipotesis` para un dato.
2. **`dato_publicado`:** `fuente` completa: `documento`, `version` (nombre del PDF y su SHA-256), `archivo` (ruta del texto, `texto/…`), `sha256` del archivo de texto, `pagina` (entero, página del PDF), `folio` (número impreso, aparte), `ubicacion` (tabla o nota), `concepto`, `columna`, `periodo`, `unidad`, `escala`, `signo`, `tratamiento`, `perimetro` (`consolidado`), `reexpresado`, `valor_fuente` (**la cifra publicada con su signo**: «(1,944)» es −1944) y `cita` (**copia literal** de la línea de esa página que contiene la cifra, sin redondear).
3. **`derivado`** (sumas como la deuda, el circulante o el EBIT derivado): `derivacion` con `origenes` (entradas auxiliares `aux:<documento>_p<página>_<concepto>_<año>`, cada una con su propia fuente completa), `formula` sobre `o["<origen>"]` que use todos sus orígenes y solo ellos, y `conciliacion` en una frase con los números.
4. **`cero_comprobado`:** fuente con la cita que demuestra que la partida no existe. Ojo: «no material» no es «no existe» (por ejemplo, los minoritarios de 2019). Si la cita no prueba la inexistencia, `dato_ausente` con justificación.
5. `comprobacion`: `extractor` = «Mistral (nombre exacto del modelo que uses)», `revisor` = null, `resultado` = «pendiente», `fecha` = la de hoy, `nota` con lo que dudaste. **No escribas `vinculo`.**
6. Cabecera del registro: `perimetro_del_expediente` = «consolidado», con `perimetro_justificacion`; `extractor`, `fecha_extraccion` y `nota_del_extractor`.

**Precio y tasa sin riesgo (Análisis C37, C41 y la tasa).** Lo que hay ahora (36,05 € de una web de terceros sin hora; Bund 3,34 % de un resumen de búsqueda) **no vale**. Consigue:
- el **cierre oficial no ajustado** de Ahold Delhaize (ISIN NL0011794037, Euronext Amsterdam) de la sesión más reciente, en la página de histórico de Euronext Live, guardado como archivo de texto con su SHA-256, y di si esa fecha incluye algún dividendo pendiente de pagar;
- la **rentabilidad del Bund a 10 años** de la misma fecha, de una fuente oficial (Deutsche Bundesbank o BCE), guardada igual.
Deja esos archivos en tu carpeta de resultados (son texto, no PDF) y regístralos como `fuentes_mercado` en la cabecera, como hizo Elis. Si no puedes acceder a una fuente oficial, dilo; **no pongas otra en su lugar sin avisar**.

**Prioridad**, por si no llegas a todo: primero las entradas de cálculo (`ambito` = «calculo») de 2023–2025 y del Análisis (precio, acciones, C46–C50, deuda, caja, arrendamientos y pensiones de 2025); después el resto de cálculo; al final las de juicio.

## 4. Lo que tienes que vigilar especialmente en Ahold

- **Arrendamientos:** «Repayment of lease liabilities» incluye principal **e intereses** (el informe no los separa). Regístralo así en `concepto` y `tratamiento`; no lo partas tú.
- **Deuda:** préstamos + préstamos a corto plazo + descubiertos bancarios (+ las acciones preferentes de financiación mientras existieron, 2016–2018). Los descubiertos incluyen un *cash pooling* nocional que el balance compensa con el mismo importe dentro de la caja: dilo en `tratamiento`.
- **Ejercicios de 52 y 53 semanas** (2020 tuvo 53): el `periodo` lleva las fechas exactas de cierre.
- **Reexpresiones:** 2018 se reexpresó por NIIF 16 en el informe 2019; 2023 se reexpresó en el informe 2024 (ventas). La Historia usa el comparativo más reciente: tu fuente tiene que ser **la columna y el informe que dan el valor del libro**, no otra edición.
- **Acciones:** la nota de beneficio por acción las imprime en millones.

## 5. Qué entregas

En el repositorio auxiliar, **rama nueva `mistral/examen-ahold-entradas`**, carpeta `resultados_examen/ahold/`:
1. `verificacion_entradas.json`: el registro completo, con las 288 entradas (las 30 hipótesis, sin tocar).
2. `fuentes_mercado/`: los archivos del precio y del Bund, con un `HUELLAS.txt` (SHA-256).
3. `DESCARGAS.tsv`: cada PDF descargado, con URL, fecha, bytes, SHA-256 y si coincide con el índice.
4. `ENTREGA.md` (máximo una página): cuántas entradas de cada clase; **cuáles no pudiste resolver y por qué**; dudas de concepto o de columna; modelo y herramientas realmente usados.

Commit y push al terminar cada bloque grande. No fusiones nada.

## 6. Cómo se acepta (lo comprueba la máquina, no tú)

El coordinador ejecutará `verificacion_entradas.py comprobar` sobre una copia del expediente con tu registro. Se acepta para pasar a la revisión cuando:
- las 288 entradas están, sin repetir ni sobrar;
- **cero errores de formato**: toda `cita` está en su página y contiene `valor_fuente` con su signo; toda página existe; toda fórmula reproduce su valor; todo SHA-256 coincide;
- ninguna entrada de dato queda sin `clase`, salvo las que declares sin resolver en `ENTREGA.md`.

Después, un agente Claude distinto **revisa en la fuente** cada entrada material y sella solo lo que comprueba. Hay como máximo dos rondas de corrección. **Si declaras más de lo que hiciste, se verá en la revisión**: prefiero un «no lo encontré» honesto a una cita forzada.
