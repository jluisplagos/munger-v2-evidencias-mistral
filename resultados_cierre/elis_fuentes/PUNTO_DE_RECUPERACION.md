# Punto de recuperación · etapa E (E-ELIS) · rama `mistral/e-fuentes-elis`

Reescrito al cerrar cada bloque. La entrega anterior B/P-M1 se conserva intacta en `mistral/m2-fundamento-pm1` @ `daa74783d2708fcd46ca7c24ae1ffbb327c35784` (no se toca desde aquí).

## Estado actual

- Rama `mistral/e-fuentes-elis` creada desde el commit del paquete de coordinación `ec707a5ba2bd684381a63ce0f6f6c143aa59f4c0`. Escritura solo en `resultados_cierre/elis_fuentes/`.
- Control común consultado (solo lectura, `git show`): `coordinacion/cierre-v2` @ `ff0c60cd` — fila E-ELIS en PENDIENTE; versiones fijadas: producto f1 = `716cbd6`, revision_F1 = `f5775dc`, B = `daa7478`.
- Cambios posteriores comprobados en el producto: el frente F1 pasó de `716cbd6` a `bf0d5c2` (W1–W3 en `d519eb0`, C20); `datos/fuentes.json` sin cambios. No se escribe nada en el repo producto.
- **Bloque 1 cerrado (este commit):** inventario de preguntas (M1/M2/M6/N2) y de recursos ya examinados vs candidatos nuevos.

## Bloque 1 · entregado

- `PREGUNTAS_Y_RESULTADOS.csv`: 4 preguntas factuales (M1 reparto capex mantenimiento/crecimiento + «dos tercios» lino plano + plan climático; M2 tasa de bajas de clientes y desembolso inicial por cliente nuevo; M6 finalidad de compras pequeñas y orgánico sin ellas; N2 seguros/bajas 2025, dónde cobró, fiscalidad, reposición) con estado inicial ABIERTO, definición citada (INFORME F1 §6.4 l561-566, §6.1 l480-506, ESPECIFICACION l31/l114 en producto `716cbd6`), salida afectada y límite.
- `FUENTES_Y_BUSQUEDA.csv`: separa YA_EXAMINADO (5 URD/DEU 2021–2025 + libro, conservados en Release base-4.14 con sha256 cruzados; comunicado 2025 y docs S1-2026 usados solo como alcance de búsqueda previa; 92 extractos de páginas del frente) de CANDIDATO_NUEVO_POR_SELECCIONAR (bloque 2).
- `scripts/inventario_bloque1.py`: regenera ambos CSV desde `git show` de SHAs fijados; falla si algún sha256 o el ZIP base-4.14 (sha256 `bb51942c…`) se mueve. Ejecutado: exit 0.

## Commits

- Local: ver `git log --oneline -2` en esta rama. Remoto: `git ls-remote origin mistral/e-fuentes-elis` tras el push de este bloque.

## Pendiente / siguiente acción exacta

1. **Bloque 2:** seleccionar hasta 12 documentos oficiales nuevos por relación con M1/M2/M6/N2 (prioridad: presentaciones oficiales de resultados/CMD, documentos regulatorios AMF, Q&A de IR publicados; buscadores/terceros solo como pistas). Descargar con TLS verificado y registrar por fuente: URL oficial final, título, fecha, ejercicio, idioma, bytes, SHA256, versión y estado real de preservación (PDF/XLSX/ZIP fuera del Git del auxiliar; si el upload a Release falla con 401 se registra provisional y se continúa; no se piden tokens).
2. Leer cabeceras/tablas/notas pertinentes con página PDF y columna, unidad/escala/perímetro/periodo; primera lectura antes de comparar con cifras heredadas; ambigüedades confirmadas con representación visual o segundo extractor; por pregunta registrar hallazgo / qué significa / qué no demuestra / salida afectada; derivas en script con operandos, fórmula, unidades y redondeo.
3. No repetir la búsqueda ya agotada de §6.1 (URD 2016–2023 y 2025, DEU 2024, comunicado 2025, docs S1-2026; términos ya usados) sin pista nueva.
4. **Bloque 3:** `LECTURA_FUENTES.jsonl`, preguntas/resultados actualizados, inventario fuentes/búsqueda, hallazgos/límites, scripts, resumen para el integrador, `ENTREGA.json`, manifiesto y esta recuperación; commit/push por bloque. Cada pregunta termina con evidencia examinada, ambigüedad o «no localizado en esta búsqueda» (nunca «no publicado en ninguna parte»).

## Límites vigentes

- No se elige R (ni dentro de 736,0–867,2), θ, λ, k, probabilidades ni política para desbloquear; Elis sigue `pendiente_de_datos`; C48=108, C49=128,1 y FCF base=307,933 se conservan; no se tocan decisiones E1/D3/E2/E6.
- Una proporción de ventas no es proporción de capex; «dos tercios» de un bloque no se extrapola al total; categoría contable no identifica reposición económica; no suponer que dos magnitudes parecidas son la misma partida (N2).
- No contacto privado con empresas, no comprar acceso, no cambiar credenciales, no pedir tokens en el chat.
- `uploads.github.com` devuelve HTTP 401 en este sandbox (bloqueo documentado en la etapa B): cualquier PDF nuevo queda en cobertura provisional con URL+SHA+bytes+script reproducible.

## Modelo y herramientas

Vibe Code de Mistral AI, modelo `mistral-large-4-0`; consumo no visible desde la sesión. Python 3.12.15 + pypdf/openpyxl/PyMuPDF instalados en la sesión anterior. Red vía urllib con TLS verificado donde aplica (curl bloqueado por el sandbox). Sin LibreOffice ni pipeline.
