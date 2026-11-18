# Plan de los tres frentes · del 18-nov (tarde) al 20-nov (restablecimiento)

**Objetivo:** gastar en trabajo útil, no en relleno, el crédito de API (unos 197 USD), el de Mistral (unos 200 €) y el uso semanal de Claude, y llegar al **23-nov con el veredicto del examen** («Sí, con poco», «Todavía no» o «No, para»), con calidad suficiente para poco dinero real junto con tu propia investigación.

**Reglas que no cambian:** la tasa del 9 % es provisional; tus decisiones son las registradas; ninguna salida se edita a mano; cada pieza la revisa alguien distinto de su autor, con dos rondas como máximo; LibreOffice va de una tarea en una.

**Reparto de modelos:**
- **Claude Fable**, hoy y mañana sin tope: revisiones, reparaciones, el contradictor de cada empresa y las auditorías.
- **Claude Opus**: las fases del personaje (A, B y C).
- **Claude Sonnet**: extraer cifras.
- **Mistral**: volumen y la mirada de otra familia de modelos.
- **API**: el análisis directo y el cribado del universo.

Leyenda: 👤 = lo haces tú · 🤖 = lo hago yo (Claude) · 🟠 = Mistral · 💳 = gasta crédito de API.

---

## 0 · Lo primero, por orden (👤 unos 40 minutos en total)

### 0.1 · Restablecer tu uso de Claude
- [ ] Como sabes hacerlo. Avísame con un «listo».

### 0.2 · Ver tu saldo de API y su caducidad (2 minutos)
1. Abre https://console.anthropic.com e inicia sesión.
2. Menú de la izquierda → **Settings** → **Billing**.
3. Apunta dos datos: el **saldo** («Credit balance») y la **fecha de caducidad** de los créditos, si aparece.
4. Escríbeme los dos aquí.

### 0.3 · Subir los PDF que tienes a una Release (15–20 minutos)
Sirve para todos los PDF de todas las empresas: los que tengas en tu ordenador, los que descargues de Jumbo y de Zoetis, y la carpeta `munger_fuentes_examen` de Mistral, si está en tu ordenador.
1. **Jumbo**, desde tu navegador. Abre la página de informes de Jumbo: https://corporate.e-jumbo.gr/en/investor-relations/financial-statements/group-parent/etisies-oikonomikes-katastaseis/
   - Descarga los **informes anuales en inglés** de los ejercicios 2025, 2024, 2023, 2022, 2021 y 2020, el de transición de 2019 y los de 2018/19, 2017/18 y 2016/17. Los antiguos están en la página 2: el enlace «2» al final de la lista.
   - Descarga además el semestral de 2026: https://corporate.e-jumbo.gr/uploads/159323/eaf6_jumbo_h1financialresults2026_en.pdf
2. **Zoetis**, desde tu navegador. Abre https://investor.zoetis.com → **Financials** → **SEC Filings**.
   - Descarga el **10-Q del segundo trimestre de 2026** (presentado el 6-ago-2026) y el **del tercero** (5-nov-2026), en PDF. Suele haber un icono de PDF a la derecha de cada fila.
3. **La carpeta de Mistral:** busca en tu ordenador una carpeta llamada `munger_fuentes_examen`. Si no la encuentras, pregúntale a Mistral en su ventana «¿En qué ruta exacta guardaste munger_fuentes_examen?» y dime lo que conteste.
4. **Crear la Release:**
   1. Abre https://github.com/jluisplagos/munger-v2-evidencias-mistral/releases/new
   2. Arriba, en el botón **«Choose a tag»**, escribe `fuentes-examen-20261118` y pulsa **«+ Create new tag: fuentes-examen-20261118 on publish»**.
   3. Justo al lado, en **«Target»**, elige la rama `coordinacion/cierre-v2`.
   4. En **«Release title»** escribe: `Fuentes del examen (Jumbo, Zoetis, Vinci, Waste Management)`.
   5. En el recuadro de abajo, **«Attach binaries by dropping them here»**, arrastra todos los PDF: los de Jumbo, los dos de Zoetis y todo lo que haya dentro de `munger_fuentes_examen`, con sus subcarpetas abiertas, porque GitHub no acepta carpetas. Si tienes otros PDF oficiales de cualquier empresa del universo, súbelos también.
   6. Espera a que todas las barras terminen y pulsa **«Publish release»**.
   7. Escríbeme «release subida». Yo descargo cada archivo y compruebo sus huellas.

### 0.4 · Preparar GitHub para el crédito de API (15 minutos, una sola vez)
Hay cuatro pasos. Si algo no aparece como lo describo, hazme una foto de la pantalla.

**Paso A · Conseguir una clave de API nueva.** El secreto viejo no se puede leer, así que creamos otro.
1. https://console.anthropic.com → **Settings** → **API keys** → botón **«Create Key»**.
2. Nombre: `munger-github`. Pulsa **Create** y **copia la clave**. Empieza por `sk-ant-` y solo se ve esta vez.
3. **No me la pegues aquí.** Va directa a GitHub, en el paso B.

**Paso B · Crear el «environment» protegido.**
1. Abre https://github.com/jluisplagos/munger-v2-evidencias-mistral/settings/environments
2. Pulsa **«New environment»**, escribe `inferencia-aprobada` y pulsa **«Configure environment»**.
3. Marca la casilla **«Required reviewers»**, escribe `jluisplagos` en el buscador, elígete y pulsa **«Save protection rules»**.
4. Más abajo, en **«Environment secrets»**, pulsa **«Add environment secret»**:
   - **Name:** `ANTHROPIC_API_KEY`
   - **Value:** pega la clave del paso A.
   - Pulsa **«Add secret»**.
5. En **«Environment variables»**, pulsa **«Add environment variable»**:
   - **Name:** `MUNGER_TOPE_ACUMULADO_ANTHROPIC_USD`
   - **Value:** `180`. Es el tope total que podrá gastar el proyecto; deja margen sobre tu saldo.
   - Pulsa **«Add variable»**.

**Paso C · Quitar la clave antigua del repositorio**, para que nada pueda usarla sin tu aprobación.
1. Abre https://github.com/jluisplagos/munger-v2-evidencias-mistral/settings/secrets/actions
2. En **«Repository secrets»**, si aparece `ANTHROPIC_API_KEY`, pulsa el icono de la papelera que tiene a la derecha y confirma.
3. Si no aparece, no pasa nada.

**Paso D · Autorizarme.** Escríbeme exactamente esto: **«Autorizo fusionar el lanzador del análisis directo en main del repositorio auxiliar»**. Lo necesito porque GitHub solo deja lanzar a mano los workflows que están en la rama principal.

---

## 1 · Frente API 💳 (unos 197 USD)

| # | Qué | Quién | Necesita | Terminado cuando |
|---|---|---|---|---|
| A1 | Fusionar el lanzador revisado (`automatizacion/analisis-directo` @ 74fe0cf, tres rondas) en `main` del auxiliar; antes, la comprobación rápida de su tercera ronda | 🤖 | tu autorización (0.4 D) | en «Actions» aparece «Análisis directo» |
| A2 | Paquetes de datos verificados para el análisis directo: Ahold, Zoetis T1 (corte 9-oct), Elis, Vinci, Waste Management y Jumbo, cada uno con tu etapa 1 (L2) | 🤖 | las fuentes de cada empresa | `datos_analisis_directo/<empresa>/` con su manifiesto de huellas |
| A3 | **Primera ejecución de prueba** (Ahold): mide el coste real y si el esquema funciona | 👤 lanza y aprueba (pasos abajo) · 🤖 revisa | A1, A2 | coste real anotado; salida aceptada |
| A4 | Análisis directo de las seis empresas × **3 repeticiones**, para medir cuánto varía el análisis directo | 👤 aprueba · 🤖 prepara | A3 correcta | 18 resultados con su coste (unos 20–40 USD) |
| A5 | **Modo por tandas** del lanzador: una aprobación cubre un grupo de unas 20 empresas, con su tope y una llamada por empresa, sin reintentos. Lo revisa Fable | 🤖 | — | revisado, en `main` |
| A6 | **Cribado del universo** (135–140 empresas) con el embudo corregido de la reorientación §4: calidad, caja, balance, precio y encaje al final. Es un cribado, no un veredicto | 👤 aprueba cada tanda · 🤖 prepara y lee | A5, tu lista y tus etapa 1 | una tabla ordenada con el motivo de cada empresa (unos 100–140 USD) |
| A7 | Informe del gasto: lo comprometido frente al tope | 🤖 | — | en el estado diario |

**Cómo lanzas y apruebas una ejecución** (👤, unos 2 minutos cada vez; yo te dejaré los valores exactos para copiar):
1. Abre https://github.com/jluisplagos/munger-v2-evidencias-mistral/actions
2. A la izquierda, pulsa **«Análisis directo»**. A la derecha aparece el botón gris **«Run workflow»**: púlsalo.
3. Rellena los campos con lo que te pase yo, por ejemplo `empresa: ahold`. Pulsa el botón verde **«Run workflow»**.
4. Espera un minuto y entra en la ejecución nueva, la de arriba. Primero termina el paso «preparar», que **muestra cuánto va a reservar**. Si te parece bien, pulsa **«Review deployments»**, marca `inferencia-aprobada` y pulsa **«Approve and deploy»**.
5. Cuando se ponga en verde, escríbeme «aprobado». Si no te cuadra la reserva, no apruebes y pregúntame.

---

## 2 · Frente Mistral 🟠 (unos 200 €)

**Cada encargo se pega en una ventana nueva de Mistral**, salvo que diga «la misma ventana». Yo te paso el texto exacto cada vez, ya listo para pegar.

| # | Qué | Ventana | Cuándo | Terminado cuando |
|---|---|---|---|---|
| M1 | Ronda 1 del registro de entradas de Ahold (las 11 que faltaban) | la misma del registro de Ahold (ya pegado) | ahora | 🤖 lo compruebo; si cuadra, lo revisa y sella un agente de Claude |
| M2 | **Registro de entradas** de Jumbo, Zoetis T1, Vinci y Waste Management, una ventana por empresa, como el de Ahold | 4 nuevas | en cuanto yo monte cada expediente | 🤖 comprobador sin errores de formato |
| M3 | **Revisión económica de otra familia de modelos (K8)** de cada expediente terminado: busca errores económicos, sin ver la rúbrica | una por expediente | cuando cada uno termine | informe con hallazgos; 🤖 contesto cada uno |
| M4 | **Segunda comprobación de la historia** de cada empresa: cada cifra de los diez años contra su PDF | una por empresa | en paralelo con M2 | lista de discrepancias, o «ninguna» |
| M5 | **Inventario del universo**: con tus etapa 1, una tabla con nombre, bolsa, ticker, moneda, sector, norma contable y si hay informes en inglés | 1 nueva | en cuanto me pases los ficheros (0.5) | tabla en el auxiliar; prepara A6 |
| M6 | **Fuentes del universo**: para las empresas que A6 deje arriba, descargar y huellar sus informes oficiales | varias | tras A6 | índices con huella |

### 0.5 · Tus ficheros del universo (👤, cuando puedas hoy)
1. Junta en una carpeta los `<Empresa>_evaluada.xlsx` y `<Empresa>_respuesta.md` de todas tus empresas.
2. Comprime la carpeta: botón derecho → «Comprimir» o «Enviar a → Carpeta comprimida».
3. Súbela aquí, a esta conversación. Si pesa demasiado, en dos o tres partes.

---

## 3 · Frente Claude 🤖 (Fable sin tope hoy y mañana; personaje en Opus)

En orden de prioridad. Lo que no dependa de otra tarea va en paralelo.

| # | Qué | Modelo | Terminado cuando |
|---|---|---|---|
| C1 | **Ahold, entero.** Expediente nuevo con la plantilla V6.3.1 revisada (`eaece01a`) y la declaración F1, pipeline desde el paso 1, fases A, B y C, **contradictor**, respuesta, verificación, **auditoría** y cierre | Opus (personaje) · Fable (contradictor y auditoría) | ficha cerrada y auditada |
| C2 | **Ahold con el motor B** (V6.4.1, perímetro NIIF 16), para el criterio de los dos motores (K4) | Opus · Fable | las dos zonas comparadas |
| C3 | **Registro de entradas de Ahold:** revisión en la fuente y sellado de cada entrada material, tras M1 | Fable (revisor distinto de Mistral) | `verificacion_entradas` apto, o lo que falte, explicado |
| C4 | **Reparación clave: F1 con la norma de EE. UU.** Hoy F1 bloquea con US GAAP, así que **Zoetis y Waste Management acabarían en «límite del modelo»** y no examinarían la trampa. Hay que implantar el tratamiento de los arrendamientos operativos de US GAAP, con casos sintéticos y revisión crítica | autor Opus · revisión Fable | Zoetis y WM pueden concluir; K11 con EE. UU. |
| C5 | **Hoja resumen en lenguaje llano** generada desde la ficha: párrafo llano, sensibilidad al 7–11 %, prueba del 10 % (informativa), predicciones fechadas (K9) y lo que haría falso el veredicto | autor Opus · revisión Fable | la hoja sale en cada expediente |
| C6 | **Elis con F1** (sus decisiones del 17-nov): debe quedar en «faltan datos» sin inventar R | Opus · Fable | estado y motivo correctos |
| C7 | **Jumbo, entero**, en cuanto estén sus PDF: diez años, metadatos, F1 con la regla F1-A, personaje, contradictor y auditoría | Sonnet · Opus · Fable | ficha auditada |
| C8 | **Zoetis T1** (hasta el 9-oct) y **T2** (con el 5-nov), dos expedientes | ídem | dos fichas |
| C9 | **Vinci** hasta la fase A: tiene que abstenerse por el motivo correcto | Opus · Fable | límite del modelo, bien razonado |
| C10 | **Waste Management, entero** (si C4 llega a tiempo) | ídem | ficha auditada |
| C11 | **Repetibilidad (K7):** una segunda ejecución independiente de Jumbo y de Zoetis T1 | Opus | mismo cubo y precio de Sí a menos del 15 % |
| C12 | **Variante con Fable dentro del personaje** (Jumbo y Zoetis T1), solo si sobra tiempo | Fable | comparación Opus/Fable |
| C13 | **Evaluación con la rúbrica congelada**, caso por caso, con un evaluador distinto | Fable | la tabla del §7 rellena |
| C14 | **Contradictor del veredicto final** y el veredicto (23-nov), con lo que lo haría falso | Fable | tus tres frases |
| C15 | **Procedimiento corto** «así se analiza una empresa nueva», para cuando ya no esté Claude | Opus · revisión Fable | dos páginas probadas por un agente sin historial |
| C16 | **Estado diario de cinco líneas** y registro de gasto de los tres frentes | — | cada mañana y cada noche |

---

## 4 · Calendario orientativo

| Momento | API | Mistral | Claude |
|---|---|---|---|
| **18-nov tarde** | 0.4, A1, A2, A3 | M1; M5 si ya llegaron tus ficheros | C1 (Ahold), C4 (US GAAP), C5 (hoja), C6 (Elis) |
| **18-nov noche** | A4 (repeticiones) | M2 de Vinci y WM; M4 | C1 sigue; C3; C9 (Vinci) |
| **19-nov** | A5, A6 (universo por tandas) | M2 de Jumbo y Zoetis; M3 según terminen | C7, C8, C10, C11, C2 |
| **20-nov madrugada** | A6 termina; A7 | M3, M6 | C12, C13 |
| **21–23-nov** (uso medido) | lo que quede, con tu visto bueno | M3 restantes | C13, C14, C15 |

**Lo que me haría estar equivocado con este plan:** C4 (US GAAP) es la pieza técnica más arriesgada. Si no queda bien revisada a tiempo, Zoetis y Waste Management acabarán en «límite del modelo». La trampa del examen solo se comprobaría entonces en parte, y el veredicto tendría que ser «Todavía no».
