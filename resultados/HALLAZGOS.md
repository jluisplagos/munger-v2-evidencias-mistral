# Hallazgos · frente M · Vidrala y Viscofan (26 objetivos, 34 dependencias)

Evidencia propuesta por Mistral; pendiente de revisión e incorporación por el integrador.
Clasificación: [ERROR_DATO] [CONFLICTO_FUENTE] [HIPOTESIS] [LIMITE_COBERTURA]. Ninguno de estos hallazgos edita el XLSX, el registro oficial ni las decisiones.

## 1. [CONFLICTO_FUENTE] Traducción inglesa de Vidrala invierte el sentido de dos rótulos clave
- **Reproducción**: comparar `VIDRALA_EN2025` p.7 con el original español `VIDRALA_ES2025` p.14 (ambos conservados, sha256 en `lectura_fuentes.jsonl`).
  - EN p.7 imprime `Payments from sale of property, plant and equipment (178,746)`; el ES original p.14 imprime `Pagos por la adquisición de inmovilizado material (178.746)`. Son **pagos por adquisición** (salida), no cobros por venta.
  - EN p.7 rotula el subtotal `Cash used in operating activities 799 (84,994)`; el ES original lo rotula `Efectivo generado por las operaciones 799 (84.994)` (mismo signo: +799 en 2025, −84.994 en 2024).
- **Impacto potencial**: leer la versión inglesa al pie de la letra invierte concepto y signo en capex y en el subtotal de circulante (K14/L14). Los valores del libro (positivos en capex, K14=+84,994, L14=−0,799) son coherentes con el español.
- **Qué falta comprobar**: nada para el contraste (el español prevalece y está verificado); queda como aviso para quien lea solo la versión EN.

## 2. [LIMITE_COBERTURA] Paréntesis omitido en la versión EN del subtotal de circulante 2024 (P1)
- **Reproducción**: `VIDRALA_EN2025` p.7 y `VIDRALA_EN2024` p.7 imprimen `Other current liabilities 106,417)` (sin paréntesis de apertura) en la columna 2024. El ES original (`VIDRALA_ES2025` p.14, verificación visual) imprime `(106.417)`.
- **Comprobación aritmética**: 36.800 − 15.655 + 3.916 − 106.417 − 3.638 = −84.994 = subtotal publicado `(84,994)`. El valor es negativo.
- **Estado**: coherente con el registro (P1 ya anotado). No es un error del dato del libro.

## 3. [CONFLICTO_FUENTE] Viscofan: comparativo 2024 reexpresado en AR_2025 (K14)
- **Reproducción**: `VISCOFAN_2025` (AR_2025.pdf) p.27, columna 2024 comparativo, imprime acreedores `−2.953`; el original `CF_2024.pdf` p.9 imprime `−2.639` para el mismo ejercicio 2024. La reexpresión corresponde a la asignación definitiva del precio de Brasfibra y Master Couros (AR_2025 pp. 33 y 37).
- **Efecto**: K14 = −(35.919 − 41.828 − 2.953) = **8,862** con el reexpresado (el que usa el libro); con el original daría 8,548.
- **Decisión ya registrada**: se usa el comparativo reexpresado (regla de construcción: cifra publicada más reciente, mismo criterio que E2/E3). Coincide con el XLSX (K14=8.862). Documentado como conflicto de fuente resuelto, no como error.

## 4. [HIPOTESIS] Vidrala C48 (intereses en financiación): dato ausente, no cero
- **Reproducción**: en `VIDRALA_EN2025` p.7, `VIDRALA_EN2024` p.7 y `VIDRALA_ES2025` p.14 (verificación visual) la sección de **financiación no tiene ninguna línea de intereses**; `Pagos de intereses (20.800)/(32.100)` está en **explotación**. La nota 8 da solo el interés devengado de arrendamientos (2.131/2.179/2.452 miles; CF_2024 p.56, CF_2025 p.52), sin desglosar si va en «Pagos de intereses» o en pagos de deuda.
- **Estado del objetivo**: `HIPOTESIS_O_AUSENCIA` (E4: vacío declarado, no cero no publicado). C48 está vacío (None) en el XLSX; el motor A queda no calculable (C52 sin valor cacheado en Vidrala).
- **Alternativa identificada, NO adoptada**: 2,254 mm = media del interés devengado de arrendamientos (no es un pago publicado).
- **Qué falta comprobar**: consulta a Vidrala (P9-c1) o desglose del ESEF 2025.

## 5. [HIPOTESIS] Vidrala C49 (arrendamientos): el principal no está publicado
- **Reproducción**: nota 8 (CF_2024 p.56, CF_2025 p.52, verificación visual de la página) publica solo el **pago total** (5.861 + 6.117 + 8.314 = **20.292 miles**; media = 20.292/3 = **6.764 miles = 6,764 mm**) y el **interés devengado** (2.131 + 2.179 + 2.452 = **6.762 miles**; media = 6.762/3 = **2.254 miles = 2,254 mm**). No hay fila de principal.
- **Diferencia** (pago total − interés devengado) = 20.292 − 6.762 = **13.530 miles**; media = 13.530/3 = **4.510 miles = 4,510 mm** (4,510333), aproximación del principal — **no acredita el principal pagado**.
- **Estado del objetivo**: `HIPOTESIS_O_AUSENCIA`; el valor 4,5 mm del libro es un supuesto heredado. Alternativas cuantificadas: 6,764 mm (media del pago total, igual que la que construye la fase 1) y ≈4,510 mm (diferencia media). C49 se mantiene como hipótesis.
- **Nota de extracción**: la tabla de resultados por arrendamientos imprime «Expenses related to short-term/low-value 8,314 / 6,117», numéricamente igual a la fila Payments de la tabla de pasivos (confirmado visualmente; no afecta al contraste).

## 6. [HIPOTESIS] Vidrala C50 (pagos basados en acciones): cero no publicado como tal
- **Reproducción**: `VIDRALA_ES2025` p.357, cuadro ii) del informe anual de remuneraciones: todos los planes de los **consejeros** con 0,00. Ese informe no cubre directivos/empleados del grupo; no hay afirmación expresa de ausencia de planes para todo el grupo en 2023-2025.
- **Estado del objetivo**: `HIPOTESIS_O_AUSENCIA`; 0 se mantiene como supuesto (solo afecta al motor A).

## 7. [LIMITE_COBERTURA] Vidrala K14 (E2): cifra publicada mantenida, reserva sobre la plusvalía de Italia
- **Reproducción**: K14 = 84,994 mm (subtotal 2024, verificado). En 2024 la venta de Italia cobró 230.000 miles en inversión (CF_2025 p.7) con plusvalía de 50.547 (60.065 discontinuadas − 9.518); ninguna línea de ajustes la elimina de forma explícita.
- **Decisión registrada (E2)**: mantener K14 = +84,994 publicado; la reserva sobre la plusvalía (alternativas ≈34,447 / ≈33,594) queda aparte y **no** se descuenta. No se trata como error del dato.

## 8. [LIMITE_COBERTURA] Numeración de páginas del AR_2025 de Viscofan
- La página impresa difiere de la página PDF (p. PDF 23 = impresa 3; p. 27 = impresa 7; p. 28 = impresa 8; p. 76 = impresa 68; p. 83 = impresa 75). En `lectura_fuentes.jsonl` se registran ambas. No afecta a las cifras.

## 9. [LIMITE_COBERTURA] Celdas del XLSX son valores hardcodeados; C48 de Vidrala vacío
- **Reproducción**: lectura solo lectura con openpyxl de `Vidrala_v63_evaluada.xlsx` (sha256 82ff7fb8…) y `Viscofan_v63_evaluada.xlsx` (sha256 95a78291…): las 26 celdas objetivo contienen valores literales (no fórmulas); solo C52/C59 aguas abajo son fórmulas. `Análisis!C48` de Vidrala es `None` (vacío), coherente con E4; en Viscofan C52 cachea 97,219 y en Vidrala C52 queda sin valor (motor A no calculable por C48 vacío).
- **Derivados**: todos los recalculados desde fuentes coinciden con el libro a 3 decimales (redondeo E1): C46 335,413333→335,413; C47 169,667667→169,668; Viscofan C46 192,300333→192,3; C47 77,533333→77,533; C48 8,294 exacto; C49 5,547333→5,547; C50 3,707333→3,707; C55 exactos (35,182858 / 45,993399).

## Resumen de estados (26 objetivos)
- `COINCIDE_EN_REVISION_MISTRAL`: 23
- `HIPOTESIS_O_AUSENCIA`: 3 (Vidrala C48 dato ausente, C49 y C50 hipótesis)
- `DIFERENCIA`: 0 · `NO_ACREDITADO`: 0

No hay hallazgos de error en los datos publicados dentro del universo fijado; los puntos 1-3 son avisos de lectura de la versión inglesa y de reexpresión, y los 4-7 son las ausencias/hipótesis ya declaradas en el registro (E4, C49, C50, E2), ahora verificadas contra los PDF conservados.

## Correcciones aplicadas tras la revisión externa del commit `6b53ef9`

La primera lectura queda conservada íntegramente en el historial (commits `5641bec` y `b278727`); las correcciones se publican en un commit nuevo sobre la misma rama. Auditoría aritmética determinista (`auditar_aritmetica.py`): todas las sumas, medias y conversiones pasan; el único error detectado fue el de C49.

1. **Vidrala C49**: `valor_leido` corregido de 20.492 a **20.292** miles (5.861+6.117+8.314); medias recalculadas: pago total **6.764 mm**, interés devengado **2.254 mm**, diferencia **4.510 mm** (13.530/3). Se retira la atribución de la diferencia con el registro a «otros operandos»: 6,764 mm es exactamente la media del pago total con los mismos operandos. C49 sigue como **hipótesis** (restar el interés devengado no acredita el principal pagado).
2. **Vidrala Historia!L7**: corregida la explicación — el EBIT publicado de 292.068 miles **incluye** el deterioro de 2.362 miles (línea anterior al EBIT en la cuenta de resultados, p.4); sin él sería 294.430 miles. La línea L8 (D&A del estado de flujos) **sí** excluye el deterioro (línea aparte del ajuste, p.7).
3. **Vidrala Historia!L14**: nota corregida a «−799 miles = −0,799 millones».
4. **C55 de Vidrala**: retirada la atribución a D3 (D3 es la decisión de Viscofan: 46.500.000 − 506.601 = 45.993.399).
5. **Recuperación y resumen**: la rama `mistral/fuentes-vm-01` y sus commits ya están publicados en el auxiliar; el presupuesto de 25 EUR se presenta como **recomendación del encargo**, no como configurado (no se puede comprobar desde la sesión).
