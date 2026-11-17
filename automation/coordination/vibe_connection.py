#!/usr/bin/env python3
"""Preparación de Vibe CLI; una prueba de autenticación requiere --execute."""
import argparse
import json
import os
from pathlib import Path
import subprocess
import tempfile

VERSION = '3.1.2'
MARKER = 'MUNGER_VIBE_CONEXION_OK'


def check(output, execute=False, runner=subprocess.run):
    report = {'state': 'PREPARADO_SIN_INFERENCIA', 'vibe_version_expected': VERSION,
              'authenticated': False, 'product_executed': False, 'accepted': False,
              'integrated': False, 'invocations_started': 0,
              'billing_source': 'NO_COMPROBADA_EN_CUENTA_MISTRAL'}
    key = os.getenv('MISTRAL_VIBE_CLI_KEY', '')
    if not key:
        report['state'] = 'PENDIENTE_CLAVE_VIBE_CLI'
    elif execute:
        # Directorios vacíos: no instrucciones, MCP ni hooks del repositorio.
        with tempfile.TemporaryDirectory(prefix='munger-vibe-') as tmp:
            home = Path(tmp) / 'vibe'; home.mkdir()
            work = Path(tmp) / 'work'; work.mkdir()
            export = Path(tmp) / 'export'
            (home / 'config.toml').write_text(
                'enable_auto_update = false\n'
                'enable_notifications = false\n'
                'api_retry_max_elapsed_time = 0\n'
                'api_stream_idle_timeout = 0\n'
                'output_limit_retries = 0\n'
                'agent_max_output_tokens = 512\n')
            env = {k: v for k, v in os.environ.items()
                   if k not in ('GH_TOKEN', 'GITHUB_TOKEN', 'ANTHROPIC_API_KEY',
                                'MISTRAL_API_KEY', 'MISTRAL_VIBE_CLI_KEY')}
            env.update(MISTRAL_API_KEY=key, VIBE_HOME=str(home))
            command = ['vibe', '--workdir', str(work), '--prompt',
                       'Responde únicamente con esta línea: ' + MARKER,
                       '--disabled-tools', '*', '--max-turns', '1',
                       '--max-tokens', '8192', '--max-price', '0.05',
                       '--time-limit', '90', '--output', 'text',
                       '--output-dir', str(export)]
            report['invocations_started'] = 1
            try:
                result = runner(command, env=env, cwd=work, capture_output=True,
                                text=True, timeout=110, check=False)
                doc = json.loads((export / 'export.json').read_text())
                report.update(exit_code=result.returncode, outcome=doc.get('outcome'),
                              vibe_version=doc.get('vibe_version'),
                              usage=doc.get('usage'), cost_reported_usd=doc.get('cost_usd'),
                              steps=doc.get('steps'))
                ok = (result.returncode == 0 and doc.get('outcome') == 'finished'
                      and doc.get('vibe_version') == VERSION and doc.get('steps') == 1
                      and not doc.get('subagents') and not doc.get('warnings')
                      and result.stdout.strip() == MARKER)
                report['authenticated'] = ok
                report['state'] = 'CONEXION_COMPROBADA' if ok else 'CONEXION_NO_VALIDADA_NO_REINTENTAR'
            except (subprocess.TimeoutExpired, OSError, ValueError):
                report['state'] = 'CONEXION_NO_VALIDADA_NO_REINTENTAR'
    output = Path(output); output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(report, ensure_ascii=False, indent=2) + '\n')
    return report


if __name__ == '__main__':
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--output', type=Path, required=True)
    p.add_argument('--execute', action='store_true')
    a = p.parse_args()
    r = check(a.output, a.execute)
    print(json.dumps(r, ensure_ascii=False))
