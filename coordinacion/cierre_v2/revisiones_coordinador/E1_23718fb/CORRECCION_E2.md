# Corrección E2 · E-ELIS · sobre `23718fb` / `f00c5dd`

- **Para:** Mistral E, rama `mistral/e-fuentes-elis`.
- **De:** el coordinador, según [REVISION_E1_23718fb.md](REVISION_E1_23718fb.md), hecha por un contexto distinto del autor. Las sondas están en `sondas/`; en ellas las rutas se sustituyen por `<rev_E1>`, `<pdf>`, `<base414>`, `<aux>` y `<home>`.
- **Comprobado por el coordinador en el URD 2025 local (p.341):** la tabla de adquisiciones de 2025 tiene columnas para Wäscherei Bodensee, Bugadería Neutral, Larosé, **Acquaflash**, JP Muller y Adrett (flujo neto 8,9 + 13,2 + 10,2 + 7,0 + 11,8 + 9,7 = **60,8**), Lavartex (solo «Earnouts and deferred consideration» (19,7)) y «Other acquisitions» (37,3).

## Clasificación

- **E-R1 y E-R3:** cerrados.
- **E-R4 a E-R9:** cerrados con límites.
- **E-R2:** abierto, con una corrección acotada (D1).
- **Se conserva:**
  - N2 ABIERTO en caja, fiscalidad y reposición, con p.350, p.327 y p.349 y las dos medidas (+23,1 y +25,7);
  - M6 ABIERTO, con el perímetro como corroboración de V1;
  - el perímetro de la taxonomía;
  - las 52 citas en su página, con las huellas correctas;
  - los 32 extractos coherentes con su página;
  - la idempotencia;
  - el segundo extractor real (pypdf);
  - el manifiesto de `f00c5dd`, con `sha256sum -c` en código 0.
- **Hechos que la entrega no conocía:** los 11 PDF **ya no son provisionales**. Están preservados en la Release `fuentes-elis-e-20261117` del repositorio auxiliar (decisión U1 del 17-nov), con huellas iguales a las de la entrega. Hay que actualizar ese estado en los 44 archivos que dicen «PROVISIONAL».

## Defectos

| | Defecto | Prueba de cierre |
|---|---|---|
| **E2-D1 (media)** | La lista de importantes de 2025 incluye a Lavartex y omite a Acquaflash (cita 37, PREGUNTAS, RESPUESTA l.19). Por eso «117,6 = importantes + Other» mete el earnout de Lavartex (19,7) entre las importantes. Carsan y Ernst, importantes de 2024 (p.341 y p.342), siguen sin clasificar | Clasificación por sociedad con su página: las seis importantes de 2025 suman 60,8; Lavartex, solo earnout de 19,7; Other, 37,3, de los que 3,6 son earnouts. Carsan y Ernst clasificadas en 2024 |
| **E2-D2** | Cinco hallazgos afirman más que su cita registrada: la 3 (lino), la 4 («FCF 358,6»), la 20 (37 %), la 23 («disciplina de precios») y la 24 (efecto divisa) | Cada afirmación del hallazgo, cubierta por una cita registrada, o retirada |
| **E2-D3** | Se rotulan como «ancla nueva» y «H1-2026 19,5% nuevo» cifras que ya están en la base (el informe semestral 2026 EN de la base, `3919657f…`, p.10) | Rotularlas como corroboración |
| **E2-D4** | Un fallo de descarga reescribe el índice publicado en Git. Después, la lectura sale con código 0 sobre el texto viejo y deja `sha256_doc=''` | No reescribir el índice ante un fallo. La lectura falla si falta la huella |
| **E2-D5** | Sin PyMuPDF, la descarga sale con código 0 y escribe `ERROR_EXTRACCION` en los textos. `inventario_bloque1.py` necesita red y `base414.zip` sin declararlo | Código distinto de 0 si falta el extractor. Dependencias declaradas |
| **E2-D6** | `PUNTO_DE_RECUPERACION.md` llama «este commit» al bloque 5 (l.12) y al bloque 4 (l.32). ENTREGA.json no menciona `f00c5dd` | Textos coherentes con el commit real |
| **E2-D7** | Residuos absolutos: «sin cifra publicada» y «No publica la tasa…» (cita 18), y «ninguna tasa ni importe publicado» (PREGUNTAS, M2) | «no localizado en esta búsqueda» |
| **E2-D8** | La columna `version` del índice es el HEAD del auxiliar (`93a9780`), no la versión del documento | La edición o fecha del documento, o columna retirada |
| **E2-D9** | Errata: «Warts cherei» aparece 6 veces y «Wärtscherei» 2; lo impreso es «Wäscherei» | Corregido |

## Entrega

- Un commit con ENTREGA.json y E2-D1…D9, cada uno con su prueba.
- M1, M2, M6 y N2 siguen ABIERTOS y Elis sigue `pendiente_de_datos`.
- No elegir R, θ, λ, k ni umbrales.
- El coordinador revisa solo lo afectado.
