#!/usr/bin/env python3
"""Inventario por job (PyYAML): disparadores, secretos de inferencia, environment, instalaciones.

Uso: python3 -I sonda_workflows_por_job.py <raiz_del_repositorio>
No conforme si un job con ANTHROPIC_API_KEY o MISTRAL_VIBE_CLI_KEY se dispara con push,
pull_request*, schedule o workflow_run, o no declara environment; también si un job con
ANTHROPIC_API_KEY instala paquetes o comparte job con MISTRAL_VIBE_CLI_KEY.
Comprueba además el uso de secretos en el nivel `env:` del workflow (fuera de los jobs).
"""
import json
from pathlib import Path
import re
import sys

import yaml

INFERENCE = {'ANTHROPIC_API_KEY', 'MISTRAL_VIBE_CLI_KEY'}
AUTO = {'push', 'pull_request', 'pull_request_target', 'schedule', 'workflow_run', 'issue_comment', 'release'}
root = Path(sys.argv[1])
rows, bad = [], 0
for path in sorted((root / '.github/workflows').glob('*.y*ml')):
    doc = yaml.safe_load(path.read_text())
    on = doc.get('on', doc.get(True))
    triggers = [on] if isinstance(on, str) else list(on or [])
    top_secrets = set(re.findall(r'secrets\.([A-Z_]+)', yaml.safe_dump(doc.get('env', {}))))
    for name, job in doc.get('jobs', {}).items():
        dump = yaml.safe_dump(job)
        secrets = set(re.findall(r'secrets\.([A-Z_]+)', dump)) | top_secrets
        env = job.get('environment')
        env = env.get('name') if isinstance(env, dict) else env
        installs = sum('pip install' in (s.get('run') or '') for s in job.get('steps', []))
        hashes = sum('--require-hashes' in (s.get('run') or '') for s in job.get('steps', []))
        problems = []
        if secrets & INFERENCE:
            if set(triggers) & AUTO:
                problems.append('secreto_de_inferencia_con_disparador_automatico')
            if not env:
                problems.append('secreto_de_inferencia_sin_environment')
        if 'ANTHROPIC_API_KEY' in secrets and (installs or 'MISTRAL_VIBE_CLI_KEY' in secrets):
            problems.append('anthropic_con_instalacion_o_mistral')
        perms = job.get('permissions', doc.get('permissions'))
        rows.append({'workflow': path.name, 'job': name, 'disparadores': triggers,
                     'secretos': sorted(secrets), 'environment': env, 'permisos': perms,
                     'pip_install': installs, 'require_hashes': hashes, 'problemas': problems})
        bad += bool(problems)
for r in rows:
    print(json.dumps(r, ensure_ascii=False))
print(json.dumps({'jobs': len(rows), 'jobs_no_conformes': bad,
                  'jobs_con_secreto_de_inferencia': sum(bool(set(r['secretos']) & INFERENCE) for r in rows),
                  'jobs_con_pip_sin_hashes': sum(r['pip_install'] > r['require_hashes'] for r in rows)}, ensure_ascii=False))
