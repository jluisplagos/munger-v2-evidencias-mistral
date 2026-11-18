# Revisión independiente de la orquestación · Ronda 2 (commits d70635d y 6423980)

Revisor: agente Claude distinto del autor, solo lectura, 18-nov-2026. Rama `examen/expedientes-f1`. Cada cifra se contrastó con `texto/` (marcas `[PDF PAGE n]`) y con los registros `resultados/*r3*`, `recalculo_C40_C42_C88.json` y `antecedentes/`. No se leyó `fase_a.json` y no se ejecutó el pipeline. Esto no acredita aptitud para dinero real. Veredictos: **C** = conforme · **X** = corregir · **D** = duda (decide la persona responsable o un revisor económico).

## Ahold (ahold_f3)

| Punto | V. | Evidencia | Propuesta |
|---|---|---|---|
| C40 = 2.096 (FCF LTM, regla espejo) | C | Q2-26 p. 15: CFO 2.500/2.891, capex 1.229/1.227, intereses pagados 178/168, arrendamientos 980/984, dividendos de negocios conjuntos 21/22, intereses cobrados 50/76, subarriendos 74/68. AR2025 p. 216: 6.989, 2.564, 261, 1.944, 28, 130 y 138. La suma 1.821 + 27 + 104 + 144 = 2.096 cuadra. | — |
| C42 = 6,5903x | Cálculo C · fechas **D** | EV = 31.971,925 + 19.261 − 3.196 − 244 = 47.792,9. EBITDA LTM = 3.542 + 19 + 3.733 − 42 = 7.252 (Q2-26 p. 11, 13 y 15). La deuda bruta de 19.261 está en **Q2-26 p. 23**, no en las páginas citadas. | (1) Añadir la p. 23. (2) Vigencia: el informe del Q3 2026 (4-nov-2026, anterior al precio del 13-nov) está en `texto/`, y la propia etapa 1 pedía «recalcular con el Q3». Con el Q3 sale ≈ 6,53x: deuda 19.747, caja 3.559 y negocios conjuntos 254 (Q3 p. 14 y p. 24); EBITDA LTM 7.334 (Q3 p. 6 y p. 16). Con las acciones a 27-sep-2026 (865.173.863, Q3 p. 21) sale ≈ 6,43x. Pasar al Q3 o declarar por qué se queda en el Q2. La desalineación con las acciones a 28-dic-2025 (P-O2 a) tampoco está declarada en C42. |
| C88 = 12,49x | C | Capitalizaciones de AR2025 p. 65 (30.659 … 24.751). Los cobros de cada año salen del comparativo del informe siguiente (AR2020 p. 149, AR2021 p. 184, AR2022 p. 194, AR2023 p. 204, AR2024 p. 263, AR2025 p. 216). Comprobados los 7 años. Por ejemplo, 2019: 5.449 − 2.218 − 189 − 1.530 + 186 = 1.698. La mediana es 12,49. | — |
| C96 = 0,000639 | C | AR2025 p. 199: «Total … 556,165» y nota 2, «9,579 … American Depository Receipts». AR2025 p. 209: Weir 1.000; el resto del Supervisory Board no tiene acciones. 566.744 ÷ 886.877.259 = 0,000639. | — |
| C26 sin cambio | C | Σ CFO 2021–2025 = 31.257. Las variantes de la regla espejo cuadran: 138 / 558 / 598. | — |
| Rastro | C | Las copias de antes están en `antecedentes/etapa1_antes_de_C40_C42_C88` y `entradas_antes_de_r3`, con huellas. | Queda pendiente retirar `aux:etapa1_capitalizacion_oct2026` del registro auxiliar, como dice el propio registro. |

## Jumbo (jumbo_e)

| Punto | V. | Evidencia | Propuesta |
|---|---|---|---|
| C40 = 254,32 | C | AR2025 p. 155: CFO 296.912.917, capex 38.384.015, «Lease repayments» 2.325.789 (interés, J3), «Interest paid for leases» 9.727.205 (principal), dividendos 1.876.200, intereses 9.916.790. Cupones 595.058 (p. 179), s = 200 ÷ 471,8284. 246,476 + 1,8762 + 5,9655 = 254,318. | — |
| C96 = 16,63 % | C · redacción D | AR2025 p. 48: Vakakis 22.339.966 indirectas, Athanasiou 360. p. 49: Terzaki 2.022. p. 16: 134.365.561 acciones. Resultado 0,166280. | La nota afirma como hecho que el 16,42 % impreso (p. 143) está calculado sobre 136.059.759 acciones. Es una inferencia aritmética: 22.339.966 ÷ 136.059.759 = 16,419 %. Escribirla como inferencia. |
| C42 con la desalineación declarada | C | 7,441x / 7,746x, con el dividendo del H1 2026 p. 20. El valor no se ajusta y queda pendiente de decisión. | — |
| C88 «no verificable» | C | Capitalizaciones de terceros sin bytes en el expediente; la marca F está puesta. | — |
| Adquisiciones 2019 y 2021, de vuelta a cero pendiente | C | Hay 28 pendientes otra vez (2016, 2017, 2019, 2020 y 2021). Citas: transición p. 57 y AR2021 p. 63, «Share Capital Change of Subsidiaries», «-» en el grupo. | El cero de 2019 es del año natural, pero el informe de transición solo cubre jul–dic 2019. Basta con anotarlo: el cero sigue pendiente. |
| Citas del bloque de financiación (p. 46 y p. 48) | C | AR2016-17 p. 46 y AR2018-19 p. 48: no hay línea de arrendamientos en financiación. | — |
| PPA de 2023 con NIVAMO | C · redacción D | AR2023 p. 16 y p. 71. | El motivo dice «hubo una combinación de negocios», pero el texto solo dice que se compró el 100 % de una sociedad inmobiliaria; no la califica como combinación (NIIF 3) ni como compra de activos. Escribir «compra de una sociedad dependiente». |
| Rastro | C | `fase1_partes_antes_de_r3`, `motor_a_f1_antes_de_r3` y la adenda de `cambio_de_base.md`. | — |

## Zoetis (zoetis_t1c)

| Punto | V. | Evidencia | Propuesta |
|---|---|---|---|
| C41 = 31.053,73824 «sin redondear» | **X** | La cifra sale de 73,08 × **424,928**, que es C55 redondeado. El 10-K 2025 p. 68 y el 10-Q T2 p. 5 dan 424.927.535 acciones, y 73,08 × 424,927535 = **31.053,704**. El 31.053,7 anterior era el exacto. | Poner C55 = 424,927535 y C41 = 31.053,704. C42 no cambia en 4 decimales (9,6758). |
| C42 = 9,676x y C33 = 1,897x | Cálculo C · fechas **D** | 10-Q T2 2026: p. 3 (BAI 1.624/1.685, intereses 123/107), p. 5 (deuda 9.048, caja 1.476), p. 8 (D&A 238/243), p. 10 (BAI «as previously reported» 1.712). TTM: 3.272 + 238 + 482 = 3.992. La aproximación por la «Fiscal Year Alignment» está declarada. | El balance es del 30-jun-2026, pero C41 usa las acciones del 31-dic-2025. El 10-Q p. 5 da **414.154.046** acciones a 30-jun-2026 (−2,5 %, recompras pagadas con la caja de ese balance). Con ellas, C42 ≈ 9,48x. Declarar la desalineación, como en Jumbo. C33 no depende de las acciones. |
| C40 = 2.363 | C | CFO 2.904 − 1.073 + 1.056 = 2.887 (10-Q p. 8 y p. 11); capex 621 − 324 + 227 = 524; principal de arrendamientos financieros 2 − 2 + 0 (p. 8, «— 2»). La mezcla de bases está declarada; todo reexpresado da 2.316. | — |
| C88 no verificable | C | Precios de terceros sin bytes en el expediente; marca F puesta. | — |
| PPA como cota superior; A1 = 2.624,9 | C · rastro D | La página de la definición ya es la p. 52. El sesgo optimista y la comprobación 325 + 34 + 128 = 487 están declarados. | Las cifras de A1 (f 0,0255 frente a 0,0101; 2.624,9 frente a 2.771,1) no están en ningún archivo del expediente; solo aparecen en la nota y en el guion. El pipeline está en el paso 6. Guardar la salida del diagnóstico (orden y archivo) en `resultados/`, o marcar las cifras como no reproducibles en el expediente. |
| L17, E13, extracto | C | La nota de L17 dice «ubicación no publicada». La duda de E13 está anotada sin cambiar la cifra. Extracto: ganado 731 en FR p. 15 y EC p. 7, y 12 marcas «(paráfrasis traducida)». | — |
| Rastro | C | `metadatos_antes_de_C41_r3`, `entradas_antes_de_r3`, `extracto_v63_antes_de_r3` y `motor_a_f1_antes_de_r3`, con huellas. | — |

## Fuentes y huellas

**C.** Ninguno de los dos commits toca `texto/`, `pdf/`, `FUENTES.tsv` ni `fase1_fuentes.json`. Todo cambio deja su copia anterior en `antecedentes/`.
