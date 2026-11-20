#!/bin/bash
# Pruebas de lanzador_comun.sh y comprobar_registro.py: positivas y negativas. Uso: bash test_herramientas.sh [REGISTRO_REAL_C18]
# Sale con 0 solo si todos los casos dan el código esperado.
set -u
D=$(cd "$(dirname "$0")" && pwd); T=$(mktemp -d); trap 'rm -rf "$T"' EXIT
ok=0; mal=0
espera() { local desc=$1 esperado=$2 obtenido=$3
  if [ "$esperado" -eq "$obtenido" ]; then ok=$((ok+1)); echo "OK    $desc: código $obtenido"; else mal=$((mal+1)); echo "FALLO $desc: esperado $esperado, obtenido $obtenido"; fi; }
C="python3 -I $D/comprobar_registro.py"
# --- comprobador ---
if [ $# -ge 1 ]; then
  $C "$1" --esperados 26 >/dev/null; espera "registro real de C18 (26 pasos, todos 0)" 0 $?
  $C "$1" --esperados 28 >/dev/null; espera "registro real con 28 esperados" 3 $?
  sed '0,/código 0/s//código 1/' "$1" > $T/r1.log; $C $T/r1.log >/dev/null; espera "un paso con código 1" 1 $?
  grep -v '^fin' "$1" > $T/r2.log; $C $T/r2.log >/dev/null; espera "registro sin línea fin (truncado)" 2 $?
  head -n -2 "$1" > $T/r3.log; $C $T/r3.log >/dev/null; espera "paso final sin código" 2 $?
fi
$C $T/no_existe.log >/dev/null; espera "registro inexistente" 2 $?
mkdir $T/dir.log; $C $T/dir.log >/dev/null; espera "ruta que es un directorio (error de lectura)" 2 $?
printf '\xff\xfe\x00basura\n' > $T/bin.log; $C $T/bin.log >/dev/null; espera "registro no UTF-8" 2 $?
: > $T/vacio.log; $C $T/vacio.log >/dev/null; espera "registro vacío" 2 $?
printf '== a 10:00:00\n   código 0\notra cosa\nfin 10:00:01\n' > $T/raro.log; $C $T/raro.log >/dev/null; espera "línea no reconocida" 2 $?
# --- cierre del registro (contraste externo REVISION_0955, S1 y S2) ---
printf '== primero 10:00:00\n   código 0\nfin 10:00:01\n== segundo 10:00:02\n   código 0\n' > $T/s1.log; $C $T/s1.log --json >/dev/null; espera "S1: pasos después de fin" 2 $?
printf '== primero 10:00:00\n   código 0\nfin 10:00:01 · ejecutados 1 · esperados 1 · fallidos 1 · resultado 1\n' > $T/s2.log; $C $T/s2.log --json >/dev/null; espera "S2: resumen que declara un fallo inexistente" 2 $?
printf '== a 10:00:00\n   código 0\nfin 10:00:01\n   código 0\n' > $T/s1b.log; $C $T/s1b.log >/dev/null; espera "código suelto después de fin" 2 $?
printf '== a 10:00:00\n   código 0\nfin 10:00:01\nfin 10:00:02\n' > $T/dosfin.log; $C $T/dosfin.log >/dev/null; espera "dos líneas fin" 2 $?
printf '== a 10:00:00\n   código 0\n== b 10:00:01\n   código 0\nfin 10:00:02 · ejecutados 1 · esperados 2 · fallidos 0 · resultado 0\n' > $T/n.log; $C $T/n.log >/dev/null; espera "resumen con ejecutados distinto de los pasos" 2 $?
printf '== a 10:00:00\n   código 0\nfin 10:00:01 · ejecutados 1 · esperados 2 · fallidos 0 · resultado 0\n' > $T/r.log; $C $T/r.log >/dev/null; espera "resumen con resultado 0 cuando las reglas dan 3" 2 $?
printf '== a 10:00:00\n   código 0\nfin 10:00:01 · ejecutados 1 · esperados 2 · fallidos 0 · resultado 3\n' > $T/r3.log; $C $T/r3.log >/dev/null; espera "resumen coherente con menos pasos de los declarados" 3 $?
printf '== a 10:00:00\n   código 2\nfin 10:00:01 · ejecutados 1 · esperados 1 · fallidos 1 · resultado 1\n' > $T/r1.log; $C $T/r1.log >/dev/null; espera "resumen coherente con un fallo real" 1 $?
printf '# lanzador · inicio 2026-11-17T10:00:00Z · esperados 5\n== a 10:00:00\n   código 0\nfin 10:00:01 · ejecutados 1 · esperados 1 · fallidos 0 · resultado 0\n' > $T/cab.log; $C $T/cab.log >/dev/null; espera "cabecera y resumen con esperados distintos" 2 $?
printf '== a 10:00:00\n   código 0\nfin 10:00:01 · resultado 0\n' > $T/finraro.log; $C $T/finraro.log >/dev/null; espera "línea fin con formato no reconocido" 2 $?
printf '== a 10:00:00\n   código 0\nfin 10:00:01\n' > $T/hist.log; $C $T/hist.log >/dev/null; espera "positivo: formato histórico fin HH:MM:SS" 0 $?
printf '# lanzador · inicio 2026-11-17T10:00:00Z · esperados 1\n== a 10:00:00\n   código 0\nfin 10:00:01 · ejecutados 1 · esperados 1 · fallidos 0 · resultado 0\n' > $T/ampl.log; $C $T/ampl.log --esperados 1 >/dev/null; espera "positivo: formato ampliado coherente" 0 $?
# --- biblioteca ---
cat > $T/l_ok.sh <<EOS
source $D/lanzador_comun.sh; iniciar $T/ok.log 3
paso uno $T/o1 true; en_dir dos $T; copiar tres $T/ok.log $T/copia
terminar
EOS
bash $T/l_ok.sh; espera "lanzador: 3 pasos correctos" 0 $?; $C $T/ok.log --esperados 3 >/dev/null; espera "comprobador sobre ese registro" 0 $?
cat > $T/l_falla.sh <<EOS
source $D/lanzador_comun.sh; iniciar $T/falla.log 3
paso uno $T/o1 true; paso dos $T/o2 false; paso tres $T/o3 true
terminar
EOS
bash $T/l_falla.sh; espera "lanzador: un paso falla (y el último va bien)" 1 $?; $C $T/falla.log --esperados 3 >/dev/null; espera "comprobador sobre ese registro" 1 $?
cat > $T/l_cd.sh <<EOS
source $D/lanzador_comun.sh; iniciar $T/cd.log 2
en_dir entrar $T/no_existe; paso despues $T/o1 true
terminar
EOS
bash $T/l_cd.sh; espera "lanzador: cd fallido se anota y no se salta en silencio" 1 $?; grep -c "código" $T/cd.log | { read n; [ "$n" -eq 2 ]; }; espera "  los dos pasos quedan en el registro" 0 $?
cat > $T/l_cp.sh <<EOS
source $D/lanzador_comun.sh; iniciar $T/cp.log 1
copiar copia $T/no_existe $T/destino
terminar
EOS
bash $T/l_cp.sh 2>/dev/null; espera "lanzador: copia fallida" 1 $?
cat > $T/l_menos.sh <<EOS
source $D/lanzador_comun.sh; iniciar $T/menos.log 3
paso uno $T/o1 true
terminar
EOS
bash $T/l_menos.sh; espera "lanzador: menos pasos de los esperados" 3 $?
echo "$ok correctos, $mal fallidos"; [ $mal -eq 0 ]
