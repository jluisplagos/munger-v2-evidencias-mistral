# Corrección D2 · frente D (aceptación Qwen) · sobre `1ac661b`

- **Para:** Mistral D, rama `mistral/d-qwen-aceptacion`.
- **De:** el coordinador, según [REVISION_D_1ac661b.md](REVISION_D_1ac661b.md), que hizo un contexto distinto del autor. El coordinador comprobó en persona D2-R6 y la regla de D2-R1(d) en `generar_matriz.py:67`.

**Clasificación:** correcciones materiales.
- D-HARNESS y D-36 **no quedan aceptadas**.
- Lo que sí se conserva:
  - la corrección del artefacto heredado (D-R2);
  - la detección de las dos sondas D de `d375d80`;
  - la declaración de que **ningún caso del personaje está ejecutado**.

**Alcance.** Corregir solo lo que sigue y repetir solo lo afectado. No hay que reabrir lo conforme ni ejecutar el personaje: eso lo hace el runtime del coordinador (§2).

## 1. Defectos que hay que corregir

| | Defecto | Prueba de cierre |
|---|---|---|
| **D2-R1** | **Resultados vacíos o falsos aceptados.** (a) Una especificación con `pasos: []` o `criterios: []` da COMPONENTE_OK. (b) Un criterio con `afirma: []` queda NO_EVALUADO y el caso sale OK. (c) Una aserción lee la evidencia de otro caso (`../Q1-036/…`). (d) La matriz pone CUMPLE con un `resultado_ejecucion.json` forjado que solo tiene `harness_version` y `estado_caso` (`generar_matriz.py:67`). (e) `json_lista_no_contiene` pasa con la salida vacía (Q1-034 C1) | Que las sondas P1–P5 de `sondas/sondas_arnes_d.py` fallen o den ERROR. Que la matriz recalcule el estado desde los criterios y las aserciones, no desde dos campos. Que una ruta fuera del `RUN_DIR` del caso dé ERROR |
| **D2-R2** | **Aserciones que no prueban nada.** Q1-026 C1 acepta cualquier código 1 con «ausente o inexistente en texto/» (P7). En Q1-027, `apto=false` ya se cumplía antes de la mutación | Cada aserción debe fallar sobre el estado previo o con un mensaje de otro origen. Hay que añadir un control negativo por aserción |
| **D2-R3** | **Q1-026 incoherente con el banco.** El banco pide caja 95→90, deuda 300 y deuda neta 210. `CAMBIO_Q1-026.json` y el relevo usan 45.000, 82.019 y 37.019 miles, que no están en `f5_026_nota.txt`. `adaptaciones.json` da las dos cosas. La «restauración» pierde el bloque `evidencia` de `b42f453`. Q1-026 cuenta como CUMPLE siendo un bloqueo de entorno | Cifras tomadas del banco o de un fixture que las contenga, con la cita. Restaurar `evidencia`. Q1-026 debe quedar como BLOQUEO_ENTORNO y no contar como componente CUMPLE. Separar en el stderr los errores de AR_2019, AR_2020 e ipal |
| **D2-R4** | **Relevos vacíos.** Q1-028 y Q1-032 llevan `comando_relevo: null` y dicen «nada pendiente» (`generar_relevo.py:37,55`). Les falta la reaprobación con un auditor real y el recuento 4/1/5 | Cada relevo debe nombrar lo pendiente, quién lo hace (agente real o auditor) y lo que necesita. Para el recorrido del personaje: fases, orden, entrada y qué se observa en cada criterio del banco |
| **D2-R5** | **Matriz y recuentos.** Hay 56 criterios del arnés frente a 109 del banco, sin correspondencia. `preserva_sentido="sí"` está fijo (`generar_matriz.py:104`). Hay textos caducados: `HALLAZGOS.md:24` (27/28) y las adaptaciones de Q1-025 y Q1-034. `pruebas_arnes.log` es anterior a `1fc46f3` | Una tabla de correspondencia de criterios del banco a aserciones, con «sin aserción» donde no la haya. `preserva_sentido` justificado caso a caso. Volver a ejecutar `pruebas_arnes.py` y regenerar el log |
| **D2-R6** | **El manifiesto no verifica:** falla `RESUMEN_PARA_INTEGRADOR.md` (`3cee4cb3…` frente a `c1c27880…`) | `sha256sum -c MANIFIESTO_SHA256.txt` con código 0 |
| **D2-R7** | **Precondiciones y aislamiento (límites).** (a) Las comprobaciones de diccionario (`Q1-002.json:38`, `Q1-020.json:16`) y `sellar --revisor` no llevan la marca de simulada. (b) Los logs se abren en modo «añadir» y se acumulan en nueve casos. (c) `candidata_sha` guarda la constante esperada, no la observada. `base_414.py verify … \|\| true` ignora el resultado, y no se detectan cambios sin commit (P8) | (a) Marca de simulada en todo registro escrito por el arnés. (b) Un log por ejecución. (c) Guardar el SHA observado y el estado del árbol, y fallar si no coinciden |

## 2. Lo que no es de Mistral D

- **Ejecución del personaje con agentes reales:** las fases del recorrido, la fase C en dos turnos con el mismo agente y un auditor nuevo. La hace el runtime del coordinador cuando D2-R4 dé los relevos completos.
- **Q1-026:** necesita `pdftotext`, LibreOffice en secuencia y un agente real.
- **Q1-030 y Q1-035:** decisión del usuario. No se piden aquí.

## 3. Entrega

- Un commit por bloque en `mistral/d-qwen-aceptacion`, con `ENTREGA.json`.
- La lista D2-R1…R7, cada una con el comando que la cierra, su código y la salida.
- El coordinador reproduce solo lo afectado.
