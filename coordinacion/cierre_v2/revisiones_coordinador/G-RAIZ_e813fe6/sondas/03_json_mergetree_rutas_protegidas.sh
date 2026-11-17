#!/usr/bin/env bash
# Sonda 03: JSON, merge-tree sobre 3149128, rutas locales e instrucciones protegidas (solo lectura)
set -u
R=${REPO:?ruta al clon del producto}
C=e813fe66b0210a698398d4f9a4d84788f9dda8e3
B=957af652cdc3bef3d67e8623c9572138bac685e9
P=3d66437e797b6b0bf137b42fa62b561f39121722
K=31491289a9a13a670dd563c1b2df85dad54eb74a
cd "$R"
echo "== JSON válido y recuentos"
git show $C:docs/MIGRATION_STATUS.json | python3 -c '
import json,sys
d=json.load(sys.stdin); print("JSON_OK claves:",len(d))
for k in ("tracked_baseline_files_copied","tracked_baseline_bytes_copied","release_asset_files","missing_git_files","candidate_branch","candidate_base_commit","candidate_source"): print(k,"=",d.get(k))'
git show $B:docs/MIGRATION_STATUS.json | python3 -c 'import json,sys;d=json.load(sys.stdin);print("base:",d.get("tracked_baseline_files_copied"),d.get("tracked_baseline_bytes_copied"),d.get("release_asset_files"),d.get("missing_git_files"))'
git cat-file -t "$(git show $C:docs/MIGRATION_STATUS.json | python3 -c 'import json,sys;print(json.load(sys.stdin)["candidate_base_commit"])')"
echo "== Archivos tocados frente a 957af65 y 3d66437"
git diff --name-only $B $C; echo "--"; git diff --name-only $P $C
echo "== Padre de e813fe6"; git rev-parse $C^
echo "== merge-tree --write-tree sobre 3149128"
T=$(git merge-tree --write-tree $K $C); echo "rc=$?"; echo "tree=$T" | head -1
for f in CLAUDE.md README.md docs/MIGRATION_STATUS.json; do a=$(git rev-parse "$T:$f" 2>/dev/null | head -1); b=$(git rev-parse $C:$f); [ "$a" = "$b" ] && echo "idéntico a e813fe6: $f" || echo "DIFIERE: $f"; done
echo "-- G-DOCS no toca los tres archivos:"; git diff --name-only $B $K -- CLAUDE.md README.md docs/MIGRATION_STATUS.json; echo "(vacío = no los toca)"
echo "-- resto del árbol fusionado = 3149128 salvo los tres archivos:"
git diff --name-only $K $(echo "$T" | head -1)
echo "== Rutas locales o datos personales en líneas añadidas (rc=1 = ninguna)"
git diff $B $C | grep '^+' | grep -v '^+++' | grep -n -E '/home/|/tmp/|/root/|[A-Za-z]:\\|~/|@[a-z0-9.-]+\.[a-z]{2,}|/Users/'; echo "rc=$?"
echo "== Instrucciones protegidas: líneas de 957af65 presentes literalmente en e813fe6"
python3 - "$B" "$C" <<'PY'
import subprocess,sys
b,c=sys.argv[1:3]
def lines(r,f): return subprocess.run(['git','show',f'{r}:{f}'],capture_output=True,text=True).stdout.splitlines()
claves=["Idioma: español claro.","Leer primero README.md","La base histórica está completa: 5790","No declarar completa la migración","1. página inexistente","2. fuente local ausente","3. redondeo aceptado","4. C48 de Elis","5. vigencia de fundamentos","6. relevo caducado","7. F1:","Mantener originales y decisiones humanas","No cambiar fuentes ni huellas","LibreOffice y pipelines","No reactivar aprobaciones","No inventar firmas","Usar Opus con esfuerzo alto","Fable con esfuerzo máximo","con aviso y registro","La revisión debe hacerse por un agente distinto","El encargo correctivo vigente","Para recuperar los binarios históricos"]
B=lines(b,'CLAUDE.md'); C=set(lines(c,'CLAUDE.md'))
for k in claves:
    src=[l for l in B if l.startswith(k)]
    for l in src: print(('IGUAL ' if l in C else 'CAMBIA ')+l[:90])
# README: todo a partir de la línea 9 (--- y siguientes) salvo :17
Rb=lines(b,'README.md'); Rc=lines(c,'README.md')
print('README líneas',len(Rb),len(Rc))
dif=[i+1 for i,(x,y) in enumerate(zip(Rb,Rc)) if x!=y]
print('README líneas distintas:',dif)
print('Main conserva 4.14 en README:5:', 'main' in Rc[4], Rc[4][:80])
PY
echo "== main sigue con la 4.14 y no contiene 957af65"
git merge-base --is-ancestor $B origin/main && echo "957af65 ES antecesor de main" || echo "957af65 no es antecesor de main"
git show origin/main:munger_v2_r1/VERSION | head -c 60; echo
