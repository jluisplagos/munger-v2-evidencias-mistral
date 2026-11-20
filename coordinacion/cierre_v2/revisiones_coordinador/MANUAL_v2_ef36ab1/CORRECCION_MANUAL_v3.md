# Corrección del manual v2 (`ef36ab1`) hacia v3

- **Autor de la corrección:** el coordinador, que también es autor del manual. La v3 la revisará otro contexto, ya sea Mistral R o un subagente distinto, y solo en lo afectado.
- **Base:** [REVISION_MANUAL_v2_ef36ab1.md](REVISION_MANUAL_v2_ef36ab1.md), hecha por un contexto distinto del autor, en solo lectura y sin red. Las sondas S01–S16 están en `sondas/`.
- **M2, comprobado por el coordinador:** el worktree de la candidata en 3149128 tiene 71 PDF materializados, ignorados por `*.pdf`, y `info/exclude` tiene 90 líneas. La línea 705 del manual («no tiene los binarios materializados») es falsa.

## Veredicto

- **CORRECCIONES:** 4 medios y 12 menores. No hay hallazgos materiales, política económica ni aptitud declarada.
- **Conforme:**
  - las 603 citas archivo:línea;
  - los 44 prefijos SHA-256 del §13;
  - los controles 4.10, 4.11 y 4.12;
  - H9, I19 e I20;
  - las dos frases actuales de CONTINUIDAD §2.5, byte a byte, sin aplicar la propuesta.

## Puntos a corregir en v3

| | Defecto | Prueba de cierre |
|---|---|---|
| MAN-M1 | El 4.8 también copia `_v64/` a un temporal (`comprobar_entrega_4_8.py:60`), igual que el 4.8.1. C-14 y la propuesta §2.5 solo cubren el 4.8.1 | C-14 y la propuesta incluyen el 4.8, con su línea de código |
| MAN-M2 | §13, l.705, y l.200/516: se afirma que faltan los binarios, cuando están ignorados o excluidos | El hecho se corrige con `git status --ignored` y el recuento de PDF |
| MAN-M3 | Faltan 7 marcas «(autodeclarado)» en «probado en el traspaso»: l.88, 155, 196, 224, 269, 282 y 323 | Las marcas coinciden con la regla de la l.12 |
| MAN-M4 | Comandos no probados sin marca, o marcados solo como «literal de la fuente»: l.183, 230, 354, 363, 366, 336, 348 y 374-375. La l.585 está adaptada y la l.13 exagera | Cada uno lleva [NO DOCUMENTADO] o su prueba real |
| Menores | Ver §2.3 del informe: supresiones que faltan en CAMBIOS, «excluyendo solo», citas del README frente a main, `/tmp` y `HOME`, `INFORME_TRASPASO.md` sin prefijo, método del sondeo de literales | Corregido o justificado punto por punto |
