# Entrega · Registro de entradas de Jumbo S.A. (examen del personaje)

- **Extractor:** Mistral (mistral-large-4-0), fecha 2026-11-18. Todas las comprobaciones quedan `pendiente` (revisor = null, sin `vinculo`): no sello nada; el agente Claude distinto revisa y sella.
- **Alcance:** las 283 entradas con `en_este_encargo` = «sí» de las 313 de la plantilla. Las 30 hipótesis se dejan sin tocar.
- **Entrega:** `resultados_examen/jumbo/verificacion_entradas.json` (313 entradas del universo + 246 auxiliares `aux:`), `fuentes_mercado/` con `HUELLAS.txt`, `DESCARGAS.tsv`, este `ENTREGA.md`.

## Resultado por clase (universo, 313 entradas)

| clase | n |
|---|---|
| derivado | 176 |
| dato_ausente | 38 |
| dato_publicado | 27 |
| cero_comprobado | 22 |
| hipotesis (sin tocar) | 30 |
| convencion | 4 (Palancas!C45, C46, Palancas!A32, Control maestro!J4) |
| no_aplicable | 6 |
| **sin resolver (clase null, declaradas abajo)** | **10** |

## Verificación ejecutada

`verificacion_entradas.py comprobar` (rama `examen/ahold-f1` de `jluisplagos/munger-v2`) sobre una copia del expediente `jumbo_c/Jumbo` con este registro: **cobertura completa (313/313, sin sobrantes ni repetidas), 0 discrepancias, 0 desactualizadas**. Los únicos errores de contrato son los 30 de las hipótesis (las escriben las fases del personaje, igual que en Ahold) y las 10 sin resolver declaradas aquí. Comprobación adicional propia: las 176 fórmulas derivadas se evaluaron con aritmética exacta (`_eval_formula_exacta`) y **todas reproducen el valor del libro**; todas las citas pasan `contraste_pagina` (cita literal en la página `[PDF PAGE n]` con el valor y su signo). Los 17 documentos de la Release `fuentes-examen-20261118` descargados con `gh release download` coinciden 17/17 en SHA-256 con `RELEASE_FUENTES_EXAMEN_SHA256SUMS` (ver `DESCARGAS.tsv`).

## Detalles clave del registro

- **Unidades:** los estados de Jumbo están en euros enteros; el libro trabaja en mm. Cada entrada declara `escala` 1e-6 y las filas numéricas de la Historia van como `derivado` `round(aux, 4)` (el libro guarda 4 decimales en mm). `Control maestro!J4` = «mm» se declara `convencion` (el texto de la fuente no puede contener «mm»).
- **Ejercicios:** 2016 = 1-jul-2016 a 30-jun-2017, 2017 = 2017/18, 2018 = 2018/19; **2019 se lee de la columna comparativa del informe 2020 (año natural 1-ene a 31-dic-2019)**; la transición de 6 meses (1-jul a 31-dic-2019) no entra en la Historia (J-T). Desde 2020, año natural. El `periodo` lleva las fechas exactas.
- **2022 y 2023:** conversiones registradas de los XHTML ESEF oficiales (LEI 549300TGIVUUMY40MZ05); `version` = XHTML original + sha256 y la conversión registrada (anexo de `RELEASE_FUENTES_EXAMEN_VERIFICACION.md`); en `tratamiento` se anota que la página es la de la conversión.
- **Cruce de etiquetas J3 (2020–2025):** «Lease repayments» = interés y «Interest paid for leases» = principal en el estado de flujos. Se registra la cifra **tal como está impresa** y en `tratamiento` se explica el cruce con la página de la nota de costes financieros de cada informe que lo prueba (p. 86/87/92/95/178/179) y las pruebas comunes (transición 2019 p. 57/84; H1 2026 p. 30 rotulan bien).
- **C46 (J1+J2):** derivado declarado en `cambio_jumbo_c.json` con 15 aux publicados (CFO, dividendos de la cartera, intereses cobrados, cupones de bonos y caja de cierre 2023–2025, en euros) y `Análisis!C76`; lleva `justificacion_clase` por depender de la hipótesis C76. C48/C49 salen de la Historia corregida por J3 (medias 2023–2025 sobre las filas 16/17).
- **Acciones:** 134.365.561 en circulación a 31-dic-2025 (nota de capital AR2025 p. 142; también p. 181), sin autocartera ni dilutivos (P-O2).
- **Precio C37 = 27,28 € (17-nov-2026):** verificado por la persona responsable en la página oficial de Euronext Athens (registro `JUMBO_BELA_20261118.md`, copia en `fuentes_mercado/` con sha256). **No pude descargar el histórico de Euronext Live desde esta sesión** (el endpoint público `getFullDownloadAjax` no devolvió filas): lo declaro; C37 queda como lectura externa con la evidencia de la persona responsable. Ex distribución extraordinaria de 1,00 €/acción (fecha ex 16-nov-2026): el precio es sin derecho a ella.
- **Tasa sin riesgo C57 = 3,35 % (0,0335):** **AVISO: no pude acceder a Deutsche Bundesbank ni al BCE Data Portal desde esta sesión** (bloqueo de acceso automatizado / comprobación de seguridad), así que no hay bytes oficiales conservados y **no pongo otra fuente como oficial**: se declara lectura externa con las lecturas recogidas en `datos_v63.md` (Trading Economics 3,35 % el 18-nov; Ideal-investisseur 3,35 % el 17-nov, que declara fuente Deutsche Bundesbank; rango 3,35–3,38 %).
- **Caja y depósitos (C53):** efectivo y equivalentes a 30-jun-2026 = 546.140.091 € (H1 2026 p. 25); la cartera de acciones/bonos cotizados y los depósitos restringidos no son caja. C54 = deuda total H1 2026 = total lease liabilities 62.247.015 € (p. 57; bono de 200 mm prepagado el 29-may-2023).

## Sin resolver (10, clase null) y por qué

- `Historia!I17` (7,0351) y `Historia!L14` (61,1585): el impreso exacto es 7.035.150 / suma −61.158.550; el libro guarda el empate redondeado en coma flotante (7,0351 / 61,1585); ninguna variante de fórmula exacta lo reproduce (diferencia 0,00005 mm = 50 €). No fuerzo.
- `Análisis!C28` («Recompra"), `C31` («No»), `C34` («Sí»): veredictos de texto de juicio de la etapa 1; no son cifras impresas ni fórmulas sobre celdas.
- `Análisis!C32` (0): el balance AR2025 no publica línea de goodwill (solo intangibles agregados, p. 150; nota 4.3 p. 161 sin importe): no hay cita con guion/0 que pruebe el cero mecánicamente.
- `Análisis!C33` (−1,0992): no impreso como ratio en el H1 2026; mejor fórmula con deuda neta H1 (−483,893) y EBITDA LTM ≈ 440,23 (no impreso como cifra única) da ≈ −1,0992.
- `Análisis!C42` (6,4458 EV/EBITDA): no impreso en el H1 2026 ni reproducible con EV sobre EBITDA LTM publicado.
- `Análisis!C60` (−0,0025): CAGR 5a de acciones = −0,2507 % → round 4 = −0,0025 = libro, pero la fórmula usa una potencia, que el registro no admite.
- `Análisis!C96` (0,1663): 16,63 % no aparece impreso en AR2025 ni en H1 2026 (AR2025 p. 143 imprime TANOCERIAN 16,42 % / 16,419 %).

## Fuentes de mercado y lecturas externas

`fuentes_mercado/HUELLAS.txt` trae los sha256 de `JUMBO_BELA_20261118.md` (evidencia del precio, lectura de la persona responsable) y del extracto Damodaran `mgnroc.html` (enero 2026, fila «Retail (General)», usada por Palancas!C7). C38 (Simply Wall St) y C88 (MarketScreener/StockAnalysis) son lecturas externas de terceros sin bytes conservados, declaradas en su entrada.

## Modelo y herramientas realmente usados

Modelo `mistral-large-4-0` (Vibe Code, sesión del 2026-11-18). Herramientas: `gh` (clone y `gh release download`), Python 3.12 con el módulo `verificacion_entradas.py` del repo del producto para autocomprobar citas, fórmulas y cobertura; `web_fetch`/`web_search` para Euronext Athens, Bundesbank, BCE y Damodaran (los dos primeros bloquearon el acceso automatizado). No se ejecutó LibreOffice ni el pipeline; no se escribió en `jluisplagos/munger-v2`; no hay PDF/XLSX/ZIP en el commit.
