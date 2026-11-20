#!/bin/bash
# Revisor A2 (8b88fab): higiene. Manifiesto, contenido del diff, secretos, rutas locales,
# ENTREGA.json frente a PLANTILLA_ENTREGA.json. Solo lectura (git diff/show/ls-tree).
# Uso: bash s10_higiene.sh GITDIR ENTREGA_EXTRAIDA
G=$1; ENT=$2; cd "$G"
echo "## sha256sum -c MANIFIESTO_SHA256.txt (arbol extraido de 8b88fab)"
( cd $ENT/resultados_m2/cobertura_vm && sha256sum -c MANIFIESTO_SHA256.txt > /tmp/_s10 2>&1; echo "exit=$?"; grep -vc ': OK$' /tmp/_s10 | sed 's/^/lineas no OK: /'; wc -l < MANIFIESTO_SHA256.txt | sed 's/^/entradas: /'; find . -type f ! -name MANIFIESTO_SHA256.txt | wc -l | sed 's/^/archivos en la carpeta (sin el manifiesto): /'; rm -f /tmp/_s10 )
for B in 2c41d68 9d676ce; do
 echo "## git diff --stat $B 8b88fab fuera de resultados_m2/cobertura_vm/"; git diff --name-only $B 8b88fab -- . ':!resultados_m2/cobertura_vm' | wc -l
 echo "## binarios en git diff --numstat $B 8b88fab"; git diff --numstat $B 8b88fab | awk '$1=="-"' | wc -l
 echo "## extensiones prohibidas en el diff $B..8b88fab"; git diff --name-only $B 8b88fab | grep -Eic '\.(pdf|xlsx|xlsm|zip|pyc)$|__pycache__|\.trabajo/' 
 echo "## patrones de secreto en lineas anadidas $B..8b88fab"; git diff $B 8b88fab | grep '^+' | grep -Eic 'ghp_|github_pat_|sk-[A-Za-z0-9]{20}|AKIA[0-9A-Z]{16}|BEGIN [A-Z ]*PRIVATE KEY|authorization:|password='
 echo "## rutas locales absolutas en lineas anadidas $B..8b88fab"; git diff $B 8b88fab | grep '^+' | grep -Ec '/(home|root|workspace|tmp|Users)/'
done
echo "## lineas con rutas absolutas anadidas (2c41d68..8b88fab), primeras 5"; git diff 2c41d68 8b88fab | grep '^+' | grep -Eo '/(home|root|workspace|tmp|Users)/[^ "]{0,60}' | sort | uniq -c | head -5
echo "## arbol 8b88fab: archivos PDF/XLSX/ZIP/pyc"; git ls-tree -r --name-only 8b88fab | grep -Eic '\.(pdf|xlsx|xlsm|zip|pyc)$|__pycache__'
echo "## commits 2c41d68..8b88fab"; git log --oneline 2c41d68..8b88fab | cat
echo "## ENTREGA.json frente a PLANTILLA_ENTREGA.json (claves)"
git show origin/coordinacion/cierre-v2:coordinacion/cierre_v2/PLANTILLA_ENTREGA.json > /tmp/_plant.json
python3 -I - "$ENT/resultados_m2/cobertura_vm/ENTREGA.json" /tmp/_plant.json <<'PY'
import json, sys
e = json.load(open(sys.argv[1], encoding='utf-8')); p = json.load(open(sys.argv[2], encoding='utf-8'))
print('faltan en ENTREGA:', sorted(set(p) - set(e))); print('sobran en ENTREGA:', sorted(set(e) - set(p)))
for k in p:
    if k in e and type(p[k]) != type(e[k]) and p[k] is not None:
        print('tipo distinto:', k, type(p[k]).__name__, '->', type(e[k]).__name__)
pp = (p.get('pruebas') or [{}])[0]
for i, t in enumerate(e.get('pruebas') or []):
    print(f'prueba {i}: faltan', sorted(set(pp) - set(t)), '| sobran', sorted(set(t) - set(pp)))
print('es_plantilla:', e.get('es_plantilla'), '| commit_entrega:', e.get('commit_entrega'), '| revision_por_otro_contexto:', str(e.get('revision_por_otro_contexto'))[:80])
PY
rm -f /tmp/_plant.json
