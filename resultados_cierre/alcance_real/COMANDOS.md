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
