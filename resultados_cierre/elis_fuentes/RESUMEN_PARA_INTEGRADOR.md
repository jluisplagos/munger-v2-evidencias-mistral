# Resumen para el integrador (Claude coordinador) · E-ELIS · bloque 2 + corrección E1 · sobre `93a9780`

Rama `mistral/e-fuentes-elis` (auxiliar), carpeta `resultados_cierre/elis_fuentes/`. Encargo: §4 de `REANUDACION.md` (`c241a59`) + `CORRECCION_E1.md` (control de referencia `99adbbf`; sin cambios en `E_93a9780` en el HEAD `57b34a6` consultado). B/P-M1 intacta en `mistral/m2-fundamento-pm1` @ `daa7478`. Nada integrado en producto; revisión pendiente del coordinador. Estados: **entregado** (esta rama), **revisado** (E1 externo, respondido E-R1…E-R9), **integrado** (no), **probado** (scripts ejecutados, ver `RESPUESTA_REVISION_E1.md`).

## Qué se corrigió (E-R1…E-R9)

- **E-R1 N2:** retirada la afirmación falsa («concepto monetario / sección operativa»). +25,7 va en línea propia de la nota 4.6 (URD p.350), separada de «monetary items» (28,2); EFE p.327 resta (23,1) en operativo y lleva cobros 15,3 a inversión; 16,9 a cobrar (p.349). Dos medidas separadas (+23,1 resultado vs +25,7 nota). N2 **ABIERTO** en cobro/fiscalidad/reposición.
- **E-R2 M6:** Bodensee = adquisición **importante** (URD p.306/p.312, columna propia p.341); **117,6** (M&A total 2025) separado de **37,3** («Other acquisitions» 2025, p.341). **E-R3:** perímetro p.313 = corroboración de F1 V1 (informe `716cbd6` l550), no confirma el 31,5 M€/año. M6 **ABIERTO**.
- **E-R4 M1:** capex p.311–312 y taxonomía p.215–217 declarados corroboración de la base; perímetro taxonomía añadido (p.217: 26,2+183,9+887,1+62,7 ≈ 1.160,0); alineado 842,0 es sobre todo economía circular (70,7 pp; clima 1,9 pp), no importe del plan climático. M1 **ABIERTO**.
- **E-R5:** citas 20/21 (y todas las demás con `.*`) reescritas sin greed ni alternativas, split atómicas (Q1-2025 p.1 ×2; Q3-2026 p.1/p.2/p.3). **E-R6:** índice de descarga en Git + 32 extractos acotados con sha256 del PDF; PDF siguen PROVISIONAL (401). **E-R7:** «no localizado en esta búsqueda» con alcance, sin frases absolutas. **E-R8:** textos/refs de control actualizados (`99adbbf`; HEAD remoto anotado). **E-R9:** idempotencia probada (2 ejecuciones, sha256 idénticos), carpetas creadas, exit 1 en fallo de descarga (negativo ejecutado), exit 2 con comando `git fetch` si falta una dependencia (negativo ejecutado), segundo extractor pypdf 7.1.0 ejecutado: 52/52 citas.

## Resultados por pregunta (máximo defensible)

- **M1 — ABIERTO.** Nivel corroborado (capex bruto 823,9/887,4/890,2; neto 874,7 = 18,2%; H1-2026 19,5% → ~18%) sin reparto mantenimiento/crecimiento ni importe del plan climático. No localizado en esta búsqueda.
- **M2 — ABIERTO.** Solo cualitativo (attrition «monitored», retención «back to normative», 4-year contracts, «initial outlay» sin importe). No localizado en esta búsqueda.
- **M6 — ABIERTO.** Perímetro corroborado (umbral >5,0/3,0 M€); clasificación 2025 por página (seis importantes incl. Bodensee; «Other acquisitions» 37,3); M&A total 117,6; bolt-on 50–150 M€/año. Finalidad reposición vs crecimiento no localizado en esta búsqueda.
- **N2 — ABIERTO.** Dos medidas separadas (+23,1 EFE p.327; +25,7 nota 4,6 p.350) y 16,9 a cobrar (p.349); seguro no igualado con el +25,7; cobro/fiscalidad/reposición no localizados en esta búsqueda.

## Para el control

- Entrega: `RESPUESTA_REVISION_E1.md` (E-R1…E-R9 con pruebas ejecutadas), `ENTREGA.json`, `LECTURA_FUENTES.jsonl` (64 registros, 52 citas, `tipo_evidencia`), `PREGUNTAS_Y_RESULTADOS.csv` (incl. `estado_tras_revision_e1`), `FUENTES_Y_BUSQUEDA.csv`, `fuentes_descargadas/INDICE_DESCARGAS.csv`, `extractos/` (32), `VERIFICACION_SEGUNDO_EXTRACTOR.json`, `MANIFIESTO_SHA256.txt`, `PUNTO_DE_RECUPERACION.md`, `scripts/` (5).
- Nada desbloquea R/θ/λ ni cambia el estado de Elis (`pendiente_de_datos`); C48=108, C49=128,1, FCF base=307,933 y decisiones vigentes conservadas. Sin autoaprobación ni ciclos recursivos.
- Pendiente: revisión del coordinador sobre esta respuesta; preservación duradera de los 11 PDF (PROVISIONAL; decisión del usuario).
- Modelo/herramientas: Vibe Code Mistral AI `mistral-large-4-0`; Python 3.12 + PyMuPDF (primario) y pypdf 7.1.0 (segundo extractor); urllib con TLS verificado en fr.elis.com; consumo no visible desde la sesión.
