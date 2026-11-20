# Revisión del registro de entradas de VINCI (examen)

- **Revisor:** «Claude revisor registro», un agente Claude distinto del extractor Mistral (`mistral-large-4-0`). Fecha: 2026-11-19. **No se sella nada.**
- **Material revisado:**
  - rama `mistral/examen-vinci-entradas` @ `737a8d8`: `resultados_examen/vinci/verificacion_entradas.json` (315 entradas + 162 aux), `ENTREGA.md`, `DESCARGAS.tsv` y `fuentes_mercado/`;
  - contraste con el expediente `vinci/Vinci` (repo producto, rama `examen/expedientes-f1` @ `b8b151e`): textos `[PDF PAGE n]` (URD 2021–2023 por mitades), `fase1_partes`, `motor_a_f1.json`, `cambio_vinci.json`, `datos_v63.md` y el libro `Vinci_v63_datos.xlsx`.
- **Detalle:** `REVISION.tsv`, con una fila por entrada del alcance (285; las 30 hipótesis no se revisan) y por auxiliar (162).

## Recuentos

| | verificado | discrepancia | duda | total |
|---|---|---|---|---|
| universo (sin hipótesis) | 259 | 24 | 2 | 285 |
| auxiliares | 41 | 121 | 0 | 162 |
| **total** | **300** | **145** | **2** | **447** |

De las 145 discrepancias, 128 son de forma: la cita o un campo impiden el contraste, pero el valor es correcto. **Valores que cambian: 1** (C57). **Clase o vigencia mal: 18.**

**`comprobar`** se ejecutó sobre una copia del expediente en /dev/shm con el registro de Mistral:
- resultado: 0 comprobadas, **4 discrepancias** y **49 errores de contrato** (30 hipótesis, 10 datos ausentes que tienen valor y 9 clases null);
- con una simulación de revisión (vínculos dados por escritos, sin sellar ni escribir), 180 entradas quedan pendientes. **121 aux tienen `cita` = null**: la línea literal solo está en `comprobacion.nota`. Con esa línea copiada como cita, las 121 pasan el contraste de página, cifra y signo, y solo quedan las 4 discrepancias y C7.

`ENTREGA.md` dice que «cada cita está en su página». Es falso para esas 121 aux, para K22/L22 y para C48/H4.

## Discrepancias materiales y corrección

1. **Capa F1, H86:L87 (10).** El libro tiene la amortización de derechos de uso 2021–25 (605/623/668/714/817) y la PPA de Cobra IS (0/128/128/108/38), que vienen de `motor_a_f1.json`. Mistral las registró como `dato_ausente` copiando la justificación de las celdas vacías.
   - **Corrección:** H87 pasa a `cero_comprobado`, con la cita de la compra de Cobra IS el 31-dic-2021 (URD2021 p. 150). Las otras nueve pasan a `dato_publicado` con las citas de la nota 4.3, que he comprobado en su página (URD2022 p. 168, URD2023 p. 171, URD2024 p. 350, URD2025 p. 372).
   - **Justificación de F86/G86:** dice que la cifra no se publica, y es falso. El URD2020 p. 319 da 548 (2019) y 582 (2020). La clase sigue bien porque la celda está vacía.
2. **`Análisis!C40` (vigencia).** El libro actual guarda **4.132**, no 7.228. El commit `ee1ca6a` (07:08) recalculó C40 después de la plantilla (06:54). Mistral llegó a 4.132 y aun así la dejó sin resolver.
   - **Corrección:** derivado del cálculo declarado de 2025: 11.886 − 2.496 + 40 − 3.873 + 179 − 311 − 110 − 761 − 422 = 4.132.
   - **Además:** hay que regenerar la plantilla.
3. **`Análisis!C57` (mercado).** El valor de 3,486 % no tiene fuente oficial. La serie que fijó la persona, Bundesbank **WT1010** (`bund_10y_WT1010.csv`, `fef9498e…`), da «2026-10-09,3.47».
   - **Corrección:** en vinci_b, C57 = 0,0347 como `dato_publicado`, conservando ese archivo.
   - **Series de Mistral:** son otras dos. La UMU de 9 a 10 años da 3,46 % y la curva AAA del BCE da 3,5112 %. Sirven de contraste, no como fuente de C57.
4. **Clases null que se resuelven con lo publicado.**
   - `C26`: Σ CFO 2021–25 ÷ Σ resultado neto **consolidado** = 51.333 ÷ 22.263 = 2,3057 → **2,31**. Es `derivado` con round 2, y los aux ya existen.
   - `C60`: (567,0603 ÷ 570,51)^(1/3) − 1 = −0,002. La potencia no se admite en la fórmula, así que va como `convención`.
   - `C28`, `C31` y `C34`: `convención` con el fundamento de la etapa 1, como en Jumbo.
5. **Citas que no pasan (el valor es correcto).**
   - Las 121 aux sin cita.
   - K22/L22: la página imprime la raya «I – Gross financial debt» y la cita lleva un guion.
   - `Palancas!C48` y `Control maestro!H4`: falta `equivalencia` «€».
   - `Palancas!C7`: el HTML no tiene `archivo_texto`. El sector es correcto: el indname de Damodaran pone a «Vinci SA (ENXTPA:DG)» en Engineering/Construction.

## Comprobado sin objeción

- **Columnas, años y escalas.** Todos los orígenes de la Historia salen del comparativo del informe siguiente, que es la cifra más reciente; en 2021, la deuda reexpresada de 30.738. 2025 sale del URD2025. Todo está en millones de euros.
- **Signos.** Las cifras entre paréntesis llevan signo −1 hacia el libro. El circulante impreso en positivo es una entrada de caja, y la fila 14 es su opuesto.
- **EBIT derivado.** Es el resultado neto consolidado menos el impuesto, el coste de la deuda neta y los otros financieros, con sus signos impresos. Da el «Operating income» con ±1 de redondeo en los diez años.
- **Capex.** Suma dos líneas: las compras de inmovilizado y las inversiones en concesiones.
- **Deuda bruta.** No incluye arrendamientos NIIF 16 ni derivados. 2016–17 incluye NIC 17 (78 y 130): conviene declararlo como en A-NIC17, aunque es inmaterial.
- **No aplicables 2016–18 (filas 16, 17 y 23).** Son correctos.
- **Fila 17.** El principal más la fila 16 da la línea de financiación (575 … 871), con 1 de redondeo del emisor en 2023.
- **C46–C50.** Reproducen 9.327,333 / 3.799,667 / 89,333 / 675,333 / 343,667. Tienen el significado declarado: CFO sin la entrada de circulante (M43, V-CIRC a), con la regla espejo de P-O1 c, capex definición D, intereses y principal de arrendamientos, y SBC abonada a patrimonio. El «Other 41 31» del URD2024 p. 348 es la misma fila que el URD2025 rotula como dividendos de no consolidadas.
- **C55.** 555.967.094 = 581.816.830 − 25.849.736 de autocartera (URD2025 p. 346), con P-O2 a.
- **C42.** Da 6,27964 con columnas del semestral comprobadas. La desalineación Z-ACC está declarada.
- **C37.** 107,05 € en el histórico no ajustado de Euronext que conservó Mistral. Coincide con el cierre de la exportación de la persona según el anexo 3 bis. El cierre lleva el dividendo a cuenta de 1,10 €, con ex el 13-oct.

## Dudas

- `C38` (Simply Wall St) y `C88` (P/FCF de la etapa 1, mediana con precios de cierre de año): no hay bytes. Propongo `dato_publicado` con lectura externa para C38, y `convención` para C88.
- `Historia!J19/K19` (verificadas): el informe integrado cita un I+D de «approximately €50 million». La justificación «no publican» hay que matizarla.

## Límites

- Revisé cada entrada con scripts propios (cita y línea en su página, columna por año del informe, signo, escala, fórmulas y valor actual del libro) y a mano en las páginas señaladas.
- No releí los PDF: usé los textos del expediente, cuyas huellas coinciden con la Release según `DESCARGAS.tsv`.
- No pude leer el XLS de Euronext de la persona porque no tengo lector de XLS. Para C37 me apoyo en la lectura del coordinador, anexo 3 bis.
- El Euronext conservado no tiene los bytes crudos de la descarga: Mistral le añadió la marca de página.
- No revisé las hipótesis ni leí la rúbrica ni `contradictor/`.

Esto no acredita aptitud para dinero real.
