#!/bin/bash
# Genera las sondas S01–S13 de la revisión de la v3. Solo lectura (git show, git status, grep, sha256sum). Uso: CAND=<candidata> AUX=<aux> bash generar_sondas.sh
set -u
C=${CAND:?}; A=${AUX:?}; O=$(cd "$(dirname "$0")/.." && pwd); H="$O/herramientas"
M=coordinacion/cierre_v2/manual; V3=$A/$M/MANUAL_OPERATIVO_3149128_v3.md
T=$(mktemp -d)
san() { sed -e "s|$C|<candidata>|g" -e "s|$A|<aux>|g" -e "s|$T|<tmp>|g" -e "s|/home/user|<home>|g" -e "s|/root/|<root>/|g"; }
s() { local f=$1; shift; { echo "# $f · $(date -u +%FT%TZ)"; "$@"; } 2>&1 | san > "$O/$f"; }
B=munger_v2_r1/personaje_v2/empresas_v2_correcciones
B2=personaje_v2/empresas_v2_correcciones
s S01_identidad.txt bash -c "
echo '## aux'; git -C $A rev-parse HEAD; git -C $A log --oneline -8; echo; echo '## commits que tocan el material revisado'; git -C $A log --format='%h %s' -- $M/MANUAL_OPERATIVO_3149128_v3.md $M/PROPUESTA_CONTINUIDAD_2_5.md $M/CAMBIOS_FRENTE_A_957af65.md $M/sondeo_literales_v3 $M/MANIFIESTO_SHA256.txt
echo; echo '## manifiesto de manual/ en HEAD'; (cd $A/$M && sha256sum -c MANIFIESTO_SHA256.txt); echo; echo '## v2 (ef36ab1) = MANUAL_OPERATIVO_3149128.md en HEAD'; git -C $A show ef36ab1:$M/MANUAL_OPERATIVO_3149128.md | cmp - $A/$M/MANUAL_OPERATIVO_3149128.md && echo igual
echo; echo '## diff v2 -> v3: bloques, líneas añadidas, suprimidas'; git -C $A show ef36ab1:$M/MANUAL_OPERATIVO_3149128.md > $T/v2.md; diff -U0 $T/v2.md $V3 | grep -c '^@@'; diff $T/v2.md $V3 | grep -c '^>'; diff $T/v2.md $V3 | grep -c '^<'
echo; echo '## candidata'; git -C $C rev-parse HEAD; git -C $C status | head -2; git -C $C log --oneline -3; echo 'status --short (líneas):'; git -C $C status --short | wc -l
"
s S02_M1_copias_v64.txt bash -c "
cd $C/munger_v2_r1; python3 -I -B - <<'PY'
import re
src=open('$B2/2026-11_Vidrala_ensayo_4_13/scripts/controles_historicos_4_13.py').read()
C='personaje_v2/empresas_v2_correcciones/'; ctl=[(C if m.group(2) else '')+m.group(3) for m in re.finditer(r'\(\"([0-9a-z_]+)\", (C \+ )?\"([^\"]+\.py)\"',src)]
print('controles en controles_historicos_4_13.py:28-48:',len(ctl))
pat=re.compile(r'copytree|os\.walk|rglob|\.glob\(|listdir|_v64|mkdtemp|shutil\.copy|rmtree')
for c in ctl:
    L=open(c,encoding='utf-8').read().split('\n'); h=[(i+1,l.strip()[:200]) for i,l in enumerate(L) if pat.search(l)]
    print(f'\n## {c} · {len(h)} coincidencias')
    for i,l in h: print(f'  {i}: {l}')
PY
echo; echo '## líneas citadas por la v3 y la Propuesta'
awk 'NR==38||(NR>=73&&NR<=77)||NR==109||NR==124||NR==125||NR==130||NR==184{print \"4_8_1:\"NR\": \"\$0}' $B2/2026-11_Vidrala_ensayo_4_8_1/scripts/comprobar_entrega_4_8_1.py | cut -c1-230
awk '(NR>=54&&NR<=60)||NR==75||NR==82||NR==84||NR==85||NR==91||NR==94||NR==195{print \"4_8:\"NR\": \"\$0}' $B2/2026-11_Vidrala_ensayo_4_8/scripts/comprobar_entrega_4_8.py | cut -c1-230
grep -n actuales $B2/2026-11_Vidrala_ensayo_4_9/scripts/comprobar_entrega_4_9.py | sed 's/^/4_9:/' | cut -c1-200
sed -n '87p' $B2/2026-11_Vidrala_ensayo_4_11/scripts/comprobar_entrega_4_11.py | sed 's/^/4_11:87: /'; sed -n '91p' $B2/2026-11_Vidrala_ensayo_4_12/scripts/comprobar_entrega_4_12.py | sed 's/^/4_12:91: /'; awk 'NR==55||NR==107{print \"4_13:\"NR\": \"\$0}' $B2/2026-11_Vidrala_ensayo_4_13/scripts/comprobar_entrega_4_13.py | cut -c1-200
awk 'NR==39||NR==41||NR==59{print \"controles_historicos:\"NR\": \"\$0}' $B2/2026-11_Vidrala_ensayo_4_13/scripts/controles_historicos_4_13.py | cut -c1-200
echo; echo '## REG resumen.md:15 y :17'; sed -n '15p;17p' $A/coordinacion/cierre_v2/traspaso/resultado_20261117/registro/paso10_controles_historicos/resumen.md | cut -c1-260
"
s S03_M2_entorno_candidata.txt bash -c "
cd $C; echo \"HEAD \$(git rev-parse HEAD) (los archivos de munger_v2_r1/ son iguales en 3149128 y en HEAD: \$(git diff --stat 3149128 HEAD -- munger_v2_r1 | wc -l) líneas de diff)\"
echo \"status --short: \$(git status --short | wc -l)\"; echo \"status --short --ignored: \$(git status --short --ignored | wc -l)\"; git status --short --ignored | awk '{print (\$2 ~ /\/\$/)?\"carpeta\":\"archivo\"}' | sort | uniq -c
echo \"PDF en munger_v2_r1: \$(find munger_v2_r1 -name '*.pdf' | wc -l)\"; G=\$(git rev-parse --git-common-dir); echo \"info/exclude: \$(wc -l < \$G/info/exclude) líneas · comentarios \$(grep -c '^#' \$G/info/exclude) · rutas \$(grep -v -c '^#' \$G/info/exclude)\"
grep -v '^#' \$G/info/exclude | sed 's|^/||' | sort > $T/ex; git status --short --ignored | awk '\$2 ~ /\.json\$/{print \$2}' | sort > $T/ij; echo \"JSON ignorados: \$(wc -l < $T/ij) · diff con info/exclude: \$(diff $T/ex $T/ij | wc -l) líneas\"
python3 -I -B -c \"
import json,os,subprocess,collections
b=json.load(open('baselines/4.14.json')); ra=['munger_v2_r1/'+f['path'] for f in b['files'] if f.get('storage')=='release_asset']
print('release_asset',len(ra),dict(collections.Counter(os.path.splitext(p)[1].lower() for p in ra)))
print('existen',sum(os.path.isfile(p) for p in ra))
r=subprocess.run(['git','check-ignore','-v','--stdin'],input='\n'.join(ra),capture_output=True,text=True).stdout.split('\n')
print('ignorados',len([l for l in r if l]),dict(collections.Counter(('info/exclude' if 'info/exclude' in l else l.split(chr(9))[0]) for l in r if l)))\"
cd munger_v2_r1; echo \"manifiesto: \$(tail -n +2 MANIFIESTO_SHA256.txt | wc -l) entradas\"; tail -n +2 MANIFIESTO_SHA256.txt | sha256sum -c --quiet; echo \"sha256sum -c --quiet código \$?\"
"
s S04_M3_marcas_traspaso.txt bash -c "
echo 'líneas con «probado en el traspaso»:'; grep -c -i -E 'probad[oa]s? en el traspaso' $V3; echo 'de ellas sin «autodeclarado»:'; grep -i -E 'probad[oa]s? en el traspaso' $V3 | grep -v -i -c autodeclarad
grep -n -i -E 'probad[oa]s? en el traspaso' $V3 | grep -o -E '^[0-9]+:.{0,150}'
echo; echo '## REVT/REVISION_TRASPASO.md:30 y :54-75'; sed -n '30p;54,75p' $A/coordinacion/cierre_v2/traspaso/revision_20261117/REVISION_TRASPASO.md | cut -c1-220
"
s S05_M4_marcas_comandos.txt bash -c "
python3 -I -B $H/marcas_comandos.py $V3
echo; echo 'Nota del revisor: los «SIN MARCA» de las líneas 174, 194, 225 y 335 son la propia marca (texto sangrado), no un comando; el bloque 598-607 es la plantilla, marcada **[NO DOCUMENTADO]** en la línea 593.'
echo; echo '## órdenes en línea y sus marcas'; grep -n -o -E '(verify --git-only|bash verificar_paquete.sh\x60, sin \x60completa|verificacion_entradas.py plantilla CARPETA|verificacion_entradas.py comprobar CARPETA).{0,70}' $V3
echo; echo '## F1PREP: órdenes y códigos'; P=docs/validacion_economica_paralela/frente_E_F1_elis/evidencias/preparacion; git -C $C show 03e7851:\$P/log_base414.txt | awk 'NR==2||NR==12||NR==14||NR==23'; git -C $C show 03e7851:\$P/preparacion.json | python3 -I -B -c \"
import json,sys; d=json.load(sys.stdin); p=d['paso4_worktree_B']; print('copia_binarios claves:',list(p['copia_binarios'])); print('manifiesto_B.comando:',p['manifiesto_B']['comando'],'· código',p['manifiesto_B']['codigo_salida']); print('paso2.codigo_salida_alternativa:',d['paso2_descarga']['codigo_salida_alternativa'])\"
"
s S06_continuidad_2_5_literal.txt python3 -I -B $H/literal_2_5.py $C $A
s S07_sondeo_literales.txt bash -c "
echo '## 1. reproducción del sondeo del autor (python3 -I -B sondeo_literales_v3.py <candidata>) frente a salida.txt'; python3 -I -B $A/$M/sondeo_literales_v3/sondeo_literales_v3.py $C > $T/rep.txt; echo \"código \$?\"; tail -n +2 $A/$M/sondeo_literales_v3/salida.txt | grep -v '^\[código' | diff - $T/rep.txt && echo 'salida idéntica a salida.txt'
echo; echo '## 2. sondeo independiente (universo ampliado)'; python3 -I -B $H/sondeo_independiente.py $C $A
echo; echo '## 3. uso de CONTINUIDAD en los controles: regex, count, split'; cd $C/munger_v2_r1/personaje_v2/empresas_v2_correcciones; grep -n -E 're\.(search|findall|match|finditer|sub)\([^)]*\b(cont|prom|prm)\b|\b(cont|prom|prm)\.(count|split|index|find)\(' 2026-11_Vidrala_ensayo_4_*/scripts/comprobar_entrega_*.py | cut -c1-260
echo; echo '## 4. ¿algún script o control ejecuta archivos_citados.py?'; git -C $C grep -n 'archivos_citados' 3149128 -- '*.py' '*.sh' | wc -l
"
s S08_discrepancias.txt bash -c "
echo '## m5: paso 13/14 del traspaso frente a filas 13/14 del §10'; sed -n '37,38p' $A/coordinacion/cierre_v2/traspaso/resultado_20261117/INFORME_TRASPASO.md | cut -c1-330; sed -n '70,72p' $A/coordinacion/cierre_v2/traspaso/revision_20261117/REVISION_TRASPASO.md | cut -c1-200
echo '-- primeras líneas de REG/paso_h9_pipeline.txt y REG/paso_p13_pipeline.txt'; head -1 $A/coordinacion/cierre_v2/traspaso/resultado_20261117/registro/paso_h9_pipeline.txt | cut -c1-220; head -1 $A/coordinacion/cierre_v2/traspaso/resultado_20261117/registro/paso_p13_pipeline.txt | cut -c1-220
echo '-- filas 13 y 14 del §10 en v2 (ef36ab1) y v3'; git -C $A show ef36ab1:$M/MANUAL_OPERATIVO_3149128.md | grep -E '^\| 1[34] \|' | cut -c1-200; grep -E '^\| 1[34] \|' $V3 | cut -c1-200
echo '-- v2:508 y v3:537'; git -C $A show ef36ab1:$M/MANUAL_OPERATIVO_3149128.md | sed -n 508p | cut -c1-200; sed -n 537p $V3 | cut -c1-330
echo; echo '## S-12: paso_pipeline.py en la guía'; G=munger_v2_r1/personaje_v2/GUIA_RECORRIDO_SUPERVISADO.md; for r in 957af65 3149128; do echo \"\$r:\"; git -C $C show \$r:\$G | grep -n -o 'paso_pipeline.py CARPETA \[--config …\]\` hace una pasada'; done; git -C $C ls-tree -r --name-only 3149128 | grep '_4_13/scripts/paso_pipeline.py'
echo; echo '## REVISION v2, m1, texto sobre S-12'; grep -o 'v1:255; lo quitó G-DOCS de la guía' $A/coordinacion/cierre_v2/revisiones_coordinador/MANUAL_v2_ef36ab1/REVISION_MANUAL_v2_ef36ab1.md
"
s S09_citas_v3.txt bash -c "
cd $H; for f in MANUAL_OPERATIVO_3149128_v3.md PROPUESTA_CONTINUIDAD_2_5.md CAMBIOS_FRENTE_A_957af65.md; do echo \"## \$f\"; CAND=$C AUX=$A python3 -I -B citas_v3.py $A/$M/\$f $T/\$f.cit; grep -E 'NO EXISTE|FUERA|AMBIG|sin archivo' $T/\$f.cit | cut -c1-200; done
echo; echo 'Detalle completo de las citas de la v3 en S09_citas_v3_detalle.txt'; cp $T/MANUAL_OPERATIVO_3149128_v3.md.cit $T/det
"
san < $T/MANUAL_OPERATIVO_3149128_v3.md.cit > "$O/S09_citas_v3_detalle.txt"
s S10_rutas_locales.txt bash -c "
cd $A/$M; grep -n -o -E '/home[^ \x60)]*|/root[^ \x60)]*|/tmp[^ \x60)}\"]*|/Users/[^ \x60)]*|claude-0[^ ]*|e_work/[^ \x60>)]*' MANUAL_OPERATIVO_3149128_v3.md PROPUESTA_CONTINUIDAD_2_5.md CAMBIOS_FRENTE_A_957af65.md sondeo_literales_v3/* | sort | uniq -c
echo '-- apariciones de /tmp que no son \${TMPDIR:-/tmp}:'; grep -n '/tmp' MANUAL_OPERATIVO_3149128_v3.md PROPUESTA_CONTINUIDAD_2_5.md CAMBIOS_FRENTE_A_957af65.md sondeo_literales_v3/* | grep -v -F '\${TMPDIR:-/tmp}' | wc -l
echo '-- HOME y <root>:'; grep -n -o -E '.{0,30}(\\\$HOME|<root>|/root).{0,30}' MANUAL_OPERATIVO_3149128_v3.md
"
s S11_candidata_avanzada.txt bash -c "
cd $C; git log --format='%h %cd %s' --date=iso -3; echo; git diff --stat 3149128 b129b36; echo; for r in 3149128 b129b36; do echo \"== \$r\"; git show \$r:README.md | sed -n 1p; git show \$r:CLAUDE.md | sed -n 1p | cut -c1-120; git show \$r:CLAUDE.md | grep -n -E 'LibreOffice y pipelines|Usar Opus|distinto del autor|No interrumpir|exclusivas de la base' | cut -c1-60; git show \$r:munger_v2_r1/CONTINUIDAD.md | grep -c 'los controles no recorren'; done
echo; echo '-- v3 sobre la rama:'; grep -n -o -E 'que hoy apunta a .{0,12}|HEAD \x603149128\x60.{0,40}|dicen «hito 1»' $V3
"
s S12_cambios_correspondencia.txt bash -c "
cd $A/$M; echo 'v1 -> v2 bloques:'; diff -U0 MANUAL_OPERATIVO_957af65.md MANUAL_OPERATIVO_3149128.md | grep -c '^@@'
python3 -I -B - <<'PY'
import re,subprocess
h=[re.sub(r'^@@ (-\S+) (\+\S+) @@.*',r'\1 \2',l) for l in subprocess.run(['diff','-U0','MANUAL_OPERATIVO_957af65.md','MANUAL_OPERATIVO_3149128.md'],capture_output=True,text=True).stdout.split('\n') if l.startswith('@@')]
t=open('CAMBIOS_FRENTE_A_957af65.md',encoding='utf-8').read(); sec=t.split('## 4.')[1].split('## 5.')[0]
tab={int(m.group(1)):(m.group(2).strip(),m.group(3).strip()) for m in re.finditer(r'\| (\d+) \x60([^\x60]+)\x60 \| ([^|]+) ',sec)}
print('filas de la tabla §4:',len(tab),'· cabeceras distintas del diff:',sum(1 for i,x in enumerate(h) if tab.get(i+1,('',''))[0]!=x))
for n in (35,59,64,69): print(f'bloque {n} {h[n-1]} -> filas: {tab[n][1]}')
PY
echo '-- v2: dónde están 7d (13 esperas) y G-06 (N-12 por lectura)'; grep -n -o -E 'Hay 13 esperas|13 esperas; ninguna|N-12 \| Si .{0,30}Cerrado por lectura|Por lectura, no llama a LibreOffice' MANUAL_OPERATIVO_3149128.md
echo; echo 'v2 -> v3 bloques:'; diff -U0 MANUAL_OPERATIVO_3149128.md MANUAL_OPERATIVO_3149128_v3.md | grep -c '^@@'
echo; echo '-- CAMBIOS:145 frente al manifiesto'; sed -n 145p CAMBIOS_FRENTE_A_957af65.md; grep -E 'v3|sondeo' MANIFIESTO_SHA256.txt; sha256sum -c MANIFIESTO_SHA256.txt
"
s S13_menores.txt bash -c "
cd $C; echo '## m2'; grep -c 'excluyendo solo' $V3 $A/$M/PROPUESTA_CONTINUIDAD_2_5.md
echo '## m3'; awk 'NR>=52&&NR<=54||NR==78||NR==82' $B/2026-11_Vidrala_ensayo_4_13/scripts/controles_historicos_4_13.py
echo '## m4'; git show 3149128:munger_v2_r1/personaje_v2/GUIA_RECORRIDO_SUPERVISADO.md | sed -n 141p; git show 3149128:$B/2026-11_Vidrala_ensayo_4_15/hito2/HITO_2_4_15.md | sed -n 92p | cut -c1-200
echo '## m6'; python3 -I -B -c \"
import subprocess
s=lambda r:subprocess.run(['git','show',r+':README.md'],capture_output=True,text=True).stdout.split(chr(10))
c,m=s('3149128'),s('d69d483')
for (a,b),(x,y) in [((33,35),(23,25)),((39,39),(29,29)),((41,41),(31,31)),((42,43),(32,33)),((45,45),(35,35)),((46,46),(36,36)),((51,51),(41,41))]: print(a,b,'->',x,y,c[a-1:b]==m[x-1:y])
print('README:5 en main:',c[4] in m)\"; git diff --stat d69d483 3149128 -- tools/base_414.py .gitignore | wc -l; git rev-parse origin/main
echo '## m10'; F=$B/2026-11_Vidrala_ensayo_4_14/documentacion_cierre_4_14/INCIDENCIAS_4_14.md; git show 3149128:\$F | wc -l; git show 3149128:\$F | awk 'NR==144||NR==161||NR==169||NR==178' | cut -c1-80; git show 3149128:\$F | sha256sum | cut -c1-16
echo '## m11 (CONTROL.json en acea175)'; git -C $A show acea175:coordinacion/cierre_v2/CONTROL.json > $T/ctl.json; python3 -I -B -c \"
import re
L=open('$T/ctl.json').read().split(chr(10))
for n in (34,35,589,762,810,817,818,841):
    i=n-1
    while i>0 and not re.search(r'\\\"id\\\": \\\"|candidata_integrada',L[i]): i-=1
    print(n,L[n-1].strip()[:70],'· bloque:',L[i].strip()[:40])\"; sha256sum $T/ctl.json | cut -c1-16
echo '## citados de EVID: cambios acea175 -> 88144b5'; git -C $A diff --stat acea175 88144b5 -- coordinacion/cierre_v2/PROGRAMA.md coordinacion/cierre_v2/INTEGRACION.md coordinacion/cierre_v2/traspaso coordinacion/cierre_v2/herramientas coordinacion/cierre_v2/pruebas_candidata AGENTS.md | wc -l
echo '## m12'; sed -n 24p $A/coordinacion/cierre_v2/traspaso/resultado_20261117/INFORME_TRASPASO.md | cut -c1-200
echo '## §13: prefijos nuevos de la v3'; for f in $B/2026-11_Vidrala_ensayo_4_14/documentacion_cierre_4_14/INCIDENCIAS_4_14.md $B/2026-11_Vidrala_ensayo_4_8/scripts/comprobar_entrega_4_8.py $B/2026-11_Vidrala_ensayo_4_9/scripts/comprobar_entrega_4_9.py $B/2026-11_Vidrala_ensayo_4_11/scripts/comprobar_entrega_4_11.py $B/2026-11_Vidrala_ensayo_4_12/scripts/comprobar_entrega_4_12.py $B/2026-11_Vidrala_ensayo_4_13/scripts/comprobar_entrega_4_13.py; do echo \"\$(git show 3149128:\$f | sha256sum | cut -c1-16) \$f\"; done; echo \"\$(git show d69d483:README.md | sha256sum | cut -c1-16) origin/main README.md\"
echo '## sondeo: huellas'; sha256sum $A/$M/sondeo_literales_v3/*
"
python3 -I -B - "$T/v2.md" "$V3" "$O/S09_citas_v3_detalle.txt" "$O/S09b_citas_lineas_cambiadas.txt" <<'PY'
import re,subprocess,sys
v2,v3,det,out=sys.argv[1:5]; ch=set()
for l in subprocess.run(['diff',v2,v3],capture_output=True,text=True).stdout.split('\n'):
    m=re.match(r'^\d+(?:,\d+)?[acd](\d+)(?:,(\d+))?',l)
    if m: a=int(m.group(1)); ch|=set(range(a,int(m.group(2) or a)+1))
o=[];k=False
for l in open(det,encoding='utf-8'):
    m=re.match(r'^L(\d+): ',l)
    if m: k=int(m.group(1)) in ch
    if k: o.append(l)
open(out,'w',encoding='utf-8').write('# S09b: citas de las líneas de la v3 que cambian frente a la v2\n'+''.join(o))
PY
rm -rf "$T"
