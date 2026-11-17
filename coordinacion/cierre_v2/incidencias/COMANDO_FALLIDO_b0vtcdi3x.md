# Comando en segundo plano «fallido» · `b0vtcdi3x` · análisis (17-nov-2026)

**Qué muestra la interfaz.** «1 fallidos» en los comandos en segundo plano de la sesión del coordinador. Es el único de la sesión que terminó con un código distinto de 0. Otros cuatro se detuvieron (`[killed]`), lo que no es un fallo de prueba:
- tres por cortes o relanzamientos;
- `bqnfftqeg`, la verificación completa de la candidata, por el reinicio del contenedor. Se relanzó como `b51s9e5z9`: PASA, código 0.

**Tarea.** La respuesta a la revisión n.º 8 del verificador (C18), el 16-nov a las 08:27 UTC: volver a ejecutar sobre C18 los scripts de los revisores 1–8 que dependen del verificador.

**Comando:**

```
bash <scratchpad>/c18/revisores_C18b.sh; echo "fin del lanzador $?"; \
grep -c "código 0" <scratchpad>/c18/revisores_C18b.log; \
grep -B1 "código [1-9]" <scratchpad>/c18/revisores_C18b.log
```

**Salida** (`b0vtcdi3x.output.txt`): `fin del lanzador 0`, `26` y `[exited with code 1]`.

**Causa.** El último `grep` busca pasos con código distinto de 0. No encuentra ninguno, y `grep` sin coincidencias devuelve 1. Ese 1 es el código de todo el comando compuesto. **No falla ningún paso:**
- `revisores_C18b.log`: 26 de 26 pasos con «código 0»;
- el lanzador termina con 0;
- los dos pasos que no se repitieron, `umbral7` y `sondas8`, dieron «código 0» en la primera pasada (`revisores_C18_pasada1.log`).

En total, 28 pasos con código 0: es la cifra que declara la respuesta a la revisión n.º 8 (`revision/RESPUESTAS_AUTOR_1.md`, C18).

| | Esperado | Observado |
|---|---|---|
| Pasos de los revisores | 26 con código 0 en esta pasada | 26 con código 0 |
| Lanzador | 0 | 0 |
| Último `grep` | sin coincidencias, código 1 | sin coincidencias, código 1 |

**Clasificación.** Es un negativo esperado del propio comando de comprobación (la ausencia de fallos), no un fallo de prueba ni de producto.

**Impacto.** Ninguno en pruebas, entregas ni revisiones. C18 y lo posterior (C20, CSV) no cambian. No hay nada que corregir en el producto ni que repetir.

**Corrección de procedimiento** (sustituye a la propuesta inicial «`grep … || echo`», que no basta: el código 1 de grep «sin coincidencias» seguiría confundiéndose con el 2 «no se puede leer», y el `echo` taparía los dos).

Los lanzadores usan ahora `../herramientas/lanzador_comun.sh`, que propaga el resultado de los pasos (también un `cd` o una copia fallidos). Los registros se comprueban con `../herramientas/comprobar_registro.py`, que da 0 sin fallos, 1 con fallos, 2 ante un error de lectura o un registro mal formado y 3 si el número de pasos no es el esperado. Pruebas: `../herramientas/test_herramientas.out`, 18/18; el registro real de C18 da 0.

Según el contraste de ChatGPT, no hay que repetir las 26 comprobaciones por este aviso.
