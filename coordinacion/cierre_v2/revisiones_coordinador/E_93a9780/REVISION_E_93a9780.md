# Revisión independiente de E-ELIS @ 93a9780

**Objeto.** Entrega E-ELIS de Mistral (antigua B, nueva E). Repositorio auxiliar `munger-v2-evidencias-mistral`, rama `origin/mistral/e-fuentes-elis`, commit `93a97801f8c4f6a4dc5cabd4540248390cf113d0`. Bloques `b4a4703` (inventario), `78d2898` (búsqueda y lectura) y `93a9780` (cierre) sobre la base `ec707a5`. Carpeta `resultados_cierre/elis_fuentes/`.

**Revisor.** Subagente de revisión de Claude (Opus), a petición del coordinador. Es un contexto distinto del autor: el autor es Vibe Code de Mistral, `mistral-large-4-0`, firmado como «Vibe Nuage Agent». Responde a la `solicitud_revision` de E-ELIS en `CONTROL.json` (`origin/coordinacion/cierre-v2` @ `9454b44`), cuyo estado es `EN_CURSO` y cuyo `sha_autor` es `93a9780`.

**Fecha.** 2026-11-16.

**Cómo se hizo.**
- Sin red, sin checkout, sin worktree.
- Ningún repositorio modificado: `git status` está limpio en el auxiliar y en el producto.
- La entrega se extrajo con `git archive 93a9780 resultados_cierre/elis_fuentes | tar -x` en `<rev_E>/entrega`.
- Los PDF son los de `<base414>`, con la huella comprobada.
- Texto con `pdftotext -layout` y, como segundo extractor, `pdftotext` en orden de lectura.
- Las sondas están en `<rev_E>/sondas/`. Se ejecutan todas con `s00_ejecutar_todo.sh`. Todas terminan con exit 0.

Rutas: `<base414>` es el árbol materializado de la base 4.14 (`munger_v2_r1`). `<rev_E>` es la carpeta de esta revisión.

---

## 0. Veredicto por criterio

| # | Criterio | Veredicto |
|---|---|---|
| 1 | ENTREGA.json | **CUMPLE CON LÍMITES** |
| 2 | Preservación de los 11 PDF | Registro: **CUMPLE**. Copia duradera: **NO CUMPLE** (lo declara el propio autor). Contenido: **NO OBSERVABLE AQUÍ** |
| 3 | 28 citas | 7 del URD 2025: **CUMPLE**, verificadas en su página. 21: **NO OBSERVABLE AQUÍ**. Dos registros (20 y 21) tienen defectos de forma |
| 4 | M1/M2/M6/N2 | M1: **CUMPLE CON LÍMITES**. M2: **CUMPLE**. M6: **CUMPLE CON LÍMITES** (etiqueta sobredimensionada; un contraejemplo). N2: **NO CUMPLE** en la parte de caja (afirmación contradicha por la propia nota 4.6 y por el EFE) |
| 5 | Conservación | **CUMPLE** |
| 6 | Higiene | **CUMPLE CON LÍMITES**: manifiesto y diff limpios; scripts con defectos de reproducibilidad |

Clasificación global (INTEGRACION.md, «Recepción y revisión» 5): **correcciones materiales en N2 y M6; conforme con límites en lo demás.** La entrega no desbloquea R, θ ni λ, y Elis sigue `pendiente_de_datos`. Esta revisión limitada no acredita aptitud económica.

---

## 1. ENTREGA.json — CUMPLE CON LÍMITES

Evidencia: sonda `s04_entrega_y_preservacion`, comparada con `PLANTILLA_ENTREGA.json` de `origin/coordinacion/cierre-v2`.

**Campos.** Los 24 de la plantilla están presentes; no hay campos de más ni nulos indebidos. Cada prueba tiene las 9 claves de la plantilla. `es_plantilla` vale false.

**Pruebas declaradas.** Son tres, con comando y exit esperado/observado 0/0, y las tres marcadas `EJECUTADO_OK`:
- `inventario_bloque1.py`;
- `descargar_fuentes_elis.py`;
- `lectura_bloque2.py`.

Su ejecución **no es observable aquí**, por estas razones:
- Las tres dependen de `.trabajo/`, que está excluido de Git: allí están `base414.zip`, `elis_fuentes/pdf/`, `texto/` e `INDICE_DESCARGAS.csv`.
- `descargar` necesita red.
- `inventario_bloque1.py` hace `git show 716cbd6…` dentro del repositorio auxiliar, y ese objeto **no existe** en el auxiliar local; sí existe en el producto (s06). Tal como está escrito, no reproduce en un clon limpio del auxiliar.

Lo que sí se observa es coherente con que se ejecutaron:
- Las 28 entradas `CITAS` del script, leídas con `ast.literal_eval` sin ejecutarlo, coinciden en pregunta, documento y página con las 28 citas del JSONL.
- El JSONL tiene 40 registros, como declara la entrega.
- Las 7 citas observables se encuentran en su página.
- Rehecha aparte la comprobación cruzada del bloque 1, `fuentes.json@716cbd6` frente a `seleccion_fuentes.json@f5775dc`, coinciden las 6 huellas, y las 6 figuran en `FUENTES_Y_BUSQUEDA.csv`.

**Límites honestos: sí, en general, con estas excepciones:**
- **Línea de N2 en `limites_y_bloqueos`.** Dice «+25,7 … (nota 4.6, concepto monetario)». Es falso; véase §4 (N2).
- **Prueba de descarga.** Su exit 0 no codifica «12/12 HTTP 200»: el script termina con 0 aunque fallen descargas, porque solo imprime el recuento. Su evidencia (`.trabajo/elis_fuentes/INDICE_DESCARGAS.csv`) no está publicada.
- **Textos desfasados:**
  - `cambios_respecto_entrega_anterior` dice «Bloque 2 (este commit)» en el commit del bloque 3.
  - `README.md` mantiene «Bloque 2 (pendiente)» y «Bloque 3 (pendiente)».
  - `RESUMEN_PARA_INTEGRADOR.md` y `HALLAZGOS_ELIS.md` se titulan «bloque 2».
  - `PUNTO_DE_RECUPERACION.md` dice «Bloque 2 cerrado (este commit)» y, más abajo, «Bloque 3 cerrado en este commit». Cita además el control en `ff0c60cd` y en `2fea890`. El `2fea890` existe (21:34:49Z) y no asigna nada nuevo a E, así que lo declarado es cierto.

**Nada declarado como ejecutado sin serlo:** NO OBSERVABLE AQUÍ en sentido estricto. No hay indicios de lo contrario. `precondiciones_simuladas` está vacío.

**Sin autoaprobación: CUMPLE.**
- `revision_por_otro_contexto` vale null.
- `integrado_en_producto` vale false.
- La única mención es «no se abren ciclos recursivos ni se autoaprueba».
- Los criterios pendientes incluyen la revisión por Claude.

**`apto_dinero_real`: CUMPLE.** Vale exactamente «No se declara por este formulario», igual que la plantilla.

**Huellas en ENTREGA.json.** Solo figura la del URD 2025 (`04bfd087…`). Las de los 11 PDF se remiten a `FUENTES_Y_BUSQUEDA.csv`, que sí las tiene, y a `INDICE_DESCARGAS.csv`, que no está publicado. La plantilla no lo exige, pero la referencia a un archivo no publicado debe retirarse o sustituirse.

---

## 2. Preservación de los 11 PDF — registro CUMPLE; preservación duradera NO CUMPLE; contenido NO OBSERVABLE AQUÍ

Lo que declara la entrega: los bytes están en `.trabajo/elis_fuentes/pdf/<id>.pdf`, en el sandbox del autor, fuera de Git (`.gitignore` contiene `.trabajo/`). La subida a la Release falló con HTTP 401 y no se reintenta. Estado `DESCARGADO_PROVISIONAL`. El propio autor dice que «URL+SHA no equivalen a documento preservado duraderamente».

Lo comprobado (s04, s05):
- **Ninguna copia en esta máquina.** Se recorrieron `/home`, `/tmp`, `/root`, `/srv`, `/opt`, `/var` y `/mnt` buscando por tamaño exacto y SHA-256: 0 coincidencias para cada uno de los 11. Del URD 2025 hay 12 copias locales con la huella declarada.
- **Ninguna copia en Git.** El árbol `93a9780` no contiene `.trabajo/` ni `INDICE_DESCARGAS.*`. La única Release usable sigue siendo base-4.14, que no contiene estos 11; ninguna de las huellas de la base coincide.
- **No hay copia duradera accesible** para otra sesión ni para el usuario. `CONTROL.json` registra lo mismo como bloqueo.
- **Registro coherente y completo** entre `FUENTES_Y_BUSQUEDA.csv` y `LECTURA_FUENTES.jsonl`. Para los 12 documentos coinciden SHA-256, bytes, páginas y URL final. Cada cita lleva el `sha256_doc` de su documento y una página dentro del rango. ENTREGA.json no lista las 11 huellas: remite al CSV.
- **Falta en el registro, frente a lo que pide el encargo:**
  - versión;
  - fecha de descarga por documento (solo hay una global, 2026-11-16, en ENTREGA.json);
  - content-type, que solo está en el índice no publicado.
- **Contenido de los 11: NO OBSERVABLE AQUÍ.** No se supone nada sobre él.

| id | bytes | págs | SHA-256 | Bytes en | Copia duradera | CSV = JSONL | En ENTREGA.json | Citas |
|---|---|---|---|---|---|---|---|---|
| fy2025_presentacion_en | 13742386 | 53 | b3642606567cb4d9082e007843670e1fab6d46fab4dd466badfda92648c06786 | sandbox autor | No | sí | no | 4 |
| fy2025_comunicado_en | 493029 | 16 | e9dcd1bc48ae775d74753abbb8efca90443b7e63ea20a362b3d67e3b4dcf0810 | sandbox autor | No | sí | no | 5 |
| cgmbrochure2026 | 1389987 | 132 | dcd8949267b4e5580e3fe80aa59d9c5e6061271223777da3f5600a26b374cdc3 | sandbox autor | No | sí | no | 5 |
| factsheet2026 | 643129 | 2 | ef17a28f4b95abcce862184e7a8419b3c2eb92ad1a9f9b6b4b5979adad3898d7 | sandbox autor | No | sí | no | 1 |
| fy2024_presentacion_en | 5522280 | 54 | d733b56d6fd25e538d945da6434a0c90a4579fd291550558d2ff786cb2ec4e7d | sandbox autor | No | sí | no | 1 |
| fy2024_comunicado_en | 360913 | 15 | 87684906caf1f3253112b6031dcba7eb07ed6b2616dd7c0f70a01b9ebac95324 | sandbox autor | No | sí | no | 1 |
| fy2024_revenue_en | 175461 | 5 | 07a29d70aa53f09e898455c4550c9f14d12b2562768fdffff2947a71c25ab999 | sandbox autor | No | sí | no | 0 |
| q1_2025_revenue | 144522 | 4 | 2cdc713aa63a658aef107907114e35417b5bc9cccb57915d607624d3cad22b6f | sandbox autor | No | sí | no | 1 |
| h1_2025_comunicado_fr | 413358 | 13 | 1347fc21135ebd6ad5705853f87e489ceee68e864c172b0e2aec4a1a702c9779 | sandbox autor | No | sí | no | 0 |
| q3_2026_revenue | 229631 | 5 | 24271931bf7da33a0ed63f711495448ab440e33ae9618e6febda424bff30045c | sandbox autor | No | sí | no | 2 |
| h1_2026_comunicado_en | 498753 | 13 | 5a84458c26fc5b060f5e45e631139436d3a65592e7b676cc29b68ecc44579cb4 | sandbox autor | No | sí | no | 1 |

En las columnas: «sandbox autor» significa `.trabajo/elis_fuentes/pdf/` según lo declarado; «Copia duradera» incluye la búsqueda local, con 0 coincidencias; «CSV = JSONL» se refiere a SHA, bytes, páginas y URL.

Total: 21 citas en 9 documentos. `fy2024_revenue_en` y `h1_2025_comunicado_fr` se descargaron pero no se citan.

**Qué falta para preservarlos:**
1. Llevar los bytes de los 11 a un almacén duradero autorizado y accesible al coordinador y al usuario. La decisión es del coordinador o del usuario; el autor no debe reintentar ni pedir tokens.
2. Verificar allí SHA-256, bytes y páginas contra la tabla.
3. Publicar en Git, como texto, el índice de descarga: url_solicitada, url_final, http, content_type, fecha de descarga por archivo y versión.
4. Opcionalmente, extractos de texto acotados de las páginas citadas, para que las 21 citas sean revisables sin los PDF.

Mientras no se haga, las 21 citas solo se sostienen por URL+huella.

---

## 3. Citas — 7/7 observables verificadas; 21 NO OBSERVABLES

Antes de nada se confirmó la huella del URD 2025 local: `04bfd08724e768804e7110093d3ec2cf017a7e7fe2983bacd75656d3a95cd62e`, 18.963.024 bytes, 468 páginas. Es igual a la declarada.

| # | Preg. | Doc. | Pág. | Resultado |
|---|---|---|---|---|
| 6 | M1 | urd2025 | 137 | VERIFICADA. En orden de lectura; en `-layout` la frase queda partida por las dos columnas |
| 7 | M1 | urd2025 | 215 | VERIFICADA (fila «Capex 1,160.0 86.0% 842.0 72.6%») |
| 10 | M2 | urd2025 | 141 | VERIFICADA (orden de lectura) |
| 16 | M6 | urd2025 | 313 | VERIFICADA (orden de lectura) |
| 24 | N2 | urd2025 | 350 | VERIFICADA («Net gain (loss) related to retirement of fixed assets 25.7 (1.5)») |
| 25 | N2 | urd2025 | 350 | VERIFICADA («OTHER OPERATING INCOME AND EXPENSES (3.1) (18.5)»; la misma fila aparece también en p.309) |
| 26 | N2 | urd2025 | 309 | VERIFICADA |

Las 21 restantes son de los 11 documentos ausentes y quedan **NO OBSERVABLES**: 1–5, 8, 9, 11–15, 17–23, 27 y 28.

**Corroboración indirecta en otros documentos locales** (s03, s03b). No verifica la cita en su documento declarado; solo indica que el mismo texto o cifra existe en otro documento conservado:
- Cita 1 («covers investments for both growth … and maintenance») y cita 13 («initial outlay required to set up a new customer», del brochure CGM p.15): el mismo texto está en el **URD 2025 p.312** y en los URD 2019–2023.
- Cita 2 (capex bruto 823,9/887,4/890,2, del brochure p.15): la frase completa está en el **URD 2025 p.312**.
- Cita 8 («capex contained despite … Climate plan», del brochure p.60): está en el **URD 2025 p.122**. El informe F1 §6.2 ya la citaba de ahí.
- Citas 4 y 22 (874,7 y 117,6, de la presentación FY2025 p.29): están en el **URD 2025 p.314** y en p.311/327.
- Cita 5 (19,5 % en H1 2026, del comunicado H1 2026 EN p.6): frase idéntica en el informe semestral 2026 EN de la base, p.10.
- Cita 17 (definición del orgánico, del comunicado FY2025 EN p.11): está en el URD 2025 p.313 y en anteriores.
- Equivalentes en francés del comunicado anual 2025 FR de la base (huella `03190142…`):
  - 18,2 %/19,2 % (cita 3), en p.6;
  - «indemnités d'assurance» (cita 27), en p.5;
  - sobre 50–150 M€ (cita 19), en p.7;
  - 874,7 y 117,6, en p.6.

Consecuencia: buena parte de lo presentado como «nuevo» en M1 y M6 ya estaba en el URD 2025 de la base 4.14.

**Defectos en el registro de citas** (s06):
- **Cita 20** (q1_2025_revenue p.1). Su patrón usa `.*` codicioso: `Carsan in Spain, Ernst in .* with annual combined revenue of c\. 55 million euros in 2024`. La cita registrada está truncada a 400 caracteres y **no contiene el final que el patrón exigía**. Lo que muestra es «their combined revenue was c. 55 million euros in 2024 o Q1 2025 external growth…», es decir, un tramo largo de página, no una frase verificada. El contenido no es observable aquí.
- **Cita 21** (q3_2026_revenue p.1). Su patrón es una alternativa: `RS10 in Spain|acquisitions contributed 1\.5 percentage points`. Solo se verificó «acquisitions contributed 1.5 percentage points». El `hallazgo` afirma además «RS10 … consolidada desde 1-jun-2026; Muller +0,5 pp; pipeline “remains strong”», y nada de eso queda cubierto por la cita registrada.
- Falso positivo descartado: la sonda señaló que la cita 16 no casa con su propio patrón. Es un artefacto de normalizar los espacios (el patrón exige un carácter más un `\s+` tras «5.0»). La cita está verificada en la página.

---

## 4. M1, M2, M6 y N2

### M1 — estado ABIERTO: se sostiene. CUMPLE CON LÍMITES

- **No inventa un reparto entre mantenimiento y crecimiento.** Lo declara no localizado y conserva los límites («proporción de ventas ≠ proporción de capex»; «dos tercios» no se extrapola). CUMPLE.
- **Las cifras coinciden con el URD 2025 local** (s02):
  - capex bruto 823,9/887,4/890,2 en **p.312**;
  - identidad: 26,2 + 864,0 = 890,2 (p.311/327);
  - net capex 874,7 (2024: 876,0) en **p.311**;
  - identidad: 890,2 − 15,3 (cobros por bajas de PP&E) − 0,2 (subvenciones) = 874,7;
  - 18,2 %/19,2 % en p.311;
  - taxonomía 1.160,0 / 86,0 % / 842,0 / 72,6 % en **p.215**.
- **Defecto: lo presentado como nuevo no es nuevo.** «Nivel publicado (nuevo ancla)» y «Nuevos datos de nivel» se refieren a cifras que ya están en el URD 2025 de la base, p.311–312. El informe F1 §6.1 ya citaba p.311–312. El brochure CGM repite ese texto. Es corroboración, no evidencia nueva.
- **Defecto: cruce de perímetro latente en la taxonomía.**
  - El CapEx de taxonomía 1.160,0 incluye derechos de uso (IFRS 16: 183,9) y altas por combinaciones (62,7), además de IAS 38 (26,2) e IAS 16 (887,1); la suma es 1.159,9 (URD 2025 **p.217**).
  - No es el mismo perímetro que el capex propio de 890,2. La entrega lo pone en la misma lista de «nuevos datos de nivel» sin advertirlo.
  - El 842,0 alineado es casi todo economía circular (70,7 de los 72,6 puntos). El alineado con mitigación climática es el 1,9 %, unos 22 (ilustrativo).
  - Aun así, LECTURA (cita 7) registra como `salida_afecta`: «importe de capex alineado con clima/economía circular publicado (842,0 M EUR)», bajo M1, cuya pregunta incluye el plan climático. El 842,0 no es el importe del plan climático. La entrega no lo afirma expresamente, pero la etiqueta invita a ese cruce.
  - Corrección: decir que es otro perímetro (con ROU y combinaciones) y otro objetivo (economía circular), y que no sirve para M1.

### M2 — estado ABIERTO: se sostiene. CUMPLE

- URD 2025 p.141 verificada: «attrition rates are monitored», sin cifra.
- Las demás citas son no observables y cualitativas.
- «initial outlay» también está en el URD 2025 p.312, no solo en el brochure.
- No infiere ninguna tasa.

### M6 — «PERÍMETRO ACLARADO, finalidad ABIERTA»: CUMPLE CON LÍMITES, con una corrección material

- **El texto de p.313 sostiene la conclusión.** El orgánico «is calculated excluding (i) the impacts of changes in the scope of consolidation of “major acquisitions” and “major disposals” … (ii) exchange rate». Las «major» son las de más de 5,0 M€ de ingresos anuales en Francia y más de 3,0 M€ en otros países. Por definición, el efecto de las compras por debajo del umbral queda dentro del orgánico.
- **Pero no aclara nada nuevo.** El informe F1 (§6.3, corrección V1) ya establecía exactamente eso con URD 2025 p.313, DEU 2024 p.259 y URD 2023 p.267. La pregunta M6 del encargo lo daba como premisa. Por tanto:
  - «Definición publicada (nueva, precisa)» es inexacto;
  - el umbral **no «confirma»** el 31,5 M€/año de compras pequeñas, que procede de otra lectura (flujos de adquisiciones, URD 2025 p.341–342; DEU 2024 p.288).
  - El estado correcto es: **M6 ABIERTO**; la definición del perímetro ya era conocida (F1 V1); finalidad no localizada.
- **Contraejemplo (cruce de perímetro).**
  - LECTURA (cita 20, `no_demuestra`) presenta Carsan, Ernst y Bodensee como «ejemplo de compras pequenas dentro del perimetro organico/externo publicado».
  - El URD 2025 **p.312** dice: «six major acquisitions … in 2025, including the laundries Wäscherei Bodensee in Switzerland, Bugaderia Neutral in Spain, Larosé and Adrett in Germany».
  - En **p.341**, Wäscherei Bodensee tiene columna propia, fuera de «Other acquisitions».
  - **Bodensee es una adquisición importante y queda fuera del orgánico.** La propia cita declara que contribuyen al crecimiento externo (+2,1 %).
- **Contraejemplo (cifras de distinto perímetro bajo el mismo epígrafe).**
  - RESUMEN y PUNTO DE RECUPERACIÓN ponen bajo «M6 — perímetro aclarado» la caja de M&A de 2025, 117,6, y el sobre de bolt-on de 50–150.
  - El 117,6 (p.327/341) es el total: adquisiciones importantes, earnouts (Lavartex 19,7) y otras.
  - Las compras pequeñas de 2025 son la columna «Other acquisitions», 37,3 (p.341), que es el valor que usa F1.
  - LECTURA rotula bien el 117,6 («Importe total de M&A»), pero el resumen lo mezcla con el perímetro de las compras pequeñas.
- **«No publicada».** ENTREGA.json, RESUMEN y PUNTO DE RECUPERACIÓN dicen que la finalidad «no está publicada» o «no publicada», sin la salvedad «en esta búsqueda». Véase el apartado de redacción, más abajo.

### N2 — «PARCIAL»: NO CUMPLE en la caja; CUMPLE en no igualar el +25,7 con el seguro

- **No iguala magnitudes parecidas: CUMPLE.** Repite que ninguna línea dice que el +25,7 sea la indemnización del seguro.
- **La cita está bien:** nota 4.6, **p.350**, «Net gain (loss) related to retirement of fixed assets 25.7 (1.5)» (s01, s02). OOIE 2025 = −3,1 (−18,5).
- **Defecto material: la afirmación de caja es falsa.** HALLAZGOS, LECTURA (cita 24), RESUMEN y `limites_y_bloqueos` de ENTREGA.json afirman que el +25,7 es «concepto monetario (el detalle separa los de impacto no monetario 0,3)» y que dejó una ganancia neta «en la sección operativa (flujo de caja operativo), no en financiación/inversión». Lo contradicen:
  1. **La propia nota 4.6 (p.350).** El desglose «of which» separa:
     - monetary items: −28,2;
     - deterioros: −0,1;
     - provisiones: −0,6;
     - **net gain (loss) on disposal of non-current assets: +25,7**;
     - earnouts: −0,2;
     - otros sin impacto en caja: +0,3.

     La suma es −3,1, que es el total de OOIE. El +25,7 **no** está en «monetary items»; es una fila propia. El 0,3 es solo una de las filas no monetarias.
  2. **El estado de flujos de efectivo (p.327).** «Net gains and losses on disposal of property, plant and equipment and intangible assets (23.1)» se **resta** del flujo operativo como partida sin caja. Los cobros por bajas, «Proceeds from disposal of property, plant and equipment 15.3», están en **inversión**. Ya restan en el net capex: 890,2 − 15,3 − 0,2 = 874,7.
  3. **La nota 4.4 (p.349).** «Change in receivables on disposal of fixed assets 16.9» en 2025: al cierre había una cuenta a cobrar nacida de bajas de inmovilizado.

     No se infiere que sea el seguro; solo que no todo se cobró en 2025.

  Contraejemplo, en una frase: si el +25,7 fuera caja operativa, el EFE no lo restaría del flujo operativo (−23,1) ni habría cobros por bajas en inversión (15,3).
- **Mezcla de dos medidas.** El informe F1 (l.328–330) usa +23,1 (la plusvalía neta del EFE, que abarca todas las bajas de PP&E e intangibles) para f, y +25,7 (la fila de OOIE) para m0. La entrega no distingue estas dos medidas de perímetro distinto.
- **Estado correcto:**
  - **N2 ABIERTO** en dónde se cobró, fiscalidad y reposición;
  - publicado: la fila de OOIE (+25,7, nota 4.6) y la narrativa de seguros (p.309; comunicado FR p.5 como equivalente local);
  - el EFE y la nota 4.4 indican que la plusvalía es contable y que el cobro, cuando lo hubo, fue de inversión, en parte pendiente al cierre;
  - el vínculo con el seguro sigue sin acreditarse.

### Redacción «no publicado» frente a «no localizado en esta búsqueda»

- Nunca escribe «no publicado en ninguna parte»; la única aparición es «nunca “no publicado en ninguna parte”».
- «No localizado en esta búsqueda» aparece 3 veces en HALLAZGOS, 4 en PREGUNTAS y 4 en PUNTO DE RECUPERACIÓN.
- Quedan afirmaciones absolutas sin esa salvedad:
  - ENTREGA.json (M6: «finalidad reposicion/crecimiento no publicada»);
  - RESUMEN («Sigue sin publicarse el reparto…»; «La finalidad … no está publicada»);
  - PUNTO DE RECUPERACIÓN («**no publicada**»);
  - PREGUNTAS M6 («no publicada; no localizado…»);
  - LECTURA cita 3 («Sigue sin publicar el desglose»).
- Veredicto: **CUMPLE CON LÍMITES.** Hay que unificar en «no localizado en esta búsqueda».

---

## 5. Conservación — CUMPLE

- Elis sigue `pendiente_de_datos`: lo dicen todos los documentos y el diff no toca el producto.
- No se elige R (tampoco dentro de 736,0–867,2), θ, λ, k, probabilidades ni umbrales. Los únicos umbrales citados son los publicados por Elis (5,0/3,0 M€) y no se adoptan como política.
- C48 = 108, C49 = 128,1, FCF base = 307,933 y E1/D3/E2/E6 solo se mencionan para declararlos conservados. El diff se limita a `resultados_cierre/elis_fuentes/` (s05).
- **B/P-M1 intacta:**
  - `origin/mistral/m2-fundamento-pm1` = `daa74783d2708fcd46ca7c24ae1ffbb327c35784`;
  - ningún archivo `resultados_m2/` en el diff;
  - `resultados_m2` es idéntico entre `ec707a5` y `93a9780`.

---

## 6. Higiene — CUMPLE CON LÍMITES

- **Manifiesto.** `sha256sum -c MANIFIESTO_SHA256.txt` en su carpeta: 11/11 OK, exit 0. No hay archivos de la carpeta fuera del manifiesto, salvo el propio manifiesto.
- **`git diff --name-only ec707a5 93a9780`.** Contiene 12 archivos de texto, todos en la carpeta. Ningún PDF, XLSX, ZIP, caché ni `.trabajo/`; ningún binario (numstat) y ningún patrón de secreto. El archivo mayor es LECTURA_FUENTES.jsonl, de 26.026 bytes. `.gitignore` excluye `.trabajo/`, `__pycache__/` y `*.pyc`.
- **Scripts, revisados por lectura sin ejecutarlos.** Ninguno es malicioso; no envían datos ni usan credenciales. Defectos:
  1. **`lectura_bloque2.py` no es idempotente.** Relee y reescribe `FUENTES_Y_BUSQUEDA.csv` añadiendo las 12 filas cada vez. En `PREGUNTAS_Y_RESULTADOS.csv`, `campos += [...]` duplica columnas en una segunda ejecución. Solo reproduce si antes se ejecuta `inventario_bloque1.py`, y eso no se declara.
  2. **`inventario_bloque1.py` depende de un objeto ausente.** Hace `git show 716cbd6` en el auxiliar, donde ese objeto no existe en un clon normal, y necesita `.trabajo/base414.zip`.
  3. **`descargar_fuentes_elis.py`:**
     - no crea `.trabajo/elis_fuentes/pdf/` ni `texto/`, así que falla en un entorno limpio;
     - termina con exit 0 aunque fallen descargas;
     - compone `https://` por partes (`"ht" + "tps" + "://"`). Es inocuo, pero no aporta nada y dificulta la lectura.
  4. **Patrones de cita.** La tabla `CITAS` usa `.*` codicioso con `re.DOTALL` y trunca la cita a 400 caracteres (cita 20), y admite alternativas (cita 21). El registro deja de ser una cita literal de lo verificado.
  5. **El encargo pedía confirmar las ambigüedades con un segundo extractor o con representación visual.** ENTREGA.json lo deja como «pendiente si procede». La lectura de la fila «of which» de la nota 4.6 era precisamente una de esas ambigüedades.

---

## 7. Defectos y correcciones pedidas (para devolver al autor)

| # | Severidad | Defecto | Corrección |
|---|---|---|---|
| E-R1 | **Material** | N2: «+25,7 concepto monetario … flujo de caja operativo» es falso según la nota 4.6 p.350, el EFE p.327 y la nota 4.4 p.349 | Retirarlo de HALLAZGOS, LECTURA cita 24, RESUMEN, PUNTO DE RECUPERACIÓN, PREGUNTAS y `limites_y_bloqueos`. Estado N2 = ABIERTO (caja, fiscalidad y reposición); registrar la fila «of which net gain on disposal», el −23,1 del EFE, el 15,3 en inversión y el 16,9 a cobrar, sin igualar nada con el seguro |
| E-R2 | **Material** | M6: Bodensee y otros presentados como «compras pequeñas», cuando el URD p.312 y p.341 dicen que Bodensee es «major» | Corregir la cita 20 y el RESUMEN. Separar 117,6 (total de M&A) de 37,3 (otras adquisiciones de 2025) |
| E-R3 | Media | M6: «perímetro aclarado» y «definición nueva» presentan como avance lo que F1 V1 ya tenía con la misma página; el umbral no «confirma» el 31,5 | Estado M6 = ABIERTO; definición del perímetro ya conocida (F1 V1); finalidad no localizada en esta búsqueda |
| E-R4 | Media | M1: cifras presentadas como «nuevo ancla» que ya están en el URD 2025 p.311–312; taxonomía 1.160,0/842,0 junto al capex propio sin advertir el perímetro (ROU + combinaciones; economía circular) | Rotularlas como corroboración del URD 2025. Añadir el perímetro de la taxonomía (p.217) y que no mide el plan climático |
| E-R5 | Media | Registros de las citas 20 (tramo truncado) y 21 (alternativa; el hallazgo cubre más que la cita) | Patrones no codiciosos y sin alternativas; una cita por afirmación; no truncar |
| E-R6 | Media | 11 PDF sin copia duradera; el índice de descarga no está publicado | Ver §2, «Qué falta» |
| E-R7 | Menor | Redacción «no publicada» / «sigue sin publicarse» sin la salvedad | Unificar en «no localizado en esta búsqueda» |
| E-R8 | Menor | Textos desfasados (README, títulos «bloque 2», «este commit», control ff0c60cd/2fea890) | Actualizar al cierre del bloque 3 |
| E-R9 | Menor | Reproducibilidad de los scripts: idempotencia, mkdir, exit code, dependencia de 716cbd6 | Ver §6 |

---

## 8. Sondas

En `<rev_E>/sondas/`:
- `comun.py`;
- `s00_ejecutar_todo.sh` (ejecutor);
- `s01_citas_urd2025.py` (las 7 citas observables);
- `s02_cifras_urd2025.py` (22 comprobaciones de cifras e identidades, con Decimal);
- `s03_corroboracion_local.py` y `s03b_equivalentes_fr.py`;
- `s04_entrega_y_preservacion.py`;
- `s05_higiene.sh`;
- `s06_scripts_y_texto.py`.

Cada una tiene su `.out` y, si procede, su `.json`; todas terminan con exit 0. Las rutas absolutas de las salidas están normalizadas a `<base414>`, `<rev_E>`, `<aux>` y `<prod>`.

Comando: `bash s00_ejecutar_todo.sh <base414> <rev_E> <repositorio auxiliar> <repositorio producto>`.
