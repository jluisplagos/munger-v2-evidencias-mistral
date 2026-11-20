# Antigua sesión B · nueva etapa E: fuentes económicas de Elis

Sesión visible: **«M2-FRENTE B PM1 ampliación económica»**. Tu bloque B/P-M1 se conserva; **este es un encargo nuevo y explícito**, que amplía su alcance sin reabrir ni modificar el dossier anterior. Lee LEEME.md, PROGRAMA.md e INTEGRACION.md.

Consulta los remotos. Crea **`mistral/e-fuentes-elis`** desde el commit del paquete de coordinación, con escritura solo en **`resultados_cierre/elis_fuentes/`** del auxiliar `jluisplagos/munger-v2-evidencias-mistral`. No sobrescribas cambios locales ni toques B, A/C/D/F, el producto o main. Si ya existe la rama, inspecciónala y retómala sin forzarla.

## Objetivo

Entregar evidencia primaria nueva o una búsqueda acotada que identifique lo no encontrado para **M1/M2/M6/N2 de Elis**. Eso descarga investigación a Claude. No se pide una valoración, una R ni una política que permita terminar. Que exista saldo no obliga a gastarlo ni permite inventar información.

## Bloque 1 · preguntas y recursos ya examinados

Lee la recuperación F1 y la propuesta actual del producto (base conocida716cbd6), la revisión externa f5775dc y su `datos/fuentes.json`. Comprueba cambios posteriores. Los cinco PDF/libro ya conservados están en la Release base-4.14; no vuelvas a pedir al usuario las partes ni presentes su lectura previa como fuente nueva.

Divide en preguntas factuales:

1. **M1:** reparto anual por activos del capex mantenimiento/crecimiento; base y fecha de «dos tercios» del lino plano; importe, horizonte y finalidad del plan climático.
2. **M2:** tasa de bajas de clientes y desembolso inicial por cliente nuevo; distinguir gasto comercial corriente de inversión propia y compras de cartera.
3. **M6:** finalidad de compras pequeñas y crecimiento orgánico sin ellas. El orgánico publicado excluye solo adquisiciones importantes; no vuelvas a inferir «sin compras».
4. **N2:** relación de seguros/resultado por bajas de 2025, dónde se cobró, fiscalidad y reposición de activos. No supongas que dos magnitudes parecidas son la misma partida.

Publica primero `PREGUNTAS_Y_RESULTADOS.csv` con estado inicial y `FUENTES_Y_BUSQUEDA.csv` que separe recursos ya examinados de candidatos nuevos. No repitas una búsqueda cuyo ámbito ya está agotado sin una pista nueva.

## Bloque 2 · búsqueda finita y lectura

Prioriza presentaciones oficiales de resultados/CMD, documentos regulatorios y preguntas/respuestas de IR **publicadas**, no contacto privado. Explora hasta **12 documentos oficiales nuevos** seleccionados por relación con las preguntas; es un alcance inicial finito, no una meta de descargar por descargar. Los buscadores y terceros son pistas, no sustitutos silenciosos de la fuente primaria. No compres acceso, no envíes mensajes ni cambies credenciales.

Por fuente: URL oficial y final, título, fecha, ejercicio, idioma, bytes, SHA256, versión y estado real de preservación. Sigue las reglas del auxiliar para binarios; URL+hash no equivale a documento preservado. Conserva scripts reproducibles de recuperación y fragmentos acotados. Si falla un upload, registra y continúa lo independiente; no pidas tokens.

Lee cabeceras/tablas/notas pertinentes, con página PDF y columna, unidad/escala/perímetro/periodo. Haz la primera lectura antes de compararla con cifras heredadas. Confirma ambigüedades con representación visual o segundo extractor. Registra por pregunta el hallazgo, lo que significa, lo que no demuestra y a qué salida afecta. Si hay deriva/cálculo, muestra operandos, fórmula, unidades y redondeo en script; no sumas manuales del chat.

Una proporción de ventas no es proporción de capex; «dos tercios» de un bloque no se extrapola al total. Categoría contable no identifica reposición económica. No escojas R entre736,0–867,2 ni θ/λ para ayudar a cerrar. Una estimación defendible exige evidencia/método/rango; no se genera por falta del dato.

## Bloque 3 · entrega y siguiente trabajo

Cada pregunta termina con evidencia examinada, ambigüedad o «no localizado en esta búsqueda», con lista de documentos/páginas y límites. No afirmar «no publicado en ninguna parte». Fuentes suficientes pueden reducir un bloqueo; solo el integrador y una revisión posterior establecen ese uso, no tú por autoaprobación.

Entrega `LECTURA_FUENTES.jsonl`, preguntas/resultados, inventario de fuentes/búsqueda, hallazgos/límites, scripts, resumen para integrador, ENTREGA.json, manifiesto y recuperación. Conserva C48/C49/FCF base y decisiones vigentes. Publica commit/push tras inventario y cada bloque documental sustantivo. Continúa sin confirmación rutinaria.

Cuando E esté finito: revisa control de Claude. Si te asigna buscar una fuente concreta pendiente de P-M1 u otra tarjeta documental, hazlo en bloque separado con pregunta y límite explícitos. No te metas en revisiones genéricas ni prepares una estimación financiera sin un encargo distinto. Si todo lo pendiente depende de información no pública, declara el límite; no contactes empresas por iniciativa propia. Registra modelo/herramientas/consumo solo si visibles.
