# Verificación documental de FinecoBank · U3 / F-C1

- **Autoría:** subagente de fuentes del coordinador, 17-nov-2026, 13:25–13:40 UTC. Autorización: decisión U3 de la persona responsable (descarga desde `finecobank.com` y sus subdominios).
- **Estado:** hechos de fuente e interpretaciones. **No es una decisión, una designación ni una aprobación.** Necesita revisión por un contexto distinto.
- **Rutas:** `<fuentes>` = carpeta de esta entrega; `<u3>` = `coordinacion/cierre_v2/u3_motor_c/` de `munger-v2-evidencias-mistral` (actualizado con `git pull --ff-only`, sin cambios locales en `<u3>`).
- **Contrato y protocolo aplicados:** `<u3>/CONTRATO_C_DESDE_EL_MOTOR.md` y `<u3>/PROTOCOLO_SELECCION_C.md`, en la versión del repositorio a 17-nov-2026.
- **Sin precios (C7).** No he consultado precios de mercado. La página 35 del informe anual incluye cotizaciones y capitalización (l11-29): **no las he usado**. Solo cito de esa página el número de acciones (l33) y el historial de dividendos (l37-53).
- **Método:** `curl -sSL -A 'Mozilla/5.0'` a través del proxy, con TLS verificado; `pdftotext -layout`, y, para el ESEF, lectura del iXBRL con `python3 -I` (expresiones regulares sobre el texto, sin extraer el ZIP ni ejecutar nada). No hice commit ni push y no contacté con nadie.
- **Citas:** «AR» = informe anual 2025 (página del PDF = página impresa). «P3» = Pilar 3 a 31-12-2025: cito la página del PDF y entre paréntesis la impresa (impresa = PDF − 2). «AR16» y «AR17» = informes de 2016 y 2017, con página del PDF (impresa = PDF − 2). `lN` = línea dentro de la página en el `.txt` de `pdftotext -layout` que está junto a cada PDF.

---

## 1. Acceso y descargas (hechos)

| Paso | URL | Resultado |
|---|---|---|
| Portada | `https://finecobank.com/` | 200 tras redirección a `https://it.finecobank.com/` |
| Relación con inversores | `https://about.finecobank.com/it/investors/risultati/` | **CONNECT 403 del proxy** (13:25Z): el host no estaba en la lista permitida del entorno |
| Documentos | `https://images.finecobank.com/...` | **CONNECT 403 del proxy** (13:25Z), por la misma causa |
| Cambio de entorno | — | Propuse añadir **solo** `about.finecobank.com` e `images.finecobank.com` al entorno personal «munger-v2 (fuentes Elis)». La persona lo **aprobó** en la ventana de permisos. **Esos dos hosts siguen en el entorno**; si se quieren quitar, lo decide ella. |
| Ruta supuesta | `https://about.finecobank.com/en/investors/results/` | 404 (la ruta real es `/en/investors/`) |
| Resto | ver `<fuentes>/INDICE.tsv` | Todas las descargas dieron 200 |

- No toqué otros dominios. Los comunicados de resultados se enlazan en `images.fineco.it`, que es **otro dominio**: no lo he consultado.
- Todos los PDF de 2025 tienen `Last-Modified: Fri, 27 Mar 2026 12:38:5x GMT` (carga conjunta en el servidor). Esta fecha no sirve para fechar la edición.

### Archivos y huellas

| Documento | Ruta | Bytes | SHA-256 |
|---|---|---|---|
| Accounts and Reports 2025 (EN) | `<fuentes>/informe_anual_2025/accounts-and-reports-2025.pdf` | 12 539 882 | `ef5445c34bca26f6fee28b9e4f025f4907e0ffa19980913204039b31863941c8` |
| Pillar III a 31-12-2025 (EN) | `<fuentes>/pilar3_2025/public-disclosure-pillar-III-december-31-2025.pdf` | 2 067 502 | `f6717b644857f31611cdc17f04372aeb40d92aeae22134a2d1c37e0404b338e0` |
| ESEF 2025 (IT) | `<fuentes>/esef_2025/549300L7YCATGO57ZE10-2025-12-31-1-it.zip` | 15 012 546 | `4ef57405261c20d887520c5953211c56374cecc9d6e06d98dd86fcf31549e363` |
| Votaciones de la junta del 29-abr-2026 | `<fuentes>/verificacion_edicion/votes-summary-report-290426.pdf` | 391 887 | `d34d6d52…69e9` |
| Convocatorias de las juntas extraordinarias del 10-mar y 29-jun-2026 | `<fuentes>/verificacion_edicion/` | 390 346 / 426 210 | `21e2ab45…fe8` / `b68cb5b9…e9` |
| Informes 2016 y 2017 (solo perímetro) | `<fuentes>/serie_perimetro/` | 3 569 871 / 2 818 356 | `d21e459b…2513` / `bcccdadd…6ccf` |

Las huellas completas, las URL y las fechas están en `<fuentes>/INDICE.tsv`. Cada descarga conserva junto al archivo sus cabeceras HTTP (`.headers`), su fecha (`.fecha`) y el texto extraído (`.txt`).

---

## 2. Edición (hechos)

1. **El PDF inglés es una traducción de cortesía, no la versión oficial.**
   - AR p. 10 l29: «This report has been translated into the English language solely for the convenience of international readers».
   - AR p. 529 l9-12 (auditor): «The accompanying translated consolidated financial statements … constitute a **non-official version** … only the original Italian version is authoritative».
   - AR p. 10 l25-26: el PDF «does not fulfill the obligations» de la Directiva de Transparencia ni del Reglamento ESEF.
2. **Existe el ESEF/xhtml, solo en italiano.**
   - El paquete ZIP y el xhtml de 2025 se enlazan en `/en/investors/` como «Accounts and Reports 2025 (ESEF)». Ver `<fuentes>/listados_ir/about_finecobank_en_investors.html`.
   - El iXBRL lleva `xml:lang="it"` y el título «FinecoBank S.p.A. - 549300L7YCATGO57ZE10 - 2025».
   - Opinión ESEF del auditor: AR p. 535 l17-19.
   - El nombre del archivo lleva el sufijo «-1» (el de 2024 lleva «-0»). Qué significa ese número **no lo he verificado**.
3. **Aprobación.**
   - El Consejo aprobó los estados consolidados el 3-mar-2026 y autorizó su publicación (AR p. 295 l20-21).
   - Certificación art. 81-ter: 3-mar-2026 (AR p. 525 l39).
   - Informe de KPMG con opinión favorable y sin salvedades (AR p. 529 l29-30), firmado en Milán el 24-mar-2026 (AR p. 536 l12).
   - La junta del 29-abr-2026 **aprobó las cuentas individuales de 2025 y se le presentaron las consolidadas**: votos a favor 99,36 % (votes-summary p. 1 l15-20). Aprobó también el reparto del beneficio (p. 1 l28-33).
   - En Italia la junta no aprueba las cuentas consolidadas: solo se le presentan. Esto es contexto legal, no un dato del documento.
4. **El ESEF coincide con el PDF inglés** en las cifras clave (miles de euros):
   - activo 37 295 901;
   - beneficio atribuible 647 041;
   - patrimonio atribuible 2 553 324, con minoritarios «-»;
   - instrumentos de capital 500 000;
   - OCI 136;
   - resultado global 647 177.

   Etiquetas `ifrs-full:Assets`, `ifrs-full:ProfitLossAttributableToOwnersOfParent`, `finecobank:TotalEquityAttributableToOwnersOfParent` con miembro `EquityAttributableToOwnersOfParentMember` y `finecobank:StrumentiDiCapitale`.
5. **Pilar 3.**
   - Declaraciones del directivo responsable (art. 154-bis) y de cumplimiento de la Parte Octava del CRR, ambas de 3-mar-2026 (P3 p. 157 l23 (imp. 155) y p. 159 l25 (imp. 157)).
   - Se publica también en italiano (`informativa-pubblico-pillar-III-31-dicembre-2025.pdf`, 200 por cabecera, no descargado).
   - El PDF inglés no lleva ninguna cláusula sobre qué versión prevalece.
   - Algunas tablas conservan texto en italiano: EU LI1, P3 p. 26 l10-20; EU CC2, P3 p. 42 l16-25.

**Interpretación:** la edición es la definitiva: aprobada por el Consejo, auditada y presentada a la junta. La **versión oficial** es la italiana (ESEF). La inglesa es una traducción publicada por la propia entidad.

---

## 3. Período (hechos)

- Balance a «12/31/2025» y «12/31/2024» (AR p. 283 l15). Cuenta de resultados de 2025 y 2024 (AR p. 285 l11). Importes en miles de euros (AR p. 283 l13).
- Pilar 3 «as at 31 December 2025» (P3 p. 1 l1-4). EU KM1, columna a = 12.31.2025 (P3 p. 32 (imp. 30) l6).
- No hay cambio en el saldo de apertura de 2025: la columna «Change in opening balance» está a «-» (AR p. 287 l113-125).

Período **31-12-2025: verificado**.

---

## 4. Perímetro (hechos)

| Punto | Evidencia |
|---|---|
| Grupo contable | Matriz FinecoBank S.p.A. y **Fineco Asset Management DAC** (Dublín), con un 100 % de participación y de votos, consolidada por integración global (AR p. 292 l18-23, l39). «There are no companies indirectly controlled» (l19). |
| Cambios en 2025 | «There are no changes in the scope of consolidation since December 31st, 2024» (AR p. 292 l30-31) |
| Asociada | Vorvel SIM S.p.A. (20 %), consolidada por el método de la participación con datos **preliminares** (AR p. 292 l26-27; p. 354 l27, l70). Su valor en libros es 1 756 (AR p. 283 l27). |
| Grupo prudencial | «FinecoBank Banking Group … consisting of the Parent Company FinecoBank S.p.A. and Fineco Asset Management DAC» (P3 p. 25 (imp. 23) l12-13). Vorvel también por el método de la participación (l14-15). |
| **Mismo perímetro contable y prudencial** | En EU LI1 las columnas a y b van fusionadas «as the scope of accounting consolidation and the scope of prudential consolidation are the same» (P3 p. 25 (imp. 23) l22). EU CC2: «There are no differences in the accounting figures for the Balance Sheet Perimeter and the Prudential Perimeter» (P3 p. 42 (imp. 40) l29). |
| Matiz prudencial | Fineco AM no está sujeta a CRR/CRD, sino a normas irlandesas de capital que limitan la transferencia de capital o dividendos (P3 p. 29 (imp. 27) l7-10) |
| Minoritarios | Partida 190: «No data to report» (AR p. 387 l34-37). SOCE, fila «Minorities»: «-» (AR p. 287 l127-129). CC1, fila 5: «-» (P3 p. 36 (imp. 34) l23). |
| Supervisión | Entidad significativa, supervisada directamente por el BCE (AR p. 50 l6-7). Banco inscrito en el registro de bancos y matriz del grupo bancario n.º 3015 (P3 p. 3 l29-32). |

### Perímetro de la serie (para C4 y R2)

- **2016:** solo estados individuales. «At the balance sheet date, the Bank held no investments in subsidiaries, associates and joint ventures» (AR16 p. 89 l50). El índice no tiene estados consolidados (AR16 p. 5 l31-36). La portada dice «Member of UniCredit» (AR16 p. 3 l1).
- **2017:** «FinecoBank presents consolidated financial statements **for the first time** for the year ended December 31, 2017 … as it controls Fineco AM Limited, an Irish company **incorporated on October 26, 2017** … the figures from the previous year's **separate** financial statements of the Bank are provided for comparative purposes» (AR17 p. 108 (imp. 106) l50-52).
- **2017, ratios prudenciales:** se calcularon en base individual, «as FinecoBank is not required to prepare the disclosure relating to own funds and regulatory ratios on consolidated basis as it is part of the UniCredit banking group» (AR17 p. 21 (imp. 19) l71-72).
- **2018–2024:** no descargados. La fecha de la salida del grupo UniCredit y del inicio del grupo bancario FinecoBank **no la he verificado** en una fuente.

**Interpretación:**
- El perímetro económico 2016–2025 es estable. No hay adquisiciones ni ventas: la única filial es de creación propia (2017).
- Hay **dos rupturas formales**:
  - 2016 es individual, no consolidado;
  - el perímetro prudencial cambia: en 2017 la entidad estaba dentro del grupo UniCredit; en 2025 es la matriz de su propio grupo bancario.
- Para 2025 el Pilar 3 tiene **el mismo perímetro** que el informe anual.

---

## 5. Correspondencia entre el informe anual y el Pilar 3 (hechos)

Miles de euros.

| Cifra | Informe anual 2025 | Pilar 3 a 31-12-2025 | ¿Coincide? |
|---|---|---|---|
| CET1 | 1 445 203 (AR p. 24 l42) | 1 445 203 (KM1, P3 p. 32 (imp. 30) l8; CC1 fila 29, P3 p. 37 (imp. 35) l26) | Sí |
| Tier 1 = fondos propios totales | 1 945 203 (AR p. 24 l43, l54); 1 945,2 millones (AR p. 82 l7) | 1 945 203 (KM1 l9-10; P3 p. 35 (imp. 33) l24; CC2, P3 p. 42 (imp. 40) l26) | Sí |
| AT1 | Instrumentos de capital 500 000 (AR p. 284 l25) | AT1 500 000 (CC1 fila 44, P3 p. 37 (imp. 35) l62); LI1 fila 21 (P3 p. 27 (imp. 25) l41) | Sí |
| Tier 2 | «there are no Tier 2 capital elements» (AR p. 82 l10-11) | T2 «-» (P3 p. 43 (imp. 41) l31-33) | Sí |
| APR (RWA) | 6 201 582 (AR p. 24 l44); 6 201,6 millones (AR p. 82 l12) | 6 201 582 (KM1, P3 p. 32 (imp. 30) l12) | Sí |
| Ratio CET1, Tier 1 y total | 23,30 %, 31,37 %, 31,37 % (AR p. 24 l45-47) | 23,30 %, 31,37 %, 31,37 % (KM1 l15, l17, l19) | Sí |
| Apalancamiento | 5,07 % (AR p. 24 l56) | 5,07 % (KM1 l52) | Sí |
| Activo total | 37 295 901 (AR p. 283 l35) | 37 295 900 (LI1, P3 p. 26 (imp. 24) l45; CC2 P3 p. 42 l25) | Diferencia de 1, por redondeo |
| Beneficio neto | 647 041 (AR p. 284 l30; p. 285 l54) | 647 041 (LI1 fila 26, P3 p. 27 l46; CC2 fila 26, P3 p. 42 l15) | Sí |
| Capital, prima y autocartera | 201 820 / 1 934 / (1 280) (AR p. 284 l27-29) | Iguales (CC2 filas 23-25, P3 p. 42 l12-14) | Sí |
| Reservas, partida 150 | 1 222 722 (AR p. 284 l26) | 1 222 720 (LI1, P3 p. 27 l42) | Diferencia de 2, por redondeo |
| Reservas de valoración | (18 913) (AR p. 284 l24) | (18 912) (LI1, P3 p. 27 l40) | Diferencia de 1 |
| Reservas de beneficios | 1 166 080 (SOCE, AR p. 287 l118) | 1 166 078 (CC1 fila 2, P3 p. 36 l15) | Diferencia de 2 |
| Dividendo propuesto del ejercicio 2025 | 483 393 576,37 € (AR p. 281 l22); 483,4 millones (AR p. 82 l8) | 483 394 (P3 p. 31 (imp. 29) l46-47) | Sí |
| Beneficio intermedio computado en CET1 | 155,4 millones (AR p. 82 l21) | 155 447 (CC1 EU-5a, P3 p. 36 l25) | Sí |
| Cupones AT1 devengados como carga previsible | 8,2 millones (AR p. 82 l9) | Implícitos: 491 594 − 483 394 = 8 200 (CC2 fila 27, P3 p. 42 l17) | Sí (cálculo mío) |
| Patrimonio contable total | 2 553 324 (AR p. 287 l125; ESEF) | 2 553 323, suma mía de las filas 20-26 de LI1 | Diferencia de 1, por redondeo |

**Discrepancias y erratas de la traducción inglesa** (hechos; ninguna afecta a las cifras del motor):
- **D1.** AR p. 82 l20 dice «Tier 1 capital ratio stood at 23.30%». El 23,30 % es el ratio **CET1** (AR p. 24 l45; KM1 l15). El Tier 1 es 31,37 %.
- **D2.** La nota del SOCE consolidado (AR p. 287 l131) fecha la junta el «April 24th, 2025». La tabla de dividendos (AR p. 35 l45: 04/29/2025), la nota 13.4 (AR p. 386 l35) y el SOCE individual (AR p. 549 l108) dicen **29 de abril de 2025**.
- **D3.** Fecha de emisión del AT1: «4 March 2024» (AR p. 387 l22; P3 p. 40 (imp. 38) l9) frente a «11/03/2024» en EU CCA (P3 p. 48 (imp. 46) l27). *Interpretación no verificada:* fecha de fijación del precio frente a fecha de desembolso.
- **D4.** El SOCE de 2024 muestra los instrumentos de capital en 500 000 al principio y al final, sin movimiento (AR p. 287 l244), aunque el instrumento vigente se emitió en marzo de 2024. Cómo se sustituyó el instrumento anterior **no lo he verificado** (haría falta el informe de 2024).

---

## 6. Protocolo y contrato, criterio por criterio

### 6.1 Criterios de admisión (PROTOCOLO §2)

| Id | Resultado | Evidencia | Hecho o interpretación |
|---|---|---|---|
| C1 · Tipo | **Cumple.** Es un banco (entidad de crédito). | «Bank enrolled in the Register of Banks and Parent Company of the FinecoBank Banking Group» (P3 p. 3 l29-32); supervisión directa del BCE (AR p. 50 l6-7). Sin actividad aseguradora: la única filial es una gestora UCITS (AR p. 292 l39; AR p. 95 l6). | Hecho |
| C2 · Cotizada | **Cumple** | «FinecoBank is listed on the Milan Stock Market and is included on Borsa Italiana's FTSE Mib» (AR p. 13 l18). Euronext Milan es un mercado regulado del EEE: conocimiento general, no citado en el documento. | Hecho, más contexto |
| C3 · Idioma | **Dudoso, pendiente de decisión** | Hay informe anual consolidado en inglés en el sitio oficial, pero declarado **«non-official version … only the original Italian version is authoritative»** (AR p. 529 l9-12). El ESEF, la versión reglamentaria, solo existe en italiano. | Hecho. **Que cumpla o no depende de qué signifique «oficial» en C3 y X1:** (a) publicado por la entidad en su sitio oficial: cumple; (b) versión fehaciente: no cumple, y además X1 podría aplicar. Lo decide la persona responsable. |
| C4 · 10 años | **No cumple tal como está escrito**: hay 9 informes consolidados (2017–2025), no 10 | 2016 solo tiene estados individuales y no hay filiales (AR16 p. 89 l50). Los primeros consolidados son de 2017 (AR17 p. 108 l50-52). Listado oficial de los informes anuales de 2014–2025 y del Pilar 3 de 2014–2025: `<fuentes>/listados_ir/about_finecobank_en_investors.html`, URL en §8. Descargué el último informe anual y el último Pilar 3, con URL, fecha, HTTP, bytes, SHA-256 y páginas (`INDICE.tsv`). | Hecho. *Interpretación:* el individual de 2016 cubre la misma entidad económica, porque no había filiales. Aceptarlo como sustituto es una **excepción que corresponde a la persona responsable**. Además, el Pilar 3 de 2016–2017 sería individual o del grupo UniCredit (AR17 p. 21 l71-72). |
| C5 · Datos del motor | **Cumple** | Ver §6.3: beneficio y patrimonio atribuibles, SOCE con dividendos, recompras, emisiones, OCI y AT1, y acciones (nota del BPA). | Hecho |
| C6 · Fuera de muestra | **Cumple** (con un límite) | `git grep -il fineco` en `munger-v2` (HEAD): ninguna coincidencia. En `munger-v2-evidencias-mistral`, `origin/coordinacion/cierre-v2` y `origin/mistral/f-alcance-real` solo aparece en documentos de coordinación de U3 (`CANDIDATOS_C.md`, `PROTOCOLO_CONGELADO.md`, `CONTRATO_C_PROPUESTA.md`), como candidata. La candidata `957af65` **no está** en los repositorios locales («Not a valid object name»): para ella me baso en `CANDIDATOS_C.md` §1. | Hecho; la candidata se hereda sin repetir la comprobación |
| C7 · Sin precios | **Cumple** | No usé ningún dato de mercado. La p. 35 del AR (l11-29) contiene cotizaciones: no las cito ni las uso. | Hecho |

**Exclusiones (PROTOCOLO §3):**
- **X1:** ver C3, pendiente de decisión.
- **X2:** no aplica. El patrimonio atribuible es 2 553 324 > 0 (AR p. 287 l125).
- **X3:** no aplica. Beneficio atribuible (AR p. 285 l54) y patrimonio de grupo (AR p. 287 l124-125) se publican por separado.
- **X4:** no aplica. Hay 9 ejercicios consolidados consecutivos.

### 6.2 Riesgos pedidos

| Id | Situación | Evidencia |
|---|---|---|
| **R2 · perímetro** | **Bajo en lo económico, con dos rupturas formales.** 2025 no tiene cambios de perímetro. La filial es de creación propia (26-oct-2017), no hay fusiones ni ventas en lo verificado. Rupturas: 2016 es individual y 2017 consolidado; en lo prudencial, de dentro del grupo UniCredit (2017) a matriz de su propio grupo (2025). 2018–2024 no se ha verificado documento por documento. | AR p. 292 l30-31; AR16 p. 89 l50; AR17 p. 108 l50-52; AR17 p. 21 l71-72; P3 p. 25 l12-13 |
| **R3 · minoritarios** | **Ninguno.** El beneficio neto es igual al atribuible porque Fineco AM es 100 % propiedad del banco. | AR p. 80 l43; AR p. 285 l53-54; AR p. 387 l34-37; P3 CC1 fila 5 |
| **R5 · moneda** | **Euro, sin hiperinflación** | Importes «in € thousand» (AR p. 283 l13). Filial en Irlanda (zona euro). |
| **R6 · grupo mixto** | **No mixto.** Banco más gestora UCITS. Sin aseguradora en el perímetro: las «partner insurance companies» son distribución de terceros (AR p. 237 l27). | AR p. 292 l39; P3 p. 25 l12-13; P3 p. 29 l7-8 |
| R4 · AT1 (informativo) | **Hay AT1 dentro del patrimonio atribuible:** 500 millones, perpetuo, cupón del 7,5 % durante 5,5 años (AR p. 387 l21-24). Se identifica por separado en la partida 140 (AR p. 284 l25). Cupones de 2025, netos de impuestos: 27 187, cargados a reserva extraordinaria (AR p. 386 l48-49). Clasificación contable «Equity» (P3 p. 48 l26). PD-3 se puede aplicar con cualquiera de sus dos opciones. | Hecho |
| R7 · límite del modelo (informativo) | El negocio vive de comisiones y corretaje. Los préstamos a clientes incluyen 23 688,2 millones de valores de deuda a coste amortizado, de un total de 30 066,6 millones (AR p. 531 l11-14). | *Interpretación:* L2 es posible y no es mecánico, igual que en `CANDIDATOS_C.md` §2 |
| R8 · norma o cierre (informativo) | Cierre a 31-12 y NIIF de la UE (AR p. 525 l27-28). No he verificado los ajustes de primera aplicación de NIIF 9 (2018) ni de NIIF 16 (2019). | — |

### 6.3 Contrato C: entradas que la fuente permite documentar

Son hechos de fuente, **no valores fijados**. Las elecciones son PD pendientes.

| Celda (contrato §2) | Dato de fuente 2025 (miles de euros) | Cita |
|---|---|---|
| `Historia!L9`, beneficio neto atribuible | 647 041 | AR p. 285 l54; ESEF |
| `Historia!L21`, patrimonio atribuible al cierre | 2 553 324, AT1 incluido. Sin AT1: 2 053 324 (2 553 324 − 500 000). Elegir entre las dos es PD-3. | AR p. 287 l125; AR p. 284 l25 |
| L9 con la opción PD-3(b) | Restaría los cupones AT1 netos pagados, 27 187 (AR p. 386 l48). Qué cupón se usa, el pagado o el devengado (8,2 millones, AR p. 82 l9), es parte de PD-3. | — |
| Fila 6 «Ventas» (PD-4), solo se identifica | Posibles líneas: margen de intermediación (partida 120) 1 315 205; margen de intereses 631 618; comisiones netas 582 228 | AR p. 285 l27, l16, l19 |
| `Análisis!C55`, acciones | Media 611 352 285; media diluida 612 927 595. Acciones al cierre: 611 575 321, que cuadra con un capital de 201 820 / 0,33 €. Tras la ampliación de 2026: 611 890 603. Qué fecha y qué cifra se usan no se decide aquí. | AR p. 417 l15-16; AR p. 386 l37; AR p. 284 l28; AR p. 281 l20-21 |

**Puente de patrimonio de 2025 (contrato §6), con el SOCE:**

```
E_2024                         2 389 312   (AR p. 287 l125)
− dividendos                    (452 566)  (AR p. 287 l123, l125)
− «changes in reserves»          (35 515)  (cupones AT1 netos, contribución extraordinaria, costes; nota l133-134)
+ emisión de acciones                 962
− compra de acciones propias         (970)
+ pagos en acciones (stock options) 4 924
+ resultado global                647 177  (= 647 041 beneficio + 136 OCI; AR p. 286 l16, l28-30)
= E_2025                       2 553 324   residuo 0
```

- **Interpretación:** «changes in reserves» de 35 515 se reconstruye casi exactamente con las notas: 27 187 de cupones AT1 + 8 382 de reserva negativa por la contribución extraordinaria + 8 de costes − 60 de dividendos no repartidos de la autocartera = 35 517 (AR p. 386 l27-28, l48-53). La diferencia de 2 parece de redondeo; **no la he verificado**.
- **Con nombre:** la reserva negativa de 8 382 es un movimiento con nombre, ni OCI ni reparto, como pide el contrato §6.
- **Excedente limpio:** en 2025 el OCI es pequeño (136) y en 2024 fue de −12 319 (AR p. 286 l28).
- **Reparto frente a beneficio menos ΔB:** los beneficios de 2019 y 2020 se llevaron íntegros a reservas por la recomendación del BCE, y el dividendo de 2021 salió de reservas (AR p. 35 l51-53). Es el caso previsto en `CANDIDATOS_C.md` §2, ahora **con fuente**.

---

## 7. Qué validaría del motor C y qué no

**Validaría** (interpretación sobre los hechos de §4–§6):
- **ROE de la Historia (L9/L21):** sin minoritarios y con perímetro económico estable. Hay serie consolidada desde 2017; 2016 solo en base individual (C4).
- **B0 y PD-3:** el AT1 es identificable, con importe y cupones separados, así que las dos opciones de PD-3 se pueden documentar.
- **Puente de patrimonio:** con las partidas reales (dividendos, cupones AT1 en reservas, autocartera, pagos en acciones, OCI y la reserva negativa con nombre) cuadra con residuo 0 en 2025.
- **Excedente limpio frente al reparto real:** los años 2019–2020 sin dividendo y 2021 con dividendo de reservas separan el «flujo» del motor del reparto observado.
- **PD-4 («Ventas»):** las tres líneas candidatas están identificadas.

**No validaría:**
- **Solvencia y capital regulatorio** (CET1, Tier 1, APR, MREL, colchones, P2R). Quedan **fuera del motor** (contrato §7.1; `Análisis!E62`). Las cifras del Pilar 3 de §5 sirven solo para comprobar la **coherencia documental** entre fuentes y, como mucho, de contexto para una PD-1 sin definir. Ni el motor ni esta verificación juzgan la suficiencia de capital.
- El riesgo de crédito típico de un banco de préstamos: la cartera son sobre todo valores de deuda a coste amortizado.
- El riesgo de tipos (IRRBB) y la sensibilidad del margen de intereses.
- El negocio de comisiones (L2 posible).
- Que el motor sirva para otros bancos.
- La serie de 2018–2024, documento por documento: no descargada.

---

## 8. Series disponibles (C4), por listado oficial y sin descargar

Según `<fuentes>/listados_ir/about_finecobank_en_investors.html` (SHA-256 `9c132f04…2dda`):
- **Informe anual en inglés:** FY11–FY25. FY16 = `…/assemblea/2017/en/2016_reports_accounts.pdf`, FY17 = `…/corporate/reports_accounts_2017.pdf`, FY18 = `…/governance/2019/Reports-and-accounts-2018.pdf`, FY19 y FY20 = `…/investors/Reports-Accounts-20{19,20}.pdf`, FY21–FY24 = `…/accounts-and-reports-20xx.pdf`.
- **ESEF en italiano:** FY21–FY25.
- **Pilar 3 en inglés:** FY14–FY25. FY16 a FY18 llevan el título «Disclosure by Institutions according to Regulation (EU) No. 575/2013».

Solo descargué 2016, 2017 y 2025.

---

## 9. Correcciones a `CANDIDATOS_C.md` §2 (antes [a verificar])

| Afirmación previa | Resultado |
|---|---|
| «informes en inglés» | Matizada: es una traducción **no oficial**. La oficial es italiana (ESEF). Afecta a C3. |
| «perímetro estrecho (la filial irlandesa)» | Confirmada para 2025 (AR p. 292). Pero la serie consolidada **empieza en 2017**: afecta a C4. |
| «sin minoritarios» | Confirmada (R3) |
| «AT1 dentro del patrimonio» | Confirmada: 500 millones, partida 140 |
| «restricciones al dividendo en 2020» | Confirmada y ampliada: los beneficios de 2019 y 2020 fueron íntegros a reservas (AR p. 35 l51-53) |
| «NIIF 9 (2018)» | Sin verificar |
| «salida de UniCredit (2019)» | Sin verificar la fecha. Lo verificado es que en 2017 estaba dentro del grupo UniCredit (AR16 p. 3; AR17 p. 21) y que en 2025 es la matriz de su propio grupo (P3 p. 3, p. 25). |

---

## 10. Conclusión

**No encaja tal como está escrito el protocolo.** No he forzado el caso.

- **C4 no se cumple literalmente.** Hay 9 informes anuales consolidados en la ventana 2016–2025, no 10. El de 2016 es individual porque no había filiales.
- **C3 es dudoso.** El informe en inglés es una traducción declarada «non-official». Solo la italiana es fehaciente, y el ESEF solo existe en italiano.
- **El resto encaja:**
  - C1, C2, C5, C6 y C7;
  - R3 (sin minoritarios), R5 (euro) y R6 (no mixto);
  - R2, bajo en lo económico;
  - el mismo perímetro contable y prudencial en 2025;
  - cifras comunes del informe anual y del Pilar 3 que coinciden, salvo redondeos de 1–2 mil.
- **Salida posible, que no me corresponde:** si la persona responsable acepta (a) la traducción publicada por la entidad como fuente en inglés y (b) el informe individual de 2016 como sustituto del consolidado, FinecoBank encajaría. Ver la tabla de §6.1.

*Sin valoración, sin palancas y sin precios. Ningún número de este documento es una estimación de la entidad: todos son cifras de sus fuentes publicadas, o cálculos aritméticos marcados como míos.*
