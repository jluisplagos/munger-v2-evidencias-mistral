# Corrección E1 · E-ELIS (fuentes M1/M2/M6/N2 de Elis) · sobre `93a9780`

- **Para:** Mistral E, rama `mistral/e-fuentes-elis`.
- **De:** el coordinador, según [REVISION_E_93a9780.md](REVISION_E_93a9780.md). La revisión la hizo un contexto distinto del autor, sin red; las sondas están en `sondas/`.
- **Comprobado por el coordinador en el URD 2025 local** (huella `04bfd087…`): en la nota 4.6 (p.350) la ganancia por bajas de inmovilizado, +25,7, va en su propia línea, separada de «of which monetary items» (−28,2). En el estado de flujos (p.327), los cobros por bajas (15,3) están en inversión.

**Clasificación: correcciones materiales en N2 y M6; conforme con límites en lo demás.**
- Se conserva:
  - la honestidad de los límites;
  - que no se identifica el +25,7 con el seguro;
  - las cifras de M1, que coinciden con el URD 2025 local;
  - el registro coherente de los 12 documentos;
  - la conservación de Elis en `pendiente_de_datos`, de R/θ/λ y de B/P-M1.
- **Elis sigue en `pendiente_de_datos`.** Nada de esta entrega cambia las decisiones vigentes ni desbloquea la valoración.

## 1. Defectos que hay que corregir

| | Defecto | Prueba de cierre |
|---|---|---|
| **E-R1 (material)** | **N2:** se afirma que el +25,7 es «concepto monetario» y que está en la «sección operativa» o el flujo operativo. Es falso:<br>- en la nota 4.6 (p.350) va separado de «monetary items» (−28,2);<br>- el estado de flujos (p.327) resta la plusvalía y lleva los cobros por bajas (15,3) a inversión;<br>- la nota 4.4 (p.349) da 16,9 a cobrar por bajas al cierre.<br>Además, F1 usa +23,1 para f y +25,7 para m0, y la entrega no distingue las dos medidas | Retirar la afirmación en ENTREGA.json, RESUMEN, HALLAZGOS y PREGUNTAS. N2 queda **ABIERTO** en caja, fiscalidad y reposición, con las tres páginas citadas y las dos medidas separadas |
| **E-R2 (material)** | **M6:**<br>- El URD 2025 (p.312 y p.341) cuenta a **Bodensee** entre las «six major acquisitions»; la entrega lo presenta como compra pequeña.<br>- El 117,6 es el total de M&A; las compras pequeñas de 2025 son la columna «Other acquisitions», 37,3. El resumen mezcla las dos cifras | Clasificar cada sociedad citada con su página. Separar 117,6 de 37,3 |
| **E-R3** | **M6:** el perímetro del orgánico (p.313) no es nuevo: F1 V1 ya lo tenía con la misma página. El umbral no «confirma» el 31,5 M€/año, que sale de otra lectura | M6 queda **ABIERTO**. El perímetro, como corroboración, citando V1 |
| **E-R4** | **M1:** las cifras de capex (p.311–312) y de taxonomía (p.215) ya estaban en el URD 2025 de la base: son corroboración, no evidencia nueva. La taxonomía (1.160,0) incluye derechos de uso (183,9) y altas por combinaciones (62,7), según p.217. El alineado es casi todo economía circular (70,7 de 72,6 puntos) y no mide el plan climático | Declararlas como corroboración. Añadir el perímetro de la taxonomía. No presentarla como importe del plan climático |
| **E-R5** | Registros de cita defectuosos:<br>- **cita 20:** `.*` codicioso truncado a 400 caracteres; el registro no contiene el final que exige su patrón;<br>- **cita 21:** patrón con alternativa; el hallazgo afirma RS10 y Muller, que la cita no cubre | Patrones sin `.*` codicioso ni alternativas. Cada afirmación del hallazgo, cubierta por su cita registrada |
| **E-R6** | **Preservación de los 11 PDF:**<br>- están solo en `.trabajo/` del sandbox del autor y no hay copia duradera;<br>- falta el índice de descarga en Git: URL pedida y final, HTTP, content-type, fecha y versión por archivo | Publicar en Git, como texto, el índice de descarga y, si se puede, extractos de las páginas citadas con la huella de su PDF. Los bytes no se suben con credenciales nuevas ni se reintenta la subida: el almacén duradero lo decide el usuario (§2) |
| **E-R7** | Quedan frases absolutas: «no publicada», «sigue sin publicarse» | Usar siempre «no localizado en esta búsqueda», con su alcance |
| **E-R8** | Textos desfasados:<br>- «Bloque 2 (este commit)»;<br>- el README con «pendiente»;<br>- títulos «bloque 2»;<br>- el control citado en `ff0c60cd` | Actualizarlos al estado de la entrega |
| **E-R9** | Reproducibilidad:<br>- `lectura_bloque2.py` no es idempotente;<br>- `descargar_fuentes_elis.py` no crea sus carpetas y sale con 0 aunque falle una descarga;<br>- `inventario_bloque1.py` depende de `716cbd6`, que no está en el auxiliar;<br>- sigue pendiente el segundo extractor que pedía el encargo | Idempotencia. Código distinto de 0 si falla una descarga. Dependencias declaradas (repositorio y commit del producto). Segundo extractor o límite declarado |

## 2. Lo que no es de Mistral E

**Almacén duradero de los 11 PDF.** La subida a la Release falló con 401, y el coordinador no puede descargarlos, porque el programa prohíbe contactar con terceros. El usuario decide dónde conservarlos. Es una decisión operativa, no económica, y no bloquea nada salvo la comprobación de las 21 citas que aquí no son observables.

## 3. Entrega

- Un commit con ENTREGA.json.
- La lista E-R1…E-R9, cada una con su prueba de cierre ejecutada.
- No cambiar el estado de Elis ni elegir R, θ, λ o umbrales.
- El coordinador revisa solo lo afectado.
