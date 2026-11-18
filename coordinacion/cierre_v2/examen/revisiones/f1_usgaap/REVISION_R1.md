# Revisión crítica independiente · F1 con US GAAP (ASC 842) · ronda 1

- **Revisor:** agente distinto del autor (Claude, modelo Fable 5.2, esfuerzo máximo), 18-nov-2026. No modifiqué la rama ni ningún repositorio. No hice commit.
- **Material:** `jluisplagos/munger-v2`, rama `f1/usgaap` @ `34b68fc` (código y pruebas en `e906b06`; base `1694f08`), worktree `/home/user/e_work/wt_usgaap`. Sigue limpio y en `34b68fc`. Entre `e906b06` y `34b68fc` solo cambian documentos, `VERSION` y el manifiesto (comprobado con `git diff --stat`).
- **Dónde trabajé:** una copia en `/home/user/e_work/revision_usgaap/copia/` (borrada al terminar) y carpetas temporales. LibreOffice siempre con `flock /home/user/e_work/libreoffice.lock`, una ejecución detrás de otra.
- **Evidencia:** carpeta `evidencia/` junto a este informe: mis guiones (`*.py`, `*.sh`) y sus salidas (`*.txt`).
- **Aptitud:** uso supervisado experimental. No apto para decisiones con dinero real. Que pase estas pruebas no lo acredita.

Distingo **hechos** (los reproduje), *interpretaciones* y ***propuestas***.

## Veredicto: CORRECCIONES (acotadas)

**Lo que está bien (hechos).**
- Todas las pruebas declaradas se reproducen con las mismas cifras (§1).
- **NIIF no cambia de valor.** Comparé la base `1694f08` con la entrega en 425 casos NIIF (400 al azar, el libro real de Elis con sus cuatro declaraciones y 21 variantes de la norma del libro): 412 dan el resultado idéntico campo a campo; los 13 que cambian son todos variantes de `Control maestro L4`, que es el cambio que el autor declara (d).
- El diseño es correcto: operativos y financieros por separado, la norma como valor cerrado, y la hipótesis D-US1 con una cota que, con declaraciones veraces, cubre siempre el error (matriz del hallazgo R1-3).
- El libro V6.3.1 real coincide con la capa (13/13) y el pipeline llega a `concluido` condicionado en el caso habitual (PU1; lo repetí como X3).
- El autor documenta sus límites con honradez. Varios de mis hallazgos amplían límites que él ya señala.

**Por qué hacen falta correcciones antes de usarlo con Zoetis y Waste Management.**
1. **Con el motor B la exigencia nueva no se cumple de extremo a extremo** (R1-1): un expediente US GAAP sin declaración F1 llega a `concluido` sin evaluar el puente. La prueba del autor no pasa por el camino real.
2. **Un cero publicado («—») no se puede declarar** (R1-2). Con el 10-K de Zoetis tal como viene, `F1-SERIES` da DATOS INVÁLIDOS.
3. **Hay tres caminos a `concluido` sin condición y con el valor sobrestimado**, con una ubicación falsa y una cita real (R1-3). El autor señala uno (b). Los otros dos son nuevos, y uno de ellos («fila_8» falsa) no lo detecta nada, ni con `fase1_partes`.
4. **El contraste de «no_publicada» con la página se anula con etiquetas normales** y sus patrones no ven rótulos habituales (R1-6).
5. **Arrendamientos financieros** (R1-5): Zoetis termina en `pendiente_de_datos` por 1 millón sobre 1.995, y Waste Management no publica las series que la capa exige.

**Lo que tiene que decidir la persona** (§5): la regla de D-US2 cuando el alquiler va mezclado en las líneas del circulante (caso Nike), y el trato de los arrendamientos financieros que la empresa no desglosa (caso Waste Management).

---

## 1. Pruebas reproducidas

Todo sobre la copia de `34b68fc`. Salidas literales en `evidencia/`.

| Prueba | Declarado | Reproducido |
|---|---|---|
| `test_motor_a_f1_usgaap.py` | 121/121 | **121/121** |
| `mutaciones_usgaap.py` | 38 de 38 | **38 de 38** |
| `prueba_pipeline_usgaap.py` (LibreOffice) | 11/11 | **11/11** |
| `probar_libro_v631_usgaap.py` (libro V6.3.1 real) | 13/13 | **13/13** |
| `test_motor_a_f1.py` (NIIF) | 163/163 | **163/163** |
| `test_v631_f1.py` | 28/28 | **28/28** |
| `probar_v631_f1.py` estructura · a0 · f1 | 21/21 · 22/22 · 35/35 | **21/21 · 22/22 · 35/35** |
| `regresion_elis_f1.py` | 39/39 | **39/39** |
| `prueba_pipeline_f1.py` (gancho) | 7/7 | **7/7** |
| `prueba_pipeline_v631.py` | 9/9 | **9/9** |
| `verificar_paquete.sh rapida` | — | **`RESULTADO GLOBAL: PASA`**, código 0 (con los 50 binarios de Ahold; ver abajo) |
| `verificar_paquete.sh completa` | PASA en `e906b06` (registro del autor) | **no la repetí** (ver abajo) |

**`rapida` y el manifiesto.** En el worktree tal cual, `rapida` da FALLA en el manifiesto: faltan 50 binarios de los expedientes de Ahold (`2026-11_examen_universo/ahold*`), que Git no versiona y que en `wt_usgaap` no están materializados. Están en `wt_examen` con las mismas huellas del manifiesto. Con ellos copiados en la copia limpia: `8061 archivos en el manifiesto · modificados 0 · ausentes 0 · de más 0`, entorno PASA, piloto 35 comprobaciones, comprobadores 114/114 y `RESULTADO GLOBAL: PASA` (`verificar_paquete_rapida_34b68fc_con_binarios.txt`; la salida del worktree tal cual, en `…_worktree_tal_cual.txt`). No es un defecto del código; es un aviso para quien reciba la rama.

**Por qué no repetí `completa`.** La última medida tardó 63 minutos con el cerrojo de LibreOffice tomado, y mientras revisaba había otras sesiones ejecutando pipelines del examen (Ahold y Jumbo) y otra revisión esperando el cerrojo con plazo. El disco estaba al 76–79 % con otras copias en uso. Repetí una a una todas las baterías que tocan lo que cambia esta rama. Lo que no repetí: V6.4 (199), trazabilidad, integridad, auditorías, estados, resumen y cierre. Para esas me apoyo en el registro del autor (`verificacion_completa_e906b06.txt`) y en que después de `e906b06` no cambia código.

**Comprobaciones propias, además de las del autor.**

| Comprobación | Resultado | Evidencia |
|---|---|---|
| Diferencial NIIF, base `1694f08` frente a la entrega, 425 casos | 412 idénticos; 13 distintos, todos por `L4` | `diferencial_niif.txt` |
| Estado F1 (`vigencia`) de los 41 expedientes del árbol con pipeline, con la base y con la entrega | idéntico en los 41 | `vigencia_41_expedientes.txt` |
| Valores de `Control maestro L4` en 844 libros del árbol y 69 del examen | solo `IFRS`, las dos variantes históricas, `US GAAP` y vacío | `escanear_l4.txt` |
| Matriz «dónde están de verdad los tramos» × «qué se declara», 72 pares × 2 | ver R1-3 | `matriz_verdad_declaracion.txt` |
| Casos adversariales sobre la capa | ver hallazgos | `adversarial_capa.txt` |
| Casos adversariales de extremo a extremo, 9 pipelines | ver R1-1 y R1-3 | `adversarial_pipeline.txt`, `xb3_diag.txt` |
| Declaración de Zoetis contra el texto real de su 10-K FY2025 | ver R1-2 y §4 | `zoetis_texto_real.txt` |
| 3.000 declaraciones mal formadas | ninguna «utilizable» con el desglose incompleto; excepciones sin controlar (R1-14) | `fuzz_us.txt` |

---

## 2. Hallazgos, por gravedad

### R1-1 · ALTA · Con el motor B, un expediente US GAAP sin declaración F1 llega a `concluido` sin evaluar el puente

**Qué promete la entrega.** Regla 6 y §5 de `F1_USGAAP.md`: «con el motor B y US GAAP, F1 se exige solo para esto (gancho del pipeline, vigencia y cierre)». Prueba P: «nunca un puente silencioso».

**Hecho** (`xb3_diag.py`, caso XB3). Empresa sintética US GAAP con 50 de pasivo por arrendamiento operativo en la fila 23, motor B, sin `motor_a_f1.json`:

```
estado final: concluido · paso 14 · motor B · registro F1 en el estado: None · ¿existe motor_a_f1_resultado.json?: False
libro recalculado (recalc/, el que recibe el gancho): LibroV63.leer(Control maestro, L4) = '1149' → norma_del_libro = None
                                                      leer_libro (openpyxl) = 'US GAAP' → US_GAAP
Historia L22 = 200 · L23 = 50 · C64 = 250 (lo que resta el puente)
us_gaap_del_expediente(carpeta) = False · exigido_puente(carpeta, libro recalculado) = False · con el libro leído entero: True
vigencia(motor B): exigido False · motivo: el motor no es el A
objeción F1 del cierre a «concluido»: None
```

El puente resta 250 en lugar de 200. La ficha no lleva bloque F1 y el informe no nombra F1.

**Causa.** `us_gaap_del_expediente()` lee `L4` con `LibroV63.leer`, que en una celda de texto compartido devuelve el **índice** del texto (`'1149'`), no el texto. Los libros que recalcula LibreOffice guardan así los textos. El gancho recibe el libro recalculado y `vigencia()` prefiere `recalc/…`. Como no hay excepción, tampoco entra la lectura de reserva con `leer_libro`. El resultado es «no es US GAAP» y F1 no se exige ni en el paso 7, ni en el 12, ni en el 13, ni en el cierre.

**Por qué no lo vieron las pruebas.** Las de `EX` pasan el libro ya leído (`L=`) o usan libros escritos con openpyxl. El autor declara que no ejecutó el recorrido de extremo a extremo con el motor B (límite 7). Con la declaración diciendo `US_GAAP` sí funciona: lo comprobé de extremo a extremo. XB1 termina en `no_entregable · límite del modelo` en el paso 7. XB2 llega al paso 14 con F1 evaluado en el paso 12 y utilizable (su estado final, `pendiente_de_investigacion`, lo causan los agentes simulados del motor B, no F1).

**Mismo fallo en otro caso** (XB4): declaración que dice `NIIF` y libro `US GAAP`, motor B. El gancho tampoco se ejecuta, así que la mezcla de normas no se detecta. (Ese pipeline terminó en el paso 8 por otra causa que no investigué.)

**Efecto en el valor:** infravalora (el alquiler se cuenta en el EBIT y en la deuda). No es un camino de sobrevaloración, pero es justo lo que la guarda nueva tenía que impedir. Afectaría a Waste Management si sale con el motor B y sin declaración.

***Corrección propuesta.*** Leer `L4` con un lector que resuelva los textos compartidos (o con `leer_libro`). Si con el motor B no se puede determinar la norma en un expediente de la 4.15, exigir F1 (fallar en cerrado, como hace el motor A). Añadir la prueba de extremo a extremo con el motor B sin declaración.

Relacionado y de menor gravedad: con `L4` fuera de la lista (p. ej. «U.S. GAAP») y motor B, F1 no se exige; con el motor A el mismo libro bloquea por `F1-NORMA` (`adversarial_capa.txt`, G1 y G2).

---

### R1-2 · ALTA · Un cero publicado no se puede declarar: `F1-SERIES` lo da por inválido

**Hecho** (`zoetis_texto_real.py`, sobre el texto real del 10-K FY2025 de Zoetis, página 89). La nota de arrendamientos imprime `Financing cash flows – finance leases   2   1   —`. La capa exige el principal de los tres años de la ventana. Para 2023:

```
series.pagos_arr_financiero_principal.2023: la cifra '—' no está, como cifra completa, en la página 89      (literal «—»)
series.pagos_arr_financiero_principal.2023: la cifra '0' no está, como cifra completa, en la página 89      (literal «0»)
```

**Causa.** `_literal_valores` admite «—» como cero, pero la búsqueda en la página (`_TOK`) solo reconoce cifras con algún dígito. Un guion nunca se encuentra, y un «0» suelto casi nunca está en un 10-K. Es un mecanismo heredado de F1-IMPL y de la V6.3.1 (el mismo código en la base). Con NIIF apenas se nota; con US GAAP bloquea, porque las series nuevas llevan ceros a menudo.

**Efecto.**
- **Zoetis**: aunque todo lo demás esté bien, `F1-SERIES` da DATOS INVÁLIDOS y el expediente queda en `pendiente_de_datos`. Si se omite 2023, bloquea `F1-US-C49` por serie incompleta. No hay salida honrada.
- **«Importe dentro de la fila» igual a cero.** Tres series no son cifras publicadas sino clasificaciones: `pasivo_arr_operativo` (dentro de la fila 23), `circulante_arr_operativo` (dentro de la fila 14) y `da_rou_operativo` (dentro de la fila 8). El documento pide «0 explícito», pero un cero así no tiene cifra impresa que citar. Con el motor B la serie del pasivo es obligatoria: si la fila 23 no lleva pasivo operativo no se puede declarar el cero, y si lo lleva bloquea `F1-US-PUENTE`. Las pruebas del autor pasan porque su fuente sintética escribe un «0» en la página.

***Corrección propuesta.*** Aceptar el guion («—», «–», «-») como cero publicado cuando está en la fila declarada. Para los importes «dentro de la fila», permitir un cero con motivo y cita (como el `cero` de la fase 1) en lugar de una cifra impresa.

Otros dos resultados del mismo ensayo, que no bloquean:
- La comprobación de la columna queda «pendiente» en las 15 cifras: en el texto real ningún encabezado de ejercicio queda alineado con la cifra.
- La página 70 (el estado de flujos real de Zoetis) se acepta como «sin línea propia del arrendamiento operativo», y las dos citas de existencia se encuentran en la página 88. La vía D-US1 funciona con el texto real.

---

### R1-3 · ALTA · Una ubicación falsa con cita real llega a `concluido`, sin condición y con el valor sobrestimado, por tres caminos

El autor señala el primero (riesgo b). Los otros dos no están en su documento.

**Empresa de referencia del autor:** caja correcta 68; amortización del derecho de uso 10; variación del pasivo 10.

| Camino | Verdad en el libro | Declaración (con cita real) | Flujo | Exceso | ¿Lo detecta algo? |
|---|---|---|---|---|---|
| (i) «fuera» falsa · riesgo (b) del autor | la variación del pasivo está en la fila 14 | los dos tramos «fuera de las filas» | 78 | +14,7 % | solo `F1-US-FILAS`, si hay `fase1_partes` y la etiqueta nombra el arrendamiento |
| (ii) **«fila_8» falsa** · nuevo | la D&A (20) no lleva la amortización del derecho de uso | amortización «fila_8» con `da_rou_operativo` = 10; A2 la excluye de D_X | 78 | +14,7 % | **nada**, ni con `fase1_partes` |
| (iii) **«los dos dentro de la fila 14» falsa** · nuevo | solo la variación del pasivo está en la fila 14 | los dos tramos «fila_14», pagos = coste | 78 | +14,7 % | **nada**, ni con `fase1_partes` |
| (i) + (ii) | pasivo en la fila 14 | «fila_8» y «fuera» | 88 | +29,4 % | como (i) |

En los cuatro, el rótulo es «motor A utilizable para una conclusión», sin condición, y K3b dice «alquiler contado una vez».

**Hechos.**
- **Capa** (`adversarial_capa.txt`, grupos B y C). El caso (i) pasa sin `fase1_partes` (B1), con la línea rotulada «Accrued and other liabilities» (B2), con la etiqueta real de Nike 2025 (B3), con la línea solo en el lado «anterior» (B4) y con el año escrito como texto (B5). El caso (ii) pasa con `fase1_partes`, con la cita genérica «Depreciation and amortization» y con el libro V6.3.1 calculando lo declarado (C1): no saltan `F1-US-FILAS`, `F1-SERIES`, `F1-LIBRO`, `V-F1e` ni K3c.
- **De extremo a extremo** (`adversarial_pipeline.txt`), con el pipeline real, la plantilla V6.3.1 y la auditoría simulada:

| Caso | Estado final | Flujo sin crecimiento | Valor ponderado por acción |
|---|---|---|---|
| X0 · control (tramos de verdad fuera) | concluido | 148,00 | 22,562 |
| X1 · camino (i): 2,5 al año de variación del pasivo dentro de la fila 14 | **concluido**, sin condición | 150,69 | 22,919 (+1,6 %) |
| X2 · camino (ii): 3,0 al año de amortización declarada «fila_8» | **concluido**, sin condición | 151,23 | 22,958 (+1,8 %) |

  El porcentaje es pequeño porque en la empresa sintética el alquiler es pequeño. Es proporcional al peso del alquiler.
- **Matriz completa** (`matriz_verdad_declaracion.txt`): 6 situaciones reales × 12 declaraciones.

| | Utilizables | Con error en el flujo | De ellos, sin condición | Condicionados con el error fuera de la cota |
|---|---|---|---|---|
| Sin `fase1_partes` | 32 de 72 | 13 | 6 | 2 |
| Con `fase1_partes` veraz | 11 de 72 | 3 | 2 | 0 |

  Todos los errores van al alza (+10 o +20). Los dos «fuera de la cota» y los dos que sobreviven a `fase1_partes` llevan siempre una declaración falsa del tipo (ii) o (iii). **Con declaraciones veraces, la cota de D-US1 cubre el error en todos los casos.**

**Por qué `F1-US-FILAS` no basta** (amplía el límite 2 del autor):
1. Sin `fase1_partes` solo informa, y el pipeline sigue (así llegan a `concluido` X0–X3 y el PU1 del autor).
2. Lee el campo `concepto`, que escribe el agente de la fase 1, y `linea`, que en una etiqueta de dos renglones es solo el segundo. Caso real, Nike 2025 (`empresas_v2/Nike/fase1_partes/AR_2025.json`): la línea que lleva «operating lease liabilities» quedó como «Accounts payable, accrued liabilities and other liabilities» / «liabilities and other current and non-current liabilities (426) 397». No la ve.
3. Solo contrasta en un sentido: línea que nombra el arrendamiento y declaración que dice que no hay nada. No comprueba el contrario («declaras fila 8 y ninguna línea de la fila 8 lo nombra»): de ahí el camino (ii).
4. Le basta con que **algún** tramo esté declarado en la fila 14. No mira si la línea es la del activo o la del pasivo: de ahí el camino (iii).
5. Solo mira el lado «actual» y los informes cuyo `anio` es un entero. La Historia toma nueve de los diez años del lado «anterior» del informe siguiente. Si faltan los archivos dice «no contradicen» con cero líneas examinadas.

**Alcance del camino (iii) hoy.** Solo se abre si pagos = coste exactos. Si difieren, `F1-LIBRO` bloquea. Pero si se relaja la regla de D-US2 (R1-4), este camino queda abierto siempre, y entonces hay que cerrarlo antes.

***Corrección propuesta*** (técnica; aplica «donde la empresa publica las líneas, manda el dato»): **quien afirma una ubicación tiene que enseñar la línea, y lo que el programa no pueda contrastar con una línea no debe dar una conclusión sin condición.**
- «fila_8» o «fila_14»: la cita tiene que nombrar el arrendamiento o el derecho de uso, y esa línea tiene que estar entre los componentes de esa fila en `fase1_partes`. Para la fila 14, por tramo: una línea de pasivo para la variación del pasivo y una de activo para la amortización, o una línea que nombre los dos.
- «fuera»: la cita tiene que ser una línea del estado de flujos que nombre el arrendamiento y que **no** esté entre los componentes de las filas 8 y 14. Si no hay tal línea, el tramo es «no_publicada»: hipótesis D-US1, condicionada y con cota.
- Sin `fase1_partes`, o con cero líneas examinadas en los años que usa el modelo: como mínimo, condicionada con la misma cota. No «utilizable» a secas.

---

### R1-4 · ALTA · decisión · La lectura estricta de D-US2 bloquea donde la decisión dice «sin bloquear»

Es el riesgo (a) del autor. Lo juzgo en el §3 y redacto la decisión en el §5. Los hechos:

- **D-US2** dice: «se cuentan los **pagos** y la diferencia queda a la vista en la ficha, **sin bloquear**».
- Con los dos tramos netos dentro de la fila 14 (líneas mixtas), la fila 14 lleva `pagos − coste lineal`. El libro tal cual cuenta el **coste**. Para contar los pagos hay que retirar esa diferencia del circulante, y ningún libro lo hace: `F1-LIBRO` bloquea como límite del modelo.
- **Bloquea con cualquier diferencia** (`adversarial_capa.txt`, grupo D):

| Pagos y coste | Capa (pagos) | Libro (coste) | Diferencia | Resultado |
|---|---|---|---|---|
| 11 y 12 | 69,0 | 68,0 | 1,45 % del flujo | `no_entregable · límite del modelo` |
| 12,001 y 12 | 67,999 | 68,0 | 0,001 % | `no_entregable · límite del modelo` |
| 12 y 12 | 68,0 | 68,0 | 0 | utilizable |

- Además exige pagos y coste de **cinco** años (la ventana y los años del ancla), no solo de la ventana.
- **Nike es este caso.** Sus dos líneas son mixtas (`fase1_partes/AR_2023.json`): «…prepaid expenses, operating lease ROU assets and other current and non-current assets» y «…accounts payable, accrued liabilities, operating lease liabilities and other liabilities».
- **La salida que da el §7 no vale para líneas mixtas.** «Corregir la fila 14 y declarar los tramos fuera» choca con `F1-US-FILAS` (la prueba F del propio autor: «Prepaid expenses, ROU assets and other assets» bloquea). Declarar «los dos dentro con importe 0» choca con R1-2. Y `correcciones_fase1_partes` sustituye un componente por otro con su cifra impresa; no retira una parte de una línea mixta.

---

### R1-5 · ALTA para el examen · Arrendamientos financieros: tolerancia cero y series que las empresas no publican separadas

**Zoetis** (`adversarial_capa.txt`, grupo E; cifras de su 10-K y de su etapa 1). Tiene un arrendamiento financiero de equipos: amortización 1/1/1, principal —/1/2, pasivo 7. La etapa 1 dejó `C49` vacía: «Inmaterial (<0,1 % del FCF): celda vacía (= 0)». FCF base: 1.995.

| Caso | Resultado |
|---|---|
| E1 · `C49` vacía | `pendiente_de_datos`: `F1-C49`, `F1-M-SIM`, `F1-K3b`, `F1-K3a` |
| E2 · `C49` = 0 | `pendiente_de_datos`: `F1-US-C49` (DATOS INVÁLIDOS), `F1-M-SIM`, `F1-K3b`, `F1-K3a` |
| E3 · `C49` = 1,0 y fila 17 = 0/1/2 | utilizable, condicionada (cotas de D-US1: −64 y +64 millones, del orden del 3 % del flujo) |
| E4 · como E3, declarando la verdad (`da_rou` = 0: la D&A de 487 es 330 + 157 y no lleva esa amortización) | bloquea `F1-ROU-HISTORIA` |
| E6 · redondeo: principal 5/6/6 (media 5,667) y `C49` = 5,7 | `F1-US-C49` DATOS INVÁLIDOS: «…restarlos además en C49 los cuenta dos veces» |

*Interpretación.* Zoetis solo pasa si `C49` vale 1,0 y la fila 17 lleva —/1/2. Eso depende de que la fase 1 recoja el principal de la nota (su instrucción lo pide «(principal; IFRS 16) … estado de flujos», y Zoetis no lo tiene en el estado de flujos) y de resolver R1-2. Bloquear por el 0,05 % del FCF base es coherente con que no hay umbral adoptado, pero conviene que la persona lo sepa. El mensaje de E6 es engañoso: es redondeo de la etapa 1, no pagos operativos. La tolerancia (0,005) supone dos decimales; la etapa 1 de Zoetis usa uno y la de Nike, ninguno.

**Waste Management** (10-K 2025, nota 7; `adversarial_capa.txt`, F1). Publica «financing lease expense» 96/73/58, que suma amortización e interés, y «cash paid» 101/90/60 sin separar el principal. Lleva esos pasivos dentro de la deuda (563) y los activos dentro del inmovilizado (568). La capa exige `da_rou` y `pagos_arr_financiero_principal` por año:

```
F1-US-DESGLOSE · INCOMPLETO · series.da_rou sin declarar en [2023, 2024, 2025]
F1-US-C49 · INCOMPLETO · series.pagos_arr_financiero_principal sin declarar en [2023, 2024, 2025]
```

Con el motor A queda en `pendiente_de_datos` y no hay declaración honrada que lo evite. Necesita regla: decisión 2 del §5.

---

### R1-6 · MEDIA · El contraste de «no_publicada» con la página se anula con etiquetas normales, y sus patrones no ven rótulos habituales

**Hecho** (`adversarial_capa.txt`, grupo N). Página con la línea `Operating lease liabilities (10)`, que de verdad está en la fila 14, y los dos tramos declarados «no_publicada»:

| Caso | `F1-SERIES` | Resultado |
|---|---|---|
| N1 · control | DATOS INVÁLIDOS («manda el dato») | bloquea, como debe |
| N2 · la serie `pasivo_arr_operativo` lleva `fila`: «Operating lease liabilities» (la etiqueta del balance) | no salta | **utilizable, condicionada, 78 frente a 68** |
| N3 · la cita de «operativos.existen» es «Operating lease liabilities» | no salta | **utilizable, 78** |

**Causa.** La página se da por limpia si la línea contiene **cualquier** cita o etiqueta `fila` de la declaración. La intención es no señalar la línea del otro tramo ya declarado, pero vale también la etiqueta del balance o la cita de existencia.

**Patrones** (N4). De 14 rótulos habituales en estados de flujos de EE. UU. (los escribí yo; no los saqué de informes concretos), el patrón de la página no ve 10: «Operating lease right-of-use assets», «Reduction in the carrying amount of right-of-use assets», «Amortization of ROU assets», «Lease assets and liabilities, net», «Operating leases, net», «Operating lease asset amortization», «Right-of-use assets», entre otros. El patrón de `fase1_partes` (`_LINEA_ARR`) los ve todos. Una línea que mezcle operativos y financieros se descarta por contener «financ».

***Corrección propuesta.*** Excluir solo las citas de los dos tramos con ubicación declarada, y usar el patrón amplio en la página.

Aquí la conclusión sale condicionada y la cota cubre el error. Lo que falla es «donde la empresa publica las líneas, manda el dato».

---

### R1-7 · MEDIA · Lo que queda «a la vista» por D-US2 mezcla perímetros (caso Waste Management)

**Hecho** (`adversarial_capa.txt`, F2). WM publica «operating lease expense» 427/264/189 (2025/2024/2023), que por su tamaño frente a los pagos incluye más que el coste lineal de los contratos capitalizados (*interpretación:* corto plazo y variable; WM no lo desglosa), y caja pagada por arrendamientos operativos 214/103/77. Con esas cifras la capa muestra:

```
coste lineal medio 293,333, pagos medios 131,333: coste − pagos = +162,000 de media en la ventana
D-US2: se cuentan los pagos. Si se contara el coste lineal, el flujo sin crecimiento cambiaría en −(coste − pagos) a la escala del año base
```

Para WM esa frase no se sostiene: una diferencia del 55 % del coste no es de calendario (un contrato lineal no se aparta tanto de sus pagos); es de perímetro. El gasto que no pasa por el pasivo está en el EBIT y en el CFO por igual. También infla la cota al alza de D-US1, que usa el coste.

***Corrección propuesta.*** Definir `coste_arr_operativo` con el mismo perímetro que los pagos («operating lease cost», sin corto plazo ni variable). Si la empresa no lo separa, declararlo «no comparable» y no calcular la diferencia.

---

### R1-8 · MEDIA · La cota de D-US1 no aparece en el informe

D-US1: «la conclusión se presenta como condicionada, **con la cota de sensibilidad**».

**Hecho** (X3; `X3_salidas/X3_informe.md`, línea 9). El informe dice «utilizable para una conclusión CONDICIONADA … condicionada a la hipótesis D-US1 (no es un dato)…» y no da ninguna cifra de la cota. La cota sí está en `ficha.json` (`motor_a_f1.condicionada.cota`) y en `motor_a_f1_resultado.md`.

***Corrección propuesta.*** Añadir a la línea del informe las dos cifras de la cota: % del flujo sin crecimiento y % del valor presente en el escenario normal.

---

### R1-9 · MEDIA · Motor B: lo que F1 no mira no se avisa, y la línea del informe confunde

- **Ancla de S2C** (`adversarial_capa.txt`, G4). Con la amortización operativa dentro de la D&A (2,5 % de las ventas), `Historia C53` pasa de 2,0 a vacío, y F1 dice «motor B utilizable» sin aviso. El autor lo declara como límite 6. Al menos debería salir un AVISO en el resultado, porque esa ancla es la referencia de la fase B.
- **Informe** (XB2): «Motor B · F1: utilizable…; K3: alquiler contado una vez, **caja base por dos vías sin explicar**; perímetro declarado: **sin declarar**». Con el motor B esas dos cosas no se evalúan; «sin explicar» parece un defecto que no existe.

---

### R1-10 · MEDIA · La salida que el §7 propone para el límite `F1-LIBRO` no está demostrada

El caso «variación del pasivo sola en la fila 14» es frecuente, y el autor lo reconoce. La salida propuesta («corrección registrada: la fila 14 sin esas líneas») no se ha probado. `correcciones_fase1_partes` sustituye un componente por otro; no lo retira. Para líneas mixtas no hay salida (R1-4).

***Propuesta.*** Resolverlo en origen. La instrucción de la fase 1 (`prompts/historia_anio.md`) no está adaptada a US GAAP:
- pide «TODAS las líneas de variación del capital circulante»;
- pide «amortizaciones y depreciaciones»;
- pide el principal y el pasivo «NIIF 16 (solo esos)».

Con US GAAP convendría que las líneas propias del arrendamiento operativo no se sumaran ni en `da` ni en `circulante_lineas` y se anotaran aparte. Así el caso frecuente quedaría «fuera de las filas», lo calcularía la V6.3.1 tal cual y `F1-US-FILAS` lo comprobaría. Es un cambio de especificación de la fase 1, fuera de esta rama. La persona debe conocerlo.

---

### R1-11 · BAJA · (d) La lista cerrada de `L4` se alimenta de un campo de vocabulario abierto

Confirmado lo que declara el autor (`diferencial_niif.txt`): 9 variantes NIIF verosímiles pasan de «utilizable» a `pendiente_de_datos` («IFRS (EU)», «IFRS-EU», «IFRS (UE)», «NIIF-UE», «NIIF (UE)», «IFRS as adopted by the EU», «IAS/IFRS», «IFRS/IAS», «IFRS (IASB)»), además de las dos que H13 quería cerrar. Los expedientes del examen en curso dicen `IFRS` (Ahold, Jumbo) o la variante de Elis: no les afecta.

El riesgo: `L4` lo escribe la fase 1 desde `norma_contable`, que rellena un agente con la instrucción «"IFRS" / "US GAAP" / …» (`prompts/metadatos_fase1.md`), y el bloqueo llega en el paso 7, después de gastar la fase A.

***Propuesta.*** Cerrar el vocabulario en esa instrucción y validarlo en el paso 2 o 3.

### R1-12 · BAJA · NIIF: la ficha gana dos claves nulas

`ficha.py` añade `condicionada` y `us_gaap` al bloque `motor_a_f1` también con NIIF, con valor nulo (`ficha_elis_base_vs_entrega.txt`). El valor no cambia, pero el archivo y su huella sí. Si se regenera la ficha oficial de un expediente NIIF ya cerrado con este código, deja de ser «la ficha registrada al cerrar».

***Propuesta.*** Escribir las dos claves solo con US GAAP. El informe NIIF no cambia (lo comprobé leyendo el código de la línea F1).

El estado F1 de los 41 expedientes del árbol es el mismo con la base y con la entrega (`vigencia()` ejecutada con los dos códigos sobre la copia).

### R1-13 · BAJA · `F1-US-C49`: tolerancia y mensaje

Ver E6 en R1-5. ***Propuesta:*** admitir la diferencia explicada en `conciliacion_fcf_base`, como hace K3a, y no afirmar «pagos operativos» cuando la diferencia es menor que la unidad de redondeo.

### R1-14 · BAJA · Excepción sin controlar con una serie de US GAAP mal formada

**Hecho** (`fuzz_us.txt`): si una serie de US GAAP no es un objeto (texto, número o lista), `_guarda_fuentes_series` lanza `AttributeError` en la línea 1768. En el pipeline sale como «fallo de implementación» en lugar de DATOS INVÁLIDOS. Fueron 326 de 3.000 declaraciones al azar. Otras tres excepciones del mismo tipo (líneas 213, 688 y 726) ya estaban en la base.

### R1-15 · BAJA · (f) K3b repite la declaración; no es una comprobación independiente

En los 13 pares de la matriz que son utilizables y están mal, K3b dice «una vez». El informe lo presenta como comprobación («K3: alquiler contado una vez»). ***Propuesta:*** rotularlo «según lo declarado» y no mostrarlo como conforme cuando `F1-US-FILAS` no ha contrastado líneas.

### R1-16 · BAJA · Con financieros cuya amortización no está en la D&A, declarar la verdad bloquea

Ver E4. La capa supone que la amortización del derecho de uso financiero está siempre dentro de la fila 8, como en NIIF 16. Suele ser así. En Zoetis, 487 = 330 + 157 no deja sitio para ella, aunque es 1 millón.

### R1-17 · BAJA · (g) Citas de ASC 842 y ASC 230

Las contrasté con fuentes secundarias por búsqueda web: resúmenes de Deloitte (Roadmap de arrendamientos §14.2 y de flujos §7.6), BDO, KPMG, CLA y *Journal of Accountancy*. **Son coherentes.** No pude leer el texto literal de la Codificación: `dart.deloitte.com` no está entre los dominios permitidos de esta sesión y la del FASB pide registro. Matices:
- 842-20-45-4 dice «income from continuing operations», no «resultado de explotación». En la práctica es gasto de explotación.
- 842-20-45-5(c) tiene una excepción: los pagos que son coste de poner otro activo en uso van a inversión.
- 842-20-50-4(a) pide separar amortización e interés del coste financiero; WM los da sumados.
- KPMG describe dos presentaciones aceptadas de los dos tramos en la conciliación, en líneas distintas o en la misma. Confirma «lo que la norma no fija».

---

## 3. Juicio de los riesgos (a)–(g) del autor

**(a) Lectura estricta de D-US2. No es una consecuencia de D-US2: contradice su letra.**
D-US2 manda dos cosas, contar los pagos y no bloquear. En un caso concreto (los dos tramos mezclados en la fila 14 y pagos ≠ coste) la hoja actual no puede cumplir las dos. El autor sacrifica «sin bloquear». *Mi lectura:* la persona decidió precisamente que esa diferencia no detuviera un análisis. Bloquear por una milésima, y dejar fuera a Nike, va contra el propósito. Pero la alternativa (publicar el valor de la hoja, que cuenta el coste) sacrifica «contar los pagos». **Ninguna de las dos lecturas la puede elegir el autor ni el revisor: hace falta una decisión nueva** (§5, decisión 1). Como salvaguarda provisional, el bloqueo es seguro, porque no publica ningún valor. El documento debe presentarlo como «pendiente de decisión», no como consecuencia de D-US2.
*Regla que propongo:* no bloquear; publicar el valor de la hoja con la diferencia a la vista, en millones y en % del flujo y del valor, o con un tope si la persona lo quiere. Condición técnica: cerrar antes el camino (iii) de R1-3.

**(b) Ubicación falsa con cita real. Confirmado y ampliado** (R1-3 y R1-6): llega a `concluido` de extremo a extremo; hay dos caminos más («fila_8» falsa y «los dos en la 14» falsa); la detección depende del texto que escribió un agente.

**(c) Motor B con US GAAP. Defecto** (R1-1): la exigencia nueva no funciona sin declaración en el pipeline real. Con declaración `US_GAAP`, gancho, vigencia y cierre se comportan como dice el documento (XB1, XB2). Límites reales: R1-2 (no se puede declarar el pasivo a cero) y R1-9.

**(d) Único cambio NIIF. Confirmado con exactitud** (R1-11). Añado un cambio de formato, no de valor: R1-12.

**(e) Cota de D-US1. Correcta como cota de f:** con declaraciones veraces cubre el error en todos los casos de la matriz. Reparos: usa el coste publicado, que puede incluir corto plazo y variable (R1-7); no cubre el error de otra ubicación mal declarada (R1-3); no sale en el informe (R1-8).

**(f) K3b depende de lo declarado. Confirmado** (R1-15).

**(g) Citas. Coherentes con fuentes secundarias;** texto literal sin contrastar (R1-17).

---

## 4. ¿Sirve para Zoetis y Waste Management tal como vienen sus 10-K?

La fase 1 de las dos no se ha ejecutado. Lo que sigue sale de sus 10-K (texto de `zoetis_t1` y PDF de la Release del examen), de la etapa 1 de Zoetis y de la instrucción de la fase 1. Es una previsión.

**La parte de los arrendamientos operativos sirve.** Ninguna de las dos muestra líneas del arrendamiento en el estado de flujos:
- **Zoetis** (página 70): «Depreciation and amortization expense 487», «Other non-cash adjustments», «Other assets», «Other liabilities». Su D&A (487) es 330 de depreciación más 157 de amortización de intangibles.
- **WM** (página 78): «Depreciation, depletion and amortization 2.863», que es 2.442 más 421 de intangibles, y cinco líneas de circulante sin arrendamientos.

Por tanto, en las dos los tramos son «no_publicada»: hipótesis D-US1, conclusión condicionada. La fase 1 sumaría en las filas 8 y 14 solo líneas que no nombran el arrendamiento, así que `F1-US-FILAS` no saltaría. Es el caso que la V6.3.1 calcula tal cual. Cota en Zoetis (pagos 67/61/57, coste 68/59/56): unos 64 millones en cada sentido, del orden del 3 % del flujo sin crecimiento (calculada con un libro sintético de sus cifras; la exacta saldrá del expediente).

**Lo que las detiene hoy.**

| | Zoetis (motor A, V6.3.1) | Waste Management |
|---|---|---|
| Norma del libro | `US GAAP` en la etapa 1. La fase 1 la reescribe con lo que diga el agente de metadatos: tiene que ser exactamente «US GAAP» (R1-11) | igual |
| Financieros | existen (1 millón). Hace falta `C49` = 1,0 y la fila 17 = —/1/2; la etapa 1 dejó `C49` vacía (R1-5) | existen y son materiales (pasivo 563). La empresa no publica amortización ni principal por separado: `pendiente_de_datos` con el motor A (R1-5) |
| Cero publicado | el principal de 2023 es «—»: `F1-SERIES` lo rechaza (R1-2) | — |
| Fila 23 | la fase 1 pide el pasivo «NIIF 16 (solo esos)». En Nike el agente puso ahí el pasivo operativo. Con el motor A solo informa | con el motor B: si la fila 23 lleva los 1.010 de pasivo operativo, `F1-US-PUENTE` bloquea; si lleva 0, no se puede declarar el cero (R1-2); y sin declaración no se evalúa nada (R1-1) |
| Diferencia coste − pagos | −0,7 de media: correcta | +162 de media: engañosa (R1-7) |
| Textos | los 10-K de 2020 a 2024 son ilegibles con `pdftotext` (pendientes de OCR): las series de 2021 y 2022 para el ancla no se pueden citar todavía | — |

**En una frase:** el tratamiento de los operativos vale para las dos; **Zoetis no concluye hoy** por R1-2 y por `C49`, las dos cosas arreglables sin decisión nueva; **Waste Management no concluye con el motor A** sin la decisión 2, y con el motor B necesita R1-1 y R1-2.

**Qué presentaciones puede concluir hoy la entrega** (con la V6.3.1, A2):

| Cómo presenta la empresa los dos tramos | ¿Concluye? |
|---|---|
| No los muestra (Zoetis, WM) | sí, condicionada (D-US1) |
| Líneas propias fuera de la D&A y del circulante, si la fase 1 no las suma | sí |
| Amortización dentro de la D&A y variación del pasivo sin mostrar | sí, condicionada |
| Variación del pasivo como línea propia del circulante (frecuente) | no: `F1-LIBRO` (R1-10) |
| Los dos mezclados en líneas del circulante (Nike) | no, salvo pagos = coste exactos (R1-4) |
| Amortización en la D&A y variación del pasivo en el circulante | no: `F1-LIBRO` |

---

## 5. Decisiones que tiene que tomar la persona

### Decisión 1 · El alquiler mezclado dentro de las líneas del circulante (caso Nike)

**En llano.** Algunas empresas de EE. UU. no ponen el alquiler en líneas propias de su estado de flujos: lo meten dentro de «otros activos» y «otros pasivos». En ese caso la hoja de cálculo solo sabe contar el coste contable del alquiler, no lo que se pagó. Tu decisión D-US2 dice dos cosas: contar lo pagado y no bloquear. Aquí no se pueden cumplir las dos a la vez con la hoja actual. Hoy el programa bloquea («límite del modelo»), aunque la diferencia sea de céntimos.

| Opción | Qué pasa | Efecto |
|---|---|---|
| **A · No bloquear** | Se publica el valor de la hoja, que cuenta el coste, y al lado se enseña cuánto cambiaría contando los pagos | Nike y similares pueden concluir. El valor se aparta en la diferencia entre pagos y coste: 1,4 % del flujo en el ejemplo de prueba; con las cifras de Zoetis sería del 0,03 %. Puede ir a favor o en contra |
| **B · Bloquear siempre** (lo que hay hoy) | Esas empresas no concluyen hasta tener una hoja nueva | Seguro, pero deja fuera a empresas por diferencias mínimas y va contra el «sin bloquear» |
| **C · Tope** | No bloquea si la diferencia es menor que un tope que tú fijes; bloquea si es mayor | Intermedio; hay que fijar el tope |

**Recomendación del revisor:** A o C. Con cualquiera de las dos, el programa tiene que comprobar antes que el expediente muestra las dos líneas, la del activo y la del pasivo (R1-3, camino iii).
**No cambia** Zoetis ni Waste Management.

### Decisión 2 · Arrendamientos financieros que la empresa no desglosa (caso Waste Management)

**En llano.** Waste Management tiene arrendamientos financieros (pasivo de 563 millones), pero los presenta dentro de su deuda y de su inmovilizado, y no publica por separado cuánto amortiza ni cuánto principal paga. El programa pide esas dos cifras y, sin ellas, deja la empresa en «faltan datos».

| Opción | Qué pasa | Efecto |
|---|---|---|
| **A · Tratarlos como deuda y activos propios**, como hipótesis declarada | No se piden esas cifras; su amortización se queda dentro de la reinversión y sus pagos, dentro de la deuda | WM puede concluir con el motor A. Límite: las altas de esos activos no pasan por el capex. Hay que enseñarlo con su tamaño |
| **B · «Faltan datos»** (lo que hay hoy) | WM no concluye con el motor A | Seguro; el examen pierde ese caso con el motor A |
| **C · Estimar el reparto** con método, rango y revisión | Se declara una estimación, no un dato | Más trabajo; conserva su naturaleza de estimación |

**Relacionado, para Zoetis** (no hace falta decidir si se registra el dato): su arrendamiento financiero es de 1 millón al año sobre una caja de 1.995. Hoy bloquea si `C49` no lleva ese millón. Se arregla registrando `C49` = 1,0. Si prefieres que los importes mínimos no bloqueen, hace falta un tope de materialidad, que es una decisión tuya y hoy no existe.

**Sin decisión nueva** (correcciones técnicas): R1-1, R1-2, R1-3, R1-6, R1-7, R1-8, R1-9 y R1-12 a R1-15. **Para tu información:** R1-10, que propone cambiar la instrucción de la fase 1 para US GAAP. Es especificación de extracción, no política, pero cambia qué entra en las filas 8 y 14.

---

## 6. Lo que no hice, y límites de esta revisión

- No repetí `verificar_paquete.sh completa` (motivo en el §1).
- No ejecuté la fase 1 ni el pipeline con Zoetis o Waste Management reales: el §4 es una previsión.
- No cuantifiqué Nike con sus cifras: su 10-K no está en el árbol.
- No contrasté las citas con el texto literal de la Codificación.
- En XB4 no investigué por qué el pipeline terminó en el paso 8.
- No revisé la plantilla V6.4.1 con US GAAP (límite 5 del autor).
- Todo el recálculo es con LibreOffice; Excel real, sin probar (igual que el autor).

## Anexo · Evidencia

| Archivo | Qué es |
|---|---|
| `ayudas.py` | carga las mismas ayudas de la batería del autor (libros y declaraciones sintéticos) |
| `adversarial_capa.py` → `adversarial_capa.txt` | grupos B, C, D, E (Zoetis), F (WM), N y G (motor B) |
| `matriz_verdad_declaracion.py` → `.txt` | 72 pares verdad × declaración, sin y con `fase1_partes` |
| `adversarial_pipeline.py` → `adversarial_pipeline.txt`, `X3_salidas/` | X0–X3 y XB1–XB3 de extremo a extremo |
| `xb3_diag.py` → `xb3_diag.txt` | causa de R1-1 |
| `zoetis_texto_real.py` → `zoetis_texto_real.txt` | declaración de Zoetis contra el texto real de su 10-K FY2025 |
| `diferencial_niif_worker.py`, `comparar_diferencial.py` → `diferencial_niif.txt` | base `1694f08` frente a la entrega, 425 casos NIIF |
| `fuzz_us.py` → `fuzz_us.txt` | 3.000 declaraciones mal formadas |
| `escanear_l4.py` | valores de `Control maestro L4` en un árbol |
| `ficha_elis_base_vs_entrega.txt` | las dos claves nuevas de la ficha con NIIF (las otras 26 diferencias de ese archivo son de mi árbol parcial de la base, que no pudo ejecutar la verificación de entradas; no son de la entrega) |
| `correr_lo.sh`, `limpiar_copia.py` | reproducción de las pruebas con LibreOffice y limpieza de la copia |
| `test_*.txt`, `mutaciones_usgaap.txt`, `prueba_pipeline_*.txt`, `probar_*.txt`, `regresion_elis_f1.txt`, `verificar_paquete_rapida_*.txt` | salidas de las pruebas del autor reproducidas |
