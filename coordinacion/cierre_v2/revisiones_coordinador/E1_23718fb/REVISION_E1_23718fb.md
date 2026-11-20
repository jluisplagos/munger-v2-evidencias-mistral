# Revisión independiente de la respuesta de E-ELIS a la corrección E1 · `23718fb` (+ relevo `f00c5dd`)

**Objeto.** Respuesta de Mistral E a `CORRECCION_E1.md`. Repositorio auxiliar `munger-v2-evidencias-mistral`, rama `origin/mistral/e-fuentes-elis`:
- `23718fb3e842d52711705f70052244eec6a4fb5c`: respuesta E-R1…E-R9;
- `f00c5dd64cb956b93ebb199389ce748e9d218f6c`: checkpoint de relevo;
- base `93a97801f8c4f6a4dc5cabd4540248390cf113d0`.

La carpeta es `resultados_cierre/elis_fuentes/`. Solo se revisan E-R1…E-R9 y la conservación. Las referencias son `CORRECCION_E1.md`, `REVISION_E_93a9780.md` y `adenda_20261117/ADENDA.md`, leídas con `git show origin/coordinacion/cierre-v2:…`.

**Revisor.** Subagente de revisión de Claude (Opus), a petición del coordinador. Es un contexto distinto del autor, que es Vibe Code de Mistral, `mistral-large-4-0`, firmado como «Vibe Nuage Agent».

**Fecha.** 2026-11-17.

**Cómo se hizo.**
- Ningún repositorio se ha modificado: no hay commit, push, checkout ni worktree.
- La entrega se extrajo con `git archive f00c5dd resultados_cierre/elis_fuentes | tar -x` en `<rev_E1>/entrega`. Para comprobar el manifiesto de `23718fb` se extrajo además ese árbol en una carpeta temporal.
- Los 11 PDF son los de `<pdf>`. Su `sha256sum -c` contra `SHA256SUMS` de `origin/coordinacion/release-fuentes-elis` da 11/11 OK.
- El URD 2025 es el de `<base414>`: `04bfd08724e768804e7110093d3ec2cf017a7e7fe2983bacd75656d3a95cd62e`, 18.963.024 bytes.
- Texto con `pdftotext` página a página, en orden de lectura y con `-layout`.
- Los scripts del autor se reprodujeron **sin red** en copias desechables (`<rev_E1>/repro`, borrada al terminar). La red se sustituye por un `urlopen` local que sirve los PDF locales. Se usó un entorno virtual con PyMuPDF 2.1 y pypdf 7.1.0 (`pip install pymupdf pypdf==7.1.0`).
- Python siempre con `-I`.
- Las sondas están en `<rev_E1>/sondas/` y se ejecutan con `s00_ejecutar_todo.sh`; las seis terminan con exit 0.

---

## 0. Veredicto por E-R

| E-R | Veredicto | En una línea |
|---|---|---|
| **E-R1** N2 | **CERRADO** | Afirmación retirada en todos los textos; N2 ABIERTO con p.327, p.349 y p.350; +23,1 y +25,7 separados |
| **E-R2** M6 | **ABIERTO** (corrección acotada) | Bodensee: bien, con p.306, p.312 y p.341; 117,6 y 37,3: separados. Pero **Lavartex** se clasifica como importante de 2025 y se omite **Acquaflash**; Carsan y Ernst siguen sin clasificar |
| **E-R3** M6 | **CERRADO** | M6 ABIERTO; perímetro como corroboración de F1 V1 (`716cbd6` l.550, comprobada) |
| **E-R4** M1 | **CERRADO CON LÍMITES** | Corroboración y perímetro de p.217 (183,9 y 62,7); no se presenta como plan climático. Quedan rótulos «nuevo/ancla nueva» para cifras que ya están en la base |
| **E-R5** citas | **CERRADO CON LÍMITES** | Citas 20 y 21 corregidas; sin `.*` ni `|`; 52/52 en su página con huella correcta. Cinco hallazgos afirman algo más que su cita registrada |
| **E-R6** preservación | **CERRADO CON LÍMITES** | Índice en Git completo; 32/32 extractos coinciden con su página; ningún PDF en Git. «Versión» es el HEAD del auxiliar, no la del documento. Desfase PROVISIONAL (no imputable) |
| **E-R7** redacción | **CERRADO CON LÍMITES** | No quedan «no publicada» ni «sigue sin publicarse». Quedan dos residuos de la misma familia |
| **E-R8** desfases | **CERRADO CON LÍMITES** | Los cuatro desfases señalados están corregidos; el relevo `f00c5dd` reintroduce «este commit» contradictorio |
| **E-R9** reproducibilidad | **CERRADO CON LÍMITES** | Idempotencia, exit 1, carpetas, exit 2 y segundo extractor real (pypdf 7.1.0, 52/52) reproducidos. Dos contraejemplos nuevos (índice sobrescrito tras un fallo; falta de PyMuPDF con exit 0). El manifiesto de `23718fb` listaba 2 `.pyc` (corregido en `f00c5dd`) |

**Conservación: CUMPLE.**
- M1, M2, M6 y N2 siguen ABIERTOS.
- Elis sigue `pendiente_de_datos`.
- No se elige R, θ, λ, k ni umbrales.
- B/P-M1 sigue en `daa7478`.
- El diff está limpio.

**Clasificación global.** Conforme con límites, con una corrección acotada pendiente en M6 (E-R2: clasificación por sociedad). Esa corrección:
- no cambia el estado de M6, que sigue ABIERTO;
- no cambia el 37,3 ni el 117,6;
- sí cambia lo que se dice que contiene el 117,6.

Nada de esto desbloquea R, θ ni λ. Esta revisión no acredita aptitud económica.

---

## 1. E-R1 · N2 — CERRADO

Evidencia: s03, s06 y s01 (citas 41–52).

**1. Afirmación retirada en todos los textos.**
- La única mención que queda de «concepto monetario» o «sección operativa» referida al +25,7 es la que **niega** o **retira** la afirmación. Aparece en:
  - LECTURA cita 42;
  - HALLAZGOS l.29;
  - RESUMEN l.7;
  - PREGUNTAS (N2);
  - RESPUESTA l.11;
  - `lectura_bloque2.py`.
- No queda ninguna formulación positiva de «flujo operativo» o «caja operativa» para el +25,7.
- En ENTREGA.json, `limites_y_bloqueos` dice ahora «+25,7 … nota 4.6 p.350 en linea propia, separada de 'monetary items' (28,2)».

**2. N2 ABIERTO en caja, fiscalidad y reposición, con las tres páginas citadas.** Lo dicen:
- PREGUNTAS (`estado_tras_revision_e1`);
- HALLAZGOS;
- RESUMEN;
- ENTREGA.json;
- PUNTO DE RECUPERACIÓN.

Las páginas se comprobaron en el URD local:
- **p.350:**
  - «Net gain (loss) related to retirement of fixed assets 25.7 (1.5)» va en su propia fila;
  - el desglose «of which» se compone de monetary −28,2, deterioros −0,1, provisiones −0,6, net gain on disposal +25,7, earnouts −0,2 y sin impacto en caja +0,3;
  - el desglose suma **−3,1**, que es el total de OOIE (s03, con Decimal).
- **p.327:**
  - «(23.1)» está **antes** de «NET CASH FROM OPERATING ACTIVITIES 1,510.6»;
  - «Proceeds from disposal of property, plant and equipment 15.3 7.3» está **entre** el subtotal operativo y «NET CASH FLOWS FROM INVESTING ACTIVITIES (991.5)».
- **p.349:** «Change in receivables on disposal of fixed assets 16.9 (0.1)».

**3. Las dos medidas, distinguidas.**
- Los textos separan +23,1 (EFE p.327; «la que F1 usa para f», informe `716cbd6` l.317/l.328) de +25,7 (nota 4.6; «eleva m0 +0,54 pp»).
- Comprobado en el producto `716cbd6`:
  - l.317: «Plusvalías por enajenación … 2025: +23,1 (bajas de inmovilizado +25,7 en OOIE)»;
  - l.328: «+23,1 en 2025»;
  - l.330: «+25,7 en OOIE … eleva m0 … 0,54 puntos».

**4. Nada se iguala con el seguro.** Las citas 50–52 llevan «NO se iguala con el +25,7».

**Precisión, no defecto.** La fila de p.349 es un **movimiento** del año en la conciliación de cuentas a cobrar (de 892,8 a 998,8). «16,9 a cobrar al cierre» es una lectura razonable, porque el movimiento de 2024 fue −0,1. Es la misma formulación que usó el coordinador.

---

## 2. E-R2 · M6 — ABIERTO (corrección acotada)

**Lo pedido que sí está:**
- **Bodensee es una adquisición importante, con su página.**
  - URD p.306, §4.1.2: «The major acquisitions the Group completed during the financial year were: › Wäscherei Bodensee in Switzerland; …»;
  - p.312: «six major acquisitions … including the laundries Wäscherei Bodensee …»;
  - p.341: columna propia.
  - Lo recogen LECTURA (citas 34–37), HALLAZGOS, RESUMEN, PREGUNTAS, ENTREGA y PUNTO. Ya no se presenta como compra pequeña.
- **117,6 y 37,3, separados.**
  - 117,6 es el total de M&A de 2025: p.341, p.327 y presentación p.29.
  - 37,3 es «Other acquisitions» de p.341.
  - El RESUMEN ya no los mezcla.

**Defecto que queda: la clasificación por sociedad (prueba de cierre «Clasificar cada sociedad citada con su página»).**
- LECTURA cita 37, PREGUNTAS (M6) y RESPUESTA l.19 dicen: «cada adquisición importante de 2025 tiene columna propia **(Bodensee, Bugaderia Neutral, Larosé, JP Muller, Adrett, Lavartex)**». Es incorrecto por dos lados:
  1. **Lavartex no es una adquisición de 2025.**
     - En p.341, su columna tiene «Net cash acquired –» y «Cash outflows for the acquisition –»; solo «Earnouts and deferred consideration (19.7)».
     - En p.342 (tabla de 2024), Lavartex ya figura con un earnout de (83,2).
     - No está en la lista de importantes de 2025 de p.306.
  2. **Se omite Acquaflash.** Está en la lista de p.306 («› Acquaﬂash in Brazil») y tiene columna propia en p.341. El propio patrón de la cita 37 contiene `Acqua\S+ash`, pero el hallazgo no la nombra.
- Por eso «117,6 = suma de las columnas de las importantes + Other (37,3)» (LECTURA cita 38, HALLAZGOS l.23 y RESPUESTA) mete en «importantes» un earnout de 19,7 de una compra anterior.
  - Las seis importantes de 2025 suman **60,8**.
  - Lavartex aporta **19,7** de earnout.
  - «Other acquisitions» aporta **37,3**, del que **(3,6)** es earnout o pago aplazado.
  - Las ocho columnas suman 117,8, frente al total impreso de 117,6: diferencia de redondeo de 0,2 (s03).
- **Carsan y Ernst** (citados en Q1 2025 p.1) siguen sin clasificar.
  - El URD 2025 los da como «Major acquisitions» del ejercicio anterior: p.341, «Acquisitions during the previous financial year … Major acquisitions»; Ernst, 19,0 M€ de ingresos; Carsan, 9,7 M€.
  - Tienen columna propia en la tabla de 2024 (p.342).
  - Para M6 importa: su efecto en el primer trimestre de 2025 es crecimiento externo, no orgánico.
- **Contraejemplo mínimo.**
  - URD 2025 p.341, columna «Lavartex»: «Cash outflows for the acquisition –», «Earnouts and deferred consideration (19.7)».
  - p.306: la lista de las seis «major acquisitions» de 2025 es Bodensee, Bugadería Neutral, Larosé, **Acquaflash**, JP Muller y Adrett, sin Lavartex.
- **Corrección pedida.**
  - Sustituir la lista por «Bodensee, Bugadería Neutral, Larosé, Acquaflash, JP Muller, Adrett (p.306/p.341)».
  - Rotular Lavartex como «earnout/aplazado de una adquisición anterior, 19,7 (p.341; p.342)».
  - Clasificar Carsan y Ernst como importantes de 2024 (p.341/p.342).
  - Opcional: notar que 37,3 incluye 3,6 de earnouts y pagos aplazados.

**Errata menor.**
- «Warts cherei» aparece 6 veces: LECTURA ×2, PREGUNTAS ×2 y `lectura_bloque2.py` ×2.
- «Wärtscherei» aparece en HALLAZGOS y en RESPUESTA.
- El nombre impreso es «Wäscherei».

---

## 3. E-R3 · M6 perímetro — CERRADO

- M6 queda **ABIERTO** en PREGUNTAS, HALLAZGOS, RESUMEN y ENTREGA.
- El perímetro (p.313: más de 5,0 M€ en Francia y más de 3,0 M€ en otros países) lleva `tipo_evidencia=corroboracion_base` y cita F1 V1: informe `716cbd6` l.550.
- Comprobado en el producto: l.550 dice literalmente «Corrección V1 … [P: URD 2025 p. 313; DEU 2024 p. 259; URD 2023 p. 267] … 35,3 / 22,0 / 37,3 en 2023–25, 31,5 de media».
- Se retira que el umbral «confirma» el 31,5: «NO confirma el 31,5 M EUR/ano (esa media sale de los flujos de las compras pequenas…)».

---

## 4. E-R4 · M1 — CERRADO CON LÍMITES

**Lo pedido:**
- Capex (p.311–312) y taxonomía (p.215) llevan `corroboracion_base`.
- Perímetro de p.217 añadido, comprobado con Decimal: 26,2 + **183,9** (derechos de uso) + 887,1 + **62,7** (combinaciones) = 1.159,9, frente a 1.160,0.
- Alineado: 72,6 = 1,9 (clima) + 70,7 (economía circular), p.215.
- Se dice expresamente que «no mide el plan climático» y que no es su importe: HALLAZGOS, ENTREGA, PREGUNTAS y PUNTO.

**Límite.** Se siguen rotulando como nuevas cifras que ya están en la base 4.14:
- HALLAZGOS l.7: «Nivel (corroboración de base + **ancla nueva**)». El brochure CGM p.15 aparece como «nueva», pero repite literalmente el URD 2025 p.312, como ya se vio en la revisión anterior.
- PREGUNTAS (M1) y PUNTO l.16: «H1-2026 19,5% **nuevo**». La frase está idéntica en el informe semestral 2026 EN de la base (`3919657f…`, p.10): «the ratio stood at 19.5% in H1 2026 (versus 18.4% in H1 2025), reflecting the ramp up …» (s06).
- `tipo_evidencia=nueva` está bien como atributo del **documento**, pero no como novedad de la **cifra**.
- Corrección sugerida, menor: «corroboración (cifra ya en la base; documento nuevo)».

---

## 5. E-R5 · citas — CERRADO CON LÍMITES

Evidencia: s01, que reutiliza y adapta `citas_E.py`.

**Citas 20 y 21 corregidas.** Se partieron en citas atómicas, sin truncar:
- Q1 2025 p.1, dos citas: Carsan, Ernst y Bodensee con unos 55 M€; y crecimiento externo de +2,1 %.
- Q3 2026:
  - p.1: +1,5 pp y «pipeline remains strong»;
  - p.2: Muller, +0,5 pp;
  - p.3: RS10 desde el 1-jun-2026, +1,3 pp.
- Cada afirmación del antiguo hallazgo 21 tiene ahora su cita.

**Patrones.**
- Ninguno de los 52 contiene `.*`, `.+` ni `|`.
- Usan `\S*` y `\S+`, que no tienen cota pero no cruzan blancos, para los signos `‑€` y los acentos.
- Una vez usan `[\s\S]{0,6}`, que sí tiene cota.
- Ninguna cita llega a 400 caracteres: no hay truncamiento.
- La guarda de `lectura_bloque2.py` falla con `|` (se reprodujo el negativo; s04-E).

**52 de 52 en su página con los PDF locales:**
- 52/52 huellas `sha256_doc` iguales al PDF local.
- Con pdftotext:
  - 48 citas están literalmente en la página;
  - 2 están en orden de lectura: factsheet p.1, en columnas, y URD p.312;
  - 2 dependen del extractor: la cita 33, presentación p.29, y la 37, cabecera de tabla de p.341.
- Las 52 casan además con PyMuPDF 2.1 (reproducción s04) y con pypdf 7.1.0: **52/52**.
- Cita 33: pdftotext muestra el marcador impreso «5» entre rótulo y cifra («acquired 5 (117.6) (183.3)»). La cita registrada lo sigue omitiendo, aunque el hallazgo lo declara.
- Cita 37: en `-layout` se ve la cabecera completa en columnas (Wäscherei Bodensee … Lavartex, Other acquisitions).

**Límites:**
1. **Hallazgos que dicen más que su cita registrada.** El dato está en la página y en el extracto, pero no en la cita:
   - [3] «mejora por mejor gestión de la inversión en lino»;
   - [4] «18,2 %/19,2 % de ventas; FCF 358,6»;
   - [20] «workwear = 37 % de ventas»;
   - [23] «(disciplina de precios)»;
   - [24] «el crecimiento orgánico solo excluye esas y el efecto divisa».

   La regla de E-R5 era «cada afirmación del hallazgo, cubierta por su cita registrada». Hacen falta citas atómicas adicionales o recortar el hallazgo.
2. La guarda solo detecta las cadenas literales `.*` y `|`; patrones como `[\s\S]*` o `.{0,999}` pasarían. Es un riesgo futuro, no un defecto actual.

---

## 6. E-R6 · preservación — CERRADO CON LÍMITES

**Índice de descarga en Git** (`fuentes_descargadas/INDICE_DESCARGAS.csv`):
- 12 filas con `url_solicitada`, `url_final`, `http`, `content_type`, `bytes`, `sha256`, `fecha_descarga` y `version`.
- Valores: 12/12 HTTP 200 y `application/pdf`; URL pedida igual a la final; fecha `2026-11-17T08:43:57Z`.
- Las 11 huellas son iguales a las de `SHA256SUMS` de la Release (11/11).
- La fila del URD lleva la huella de la base.

**Límite: «versión».** La columna `version` vale «auxiliar 93a9780… rama mistral/e-fuentes-elis», es decir, el HEAD del auxiliar en la ejecución. Identifica el script, no la versión del documento. No hay Last-Modified, ETag ni edición. Además, solo queda la fecha de la última descarga, no la del 16-nov.

**Extractos acotados con la huella de su PDF.** Resultado de s02: **32/32 OK**. En cada uno:
- `sha256_pdf` y `bytes_pdf` de la cabecera son iguales al PDF local;
- cada ventana es subcadena exacta del texto PyMuPDF de su página;
- todas sus palabras interiores están en el texto pdftotext de esa misma página;
- contiene todas las citas de esa página;
- la ventana mayor tiene 1.006 caracteres.

Las 32 páginas son exactamente los pares (documento, página) citados. Al reproducir `publicar_extractos.py` sin red se obtienen los 32 archivos **byte a byte idénticos** a los entregados.

**Ningún PDF en Git.** No hay PDF, XLSX, ZIP, `.pyc` ni `.trabajo/` en el diff ni en el árbol `f00c5dd` (s05).

**Desfase, no imputable al autor.**
- La entrega sigue llamando «PROVISIONAL» a los 11 PDF: 44 archivos lo dicen.
- No menciona la Release `fuentes-elis-e-20261117`, que según el control ya los preserva:
  - `CONTROL.json` l.377;
  - commit `1afda4f` «U1 done … 11/11 verified».
- El autor no podía saberlo. Basta con actualizar el texto en la próxima entrega.

---

## 7. E-R7 · frases absolutas — CERRADO CON LÍMITES

Con `grep -rniE "no publicad|sin publicar|sigue sin publicarse"`, fuera de los scripts, solo quedan menciones meta: ENTREGA.json l.37 y RESPUESTA l.47–48. «No localizado en esta búsqueda», con su alcance, aparece en ENTREGA (×5), LECTURA (×5) y PREGUNTAS (×6).

Quedan dos residuos de la misma familia, que el grep del autor no captura:
- LECTURA cita 18, y PREGUNTAS (M2), que la copia:
  - hallazgo: «sin cifra publicada»;
  - no_demuestra: «No publica la tasa de bajas ni por segmento ni total».
- PREGUNTAS (M2), columna de inventario del bloque 1: «ninguna tasa ni importe publicado».

Corrección sugerida: «sin cifra en esta página» y «ninguna tasa ni importe localizado en la búsqueda previa».

---

## 8. E-R8 · textos desfasados — CERRADO CON LÍMITES

**Los cuatro desfases señalados están corregidos:**
- «Bloque 2 (este commit)» ya no está en ENTREGA.json.
- El README ya no dice «pendiente» (bloques 1–5 «publicados»).
- Los títulos dicen «bloque 2 + corrección E1».
- El control citado es `99adbbf`, con el HEAD remoto anotado (`57b34a6`); ya no aparece `ff0c60cd`.

**Límite: el relevo `f00c5dd` reintroduce el mismo patrón.**
- `PUNTO_DE_RECUPERACION.md` es contradictorio:
  - l.12: «Bloque 5 cerrado (relevo, **este commit**)»;
  - l.32: «Revisión del coordinador sobre el bloque 4 (**este commit**)».
- ENTREGA.json, que no se actualizó en `f00c5dd`:
  - dice «Bloque 4 (este commit)»;
  - no menciona `f00c5dd` ni `CHECKPOINT_RELEVO.md` (tampoco en `salida_siguiente`).
- Corrección: sustituir «este commit» por el SHA explícito.

---

## 9. E-R9 · reproducibilidad — CERRADO CON LÍMITES

Evidencia: s04. Reproducción sin red sobre los PDF locales, con PyMuPDF 2.1 y pypdf 7.1.0.

**Lo que se reproduce:**
- **Carpetas.** `descargar_fuentes_elis.py` crea `.trabajo/elis_fuentes/{pdf,texto}` y `fuentes_descargadas/`.
- **Índice.** El índice regenerado es igual al publicado en las columnas `id`…`sha256`.
- **Idempotencia.**
  - Se ejecutaron dos veces seguidas `lectura_bloque2.py` y `publicar_extractos.py`.
  - LECTURA, PREGUNTAS, FUENTES y los 32 extractos salen **idénticos entre las dos ejecuciones e idénticos a los entregados en `f00c5dd`**.
  - `VERIFICACION_SEGUNDO_EXTRACTOR.json` solo cambia en el campo `fecha`, así que no es idempotente byte a byte. Es menor: ENTREGA declara la idempotencia solo para las tres salidas de lectura.
- **Código distinto de 0 si falla una descarga.**
  - Por lectura de código: las excepciones y las respuestas que no son 200 o no empiezan por `%PDF` van a `fallos`, y entonces `sys.exit(1)`.
  - Reproducido: una excepción de red da exit 1; una respuesta 200 `text/html` da exit 1.
- **Negativos de lectura.**
  - Patrón movido a otra página: `AssertionError cita no verificada`, exit 1.
  - Patrón con `|`: la guarda falla, exit 1.
- **Dependencias de commits.**
  - En un repositorio sin los commits, `inventario_bloque1.py` imprime «DEPENDENCIA AUSENTE: 716cbd6… Ejecuta: git fetch https://github.com/jluisplagos/munger-v2.git 716cbd6…» y sale con exit 2.
  - En el auxiliar local, `716cbd6` sigue sin existir; `f5775dc` y `99adbbf` sí.
- **Segundo extractor: es de verdad pypdf.**
  - Llama a `pypdf.PdfReader(<.trabajo>/pdf/<id>.pdf).pages[p-1].extract_text()`, una biblioteca distinta de PyMuPDF.
  - Reproducido con pypdf 7.1.0: **52/52**, el mismo informe salvo `fecha`.
  - Límites:
    - reutiliza los mismos patrones, con `IGNORECASE` y `\s+`;
    - **no recalcula la huella** del PDF que lee: copia `sha256_doc` del JSONL;
    - no es una comprobación visual. El autor dice haber renderizado p.341, lo que no es observable aquí.

**Defectos menores nuevos, con contraejemplo:**
1. **Un fallo de descarga sobrescribe el índice publicado en Git y deja un estado incoherente que pasa con exit 0** (s04-H).
   - Sobre una ejecución buena, se provoca un fallo de red en `q1_2025_revenue`: `descargar` sale con exit 1, pero reescribe `fuentes_descargadas/INDICE_DESCARGAS.csv` con la fila `FALLO_DESCARGA`.
   - Después, `lectura_bloque2.py` sale con **exit 0**: usa el texto viejo de `.trabajo/texto/` y escribe el documento y sus dos citas con `sha256_doc = ''`.
   - Corrección: escribir el índice de Git solo si no hay fallos; en `lectura`, exigir `http == 200` y recalcular el SHA del PDF.
2. **Falta de PyMuPDF con exit 0** (s04-I).
   - Sin `fitz`, `descargar` escribe «ERROR_EXTRACCION: ModuleNotFoundError» en cada texto, deja `paginas_pdf` vacío y sale con **exit 0**.
   - El fallo solo aparece después, en `lectura`.
   - Las dependencias de Python (PyMuPDF, cuya versión no se fija, y pypdf 7.1.0) se mencionan en README y PUNTO, pero no hay `requirements` ni comprobación.
3. **`inventario_bloque1.py`** (lectura de código):
   - necesita red: `git ls-remote origin …`, cuyo `.stdout.split()[0]` lanza IndexError sin red;
   - necesita `.trabajo/base414.zip`: si no está, lanza FileNotFoundError;
   - ninguna de las dos se declara con el exit 2 y el comando.
4. **Manifiesto.**
   - El de `23718fb` lista `scripts/__pycache__/descargar_fuentes_elis.cpython-312.pyc` y `…/inventario_bloque1.cpython-312.pyc`, que no están en Git (`.gitignore`). `sha256sum -c` desde su raíz da **exit 1** (2 no legibles). Es el defecto menor previsto, y queda confirmado.
   - **Corregido en `f00c5dd`:** 49 entradas, sin `.pyc` ni el propio manifiesto, que coinciden con los 49 archivos restantes del árbol; `sha256sum -c` da exit 0.

---

## 10. Conservación — CUMPLE (s05)

- **Estados.** M1, M2, M6 y N2 están **ABIERTOS** en `PREGUNTAS_Y_RESULTADOS.csv` (`estado_tras_revision_e1`) y en todos los resúmenes.
- **Elis.** Sigue `pendiente_de_datos` en ENTREGA, RESUMEN, HALLAZGOS, PUNTO, CHECKPOINT y RESPUESTA. No hay ningún otro estado.
- **R, θ, λ, k y umbrales.** No se elige ninguno. Solo hay frases de no elección. Los únicos umbrales citados son los publicados por Elis (5,0 y 3,0 M€), y no se adoptan.
- **B/P-M1.**
  - `origin/mistral/m2-fundamento-pm1` = `daa74783d2708fcd46ca7c24ae1ffbb327c35784`.
  - Ningún archivo de `resultados_m2` en el diff.
  - `resultados_m2` es idéntico entre `ec707a5` y `f00c5dd`.
- **Diff `93a9780..f00c5dd`:**
  - 50 archivos, todos en `resultados_cierre/elis_fuentes/`;
  - ningún binario (numstat);
  - ningún PDF, XLSX, ZIP, `.pyc`, `__pycache__` ni `.trabajo/`;
  - ningún patrón de secreto;
  - el archivo mayor es `LECTURA_FUENTES.jsonl`, de 51.733 bytes.
- **ENTREGA.json.** `integrado_en_producto` = false; `apto_dinero_real` = «No se declara por este formulario»; `precondiciones_simuladas` = [].

---

## 11. Defectos que quedan (para devolver al autor)

| # | E-R | Severidad | Defecto | Contraejemplo mínimo | Corrección |
|---|---|---|---|---|---|
| D1 | E-R2 | Media (acotada) | Lavartex presentado como importante de 2025; Acquaflash omitido; Carsan y Ernst sin clasificar | p.341, columna Lavartex: «Cash outflows –; Earnouts (19.7)»; p.306: las 6 importantes incluyen Acquaflash y no Lavartex | Lista de p.306; Lavartex como earnout; Carsan y Ernst como importantes de 2024 (p.341/p.342) |
| D2 | E-R5 | Menor | Hallazgos [3], [4], [20], [23] y [24] afirman más que su cita | [4]: la cita es «Net capex (874.7) (876.0)»; el hallazgo añade «FCF 358,6» | Citas atómicas adicionales o recortar el hallazgo |
| D3 | E-R4 | Menor | «ancla nueva» y «H1-2026 19,5 % nuevo» para cifras ya en la base | Informe semestral 2026 EN de la base, p.10: «ratio stood at 19.5% in H1 2026 …» | «Corroboración (documento nuevo, cifra ya en base)» |
| D4 | E-R9 | Menor | Un fallo de descarga reescribe el índice de Git; `lectura` pasa con exit 0 y `sha256_doc=''` | s04-H | No publicar el índice si hay fallos; `lectura` exige 200 y recalcula el SHA |
| D5 | E-R9 | Menor | Sin PyMuPDF, `descargar` sale con exit 0; `inventario` necesita red y `base414.zip` sin declararlo | s04-I; `ls-remote` sin red da IndexError | Comprobar dependencias y salir con exit ≠ 0; fijar versiones |
| D6 | E-R8 | Menor | «este commit» contradictorio en PUNTO (l.12 frente a l.32); ENTREGA sin `f00c5dd` | PUNTO l.12 dice bloque 5 y l.32 dice bloque 4, ambos «este commit» | SHA explícitos |
| D7 | E-R7 | Menor | «sin cifra publicada», «No publica la tasa…», «ninguna tasa ni importe publicado» | LECTURA cita 18; PREGUNTAS M2 | «En esta página» o «en la búsqueda previa» |
| D8 | E-R6 | Menor | `version` = HEAD del auxiliar, no la versión del documento | Índice: «auxiliar 93a9780… rama …» | Añadir Last-Modified/ETag o declarar el significado |
| D9 | — | Errata | «Warts cherei» ×6 y «Wärtscherei» ×2 | LECTURA citas 35–36 | «Wäscherei» |
| — | E-R6 | Desfase (no imputable) | «PROVISIONAL» sin mencionar la Release `fuentes-elis-e-20261117` | `CONTROL.json` l.377; `1afda4f` | Actualizar en la próxima entrega |
| — | E-R9 | Corregido | El manifiesto de `23718fb` listaba 2 `.pyc` que no están en Git | `sha256sum -c` da exit 1 en `23718fb` y exit 0 en `f00c5dd` | Ya corregido en `f00c5dd` |

---

## 12. Sondas

En `<rev_E1>/sondas/`. Cada una tiene su `.out` y, si procede, su `.json`; las rutas están normalizadas a `<rev_E1>`, `<pdf>`, `<base414>` y `<aux>`.

| Sonda | Qué comprueba |
|---|---|
| `s00_ejecutar_todo.sh` | Ejecutor y manifiestos de `f00c5dd` y `23718fb` |
| `s01_citas_52.py` | 52 citas: huella, página, patrón y prohibidos. Adaptado de `citas_E.py` |
| `s02_extractos.py` | 32 extractos: huella, subcadena PyMuPDF, palabras en pdftotext y citas |
| `s03_cifras_y_clasificacion.py` | Identidades con Decimal y clasificación por sociedad (p.306, 327, 341, 342, 349, 350, 215, 217); 3 FALLA, que son D1 |
| `s04_reproduccion.sh` y `s04_descarga_simulada.py` | Reproducción sin red; negativos B–I |
| `s05_higiene_conservacion.sh` | Diff, binarios, secretos, B/P-M1, estados y Release |
| `s06_textos.sh` | E-R1, E-R7, E-R8, cobertura hallazgo/cita y «nuevo» frente a la base |

**Comando:**

```
bash s00_ejecutar_todo.sh <rev_E1> <pdf> <urd2025.pdf en base414> <informe semestral 2026 EN en base414> <aux> <python con PyMuPDF y pypdf 7.1.0>
```

Antes hay que extraer la entrega con `git -C <aux> archive f00c5dd resultados_cierre/elis_fuentes | tar -x -C <rev_E1>/entrega`.
