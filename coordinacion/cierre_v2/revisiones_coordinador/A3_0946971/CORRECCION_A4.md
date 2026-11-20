# Corrección A4 · frente A (M2, cobertura VM) · sobre `0946971` (respuesta A3)

- **Para:** Mistral A, rama `mistral/m2-cobertura-vm`. Va **después** de la revisión de G-RAIZ (`integracion/hechos-raiz-957af65` @ `3d66437`), que sigue pendiente y estaba asignada antes que A3.
- **De:** el coordinador, según [REVISION_A3_0946971.md](REVISION_A3_0946971.md), hecha por un contexto distinto del autor, sin red y sin LibreOffice.
- **Comprobado por el coordinador en `0946971`:** en `verificacion_contexto.jsonl`, Vidrala `Historia!J6` y `J7` llevan como texto declarado «sí: 2023 reexpresado sin (Vidrala) Italia…» y la reexpresión sale CONFLICTO «declara no reexpresado». Es la polaridad invertida.

## Clasificación

- **R7:** cerrado.
- **R1, R5 y R6:** cerrados con límites.
- **R2, R3, R4 y R8:** abiertos.

**Se conserva:**
- la reproducción: 192 de 196 salidas byte a byte; las 4 diferencias son de marca de tiempo, ruta y ENTREGA;
- todas las sondas de cierre de la revisión A2;
- los 79 CONFLICTO de columna, que pasan a OK;
- la eliminación del atajo de 18 entradas: quedan PENDIENTE, incluidas las promociones 28/35;
- la propagación transitiva de derivados;
- **ninguna entrada en REVISADO sin todas sus dimensiones**;
- el manifiesto, 196/196.

**Cambio en los datos reales:** el CSV pasa de 169/209/133 a **209/283/19** (REVISADO, PENDIENTE y CONFLICTO). Ninguno de los 15 CONFLICTO de fuente examinados es un conflicto real: 13 son artefactos nuevos de R3 y R4, y 2 (B46 y B47) son el defecto 8 de A2, que persiste.

## Defectos

| | Defecto, con contraejemplo mínimo (detalle en el informe) | Prueba de cierre |
|---|---|---|
| **A4-R1 (material, R4)** | **Polaridad invertida:** «sí: … reexpresado sin …» con diferencia da CONFLICTO «declara no reexpresado». Afecta a 5 entradas reales: Vidrala `Historia!J6`, `J7`, `J8`, `aux:bai_2023` y `aux:impuesto_2023`. Dos de ellas, J7 y bai_2023, pierden REVISADO sin contradicción. **Negación no reconocida:** «None of the comparative figures were restated» o «reexpresión: ninguna» con diferencia dan OK «reexpresión confirmada» | La polaridad se decide por la declaración (sí o no) y no por palabras sueltas como «sin». Las 5 reales y las sondas del informe dan el estado esperado |
| **A4-R2 (material, R3/R4)** | El cambio de R3 es global: los años de la línea de cabecera y de los rótulos cuentan como importes. Además, el rótulo se compara quitando los dígitos, de modo que «At 31 December 2015» equivale a «…2017». Da CONFLICTO falsos reales en `D25`, `E25`, `F25`, `G25`, `H25` y `aux:ing_fin_2017`; y un valor no numérico («EUR») da CONFLICTO en Viscofan `Palancas!C48` y `Control maestro!H4` | Tratar como importe solo los tokens de la fila de datos, nunca los de la cabecera ni del rótulo. Comparar el rótulo con sus fechas. Un valor no numérico da NO_APLICA. Regenerar y listar los estados que cambian |
| **A4-R3 (material, R2)** | El desempate por la cabecera más próxima crea OK falsos que antes eran CONFLICTO: «Notes 2025 2024» / «* 2024 and 2025 figures restated» / fila; cabecera partida en dos líneas con «Goodwill 1.500 -». La cabecera real «EQUITY AND LIABILITIES Note 2025 2024» se descarta como frase. 61 OK reales, 56 de ellos REVISADO, se apoyan en el título «31 December … and …» | Una cabecera solo vale si es tabular e inequívoca para esa fila; si no, NO_DECIDIBLE. Revisar las 61 |
| **A4-R4 (R4)** | La escala y el perímetro se comparan solo por página: una página con tabla consolidada e individual, o con «(in millions)» en la página anterior, da NO_APLICA «coherente». Siguen las tablas de movimiento (B46, B47 y el M1 `CF2024_p9`) | Comparación por tabla. Tablas de movimiento: NO_DECIDIBLE salvo con un mapeo explícito |
| **A4-R5 (R8)** | `ENTREGA.json` no es la salida del generador y publica una huella errónea (`…c3568c2…` en lugar de `…c3558c2…`, la de `control_cobertura.json`). `base_revisada_sha` y `naturaleza` están desfasados. El motivo de AR2025_p27 es inexacto en RESUMEN y PUNTO. HALLAZGOS da 97 donde son 101. El docstring de `cola_pendientes` da 26 donde son 50. `RESPUESTA_A3` afirma cosas que no se cumplen («las que pierden quedan PENDIENTE», «G25 reparado»). `actualizar_textos_resumen.py` sale con código 1 si se ejecuta otra vez. La guarda de pypdf es `>= 6.0` y el mensaje dice `>= 7.0`. Las salidas publicadas llevan rutas del entorno | ENTREGA idéntica a la salida del generador. Textos generados o corregidos. Idempotencia. Una sola versión mínima de pypdf. Rutas sustituidas en las salidas |
| **A4-R6 (menor, R1/R5/R6)** | U+2013 («–7.660») e importes < 1 («0,21») dan CONFLICTO. Un «2025» sin puntuar acredita la versión. «Cifras en millones», «(€m)», «MEUR» y «(M€)» dan OK. Ninguno tiene casos reales hoy | Corregido, con sondas |

## Entrega

- Un commit por punto, con ENTREGA generada.
- Para cada A4-R: las sondas del informe, una variante propia y la lista de entradas que cambian de estado.
- Ninguna entrada pasa a REVISADO sin todas sus dimensiones.
- No sustituir cifras ni fuentes.
- El coordinador revisa solo lo afectado.
