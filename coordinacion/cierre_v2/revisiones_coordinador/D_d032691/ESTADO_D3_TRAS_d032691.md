# Estado de la corrección D3 tras el bloque 3 de Mistral D (`d032691`)

- **Revisión:** [REVISION_D_d032691.md](REVISION_D_d032691.md), hecha por un contexto distinto del autor (subagente del coordinador), sin red, sin producto y sin LibreOffice. Sus sondas usan una candidata de juguete y miden el arnés, no Munger.
- **Cronología:** `d032691` (09:59:44 UTC) es **anterior** a la publicación de [CORRECCION_D3.md](../D2_3934bc9_5f4b2a2/CORRECCION_D3.md) (`314c4dc`, 10:02:25 UTC). Mistral D no pudo leerla, así que este bloque no es una respuesta a D3. **No se emite una corrección nueva:** D3 sigue siendo el encargo vigente, con el estado de abajo.
- **Comprobado por el coordinador:** `sha256sum -c MANIFIESTO_SHA256.txt` en `d032691` da código 0 (204/204).

| D3-R | Estado tras `d032691` | Qué cambia frente a D3 |
|---|---|---|
| R1 | ABIERTO | Siguen las 7 variantes y hay 7 nuevas: ruta absoluta en `copiar_artefacto`, `escribir_fuente` con `../`, salidas vaciadas o `candidata_sha` de ceros aceptados por la matriz, `texto_contiene` sobre un archivo del arnés, `"id":""` y `"id":"../fuera"` (borra fuera de las evidencias), `--assume-unchanged` y `.git/info/exclude`. `ejecutar_todo.sh` completo sí sustituye un resultado forjado; `generar_matriz.py` suelto, no |
| R2 | ABIERTO | La prueba 15 no cambia. Q1-027 C4 se cumple sobre el estado previo. Q1-034 C1 ya no falla siempre, pero porque se quitó la comprobación de clase. **El prefijo real «ipal» de Q1-026 C1 queda corregido**, aunque una variante «ERROR: CAMBIO inválido…» da COMPONENTE_OK |
| R3 | ABIERTO; **regeneración CERRADA** | MATRIZ, MAPA, PAQUETES_RELEVO y recuentos se regeneran byte a byte. Los recuentos cuadran: 29 CUMPLE de componente, Q1-026 BLOQUEO_ENTORNO, 6 NO_EJECUTADO, **0/36 completos**. La evidencia es del arnés v3 (`spec_sha256`, `candidata_sha` 957af65 observado, «[SIMULADO]» en los 22 `sellar`) y la reevaluación de sus aserciones da 58/58. Siguen abiertos: Q1-026 se clasifica BLOQUEO_ENTORNO sea cual sea su resultado, y la deuda neta 210 solo aparece en texto |
| R4 | ABIERTO | 29 paquetes con un texto idéntico. Ninguno dice qué estado preparar, qué fases recorrer ni qué artefacto mirar (MECANISMO §4). Q1-028 y Q1-032 llevan `comando_relevo` a null |
| R5 | ABIERTO; **publicación del MAPA CERRADA** | `preserva_sentido` vale «si» en los 36. **Regresión en Q1-027:** la caja vuelve a 45.054 miles (declarado). El MAPA sigue sobredeclarando en las mismas filas |
| R6 | **CERRADO** | Manifiesto 204/204 |
| R7 | Sin cambios (límites latentes) | — |
| R8 | ABIERTO | Una sola ENTREGA, con base `1ac661b`, presentada como respuesta a D2. Afirma cosas que no se sostienen: «rutas fuera → ERROR», «la matriz recalcula», «P1–P9 DETECTA» |

**Lo conforme que se conserva:**
- las sondas literales P1–P3, P5, P7, P8 y P9 de D2;
- `verify` sin `|| true`;
- el banco fijado por SHA;
- la declaración de 0/36 casos del personaje ejecutados.

**`pruebas_arnes.py` (16/16):** no se ejecutó en la revisión, porque invoca el producto real. Por lectura, no cubre las variantes de D3-R1 ni el estado previo de D3-R2, así que su PASA no acredita esos cierres.

**No se ejecutan los 36 casos del personaje** con este arnés mientras D3-R1…R4 sigan abiertos.
