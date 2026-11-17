#!/usr/bin/env bash
# Sonda 02: respaldo archivo:línea de cada afirmación nueva de e813fe6 (solo lectura)
set -u
R=${REPO:?ruta al clon del producto}
A=${AUX:?ruta al clon auxiliar}
B=957af652cdc3bef3d67e8623c9572138bac685e9
D=munger_v2_r1/personaje_v2/empresas_v2_correcciones/2026-11_Vidrala_ensayo_4_15
cd "$R"
l(){ git show "$B:$1" | sed -n "$2p" | cut -c1-260 | sed "s|^|$3:$2: |"; }
echo "== VERSION:1 (hito 2; aptitud)"; l munger_v2_r1/VERSION 1 VERSION
echo "== H1 R1-R3 (16-40), I13 (42-63), I8/I9 (65-72)"; for n in 16 24 30 42 54 65 72; do l $D/HITO_1_4_15.md $n H1; done
echo "== H2 I20/I19/H9 (82-93), 190 (99)"; for n in 82 85 89 92 99; do l $D/hito2/HITO_2_4_15.md $n H2; done
echo "== H2 §7 (190-199) y §9 (211-220)"; for n in 190 192 194 195 196 197 198 211 214 215 216 219 220; do l $D/hito2/HITO_2_4_15.md $n H2; done
echo "== H2:9 y :20 (otra tarea, no incorporado)"; for n in 9 20; do l $D/hito2/HITO_2_4_15.md $n H2; done
echo "== PR:33-42 y 49-53"; for n in 33 35 37 39 40 42 49 51 52 53; do l $D/hito2/PUNTO_DE_RECUPERACION.md $n PR; done
echo "== Rutas citadas existen en 957af65"
for p in munger_v2_r1/VERSION $D/hito2/HITO_2_4_15.md $D/hito2/PUNTO_DE_RECUPERACION.md docs/RECEPCION_ENTREGA_CLAUDE.md docs/revision_externa_4_15_hito1 munger_v2_r1/personaje_v2/pruebas/test_verificacion_entradas_415.py; do git cat-file -e "$B:$p" 2>/dev/null && echo "existe: $p" || echo "FALTA: $p"; done
echo "== Contrato del programa (repositorio auxiliar)"
cd "$A"
git rev-parse HEAD; git diff --quiet ec707a5 HEAD -- coordinacion/cierre_v2/INTEGRACION.md && echo "INTEGRACION.md igual en ec707a5 y HEAD"
for n in 5 7 26 31; do sed -n "${n}p" coordinacion/cierre_v2/INTEGRACION.md | cut -c1-400 | sed "s|^|INTEGRACION.md:$n: |"; done
echo "== «técnica» en INTEGRACION.md (rc=1 = no aparece) y en CONTROL.json"
grep -n 'técnica' coordinacion/cierre_v2/INTEGRACION.md; echo "rc=$?"
grep -n '"tarea": "Candidata única de integración técnica"' coordinacion/cierre_v2/CONTROL.json
echo "== Solicitud de revisión registrada para e813fe6"
python3 - <<'PY'
import json
d=json.load(open('coordinacion/cierre_v2/CONTROL.json'))
def walk(o):
    if isinstance(o,dict):
        if o.get('id')=='G-RAIZ': yield o
        for v in o.values(): yield from walk(v)
    elif isinstance(o,list):
        for v in o: yield from walk(v)
for g in walk(d):
    s=g.get('solicitud_revision',{})
    print('commit_origen:',g.get('commit_origen'))
    print('commit_revisado:',g.get('commit_revisado'))
    print('solicitud.estado:',s.get('estado'),'sha_autor:',s.get('sha_autor'))
    print('siguiente_accion:',g.get('siguiente_accion'))
PY
