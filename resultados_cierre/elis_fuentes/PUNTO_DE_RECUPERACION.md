# Punto de recuperación · etapa E (E-ELIS) · rama `mistral/e-fuentes-elis`

Reescrito al cerrar cada bloque. B/P-M1 se conserva intacta en `mistral/m2-fundamento-pm1` @ `daa7478` (no se toca desde aquí).

## Estado actual

- Rama `mistral/e-fuentes-elis` desde el paquete de coordinación `ec707a5`. Escritura solo en `resultados_cierre/elis_fuentes/`. Control común consultado en lectura (`coordinacion/cierre-v2` @ `ff0c60cd`): E-ELIS, f1=`716cbd6`, revision_F1=`f5775dc`.
- **Bloque 1 cerrado:** inventario de preguntas M1/M2/M6/N2 y de recursos ya examinados vs candidatos (`PREGUNTAS_Y_RESULTADOS.csv`, `FUENTES_Y_BUSQUEDA.csv`, `scripts/inventario_bloque1.py`).
- **Bloque 2 cerrado (este commit):** 12 documentos oficiales nuevos de `fr.elis.com` descargados (HTTP 200, TLS verificado; sha256/bytes/páginas en `INDICE_DESCARGAS.csv` bajo `.trabajo/elis_fuentes/`); lectura verificada con 28 citas (documento + página PDF + patrón) en `LECTURA_FUENTES.jsonl` (`scripts/lectura_bloque2.py`); resultados por pregunta actualizados en `PREGUNTAS_Y_RESULTADOS.csv` y en `HALLAZGOS_ELIS.md`; resumen en `RESUMEN_PARA_INTEGRADOR.md`.

## Resultados del bloque 2 (por pregunta)

- **M1 ABIERTO:** nivel publicado (capex bruto 823,9/887,4/890,2 M€ 2023–25 sin adquisiciones; neto 874,7 M€ = 18,2% de ventas 2025; H1-2026 19,5% → ~18% esperado; taxonomía 2025: 1.160,0 M€, 842,0 alineados 72,6%) pero **sin reparto mantenimiento/crecimiento en importes ni importe/horizonte del plan climático**. No localizado en esta búsqueda.
- **M2 ABIERTO:** solo cualitativo (attrition «monitored» URD p.141; retención «back to normative» FY2024; contratos 4 años; «initial outlay» por cliente nuevo sin importe, brochure CGM p.15). Sin tasa de bajas ni desembolso inicial cuantificados. No localizado en esta búsqueda.
- **M6 perímetro aclarado, finalidad abierta:** umbral «major acquisition» > 5,0 M€ (Francia) / > 3,0 M€ (otros países) de ingresos anuales (URD 2025 p.313) — el orgánico solo excluye esas; bolt-on 50–150 M€/año; M&A 2025 en caja 117,6 M€; ejemplos Carsan/Ernst/Bodensee, RS10/Muller. La finalidad reposición vs crecimiento **no publicada**. No localizado en esta búsqueda.
- **N2 parcial con ambigüedad:** +25,7 M€ ganancia neta por bajas de inmovilizado en OOIE 2025 (nota 4.6 URD p.350, concepto monetario/operativo) + narrativa «insurance benefits/compensations 2025» (URD p.309, comunicado FY2025 p.4, presentación p.25). **No se afirma que el +25,7 sea el seguro**; fiscalidad no identificada; reposición de activos no localizada.

## Commits

- `b4a4703` bloque 1 (inventario). Este push: bloque 2. Remoto: `git ls-remote origin mistral/e-fuentes-elis`.

## Pendiente / siguiente acción exacta

1. **Bloque 3:** leer el control de Claude (`git show origin/coordinacion/cierre-v2:coordinacion/cierre_v2/CONTROL.json`); si asigna una fuente concreta pendiente de E (o de P-M1), buscarla en bloque separado con pregunta y límite explícitos; si no hay asignación nueva, cerrar E como búsqueda finita: cada pregunta queda en «evidencia examinada / ambigüedad / no localizado en esta búsqueda» (nunca «no publicado en ninguna parte»), con lista de documentos/páginas y límites.
2. Entrega final del bloque 3: ENTREGA.json definitivo, MANIFIESTO_SHA256.txt regenerado, esta recuperación actualizada, commit + push.
3. Preservación pendiente: 11 PDF nuevos en PROVISIONAL (uploads.github.com → 401; no reintentar ni pedir tokens); si hubiera otra vía autorizada de conservación, verificarla antes de afirmar preservación.

## Límites vigentes

- No se elige R (ni dentro de 736,0–867,2), θ, λ, k, probabilidades ni política; Elis sigue `pendiente_de_datos`; C48=108, C49=128,1, FCF base=307,933 y las decisiones E1/D3/E2/E6 se conservan sin tocar.
- Proporción de ventas ≠ proporción de capex; «dos tercios» de un bloque no se extrapola; categoría contable ≠ reposición económica; dos magnitudes parecidas no son la misma partida (N2).
- Sin contacto privado con empresas, sin comprar acceso, sin cambiar credenciales, sin LibreOffice/pipeline, sin tocar producto/main/otros frentes.

## Modelo y herramientas

Vibe Code de Mistral AI, modelo `mistral-large-4-0`; consumo no visible desde la sesión. Python 3.12.15 + PyMuPDF (extracción con marcadores `[PDF PAGE n]`); urllib con TLS verificado (curl bloqueado por el sandbox); web_search/web_fetch solo como pistas hacia URLs oficiales.
