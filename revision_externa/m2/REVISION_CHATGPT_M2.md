# Revisión externa M2 · 16 de noviembre de 2026

Repositorio revisado: `jluisplagos/munger-v2-evidencias-mistral`. No se modifica ni integra el producto de `jluisplagos/munger-v2`.

| Frente | Commit congelado | Dictamen de esta revisión |
|---|---|---|
| A · cobertura | `08c9799e0534e8968b5670060db612941f02ecf9` | Inventario y coincidencia mecánica reproducibles; **revisión contextual solicitada todavía no acreditada**. |
| B · P-M1 | `b5a07e007785f0cd194cb6437fcb5cd7029cb79f` | **Corregir la clasificación de inversiones de Vidrala y la conclusión de D2** antes de utilizar el dossier. |
| C · matemática | `fe46f0761cb0590a280907b42e4605f6d3fec845` | Núcleo aritmético reproducido; **corregir el supuesto hallazgo de D7 por mezclar comparaciones de perímetros diferentes**. |

No corresponde aprobar ahora θ=0 ni declarar P-M1 delimitado. Los problemas señalados son de evidencia e interpretación; no se resuelven pidiendo al inversor que acepte un número sin fundamento.

## Comprobaciones realizadas

- Las huellas y tamaños de los **251 insumos** coinciden con `docs/programa_mistral_m2/entrada/indice_fuentes.json` y la copia local de la base histórica 4.14. Esto no es una nueva verificación del producto completo.
- Manifiestos de A, B y C: **44, 21 y 21 entradas**, respectivamente, todas conformes.
- A: `control_cobertura.py` termina con código 0; concilia 677 filas, 60 del piloto y 617 nuevas. Una ejecución aislada de `verificar_fuentes.py` reproduce las 467 coincidencias mecánicas. La sonda descrita abajo demuestra el límite de ese resultado.
- B: se ejecutaron `extraer_pdfs_viscofan.py`, `tablas_viscofan.py`, `tablas_vidrala.py` y `calculos_pm1.py`, todos con código 0. Las salidas regeneradas coinciden byte a byte con las publicadas. Esto **reproduce también la clasificación incorrecta**, no la valida.
- C: se ejecutaron el autotest del oráculo y los seis scripts restantes de `codigo/`, todos con código 0. Se reprodujeron 56 casos, diez propiedades globales, 192 puntos de sensibilidad y las 24 comparaciones de cobertura. Residuo máximo oráculo/producto: `2.842e-14`.
- Tras regenerar las salidas, los archivos publicados de los tres frentes permanecen iguales byte a byte a sus commits revisados; las ejecuciones fueron sobre copias locales.

## A1 · Coincidencia numérica y revisión contextual son resultados diferentes

En `scripts/verificar_fuentes.py`, el resultado depende de que existan archivo/página/cita/número, cuadre la transformación declarada y coincida el libro. Los campos `concepto`, `columna`, `periodo` y `perimetro` se copian del registro antiguo; no se demuestra su correspondencia con encabezados y notas de la fuente.

Sonda en memoria sobre Vidrala `Análisis!C37`: cambiar esos campos a ejercicio 1900, otra columna, otra empresa y dividendos mantiene `COINCIDE_PROPUESTO`. La cita y el número permanecen intactos. **Esto no prueba que C37 real sea incorrecta**: prueba que el control mecánico no acredita la revisión contextual encargada. `SONDA_A_SEMANTICA.json` conserva el resultado.

Las 123 observaciones agrupan declaraciones del registro; no documentan por sí solas una nueva lectura de encabezado, columna, unidad y perímetro. En derivados, recalcular la fórmula y copiar `uso` como significado tampoco demuestra su adecuación económica o dimensional.

Acción: conservar la cobertura mecánica como trabajo aprovechable, añadir evidencia contextual independiente por tabla/entrada y distinguir explícitamente coincidencia mecánica, verificación contextual y pendientes. Las 60 entradas M1 se reutilizan con su alcance y huellas; no se exige repetirlas sin motivo. Los estados de las dependencias deben llegar al mapa de regeneración.

## B1 · Las nueve altas «PP&E» de Vidrala proceden de la nota de intangibles

`scripts/tablas_vidrala.py`, diccionario `PPE_ADD`, y `VIDRALA_REPOSICION_CAPACIDAD.csv` etiquetan como inmovilizado material los totales de **Intangible Assets** de 2017–2025. Las citas son reales, pero la partida está mal identificada.

Ejemplos reproducibles en los textos conservados:

- **2025:** CF_2025, página PDF 43, nota 7, total de altas al coste de inmovilizado material: **177.848 miles de euros**. La tabla de Mistral utiliza **45.173**, total de altas de intangibles de la nota 8, página PDF 46.
- **2017:** los **156.743** utilizados corresponden a intangibles e incluyen **150.657 de goodwill** en la propia fila. No son inversión en instalaciones productivas.

Las nueve referencias apuntan a la nota de intangibles; revisar la columna completa y sus consecuencias, incluida la discrepancia comparativa de 2023, antes de conservar cualquier conclusión sobre reposición. No basta con cambiar el nombre de una columna si el objetivo era documentar PP&E. No se ha detectado ni afirmado una modificación del libro oficial por este error del auxiliar.

## B2 · θ negativo no identifica θ=0

Los cálculos publicados reproducen θ aproximados de −4,5427, −2,8442 y −1,5198 bajo las tres definiciones propuestas de mantenimiento. Son diagnósticos condicionales fuera del dominio [0,1], no una estimación dentro de él.

`DOSSIER_D2.md` §4 y §6, y su resumen, ofrecen «P-M1 delimitable con θ acotado a 0» si la persona responsable acepta el desglose. Esto contradice la advertencia correcta del propio documento de que truncar no valida cero y de que estructura y familia siguen sin delimitar. **Aceptar una clasificación no convierte una incompatibilidad de definición en identificación.**

Además, aplicar porcentajes del total de inversión publicado a capex de caja más altas ROU requiere justificar el cambio de perímetro; una multiplicación reproducible no acredita esa equivalencia. Mantener ambos cálculos separados y rotular cualquier extrapolación como hipótesis.

Acción: retirar la opción de dar D2 por resuelta con cero, salvo evidencia económica adicional que la justifique expresamente. Se puede presentar una política de prudencia como propuesta humana, con sus límites; no como parámetro identificado ni como cierre del bloqueo económico. Con la evidencia actual revisada aquí **P-M1 sigue sin delimitarse de forma suficiente para liberar el objetivo**.

## C1 · La cifra de D7 sí se reproduce con el perímetro correcto

La base dice expresamente «Viscofan (Caja)». Mistral calcula correctamente el cambio **de la activa NIIF16**, pero lo compara con el cambio de Caja y declara no reproducible una diferencia de 0,0092 €.

| Misma convención Caja en ambos años | Precio de Sí histórico |
|---|---:|
| 4.12 · probabilidades 0,25 / 0,60 / 0,15 | 39,2877008705048 |
| 4.12 · probabilidades de referencia | 40,94819933093843 |
| 4.13 · probabilidades 4.12 | 39,19204962434291 |
| 4.13 · probabilidades de referencia | 40,82634677728604 |

Total Caja: **+1,538645906781241 €**, que redondea a **+1,5386 €**, como D7. Efecto de probabilidades según orden: **+1,6604984604** o **+1,6342971529 €**. Efecto del vector: **−0,1218525537** o **−0,0956512462 €**. La otra comparación NIIF16, **+1,5477811279 €**, también es válida, pero responde a otra pregunta.

Fuentes: los dos `configuracion_v64_variantes.json` de Viscofan en la 4.13, `viscofan/antecedentes/ejecucion_1_4_13` y `viscofan/Viscofan`, variante `perimetro_alternativo`. Detalle y huellas en `SONDA_C_D7_CAJA.json`.

Acción acotada: añadir el caso Caja 4.13 y su tabla 2×2, conservar la comparación NIIF16 con etiqueta correcta y retirar la falsa discrepancia de todos los informes. No hace falta rediseñar el oráculo ni iniciar otra ronda general de matemática.

La llamada directa a la función interna `p_estrella` con probabilidades fuera de contrato no demuestra un fallo de la entrada pública: `calcular` rechaza el caso ensayado. Registrar precondiciones y alcance; no elevarlo a bloqueo de seguridad sin una vía pública reproducible.

## Fuentes nuevas: descargadas y contrastadas; subida pendiente

Se descargaron de nuevo los cuatro PDF de `FUENTES_NUEVAS.csv` con TLS verificado. **Tamaños y SHA-256 coinciden en los cuatro**; ver `FUENTES_DESCARGADAS_REVISION.json`. El HTML oficial ya está conservado en Git.

La Release auxiliar `fuentes-mistral-m2-20261116` existe pero no tiene assets. El intento de esta revisión de subir los PDF y su índice devolvió también **HTTP 401 en uploads.github.com**. No es una discrepancia de bytes ni una decisión económica; sigue pendiente preservar los PDF en una ubicación recuperable, con autenticación que permita ese endpoint. No se sustituyeron ni publicaron bytes bajo nombres existentes. No enviar contraseñas o tokens al chat.

## Continuación delimitada

Las instrucciones completas para cada autor están en `CORRECCION_A.md`, `CORRECCION_B.md` y `CORRECCION_C.md`, en este mismo directorio. Cada sesión mantiene su rama y carpeta. Corregir una vez, regenerar lo afectado, publicar un commit congelado y devolver las respuestas numeradas a estos hallazgos. La siguiente revisión será de los cambios y sus dependencias; no se ordenan ciclos recursivos.

No se aprueban inversiones ni políticas de θ, λ, k o probabilidades. Esta revisión no sustituye la validación económica del producto, la regeneración de expedientes ni el frente F1/Elis de Claude.
