# Revisión independiente · Frente A (Mistral, «M2 cobertura VM») · respuesta a la corrección A2 · `8b88fab`

- **Revisor:** agente Claude distinto del autor. No ha escrito ni modificado este material. Fecha: 17-nov-2026.
- **Objeto:** rama `origin/mistral/m2-cobertura-vm`, commit `8b88fab28261506c60bc7631fd24894e225099d2` (v4.0), carpeta `resultados_m2/cobertura_vm/`.
- **Alcance:** solo la respuesta a A2-R1…R5 de `coordinacion/cierre_v2/revisiones_coordinador/A_2c41d68/CORRECCION_A2.md` (rama `origin/coordinacion/cierre-v2`). He leído íntegros `RESPUESTA_A2_CIERRE_V2.md` y `ENTREGA.json`.
- **Comparación:** con `2c41d68`, la entrega revisada antes, y con `9d676ce`, el último commit intermedio. Los commits `94d1a87` a `9d676ce` no respondían a A2, pero sí cambian código que A2 toca.
- **Restricciones respetadas:** sin commit, push ni cambios en ningún repositorio; sin red; sin LibreOffice; sin checkout ni worktree. Extraje con `git archive` y ejecuté Python con `-I -B`. Hay una excepción documentada en `s01b`.
- **Alcance del juicio:** ningún resultado de esta revisión atribuye aptitud financiera ni económica. Un PASS, un recuento o un CONFLICTO de software no prueban la verdad ni el error de una cifra.

## Dictamen

| Punto | Veredicto | En una línea |
|---|---|---|
| **A2-R1** columna posicional | **ABIERTO** | 2a–2e dan el estado esperado, pero el arreglo no es general. **Los 79 CONFLICTO de columna de los datos reales son artificiales**: el valor negativo está en su columna, impreso `(x)` o `−x`. Además, una frase narrativa, una cabecera en dos líneas o un importe con forma de año dan OK falsos |
| **A2-R2** reexpresión | **ABIERTO** | **3e, 3f y 3g siguen fallando**, aunque la respuesta dice «3c–3h y 3j verificadas». Escala y perímetro no se comparan: el código está escrito, pero no se usa. La fila se sigue eligiendo por subcadena. Hay un **atajo nuevo** («no reexpresado documentado» + el valor en cualquier parte del original) en 18 entradas reales: 9 REVISADO, entre ellas las 2 únicas promociones PENDIENTE→REVISADO |
| **A2-R3** escala | **CERRADO CON LÍMITES** | 4a–4c pasan y la página manda. `MILLONES_RE` no reconoce «EUR million» ni «Millones €», que dan OK por la cabecera. Sin impacto en los datos reales |
| **A2-R4** años | **ABIERTO** | `YEAR_RE` ya tiene límites y la cabecera excluye las líneas con importes: 1b y 1c pasan y el caso real C37 queda corregido. Pero **1d sigue fallando**: `check_version` busca el año sin límites (`:518`). El caso inverso, un año seguido de coma («December 31, 2020,»), se lee como importe y produce CONFLICTO falsos reales |
| **A2-R5** textos, comandos, versiones | **ABIERTO** | Los recuentos generados existen y se reproducen. Pero `asociacion_pdf.py` falla con pypdf 6.17.0 con una traza, no con un mensaje claro. `ENTREGA.json` publica huellas del CSV, la verificación y la cola de `160faf9`, que no corresponden a lo publicado. `RESUMEN_PARA_CLAUDE.md` sigue diciendo 0 CONFLICTO. El motivo de AR2025_p27 solo está corregido en 2 de 4 documentos |

**Reproducibilidad: CUMPLE.** De los 62 archivos del manifiesto, 59 se reproducen byte a byte. Los 3 restantes difieren solo por la marca de tiempo del bloque generado (2 archivos) y por la ruta absoluta de `inventario.json`. El control da PASS con código 0. El manifiesto da 62/62. El diff está limpio.

**Propagación: CUMPLE en los datos.** Ningún derivado queda REVISADO con un operando que no lo esté. Pero propaga también los CONFLICTO artificiales: de los 133 CONFLICTO del CSV, **104 dependen únicamente** del defecto de signo de A2-R1.

## Preparación y ejecución

**Extracción**
- `git archive 8b88fab` → `<rev_A2>/entrega`.
- `2c41d68` y `9d676ce` (solo la carpeta) → `<rev_A2>/e_2c41d68` y `<rev_A2>/e_9d676ce`.

**Insumos** (`sondas/s00_preparar_copia.py`, la misma lógica que el revisor anterior)
- ZIP `<zip>`: 1.130.912.246 bytes, SHA-256 `bb51942c…b7b93e`.
- **251/251 conformes**, código 0. Copia aislada en `<rev_A2>/repro`.

**Entorno del revisor**
- Python 3.13.18, openpyxl 3.1.5, pypdf 6.17.0.
- El autor declara Python 3.12.15 y pypdf 7.1.0.

**Reproducción** (`s01_reproducir.sh` y `s01b_cola_resolver.sh`, en el orden de `COMANDOS.md`)

| Comando | Código | Salida clave |
|---|---:|---|
| `inventario.py` | 0 | 677 / 617 / 22 lotes / 21 CONFORME |
| `verificar_fuentes.py` | 0 | 467 COINCIDE_PROPUESTO |
| `verificar_contexto.py` | 0 | fuentes 148 REV / 183 PEND / 93 CONFL / 43 M1 / 210 NA |
| `derivaciones.py` | 0 | 101 nodos (14/87), 0 ciclos |
| `construir_cobertura.py` | 0 | CSV **169 / 209 / 133 / 60 / 106** |
| `control_negativo.py` | 0 | 218 mutaciones, 149 contextual, 40 mecánico; bilaterales 15/15; `sondas_revisor` 5/5 CONFLICTO |
| `control_cobertura.py` (dos veces) | 0 | **PASS, 0 violaciones** |
| `cola_pendientes.py`, `resolver_bloque2.py` con `-I` | **1** | `ModuleNotFoundError: comun`: hacen `import comun` sin insertar su carpeta en `sys.path` |
| ídem con `python3 -E -s -B`, como en `COMANDOS.md` | 0 | 183 fuentes / 26 derivados / 89 grupos; salidas IGUALES |
| `revisar_lote.py L00..L21` | 0 | 22 lotes IGUALES |
| `asociacion_pdf.py` | **1** | `pypdf.errors.PdfReadError` (traza) con pypdf 6.17.0, aunque el guard declara que basta ≥ 6.0 |
| `generar_recuentos_doc.py` | 0 | igual salvo la marca de tiempo |
| `generar_cambios_estado.py 9d676ce… a2_v4` (con `GIT_DIR` del clon, solo lectura) | 0 | 230 fuentes / 286 filas; **IGUAL** byte a byte |
| `generar_manifiesto.py` | 0 | 62 archivos |

**Comparación byte a byte**
- 59 IGUALES.
- `MAPA_REGENERACION.md` y `resultados/RECUENTOS_VIGENTES.md` difieren solo en la marca de tiempo `2026-11-16T22:37:16Z`: el generador escribe la hora actual, así que nunca se reproducen exactos.
- `resultados/inventario.json` difiere en la ruta absoluta `directorio`, que no forma parte del diff.

## Sondas del revisor anterior sobre el código nuevo

`s02` y `s03` son las sondas de la revisión de `2c41d68`, sin cambios de contenido. Las ejecuté sobre `<rev_A2>/entrega/.../verificar_contexto.py`.

| Grupo | Sonda | Obtenido en `8b88fab` | ¿Estado esperado? |
|---|---|---|---|
| A2-R4 | 1b importe 2045,3 con cabecera en dos líneas | NO_DECIDIBLE | sí |
| | 1c el importe contamina las filas siguientes | NO_DECIDIBLE | sí |
| | **1d versión por el importe 2025,4** | **OK** | **no** |
| | 1a (control positivo, fila `2045 2001` sin separador) | PENDIENTE (columna «fila sin valores») | regresión conservadora: los importes 20xx sin separador se descartan como años |
| A2-R1 | 2a años repetidos (consolidado/individual) | NO_DECIDIBLE | sí |
| | 2b mismo valor en dos columnas | NO_DECIDIBLE | sí |
| | 2c valor ausente | CONFLICTO | sí |
| | 2d EPS 950 900 | CONFLICTO | sí |
| | 2e columna de variación | NO_DECIDIBLE | sí |
| | 2f / 2g (controles) | OK / CONFLICTO | sí |
| A2-R2 | 3c columnas ascendentes | CONFLICTO | sí |
| | 3d prefijo numérico | CONFLICTO | sí |
| | **3e otro perímetro en el original** | **NO_APLICA** «coherente» (toma la tabla individual) | **no** |
| | **3f original en millones** | **NO_APLICA** «coherente» | **no** |
| | **3g otra fila con el mismo prefijo** | **NO_APLICA** (fila «Revenue from discontinued operations») | **no** |
| | 3h sin razón documental | NO_DECIDIBLE | sí |
| | 3j «no (igual que…)» | CONFLICTO | sí |
| | 3a, 3b, 3i (controles) | CONFLICTO, CONFLICTO, NO_APLICA | sí |
| A2-R3 | 4a página en millones, cabecera en miles | CONFLICTO | sí |
| | 4b «Millones de euros» | CONFLICTO | sí |
| | 4c miles de acciones | NO_DECIDIBLE | sí |
| | 4d–4g | CONFLICTO / CONFLICTO / CONFLICTO / OK | sí |
| d375d80 | las 5 sondas de `s03` | **5/5 CONFLICTO** | sí |

**Resultado:** 4 sondas de la lista fallan (1d, 3e, 3f, 3g). Las 4 son pruebas de cierre explícitas de A2-R2 y A2-R4.

La respuesta afirma «Sondas 3c–3h y 3j verificadas» y «Sondas 1b–1d verificadas». Esas afirmaciones son falsas para estas cuatro. Las sondas A2 tampoco se publican como artefacto reproducible: `control_negativo.json` solo contiene las 5 de d375d80 y las 15 bilaterales.

## Sondas nuevas: una variante por defecto que no está en la lista (`s07`)

| Punto | Sonda | Entrada mínima | Obtenido | Debía | Clase |
|---|---|---|---|---|---|
| R1 | **R1a** | `2025 2024` / `Cash used in investing (10.000) (9.000)`; declarado 2024 = −9000 | **CONFLICTO** «el valor −9000 no está en la fila» | OK | CONFLICTO falso |
| R1 | **R1b** | `2025 2024` / `Changes in inventories −47.708 −7.660` (U+2212); 2024 = −7660 | **CONFLICTO** | OK | CONFLICTO falso |
| R1 | **R1c** | `During 2024 and 2025 the Group restructured its plants.` / `Notes 2025 2024` / `Revenue 10.000 9.000`; 2024 = 10.000 | **OK**: toma la frase como línea de columnas `['2024','2025']` | CONFLICTO / ND | OK falso |
| R1 | **R1d** | `2025` / `2024` (cabecera en dos líneas) / `Impairment - 1.500`; 2025 = 1.500 | **OK** «posición 0 de 1 → 2025» | CONFLICTO / ND | OK falso |
| R1 | **R1e** | `2025 2024 Variation` / `Revenue 3.100 2030 1.070`; 2024 = 1.070 | **OK**: al quitar el «año» 2030, la variación ocupa la posición de 2024 | CONFLICTO / ND | OK falso |
| R2 | **R2a** | original `Revenue 10000 8000`; comparativo 9000, «el comparativo no ha sido reexpresado» | **OK** «reexpresión confirmada» | CONFLICTO | OK falso |
| R2 | **R2b** | ídem, «reexpresado: no» | **OK** «reexpresión confirmada» | CONFLICTO | OK falso |
| R2 | **R2c** | original `Total equity attributable to owners of the parent 9000 8000` / `Total equity 10000 9500`; cita `Total equity 9000`, no reexpresado | **NO_APLICA** «coherente» (fila por subcadena) | CONFLICTO | acreditación indebida |
| R2 | **R2d** | original «Amounts in euros» `Revenue 9.000 8.000`; comparativo en miles, 9.000 | **NO_APLICA** «coherente» | CONFLICTO / ND | acreditación indebida (escala) |
| R2 | **R2e** | el original dice «did not restate the comparative figures»; no hay fila «Right-of-use assets»; el 28 solo aparece en «Note 28» | **NO_APLICA** «no reexpresado documentado… el valor 28 figura en el original» | ND / CONFLICTO | atajo nuevo |
| R2 | R2f | frase `At December 31, 2024, Euros 335 million…`; cita `At 31 December 2024 9,071` | NO_DECIDIBLE (valores leídos `['2024,', '2025.']`) | ND | correcto aquí; véase el caso real G25 |
| R3 | **R3a** | página «Figures in EUR million», cabecera del documento en miles | **OK** por la cabecera | CONFLICTO / ND | OK falso |
| R3 | **R3b** | página «(Millones €)», cabecera del documento en miles | **OK** por la cabecera | CONFLICTO / ND | OK falso |
| R3 | R3c | «(Miles de euros)» (control) | OK | OK | — |
| R4 | **R4a** | página 2019 atribuida a `CF_2025.txt`; único «2025» en el importe `12025` | **OK** | CONFLICTO / ND | versión acreditada por un importe |
| R4 | R4b | precios `0,2050 0,2095` (control C37) | sin años | sin años | — |
| R4 | **R4c** | `Balance at December 31, 2024, and 2023,` | el «2024,» no cuenta como año (`(?![\d.,])`) y otras rutas lo leen como importe | año | inverso de R4 |

**Lectura de las sondas nuevas:**
- **R1:** los arreglos de 2a–2e son locales.
  - La comparación posicional (`:438`) solo quita `-`: no normaliza `(x)` ni `−`.
  - La línea de columnas sigue siendo la línea con más años de toda la página (`:213`). Puede ser una frase narrativa o la primera línea de una cabecera partida.
  - Quitar de la fila los tokens con forma de año (`:420`) desplaza las posiciones.
- **R2:**
  - La fila del original se acepta si el rótulo de la cita es una **subcadena** de la línea (`:749`), o si todos sus tokens están en la línea (`:753`).
  - `escala_pagina()` (`:726`), `orig_consolidado` (`:745`), `perimetro_decl` (`:709`) y `orig_pg` (`:774`) se calculan o se definen, pero **no se usan**. Escala y perímetro no se comparan, aunque el docstring y la respuesta dicen que sí.
  - La negación solo se reconoce en redacciones literales (`:705`). En cambio, la afirmación se reconoce por `'reexpresado' in dl` (`:707`), así que «no ha sido reexpresado» cuenta como afirmación.
  - El atajo `nota_no_reexpresion_citada` (`:611`, `:802`) es **nuevo en `8b88fab`**: no existe en `9d676ce` ni en `2c41d68`. Acepta el valor en cualquier parte del texto.
- **R3:** `MILLONES_RE` (`:245`) solo reconoce frases fijas: «millones de euros», «millions of euros», «amounts in millions» y «expressed in millions».
- **R4:** `check_version` hace `re.search(archivo_year, head)` sin límites (`:518`).

## Datos reales

### Reproducción frente a lo publicado

Véase la tabla de ejecución: 59/62 IGUALES y 3 diferencias explicadas.

**Huellas que no coinciden.** `ENTREGA.json` declara como evidencia:
- `COBERTURA_677.csv` → `2d8f98c4…`;
- `verificacion_contexto.jsonl` → `52d6cbda…`;
- `cola_pendientes.json` → `755e208e…`.

Esos valores no son las huellas publicadas ni las reproducidas:
- `COBERTURA_677.csv` → `c71a095e7eadcf976307e15f50bb249de6a29e0b223c2a1cf4186961d73e7621`;
- `verificacion_contexto.jsonl` → `021f068ba034f61a9f6c9ce40236a8bcf47e60a9e1f2b71784bb19078e523014`;
- `cola_pendientes.json` → `345c229a3fcd78dc37425241212e197c0ee0c93ed0da18103c202b912a5a4c8b`.

Las dos primeras huellas declaradas son las de **`160faf9` (v3.4)**. Las de `control_cobertura.json` (`1ac6292d…`) y `control_negativo.json` (`8bd41f48…`) sí coinciden.

### Las 32 entradas de A2-R1 (`s04`)

| Estado en `8b88fab` | n | Comentario |
|---|---:|---|
| PENDIENTE | 22 | columna NO_DECIDIBLE, como pedía A2-R1 |
| CONFLICTO | 7 | no hay contradicción acreditada en ninguna; véase el detalle |
| REVISADO | 3 | `Vidrala Historia!F23`, `Viscofan Historia!F13`, `Viscofan Configuración V6.4!B150` |

Detalle de los 7 CONFLICTO:
- **2 artificiales por el signo:** `aux:capex_int_2017` (`(2,541)`) y `Viscofan Historia!G15` (`−1,800`).
- **5 con un CONFLICTO de reexpresión no acreditado:** `Historia!F25`, `G25`, `H25` e `I25` comparan con una tabla o una frase distinta, por ejemplo «Euros 520,000,000» o el año «2020,». `B49` compara columnas de una tabla de movimiento que no es de años.

Detalle de los 3 REVISADO:
- `F23`: tabla de una sola columna, «(Thousand of Euros) 2019».
- `F13`: posicional.
- **`B150`**: la línea de columnas es la frase «The balances of this heading at 31 December 2024 and 2023 are the following:», el patrón de R1c. Además, la fila se da por OK como «concepto genérico de metadato» porque el concepto contiene «ejercicio».

### Las 19 + 44 de A2-R2 (`s04`)

**19 «no reexpresado» con diferencia** (antes REVISADO):

| Estado en `8b88fab` | n | Comentario |
|---|---:|---|
| REVISADO | 8 | `lyb_c_2017…2024` y `CF2021_p8_var_acreedores_2020`: ahora casan con la fila correcta (p. ej. CF_2017 línea 112, 41,519), por igualdad |
| CONFLICTO | 8 | 7 por el artefacto de signo en la columna (la reexpresión es NO_APLICA o ND); `Historia!H13` por reexpresión |
| PENDIENTE | 3 | `Historia!H8`, `Historia!F21`, `CF2022_p25_var_acreedores_2021` |

- La entrada PENDIENTE de la lista sigue en PENDIENTE.

**44 «solo signo»** (37 REVISADO + 7 M1):
- La reexpresión de 36 + 5 pasa a NO_APLICA por igualdad con signo: el original imprime `(25,544)`, que equivale a −25544.
- **La clase SOLO_SIGNO tiene 0 entradas reales.**
- **33 de las 37 quedan en CONFLICTO, todas por el artefacto de signo en la columna.**

**12 + 2 «sí, reexpresado»:** 11 siguen con OK por diferencia, con razón documental declarada que no he verificado.

**Promociones.** Las dos únicas transiciones PENDIENTE→REVISADO de `cambios_estado_a2_v4.json` son `Viscofan aux:AR2019_p11_derechos_uso_c_2018` (35) y `…_nc_2018` (28). Las dos se deben al atajo nuevo:
- `IA_2018_es.txt` p.37 dice «no reexpresará las cifras comparativas» (plan de transición a la NIIF 16);
- el «28» aparece 30 veces como token en un documento de 321 páginas, y el «35», 46 veces.

### Propagación (`s06`)

**Método.** Para cada uno de los 101 nodos de DERIVADOS.json, comparé el estado de cada operando con su estado real:
- fuente → estado en el CSV;
- derivado → estado de su nodo, de forma transitiva.

**Resultado:**
- **0 derivados REVISADO con algún operando no revisado.**
- 0 nodos del piloto (REUTILIZADO_M1) con operandos en CONFLICTO o PENDIENTE.
- 0 diferencias entre el nodo y el CSV.
- La regla del control coincide con la propagación real en los 87 nodos nuevos.
- Clases de operando: 277 `dato_publicado` y 5 `derivado`. Los 5 operandos derivados son nodos del piloto.

**Límite latente, sin impacto actual.** `derivaciones.py:119` y `control_cobertura.py:183` leen el estado del operando en `verificacion_contexto.jsonl`. Ahí un derivado figura como NO_APLICA, que se trata como revisado.
- Contraejemplo mínimo: un derivado D = f(E), con E un derivado nuevo en PENDIENTE. D quedaría REVISADO y el control daría PASS.
- Hoy no ocurre porque todos los operandos derivados son del piloto.

### Los 133 CONFLICTO (`s05`, `s09`)

**Composición: 133 = 93 fuentes + 40 derivados.**
- Las 93 fuentes se reparten en 71 con conflicto **solo de columna** y 22 **solo de reexpresión**.

**Columna: los 79 CONFLICTO (71 fuentes + 8 M1) son artificiales.** En los 79 casos, la magnitud está en la fila una sola vez, en la posición del año declarado, impresa `(x)` o `−x`.

**Reexpresión: 24 CONFLICTO (22 + 2 M1).**
- **17 tienen un motivo objetivo para no acreditarse:**
  - rótulo distinto: «Cash and cash equivalents» frente a «Net increase/(decrease) in cash and cash equivalents»;
  - frase narrativa;
  - año seguido de coma leído como importe (3 casos: `Vidrala Historia!G25`, `Viscofan Historia!F6`, `Historia!J21`).
- **De los otros 7:**
  - `F25` y `H25` comparan con otra tabla del mismo rótulo «At December 31»;
  - `B46` y `B47` (valor 0, «-») comparan con otra columna de una tabla de movimiento cuyas columnas no son años; la fila del original es idéntica;
  - `J15` y `CF2024_p9_pagos_acciones_2023` son M1.
- Solo `B49` merece revisión humana.

**Contrafactual en memoria (`s09`).** No es una corrección ni acredita nada. Si las 71 fuentes con conflicto solo por el signo tuvieran la columna en OK, quedarían 49 REVISADO y 22 PENDIENTE. El CSV pasaría de 169/209/**133** a 239/243/**29**: **104 de los 133 CONFLICTO dependen únicamente del artefacto de signo.**

**Por tanto, los 133 no son 133 errores económicos, ni 133 contradicciones documentadas.** `ENTREGA.json` y `MAPA_REGENERACION.md` los llaman así («contradicciones documentadas que requieren resolución humana»).

### Otras comprobaciones de datos (`s05`, `s08`)

- **Versión OK solo por un importe:** 0 casos reales.
- **Unidad OK con una forma de millones no reconocida:** 0 casos.
- **Escala del original en la reexpresión por igualdad:** 162 casos, todos «miles»; ninguna contradicción real.
- **Reexpresión por igualdad con rótulo distinto:** 17 de 162, de ellas 12 REVISADO. Ejemplos:
  - `Viscofan Historia!G21`: «Total Equity» frente a «Total equity attributable to owners of parent», el patrón de R2c;
  - `G9`: «Profit (loss)» frente a «Profit or loss for the financial year».
- **«Reexpresión confirmada» con negación:** 8 de 11 contienen «sin» o «no», pero todas empiezan por «sí:», así que las sondas R2a y R2b no tienen impacto real hoy.
- **Atajo «no reexpresado documentado»:** 18 entradas (9 REVISADO, 5 CONFLICTO, 4 PENDIENTE), todas con IA_2018_es p.37 salvo una. Valores 0, 13, 28 y 35 «figuran en el original».
- **Columna OK con cabecera narrativa:** 4 casos (3 REVISADO y 1 M1).

## A2-R5 en detalle

**Recuentos generados: sí, en parte.**
- `generar_recuentos_doc.py` produce `resultados/RECUENTOS_VIGENTES.md` y el bloque con marcadores de `MAPA_REGENERACION.md`.
- Se reproducen salvo la marca de tiempo; los números coinciden con el CSV y con `verificacion_contexto.jsonl`.

**Quedan textos sin generar o desfasados:**
- `HALLAZGOS.md:60` sigue diciendo «reexpresión 199 OK/179 ND/89 NA». Es el mismo desfase que señaló A2, sin marca de histórico corregida. `RESPUESTA_A_D_20261116.md:18,33,62` tampoco cambia.
- `RESUMEN_PARA_CLAUDE.md:20`, sección «Recuentos», todavía vigente, dice «198 REVISADO, 313 PENDIENTE … 0 CONFLICTO_CONTEXTUAL». No tiene sección v4.0.
- En `ENTREGA.json`:
  - «183 fuentes y 46 derivados pendientes»: lo generado da 26 derivados PENDIENTE;
  - «36 SIN_ORIGINAL»: `resoluciones_bloque2.json` da 26;
  - las huellas de evidencia del CSV, la verificación y la cola son de `160faf9`.
- `cola_pendientes.py` declara «46 derivados» en su docstring.

**Motivo de `aux:AR2025_p27_pagos_acciones_2024`.**
- Corregido en `HALLAZGOS.md` §11 y en `RESPUESTA_A2_CIERRE_V2.md`. Lo comprobé: CF_2024 línea 414, `Share-based payment 2,001 2,346`. La entrada es REUTILIZADO_M1 y su reexpresión da OK por igualdad.
- **Sin corregir** en `PUNTO_DE_RECUPERACION.md:101` («no en la misma fila/columna 2024») ni en `RESUMEN_PARA_CLAUDE.md:63`.
- `HALLAZGOS.md:66` mezcla el estado v3.1 (NO_DECIDIBLE) con el v4.0 (OK).

**`COMANDOS.md`: existe** y basta para reproducir.
- No advierte que `cola_pendientes.py` y `resolver_bloque2.py` solo funcionan sin `-I`: dependen de que Python anteponga la carpeta del script a `sys.path`.

**pypdf: no cumple.**
- `asociacion_pdf.py:40` acepta pypdf ≥ 6.0.
- Con pypdf 6.17.0 termina con código 1 y una traza `PdfReadError`, no con un mensaje claro.
- A2 pedía «falla con un mensaje claro si la versión no basta, o funciona con 6.x»; no ocurre ninguna de las dos cosas. Solo está probado con 7.1.0, según el autor.

**Proceso.**
- A2 pedía «un commit por bloque»; hay uno solo para R1–R5.
- Las sondas A2 no se publican como sondas reproducibles.

## Higiene (`s10`)

- **Manifiesto:** `sha256sum -c` → código 0, 62/62 OK; cubre todos los archivos de la carpeta salvo el propio manifiesto.
- **Diff `2c41d68..8b88fab` y `9d676ce..8b88fab`:**
  - 0 archivos fuera de `resultados_m2/cobertura_vm/`;
  - 0 binarios;
  - 0 `.pdf`, `.xlsx`, `.zip`, `.pyc`, `__pycache__` o `.trabajo/`;
  - 0 patrones de secreto;
  - 0 rutas absolutas añadidas.
- **Árbol de `8b88fab`:** 0 PDF, XLSX, ZIP o pyc.
- **`ENTREGA.json` frente a `PLANTILLA_ENTREGA.json`:**
  - no falta ninguna clave; sobra `bloque`, que es inocuo;
  - las 3 pruebas tienen las claves de la plantilla;
  - `es_plantilla=false`, `commit_entrega` según la plantilla, `revision_por_otro_contexto` = PENDIENTE, `apto_dinero_real` = «No se declara»;
  - **defecto de contenido:** huellas y recuentos desfasados (véase A2-R5).

## Defectos que quedan, con su contraejemplo mínimo

1. **R1 · signo impreso** (`verificar_contexto.py:438`). `2025 2024` / `X (10.000) (9.000)`, declarado 2024 = −9000 → CONFLICTO. Impacto: 79 CONFLICTO reales y, por propagación, 104 de los 133 del CSV.
2. **R1 · línea de columnas tomada de una frase o de una cabecera partida** (`:181`, `:213`).
   - `During 2024 and 2025 …` / `Notes 2025 2024` / `Revenue 10.000 9.000`, 2024 = 10.000 → OK.
   - `2025` / `2024` / `Impairment - 1.500`, 2025 = 1.500 → OK.
   - Impacto real: 3 REVISADO con cabecera narrativa (p. ej. `Viscofan Configuración V6.4!B150`).
3. **R1/R4 · el descarte de tokens con forma de año desplaza las posiciones** (`:420`). `2025 2024 Variation` / `Revenue 3.100 2030 1.070`, 2024 = 1.070 → OK.
4. **R2 · fila por subcadena o por subconjunto de tokens** (`:749`, `:753`). 3g; `Total equity …attributable…` frente a `Total equity`. Impacto real: 12 REVISADO con rótulo distinto y CONFLICTO falsos («Cash and cash equivalents»).
5. **R2 · escala y perímetro no comparados** (código muerto en `:709`, `:726`, `:745`, `:774`). 3e, 3f y R2d → NO_APLICA «coherente».
6. **R2 · negación literal**: «no ha sido reexpresado» o «reexpresado: no» + diferencia → OK. Sin impacto real hoy.
7. **R2 · atajo nuevo «no reexpresado documentado»** (`:611`, `:802`): una nota de no reexpresión en el documento + el valor en cualquier parte → NO_APLICA. 18 reales, 9 REVISADO (valores 28 y 35).
8. **R2 · CONFLICTO de reexpresión por columna de un año tomada en tablas cuyas columnas no son años** (`B46`, `B47`).
9. **R3 · formas de millones no reconocidas** (`:245`): «Figures in EUR million» y «(Millones €)» → OK por la cabecera. Sin impacto real.
10. **R4 · versión acreditada por un importe** (`:518`). 1d (`2025,4`) y R4a (`12025`) → OK.
11. **R4 inverso · año seguido de coma leído como importe** («December 31, 2020,»). 3 CONFLICTO reales.
12. **R5 · pypdf 6.x:** traza en lugar de un mensaje claro.
13. **R5 · textos sin generar o desfasados:** `ENTREGA.json` (huellas de `160faf9`, 46 derivados, 36 SIN_ORIGINAL), `RESUMEN_PARA_CLAUDE.md` (0 CONFLICTO), `HALLAZGOS.md:60`, el motivo en `PUNTO_DE_RECUPERACION.md:101`.
14. **Propagación (latente):** un operando derivado se lee como NO_APLICA (`derivaciones.py:119`, `control_cobertura.py:183`).

## Lo que se conserva

- La reproducibilidad: 59/62 byte a byte, y las otras 3 explicadas.
- El control da PASS con código 0. El autocontrol es coherente consigo mismo, pero no detecta ninguno de los defectos anteriores.
- Las 5 sondas de d375d80 siguen en CONFLICTO.
- Sondas que ahora pasan:
  - **A2-R1:** 2a–2e;
  - **A2-R2:** 3c, 3d, 3h, 3j;
  - **A2-R3:** 4a–4c;
  - **A2-R4:** 1b, 1c y el caso C37.
- Propagación sin derivados REVISADO con operandos no revisados.
- Manifiesto y diff limpios.

## Archivos de esta revisión

**Sondas y salidas** en `<rev_A2>/sondas/` (ver `SHA256SUMS.txt`):
- `s00_preparar_copia.py/.out`: copia aislada e insumos.
- `s01_reproducir.sh/.out` y `s01b_cola_resolver.sh/.out`: reproducción y comparación byte a byte.
- `s02_sondas_revisor_A.py/.json/.out` y `s03_sondas_d375d80_A.py/.json/.out`: sondas anteriores sobre el código nuevo.
- `s04_seguimiento_entradas_A2.py/.json/.out`: las 32 y las 19 + 44.
- `s05_auditoria_datos_reales.py/.json/.out`: CONFLICTO, igualdades, atajo, versión, cabecera.
- `s06_propagacion.py/.json/.out`.
- `s07_sondas_nuevas_A2.py/.json/.out`.
- `s08_impacto_sondas_nuevas.py/.json/.out`.
- `s09_contrafactual_signo.py/.json/.out`.
- `s10_higiene.sh/.out`.

Las salidas `.out` y `.json` conservan las rutas originales del entorno, sin sustituir, como en la revisión anterior.

**Copias:**
- `<rev_A2>/entrega` (`8b88fab`, sin modificar);
- `<rev_A2>/repro` (reproducción con los insumos);
- `<rev_A2>/e_2c41d68` y `<rev_A2>/e_9d676ce`.
