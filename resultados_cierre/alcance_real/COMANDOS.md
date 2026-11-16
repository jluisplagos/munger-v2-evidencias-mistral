# Comandos ejecutados · bloque F-REV (rama mistral/f-alcance-real)

Fecha: 2026-11-16 ~21:05–21:15 UTC. Entorno: sandbox `/workspace`, repo auxiliar clonado en
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
