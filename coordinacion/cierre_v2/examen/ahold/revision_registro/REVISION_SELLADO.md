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

## Segunda pasada: las 51 entradas corregidas tras el sellado (2026-11-19)

- **Material:** la orquestación corrigió 51 entradas en `f02f7b1` (lista en `resultados/registro_cambios_sellado_ahold_f3.json`). Las examiné todas en `texto/`. Volví a examinar también C40, E13 y E14, que estaban pendientes por sus orígenes.
- **Commit del sellado:** `a1a25fb`.

**Selladas (50):**
- **Folios y periodo:**
  - AR2019 PDF p. 125 → folio 124 (13 entradas);
  - AR2018 p. 160 → 160;
  - Q2-2026 p. 15 → 15 (8 entradas);
  - periodo del CFO del 1S-26 al 28-jun-2026.
- **`C23` y `D23`:** pasan a `no_aplicable`, con la nota 1 de AR2025 PDF p. 65 (sin reexpresión NIIF 16 antes del 30-dic-2018).
- **Minoritarios `D26`, `E26` y `F26`:** Group equity − patrimonio atribuible = 0. Lo comprobé en AR2018 p. 43/91, AR2019 p. 40/123 y AR2020 p. 67/147, con sus 6 auxiliares.
- **Fila 19:** la justificación ya habla de I+D.
- **Convenciones:** `C28`, `C31`, `C34` y `Palancas!A30`. C34: la caja (3.196) es menor que la deuda a corto (3.625), así que «No». A30 ya no afirma que Bélgica sea la mayor parte.
- **Antes pendientes:** C40 (2.096), E13 y E14.

**Discrepancias nuevas (4):**
- **`G26`, `H26` y `K26`:** el 0 y la cita nueva («Non-controlling interests — —») son correctos. Pero el campo «columna» dice «ejercicio corriente del informe N», y la cita es el comparativo del informe N+1. Es formal.
- **`Análisis!C24`:**
  - el numerador, resultado operativo LTM a 28-jun-2026 = 3.561, es correcto;
  - el denominador es el capital empleado a 28-dic-2025 (32.598). Con el del 28-jun-2026 (14.445 + 19.261, Q2-2026 p. 13 y p. 23) sale **0,106**, y con el capital medio, 0,107;
  - el 0,109 solo se reproduce mezclando fechas, y la etapa 1 no documenta esa fecha.

**Siguen en discrepancia:** `C22` y `D22` (decisión pendiente).

**Siguen pendientes:** `C38` y `Palancas!C7` (lecturas externas).

**`comprobar` ahora:**
- **Cobertura:** universo 309, de las que 270 están comprobadas (178 de 214 de cálculo y 92 de 95 de juicio), más 228 auxiliares; 498 selladas en total.
- **Estado:** 6 discrepancias y 33 pendientes (31 hipótesis y convenciones de las fases, más C38 y C7). 0 errores y 0 desactualizadas.
- **Apto por entradas: False.**

## ahold_f4, el expediente definitivo de Ahold: sellado de los 73 pendientes (2026-11-19)

- **Material:** `ahold_f4/Ahold/verificacion_entradas.json`, cabeza `fe8e898`. LTM al 3T por la decisión A-Q3. Commit del sellado: `897db35`.
- **Auxiliares del 3T 2026:** examinados en `texto/AD_q3-2026-interim-report.txt` (p. 12, 14, 16 y 24): columnas Q3 | Q3 | YTD 26 | YTD 25 y balance a 27-sep-2026.
- **C24, C33, C40 y C42:**
  - **C24** = 3.635 ÷ (14.375 + 19.747) = 0,107. Numerador y denominador tienen ya la misma fecha, lo que resuelve la discrepancia de f3.
  - **C33** = 16.188 ÷ 7.334 = 2,2073.
  - **C40** = 2.150, con la regla espejo. La línea del 3T es «Interest and dividend received», y está declarado.
  - **C42** = 6,532032. La desalineación entre las acciones de diciembre y el balance de septiembre está declarada (Z-ACC).
- **C22 y D22:** sellados por la decisión A-NIC17 de la persona responsable («dejarla»), ya declarada en la conciliación.
- **G26, H26 y K26:** la columna está corregida.
- **Datos de mercado:**
  - C57 = 3,37 %, del CSV WT1010 de la Bundesbank del 13-nov, la fecha del precio;
  - C7 sale de la tabla de EE. UU. de Damodaran, con la limitación declarada;
  - C37 y C41 se vuelven a sellar.
- **Convenciones:**
  - C28;
  - C31: «Sí» literal y «No» económico, con la aproximación declarada;
  - C34 = 0,82x, así que «No»;
  - C60.
- **Hipótesis:** las 30 de las fases tienen el fundamento igual al de Control maestro!N; C85 es la decisión F1-A. El sello no acredita el acierto del juicio.
- **C38, materialidad (N1):** solo la leen C39/D39, C87/D87/E43 y el aviso E235. Las fases A y B no la citan. La fase C la vio y dice no haberla usado. Su valor (61,27) está lejos del ponderado (35,95). Acepto que no es material, con ese límite. El dato sigue siendo una lectura externa sin bytes.

**`comprobar`:**
- **Cobertura:** universo 309, de las que 308 están comprobadas (214 de 214 de cálculo y 94 de 95 de juicio); la que falta es C38, no material con el juicio revisado.
- **Estado:**
  - 229 auxiliares y 537 sellos;
  - 0 discrepancias, 0 pendientes, 0 errores, 0 desactualizadas;
  - 1 lectura externa listada aparte (C38).
- **Apto por entradas: True.** Es condición necesaria, no suficiente: no acredita aptitud para dinero real ni sustituye la auditoría.
