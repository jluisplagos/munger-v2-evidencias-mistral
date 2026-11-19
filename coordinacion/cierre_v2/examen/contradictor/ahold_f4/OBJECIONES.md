# Contradictor · Ahold Delhaize (AD)

**Conclusión atacada:** Vigilar · esperar · precio de Sí 33,79 €. El precio es 36,05 € (13-nov-2026) y la zona, caro. Estado: concluido, provisional hasta la auditoría.

**Resultado:** dos objeciones válidas, una a la baja y otra al alza. Las dos atacan el precio de Sí, no la acción.

## O1 · A la baja: una devolución fiscal de una sola vez infla todos los flujos (−2,0 €)

- **Hecho.** En 2023 Ahold recuperó 367 M€ de Hacienda belga. Era la devolución de un pago de 390 M€ hecho en 2021 por la declaración de 2018 [AR2023 PDF p. 220; AR2021 PDF p. 199]. La empresa lo llama «an incidental receivable related to a tax refund in Belgium» [AR2024 PDF p. 52].
- **Por qué importa.** El FCF base (2023–2025) lleva la devolución, pero no el pago de 2021. El motor no usa el FCF base tal cual: usa f, el residuo que cuadra su flujo con ese FCF. Reconstruí f con los datos del expediente y sale igual que la hoja (0,0001397). Sin la devolución, f es 0,0015, y el motor resta unos 125 M€ más cada año, también en el valor a perpetuidad.
- **Cuánto.** MALO 26,72 · NORMAL 33,59 · BUENO 41,62 (−1,7 / −2,2 / −2,4 €). Precio de Sí 31,79 € (−2,00; −2,09 con el salto completo de 382). Ponderado 33,82 €.
- **Qué cambia.** Esperar sigue, pero comprar a 33,79 sería pagar un 6 % de más. Y cae la frase de la tesis «a 36,05 pago lo que vale seguir sin crecer (34,70)»: sin la devolución, ese valor es 33,13.

## O2 · Al alza: el valor está fechado casi once meses antes que el precio (+0,9 a +1,4 €)

- **Hecho.** El motor parte de las ventas de 2025 y de las acciones a 28-dic-2025, y descuenta 2026 como un año entero. El valor está fechado a 28-dic-2025; el propio expediente dice que «no es una valoración actualizada a 2026». El precio es del 13-nov-2026, y entre medias el accionista ya cobró 0,73 € y 0,51 € de dividendo [Q3-26 PDF p. 21].
- **Cuánto.** Llevado al día del precio (valor × 1,09^0,877, menos los 1,24 € de dividendo capitalizados, 1,29 €): MALO 29,35 · NORMAL 37,29 · BUENO 46,22. Precio de Sí 35,16 € (+1,37). Si además el flujo de 2026 se baja a la guía de la empresa (unos 2.100), queda en 34,65–34,80 €.
- **Qué cambia.** El umbral del método es 34,7–35,2 €, no 33,79. La zona pasa de caro a vigilar y la distancia al Sí baja de 2,26 € a 0,9–1,4 €. Con el margen NORMAL de 0,04, que la fase C pone como condición para revisar al alza, el precio de Sí sería 37,4 € y la acción pasaría a comprar.

## Las dos juntas

Van en sentido contrario y casi se compensan: precio de Sí 32,5–33,0 € y ponderado 34,8–35,2 €, por debajo de 36,05. **Esperar se mantiene**, con un objetivo algo más bajo que 33,79 €. Con las dos y el margen 0,04, el precio de Sí es 35,27 €: tampoco llega.

## Lo que vi y no cuento como objeción

- La fase C dice que con las acciones de septiembre la zona pasaría a vigilar, y que con el margen 0,04 se cumpliría la regla (≈ 36,8). Esa cuenta olvida los 864 M€ que costó la recompra. Con ellos sale 33,64 y 35,80: esperar es menos estrecho de lo que dice la fase C.
- Los intereses cobrados de 2024 estaban altos por una caja pasajera [AR2024 PDF p. 52]. Al nivel de 2025, el precio de Sí bajaría otros 0,4–0,5 €. Depende de tipos y de caja; no lo cuento.
- Busqué salidas de caja extraordinarias en 2023–2025 que compensaran O1. La del plan de pensiones neerlandés de 2024 no lo hace.
- El S2C, el ROIC terminal, las probabilidades, C8 y el flujo de 2026 mueven poco o son juicio sin hecho nuevo.

**Límites.** Reconstruí el motor y f con `resultados.json` y `datos_v63.md`: coinciden con la hoja al céntimo. No abrí el Excel. Los cálculos están en `calc/`. No propongo tamaños de posición ni toco la tasa del 9 %.
