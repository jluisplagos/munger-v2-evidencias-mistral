# vinci_b · revisión independiente y sellado del registro de entradas

Revisor: **Claude revisor sellado**, con fecha **2026-11-20**, la fecha del sistema que exige `sellar`.
- Producto: `examen/expedientes-f1`, commit **9a9e8ab**, sobre 19cec55.
- Solo cambian los bloques `comprobacion` de `vinci_b/Vinci/verificacion_entradas.json`.
- No se tocaron valores, fuentes, huellas ni fases.
- No se ejecutó el pipeline.
- Uso experimental supervisado; no apto para dinero real.

## Resultado de `comprobar`
- Universo: **320 de 326 comprobadas**:
  - cálculo: 222 de 225;
  - juicio: 98 de 101;
  - además, 162 auxiliares.
- Estado: 9 discrepancias, 1 pendiente, 0 desactualizadas, 0 errores.
- **Apto por entradas: NO.**

De las 488 entradas, se sellaron **478**. Todas se examinaron, por ser el primer sellado:
- Las entradas sin cambios de Mistral se contrastaron con `examen/vinci/revision_registro/REVISION.md`.
- Además, se comprobó la columna y el año de las 282 cifras con cabecera de cuadro.

## Entradas no selladas
| Entrada | Resultado | Motivo |
|---|---|---|
| Historia!C86, D86, E86 | discrepancia | La celda vacía es correcta: antes de NIIF 16 no hay derechos de uso. Pero la justificación afirma que en 2019-2020 la nota 4.3 no desglosa la amortización de derechos de uso. Es falso: URD 2020 p. 319 publica 548 y 582, como ya reconocen F86/G86. Es una justificación desfasada. |
| Palancas!A29 | discrepancia | «Región · Western Europe» se aplica a «Europe excluding France» (28.511, URD 2025 p. 369). Esa fila incluye Central and Eastern Europe (3.297; un 4,4 % de las ventas). Los límites solo declaran la aproximación de Asia. Hay que anotar la diferencia, como en Z-R. El peso B29 es correcto. |
| aux p148 board_shares de Lombard, Aguilar, Assouad, Bertocco Trindade y Zingoni | discrepancia | Los valores son correctos (1.016 y 1.000), pero cada cita es la fila de otra consejera (Grégoire Sainte Marie o Messemer). La revisión previa no lo detectó. |
| Análisis!C96 | pendiente | La derivación es correcta: 550.233 ÷ 555.967.094 = 0,000989686. Pero `sellar` la rechaza mientras esos cinco orígenes estén en discrepancia. |

## Puntos de riesgo pedidos: verificados y sellados (salvo Palancas!A29, arriba)
**1. C46 y C40, límite 9.4.1**
- C46: (10.540 + 11.714 + 11.886 − 1.463 − 2.311 − 2.496 + 31 + 41 + 40) ÷ 3 = 9.327,333.
  - «Other 41 31» de URD 2024 p. 348 ocupa la posición de «Dividends received from unconsolidated companies» de URD 2025 p. 370, y su valor de 2024 (41) coincide. Por tanto, 31 es el dividendo de 2023.
  - F1-CIRC: el circulante medio de −2.090 queda fuera de la caja base.
- C40 = 4.132.
  - Arrendamientos: 871 = 761 + 110.
  - SBC: 422/344/265 del estado de cambios en el patrimonio, cada uno en su año.

**2. C38 y C88 (N1)**
- Sello el juicio de materialidad, no el dato.
- C38 solo alimenta C39/D39, C87/D87/E43 y el aviso de Motor E235.
- C88 solo alimenta el rótulo D88, que nunca activa las banderas de B311/C311.
- Las fases A y B no las citan. La fase C dice: «El Fair Value ajeno (111,79) no entra en nada».
- C88 se apoya en una mediana de la etapa 1 sin precios conservados, así que sigue sin ser reproducible.

**3. Serie F1**
- H87 no_aplicable: Cobra IS se adquirió el 31-dic-2021 (URD 2021 p. 150).
- Las series H86:L86 (605/623/668/714/817) e I87:L87 (128/128/108/38) están citadas del URD de su propio año y coinciden con el comparativo del año siguiente.
- C85, C93 y H94:L94 coinciden con `motor_a_f1.json` y con DECISIONES_PARA_EL_USUARIO.md:134–135 (V-CIRC (a) y V-ANCLA (a)).

**4. Datos de mercado**
- C37 = 107,05: comprobado en el XLS de Euronext convertido con LibreOffice bajo flock, fila 2026-10-09.
- C57 = 3,47: WT1010, fila 2026-10-09.
- Palancas!C7 = 48: Damodaran, fila 39, «Engineering/Construction».
- C45 = 46304, que corresponde a 2026-10-09. C46 = 46022, que corresponde a 2025-12-31.

**5. Otras entradas**
- C60: (567,0603 ÷ 570,51)^(1/3) − 1 = −0,00202.
- C28 «Estable»: −0,20 % al año, dentro de la banda de ±0,5 %.
- C31: cobros +2,31 % frente a ingresos +2,14 % (semestral p. 3 y p. 1). El «No» es una decisión declarada del inversor.
- C34: 14.998 ÷ 7.604 = 1,97x.
- Palancas!A28, A30, A31 y A33 coinciden con las zonas impresas. A32 es la aproximación declarada de Asia.

Las 28 hipótesis y 22 convenciones coinciden con el texto vigente de su fase o de `motor_a_f1.json`.
- El sello acredita que el registro es fiel.
- No acredita que el juicio sea correcto.

## Segunda revisión, tras la corrección del extractor (04e86dd y 871b72e)
Revisor: Claude revisor sellado, con fecha 2026-11-20 (fecha del sistema).
- Producto: commit **ed65330**; manifiesto **d7537ae**, con `rapida` en PASA (rc 0, 136 s) sobre una copia limpia.
- Solo cambian los bloques `comprobacion` de las 10 entradas.
- No se ejecutó el pipeline.

Examiné cada corrección en su fuente. Las **10 de 10** están selladas:

| Entrada | Lo que comprobé |
|---|---|
| Historia!C86, D86, E86 | Ya no está la frase falsa. La justificación nueva es correcta: el año es anterior a la NIIF 16 y no hay derechos de uso. La referencia a 548/582 coincide con URD 2020, p. 319. |
| Palancas!A29 | Los límites anotan ahora que «Europe excluding France» (28.511) incluye «Central and Eastern Europe» (3.297, un 4,4 % de 74.599) y «Rest of Europe» (5.732), según URD 2025, p. 369. Es una convención declarada, como en Z-R. |
| Acciones de cinco consejeros (p. 148) | Cada cita es ya la fila literal de su persona (Lombard 1.016; Aguilar, Assouad, Bertocco Trindade y Zingoni 1.000). Están en la página y los valores no cambian. |
| Análisis!C96 | Con sus 12 orígenes ya sellados, la sellé después: 550.233 ÷ 555.967.094 = 0,000989686, igual que el libro. |

**C38.** Su juicio de materialidad ya estaba sellado desde 9a9e8ab y tenía su huella antes de la corrección. `comprobar` lo confirma: `no_materiales_revisados` = [C38] y `no_materiales_sin_revisar` = [].
- C38 es la única celda del universo que no cuenta como comprobada: el dato de terceros no tiene bytes.
- No es material.

**`comprobar` ahora:**
- **325 de 326** del universo (225/225 de cálculo y 100/101 de juicio), más 162 auxiliares.
- 0 pendientes, 0 discrepancias, 0 desactualizadas, 0 errores.
- **Apto por entradas: SÍ.**

Es una condición necesaria, no suficiente. No acredita la aptitud para dinero real.
