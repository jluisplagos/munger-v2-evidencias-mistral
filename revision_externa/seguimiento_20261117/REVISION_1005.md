# Contraste externo del informe de las 10:05 UTC · 17-nov-2026

Auxiliar consultado: coordinacion/cierre-v2 @ 314c4dcfb21e29d2b6023538838a5bbe33ef414b.
Producto: candidata 31491289a9a13a670dd563c1b2df85dad54eb74a, sin cambios desde el contraste anterior.
Contexto revisor: ChatGPT, distinto del autor de las herramientas.

## Cierre del hallazgo REVISION_0955

Se leyeron íntegramente las tres herramientas publicadas (comprobar_registro.py, lanzador_comun.sh, test_herramientas.sh) en el SHA auxiliar anterior. Se guardaron sin modificar en /tmp/munger_revision_1005/, con revisores_C18b.log del mismo SHA.

Comando realmente ejecutado:
```text
bash test_herramientas.sh revisores_C18b.log
```

Salida final: 30 correctos, 0 fallidos. Código de salida: 0.

Incluye:
- S1, pasos después de fin: ahora salida 2.
- S2, resumen contradictorio: ahora salida 2.
- Compatibilidad histórica C18: 0.
- Fallo real: 1; fallo de lectura/formato: 2; recuento coherente discordante: 3.
- Positivos históricos y ampliados.
- Los 18 casos anteriores y los 12 añadidos.

**Veredicto: cerrado el hallazgo acotado de integridad del cierre del registro documentado en REVISION_0955.**
No se exige otra ronda por ese hallazgo. No se reejecutaron C18 ni la batería completa del producto; no se acredita aquí aptitud económica.

## Otros contrastes de este informe

- HEAD remotos coinciden con el informe para candidata, main, D d032691, A d11ee44, E f00c5dd y F 98bdf8f.
- Leídas CORRECCION_D3.md y CORRECCION_F3.md en el control publicado. Las revisiones de Claude no se convierten por ello en reproducciones propias de ChatGPT.
- F3-R5: comprobado directamente en build_v6.py de un checkout fijado en 957af652cdc3bef3d67e8623c9572138bac685e9. Análisis C62 elige A/B/C; Palancas C6 alimenta el aviso de coherencia y la restricción V11 para financieras en A/B. El código no cambia en 3149128.
- D d032691 es posterior al SHA 5f4b2a2 revisado. Comparado su diff: regenera artefactos y cambia ejecutar_todo.sh y especificaciones; no modifica lib_arnes.py, ejecutar_caso.py ni generar_matriz.py. La regeneración no acredita por sí sola el cierre de los defectos de esas piezas. La revisión del coordinador sobre d032691 sigue siendo necesaria; no se rechaza el conjunto sin examinarlo.
- G-RAIZ sigue pendiente de revisión. A3 tiene entregas parciales. E2 y F3 conservan su cola.
- T-TRASPASO sigue sin resultado publicado; 0/36 casos Qwen completos acreditados en el control.

## Orden de continuación

Mantener el programa y revisiones ya asignadas. Prioridad técnica: invariantes de D3 (rutas/identificadores, matriz que reevalúe, evidencia del producto, resultados regenerados y relevos completos). Conservar lo conforme, contrastar variantes además de las sondas literales, y no ejecutar los 36 casos completos apoyándose en un arnés aún sin aceptar.

La revisión de G-RAIZ y las correcciones independientes de A/E/F pueden continuar. Ninguna política económica se adopta por este contraste.
