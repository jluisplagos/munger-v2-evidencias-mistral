# CONTRASTE_E2_23718fb · revisión del coordinador que emite CORRECCION_E2 (respuesta de Mistral E a E1)

- **Revisión contrastada:** `coordinacion/cierre_v2/revisiones_coordinador/E1_23718fb/` @ `30c314c`: `REVISION_E1_23718fb.md`, `CORRECCION_E2.md`, `sondas/` (18 archivos).
- **Objeto:** rama `mistral/e-fuentes-elis` @ `23718fb` (respuesta E-R1…E-R9) y `f00c5dd` (relevo), carpeta `resultados_cierre/elis_fuentes/`.
- **Veredicto del contraste: CONFORME, con límites de reproducción.** Manifiestos, extractos y la clasificación M6 (E-R2) se verifican; la comprobación 52/52 citas página a página no la reejecuté (requiere descargar los 11 PDF de la Release y el extractor). CONTROL refleja la revisión. Sin hallazgos falsos ni omitidos detectados.

## Sondas propias (verificación sobre `git archive`)

| Comprobación | Resultado mío | Informe |
|---|---|---|
| Manifiesto @ `23718fb` | exit 1; fallan exactamente **2 `.pyc`** (`scripts/__pycache__/…`) | «listaba 2 .pyc» |
| Manifiesto @ `f00c5dd` | exit 0; **49/49 OK** | corregido en f00c5dd |
| `extractos/` @ `f00c5dd` | **32 archivos** | «32/32 extractos coinciden» |
| E-R2 (clasificación M6) | `extractos/urd2025_p306.txt` (URD sha256 `04bfd087…`, 18.963.024 bytes, el de la base 4.14) §4.1.2 lista **seis** adquisiciones importantes de 2025: Bodensee, Bugadería Neutral, Larosé, **Acquaflash (Brasil)**, JP Muller, Adrett — **Lavartex no está**; p.312 «six major acquisitions»; p.341 (Note 2.4) tiene columna propia para cada una de las seis **más Lavartex** y «Other acquisitions» (37,3). Por tanto: «Lavartex no es importante de 2025 y falta Acquaflash» es **correcto** | E-R2 ABIERTO por ese motivo; «comprobado por el coordinador en p.341» confirmado (p.306 + p.341) |
| Conservación | existe la Release `fuentes-elis-e-20261117` («11 PDF verificados») en el auxiliar | E-R6 cerrado con límites |
| 52/52 citas en su página; 32/32 extractos | extractos presentes (32); la verificación página a página de las 52 citas **no reejecutada** (necesita los PDF de la Release + pdftotext/PyMuPDF) | límite |

## Control (CONTROL.json)

E-ELIS: `revision=CORRECCIONES`, `integracion=NO`, `solicitud_revision.estado=RESPONDIDA` con `informe_revision.ruta = …/E1_23718fb/REVISION_E1_23718fb.md` y veredicto «E-R1 y E-R3 cerrados; E-R4…E-R9 cerrados con límites; E-R2 abierto (clasificación por sociedad: Lavartex no es importante de 2025 y falta Acquaflash, comprobado por el coordinador en p.341). 52/52 citas…; 32 extractos coherentes; conservación cumplida» — **coincide con el informe** y con mi verificación de p.306/p.341. Evento en `registro_eventos`. M1/M2/M6/N2 siguen abiertos y Elis `pendiente_de_datos`; nada aceptado sin evidencia.

## Discrepancias

Ninguna en la revisión. Nota menor: el propio extracto de E (`urd2025_p341.txt`) redacta «cada adquisición importante … columna propia (…, Lavartex)», que incluye a Lavartex en la lista de columnas propias aunque no está en la lista de importantes de p.306; la revisión lo corrige usando p.306, así que no es un hallazgo omitido del coordinador.
