# Zoetis: sellado del registro de entradas (zoetis_t1c)

- **Revisor:** «Claude revisor sellado», 2026-11-19. No he extraído ninguna entrada. Los extractores son Mistral (`mistral-large-4-0`) y «Claude orquestación».
- **Material:** `zoetis_t1c/Zoetis/verificacion_entradas.json` en la rama `examen/expedientes-f1` del repo producto (cabeza `6c0e678`). Commit del sellado: `4743cb0`.
- **Qué cambié:** solo el bloque `comprobacion`. `sellar` escribe además el vínculo. No toqué valores, fuentes, huellas ni derivaciones.

## Cómo revisé

- **Las entradas cambiadas que no son hipótesis** (de las 131 que lista `resultados/registro_entradas_zoetis_t1c.json`): las examiné a mano en `texto/` y en `fuentes_mercado/`:
  - EBIT = BAI + intereses en los diez años, sobre la cuenta de resultados de cada 10-K;
  - D13, J13 y E13 (10-K 2018 p. 75 y p. 87, 10-K 2019 p. 75, 10-K 2024 p. 68);
  - L17 y la fila 23 «solo financieros» (10-K 2024 p. 86 y 10-K 2025 p. 89; decisión D-US1);
  - los 23 ceros que pasan a `no_aplicable`;
  - la capa F1 H86:L87 (10-K 2022 p. 52 y 10-K 2025 p. 54 y p. 89);
  - los auxiliares del 10-Q T2-2026 (p. 3, 5, 8, 10 y 11);
  - C26, C33, C40, C41 y C42.
- **Las entradas sin cambios:**
  - 38 examinadas a mano, más todas las dudas y discrepancias de la revisión previa;
  - para el resto, los controles automáticos y la revisión del 2026-11-18, que contrastó las columnas por guion y con la segunda lectura OCR.

## Resultado (491 entradas)

| | verificadas y selladas | discrepancias | pendientes | sin revisar (hipótesis/fases) |
|---|---|---|---|---|
| total | 432 | 22 | 6 | 31 |

**Discrepancias (22).** No he corregido ninguna.

- **C41 (confirmada):** usa C55 redondeado (424,928) en lugar de 424.927.535. Sale 31.053,73824 frente a 31.053,704.
- **C55:** el redondeo a 3 decimales está declarado, pero no tiene justificación para una cifra de acciones. Es el origen del desfase de C41.
- **C33, C40 y C42 (respuesta a la pregunta):** la aritmética y las fuentes son correctas (1,8968; 2.363; 9,6758), pero **la clase no**:
  - es una aproximación por la *Fiscal Year Alignment*: el 2025 sale del 10-K en la base antigua y el 6M-2025 mezcla dos bases. El BAI y el CFO van «as previously reported»; los intereses, la D&A y el capex, reexpresados;
  - la incidencia lo declara, pero como `derivado` cuenta entre los derivados comprobados;
  - debería ser convención o aproximación con `justificacion_clase`, como C24, o rehacerse con el 10-Q T2-2025;
  - C42 arrastra además C41 y mezcla el balance de junio con las acciones de diciembre.
- **I26 y J26:** el balance imprime (2) y (6), minoritarios negativos. El libro guarda +2 y +6.
- **E26:** el 10-K 2018 p. 73 imprime «—» en 2018. Es un cero publicado, no un dato ausente.
- **C86:G86 y C87:G87:** la justificación dice que la D&A de derechos de uso y la de compras no se publican. Con la F1 vigente, la serie de derechos de uso es la de arrendamientos financieros, y la de compras sí se publica.
- **A31/B31 y A33/B33:**
  - «Asia» incluye «Other emerging markets»;
  - «Australia & NZ» incluye «Other developed markets» y la fabricación por contrato.
  - Esto fija la r mínima. Lo decide la persona responsable.

**Pendientes (6):**

- **C37 (73,08) y C57 (5,22 %):** coinciden con `fuentes_mercado/`, pero son transcripciones o extractos del extractor, no los bytes oficiales.
- **C38, C88 y Palancas!C7:** lecturas externas sin bytes.
- **C24:** ROIC de la etapa 1, no reproducible exactamente con el expediente.

**Verificadas con matiz:**

- **E13 (la duda):** mantengo 1.998, que es Abaxis 1.884 más otras 114. Los ≈ 47 de la desinversión agrícola van en «Net proceeds from sales of assets», como en D13. Con el criterio de venta de negocio saldría ≈ 1.951 (−2,4 %).
- **C14:** usa el comparativo del 10-K 2017. El 10-K 2018 reexpresa 2016: daría 434.
- **H87:L87:** son una cota superior de la PPA.
- **J8:** sale de una línea OCR de la nota de segmentos, que coincide con el estado de flujos.

## `comprobar` tras el sellado

- **Cobertura:** universo 315, de las que 256 están comprobadas (167 de 214 de cálculo y 89 de 101 de juicio), más 176 auxiliares.
- **Estado:** 20 discrepancias y 39 pendientes. C41 y C42 figuran como pendientes por su origen C37. 0 errores y 0 desactualizadas.
- **Apto por entradas: False.**

No acredita aptitud para dinero real.

## zoetis_t1d, el expediente definitivo de Zoetis (primer tiempo): sellado de los 68 pendientes (2026-11-19)

- **Material:** `zoetis_t1d/Zoetis/verificacion_entradas.json`, cabeza `fe8e898`. Commit del sellado: `897db35`.
- **C37 (73,08 USD):** examiné la imagen `Zoetis_ZTS_2026-10-08_investor_zoetis_historical_quote.png`. La huella c1871f7e… coincide con el anexo 3 ter. Muestra investor.zoetis.com, «Historical Stock Quote», 2026 Oct 8, Closing Price $73.08 y Volume 6,176,469. Identifica la empresa. Límite: otras capturas de la misma consulta mostraban una tabla sin refrescar. Esta coincide con la lectura anterior de la tabla histórica de la empresa.
- **C41 y C55:** ahora son exactos. C41 = 73,08 × 424,927535 = 31.053,7042578.
- **Fila 26 (Z-MIN):**
  - E26 = 0, el «—» impreso en el 10-K 2018;
  - I26 y J26 = max(impreso, 0) = 0, con −2 y −6 en sus auxiliares;
  - C26:H26 y K26:L26 se vuelven a sellar.
- **C86:G87:** las justificaciones están corregidas.
- **Las aproximaciones son honestas:**
  - C33, C40 y C42 pasan a convención, con una `justificacion_clase` que declara la mezcla de bases de la Fiscal Year Alignment. La aritmética está comprobada.
  - C24 declara que no se reproduce exactamente: con lo conservado sale ≈ 26,2–26,9 %, un rango que contiene el 26,6 %.
  - Esto resuelve la discrepancia de clase de t1c.
- **A31/B31 y A33/B33:** la decisión Z-R de la persona deja la agrupación, con la diferencia anotada.
- **C57 (5,22 %):** CSV del Tesoro, «10 Yr», 10/08/2026.
- **C7:** tabla de Damodaran, Drugs (Pharmaceutical).
- **Hipótesis del motor B:** las 30 de las fases son iguales a Control maestro!N; C85 es la decisión F1-A.
- **C38 y C88, materialidad (N1):** solo las leen rótulos informativos del libro.
  - La fase C dice no usar C38 (197,36).
  - Ninguna fase cita C88.
  - Los datos siguen siendo lecturas externas sin bytes.

**`comprobar`:**
- **Cobertura:** universo 315, de las que 313 están comprobadas (214 de 214 de cálculo y 99 de 101 de juicio); faltan C38 y C88, no materiales con el juicio revisado.
- **Estado:**
  - 178 auxiliares;
  - 0 discrepancias, 0 pendientes, 0 errores, 0 desactualizadas;
  - 15 datos tratados como hipótesis o convención, listados.
- **Apto por entradas: True.** Es condición necesaria, no suficiente: no acredita aptitud para dinero real ni sustituye la auditoría.
