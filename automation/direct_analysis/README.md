# Lanzador del análisis directo

## Para qué sirve

Compara el personaje completo con un **análisis directo en una sola pasada** de un
modelo potente, con los **mismos datos verificados** y la misma tasa (9 %).
Es la comparación de `REORIENTACION_UNIVERSO.md` §10: Ahold y Zoetis (primer tiempo).
Más adelante sirve también para repetir un caso (repetibilidad) y para medir lo que
cuesta un análisis.

Cada ejecución hace **como máximo una llamada** a la API de Anthropic, sin reintentos,
y solo después de que una persona la apruebe en GitHub.

## Qué recibe el modelo

- **El encargo fijo** (`ENCARGO_ANALISIS_DIRECTO.md`). Pide: estado, cubo, acción,
  tres escenarios de valor por acción con su razonamiento, precio de Sí con la regla
  k = 3, sensibilidad a la tasa del 7 al 11 %, qué haría falsa la conclusión y qué no
  sabe. Prohíbe usar memoria o hechos que no estén en el paquete. Su texto no cambia
  entre ejecuciones; su huella queda registrada.
- **El paquete de entrada**: los archivos de texto que declara un manifiesto, con su
  fecha de corte.

El modelo **no** recibe la rúbrica, el informe crítico, nada bajo `examen/`, ni las
salidas, fases o prompts del personaje. El lanzador rechaza esas rutas por su nombre
y rechaza los textos que mencionan la rúbrica o el informe crítico.

## Paso a paso

### 1. Preparar el paquete (una vez por caso)

1. Ten los datos verificados como archivos de texto UTF-8 en el repositorio: registro
   de entradas, extracto, Historia y textos de las fuentes. Excel y PDF no valen;
   hace falta su versión en texto.
   - Ojo: lo que está bajo `examen/` no se acepta. Por ejemplo,
     `coordinacion/cierre_v2/examen/ahold/LISTA_ENTRADAS.csv` tiene que estar en
     otra carpeta (una copia con la misma huella sirve).
   - Los archivos pueden estar en otra rama: basta indicar el commit.
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
       {"id": "registro_entradas", "ruta": "datos/zoetis_t1/registro_entradas.json",
        "commit": "<40 caracteres del commit, opcional>",
        "sha256": "<64 caracteres>", "descripcion": "Registro de entradas verificado"},
       {"id": "extracto", "ruta": "datos/zoetis_t1/extracto.md",
        "sha256": "<64 caracteres>", "descripcion": "Extracto de las fuentes hasta el 9-oct-2026"}
     ]
   }
   ```

   - Sin `commit`, el archivo se lee del mismo commit que el código.
   - Si la huella no coincide, si falta, o si el archivo no es texto, no se llama.
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
- Las «comprobaciones mecánicas» (precio de Sí recalculado con sus escenarios, citas
  literales, probabilidades) son avisos para la revisión. No aceptan ni rechazan.
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

## Qué no hace

- No reintenta. No usa modelo de reserva (*fallback*): sería otra llamada a otro modelo.
- No recorta ni resume el paquete.
- No decide si el análisis es bueno: eso es la revisión a ciegas (`RUBRICA_EXAMEN.md` §10).
- No ejecuta el personaje, no cambia el producto, no acepta ni integra nada, no
  acredita aptitud para dinero real.
- No garantiza que el modelo no use su memoria: lo prohíbe el encargo y las citas
  literales ayudan a detectarlo, pero hay que revisarlo.
- La lista de rutas prohibidas es por nombre y por unas pocas marcas de contenido.
  Elegir bien los archivos sigue siendo responsabilidad de quien hace el manifiesto.

## Límites conocidos

- La salida máxima es 32 768 tokens y el stream de AUTO1 se corta a los 720 s. Un
  esfuerzo `max` con un paquete grande puede agotar cualquiera de los dos: el
  resultado se paga y queda no aceptado.
- No se ha probado contra la API real: ni el esquema de salida, ni los campos de uso
  de Opus 5.5. Si el uso trae una facturación no prevista, el estado de coste queda
  `INCIERTO_SIN_COTA` y bloquea nuevas reservas hasta reconciliarlo.
- La exclusión mutua es entre ejecuciones de este workflow. Otro workflow de AUTO1
  que reserve a la vez podría pasar la misma comprobación del tope.

## Probar sin gastar

```
python3 -I -m unittest discover -s automation/direct_analysis -p 'test_*.py' -v
```

Las pruebas simulan la API y la rama de registro; no abren red.
