"""Revisor A3 · control negativo de A3-R7 con datos reales, en copias aisladas (no toca REPRO).
Unica cadena real con un operando derivado no piloto: Vidrala Análisis!C41 = C37 × C55, con
C55 derivado (piloto). Mutaciones:
 (a) derivaciones: C55 deja de ser piloto y su origen aux:acciones_propias_2025 pasa a
     CONFLICTO_CONTEXTUAL en verificacion_contexto.jsonl -> C55 CONFLICTO; C41 debe quedar CONFLICTO
     (hoy PENDIENTE por C37). Se ejecuta derivaciones.py de 0946971 y de 8b88fab sobre la misma copia.
 (b) control: en DERIVADOS.json publicado, C55 -> CONFLICTO_CONTEXTUAL sin recalcular C41:
     control_cobertura.py de 0946971 debe señalar C41; el de 8b88fab no lo ve.
Uso: python3 -I -B s08_r7_control_negativo_real.py REPRO SCRIPTS_8b88fab DEST SALIDA.json"""
import json, shutil, subprocess, sys
from pathlib import Path
repro, old_sc, dest, outp = map(Path, sys.argv[1:5])
res = {}
def copia(nombre, scripts_from=None):
    d = dest / nombre
    if d.exists(): shutil.rmtree(d)
    (d / '.trabajo').mkdir(parents=True)
    (d / '.trabajo/insumos_m2').symlink_to(repro / '.trabajo/insumos_m2')
    shutil.copytree(repro / 'docs', d / 'docs')
    shutil.copytree(repro / 'resultados_m2', d / 'resultados_m2')
    if scripts_from:
        sc = d / 'resultados_m2/cobertura_vm/scripts'; shutil.rmtree(sc); shutil.copytree(scripts_from, sc)
    return d
def run(d, script):
    p = subprocess.run([sys.executable, '-I', '-B', str(d / 'resultados_m2/cobertura_vm/scripts' / script)], cwd=d, capture_output=True, text=True)
    return p.returncode, (p.stdout + p.stderr)[-600:]
def mut_a(d):
    rp = d / 'docs/programa_mistral_m2/entrada/registro_base.json'
    reg = json.loads(rp.read_text(encoding='utf-8')); n = 0
    def walk(x):
        nonlocal n
        if isinstance(x, dict):
            if x.get('celda') == 'Análisis!C55' and x.get('clase') == 'derivado' and 'cubierta_en_piloto' in x and n == 0:
                x['cubierta_en_piloto'] = False; n += 1; return
            for v in x.values(): walk(v)
        elif isinstance(x, list):
            for v in x: walk(v)
    walk(reg['Vidrala']['entradas'])  # solo Vidrala
    rp.write_text(json.dumps(reg, ensure_ascii=False, indent=2), encoding='utf-8')
    vp = d / 'resultados_m2/cobertura_vm/resultados/verificacion_contexto.jsonl'
    ls = []
    for l in vp.read_text(encoding='utf-8').splitlines():
        x = json.loads(l)
        if x['empresa'] == 'Vidrala' and x['celda'] == 'aux:acciones_propias_2025':
            x['estado_contextual'] = 'CONFLICTO_CONTEXTUAL'
        ls.append(json.dumps(x, ensure_ascii=False))
    vp.write_text('\n'.join(ls) + '\n', encoding='utf-8')
    return n
def nodos(d):
    der = json.loads((d / 'resultados_m2/cobertura_vm/DERIVADOS.json').read_text(encoding='utf-8'))
    return {n['celda']: n['estado_contextual'] for n in der['nodos'] if n['empresa'] == 'Vidrala' and n['celda'] in ('Análisis!C55', 'Análisis!C41')}
for tag, sc in (('a_0946971', None), ('a_8b88fab', old_sc)):
    d = copia(tag, sc); n = mut_a(d)
    rc, o = run(d, 'derivaciones.py')
    res[tag] = {'piloto_desactivado': n, 'derivaciones_exit': rc, 'estados': nodos(d)}
for tag, sc in (('b_0946971', None), ('b_8b88fab', old_sc)):
    d = copia(tag, sc)
    dp = d / 'resultados_m2/cobertura_vm/DERIVADOS.json'
    der = json.loads(dp.read_text(encoding='utf-8'))
    for n in der['nodos']:
        if n['empresa'] == 'Vidrala' and n['celda'] == 'Análisis!C55': n['estado_contextual'] = 'CONFLICTO_CONTEXTUAL'
    dp.write_text(json.dumps(der, ensure_ascii=False, indent=2), encoding='utf-8')
    rc, o = run(d, 'control_cobertura.py')
    cc = json.loads((d / 'resultados_m2/cobertura_vm/resultados/control_cobertura.json').read_text(encoding='utf-8'))
    res[tag] = {'control_exit': rc, 'PASS': cc.get('PASS'), 'violaciones_C41': [v for v in cc.get('violaciones', []) if 'C41' in v], 'n_violaciones': len(cc.get('violaciones', []))}
outp.write_text(json.dumps(res, ensure_ascii=False, indent=1), encoding='utf-8')
print(json.dumps(res, ensure_ascii=False, indent=1))
