# Dictamen técnico-económico · perímetro de las palancas y G4 (Ahold, F1 con A2_propio)

**Quién y sobre qué.** Agente independiente (Fable, esfuerzo máximo; sesión 8 de `REGISTRO_FABLE.md`), 18-nov-2026; no soy autor de la plantilla, de F1 ni de las fases. Solo lectura de `munger-v2` @ `e6ae912` (`examen/ahold-f1`). `PV` = `munger_v2_r1/personaje_v2`; `EXP` = `PV/empresas_v2_correcciones/2026-11_examen_universo/ahold_f2/Ahold`; celdas de `EXP/recalc/Ahold_v63_evaluada.xlsx` (primera pasada de la fase B). Millones de euros. Las cifras salen de una réplica propia (`replica/`, salidas en `replica/salidas/`) que reproduce los 33 flujos del libro (desviación máxima 4·10⁻¹¹), `precio.json` y las dos cifras de la fase C (35,88 y 37,68 €). No sustituye al recálculo oficial: no ejecuté LibreOffice ni el pipeline.

## 1. Conclusión

1. **G4 no está mal medido y el bloqueo es correcto en el fondo.** G4 no usa `Historia!C55`: compara `Palancas!B18:D18` con `Análisis!C56` + 0,03 (`PV/scripts/comprobar_gramatica.py`:228–239). En el motor A, el ROIC terminal que ni crea ni destruye valor es r·N/(N − f), con N = margen objetivo × (1 − τ). Con la f de A2 de Ahold es 9,04 %, es decir, r, y no depende de con qué capital se mida la historia. Un 0,15 no es «el equivalente de r»: es reinvertir para siempre al 15 % cuando se exige el 9 %, y da un 11,4 % más de valor terminal (+2,23 € por acción en el NORMAL). Con `C18` = No, eso es lo que G4 existe para parar.
2. **El origen es un juicio de las fases, inducido por tres defectos del producto** (§3): las anclas de retorno son de otro perímetro que el motor; nadie dice a las fases el perímetro declarado; y la guarda F1 compara etiquetas, no palancas.
3. **Lo que sí estaba mal en la primera pasada era el S2C** (2,5/3,2/3,5, de todo el capital): cobraba dos veces el local arrendado. Llevarlo a A2 (3,9/5,4/5,9) es lo correcto y vale +1,51 € de precio de Sí. Subir el ROIC terminal a 0,13/0,15/0,15 no corrige un perímetro: cambia la hipótesis.
4. **Ahold** (réplica; precio 36,05 €). Hay dos juegos coherentes: `C18` = No con ROIC terminal entre 0,09 y 0,12, que da un precio de Sí de **35,99–36,94 €** y un ponderado de 39,02–40,35 €; o `C18` = Sí con las palancas vigentes, 37,70 € y 41,24 €. El juego actual, `C18` = No con 0,13/0,15/0,15, no lo es. Para seguir no hace falta ninguna decisión; propongo una, P-FOSO (§3).

## 2. Pregunta 1 · Dónde se mide cada cosa con A2_propio

| Magnitud | Perímetro coherente con el motor | Ahold |
|---|---|---|
| Margen (`B15:D15`, m0) | EBIT NIIF 16: lleva la amortización de derechos de uso. El resto del alquiler (pagos − esa amortización) va en f (V-F1h) | 3,84 %; f = 0,00014 |
| S2C (`B16:D16`) | Ventas nuevas ÷ inversión propia, sin derechos de uso | ancla A1 5,10; medio 4,7–5,4 |
| ROIC terminal (`B18:D18`) | Unidades del motor: N × S2C del terminal. Hipótesis sobre el capital nuevo; se compara con r | neutro 9,04 % |
| ROIC histórico para las palancas (G7, referencias) | NOPAT NIIF 16 ÷ (capital invertido − arrendamientos) | 14,8 %, no 8,8 % |
| ROIC histórico frente a r (foso, `C18`) | (EBIT − intereses de arrendamiento) × (1 − t) ÷ capital propio; o todo el capital frente a su listón mezclado | 13,0 % frente a 9 %; u 8,8 % frente a 6,4 % |
| `C55` tal cual | Solo frente al sector (`Palancas!H18`) | 8,8 % frente a 10,1 % |
| Umbrales | G4: r + 3, sin cambio; solo su holgura pesa distinto (3 puntos sobre el capital propio son 1,8 sobre todo el capital: opción (c) de §3). G7: 2 × el ROIC histórico del perímetro del S2C. G8: sin cambio (sus dos términos ya están en las mismas unidades) | 12 %; 29,6 % y no 17,6 %; 5 puntos |

**Qué EBIT corresponde a A2.** Para medir el retorno del capital propio, el EBIT NIIF 16 menos el interés del arrendamiento, que es restar el alquiler entero una sola vez (EBITDA − pagos − amortización propia): 3.077 en 2025 con el interés publicado y 2.998 con los pagos. Como palanca de margen, el EBIT NIIF 16 sin tocar: restar también ahí el interés lo contaría dos veces.

**Demostración (réplica).**
- *El alquiler entra una vez.* f × ventas = NOPAT 2.403,6 − reinversión propia 79,0 − FCF base 2.312,0 = 12,6 (`Historia!C75:C79`). Los pagos (fila 17, con principal e intereses: AR2025 PDF p. 260) son 1.834 de media: 1.356 van en el margen y 478 en f. f es casi cero porque lo compensan impuestos pagados por debajo de τ × EBIT (−264) y partidas no monetarias (−164). Los 465 de intereses no faltan en el flujo; sí en un «ROIC propio» leído como retorno del accionista, que es 13,0 % y no 14,8 %.
- *Sin doble cuenta y sin omisión.* Arrendatario sintético con las proporciones de Ahold y cuentas explícitas (`04_arrendatario_explicito.py`): descontar su caja del accionista da 349,03, y el motor con la f de A2, el S2C propio y el ROIC terminal en esas unidades, 349,03. Con S2C y ROIC de todo el capital, −10,9 % (el local, dos veces); con A0, −62 %; con f = 0, +16 % (el interés, ninguna).
- *El terminal.* Reinvierte g ÷ ROIC del NOPAT (`v6/docs/Convenciones_financieras_V6_3.md`:24–27): `B18` equivale a un S2C de `B18` ÷ N, 2,86 con 0,09 y 4,77 con 0,15. Con el ROIC neutro, el valor terminal es el de crecimiento cero (41.307,06 por las dos vías). Un 0,09 no cobra el local dos veces: dice que el capital nuevo solo gana r. Con una f que llevara entero el interés, el neutro sería 10–11 %, aún bajo el 12 % de G4.
- *La prueba del foso cruzaba perímetros* (O3). En 2021–2025, Ahold ganó un 8,78 % con todo el capital, cuyo listón coherente es 6,4 % (capital propio al 9 % y arrendamientos a su coste); la hoja trae el coste de capital del sector, 7,4 % (`Sector!M78`), que las fases no reciben. Sobre el capital propio, pagado todo el alquiler, ganó un 13,0 %, frente a r = 9 %. El exceso es de +2,4 o +4,0 puntos según el perímetro; nunca de −0,2.

## 3. Pregunta 2 · Defecto, juicio o decisión

**Juicio de las fases.**
- La fase A apoyó `C18` = No en «8,8 % bajo r» (`EXP/fase_a.json`, Observación de C18): el retorno de un perímetro contra el listón del otro. El texto del personaje lo induce (`PV/personaje_munger_v2.md`:213). Su comparación con el sector sí parece de un mismo perímetro (`Sector!J78` = 3,19, como `C54`).
- La fase C pidió subir el ROIC terminal «como efecto del perímetro», y la fase B lo multiplicó por 1,69 (`EXP/fase_b.json`, `roic_lp` y G4). Pero r no se traduce: ya es el listón del flujo del motor. No hay conflicto entre G4 y F1 (4a), que fija las unidades del ROIC terminal y no su nivel (`ESPECIFICACION_F1_PROPUESTA.md`:80–84, rama `auditoria/economica-f1-frente-e`).

**Defectos del producto y corrección mínima** (con revisión independiente y expediente nuevo):

- **D1 · G7 y las referencias mezclan perímetros.** Comparan una rentabilidad marginal de A2 con 2 × `C55`, de todo el capital, y la referencia BUENO del ROIC usa `C55` (`comprobar_gramatica.py`:143 y :269; `referencias_mecanicas.py`:170, :196 y :249). *Corrección:* con `Historia!C89` ≠ A0, usar el ROIC histórico del perímetro (filas 7, 10, 23 y 32) o decirlo en el hallazgo, como con la V6.4 (:270–273); G4 y G8 no cambian. *Prueba:* casos nuevos en `pruebas/test_v631_f1.py` (A2 entre los dos umbrales: G7 no salta; A0: igual que hoy).
- **D2 · Las fases no reciben el perímetro ni anclas en él.** `datos_v63.md` no vuelca las filas 85–89; sin la PPA de 2021–2022, `C53` queda vacía y la fase B se fue a `C54`. *Corrección:* bloque «perímetro F1» en `volcar_datos_v63.py` (precedente de la V6.4.1 en :106–113) y en `prompts/fase_b.md`: qué miden el S2C y el ROIC terminal, `C54` y `C55` rotuladas «todo el capital», anclas del perímetro (`C53` o la cota A1; retorno propio antes y después del alquiler) y ROIC neutro. *Prueba:* `test_v631_f1.py` (aparece con A2; con A0 la salida no cambia) y `prueba_pipeline_v631.py`, caso P6.
- **D3 · La guarda afirma lo que no ha medido.** V-F1g y V-F1k comparan dos etiquetas de la declaración (`motor_a_f1.py`:634–639): en el paso 7 dicen «palancas S2C en el mismo perímetro» con `palancas: null` (`EXP/motor_a_f1_resultado.md`:27–28), y en el 12 tampoco miran las cifras (`pipeline.py`:797 y :1097). *Corrección:* sin palancas, «declarado; aún sin palancas»; con palancas, una fila INFORMA con el S2C frente al ancla del perímetro y a `C54`, y el ROIC neutro. Sin umbral nuevo; no hace falta mover la guarda. *Prueba:* `pruebas/test_motor_a_f1.py`, bloque «G · V-F1g» (:212–227).

Efecto de las tres en Ahold: ninguno en los valores. G7 BUENO deja de saltar (20,9 % < 29,6 %). G4 sigue bloqueando 0,13/0,15/0,15 con `C18` = No, como hoy: la gramática del producto, sobre una copia con el `fase_b.json` vigente, da código 1 con tres G4 sin justificar (`salidas/06…`).

**Efecto en Ahold** (S2C 3,9/5,4/5,9 salvo la primera fila; p = 0,2/0,6/0,2; k = 3):

| ROIC terminal | MALO / NORMAL / BUENO | Precio de Sí | Ponderado | Zona | Gramática |
|---|---|---|---|---|---|
| Libro: S2C 2,5/3,2/3,5 y 0,08/0,09/0,09 | 28,01 / 37,48 / 44,28 | 34,39 | 36,95 | vigilar | código 0 |
| 0,09/0,09/0,09 (referencia) | 28,41 / 39,71 / 47,55 | 35,99 | 39,02 | vigilar, a 6 céntimos | G8 NORMAL y BUENO y G7 BUENO, justificables |
| 0,09/0,12/0,12 (tope sin foso) | 28,41 / 41,12 / 49,96 | 36,94 | 40,35 | cumple_regla_k | G8 y G7 BUENO, justificables |
| 0,13/0,15/0,15 (vigente) | 28,87 / 41,96 / 51,41 | 37,70 | 41,24 | cumple_regla_k | G4 × 3, sin justificación posible sin foso |

**Para seguir con este expediente** no hay que tocar el producto: al relanzar, el pipeline pide a la fase B la corrección 1 de 2. Con `C18` = No, lo coherente es un ROIC terminal entre 0,09 y 0,12 y explicar el salto del año 11 (G8) como el fin de la ventaja sobre el capital nuevo. Lo que le falta a la fase B es un hecho del motor, no un juicio: el ROIC terminal neutro es 9,04 %.

**Decisión para la persona · P-FOSO: con qué vara se juzga el foso de quien alquila sus locales.** No bloquea el recorrido de Ahold; sí el cierre de O3 y el texto del personaje (`personaje_munger_v2.md`:147 y :213). Decisión anterior: G4 con r + 3 (3-nov-2026); (a) y (b) no la tocan.
- *Qué pasa.* Ahold alquila el 85 % de sus tiendas. La hoja mide su rentabilidad contando como capital también esos locales (8,8 %), y el personaje la compara con tu 9 %, que es lo que pides al dinero del accionista. Pero ese capital lo pone el casero, que cobra un 3–4 %. Con el dinero del accionista, y pagado todo el alquiler, Ahold ganó un 13,0 % en 2021–2025 (10,7 % el peor año).
- **(a) Misma vara en los dos lados (recomendada).** El personaje compara ese 13,0 % con el 9 %, y `C55` solo con el sector. G4 se queda como está. El foso se vuelve a juzgar con esa cifra: si sigue en «No» porque la ventaja no se ve duradera, 35,99–36,94 €; si pasa a «Sí» y dice cuánto dura, hasta 37,70 €.
- **(b) Dejarlo como está** (8,8 % frente a 9 %), declarado como listón de calidad exigente: foso «No»; 35,99–36,94 €. O3 volverá en toda empresa con muchos alquileres.
- **(c) Subir la holgura de G4 con el peso del alquiler** (de 3 a 5,1 puntos en Ahold: los 2–3 puntos de E2, que son sobre todo el capital, llevados al capital propio). Cabría 0,13/0,14/0,14 sin foso: 37,54 €. No la recomiendo: sin foso la referencia es r, da un umbral distinto por empresa y las palancas vigentes (0,15) tampoco pasarían. Admitir el 15 % «por perímetro» sin foso no es una opción: son 6 puntos de más para siempre.
- *Qué me haría estar equivocado.* Que quieras juzgar la calidad como si fueras dueño de los locales: entonces es (b), pero no sirve para decir «no hay retorno en exceso» ni para traducir r a 15 %. Nada de esto valida la tasa (9 % provisional), la f ni la aptitud.

## 4. Pregunta 3 · Jumbo y Elis

No afecta igual. El efecto es proporcional al peso de los arrendamientos en el capital invertido (Historia filas 23 y 32; `salidas/05_jumbo_elis.txt`):
- **Ahold:** 41,3 %; factor 1,70; ROIC 8,8 % → 14,8 %. El signo frente a r cambia.
- **Jumbo** (`jumbo_d/Jumbo`, espera la fase A): 66,4 de 1.106,1 (6,0 %); factor 1,06; ROIC 26,8 % → 28,9 %; umbral de G7 53,6 % → 57,9 %. Tiene `C53` (1,70) y `C18` = Sí heredado: G4 es justificable. Ninguna regla cambia de lado; le alcanzan D2 y D3.
- **Elis** (`elis_f1/Elis`): detenida en el paso 7 por falta de datos (V-F1d y otras); sin palancas, G4 no se evalúa. 703,2 de 7.535,9 (9,3 %); factor 1,10; ROIC 4,7 % → 5,2 %, bajo r en los dos perímetros. Su problema de anclas es otro: fondo de comercio, PPA y R pendiente.

## 5. Límites

- **Lo que más mueve el valor no es esto: es f.** El flujo de partida (2.770) aplica al EBIT de 2025 una f calibrada con la devolución fiscal de 2023 y cargos no monetarios (K3 «+381», `EXP/motor_a_f1_resultado.md`). Sin la devolución, el precio de Sí baja 1,98 €; con la f de 2025 sola, 3,22 €. Esa conciliación del modelo A sigue abierta.
- El «capital propio» usa el pasivo por arrendamientos, no el activo, y no resta la PPA: 5,4 es el extremo alto del S2C medio (4,73 con el activo; AR2025 PDF p. 214). El arrendatario sintético es ficticio. Los listones mezclados dependen de r, que no está decidida.
