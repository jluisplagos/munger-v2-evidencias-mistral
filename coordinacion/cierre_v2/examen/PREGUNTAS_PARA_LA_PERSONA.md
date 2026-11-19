# Preguntas para la persona responsable (se contestan cuando pueda; ninguna bloquea esta noche)

## L1 · Lanzador del análisis directo: un fallo pequeño hallado en la segunda y última ronda
**DECIDIDA el 18-nov: (a) tercera ronda mínima.** 
- **Qué pasa:** si los tres escenarios del análisis directo dieran exactamente el mismo valor y fuera grande, una comprobación auxiliar falla con un error en vez de un aviso, y el análisis pagado quedaría «no aceptado» (R2-1 de la revisión).
- **Opciones:** (a) **recomendada:** permitir una tercera ronda mínima solo para eso (cambiar el error por un aviso, con su prueba) y una comprobación rápida del revisor; (b) dejarlo como límite declarado y aceptar el riesgo, que es bajo.

## L2 · ¿Recibe el análisis directo la etapa 1?
**DECIDIDA el 18-nov: (a) sí, la misma etapa 1.** 
- **Qué pasa:** el personaje recibe tu etapa 1 y la trata como hipótesis. El lanzador, tal como está, también acepta tus respuestas de etapa 1 si se le dan, aunque su README dice que no (R2-2).
- **Opciones:** (a) **recomendada:** sí, darle la misma etapa 1 que al personaje, para que los dos partan de lo mismo y la comparación sea justa (REORIENTACION §10: «los mismos datos»); se corrige el README. (b) No dársela, y añadirla al material que el lanzador rechaza; entonces el análisis directo parte con menos información que el personaje.

## F1-A · La reinversión necesaria en las empresas del motor A con alquileres (Ahold, Jumbo y las que sigan)
**DECIDIDA el 18-nov: (b) amortización propia como hipótesis declarada, para todas salvo Elis.** 

- **Qué pasa.** Con las decisiones F1, el motor A ya no puede usar la regla antigua, que contaba el alquiler dos veces. Para cada empresa hay que **declarar cuánto tiene que invertir solo para mantenerse** (la «reinversión necesaria»). Las empresas casi nunca publican ese reparto entre mantener y crecer. En Elis, por eso, el resultado es «faltan datos».
- **La pregunta no es de software:** es una elección económica, y por las reglas solo la puedes hacer tú. Sin ella, el motor A de Ahold y de Jumbo acaba en «faltan datos» o en «límite del modelo».
- **Opciones** (en las tres, el personaje muestra la sensibilidad y dice qué supuesto usa):
  - **(a) Como en Elis:** sin un dato publicado o una estimación documentada, la empresa queda en «faltan datos». Es lo más estricto. Con esto el examen probablemente no puede dar ningún «Sí» en el motor A.
  - **(b) Una regla general escrita, igual para todas las empresas:** si la empresa no publica el reparto, la reinversión necesaria se iguala a su **amortización propia** (sin los alquileres), como hipótesis declarada y no como dato. Es el perímetro que la propuesta F1 llama A2. El personaje lo presenta como «condicionado a esta hipótesis», con su sensibilidad.
  - **(c) Empresa por empresa,** con una estimación documentada (método, rango y responsable). Es lo más fino, pero no cabe en los días que quedan.
- **Mi recomendación:** (b), decidida una vez y por escrito para todas, como la tasa. Así no se elige empresa a empresa según convenga (la misma regla que «no bajar la tasa para la empresa que a uno le gusta»). **Lo que me haría estar equivocado:** en negocios que crecen mucho, o con inflación alta, la amortización puede quedarse corta como medida del mantenimiento y la regla sobrevaloraría; la sensibilidad lo tiene que enseñar.

## F1-B · Las compras de empresas en Ahold (decisión (4b), tomada para Elis)
**DECIDIDA el 18-nov: (B) como crecimiento, para todas salvo Elis.** 

- **Qué pasa.** En Elis decidiste la opción A: las compras de empresas quedan pendientes mientras no se sepa si mantienen o hacen crecer el negocio. Ahold compra empresas grandes (por ejemplo, Profi en 2025 y el negocio de Tesco en Chequia y Eslovaquia, anunciado para 2027).
- **Opciones:** (A) lo mismo que en Elis: pendiente, y Ahold quedaría en «faltan datos»; (B) tratarlas como crecimiento, como hipótesis declarada y revisable.
- **Mi recomendación:** lo que decidas en F1-A arrastra a este punto: con (b) en F1-A, aquí (B), con la misma regla escrita para todas las empresas del examen.

## F1-C · Un hueco que quedó tras las dos rondas de F1-IMPL (R2-1) · **ya no hace falta decidir**: la revisión de la V6.3.1 lo volvió a encontrar (V631-1) y se corrige dentro de la primera ronda de esa pieza
- **Qué pasa.** Relanzar un expediente **antiguo** (cerrado antes de F1) con la combinación `--reiniciar --desde 13` puede dar todavía una ficha «Sí · comprar» sin pasar por F1. Los expedientes nuevos del examen quedan protegidos.
- **Opciones:** (a) **recomendada:** una tercera ronda mínima (cuatro líneas que el revisor ya probó en una copia: el motor se lee de `fase_a.json`), con una comprobación del revisor; (b) solo una regla de trabajo: nunca usar `--reiniciar` junto con `--desde` (mientras tanto, el coordinador la aplica).

## A-Q3 · Ahold: ¿doce últimos meses hasta junio (informe del 2T) o hasta septiembre (informe del 3T, 4-nov-2026)?
**DECIDIDA el 19-nov: (a) 3T.**
- **Qué pasa:** la etapa 1 y el expediente `ahold_f3` usan los doce meses hasta el 2T 2026. El informe del 3T se publicó el 4-nov-2026, antes del precio que usamos (13-nov), y ya está en las fuentes del expediente. La revisión independiente lo señala como cifra no vigente (`revisiones/expedientes_f1/REVISION_ORQUESTACION_R2.md`).
- **Efecto conocido:** EV/EBITDA 6,59x (2T) frente a ≈6,53x (3T); con las acciones a 27-sep-2026, ≈6,43x. La caja de los doce meses y otras cifras del último año también cambiarían. La fase A de `ahold_f3` se está haciendo con el 2T.
- **Opciones:** (a) **recomendada:** pasar a los doce meses hasta el 3T en un expediente nuevo (`ahold_f4`) y repetir la fase A, porque es lo más reciente publicado antes del precio; (b) quedarse en el 2T, como la etapa 1, declarando la desalineación en cada cifra afectada.

## Z-ACC · Zoetis y Ahold: acciones de cierre de año frente a balance de mitad de año (fechas desalineadas)
**DECIDIDA el 19-nov: mantener.** Por P-O2 se usan las acciones al cierre del ejercicio (31-dic-2025), pero la deuda y la caja del EV son del 30-jun-2026. En Zoetis, con las acciones del 30-jun (414,15 M) el EV/EBITDA bajaría de 9,68x a ≈9,48x. **Recomendación:** mantener P-O2 tal cual y declarar la desalineación en la nota de cada cifra (como en Jumbo); no cambia ninguna conclusión.

## A-NIC17 · Ahold: deuda de 2016 y 2017 con arrendamientos financieros de la norma antigua (NIC 17)
**DECIDIDA el 19-nov: dejarla.** La fila «deuda sin arrendamientos» de 2016–2017 incluye los arrendamientos financieros de la norma antigua, porque así se publicaban (antes de la NIIF 16). **Recomendación:** dejarla como se publicó y declararlo (son años fuera de la base de caja 2023–2025 y no mueven la conclusión); la alternativa es restarlos con la nota de arrendamientos de esos años.

## M-BYTES · Datos de mercado sin archivo guardado (bloquean «apto por entradas»)
**PENDIENTE (19-nov).** El programa solo acepta como comprobado un dato de mercado si el archivo original está guardado con su huella. Faltan: Jumbo, precio 27,28 € del 17-nov (la captura de Euronext Athens de la persona) y Bund a 10 años del 17-nov; Damodaran (margen del sector) de Ahold, Jumbo y Zoetis. Propuesta: la persona sube a la Release la captura y las páginas guardadas como PDF; las lecturas de terceros C38 (valor intrínseco de webs) y C88 (P/FCF de terceros) se declaran «no materiales» con justificación que sella un revisor, sin subir nada.

## Z-MIN · Zoetis: minoritarios negativos (2022: −2; 2023: −6 mm USD)
**DECIDIDA el 19-nov: (a) cero con aviso.** El libro exige minoritarios ≥ 0 (Convenciones V6.3 §8; Motor!E234; validación de Historia!C26:L26; el puente del motor B los resta). Hoy el programa los guarda en positivo (+2, +6), que no es la cifra publicada. Opciones: (a) **recomendada:** tratarlos como 0 con aviso y la cifra impresa en el registro (como el superávit de pensiones); (b) restarlos con su signo (cambia la plantilla); (c) dejarlos en positivo (no es exacto y el registro seguirá en discrepancia). Efecto económico nulo: en 2025 son 0 y el puente usa 2025.

## Z-R · Zoetis: agrupación geográfica que fija la r mínima (A31/B31, A33/B33)
**DECIDIDA el 19-nov: dejarla.** El sellado del registro señala que la agrupación de ventas por regiones no corresponde a las etiquetas del informe; esa agrupación fija la tasa mínima. **Recomendación:** dejarla como está y anotar la diferencia (la r usada es el 9 % fijo de la política; la mínima solo es un control).

## V-CIRC · Vinci: el capital circulante en la reinversión (bloqueo F1-K3c)
**DECIDIDA el 19-nov: (a).** En la etapa 1 la persona excluyó el circulante de la caja base (C46, Control maestro M43): VINCI cobra por adelantado en construcción y su circulante da entradas de caja (10,5 bn en 2016–2025). El motor A, en cambio, cuenta ese circulante dentro de la reinversión (fila 30) y lo resta otra vez. El coordinador había propuesto convertir el bloqueo en aviso; la revisión independiente (`revisiones/vinci_montaje/REVISION.md`) mostró que eso contaba el circulante dos veces, y se retiró. Opciones: (a) **recomendada por coherencia con la decisión M43:** circulante a 0 también en la reinversión, con un mecanismo declarado (ni entradas ni salidas de circulante); (b) contar el circulante en la caja base (revoca M43); (c) dejar la salida de circulante como hipótesis conservadora declarada. El efecto en el flujo sin crecimiento es grande (≈ 3.016 con la doble exclusión frente a ≈ 5.191 con (a)); se presentará calculado antes de la fase A.
- **Actualización (19-nov, diagnóstico calculado, `vinci/resultados/diagnostico_k3c_vinci.md`):** (c) flujo sin crecimiento 3.016, f 4,49 %, se declara como hipótesis de la persona y el bloqueo pasa a aviso (inmediato); (a) 5.191, f 1,57 %, caja base enseñada 4.419 — **requiere un cambio de producto** (campo declarado de normalización del circulante en la capa F1 y una fila nueva del libro, con pruebas y revisión; del orden de medio día); (b) 5.191, f 1,57 %, caja base enseñada 6.509 — revoca M43 y además necesita una justificación coherente. (d) también es posible: no tocar nada y dejar que el programa trate el motor A de Vinci como no utilizable (F1-K3c bloquea) y siga con lo que el producto prevea; no se recomienda elegirla por el resultado que dé.

## V-ANCLA · Vinci: ¿el circulante tampoco cuenta en la referencia de «cuánto capital hace falta para crecer»?
**PENDIENTE (19-nov).** Con V-CIRC (a) el circulante no entra ni en la caja base ni en la reinversión. Queda una tercera pieza: el ancla de ventas sobre capital (S2C) que el personaje usa para estimar cuánto hay que invertir por cada euro de crecimiento. Si también se excluye el circulante ahí (lo coherente con «ni entradas ni salidas»), el ancla de VINCI pasa de 5,96 a 2,32: crecer cuesta más capital y los escenarios con crecimiento valen menos (es la opción prudente). Si no se excluye, el ancla queda en 5,96 (crecer saldría casi gratis gracias a los anticipos de clientes, que es justo lo que la persona no quiso contar como caja). **Recomendación:** excluirlo también (2,32), por coherencia. Límite declarado en ambos casos: el capital del balance (ROIC medio 10,5 %) sigue incluyendo el circulante negativo. Revisión: `revisiones/circulante_normalizado/REVISION.md`.
