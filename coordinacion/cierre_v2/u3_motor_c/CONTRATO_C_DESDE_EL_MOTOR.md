# Contrato del motor C, leído del producto · U3 / F-C1

- **Estado:** propuesta corregida (F2-D3). No ejecutada sobre ninguna entidad real. No es una decisión ni una aprobación.
- **Fuente:** candidata `957af65`, en `<candidata>/munger_v2_r1/`. Las rutas de abajo son relativas a esa carpeta.
  - `B6` = `v6/scripts/V6.1/build_v6.py`: construye la plantilla V6.1.
  - `P62` = `v6/scripts/patch_v62_base.py` y `P63` = `v6/scripts/patch_v63.py`: capas V6.2 y V6.3.
  - `TF` = `v6/scripts/V6.1/test_fill.py`: réplica Python del motor.
  - `REF` = `v6/referencia/referencia_V6.3.json`: fórmulas de la plantilla final, citadas por su clave `Hoja!Celda`.
  - Plantilla: `v6/entregables/Plantilla_V6.3.xlsx`. Su SHA-256 es `8381a6cd…15ac12f` y coincide con `REF.sha256_origen` (comprobado).
- **Método:** lectura estática del código y de las fórmulas de `REF`, más una réplica Python independiente de las fórmulas. No he ejecutado LibreOffice, el pipeline ni ningún recálculo de la hoja.
- **Contraste numérico:** la réplica reproduce los valores de los dos fixtures del motor C (`v6/pruebas/fixtures/LEEME.txt:4-7`), recalculados en su día con LibreOffice:
  - C_orig: B78:D78 = 8,3362525831 / 11,9777149618 / 15,2293638877 y C83 = 11,8997522712;
  - palancas A: C83 = 17,8908417409;
  - coinciden en las 10 cifras publicadas.

Convención de celdas: **X** = B, C o D = MALO, NORMAL o BUENO. «Fila del Motor» = 6, 7 u 8 respectivamente (`B6:980`).

---

## 1. Cuándo se elige el motor C

| Paso | Qué ocurre | Cita |
|---|---|---|
| Elección | La fase A elige `Análisis!C62` = «No · banco o aseguradora». Es una de las cuatro opciones de `Lista_C62`. | `B6:169-170`, `B6:1404`; personaje: `personaje_v2/prompts/fase_a.md:16`, `personaje_v2/personaje_munger_v2.md:274` |
| Traducción | `Diagnóstico V6!C5` = "C" si C62 es «No · banco o aseguradora» o «No · banco, aseguradora o regulada». | `B6:581-582`; `REF["Diagnóstico V6!C5"]` |
| Coherencia | Con `Palancas!C6` = «Financiera (banco o aseguradora)» y motor A o B salen REVISAR (Diagnóstico C6) y la regla V11 = NOA (modelo no aplicable). | `B6:588-590`, `B6:1132-1135`; gramática N7/G18: `personaje_v2/ANEXO_B_gramatica_damodaran.md:30,109` |
| Límite del modelo | Si el personaje juzga que el motor C no captura el negocio (capital regulatorio, cartera, seguros), la salida es `modelo_no_aplicable` (L2) y el juicio cualitativo se conserva. | `personaje_munger_v2.md:196`; `ANEXO_B…:112` |

---

## 2. Entradas que lee el motor C

### 2.1 Historia (DATOS)

Unidad: millones, en la moneda del modelo. El año más reciente va siempre en la columna L (`B6:271-273`). Una celda vacía significa dato desconocido, nunca cero (`P62:8-11`).

| Celda | Significado exacto | Unidad | Uso en el motor C | Cita |
|---|---|---|---|---|
| `Historia!L9` | **Beneficio neto atribuible** del último año: el resultado atribuido a la sociedad dominante. Es después de impuestos y de minoritarios. | mm | Numerador del ROE de partida | `B6:282`; extracción: `personaje_v2/prompts/historia_anio.md:13` |
| `Historia!L21` | **Patrimonio neto atribuible** a la dominante, **al cierre** del último año | mm | B0, la base del motor, y denominador del ROE de partida | `B6:294`; `historia_anio.md:26` |
| `Historia!C9:K9`, `C21:K21` | Las mismas partidas en los años anteriores | mm | Solo anclas: fila 34 (ROE por año), C56 (ROE medio de 5 años) y la referencia mecánica (CAGR del patrimonio a 5 años). **No entran en el valor.** | `B6:328`; `P62:80,357`; `personaje_v2/scripts/referencias_mecanicas.py:108-111,139-144` |
| `Historia!C5:L5` | Años fiscales, consecutivos, con el último en L | año | Control (V04) | `B6:278`, `B6:1108-1111` |
| `Historia!C6:L6` | «Ventas» | mm | **No entra en el cálculo C**, pero bloquea: V02 exige al menos 5 años numéricos (nivel 1, bloquea el valor), V03 exige L6 numérico, V04 los usa para comprobar años consecutivos y C43 = COUNT(C6:L6) condiciona C56. Ver §7.1. | `B6:1091`, `B6:1104-1111`; `REF["Motor!E202"]`, `REF["Motor!C202"]` = TRUE; `REF["Historia!C56"]` |
| `Historia!C5:L26` | Cualquier celda informada tiene que ser numérica | — | V37 (nivel 1) | `B6:1194-1195` |

### 2.2 Series y anclas calculadas (no se escriben)

| Celda | Fórmula | Cita |
|---|---|---|
| `Historia!X34` (ROE del año) | `=IF(AND(ISNUMBER(X9),ISNUMBER(X21),N(X21)>0),X9/X21,"")`: **beneficio neto atribuible ÷ patrimonio atribuible de cierre** | `B6:312,328`; `REF["Historia!L34"]` |
| `Historia!C56` (ROE medio de 5 años) | `=IF(AND($C$43>0,COUNT(H34:L34)=MIN(5,$C$43)),AVERAGE(H34:L34),"")`: media simple, sin años incompletos | `P62:80,357`; `REF["Historia!C56"]` |
| `Historia!C59` (B0) | `=IF(ISNUMBER(L21),L21,"")` | `B6:379` |
| `Historia!C60` (ROE de partida) | `=IF(ISNUMBER(L34),L34,"")` | `B6:380` |
| `Diagnóstico V6!C13`, `C14` | `=Historia!$C$59` y `=Historia!$C$60` | `B6:611-612`; `REF` |

### 2.3 Palancas (HIPÓTESIS por escenario)

| Celda | Significado en el motor C | Unidad | Cómo la usa el motor | Cita |
|---|---|---|---|---|
| `Palancas!X14` | **Crecimiento del patrimonio en los años 1–5.** En los años 6–10 baja en línea recta hasta g∞, al que llega en el año 10. | decimal anual | `Motor!E` → g_t (columnas Q:Z): `IF(t<=5,E,E-(E-H)*(t-5)/5)` | `B6:444-445,926,969`; `REF["Motor!Q7"]`; guía: `P63:245-247` |
| `Palancas!X15` | **ROE objetivo, alcanzado en el año 5.** Sale del ROE de partida (C60), sube en línea recta en 5 años y se mantiene en los años 6–10. | decimal | `Motor!F` → m_t (AK:AT): `D+(F-D)*MIN(t,5)/5` | `B6:446-449,928,970`; `REF["Motor!AK7"]` |
| `Palancas!X16` | S2C: **no se usa en el motor C**. El motor pone 1 y no lo lee en el flujo. La gramática exige dejar B16:D16 **vacías** (G18). | — | `G` = 1 | `B6:450-452,971`; `personaje_v2/scripts/comprobar_gramatica.py:158-161`; `ANEXO_B…:109` |
| `Palancas!X17` | **No es una entrada:** copia `Análisis!X68` | — | — | `B6:453,479-480`; `REF["Palancas!B17"]` |
| `Palancas!X18` | **ROE a largo plazo, tras el año 10.** Solo entra en el terminal. | decimal | `Motor!I` → `BF` | `B6:454-456,973,932` |
| `Palancas!C22`, `C23` | Probabilidad de quiebra en 10 años (vacío = 0 por convención, con aviso) y valor presente de la recuperación | decimal; mm | `BJ = (1-p)·BI + p·rec` | `B6:507-509,936`; `P62:189-195,205-211` |

### 2.4 Análisis (HIPÓTESIS y DATOS de mercado)

| Celda | Significado | Unidad | Uso | Cita |
|---|---|---|---|---|
| `Análisis!X68` | **g∞**, el crecimiento para siempre | decimal; solo valores de lista 0–0,03 | `Motor!H` | `B6:972`; V15: `B6:1142-1145`; lista: `personaje_munger_v2.md:276` |
| `Análisis!C56` | **r**, la rentabilidad exigida. Es la tasa de descuento del motor C. | decimal | `Motor!J` (`DISC`: r operativa solo en B) | `B6:963`; `REF["Motor!J7"]` |
| `Análisis!X69` | Probabilidades de los escenarios | decimal; suman 1 | C83 = media ponderada de B78:D78 | `REF["Análisis!C83"]` |
| `Análisis!C55` | Acciones diluidas vigentes en la fecha de valoración | mm acciones | `Motor!P` → `BK = BJ/P` | `B6:964,937`; `P62:252-254` |
| `Análisis!C37`, `C41` | Precio y capitalización | moneda; mm | **No entran en el valor C.** V06 y V22 bloquean si faltan, y se usan en la lectura del precio y en el DCF inverso. | `B6:1116-1117,1162`; `B6:1417-1418,1484-1493` |
| `Análisis!C76` | Exceso de caja: no se usa en C (ajuste 0); si no es 0, aviso V34 | — | `M` = 0 | `B6:962,1419-1421,1192-1193` |

En el motor C son fijos: t = 0 (`K`, el ROE ya va después de impuestos), f = 0 (`L`) y ajuste = 0 (`M`) (`B6:960-962`). Por tanto **no se restan deuda, minoritarios ni pensiones, ni se suma caja**: el valor es directamente del accionista de la dominante. Por coherencia, B0 tiene que ser patrimonio **atribuible**.

---

## 3. El flujo

Para t = 1…10, en la fila del Motor:

- `L_t = L_{t-1}·(1+g_t)`, con L_0 = B0 = Historia L21 (`B6:927`; `REF["Motor!AA7"]`);
- **`flujo_t = L_{t-1}·m_t − (L_t − L_{t-1})`**, es decir B(t−1)·ROE_t − ΔB_t (`B6:929-930`; `REF["Motor!AU7"]`; réplica: `TF:94-95`);
- VP de los flujos: `BE = Σ flujo_t/(1+r)^t` (`B6:931`).

Lectura económica:
- m_t se aplica al patrimonio de **apertura** B(t−1). B(t−1)·m_t es el beneficio proyectado y ΔB es la retención.
- El flujo es lo que se reparte: dividendos más recompras menos emisiones, **solo si el patrimonio cambia únicamente por beneficio y reparto** (excedente limpio).
- El motor **no proyecta OCI** ni otros movimientos.
- El reparto implícito del año t es 1 − g_t/m_t. **Es un resultado, no una entrada:** no hay ninguna celda de *payout*.

## 4. El terminal

- Flujo del año 11: `BF = L_10·(ROE_lp − g∞)` (`B6:932`; `REF["Motor!BF7"]`; `TF:99-100`). Es B10·ROE_lp − ΔB11, con B11 = B10·(1+g∞).
- Valor terminal: `BG = BF/(r − g∞)` (`B6:933`). Su VP es `BH = BG/(1+r)^10` (`B6:934`).
- Equivale a un múltiplo de valor contable al final del año 10: **(ROE_lp − g∞)/(r − g∞)**.
- Total: `BI = BE + BH + 0`; con la quiebra, `BJ`; por acción, **`BK = BJ / Análisis C55`**. BK alimenta `Análisis!X78`, y el ponderado va a C83 (`B6:935-937`; `REF["Análisis!C78"]`).
- El motor solo calcula si se cumplen las condiciones de `BS` (`B6:919-922`):
  - r > g∞;
  - ROE_lp > 0 y ROE_lp > g∞;
  - B0 > 0;
  - en C no se exige S2C.
  - V16 repite «ROE_lp > g∞» como DATOS INVÁLIDOS (`B6:1146-1148`).
- Valor sin crecimiento: `BL = B0·ROE0/r` (`B6:938`).

## 5. Sensibilidad que ya calcula el producto

- **Filas 12–38 del Motor:** cada escenario con r ±2 puntos y g∞ ±0,5 puntos (`B6:995-1001`). El resultado ponderado va a `Análisis!B90:D92` (`B6:1469-1473`).
- **Tornado del NORMAL, filas 41–52:**
  - crecimiento 1–5 ±2 puntos;
  - ROE objetivo ±2 puntos;
  - S2C ±0,3, **sin efecto en C**;
  - g∞ ±0,5 puntos;
  - ROE_lp ±5 puntos;
  - r ±1 punto.
  - Cita: `B6:1002-1021`. El bloque 11 de Diagnóstico lo resume (`P62:300-324`).
- **DCF inverso, filas 56–136:** usa el precio. Sirve para la lectura del precio, **no para elegir** (`B6:1022-1035,1481-1493`).
- En C no aplican la rentabilidad marginal ni el aviso de salto del año 11 (`P62:216-217,242`).

---

## 6. Puente de patrimonio correcto (control de datos, fuera de la hoja)

El motor lee B y ROE, pero **no comprueba el puente**. El contrato lo exige como conciliación de la Historia, año a año, desde el estado de cambios en el patrimonio, con página y cita:

```
E_t = E_{t-1}
      + beneficio neto atribuible_t          (Historia X9; después de impuestos)
      + OCI atribuible_t                     (otro resultado global, con su signo)
      − dividendos a ordinarias_t            (los dividendos RESTAN)
      − recompras_t (+ amortización de autocartera si aplica)
      + ampliaciones / emisiones de ordinarias_t
      ± instrumentos AT1, si están dentro del patrimonio atribuible (emisión +, amortización −, cupones −)
      ± otros movimientos con nombre (pagos en acciones, cambios de participación sin pérdida de control,
        ajustes de transición NIIF 9/17, hiperinflación…)
```

- La diferencia no explicada tiene que ser ≈ 0. Si no lo es, se declara como hueco, nunca se absorbe en «otros».
- La tolerancia es **una propuesta pendiente de decisión**, sin número.

**Caso numérico** (comprobado con `<scratchpad>/u3_scripts/motor_c_replica.py`, `python3 -I`). Datos: E0 = 1000, beneficio neto atribuible 100, dividendos 40, sin OCI, recompras ni emisiones.

| Concepto | Importe |
|---|---|
| E0 | 1000 |
| + beneficio neto atribuible | +100 |
| − dividendos | −40 |
| **E1** | **1060** |
| ROE de Historia (fila 34) = 100 / 1060 | 9,434 % |
| ROE sobre apertura = 100 / 1000 | 10,000 % |
| Flujo del motor con B(t−1) = 1000, ROE 10 % y B(t) = 1060: 1000·0,10 − 60 | **40 = dividendos** ✓ |

- El puente de 52fb120 («BAI + OCI **+ dividendos** …»), con un impuesto de 30 (BAI 130), da 1000 + 130 + 40 = **1170**: sobran 110 = 30 de impuesto + 2 × 40 de dividendos.
- **Variante con OCI −25 y recompras 10:**
  - E1 = 1000 + 100 − 25 − 40 − 10 = 1025;
  - el «flujo» que implica el motor, beneficio − ΔB = 75, difiere del reparto real (50) en 25 = −OCI;
  - por eso el excedente limpio es una **hipótesis del motor**, y el OCI histórico se declara aparte.

---

## 7. Lo que el motor C NO valida, y observaciones sobre el producto

1. **Solvencia y capital regulatorio** (CET1, ratio de Solvencia II, MREL, colchones). Lo dice `Análisis!E62` (`P62:255-257`; gramática E9: `ANEXO_B…:42`). La hoja no tiene ninguna celda de capital. Que el crecimiento X14 sea compatible con el capital es un juicio que la plantilla no comprueba.
2. **El negocio:** calidad de la cartera, provisiones, margen de servicio contractual (CSM) NIIF 17, reservas y riesgo de tipos. Si el personaje juzga que el motor no lo captura, se aplica L2 (§1).
3. **El puente de patrimonio, el OCI y el excedente limpio** (§6). Ninguna regla de la hoja los comprueba.
4. **AT1 y minoritarios:** el motor no los distingue. Si L21 incluye AT1, o L9 incluye los cupones AT1 o los minoritarios, B0 y ROE0 no son del accionista ordinario (ver §8).
5. **Diferencias de definición en el propio producto.** No se corrigen aquí: son hallazgos de lectura estática.
   - **7.1 «Ventas» bloquea el motor C sin entrar en él.**
     - V02, V03 y V04 y C43 usan `Historia!C6:L6` para todos los motores (`B6:1091,1104-1111`; `REF["Motor!C202"]` = TRUE).
     - La relación de entradas materiales, en cambio, declara `h_ventas` solo para A y B (`v6/scripts/relacion_entradas_materiales.py:77-79`).
     - Para un banco o una aseguradora hay que decidir qué cifra va en la fila 6 (margen bruto, ingresos totales o primas). **Propuesta pendiente de decisión.**
     - Además, la extracción de la fase 1 trata ventas, EBIT, CFO y capex como esenciales (`personaje_v2/scripts/fase1_historia.py:45,578`), y en una financiera no tienen equivalente directo.
   - **7.2 ROE de cierre frente a ROE de apertura.**
     - La Historia mide el ROE sobre el patrimonio de cierre (L9/L21).
     - El motor aplica m_t al patrimonio de apertura.
     - Con patrimonio creciente, ROE0 queda por debajo del ROE sobre apertura: 9,43 % frente a 10 % en el caso de §6.
     - Es una convención del producto. Cambiarla es una **propuesta pendiente de decisión**.
   - **7.3 Crecimiento del patrimonio comparado con el crecimiento de ventas del sector.**
     - En C, `Palancas!G14:I14` siguen siendo cuartiles de crecimiento de **ventas** de Damodaran (`B6:445`).
     - La referencia mecánica acota con ellos el CAGR del **patrimonio** (`referencias_mecanicas.py:108-117`).
     - El semáforo de crecimiento usa el Q3 de ventas (`B6:681-686`).
     - Son magnitudes distintas. Queda anotado; no se cambia.

## 8. Propuestas pendientes de decisión (sin números)

| # | Propuesta | Por qué hace falta | Quién decide |
|---|---|---|---|
| PD-1 | **Guarda de capital regulatorio:** un control que compare el crecimiento X14 y el reparto implícito con la generación de capital publicada (Pilar 3 o SFCR). Sería un AVISO, no un cálculo de valor. | El motor no valida el capital (E62). | Persona responsable. Ni la definición ni ningún umbral están fijados. |
| PD-2 | **Base de valor distinta del motor** (múltiplos de valor contable, valor liquidativo o *embedded value*) | El motor C es un flujo al accionista con terminal de Gordon sobre B10 (§3–4). Otra base sería **otro método**, no una variante. | Persona responsable. Por defecto, la del motor. |
| PD-3 | **Tratamiento de AT1:** (a) el patrimonio «atribuible a la dominante» tal como se publica, o (b) solo ordinarias, excluyendo los AT1 de L21 y restando sus cupones de L9 | Cambia B0, ROE0 y el valor por acción | Persona responsable |
| PD-4 | **Qué va en «Ventas» (Historia fila 6)** para un banco o una aseguradora (§7.1) | Sin la fila 6, V02 bloquea el valor | Persona responsable |
| PD-5 | **Tolerancia del puente** (§6) y cómo se declara un residuo | Hoy no hay ninguna regla | Persona responsable |
| PD-6 | **Reexpresiones** (NIIF 17/9, cambios de perímetro): qué año manda en la serie, el original o el reexpresado | Afectan a C56 y a la referencia mecánica, no a B0 | Persona responsable |

---

## 9. Correcciones frente a `52fb120` (`CONTRATO_C_PROPUESTA.md` y `MAPA_ENTRADAS.jsonl`)

| # | 52fb120 decía | El motor dice | Cita |
|---|---|---|---|
| 1 | «g∞ del patrimonio (B14)» | X14 = crecimiento del patrimonio años 1–5. g∞ está en `Análisis!B68:D68`; Palancas fila 17 es una copia. | `B6:444-445,453,479-480,972` |
| 2 | «payout (B15)» | X15 = **ROE objetivo** del año 5. No hay celda de *payout*: el reparto es un resultado (1 − g/ROE). Escribir un *payout* de 0,40 en C15 del fixture C_orig lleva el NORMAL de 11,98 a 21,71 (×1,81) en mi réplica. El revisor midió ×2,42 sobre su propia base (sonda4); no la reproduzco, pero la conclusión es la misma. | `B6:446-449,928` |
| 3 | «B16 n/a» como regla propia del motor C; «reglas propias en B16:D16» | B16:D16 son el S2C: en C no se leen y la gramática exige dejarlas vacías | `B6:450-452,971`; `comprobar_gramatica.py:158-161` |
| 4 | «ROE terminal (B18)» | Correcto en lo esencial: X18 = ROE a largo plazo, solo en el terminal, y con la condición ROE_lp > g∞ | `B6:454-456,932`; V16 |
| 5 | «ROE = BAI / patrimonio medio» | ROE = **beneficio neto atribuible ÷ patrimonio atribuible de cierre** (L9/L21) | `B6:328`; `REF["Historia!L34"]` |
| 6 | Puente «BAI + OCI **+ dividendos** − recompras + ampliaciones + otros» | Beneficio neto atribuible (después de impuestos) + OCI **− dividendos** − recompras + emisiones ± AT1 ± otros con nombre. Caso: 1060, no 1170. | §6 |
| 7 | «crecimiento del patrimonio = (1 − payout) × ROE» como modelo del motor | El crecimiento es una entrada (X14) y el reparto se deriva. La identidad solo vale con excedente limpio y ROE sobre apertura. | `B6:927-930` |
| 8 | «Unidad: patrimonio por acción (o valor liquidativo); valor = patrimonio × múltiplos» | VP a r (`Análisis!C56`) de B(t−1)·ROE − ΔB más el terminal de Gordon sobre B10, dividido entre `Análisis!C55`. Múltiplos o valor liquidativo serían otro método (PD-2). | `B6:929-937` |
| 9 | «Capital regulatorio … como contexto y guarda» | La hoja no lee capital. La guarda queda como PD-1, sin definición ni números. | `P62:255-257` |
| 10 | No mencionaba r, g∞, las probabilidades, las acciones, la quiebra, el precio, la capitalización, la fila de ventas ni la condición de años consecutivos | Son entradas o controles del motor C: §2.3–2.4 y §7.1 | `B6:1102-1167,1187-1195` |
| 11 | «ver si el reparto y el crecimiento son coherentes» como función de valor | Esa frase es la delimitación de E62, no la fórmula. El valor sale de §3–4. | `P62:255-257` |

*Contrato sin aplicar a ninguna entidad. No fija r, g∞, ROE, probabilidades, umbrales ni base de valor. Ninguna cifra de este documento es una estimación de entidad real.*
