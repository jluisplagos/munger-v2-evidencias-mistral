# Revisión crítica independiente · modo cribado por tandas (40dbfd9, 86b2e24)

- **Repositorio:** `jluisplagos/munger-v2-evidencias-mistral`.
- **Rama:** `automatizacion/cribado-tandas`, cabeza `86b2e242139c376757d7dd6aa951a648f108207a` (y `40dbfd9`), sobre `main` `e1d5f4b`.
  - La rama no entra en el refspec local de `origin`; `git ls-remote` da el mismo SHA.
  - Worktree propio, desacoplado en `86b2e24`: `/home/user/e_work/wt_rev_cribado`, árbol limpio, borrado al terminar.
- **Diff revisado** (`git diff e1d5f4b 86b2e24`):
  - `automation/screening/`: `screening.py`, `ENCARGO_CRIBADO.md`, `excepciones_ceguera.json`, `README.md` y `test_screening.py`;
  - `.github/workflows/cribado-universo.yml`;
  - `automation-tests.yml`: añade la rama al disparo por push y dos baterías de pruebas;
  - `test_auto1_workflows.py`: inventario y plazo.
- **Contexto leído:**
  - AUTO1: `critical_review.py` y `pilot.py`;
  - `direct_analysis.py` y su README;
  - `REORIENTACION_UNIVERSO.md` §4–§6;
  - `DECISIONES_PARA_EL_USUARIO.md` (F1-A/B, P-O1, P-O2, P-FOSO, D-US1/2, D-WM);
  - `PLAN_TRES_FRENTES.md` (A5/A6);
  - las revisiones anteriores del lanzador y el dictamen de perímetro G4.
- **Revisor:** agente distinto del autor (Claude Opus 5.5).
  - No he cambiado la rama ni hecho commit, y no he hecho ninguna llamada a la API de Anthropic.
  - Solo he hecho lecturas en la API de GitHub: el listado de la rama de registro y la visibilidad del repositorio.
  - Para reproducir el material ciego que verá Actions, usé un clon desnudo temporal con todas las ramas del origen, en el scratchpad.

## Veredicto: CORRECCIONES (acotadas)

**El control de gasto es conforme.**
- Hay una sola aprobación por tanda y una llamada por empresa, sin reintentos.
- Los tres topes (por empresa, por tanda y acumulado) se comprueban antes de cada llamada, con la reserva create-only y el registro de AUTO1.
- No encontré ningún camino por el que una tanda pase de su máximo: ni por concurrencia, ni por «Re-run», ni por un fallo de publicación.

**La ceguera del paquete es conforme.**
- El paquete sale solo de la Release fijada, con una lista blanca estricta.
- En el universo real no lleva material del examen. Lo comprobé también con las 45 ramas del origen.
- El dry-run se reproduce byte a byte.

**Antes de las tandas de 20 hacen falta tres correcciones:**
- **H1 · Límite de la API de GitHub.** El registro se recorre entero tres veces por empresa, y el límite del `GITHUB_TOKEN` corta la tanda. La tanda se para sin gastar de más, pero no se cumple «una aprobación por 20» y algunos resultados pagados quedan a medio publicar.
- **H2 · Arrendamientos.** «Arrendamientos siempre» es política no decidida. Además, tal como está escrita, deja contar el alquiler dos veces en el cociente deuda/caja libre.
- **H3 · Empresas del examen.** Hay que aplazar las seis, Elis incluida, hasta cerrar la evaluación con la rúbrica.

Lo demás son mejoras menores.

**La tanda de prueba de una empresa puede lanzarse ya**, como prueba técnica, con una empresa que no sea del examen (§4). Si después cambia el encargo, su veredicto no cuenta para A6.

## Hallazgos

### H1 · Alta (operativa; sin riesgo de gasto) · La tanda de 20 no cabe en el límite de la API de GitHub

**Cuántas llamadas hace.** Por cada empresa, el código recorre la rama de registro completa tres veces:
1. `register_exposure`, para el máximo de la tanda;
2. `admit(MAX_USD)`, la comprobación previa de `cr.run`;
3. `admit` con la reserva exacta, dentro de `Receipt.reserve`.

Cada recorrido hace dos listados y un GET de `reservation.json` por cada carpeta. En total, por empresa salen unas **3·D + 17 llamadas**, donde D es el número de carpetas del registro:
- hoy, D = 12: 10 en `reviews/` y 2 en `claude_review/results/`;
- cada empresa añade una carpeta, y cada tanda otra más.

Lo simulé con las dobles de prueba (`GitHubStore`, 20 empresas, sin red):

| D al empezar la tanda | Llamadas a GitHub en la tanda |
|---|---|
| 12 (hoy) | 1.630 |
| 60 (tras dos o tres tandas) | 4.510 |
| 120 (hacia el final del universo) | 8.110 |

**El límite.** El `GITHUB_TOKEN` de Actions tiene un límite primario de **1.000 peticiones por hora y repositorio**, según la documentación de GitHub. No pude abrirla desde esta sesión. El repositorio es personal, así que no se aplica el límite de Enterprise. Con ese límite:
- la primera tanda cabe o no según lo que tarde cada llamada;
- desde la segunda, no cabe.

**Qué pasa al llegar al límite** (respuesta 403 o 429). Lo comprobé con pruebas ad hoc:
- **Casi siempre** el corte llega en un recorrido previo. La tanda se para con `REGISTRO_NO_VERIFICABLE:GITHUB_HTTP_403` o con un código directo, sin reservar ni llamar.
- **A veces** llega al publicar, después de la llamada pagada. Queda `FALLO_TRAS_RESERVAR`: la tanda cuenta el máximo y se para.
  - `reservation.json` suele quedar con el coste, porque se publica el primero. Si el corte llega antes, queda la reserva previa, que es mayor que el coste: el tope sigue a salvo.
  - Pueden faltar `report.md` y `sources.json` de esa empresa.
  - El informe de la tanda no se publica (salida 2).

No hay sobrecoste. Pero cada parada exige otro «Re-run», con otra aprobación, después del reinicio horario. Con D ≈ 120 cabrían unas dos empresas por hora.

**Corrección.** Toca AUTO1, así que debe revisarla otro agente:
- **Opción a.** Que `Register.committed()` guarde en memoria la exposición de cada carpeta según el SHA de árbol que trae el listado, y solo lea las carpetas nuevas o cambiadas. Ese SHA depende del contenido, así que no puede quedar obsoleto.
- **Opción b.** Usar la API de árboles (`git/trees/<rama>?recursive=1`) y leer los blobs por su SHA.
- **Además, en `screening.py`:** leer una sola vez lo comprometido por los intentos anteriores y sumarle lo local.

Así cada empresa bajaría a unas 20 llamadas. Mientras tanto, tandas pequeñas: hoy unas 12 empresas por hora; con D = 60, unas 4.

### H2 · Media · «Arrendamientos siempre» no es una decisión de la persona y, como está escrito, cuenta el alquiler dos veces

**Qué está decidido.** `REORIENTACION_UNIVERSO.md` §4.3 deja abierto «siempre, o nunca, en coherencia con F1», y es una opinión del coordinador. Lo que sí decidió la persona apunta a otra cosa: contar el alquiler **una sola vez y en el flujo**.
- **F1-A** fija la reinversión en el perímetro A2_propio. El dictamen de perímetro lo resume así: «el alquiler entra una vez».
- **P-FOSO** dice que el capital del local es del casero.
- **D-WM** trata como deuda los arrendamientos financieros que no se desglosan, y entonces sus pagos no se restan de la caja.
- **D-US1 y D-US2** tratan el arrendamiento operativo dentro del flujo de explotación.

Ninguna de esas decisiones fija «siempre» para el apalancamiento del cribado. El README lo reconoce: «la convención que propone el autor». Es política económica no decidida (CLAUDE.md; DECISIONES, arrendamientos).

**La redacción no evita la doble cuenta.** El encargo dice: «la deuda incluye los pasivos por arrendamiento… y la caja libre no resta dos veces los pagos». Pero las hojas de etapa 1 ya restan esos pagos en la caja libre. En la hoja de Ahold:
- `Análisis!C52` = 1.999,4 es la caja libre, ya descontado el principal de arrendamientos de `C49` (1.834);
- `C54` = 19.261 es la «deuda bruta con arrendamientos»; sin ellos sería unos 6.978–7.004, según `Control maestro`.

| Cociente | Resultado | Lectura |
|---|---|---|
| Deuda neta con arrendamientos / caja libre (el encargo lo admite): (19.261 − 3.196) / 1.999,4 | ≈ 8,0x | Cuenta el alquiler dos veces |
| Deuda neta sin arrendamientos / la misma caja libre | ≈ 1,9x | Coherente con esa caja |
| Deuda/EBITDA NIIF 16 de la propia hoja (`C33`) | 2,2153 | Coherente |

Es justo el error que el examen persigue en Ahold, y afectaría a cualquier arrendatario: Inditex, Petsathome, Chewy, Pandora…

**Corrección:**
1. **Declararlo en cada resultado.** Añadir una línea fija en cada `report.md` y en `tanda.md`, escrita por el código y no por el modelo: «Hipótesis del cribado no decidida: arrendamientos como deuda (NIIF 16)».
2. **Regla de emparejamiento en el encargo**, que no elige política:
   - si la deuda incluye los arrendamientos, se compara con el EBITDA NIIF 16 o con una caja libre antes de los pagos por arrendamiento;
   - si se usa la caja libre de la hoja, que ya los resta, la deuda va sin arrendamientos;
   - `dato_clave` dice cuál de las dos se usó.
3. **Llevar la elección a la cola de decisiones de la persona:**
   - (a) siempre, como en la NIIF 16;
   - (b) como en F1/A2_propio.

   Hasta que decida, el filtro de balance de los arrendatarios queda condicionado.

Cambiar el encargo cambia su huella: conviene hacerlo antes de las tandas.

### H3 · Media · Aplazar las seis empresas del examen, Elis incluida, hasta cerrar C13 y C14

`PROPUESTA_TANDAS.md` mete en las tandas a todas las del examen: Ahold en la 1, Elis en la 2, Jumbo en la 3, y Vinci, WasteManagement y Zoetis en la 6.

**Por qué aplazarlas:**
1. **Sería un tercer veredicto, no previsto, sobre las empresas del examen.**
   - Quedaría en un repositorio **público** y en la rama de registro.
   - Estaría ahí antes de la evaluación con la rúbrica (C13) y del veredicto final (C14), con riesgo de anclaje para el coordinador y los evaluadores.
2. **El encargo convierte en reglas generales las trampas del examen** (§5 de la reorientación):
   - Waste Management: «excelente y caro es `vigilar`»;
   - Zoetis: «hoja anterior a resultados»;
   - Vinci: «concesiones… suma de partes»;
   - Ahold: arrendamientos;
   - Elis: «`faltan_datos`… no te la inventes».

   Por eso, su cribado no sirve como referencia independiente ni se puede comparar con el personaje.
3. **No es la misma etapa 1.**
   - En la Release, Jumbo, Vinci y Zoetis están en su **v2**: los cambios del 25-oct, con `Análisis!C97` y otras celdas distintas (4, 5 y 2 celdas).
   - El examen usa la **v1**, la de `fuentes/etapa1-examen-20261117`. El paquete del análisis directo de Jumbo, por ejemplo, lleva `C97` = «Vendiendo».
   - WasteManagement sí coincide.
4. **Elis necesita dos excepciones de ceguera** (H5), y lo que se le examina es justamente «faltan datos».
5. **Aplazar no cuesta nada.** Esas empresas ya se estudian a fondo, con el personaje y tres análisis directos, y el cribado no añade información para A6. Se ahorran unos 2,74 USD orientativos (7,32 en cotas).

**Cómo hacerlo:**
- **Elis:** borrar sus dos entradas de `excepciones_ceguera.json`. Elis pasa a `NO_PREPARADA`, sin coste.
- **Las otras cinco:** una lista fija en el código, mejor que dejarlas fuera a mano. El propio diseño dice que «no se elige a mano qué se manda».
- **La propuesta:** rehacerla con 111 empresas.

Después del 23-nov se pueden cribar. Es un aplazamiento, no una reducción de alcance; lo confirma el coordinador o la persona.

### H4 · Media-baja · No hay parada por respuestas pagadas e inválidas seguidas

**El fallo.** `consecutive` solo cuenta los resultados `INFERENCIA_SIN_VEREDICTO_COSTE_INCIERTO`. Un `RESULTADO_NO_ACEPTADO_NO_REINTENTAR` (pagado, pero con la forma o el esquema inválidos) lo vuelve a cero.

**El riesgo.** Con `gramatica = no`, un fallo sistemático de forma haría pagar las 20 empresas, unos 9 USD, sin ningún resultado útil. Por ejemplo, un `null`, una clave con otra mayúscula o texto entre bloques. Además, `revalidar.py` solo sirve para el esquema del análisis directo.

**Corrección:** parar tras dos rechazos pagados seguidos y añadir una revalidación fuera de línea con el validador del cribado. Con la gramática (§4), el riesgo casi desaparece.

### H5 · Baja · Excepciones de ceguera: contenido seguro, motivo de Elis inexacto y cobertura de «primer acierto»

**Andina y Petsathome: seguras.**
- Usan «rúbrica» en sentido contable: una vez en Andina («tres rúbricas» del patrimonio) y seis en Petsathome («rúbrica literal» del estado de flujos).
- Ninguna menciona el informe crítico.
- Cada excepción está ligada a la huella exacta del archivo.

**Elis: segura en el contenido, con el motivo mal descrito.**
- El solape es con `traspaso/…/relevo_copia_base/ficha_provisional.json`. Es el texto de la propia persona, que la ficha cita como `"antes"` en **tres** celdas: B66, B101 y B102, con unos 238, 702 y 1.345 caracteres.
- En los tres casos el texto va precedido de `"antes": "`, y ningún `"después"` aparece en el paquete.
- La dirección que da el motivo se sostiene: el texto va de la etapa 1 al traspaso.
- Lo que falla es la extensión. El motivo dice «unos 460 caracteres… B101… el resto de la respuesta no solapa», y el README repite lo mismo. No es exacto.

**El mecanismo de la excepción.**
- `da.overlap` devuelve solo el **primer** archivo con el que solapa el texto. Una excepción para ese archivo taparía un solape posterior del mismo texto con otro material ciego.
- Hoy no lo hay. Con las 45 ramas del origen solo aparece la ficha, y el resultado es el mismo que en local: 117 empresas preparadas de 117 y las mismas cuatro excepciones.
- El código `CONTENIDO_PROHIBIDO` tampoco dice qué marca saltó.

**Corrección:**
- calcular todos los archivos con los que solapa y exceptuar solo ese conjunto;
- guardar qué marca saltó;
- corregir el motivo de Elis, si al final no se aplaza.

### H6 · Baja · Lo que cada resultado no declara

- **La fecha de la hoja.** Cada precio es el de la fecha de su hoja: de 7-oct a 15-nov-2026.
  - §4.4 pide «la hoja al día».
  - Ni `report.md` ni `tanda.md` muestran la «Fecha de análisis».
  - La cláusula «`dudoso` si la hoja es anterior a resultados que figuran en el paquete» casi nunca se activa: el paquete no trae resultados posteriores a la hoja.
- **Las decisiones posteriores a la etapa 1.** Las cifras son las de la etapa 1, sin P-O1 (regla espejo), P-O2, F1-A/F1-B, D-US1/2 ni D-WM.
  - Para un cribado está bien, pero ningún resultado lo dice.
  - Hay además una asimetría: se aplica una convención no decidida (H2) y no las que sí están decididas.

**Corrección:** añadir mecánicamente la fecha de cada hoja a su fila, y una línea fija con estas dos condiciones.

### H7 · Baja · Lectura de la hoja

- **Porcentajes.** Unas 110 celdas numéricas por hoja «Análisis» tienen formato de porcentaje y llegan como fracción: en Ahold, `C24` = 0.109 es un 10,9 %. El encargo no lo avisa.
- **Fechas.** La «Fecha de análisis» llega en formatos distintos: 108 en ISO, 7 como texto dd/mm/aaaa y 2 en otros formatos.
- **Juicios de la etapa 1.** El paquete lleva el «VEREDICTO GLOBAL», los semáforos (✓ PASA / ✗ BANDERA) y el «Tamaño de posición pensado» de la etapa 1, hechos con el embudo antiguo. El cribado podría heredarlos, cuando A6 existe precisamente para rehacerlos con el embudo corregido.

**Corrección:** una o dos líneas en el encargo: «los porcentajes vienen como fracción; los semáforos y el veredicto de la hoja son de la etapa 1, con otro embudo: no los heredes; si discrepas, dilo».

### H8 · Baja · Uso y registro

- El README dice «**1,6** basta», pero la entrada exige `1.6`. Con `1,6`, `preparar` la rechaza, sin coste.
- Un run nuevo con las mismas empresas vuelve a pagarlas: no hay aviso entre ejecuciones. `preparar` podría señalar las que ya están cribadas en el registro.
- Con varias tandas en cola, GitHub cancela la que espera en el mismo grupo de concurrencia. Conviene lanzarlas de una en una.
- En un «Re-run», `tanda.md` solo suma ese intento. Para A7 hay que sumar desde el registro.
- No hay un procedimiento escrito para reconciliar un `INCIERTO`, por ejemplo tras un 400 de gramática.
- Los 15 minutos de margen antes del timeout se cuentan desde el inicio de `run_batch`, no del job. Además, los recorridos del registro pueden pasar de los 120 s previstos.

### Límites declarados (no bloquean)

- **Tope acumulado.** Otro workflow de AUTO1 con otro grupo de concurrencia (la revisión crítica, el piloto o los grupos Qwen) puede pasar la misma comprobación a la vez. Lo declara el README.
- **Repositorio público.** Cada empresa publica en Git (rama de registro) su `sources.json`, con el texto de la etapa 1 de la persona, y la salida del modelo; los artefactos también. La Release ya es pública, pero del historial de Git es difícil borrar algo.
- **Listados de 1.000 entradas.** La API de contenidos lista como mucho 1.000 entradas por carpeta. Es un límite latente de AUTO1 para el tope acumulado.
- **El informe crítico.** Es un PDF, así que el control de solape no ve su texto. Lo comprobé aparte: ninguna de las fuentes de las 117 empresas comparte 130 caracteres seguidos (normalizados) con el texto extraído con pdftotext.
- **Vocabulario de la etapa 1.** Los paquetes reales llevan «Munger» (159 fuentes) y «personaje» (25), propios de la plantilla y de la etapa 1. No es una fuga. La prueba que lo descarta solo mira la Release sintética.

## Comprobaciones pedidas

### 1. Gasto — conforme (H1 es operativo)

**Una sola aprobación por tanda.**
- El job `cribado` está protegido por el environment `inferencia-aprobada`.
- `preparar` y `tests` no tienen secretos, y `preparar` muestra las reservas antes de aprobar.
- Un «Re-run» pide otra aprobación.

**Una llamada cobrable por empresa, sin reintentos.**
- `GET /v1/models` y `count_tokens` son gratis.
- Antes de llamar se publica la reserva create-only. Si ya existe `reservation.json`, la empresa queda `YA_RESERVADO_SIN_NUEVA_LLAMADA`.
- Ni urllib ni el bucle reintentan.

**Topes comprobados antes de cada llamada.**
- **Por empresa:**
  - `parse_usd` no deja pasar de 2;
  - `preflight` acota por bytes;
  - `cr.budget` usa el conteo real. Si se pasa, salta `RESERVA_SUPERA…` y solo afecta a esa empresa.
- **Por tanda:**
  - `parse_usd` no deja pasar de 30;
  - lo comprometido más el máximo por empresa no puede superar el máximo de la tanda. Lo comprometido es el mayor de dos valores: lo local, o lo que hay en el registro con el prefijo `cribado-<run>-`, todos los intentos. Es un cálculo conservador.
- **Acumulado:**
  - `admit(MAX_USD)` y luego `admit` con la reserva exacta, antes del PUT create-only;
  - sin la variable del environment no se llama.

**Concurrencia.** El job comparte grupo con el análisis directo. La tanda no puede pasar de su máximo; el tope acumulado tiene la carrera ya declarada.

**«Re-run».** Lo ya reservado no se repite, y los intentos anteriores cuentan para el mismo máximo. Lo muestran la prueba del autor y un escenario propio.

**Fallo de publicación.** Después de reservar, cuenta el máximo y para.

**Facturación no prevista.** `INCIERTO_SIN_COTA` para la tanda y bloquea el registro.

**Escenarios propios.** Todos terminan en una parada segura:
- coste sin cota;
- registro que responde 403: ninguna llamada;
- 403 al publicar, tras la llamada pagada: la reserva queda con el coste y falta `report.md`;
- «Re-run» posterior: no repite la empresa pagada.

**El informe de tanda sin `reservation.json` no deja fuera ningún gasto real.** No es gasto, y cada llamada pagada tiene su propia reserva, creada antes y actualizada después. Solo añade un GET por recorrido (H1).

### 2. Seguridad y ceguera — conforme en el contenido (con H3 y H5)

**Release fija.** El código comprueba su tamaño y su SHA-256, y los dos jobs la descargan. La huella coincide. Las 117 huellas de libro y los conjuntos de archivos coinciden con `INDICE.tsv`.

**Lista blanca estricta.**
- En la carpeta de cada empresa solo valen tres nombres.
- Cualquier otro archivo invalida la Release entera; también una ruta rara, un enlace, un cifrado, un duplicado o un nombre ambiguo.
- Del libro solo van dos hojas, sin macros ni binarios.
- El XML se lee sin DTD ni entidades, y con lectura acotada.

**Ceguera.** Se aplican las capas del análisis directo:
- huella exacta de cualquier blob ciego, en cualquier rama;
- las marcas «rúbrica» e «informe crítico»;
- solape de 400 caracteres.

En Actions (`fetch-depth: 0`) el material ciego es algo mayor que en local: 496 blobs frente a 488. Con las 45 ramas del origen salen igualmente 117 empresas preparadas de 117 y las mismas cuatro excepciones. El encargo no contiene ninguna marca, y no comparte 40 caracteres seguidos (normalizados) con la rúbrica, el contradictor, la reorientación ni la lectura del informe.

**Excepciones.** Son seguras (H5). A Elis conviene aplazarla (H3).

### 3. Encargo — corrección en H2; lo demás, conforme

**Lo que aplica bien de la reorientación:**
- el orden del embudo: calidad → caja → balance → precio → encaje;
- distingue «el negocio no se entiende» de «el DCF de la plantilla no aplica» (§4.2);
- el límite de deuda depende de la estabilidad del negocio (§4.3);
- el precio, al 9 % provisional y con ±1–2 puntos;
- el encaje va al final y nunca elimina, porque el paquete no trae la cartera (§1 y §4.1);
- las financieras van a `demasiado_dificil`.

**Evita recomendaciones y tamaños de posición.**
- La enumeración del veredicto no tiene «comprar».
- El encargo prohíbe tamaños y órdenes.
- El esquema rechaza claves extra.
- Los informes dicen que no es una recomendación.

Queda un resto: los textos libres podrían repetir el tamaño o el precio de Sí de la hoja (fila 104), que van en el paquete. No hay aviso mecánico para eso.

**Política no decidida:**
- arrendamientos: H2;
- los ejemplos de motor («caja después de las adquisiciones», «ciclo medio») son descriptivos y no cambian cifras. Aun así, conviene decir que no son decisiones: F1-B trata las compras de empresas como crecimiento.

### 4. Robustez de la respuesta — con gramática, tras una tanda de una empresa

**El esquema es pequeño:** 2.182 caracteres, 7 objetos y 7 enumeraciones, solo cadenas, sin `anyOf` ni números. Todo lo que usa lo admiten las salidas estructuradas, que funcionan con el razonamiento adaptativo de Opus 5.5.

**El 400 anterior.** El error «grammar too large» vino de un esquema mucho mayor. `count_tokens` no compila la gramática, así que un 400 llegaría después de reservar. No se cobra, pero la reserva queda `INCIERTO` hasta reconciliarla.

**Sin gramática** siguen abiertos los rechazos pagados: un `null`, claves con otra mayúscula, saltos de línea sin escapar, texto entre bloques.

**Recomendación: sí, primero una tanda de una sola empresa** que no sea del examen. Por ejemplo, Pandora o Inditex: son arrendatarias (sirven también para ver H2) y su cota es de 1,17–1,18 USD.

Valores de la prueba:
- `coste_maximo_por_empresa_usd = 1.6`;
- `coste_maximo_tanda_usd = 2`;
- `gramatica = si`;
- Opus 5.5, esfuerzo `high`.

Qué comprobar en el resultado:
- el estado;
- `model_returned` = `claude-opus-5-5`, y los campos de facturación;
- los tokens reales frente a la cota y al orientativo;
- lo que tarda la llamada;
- que se publiquen el informe de la empresa y el de la tanda.

Según el resultado:
- **Si da 400:** reconciliar la reserva y repetir con `gramatica = no`.
- **Si funciona:** usar `si` en todas las tandas, sin quitar la validación local.

Después, una tanda de 3–5 empresas para medir tiempos y llamadas a GitHub antes de subir el tamaño (H1).

### 5. Pruebas como CI — conforme

Orden: `python3 -I -m unittest discover -s automation/<dir> -p 'test_*.py'`, en el worktree de `86b2e24`, con Python 3.13.18 y PyYAML 6.0.1.

| Carpeta | Pruebas | Resultado |
|---|---|---|
| `claude_review` | 49 | OK |
| `coordination` | 97 | OK |
| `direct_analysis` | 48 | OK |
| `screening` | 35 | OK |

En total, 229 pruebas, ninguna omitida, y el árbol queda limpio.

Faltan pruebas para tres caminos, que comprobé ad hoc fuera del repositorio:
- la parada `REGISTRO_NO_VERIFICABLE`;
- `COSTE_SIN_COTA`;
- un 403 o 429 de GitHub a mitad de tanda.

Las pruebas de workflow se omiten si el runner no tiene PyYAML.

## Verificaciones propias (reproducibles)

- **Dry-run reproducido.** `screening.py cotas` con la Release y `86b2e24` da un `cotas.json` idéntico byte a byte al del autor:
  - 117 empresas preparadas;
  - 142,187376 USD en cotas y 53,2699 USD orientativos;
  - la cota mayor es la de Parex (1,513684 USD) y la menor la de Campine (1,126048 USD).
- **Material ciego como en Actions.** Con el clon desnudo de las 45 ramas, `blind_material` tarda 3,1 s y preparar 20 paquetes, 1,6 s. Al job `preparar` le sobra tiempo dentro de sus 10 minutos.
- **Llamadas a GitHub.** Simulé una tanda de 20 empresas con D = 12, 60 y 120 (H1), y los escenarios de parada de §1.
- **Solapes revisados:**
  - Elis frente a la ficha, bloque a bloque;
  - Andina y Petsathome, por el contexto de la palabra;
  - el encargo frente a la rúbrica, el contradictor, la reorientación y la lectura del informe;
  - las 117 empresas frente al texto del informe crítico (pdftotext).
- **Hojas.** Los 117 libros tienen las mismas cuatro hojas, los porcentajes llegan como fracción y las fechas de análisis van de 7-oct a 15-nov-2026.
- **Etapa 1 del examen frente a la de la Release.**
  - Jumbo, Vinci y Zoetis no coinciden: v1 en el examen, v2 en la Release.
  - WasteManagement coincide.

## Ronda 2 · 833cd50

- **Qué se revisa.** La rama `automatizacion/cribado-tandas` en `833cd50a9bba34006519119c72a29c70a1656fb7`, rebasada sobre `main` `e96470e`.
  - `ab955cd` y `ec81ece` son el rebase puro de `40dbfd9` y `86b2e24`: los archivos del cribado son idénticos.
  - `5e8d4b9` trae el código y `833cd50` solo cambia el README.
- **Decisiones de la persona aplicadas:** C-ARR y C-EX (`DECISIONES_PARA_EL_USUARIO.md`, en `2bc918e`).
- **Cómo se revisó.** Worktree propio, desacoplado (`/home/user/e_work/wt_rev_cribado2`), borrado al terminar. Sin cambios en la rama, sin commit, sin llamadas a la API de Anthropic.

### Veredicto ronda 2: CONFORME CON LÍMITES

H1–H4 están cerrados, y H5–H8 también, salvo la revalidación fuera de línea, que queda como límite declarado en el README. No hay regresión de gasto ni de ceguera. La tanda 0 (Pandora) puede lanzarse.

### H1–H4: cerrados

**H1 · Llamadas a GitHub.** Una tanda de 20, simulada con listados que traen el SHA de cada carpeta según su contenido:

| Carpetas en el registro | Ronda 1 | Ronda 2 |
|---|---|---|
| 12 | 1.630 | 333 |
| 60 | 4.510 | 381 |
| 120 | 8.110 | 441 |

Coincide con el autor y queda muy por debajo de 1.000 por hora. Detalles:
- El SHA del listado real es el SHA de árbol de Git. Lo comprobé en la rama de registro: el listado y `git ls-tree` dan el mismo valor. Por eso cualquier cambio de contenido obliga a releer.
- Sin SHA, el código vuelve a leerlo todo: 1.174, 3.142 y 5.602 llamadas. La API real sí lo trae.
- Lo comprometido por intentos anteriores se lee una vez y se le suma lo local. Las empresas ya reservadas aportan 0 en local, así que no se cuentan dos veces.

**H2 · C-ARR aplicado.**
- El encargo cuenta el alquiler una vez, en el flujo.
- La deuda y sus cocientes se miden sin arrendamientos, contra un EBITDA que ya resta el alquiler.
- Un cociente NIIF 16 de la hoja no se usa tal cual: o se recalcula, o queda `dudoso`.
- El pasivo va aparte, en `pasivo_arrendamientos` (esquema de 2.252 caracteres, 9 claves).
- La convención y las condiciones van en el paquete y, como líneas fijas del código, en cada `report.md` y en `tanda.md`.

Con eso desaparece la doble cuenta del ejemplo de Ahold. En una muestra de hojas con US GAAP (Chewy, Nike, Quanta, CocaCola…), la plantilla ya resta los pagos del arrendamiento operativo (dentro del CFO) y, cuando lo hay, el principal del financiero (`C49`). La deuda sin arrendamientos es, por tanto, coherente.

**H3 · C-EX aplicado.**
- Hay una lista cerrada en el código, verificada por bytes contra el SHA: las seis empresas del examen quedan `NO_PREPARADA:EMPRESA_DEL_EXAMEN_EXCLUIDA_HASTA_DESPUES_DEL_23_NOV`, también si se escriben a mano.
- Las excepciones de Elis se han retirado.
- El dry-run se reproduce byte a byte: 111 empresas, 135,588848 USD en cotas y 50,7365 orientativos.

**H4.** La tanda se para tras dos `RESULTADO_NO_ACEPTADO_NO_REINTENTAR` seguidos. Si entre dos rechazos hay una respuesta válida, sigue.

### Gasto, sin regresión

Repetí los escenarios de la ronda 1 con el código nuevo y listados con SHA:

| Escenario | Resultado |
|---|---|
| Facturación no prevista | Para, con 1 llamada |
| Registro con 403 | Para, sin ninguna llamada |
| 403 al publicar tras la llamada pagada | `FALLO_TRAS_RESERVAR`; el «Re-run» no la repite |
| Máximo de la tanda con un intento anterior, incluida una reserva create-only sin actualizar | No se supera |
| Tope acumulado bajo | Para antes de llamar |
| Dos respuestas pagadas inválidas | Para |
| `INCIERTO_SIN_COTA` ya en el registro | Bloquea la tanda siguiente: la caché no lo oculta, porque no se guarda |

### Ceguera, sin regresión

- Con las 46 ramas del origen (498 blobs) salen 111 empresas preparadas y 6 excluidas.
- Solo se aplican las excepciones de Andina y Petsathome, con su nuevo código, que nombra la marca: `…:hoja_control_maestro:rubrica`.
- Ningún paquete lleva el nombre del repositorio, motivos de excepción ni rutas del traspaso.
- Los 111 paquetes llevan su `fecha_hoja`, en ISO o como texto: «25.10.2026», «25-oct-2026».
- El encargo nuevo no tiene marcas ni solapes. El tramo común más largo con la rúbrica es de 31 caracteres normalizados, y con el contradictor, de 22.

### Tanda 0

Reproducida sin API: Pandora `PREPARADO_SIN_API`, reserva de 1,183068 USD con gramática, hoja del 2026-10-25.

### Pruebas como CI

`python3 -I -m unittest discover -s automation/<dir> -p 'test_*.py'`:

| Carpeta | Pruebas | Resultado |
|---|---|---|
| `claude_review` | 49 | OK |
| `coordination` | 97 | OK |
| `direct_analysis` | 48 | OK |
| `screening` | 41 | OK |

En total, 235 pruebas, ninguna omitida, y el árbol queda limpio.

### Límites que quedan (no bloquean)

- **Revalidación fuera de línea:** no la hay para el esquema del cribado (declarado). Con la gramática y la parada de H4, como mucho se pierden dos respuestas pagadas por tanda.
- **«Re-run» con el máximo alcanzado:** una empresa ya reservada puede figurar como `NO_LLAMADA_TANDA_PARADA` en vez de `YA_RESERVADO_SIN_NUEVA_LLAMADA`. Es cosmético, sin gasto.
- **Tope acumulado:** sigue la carrera con otros workflows de AUTO1 de otro grupo de concurrencia (declarada).
- **C-EX:** vence después del 23-nov y exige un cambio de código revisado.
