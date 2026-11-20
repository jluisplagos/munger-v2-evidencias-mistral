# Jumbo: sellado del registro de entradas (jumbo_e)

- **Revisor:** «Claude revisor sellado», 2026-11-19. No he extraído ninguna entrada. Los extractores son Mistral (`mistral-large-4-0`) y «Claude orquestación».
- **Material:** `jumbo_e/Jumbo/verificacion_entradas.json` en la rama `examen/expedientes-f1` del repo producto. Commit del sellado: `cdf1b6f`.
- **Qué cambié:** solo el bloque `comprobacion` (revisor, fecha, resultado, fuente examinada y nota). `sellar` escribe además el vínculo. No toqué valores, fuentes, huellas ni derivaciones.

## Cómo revisé

- **Las 46 entradas cambiadas que no son hipótesis** (de las 77 que lista `resultados/registro_entradas_jumbo_e.json`; las otras 31 son textos de las fases): todas a mano en `texto/`. Comprobé página, cita, columna, escala, signo y significado:
  - J3 de 2019 (AR2020 p. 59 y p. 86);
  - F1 `da_rou`/`da_ppa` de 2021 a 2025;
  - EBITDA LTM, C33, C42 y C96;
  - el subtotal de L14;
  - las 3 líneas de acciones del consejo y de la alta dirección.
- **Las entradas sin cambios:**
  - un guion propio comprueba la cifra bajo la cabecera del año, la columna del grupo, la escala y el signo en las 201 líneas numéricas auxiliares (198 alineadas; las 3 restantes son ceros «–», revisados a mano);
  - 45 entradas, examinadas a mano, y todas las dudas y discrepancias de la revisión previa;
  - para el resto me apoyo en la revisión del 2026-11-18.

## Resultado (567 entradas)

| | verificadas y selladas | discrepancias | pendientes | sin revisar (hipótesis/fases) |
|---|---|---|---|---|
| total | 504 | 24 | 8 | 31 |

**Discrepancias (24).** No he corregido ninguna.

- **`Análisis!C46` y `C40`:** se calcularon con C76 = 200, pero el libro vigente tiene C76 = 160. Con 160 salen **317,616988** (libro 316,475) y **255,107832** (libro 254,317567).
- **`Historia!I17`:** 7,03515 mm da **7,0352** con redondeo exacto; el libro guarda 7,0351. Son 50 €.
- **Ceros con cita que no prueba el cero:** D13, D17, E17, C23 y D23 (cartas de garantía, «available for sale», «Other liabilities»).
- **Años:**
  - D5, G5 e I5 salen de dígitos sueltos (una ley, un reglamento, una decisión);
  - E5 y F5 citan otro periodo (el semestre de 2018 y la transición de jul–dic 2019).
- **Justificaciones desactualizadas:**
  - `C86:G86` y `C87:G87` dicen que el motor F1 no declaró la serie. Ya la declara para 2021–2025, con C85 = A2_propio;
  - `C50` cita «fy2024 p. ?» y dice que K18 es dato ausente.

**Pendientes (8).** El programa no admite darlas por verificadas.

- **Lecturas externas sin bytes:**
  - C37, precio de 27,28 €. La copia de la persona responsable coincide, pero no son bytes oficiales;
  - C57, Bund;
  - C38;
  - C88, marcado «no verificable»;
  - Palancas!C7, Damodaran, contrastado solo con su extracto.
- **C41 y C42:** dependen de C37. La fórmula es correcta: C42 = 7,227054.
- **C31:** su apoyo cita el informe del 1S-2025, que no está en `texto/`.

**Verificadas con matiz** (lo anoto en su entrada):

- J13 es cifra bruta: neta de la caja adquirida sería 0,301;
- J14 y L14 incluyen los depósitos restringidos no corrientes, que el emisor presenta en el circulante;
- C5, K5 y L5 tienen la ubicación inexacta;
- C28 tiene un umbral no declarado.

## `comprobar` tras el sellado

- **Cobertura:** universo 313, de las que 250 están comprobadas (162 de 214 de cálculo y 88 de 99 de juicio), más 254 auxiliares.
- **Estado:** 22 discrepancias y 41 pendientes. C46 y C40 figuran como pendientes porque su origen C76 está pendiente. Las 31 hipótesis y convenciones de las fases siguen pendientes. 0 errores y 0 desactualizadas.
- **Apto por entradas: False.**

No acredita aptitud para dinero real.

## jumbo_g, el expediente definitivo de Jumbo: sellado de los 64 pendientes (2026-11-19)

- **Material:** `jumbo_g/Jumbo/verificacion_entradas.json`, cabeza `c6726b0`. Había 249 sellos vigentes y 64 pendientes. Commit del sellado: `3355b60`.
- **Selladas (59):**
  - **Correcciones desde jumbo_e,** examinadas en `texto/`:
    - I17 = 7,0352 (redondeo exacto de 7,03515);
    - L14 = 61,1586, desde las cinco líneas de AR2025 p. 209;
    - D13, D17, E17, C23 y D23 a `no_aplicable`: sin línea de adquisiciones ni de arrendamientos en los estados de flujos de 2016/17–2018/19;
    - años: F5, G5 e I5 citan cabeceras de columnas; D5 y E5 citan la denominación del ejercicio en el informe de gestión, con la ubicación bien declarada;
    - justificaciones de C50 y C86:G87 actualizadas.
  - **Mercado con archivo local:**
    - **C37 (27,28 €):** examiné la imagen. Euronext Athens «Historical Data», 11/17/2026, CLOSE 27.2800; la huella coincide con el anexo 3 ter y la transcripción es fiel. **Límite:** la imagen no muestra el instrumento. La identificación como BELA no la dan los bytes: la dan el nombre del archivo, el anexo 3 ter y el registro de la persona (`JUMBO_BELA_20261118.md`, «Previous Close: 27,2800 EUR» en la página de BELA), que coinciden. La acepto como identificación atestada por la persona.
    - **C57:** 3,35 %, fila 2026-11-17 del CSV WT1010 de la Bundesbank.
    - **Palancas!C7:** Damodaran margin.xls, «Industry Averages», fila 82, Retail (General). Es la tabla de EE. UU.: elegirla es un juicio de la etapa 1.
    - **C41 y C42:** dependían de C37 y ahora se pueden sellar.
  - **Hipótesis y convenciones (31):** C85 coincide con la decisión F1-A vigente. Las 30 de las fases tienen el valor del libro y un fundamento idéntico a Control maestro!N. En C76 = 150 comprobé la aritmética del apoyo: 150,61. El sello acredita el registro, no el acierto del juicio.
- **Discrepancias (2): C46 y C40.**
  - Valor y fórmula correctos con la C76 vigente (150): 317,9025 → 317,902 y 255,3054 → 255,305.
  - Pero la conciliación registrada sigue diciendo «C76 = 160, fase B de jumbo_e» y 317,617 / 255,108. Hay que corregir el texto.
- **Pendientes (3):**
  - C38 y C88: terceros sin bytes;
  - C31: el apoyo cita el H1-2025, que no está en `texto/`.

**`comprobar`:**
- **Cobertura:** universo 313, de las que 308 están comprobadas (213 de 214 de cálculo y 95 de 99 de juicio), más 253 auxiliares; 561 sellos.
- **Estado:** 2 discrepancias, 3 pendientes, 0 errores, 0 desactualizadas.
- **Apto por entradas: False.** Lo impiden exactamente 5 entradas materiales sin comprobar:
  - C46 y C40 (conciliación desactualizada);
  - C38 y C88 (lecturas de terceros sin bytes);
  - C31 (fuente fuera del expediente).

### jumbo_g, ronda corta tras la corrección de la orquestación (2026-11-19)

- **Material:** producto `dea03c5`, `resultados/registro_tras_sellado_jumbo_g.json`. Commit del sellado: `440f022`.
- **C46 y C40, sellados.** La conciliación ya dice C76 = 150 y cita `recalculo_dependientes.json`. Recalculé con la fórmula registrada:
  - C46: s = 450 ÷ 1.415,485114 = 0,317912 → 317,9025 → 317,902;
  - C40: 255,3054 → 255,305.
- **C38 y C88: sellado el juicio de materialidad (N1), no el dato.** Los dos siguen siendo lecturas externas sin bytes.
  - **Qué comprobé en el libro:** busqué en las fórmulas de las 11 hojas quién lee cada celda.
    - C38 solo la leen C39 → D39, C87 → D87 y E43, y el aviso Motor!E235.
    - C88 solo la lee el rótulo D88, cuya fórmula nunca escribe «BANDERA» ni «REVISAR». Así, Motor!B311 y C311 no pueden saltar por ella.
    - Ninguna fórmula de la valoración, de los escenarios ni de la Historia las usa.
  - **Qué comprobé en las fases:**
    - C38: las fases A y B no la citan. La fase C la examina en su autocomprobación de anclaje y la descarta («no uso C38 ni como contraste de la conclusión»).
    - C88: ninguna fase la cita.
  - **Límite que dejo anotado:** C38 estuvo a la vista del juicio (`datos_v63.md`), y el libro la marca «Rellenado y verificado». Que no haya anclaje lo declara la fase C; no se puede demostrar.
- **C31, pendiente:** su apoyo cita el H1-2025, que no está en el expediente.

**`comprobar`:**
- **Cobertura:** universo 313, de las que 310 están comprobadas (214 de 214 de cálculo y 96 de 99 de juicio), más 253 auxiliares.
- **Estado:**
  - 0 discrepancias, 0 errores, 0 desactualizadas;
  - 2 entradas no materiales con el juicio revisado;
  - 2 lecturas externas sin bytes, listadas aparte.
- **Apto por entradas: False.** Lo impide **una sola entrada material sin comprobar: `Análisis!C31`.**

### jumbo_g · Análisis!C31 con el informe H1-2025 (2026-11-20)

- **Material:** commits `b9c6be3` y `99b62e8`. El informe semestral H1-2025 se añadió como fuente: el PDF tiene la huella 0e69fd76…, la misma que `FUENTES.tsv`.
- **Contraste en `texto/`, y con `pdftotext` para la p. 23 del PDF:**
  - **H1-2025:** inventario 316.655.374 (p. 23; «€ 316,66 mil» en p. 8), deudores 90.278.641 (p. 23 y nota 4.11, p. 50), clientes netos 15.390.263 y ventas del 1S 497.278.437 (p. 21).
  - **H1-2026:** inventario 325.764.610 (p. 25), deudores 86.024.991 (p. 25), clientes netos 15.072.374 (p. 52) y ventas 519.257.126 (p. 23). Su comparativo de ventas coincide con el H1-2025.
- **Recálculo:** inventario +2,88 %, deudores −4,71 %, clientes netos −2,07 %, ventas +4,42 %. Ni el inventario ni los cobros crecen más que las ventas, así que sale «No» con la comparación semestral que decidió el inversor. La alternativa anual (BANDERA) queda declarada.
- **Resultado:** sellada. El sello acredita el registro, no la elección de la comparación.
- **Commit del sellado:** `39214ae`.

**`comprobar`:**
- **Cobertura:** universo 313, de las que 311 están comprobadas (214 de 214 de cálculo y 97 de 99 de juicio). Las otras dos son C38 y C88, no materiales con el juicio revisado.
- **Estado:** 0 pendientes, 0 discrepancias, 0 errores, 0 desactualizadas.
- **Apto por entradas: True.** Es condición necesaria, no suficiente: no acredita aptitud para dinero real ni sustituye la auditoría.
