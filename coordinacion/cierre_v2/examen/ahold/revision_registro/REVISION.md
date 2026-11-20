# Revisión del registro de entradas de Ahold Delhaize (examen)

- **Revisor:** «Claude revisor registro», 2026-11-18. Es un agente Claude distinto del extractor Mistral (`mistral-large-4-0`) y del extractor complementario (`claude-opus-extractor-complementario`). **No se sella nada:** el sellado se hará sobre `ahold_f3`.
- **Material revisado:** `registro/verificacion_entradas.json` en `coordinacion/cierre-v2` @ `33d5f2d`, con 502 entradas: 309 del universo y 193 auxiliares. Las huellas de `fuentes_mercado/` salen de `mistral/examen-ahold-entradas` @ `9a06d4a`.
- **Contraste:** textos `[PDF PAGE n]` de `ahold_f1` y `ahold_f2` (repo producto, `examen/ahold-f1` @ `1c73f22`), el libro, `fase1_v63.json` y `etapa1/Ahold_evaluada.xlsx`.
- **Detalle:** `REVISION.tsv`, con 471 filas. Están las 278 celdas del universo y los 193 auxiliares. Quedan fuera las 30 hipótesis de las fases y `Historia!C85`, que es la hipótesis F1-A: no se revisan.

## Recuentos

| | verificado | discrepancia | duda | total |
|---|---|---|---|---|
| universo (sin hipótesis) | 238 | 32 | 8 | 278 |
| auxiliares | 178 | 15 | 0 | 193 |
| **total** | **416** | **47** | **8** | **471** |

### Las 47 discrepancias, por tipo

- **7 materiales:**
  - P-O2: C55 y C41.
  - P-O1: C46, C48 y C49.
  - Vigencia: C42 y su auxiliar de convención.
- **8 de evidencia o clase en ceros:** el valor está bien, pero la cita no lo prueba.
- **10 de justificación:** I+D.
- **22 formales:** folios y un periodo.

### Lo que se comprobó en todas las entradas

Por script, y a mano en las señaladas:
- la cita está en su página;
- la posición de la cifra en la línea coincide con la cabecera de columnas (comparativo de AR(N+1), o la columna corriente en 2025);
- la edición del informe;
- la escala, el signo y el periodo;
- que la fórmula reproduce el libro.

### Resultado de `comprobar`

- **Sobre una copia de `ahold_f1` con `fuentes_mercado/`:** 0 errores, 0 discrepancias y 502 pendientes, como declara el extractor complementario.
- **Sobre `ahold_f2`:** 18 desactualizadas. Son C41, C55, C46, C48, C49 y 13 hipótesis.
- **Huella de la cabecera:** es `df6bce…`, la de la plantilla `ahold_4_15`. No coincide con la de f1 (`246af8…`) ni con la de f2 (`db0b62…`).

## Discrepancias materiales y corrección propuesta

1. **P-O2, acciones al cierre.**
   - **Qué pasa:** `Análisis!C55` = 905 es la media diluida de 2025 (AR2025 p. 260; la cita es correcta). La decisión exige las acciones en circulación a 28-dic-2025.
   - **Corrección:** **886,877259 M**, de Q3-2026 PDF p. 21 («December 28, 2025: 886,877,259», escala 1e-6). AR2025 p. 244 imprime 886,877 (en miles).
   - **Arrastre:** **C41 = 36,05 × 886,877259 = 31.971,925**.
   - Los dos valores ya están en el libro de `ahold_f2`.
2. **P-O1 (c), regla espejo.**
   - **Qué pasa:** el registro resta lo que se paga, pero no suma lo que se cobra por lo mismo. Los cobros van en inversión:
     - AR2024 p. 263: «Dividends received from joint ventures 15 22 22», «Interest received 196 160», «Lease payments received on lease receivables 125 117».
     - AR2025 p. 216: «… 28 22», «… 130 196», «… 138 125».
   - **Corrección** (todos los valores coinciden con `ahold_f2`, cada uno con 3 auxiliares nuevos):
     - **C46** = (6.466+22 + 6.224+22 + 6.989+28)/3 = **6.583,667**;
     - **C48** = (226−160 + 230−196 + 261−130)/3 = **77**;
     - **C49** = (1.815−117 + 1.743−125 + 1.944−138)/3 = **1.707,333**.
   - Los auxiliares actuales de CFO, intereses y arrendamientos están bien.
   - Los signos de los gastos están bien aplicados: −1 sobre la cifra impresa entre paréntesis, para obtener la magnitud positiva que se resta.
3. **C42 desfasado** (EV/EBITDA = 6,129).
   - **Qué pasa:** usa la capitalización de la etapa 1, 28.626, que no tiene fuente.
   - **Corrección:** con C37 y C55 vigentes, (31.971,9 + 16.065 − 244) ÷ 7.252 = **6,590x**. Hay que recalcularlo en f3 y retirar `aux:etapa1_capitalizacion_oct2026`.

## Evidencia forzada y otras discrepancias (el valor es correcto)

- **`Historia!C23` y `D23`, `cero_comprobado`.**
  - **Qué pasa:** citan la asignación del precio de compra de Delhaize: «Finance lease liabilities (517) — …». No prueba ningún cero.
  - **Corrección:** `no_aplicable`. En 2016 y 2017 rige la NIC 17. AR2025 p. 65, nota 1: «prior to December 30, 2018, has not been restated…». Los arrendamientos financieros NIC 17 ya están en la fila 22.
- **Minoritarios `D26`, `E26`, `F26`, `G26`, `H26` y `K26`.**
  - **Qué pasa:** citan filas del estado de cambios en el patrimonio de otro año («… 1,817», «… 1,780», «… 1,397», «… 1,874»). No prueban el cero.
  - **Corrección:**
    - citar «Non-controlling interests — —» de AR2021 p. 180 (2020–21) y de AR2024 p. 259 (2023–24);
    - para 2017–2019, derivar 0 = Group equity − patrimonio atribuible (AR2025 p. 65).
  - C26, I26, J26 y L26 sí lo prueban.
- **`Historia!C19:L19`.** La clase `dato_ausente` es correcta, pero la justificación habla de «deterioros». La fila es **I+D**.
- **Formales:**
  - Folios: AR2019 PDF p. 125 tiene el folio impreso 124, no 110 (13 entradas). AR2018 p. 160 tiene el folio 160, no 281. AR2017 p. 147 tiene el folio 147, no 54. Q2-26 p. 15 tiene el folio 15, no 30 (8 auxiliares).
  - Periodo «12 meses hasta 30-jun-2026» en el CFO del 1S-26: es el semestre que cierra el 28-jun.

## Dudas (8)

- **Deuda 2016–17 (`C22`, `D22`).** Incluye los arrendamientos financieros NIC 17 (1.960 y 1.607), aunque el rótulo de la fila dice «sin arrendamientos». No hay doble cuenta. Lo decide la persona.
- **`C24`.** La fórmula sobre FY2025 coincide con 0,109 por redondeo. La etapa 1 lo define como un ROCE LTM a jun-2026.
- **`C40` y `C88`.** Son anteriores a P-O1. Con la regla espejo:
  - el FCF LTM sería **2.096**, no 1.821; la propia definición de Ahold, Q2-26 p. 23, suma esos cobros;
  - la mediana P/FCF bajaría a ≈ **12,5x**, no 14,7x. La red min/max sí calcula la mediana.
- **`C96`.** Sin fuente conservada. AR2025 da 0,0006.
- **`C38`.** Lectura externa sin bytes.
- **`Palancas!A30`.** Es una etiqueta asignada, así que la clase debería ser convención. Además, no está probado que «Rest of world» sea sobre todo Bélgica: incluye Chequia, Rumanía con Profi, Grecia y Serbia. Afecta a la r mínima de la fase A.

## Datos de mercado

- **Huellas.** Las cinco de `fuentes_mercado/` coinciden con `HUELLAS.txt` y con la cabecera.
- **Precio C37.** La fila «13/11/2026;…;36.05;36.05» es el cierre no ajustado de Euronext. No hay dividendo pendiente: la fecha ex del dividendo a cuenta de 2026 fue el 07-08 y el pago, el 27-08 (página oficial).
  - No es la sesión más reciente: el 17-11 cerró a 35,14. El libro fija la fecha del 13-nov.
- **Bund C57.** El 17-11 está a 3,34 %, en la serie UMU de 9 a 10 años. El 13-nov, la fecha del precio, la serie da 3,36 %.
- **Damodaran C7.** «Retail (Grocery and Food)» está en la copia conservada.
- **Conservación.** Los ficheros de mercado están en la rama de Mistral, no en el expediente. Para sellar hay que llevarlos a `ahold_f3` (R2).

## Límites

- **Valores contra los que se revisó:** los del libro `ahold_f1`. Los recálculos propuestos se contrastaron con `ahold_f2`. `ahold_f3` no existe aún: al sellar hay que repetir `comprobar` y regenerar la huella.
- **Omisiones del registro frente al encargo:** no tienen efecto en las cifras, pero el encargo las pedía.
  - Falta declarar el cash pool nocional en `tratamiento` de los descubiertos.
  - Falta declarar que «Repayment of lease liabilities» es principal más intereses.
- **Convenciones aceptadas de la fase 1, con su nota en el TSV:**
  - D17 (2017) sale de AR2017; AR2018 imprime el mismo 190.
  - Pensiones: línea del balance, sin restar los activos de 70 (2025).
  - Circulante: incluye la línea de otros activos y pasivos no corrientes y provisiones.
- **Qué no se hizo:**
  - no se descargaron los PDF; se usaron los textos del expediente, con la huella registrada;
  - no se revisaron las hipótesis.
- Esto no acredita aptitud para dinero real.
