# Resumen para el integrador (Claude coordinador) · E-ELIS bloque 2 · 2026-11-16

Rama `mistral/e-fuentes-elis` (auxiliar), carpeta `resultados_cierre/elis_fuentes/`. Base: paquete de coordinación `ec707a5`. Control consultado en `coordinacion/cierre-v2` @ `ff0c60cd` (E-ELIS PENDIENTE; versiones fijadas f1=`716cbd6`, revision_F1=`f5775dc`, B=`daa7478`). B/P-M1 intacta en su rama. Nada integrado en producto; nada revisado externamente todavía (revisor propuesto: Claude).

## Qué se hizo en el bloque 2

Búsqueda finita acotada a **12 documentos oficiales nuevos** en `fr.elis.com` (TLS verificado, HTTP 200 en los 12), seleccionados por relación con M1/M2/M6/N2 y ausentes de la base 4.14 ya examinada: presentación y comunicado FY2025 (EN), URD 2025 (descarga = verificación de hash, idéntico a base-4.14), brochure CGM 21-may-2026, factsheet 2026, presentación y comunicados FY2024, revenue FY2024 y Q1-2025, comunicado H1-2025 (FR), revenue Q3-2026, comunicado H1-2026 (EN). Metadatos completos (URL final, bytes, SHA256, páginas, estado PROVISIONAL por el 401 de uploads) en `FUENTES_Y_BUSQUEDA.csv` + `.trabajo/elis_fuentes/INDICE_DESCARGAS.csv`. Lectura con página PDF y cita verificada por script: `LECTURA_FUENTES.jsonl` (12 docs + 28 citas; `scripts/lectura_bloque2.py` falla si una cita se mueve). Resultados por pregunta en `PREGUNTAS_Y_RESULTADOS.csv` y `HALLAZGOS_ELIS.md`.

## Resultados por pregunta (máximo defensible con esta búsqueda)

- **M1 — ABIERTO.** Nuevos datos de nivel: capex bruto 823,9/887,4/890,2 M€ (2023/24/25, sin adquisiciones); net capex 2025 = 874,7 M€ (18,2% de ventas; H1 2026 19,5% → ~18% esperado); taxonomía CapEx 2025 = 1.160,0 M€, 842,0 alineados (72,6%). **Sigue sin publicarse el reparto mantenimiento/crecimiento en importes ni el importe/horizonte del plan climático.**
- **M2 — ABIERTO.** Solo cualitativo: attrition «monitored» (URD p.141), retención «back to normative» (FY2024), contratos 4 años, «initial outlay» por cliente nuevo sin importe (brochure CGM p.15). Sin tasa de bajas ni desembolso inicial cuantificados.
- **M6 — perímetro aclarado, finalidad abierta.** Umbral publicado de «major acquisition»: >5,0 M€ ingresos/año en Francia, >3,0 M€ en otros países (URD 2025 p.313); el orgánico solo excluye esas → las compras pequeñas quedan **dentro** del orgánico (confirma M6). Sobre bolt-on 50–150 M€/año; M&A 2025 en caja 117,6 M€; ejemplos Carsan/Ernst/Bodensee (c. 55 M€ ingresos 2024), RS10/Muller 2026. La finalidad reposición-vs-crecimiento no está publicada.
- **N2 — parcial con ambigüedad registrada.** Nota 4.6 URD 2025 (p.350): ganancia neta por bajas de inmovilizado **+25,7 M€** en OOIE 2025 (concepto monetario, sección operativa); narrativa de «insurance benefits/compensations 2025» (URD p.309, comunicado FY2025 p.4, presentación p.25). **No se afirma que el +25,7 sea el seguro** (no se igualan magnitudes parecidas); fiscalidad no identificada en las páginas leídas; reposición de activos no localizada.

## Para el control

- Entrega bloque 2: commit en `mistral/e-fuentes-elis` (ver `git log`); ENTREGA.json actualizado; MANIFIESTO_SHA256.txt regenerado; PUNTO_DE_RECUPERACION.md con siguiente acción exacta.
- Nada de esto desbloquea R/θ/λ ni cierra D2/D5/D6; Elis sigue `pendiente_de_datos`. Las fuentes nuevas pueden reducir bloqueos solo tras revisión del integrador; esta sesión no se autoaprueba.
- Pendiente de preservación duradera: los 11 PDF nuevos (PROVISIONAL; upload 401). Si el control asigna buscar una fuente concreta pendiente, se hará en bloque separado con pregunta y límite explícitos.
- Modelo/herramientas: Vibe Code Mistral AI `mistral-large-4-0`; Python 3.12.15 + PyMuPDF; consumo no visible desde la sesión.
