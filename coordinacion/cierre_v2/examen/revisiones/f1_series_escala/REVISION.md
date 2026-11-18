# Revisión independiente · `f1/series-escala` (F1-SERIES con escala y ceros sin cifra)

- **Rama revisada:** `f1/series-escala` @ `b3998a8` (código y pruebas `a0817ed`, manifiesto `b3998a8`) sobre `examen/ahold-f1` `1a7a6c6`.
- **Revisor:** agente distinto del autor (Opus, esfuerzo alto), 18-nov-2026. No modifiqué la rama ni hice commit.
- **Copia de trabajo:** worktree `/home/user/e_work/wt_rev_series` y copia limpia `git archive b3998a8` en `/home/user/e_work/rev_series_copia`
  con los 1008 binarios de la base 4.14 (`tools/base_414.py verify`: 6798 esperados, 0 ausentes, 0 cambiados) y los 51 binarios del
  examen (Ahold, Jumbo) copiados de `wt_examen` solo si su huella coincide con el manifiesto. Las copias se borran al terminar.
- **Evidencia:** `evidencia/` (sondas, comparación de declaraciones, salidas de las baterías y del arreglo que propongo).

## Veredicto: **CORRECCIONES** (pequeñas y locales)

El diseño es correcto y prudente (comparación exacta, `cero_comprobado` nunca cierra solo, nada de lo que pasaba o bloqueaba cambia).
Pero el cero impreso admite dos falsas aceptaciones con la columna **comprobada** (no pendiente) sobre filas que tienen cifra distinta de
cero, y la escala declarada no se contrasta con la página. Las dos primeras se corrigen con dos líneas (probado: 55/55 sigue pasando).

## 1. ¿Se puede colar una cifra falsa o mal escalada?

Sondas en `evidencia/sondas_series_escala.py` (fuente sintética con huella; resultados con el código de la rama, con el anterior y con
el arreglo propuesto).

| Sonda | Código anterior | Rama | Juicio |
|---|---|---|---|
| S1 · página «EUR million» con «(450)», declarado `escala` «miles» y `valor_fuente` −0,45 (o «unidades», −0,00045) | INVÁLIDO | **no salta, columna comprobada** | **Hallazgo B** |
| S2 · «1.234» en miles leído como 1,234 miles (0,001234 mm) | INVÁLIDO | no salta | ambigüedad heredada de `_literal_valores`, multiplicada por la escala; menor |
| S3 · fila «Finance lease - principal  (12) (10) (9)», `fila` «Finance lease», `literal` «-», 2024 | INVÁLIDO | **no salta, columna comprobada** | **Hallazgo A1** |
| S4 · fila con «- 7» (negativo con espacio, como lo deja `pdftotext`) declarada «-» = 0 | INVÁLIDO | **no salta, columna comprobada** | **Hallazgo A2** |
| S5 · `cero_comprobado` con una frase irrelevante (moneda de presentación) | INCOMPLETO | PENDIENTE (no bloquea) | ver §1.3 |
| S6 · cita «…amounted to 15 million…» (importe entero sin separador) | INCOMPLETO | PENDIENTE | el filtro de importes no la ve; menor |
| S7 · cita truncada que invierte el sentido («no intangible assets arising from business combinations» de «…other than the brands…») | INCOMPLETO | PENDIENTE | inevitable con una subcadena; menor |
| S8 · `cero_comprobado` con `valor_fuente` 3 | INCOMPLETO | INVÁLIDO | correcto |
| S9 · `cero_comprobado` vacío | INCOMPLETO | INCOMPLETO | correcto |
| S10 · «—» real en la columna de 2023 | INVÁLIDO | no salta, comprobada | correcto (el objetivo del cambio) |

Además verifiqué: una cifra que solo coincide por redondeo no pasa (`Q` toma el float por su `repr` y la comparación es con `Fraction`
exacta: −9,2 no vale por −9,199774); la cifra impresa se sigue buscando literal y completa; una escala fuera de los tres valores es
DATOS INVÁLIDOS en `leer_serie` (V-F1e) y en F1-SERIES; un «—» de otra columna da INVÁLIDO; un «—» de otra fila no se toma porque la
búsqueda se limita a la única línea que contiene la `fila` (si hay varias, INCOMPLETO).

### Hallazgo A · ALTA · el cero impreso acepta un guion que no es la celda del ejercicio

`_cero_en_pagina` toma como marca cualquier «-», «–», «—» aislado **después de la etiqueta declarada** y lo alinea con el primer año que
encuentre hacia arriba a ±4 caracteres, en cualquier línea (no solo en un encabezado). Dos casos reales:

- **A1, guion dentro de la etiqueta.** Si `fila` es un prefijo de la etiqueta impresa («Finance lease» de «Finance lease - principal»),
  el guion de la etiqueta cuenta como marca; si encima hay un texto con un año en esa posición («Year ended 2024»), queda **ok** con la
  fila mostrando (10) en 2024. No es teórico: la línea de Zoetis que motivó el cambio es `Financing cash flows – finance leases 2 1 —`,
  con un «–» en la etiqueta (R1-2 de la revisión de `f1/usgaap`).
- **A2, signo separado de su cifra.** «- 7» es un −7 en muchas maquetaciones; el «-» queda a 2 caracteres del final de la celda y la
  tolerancia de 4 lo alinea con la columna: un −7 pasa como cero **comprobado**.

*Corrección propuesta (probada en una copia, no en la rama; `evidencia/arreglo_propuesto_guion.diff`):* descartar la marca si a su
derecha, en la misma línea, quedan letras (salvo otra marca «nil») o si va seguida de un espacio como mucho y una cifra o un paréntesis.
Con ella S3, S4 y S4b dan DATOS INVÁLIDOS, S10 sigue comprobada y la batería del autor sigue en **55/55**
(`sondas_con_arreglo_propuesto.txt`). Conviene añadir S3 y S4 a `test_f1_series_escala.py` como mutaciones.

### Hallazgo B · MEDIA · la escala declarada no se contrasta con la página

La guarda comprueba que `valor_fuente` es la cifra convertida con la escala **declarada**, pero no que la página (o el documento) esté
impresa en esa escala. Antes, sin campo de escala, una página en millones solo admitía `valor_fuente` = cifra; ahora admite también
cifra/1000 y cifra/1 000 000 con la columna **comprobada** (S1). El error al alza ya lo frena V-F1e (ROU o PPA > D&A total); el error a
la baja no lo frena nada: con A1/A2 una ROU mil veces menor deja casi toda la amortización del derecho de uso en D_X (el doble cómputo
que F1 quiere quitar) sin que salte ninguna guarda. *Corrección propuesta:* cuando se declara `escala`, buscar en la página una marca de
esa escala («amounts in euro(s)», «in thousands», «€000», «'000», «million», «€m», «en miles», «en millones»…; una lista cerrada por
escala) y, si no está o está la de otra escala, dejar la columna PENDIENTE (o INVÁLIDA si aparece solo la de otra escala); como mínimo,
que el detalle de F1-SERIES diga que la escala es declarada y no comprobada. En Jumbo la marca está: «(amounts in Euro)» en las cuatro
páginas citadas.

### 1.3 · `cero_comprobado`: qué consecuencia tiene

Con una frase cualquiera de ≥ 8 palabras que esté en la página y sin importes con separador, el año queda **PENDIENTE**: F1-SERIES no
salta. No puede cerrar por sí solo (no hay campo de confirmación del revisor; siempre queda en `columna_pendiente`), y la aptitud por
entradas sigue en «no» porque las filas 85–87 del libro están en el universo de `verificacion_entradas.py`. Pero hay que decirlo claro:
**antes un cero sin cifra bloqueaba F1-SERIES (INCOMPLETO); ahora no bloquea**, así que el rótulo del motor A puede llegar a «utilizable
según F1» con una PPA cero apoyada en una frase que no prueba nada (S5). Es el mismo trato que ya tenía una columna sin encabezado
alineado, y está documentado en el §10 del README, pero es una relajación del estado de F1 que la persona responsable debe conocer. Los
huecos S6 (importe entero) y S7 (subcadena que invierte el sentido) son menores mientras el resultado sea solo PENDIENTE.

## 2. ¿Cambia algún resultado de lo existente?

- **Declaraciones existentes:** las 9 declaraciones con `series` del paquete (Elis, Ahold, Jumbo, ensayos F1) dan exactamente el mismo
  F1-SERIES (salta, severidad, efecto, detalle y resumen) y la misma `leer_serie` con el código anterior y con el de la rama
  (`comparar_declaraciones.txt`: 0 distintas). Solo cambian declaraciones que usan `escala`, «—»/«nil» o `cero_comprobado`, que antes
  eran inválidas o incompletas.
- **Baterías en la copia limpia con binarios** (salidas en `evidencia/`):

| Batería | Resultado |
|---|---|
| `test_f1_series_escala.py` | 55/55 (con el código anterior, 12/55, como dice el autor) |
| `test_motor_a_f1.py` | 163/163 (en el worktree sin binarios, 151/152: falta el libro de Elis; no es del cambio) |
| `test_v631_f1.py` | 28/28 |
| `probar_v631_f1.py estructura` | 21/21 |
| `prueba_pipeline_f1.py` (LibreOffice) | 7/7 |
| `probar_v631_f1.py a0` (LibreOffice) | 22/22 |
| `probar_v631_f1.py f1` (LibreOffice) | RESULTADO_F1 |
| `prueba_pipeline_v631.py` (LibreOffice) | 9/9 |
| `verificar_paquete.sh rapida` | RESULTADO_RAPIDA |

LibreOffice, siempre con `flock /home/user/e_work/libreoffice.lock` y en secuencia.

- **Manifiesto (nota, no defecto del código):** el commit `b3998a8` no solo añade los archivos del cambio: también incorpora 673 archivos
  del examen (`2026-11_examen_universo`) que `1a7a6c6` ya versionaba sin estar en el manifiesto, y actualiza la huella de
  `personaje_v2/prompts/metadatos_fase1.md`, cambiado en `f5bc5d4` (decisión P-O2) sin regenerar el manifiesto. Es decir, el manifiesto de
  la base `1a7a6c6` estaba desfasado. La regeneración es correcta, pero el mensaje del commit solo dice «8723 files»; conviene dejarlo
  escrito en el registro de la rama para que nadie lo lea como un cambio del prompt hecho aquí.

## 3. Integración con `origin/f1/usgaap` (@ `bcb6dc3`)

`git merge-tree --write-tree origin/f1/series-escala origin/f1/usgaap` (base común `1694f08`): **un solo conflicto, en
`MANIFIESTO_SHA256.txt`** (se regenera). `motor_a_f1.py`, `README_V6.3.1_F1.md`, `verificar_paquete.sh` y `metadatos_fase1.md` se
fusionan solos. Probé el árbol fusionado (los archivos de código, pruebas y el prompt del árbol `45426a5`, sobre la copia limpia):
`test_f1_series_escala` 55/55, `test_motor_a_f1` 163/163, `test_motor_a_f1_usgaap` 246/246, `test_v631_f1` 29/29. En el código fusionado
el bucle de F1-SERIES recorre también las series de US GAAP, así que el cero impreso y `cero_comprobado` les llegan: el Hallazgo A
importa todavía más allí (Zoetis lleva un «–» en la etiqueta de la fila). No probé con LibreOffice el árbol fusionado.

## 4. Jumbo (`/home/user/e_work/series_escala/jumbo_d_copia/Jumbo/motor_a_f1.json`, `comparacion_jumbo.json`)

**D&A de derechos de uso 2021–2025: correcta.** En las cuatro páginas (AR2022 p. 97, AR2023 p. 100, AR2024 p. 183, AR2025 p. 185) la
nota 5.8 del grupo dice «(amounts in Euro)», la sección «Depreciation», fila «- Additions» del ejercicio, columna «Total of leasehold
fixed assets» imprime (9.199.774), (8.660.374), (7.942.175), (8.292.855) y (8.503.619); 2021 cuadra con sus tres componentes
(282.044 + 8.864.305 + 53.425). `escala` «unidades» y `valor_fuente` −9,199774… son exactos, signo −1 con tratamiento declarado. La columna
queda PENDIENTE con razón: «- Additions» está en 4 líneas de cada página y la columna es una clase de activo, no un ejercicio; el año lo
da el bloque entre «Net Cost as at 31/12/…», que debe confirmar un revisor. Nota: la cabecera de la p. 189 del texto FY2025 dice
«01.01.2024-31.12.2024»; es una errata del propio informe (la p. 185 trae saldos a 31/12/2025).

**PPA cero: la cita prueba menos de lo que dice, y nada para 2021–2024.** Los cinco años citan la misma frase de AR2025 p. 189: «The
changes arising from the measurement … at fair value relate to the remeasurement of the property at fair value». Esa frase solo dice
que en la asignación del precio de HERALD 2 (adquirida el 24-oct-2025) la única revalorización es la del inmueble; es decir:
- para **2025** apoya que esa combinación no creó intangibles (el cuadro de la misma página no tiene ninguna línea de intangibles), pero no
  excluye intangibles de combinaciones anteriores; y sí muestra un mayor valor de 162.000 € en la inversión inmobiliaria, que Jumbo mide
  al coste (nota 4.7) y por tanto amortiza: si la serie PPA incluye la amortización de revalorizaciones de la asignación, no es cero
  exacto (es inmaterial: del orden de miles de euros al año);
- para **2021–2024** no prueba nada: es un hecho de octubre de 2025. El propio `motivo` lo admite («se apoya además en el cuadro de la
  nota 5.8 de su informe»), pero ese cuadro no está citado ni comprobado. La prueba honrada para cada año es el cuadro de inmovilizado
  e intangibles de su propio informe (único intangible «Software», sin fondo de comercio ni otros intangibles; los textos solo mencionan
  el fondo de comercio en las políticas contables), y eso no cabe en una frase de ≥ 8 palabras sin importes. El diseño de
  `cero_comprobado` no tiene salida para un cero probado por la estructura de un cuadro.

Como queda PENDIENTE de revisor, el resultado del programa no es falso; pero un revisor no debe confirmar 2021–2024 con esta cita.
Recomendación: citar para cada año su propio informe (p. ej. una frase de la nota 5.8 o de las políticas que diga que el grupo no tiene
intangibles distintos del software, si existe) o dejar esos años como decisión registrada de la persona responsable. En
`comparacion_jumbo.json` el estado global no cambia (`pendiente_de_datos` por F1-K3a y F1-LIBRO en los tres casos); con la declaración
ajustada F1-SERIES pasa de AVISO/DATOS INVÁLIDOS a no saltar, con 0 columnas comprobadas y 10 pendientes. Lo he reproducido.

## Qué pido antes de integrar

1. Hallazgo A: el filtro de marcas (o uno equivalente) y las mutaciones S3/S4 en la batería.
2. Hallazgo B: contraste de la escala con la página (PENDIENTE si no hay marca de escala), o como mínimo decirlo en el detalle y en el §10.
3. Registrar en el §10 que `cero_comprobado` deja de bloquear F1-SERIES (antes INCOMPLETO) y que no hay vía para que un revisor lo cierre.
4. Jumbo: no presentar la cita de AR2025 p. 189 como prueba del cero de 2021–2024.

Lo que no comprobé: Excel real; el árbol fusionado con `f1/usgaap` con LibreOffice; `verificar_paquete.sh completa`.
