# Revisión independiente del commit f5a3381 (rama examen/ahold)

«fase1_historia: honour the declared unit of diluted shares». Revisor: agente distinto del autor. Fecha: 2026-11-17.
Archivos: `munger_v2_r1/personaje_v2/scripts/fase1_historia.py` (`comprobar_anio` y `leer` dentro de `construir`) y `munger_v2_r1/personaje_v2/prompts/historia_anio.md`.
No he modificado nada del repositorio. Todo se ejecutó sobre copias en `/tmp/claude-0/revision_acciones/`.

## Veredicto: CONFORME CON LÍMITES

El cambio es correcto en lo que hace: con la unidad declarada, la fila 20 de la Historia sale en millones de acciones en las tres unidades. Sin unidad, la salida es idéntica byte a byte a la del código anterior. Una unidad inválida bloquea y una unidad ausente no rompe nada. Para Ahold, las diez partes declaran «millones», la Historia da 1.031 … 905 y lo he contrastado con el texto citado y con el BPA impreso.

Los límites son estos:
- la regla antigua sigue actuando en silencio para cualquier expediente que no declare la unidad, y es errónea en dos franjas;
- un expediente existente (Nike) ya tiene la fila 20 mil veces más pequeña por este mismo fallo;
- no hay ninguna prueba nueva: el «114/114» del autor no ejercita el código cambiado.

Nada de esto obliga a retirar el parche ni a rehacer Ahold. Antes de extraer empresas nuevas del universo, sí hace falta la corrección del hallazgo 1 (o como mínimo la de 1b).

## Hallazgos

### 1. La regla por tamaño sigue siendo silenciosa y es errónea en dos franjas. Gravedad: ALTA para expedientes nuevos (no afecta a Ahold)
- **Evidencia.** Sin `"unidad"`, el código aplica `v/1e6 si v>1e5; v/1e3 si v>1e3; si no, v`. Falla en dos franjas:
  - **(a)** cifras en millones superiores a 1.000 (más de 1.000 millones de acciones, lo habitual en grandes empresas). Ejemplos: Ahold y Nike.
  - **(b)** cifras en miles superiores a 100.000 (más de 100 millones de acciones impresas en miles, frecuente en los 10-K). Salen divididas por un millón en vez de por mil.
- **Ni `comprobar_anio` ni `construir` exigen la unidad.** El prompt la pide, pero si el extractor la omite el resultado es OK y la Historia se construye.
- **Prueba de mezcla** (copia de Ahold sin la unidad solo en AR_2021):
  - `comprobar_anio` → OK y `construir` → rc=0;
  - la Historia sale `[1031, 1281, 1203, 1112, 1.072, 1034, 1001, 966, 933, 905]`;
  - el 1.072 se usa porque es el comparativo «más reciente». Solo queda una nota en `historia_revision.md` («revisar si la diferencia es grande»).
- **El salto de escala tampoco se detecta.** Con el código anterior, la serie de Ahold era `[1.031 … 1.001, 966, 933, 905]`: un salto de mil veces entre 2022 y 2023 que no produjo ninguna nota. Esa serie daba C28 = «Emite» (CAGR a 5 años +284,85 %) en vez de «Recompra» (−3,33 %).
- **Corrección propuesta** (no cambia la salida de los expedientes antiguos, que no declaran nada):
  - **1a.** En `construir`: si alguna parte declara la unidad de `acciones_diluidas` y otra no, bloquear con una entrada en `historia_revision.md`.
  - **1b.** En `construir`: bloquear o avisar si dos años consecutivos de la serie, o el valor propio frente al comparativo del informe siguiente, difieren más de ×10.
  - **1c.** En `construir`: comparar el último año de la fila 20 con `fase1_metadatos.acciones_diluidas.valor` (C55, en millones) y avisar si difieren más de ×2. Esto detecta también el caso uniforme del hallazgo 2.
  - **1d.** Para expedientes nuevos: exigir la unidad en el `comprobar-anio` que ejecuta el agente. Ojo: `preparar` usa `comprobar_anio` para decidir si vuelve a pedir un año (línea 275), así que el requisito no puede imponerse sin más a los antiguos. Valen una opción del CLI o una marca en `fase1_metadatos`.

### 2. Nike (expediente existente) tiene la fila 20 mil veces más pequeña y el parche, por diseño, lo conserva. Gravedad: MEDIA (declarar; no corregir en el original)
- **Evidencia.**
  - En `empresas_v2/Nike/fase1_partes/AR_2024.json`, el concepto es «Weighted average diluted shares (millions)» con impreso «1,529.7». No declara la unidad.
  - Las diez cifras están entre 1.488 y 1.742.
  - `fase1_v63.json` y `Nike_v63_datos.xlsx` tienen en Historia!C20:L20 los valores `[1.7425, …, 1.4876]`, mientras Análisis!C55 = 1487,6.
  - C28 («Recompra») y C60 (−1,92 %) no cambian, porque son cocientes con escala uniforme. La fase A leyó bien «1.742,5 M».
  - En la plantilla, la fila 20 solo la consumen el control genérico «numérico» del Motor (E234) y la derivación de C28. No hay fórmulas por acción sobre ella, así que el efecto económico es nulo, pero el dato registrado es erróneo.
- **No he podido regenerarlo.** El texto de los informes de Nike no está en `texto/` de la copia, así que no pude rehacer su Historia. Por inspección del código, sin unidad el resultado es el mismo.
- **Corrección propuesta.** Registrar el defecto en un expediente nuevo de corrección. No modificar los originales (CLAUDE.md). Si Nike se vuelve a recorrer, que declare `"unidad": "millones"` en sus diez partes.
- **Barrido de todas las partes `fase1_partes/AR_*.json` del árbol:**
  - Aarsleff (19.313–20.665): miles, bien con la regla antigua.
  - Vidrala: cambia de unidad entre informes (miles en unos años, unidades en otros). Bien con la regla antigua.
  - Elis, Hermes, Rational y Viscofan: unidades, bien.
  - EmpresaX (100): bien.
  - Solo Nike cae en una franja errónea.

### 3. El parche no añade ninguna prueba de regresión. Gravedad: MEDIA
- **Evidencia.** `test_comprobadores.py` no menciona la unidad de `acciones_diluidas`. Las dos menciones de `unidad` que contiene son la del informe. En la copia, `grep` de «acciones|unidad» sobre la salida da 0 líneas. Con 114/114 se demuestra que no hay regresión, no que el cambio funcione.
- **Corrección propuesta.** Añadir casos sintéticos: las tres unidades con el mismo número de acciones; una unidad inválida (bloquea); una ausente (regla antigua); una mezcla (bloquea, cuando exista 1a); un salto ×1000 (bloquea, cuando exista 1b).

### 4. Una unidad de tipo no textual hace que la comprobación se caiga en vez de informar. Gravedad: BAJA
- **Evidencia.** Con `"unidad": []`, tanto `comprobar_anio` como `construir` lanzan `TypeError: unhashable type: 'list'`. Falla a la vista, no acepta nada, pero no da un mensaje útil al extractor. El mismo defecto ya existía en la unidad del informe (línea 181).
- **Corrección propuesta.** Comprobar `isinstance(u, str) and u in ESCALA` en ambos sitios.

### 5. Unidad del comparativo («anterior») frente a la del año. Gravedad: BAJA (basta con declararlo)
- **Evidencia.** La unidad es una por partida y por informe, y se aplica a las dos columnas de ese informe. Es lo correcto, porque las dos columnas salen de la misma tabla de la nota.
- **Cambio de unidad entre informes.** Vidrala lo hace de verdad, y se resuelve informe a informe porque cada uno declara la suya.
- **Riesgo residual.** Un informe que reexprese el comparativo en otra unidad dentro de la misma tabla. No lo he visto en ningún expediente.
- **Por qué basta con declararlo.** La nota de diferencias de `historia_revision.md` lo haría visible, aunque sin bloquear (lo que propone 1b).

## Comprobaciones realizadas (evidencia)

1. **Las tres unidades.** Copia de Ahold con el comparativo 2016 de AR_2017 reescrito, en la parte y en la página del texto, como «1,031,000,000» (unidades), «1,031,000» (miles) y «1,031» (millones). En los tres casos: `comprobar_anio` OK y Historia 2016 = 1031,0. `ESCALA = {"unidades": 1e-6, "miles": 1e-3, "millones": 1.0}` lleva la cifra a millones.
   - **Lo que espera el resto del código, que es millones:**
     - la plantilla: Historia!A20 = «Acciones diluidas (mm)»;
     - el prompt de metadatos: `acciones_diluidas.valor` en millones, que va a C55;
     - `rellenar_fase1_v63.py`: C28 = CAGR de la fila 20 a 5/3 años.
   - **Ninguna fórmula de la plantilla usa la fila 20 salvo el control numérico (Motor E234).** Las cifras por acción salen de C55.
2. **Sin unidad, la salida es idéntica.** Construí con `git show f5a3381^:…` y con f5a3381 sobre copias de Elis, Vidrala y Viscofan (`2026-11_Vidrala_ensayo_4_14/{elis,vidrala,viscofan}`). En los tres, `fase1_v63.json` y `historia_revision.md` son idénticos byte a byte. Fila 20 de Elis = `[114.1355 … 259.0777]`, de Vidrala = `[24.728 … 35.206]` y de Viscofan = `[46.6037 … 45.4792]`.
3. **Unidad inválida y ausente.**
   - «Millones», «», «mm» y 1000: `comprobar_anio` devuelve el error y `construir` sale con rc=1 y lo lista en `historia_revision.md`.
   - Ausente o null: `comprobar_anio` OK y `construir` rc=0 con la regla antigua.
   - Partida no objeto: el mismo error que antes.
   - `[]`: falla (hallazgo 4).
4. **Ahold** (copia de `2026-11_examen_universo/ahold/Ahold/`).
   - **Unidad:** las diez partes, 2016–2025, declaran `"unidad": "millones"`, y cada página citada contiene «Number of shares (in millions)».
   - **Historia nueva:** `[1031, 1281, 1203, 1112, 1072, 1034, 1001, 966, 933, 905]`. Es igual al `fase1_v63.json` guardado, y C55 = 905 coincide con el último año.
   - **Diferencia frente al código anterior:** la única es esa fila.
   - **Contraste con el texto:**
     - **2016:** p. 183 del AR 2016, nota 29, «Number of shares (in millions) … for the purposes of diluted earnings per share 1,031 857». Coherencia: 830 M€ / 1.031 M = 0,81 €.
     - **2019:** p. 168 del AR 2019, «diluted earnings per share 1,112 1,203». Beneficio diluido 1.766 / 1.112 = 1,588; el informe imprime un BPA diluido de 1,59. Para 2018, 1.797 / 1.203 = 1,49, y el informe imprime 1,49.
     - **2025:** p. 260 del AR 2025, «EPS 905 933». 2.264 / 905 = 2,50, igual al impreso; 1.764 / 933 = 1,89, igual al impreso.
   - **Procedencia de la unidad:** la añadieron los extractores de cada año en 99b539d, posterior al parche. Los prompts generados de Ahold son anteriores al cambio del prompt y no contienen la instrucción nueva.
5. **Pruebas.** Ejecuté `python3 -B pruebas/test_comprobadores.py` en una copia del árbol: todo menos `empresas_v2_correcciones/`, de la que copié solo `ceros_heredados_H1.csv` y `2026-11_H3/`, que exige H3. Lo envolví con `flock /home/user/e_work/libreoffice.lock`. Resultado: **114/114 PASAN**, rc=0.
   - **Comprobé que no se escribió nada en el repositorio.** `git status` no cambió, salvo archivos nuevos en `ahold_4_15/`. Esos archivos los está creando otra sesión, ajena a esta revisión (commit bbea4ab de las 20:39). No los toqué.

## Lo que no pude comprobar
- La Historia de Nike con el texto original: falta `texto/` (hallazgo 2).
- Que los extractores declaren la unidad sin que nadie se lo pida, con el prompt nuevo: los prompts de Ahold son anteriores al cambio.
- Ningún caso real con acciones en «miles» por encima de 100.000 (franja 1b): solo razonado sobre el código.
- El efecto aguas abajo del pipeline completo de Ahold con la fila corregida: el pipeline está detenido en el paso 2 por otro motivo (C46/C47).

Guiones y copias de la revisión: `/tmp/claude-0/revision_acciones/scripts/casos.py`, `/tmp/claude-0/revision_acciones/scripts/barrido.py`, `/tmp/claude-0/revision_acciones/test_nuevo.log`.

---

## Segunda ronda: corrección 38149b8 (revisión limitada a lo que cambia)

### Veredicto de la segunda ronda: CONFORME CON LÍMITES

La corrección resuelve el hallazgo 1 (bloqueo de series incoherentes), el 3 (pruebas) y el 4 (mensaje en vez de TypeError en la unidad de la partida). No bloquea ninguno de los expedientes coherentes. Las pruebas nuevas detectan 7 de las 8 mutaciones que les apliqué. Los límites que quedan son menores y basta con declararlos (R2-1 a R2-4). Ninguno exige otra ronda.

### Qué comprobé (copias en `/tmp/claude-0/revision_acciones/ronda2/`)

1. **No bloquea expedientes coherentes.**
   - **Qué ejecuté.** Construí con `f5a3381^` y con `38149b8` sobre los ocho expedientes de `2026-11_Vidrala_ensayo_4_14` que tienen `fase1_partes/`: elis, elis_decisiones, elis_motor_A, vidrala, vidrala_decisiones, vidrala_decisiones_INVALIDO_perdio_analisis, viscofan y viscofan_decisiones. Los scripts corrieron dentro de una copia del árbol, porque `construir` importa `verificacion_entradas`.
   - **Resultado.** Los ocho dan rc=0 y `fase1_v63.json` e `historia_revision.md` son idénticos byte a byte al código anterior al parche.
   - **Ahold.** En `ahold/Ahold` y en `ahold_4_15/Ahold`, rc=0 y la serie es 1.031 … 905. En `ahold/Ahold`, la salida de 38149b8 es idéntica a la de f5a3381.
2. **Bloquea lo que debe** (copias de Ahold; siempre rc=1, sin `fase1_v63.json` y con el motivo en «## BLOQUEA» de `historia_revision.md`):
   - un solo año sin unidad (AR_2021): saltos 1112→1,072→1034;
   - las diez partes sin unidad: salto 1,001 (2022) → 966 (2023), el caso que antes pasaba sin ninguna nota;
   - las diez partes en «miles» (error uniforme, sin saltos): el control frente a C55 da 0,905 frente a 905;
   - C55 escrito en unidades (905.000.000).
   - **Límites y bordes:** con C55 = 9.050 (×10 exacto) no bloquea; con 9.051 bloquea. Con C55 en texto («905») se compara bien. Sin C55, ya se detenía antes por «falta acciones_diluidas».
3. **Nike, con los valores guardados en `empresas_v2/Nike/fase1_v63.json`:**
   - `incoherencias_acciones` da «1.4876 millones en 2025 frente a 1487.6 en los metadatos». Si Nike se regenerara, ahora se detendría, que es lo correcto según el hallazgo 2.
   - Aarsleff, Hermes, Rational, Vidrala y Viscofan (empresas_v2) son coherentes con el control.
4. **Mutaciones** (sobre la copia de `scripts/fase1_historia.py`; restaurada y comprobada con `cmp` frente a 38149b8). `pruebas/test_acciones_unidad_examen.py` sin mutar da 10/10.

   | Mutación | Resultado | Pruebas que fallan |
   |---|---|---|
   | M1 `incoherencias_acciones` devuelve [] | detectada (7/10) | salto, C55, Ahold sin unidad |
   | M2 sin el `return 1` del bloqueo | detectada (9/10) | Ahold sin unidad |
   | M3 se ignora la unidad declarada | detectada (8/10) | Ahold construye; 1.031…905 |
   | M4 se quita el `isinstance` de `comprobar_anio` | detectada (9/10) | unidad [] |
   | M5 sin el control frente a C55 | detectada (9/10) | C55 |
   | M6 umbral ×10 000 | detectada (8/10) | salto; Ahold sin unidad |
   | M7 «millones» = 1e-3 | detectada (7/10) | Ahold ×3 |
   | M8 «miles» = 1e-6 | **sobrevive (10/10)** | — |

5. **`test_comprobadores.py` en la copia** (con flock): 114/114 PASAN, rc=0. El repositorio queda intacto: ni `git status` ni ningún archivo más nuevo que la marca de inicio.

### Hallazgos de la segunda ronda

- **R2-1 (BAJA). Las pruebas solo ejercitan la unidad «millones».** Lo demuestra la mutación M8: un factor erróneo para «miles» o «unidades» no lo detecta ninguna prueba. En datos reales lo frenaría el control frente a C55, porque el error sale uniforme y de ×1000. Corrección propuesta: añadir a la prueba el caso de las tres unidades con la misma cifra (como el caso [1] de la primera ronda).
- **R2-2 (BAJA, anterior al parche). La unidad del informe no textual sigue cayéndose.** Con `"unidad": []` en la raíz de AR_*.json (línea 181), `comprobar_anio` lanza `TypeError: unhashable type: 'list'`. La corrección solo arregló la unidad de la partida. Basta con declararlo o aplicar el mismo `isinstance`.
- **R2-3 (BAJA, declarar). El umbral ×10 deja casos fuera por los dos lados.**
  - Detiene también un salto real de más de ×10, como un *split* 20:1 no reexpresado en los años antiguos. La única salida es `fase1_decisiones.json`, que solo escribe una persona. Es correcto, pero conviene decirlo en la documentación.
  - No detecta *splits* de ×10 o menos (2:1, 5:1) con la serie sin homogeneizar, que siguen falseando C28 sin aviso. Esto ya ocurría antes y queda fuera del alcance del parche.
- **R2-4 (BAJA). La prueba nueva depende de expedientes vivos.** Lee `ahold_4_15/Ahold`, que es un expediente de examen en curso de otra sesión, y `elis_motor_A`. Si alguno cambia, la prueba fallará de forma visible (no pasa en silencio). Conviene fijar una copia propia de la prueba o un manifiesto de huellas.
- **Detalle irrelevante.** Un `True` en `acciones_diluidas.valor` de los metadatos se toma como 1. Ese valor ya sería inválido por otras vías.

### Lo que no pude comprobar
- Nike con `construir`: falta `texto/`. Solo apliqué la función a los valores guardados.
- Un caso real con un *split* de más de ×10.
