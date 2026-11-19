# Contradictor · Zoetis (ZTS) · fase C

**Conclusión atacada:** pendiente de datos · Vigilar · acción `null` · precio de Sí 73,31. El precio es 73,08, así que el colchón es de 0,23. Como la conclusión es Vigilar, he buscado errores en las dos direcciones.

**Resultado:** hay cuatro objeciones válidas. Tres van a la baja y una al alza. Las cifras salen de una réplica del motor A (`calc/motor.py`) que reproduce la hoja al céntimo.

| # | Dirección | Hecho (texto/) | Precio de Sí |
|---|---|---|---|
| O1 | baja | El IRS reclama ≈450 millones, sin contar intereses ni sanciones, y el caso está en apelación [10-Q 2T26, p. 16; 10-K 2025, p. 84] | 72,25 a 72,81 (central 72,71) |
| O2 | baja | La deuda pasa de 6.650 a 9.150. Incluye un convertible de 2.000 al 0,25 % que vence el 15-jun-2029 [10-K 2025, p. 59 y 86] | 70,63 a 72,91 (central 71,43) |
| O3 | baja | Tipo efectivo del 20,4 % en 2025 y del 20,3 % en 2024 [10-K 2025, p. 50]; la guía de 2026 da un 20,5 % | 72,78 a 72,92 |
| O4 | sube | 414,15 M de acciones a 30-jun-2026, frente a 424,93 M a 31-dic-2025 [10-Q 2T26, p. 5] | 75,39 a 75,71 |

**O1 · Reclamación fiscal.** La fase C la quitó de la tesis inversa porque, según dijo, «no están en mis entradas o no son verificables». Sí está, en dos documentos. El motor A no resta pasivos, así que esos 450 (1,06 por acción) no están en el valor. Si la pérdida completa va solo al escenario MALO, el precio de Sí queda en 72,71; si va a los tres, en 72,25.

**O2 · Coste de la deuda.** La fuga `f` se calibró con la deuda de 2023–25, pero las acciones de la hoja ya descuentan las recompras pagadas con la deuda nueva. La fase A vio el aumento («≈2 % del FCF base») y no lo llevó al valor.
- Solo el nivel de cupones de 2026 (296 frente a 276,7 de media) deja el precio de Sí en 72,91.
- Refinanciar el convertible al 5,000 % de la emisión de agosto de 2025, como exige la premisa de la hoja de que la deuda se refinancia siempre, lo deja en 71,43.

**O3 · Impuestos.** La hoja proyecta con un tipo del 19,97 %, que es la media de 2021–25 y arrastra el 18,25 % de 2021. Pero `f` está calibrada con el tipo de cada año de 2023–25. Con ese mismo tipo (20,36 %), el precio de Sí es 72,92.

**O4 · Fecha (al alza).** La hoja calcula el valor a 31-dic-2025 y lo compara con un precio del 8-oct-2026; su propio aviso V28 lo señala. Llevé el valor a la fecha del precio: lo hice crecer al 9 %, le resté los 1.637 ya repartidos y lo dividí entre 414,15 M de acciones. Así el precio de Sí sube a 75,71. Con este colchón de 2,63, el dato del rival deja de ser material: con probabilidades 0,4 / 0,4 / 0,2 el precio de Sí queda en 73,22. El dato de las patentes sigue siéndolo: la rama de genéricos da 71,13.

## Las cuatro juntas

Las tres objeciones a la baja restan entre 1,30 y 4,26 (central: −2,85, precio de Sí 70,46). Si se suma la corrección de fecha, el neto queda entre 69,95 y 74,33, con un central de **72,62**. En el caso central, la zona pasa a `vigilar` por 0,46.

## Qué cambia

El cubo Vigilar resiste en las dos direcciones; lo que no resiste es el motivo. La fase C dice que el precio cumple la regla y que solo faltan dos datos. En realidad, 73,08 está dentro del margen de error de la escalera, y en el caso central por encima del precio de Sí. Por eso «comprar en cuanto lleguen las fechas» no está respaldado: el Vigilar es por precio y por datos.

## Descartadas tras medirlas

- **Trayectoria de 2026.** Con el margen de la propia guía, el EBIT del MALO coincide con el guiado y el efecto es −0,03.
- **El 74,12 de la fase C por la I+D.** El exceso de la fila 31 es la amortización de intangibles (161/150/149/141/128), no I+D neta. No hay un colchón oculto a favor de la tesis.
- **Lista de patentes del 10-K 2025 (p. 17).** Solo nombra Draxxin, Excede y Cerenia. Sin fechas para Simparica Trio ni Apoquel, no se puede cifrar.
- **Rimadyl −39 % frente a Draxxin −66 % (p. 25).** Solo afecta a una rama que no está en la hoja.

No propongo tamaños de posición ni cambio la r del 9 %.
