#!/usr/bin/env bash
# (revisor, ronda 2) reproducciones de vigencia sobre copias completas de Vidrala 4.14 (vigente, con hoja v2 ya generada)
R=/tmp/claude-0/revision_hoja_r2; SC=$R/limpia/munger_v2_r1/personaje_v2/scripts; H="python3 -I -B $SC/hoja_resumen.py"
base=$R/exp/Vidrala_414/Vidrala
copia() { rm -rf $R/rep/$1; mkdir -p $R/rep/$1; cp -a $base $R/rep/$1/Vidrala; echo $R/rep/$1/Vidrala; }
hoja() { ls $1 | grep -c '^hoja_resumen\.\(md\|json\)$'; }
echo "### S1 · A1/A6: fase_c.json alterado después de la auditoría, con hoja vigente dentro"
E=$(copia S1); python3 - "$E" <<'PY'
import json, sys
p = sys.argv[1] + '/fase_c.json'; fc = json.load(open(p, encoding='utf-8'))
fc['cambiaria_de_cubo']['a_no'] = 'Nada me haría pasar a No: el negocio es seguro y el precio da igual.'
fc['cambiaria_de_cubo']['a_si'] = 'Ya es un Sí: compraría hoy a cualquier precio por debajo de 120 €.'
json.dump(fc, open(p, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
PY
python3 -B $R/herr/vig.py $E
echo "   --comprobar: $($H $E --comprobar | cut -c1-230) (código ${PIPESTATUS[0]})"
out=$($H $E --trabajo $R/tmp --espera-cerrojo 3000 2>&1); echo "   generar: código $? · $(echo "$out" | head -2 | cut -c1-260 | tr '\n' ' ')"
echo "   archivos hoja_resumen.md/.json en el expediente: $(hoja $E) · apartados: $(ls $E | grep NO_VIGENTE | tr '\n' ' ')"
echo "   --comprobar: $($H $E --comprobar | cut -c1-120) (código ${PIPESTATUS[0]})"
echo "   con los apartados dentro, la vía oficial:"; python3 -B $R/herr/vig.py $E asegurar
echo "   tras la retirada oficial: hojas en el expediente: $(hoja $E) · generar: $($H $E --trabajo $R/tmp 2>&1 | head -1 | cut -c1-200)"
echo
echo "### S2 · retirada oficial con la hoja vigente todavía en el expediente (decisión del coordinador)"
E=$(copia S2); cp $E/fase_c.json $R/rep/S2/fase_c.original.json; python3 - "$E" <<'PY'
import json, sys
p = sys.argv[1] + '/fase_c.json'; fc = json.load(open(p, encoding='utf-8')); fc['cambiaria_de_cubo']['a_no'] = 'Nada me haría pasar a No.'
json.dump(fc, open(p, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
PY
echo "   antes: hojas en el expediente: $(hoja $E)"; python3 -B $R/herr/vig.py $E asegurar
echo "   después: hojas en el expediente: $(hoja $E) · quedan salidas oficiales: $(ls $E | grep -E '^(ficha.json|informe.md|cierre_vigente.json)$' | tr '\n' ' ')· aprobaciones_retiradas.json: $(ls $E | grep -c aprobaciones_retiradas)"
echo "   --comprobar: $($H $E --comprobar | cut -c1-120) (código ${PIPESTATUS[0]})"
arch=$(ls -d $E/historial_cierres/*/ | tail -1)
echo "   primera línea de la hoja archivada: $(head -1 ${arch}hoja_resumen.NO_VIGENTE.md)"
echo "   restauro a mano ficha, informe, cierre_vigente y el fase_c original (intento de reactivar):"
cp ${arch}ficha.json ${arch}informe.md ${arch}cierre_vigente.json $E/; cp $R/rep/S2/fase_c.original.json $E/fase_c.json; cp ${arch}hoja_resumen.NO_VIGENTE.md $E/hoja_resumen.md; cp ${arch}hoja_resumen.NO_VIGENTE.json $E/hoja_resumen.json
python3 -B $R/herr/vig.py $E
echo "   --comprobar (hoja restaurada): $($H $E --comprobar | cut -c1-260) (código ${PIPESTATUS[0]})"
out=$($H $E --trabajo $R/tmp 2>&1); echo "   generar: código $? · $(echo "$out" | head -1 | cut -c1-260)"
echo
echo "### S4 · A2: precio.json alterado (precio 90,10 → 50,00; zona → cumple_regla_k)"
E=$(copia S4); python3 - "$E" <<'PY'
import json, sys
p = sys.argv[1] + '/precio.json'; x = json.load(open(p, encoding='utf-8')); x['precio'] = 50.0; x['zona'] = 'cumple_regla_k'
json.dump(x, open(p, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
PY
out=$($H $E --trabajo $R/tmp 2>&1); echo "   generar: código $? · $(echo "$out" | head -2 | cut -c1-250 | tr '\n' ' ')"
echo "   hojas en el expediente: $(hoja $E) · apartados: $(ls $E | grep NO_VIGENTE | tr '\n' ' ') · --comprobar: $($H $E --comprobar | cut -c1-80) (código ${PIPESTATUS[0]})"
echo
echo "### S6 · H9: hoja_resumen.md editada a mano (conclusión cambiada a «Compraría…»)"
E=$(copia S6); python3 - "$E" <<'PY'
import sys
p = sys.argv[1] + '/hoja_resumen.md'; t = open(p, encoding='utf-8').read()
a = 'No comprar ahora; esperar a mejor precio.'; assert a in t
open(p, 'w', encoding='utf-8').write(t.replace(a, 'Compraría al precio del análisis.'))
PY
echo "   --comprobar: $($H $E --comprobar | cut -c1-200) (código ${PIPESTATUS[0]})"
echo "   --verificar-origen: $($H $E --verificar-origen | cut -c1-200) (código ${PIPESTATUS[0]})"
