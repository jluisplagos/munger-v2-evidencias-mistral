# Etapa E · fuentes económicas de Elis (E-ELIS)

Rama `mistral/e-fuentes-elis` (auxiliar `jluisplagos/munger-v2-evidencias-mistral`), creada desde el commit del paquete de coordinación `ec707a5`. Encargo: `coordinacion/cierre_v2/PROMPT_MISTRAL_B_E.md` (leer con `git show ec707a5:coordinacion/cierre_v2/PROMPT_MISTRAL_B_E.md`). Escritura solo en esta carpeta.

Objetivo: evidencia primaria nueva o búsqueda acotada que identifique lo no encontrado para **M1 / M2 / M6 / N2 de Elis** (definiciones en `PREGUNTAS_Y_RESULTADOS.csv`, con citas al frente F1 del producto `716cbd6`). No se pide valoración ni política; **no se elige R, θ ni λ**.

- Bloque 1 (publicado): inventario — `PREGUNTAS_Y_RESULTADOS.csv`, `FUENTES_Y_BUSQUEDA.csv`, `scripts/inventario_bloque1.py` (reproduce desde SHAs fijados: producto f1 `716cbd6`, revisión `f5775dc`, control `99adbbf`, ZIP base-4.14 verificado; dependencias declaradas con exit 2 + comando `git fetch` si faltan).
- Bloque 2 (publicado): búsqueda finita (12 documentos oficiales nuevos) y lectura verificada — `LECTURA_FUENTES.jsonl`, `scripts/descargar_fuentes_elis.py` + `scripts/lectura_bloque2.py`.
- Bloque 3 (publicado): entrega final de la etapa E — `HALLAZGOS_ELIS.md`, `RESUMEN_PARA_INTEGRADOR.md`, `ENTREGA.json`, `MANIFIESTO_SHA256.txt`, `PUNTO_DE_RECUPERACION.md`.
- Bloque 4 (publicado): **corrección E1 (E-R1…E-R9)** sobre `93a9780` — `RESPUESTA_REVISION_E1.md`, citas reescritas (52, sin `.*`/alternativas, verificadas con PyMuPDF y pypdf 7.1.0), `tipo_evidencia` nueva/corroboración_base, índice de descarga en Git (`fuentes_descargadas/`), extractos acotados con huella PDF (`extractos/`), idempotencia y códigos de error probados.

La entrega anterior B/P-M1 se conserva en `mistral/m2-fundamento-pm1` @ `daa7478` y no se modifica desde aquí.
