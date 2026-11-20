# U2 · Propuesta para el tercer caso B fuera de muestra (F-B3) · 17-nov-2026

**Naturaleza.** Es una propuesta de preparación: no es una decisión, una adopción ni una aptitud.
- No elige el motor: lo decide la fase A del producto a partir de los hechos.
- No fija R, θ, λ, k, probabilidades ni umbrales.
- No usa precios.
- Inventario y huellas: `RECURSOS_EXISTENTES.md`. Fuentes: `INDICE_FUENTES.csv`.

## 1. Candidato y alternativa

| | Propuesta | Condición |
|---|---|---|
| **Candidato** | **Koninklijke Ahold Delhaize N.V.**, la reserva que nombró la persona responsable el 14-nov-2026 | Avanza cuando la persona entregue H1 y H2: la etapa 1 de Ahold (`RECURSOS_EXISTENTES.md` §5.1) |
| **Alternativa** | **Una empresa de las 116 de la etapa 1 que designe la persona responsable**, con su `<E>_evaluada.xlsx` y su `<E>_respuesta.md`. Debe cumplir los criterios del §2, fijados aquí antes de nombrarla. | Se activa en cualquiera de estos casos: (a) la etapa 1 de Ahold no existe o no está íntegra; (b) la fase A de Ahold elige A, C u «otro método» y la persona quiere seguir buscando un tercer B en vez de reducir el alcance (U2-c). |
| Lo que queda si no hay alternativa | U2-c: reducir el alcance a dos casos B | Exige una decisión explícita de la persona |

**Por qué la alternativa no lleva nombre.**
- **No conozco las otras ≈113 empresas:** no hay nada conservado.
- **No hay que empezar ninguna «desde cero»:**
  - la persona descartó esa vía el 14-nov para Meliá y Gestamp;
  - un caso sin etapa 1 obligaría a fijar la r heredada (C56), que es un parámetro económico.
- **Nombrar yo una empresa conocida sería elegir por conveniencia, sin protocolo.**

## 2. Por qué cumple «fuera de muestra» y el protocolo de selección

**Criterios fijados antes de abrir la etapa 1 de Ahold.**
- Se aplican igual a la alternativa.
- No usan precio, valoración ni resultado de la etapa 1.

| # | Criterio | Ahold | Fuente |
|---|---|---|---|
| S1 | No está en la muestra del producto: no es Aarsleff, Hermès, Nike, Rational, Vidrala, Viscofan ni Elis, ni tiene expediente del producto | Cumple. No hay ningún expediente ni archivo de Ahold en el ZIP base-4.14 ni en los repositorios. | `RECURSOS_EXISTENTES.md` §2.1 |
| S2 | La configuración y las convenciones del motor B no se ajustaron con ella | Cumple: P-M1, k y los protocolos se construyeron con Viscofan y Vidrala | `MATRIZ_ALCANCE_4_14.md` §1 |
| S3 | Está entre las 116 de la etapa 1 y la seleccionó la persona responsable antes de examinar la valoración del producto | Cumple según el registro. Límite: la limpieza respecto del juicio de precio de la propia etapa 1 la tiene que confirmar la persona (H4). | `SELECCION_TERCERA_EMPRESA.md` (`d8b9464d…`) |
| S4 | No es financiera (el motor C queda fuera de F-B3) | Cumple: es distribución minorista de alimentación | informes anuales |
| S5 | Documental: diez ejercicios auditados con NIIF, descargables del emisor con huella | Cumple: 10/10 descargados (§6) | `INDICE_FUENTES.csv` |
| S6 | Negocio: hay hechos de financiación que la fase A tendría que pesar (deuda, arrendamientos, pensiones, recompras). **Es condición de posibilidad, no predicción del motor.** | Hay hechos (§5) | informes 2019 y 2025 |
| S7 | Método posible: el producto tiene una plantilla para el motor que elija la fase A, o un cierre legítimo si no la tiene | Cumple: V6.4/V6.4.1 para B; «límite del modelo» para A, C u otro | `GUIA_RECORRIDO_SUPERVISADO.md` §4 y §8.5 |

**Lo que este protocolo no hace:**
- no reordena candidatas después de ver un resultado;
- no cambia de empresa si Ahold sale A;
- en ese caso, se conserva el resultado (regla 3 de la selección) y la persona decide si activa la alternativa.

## 3. Qué entradas tendría el expediente

Expediente nuevo y aislado, con el modelo de Elis 4.14 (`elis/`, `elis_decisiones/`) y de Vidrala y Viscofan. Nada se escribe sobre el producto ni sobre `main`.

| Entrada | De dónde sale | Quién la produce |
|---|---|---|
| `etapa1/Ahold_evaluada.xlsx`, `etapa1/Ahold_respuesta.md`; `juicio.json`, `extracto.md` y archivo de cambios, si existen | **La persona responsable** (H1 y H2) | Ella. Se inventaría como `INVENTARIO_ELIS.md`: integridad, versión V5.3, fecha D4, unidad, períodos de cada celda. Si hace falta una copia de ensayo con `cambiar_base.py`, el original se conserva (precedente: Elis, `b775e6b0…` frente a `bc9bc6ea…`). |
| `pdf/`: los diez informes 2016–2025 | §6 (descargados) o sus copias, si H3 muestra otra edición | Nosotros |
| `texto/` con marcas de página | `scripts/pdf_a_texto.py` | Orquestación |
| `fase1_partes/`, `fase1_v63.json`, `fase1_metadatos.json`, `fase1_fuentes.json`, `historia_revision.md` | Historia de 10 años con `prompts/historia_anio.md` (un agente por año) y `fase1_historia.py construir`; metadatos con `prompts/metadatos_fase1.md`: precio, acciones y rf con su fecha y fuente | Agentes de extracción (Sonnet, esfuerzo medio) |
| `verificacion_entradas.json` | `verificacion_entradas.py plantilla`; el extractor rellena; **un revisor distinto** comprueba | Dos agentes distintos |
| `CAMBIO.json` / base | Si la etapa 1 trae celdas de 2026 (como Elis), se reexpresan a la base del último ejercicio auditado. **El ejercicio 2025 de Ahold cierra el 28-dic-2025, no el 31-dic** (AR 2025: «52 weeks and ended on December 28, 2025»). Hay que declarar la fecha de base exacta. | Orquestación, con `cambiar_base.py` |
| `configuracion_economica.json` (N1, N2, N3, P-M1 con perímetro «Caja» o «NIIF 16», `altas_derechos_uso` de cinco años, `protocolo_objetivo`) | Análisis propio de Ahold con página, sin trasladar nada de otra empresa. λ y θ, si no se observan, van como rango. **Nada se adopta.** | Orquestación, congelada **antes** de evaluar (precedente: `elis_configuracion/analisis_configuracion_elis.md`) |
| `alcance_v2.json` | Aviso de ensayo experimental | Orquestación |
| Selección de la plantilla (`config_v2_v64_experimental.json` o `config_v2_v641_experimental.json`) | Declarada en el protocolo congelado antes de ejecutar (precedente: Elis, V6.4.1) | Orquestación; no es parámetro económico |
| Fases A, B y C, verificación, auditoría | Pipeline con agentes reales: Opus alto para A, B y C; auditoría con un agente nuevo de otro contexto | Cola 3, en secuencia por LibreOffice |

## 4. Qué exige la etapa 1 que no se puede reconstruir

1. **Sin `Ahold_evaluada.xlsx` (V5.3), el pipeline no arranca.** Se detiene en el paso 1 (`pipeline.py:636-638`, S-1).
2. **Lleva decisiones fechadas:**
   - las 37 celdas del v1 y sus observaciones;
   - el motor heredado C62, que la fase A revisa con «mantiene/cambia»;
   - **la r heredada C56, que la fase A no cambia** (`prompts/fase_a.md:13`). Reconstruirla obligaría a elegir una tasa de descuento, cosa que está prohibida.
3. **Su Control maestro guarda la evidencia de la fase 1 a la fecha de la etapa 1:**
   - precio, acciones y rf;
   - insiders (C97, ventana de 12 meses);
   - pares.

   Se puede contrastar con fuentes, pero no recrear «como estaba».
4. **La respuesta** (cubo, precio de Sí v1, seis preguntas, qué le haría cambiar) **es el juicio humano heredado** que la fase A trata como hipótesis.
5. **La regla 1 de la selección:** «La etapa 1 no se repite automáticamente». Una etapa 1 nueva hecha por nosotros sería otro análisis, con otro autor y otra fecha. Rompería la comparación con Vidrala, Viscofan y Elis, que heredan de la etapa 1 de la persona.

**Lo que sí se reconstruye:**
- la Historia de 10 años, porque el Excel V5.3 no la tiene, como en Elis;
- los metadatos de la fase 1, con fecha;
- la verificación de las entradas;
- los textos de los PDF.

## 5. Hechos de financiación de Ahold (describen; no eligen el motor)

Con página del PDF, extraídos hoy. **No son entradas verificadas** ni se han registrado en `verificacion_entradas`.

- **Arrendamientos materiales.**
  - A 29-dic-2019: préstamos 3.841 M€, pasivos por arrendamiento 8.484 M€ y deuda neta 11.581 M€ (AR 2019, PDF p. 41).
  - A 28-dic-2025: derechos de uso de 9.488 M€, el 19,3 % del activo total de 49.089 M€; pensiones y otras prestaciones de 504 M€ (AR 2025, PDF p. 53).
- **Ruptura NIIF 16 en la serie.** Los pasivos por arrendamiento de 30-dic-2018 eran 1.379 M€ «as reported» y pasan a 8.270 M€ reexpresados, con un efecto de +6.891 M€ (AR 2019, PDF p. 41; nota 36, PDF pp. 188–192). 2016 y 2017 no están reexpresados.
- **Recompras todos los años.** El sitio oficial tiene una página de programa de recompra para cada año de 2016 a 2026 (`/investors/share-buyback-programs/<año>/`). AR 2025 (PDF p. 54) cita el dividendo ordinario (1.070 M€) y «the completion of the €1 billion share buyback».

**Interpretación.**
- Hay materia para que la fase A considere el motor B: «la hoja restará deuda, arrendamientos, pensiones y minoritarios menos caja».
- Pero la política financiera declarada («Remaining investment-grade rated is a cornerstone of Ahold Delhaize’s financial policy», AR 2025, PDF p. 55) y las recompras regulares también pueden leerse como «financiación estable», que es el motor A.
- **Las dos salidas son posibles. No se predice ninguna.**

## 6. Fuentes públicas recopiladas (estado)

- Sitio oficial del emisor: `https://aholddelhaize.com/investors/annual-reports/<año>/`; los PDF están en `media.aholddelhaize.com`.
- Descarga del 17-nov-2026, entre 09:28 y 09:29 UTC, con `curl --fail --proto =https`, TLS verificado por el proxy y comprobación de la cabecera `%PDF-`.
- Destino: `<e_work>/u2_ahold/pdf/`. Índice: `<e_work>/u2_ahold/INDICE_FUENTES.csv`.

| Ejercicio (cierre) | Archivo | HTTP | Bytes | SHA-256 | Págs. |
|---|---|---|---|---|---|
| 2016 (1-ene-2017) | AD_annual-report-2016.pdf | 200 | 12328415 | `1971488f…3aa5f69` | 251 |
| 2017 (31-dic-2017) | AD_annual-report-2017.pdf | 200 | 48981559 | `c6453a9c…bb7918e11` | 285 |
| 2018 (30-dic-2018) | AD_annual-report-2018.pdf | 200 | 10705670 | `1166874b…f3d58f2` | 241 |
| 2019 (29-dic-2019) | AD_annual-report-2019.pdf | 200 | 12426820 | `0cf336d2…049be31a` | 219 |
| 2020 (3-ene-2021, 53 sem.) | AD_annual-report-2020.pdf | 200 | 16151687 | `7488a116…ee0e24610` | 253 |
| 2021 (2-ene-2022) | AD_annual-report-2021.pdf | 200 | 15864835 | `96f7b7b0…dd987540bb` | 290 |
| 2022 (1-ene-2023) | AD_annual-report-2022.pdf | 200 | 10829225 | `20506e23…77ece40a` | 317 |
| 2023 (31-dic-2023) | AD_annual-report-2023.pdf | 200 | 63256896 | `418802ab…bd169106` | 340 |
| 2024 (29-dic-2024) | AD_annual-report-2024.pdf | 200 | 47722143 | `eb5cbebf…cb32b13` | 382 |
| 2025 (28-dic-2025) | AD_annual-report-2025.pdf | 200 | 17713203 | `11a2faee…c47967a` | 365 |
| Folleto NIIF 16 de 2018 | `https://www.aholddelhaize.com/media/8952/2018-restatement-booklet-ifrs-16-dated-march-25-2019.pdf` (URL del `.bat`) | **404** (2026-11-17T09:29Z; la URL redirige a `aholddelhaize.com/media/8952/…` y devuelve 404) | — | — | — |

- **Huellas completas:** en el índice y en `<e_work>/u2_ahold/SHA256SUMS_pdf.txt`.
- **Folleto:** no está enlazado en las páginas oficiales de 2018 y 2019, ni en las de resultados del 4T-2018 y el 1T-2019. La nota 36 del AR 2019 lo sustituye y es posterior.
- **Comprobaciones de cada PDF:**
  - portada «Annual Report <año>»;
  - fecha de cierre leída en el propio informe;
  - la página del estado de flujos, la que contiene «Net cash from operating activities».

  Son comprobaciones de identidad, **no una verificación de entradas**.
- **Preservación:** el sandbox es efímero. Hace falta una copia duradera que decida la persona (como U1).

## 7. Qué validaría el caso y qué no

**Si la fase A elige B y el recorrido termina con auditoría de otro contexto, validaría:**
- que el recorrido etapa 1 → V6.4/V6.4.1 → verificación de las entradas → fases de juicio → auditoría se transfiere a una tercera empresa B fuera de muestra, de otro sector y de mayor tamaño;
- que la configuración P-M1, con su perímetro «Caja» o «NIIF 16», se puede construir con fuentes de una empresa con arrendamientos muy materiales.

**Si la fase A elige A, validaría otra vez el cierre legítimo `no_entregable · límite del modelo`.** El tercer B seguiría sin validar (§8, R1).

**No validaría en ningún caso:**
- capacidad predictiva;
- un backtest;
- aptitud para dinero real;
- la adopción de P-M1, k = 3, las probabilidades o los protocolos del objetivo;
- la universalidad del motor B;
- la corrección F1 del motor A;
- el motor C.

## 8. Riesgos

| # | Riesgo | Efecto | Tratamiento propuesto |
|---|---|---|---|
| R1 | **La fase A puede elegir el motor A** («financiación estable») | Con la V6.4 termina en «límite del modelo», como Elis. El tercer B no queda cubierto. | Se conserva el resultado. La persona decide entre la alternativa del §1 y U2-c. No se fuerza. |
| R2 | Si sale A: el hallazgo NIIF 16 del motor A (F1) afecta mucho a Ahold (derechos de uso del 19,3 % del activo) | Un precio de Sí del motor A no sería utilizable (precedente: Elis 7,30 €) | Declararlo. No es motivo para elegir ni descartar a Ahold. |
| R3 | Ruptura por la fusión: Delhaize solo consolida desde el 24-jul-2016. Las cifras de 2016 en gráficos son pro forma («The 2016 figures presented in the graphs are pro forma», página oficial de 2019) | La Historia 2016 no es comparable con 2017+ | El extractor declara el perímetro de 2016 y no mezcla pro forma con lo auditado |
| R4 | Ruptura NIIF 16: 2016–2017 sin reexpresar; 2018 en dos versiones | La serie de deuda y arrendamientos mezcla normas | Etiquetar la norma por año. Usar la nota 36 del AR 2019 para 2018 y no inventar reexpresiones de 2016–2017. Huecos como huecos. |
| R5 | Ejercicios de 52/53 semanas (2020 y 2015 de 53) y cierres que no caen en el 31-dic | Distorsión del crecimiento y fecha de base | Declarar las semanas y la fecha exacta de la base (28-dic-2025) |
| R6 | Hecho posterior a la base: la portada oficial del 17-nov-2026 enlaza a un comunicado del 3T-2026 sobre una «business disruption caused by recent cybersecurity incident» (texto de la URL; contenido no descargado; host `newsroom.aholddelhaize.com` no permitido) | Puede ser material para el juicio y para las fechas, y la etapa 1 puede ser anterior | Tras el inventario de la etapa 1, pedir solo los documentos materiales de 2026, con fecha separada de la base (regla 4) |
| R7 | Las ediciones de los PDF de la persona (2019–2025) pueden no coincidir con las de hoy | Páginas de la etapa 1 que no casan | H3: comparar huellas antes de extraer |
| R8 | Selección contaminada si la reserva se eligió viendo el cubo o el precio de Sí de la etapa 1 | Debilita «fuera de muestra» | H4: una línea de la persona |
| R9 | Tamaño: 219–382 páginas por informe; 2023 y 2024 superan los 45 MB | Coste de extracción y de revisión | Un agente por año, como prevé el producto |
| R10 | Grupo sobre todo estadounidense que informa en euros | Efectos de tipo de cambio en la serie | Lo declara la fase A o la B; no es parámetro nuestro |
| R11 | La preservación de las fuentes depende de una decisión de la persona | Sin copia duradera, la trazabilidad depende del emisor | Release o almacén que ella autorice (como U1) |
| R12 | LibreOffice está ocupado por otra prueba | La ejecución no puede ir en paralelo | Cola 3 en secuencia, en copia aislada |

## 9. Petición mínima a la persona responsable (texto listo)

> Para el tercer caso B (Ahold Delhaize, su reserva del 14-nov) necesitamos de su carpeta `KONINKLIJKE AHOLD DELHAIZE`:
> 1. `Ahold_evaluada.xlsx` y `Ahold_respuesta.md` de la etapa 1, tal cual, y `juicio.json`, `extracto.md` o un archivo de cambios si existen.
> 2. Las huellas SHA-256 de sus PDF 2019–2025, o el `HUELLAS.txt` que genera el `.bat`. No hace falta ejecutar el `.bat`: ya tenemos los diez informes del sitio oficial.
> 3. Una línea: ¿influyó el resultado de la etapa 1 de Ahold en elegirla como reserva?
> 4. Dónde guardar de forma duradera los diez PDF descargados, por ejemplo en una Release como la de Elis.
>
> No necesitamos la lista de las 116. Si prefiere no seguir con Ahold, basta con el nombre de otra empresa de las 116 y su etapa 1.
