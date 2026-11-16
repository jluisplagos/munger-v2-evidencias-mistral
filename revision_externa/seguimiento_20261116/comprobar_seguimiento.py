"""Sondas limitadas: no ejecuta producto ni aceptación Qwen.

Uso: python3 -B comprobar_seguimiento.py --a WORKTREE_A --b WORKTREE_B
  --c WORKTREE_C --f1 WORKTREE_F1
Requiere los commits fijados en SEGUIMIENTO.md. Trabajar en copias aisladas.
"""
import argparse
from collections import Counter
import hashlib
import importlib.util
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import shutil

p = argparse.ArgumentParser()
for name in ('a', 'b', 'c', 'f1'):
    p.add_argument('--' + name, type=Path, required=True)
args = p.parse_args()
roots = {
    'a': args.a / 'resultados_m2/cobertura_vm',
    'b': args.b / 'resultados_m2/pm1',
    'c': args.c / 'resultados_m2/matematica_b',
    'f1': args.f1 / 'docs/validacion_economica_paralela/frente_E_F1_elis',
}
out = {'naturaleza': 'revision dirigida; no producto ni Qwen', 'manifiestos': {}}
for name, root in roots.items():
    passed, failed = 0, []
    for line in (root / 'MANIFIESTO_SHA256.txt').read_text().splitlines():
        if not line.strip() or line.startswith('#'):
            continue
        h, file = line.split(maxsplit=1)
        file = file.lstrip('*')
        q = root / file
        if q.is_file() and hashlib.sha256(q.read_bytes()).hexdigest() == h:
            passed += 1
        else:
            failed.append(file)
    out['manifiestos'][name] = {'coinciden': passed, 'fallos': failed}
    assert not failed, (name, failed)

rows = [json.loads(line) for line in (roots['a'] / 'resultados/verificacion_contexto.jsonl').read_text().splitlines()]
reviewed = [r for r in rows if r['estado_contextual'] == 'REVISADO_CONTEXTUAL']
out['a'] = {
    'fuentes_revisado_contextual': len(reviewed),
    'con_dimensiones_pendientes': sum(bool(r.get('pendientes')) for r in reviewed),
    'pendientes_por_dimension': dict(Counter(k for r in reviewed for k in r.get('pendientes', []))),
    'version_ok_sin_decidir': sum(r.get('checks', {}).get('version', [''])[0] == 'OK' and 'no decidible' in r.get('detalle', {}).get('version', '') for r in reviewed),
}
sys.path.insert(0, str(roots['a'] / 'scripts'))
spec = importlib.util.spec_from_file_location('contexto_sonda', roots['a'] / 'scripts/verificar_contexto.py')
v = importlib.util.module_from_spec(spec)
spec.loader.exec_module(v)
out['a']['sonda_euros_sin_miles'] = v.check_unidad(['Amounts in euros', 'Revenue 1000'], 1, 'miles de euros', '0.001', 1000, 'Revenue 1000')

with tempfile.TemporaryDirectory() as tmp:
    copy = Path(tmp) / 'matematica_b'
    shutil.copytree(roots['c'], copy)
    script = copy / 'codigo/efectos_probabilidades.py'
    normal = subprocess.run([sys.executable, '-B', str(script)], capture_output=True, text=True)
    assert normal.returncode == 0, normal.stderr
    identical = (copy / 'EFECTOS_PROBABILIDADES.csv').read_bytes() == (roots['c'] / 'EFECTOS_PROBABILIDADES.csv').read_bytes()
    assert identical
    cases = copy / 'casos_fijados.json'
    data = json.loads(cases.read_text())
    for entry in data['identidad']:
        if entry['caso'] == 'H6':
            entry['perimetro'] = 'NIIF 16'
    cases.write_text(json.dumps(data))
    mutated = subprocess.run([sys.executable, '-B', str(script)], capture_output=True, text=True)
    assert mutated.returncode == 1 and 'FALLA' in mutated.stdout
    out['c'] = {'normal': json.loads(normal.stdout), 'csv_identico': identical,
                'sonda_extremo_real_h6_mutado': {'exit': mutated.returncode, 'detectado': True}}
    out['c']['normal'].pop('destino', None)
print(json.dumps(out, ensure_ascii=False, indent=2))
