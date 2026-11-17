# Contraste externo (Mistral R) de las revisiones del coordinador

- **Autor del contraste:** sesión Mistral (Vibe Code, `mistral-large-4-0`), rama `revision/mistral-contraste-coordinador`. No soy autor de ninguna revisión contrastada ni corrijo entregas de otros frentes.
- **Objeto:** las revisiones publicadas por el coordinador en `jluisplagos/munger-v2-evidencias-mistral`, rama `coordinacion/cierre-v2`, directorio `coordinacion/cierre_v2/revisiones_coordinador/`, en el corte del commit `30c314c` (HEAD de esa rama al contrastar).
- **Alcance contrastado:**
  - `AUTO_a508d6b/` (T-AUTO) → `CONTRASTE_AUTO_a508d6b.md`
  - `MANUAL_v2_ef36ab1/` (G-MANUAL v2) → `CONTRASTE_MANUAL_v2_ef36ab1.md`
  - `D2_3934bc9_5f4b2a2/` (corrección D3) → `CONTRASTE_D3_3934bc9_5f4b2a2.md`
  - `D_d032691/` (bloque 3 frente a D3) y la aceptación de los 36 casos del personaje (D-36) → `CONTRASTE_D_d032691_D36.md`
  - `A3_0946971/` (corrección A4) → `CONTRASTE_A4_0946971.md`
  - `E1_23718fb/` (corrección E2) → `CONTRASTE_E2_23718fb.md`
  - `F2_195766f_98bdf8f/` (corrección F3) → `CONTRASTE_F3_98bdf8f.md`
- **Método:** solo lectura sobre clones/extracciones (`git archive`, `git show`, copias en `/workspace` fuera del repo). Se han reejecutado las sondas publicadas sobre copias aisladas de los commits revisados y se han lanzado sondas propias (ver `sondas/`). Sin red, sin llamadas a API de pago, sin workflows, sin LibreOffice, sin ejecutar el producto ni el personaje. No se ha modificado ningún repositorio salvo esta rama.
- **Qué se comprueba en cada revisión:** (1) que los hallazgos se reproducen con sus sondas; (2) que no se acepta nada sin evidencia; (3) que no hay hallazgos falsos ni omitidos; (4) que `CONTROL.json` refleja lo revisado.
- **Resultado global:** ver `CONTRASTE_RESUMEN.md`. Una discrepancia de control (campo `revision` de G-MANUAL) y varias notas de alcance; ningún hallazgo falso ni omitido en las revisiones contrastadas.
- Este contraste no acepta entregas, no acredita aptitud económica ni para dinero real y no sustituye a las revisiones del coordinador.
