#!/usr/bin/env bash
# F3-R9 · control negativo de ENTREGA_F3 prueba 2 / ENTREGA_B_PM1 prueba 1 (tablas_vidrala.py).
# Ejecutar dentro de un espacio de montaje con /tmp redirigido y cwd = raiz del worktree revisado:
#   unshare -m bash -c 'mount --bind <rev_F3>/sondas/tmp_ns2 /tmp && cd <rev_F3>/wt && ZIP_414=<zip> bash <rev_F3>/sondas/sonda_r9_control_tablas.sh'
set -u
T='munger_v2_r1/personaje_v2/empresas_v2_correcciones/2026-11_Vidrala_ensayo_4_14/vidrala_decisiones/Vidrala/texto/*'
CSV=resultados_m2/pm1/VIDRALA_REPOSICION_CAPACIDAD.csv
prep() {
  mkdir -p "/tmp/$1/.trabajo/insumos_m2"
  git archive origin/mistral/m2-fundamento-pm1 resultados_m2 | tar -x -C "/tmp/$1"
  unzip -oq "$ZIP_414" "$T" -d "/tmp/$1/.trabajo/insumos_m2"
  mv "/tmp/$1/.trabajo/insumos_m2/munger_v2_r1/personaje_v2" "/tmp/$1/.trabajo/insumos_m2/personaje_v2"
}
git show origin/mistral/m2-fundamento-pm1:$CSV > /tmp/vidrala_daa7478.csv
echo "== A. mismo comando, pero sin ejecutar el script (python3 -I -c pass):"
prep ctlA; ( cd /tmp/ctlA && python3 -I -c pass && cmp $CSV /tmp/vidrala_daa7478.csv ); echo "   exit=$?  (0 = la prueba publicada pasa aunque el script no regenere nada)"
echo "== B. borrando antes el CSV extraido y ejecutando el script del autor:"
prep ctlB; ( cd /tmp/ctlB && rm -f $CSV && python3 -I resultados_m2/pm1/scripts/tablas_vidrala.py > /dev/null && cmp $CSV /tmp/vidrala_daa7478.csv ); echo "   exit=$?  (0 = el script regenera el CSV byte a byte)"
echo "== C. borrando el CSV y sin ejecutar el script:"
prep ctlC; ( cd /tmp/ctlC && rm -f $CSV && python3 -I -c pass && cmp $CSV /tmp/vidrala_daa7478.csv ); echo "   exit=$?  (distinto de 0 = control negativo discrimina)"
