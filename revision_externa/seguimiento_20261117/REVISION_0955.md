# Contraste externo del informe de las 09:55 UTC · 17-nov-2026

Referencia auxiliar: coordinacion/cierre-v2 @ 5bf5a6ad8671642302f57a57183a45095e415c4d.
Revisor: ChatGPT, contexto distinto del autor de las herramientas. No se adopta política económica.

## Confirmado

- Candidata producto: 31491289a9a13a670dd563c1b2df85dad54eb74a.
- Comparación Git con 957af652cdc3bef3d67e8623c9572138bac685e9: solo cuatro archivos modificados.
- Los blob SHA de los cuatro coinciden con c0542b83b9923f98124d3c72e48b7fc7245284d2: CAMBIOS_ARCHIVOS.txt, CONTINUIDAD.md, MANIFIESTO_SHA256.txt y personaje_v2/GUIA_RECORRIDO_SUPERVISADO.md, dentro de munger_v2_r1/.
- Se descargaron a una carpeta temporal las tres herramientas publicadas y el registro C18. Comando ejecutado: bash test_herramientas.sh revisores_C18b.log. Resultado: 18 correctos, 0 fallidos; salida 0.
- Esto no reproduce las 26 comprobaciones históricas ni la materialización/manifiesto completo de 7762 archivos.
- D @5f4b2a2 y F @98bdf8f constan entregados. Su contenido sustantivo no queda aceptado por este contraste.
- T-TRASPASO y los 36 Qwen no se ejecutaron en este contraste.

## Corrección acotada pendiente: integridad del cierre del registro

En comprobar_registro.py, FIN solo comprueba un prefijo y activa un booleano. No rechaza pasos posteriores al cierre ni contrasta los campos del resumen ampliado del lanzador con los pasos realmente leídos.

### S1: pasos después del cierre

Registro exacto:

```text
== primero 10:00:00
   código 0
fin 10:00:01
== segundo 10:00:02
   código 0
```

Ejecutado con python3 -I comprobar_registro.py CASO.log --json.
Observado: salida 0, "2 pasos, todos con código 0".
Esperado para este registro estructuralmente inconsistente: salida 2.
Una línea fin anterior no debe acreditar el cierre de pasos posteriores.

### S2: resumen ampliado contradictorio

Registro exacto:

```text
== primero 10:00:00
   código 0
fin 10:00:01 · ejecutados 1 · esperados 1 · fallidos 1 · resultado 1
```

Mismo comando.
Observado: salida 0, "1 pasos, todos con código 0".
Esperado: salida 2 por inconsistencia entre resumen y pasos.
El programa anuncia éxito aunque el cierre declara un fallo.

## Cierre solicitado

- Un único cierre, después de todos los pasos; rechazar pasos/códigos posteriores y cierres múltiples.
- Validar completamente los campos del resumen ampliado, si existen: ejecutados, esperados, fallidos y resultado, con las reglas del lanzador. Conservar la compatibilidad explícita con el formato histórico fin HH:MM:SS.
- Añadir estas dos contrapruebas y positivos de ambos formatos; conservar los 18 casos existentes.
- Registrar causa y salida 2 para registros inconsistentes. Los fallos reales siguen siendo 1, y el desacuerdo de recuento válido sigue siendo 3, conforme al contrato publicado.
- Revisar únicamente las herramientas y su evidencia. No repetir las 26 comprobaciones de C18 ni la batería completa de la candidata por este cambio del auxiliar.

Este hallazgo afecta a la confianza del comprobador de registros, no demuestra un fallo de las pruebas C18 ni invalida la integración documental ya contrastada.
