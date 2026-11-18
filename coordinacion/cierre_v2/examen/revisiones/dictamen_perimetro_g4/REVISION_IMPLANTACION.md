# Revisión crítica · implantación de P-FOSO (a) y de D1–D3 (`f1/perimetro-foso` @ `688df46`)

**Quién y sobre qué.** Agente independiente (Fable, esfuerzo máximo), autor del dictamen `DICTAMEN.md` de esta carpeta y no del código. 18-nov-2026. Revisé `jluisplagos/munger-v2`, rama `f1/perimetro-foso` (`58be421` el cambio, `688df46` el manifiesto), en un worktree propio: `/home/user/e_work/wt_rev_perimetro`. No modifiqué la rama ni hice commit. `PV` = `munger_v2_r1/personaje_v2`. No ejecuté LibreOffice ni el pipeline. Mis comprobaciones están en `revision_implantacion/` (guiones y `salidas/`, `r0`–`r8`) y trabajan sobre copias fuera de los repositorios.

## 1. Veredicto: CORRECCIONES (pocas y acotadas)

Lo que pedía el dictamen está hecho: las cifras y las reglas se reproducen, y sin perímetro declarado nada cambia. Falla una pieza, y es la que sostiene la decisión: **la serie de intereses de arrendamiento puede pasar por comprobada sin estarlo** (C1). De esa serie depende la referencia mecánica que en Ahold separa «vigilar» de «cumple la regla» (punto 6). Con C1 corregida y las tres frases de C2 aclaradas, el veredicto sería CONFORME CON LÍMITES. C3 es condición para fusionar con `f1/usgaap`.

## 2. Lo que comprobé y sale conforme

- **Cifras.** Con los datos de Ahold y la serie de intereses (337, 356, 382, 422, 465), el módulo `PV/scripts/perimetro_f1.py` da exactamente las de mi réplica: 13,0280 % (capital propio, pagado todo el alquiler), 14,8181 % (sin arrendamientos), 8,7815 % (= `Historia!C55`) y neutro 9,04 % (9,0537 / 9,0402 / 9,0357 por escenario). Diferencia 0 (`salidas/r4_…txt`). Declaré 2022, 2023 y 2024 por la columna comparativa del informe siguiente (AR2023 p. 262, AR2024 p. 321, AR2025 p. 272), no por la que usa su batería: también pasa, con la columna comprobada en los cinco años.
- **Reglas** (gramática nueva sobre copias, `salidas/r1_…txt`):

| Palancas (S2C 3,9/5,4/5,9) | `C18` | Resultado |
|---|---|---|
| ROIC terminal 0,09/0,09/0,09, 0,09/0,09/0,12 o 0,09/0,12/0,12 | No | código 0; G7 ya no salta |
| 0,13/0,15/0,15 (el `fase_b.json` vigente) | No | tres G4 sin justificación posible |
| 0,13/0,15/0,15 | Sí | tres G4 que piden justificación |
| S2C 9,0 en el BUENO (0,318 > 2 × 14,82 %) | No | G7 salta y dice su base |

- **G7, S2C y G4 son coherentes entre sí.** G7 y el tope de la referencia del S2C usan 2 × 14,82 %, que tiene el mismo numerador (NOPAT NIIF 16) y el mismo capital (propio) que la rentabilidad marginal con la que se comparan. G4 no cambia. La referencia BUENO del ROIC terminal es mín(13,03 %, r + 0,03) = 0,12 si los intereses pasan la comprobación, y r = 0,09 si no (`referencias_mecanicas.py`:256–272).
- **Sin perímetro nada cambia.** Ejecuté los guiones de `ab40e80` y los nuevos sobre los 42 expedientes con libro recalculado. En los 40 sin perímetro propio comparé solo lo que cada versión volvió a escribir: 210 archivos (120 de volcado y referencias, 88 de gramática, 2 de la capa F1), con los mismos códigos de salida y la misma consola. Son idénticos byte a byte salvo uno: `motor_a_f1_resultado.json` de Elis (A3) gana la clave `perimetro_f1_valores: null` (`salidas/r2b_…txt`). Alcance: solo Elis ejercita la capa F1 sin perímetro propio; el caso A0 lo cubre la batería.
- **Baterías.** `test_perimetro_foso.py` 39/39. Con tres libros que Git no lleva materializados en mi worktree, `test_motor_a_f1.py` 163/163 y `test_v631_f1.py` 28/28.
- **Sin doble cuenta nueva con NIIF.** La fórmula resta el interés una sola vez, de un EBIT que ya lleva la amortización del derecho de uso, y quita el arrendamiento del capital. No toca flujos ni valor: `f1_libro_v631.py aplicar` ignora la serie nueva (0 celdas distintas) y F1-LIBRO sigue contrastando los 33 flujos.
- **La regla llega a las fases y no decide por ellas.** La sección «1 bis» se vuelca antes de la fase A (`pipeline.py`:740) y otra vez, con la cota A1, antes de la B (:799); la fase C la recibe con `datos_v63.md` (:897). La sección, el prompt de la fase A (`prompts/fase_a.md`:19) y el personaje (:94) dicen que la cifra no decide la celda y que el foso puede seguir en «No». La tabla enseña el peor año (10,67 %). La fase C no puede reescribir `C18`: lo anota y, si duda, no emite conclusión favorable (`prompts/fase_c_turno1.md`:19). Dos reservas: C2 y el punto 5.6.
- **Fusión.** Con `f1/usgaap` (`bcb6dc3`) y `f1/series-escala` (`7be4665`), `git merge-tree` solo da conflictos en el manifiesto (5 y 13 bloques). `motor_a_f1.py` y `verificar_paquete.sh` los tocan las dos ramas y casan sin conflicto de texto. No ejecuté baterías sobre la fusión.

## 3. Correcciones

**C1 · La serie de intereses puede pasar por comprobada sin estarlo (alta).** La serie no está en el libro ni entra en `verificacion_entradas.py` (límite que el implantador declara), así que la comprobación de su fuente es la única barrera. Tiene dos huecos:

- *Sin la etiqueta de la fila, vale cualquier cifra de la página.* Si la serie se declara sin «fila», el producto no puede comprobar que la cifra está en la fila de los intereses ni en la columna del año, y deja la columna «pendiente». El módulo la cuenta igual como comprobada (`perimetro_f1.py`:96 y :149). Probé para 2025 dos cifras equivocadas de AR2025 p. 272: la del año anterior (422) y el «Total rent expense» (57), que no son intereses. En los dos casos la sección dice «comprobados en su fuente (…, PENDIENTE en 5)», la media sale 13,07 % y 13,40 %, y la referencia BUENO del ROIC terminal es 0,12, como con la serie buena (`salidas/r3_…txt` caso B, `salidas/r7_…txt`). Con «fila», el mismo error se detecta. En las series de D&A una columna pendiente no llega lejos, porque la aptitud por entradas sigue en «no» hasta que la comprueba un revisor (`motor_a_f1.py`:1118–1120); aquí no hay nada detrás.
- *Con la fuente inválida, la cifra se sigue enseñando.* Con una cifra que no está en la página, la referencia mecánica no la usa (bien). Pero la sección la titula en negrita con su diferencia frente a r («13.21 % … +4.21 puntos») y lo desmiente en la línea siguiente; «V-F1k (valores)» la da sin aviso; y la capa F1 no bloquea, cuando con las otras series una fuente inválida sí bloquea (`salidas/r5_…md`). El prompt de la fase A pide no apoyar `C18` en una media no comprobada: la defensa queda en que la fase lo lea bien.
- *Corrección.* Dar la serie por utilizable solo con la columna comprobada en los cinco años. Si no lo es, no titular la media ni su diferencia con r, y avisarlo en «V-F1k (valores)». Bloquear como datos inválidos una serie declarada cuya fuente falla, igual que F1-SERIES. *Pruebas que faltan en `test_perimetro_foso.py`:* serie sin «fila»; cifra de otra fila de la misma página; sección con fuente inválida (la prueba de la línea 110 solo cubre la serie ausente).
- El signo y el valor sí están cerrados: un signo cambiado o un valor distinto del literal dejan la medida sin usar (`salidas/r8_…txt`). En Ahold el hueco no cambiaría hoy el resultado, porque la cifra buena ya supera r + 0,03; importa porque la regla vale para cualquier empresa.

**C2 · Tres frases nuevas se pueden leer como «sin foso, nada por encima de r» (baja).** «V-F1k (valores)» dice «G4 limita el ROIC terminal a r + 0,03 y sin foso no admite exceso» (`perimetro_f1.py`:267–268); el prompt de la fase B, «G4 (r + 0,03) solo lo admite con `C18` = Sí» (`prompts/fase_b.md`:34); y el personaje, «r + 3 puntos, solo con foso» (`personaje_munger_v2.md`:94). G4 no salta hasta r + 0,03, con foso o sin él, y la referencia BUENO nueva es 0,12 con `C18` = No: los textos y la referencia tiran en sentidos distintos. *Corrección:* decir lo que hace G4, «por encima de r + 0,03, solo con `C18` = Sí».

**C3 · El módulo no mira la norma contable (antes de fusionar con `f1/usgaap`).** En esta rama US GAAP bloquea en la capa F1, así que hoy no llega a una conclusión. Tras la fusión sí: con arrendamiento operativo el EBIT ya lleva todo el alquiler, y restarle «intereses» lo contaría dos veces. Con `US_GAAP` declarado el bloque sale igual, resta los intereses y habla de «EBIT NIIF 16» (`salidas/r3_…txt`, último caso). *Corrección:* con US GAAP, no emitir la medida hasta que tenga su fórmula, y decirlo.

**C4 · La lectura «¿perímetro cruzado?» confunde medio con marginal (baja).** Compara la palanca con el ancla marginal del perímetro y con `C54`, que es un medio. En Jumbo (ancla 1,70; S2C medio propio 1,19; `C54` 1,11), un NORMAL de 1,2 apoyado en el medio propio sale señalado como «de todo el capital» (`salidas/r6_…txt`). *Corrección:* leer el perímetro comparando medio con medio y dar el ancla marginal aparte.

## 4. D3: ¿basta con INFORMA?

- **Para las palancas, sí: no debe bloquear.** Bloquear por cifras exigiría una frontera que nadie ha decidido (en Ahold sería un S2C NORMAL bajo 4,03) y, con la lectura actual, bloquearía a Jumbo por C4. Convertirlo en desviación con justificación obligatoria sería una regla nueva: decisión de la persona.
- **Debería bloquear un solo caso, que no es de juicio:** la serie de intereses declarada con fuente inválida (C1).
- **Lo que no basta es dónde se ve.** Las filas «(valores)» solo llevan cifras en el paso 12, después de la última fase (en el paso 7 dicen «aún sin palancas»). La fase C no recibe `motor_a_f1_resultado.md` y el informe solo lista las guardas que bloquean (`informe.py`:220–230); la ficha sí las recoge. La fase C tiene las anclas en «1 bis», así que no lo exijo. Recomiendo medirlo también tras el recálculo de la fase B (paso 9) y enseñarlo en el informe.
- **Serie ausente con A1 o A2.** Hoy la sección dice «no calculable» y nada más: la regla de la decisión se queda sin su cifra. No lo bloquearía, pero debería verse en el informe. Si la persona quiere que la regla se aplique siempre, es una decisión suya.

## 5. Límites que faltan por declarar

1. **I+D capitalizada** (`Palancas!C9` = Sí): `C55` pasa a ser la media de la fila 38 y el módulo no lleva ese ajuste. Imprime «8.78 % (Historia!C55 = 7.00 %)» sin avisar.
2. **Historia con menos de diez años:** `desde_datos` devuelve `None` (:188–191). La sección desaparece y G7 vuelve a `C55` sin decirlo.
3. **El semáforo de la fila 42 del libro** (`Diagnóstico V6`, rentabilidad marginal frente a la historia) sigue con 2 × `C55`. Con el S2C en A2 marcará «⚠ REVISAR · cada euro nuevo rendiría 21 %, más del doble de su historia» en el BUENO (0,209 > 2 × 0,0878; lo deduzco de la fórmula, sin recalcular el libro), y el informe lo enseñará mientras la gramática ya no da G7. Es el único semáforo que cruza perímetros: el de la fila 46 compara historia con sector, los dos de todo el capital.
4. **Jumbo también necesita la serie.** `jumbo_d` espera la fase A; con esta rama recibiría «no calculable» y la orden de no comparar `C55` con r.
5. **La decisión nombra A2_propio; el módulo la aplica también a A1_sin_ROU.** Es coherente (mismo trato del arrendamiento), pero es una extensión que conviene que la persona conozca.
6. **El titular favorece un lado.** La sección da en negrita la diferencia con r (+4,03 puntos) y deja sin calcular la de `C55` con el sector (8,78 % frente a 10,08 %: −1,30). El ejemplo del Anexo D (:35) sigue comparando `C55` con r.
7. **El capital propio es capital invertido menos el pasivo por arrendamientos**, no menos el activo. Es la definición del libro, no un error; con el activo, 2023–2025 daría 10,1 / 9,3 / 12,2 % en lugar de 11,5 / 10,7 / 14,0 %. Con capital propio pequeño o negativo la medida pierde sentido.
8. La referencia BUENO usa la medida pagado el alquiler como valor de `B18`, que está en unidades del motor: es prudente cuando cae entre r y r + 0,03. En Ahold da igual (0,12).
9. Menores: con A0 el texto de V-F1g remite a filas «(valores)» que no existen; «ROIC propio 5 años (F18)» en el volcado (`volcar_datos_v63.py`:156) es `C55` y choca con el vocabulario nuevo; `VERSION` no menciona el cambio; el manifiesto regenerado incorpora 701 archivos del examen (Ahold, Jumbo, Elis, Zoetis) que la base tenía en el árbol y no en su manifiesto, además de los 2 nuevos y las 11 huellas cambiadas.

## 6. Efecto en Ahold con esta rama (réplica, `salidas/r7_…txt`)

Con la serie comprobada, las referencias mecánicas del ROIC terminal pasan de 0,09/0,09/0,09 a **0,09/0,09/0,12**. Copiadas tal cual, con el S2C en A2:

| Referencias | Valor MALO / NORMAL / BUENO | Precio de Sí | Ponderado | Zona (precio 36,05 €) |
|---|---|---|---|---|
| Antes: 0,09/0,09/0,09 | 28,41 / 39,71 / 47,55 | 35,99 € | 39,02 € | vigilar |
| Con la rama: 0,09/0,09/0,12 | 28,41 / 39,71 / 49,96 | 36,33 € | 39,50 € | cumple_regla_k |

El margen sobre el precio es de 0,28 € (0,8 %): la zona depende de esa referencia, y la referencia depende de que la serie cuente como comprobada. Por eso C1 es la corrección que importa. El `fase_b.json` vigente deja de valer por G14 (referencia 0,09 ≠ 0,12): hace falta expediente nuevo, como declara el implantador.

## 7. Lo que no comprobé

El recorrido con LibreOffice y con agentes reales; `verificar_paquete.sh completa` entero (el implantador ejecutó `rapida` y varias baterías sueltas; `test_integracion_v64.py` no consta); las baterías sobre la fusión con las otras dos ramas; Excel; el comportamiento real de las fases con los textos nuevos.
