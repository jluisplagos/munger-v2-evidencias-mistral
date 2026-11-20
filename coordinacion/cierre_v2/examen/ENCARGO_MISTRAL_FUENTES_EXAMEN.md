# Encargo para Mistral · Fuentes oficiales de Jumbo, Zoetis, Vinci y Waste Management (examen del personaje)

**Para pegar en una ventana nueva de Mistral** (otra distinta de la del registro de Ahold). Fecha: 17-nov-2026, de noche. Encarga: el coordinador Claude. Duración esperada: varias horas.

## 1. Por qué te lo pido a ti

El coordinador trabaja en un servidor en la nube y **las webs de Jumbo y de Vinci bloquean las descargas desde servidores** (Cloudflare y un filtro anti-robots). Tú trabajas desde el ordenador de la persona responsable, así que probablemente sí puedes descargarlas. Lee antes `AGENTS.md` del repositorio auxiliar y cumple sus reglas: no subir PDF a Git, no escribir en `jluisplagos/munger-v2`, no aprobar tu propio trabajo y no hacer ninguna valoración.

## 2. Qué tienes que descargar

Solo **documentos oficiales del emisor** (su web de inversores) o de su **registro oficial** (SEC EDGAR para las de Estados Unidos). Nada de resúmenes de terceros. Prefiere siempre el **PDF** que publica la empresa. Si un documento solo existe en HTML (algunos de la SEC), guarda el original HTML tal cual y dilo.

Orden de prioridad. Si no llegas a todo, termina antes lo primero.

1. **Jumbo S.A.** (Grecia, `corporate.e-jumbo.gr`):
   - los informes financieros anuales de los **diez últimos ejercicios** (hasta el cerrado el 31-dic-2025, en inglés);
   - el informe semestral del **primer semestre de 2026**.

   Ojo: Jumbo cambió de ejercicio (antes cerraba el 30 de junio). Anota qué periodo cubre cada informe, incluido el ejercicio de transición si lo hubo.
2. **Zoetis Inc.** (Estados Unidos) en **dos tiempos**, en carpetas separadas:
   - `primer_tiempo/`: solo lo publicado **hasta el 9-oct-2026 inclusive**: los 10-K de los diez últimos ejercicios (hasta el ejercicio 2025, publicado en febrero de 2026) y los 10-Q del primer y segundo trimestre de 2026;
   - `segundo_tiempo/`: lo publicado **después**: el comunicado de resultados del tercer trimestre (5-nov-2026) y el 10-Q de ese trimestre.

   **Anota la fecha de publicación de cada documento**: es lo que decide en qué carpeta va.
3. **VINCI SA** (Francia, `www.vinci.com`):
   - como mínimo, los Universal Registration Documents (URD) de 2023, 2024 y 2025 en inglés; si puedes, los diez últimos;
   - el informe financiero semestral de 2026;
   - la información del tercer trimestre de 2026.
4. **Waste Management, Inc.** (Estados Unidos):
   - los 10-K de los diez últimos ejercicios (hasta el ejercicio 2025);
   - los 10-Q de 2026;
   - el comunicado de resultados del tercer trimestre (27-oct-2026).

**SEC EDGAR.** La SEC pide que cada descarga se identifique en el `User-Agent` con un nombre y un correo. Usa **solo** los datos que te dé la persona responsable. Si no te ha dado ninguno, descarga los documentos desde la web de inversores de la empresa, no desde EDGAR.

## 3. Qué entregas

En el repositorio auxiliar, **rama nueva `mistral/examen-fuentes`**, carpeta `resultados_examen/fuentes/`:

1. Por empresa, `<empresa>/INDICE.tsv` con una fila por documento y estas columnas: `archivo`, `titulo` (el de la portada), `periodo_que_cubre` (fechas exactas), `fecha_publicacion`, `url`, `pagina_oficial_que_enlaza`, `fecha_descarga_utc`, `http`, `bytes`, `sha256`, `paginas` (PDF), `formato` (pdf/html), `idioma` y `nota`.
2. Por empresa, `<empresa>/SHA256SUMS`.
3. `ENTREGA.md` (máximo una página):
   - qué conseguiste y qué no, con el motivo exacto (bloqueo, 404, no existe en inglés…);
   - qué periodos cubre cada empresa;
   - el modelo y las herramientas que usaste de verdad.

**Los PDF y HTML no se suben a Git.** Guárdalos en una carpeta local del ordenador, `munger_fuentes_examen/<empresa>/`. Si tu herramienta lo permite, súbelos además como assets a una Release nueva del repositorio auxiliar, `fuentes-examen-20261118`, con el mismo nombre de archivo. Si no lo permite, dilo y la persona los subirá mañana.

Haz commit y push al terminar cada empresa.

## 4. Cómo se acepta

El coordinador descargará de nuevo, desde la Release o desde la URL, una muestra de cada empresa y comprobará que el SHA-256 coincide. **Un documento que no sea el oficial, o una fecha de publicación mal puesta en Zoetis, invalida esa empresa.** Prefiero un «no lo pude descargar» honesto a un documento de otra fuente.
