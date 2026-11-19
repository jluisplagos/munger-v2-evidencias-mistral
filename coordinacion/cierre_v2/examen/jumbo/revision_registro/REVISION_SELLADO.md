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
