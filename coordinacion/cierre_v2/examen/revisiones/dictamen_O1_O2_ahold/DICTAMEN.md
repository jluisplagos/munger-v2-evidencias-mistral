# Dictamen técnico-económico · O1 y O2 de Ahold (examen de Munger V2)

**Quién y sobre qué.** Agente independiente (Fable, esfuerzo máximo; sesión 5 de `REGISTRO_FABLE.md`), 18-nov-2026. No es autor del motor, de la plantilla ni de las objeciones. Solo lectura de `munger-v2` @ `11c31be`. Rutas: `PV` = `munger_v2_r1/personaje_v2`; `EC` = `PV/empresas_v2_correcciones`; `EX` = `EC/2026-11_examen_universo`. Celdas: libro `EX/ahold_f1/Ahold/recalc/Ahold_v63_evaluada.xlsx`. Importes en millones de euros. Los efectos salen de una réplica propia del motor A que reproduce el libro y `precio.json` (diferencias menores de 10⁻¹³); no sustituyen al recálculo oficial. No se ejecutó LibreOffice ni el pipeline.

## 1. Conclusión

1. **O1 no es un defecto de la plantilla ni de la extracción.** Es una decisión escrita en el expediente sobre un vacío del método. Cambiarla es política económica.
2. **O2 sí es un defecto de entrada**, de la fase 1 y de la orquestación. Ninguna decisión eligió 905. Ya pasó en Viscofan, y la persona lo resolvió con D3 y, en Elis, con E6.
3. Efecto en el precio de Sí (27,74 €): O1, de +2,37 a +4,92 €; O2, +0,57 € con el criterio de D3 y E6. Ninguna combinación da un Sí a 36,05 €.

## 2. O1 · qué incluye el flujo del accionista

**Qué dice la documentación.**
- La plantilla define el flujo base solo con restas: «CFO − Capex − intereses y arrendamientos en financiación (IFRS) − SBC» (`Análisis!B52`). No tiene celda para los cobros que la NIIF deja fuera del CFO. No lo cambian la V6.3.1 (`v6/v631_f1/docs/README_V6.3.1_F1.md`:26–27) ni F1 (`EC/2026-11_Vidrala_ensayo_4_15/f1_impl/F1_IMPL.md`:46).
- Ningún documento dice qué hacer con esos cobros. La f (las «fugas») «recoge lo que el FCF base declarado ya absorbe… en la medida en que lo recoja» (`v6/docs/Convenciones_financieras_V6_3.md`:60–65). Hay una regla del inversor del 18-oct-2026, pero solo para los intereses cobrados y solo para no sumar la caja dos veces en `C76` (`PV/personaje_munger_v2.md`:159; `kit_pipeline_munger/CONTEXTO.md`:140). No cubre el caso de Ahold: intereses en inversión y caja que no sobra. La fase 1 no tiene partida para ninguno (`PV/scripts/fase1_historia.py`:38–40).
- La etapa 1 de Ahold lo dejó escrito. `Control maestro!M43`: «Decisión del inversor (28-oct-2026): FCF base con media de 3 años… (… intereses recibidos en inversión)». `M47`: «Cobros por subarriendos (138 en 2025) y dividendos de negocios conjuntos van en inversión: no se suman (sensibilidad)». Las fases y el contradictor no ven esas notas: `datos_v63.md` solo vuelca las columnas F, J, L y N (`PV/scripts/volcar_datos_v63.py`:126).

**Clasificación: (c) decisión documentada del expediente, sobre (d) un vacío del método general.** No es (a), porque la plantilla calcula lo que dice, ni (b), porque la extracción hizo lo definido.

**No afecta igual a todas.** Con US GAAP los intereses cobrados ya están en el flujo: en Zoetis van dentro del CFO (10-K 2025, sin línea en inversión). Con NIIF depende de dónde los presente cada empresa. Ahold, Jumbo y Viscofan presentan los intereses cobrados en inversión (AR2025 PDF p. 216 y 260; Jumbo 2025, PDF p. 155; Viscofan AR_2025, PDF p. 27): quedan fuera. Vidrala los presenta en explotación (CF_2025 PDF p. 7): quedan dentro. En Elis el inversor eligió intereses netos (`EC/2026-11_Vidrala_ensayo_4_15/configuracion/cambio_elis_c48_4_15.json`:378). Por verificar, fuera del repositorio: la NIIF 18 (desde 2027) los llevaría a inversión en todas.

**Cuantía en Ahold** (AR2024 PDF p. 263; AR2025 PDF p. 216; millones; ventana de 3 años del libro):

| Cobro que no se suma | 2023 / 2024 / 2025 | Media | Precio de Sí |
|---|---|---|---|
| Libro (f = 0,003608) | — | — | 27,74 |
| Cobros de subarriendos | 117 / 125 / 138 | 127 | 29,73 (+1,99) |
| Dividendos de negocios conjuntos | 22 / 22 / 28 | 24 | 28,11 (+0,38) |
| Intereses cobrados | 160 / 196 / 130 | 162 | 30,29 (+2,55) |
| Los tres (f = 0,000140) | 938 en total | 313 (15,6 % del flujo base) | 32,66 (+4,92) |

Los +3,00 € «centrales» del contradictor restan además la devolución fiscal belga, que es cuestión de ventana (`N43`).

**Simetría.**
- El motor A no resta deuda ni suma caja: «NO restes deuda aquí, el FCF ya va después de intereses» (`Análisis!E76`). La deuda pesa solo por sus intereses; el espejo de la caja es su rendimiento, no su saldo. Solo habría doble cuenta si además se sumara esa caja en `C76`, que en Ahold es 0 (`fase_b.json`:233). La etapa 1 de Jumbo, que sí suma caja, deja fuera los intereses por eso (`EX/jumbo/Jumbo/etapa1/Jumbo_evaluada.xlsx`, `Control maestro!N40`). El motor B no cambia.
- Los subarriendos son el caso más claro: el alquiler de las tiendas realquiladas está en los 1.944 que se restan y su derecho de uso se dio de baja (AR2025 PDF p. 273). Se cuenta el coste y no su reembolso. Los intereses son la parte más sensible a la ventana: con el nivel de 2025 (130) su efecto es +2,05 €, no +2,55 €.

## 3. O2 · entre cuántas acciones se divide

**Qué dice la documentación.**
- Plantilla: «acciones vigentes en la fecha de valoración (no la media del ejercicio)» (`Control maestro!H181`; `Análisis!E55`). Con fechas separadas más de 90 días solo avisa (`Motor!E228`; aviso A3).
- Decisiones de la persona del 14-nov-2026, D3 (Viscofan) y E6 (Elis): acciones en circulación al cierre de las cuentas; dilución potencial aparte; «no presentarla como una valoración actualizada a 2026 ni aplicar parcialmente la conversión o la recompra» (`EC/2026-11_Vidrala_ensayo_4_14/documentacion_cierre_4_14/DECISIONES_ENTRADAS_4_14.md`:25–30 y :51–52).
- Nadie pide la media del ejercicio. La permite el encargo del agente de metadatos (`PV/prompts/metadatos_fase1.md`:9), y `PV/scripts/rellenar_fase1_v63.py` (:61 y :283) la impone sobre la etapa 1.

**Qué pasó.** La etapa 1 traía 881 (media diluida del 2T de 2026) y anotaba «Base actual ≈867,8 M». La fase 1 puso 905 y sustituyó esa evidencia (`Ahold_v63_datos.xlsx.fase1.registro.json`, `evidencias_sustituidas`). La configuración lo describió (`EX/configuracion/cambio_ahold_f1.json`:15), pero no como un cambio. Ya pasó en Viscofan (`EC/2026-11_Vidrala_ensayo_4_13/fuentes/CONCILIACION_ACCIONES_VISCOFAN_4_13.md`:68–71).

**Clasificación: defecto de entrada de la fase 1 y de la orquestación.** No es de la plantilla, que pide otra cosa y avisa, ni una convención decidida.

**Cifras.** 905 de media diluida de 2025 (AR2025 PDF p. 260): 27,74 €. 886,877 en circulación a 28-dic-2025 (AR2025 PDF p. 244; Q3-26 PDF p. 21), el criterio de D3 y E6: 28,30 € (+0,57). 865,174 a 27-sep-2026 (Q3-26 PDF p. 21), 867,2 con la dilución que estima el contradictor: 28,94 € (+1,21).

- El motor valora a cierre de 2025: descuenta un año entero el flujo de 2026. Dividir por las acciones de septiembre aplica a medias la recompra de 2026 (844, pagados con ese flujo). Llevando el valor a esa fecha y restando lo repartido, el precio de Sí queda en unos 28,6 € (estimación propia).
- **Otras empresas.** Zoetis: 443,8 de media diluida de 2025 (10-K, PDF p. 66), 424,9 al cierre y 413,2 a 31-jul-2026 (10-Q 2T26, PDF p. 5 y 1). El mismo defecto le quitaría entre un 4,5 % y un 7,4 % del valor por acción. Jumbo: sin efecto. Elis: decidido (E6). Vinci y Waste Management no están montadas.

## 4. Corrección mínima, riesgos y pruebas

- **O1.** *Dónde:* en la configuración del cambio, con un expediente nuevo y sin tocar plantilla ni código. `analisis.C48` (intereses pagados − cobrados), `C49` (pagos − cobros de subarriendos) y `C46` (CFO + dividendos), con cálculo declarado y componentes con página y cita, como el C48 de Elis; y `conciliacion_fcf_base` en `motor_a_f1.json` (guarda F1-K3a, `PV/scripts/motor_a_f1.py`:817–853). Como regla general, después: partidas en la fase 1 y filas en la plantilla. *Riesgos:* `C48` y `C49` pasan a llevar cifras netas y la fila 35 deja de coincidir con `C52`; doble cuenta si `C76` > 0; hay que repetir las fases B y C y la auditoría. *Pruebas:* igualdad exacta con el libro actual si los cobros son cero; `fase1_historia.py construir` reproduce 77,000 / 1.707,333 / 6.583,667 con cada cita; F1 con K3a explicada y la f del libro igual a la de la capa; recálculo con 27,84 / 35,55 / 45,14 en la opción (c); revisor distinto para las nueve cifras; `verificar_paquete.sh completa`.
- **O2.** *Dónde:* en la configuración del cambio: `metadatos.acciones_diluidas` (886,877259; 28-dic-2025) y `metadatos.capitalizacion` (31.971,9), como `cambio_decisiones_viscofan_4_14.json`. Aparte y con revisión: `metadatos_fase1.md`:9, y que la fase 1 no sustituya en silencio las acciones de la etapa 1. *Riesgos:* bajos; actualizar `C41` a la vez; la dilución (4 millones: −0,13 €) se declara aparte; `C42`, `C53` y `C54` siguen a 28-jun-2026. *Pruebas:* `cambiar_base.py comprobar`; recálculo con todo por acción × 1,020434 (24,10 / 30,71 / 39,69) y totales sin cambio; `C55` verificada con su página.
- **¿Política económica?** O1, sí: define qué caja es del accionista y toca una decisión registrada. O2: el criterio ya existe (D3 y E6), pero se dio empresa a empresa y pide confirmación.

## 5. Preguntas para la persona responsable

**P-O1 · ¿Cuentan como caja del accionista los cobros que Ahold presenta fuera de la explotación?**
- **Qué pasa.** La hoja resta los intereses que Ahold paga y todos sus alquileres, pero no suma tres cobros: los intereses de su caja (unos 160 millones al año), lo que le pagan los franquiciados por tiendas que Ahold alquila y les realquila (unos 130) y los dividendos de dos negocios compartidos (unos 25). Tu etapa 1 lo anotó: «no se suman (sensibilidad)». En Zoetis y Vidrala ya van dentro; en Elis elegiste intereses netos.
- **(a) Dejarlo así.** 27,74 €, con el límite declarado y la sensibilidad en la ficha.
- **(b) Sumar solo los subarriendos y los dividendos.** 30,11 € (+2,37). Los intereses siguen fuera.
- **(c) Regla espejo, igual para todas.** 32,66 € (+4,92). El flujo se mide igual lo presente la empresa donde lo presente: intereses netos, alquileres netos y dividendos de participadas. Amplía tu regla del 18-oct: si se suma caja en `C76`, sus intereses no entran.
- **Recomendación: (c).** Hoy Ahold se mide con un criterio más exigente que Zoetis o Vidrala, y el reembolso de un alquiler que ya se resta es la idea de F1: el alquiler, una vez. **Lo que me haría estar equivocado:** la parte de intereses depende de la caja y de los tipos de 2023–2025. Si no quieres contar rentas financieras, (b) es el mínimo sin objeción razonable.

**P-O2 · ¿Entre cuántas acciones se divide el valor de Ahold?**
- **Qué pasa.** El libro usa 905 millones, la media de 2025. No la elegiste tú: tu etapa 1 traía 881 y el paso automático la cambió. En Viscofan y Elis decidiste usar las acciones en circulación al cierre de las cuentas y no aplicar a medias las recompras posteriores.
- **(a) Cierre de 2025: 886,9 millones.** 28,30 € (+0,57). Fechas distintas, declaradas.
- **(b) Última cifra publicada: 865,2 millones a 27-sep-2026.** 28,94 € (+1,21) con dilución. Aplica a medias la recompra de 2026; con coherencia serían unos 28,6 €.
- **(c) Dejar 905.** 27,74 €, como límite declarado.
- **Recomendación: (a).** Es tu criterio de D3 y E6 y corrige lo único que es un error claro: dividir por una media de beneficio por acción. **Lo que me haría estar equivocado:** que quieras valorar al día del precio, como en tu etapa 1. Entonces sería (b) para todas, actualizando también caja, deuda y flujos.

**Las dos juntas.** Con las dos recomendaciones, (c) y (a): precio de Sí 33,32 € y ponderado 35,78 €. Con (b) y (a): 30,72 € y 32,99 €. La zona es caro mientras el precio, 36,05 €, supere el ponderado (`PV/scripts/precio_de_si.py`:43–50). Solo cambia a vigilar con O1 (c) y las acciones de septiembre: 34,08 € y 36,59 €.

## 6. Otros casos del mismo tipo (resta sin su espejo)

1. `Análisis!C47` e `Historia` fila 12: capex bruto, sin los cobros por ventas de activos (136 / 250 / 82; unos +2,5 € si se restaran del capex). En Elis el inversor usó el capex neto.
2. `Historia` fila 23, `C32` y `C64`: arrendamientos brutos, sin la inversión neta en subarriendos (704; AR2025 PDF p. 273). Baja el ROIC unos 0,2 puntos.
3. `Historia!C65`: el déficit de pensiones resta y el superávit vale cero. `Diagnóstico V6!C16` (motor B) resta minoritarios y no suma participadas. `Análisis!C50:C51` resta la SBC y no suma los cobros por opciones.
4. Caso inverso (motor A): no hay celda para dividendos a minoritarios ni cupones de híbridos.
