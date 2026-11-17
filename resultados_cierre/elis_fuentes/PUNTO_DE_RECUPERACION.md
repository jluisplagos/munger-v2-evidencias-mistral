# Punto de recuperación · etapa E (E-ELIS) · rama `mistral/e-fuentes-elis`

Reescrito al cerrar cada bloque. B/P-M1 se conserva intacta en `mistral/m2-fundamento-pm1` @ `daa7478` (no se toca desde aquí).

## Estado actual

- Rama `mistral/e-fuentes-elis` desde el paquete de coordinación `ec707a5`. Escritura solo en `resultados_cierre/elis_fuentes/`. Control consultado en lectura: referencia de la reanudación `99adbbf` (`c241a59`), rama `coordinacion/cierre-v2`; HEAD remoto durante esta corrección: `57b34a6` (E-ELIS sigue en CORRECCIONES sobre `93a9780`; `E_93a9780/CORRECCION_E1.md` sin cambios).
- **Bloque 1 cerrado:** inventario (`PREGUNTAS_Y_RESULTADOS.csv`, `FUENTES_Y_BUSQUEDA.csv`, `scripts/inventario_bloque1.py`; dependencias declaradas, exit 2 + `git fetch` si falta un commit).
- **Bloque 2 cerrado:** 12 documentos oficiales nuevos de `fr.elis.com` (HTTP 200, TLS, magic `%PDF` validado), sha256/bytes/páginas/URL pedida y final en `fuentes_descargadas/INDICE_DESCARGAS.csv` (Git) y `.trabajo/elis_fuentes/INDICE_DESCARGAS.csv`; lectura verificada en `LECTURA_FUENTES.jsonl`.
- **Bloque 3 cerrado:** entrega final de la etapa E (HALLAZGOS, RESUMEN, ENTREGA, manifiesto, recuperación).
- **Bloque 4 cerrado (este commit): corrección E1 (E-R1…E-R9) sobre `93a9780`** — ver `RESPUESTA_REVISION_E1.md`. 52 citas reescritas sin `.*`/alternativas y verificadas con PyMuPDF + pypdf 7.1.0 (52/52); `tipo_evidencia` nueva/corroboracion_base; 32 extractos acotados con sha256 del PDF en `extractos/`; idempotencia probada (2 ejecuciones, sha256 idénticos); exit 1 en fallo de descarga y exit 2 en dependencia ausente, ambos con negativos ejecutados; re-descarga 2026-11-17 con 12/12 sha256 idénticos a `93a9780`.

## Resultados tras la corrección E1 (por pregunta)

- **M1 ABIERTO:** nivel corroborado (capex bruto 823,9/887,4/890,2 y neto 874,7 = 18,2% ya en URD 2025 de la base p.311–312; H1-2026 19,5% nuevo) pero **sin reparto mantenimiento/crecimiento ni importe/horizonte del plan climático** (taxonomía 1.160,0 incluye ROU 183,9 y combinaciones 62,7, p.217; alineado 842,0 = 72,6%, sobre todo economía circular 70,7 pp, clima 1,9 pp, p.215). No localizado en esta búsqueda.
- **M2 ABIERTO:** solo cualitativo. No localizado en esta búsqueda.
- **M6 ABIERTO:** perímetro corroborado (F1 V1 ya lo tenía, informe `716cbd6` l550; URD p.313); clasificación 2025 por página: seis adquisiciones importantes con columna propia incl. **Bodensee** (p.306/p.312/p.341) y «Other acquisitions» **37,3** M€ (p.341); M&A total 2025 en caja **117,6** M€ (p.341/p.327/presentación p.29), separado de 37,3; bolt-on 50–150 M€/año; finalidad reposición vs crecimiento no localizado en esta búsqueda.
- **N2 ABIERTO:** dos medidas separadas — +23,1 M€ EFE p.327 (bajas PP&E+intangibles; resta en sección operativa; cobros 15,3 en inversión) y +25,7 M€ nota 4.6 p.350 (línea propia, separada de «monetary items» (28,2)); 16,9 M€ a cobrar por bajas a cierre (p.349); narrativa de seguros sin importe y **no igualada** con el +25,7; cobro/fiscalidad/reposición no localizados en esta búsqueda.

## Commits

- `b4a4703` bloque 1; `78d2898` bloque 2; entrega bloque 3; `93a9780` entrega revisada externamente (E1); **este commit: bloque 4, respuesta E-R1…E-R9**. Remoto verificado tras el push: `git ls-remote origin mistral/e-fuentes-elis` == HEAD local.

## Estado de cierre

E queda finito como búsqueda acotada y la corrección E1 está respondida punto a punto con pruebas ejecutadas. Nada pendiente depende de información no pública que justifique más búsqueda dentro de este encargo. Siguiente acción: **revisión del coordinador Claude** sobre `RESPUESTA_REVISION_E1.md` y este commit, registrada en el control (`coordinacion/cierre-v2`, tarea E-ELIS); sin ciclos recursivos ni autoaprobación.

## Pendiente / siguiente acción exacta

1. Revisión del coordinador sobre el bloque 4 (este commit).
2. Preservación duradera de los 11 PDF nuevos: siguen **PROVISIONAL** (upload a Release → HTTP 401; no reintentar ni pedir tokens). El almacén duradero lo decide el usuario (§2 de CORRECCION_E1). Mientras tanto, la cobertura publicada es el índice de descarga + extractos acotados con huella PDF (cobertura provisional declarada).
3. Si el control asigna una fuente concreta pendiente, bloque separado con pregunta y límite explícitos.

## Límites vigentes

- No se elige R (ni dentro de 736,0–867,2), θ, λ, k, probabilidades ni política; Elis sigue `pendiente_de_datos`; C48=108, C49=128,1, FCF base=307,933 y las decisiones E1/D3/E2/E6 se conservan sin tocar.
- Proporción de ventas ≠ proporción de capex; «dos tercios» de un bloque no se extrapola; categoría contable ≠ reposición económica; dos magnitudes parecidas no son la misma partida (N2: +23,1 ≠ +25,7).
- Sin contacto privado con empresas, sin comprar acceso, sin cambiar credenciales, sin LibreOffice/pipeline/macros, sin tocar producto/main/otros frentes.

## Modelo y herramientas

Vibe Code de Mistral AI, modelo `mistral-large-4-0`; consumo no visible desde la sesión. Python 3.12 + PyMuPDF (extractor primario, marcadores `[PDF PAGE n]`) y pypdf 7.1.0 (segundo extractor, `VERIFICACION_SEGUNDO_EXTRACTOR.json`); urllib con TLS verificado en fr.elis.com; git show de solo lectura sobre producto `716cbd6`, revisión `f5775dc` y control `99adbbf`.
