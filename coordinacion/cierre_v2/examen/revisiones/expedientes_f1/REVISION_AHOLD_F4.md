# Revisión independiente · ahold_f4 (commits 08a0ba3 y bd10398)

Revisor: agente Claude distinto del autor. Revisión de solo lectura, 19-nov-2026, sin ejecutar el pipeline y sin leer `fase_a.json`. Contrasté cada cifra con `texto/` (marcas `[PDF PAGE n]`) y con `fuentes_mercado/`. Material revisado: `resultados/registro_cambios_ahold_f4.json`, `resultados/fuentes_mercado_ahold_f4.json`, `datos_v63.md` y `Ahold_v63_datos.xlsx` (solo lectura). Esta revisión no acredita aptitud para dinero real.

Leyenda de veredictos: **C** = conforme · **X** = corregir antes de la fase A · **D** = duda (la decide la persona responsable).

## 1. Cifras declaradas

| Celda | V. | Evidencia | Observación |
|---|---|---|---|
| C53 = 3.559 | C | Q3-26 p. 14, «Cash and cash equivalents 8 3,559 3,605». | Incluye el cash pool nocional de 1.176 (p. 21), que también está en la deuda: en C33 y C42 se compensa. |
| C54 = 19.747 | C | Q3-26 p. 24, «Gross debt 19,747 19,261 18,404». | — |
| C24 = 0,107 | C | Numerador: 3.542 (AR2025 p. 212) + 2.736 − 2.643 (Q3-26 p. 12) = 3.635. Denominador: 14.375 (Q3-26 p. 14) + 19.747 = 34.122. Resultado 0,10653, redondeado a 0,107. | La definición es la de la etapa 1 y las sensibilidades están declaradas. |
| C33 = 2,2073 | C | Numerador: 16.188. EBITDA: 3.635 + (3.733 [AR2025 p. 216] + 2.739 − 2.773 [Q3-26 p. 16]) = 7.334. 16.188 ÷ 7.334 = 2,20725. | — |
| C40 = 2.150 | C | Q3-26 p. 16 y AR2025 p. 216. Partidas: CFO 6.731 − capex 2.657 − intereses 265 − arrendamientos 1.956 + negocios conjuntos 22 + cobrados 128 + subarriendos 147 = 2.150. | La línea del 3T se llama «Interest **and dividend** received» (89/91) y la de 2025 «Interest received» (130). Las cifras de 2025 enlazan: 91 = 76 del 1S + 15 del 3T. La nota ya lo dice («intereses (y dividendos)»). |
| C42 = 6,5320 | C | EV = 31.971,925 + 19.747 − 3.559 − 254 = 47.905,9 (Q3-26 p. 14). 47.905,9 ÷ 7.334 = 6,532. Z-ACC declarada: con 865.173.863 acciones (Q3-26 p. 21) saldría 6,4254. Comprobado. | — |
| C31 «Sí» / C34 «No» | C | Cobros: −91 + 83 − 128 = −136. Inventario: −158 − 42 + 258 = +58 (AR2025 p. 216; Q3-26 p. 16). Cobertura: 3.559 ÷ 4.321 = 0,82x (Q3-26 p. 24). | — |
| C57 = 0,0337 | C | `Bundesbank_WT1010…txt`, fila «2026-11-13 3.37». La huella `fef9498e…` coincide con la de `RELEASE_FUENTES_EXAMEN_VERIFICACION.md`. | — |
| Palancas!C7 | C (D menor) | Damodaran, fila 83, «Retail (Grocery and Food) \| 15». La huella `25b04fce…` coincide con la Release. | Es la tabla de **empresas de EE. UU.** (F3 «US companies»). Ahold es europea y estadounidense: conviene decir por qué se usa esta tabla y no la europea. |
| Historia C22/D22 (A-NIC17) | C (D menor) | 7.560 = 3.311 + 539 + 1.761 + 199 + 57 + 1.196 + 497 (AR2017 p. 177 y p. 191). 7.251 cuadra con AR2018. | Los descubiertos de 1.196 y 1.368 incluyen el cash pool nocional (1.184 y 1.367, AR2017 p. 191), compensado también en la caja. Inflan la deuda bruta de 2016–2017; no está declarado. |
| G26/H26/K26 = 0 | C | «Non-controlling interests — —» en AR2021 p. 180, AR2022 p. 190 y AR2025 p. 212. | — |

## 2. «Control maestro!M47» y textos desfasados que lee la fase A

**M47** (fila CONTROL: «… no se suman (sensibilidad)»):
- No aparece en `datos_v63.md`. La sección 2 vuelca solo las columnas F, J, L y N de las celdas de `DATOS_ANALISIS`, y la fila CONTROL no es una de ellas.
- En `datos_v63.md` la frase solo sale citada como **sustituida** («Sustituye la decisión de la etapa 1 (Control maestro M43/M47…)», en C46, C48 y C49). No induce a error.
- Sí está en `datos_v63.json`, que el prompt de la fase A no lista. Riesgo bajo.
- Neutralización sin tocar el original: reescribir M47 en la copia de ensayo (`Ahold_v63_datos.xlsx`, igual que se hizo con M43) con la frase «Decisión sustituida por P-O1 (c) (18-nov-2026): los cobros SÍ se suman; ver C46, C48 y C49», y guardar el texto anterior en `antecedentes/evidencia_anterior.json`. El libro original de `antecedentes/etapa1_original/` no se toca.

**Hallazgos mayores:**

1. **X — La evidencia al 3T de C25, C27 y C76 no llega a la fase A.**
   - Se escribió en Control maestro **M** (filas 30, 32 y 82 de la copia de ensayo: FCF sin circulante LTM 1.725; margen subyacente LTM 4,07 %; deuda neta 16.188 y caja depurada ≈ 2.347).
   - Pero `volcar_datos_v63.py` solo vuelca la **N v1** de las celdas heredadas (sección 6), y la sección 2 no vuelca M.
   - La fase A ve solo los textos del 2T: «LTM 1.813», «2T de 2026 en 3,9 %», «€3.196m», «€16.065m», «0,87 veces».
   - **Propuesta:** llevar esos hechos, con su página, a `extracto_v63.md` mediante un relevo de extracción registrado. Alternativa: un cambio de producto, en rama nueva y con revisión, para que el volcado incluya M de las celdas heredadas.

2. **X/D — La sección 6 (heredado) y `respuesta.md` de la etapa 1 llevan cifras sustituidas sin aviso:**
   - C13: precio 33,14 €, capitalización 28.626, FCF LTM 1.821, P/FCF 15,7x frente a 14,7x, EV/EBITDA 6,1x.
     - Hoy: 36,05 €, 31.971,9, 2.150, 14,9x frente a **12,49x** y 6,53x.
     - **La comparación cambia de sentido: el precio queda más caro respecto a su historia.**
   - C14, C93, D68 y C103: ROCE 10,9 % (hoy 10,7 %).
   - C25 y C67: LTM 1.813.
   - C76: 3.196, 16.065 y 0,87x.
   - C104 y `respuesta.md`: FCF base 1.999,4 (hoy C52 = 2.312) y 881 M de acciones.
   - Todo esto es «hipótesis» (D3), pero la fase A decide «mantiene/cambia» sobre ese texto.
   - **Propuesta:** sin tocar los originales, añadir al principio de la sección 6 una tabla de vigencia («cifra citada en la etapa 1 → valor vigente → celda»). Puede generarla el volcado o ir como bloque registrado en `extracto_v63.md`.

**Otros textos que lee la fase A:**

3. **D — C37 y C41 dicen «Trivano … pendiente de fuente oficial».** `fuentes_mercado/Euronext_AD_…NO_AJUSTADO…txt` (huella en `HUELLAS.txt`) da «13/11/2026 … Close 36.05». Hay que citar Euronext como se hizo con C57.
4. **D — C38 = 61,27 (Simply Wall St).** Está marcado «Rellenado y verificado», pero el texto dice «VERIFICAR A OJO» y no hay fuente en el expediente. Debe marcarse «Dato no verificable».
5. **Menor — Contexto del 2T sin actualizar.** C60 («con Q2-26 o 1S26»), C32 («Q2-26 … 17,1 %»), C28 («Q2-26 p11») y la N de C47 («LTM: circulante del 1S26; guía FCF ≥ 2.300»). La guía se actualizó el 4-nov a unos 2.100 según M30. Basta con anotar la fecha de esa evidencia.
6. **D (afecta a todos los expedientes) — Falta `etapa1/extracto.md`.** El prompt `06_fase_a.md` lo lista como entrada (líneas 3 y 22), pero no existe en ahold_f4. Tampoco en ahold_f3 ni en jumbo_e. Hay que quitarlo del prompt o decir que no existe, para que la fase A no lo busque ni lo improvise.

## 3. Fuentes, huellas y rastro

**C.** Las fuentes nuevas de mercado son huellas de la Release, comprobadas. El Q3 (`AD_q3-2026-interim-report.txt`, `2b3df57b…`) coincide con el del registro. El original de la etapa 1 está conservado en `antecedentes/etapa1_original/`. Los auxiliares del 2T se retiran del registro y el antes de cada uno queda en `registro_cambios_ahold_f4.json`. `bd10398` solo cambia el manifiesto.

**Antes de la fase A, corregir:**
- hallazgo 1 (evidencia al 3T de C25, C27 y C76 visible para la fase A);
- hallazgo 2 (tabla de vigencia de la sección 6);
- y, si se puede, los hallazgos 3, 4 y 6.
