# Revisión crítica · tres propuestas económicas F1 (Elis) · commit 9cad78d

**Fecha:** 17-nov-2026. **Revisor:** contexto distinto del autor de las propuestas. **Una sola pasada.**

**Material revisado:** rama `origin/auditoria/economica-f1-frente-e` @ `9cad78ddc6bba6e3597517cde6a8045960f0bdda` (sobre `5f6b65c` y `03e7851`), carpeta `docs/validacion_economica_paralela/frente_E_F1_elis/`:
`N1_ALCANCE_EJERCICIOS_TAU.md`, `N1_ACTUALIZACION_EARNOUT_MEXICO.md`, `PROPUESTA_UMBRAL_V-F1a.md`, `scripts/n1_alcance_y_actualizacion.py` y `scripts/umbral_v_f1a_frontera.py`.

Este documento no adopta ni registra ninguna decisión, no aprueba ni rechaza nada en nombre de nadie y no contiene valoraciones ni declaraciones de aptitud. No modifica el repositorio, el CSV, las fuentes ni sus huellas. Se conservan C48 = 108, C49 = 128,1, el FCF base 307,933 y Elis en `pendiente_de_datos`.

Marcas: **[P]** publicado, leído en la página · **[D]** derivado · **[I]** interpretación · **[H]** hipótesis · **[Pol]** política · **[B]** búsqueda sin resultado. Las páginas son páginas del PDF. URD21, URD22, URD23 y URD25: documentos de registro de 2021, 2022, 2023 y 2025 en inglés; DEU24: el de 2024 en francés; «Release»: `fuentes-elis-e-20261117` del repositorio auxiliar.

**Gravedad.** *Material*: cambia una cifra o el fundamento del texto que se pide aprobar; hay que corregirlo antes de decidir. *Medio*: no cambia cifras ni el sentido de las opciones, pero afecta al peso de la evidencia o a cómo se presenta la decisión; la persona responsable debe verlo antes de decidir. *Menor*: precisión, rótulo o hueco de prueba; se corrige antes de registrar o de implementar.

---

## 0. Resumen (15 líneas)

1. **Material.** Copia del commit `9cad78d` por `git archive`; los cinco PDF de Elis y el libro, con las huellas de `datos/fuentes.json`; la Release, bajada por la API REST (11 de 11 con su `SHA256SUMS`). Solo lectura.
2. **Reproducción.** Los dos scripts dan, sobre la copia, salidas idénticas byte a byte a las entregadas (107 controles; 103 lecturas; 30 casos). −11,908 / −18,948, −0,302 / −0,339 y −11,190 / −18,142 se reproducen con el script y con un recálculo propio que no usa código del autor.
3. **Veredictos:** alcance de N1, **CONFORME_CON_LIMITES**; México, **CONFORME_CON_LIMITES**; umbral, **CONFORME_CON_LIMITES**. Ningún hallazgo material; 6 medios y 14 menores. Ninguno cambia una cifra.
4. **Alcance.** Las páginas dicen lo que el documento dice. La propuesta B (2022–2025) no es «todos los ejercicios de τ»: son cuatro de cinco. Cumple como justificación año a año; como alcance es una opción con su motivo, y así debe llegar a la persona responsable.
5. **2021.** No tiene línea fiscal porque la línea se creó después (URD23). La única indicación es una medida de gestión sobre la línea conjunta (5,1 → 3,7). Es más sólida de lo que el documento enseña (en esa misma medida, el gasto IFRS 2, no deducible, solo baja de 28,0 a 25,9; sin efecto fiscal en el earnout, el resto de la nota necesitaría un 35 %), pero no acredita el hecho fiscal.
6. **¿Basta esa medida?** Basta para no extender «sin efecto fiscal» a 2021 sin más: la opción A es una hipótesis. No basta para afirmar que tributó: A′ también lo es, y B equivale a A′ con el tipo efectivo del año. La decisión real es binaria (B o A′ frente a A) y pesa 0,72 en el flujo sin crecimiento (0,23 % del FCF base).
7. **México.** Es la actualización del pasivo, en el resultado financiero (nota 8.2); no es deducible (la línea fiscal solo cuadra con ajuste y actualización juntos, los tres años); su caja está en las adquisiciones. No hay doble cómputo con C48, C49, el FCF base ni el coste de la deuda. Las dos decisiones de N1 se suman en cifras, pero comparten parte del fundamento: conviene verlas juntas (§6.1).
8. **Residuo +0,8 de 2024.** Es real, igual en las dos ediciones y no es redondeo. No toca la cifra de la actualización: la línea fiscal la acota entre 5,36 y 5,85. La nota 4.9 publica una línea de movimiento que el documento no usa y que deja +0,6 fuera en 2024.
9. **2023.** El pasivo «cierra dentro del redondeo» solo con el cierre de la edición anterior y altas cero; con la vigente, entre +0,3 y +3,2. La inferencia sobre los intereses pagados es correcta y se puede reforzar con URD23 p.267.
10. **Umbral.** La base (FCF base) es sólida. El 0,1 % es convencional: tres de sus cuatro referencias son cifras de Elis y la cuarta es externa. «Sin umbral» está presentada con justicia. No se elige por su efecto en Elis (e = 43 %; bloquea con todas las opciones).
11. **No hay caso real que necesite el umbral;** e solo está medida en Elis.
12. **Los 30 casos** dan su estado con una regla escrita aparte. Faltan tres (FCF base negativo con arrendamiento ínfimo, definición del denominador, FCF base registrado frente a exacto) y F10 no detecta la coma flotante si la suma es compensada.
13. **Las tres:** no adoptan nada; conservan C48, C49, el FCF base y `pendiente_de_datos`; no tienen rutas locales; las etiquetas son correctas, con las salvedades de A2 y B5.
14. **Sondas** en `sondas/`; `sondas/reproducir.sh` las repite todas (22 pasos correctos).
15. **No valida** el tratamiento fiscal de 2021, la causa del +0,8 ni la conveniencia de ninguna opción. No decide.

**Lo mínimo que conviene corregir o añadir antes de llevar los textos a decisión** (ninguna cambia una cifra):

| Documento | Qué | Hallazgo |
|---|---|---|
| Alcance | Decir que B son cuatro de los cinco ejercicios de τ y presentar B, A′, A y C como opciones | A1 |
| Alcance | «No acreditada» en lugar de «no la cumple» y «No se sostiene»; en el Texto B, decir de qué clase es la indicación | A2 |
| Alcance | Añadir la evidencia que falta sobre la medida de 2021: la línea IFRS 2, la nota entera y el rótulo «at standard rates» | A3 |
| México | En la respuesta corta, las dos salvedades del cuadre del pasivo (2024: +0,8; 2023: altas no determinables y edición anterior) | B1 |
| Umbral | Decir en el §1 que la cifra no tiene fuente en la base y que no hay caso real identificado | C1, C2 |
| Alcance y México | Una frase que relacione las dos decisiones de N1 | X1 |

---

## 1. Encargo, configuración y límites de la independencia

- **Encargo:** recibido de la sesión coordinadora, con las decisiones ya tomadas por la persona responsable ((1a) b; (1b); (2); (3a); (3b) iv; (4a); (4b) A; (5a), N1 sí y N2 pendiente; (5b); E8.1, τ de cinco años) y sus dos peticiones sobre N1: justificar el alcance para todos los ejercicios de τ e identificar la actualización de México antes de incluirla. Lo he contrastado con el registro del repositorio auxiliar (`coordinacion/cierre_v2/DECISIONES_PARA_EL_USUARIO.md`): «El alcance en los ejercicios de τ y la actualización de México se justificarán por separado antes de decidirlos» y «Umbral de V-F1a: se pide una propuesta; nada adoptado».
- **Configuración:** subagente de revisión lanzado por la sesión coordinadora. El entorno declara el modelo que el `CLAUDE.md` asigna a la revisión crítica; el esfuerzo lo fija quien lanza y no lo puedo verificar desde dentro.
- **Límites:**
  - soy un agente de la misma clase que el autor y recibo el encargo por el mismo cauce: no se descarta un sesgo de lectura común;
  - parto del mismo CSV verificado. He vuelto a ejecutar el verificador de seis dimensiones del autor sobre la copia (salida idéntica), pero no he revisado el verificador: eso lo hicieron las revisiones anteriores. He leído yo las páginas de las que dependen las tres propuestas (§3–§5) y 25 cifras clave con un segundo extractor;
  - los PDF de Elis los he copiado de un árbol local ya materializado de la base 4.14, comprobando sus huellas contra `datos/fuentes.json`. No he vuelto a materializar la base desde su ZIP;
  - mi recálculo de N1 no importa código del autor, pero toma del libro la f registrada y las palancas;
  - red: `git fetch` y la descarga de la Release. `gh release view` falló (GraphQL no disponible, 403) y la descarga se hizo con `gh api` (REST);
  - escribo solo en la carpeta de esta revisión.

---

## 2. Reproducción

`sondas/reproducir.sh` → `sondas/reproduccion.txt`: 22 pasos correctos, 0 con fallo. Python 3.13.18, `pdftotext` 24.02.0, openpyxl 3.1.5, pypdf 6.17.0.

| Comprobación | Resultado |
|---|---|
| Manifiesto del frente | 398 de 398 |
| Cinco PDF de Elis y libro evaluado | Huellas iguales a `datos/fuentes.json` (libro `d2593777…92385`) |
| Release `fuentes-elis-e-20261117` | 11 PDF, `sha256sum -c`: todos correctos; iguales a los `digest` de la API y a los cuatro que declara el script |
| `n1_alcance_y_actualizacion.py`, sobre la copia, con `--raiz` y `--release` | Código 0. 107 controles, 0 fallidos; 103 de 103 lecturas; 19 de 19 pasajes; 2 de 2 búsquedas sin resultado. JSON e informe idénticos byte a byte |
| `umbral_v_f1a_frontera.py` | Código 0. 30 de 30 casos, 14 de 14 comprobaciones, 6 de 6 variantes. JSON e informe idénticos byte a byte |
| `copia_investigacion_f1.py` (referencia de control del anterior) | Código 0, 67 controles. Idéntico byte a byte |
| `verificar_cifras.py` sobre el CSV | 762 filas: 748 OK, 14 PENDIENTE, 0 FALLO (código 2, por los pendientes). JSON idéntico byte a byte. Las 29 filas que usan los dos documentos de N1, OK en sus seis dimensiones |
| Cambios del commit fuera de documentos, scripts y resultados | Ninguno: el CSV, `fuentes.json`, la especificación, la propuesta de decisiones y el motor no cambian entre `77ff89f` y `9cad78d` |

**Cifras que pedía comprobar el encargo** (perímetro `A0_total`; τ de cinco años):

| Cifra | Script del autor, sobre la copia | Recálculo propio (sonda 1) |
|---|---|---|
| Opción B frente al libro: flujo sin crecimiento · año 11 NORMAL | −11,908 · −18,948 | −11,9080 · −18,9479 |
| Opción B frente a N1 en 2023–25 | −0,302 · −0,339 | −0,3025 · −0,3392 |
| Opción A frente al libro | −11,190 · −18,142 | −11,1895 · −18,1422 |

- La sonda 1 lee el CSV y el libro por su cuenta, reproduce los tres flujos del año 11 del libro y rehace 18 cifras de los dos documentos de N1, también con la fórmula cerrada ΔF0 = −V₀·m0·Δτ. Todas coinciden.
- **Los controles del script tienen dientes:** 14 mutantes de 14 detectados (literal, página, posición, huella, pasaje, signo de la regla, convención de τ; sonda 2). Los 6 mutantes del script del umbral, también (sonda 3c).
- **Dos cifras nuevas no tienen control propio en el script:** la opción A′ y la sensibilidad de B (mutantes N02 y N03 de la sonda 2b, no detectados). Son correctas: la sonda 1 las reproduce (−0,202 · −0,226 y −0,252).
- **Sin `--raiz` ni `--release`, el script de N1 termina con código 0** y escribe «0 de 103» lecturas y «huellas no comprobadas» (probado; `sondas/repro/sin_pdf/`). Está declarado en el §12 del documento de alcance; conviene recordarlo: el código de salida, por sí solo, no acredita las lecturas.

**Veredicto de los dos scripts:**

| Archivo | Veredicto | Límites |
|---|---|---|
| `scripts/n1_alcance_y_actualizacion.py` | **CONFORME_CON_LIMITES** | A6 (una [LECTURA] que ya es fila verificada), A7 (A′ y la sensibilidad, sin control) y el control del cierre del pasivo de 2023, que usa la edición anterior y altas cero (B1) |
| `scripts/umbral_v_f1a_frontera.py` | **CONFORME_CON_LIMITES** | C5 (tres casos que faltan en la columna de la propuesta; la coma flotante se detecta solo en parte) |

---

## 3. N1 · alcance en los ejercicios de τ

**Veredicto: CONFORME_CON_LIMITES.** Los hechos y las cifras son correctos. Los límites son de presentación y de peso de la evidencia sobre 2021 (A1–A3).

### 3.1 Lo que dicen las páginas

| Página | Qué he leído | ¿Coincide con el documento? |
|---|---|---|
| URD21 p.217 | Medida «net income from ordinary operations»; todas las partidas con la llamada «(a) Net of tax effect». «Costs related to acquisitions and earnout adjustments(a)»: 3,7 (2021) y 4,6 (2020). «Restructuring costs(a)»: 4,8 y 25,2. «IFRS 2 expense(a)»: 25,9 y 13,4 | Sí |
| URD21 p.253 | Nota 4.6: «Costs related to acquisitions and earnout adjustments» (5,1) y (5,7); reestructuración (6,4) y (33,4); total (16,1) y (64,5) | Sí |
| URD21 p.290 | Conciliación del impuesto de 2021 y 2020: tipo teórico 28,41 % y 32,02 %; «Permanent differences (including non-deductible IFRS 2 expenses)» (12,2) y (7,7). **Ninguna línea de earnout** | Sí |
| URD22 p.285 | Nota 4.6. 2021: costes de transacción (2,1), ajustes de earnout (3,0), total (16,1). 2022: (4,4), 2,1, total (9,0) | Sí |
| URD22 p.326 | Conciliación de 2022 y 2021: 25,83 % y 28,41 %; diferencias permanentes (11,7) y (12,2). **Ninguna línea de earnout en ninguno de los dos años** | Sí |
| URD22 p.249 y p.261 | Medida neta de impuesto de la nota entera: 7,0 (2022) y 11,5 (2021). Estado de flujos, «Other»: (2,5) y 2,9 | Sí |
| URD23 p.302 | Nota 4.6: ajustes de earnout (48,9) en 2023 y **2,4** en 2022; total (67,9) y (9,0). Casi todas las líneas de 2022 cambian respecto al URD22; el total, no | Sí |
| URD23 p.345 | «Adjustments and accretion of non-deductible earnouts**»: (15,8) en 2023 y **0,5** en 2022; «(**) See Note 4.6»; diferencias permanentes de 2022, (12,3) | Sí |
| URD23 p.267, p.279, p.346 | Medida neta de la nota: 64,6 y 7,0; actualización 12,4 y «–», sin la llamada (a). Estado de flujos: 48,4 y (2,5). Francia, tipo efectivo 50,0 %, «heavily impacted by non-deductible earnout adjustments» | Sí |
| DEU24 p.296, p.337, p.338 | (48,9) y 8,7; línea fiscal (15,8) y 0,8; 25,83 % | Sí |
| URD25 p.350, p.392 | (0,2) y 8,7; línea fiscal (0,2) y 0,8; 25,83 % | Sí |

Texto completo de URD21 y URD22: las palabras «earnout», «earn-out» y «contingent consideration» solo aparecen en la nota 4.6, en el comentario de gestión y en la medida neta de impuesto. No hay ninguna otra mención al tratamiento fiscal del ajuste de 2021 [B, confirmada].

Un apoyo que el documento no cita para «misma naturaleza contable»: la base de medición del pasivo está publicada y es la misma en las cinco ediciones. La nota 1.1 exceptúa del coste histórico los «financial liabilities representing a price adjustment, recognized in a business combination, which are measured at fair value» [P: URD21 p.233; URD22 p.265; URD23 p.283; DEU24 p.277; URD25 p.331].

### 3.2 ¿Se sostiene el argumento sobre 2021?

**Sí, como indicación; no, como hecho acreditado.** Tres precisiones (sonda 4).

1. **Que 2021 no tenga línea fiscal no dice nada: es cuestión de calendario** [P][I].
   - La línea se crea en el URD23. El último documento que publicó la conciliación de 2021 es el URD22, anterior.
   - En ese URD22 el abono de 2022 tampoco tenía línea [P]. Al crearla, el URD23 da +0,5 para 2022 y sus diferencias permanentes pasan de (11,7) a (12,3): lo más probable es que estuviera dentro de ellas [I] (URD22 p.326; URD23 p.345).
   - Un ajuste no deducible de 2021 pudo estar igual, dentro de sus (12,2) [H]. El documento lo dice bien en el §5 («Para 2021 no se ha publicado nunca»), pero en el §4 lo cuenta como incumplimiento («No se sostiene»).
2. **La indicación de la medida neta de impuesto es más sólida de lo que el documento enseña.**
   - *La medida de 2021 distingue lo no deducible* [P][D]. En la misma medida, el gasto IFRS 2 pasa de 28,0 (bruto, URD21 p.255) a 25,9 (neto, p.217): un 7,5 % de efecto fiscal. La nota del impuesto lo llama «non-deductible IFRS 2 expenses» (URD21 p.290). No es una medida que aplique un tipo a todo. El documento no usa este dato; su contraargumento (el 19,3 % de 2020) es más débil, porque un 19 % podría salir también de aplicar el tipo local de un país sin mirar la deducibilidad [H].
   - *No depende del supuesto sobre los costes de transacción* [D]. El documento supone que los 2,1 llevan el tipo teórico. Con la nota entera no hace falta: 16,1 → 11,5 es un 28,6 % (27,9–29,3 % con el redondeo). Si el ajuste de earnout no llevara efecto fiscal, el resto de la nota necesitaría un 35,1 % (34,1–36,2 %): muy por encima del tipo teórico del año (28,41 %) y el doble del que esa misma medida da al resto de la nota en 2022 (17,5 %) y en 2023 (17,4 %), años en que el earnout sí consta como no deducible.
   - *Cota sin supuestos favorables* [D]. Con los dos tipos al 34 %, al menos 1,67 de los 3,0 llevan efecto fiscal. El «entre 2,4 y 3,0» del documento vale para el 28,41 % en las dos partidas. Si los costes de transacción no fueran deducibles, el ajuste necesitaría un 46,7 %: imposible. Es decir, en la medida, **las dos partidas** de la línea llevan impuesto.
3. **Y tiene un límite que el documento no cita.** La empresa rotula hoy el efecto fiscal de esta medida «Tax effect (at standard rates)» (URD25 p.313), «Effet impôt (aux taux normaux)» (Release, comunicado del 1.er semestre de 2025, p.6) y «Tax effect (using the standard tax rates)» (comunicado del 1.er semestre de 2026, p.5). Es un efecto calculado por la dirección a tipos estatutarios, no el impuesto de la nota 9. Las cifras indican que excluye lo no deducible [D]: en el 1.er semestre de 2024 el efecto es 14,3 sobre 103,6 (13,8 %); sin unos 25 de earnout, 7,8 de actualización y 12,5 de IFRS 2, queda un 24,5 % sobre el resto, parecido al 24,0 % del 1.er semestre de 2025 (17,5 sobre 72,9). No desmiente la lectura; pero es lo que es: una medida alternativa de rendimiento, sobre una línea conjunta, de un año en que la partida era pequeña.

### 3.3 ¿Excluir 2021 cumple «todos los ejercicios utilizados en τ»?

- **Como justificación, sí:** el documento examina los cinco ejercicios, uno por uno, con su fuente (§2–§4).
- **Como alcance, no:** la propuesta B aplica N1 en cuatro de los cinco. Las opciones que alcanzan los cinco son A′ y A.
- **Debe presentarse como opción con su motivo, no como el alcance que «sigue a τ».** La primera tesis del documento dice que aplicar la regla «en unos años sí y en otros no a la misma partida» mezcla dos definiciones del tipo; la propuesta deja un año fuera. La conciliación entre las dos cosas es una inferencia fiscal sobre 2021, que es justo lo que la persona responsable tiene que valorar. El §10 ya trae las cuatro opciones con su texto; el §1 y el rótulo «(propuesta)» deben decir con las mismas palabras que B son cuatro de cinco.
- **No hay elección por el efecto.** B es, de las tres opciones que tocan 2021–22, la que más baja el flujo; el documento lo declara.

### 3.4 ¿Basta una medida alternativa de rendimiento para contradecir «sin efecto fiscal»?

- **Basta para no extender la regla a 2021 sin más.** La regla se aprobó con una premisa escrita: «No son deducibles: tienen línea propia en la conciliación fiscal». En 2021 esa premisa no está publicada, y lo único publicado apunta en contra. La opción A es, por tanto, una hipótesis [H], y así la rotula el documento.
- **No basta para dar por hecho lo contrario.** A′ aplica a 2021 una regla fiscal distinta apoyada en esa medida: también es [H].
- **B no evita la hipótesis** [D]. Dejar el tipo de 2021 como está equivale exactamente a A′ con el tipo efectivo del propio año (33,1 %) en lugar del teórico (28,41 %): (T + τ·3)/(BAI + 3) = τ. Por eso B y A′ dan casi lo mismo.
- **La decisión real es binaria:** ¿tributó el ajuste de 2021? Si sí, B o A′ (0,10 de diferencia entre ellas). Si no, A. Entre B y A hay 0,718 en el flujo sin crecimiento (0,23 % del FCF base) y 0,805 en el año 11 NORMAL. El «por debajo del 0,15 %» del §1 mide cada opción frente a C, no la distancia entre opciones.

### 3.5 Hallazgos

| Id | Gravedad | Hallazgo | Evidencia | Corrección que propongo |
|---|---|---|---|---|
| **A1** | Medio | La propuesta B no alcanza «todos los ejercicios de τ»: cuatro de cinco. El §1 afirma que el alcance «debe seguir a τ» y propone otra cosa; la diferencia descansa en una inferencia sobre 2021 | Documento, §1, §6.3 y §10 | Decir en el §1 y en el rótulo de B: «cuatro de los cinco ejercicios de τ; 2021 queda fuera por un motivo fiscal no acreditado». Presentar B, A′, A y C como opciones; la recomendación, aparte y por evidencia |
| **A2** | Medio | Redacción más fuerte que la evidencia en lo que la persona responsable lee y aprobaría: «2021 no la cumple» (§1), «**No se sostiene**» (§4) y, en el Texto B, «la única indicación publicada le atribuye efecto fiscal», sin decir de qué clase es | §3.2 de esta revisión; documento, §5 («No es concluyente») y §11 | «No está acreditada» en lugar de «no la cumple». En el Texto B: «…una medida alternativa de rendimiento, sobre la línea conjunta de costes de adquisición y ajustes de earnout, apunta a que llevó efecto fiscal, sin acreditarlo» |
| **A3** | Medio | Faltan hechos publicados que cambian el peso de la indicación: a favor, la línea IFRS 2 y la nota entera; como límite, el rótulo «at standard rates». El contraargumento que sí se cita (19,3 % en 2020) no excluye la lectura de simplificación | URD21 p.217, p.255, p.290; URD22 p.249 y p.285; URD23 p.267 y p.302; URD25 p.313; Release, comunicados de los 1.os semestres de 2025 (p.6) y 2026 (p.5) | Añadirlos al §5. El «2,4 a 3,0» debe llevar su condición y la cota de 1,67 |
| **A4** | Menor | B se presenta como la opción que no supone nada sobre 2021. Equivale a A′ con el tipo efectivo del año. La bifurcación real (B o A′ frente a A) y su tamaño (0,72; 0,23 % del FCF base) no están a la vista | Sonda 1, §5 | Una frase en el §10 y una fila con la distancia entre opciones |
| **A5** | Menor | Línea fiscal de 2022 (0,5 frente a 0,620): hay una tercera lectura que el §7 no enumera. Si los 2,4 enteros no tributan, el 0,5 corresponde a un tipo de entre el 18,4 % y el 23,4 %, es decir, a un tipo local inferior al teórico | URD23 p.345 y p.302; sonda 4, §5 | Añadirla. La sensibilidad ya calculada (−0,252) cubre el caso contrario |
| **A6** | Menor | El tipo teórico de 2024 se trata como [LECTURA] y ya es una fila verificada (`TAX_TEOR_2024`, URD25 p.392). El §2 dice que solo el de 2025 está en el CSV | CSV; script, `LECTURAS["tipo_teorico_2024"]` | Usar la fila; corregir el §2 y el §9 |
| **A7** | Menor | Los escenarios A′ y «sensibilidad de B» no tienen control de referencia en el script | Sonda 2b: N02 y N03 no detectados | Un control con las cifras del documento |

### 3.6 Qué debería ver la persona responsable para decidir el alcance

1. **La tabla de los cinco ejercicios** (documento, §2), con una fila más: clase de evidencia fiscal de cada año.
   - 2023–2025: línea propia en la nota del impuesto, que cuadra.
   - 2022: línea propia [LECTURA], que cuadra con 2,1 y no con 2,4.
   - 2021: ninguna línea, porque la línea no existía; una medida de gestión sobre la línea conjunta apunta a que llevó impuesto.
2. **Las cuatro opciones, sin etiqueta de propuesta, con lo que cada una supone de 2021:**

   | Opción | Ejercicios | Qué supone de 2021 | Tipo de 2021 | τ de cinco años | Frente a N1 en 2023–25: flujo · año 11 NORMAL |
   |---|---|---|---|---|---|
   | C | 2023–25 | Nada; deja además en τ el abono no gravado de 2022 | 0,3310 | 0,28234 | — |
   | B | 2022–25 | No se toca: equivale a que tributó al 33,1 % | 0,3310 | 0,28282 | −0,302 · −0,339 |
   | A′ | 2021–25 | Tributó al 28,41 % [H, por la medida de gestión] | 0,3302 | 0,28266 | −0,202 · −0,226 |
   | A | 2021–25 | No tributó [H, contra la única indicación] | 0,3253 | 0,28168 | +0,416 · +0,466 |

3. **Que la pregunta de fondo es una sola:** si el ajuste de 2021 tributó. Lo publicado no lo acredita en ningún sentido. Entre B y A hay 0,72 en el flujo sin crecimiento.
4. **Que incluir 2022 no depende de esa pregunta:** su línea fiscal está publicada. Dejarlo fuera (C) es mantener en τ una partida que consta como no gravada.
5. **Que ninguna opción «normaliza» el τ de cinco años:** el deterioro no deducible de 2022 (58,7; línea fiscal (15,1), URD23 p.345) pesa 0,0097 en τ y unos 6,1 en el flujo: unas veinte veces lo que mueve la opción B (0,0005). El documento lo declara (§7); es materia de E8.1, no de N1.
6. **Qué se registraría con cada texto:** los valores de T16 (B: 0,28282 y 236,588; A′: 0,28266 y 236,689; A: 0,28168 y 237,307; C: 0,28234 y 236,891) y las [LECTURA] que pasarían al CSV (documento, §9).

---

## 4. N1 · actualización del earnout de México

**Veredicto: CONFORME_CON_LIMITES.** La identificación contable, fiscal y de caja es correcta y está bien apoyada. Las dos opciones se presentan por separado y sin recomendación. Los límites: la respuesta corta sobre el cuadre del pasivo es más limpia que el cuadre (B1).

### 4.1 Lo comprobado en las páginas

| Pregunta | Qué he leído | Resultado |
|---|---|---|
| ¿Es la actualización del pasivo? | Rótulo «Accretion expense for the earnout pertaining to the acquisition in Mexico»: 12,4 (URD23 p.267), 5,6 y 0,7 (URD25 p.313); «Charge de désactualisation…»: 5,6 y 12,4 (DEU24 p.259). Técnica del pasivo: «Offsetting assets and debt related to acquisitions: discounted cash flows», nivel 3 (URD25 p.386) | Sí [P] |
| ¿Está en el resultado financiero, nota 8.2? | «Accretion expenses»: (13,8) y (0,3) (URD23 p.332); (8,8) y (13,8) (DEU24 p.324); (3,8) y (8,8) (URD25 p.379). El texto de las tres notas la nombra. No es una línea de la nota: el importe sale de la tabla del resultado neto corriente, como dice el documento | Sí [P] |
| ¿Es deducible? | Línea «Adjustments and accretion of non-deductible earnouts»: (15,8), 0,8 y (0,2). Con intervalos de redondeo (sonda 4, §5): solo el ajuste da [−12,644; −12,618], [2,234; 2,260] y [−0,065; −0,039], y **no solapa** ningún año; ajuste y actualización dan [−15,860; −15,808], [0,775; 0,827] y [−0,258; −0,207], y **solapan los tres** | No es deducible [P][D] |
| ¿Dónde está su caja? | Nota 2.4, fila «Earnouts and deferred consideration»: (34,4), de ellos Lavartex (31,4) (DEU24 p.288); (93,9) y (83,2) (URD25 p.342); (23,3) y (19,7) (URD25 p.341). Presentaciones de resultados: el pago de 83 millones de 2024 y el último, de 20, van en «Acquisitions of subsidiaries, net of cash acquired» (Release, 2024 p.29; 2025 p.29) | En las adquisiciones [P] |
| ¿Está en la deuda financiera? | Nota 8.5 (URD25 p.384): ninguna línea de adquisiciones ni de earnout | No [P] |
| ¿Hay política contable publicada? | Nota 1.1, bases de preparación: los pasivos financieros que representan un ajuste de precio reconocidos en una combinación de negocios «are measured at fair value» (URD21 p.233; URD22 p.265; URD23 p.283; DEU24 p.277; URD25 p.331) | **Sí, la base de medición** [P]. El documento la da por no encontrada [B]. Lo que no se publica es el reparto de la variación entre la nota 4.6 y el resultado financiero |
| ¿Es un devengo mecánico? | 1.er semestre de 2024: 7,8; año 2024: 5,6 (Release, comunicado del 1.er semestre de 2025, p.6). En ese semestre el earnout se había revaluado al alza «environ 25 millions» (p.5) | No: en el 2.º semestre fue −2,2 [D]. Se recalcula con el pasivo. El documento lo declara |

### 4.2 Doble cómputo

No lo hay, con ninguna de las dos opciones [D]:

- **C48 = 108.** Usa los intereses netos pagados (70,5 / 78,9 / 99,4; fila 15 de la Historia) y el interés de caja del arrendamiento. La conciliación publicada por la empresa pone la actualización solo en el lado de resultados: (5,6) de (130,4) frente a una salida de caja de (78,9) en 2024; (0,7) de (137,1) frente a (99,4) en 2025 (Release, presentaciones de 2024 p.52 y de 2025 p.51). Para 2023, §4.4.
- **C49 = 128,1.** Es el principal del arrendamiento.
- **FCF base = 307,933.** El estado de flujos suma entero el resultado financiero antes del CFO; el pago del earnout está en inversión; los intereses pagados, en financiación (URD25 p.327; orden de líneas comprobado, sonda 5, §4).
- **Coste de la deuda** (`Historia!C63`, 0,0237; motor B, no activo en Elis). Intereses pagados sobre deuda y arrendamientos. El pasivo por earnout no está en ninguno de los dos.
- **Tipo de la fila 10.** Es el único sitio por donde entra hoy: 0,2619 con ella dentro del BAI y 0,2544 sin ella, en 2023. Eso no es cobrarla: es la huella de una partida no deducible en el tipo.

Las cuatro exclusiones de implementación del §6 del documento son las correctas.

### 4.3 El residuo +0,8 de 2024 (sonda 5)

| Lectura | Inicial | Altas | Revaluación | Actualización | Pagos | Calculado | Publicado | Residuo | Sin la actualización |
|---|---|---|---|---|---|---|---|---|---|
| 2023 · cierre del URD23, altas 0 (la del documento) | 90,5 | 0 | +48,9 | +12,4 | −34,4 | 117,4 | 117,3 | −0,1 | +12,3 |
| 2023 · cierre vigente (DEU24), altas 0 | 90,5 | 0 | +48,9 | +12,4 | −34,4 | 117,4 | 118,2 | **+0,8** | +13,2 |
| 2023 · cierre vigente, altas identificadas (Indaco y Levante) | 90,5 | +0,5 | +48,9 | +12,4 | −34,4 | 117,9 | 118,2 | +0,3 | +12,7 |
| 2023 · cierre vigente, altas = precio − desembolso | 90,5 | −2,4 | +48,9 | +12,4 | −34,4 | 115,0 | 118,2 | **+3,2** | +15,6 |
| 2024 · DEU24 | 118,2 | +1,5 | −8,7 | +5,6 | −93,9 | 22,7 | 23,5 | **+0,8** | +6,4 |
| 2024 · URD25 | 118,2 | +1,9 | −8,7 | +5,6 | −93,9 | 23,1 | 23,9 | **+0,8** | +6,4 |
| 2025 · URD25 | 23,9 | +11,4 | +0,2 | +0,7 | −23,3 | 12,9 | 12,9 | 0,0 | +0,7 |

- **El +0,8 de 2024 es real y no es redondeo** (cota 0,35). Es el mismo en las dos ediciones: la reexpresión del cierre (+0,4) es exactamente la del precio de las compras (+0,4).
- **Hay un dato publicado que el documento no usa.** La nota 4.9 trae el movimiento de los pasivos corrientes, con la línea «Change in debt related to business combinations»: 52,8 en 2023 (URD23 p.304), (67,7) en 2024 (DEU24 p.298; (67,4) reexpresado, URD25 p.352) y (18,9) en 2025. Frente a la variación del saldo corriente, deja fuera −0,3 en 2023, **+0,6 en 2024** (en las dos ediciones) y +0,1 en 2025. Es del mismo signo y tamaño que el residuo: coherente con «conversión y otros movimientos» [H]. No lo acredita.
- **La cifra de la actualización de 2024 no depende de ese residuo.** La línea fiscal (0,8) la acota por sí sola entre 5,36 y 5,85, y la conciliación publicada da (5,6).
- **2023 no «cierra dentro del redondeo» sin condiciones.** Lo hace con el cierre de la edición anterior (URD23: 117,3) y suponiendo altas cero. Las altas de 2023 no se pueden determinar: las «otras adquisiciones» pagaron 35,3 por un precio de 32,4 (DEU24 p.288). Con el cierre vigente, el residuo va de +0,3 a +3,2.
- **La conclusión se sostiene en todos los casos:** sin la actualización, el residuo es de 12,3 a 15,6 en 2023, 6,4 en 2024 y 0,7 en 2025.

### 4.4 La inferencia sobre los intereses pagados de 2023

Correcta, y bien rotulada [I]: la tabla de conciliación de 2023 no está entre las fuentes. Se puede reforzar con dos cosas publicadas (sonda 5, §3):

- **La empresa explica cada cifra por separado.** El aumento de los intereses pagados en 2023, por los tipos y las refinanciaciones, sin mencionar el earnout (URD23 p.267). El resultado financiero de 2023, por la actualización del earnout (URD23 p.332).
- **La brecha entre lo devengado y lo pagado** [D]. Intereses de la deuda en resultados, netos de ingresos, menos intereses pagados: +20,8 en 2023, +19,7 en 2024 y +5,5 en 2025. En 2024 y 2025 la conciliación publicada explica esa brecha con partidas sin caja (19,4 y 5,5). Si los 12,4 estuvieran dentro de los 70,5 pagados en 2023, la brecha sería +33,2.

Sigue siendo [I]. Para acreditarlo haría falta la presentación de resultados de 2023, que no está en la base ni en la Release.

### 4.5 Hallazgos

| Id | Gravedad | Hallazgo | Evidencia | Corrección que propongo |
|---|---|---|---|---|
| **B1** | Medio | La respuesta corta («¿Cuadra con el pasivo y los pagos? Sí») y la frase «2023 y 2025 cierran dentro del redondeo» son más limpias que el cuadre: 2023 usa el cierre de la edición anterior y altas cero, que no están determinadas; 2024 deja +0,8 | §4.3; DEU24 p.288 y p.331; URD23 p.292 y p.339; sonda 5; mutante N05 | «Sí, con dos salvedades: 2024 deja +0,8 sin explicar y 2023 depende de las altas, que no se publican. Sin la actualización no cierra ningún año». Dar la fila con el cierre vigente |
| **B2** | Menor | «No hay una tabla publicada del movimiento del pasivo por earnout»: hay una línea publicada de ese movimiento para la parte corriente, y acota el residuo de 2024 | URD23 p.304; DEU24 p.298; URD25 p.352 | Citarla y usarla en el §5 |
| **B3** | Menor | La inferencia de 2023 sobre los intereses pagados se puede apoyar en dos frases publicadas y en la brecha | URD23 p.267 y p.332; §4.4 | Añadirlas; mantener [I] |
| **B4** | Menor | La opción I cambia el objeto de la regla aprobada en (5a): de los ajustes de la nota 4.6 a una partida que no está en la nota ni en el EBIT. El documento lo explica, pero el texto que se aprobaría no dice que enmienda (5a) | Documento, §10; compárese con la cláusula de enmienda de (1a) en la propuesta del umbral | Añadir al texto de la opción I: «Esta aprobación amplía el texto de (5a) solo en esto» |
| **B5** | Menor | «Política contable específica: no la he encontrado publicada [B]». La base de medición sí lo está, en la nota 1.1 de las cinco ediciones: valor razonable. Apoya con [P] lo que el §2 da como [I] («dos variaciones del valor razonable del mismo pasivo»); sigue sin publicarse el reparto entre líneas | URD21 p.233; URD22 p.265; URD23 p.283; DEU24 p.277; URD25 p.331; sonda 5, §5 | Citarla en el §2 y cambiar el [B] por «no se publica el reparto entre la nota 4.6 y el resultado financiero» |

### 4.6 Qué debería ver la persona responsable para decidir

1. **Los tres hechos, con su grado:** qué es [P]; no deducible [P][D], con un cuadre que solo sale con las dos partidas, los tres años; caja en las adquisiciones [P].
2. **Las tres salvedades:** el residuo +0,8 de 2024, sin causa publicada; las altas de 2023, no determinables; la ausencia en los intereses pagados de 2023, que es una inferencia.
3. **Que no es un interés corriente:** se recalcula con el pasivo (−2,2 en el 2.º semestre de 2024) y terminó en 2025 (el 1.er semestre de 2026 imprime «–»). Es la parte financiera de la variación de valor de un pasivo ya liquidado.
4. **Que ninguna de las dos opciones omite caja ni la cuenta dos veces.** Lo que se decide es el alcance de la regla, no un hecho.
5. **Que el efecto no sirve de criterio:** −0,790 · −1,661 con el τ de cinco años; +0,151 · −0,606 con el de la ventana. El signo del flujo sin crecimiento depende de E8.1, no de la partida.
6. **Que la opción I enmienda (5a)** y exige pasar al CSV las líneas fiscales de 2024 y 2025 de la edición vigente; la opción II no cambia nada y deja declarado que el tipo de 2023–25 lleva la partida dentro.
7. **Que esta decisión y la del alcance comparten fundamento** (§6.1): conviene tomarlas a la vista de la tabla conjunta.

---

## 5. Umbral de materialidad de V-F1a

**Veredicto: CONFORME_CON_LIMITES.** La medida está bien elegida y la regla bien definida y probada. La cifra es una convención sin fuente en la base, y el documento lo dice. No hay caso que la necesite.

### 5.1 ¿Fundamento sólido o 0,1 % arbitrario?

- **La base es sólida** [D]. Medir sobre el FCF base y no sobre las ventas da una consecuencia uniforme: el 0,5 % de las ventas de la versión 1 equivale al 2,5 % del FCF base con un margen del 20 % y al 25 % con uno del 2 % (comprobado; casos F17 y F18). La medida no tiene unidades, crece con el exceso y tiene el dominio definido.
- **La cifra no sale de ningún dato, y el documento lo reconoce** («La cifra exacta es convencional»; «0,05 % o 0,2 % serían igual de defendibles»). No es arbitraria en el sentido de escogida sin criterio: es el número redondo del orden de lo que el expediente trata como límite. Pero ese orden está anclado así:

  | Referencia del §3.4 | Valor | De dónde sale |
  |---|---|---|
  | Residuo del interés de arrendamiento | 0,04 % | Cifra de Elis (informe, §5.4: 0,133) |
  | Lo que «se decide partida a partida» | 0,10 %, 0,14 % y 0,26 % | Cifras de Elis, y además efectos de las dos propuestas hermanas, aún sin decidir |
  | Resolución de las fuentes | 0,08 % | Cifra de Elis: depende de su escala y de cómo imprime |
  | Práctica de auditoría | Décimas de punto | Externa; no está en la base |

  La segunda referencia es circular. El documento de alcance dice que esa elección «es de coherencia y de evidencia, no de importe»: no se decide una por una por su tamaño, y su tamaño no puede servir de vara.
- **«Sin coste» no es exacto.** El §1, el §3.4 y el §5 dicen que el error «se corrige sin coste»; el §3.1 enumera lo que el umbral ahorra: declarar otro perímetro, pedir la D&A ROU de los años del ancla fuera de la ventana y volver a anclar S2C, margen y ROIC. El dato de la ventana es el mismo; lo demás tiene coste.
- **e no es «la infravaloración relativa» de los flujos que se valoran** [D]. Es el exceso sobre el FCF base registrado: una medida de tamaño. En Elis, e = 43,0 %; el flujo sin crecimiento queda un 35,9 % por debajo del de `A1_sin_ROU`, y el del año 11, entre un 45,8 % y un 56,5 % (sonda 3, §5). Con un umbral del 0,1 % la diferencia no cambia ningún estado; es una precisión de redacción y un límite: e no acota el error relativo del año 11.

### 5.2 ¿«Sin umbral» está presentada con justicia?

Sí. Es la primera fila de las alternativas, lleva su texto de aprobación («Alternativa igual de fundada, que es lo vigente») y el documento da en su contra un solo inconveniente. El argumento más fuerte a su favor está en el §1 y el §3.1: para medir e hace falta la misma fila con la que se corrige el perímetro. Si acaso, el documento la deja mejor parada que a su propia propuesta, y recomienda adoptar el umbral solo si aparece un caso real.

### 5.3 Los 30 casos de frontera (sondas 3, 3b y 3c)

- **Los 30 casos dan su estado esperado, en las seis opciones, con una regla que he escrito aparte** desde el texto del §4 y el §6, sin usar la función del autor.
- **La tabla del §7 del documento coincide** con la salida: 24 casos comparados, estado por estado y con su e; ninguna diferencia.
- **Mutantes de implementación** sobre la columna de la propuesta (0,1 %):

  | Regla errónea | ¿La detecta algún caso? |
  |---|---|
  | División sin guarda (e = X ÷ FCF ≤ u) | Sí: F19 y F20 |
  | Suma sin dividir por n; último año; máximo; C49 en lugar de la D&A ROU; frontera estricta; ρ sobre ventas | Sí |
  | **Valor absoluto del FCF base** | **No.** F20 solo lo distingue en la columna del 5 % |
  | **Denominador FCF base + X** | **No** |
  | **Coma flotante con suma compensada** (`sum()` de Python ≥ 3.12 o `fsum`) | **No.** F10 solo detecta la suma secuencial con «+» |

- **Casos que añadiría** (estado con la propuesta):
  - FCF base −300 y D&A ROU 0,01: BLOQUEA. Distingue el valor absoluto.
  - X = 0,3001 con FCF base 300 (e = 0,10003 %): BLOQUEA. Fija el denominador.
  - X = 0,3 con FCF base registrado 300,000 y exacto 299,9996: AVISO con el registrado. Fija qué FCF base se compara.
  - 0,1 + 0,1 + 0,1 con FCF base 100: AVISO. Cualquier coma flotante da BLOQUEA.
- **La variante «sin la guarda del FCF base» del autor** solo se detecta por el texto del motivo, no por un estado.
- **«Aritmética exacta»** es una exigencia de implementación: la hoja de cálculo del motor trabaja en coma flotante. Hay que decir dónde se evalúa el control.

### 5.4 ¿Se elige por su efecto en Elis?

No. Elis da e = 43,0 % y bloquea con las seis opciones; con el perímetro de (1a), V-F1a no se aplica. El script lo comprueba y falla si no es así. Lo que sí hay es calibración sobre magnitudes de Elis (§5.1): no es elegir por el efecto, pero es un límite de generalidad.

### 5.5 Hallazgos

| Id | Gravedad | Hallazgo | Evidencia | Corrección que propongo |
|---|---|---|---|---|
| **C1** | Medio | El orden de magnitud del 0,1 % se apoya en tres cifras de Elis y en una referencia externa; la segunda es circular con las propuestas hermanas | §5.1; documento, §3.4; `umbral_v_f1a_frontera.md`, bloque de Elis | Decirlo en el §1: «la cifra no tiene fuente en la base». Quitar la segunda referencia o presentarla como contexto |
| **C2** | Medio | No hay caso real identificado. e solo está medida en Elis. En el árbol hay expedientes de motor A de otras empresas (`Análisis!C62` = «Sí» en Aarsleff, Hermès, Nike y Rational, además de versiones heredadas; en los expedientes de la 4.14, Vidrala y Viscofan van con motor B, donde V-F1a no se aplica): recuento sobre los `celdas_A.json` del árbol, sin verificar cifras | Documento, §1 y §9; recuento del revisor | Decirlo en el §1. Si se quiere fundar la cifra en casos, hay que medir e en esos expedientes con su D&A ROU verificada |
| **C3** | Menor | «e es la infravaloración relativa del flujo calibrado»: es una medida de tamaño sobre el FCF base registrado, no el error relativo de los flujos valorados | Sonda 3, §5 | Redacción; añadir a «Qué no valida» que e no acota el error relativo del año 11 |
| **C4** | Menor | «Se corrige sin coste» frente a lo que el §3.1 dice que el umbral evita | Documento, §1, §3.1, §3.4 y §5 | «Con el mismo dato de la ventana» |
| **C5** | Menor | Tres huecos en los casos de la columna propuesta y detección parcial de la coma flotante | §5.3; sondas 3 y 3b | Añadir los cuatro casos |
| **C6** | Menor | No se dice dónde se evalúa la comparación exacta | Documento, §4 y §6 | Una línea para el frente técnico |

### 5.6 Qué debería ver la persona responsable para decidir

1. **Lo vigente:** V-F1a bloquea con cualquier importe, como aprobó en (1a). Aprobar un umbral es enmendar (1a); el texto propuesto lo dice.
2. **A quién eximiría:** a nadie con arrendamientos corrientes. Con un FCF base del 5–10 % de las ventas, el 0,1 % tolera una amortización ROU de hasta el 0,005–0,010 % de las ventas. A Elis no le cambia nada.
3. **Que no hay caso real** y que e no está medida en los demás expedientes con motor A.
4. **Qué sostiene la propuesta y qué no:** la base de medida, sí; la cifra es una convención sin fuente en la base, anclada en magnitudes de Elis.
5. **Qué deja dentro un aviso:** un error conocido, pequeño y a la vista, que en los años 1–10 puede ir en los dos sentidos. Un aviso no acredita coherencia.
6. **Si se adopta:** registrar el parámetro con fecha, persona y motivo; añadir los casos del §5.3 a T8; decir dónde se evalúa la comparación exacta.
7. **La alternativa que el propio documento sugiere si no hay caso:** mantener «sin umbral» y conservar la propuesta preparada.

---

## 6. Comprobaciones comunes a las tres

| Comprobación | Resultado |
|---|---|
| No adoptan nada | Cumplen. Las tres lo dicen en su cabecera; el commit no toca el CSV, `fuentes.json`, la especificación ni el motor. Los textos de aprobación van entre comillas, como textos «que se pediría aprobar» |
| Conservan C48 = 108, C49 = 128,1 y el FCF base 307,933 | Cumplen. El script de N1 los recalcula y los controla contra el libro; el del umbral falla si el FCF base no es 307,933. Leídos también en el libro: `Análisis!C48` = 108, `C49` = 128,1, `C52` = 307,933 |
| Elis en `pendiente_de_datos` | Cumplen. Ninguna fija R, θ, λ, k ni probabilidades |
| Opciones por separado y sin elegir por el efecto | Cumplen. Alcance: cuatro opciones con su texto; recomienda B por evidencia, y B es la que más baja el flujo. México: dos opciones, sin recomendación. Umbral: propuesta y alternativa «igual de fundada» |
| Etiquetas | Correctas en lo esencial. Salvedades: A2 y B5 (un [B] que es [P] en parte). En el documento de alcance, «[P][D]» para «la medida le atribuye efecto fiscal» es defendible como descripción de la medida; el paso a «el ajuste tributó» es [I] y debe decirse así donde se resume |
| Rutas locales | Ninguna en los tres documentos, los dos scripts ni sus seis salidas (búsqueda de rutas absolutas, carpetas de usuario y temporales). Las instrucciones de reproducción usan `<ruta>` y `<carpeta de la Release>` |
| Páginas citadas | Todas las que he abierto existen y dicen lo citado (§3.1, §4.1). 25 cifras clave, además, con un segundo extractor (sonda 6) |

### 6.1 Relación entre las dos decisiones de N1 (hallazgo X1, menor)

Los dos documentos se presentan por separado, como se pidió, y sus efectos se suman sin interacción (comprobado). Pero no son independientes en su fundamento, y ninguno de los dos lo dice:

- **El argumento de B tiene dos partes** (documento de alcance, §6): (i) el tipo debe medirse sobre la misma base que el margen, que se declara sin ajustes de earnout; (ii) el tipo no debe llevar la distorsión de una partida de earnout no deducible.
- **La parte (ii) vale igual para la actualización:** es no deducible y está en la misma línea fiscal. La parte (i), no: la actualización es financiera, como los intereses, y nunca ha estado en el margen.
- **Consecuencia.** Con B y la opción II se quita de τ una distorsión de 0,0005 (el abono de 2022) y se deja una de 0,0022 (la actualización de 2023–25) que la misma línea fiscal identifica. Es defendible solo con el criterio (i): N1 quita del BAI lo que ha quitado del EBIT, y nada más. Con B y la opción I el criterio es (ii): τ queda sin ninguna partida de esa línea. Con C y la opción II, N1 es solo una normalización del EBIT de la ventana.
- **En los ejercicios 2021–22, N1 ya es una regla solo sobre el tipo:** su EBIT no entra en f ni en m0. La objeción que el documento de México pone a la opción I («sería una regla solo sobre el tipo») describe también lo que hace cualquier alcance más allá de la ventana.

| Frente a N1 en 2023–25: flujo sin crecimiento · año 11 NORMAL | Opción II (sin la actualización) | Opción I (con ella) |
|---|---|---|
| Alcance C (2023–25) | — | −0,790 · −1,661 |
| Alcance B (2022–25) | −0,302 · −0,339 | −1,093 · −2,000 |

Corrección que propongo: una frase en cada documento que remita a la otra decisión y diga qué criterio, (i) o (ii), sostiene cada combinación.

Fuera de los tres documentos, para quien mantenga la carpeta (**D1**, menor): el `README.md` del frente dice que `copia_investigacion_f1.py` tiene «55 controles»; hoy son 67 (`resultados/copia_investigacion_f1.log`).

---

## 7. Lo que esta revisión no valida

- **El tratamiento fiscal del ajuste de earnout de 2021.** Lo publicado no lo acredita.
- **La causa del residuo +0,8 de 2024** ni la de las altas de 2023.
- **Que la actualización no esté en los intereses pagados de 2023:** sigue siendo una inferencia, ahora mejor apoyada.
- **La conveniencia de ninguna opción.** No recomiendo alcance, ni incluir la actualización, ni adoptar el umbral: digo qué supone cada una y qué evidencia tiene.
- **El verificador del CSV:** lo he vuelto a ejecutar y da lo mismo, pero no lo he revisado. He leído las páginas de las que dependen estas tres propuestas.
- **e en los demás expedientes** con motor A.
- **Ninguna valoración de Elis.** R sigue pendiente; (4b) y N2, también.
- No se ha enviado ninguna comunicación a terceros.

---

## 8. Sondas

Carpeta `sondas/`. `reproducir.sh` las ejecuta todas y deja `reproduccion.txt`.

| Sonda | Qué hace | Resultado |
|---|---|---|
| `repro/` | Salidas de los scripts del autor ejecutados sobre la copia (verificador del CSV, copia de investigación, N1 y umbral) | Idénticas byte a byte a las entregadas |
| `s1_recalculo_independiente_n1.py` | Recalcula 18 cifras de los dos documentos de N1 desde el CSV y el libro, sin código del autor; fórmula cerrada; sensibilidad al redondeo de la fila 10 | 18 de 18 |
| `s2_mutantes_script_n1.py` | 14 mutantes sobre una copia del script de N1 | 14 detectados |
| `s2b_mutantes_sin_control.py` | Mutantes sobre cifras nuevas | A′ y la sensibilidad de B, sin control propio; altas de 2023, decisivas para su cierre |
| `s3_umbral_independiente.py` | Regla del umbral escrita aparte, 30 casos, 10 mutantes de implementación, 6 casos adicionales y medidas de Elis | 30 de 30; tres mutantes sin detectar |
| `s3b_coma_flotante.py` | Qué implementaciones en coma flotante detecta F10 | Solo la suma secuencial |
| `s3c_mutantes_script_umbral.py` | 6 mutantes sobre una copia del script del umbral | 6 detectados |
| `s4_indicacion_fiscal_2021.py` | Indicación fiscal de 2021 y línea fiscal de 2022–25, con intervalos, leyendo cada cifra en su página | §3.2 y §4.1 |
| `s5_pasivo_pagos_intereses.py` | Conciliación del pasivo por edición y por altas, línea de la nota 4.9, intereses pagados de 2023 y política de medición de la nota 1.1 | §4.1, §4.3 y §4.4 |
| `s6_segundo_extractor.py` | 25 cifras clave con pypdf | 25 de 25 |
| `pdfnum.py`, `buscar.py`, `pag.sh`, `paginas/`, `textos/` | Utilidades y texto de las páginas leídas | — |
