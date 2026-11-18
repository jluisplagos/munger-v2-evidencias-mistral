#!/usr/bin/env bash
# (revisor, ronda 2) reproducciones que necesitan LibreOffice (la hoja toma el cerrojo común en cada recálculo; espera larga)
R=/tmp/claude-0/revision_hoja_r2; SC=$R/limpia/munger_v2_r1/personaje_v2/scripts; H="python3 -I -B $SC/hoja_resumen.py"
cod() { "$@" > $R/tmp/_o2.txt 2>&1; c=$?; echo "código $c · $(head -2 $R/tmp/_o2.txt | cut -c1-230 | tr '\n' ' ')"; }
echo "### S5 · fecha del precio alterada en fase1_metadatos.json (31-dic-2025 → 13-nov-2026), que no es material auditado"
E=$R/rep/S5/Vidrala
echo "   generar → $(cod $H $E --trabajo $R/tmp --espera-cerrojo 3000)"
grep -n "Precio usado en el análisis" $E/hoja_resumen.md | cut -c1-230 | sed 's/^/   /'
echo "   --comprobar → $(cod $H $E --comprobar)"
echo
echo "### S3 · hoja escrita fuera del expediente (--salida) y retirada oficial después (límite declarado por el autor)"
rm -rf $R/rep/S3 $R/rep/S3_fuera; mkdir -p $R/rep/S3 $R/rep/S3_fuera; cp -a $R/exp/Vidrala_414/Vidrala $R/rep/S3/Vidrala; rm -f $R/rep/S3/Vidrala/hoja_resumen.*; E=$R/rep/S3/Vidrala
echo "   generar con --salida → $(cod $H $E --salida $R/rep/S3_fuera --trabajo $R/tmp --espera-cerrojo 3000)"
echo "   --comprobar --salida → $(cod $H $E --salida $R/rep/S3_fuera --comprobar)"
python3 - "$E" <<'PY'
import json, sys
p = sys.argv[1] + '/fase_c.json'; fc = json.load(open(p, encoding='utf-8')); fc['cambiaria_de_cubo']['a_no'] = 'Nada me haría pasar a No.'
json.dump(fc, open(p, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
PY
python3 -B $R/herr/vig.py $E asegurar | head -3
echo "   la hoja de fuera sigue ahí: $(ls $R/rep/S3_fuera | tr '\n' ' ')· --comprobar --salida → $(cod $H $E --salida $R/rep/S3_fuera --comprobar)"
echo
echo "### S7 · --antecedente sobre Hermès (no vigente para la vía oficial)"
rm -rf $R/rep/S7; mkdir -p $R/rep/S7; cp -a $R/exp/Hermes/Hermes $R/rep/S7/Hermes; E=$R/rep/S7/Hermes
echo "   generar sin --antecedente → $(cod $H $E --trabajo $R/tmp)"
echo "   generar con --antecedente → $(cod $H $E --antecedente --trabajo $R/tmp --espera-cerrojo 3000)"
sed -n 3,3p $E/hoja_resumen.md | cut -c1-330 | sed 's/^/   /'
echo "   --comprobar → $(cod $H $E --comprobar)"
echo
echo "### Elis 4.14 regenerada (la primera se generó mientras otro proceso mío pudo usar LibreOffice sin cerrojo)"
cp $R/exp/Elis_414/Elis/hoja_resumen.json $R/tmp/elis_primera.json
echo "   generar → $(cod $H $R/exp/Elis_414/Elis --trabajo $R/tmp --espera-cerrojo 3000)"
python3 - <<'PY'
import json
a = json.load(open('/tmp/claude-0/revision_hoja_r2/tmp/elis_primera.json', encoding='utf-8')); b = json.load(open('/tmp/claude-0/revision_hoja_r2/exp/Elis_414/Elis/hoja_resumen.json', encoding='utf-8'))
print('   filas de la sensibilidad idénticas a las de la primera generación:', a['sensibilidad']['filas'] == b['sensibilidad']['filas'])
PY
