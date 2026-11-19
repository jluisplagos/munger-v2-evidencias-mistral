# Lanzador del análisis directo

## Para qué sirve

Compara el personaje completo con un **análisis directo en una sola pasada** de un
modelo potente, con los **mismos datos verificados** y la misma tasa (9 %).
Es la comparación de `REORIENTACION_UNIVERSO.md` §10: las empresas del examen (Ahold,
Jumbo, Zoetis en sus dos tiempos, Vinci y Elis) y, en una segunda vuelta, las finalistas del
cribado del universo, solo con su etapa 1. Sirve también para repetir un caso
(repetibilidad) y para medir lo que cuesta un análisis. La lista de paquetes y su coste
están en «Paquetes preparados».

Cada ejecución hace **como máximo una llamada** a la API de Anthropic, sin reintentos,
y solo después de que una persona la apruebe en GitHub.

## Qué recibe el modelo

- **El encargo fijo** (`ENCARGO_ANALISIS_DIRECTO.md`). Pide: estado, cubo, acción,
  tres escenarios de valor por acción con una explicación breve de supuestos y cifras,
  la escalera del Anexo C con k = 3 (precio del escenario malo, P*, precio de Sí =
  mín(P*, V_normal), ponderado y zona), el crecimiento implícito, la sensibilidad a la
  tasa del 7 al 11 %, qué haría falsa la conclusión y qué no sabe. Prohíbe usar memoria
  o hechos que no estén en el paquete. Su texto no cambia entre ejecuciones; su huella
  queda registrada.
- **Reglas de salida que comparte con el personaje** (decisión registrada aquí): una
  sola tasa (9 %) y ningún tamaño de posición (D16).
- **La misma etapa 1 que el personaje** (decisión L2 de la persona responsable,
  18-nov-2026): el Excel evaluado, pasado a texto, y la respuesta de etapa 1, en
  `etapa1/`.
  La revisión a ciegas no debería contar como error lo que el análisis directo no podía
  saber por no tener las demás reglas del personaje.
- **El paquete de entrada**: los archivos de texto que declara un manifiesto, con su
  fecha de corte.

El modelo **no** recibe la rúbrica, el informe crítico, nada de `examen/`, `universo/`,
`traspaso/` o `pruebas_candidata/`, ni las salidas, fases, prompts o material de
auditoría del personaje. El lanzador lo comprueba en cuatro capas:

1. **Lista blanca de rutas.** Solo se admite `datos_analisis_directo/<empresa>/` y,
   dentro, `datos_v63.md`, `datos_v63.json`, `fase1_v63.json`, `extracto_v63.md` y
   archivos `.txt`, `.md`, `.csv` o `.json` bajo `fuentes/`, `historia/`,
   `registro_entradas/` o `etapa1/`. Todo lo demás se rechaza.
2. **Nombres prohibidos** dentro de esa raíz: fases, fichas, auditorías, prompts,
   relevos, verificaciones (salvo en `registro_entradas/`), rúbrica, informe crítico…
   En `etapa1/` se admiten los nombres propios de la etapa 1 (`respuesta`, hojas como
   «Diagnóstico V6», `precio`, `ficha`); siguen prohibidos los de material ciego
   (examen, universo, traspaso, rúbrica, informe crítico, contradictor, prompts,
   relevos, auditoría).
3. **Huellas.** Se rechaza la copia exacta de cualquier archivo de `examen/`,
   `universo/`, `traspaso/` o `pruebas_candidata/` en cualquier rama o commit
   disponible. Única excepción: el registro de entradas (`LISTA_ENTRADAS.csv` y su
   plantilla), y solo dentro de `registro_entradas/`.
4. **Contenido.** Se rechaza un texto que copie 400 caracteres seguidos de ese material
   (aunque se le quiten líneas o se dupliquen espacios), o que mencione la rúbrica o el
   informe crítico (también con guiones, espacios dobles o caracteres invisibles).

El caso y las descripciones del manifiesto tampoco pueden nombrar el examen, la
rúbrica, el personaje ni Munger. El nombre del repositorio no se envía al modelo.

## Paso a paso

### 1. Preparar el paquete (una vez por caso)

1. Copia los datos verificados, como texto UTF-8, a
   `datos_analisis_directo/<empresa>/`:
   - `fuentes/`: los textos de las fuentes (informes anuales, 10-K, comunicados,
     cotización);
   - `historia/`: la Historia;
   - `registro_entradas/`: el registro de entradas; por ejemplo, una copia de
     `coordinacion/cierre_v2/examen/ahold/LISTA_ENTRADAS.csv` con la misma huella;
   - `etapa1/`: la misma etapa 1 que recibe el personaje: la respuesta (p. ej. una
     copia de `fuentes_usuario/ahold_etapa1/Ahold_respuesta.md`) y el Excel evaluado
     pasado a texto (por ejemplo, un CSV por hoja). El `.xlsx` no se admite;
   - en la raíz, si existen: `datos_v63.md` o `.json`, `fase1_v63.json`, `extracto_v63.md`.

   Excel y PDF no valen: hace falta su versión en texto. Los archivos pueden estar
   en otra rama: basta indicar el commit.
2. Calcula la huella de cada archivo: `sha256sum <archivo>`
   (en Windows, `certutil -hashfile <archivo> SHA256`).
3. Crea el manifiesto en `automation/direct_analysis/paquetes/<nombre>.json`.
   Ejemplo para Zoetis, primer tiempo:

   ```json
   {
     "empresa": "zoetis",
     "caso": "Zoetis primer tiempo",
     "fecha_corte": "2026-10-09",
     "archivos": [
       {"id": "registro_entradas", "ruta": "datos_analisis_directo/zoetis/registro_entradas/registro.json",
        "commit": "<40 caracteres del commit, opcional>",
        "sha256": "<64 caracteres>", "descripcion": "Registro de entradas verificado"},
       {"id": "extracto", "ruta": "datos_analisis_directo/zoetis/extracto_v63.md",
        "sha256": "<64 caracteres>", "descripcion": "Extracto de las fuentes hasta el 9-oct-2026"}
     ]
   }
   ```

   - Sin `commit`, el archivo se lee del mismo commit que el código.
   - Si la huella no coincide, si falta, o si el archivo no es texto, no se llama.
   - La fecha de corte la declara el manifiesto y el código no la contrasta: para
     Zoetis, primer tiempo, tiene que ser `2026-10-09`.
4. Haz commit del manifiesto en la rama desde la que vas a lanzar.

### 2. Lanzar

1. En GitHub: **Actions → Analisis directo Claude API → Run workflow**.
2. Rellena:
   - **empresa**: igual que en el manifiesto (`zoetis`, `ahold`…);
   - **paquete**: la ruta del manifiesto;
   - **modelo**: por defecto `claude-opus-5-5`. Usa el mismo que el agente principal
     del personaje;
   - **esfuerzo**: `low` … `max`. Usa el mismo que el personaje. Estos modelos no
     admiten un presupuesto de pensamiento en tokens: el esfuerzo es el único mando;
   - **coste máximo en USD** de esta ejecución (hasta 5).
3. El workflow pasa las pruebas y prepara el paquete **sin llamar a la API**. En el
   resumen del job `preparar` verás los archivos, sus huellas, la cota de tokens y la
   reserva estimada. Si no cabe en el contexto o en el coste máximo, se para aquí.
   El paquete **nunca se recorta**.
4. El job `analisis` espera tu aprobación (environment `inferencia-aprobada`).
   Revisa el resumen de `preparar` y aprueba o rechaza.

### 3. Recoger el resultado

- **Artefacto** del job `analisis`: `report.json` (todo: análisis, salida en bruto,
  uso de tokens, coste, huellas), `report.md` (legible) y `sources.json` (el paquete
  exacto enviado).
- **Rama de registro** `automatizacion/claude-api-piloto-registro`, carpeta
  `automation/coordination/reviews/analisis-directo-<empresa>-<id de ejecución>/`:
  los mismos archivos y `reservation.json`.
- Estados posibles:
  - `AUDITORIA_DOCUMENTAL_PENDIENTE_ACEPTACION`: análisis recibido y con formato
    válido, pendiente de la revisión a ciegas (el nombre del estado viene de AUTO1);
  - `RESULTADO_NO_ACEPTADO_NO_REINTENTAR`: respuesta pagada pero incompleta o con
    formato inválido; la salida en bruto se conserva;
  - `INFERENCIA_SIN_VEREDICTO_COSTE_INCIERTO`: fallo tras enviar; cuenta la reserva
    completa hasta reconciliarla en Console;
  - `YA_RESERVADO_SIN_NUEVA_LLAMADA`: un «Re-run» de la misma ejecución. No llama.
- Las «comprobaciones mecánicas» (escalera recalculada con el Anexo C a partir de sus
  escenarios, orden de los valores, zona, citas literales, probabilidades) son avisos
  para la revisión. No aceptan ni rechazan: si una falla, queda como aviso
  («Comprobación mecánica no completada») y el análisis pagado se conserva.
- Si una enumeración vuelve con otras mayúsculas o tildes («Demasiado Difícil»), se
  guarda la forma canónica y el original queda en `normalizaciones_enum` y en la salida
  en bruto: la llamada no se pierde por eso.
- Para repetir un caso (repetibilidad), lanza una ejecución nueva con el mismo
  manifiesto. La huella `package_sha256` es la misma si el paquete no cambió.

## Qué cuesta (orden de magnitud)

Tarifas consultadas el 17-nov-2026 (USD por millón de tokens, entrada / salida):
Opus 5.5, 4 / 20; Fable 5.2, 8 / 40; Sonnet 5.5, 2 / 10.

- Paquete de 100 a 300 KB de texto con Opus 5.5: de 30 000 a 90 000 tokens de
  entrada y, con esfuerzo alto, de 10 000 a 30 000 de salida (el pensamiento cuenta
  como salida). Coste real: **de 0,3 a 1 USD**. Con Fable 5.2, el doble.
- La **reserva** es más alta: cuenta un token por byte y la salida máxima
  (32 768 tokens). Para 300 KB con Opus 5.5 ronda **1,9 USD**. El coste máximo que
  pongas tiene que cubrir la reserva que muestra `preparar`.
- **Tope acumulado**: la variable `MUNGER_TOPE_ACUMULADO_ANTHROPIC_USD` del
  environment. Antes de llamar se suma todo lo ya comprometido en la rama de registro
  (de todas las tareas) más el coste máximo de esta ejecución; si pasa del tope, no se
  llama. Sin la variable, no se llama nunca.
- El origen del crédito (promocional o comprado) solo se ve en Claude Console.

## Paquetes preparados y coste estimado por ejecución

Prueba sin API (`direct_analysis.py` sin `--execute-api`, Opus 5.5, esfuerzo `high`, con
todas las ramas del repositorio para la ceguera). «Cota» es la cota de entrada del
lanzador (un token por byte); «Reserva» es lo que hay que cubrir con `coste_maximo_usd`;
«Orientativo» es el coste esperado con lo observado en las 11 ejecuciones pagadas de Ahold,
Jumbo y Zoetis T1 (entrada real ≈ 0,40 × cota; salida ≈ 21 000 tokens, de 18 000 a
24 000), y en el cribado para los paquetes pequeños (≈ 0,45 × cota). Con Fable 5.2, el
doble.

| Manifiesto (`paquete`) | `empresa` | Corte | Cota (tokens) | Reserva USD | Orientativo USD | Estado sin API |
|---|---|---|---|---|---|---|
| `paquetes/ahold.json` | `ahold` | 2026-11-17 | 962 711 | 4,51 | 1,92–1,95 (real) | preparado |
| `paquetes/jumbo.json` | `jumbo` | 2026-11-17 | 814 919 | 3,92 | 1,76–1,84 (real) | preparado |
| `paquetes/zoetis.json` | `zoetis` | 2026-10-09 | 943 029 | 4,43 | 1,86–1,97 (real) | preparado |
| `paquetes/zoetis_t2.json` | `zoetis-t2` | 2026-11-05 | 955 377 | 4,48 | ≈ 1,95 | preparado |
| `paquetes/vinci.json` | `vinci` | 2026-10-10 | 955 094 | 4,48 | ≈ 1,95 | preparado |
| `paquetes/elis.json` | `elis` | 2026-11-05 | 924 126 (sin el control de solape) | 4,35 | ≈ 1,90 | **bloqueado por la ceguera** (abajo) |
| `paquetes/universo_fw_thorpe.json` | `fw-thorpe` | 2026-10-30 | 140 370 | 1,22 | ≈ 0,67 | preparado |
| `paquetes/universo_azkoyen.json` | `azkoyen` | 2026-10-30 | 135 585 | 1,20 | ≈ 0,66 | preparado |
| `paquetes/universo_betsson.json` | `betsson` | 2026-10-25 | 176 900 | 1,36 | ≈ 0,74 | preparado |
| `paquetes/universo_cocacola.json` | `cocacola` | 2026-10-30 | 146 450 | 1,24 | ≈ 0,68 | preparado |

- La `empresa` del workflow es la del manifiesto, con guion: `zoetis-t2` (el lanzador no
  admite guiones bajos en la empresa) y `fw-thorpe`.
- Paquetes nuevos, una ejecución de cada uno sin Elis: reservas 13,96 USD; orientativo
  ≈ 6,7 USD (con Elis, cuando se desbloquee: 18,32 y ≈ 8,6). Tres repeticiones de Vinci y
  de Zoetis T2, como en Ahold, Jumbo y Zoetis T1: ≈ 11,7 USD más.
- Los cuatro paquetes de examen nuevos rozan la cota de contexto (967 232 tokens de entrada
  como máximo con la salida de 32 768): por eso llevan selecciones de páginas declaradas.

### Cómo se hizo cada paquete (recetas reproducibles)

Cada paquete nuevo tiene su **receta** en `recetas/<paquete>.json`: de qué insumo sale
cada archivo (asset de la Release con su huella, o archivo de un commit fijado del producto
o de este repositorio), qué páginas, qué cabecera y qué ediciones declaradas. La receta
`recetas/zoetis.json` reproduce byte a byte el paquete ya fusionado de Zoetis T1 y sirve de
prueba del método. Para comprobar un paquete:

```
python3 -I automation/direct_analysis/preparar_paquete.py comprobar automation/direct_analysis/recetas/vinci.json \
  --insumos <carpeta con los assets de la Release> --repo auxiliar=<este clon> --repo producto=<clon de munger-v2>
```

Escribe `IGUAL` si regenera los mismos bytes. Necesita `pdftotext`/`pdfinfo` (poppler) y
`openpyxl` en el equipo de quien prepara; el workflow no la usa. Los PDF, HTML, XLSX y ZIP no
van a Git: se leen de la Release.

- **Vinci** (`recetas/vinci.json`): fecha de análisis de la etapa 1, 10-oct-2026, precio
  del 9-oct. Fuentes de la Release `fuentes-examen-20261118`: URD 2025 (páginas 4–18, 24–25,
  129–144 y 356–425) y semestral a 30-jun-2026 (3–30 y 35–72). Fuera: la información de
  los nueve meses del 22-oct-2026. Datos, extracto e historia del expediente `vinci/Vinci`
  del producto (`examen/expedientes-f1`, ee1ca6a); etapa 1 de `fuentes/etapa1-examen-20261117`
  (la versión 2 del 25-oct de la Release del universo no se usa). **Edición declarada**: de
  la copia de `datos_v63.md` se retira la sección «1 bis» (perímetro F1 y vara del foso
  P-FOSO, con remisiones a la gramática G4/G7), que es regla del personaje y no dato, y que
  además salta el control de solape; las etiquetas de C54 y C55 quedan neutras («(todo el
  capital)»), y de `datos_v63.md` y `fase1_v63.json` se retira el precio de contraste del
  14-oct, posterior al corte (revisión f8b2dfc, C1 y C2). Aviso: decisiones del inversor
  con fecha 23-oct (usan cifras hasta el 30-jun).
- **Zoetis T2** (`recetas/zoetis_t2.json`): los archivos del paquete del primer tiempo, con
  los mismos bytes, más el 10-Q del T3 (páginas 1 y 3–47), el comunicado (HTML a texto) y la
  presentación del 5-nov-2026, y la cotización hasta el 5-nov (82,11 USD; extracto de la
  transcripción de `mistral/examen-zoetis-t2`, sin las filas posteriores). Para caber en la
  cota sale el 10-Q del T1 y el del T2 queda en sus estados (páginas 3–9). **Edición
  declarada** (revisión f8b2dfc, O2): en las copias de `datos_v63.md` y `fase1_v63.json` el
  precio es el cierre del 5-nov (C37) y la capitalización se recalcula (C41 = 82,11 ×
  424,927535 = 34 890,8 mm); `datos_v63.md` abre con una nota: el resto del volcado y la
  etapa 1 son del primer tiempo, la etapa 1 se conserva sin cambios como hipótesis, y C42,
  C57, el estado técnico y la conciliación no se recalculan. La fila del 4-nov (89,2 USD)
  coincide en las dos transcripciones conservadas de la tabla de la empresa (la del extractor
  y la del expediente `zoetis_t1d`), pero no se ha podido contrastar con otra fuente; no se
  usa. Sin las frases de la guía retiradas en T1: si deben volver en T2, lo decide la
  persona responsable.
- **Elis** (`recetas/elis.json`): datos, extracto e historia del expediente `elis_f1`
  (`examen/expedientes-f1`, 8c5ee44), con C48 = 108; etapa 1 de la Release del universo
  (mismos bytes que el expediente); fuentes: los textos del expediente (URD 2025 y semestral
  2026, que no están como PDF en ninguna Release), la presentación del semestre y el
  comunicado de la conversión de la OCEANE. **Bloqueado**: el control de solape del lanzador
  lo rechaza (`SOLAPE_CON_MATERIAL_CIEGO`) por dos falsos positivos, textos de la etapa 1 o
  de los datos copiados después en material ciego: la ficha provisional del traspaso
  (`traspaso/resultado_20261117/registro/relevo_copia_base/ficha_provisional.json`, el párrafo
  B101, en la respuesta, la hoja Análisis y los datos) y una evidencia de revisión
  (`examen/revisiones/hoja_ef93699/evidencia_ronda2/fecha_del_precio_en_los_12.txt`, la
  cita del precio en los datos y la historia). El lanzador no tiene excepciones (las de
  `excepciones_ceguera.json` son solo del cribado). Para desbloquearlo hace falta una de
  dos decisiones: añadir al lanzador excepciones con huella y código exactos, como el
  cribado (cambio de código con revisión), o retirar de las copias esos párrafos (cambia la
  etapa 1 y la cita del precio). Tampoco entra el comunicado de ingresos del T3 2026
  (`q3_2026_revenue.pdf`): la etapa 1 cita su 9M-26, pero no está en el expediente del
  personaje.

### Segunda vuelta del universo

- `universo.py --release universo_etapa1.zip.zip --empresas A,B [--escribir]` prepara el
  paquete de etapa 1 de cada empresa con las comprobaciones del cribado (huella de la
  Release, lista blanca, empresas del examen fuera) y el mismo lector de XLSX: respuesta y
  cambios v2 byte a byte y las hojas del libro en CSV, con la fecha de corte = fecha de
  análisis de la hoja. Aplica antes las capas de ceguera y deja fuera, sin escribir nada,
  la empresa que no las pasa. El universo no trae fuentes oficiales: el análisis directo
  de estas empresas trabaja solo con la etapa 1.
- La lista de finalistas sale de `automation/screening/finalistas.py` con un criterio
  mecánico declarado (ver `automation/screening/FINALISTAS_tandas_1_3_y_pandora.md`). Con
  las tandas 1 a 3 y Pandora: FW_Thorpe (nivel 1), Azkoyen, Betsson y CocaCola (nivel 2).
  Cuando lleguen las tandas 4 a 6, se vuelve a ejecutar con sus ejecuciones y se preparan
  los paquetes de las finalistas nuevas.

## Qué no hace

- No reintenta. No usa modelo de reserva (*fallback*): sería otra llamada a otro modelo.
- No recorta ni resume el paquete.
- No decide si el análisis es bueno: eso es la revisión a ciegas (`RUBRICA_EXAMEN.md` §10).
- No ejecuta el personaje, no cambia el producto, no acepta ni integra nada, no
  acredita aptitud para dinero real.
- No garantiza que el modelo no use su memoria: lo prohíbe el encargo y las citas
  literales ayudan a detectarlo, pero hay que revisarlo.
- La ceguera se comprueba contra el material de este repositorio. Las salidas del
  personaje que solo están en el repositorio del producto (`fase_a.json`, `informe.md`…)
  se paran por la lista blanca y por el nombre, no por su contenido. Elegir bien los
  archivos sigue siendo responsabilidad de quien hace el manifiesto.
- El control de solape puede dar un falso positivo si una fuente legítima comparte un
  párrafo largo con el material ciego. Entonces se para sin coste y el error dice con
  qué archivo coincide.

## Límites conocidos

- La salida máxima es 32 768 tokens y el stream de AUTO1 se corta a los 720 s. Un
  esfuerzo `max` con un paquete grande puede agotar cualquiera de los dos: el
  resultado se paga y queda no aceptado.
- Salidas estructuradas: con este esquema la API respondió 400 «The compiled grammar is
  too large» (ejecución 44288081039; un 400 no se cobra). Desde 08fa48f no se envía
  `output_config.format`: el esquema va al final del encargo y la respuesta se valida
  aquí (`check_schema`, claves duplicadas rechazadas, `null` → 0 solo con
  `disponible` = false y anotado). Un fallo de forma se paga y queda no aceptado; la
  salida en bruto (`raw_model_output`) se conserva para revisarla fuera de línea con
  decisión humana. La huella del sistema enviado es `system_sha256`. Si el uso trae una facturación no prevista, el estado de coste queda
  `INCIERTO_SIN_COTA` y bloquea nuevas reservas hasta reconciliarlo.
- La exclusión mutua es entre ejecuciones de este workflow. Otro workflow de AUTO1
  que reserve a la vez podría pasar la misma comprobación del tope.

## Probar sin gastar

```
python3 -I -m unittest discover -s automation/direct_analysis -p 'test_*.py' -v
```

Las pruebas simulan la API y la rama de registro; no abren red. `test_paquetes.py` arma
cada manifiesto de `paquetes/` del commit actual como en `preparar` (huellas, rutas, cota de
contexto y reserva por debajo de 5 USD) y prueba las recetas y el generador del universo; la
ceguera con todas las ramas la comprueba `preparar` en el workflow.

## Respuesta partida en bloques y revalidación fuera de línea

- Desviación declarada frente a AUTO1 (que rechaza varios bloques): si la respuesta llega
  como varios bloques ```json **sin texto entre ellos y sin claves repetidas**, se unen y se
  anota `objeto_json_partido_en_N_bloques_unido`; la unión pasa `check_schema` completo
  (ejecución 44290314915: un único objeto cortado en 12 + 3 claves).
- `revalidar.py REPORT.json SOURCES.json DIR` revalida sin red una salida pagada y publicada.
  Solo admite rechazos de **forma** (`JSON_INVALIDO`), exige que `SOURCES.json` sea el paquete
  enviado (`bundle_sha256`) y marca el resultado `REVALIDADO_FUERA_DE_LINEA_PENDIENTE_DECISION_HUMANA`
  con `accepted`/`integrated`/`product_executed` = false. No toca la reserva ni el tope.

