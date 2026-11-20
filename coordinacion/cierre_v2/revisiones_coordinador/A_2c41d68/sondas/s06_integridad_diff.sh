#!/bin/bash
# Revisor A: manifiesto SHA-256 de la entrega extraída y comprobaciones del diff (solo lectura).
# Uso: bash s06_integridad_diff.sh REPO_GIT ENTREGA_EXTRAIDA
R=$1; E=$2/resultados_m2/cobertura_vm
echo "## manifiesto: sha256sum -c (desde $E)"; (cd "$E" && sha256sum -c --quiet MANIFIESTO_SHA256.txt); echo "exit=$?"
echo "lineas manifiesto: $(grep -c . $E/MANIFIESTO_SHA256.txt)"
echo "archivos en carpeta fuera del manifiesto:"; (cd "$E" && find . -type f | sed 's|^\./||' | sort | comm -23 - <(awk '{print $2}' MANIFIESTO_SHA256.txt | sort))
echo "## diff d2419e5..2c41d68 (name-status)"; git -C $R diff --name-status d2419e5 2c41d68
echo "## fuera de resultados_m2/cobertura_vm:"; git -C $R diff --name-only d2419e5 2c41d68 | grep -v '^resultados_m2/cobertura_vm/' ; echo "grep_exit=$? (1 = ninguno)"
echo "## binarios en el diff (numstat '-'):"; git -C $R diff --numstat d2419e5 2c41d68 | awk '$1=="-"'; echo "fin"
echo "## PDF/XLSX/ZIP/pyc/__pycache__ en diff 615b292..2c41d68 y en el árbol 2c41d68:"
git -C $R diff --name-only 615b292 2c41d68 | grep -iE '\.(pdf|xlsx|xlsm|xls|zip|pyc)$|__pycache__'; echo "grep_diff_exit=$?"
git -C $R ls-tree -r --name-only 2c41d68 | grep -iE '\.(pdf|xlsx|xlsm|xls|zip|pyc)$|__pycache__'; echo "grep_arbol_exit=$?"
echo "## patrones de secreto en el diff:"
git -C $R diff d2419e5 2c41d68 | grep -nEi 'ghp_[A-Za-z0-9]|github_pat_|sk-[A-Za-z0-9]{16}|AKIA[0-9A-Z]{12}|BEGIN (RSA|OPENSSH|EC) PRIVATE|x-access-token|authorization: (bearer|basic)|password *[:=]'; echo "grep_secretos_exit=$?"
echo "## rutas absolutas locales en el diff:"; git -C $R diff d2419e5 2c41d68 | grep -cE '^\+.*(/workspace/|/home/|/root/|/tmp/)'; 
