# Selección de un banco para el caso C · U3 / F-C1

- **Autoría:** subagente de fuentes del coordinador, 17-nov-2026, 15:00–15:05 UTC. Necesita revisión por un contexto distinto.
- **Estado:** propuesta y registro de acceso. **No es una decisión, una designación ni una aprobación.**
- **Encargo:** decisión de la persona responsable del 17-nov. Hannover Rück queda como prueba negativa de «modelo no aplicable» y no sustituye al caso C aplicable. Fineco, descartada por C4 y C3. Se busca un banco compatible con el motor C y con el protocolo.
- **Material:** `munger-v2-evidencias-mistral`, rama `coordinacion/cierre-v2`. `git pull --ff-only` = «Already up to date», HEAD `b4764881`. Protocolo `3e28d9c0…17855` (sin cambios desde las 09:30Z); contrato `cc9efb21…2bf2ad7`.
- **Sin precios (C7), sin contactos, sin commits.** No he cambiado la red ni he esquivado ningún bloqueo.

## Resultado en una línea

**Ningún banco encaja ni puede descartarse por el protocolo.** Los cinco candidatos de la lista (Bank of Valletta, AIB, Permanent TSB, Bankinter y Unicaja) dan **CONNECT 403 del proxy** en su sitio oficial. Es un bloqueo de acceso del entorno, no un incumplimiento. No hay ningún documento descargado, así que no hay nada verificado con página.

---

## 1. Orden de trabajo (lista antes de datos)

| Paso | Hora UTC | Evidencia |
|---|---|---|
| Lista corta, criterio y orden escritos | 15:01:19Z (mtime) | `00_LISTA_CORTA_ANTES_DE_DATOS.md`, SHA-256 `a9f6b80580d437aada29c1b0505309851e8234e43afdb9fd8956b6b3ec7d1bfd` |
| Registro de hora y huella | 15:01:23Z | `00_REGISTRO.txt`, SHA-256 `d02d66685912b8edfb4f8a6127033eb274e3d2a0828f96ac4f01b7c57629b934` |
| C6 (`git grep`, sin red) | 15:01:3xZ | §5 |
| Primera petición de red a un candidato | 15:01:40Z | `INDICE.tsv` |
| Última petición | 15:02:23Z | `INDICE.tsv` |

**Criterio de la lista** (detalle en `00_LISTA_CORTA_ANTES_DE_DATOS.md` §1): bancos europeos cotizados, de modelo minorista o comercial simple, sin aseguradora consolidada (R6), sin minoritarios materiales (R3), en euros (R5), sin fusiones relevantes en 2016–2025 (R2), con versión fehaciente en castellano o con el inglés como lengua original (C3 estricto), con diez años consolidados (C4) y fuera de muestra (C6).

**Qué es conocimiento previo:** la aplicación de todo el filtro a cada entidad. Está **pendiente de verificar** y marcada [a verificar] en la lista.

**Efecto de C3 estricto:** solo quedan España (castellano), Irlanda y Malta (el inglés es lengua oficial y el informe no es una traducción), Francia y, con duda, Países Bajos. Los bancos franceses grandes caen por R6 y R3.

**Orden** (protocolo §5.2–5.6, por conocimiento previo):

1. Bank of Valletta (MT);
2. AIB Group (IE);
3. Permanent TSB (IE);
4. Bankinter (ES);
5. Unicaja (ES).

Los españoles van detrás porque llevan marcas R2 conocidas: Bankinter (Barclays Portugal en 2016, EVO en 2019 y escisión de Línea Directa en 2021, además de R6 hasta 2021) y Unicaja (CEISS en 2017–2018 y Liberbank en 2021). Se incluyeron porque el encargo pedía bancos españoles si era posible y porque en el protocolo R2 no excluye.

---

## 2. Lista A · BLOQUEO_ACCESO (con el host)

Todas las peticiones usaron `curl -sS -A 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0 Safari/537.36'`. En todos los casos el proxy del entorno contestó `HTTP/1.1 403 Forbidden` al CONNECT, y su estado lo registró como `connect_rejected` («gateway answered 403 to CONNECT (policy denial or other refusal)»). **Ningún sitio llegó a contestar.**

| Orden | Candidato | Host que haría falta permitir | Otros hosts probados (también 403) | Hora del rechazo (estado del proxy) |
|---|---|---|---|---|
| 1 | Bank of Valletta p.l.c. | `www.bov.com` | — | 15:01:40.867Z y 15:01:41.099Z |
| 2 | AIB Group plc | `aib.ie` (relación con inversores en `/investorrelations`) | `www.aib.ie` | 15:01:53.201Z y 15:01:53.478Z |
| 3 | Permanent TSB Group Holdings plc | `www.permanenttsbgroup.ie` (sitio del grupo e inversores) | `www.ptsb.ie` (sitio comercial) | 15:02:03.817Z y 15:02:05.750Z |
| 4 | Bankinter S.A. | `www.bankinter.com` (web corporativa en `/webcorporativa/`) | `webcorporativa.bankinter.com`: host supuesto por mí, que puede no existir | 15:02:16.098Z y 15:02:16.394Z |
| 5 | Unicaja Banco S.A. | `www.unicajabanco.com` | `www.unicaja.es` (sitio comercial) | 15:02:23.931Z y 15:02:24.181Z |

**Advertencias:**
- Las rutas de inversores son supuestas: como no hubo respuesta, no se pudieron comprobar.
- Los PDF podrían servirse desde **otro host** (CDN o gestor documental), como pasó con Fineco (`images.finecobank.com`) y Hannover (`assets.hannover-re.com`). Permitir solo el host de la página podría no bastar. Ese segundo host solo se conocerá al leer la página de inversores.

## 3. Lista B · INCUMPLE_PROTOCOLO o INCUMPLE_FILTRO (con el criterio)

**Ningún candidato verificado.** No se ha leído ningún documento, así que no hay ningún incumplimiento probado de C1–C7 ni de X1–X4.

Riesgos que **podrían** convertirse en incumplimiento si se verifican. Son conocimiento previo [a verificar] y no clasifican:

| Candidato | Posible problema | Qué criterio tocaría |
|---|---|---|
| Bank of Valletta | Posible cambio de la fecha de cierre (de 30-sep a 31-dic) dentro de la ventana | R8; podría afectar a C4 (diez informes anuales) y a V04 (años consecutivos) |
| AIB Group | El informe de 2016 sería del emisor anterior, Allied Irish Banks p.l.c. (holding insertado en 2017) | C4: sería una ruptura formal, como en Fineco, aunque aquí ese informe sí es consolidado |
| AIB Group | Compras a Ulster Bank (2022) | Filtro R2, según cómo las contabilice la entidad: compra de carteras o combinación de negocios |
| Permanent TSB | Adquisición de negocio de Ulster Bank (2022) | Filtro R2 |
| Bankinter | Barclays Portugal (2016), EVO (2019), escisión de Línea Directa (2021) | Filtros R2 y R6 (2016–2020) |
| Unicaja | CEISS (2017–2018) y Liberbank (2021) | Filtro R2 |

Las entidades descartadas ya en el filtro previo, sin datos, están en `00_LISTA_CORTA_ANTES_DE_DATOS.md` §2. **Tampoco son incumplimientos verificados.**

## 4. Lista C · ENCAJA

**Ninguna.**

---

## 5. C6 · fuera de muestra (lo único comprobado)

- **`munger-v2-evidencias-mistral`** (HEAD, `origin/coordinacion/cierre-v2` y `origin/mistral/f-alcance-real`), con `git grep -il -w`:
  - Valletta, BOV, Allied Irish, Permanent TSB y PTSB: 0 coincidencias;
  - Bankinter y Unicaja: solo en documentos de coordinación de U3 (`CANDIDATOS_C.md`, `PROTOCOLO_SELECCION_C.md` e `INDICE_FUENTES.csv`), como candidatos o como sitio probado;
  - AIB: solo en `revisiones_coordinador/E2_ea641e7/sondas/urd/urd2025_full.txt`.
- **`munger-v2`** (HEAD `9cad78d`):
  - Valletta, BOV, Allied Irish, Permanent TSB y PTSB: 0;
  - AIB: 9 archivos, todos en `/texto/` de fuentes de Elis, donde «AIB» es la **Association of Issuing Bodies** (garantías de origen), no el banco. Fuera de `/texto/`: 0.
- **Interpretación:** los cinco cumplen C6.
- **Límites:**
  - La lista de las 116 empresas de la etapa 1 sigue **NO OBSERVABLE**.
  - La candidata `957af65` no la he revisado aparte: me baso en `CANDIDATOS_C.md` §1.

---

## 6. Conclusión

- **No hay banco designable hoy.** No es porque los candidatos incumplan el protocolo: es porque **el entorno no permite llegar a ninguna fuente oficial**. No he forzado nada: ni he cambiado la red, ni he esquivado el proxy, ni he usado fuentes que no sean oficiales.
- **Qué haría falta.** Lo decide la persona responsable:
  1. Permitir el host del candidato que prefiera, empezando por el orden declarado: `www.bov.com`; luego `aib.ie` y `www.aib.ie`; `www.permanenttsbgroup.ie`; `www.bankinter.com`; `www.unicajabanco.com`. Una vez leída la página de inversores, puede hacer falta permitir el host de los PDF.
  2. O que la persona descargue desde un navegador el informe anual 2025 y el Pilar 3 2025 del candidato elegido, y los entregue con su SHA-256.
  3. Con acceso, la verificación seguiría el modelo de `verificacion_fineco_20261117/`: edición, período, perímetro contable frente a prudencial, cuadre de CET1/APR/ratios, C1–C7, X1–X4, R2/R3/R5/R6, contrato con página y C4 contra el listado oficial.
- **Observación, no decisión:**
  - Con C3 estricto, la lista útil es corta. Los españoles resuelven C3, pero llevan R2 conocido.
  - Los irlandeses y Malta resuelven C3 en inglés original y tendrían menos R2, aunque cada uno tiene una duda concreta de C4 o R2 (§3).
  - Si se abre un único host, Bank of Valletta es el primero del orden, pero su riesgo R8 sobre C4 es el punto que antes podría hacerlo caer. AIB es el siguiente.

*Sin valoración, sin palancas y sin precios. Ninguna cifra de entidad aparece aquí porque no se ha leído ningún documento de los candidatos.*
