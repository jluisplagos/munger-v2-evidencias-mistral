# Cierre dirigido del frente M de fuentes · 16-nov-2026

**Resultado: utilizable como propuesta de evidencia corregida para el integrador, dentro de los 26 objetivos fijados.** No es aceptación del producto ni aptitud financiera de un expediente. No se fusiona ni modifica Munger V2.

## Material

- Preparación: commit `e137b854dc592bcad9ed3e51275f7b80d35d210e` de este auxiliar; fuente histórica `059f4f68dca7acf465b5f5b21de2dede84c885ff` y binarios base 4.14.
- Entrega inicial de Mistral: `6b53ef9f67dc4519cfd9a64bcf21e40f08baa120`.
- Corrección de Mistral revisada: `44641ff842133f3940ec9743944c0e74c1fcd050`.
- Esta rama de revisión parte de esa corrección. La rama de Mistral se conserva sin modificar.

## Comprobaciones y correcciones

La revisión anterior comprobó 15 insumos y las huellas PDF/texto citadas; la cobertura exacta de 60 observaciones (26 objetivos y 34 dependencias); los 23 objetivos numéricos recalculados desde sus observaciones frente a los XLSX; y el manifiesto y estructura de la entrega. También releyó páginas concretas de los PDF: Vidrala EN2025 p.4 y p.52, EN2024 p.56; Viscofan AR2025 p.23 y p.27 y CF2024 p.9. No fue una nueva auditoría semántica de todos los datos de las empresas.

Se ha leído el diff completo de las correcciones, comprobando en particular:

1. Pagos de arrendamiento: 5,861 + 6,117 + 8,314 = **20,292 millones**; media **6,764 millones**.
2. Intereses devengados: 2,131 + 2,179 + 2,452 = **6,762 millones**; media **2,254 millones**. Diferencia media **4,510 millones**. No se convierte en principal pagado acreditado y C49 sigue siendo hipótesis.
3. El EBIT de Vidrala de 292,068 millones **incluye** el deterioro de 2,362 millones; sin ese gasto sería 294,430. D&A en L8 excluye el deterioro presentado aparte.
4. La conversión de L14 queda como −799 miles = −0,799 millones.
5. Se retira la atribución de C55 de Vidrala a D3, decisión de Viscofan.
6. Los textos reflejan la publicación real de la rama. Los 25 EUR se presentan como recomendación, no como presupuesto cuya configuración se haya comprobado.

La corrección de Mistral dejó **dos restos textuales de «4,510333»** junto a la cifra correcta. Esta revisión los retira en `lectura_fuentes.jsonl` y `HALLAZGOS.md`, actualiza las referencias de huella actuales y regenera el manifiesto. No cambia los valores ni estados de ningún objetivo, las decisiones o los libros.

Se ejecutó nuevamente el comprobador de estructura: PASA, con las huellas conformes. Se comprobó que continúan exactamente 60 observaciones y 26 objetivos. Solo tres observaciones difieren de la entrega inicial, precisamente las corregidas; los estados y valores de los 26 objetivos se conservan. Los resultados dirigidos se guardan en `COMPROBACIONES_CIERRE.json`.

## Uso permitido de esta evidencia

- Leer resultados de esta rama/commit concreto; conservar su procedencia, documentos y huellas.
- Contrastarlos con el código, los libros y la fecha de corte de la futura regeneración. La coincidencia con una base histórica no acredita automáticamente un expediente nuevo.
- Reutilizar citas y cálculos que el integrador acepte; mantener diferenciados los 23 objetivos numéricos y las tres ausencias/hipótesis.
- Antes de convertir cualquier observación en una entrada oficial comprobada, aplicar el contrato vigente de extracción y revisión. Esta entrega no lo sustituye ni sella el registro oficial.

No se ejecutaron LibreOffice ni el pipeline, no se regeneraron expedientes, no se corrigió F1 y no se adoptó una política económica. «100% de tokens numéricos presentes» es una comprobación de correspondencia, no prueba suficiente del concepto, columna o perímetro. El integrador debe conservar estos límites.

El encargo finito de preparación de evidencia se puede dar por completado con este alcance y límites. No se requiere otra ronda de Mistral para retirar los dos restos textuales ya corregidos aquí.
