# Notas del extractor complementario · registro de entradas de Ahold (ahold_f1)

Extractor: `claude-opus-extractor-complementario`, 18-nov-2026. Parto del registro de Mistral (ronda 1, `9a06d4a`) sobre el libro de `ahold_f1` (rama `examen/ahold-f1`, en fase C turno 2, provisional). No he escrito en el expediente. Comprobaciones: todas `pendiente`, `revisor: null`, sin `vinculo`. No sello nada.

**Resultado de `comprobar`** (copia de trabajo sin PDF): universo 309, 502 entradas (193 auxiliares), **0 errores, 0 sin entrada, 0 discrepancias, 0 desactualizadas**, 502 pendientes. Prueba aparte: si se simula el sellado de todas las entradas, quedan 0 errores y 0 discrepancias. Solo quedan 3 pendientes (C37, C41, C57), porque la copia no tiene `fuentes_mercado/` de Mistral.

## Qué completé y cómo

1. **21 celdas F1 (Historia C85:L87).**
   - **C85 = A2_propio** como `hipotesis`. Es el tipo «configuracion». Fundamento: decisión F1-A del 18-nov (`DECISIONES_PARA_EL_USUARIO.md:88`) y `motor_a_f1.json`.
   - **H86:L86 (D&A de derechos de uso 2021–25) y J87:L87 (PPA 2023–25 = 18)** como `dato_publicado`. Llevan la página y el literal de la declaración F1, signo −1 y cita literal de la línea completa. La cita de la PPA que trae la declaración es una frase sin la cifra; la sustituí por la fila «Amortization» del bloque de cada año.
   - **C86, D86 (2016–17)** como `no_aplicable`: base NIC 17, sin derechos de uso.
   - **E86:G86 (2018–20)** como `dato_ausente`: la declaración no los incluye y el libro los deja vacíos, que significa «desconocido». En `incidencia` consta que los informes sí los publican: 1.000, 1.052 y 1.083.
   - **C87:I87** como `dato_ausente`: hasta 2023, el informe incluye la PPA en «Other».
2. **30 hipótesis.** El fundamento es el texto de la fase en `Control maestro!N` del libro, que es idéntico al de `celdas_A.json`/`celdas_B.json`. Las alternativas son la referencia mecánica y «Lo sustituiría». Los límites recogen el rango, la confianza y el aviso de que la fase C sigue en curso. La clase es la que declara cada fase: 6 quedan como `convencion`.
   - Además corregí `valor_modelo` en 19 de ellas. La plantilla traía el valor del libro previo a las fases: `null`, y en B69/D69 0,2. Ahora llevan el valor vigente.
3. **Las 6 celdas de Análisis.** La etapa 1 documenta cada cálculo en su Control maestro (filas 31–75):
   - **C26 = 2,9229** → `derivado` exacto: Σ CFO ÷ Σ beneficio neto 2021–25 = 31.257 ÷ 10.694.
   - **C33 = 2,2153** → `derivado` exacto: (19.261 − 3.196) ÷ EBITDA LTM 7.252. Uso 4 auxiliares del Q2-26, en las páginas 11 y 15.
   - **C42 = 6,129** → `derivado` exacto con `justificacion_clase` (N2): (28.626 + 16.065 − 244) ÷ 7.252. La capitalización 28.626 de la etapa 1 (33,14 € × 863,79 M) no tiene fuente conservada. Por eso va aislada como auxiliar `convencion`.
   - **C88 = 14,7** → `derivado` exacto. Es la mediana de los 7 P/FCF de cierre 2019–25: capitalización (AR2025, p. 65) ÷ (CFO − capex − intereses − arrendamientos). La mediana está escrita con una red de ordenación min/max, porque el contrato no tiene función mediana. Reproduce los siete valores de la etapa 1.
   - **C60 = −0,033** y **C96 = 0,0007** → `convencion` con `justificacion_clase`, citando `etapa1/Ahold_evaluada.xlsx` (hoja Análisis y Control maestro, filas 55 y 75).
     - C60 es una tasa de crecimiento compuesto: exige una raíz, que el contrato no admite. La comprobé a mano: −3,305 % / −3,330 %.
     - C96 sale del registro de la AFM y de 863,79 M acciones, que no están en el expediente. El AR2025 da 0,0006.

## Lo que no pude o queda para otros

- **C42 está desfasado** respecto de C37/C41 del libro. Con 36,05 € × 905 M acciones, la misma fórmula da 6,680. No cambié el libro: lo decide la persona responsable.
- **C60 y C96** no son reproducibles por la máquina: quedan como datos tratados como convención, a la vista.
- **Hipótesis.** Sus textos son del turno 2 de la fase C, aún provisional. Si la fase C los reescribe, hay que volver a copiarlos antes de sellar.
- **Entradas de Mistral.** No las toqué. Observo dos errores menores en sus auxiliares del Q2-26, p. 15: `folio` 30 (debería ser 15) y `periodo` «12 meses hasta 30-jun-2026» (es un semestre cerrado el 28-jun-2026). Quedan para el revisor o para Mistral.
- **Método.** Las fórmulas, citas y signos se contrastaron con las funciones de `verificacion_entradas.py`. Eso no acredita su significado económico: lo acredita el revisor independiente.
