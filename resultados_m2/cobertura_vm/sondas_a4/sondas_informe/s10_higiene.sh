#!/bin/bash
# Revisor A3: higiene de 0946971. Uso: bash s10_higiene.sh ENTREGA GITDIR
ENT=$1; GD=$2; C=$ENT/resultados_m2/cobertura_vm
echo "## sha256sum -c MANIFIESTO_SHA256.txt (desde la raiz de la carpeta)"
(cd $C && sha256sum -c --quiet MANIFIESTO_SHA256.txt; echo "exit=$?"; echo "lineas=$(wc -l < MANIFIESTO_SHA256.txt)")
echo "## archivos de la carpeta que no estan en el manifiesto"
(cd $C && find . -type f | sed 's|^\./||' | sort > /tmp/.a$$; cut -d' ' -f3- MANIFIESTO_SHA256.txt | sort > /tmp/.b$$; comm -23 /tmp/.a$$ /tmp/.b$$; rm -f /tmp/.a$$ /tmp/.b$$)
echo "## git diff --name-only 8b88fab 0946971"
git --git-dir=$GD diff --name-only 8b88fab 0946971 > /tmp/.d$$; echo "archivos=$(wc -l < /tmp/.d$$)"
echo "fuera de resultados_m2/cobertura_vm/: $(grep -vc '^resultados_m2/cobertura_vm/' /tmp/.d$$)"
echo "pdf/xlsx/zip/pyc/pycache/.trabajo/.DS_Store: $(grep -Eic '\.(pdf|xlsx|xlsm|xls|zip|pyc)$|__pycache__|\.trabajo/|\.DS_Store' /tmp/.d$$)"
echo "binarios (numstat -/-): $(git --git-dir=$GD diff --numstat 8b88fab 0946971 | awk '$1=="-"' | wc -l)"
echo "## patrones de secreto en las lineas anadidas"
git --git-dir=$GD diff 8b88fab 0946971 | grep '^+' | grep -EIc 'ghp_[A-Za-z0-9]{20,}|github_pat_|sk-[A-Za-z0-9]{20,}|AKIA[0-9A-Z]{16}|BEGIN (RSA|OPENSSH|EC) PRIVATE|xox[bp]-|api[_-]?key\s*[:=]\s*["'"'"'][^"'"'"']{8,}|password\s*[:=]'
echo "## rutas absolutas anadidas (/home, /tmp, /workspace, /root)"
git --git-dir=$GD diff 8b88fab 0946971 | grep '^+' | grep -oE '(/home/|/tmp/|/workspace/|/root/)[A-Za-z0-9_./-]*' | sort | uniq -c | sort -rn | head -12
echo "## arbol 0946971: pdf/xlsx/zip/pyc"
git --git-dir=$GD ls-tree -r --name-only 0946971 | grep -Eic '\.(pdf|xlsx|xlsm|zip|pyc)$|__pycache__'
rm -f /tmp/.d$$
