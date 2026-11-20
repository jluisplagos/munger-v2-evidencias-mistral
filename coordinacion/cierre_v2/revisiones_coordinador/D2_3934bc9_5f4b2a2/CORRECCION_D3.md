# Corrección D3 · frente D (aceptación Qwen) · sobre `3934bc9` y `5f4b2a2` (respuesta a D2)

- **Para:** Mistral D, rama `mistral/d-qwen-aceptacion`.
- **De:** el coordinador, según [REVISION_D2_3934bc9_a_5f4b2a2.md](REVISION_D2_3934bc9_a_5f4b2a2.md).
- **Comprobado por el coordinador:** `sha256sum -c MANIFIESTO_SHA256.txt` en `5f4b2a2` da código 1. Fallan 11 archivos, y `generar_correspondencia.py` no está en el manifiesto.

**Clasificación: correcciones materiales.** D-HARNESS y D-36 no quedan aceptadas.
- D2-R7 queda cerrado con límites en el código.
- **Se conserva:**
  - las sondas originales P1–P3, P5, P8 y P9, cerradas tal como estaban escritas;
  - el SHA observado, la huella de la especificación y la del banco;
  - `base_414.py verify` sin `|| true`;
  - la declaración de **0 casos del personaje ejecutados**, que es correcta.

## Defectos

| | Defecto, con su contraejemplo (detalle en el informe) | Prueba de cierre |
|---|---|---|
| **D3-R1 (material, R1 c/d)** | Las variantes abren huecos equivalentes:<br>- `copiar_artefacto` con `../../Q1-036/…` da COMPONENTE_OK;<br>- `comprobar` con `guardar="../Q1-036/…"` sobrescribe la evidencia de otro caso;<br>- un resultado v3 de 4 campos con `spec_sha256` da CUMPLE sin volver a evaluar;<br>- las aserciones sobre el propio `ejecucion.log` dan OK sin mirar el producto;<br>- `"id": "."` borra la evidencia de todos los casos antes de validar | Toda ruta, también la de salida, se resuelve dentro del `RUN_DIR` del caso o da ERROR. La matriz reevalúa las aserciones. Las aserciones no pueden leer archivos que escribe el propio arnés. El id se valida antes de tocar el disco. Las sondas de las variantes del informe dan el estado esperado |
| **D3-R2 (material, R2)** | La prueba 15 solo comprueba que las aserciones fallan sin archivos. Q1-027 C4 (`apto=false`) pasa sobre el estado previo y sigue contando. Q1-034 C1 falla siempre: el paso 5 cambia la clase, y es tautológico. Q1-026 C1 da CUMPLE con un fallo ajeno que imprima los prefijos, y con el stderr real falla, por el prefijo `ipal` | El control negativo de cada aserción se hace contra el **estado previo** del caso. C4 fuera del cómputo o cambiado. Q1-034 C1 evaluado sobre el estado de su paso. Q1-026 C1 anclado al mensaje real y a su origen |
| **D3-R3 (material, R3)** | La especificación y el generador están corregidos, pero **lo publicado no se ha regenerado**. Al regenerar: 29 «ERROR (COMPONENTE_OK)», 1 BLOQUEO_ENTORNO y 0 CUMPLE, frente a los 30 CUMPLE publicados. Q1-026 sale como BLOQUEO_ENTORNO sea cual sea su resultado. El CAMBIO no lleva la deuda 300 | Regenerar con v3 la evidencia y todo lo publicado: MATRIZ, MAPA, relevo, recuentos, log, HALLAZGOS, RESUMEN y ENTREGA. La clasificación de Q1-026, desde su resultado. El CAMBIO, con las cifras del banco y el cálculo de la deuda neta |
| **D3-R4 (material, R4)** | 30 relevos quedan sin paso de agente: el generador solo lo añade en PARCIAL_COMPONENTE. En Q1-028 y Q1-032, `comando_relevo` sigue en null | Cada relevo, completo, con lo que exige `MECANISMO_PERSONAJE.md` §4: qué estado preparar, qué pasos y fases recorrer con agentes reales, qué entrada se carga y qué artefacto se observa por criterio |
| **D3-R5 (R5)** | `preserva_sentido` vale «si» en los 36 casos, con la misma frase en 35; es falso al menos en Q1-001, Q1-032 y Q1-034. `MAPA_CRITERIOS_BANCO.csv` no está publicado y sobredeclara cobertura (Q1-027 índices 0 y 2; Q1-026 índice 2; Q1-025 índices 0–2; Q1-034 índice 0) | Justificación por caso. Mapa publicado, con «sin aserción» donde no la haya |
| **D3-R6 (R6)** | Manifiesto: 11 fallos y un script fuera de la lista | `sha256sum -c` con código 0 y la lista igual a la carpeta |
| **D3-R7 (menor)** | Faltan marcas SIMULADA en el `--revisor` del `sellar` de una especificación y en la comprobación «pendiente» por defecto. Hay 8 casos publicados sin marca. Con `ARNES_EVIDENCIAS_LIMPIAS=0` los logs se acumulan sin registrarlo. Hay un `KeyError` (`good`) en el mensaje final de `verify` | Corregido, con una prueba por punto |
| **D3-R8** | `ENTREGA.json` no cambia desde `1ac661b`, y no hay entrega por bloque con comandos, códigos y salidas | Una ENTREGA por bloque, con D3-R1…R8 |

**Lo que no es de Mistral D:** ejecutar el personaje con agentes reales. Lo hace el runtime del coordinador cuando los relevos estén completos (D3-R4).
