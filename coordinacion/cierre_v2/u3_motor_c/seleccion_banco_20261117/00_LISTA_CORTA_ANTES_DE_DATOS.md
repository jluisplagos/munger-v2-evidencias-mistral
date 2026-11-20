# Lista corta de bancos para el caso C · escrita ANTES de mirar datos de ningún candidato

- Hora UTC de redacción: 2026-11-17T15:01Z (la huella y la hora del sistema van en `00_REGISTRO.txt`).
- Repositorio `munger-v2-evidencias-mistral`, rama `coordinacion/cierre-v2`, HEAD `b4764881f3e7932050d37cb52980692c09911b55` tras `git pull --ff-only`.
- Huellas de referencia (sin cambios):
  - `PROTOCOLO_SELECCION_C.md` = `3e28d9c0456a9a3197e9a9430e988cde5cbde06b8cfa79e1608f52f836317855` (igual a la fijada a las 09:30Z);
  - `CONTRATO_C_DESDE_EL_MOTOR.md` = `cc9efb212e98c172bf60e0f24dc7b656bd3fd0d8f21ca2af32ab6a7926bf2ad7`;
  - `CANDIDATOS_C.md` = `296fad5b5361e5046323d90048099ed0d627fec9eea309b097528caf19d174bd`.
- Antes de escribir esto no he hecho ninguna petición de red en esta sesión ni he consultado precios. Todo lo que digo de cada entidad es **conocimiento previo [a verificar]**.
- Decisión de partida (persona responsable, 17-nov): Hannover Rück queda como prueba negativa de «modelo no aplicable»; Fineco descartada por C4 y C3. Se busca **un banco**.

## 1. Criterio con el que se forma la lista (filtro previo)

Bancos (C1) europeos cotizados en mercado regulado del EEE (C2) que, según conocimiento previo, cumplen a la vez:

| Filtro | Lectura | Origen |
|---|---|---|
| Modelo | Banca minorista o comercial simple (crédito y depósitos); se apartan la banca de inversión y los bancos de corretaje o gestión de activos (R7) | encargo |
| R6 | Sin aseguradora consolidada por integración global | encargo / protocolo §4 |
| R3 | Sin filiales con minoritarios materiales (en la fuente: las que la entidad identifica como tales según NIIF 12) | encargo / protocolo §4 |
| R5 | Moneda de presentación euro, sin hiperinflación | encargo / protocolo §4 |
| R2 | Sin fusión, escisión o combinación de negocios relevante 2016–2025 | encargo / protocolo §4 |
| C3 | Versión **fehaciente** del informe anual en castellano, o en inglés como lengua original (no traducción de cortesía); francés admitido por el protocolo | encargo; lectura estricta tras Fineco |
| C4 | Diez informes anuales **consolidados** 2016–2025 y serie de Pilar 3 | protocolo §2 |
| C6 | Fuera de muestra | protocolo §2 (se comprueba con `git grep` después de fijar esta lista) |
| C7 | Sin precios | protocolo §2 |

**Qué parte sale de conocimiento previo pendiente de verificar:** todo el filtro aplicado a cada entidad (modelo, R2, R3, R5, R6, idioma fehaciente, años consolidados, cotización). Lo único que no es conocimiento previo es el texto del protocolo y del contrato.

**Consecuencia de C3 estricto (conocimiento previo):** quedan fuera, como grupo, los bancos cuya lengua oficial de publicación es el italiano, el alemán, el neerlandés de Bélgica, el portugués, el griego, el esloveno, el croata o las lenguas bálticas y nórdicas. Dentro: **España** (castellano), **Irlanda y Malta** (el inglés es lengua oficial del Estado y el informe se redacta en inglés), Francia (francés) y, con duda, Países Bajos (informe en inglés como documento legal) [a verificar].

## 2. Entidades consideradas y descartadas ya en el filtro (conocimiento previo, [a verificar])

| Entidad | País | Motivo del descarte previo |
|---|---|---|
| Santander, BBVA | ES | R3 (minoritarios materiales), R5 (varias monedas, hiperinflación), R2 |
| CaixaBank | ES | R2 (fusión con Bankia, 2021), R6 (VidaCaixa consolidada) |
| Banco Sabadell | ES | R5 (TSB en GBP), R2 (venta de TSB) |
| Renta 4 Banco | ES | Modelo: banco de corretaje y gestión de activos, no comercial simple (R7, como Fineco); filiales en Chile, Colombia y Perú |
| BNP Paribas, Société Générale, Crédit Agricole SA | FR | R6 (aseguradoras consolidadas), R3, R5 |
| Bank of Ireland Group | IE | R6 (New Ireland Assurance consolidada) |
| HSBC Bank Malta | MT | R6 (aseguradora de vida consolidada), filial cotizada de otro grupo |
| Lombard Bank Malta | MT | R3 y negocio mixto (participación de control en MaltaPost) |
| FIMBank | MT | R5 (presenta en USD) |
| ING, KBC, Nordea, Erste, RBI, BAWAG, NLB, Bank of Cyprus, LHV, Šiaulių, BCP, bancos griegos, italianos y alemanes | — | C3 estricto y, además, R2/R3/R5/R6 en la mayoría |

## 3. Lista corta y orden

Orden según el protocolo §5 (paso 1 no aplica: solo se busca un banco): §5.2 menos operaciones R2 conocidas; §5.3 menos marcas R3/R5/R6; §5.4 AT1 identificable; §5.5 euro; §5.6 español > inglés > francés. Se verifican **como máximo cinco**, en este orden, y se para en el primero que encaje.

| Orden | Entidad | País · lengua | R2 conocido [a verificar] | R3 / R5 / R6 [a verificar] | Otros riesgos [a verificar] |
|---|---|---|---|---|---|
| 1 | **Bank of Valletta p.l.c.** | MT · EN (lengua oficial) | ninguna operación societaria relevante conocida | sin minoritarios materiales conocidos; EUR; participación en aseguradora de vida (MSV Life) por puesta en equivalencia, no integración global | **R8: posible cambio de fecha de cierre (de 30-sep a 31-dic) dentro de la ventana**, que podría afectar a C4 y a V04; litigios con provisiones relevantes; AT1 previsiblemente inexistente |
| 2 | **AIB Group plc** | IE · EN (lengua oficial) | inserción de holding (AIB Group plc sobre Allied Irish Banks p.l.c., 2017, reorganización sin cambio económico); compras de carteras de Ulster Bank (2022) y adquisición de Goodbody (2022, pequeña) | sin minoritarios materiales conocidos; EUR con filial en GBP (Reino Unido); sin aseguradora consolidada (empresa conjunta de vida por puesta en equivalencia) | C4: el informe 2016 sería del emisor anterior (mismo grupo); AT1 dentro del patrimonio, identificable |
| 3 | **Permanent TSB Group Holdings plc** | IE · EN (lengua oficial) | adquisición de negocio minorista y carteras de Ulster Bank (2022), material | sin minoritarios conocidos; EUR; sin aseguradora | AT1 identificable |
| 4 | **Bankinter S.A.** | ES · ES | compra de Barclays Portugal (2016), compra de EVO Banco (2019), escisión de Línea Directa (2021) | R6 hasta 2021 (Línea Directa consolidada); EUR; sin minoritarios materiales conocidos | AT1 identificable; C3 resuelto en castellano |
| 5 | **Unicaja Banco S.A.** | ES · ES | absorción de Banco CEISS/EspañaDuero (2017–2018) y fusión con Liberbank (2021) | EUR; participaciones en aseguradoras previsiblemente por puesta en equivalencia | AT1 identificable; C3 resuelto en castellano |

- Bankinter va delante de Unicaja aunque tiene más operaciones R2 en número porque las dos de Unicaja son fusiones que cambian el tamaño del grupo; es un desempate por materialidad **declarado aquí, antes de datos**, y discutible. Ambos llevan marcas R2 que el filtro del encargo pide evitar: se incluyen porque el encargo pide bancos españoles si es posible y porque el protocolo no excluye por R2.
- ABN AMRO queda fuera de los cinco (sería el sexto): R2 (venta de negocios internacionales 2020–2021, compra de Hauck Aufhäuser Lampe, fusión del holding en el banco) y duda sobre C3.

## 4. Cómo se clasificará cada candidato

- **BLOQUEO_ACCESO:** CONNECT 403 del proxy o rechazo del propio sitio con el agente de usuario indicado. Se anota el host exacto y se pasa al siguiente. No se cambia la red ni se esquiva.
- **INCUMPLE_PROTOCOLO:** falla un criterio C1–C7 o cae en X1–X4 (criterio exacto y página).
- **INCUMPLE_FILTRO:** cumple el protocolo, pero la fuente contradice un filtro de la lista (R2: fusión, escisión o combinación de negocios relevante que la propia entidad declara en 2016–2025; R3: filial con minoritarios que la entidad identifica como materiales; R5: moneda de presentación distinta del euro; R6: aseguradora consolidada por integración global). Va en la lista de incumplimientos, marcada aparte, porque en el protocolo R no excluye por sí solo: la persona puede rescatarlo.
- **ENCAJA:** cumple C1–C7, ninguna X, ningún incumplimiento de filtro; los riesgos R1–R8 restantes se declaran.

Sin umbrales numéricos: si un R2 o R3 está en el límite, se declara y se deja a la persona responsable, sin forzar.
