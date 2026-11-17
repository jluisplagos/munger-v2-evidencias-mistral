#!/usr/bin/env python3
"""Ejecuta una sola prueba Vibe autorizada, tras reserva durable; no reintenta."""
import argparse
import json
import os
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / 'automation/claude_review'))
import pilot
from vibe_connection import check

TASK = 'vibe-auth-001'


class Receipt(pilot.Ledger):
    def __init__(self, http, sha):
        super().__init__(http, sha)
        self.base = f'/repos/{pilot.REPO}/contents/automation/coordination/reviews/{TASK}'

    def prior(self):
        try:
            return self.http.call('github', 'GET', self.base + '/reservation.json?ref=' + pilot.LEDGER_BRANCH)
        except pilot.PilotError as err:
            if str(err) == 'GITHUB_HTTP_404':
                return None
            raise


def run(receipt, output, checker=check):
    output = Path(output); output.mkdir(parents=True, exist_ok=True)
    if receipt.prior() is not None:
        r = {'task_id': TASK, 'state': 'YA_RESERVADO_SIN_NUEVA_INVOCACION', 'invocations_started': 0}
        (output / 'report.json').write_bytes(pilot.canonical(r))
        return r
    if not os.getenv('MISTRAL_VIBE_CLI_KEY'):
        return checker(output / 'report.json', execute=False)
    reservation = {'task_id': TASK, 'code_sha': receipt.code_sha,
                   'state': 'RESERVADO_NO_REINTENTAR', 'max_cli_invocations': 1,
                   'scope': 'Una linea sin herramientas; no tareas del producto',
                   'limits': '1 turno, 512 salida, 90 segundos; presupuestos CLI acumulados no son techo previo de gasto'}
    receipt.reserve(reservation)
    r = checker(output / 'report.json', execute=True)
    r.update(task_id=TASK, code_sha=receipt.code_sha)
    (output / 'report.json').write_bytes(pilot.canonical(r))
    md = '# Prueba de conexión Vibe CLI\n\n' + json.dumps(r, ensure_ascii=False, indent=2) + '\n'
    (output / 'report.md').write_text(md)
    receipt.put('report.json', pilot.canonical(r))
    receipt.put('report.md', md.encode())
    receipt.put('reservation.json', pilot.canonical({**reservation, 'state': r['state']}))
    return r


if __name__ == '__main__':
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--code-sha', required=True)
    p.add_argument('--output', type=Path, required=True)
    a = p.parse_args()
    try:
        h = pilot.HTTP(github_token=os.getenv('GH_TOKEN', ''))
        if not h.github_token:
            raise pilot.PilotError('FALTA_CREDENCIAL_GITHUB')
        r = run(Receipt(h, a.code_sha), a.output)
        print(json.dumps(r, ensure_ascii=False))
        sys.exit(0 if r['state'] in ('CONEXION_COMPROBADA', 'YA_RESERVADO_SIN_NUEVA_INVOCACION') else 1)
    except pilot.PilotError as err:
        print(str(err), file=sys.stderr)
        sys.exit(2)
