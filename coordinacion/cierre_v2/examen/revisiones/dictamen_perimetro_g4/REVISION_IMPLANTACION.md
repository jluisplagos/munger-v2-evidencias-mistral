# Revisión crítica · implantación de P-FOSO (a) y de D1–D3 (`f1/perimetro-foso` @ `688df46`)

**Quién y sobre qué.** Agente independiente (Fable, esfuerzo máximo), autor del dictamen `DICTAMEN.md` de esta carpeta y no del código. 18-nov-2026. Revisé `jluisplagos/munger-v2`, rama `f1/perimetro-foso` (`58be421` el cambio, `688df46` el manifiesto; el remoto y la rama local coinciden), en un worktree propio y separado: `/home/user/e_work/wt_rev_perimetro`. No modifiqué la rama ni hice commit. `PV` = `munger_v2_r1/personaje_v2`. No ejecuté LibreOffice ni el pipeline: las pruebas con agentes y con recálculo las tomo de los registros del implantador (`/home/user/e_work/perimetro_foso/`). Mis comprobaciones están en `revision_implantacion/` (guiones `r1`–`r6` y sus salidas); trabajan sobre copias fuera de los repositorios.

## 1. Veredicto: CORRECCIONES (acotadas)

Lo pedido en el dictamen está hecho y reproduce sus cifras y sus reglas. Sin perímetro declarado nada cambia. Pero hay un hueco que toca justo lo que la decisión quería proteger: **una cifra de intereses sin comprobar llega a las fases, y en un caso a las referencias, como si estuviera comprobada** (C1). Con C1 a C3 corregidas sería CONFORME CON LÍMITES.

## 2. Lo que comprobé y sale conforme

- **Cifras.** El módulo `PV/scripts/perimetro_f1.py` da, con los datos de Ahold y la serie de intereses (337, 356, 382, 422, 465), exactamente las de mi réplica: 13,0280 % (capital propio pagado todo el alquiler), 14,8181 % (sin arrendamientos), 8,7815 % (= `Historia!C55`) y neutro 9,04 % (9,0537 / 9,0402 / 9,0357 por escenario). Diferencia 0 (`salidas/r4_…txt`). Declaré la serie por las columnas comparativas (2022 en AR2023 p. 262, 2023 en AR2024 p. 321), distintas de las de su batería, y la comprobación de la columna también pasa.
- **Reglas** (gramática nueva sobre copias, `salidas/r1_…txt`):

| Palancas (S2C 3,9/5,4/5,9) | `C18` | Resultado |
|---|---|---|
| ROIC terminal 0,09/0,09/0,09, 0,09/0,12/0,12 o 0,09/0,09/0,12 | No | código 0; G7 ya no salta |
| 0,13/0,15/0,15 (el `fase_b.json` vigente) | No | tres G4 sin justificación posible |
| 0,13/0,15/0,15 | Sí | tres G4 que piden justificación |
| S2C 9,0 en el BUENO (0,318 > 2 × 14,82 %) | No | G7 salta y dice su base |

- **Sin perímetro nada cambia.** Ejecuté los guiones anteriores (`ab40e80`) y los nuevos sobre los 42 expedientes con libro recalculado. En los 40 sin perímetro propio (V6.3, V6.4, V6.4.1, Elis con A3), las 212 salidas de volcado, referencias y gramática son idénticas byte a byte (`salidas/r2_…txt`). Única diferencia: `motor_a_f1_resultado.json` gana la clave `perimetro_f1_valores: null` (Elis).
- **Baterías.** `test_perimetro_foso.py` 39/39. Con tres binarios materializados en mi worktree, `test_motor_a_f1.py` 163/163 y `test_v631_f1.py` 28/28 (sin ellos, 151/152: la que falla pide el libro real de Elis).
- **Sin doble cuenta nueva con NIIF.** La fórmula resta el interés una vez de un EBIT que ya lleva la amortización del derecho de uso. No toca flujos ni valor. `f1_libro_v631.py aplicar` ignora la serie nueva (0 celdas distintas) y F1-LIBRO sigue contrastando los 33 flujos.
- **La regla llega a las fases y no decide por ellas.** La sección «1 bis» se vuelca antes de la fase A (`pipeline.py`:740) y otra vez, con la cota A1, antes de la B (:799). La sección, el prompt de la fase A y el personaje (:94) dicen que la cifra informa y que el foso puede seguir en «No». La fase C no puede reescribir `C18`.
- **Fusión.** Con `f1/usgaap` y `f1/series-escala` solo hay marcas de conflicto en el manifiesto (comprobado con `git merge-tree`, sin escribir).

## 3. Correcciones

**C1 · Una cifra de intereses sin comprobar llega como cifra (alta).** La serie no está en el libro ni en `verificacion_entradas.py`, así que la comprobación de su fuente es la única barrera.
- *Columna pendiente cuenta como comprobada.* `comprobar_fuentes` da «comprobada» si no hay inválidas ni incompletas (`perimetro_f1.py`:96 y :149). Declaré 2025 sin «fila» y con la cifra de la columna de 2024 de la misma página (422 en lugar de 465): sale «comprobados», utilizable, media 13,07 %, y la referencia BUENO del ROIC terminal pasa de 0,09 a 0,12 (`salidas/r3_…txt`, caso B). Con «fila», el mismo error se detecta (caso C). En D&A de derechos de uso y PPA una columna pendiente la frena la aptitud por entradas; aquí no la frena nada.
- *Una fuente inválida no quita la cifra.* Con (265) en lugar de (465), la sección titula en negrita «13.21 % frente a r 9.00 %: +4.21 puntos» y lo desmiente en la línea siguiente; el hallazgo G4 lleva el número; «V-F1k (valores)» lo da sin aviso; la capa F1 no bloquea (`salidas/r5_…md`). La prueba «no da la media como cifra» solo cubre la serie ausente.
- *Corrección:* utilizable solo con la columna comprobada en los cinco años. Si no lo es, no escribir la cifra en la sección, en G4 ni en V-F1k. Fuente inválida (no ausente): bloquear como DATOS INVÁLIDOS, igual que F1-SERIES. *Prueba:* los casos B y D en `test_perimetro_foso.py`.

**C2 · Dos textos describen mal G4 (media).** «V-F1k (valores)» dice «sin foso no admite exceso» (`perimetro_f1.py`:268) y el prompt de la fase B, «G4 (r + 0,03) solo lo admite con `C18` = Sí» (`prompts/fase_b.md`:34). G4 admite hasta r + 0,03 sin foso, y la propia referencia BUENO nueva es 0,12 con `C18` = No. Tal como están, empujan a la fase B a dejar todo en r. *Corrección:* «por encima de r + 0,03, solo con `C18` = Sí».

**C3 · El módulo no mira la norma contable (antes de fusionar con `f1/usgaap`).** Con US GAAP y arrendamiento operativo, el EBIT ya lleva todo el alquiler: restarle «intereses» lo contaría dos veces. Hoy, con `US_GAAP` declarado, el bloque sale igual, resta los intereses y habla de «EBIT NIIF 16» (`salidas/r3_…txt`, último caso). *Corrección:* con US GAAP, no emitir la medida hasta que tenga su fórmula, y decirlo.

**C4 · La lectura «¿perímetro cruzado?» confunde medio con marginal (baja).** Compara la palanca con el ancla marginal del perímetro y con `C54`, que es un medio. En Jumbo (ancla 1,70; S2C medio propio 1,19; `C54` 1,11), un NORMAL de 1,2 apoyado en el medio propio sale señalado como «de todo el capital» (`salidas/r6_…txt`). *Corrección:* leer el perímetro comparando medio con medio y mostrar el ancla marginal aparte.

## 4. D3: ¿basta con INFORMA?

- **Para las palancas, sí, y no debe bloquear.** Bloquear por cifras exigiría una frontera que nadie ha decidido (en Ahold sería un S2C NORMAL bajo 4,03) y, con la lectura actual, bloquearía a Jumbo por C4.
- **Bloquearía un solo caso, que no es de juicio:** la serie de intereses con fuente inválida (C1).
- **Lo que no basta es el momento.** Las filas «(valores)» solo existen en el paso 12, después de la última fase; el paso 7 dice «aún sin palancas». La fase C no recibe `motor_a_f1_resultado.md` (`pipeline.py`:897) y el informe solo lista las guardas que bloquean (`informe.py`:220–230). Con «1 bis» la fase C ya tiene las anclas, así que no lo exijo; recomiendo medirlo también tras el recálculo de la fase B y enseñarlo en el informe.
- Convertir «S2C más cerca de `C54`» en desviación con justificación obligatoria sería una regla nueva: es decisión de la persona.

## 5. Límites que faltan por declarar

1. **I+D capitalizada** (`Palancas!C9` = Sí): `C55` pasa a ser la media de la fila 38 y el módulo no lleva ese ajuste. Imprime «8.78 % (Historia!C55 = 7.00 %)» sin avisar.
2. **Historia con menos de diez años:** `desde_datos` devuelve `None` (:190). La sección desaparece y G7 vuelve a `C55` sin decirlo.
3. **El semáforo de la fila 42 del libro** sigue con 2 × `C55`: el informe enseñará «⚠ REVISAR… más del doble de su historia» en el BUENO mientras la gramática ya no da G7.
4. **Jumbo también necesita la serie.** `jumbo_d` espera la fase A; con esta rama recibiría «no calculable» y la orden de no comparar `C55` con r.
5. **La aptitud por entradas no ve la serie:** un expediente puede salir apto con la vara del foso fuera del universo verificado.
6. **El capital propio es capital invertido menos el pasivo por arrendamientos**, no menos el activo. Con el activo, 2023–2025 daría 10,1 / 9,3 / 12,2 % en lugar de 11,5 / 10,7 / 14,0 %. La sección no lo dice. Con capital propio pequeño la medida pierde sentido.
7. La referencia BUENO usa la medida pagado el alquiler como valor de `B18`, que está en unidades del motor: es prudente cuando cae entre r y r + 0,03. En Ahold da igual (0,12).
8. Menores: con A0 el texto de V-F1g remite a filas «(valores)» que no existen; «ROIC propio 5 años (F18)» en la sección 4 del volcado es `C55` y choca con el vocabulario nuevo; la sección da la diferencia con r (+4,03) y no la de `C55` con el sector (−1,30); `VERSION` no menciona el cambio.

## 6. Efecto en Ahold con esta rama (réplica)

Con la serie comprobada, las referencias mecánicas del ROIC terminal pasan de 0,09/0,09/0,09 a **0,09/0,09/0,12**. Copiadas tal cual, con el S2C en A2: 28,41 / 39,71 / 49,96; precio de Sí 36,33 €; ponderado 39,50 €; zona cumple_regla_k (antes 35,99 €, 39,02 € y vigilar). El `fase_b.json` vigente deja de valer por G14 (referencia 0,09 ≠ 0,12): hace falta expediente nuevo, como declara el implantador.

## 7. Lo que no comprobé

El recorrido con LibreOffice y con agentes reales; `verificar_paquete.sh completa` entero (el implantador ejecutó `rapida` y varias baterías sueltas; `test_integracion_v64.py` no consta); Excel; el comportamiento real de las fases con los textos nuevos.
