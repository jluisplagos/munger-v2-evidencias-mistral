# Comandos ejecutados · bloque F-REV (rama mistral/f-alcance-real)

Horas reales obtenidas de los propios commits (`git log --format=%ad`, UTC); las horas que había
antes aquí eran estimaciones posteriores a los commits y no coincidían con ellos (F2-D6).
Bloque F-REV: commits 90329a1 2026-11-16T21:16:13Z (F1 W1–W3), e94ee7c 21:32:34Z (C20),
c7716a0 21:42:17Z (CSV). Entorno: sandbox `/workspace`, repo auxiliar clonado en
`/workspace/github__jluisplagos__munger-v2-evidencias-mistral`. El sandbox **bloquea `git remote add`**;
todo el contenido del producto (`jluisplagos/munger-v2`, solo lectura) se obtuvo con `gh api`.
Python 3.12, solo stdlib. No se ejecutó el producto, LibreOffice, el pipeline ni macros.

## 1. Estado y control

```bash
git status --short --branch                 # mistral/f-alcance-real @ ff0c60c
git fetch origin coordinacion/cierre-v2      # CONTROL.json remoto
git show FETCH_HEAD:coordinacion/cierre_v2/CONTROL.json   # F1-W: ENTREgado @ d519eb0, revision LISTA, criterios W1/W2/W3 + conservacion; C20/CSV PENDIENTE
```

## 2. Identificación del diff (producto, solo lectura)

```bash
gh api repos/jluisplagos/munger-v2/commits/d519eb04978e64d04f1d1795c570ca96bdd7ad7f \
  --jq '{sha, message, parents: [.parents[].sha]}'          # parent = 716cbd6... (base fijada)
gh api "repos/jluisplagos/munger-v2/compare/716cbd6794b7fcde8b3862c9d1e7acdaf516d262...d519eb04978e64d04f1d1795c570ca96bdd7ad7f" \
  --jq '.files[] | [.filename,.status,.additions,.deletions] | @tsv'   # 15 archivos, todos bajo docs/validacion_economica_paralela/frente_E_F1_elis/
gh api "repos/jluisplagos/munger-v2/compare/716cbd6...d519eb0" --jq '.files[] | select(.filename|test("PROPUESTA_DECISIONES|V1_V11|README")) | .filename + "\n" + .patch'  # textos: "no adoptada ni implementada"; FCF 307,933 / C48=108 / C49=128,1 sin cambios
```

## 3. Descarga de artefactos del autor y de los dos archivos del producto en la base

```bash
# contenidos via API (el path correcto en el arbol git incluye la raiz munger_v2_r1/)
gh api "repos/jluisplagos/munger-v2/git/trees/716cbd6794b7fcde8b3862c9d1e7acdaf516d262?recursive=1" --jq '.tree[].path' | grep -E 'comprobar_gramatica\.py|patch_v62_base\.py'
gh api "repos/jluisplagos/munger-v2/contents/munger_v2_r1/personaje_v2/scripts/comprobar_gramatica.py?ref=716cbd6794b7fcde8b3862c9d1e7acdaf516d262" --jq '.content' | tr -d '\n' | base64 -d > .trabajo/f-rev/comprobar_gramatica_716cbd6.py   # sha256 5846a57e...
gh api "repos/jluisplagos/munger-v2/contents/munger_v2_r1/v6/scripts/patch_v62_base.py?ref=716cbd6794b7fcde8b3862c9d1e7acdaf516d262" --jq '.content' | tr -d '\n' | base64 -d > .trabajo/f-rev/patch_v62_base_716cbd6.py        # sha256 5cf3e467...
# 7 archivos de d519eb0 descargados igual con ref=d519eb0... a .trabajo/f-rev/ (hashes en evidencias/)
```

## 4. Rerun de las pruebas del autor (copia aislada) y comparación estructural

```bash
cd .trabajo/f-rev && python3 -I controles_sinteticos_f1.py > controles_sinteticos_f1.log 2>&1; echo "exit=$?"   # exit 1 solo por la comprobacion textual W2[8] (artefacto de entorno)
python3 - <<'EOF'   # diff estructural json publicado vs rerun -> evidencias/diff_json_rerun_vs_publicado.txt
EOF
```

## 5. Réplica independiente W1 (desde cero, Fraction, sin imports del autor)

```bash
cd .trabajo/f-rev && python3 -I ../resultados_cierre/alcance_real/revisiones_claude/evidencias/w1_independiente.py \
  | tee ../resultados_cierre/alcance_real/revisiones_claude/evidencias/w1_independiente_out.txt   # COINCIDE a 0.00e+00; regla anterior = 610,0 exacto en H=11/12
```

## 6. Comprobación textual de G8 / AVISO_TRANSICION en la base + aritmética W2

```bash
grep -n 'salto_anio_11\|umbral = num\|abs(sv) > umbral' .trabajo/f-rev/comprobar_gramatica_716cbd6.py
grep -n 'A178\|B178\|C179\|AVISO_TRANSICION\|MAX(ABS' .trabajo/f-rev/patch_v62_base_716cbd6.py
python3 - <<'EOF'   # cadenas exactas del bloque W2 del autor + Decimal: saltos Elis -> evidencias/verificacion_textual_y_aritmetica.txt
EOF
```

## 7. Entrega

```bash
# redacción de resultados_cierre/alcance_real/revisiones_claude/{CONTRASTE_F1_W1_W3_d519eb0.md, ENTREGA_F_REV.json, evidencias/}
# manifiesto y recuperación:
cd resultados_cierre/alcance_real && find . -type f | sort | xargs sha256sum > MANIFIESTO_SHA256.txt
git add resultados_cierre/alcance_real && git commit -m "..." && git push -u origin mistral/f-alcance-real
git fetch origin coordinacion/cierre-v2   # re-consulta de CONTROL.json tras el bloque
```

## Bloque C20 (mismo bloque F-REV, segunda entrega de Claude) · commit e94ee7c 2026-11-16T21:32:34Z

```bash
# control actualizado: C20 ENTREGADO @ bf0d5c2, solicitud LISTA (11 rutas, 5 criterios)
git fetch origin coordinacion/cierre-v2 && git show FETCH_HEAD:coordinacion/cierre_v2/CONTROL.json | python3 -c "...tareas C20..."
# alcance del diff (12 archivos, solo bajo frente_E_F1_elis/; cifras_fuente.csv sin cambios)
gh api "repos/jluisplagos/munger-v2/compare/d519eb0...bf0d5c2" --jq '.files[] | [.filename,.status,.additions,.deletions] | @tsv'
# descarga de artefactos @ bf0d5c2 y @ d519eb0 (scripts, datos, resultados, RESPUESTA) via gh api contents -> .trabajo/c20/
# PDFs reales desde el release base-4.14 (ya descargado en el frente M2) y verificacion de huellas:
unzip -o -j .trabajo/base414.zip '.../elis_decisiones/Elis/fuentes_pdf/*.pdf' -d .trabajo/c20/raiz/.../fuentes_pdf/
sha256sum *.pdf   # == fuentes.json (98c0012c, 04bfd087, 94e994f0, e2d316b3, 8aac7004)
# 73 paginas exportadas hash-ligadas desde el tarball del repo @ bf0d5c2:
gh api "repos/jluisplagos/munger-v2/tarball/bf0d5c2..." > /tmp/repo_bf0d5c2.tar.gz
tar xzf /tmp/repo_bf0d5c2.tar.gz -C .trabajo/c20/repo --wildcards '*/frente_E_F1_elis/{evidencias/paginas,scripts,datos}/*'
# shims pdftotext/pdfinfo en .trabajo/c20/shim (sirven export hash-ligado; fallback a texto completo solo en paginas de contexto)
# rerun de las 752 filas con el codigo C20:
PATH="$PWD/.trabajo/c20/shim:$PATH" python3 -I .trabajo/c20/verificar_cifras.py --raiz .trabajo/c20/raiz/munger_v2_r1 \
  --datos .trabajo/c20/cifras_fuente.csv --fuentes .trabajo/c20/fuentes.json --salida .trabajo/c20/out_c20.json   # exit 1 (16 filas texto solo por falta de raw)
# comparacion fila a fila vs publicado y entre commits (736/752 identical; 0 diferencias en tabla; sha256 f17bd8c5 igual en d519eb0 y bf0d5c2)
# sondas U1-U6 sobre ambas versiones + end-to-end en URD2022 p.261/p.284:
python3 -I .trabajo/c20/probes_c20.py   # todo COINCIDE con lo que propone la revision 9
# diffs de codigo y de test, y parches de texto (T14, informe) guardados en evidencias/c20/
```

## Bloque CSV (F-REV, tercera entrega de Claude) · commit c7716a0 2026-11-16T21:42:17Z

```bash
git fetch origin coordinacion/cierre-v2   # CSV ENTREGADO @ 77ff89f8, solicitud LISTA (4 criterios)
gh api "repos/jluisplagos/munger-v2/compare/bf0d5c2...77ff89f8" --jq '.files[] | [.filename,.status,.additions,.deletions] | @tsv'   # 19 archivos, solo frente_E_F1_elis/
# descarga @77ff89f8 via gh api contents a .trabajo/csv/ (CSV, verificacion, contraste, copia, respuesta, 6 paginas nuevas, cobertura, sondas)
# verificador identico: sha256 verificar_cifras.py @bf0d5c2 == @77ff89f8 (06da865b...)
# libro real del ZIP base-4.14: elis_decisiones/Elis/Elis_v63_evaluada.xlsx sha256 d2593777... == SHA_LIBRO
# 6 paginas nuevas copiadas al shim; rerun de las 762 filas:
PATH="$PWD/.trabajo/c20/shim:$PATH" python3 .trabajo/csv/verificar_cifras_77ff89f8.py --raiz .trabajo/c20/raiz/munger_v2_r1 --datos .trabajo/csv/cifras_fuente.csv --fuentes .trabajo/c20/fuentes.json --salida .trabajo/csv/out_csv.json   # 10 nuevas OK; 746/762 identicas (16 texto = limite de entorno)
# contraste y copia con libro real via shim openpyxl stdlib (solo valores cacheados):
PYTHONPATH=.trabajo/csv/shimlib PATH=.trabajo/c20/shim:$PATH python3 .trabajo/csv/contraste_f1.py --cifras ... --verificacion ... --libro ... --salida contraste_out.json --informe contraste_out.md --caja-no-nula caja_no_nula.json   # exit 0, 292/0, byte-identical
PYTHONPATH=.trabajo/csv/shimlib PATH=.trabajo/c20/shim:$PATH python3 .trabajo/csv/copia_investigacion_f1.py --cifras ... --verificacion ... --libro ... --contraste ... --salida copia_out.json --informe copia_out.md --raiz ... --fuentes ...   # exit 0, 67/0, byte-identical
# 4 controles negativos reconstruidos:
python3 .trabajo/csv/mutantes_csv.py   # Lavartex/otras adquisiciones como grupo -> PENDIENTE (no OK); anio/edicion equivocados -> FALLO
```

## Bloque B-PM1 (contraste documental del dossier de Mistral B) · commit 223f16d 2026-11-16T21:50:14Z (evidencia 21:48:58Z)

```bash
git fetch origin mistral/m2-fundamento-pm1                       # daa7478 = HEAD del frente B
git archive daa7478 resultados_m2/pm1 | tar -x -C .trabajo/pm1 --strip-components=2   # copia aislada, rama intacta
# hashes: 11 textos Vidrala == ZIP base-4.14 (unzip -p | sha256sum); 29 PDF de FUENTES_CONSERVADAS.csv OK (sha256+bytes)
mkdir -p resultados_m2/pm1 && python3 -I .trabajo/pm1/scripts/tablas_vidrala.py   # exit 0; salida byte-identical a la commiteada; control negativo OK
cmp resultados_m2/pm1/VIDRALA_REPOSICION_CAPACIDAD.csv .trabajo/pm1/VIDRALA_REPOSICION_CAPACIDAD.csv; rm -rf resultados_m2   # worktree limpio
python3 -I .trabajo/pm1/extraccion_independiente_pm1.py   # metodo propio (nota+slot): 9/9 PP&E OK, 8/8 comparativos OK, 9/9 intangibles OK -> TODO COINCIDE
gh release view fuentes-mistral-m2-20261116 --repo jluisplagos/munger-v2-evidencias-mistral --json assets   # assets: [] (401 coherente)
git show daa7478:resultados_m2/pm1/CALCULOS_PM1.json   # conclusion: P-M1 no delimitada, bloqueo; theta/lambda no identificados
```

## Bloque Cola 2 (F-B3/F-C1, paquete de preparacion) · commit 52fb120 2026-11-16T22:07:15Z; checkpoint 868f448 22:07:42Z

```bash
# estado: matriz de alcance + hito 2 + resumen empresas + fixtures motor C + E62 (via gh api / ZIP base-4.14)
unzip -l .trabajo/base414.zip > /tmp/zip_list.txt
python3 preparacion_b3_c1/scripts/inventario_desde_zip.py /tmp/zip_list.txt preparacion_b3_c1/INVENTARIO_Y_HUECOS.csv
# huellas: 29 PDF de FUENTES_CONSERVADAS.csv @ daa7478 verificados (sha256+bytes) -> fuentes/huellas_fuentes_conservadas.csv
git show daa7478:resultados_m2/pm1/FUENTES_CONSERVADAS.csv
# paquete: SELECCION.csv, PROTOCOLO_CONGELADO.md, MAPA_ENTRADAS.jsonl, CONTRATO_C_PROPUESTA.md, README.md, ENTREGA_B3_C1.json
# NO se ejecuto LibreOffice ni el pipeline; no hay recorrido real ejecutado (bloqueos declarados)
```

## Bloque F2 (respuesta a CORRECCION_F2 @ F_223f16d_52fb120) · 2026-11-17 09:24–09:47:33 UTC (horas reales; commit final 98bdf8f a las 09:47:33Z — F3-R14 corrigiendo el 09:44 anterior)

Variables usadas en este bloque (definidas, no implicitas): `ZIP_414` = ruta local del asset
`munger_v2_r1_entrega4.14_cierre_verificacion_entradas.zip` descargado de la release `base-4.14`
de `jluisplagos/munger-v2` (sha256 bb51942cefb848e409a4828e3faeb70f94aa4d29af39cda6d90cd0a97cb7b93e);
`RUTA_TEXTOS` = `/tmp/insumos_m2/munger_v2_r1/personaje_v2/empresas_v2_correcciones/2026-11_Vidrala_ensayo_4_14/vidrala_decisiones/Vidrala/texto`
(extraído del ZIP con `unzip -oq "$ZIP_414" 'munger_v2_r1/…/vidrala_decisiones/Vidrala/texto/*' -d /tmp/insumos_m2`).

```bash
# entorno y producto de referencia (solo lectura): clon de jluisplagos/munger-v2 @ 957af65
git checkout 957af652cdc3bef3d67e8623c9572138bac685e9
gh release download base-4.14 --repo jluisplagos/munger-v2 --pattern '*.zip'   # a .trabajo/
sha256sum .trabajo/munger_v2_r1_entrega4.14_cierre_verificacion_entradas.zip
# bb51942cefb848e409a4828e3faeb70f94aa4d29af39cda6d90cd0a97cb7b93e  (coincide con la referencia)

# F2-D1/D2/D7 · inventario byte a byte + 71 PDF con SHA-256 completo (commit 195766f)
python3 -I resultados_cierre/alcance_real/preparacion_b3_c1/scripts/inventario_desde_zip.py "$ZIP_414" /tmp/inv_check.csv /tmp/huellas_check.csv   # exit 0; 131 recursos, 6799 archivos, 71 PDF
cmp /tmp/inv_check.csv resultados_cierre/alcance_real/preparacion_b3_c1/INVENTARIO_Y_HUECOS.csv   # byte-identico
# F2-D7 · huellas de FUENTES_CONSERVADAS.csv @ daa7478 ejecutables:
git show origin/mistral/m2-fundamento-pm1:resultados_m2/pm1/FUENTES_CONSERVADAS.csv > /tmp/fuentes_daa7478.csv
python3 -I resultados_cierre/alcance_real/correccion_f2/scripts/verificar_huellas.py "$ZIP_414" /tmp/fuentes_daa7478.csv   # exit 0, 29/29

# F2-D3 · contrato C verificado contra el codigo @957af65 (commit e9f76a9)
python3 -I resultados_cierre/alcance_real/correccion_f2/scripts/verificar_contrato_c.py   # exit 0, TODO CUADRA
#   puente E1=1060 (viejo 1170); ROE 0,094340 vs 0,126214; B15=payout 40% -> 115,06 -> 278,45 (x2,42)
#   citas: build_v6.py:147,282,294,312,444-453,933-945,1136-1147; test_fill.py:79,84,93-99;
#   relacion_entradas_materiales.py:143-152; patch_v62_base.py:255 (E62)

# F2-D6 · protocolo C + horas reales (commit 9873234)
git log --format='%h %ad %s' --date=format:'%Y-%m-%dT%H:%M:%SZ' -7   # horas de commit usadas en este archivo

# F2-D4/D5/D7 · recuperacion, ENTREGA corregidas, extractor por argumento (commit c761cc8)
python3 -I resultados_cierre/alcance_real/revisiones_b_pm1/evidencias/extraccion_independiente_pm1.py "$RUTA_TEXTOS"   # exit 0, salida byte-identica a extraccion_independiente_out.txt

# higiene por bloque: manifiesto y push
cd resultados_cierre/alcance_real && find . -type f ! -name MANIFIESTO_SHA256.txt | sort | xargs sha256sum > MANIFIESTO_SHA256.txt && sha256sum -c --quiet MANIFIESTO_SHA256.txt
git add resultados_cierre/alcance_real && git commit -m "F · F2-D..." && git push origin mistral/f-alcance-real
```


## Bloque F3 (respuesta a CORRECCION_F3 @ F2_195766f_98bdf8f) · 2026-11-17 ~13:05–13:20 UTC (horas reales de sesión, `date -u`)

```bash
# misma definición de $ZIP_414 que arriba; producto de referencia @957af65 (solo lectura)
git -C <clon_producto> checkout 957af652cdc3bef3d67e8623c9572138bac685e9

# F3-R3/R4 · .bat registrado con huella + alcance negativo (commit 27c5931)
unzip -p "$ZIP_414" 'munger_v2_r1/personaje_v2/empresas_v2_correcciones/2026-11_Vidrala_ensayo_4_14/documentacion_cierre_4_14/descargas_bat/descargar_fuentes_ahold.bat' | sha256sum
# 04feebd409754a91e509dfde1e8dd63a1e8534695d05cb75fffca6a97bd53d88
python3 -I resultados_cierre/alcance_real/preparacion_b3_c1/scripts/inventario_desde_zip.py "$ZIP_414" /tmp/inv3.csv /tmp/huellas3.csv   # exit 0; 131 recursos + 4 .bat; 6476 dentro / 323 fuera
cmp /tmp/inv3.csv resultados_cierre/alcance_real/preparacion_b3_c1/INVENTARIO_Y_HUECOS.csv   # byte-identico

# F3-R5/R6/R7/R8/R12/R13 · contrato alineado con U3, citas reales (commit c4d918f)
python3 -I resultados_cierre/alcance_real/correccion_f2/scripts/verificar_contrato_c.py   # exit 0, TODO CUADRA (quiebra 105,55; OCI 1025/75/50; ROE 9,434% vs 10%)
sed -n '581p;926,937p;960-963p;971p;1102p;1132p' <clon_producto>/munger_v2_r1/v6/scripts/V6.1/build_v6.py   # citas verificadas (evidencias/r6_citas_reales_957af65.txt)

# F3-R9 · comandos de ENTREGA ejecutables tal cual (rerun capturado en evidencias/r9_*.txt)
git archive origin/mistral/m2-fundamento-pm1 resultados_m2 | tar -x -C /tmp/pm1_rerun   # + textos del ZIP + python3 -I resultados_m2/pm1/scripts/tablas_vidrala.py -> exit 0, CSV byte-identico
python3 -I resultados_cierre/alcance_real/revisiones_b_pm1/evidencias/extraccion_independiente_pm1.py "$RUTA_TEXTOS" | cmp - resultados_cierre/alcance_real/revisiones_b_pm1/evidencias/extraccion_independiente_out.txt   # exit 0, byte-identico
```
