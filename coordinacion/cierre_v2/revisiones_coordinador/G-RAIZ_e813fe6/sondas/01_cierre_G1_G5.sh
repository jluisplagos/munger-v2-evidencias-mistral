#!/usr/bin/env bash
# Sonda 01: comprobaciones de cierre G1-G5 sobre e813fe6 (solo lectura)
set -u
R=${REPO:?ruta al clon del producto}
C=e813fe66b0210a698398d4f9a4d84788f9dda8e3
cd "$R"
echo "== G1: grep regeneración / no aptos / C48 en CLAUDE.md"
git show $C:CLAUDE.md | grep -n -e 'regeneración' -e 'no aptos por entradas' -e 'C48 y C50' -e 'pendiente de decisión' -e 'U1' -e 'U6 (a)' -e '29/35' -e 'I19/H9'
echo "== G1: ya no aparece «1–6 corregidos»"
git show $C:CLAUDE.md | grep -n '1–6 corregidos'; echo "rc=$? (1 = ausente)"
echo "== G1: coherencia README (expedientes sin regenerar)"
git show $C:README.md | grep -n -e 'expedientes regenerados' -e 'expedientes siguen sin regenerar'
echo "== G2: esperar entrega final y conservarla"
for f in CLAUDE.md README.md; do git show $C:$f | grep -n -e 'Esperar su entrega final' -e 'esperar su entrega final' -e 'no se han importado' -e 'no están incorporadas' | sed "s|^|$f:|"; done
git show $C:docs/MIGRATION_STATUS.json | python3 -c 'import json,sys;d=json.load(sys.stdin);[print(k,"->",d[k]) for k in ("note","next_action","ongoing_claude_work")]'
echo "== G3: restricciones conservadas"
git show $C:README.md | grep -n -e 'sin incorporar correcciones propias al código del producto salvo decisión registrada' -e 'rama nueva con su manifiesto' -e 'INTEGRACION.md`:26 y :31'
echo "== G3: REC:10 (sin cambios)"
git show $C:docs/RECEPCION_ENTREGA_CLAUDE.md | sed -n 10p
git diff --quiet 957af65 $C -- docs/RECEPCION_ENTREGA_CLAUDE.md && echo "RECEPCION_ENTREGA_CLAUDE.md sin cambios"
echo "== G4: revisión externa pendiente"
for f in CLAUDE.md README.md; do git show $C:$f | grep -n 'pendiente de revisión externa\|revisión externa del hito 2 está pendiente' | cut -c1-160 | sed "s|^|$f:|"; done
echo "== G5: «sobre 957af65», sin «(commit 957af65)» ni «creada desde»"
for f in CLAUDE.md README.md; do git show $C:$f | grep -n -o 'sobre 957af65' | sed "s|^|$f:|"; done
git show $C:CLAUDE.md $C:README.md | grep -n -e '(commit 957af65)' -e 'creada desde 957af65'; echo "rc=$? (1 = ausente)"
git rev-parse origin/integracion/candidata-cierre-v2; git rev-parse 3149128^
