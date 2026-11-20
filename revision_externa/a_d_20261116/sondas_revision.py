"""Revisión dirigida A/D. No ejecuta aceptación completa ni acredita revisión humana.

python3 -B sondas_revision.py --a WORKTREE_A --d WORKTREE_D --salida SALIDA.json
Commits: A 0224b7182dd05d1e396223781d6f5db8b325ce2e; D b42f453caf0ca777b5fa56e6542ad0cc49130b9f.
Las sondas sintéticas no son datos de empresas. Trabajar en copias aisladas.
"""
import argparse
from collections import Counter
import hashlib
import importlib.util
import json
import os
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile

p = argparse.ArgumentParser()
p.add_argument('--a', type=Path, required=True)
p.add_argument('--d', type=Path, required=True)
p.add_argument('--salida', type=Path, required=True)
a = p.parse_args()
ar = a.a.resolve() / 'resultados_m2/cobertura_vm'
dr = a.d.resolve() / 'resultados_qwen/ejecucion_d'
out = {'alcance': 'sondas de auxiliares, no aceptación completa del personaje'}
out['manifiestos'] = {}
for label, root in [('A', ar), ('D', dr)]:
    ok, bad = 0, []
    for line in (root / 'MANIFIESTO_SHA256.txt').read_text().splitlines():
        if not line.strip() or line.startswith('#'):
            continue
        sha, file = line.split(maxsplit=1)
        q = root / file.lstrip('*')
        if q.is_file() and hashlib.sha256(q.read_bytes()).hexdigest() == sha:
            ok += 1
        else:
            bad.append(file)
    out['manifiestos'][label] = {'coinciden': ok, 'fallos': bad}

sys.path.insert(0, str(ar / 'scripts'))
spec = importlib.util.spec_from_file_location('verificador_a_revisado', ar / 'scripts/verificar_contexto.py')
v = importlib.util.module_from_spec(spec)
spec.loader.exec_module(v)
out['A_sondas'] = {}
s = out['A_sondas']
s['euros_no_miles'] = v.check_unidad(['Amounts in euros', 'Revenue 10000'], 1, 'miles de euros', '0.001', 10000, 'Revenue 10000')
s['escala_erronea_con_cabecera'] = v.check_unidad(['Revenue 10000'], 0, 'miles de euros', '1', 10000, 'Revenue 10000', {'miles': True})
s['columna_equivocada_aceptada'] = v.check_columna(1, ['2025 2024', 'Revenue 10000 9000'], ['2025', '2024'], '2025 2024', ['2025', '2024'], '2024 (columna comparativa del informe 2025)', 'ejercicio 2024', 10000)
with tempfile.TemporaryDirectory() as td:
    orig = Path(td) / 'CF_2024.txt'
    orig.write_text('[PDF PAGE 1]\nConsolidated accounts 2024\n2024 2023\nRevenue 10000 9000\n')
    v.TEXTO_CACHE['SINTETICA'] = {orig.name: orig}
    f = {'archivo': 'CF_2025.txt', 'columna': '2024', 'periodo': 'ejercicio 2024', 'cita': 'Revenue 9000', 'valor_fuente': 9000, 'reexpresado': 'no reexpresado; igual al original'}
    s['reexpresion_toma_otra_columna'] = v.check_reexpresion('SINTETICA', {}, f, ['2025', '2024'], ['2025', '2024'])
    orig.write_text('[PDF PAGE 1]\nConsolidated accounts 2024\n2024 2023\nRevenue 10000 8000\n')
    s['contradiccion_reexpresion_devuelve_ok'] = v.check_reexpresion('SINTETICA', {}, f, ['2025', '2024'], ['2025', '2024'])

# El generador copia etiquetas estáticas aun sin evidencia ni candidato disponible.
with tempfile.TemporaryDirectory() as td:
    root = Path(td) / 'd'
    shutil.copytree(dr / 'scripts', root / 'scripts', ignore=shutil.ignore_patterns('__pycache__'))
    bank = Path(td) / 'bank'
    bank.mkdir()
    # Solo los IDs/naturaleza/precondiciones del banco que el generador requiere.
    normative = subprocess.check_output(['git', '-C', str(a.d), 'show', '4745f3887f7fd86bb3052f5d5e32285862df18e3:resultados_qwen/q1_v2/banco_revisado/casos_aceptacion.jsonl'], text=True)
    (bank / 'casos_aceptacion.jsonl').write_text(normative)
    r = subprocess.run([sys.executable, '-B', str(root / 'scripts/generar_matriz.py')], env=dict(os.environ, BANCO_DIR=str(bank)), capture_output=True, text=True)
    import csv
    rows = list(csv.DictReader((root / 'MATRIZ_EJECUCION.csv').open()))
    out['D_matriz_sin_evidencias'] = {'exit': r.returncode, 'carpeta_evidencias_existe': (root / 'evidencias').exists(), 'filas': len(rows), 'veredictos': dict(Counter(x['veredicto'] for x in rows))}
    # Entorno defectuoso: directorio scripts existe pero no contiene código de producto.
    # Es una sonda del arnés, nunca un resultado del producto real.
    fake = Path(td) / 'candidata_incompleta'
    (fake / 'munger_v2_r1/personaje_v2/scripts').mkdir(parents=True)
    template = Path(td) / 'template'
    template.mkdir()
    (template / 'verificacion_entradas.json').write_text(json.dumps({'entradas': [{'celda': 'Historia!C23'}]}))
    env = dict(os.environ, CANDIDATA_DIR=str(fake), PLANTILLA_EXP=str(template), RUN_DIR=str(Path(td) / 'run'))
    r = subprocess.run([sys.executable, '-B', str(root / 'scripts/ejecutar_caso.py'), str(root / 'scripts/especificaciones/piloto/Q1-001.json')], env=env, capture_output=True, text=True)
    evidence = json.loads((root / 'evidencias/Q1-001/resultado_ejecucion.json').read_text())
    out['D_arnes_sin_scripts_producto'] = {'exit_arnes': r.returncode, 'stdout_arnes': r.stdout.strip(), 'exits_comandos': [x['exit'] for x in evidence['pasos']]}

out['D_inventario'] = {'especificaciones': len(list((dr / 'scripts/especificaciones').glob('*/*.json'))), 'resultados_por_caso': len(list((dr / 'evidencias').glob('*/resultado_ejecucion.json')))}
a.salida.write_text(json.dumps(out, ensure_ascii=False, indent=2))
print(json.dumps(out, ensure_ascii=False, indent=2))
