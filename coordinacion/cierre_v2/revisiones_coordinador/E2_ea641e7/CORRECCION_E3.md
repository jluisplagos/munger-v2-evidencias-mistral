# Corrección E3 · E-ELIS · sobre `ea641e7`

- **Para:** Mistral E, rama `mistral/e-fuentes-elis`.
- **De:** revisión independiente [REVISION_E2_ea641e7.md](REVISION_E2_ea641e7.md), hecha por un contexto distinto del autor. Las sondas están en `sondas/`.
- **Estado de E2:**
  - D4, D6, D7, D8 y D9 están cerrados;
  - D5 está cerrado, con un residuo documental (E3-5);
  - D1, D2 y D3 están cerrados con límites.
- **Se conserva:**
  - la clasificación por sociedad de M6 (seis importantes = 60,8; Lavartex solo earnout 19,7; Other 37,3 con 3,6 de earnouts; redondeo 0,2; Carsan y Ernst importantes de 2024);
  - las 68 citas con huella correcta;
  - la preservación verificada en la Release;
  - el manifiesto;
  - las guardas D4/D5;
  - M1, M2, M6 y N2 ABIERTOS, y Elis `pendiente_de_datos`.

## Defectos

| | Defecto | Prueba de cierre |
|---|---|---|
| **E3-1 (media)** | Factsheet 2026 p.1 (LECTURA l.35, PREGUNTAS M2, HALLAZGOS l.15, `lectura_bloque2.py` l.134). La cita `4-year contracts: Monthly fixed fee` casa por el orden de extracción. Lo impreso es «4-year contracts: Volume-based **or** Monthly fixed fee», una banda común a las tres actividades. Por eso «contratos de 4 años con tarifa fija mensual (workwear…)» no es lo que dice la página | Patrón atómico que case con lo impreso en orden de lectura («Volume-based», «or», «Monthly fixed fee»), comprobado también con un extractor que respete la maquetación (p. ej. poppler) o con la página renderizada. Hallazgo reescrito como «contratos de 4 años por volumen **o** cuota mensual fija», sin atribuirlo a Workwear |
| **E3-2 (media)** | En modo `ELIS_PDF_DIR`, `descargar_fuentes_elis.py` (l.92–99, l.113, l.169–172) reescribe el índice de Git con `http = 200`, `url_final` y `fecha_descarga = now()` sintéticos. La marca real de la descarga (08:43:57Z de `f00c5dd`) quedó sustituida por 13:22:28Z en el índice, LECTURA, FUENTES y los 33 extractos. Además, dos ejecuciones seguidas dan índices distintos | Restaurar desde `f00c5dd` los campos de procedencia de las 12 filas (`fecha_descarga`, `http`, `url_final`, `content_type`) sin tocar las huellas. En modo local, no reescribir el índice de Git, o registrar `modo/origen` sin falsear la descarga. Negativo: dos ejecuciones locales seguidas dejan el índice de Git byte-idéntico |
| **E3-3 (menor)** | La cita 45 (LECTURA l.57; `lectura_bloque2.py` l.224) dice «37,3 = compras pequeñas 2025», pero la columna Other de p.341 incluye 3,6 de earnouts y aplazados | «37,3 = columna "Other acquisitions" (33,6 de compras netas de caja + 3,6 de earnouts/aplazados)» |
| **E3-4 (menor)** | Residuos de D3: `PUNTO_DE_RECUPERACION.md` l.17 («H1-2026 19,5% nuevo»); la cita 2 (LECTURA l.14, brochure p.15) sin rótulo de corroboración de URD p.312 | Rotularlas como «corroboración (documento nuevo, cifra ya en base)» |
| **E3-5 (menor)** | `pruebas_e2/NEGATIVOS_E2.txt` l.19 y l.24 registran «exit=0 (esperado 3)» para D5a/D5b | Registro con el código de salida real del proceso (3) |

## Opcional

- **E3-6:** citar la nota 5 de la presentación FY2025 p.29 («Final earn-out related to the 2022 Mexican acquisitions paid in 2025 (€20m vs. €83m in 2024)») para identificar la compra anterior del 19,7.
- Actualizar los recuentos de `RESUMEN_PARA_INTEGRADOR.md` l.21 (80 registros, 68 citas).

## Entrega

- Un commit sobre `ea641e7` con E3-1…E3-5, cada uno con su prueba, y el manifiesto regenerado (`sha256sum -c` en código 0).
- No cambiar huellas ni fuentes. Conservar C48 = 108 y las decisiones vigentes.
- M1, M2, M6 y N2 siguen ABIERTOS y Elis sigue `pendiente_de_datos`. No elegir R, θ, λ, k ni umbrales.
- El coordinador revisa solo lo afectado.
