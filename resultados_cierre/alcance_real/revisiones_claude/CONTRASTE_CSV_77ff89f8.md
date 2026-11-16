# Contraste independiente F-REV · bloque CSV @ 77ff89f8 (base bf0d5c2)

- **Revisor**: sesión Mistral C/F distinta del autor (Claude Opus 5.5). Modelo real: `mistral-large-4-0` (Vibe Code). Herramientas: `gh` CLI, Python 3.12 stdlib, shims locales de `pdftotext`/`pdfinfo` (páginas exportadas hash-ligadas a los PDF reales) y de `openpyxl` (lectura solo-valores del libro XLSX real). No instalé nada; no ejecuté LibreOffice ni el pipeline.
- **Objeto**: commit `77ff89f8fe99a1b5f013243ea1ccd4b84512ac51`, padre `bf0d5c25d136ae9b2b1f14e4688081e1792d2363`. Diff vía API: 19 archivos, todos bajo `docs/validacion_economica_paralela/frente_E_F1_elis/` (CSV +10 filas, 6 páginas nuevas, resultados, copia_investigacion_f1.py, textos solo con recuentos, MANIFIESTO, PUNTO_DE_RECUPERACION, README). **El verificador no cambia**: sha256 de `verificar_cifras.py` idéntico en bf0d5c2 y 77ff89f8 (`06da865b…`).
- **Solicitud**: CONTROL.json @ `coordinacion/cierre-v2`, tarea CSV, LISTA, 4 criterios. Fecha: 2026-11-16 ~21:33–21:50 UTC.

## Veredicto por criterio

### 1. Diez filas nuevas OK con el verificador sin cambios; las 752 anteriores no cambian — CUMPLE, reproducido

- Diff del CSV: **exactamente 10 ids nuevos** (FIN_ACTMEX_2025/2024, FIN_ACTMEX_FR_2023/2024, OOIE_EARN_U22_2021/2022, OOIE_EARN_U23_2022, ADQ_EARNDIF_FR_2023, ADQ_EARNDIF_2024/2025), **0 de las 752 cambiadas**; todas tipo=tabla, perímetro grupo, nota «[LECTURA] pasada al CSV… no se aplica a N1».
- Mi rerun del verificador (código idéntico) sobre las 762 filas con los PDF reales (sha256 == `fuentes.json`) y las **79 páginas exportadas hash-ligadas** (73 + 6 nuevas): **las 10 nuevas dan OK en mi run**, y 746/762 filas son byte-idénticas a lo publicado (las 16 restantes son las mismas filas `tipo=texto` que en C20, limitadas solo por la ausencia de poppler en modo raw en este sandbox). De las 752 anteriores, 736 son idénticas a la salida publicada @bf0d5c2 (mismas 16 de texto). Resumen publicado @77ff89f8: 762 filas, 748 OK, 14 PENDIENTE, 0 FALLO. Evidencia: `evidencias/csv/rerun_csv_y_hashes.txt`.

### 2. Las seis columnas por sociedad no se presentan como grupo; un intento de declarlas grupo no queda OK — CUMPLE, reproducido con mutantes propios

Reconstruí los cuatro controles negativos del autor sobre las páginas exportadas (`evidencias/csv/mutantes_out.txt`):
- Lavartex 2023 (31,4) (DEU 2024 p.288) y «otras adquisiciones» 2024 (10,7) (URD 2025 p.342) declaradas como total del grupo → **PENDIENTE, «el token no está bajo ninguna columna reconocida»** → no queda OK.
- 5,6 declarado 2025 → **FALLO ejercicio** «la columna es de 2024, no de 2025».
- 2,1 del URD 2022 (pre-reexpresión) declarado vigente → **FALLO edición** «la regla exige la publicación 2023 para 2022».
Coinciden con la tabla §3 de la respuesta del autor. Límite declarado por el autor y confirmado: la columna por sociedad queda PENDIENTE, no FALLO (el contraste no la usa porque solo calcula sin FALLO y lista las PENDIENTE usadas aparte).

### 3. Contraste sin cambios (292/0, salida idéntica) y copia de investigación con las filas verificadas — CUMPLE, reproducido byte a byte

- `contraste_f1.json` @77ff89f8 es byte-idéntico al de bf0d5c2 (mismo sha256 `147f4f49…`).
- Re-ejecuté `contraste_f1.py` @77ff89f8 con CSV nuevo + verificación publicada + **libro real** `Elis_v63_evaluada.xlsx` (sha256 `d2593777…92385` == la exigida por el script) + `caja_no_nula.json`, leyendo el XLSX con un shim stdlib de openpyxl (solo valores cacheados): **exit 0, 292 comprobaciones, 0 fallidas, salida JSON byte-idéntica a la publicada**.
- Re-ejecuté `copia_investigacion_f1.py` @77ff89f8 con los mismos insumos + `--raiz` (PDFs): **exit 0, 67 controles, 0 fallidos, salida byte-idéntica a la publicada** (8 lecturas nuevas desde las filas verificadas; las sensibilidades V3–V4 quedan así con las mismas cifras al ser el JSON idéntico).
- `cobertura_por_mutacion.txt` @77ff89f8: 538 filas vigentes mutadas, «no declarada/no usada: 119», «usadas y no declaradas: 0» — coherente con el texto. `sondas_metadatos_CSV.json`: 762 filas / 723 de tabla, sondas externas detectadas.

### 4. N1 no se aplica; no se adopta (1a)–(5b); C48/C49/FCF/E1-D3-E2-E6 se conservan — CUMPLE

Los cambios de texto son solo recuentos (752→762, 530→538, 111→119) y el enlace al README; las 10 filas llevan nota «no se aplica a N1»; nada de decisiones adoptado; Elis sigue `pendiente_de_datos`; el diff no toca ningún archivo fuera de la carpeta del frente F1.

## Defectos materiales

**Ninguno.** No hay contraejemplo que construir: cada criterio se reprodujo o se verificó documentalmente con hashes.

## Límites

- Las 16 filas `tipo=texto` no se reproducen en este sandbox (falta poppler en modo raw); no afectan al bloque CSV (las 10 nuevas son de tabla) y quedan cubiertas autor-side por hashes idénticos entre commits.
- El shim de openpyxl lee solo valores cacheados (`data_only=True`); la salida byte-idéntica del contraste y de la copia lo valida para este libro.
- No re-ejecuté `test_verificar_cifras.py` completo ni `cobertura_por_mutacion.py` (mismas razones de entorno que en C20: páginas sin export hash-ligado + ausencia de poppler); sus salidas publicadas no cambiaron salvo los recuentos coherentes.
- No se revisa B-PM1 aquí; es la siguiente tarea independiente de la cola.

## Estado

Rama `mistral/f-alcance-real`; nada adoptado; producto intacto; frente C intacto. CONTROL.json re-consultado tras el bloque. Siguiente: **B-PM1 @ daa7478** (contraste documental de las nueve altas PP&E de Vidrala), luego F-B3/F-C1.

*Propuesta de evidencia o especificación de Mistral; pendiente de revisión e incorporación por el integrador. No APROBADO ni aptitud financiera general.*
