# Verificación documental de Hannover Rück SE · U3 / F-C1

- **Autoría:** subagente de fuentes del coordinador, 17-nov-2026, 14:22–14:50 UTC.
- **Autorización:**
  - la persona responsable autorizó expresamente, el 17-nov, descargar desde `www.hannover-re.com`, `assets.hannover-re.com` y `hannover-re.canto.de` con un agente de usuario de navegador;
  - después aprobó añadir `hannover-re.canto.de` y `assets.hannover-re.com` al entorno. El coordinador me lo comunicó.
- **Estado:** hechos de fuente e interpretaciones. **No es una decisión, una designación ni una aprobación.** Necesita revisión por un contexto distinto.
- **Rutas:**
  - `<fuentes>` = `<fuentes_hannover>/`;
  - `<u3>` = `coordinacion/cierre_v2/u3_motor_c/` de `munger-v2-evidencias-mistral`, actualizado con `git pull --ff-only` («Already up to date»), sin cambios locales.
- **Modelo seguido:** `<u3>/verificacion_fineco_20261117/VERIFICACION_FINECO.md`. Contrato y protocolo: `<u3>/CONTRATO_C_DESDE_EL_MOTOR.md` y `<u3>/PROTOCOLO_SELECCION_C.md`.
- **Sin precios (C7):**
  - No consulté precios ni datos de mercado.
  - Contienen cotizaciones, capitalización, ratios bursátiles o recomendaciones de analistas, y **no los he usado**:
    - AR p. 7–9;
    - AR16 p. 2 y AR17 p. 2, filas «Share price» y «Market capitalisation».
  - Las hojas de consenso de analistas («HR Consensus …xlsx») enlazadas en el sitio no las descargué.
  - De AR p. 8 y p. 9 cito solo:
    - la identificación de la acción y sus mercados (p. 8 l39-62);
    - la fila de patrimonio atribuible y las notas 1, 2 y 4 (p. 9 l16, l28-31).
- **Método:**
  - descarga con `curl -sS -A '<UA de navegador>'` a través del proxy, con TLS verificado y **sin seguir redirecciones** (`--max-redirs 0`);
  - texto con `pdftotext -layout`;
  - las páginas HTML se leyeron con `grep`, sin ejecutar JavaScript;
  - para las citas, un script propio en `python3 -I` que separa páginas por salto de página.
  - No hice commit ni push, no contacté con nadie y no cambié la red.
- **Citas:**
  - «AR» = informe anual 2025 del grupo, en inglés; «AR-DE» = el mismo, en alemán; «SFCR» = SFCR del grupo 2025; «AR16» y «AR17» = informes anuales de 2016 y 2017.
  - La página es la del PDF. En AR coincide con la impresa.
  - `lN` = línea dentro de la página en el `.txt` que está junto a cada PDF. Con texto a dos o tres columnas, la línea es la de la fila del `.txt`.

---

## 1. Acceso y descargas (hechos)

| Paso | Host | Resultado | Hora UTC |
|---|---|---|---|
| Páginas de inversores (EN y DE) | `www.hannover-re.com` | 200 (CloudFront) | 14:22–14:26 |
| 1.er intento de los cinco PDF | `hannover-re.canto.de`, `assets.hannover-re.com` | CONNECT 403 del proxy (`connect_rejected`): antes de la aprobación del entorno | 14:24:00–14:24:09 |
| 2.º intento, informe anual 2025 EN | `hannover-re.canto.de` | 302 hacia `divc94363c9dd.cloudfront.net`. Ese dominio **no está autorizado** y el proxy lo rechazó (403). **No lo usé ni lo pedí.** | 14:28:58 |
| 2.º intento, los cinco PDF | `assets.hannover-re.com` | **200**, `server: AmazonS3`, sin redirección. Los bytes coinciden con el tamaño que declara el JSON de la página. | 14:29:33–14:29:36 |

**Sobre las URL:**
- La URL `assets.hannover-re.com/asset/533267266226/document_<id>/<nombre>` del informe 2025 EN aparece **literal** en `listados_ir/en_investors_results-and-reports_annual-report.html`.
- Para los otros cuatro PDF, construí la URL con el mismo patrón y el id de activo que da el JSON de `listados_ir/en_investors_results-and-reports.html`.
- Es el mismo servidor oficial. Cada `.url` guarda la URL usada.

**Incidencia propia, ya corregida en la primera entrega:** borré por error las cabeceras de las páginas HTML y las volví a descargar. El SHA-256 es idéntico al de la primera descarga.

### Archivos y huellas

| Documento | Ruta | Bytes | Páginas | SHA-256 |
|---|---|---|---|---|
| Informe anual 2025 del grupo (EN) | `<fuentes>/informe_anual_2025/2025_GBKonzern_e.pdf` | 4 833 572 | 210 | `3cff7a3aacdecb0eb2db18b3ec12f259d9a188db2cc4fedbf78998adbaee63e9` |
| Geschäftsbericht 2025 del grupo (DE) | `<fuentes>/informe_anual_2025_de/2025_GBKonzern_d.pdf` | 5 056 130 | 220 | `cef55df560fc8b1f86383526332e602185580801b3fd0c33d2c73e587b918c0c` |
| SFCR 2025 del grupo (EN) | `<fuentes>/sfcr_2025/2025_SFCR_HRGroup_E.pdf` | 2 537 196 | 56 | `3f0704045f390a16364dc45f1285c57983153982cbbce7b673b0dede0efb3f04` |
| Informe anual 2016 (EN) | `<fuentes>/serie_perimetro/2016_GBKonzern_e.pdf` | 3 347 443 | 260 | `750a5d6b6e69779a952ed46bb537698ccda150a31ca1eb8c1b794569006cc550` |
| Informe anual 2017 (EN) | `<fuentes>/serie_perimetro/2017_GBKonzern_e.pdf` | 3 524 141 | 282 | `bae4aed34a6a7d7453d8ddee433ebf69cabd3e075b0e83cefb34acb846ae62ad` |

- Cada PDF tiene junto a él `.headers`, `.fecha`, `.url` y `.txt`.
- Las páginas HTML y las URL de la serie completa están en `<fuentes>/INDICE.tsv`.
- `Last-Modified`: 12-mar-2026 para el informe anual en las dos lenguas; 01-abr-2026 para el SFCR; 15-abr-2024 para 2016 y 2017 (recarga en el servidor). **No sirve para fechar la edición.**

---

## 2. Edición (hechos)

1. **Informe anual 2025: definitivo y auditado.**
   - Informe de PricewaterhouseCoopers GmbH sobre los estados consolidados y el informe de gestión del grupo:
     - balance «as at 31 December 2025» (AR p. 197 l34-38);
     - ninguna salvedad: «has not led to any reservations» (p. 197 l29).
   - Firmado «Hannover, 10 March 2026», «sgd. Martin Eibl / sgd. Janna Reineke» (p. 201 l35-43).
   - Auditor del grupo «without interruption since the financial year 2018» (p. 201 l50).
   - En alemán: «Hannover, den 10. März 2026» (AR-DE p. 211 l11).
2. **ESEF.** El auditor certifica los documentos ESEF del archivo **`HannoverRueckSE_KA_KLB-2025-12-31-1-de.xbri`** (AR p. 200 l37; AR-DE p. 210 l62).
   - Según el auditor, el informe y su certificado se leen junto a los documentos ESEF certificados. Las versiones ESEF «are merely electronic renderings … and do not take their place» (AR p. 201 l9-24, columna derecha).
   - **No he descargado el paquete ESEF.**
3. **SFCR 2025 del grupo.**
   - Es una publicación **voluntaria**: «Please note that this report represents a voluntary publication of the Hannover Re Group» (SFCR p. 3 l51; repetido en p. 43 l13).
   - El texto no lleva fecha de aprobación ni firma. La única fecha de 2026 en el SFCR es la opinión del comité de gobierno, de 23-mar-2026, aprobada por el Consejo de Dirección (p. 15 l11-14). El PDF se creó el 24-mar-2026 (metadatos).
   - **No he encontrado ninguna declaración de auditoría del balance de Solvencia II en el SFCR.**
4. **Las cifras de Solvencia II del informe anual son provisionales:** «The Solvency II balance sheet related audit procedures have still to be completed by the independent auditor. The remaining figures have not been audited» (AR p. 35 l34-37; p. 36 l15-18).
   - Las cifras del SFCR posterior **coinciden** con las del informe anual (§5).

**Interpretación:** el informe anual es la edición definitiva y auditada. El SFCR del grupo es una publicación voluntaria, sin certificado de auditoría visible en el documento.

### C3 · Idioma fehaciente (hechos)

| Hecho | Cita |
|---|---|
| Hay dos versiones del informe anual 2025, inglesa y alemana, en el sitio oficial, con las mismas cifras. Ejemplos: patrimonio atribuible 12 928,7 / 12.928,7, minoritarios 1 001,7 / 1.001,7, beneficio del grupo 2 641,5 / 2.641,5. | AR p. 109 l35-37 y p. 110 l43; AR-DE p. 115 l35-37 y p. 116 l41-44 |
| El ESEF certificado, que es la versión reglamentaria, es el archivo **`-de`**, en alemán | AR p. 200 l37; AR-DE p. 210 l62 |
| El PDF inglés **no contiene ninguna cláusula** sobre qué versión prevalece, ni «translation», «convenience», «non-official», «authoritative» o «German original» aplicados al documento (búsqueda en el texto completo) | `informe_anual_2025/2025_GBKonzern_e.txt` |
| El informe de auditoría en inglés lleva términos jurídicos alemanes entre corchetes, «HGB [Handelsgesetzbuch: German Commercial Code]», «§ [Article]», «Satz [sentence]», y reproduce las firmas con «sgd.» | AR p. 197 l8; p. 201 l43 |
| El SFCR en inglés conserva texto alemán: «Minimum consolidated Group SCR [entspricht HRG Gruppen-MCR]» | SFCR p. 52 l30 |
| El SFCR del grupo solo se publica en inglés en el sitio. No consta una versión alemana del SFCR del grupo en las páginas guardadas. | `listados_ir/` |

**Interpretación:**
- La versión fehaciente del informe anual es, con alta probabilidad, la **alemana**: el ESEF es alemán y el informe de auditoría inglés tiene marcas claras de traducción.
- A diferencia de Fineco, **el PDF inglés no se declara traducción ni «non-official»**: simplemente no dice nada.
- Si C3 significa «publicado por la entidad en su sitio oficial», cumple. Si significa «versión fehaciente», no cumple y podría aplicar X1.
- **Es la misma pregunta pendiente que en Fineco. La decide la persona responsable.**

---

## 3. Período (hechos)

- **Informe anual:** balance «as at 31 December 2025» y ejercicio «from 1 January to 31 December 2025» (AR p. 197 l10-12, l34-38). Importes en millones de euros (AR p. 109; p. 110).
- **SFCR:** cumple el SCR y el MCR «as at the reporting date 31 December 2025» (SFCR p. 3 l38-41). Plantillas en miles de euros (p. 43).

Período **31-12-2025: verificado** en los dos documentos.

---

## 4. Perímetro (hechos)

| Punto | Evidencia |
|---|---|
| Matriz y grupo | Hannover Rück SE, Hannover, inscrita con el número HR Hannover B 6778 (SFCR p. 5 l65-69). Talanx AG tiene el 50,2 % de las acciones (SFCR p. 5 l70), y HDI V.a.G. tiene el 76,7 % de Talanx (SFCR p. 5 l8-9). **Talanx y HDI son accionistas, no perímetro.** |
| Grupo contable (NIIF) | 135 sociedades consolidadas a 31-12-2025, 17 en Alemania y 118 en el extranjero, frente a 143 en 2024; 4 por el método de la participación (AR p. 127 l42-51). |
| Cambios en 2025 | Entran 9 sociedades y salen 17, de las que 8 se fusionaron en otras del grupo (AR p. 128 l6-10). Además: <br>- alta de HR Core Europe Real Estate GmbH (AR p. 132 l45-51); <br>- baja de Hannover Finance (UK) Ltd, con una pérdida de 12,4 por reclasificación de diferencias de conversión (AR p. 132 l39-46); <br>- compra del 20 % restante de Bowen Investment LP, que reduce los minoritarios en 24,4 (AR p. 133 l11-16). <br>«No material changes occurred during the financial year in the organisational structure» (AR p. 133 l14-16, columna derecha). |
| Grupo de solvencia | Método de consolidación. La «deduction and aggregation … is not applied» (SFCR p. 40 l21-28). Las filas de otros sectores financieros (R0410–R0440) y de D&A (R0450–R0460) están vacías (SFCR p. 52 l11-21). |
| Puente NIIF → Solvencia II | Parte de «Shareholders' equity including minorities» 13 930 471 (miles de euros) (SFCR p. 37 l8), la misma cifra que el patrimonio total NIIF de 13 930,5 millones (AR p. 109 l37). |
| Supervisión | BaFin, para Hannover Re, Talanx y HDI (SFCR p. 5 l13-14) |

**Interpretación:**
- El grupo de solvencia se construye por consolidación desde el mismo patrimonio NIIF consolidado, y no hay sectores financieros no aseguradores ni D&A.
- **El SFCR no dice expresamente** que el perímetro de Solvencia II sea idéntico al contable. No hay un equivalente a la frase del Pilar 3 de Fineco. Solo se observa que el punto de partida es el mismo.
- La diferencia sustantiva está en la valoración, no en el perímetro: el CSM y otras diferencias (§5).
- Que el SFCR del grupo Hannover sea **voluntario** (§2) indica, sin que lo haya verificado, que el grupo supervisado de último nivel es otro, el de Talanx o HDI. Es un **subgrupo**.

---

## 5. Correspondencia entre el informe anual y el SFCR (hechos)

Informe anual en millones de euros; SFCR en miles de euros.

| Cifra | Informe anual 2025 | SFCR 2025 | ¿Coincide? |
|---|---|---|---|
| Patrimonio NIIF con minoritarios | 13 930,5 (AR p. 109 l37; p. 36 l8) | 13 930 471 (SFCR p. 37 l8) | Sí |
| CSM | 7 907,7 (AR p. 36 l9) | 7 907 665 (p. 37 l9) | Sí |
| Otras diferencias | −1 497,9 (AR p. 36 l10) | −1 497 871 (p. 37 l10) | Sí |
| Exceso de activos sobre pasivos | 20 340,3 (AR p. 36 l11) | 20 340 265 (p. 37 l11; S.23.01 R0700, p. 53 l10) | Sí |
| Deuda híbrida (Solvencia II) | 2 580,6 (AR p. 36 l12) | 2 580 568, Tier 2 (p. 37 l13; R0290, p. 51 l27) | Sí |
| Dividendos previsibles | −1 551,5 (AR p. 36 l13) | −1 551 475 (p. 37 l12) | Sí |
| Minoritarios no disponibles | Se mencionan sin cifra: «non-controlling interests are in part treated as non-eligible» (AR p. 35 l40-44) | −696 737 (p. 37 l14; R0210, p. 50 l41) | Solo en el SFCR |
| **Fondos propios admisibles** | **20 672,6** (AR p. 35 l25) | **20 672 620** (p. 3 l28; R0290 p. 51 l27; R0660 p. 52 l33) | **Sí** |
| **SCR** | **8 061,2** (AR p. 35 l28-29) | **8 061 199** (p. 3 l31; R0680 p. 52 l34; S.25.05 R0220 p. 55 l19) | **Sí** |
| **Ratio de solvencia** | **256,4 %** (AR p. 35 l32) | **256 %** (p. 3 l35); **2,5645** (R0690, p. 52 l36) | **Sí.** 20 672 620 / 8 061 199 = 2,5645 (cálculo mío) |
| MCR del grupo | — | 5 453 963; ratio 350 % (p. 3 l32-36; R0610 p. 52 l30) | — |
| Capital económico disponible | 21 369,4 (AR p. 35 l24; p. 36 l14) | No se publica como tal | *Cálculo mío:* 20 340 265 − 1 551 475 + 2 580 568 = 21 369 358 ≈ 21 369,4. Restando 696 737 = 20 672 621, frente a 20 672 620 publicado: diferencia de 1, por redondeo. |

**Diferencia de definición, no de cifra:**
- La «Hybrid capital» de la tabla clave del informe anual es 2 736,0 (AR p. 2 l20).
- En la conciliación de solvencia es 2 580,6 (AR p. 36 l12).
- La deuda subordinada figura en pasivos financieros a coste amortizado por 3 484,5 (AR p. 160 l15-16).
- Son tres medidas distintas. **No las he conciliado.**

---

## 6. Protocolo y contrato, criterio por criterio

### 6.1 Criterios de admisión (PROTOCOLO §2)

| Id | Resultado | Evidencia | Hecho o interpretación |
|---|---|---|---|
| C1 · Tipo | **Cumple.** Es una reaseguradora: «Hannover Re's business model has a clear focus on reinsurance», en daños y en vida y salud. | SFCR p. 5 l28-38, l66; supervisión de BaFin (p. 5 l13-14) | Hecho |
| C2 · Cotizada | **Cumple** | «Exchange listings … official trading: Xetra, Frankfurt and Hannover»; «Market segment: Prime Standard»; «First listed 30 November 1994» (AR p. 8 l47-60) | Hecho. Que el Prime Standard de Fráncfort sea un mercado regulado es conocimiento general, no citado. |
| C3 · Idioma | **Dudoso, pendiente de decisión** | §2, tabla C3 | Hecho: existe el inglés en el sitio oficial, y el ESEF es alemán. *Interpretación:* la versión fehaciente probable es la alemana. Lo decide la persona responsable. |
| C4 · 10 años | **Cumple por listado oficial.** Informe anual del grupo 2016–2025 (10) y SFCR del grupo 2016–2025 (10). Descargados 2016, 2017 y 2025. | `listados_ir/en_investors_results-and-reports.html`; URL en `INDICE.tsv`. AR16: balance consolidado a 31-12-2016 (AR16 p. 138 l1). AR17: a 31-12-2017 (AR17 p. 150 l1). | Hecho. El SFCR del grupo de 2025 es **voluntario**; no he verificado si los de 2016–2024 también lo son. Que el archivo de 2023 sea de grupo sale de su nombre (`SFCR_HRG_2023.pdf`), no está descargado. |
| C5 · Datos del motor | **Cumple** | §6.3 | Hecho |
| C6 · Fuera de muestra | **Cumple** | `git grep -il hannover`: ninguna coincidencia en `munger-v2` (HEAD `5f6b65c`). En `munger-v2-evidencias-mistral`, `origin/coordinacion/cierre-v2` y `origin/mistral/f-alcance-real` solo aparece en documentos de coordinación de U3, como candidata. La candidata `957af65` se hereda de `CANDIDATOS_C.md` §1. | Hecho |
| C7 · Sin precios | **Cumple** | Ver la cabecera | Hecho |

**Exclusiones (PROTOCOLO §3):**
- **X1:** pendiente; depende de C3.
- **X2:** no aplica. El patrimonio atribuible es 12 928,7 > 0 (AR p. 109 l35).
- **X3:** no aplica. Beneficio del grupo atribuible, 2 641,5, y minoritarios, 126,0, por separado (AR p. 110 l40-43). Patrimonio atribuible, 12 928,7, y minoritarios, 1 001,7, por separado (AR p. 109 l35-37).
- **X4:** no aplica. AR p. 9 l16 da el patrimonio atribuible de 2016 a 2025, diez ejercicios consolidados.

### 6.2 Riesgos

| Id | Situación | Evidencia |
|---|---|---|
| **R2 · Perímetro** | **Bajo en 2025:** reorganización de sociedades instrumentales, sin compra ni venta de negocio (§4). <br>**Rupturas formales de la serie:** <br>- 2016 reexpresado en AR17 por NIC 8 (presentación de DAC y de la reserva de primas), sin efecto en el beneficio; <br>- 2022 reexpresado por NIC 8 con la NIIF 17/9, ver R1; <br>- cambio de nombre de archivo de HRAG a HRSE en 2021 (forma jurídica, sin verificar). <br>2018–2024 no se ha verificado documento por documento. | AR p. 128 l6-10, p. 133 l14-16; AR17 p. 163 l3-9; AR p. 9 l28-29 |
| **R3 · Minoritarios** | **Cuantificados y moderados.** El motor dispone de las cifras atribuibles por separado. <br>Detalle en §6.4. | AR p. 109 l35-37; p. 110 l40-43; p. 162 l9-41; SFCR p. 37 l14-18 |
| **R5 · Moneda** | **Presentación en euros.** «The euro is the reporting currency» (AR p. 124 l42-43). Exposición material a otras monedas: en 2025 la conversión resta 1 353,2 en OCI atribuible (AR p. 112 l31, columna de conversión). No he encontrado que se aplique la NIC 29 (hiperinflación): solo se menciona una modificación futura de la NIC 21 (AR p. 116 l52-55). | Hecho; la hiperinflación queda sin verificar |
| **R6 · Grupo mixto** | **No mixto dentro del perímetro.** No hay entidades de crédito ni otros sectores financieros (SFCR S.23.01 R0410–R0440 vacías, p. 52 l11-16), ni D&A. La matriz última (Talanx/HDI) es un grupo asegurador, fuera del perímetro de Hannover. | SFCR p. 52; p. 5 l8-14, l70 |
| R1 · NIIF 17/9 (informativo) | Desde 2023, con 2022 reexpresado. 2016–2021 en NIC 39 / NIIF 4 (AR p. 9 l28-29). El patrimonio atribuible pasa de 11 885,0 (2021) a 9 059,7 (2022 reexpresado) (AR p. 9 l16). CSM de 7 907,7 fuera del patrimonio (AR p. 36 l9). | Hecho |
| R4 · AT1 (informativo) | **No hay instrumentos de capital en el patrimonio NIIF.** La deuda híbrida es subordinada y está en pasivos financieros a coste amortizado: cinco bonos, 3 484,5 (AR p. 160 l7-16; «Financing liabilities» en el balance, AR p. 109 l14). PD-3 no hace falta: L21 no incluye híbridos. | Hecho |
| **R7 · Límite del modelo** | **Riesgo alto, declarado.** | *Interpretación* sobre hechos, ver §7 |
| R8 · Norma o cierre (informativo) | Cierre a 31-12. Cambio de auditor: KPMG en 2016–2017 (AR17 p. 251 l4); PwC desde 2018 (AR p. 201 l50). Cambio de norma contable de seguros en 2023 (R1). | Hecho |

### 6.3 Contrato C: entradas que la fuente permite documentar

Son hechos de fuente, **no valores fijados**. Las elecciones son PD pendientes. Millones de euros.

| Celda (contrato §2) | Dato de fuente 2025 | Cita |
|---|---|---|
| `Historia!L9`, beneficio neto atribuible | 2 641,5, «Group net income» después de minoritarios (126,0) | AR p. 110 l40-43; AR-DE p. 116 l41-44 |
| `Historia!L21`, patrimonio atribuible al cierre | 12 928,7, sin AT1 dentro | AR p. 109 l35 |
| Fila 6 «Ventas» (PD-4), solo se identifica | Posibles líneas: «Reinsurance revenue (gross)» 26 786,0; «Reinsurance service result (net)» 3 496,1. Atención: en 2016–2021 la línea comparable era «Gross written premium» bajo NIIF 4 (p. ej. 16 353,6 en 2016, AR16 p. 2 l9). **Son definiciones distintas** (R1). | AR p. 110 l10, l16 |
| `Análisis!C55`, acciones | Emitidas 120 597 134 (AR p. 8 l62); media ponderada 120 597 003, sin dilución (AR p. 192 l39-43). Qué cifra y qué fecha se usan no se decide aquí. | — |
| `Historia!C9:K9`, `C21:K21` | Patrimonio atribuible 2016–2025 en AR p. 9 l16 (la serie se rompe en 2022, R1). Beneficios: AR16 p. 2 l14, AR17 p. 2 l14; para el resto, no extraídos. | — |

**Puente de patrimonio atribuible de 2025 (contrato §6), con el estado de cambios en el patrimonio (AR p. 112, columna «Equity attributable to shareholders of Hannover Rück SE»):**

```
E_2024                                         11 794,5   (l29)
+ beneficio neto atribuible                    +2 641,5   (l30)
+ OCI atribuible                                 −434,5   (l31)
− dividendos                                   −1 085,4   (l33; = AR p. 192 l19)
± cambios de participación sin pérdida de control +0,5    (l34-35)
± cambios en el perímetro (reclasificación de conversión
  por la baja de Hannover Finance UK)            +12,4    (l36; AR p. 132 l39-46)
− autocartera                                     −0,2    (l38)
  reclasificación interna OCI → reservas (−549,0 / +549,0)   0   (l37)
= E_2025 calculado                             12 928,8
  E_2025 publicado                             12 928,7   (l39)    residuo 0,1 (redondeo; cálculo mío)
```

**Interpretación:**
- **Sin recompras ni emisiones** en 2025. El reparto es solo el dividendo.
- **El OCI es material:** −434,5 en 2025 y +214,0 en 2024 (AR p. 112 l16). Un reparto implícito «beneficio − ΔB» del motor se aleja del dividendo real en el importe del OCI.
- El +12,4 de perímetro compensa una pérdida de 12,4 en resultados por la misma baja. Es un movimiento con nombre.
- El dividendo propuesto para 2025 es 1 507,5 (12,50 € por acción), con la política de dividendo cambiada en 2025 (AR p. 192 l27-28; p. 2 l43).

### 6.4 R3 · Minoritarios, cuantificados (hechos y cálculos míos)

| Medida | Importe | Cita |
|---|---|---|
| Minoritarios en el patrimonio, 31-12-2025 | 1 001,7 (2024: 893,8) | AR p. 109 l36; p. 162 l13-14 |
| Peso sobre el patrimonio total (13 930,5) | **7,2 %** (cálculo mío) | — |
| Minoritarios en el resultado de 2025 | 126,0 (2024: 68,1) | AR p. 110 l41; p. 162 l18-20 |
| Peso sobre el resultado neto (2 767,5) | **4,6 %** (cálculo mío) | — |
| Resultado global atribuido a minoritarios | 168,4 (2024: 34,8) | AR p. 111 l35 |
| **Filial principal: E+S Rückversicherung AG** | Participación y votos de los minoritarios: **35,21 %**. Patrimonio de E+S 2 757,1, del que son de minoritarios **970,7** (97 % del total de minoritarios del grupo, cálculo mío). Resultado de E+S 438,9, del que son de minoritarios 154,5. Dividendos de E+S 100,0, de los que 35,2 a minoritarios. | AR p. 162 l22-36 |
| Resto de filiales con minoritarios | Resultado de minoritarios de −28,5 en conjunto: 126,0 − 154,5 (cálculo mío; el informe no lo desglosa) | — |
| Minoritarios en sociedades personalistas | Se registran como **pasivo** (NIC 32), no en el patrimonio; su importe no lo he extraído | AR p. 162 l16-17 |
| Puente de minoritarios de 2025 | 893,8 + 126,0 + 42,4 (OCI) − 36,1 (dividendos) − 24,4 (Bowen) = **1 001,7**, residuo 0 (cálculo mío) | AR p. 112 l29-39, columna «Non-controlling interests» |
| Restricciones | «No significant restrictions on access to or the use of Group assets due to protective rights in favour of non-controlling interests». La transmisión de acciones de E+S exige aprobación. | AR p. 128 l17-23 |
| En Solvencia II | Minoritarios no disponibles a nivel de grupo: −696 737 miles de euros, «mostly … E+S Rückversicherung AG» | SFCR p. 37 l14, l18; p. 38 l18; S.23.01 R0210, p. 50 l41 |
| Serie | 743,3 (2016) y 758,1 (2017); E+S ya con el 35,21 % de minoritarios en 2016 | AR16 p. 2 l22; AR17 p. 2 l22; AR16 p. 217 l14 |

**Interpretación:**
- R3 es **moderado y bien documentado**: el grupo publica por separado el beneficio y el patrimonio atribuibles, que son lo que pide el motor C.
- El minoritario dominante (E+S) es estable en toda la ventana.
- El riesgo para el motor no es la falta de datos, sino tomar por error el resultado neto, 2 767,5, en lugar del atribuible, 2 641,5, o el patrimonio total, 13 930,5, en lugar del atribuible, 12 928,7.

---

## 7. Qué validaría del motor C y qué no

**Validaría** (interpretación sobre §4–§6):
- **L9/L21 atribuibles con minoritarios reales:** la prueba de que el motor recibe la base del accionista de la dominante (R3) es un caso que Fineco no ofrecía.
- **Puente de patrimonio con OCI material** y un movimiento de perímetro con nombre (residuo 0,1).
- **Excedente limpio frente al reparto real:** el OCI de −434,5 separa el «flujo» del motor del dividendo.
- **PD-4** con una ruptura de definición NIIF 4 → NIIF 17, y **PD-6** con la reexpresión de 2022.

**No validaría** (contrato §7):
- La **suficiencia de reservas** de siniestros: KAM «Measurement of certain liabilities from insurance contracts», AR p. 197; pasivos por reaseguro de 47 425,8, AR p. 109 l11.
- El **riesgo catastrófico**: grandes siniestros de 1 725,1 frente a un presupuesto de 2,1 mil millones, SFCR p. 6 l28-29.
- El **CSM** de 7 907,7, que es beneficio futuro fuera de B.
- La **solvencia**: ratio de 256 %, límite interno del 180 % y umbral del 200 % (AR p. 35 l17-20, columna derecha). Las cifras de §5 solo prueban la coherencia documental.
- Los **efectos de divisa**.

**R7 · Límite del modelo:**
- *Interpretación:* el valor de una reaseguradora depende sobre todo de cosas que el motor C no ve: reservas, catástrofes, CSM, capital económico y cobertura de retrocesión.
- **Es probable** que el personaje concluya `modelo_no_aplicable` (L2), o que el resultado del motor sea poco informativo.
- No es una exclusión automática (protocolo §4): lo declaro y no ordena.

---

## 8. Series disponibles (C4), por listado oficial

Según `<fuentes>/listados_ir/en_investors_results-and-reports.html` (SHA-256 `be98bdb1…9b57d39`):
- **Informe anual del grupo en inglés:** `20xx_GBKonzern_e.pdf`, 2016–2025.
- **SFCR del grupo:**
  - `20xx_SFCR_Konzern_E.pdf`, 2016–2022;
  - `SFCR_HRG_2023.pdf`;
  - `2024_SFCR_HRGroup_EN.pdf`;
  - `2025_SFCR_HRGroup_E.pdf`.
- **Informe anual en alemán:** la página alemana del Geschäftsbericht solo enlaza el de 2025.

Descargué solo 2016, 2017 y 2025. URL e intentos en `INDICE.tsv`.

---

## 9. Correcciones a `CANDIDATOS_C.md` y a la primera entrega

| Afirmación previa | Resultado |
|---|---|
| «informes en inglés» | Matizada: hay inglés y alemán. El ESEF certificado es alemán, y el inglés no declara si es fehaciente (C3). |
| «minoritarios por filiales no participadas al 100 % (R3, a cuantificar)» | Cuantificados: 7,2 % del patrimonio y 4,6 % del resultado, casi todo por E+S Rück (35,21 %) |
| «sin operación societaria relevante conocida» (R2) | Confirmada para 2025, con reorganización menor (§4). Reexpresiones de 2016 y 2022 anotadas. |
| «SFCR de grupo» (C4) | Existe en 2016–2025, pero el de 2025 es **voluntario** (subgrupo de Talanx/HDI) |
| Primera entrega: «no decidible por acceso» | Sustituida por esta verificación |

---

## 10. Conclusión

**No decidible tal como está escrito el protocolo. El único criterio abierto es C3, que corresponde a la persona responsable.** No he forzado el caso.

- **Encaja en todo lo verificable:**
  - C1, C2, C4 (por listado), C5, C6 y C7;
  - X2, X3 y X4 no aplican;
  - edición definitiva y auditada; período 31-12-2025;
  - fondos propios, SCR y ratio iguales en el informe anual y el SFCR;
  - R3 cuantificado y moderado; R5 en euros; R6 no mixto; R2 bajo en 2025;
  - puente de patrimonio con residuo de 0,1.
- **C3 (y X1) es dudoso:**
  - la versión reglamentaria (ESEF) es alemana;
  - el PDF inglés no dice si es oficial o traducción;
  - hay indicios de traducción en el informe de auditoría y en el SFCR.
  - Con C3 = «publicado por la entidad», **encaja**. Con C3 = «versión fehaciente», **no encaja**.
- **Aviso de R7, alto:** aunque encaje, es probable que el motor C no capture el negocio de reaseguro y que el personaje concluya `modelo_no_aplicable`.
- **Matices:**
  - el SFCR del grupo es voluntario y no lleva certificado de auditoría visible;
  - la serie se rompe en 2022/2023 por la NIIF 17.

*Sin valoración, sin palancas y sin precios. Ninguna cifra de este documento es una estimación de la entidad: todas son cifras de sus fuentes publicadas, o cálculos aritméticos marcados como míos.*
