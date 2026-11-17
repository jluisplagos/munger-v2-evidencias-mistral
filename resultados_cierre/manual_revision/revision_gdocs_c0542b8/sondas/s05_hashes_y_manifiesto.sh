#!/bin/sh
# Verificacion de hashes y del manifiesto en head c0542b83:
#  - sha256 de los 4 archivos descargados coinciden con las entradas del MANIFIESTO head
#  - el manifiesto head tiene 7762 entradas (cabecera dice 7762) -> 7762/7762
#  - solo 3 entradas cambian respecto al manifiesto base (CAMBIOS, CONTINUIDAD, GUIA)
echo "== sha256 de los archivos head descargados =="
sha256sum material/head/*
echo "== entradas correspondientes del MANIFIESTO head =="
grep -E "  (CAMBIOS_ARCHIVOS.txt|CONTINUIDAD.md|personaje_v2/GUIA_RECORRIDO_SUPERVISADO.md|MANIFIESTO_SHA256.txt)$" material/head/munger_v2_r1_MANIFIESTO_SHA256.txt || true
grep -E "  (CAMBIOS_ARCHIVOS.txt|CONTINUIDAD.md|personaje_v2/GUIA_RECORRIDO_SUPERVISADO.md)$" material/head/munger_v2_r1_MANIFIESTO_SHA256.txt
echo "== recuento de entradas (sin cabecera #) base y head, y cabecera head =="
echo -n "base: "; grep -vc '^#' material/base/munger_v2_r1_MANIFIESTO_SHA256.txt
echo -n "head: "; grep -vc '^#' material/head/munger_v2_r1_MANIFIESTO_SHA256.txt
head -1 material/head/munger_v2_r1_MANIFIESTO_SHA256.txt
echo "== diff de entradas base vs head (solo deben cambiar 3 hashes) =="
grep -v '^#' material/base/munger_v2_r1_MANIFIESTO_SHA256.txt > /tmp/m_base.txt
grep -v '^#' material/head/munger_v2_r1_MANIFIESTO_SHA256.txt > /tmp/m_head.txt
diff /tmp/m_base.txt /tmp/m_head.txt || true
echo "== consistencia base: sha256 de archivos base vs entradas del manifiesto base =="
sha256sum material/base/munger_v2_r1_personaje_v2_GUIA_RECORRIDO_SUPERVISADO.md material/base/munger_v2_r1_CONTINUIDAD.md
grep -E "  (personaje_v2/GUIA_RECORRIDO_SUPERVISADO.md|CONTINUIDAD.md)$" material/base/munger_v2_r1_MANIFIESTO_SHA256.txt
echo "== CAMBIOS head: cabecera regenerada por el generador del producto y seccion RESPECTO A LA 4.14 =="
head -4 material/head/munger_v2_r1_CAMBIOS_ARCHIVOS.txt
grep -n -A3 "RESPECT" material/head/munger_v2_r1_CAMBIOS_ARCHIVOS.txt | head -8
grep -n "GUIA_RECORRIDO_SUPERVISADO.md" material/head/munger_v2_r1_CAMBIOS_ARCHIVOS.txt
