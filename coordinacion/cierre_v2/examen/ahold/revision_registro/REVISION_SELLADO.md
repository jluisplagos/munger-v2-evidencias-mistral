# Ahold Delhaize: sellado del registro de entradas (ahold_f3)

- **Revisor:** «Claude revisor sellado», 2026-11-19. No he extraído ninguna entrada. Los extractores son Mistral, `claude-opus-extractor-complementario` y «Claude orquestación».
- **Material:** `ahold_f3/Ahold/verificacion_entradas.json` en la rama `examen/expedientes-f1` del repo producto. Commit del sellado: `909d279`.
- **Qué cambié:** solo el bloque `comprobacion`. `sellar` escribe además el vínculo. No toqué valores, fuentes, huellas ni derivaciones.

## Cómo revisé

- **Las 46 entradas cambiadas que no son hipótesis** (de las 76 que lista `resultados/registro_entradas_ahold_f3.json`): las examiné todas a mano en `texto/` y en `fuentes_mercado/`.
  - **Regla espejo P-O1 (c):** 27 auxiliares de dividendos de negocios conjuntos, intereses cobrados y subarriendos (2019–2025 y 1S). Columnas comprobadas en AR2020–AR2025 y en Q2-2026 p. 15.
  - **C46, C48 y C49:** salen 6.583,667, 77 y 1.707,333.
  - **P-O2:** C55 = 886,877259, con Q3-2026 p. 21. C41 = 31.971,925.
  - **C42 = 6,590310.**
  - **C40 = 2.096.**
  - **C88:** los 7 P/FCF con la regla espejo.
  - **C96 = 0,000639,** de AR2025 p. 199 y p. 209.
- **Las entradas sin cambios:**
  - 29 examinadas a mano, más todas las dudas y discrepancias de la revisión previa;
  - para el resto, los controles automáticos y la revisión del 2026-11-18. La disposición del texto impide mi guion de columnas.
- **Mercado:**
  - **C37:** la fila del 13/11/2026, 36,05, está en el histórico no ajustado de Euronext.
  - **C57:** la fila del 2026-11-17, 3,34 %, está en la serie UMU de la Bundesbank. El 13-nov, fecha del precio, la serie da 3,36 %.
  - **Huellas:** las dos coinciden.

## Resultado (531 entradas)

| | verificadas y selladas | discrepancias | pendientes | sin revisar (hipótesis/fases) |
|---|---|---|---|---|
| total | 448 | 47 | 5 | 31 |

**Discrepancias (47).** No he corregido ninguna.

- **`Historia!C23` y `D23`:** citan la asignación del precio de compra de Delhaize, que no prueba el cero.
- **Minoritarios `D26`, `E26`, `F26`, `G26`, `H26` y `K26`:** citan filas de otro año del estado de cambios en el patrimonio. El 0 es correcto.
- **Folios y periodo (23):**
  - AR2019 PDF p. 125 tiene el folio 124, no 110 (13 entradas);
  - AR2018 p. 160 tiene el folio 160, no 281 (D20);
  - AR2017 p. 147 tiene el folio 147, no 54 (D23);
  - Q2-2026 p. 15 tiene el folio 15, no 30 (8 auxiliares);
  - el CFO del 1S-26 se rotula «12 meses hasta 30-jun», pero es el semestre al 28-jun.
- **Fila 19 (C19:L19):** la justificación habla de «deterioros», pero la fila es I+D.
- **Clase:**
  - `C28`, `C31` y `C34` son etiquetas con valor registradas como `dato_ausente`;
  - `Palancas!A30` es una etiqueta registrada como `no_aplicable`. Además afirma, sin fuente, que Bélgica es «la mayor parte» de Rest of world.
- **`Historia!C22` y `D22`:** incluyen arrendamientos financieros NIC 17, pero la fila se define «sin arrendamientos». Decide la persona.
- **`Análisis!C24`:** la fórmula (ROCE del ejercicio 2025) da 0,109 solo al redondear. El libro documenta un ROCE LTM a 28-jun-2026.

**Pendientes (5):**
- `C38` (Simply Wall St) y `Palancas!C7` (Damodaran) son lecturas externas sin bytes. La página de Damodaran está en `fuentes_mercado/`, pero el registro la declara externa.
- `C40`, `E13` y `E14` tienen derivación correcta, pero sus orígenes tienen discrepancia formal (folios). Hay que sellarlos de nuevo al corregirlos.

**Verificadas con matiz:**
- C42 usa el balance de Q2-2026 aunque el Q3 (4-nov) ya está en `texto/`. Es la vigencia que declara su incidencia.
- C37 no es la sesión más reciente del archivo.
- J87:L87 recogen solo «Franchisee and affiliate relationships», por decisión de la declaración F1.
- H5 e I5 tienen la ubicación inexacta.

## `comprobar` tras el sellado

- **Cobertura:** universo 309, de las que 240 están comprobadas (169 de 214 de cálculo y 71 de 95 de juicio), más 208 auxiliares.
- **Estado:** 47 discrepancias y 36 pendientes. Los pendientes son los 5 citados más las 31 hipótesis y convenciones de las fases. 0 errores y 0 desactualizadas.
- **Apto por entradas: False.**

No acredita aptitud para dinero real.
