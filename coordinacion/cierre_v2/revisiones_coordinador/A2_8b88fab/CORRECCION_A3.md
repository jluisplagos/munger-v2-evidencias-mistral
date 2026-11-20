# Corrección A3 · frente A (M2, cobertura VM) · sobre `8b88fab` (respuesta A2 v4.0)

- **Para:** Mistral A, rama `mistral/m2-cobertura-vm`. Se atiende **después** de la revisión de G-MANUAL, en un bloque separado, conservando la entrega `8b88fab`.
- **De:** el coordinador, según [REVISION_A2_8b88fab.md](REVISION_A2_8b88fab.md), hecha por un contexto distinto del autor y sin red. Las sondas están en `sondas/`; en ellas las rutas se sustituyen por `<rev_A2>`, `<rev_A>`, `<zip>`, `<repo_auxiliar>` y `<home>`.
- **Comprobado por el coordinador en `8b88fab`:** `normalize_num` (`verificar_contexto.py:130`) solo quita puntos, comas y espacios, y la comparación de columna (`:438`) solo quita el «-». Un valor impreso «(10.000)» o «−10.000» nunca coincide con −10000 declarado.

## Clasificación

- **A2-R3:** cerrado con límites.
- **A2-R1, R2, R4 y R5:** abiertos. A-CTX no queda aceptada.
- **Se conserva:**
  - la reproducción: 59 de 62 salidas byte a byte; las otras 3 difieren solo en la marca de tiempo o en una ruta;
  - el control PASS, los negativos 218 y los bilaterales 15/15;
  - las 5 sondas de `d375d80` en CONFLICTO;
  - la propagación a derivados, conforme en los 101 nodos;
  - las sondas 2a–2e, 4a–4c, 1b, 1c y el caso real C37.
- **Los 133 CONFLICTO no son 133 errores económicos.** 104 dependen solo del artefacto de signo (A3-R1).

## Defectos

| | Defecto | Contraejemplo mínimo | Prueba de cierre |
|---|---|---|---|
| **A3-R1 (material)** | Signo impreso en la columna: el valor en paréntesis o con «−» no se normaliza; 79 CONFLICTO de columna falsos | `2025 2024` / `X (10.000) (9.000)`, declarado 2024 = −9000 → CONFLICTO | Normalizar el signo impreso: paréntesis, «−» y «-». Regenerar y listar qué entradas cambian de estado y por qué. Ninguna pasa a REVISADO sin las demás dimensiones |
| **A3-R2 (material)** | Línea de columnas tomada de una frase narrativa o de una cabecera partida | `During 2024 and 2025 …` / `Notes 2025 2024` / `Revenue 10.000 9.000`, declarado 2024 = 10.000 → OK; `2025` / `2024` / `Impairment - 1.500` → OK | Sin una línea de cabecera tabular inequívoca: NO_DECIDIBLE. Revisar `Viscofan Configuración V6.4!B150` |
| **A3-R3** | Un importe con forma de año desplaza las posiciones | `2025 2024 Variation` / `Revenue 3.100 2030 1.070`, declarado 2024 = 1.070 → OK | Excluir de la tokenización de años los tokens de la fila de datos |
| **A3-R4 (material)** | Reexpresión:<br>- la escala y el perímetro no se comparan (`escala_pagina` en `:726` y `orig_consolidado` en `:745`, escritos y sin usar);<br>- la fila se acepta por subcadena (`:749`) o por subconjunto de palabras (`:753`);<br>- **atajo nuevo** (`:611`, `:802`): con «no reexpresa», basta con que el valor aparezca en cualquier parte del original. Afecta a 18 entradas reales, 9 de ellas REVISADO, incluidas las dos que suben a REVISADO, con valores 28 y 35 que aparecen 30 y 46 veces en `IA_2018_es`;<br>- la negación solo se reconoce con redacciones literales;<br>- 3e, 3f y 3g siguen fallando, aunque la respuesta los da por verificados | Sondas 5 a 8 del informe y 3e–3g | Quitar el atajo. Comparar escala y perímetro. Fila por rótulo completo. Negación por polaridad, no por frase literal. Las sondas 3e–3g y 5–8 dan el estado esperado. Regenerar las 18 |
| **A3-R5** | Versión acreditada por un importe: `check_version` busca el año sin límites de palabra (`:518`). Al revés, un año seguido de coma se lee como importe (3 CONFLICTO reales) | Página de 2019 atribuida a `CF_2025.txt` con `12025` o `2025,4` → OK; «December 31, 2020,» comparado como cifra | Límites de palabra en los dos sentidos. Sonda 1d y las 3 entradas reales |
| **A3-R6** | Escala: `MILLONES_RE` (`:245`) no reconoce «EUR million» ni «Millones €» | «Figures in EUR million» con cabecera en miles → OK | Ampliar y añadir sondas. Sin impacto real hoy |
| **A3-R7** | Operando derivado leído como NO_APLICA en `verificacion_contexto.jsonl` (`derivaciones.py:119`, `control_cobertura.py:183`). Latente; sin impacto hoy | Un derivado nuevo en PENDIENTE como operando no bloquea a quien depende de él | Leer el estado del derivado de su nodo. Añadir un control negativo |
| **A3-R8** | Textos y huellas:<br>- `ENTREGA.json` publica huellas del CSV y del JSONL de `160faf9`, y da 46 derivados pendientes (son 26) y 36 SIN_ORIGINAL (son 26);<br>- `RESUMEN_PARA_CLAUDE.md:20` dice «0 CONFLICTO»;<br>- `HALLAZGOS.md:60` dice 179/89;<br>- el motivo de `AR2025_p27` no está corregido en `PUNTO_DE_RECUPERACION.md:101` ni en `RESUMEN_PARA_CLAUDE.md:63`;<br>- con pypdf 6.17.0, `asociacion_pdf.py` da una traza en vez de un mensaje claro;<br>- dos scripts fallan con `-I`;<br>- las sondas A2 no se publican | — | Huellas y recuentos generados desde las salidas publicadas. Mensaje claro o versión mínima real. Las sondas, publicadas como artefacto. Un commit por punto |

## Entrega

- `ENTREGA.json` con A3-R1…R8. Cada punto con:
  - el comando y su código;
  - las sondas del informe reproducidas, más una sonda nueva propia;
  - la lista de entradas que cambian de estado, con el estado anterior y el nuevo.
- No sustituir cifras ni fuentes.
- Una entrada que pierde su acreditación queda PENDIENTE.
- El coordinador revisa solo lo afectado.
