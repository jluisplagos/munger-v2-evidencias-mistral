# Contraste independiente F-REV · C20 (U1–U6 del verificador) @ bf0d5c2 (base d519eb0)

- **Revisor**: sesión Mistral C/F distinta del autor (Claude Opus 5.5 según firma del commit). Modelo real: `mistral-large-4-0` (Vibe Code). Herramientas: `gh` CLI + Python 3.12 stdlib + shims locales de `pdftotext`/`pdfinfo` (ver §2; poppler no está instalado en el sandbox y no se instaló nada). Esfuerzo/consumo no visibles; no declarados.
- **Objeto**: commit `bf0d5c25d136ae9b2b1f14e4688081e1792d2363`, padre `d519eb04978e64d04f1d1795c570ca96bdd7ad7f` (base fijada en la solicitud). Diff vía API: **12 archivos, todos bajo `docs/validacion_economica_paralela/frente_E_F1_elis/`**; `datos/cifras_fuente.csv` **no cambia** (no se añade ninguna fila al CSV). Nada del producto fuera de esa carpeta.
- **Solicitud**: CONTROL.json @ `coordinacion/cierre-v2`, tarea C20, `solicitud_revision.estado = LISTA`, 5 criterios. Fecha de consulta: 2026-11-16 ~21:17–21:35 UTC.

## 1. Veredicto por criterio

### U1 (posiciones desde la tokenización) — CUMPLE, defect Y corrección reproducidos por mí

- Diff de código acotado a U1–U6 (ninguna línea toca tolerancias/umbrales: grep del diff → ninguno; `evidencias/c20/diff_verificar_cifras_d519eb0_vs_bf0d5c2.txt`): `tokens_con_posicion` nuevo y `spans_numericos` ahora deriva las posiciones de la tokenización en vez de `linea.find`.
- Sonda propia sobre la línea exacta citada por la revisión 9 (`as at 12/31/2025      0      92,485`): **C18 (d519eb0) coloca el primer `0` en el carácter 13, dentro de `2025`**; **C20 lo coloca en el 22, su celda real**. Lo mismo en la línea francesa (`au 31/12/2024  0  26 718 …`: C18 char 10 dentro de la fecha, C20 char 15) y en `Number of fatal accidents  0(a)  0  0` (U2a: C18 mete el `0` dentro de `0(a)`, C20 no). `evidencias/c20/probes_c20_out.txt`.
- Los casos U1a/U1b/U1d/U2a/U2b sobre páginas reales (URD2025 p.360, DEU2024FR p.306, URD2021 p.176) **no son re-ejecutables en este sandbox** (esas páginas no están entre las 73 exportadas hash-ligadas y no hay poppler); quedan cubiertos por el test del autor (143/143 publicado) y por mis sondas sintéticas equivalentes. Límite declarado, no defecto.

### U2 (decisión declarada: recuentos con fecha toman el ejercicio de su fecha) — CUMPLE

- T14 e informe §1 declaran la decisión con fecha y referencia («Precisión de C20 (revisión n.º 9, U2, decisión declarada): los recuentos con fecha cuyo rótulo es la fecha **sí toman el ejercicio de su fecha**…»), coherente con el código (la rama de saldo ya daba el ejercicio de la fecha; lo que cambia es que no queden OK por unidad/columna). Verificado en el parche de ESPECIFICACION/INFORME vía API. El caso U3b (URD2022 p.294) espera ejercicio OK + fila PENDIENTE en ambas versiones — coherente.

### U3 y U5 b/d declarados como límites — CUMPLE

- El parche añade a T14/informe §1: «(C20, revisión n.º 9, U3 y U6 e) los límites… la columna se cuenta en los tokens de la fila, no en las columnas de la tabla (U3); la búsqueda de la cabecera por países salta siempre la línea de una sola celda justo encima de una fila de datos (U5 b); … (U5 d)». Coincide con la RESPUESTA_REVISION_9_C20.md.

### U4 / U5 a / U5 c — CUMPLE, con reproducción end-to-end en páginas reales cuando hay export hash-ligado

- **U4**: `rotulos_sin_rotulo` aplica el mismo criterio que `rotulo`. Sondas sintéticas: `5      3` entre rótulos pasa a tener rótulo contiguo en C20 (C18: no); `3   Report on corporate governance…` sigue sin ser fila sin rótulo en ambas. Coincide con el test.
- **U5 c**: nueva `es_pie_de_pagina` + rama en la fila; sondas: detecta `Elis | Universal Registration Document 2022 | 259` y no `Revenue  2022  259`; `token_del_rotulo` distingue el `1` de `As at January 1` (C18: None). **End-to-end real**: U4a (URD2022 p.261, folio 259 declarado 2021) da **C18 OK → C20 PENDIENTE «el token está en el pie de página»**, exactamente lo que propone la revisión 9; U5a (URD2022 p.284, `(54.3)` declarado 2022) da **OK en ambas**, sin cambio. Mini-runs con CSV propio sobre las páginas exportadas hash-ligadas (`evidencias/c20/probes_c20_out.txt`).
- **U5 a**: nueva regla de rótulo con `published/reported/publié` → FALLO en edición vigente; sonda sobre la línea sintética `As at December 31, 2019, published  609.3 …` la detecta (C18 no tenía la rama). El caso real U3e (URD2021 p.257) espera FALLO en edición en ambas — coherente.

### 752 filas reales byte a byte; test 143/143 y 13/13; sin cambiar tolerancias ni políticas — CUMPLE (con un límite de entorno declarado)

- **Autor-side**: `verificacion_cifras.json` @ bf0d5c2 y @ d519eb0 tienen la **misma sha256** (`f17bd8c5…`) → salida byte a byte idéntica entre base y C20. `cifras_fuente.csv` no está en el diff (sin filas nuevas). Test log publicado: `143/143 casos` y `13/13 comprobaciones directas`. Barrido fecha-rótulo: 207 líneas, «solo la versión nueva: 0 / solo la anterior: 0». Sondas metadatos C20: 752 filas, 738 OK / 14 PENDIENTE / 0 FALLO.
- **Mi rerun independiente**: PDFs reales extraídos del ZIP `base-4.14` (sha256 == las declaradas en `fuentes.json` para las 5 fuentes) + shim de `pdftotext`/`pdfinfo` que sirve las **73 páginas exportadas hash-ligadas** (`evidencias/paginas/*.txt`, cabecera `# SHA-256:` verificada contra el PDF) y, solo para páginas de contexto previas no exportadas, el texto completo conservado. Resultado: **736/752 filas byte a byte idénticas** a lo publicado — **todas las 713 filas de tabla y 23 de texto**; las 16 restantes son filas `tipo=texto` cuyo literal solo aparece con `pdftotext` en **modo raw** (no `-layout`), que no existe en este sandbox: fallan solo en mi entorno, no por C20. Ninguna fila de tabla difiere. Detalle: `evidencias/c20/rerun_752_y_hashes.txt`.
- **Test 143/143 no re-ejecutado completo**: 52 de sus páginas reales no tienen export por página hash-ligado en el repo (solo 73 existen) y no hay poppler; no fabrico datos. Las 4 comprobaciones directas nuevas (U1, U4 ×2, U5 c) sí las re-ejecuté como sondas equivalentes (todas correctas). Límite de independencia declarado.
- **Sin cambios de tolerancias ni políticas**: diff de `verificar_cifras.py` sin ninguna línea de tolerancia/umbral; el diff del test solo añade los 7 casos de la revisión 9 y las 4 comprobaciones directas (`evidencias/c20/diff_test_verificar_cifras.txt`).

## 2. Método y límites

- No se ejecutó LibreOffice, el pipeline, macros ni el producto; solo el verificador de cifras sobre copias aisladas. Los shims sustituyen a poppler sirviendo texto **hash-ligado a los PDF reales** (la cabecera de cada página exportada contiene el SHA-256 del PDF y el shim lo verifica); es una sustitución de motor de extracción, no de datos.
- Los tests del autor se usaron solo como referencia publicada; mis sondas no importan su lógica salvo cargar el propio módulo del verificador en dos versiones (d519eb0 vs bf0d5c2) para comparar comportamiento.
- No se revisó CSV (sigue PENDIENTE/POR_PREPARAR en CONTROL.json) ni se reabrió ninguna revisión anterior.

## 3. Defectos materiales

**Ninguno.** No hay contraejemplo mínimo que construir: cada cambio U1–U6 se comporta como propone la revisión 9 en las sondas ejecutables, y la salida real no cambia en ninguna fila de tabla.

## 4. Estado y siguiente acción

- Nada adoptado fuera de la carpeta del frente F1; producto intacto. Mi rama sigue `mistral/f-alcance-real`; no toco `mistral/m2-matematica-b` ni otros frentes.
- CONTROL.json re-consultado tras este bloque: C20 pasa a contraste hecho por mí (este informe); CSV sigue pendiente → siguiente tarea independiente de la cola: **B-PM1 @ daa7478** (contraste documental de las altas PP&E de Vidrala), luego F-B3/F-C1.
- El coordinador registra aceptación; yo no me autoaprobo.

*Propuesta de evidencia o especificación de Mistral; pendiente de revisión e incorporación por el integrador. No APROBADO ni aptitud financiera general.*
