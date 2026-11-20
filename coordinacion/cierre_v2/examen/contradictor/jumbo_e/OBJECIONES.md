# Contradictor · Jumbo S.A. (BELA) · expediente jumbo_e

**Lo que ataco:** cubo Sí, comprar a 27,28 €. Precio de Sí 32,38 € (MALO 25,88 · NORMAL 37,23 · BUENO 45,44 €).

**Resultado:** encuentro tres objeciones válidas, las tres a la baja. Ninguna cambia por sí sola la zona ni el cubo, y tampoco las tres juntas: el precio de Sí bajaría a 30,8–31,5 €, todavía entre 3,5 y 4,2 € por encima del precio. Con r = 9 % y k = 3, comprar sigue cumpliendo la regla.

## O1 · El modelo usa un impuesto de antes del Pilar II
- **Hecho:** «On April 5, 2024, the Government of Greece […] enacted Pillar II income tax legislation, effective as of January 1, 2024 (Law 5100/2024).» [AR2025, PDF p. 180]
- La hoja aplica un 17,99 %, la media de 2021–2025, con tres años anteriores a esa ley. El tipo real fue del 18,93 % en 2025 [p. 148], del 19,39 % sin partidas sueltas (conciliación, p. 180) y del 19,97 % en el primer semestre de 2026, con Chipre al 15 % desde enero [H1 2026, p. 23 y p. 40].
- **Cuánto mueve:** el precio de Sí baja entre 0,37 y 0,78 € (32,00–31,59 €).

## O2 · Las «fugas» f llevan un 2023 que no se repite
- **Hecho:** «Interest received 13.791.382 18.490.712» [AR2024, PDF p. 154]. En 2023 la caja empezó en 803 mm y se repartió ese mismo año (401 mm de dividendos y 200 mm del bono), y la empresa pagó 6,7 mm menos de impuesto que el devengado.
- f por año: −0,0074 (2023), −0,0013 (2024) y −0,0008 (2025). La hoja usa el agregado: −0,0030.
- **Cuánto mueve:** entre −0,29 y −0,32 €. El ajuste J1 que la fase C deja pendiente, por sí solo, subiría el precio de Sí 0,14 €. Aplicado sobre un f sin 2023, el neto queda en −0,17 a −0,23 €.

## O3 · El MALO no reinvierte ni lo que cuestan los centros que ya construye
- **Hecho:** «Total investments in distribution centers are expected to exceed €95 million over the next three years.» [AR2025, PDF p. 25]. Según H1 2026 [p. 17], Giga (Rumanía) y Salónica «is progressing».
- En el MALO el motor reinvierte 37 mm en tres años y 129 mm en diez (50 y 172 mm con el 0,75 que propone la fase C). Hay dos cotas. La baja pone los centros aparte. La alta añade dos aperturas propias al año, cada una con 8,3 mm de inmueble (75 mm por nueve tiendas) y 3,5 mm de inventario; así harían falta unos 300 mm en diez años.
- **Cuánto mueve:** el MALO baja entre 0,40 y 0,98 € y el precio de Sí entre 0,20 y 0,49 €. Cada euro del MALO pesa medio euro en el precio de Sí.

## Lo que cambian las tres juntas
- El precio de Sí queda en 30,8–31,5 €: sigue por encima del precio, así que la conclusión se mantiene.
- El valor sin crecimiento cae de 28,12 € a 27,3–27,6 €. Ya no es verdad que «el precio no paga nada por crecer»: paga casi exacto el margen de 2025 para siempre.
- La fase C dice que con la r mínima de la hoja la zona no cambia (28,01 €). Con mis tres objeciones ese número baja a 26,6–27,3 €, por debajo del precio. No propongo cambiar la r del 9 %: solo pruebo la afirmación de la fase C.

## Aviso en sentido contrario
El motor descuenta 2026 un año entero, como si la valoración fuera a 31.12.2025, con la caja de junio y el precio de noviembre de 2026. Corregirlo subiría el precio de Sí entre +0,5 y +2,1 €, y eso compensa en todo o en parte mis objeciones. No lo cuento como objeción porque no ataca la compra, pero quien sume mis cifras debe tenerlo en cuenta.

## Revisado y descartado como objeción
- Balfin y Fox Group pasan a otro modelo de suministro [H1 2026, p. 17–18]. Costaría hasta −0,84 € si desapareciera el punto de crecimiento de los socios, pero depende de regalías que no se publican y de una negociación abierta.
- El margen del NORMAL (0,32) frente al 31,64 % de los últimos doce meses: −0,15 €, y es juicio.

Cuentas: la réplica del motor A en `calc/motor_a.py` reproduce la hoja al céntimo; cada cifra sale de los scripts de `calc/`.
