# Zoetis, segundo tiempo: sellado del registro de entradas (zoetis_t2)

- **Revisor:** «Claude revisor sellado». No he extraído ninguna entrada: los extractores son Mistral, el extractor complementario y «Claude orquestación».
- **Fecha del sello: 2026-11-20.** Es la del reloj del sistema (UTC), la única que admite `verificacion_entradas.py sellar` («solo la revisión de hoy»). El encargo pedía 2026-11-21, pero el programa lo habría rechazado.
- **Material:** `zoetis_t2/Zoetis/verificacion_entradas.json`, rama `examen/expedientes-f1`, cabeza `6df1558` (+ `11ab9ea`). Commit del sellado: `19b5c08`.
- **Qué cambié:** solo el bloque `comprobacion` y el vínculo que escribe `sellar`. No toqué valores, fuentes, huellas, fases ni el pipeline.

## Qué examiné y resultado: 65 de 65 pendientes sellados

**Mercado:**
- **C37 = 82,11 USD.** Examiné la imagen `fuentes_mercado/Zoetis_ZTS_2026-11-05_investor_zoetis_historical_quote.png`; su huella `994c5be3…` es la del anexo 3 ter.
  - Muestra investor.zoetis.com, «Historical Stock Quote», Lookup Date 2026 Nov 5: Day's Open $84.87, Closing Price $82.11, Low $81.54, High $88.74, Volume 10,087,799.
  - La transcripción es fiel y la página identifica la empresa (URL, logotipo, ZTS).
  - Coincide con la tabla histórica de la empresa conservada («November 05, 2026 | $82.11»). Eso descarta el fallo de tabla sin refrescar que tuvieron otras capturas.
- **C41:** 82,11 × 424,927535 = 34.890,79989885. La desalineación entre las acciones de diciembre y el precio de noviembre está declarada (Z-ACC).
- **C55 y Palancas!C45:** C55 son 424.927.535 acciones, sin redondear. Palancas!C45 = 46331, es decir, el 5-nov-2026.
- **C57 = 4,84 %:** fila 11/05/2026 del CSV del Tesoro, columna «10 Yr» según la cabecera.

**10-Q del T3 2026:**
- **Auxiliares nuevos** (p. 3, 5, 8, 10 y 11): columnas Three/Nine Months 2026 | 2025(a), balance a 30-sep-2026 y nota 2 «As previously reported» comprobados.
- **C32** = 2.888 ÷ 15.088.
- **C53** = 1.333.
- **C54** = 750 + 8.299 = 9.049.

**Aproximaciones C24, C33, C40 y C42:** la clase (convención) y la declaración son honestas.
- **Qué declaran:** el LTM a 30-sep-2026 = 2025 del 10-K (base antigua) − 9M-2025 + 9M-2026. El BAI, los impuestos y el CFO de 9M-2025 van «as previously reported»; los intereses, la D&A, el capex y los arrendamientos, solo reexpresados.
- **Aritmética rehecha:**
  - EBITDA LTM 3.835;
  - C33 = 7.716 ÷ 3.835 = 2,011995;
  - C40 = 2.773 − 493 − 1 = 2.279;
  - C42 = 42.606,8 ÷ 3.835 = 11,109987.
- **C24** = NOPAT 2.679,1959 ÷ capital a 30-sep-2026 (11.019) = 0,243143. No reproduce el 26,6 % de la etapa 1 y lo dice. Declara las alternativas: capital medio 25,5 % y con inversiones a corto 24,8 %. Declara también la razón del capital de fin de periodo: el 10-Q no publica el balance de sep-2025.
- **Lo que noto:** el Control maestro N29 lleva un aviso automático H1 («depende de un cero pendiente… 2021»). La fórmula registrada de C24 no usa la Historia de 2021. No afecta al registro, pero conviene que la orquestación lo mire.

**Convenciones con el T3:**
- **C31 «Sí»:** inventario +199 − 182 + 143 = +160 (+6,7 %) y cobros +236 − 190 + 291 = +337 (+24,9 %), frente a ingresos de 9M +0,4 %.
- **C34 «Sí»:** 1.331 ÷ 750 = 1,77x.

**Hipótesis y convenciones de las fases (29):** valor igual al libro y fundamento igual a Control maestro!N; en C76 = 0 lleva además la evidencia M. El sello acredita el registro, no el acierto del juicio.

**C38 y C88: sellado el juicio de materialidad (N1), no el dato.** Los datos siguen siendo lecturas de terceros sin bytes.
- **Libro:** busqué en las fórmulas de las 11 hojas quién lee cada celda.
  - C38: solo C39 → D39, C87 → D87/E43 y el aviso Motor!E235.
  - C88: solo el rótulo D88, que nunca escribe «BANDERA» ni «REVISAR».
- **Fases:** A y B no citan ninguna de las dos. La fase C nombra C38 en su autocomprobación de anclaje solo para decir que ninguna palanca la cita. Ninguna fase cita C88.
- **Límite:** C38 estuvo a la vista del juicio (`datos_v63.md`).

## `comprobar`

- **Cobertura:** universo 315, de las que 313 están comprobadas (214 de 214 de cálculo y 99 de 101 de juicio), más 198 auxiliares.
- **Estado:**
  - 2 entradas no materiales con el juicio revisado (C38 y C88) y 2 lecturas externas sin bytes, listadas aparte;
  - 0 pendientes, 0 discrepancias, 0 errores, 0 desactualizadas.
- **Apto por entradas: True.** Es condición necesaria, no suficiente: no acredita aptitud para dinero real ni sustituye la auditoría.

## Entradas no selladas

Ninguna.
