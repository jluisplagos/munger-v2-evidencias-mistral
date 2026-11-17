#!/usr/bin/env python3
"""Contraste documental en tandas; un intento por tanda, sin aprobar el producto."""
import argparse
import json
import os
from pathlib import Path
import subprocess
import sys

import qwen_bank_review as q

# Plantillas originales, para derivar la de cada tanda sin depender de llamadas previas.
BASE_SYSTEM, BASE_CONFIG = q.SYSTEM, q.BASE_CONFIG
REPLACEMENTS = (('los 36 casos de Qwen', 'los 6 casos asignados de Qwen'),
                ('cases (36 objetos, uno por Q1-001..036)', 'cases (6 objetos, uno por cada id de scope_ids)'))
CONFIG_REPLACEMENT = ('agent_max_output_tokens = 16384', 'agent_max_output_tokens = 32768')


def _replace_once(text, old, new):
    """AUTO1-m8: una sustitución que no se aplica bloquea antes de reservar."""
    if text.count(old) != 1:
        raise q.pilot.PilotError('PLANTILLA_DE_TANDA_NO_COINCIDE')
    return text.replace(old, new)


def configure(scope_ids, system=None, config=None):
    system = BASE_SYSTEM if system is None else system
    config = BASE_CONFIG if config is None else config
    for old, new in REPLACEMENTS:
        system = _replace_once(system, old, new)
    system += '\nEsta tanda comprende exactamente estos ids: ' + ', '.join(scope_ids) + '. No revises los demás.\n'
    system += 'Cita fragmentos continuos exactos; no unas líneas ni uses elipsis para formar una cita.\n'
    config = _replace_once(config, *CONFIG_REPLACEMENT)
    if 'agent_max_output_tokens = 32768\n' not in config:
        raise q.pilot.PilotError('PLANTILLA_DE_TANDA_NO_COINCIDE')
    return system, config


def project(original, group):
    q.verify(original)
    expected = q.IDS[(group - 1) * 6:group * 6]
    by_path = {s['path']: s for s in original['sources']}
    bank_path = q.PREFIX + 'casos_aceptacion.jsonl'
    lines = [line for line in by_path[bank_path]['text'].splitlines() if json.loads(line)['id'] in expected]
    fixtures = {q.PREFIX + f['ruta'] for line in lines for f in json.loads(line)['archivos_sinteticos']}
    selected = [bank_path, q.PREFIX + 'PLAN_DE_EJECUCION.md', q.PREFIX + 'RESUMEN_PARA_INTEGRADOR.md'] + sorted(fixtures)
    sources = []
    for path in selected:
        s = by_path[path]
        sources.append({'path': path, 'original_git_blob': s['git_blob'],
                        'projection': 'Solo líneas de los 6 casos asignados' if path == bank_path else 'Archivo íntegro',
                        'text': '\n'.join(lines) + '\n' if path == bank_path else s['text']})
    return {'task_id': f'qwen-bank-group-{group:02}', 'bank_sha': q.BANK_SHA,
            'original_bundle_sha256': q.pilot.digest(q.pilot.canonical(original)),
            'scope_ids': expected, 'sources': sources,
            'scope': 'Coherencia interna documental; no ejecución, no aprobación, no revisión ciega'}


class Receipt(q.Receipt):
    def __init__(self, http, sha, task):
        super().__init__(http, sha)
        self.base = f'/repos/{q.pilot.REPO}/contents/automation/coordination/reviews/{task}'


def run(receipt, original, group, output, invoker=q.invoke):
    bundle = project(original, group)
    sources = {s['path']: s['text'] for s in bundle['sources']}
    output = Path(output); output.mkdir(parents=True, exist_ok=True)
    r = {'task_id': bundle['task_id'], 'code_sha': receipt.code_sha, 'bank_sha': q.BANK_SHA,
         'scope_ids': bundle['scope_ids'], 'state': 'PREPARADO', 'accepted': False,
         'integrated': False, 'product_executed': False, 'complete_product_cases': 0,
         'blind_review': False, 'generation_invocations_started': 0,
         'billing_source': 'NO_COMPROBADA_EN_CUENTA_MISTRAL',
         'previous_full_attempt': 'qwen-bank-review-001: length, 16384 salida, sin texto visible; conservado'}
    if receipt.prior() is not None:
        r['state'] = 'YA_RESERVADO_SIN_NUEVA_GENERACION'
    else:
        if not os.getenv('MISTRAL_VIBE_CLI_KEY'):
            raise q.pilot.PilotError('FALTA_CLAVE_VIBE_CLI')
        system, config = configure(bundle['scope_ids'])
        reservation = {'task_id': bundle['task_id'], 'state': 'RESERVADO_NO_REINTENTAR',
                       'code_sha': receipt.code_sha, 'bundle_sha256': q.pilot.digest(q.pilot.canonical(bundle)),
                       'scope_ids': bundle['scope_ids'], 'maximum_generation_invocations': 1,
                       'max_output_tokens': 32768, 'time_limit_seconds': 300,
                       'billing_limit': 'USD 1 acumulado CLI; no es techo previo de factura'}
        receipt.reserve(reservation)
        q.SYSTEM, q.BASE_CONFIG = system, config
        try:
            raw = invoker(bundle, r, output)
            r['citation_layout_adjustments'] = []
            r['review'] = q.validate(raw, sources, expected_ids=bundle['scope_ids'], quote_corrections=r['citation_layout_adjustments'])
            r['state'] = 'REVISION_DOCUMENTAL_PENDIENTE_DE_ACEPTACION'
        except q.pilot.PilotError as err:
            r.update(state='RESULTADO_NO_ACEPTADO_NO_REINTENTAR', error=str(err))
        except (OSError, ValueError, KeyError, TypeError, AttributeError, RuntimeError, subprocess.TimeoutExpired):
            r.update(state='RESULTADO_NO_ACEPTADO_NO_REINTENTAR', error='ERROR_CLI_O_DATOS_NO_REINTENTAR')
        (output / 'report.json').write_bytes(q.pilot.canonical(r))
        md = '# Contraste parcial Mistral del banco Qwen\n\n' + json.dumps(r, ensure_ascii=False, indent=2) + '\n'
        (output / 'report.md').write_text(md)
        receipt.put('sources.json', q.pilot.canonical(bundle))
        receipt.put('report.json', q.pilot.canonical(r))
        receipt.put('report.md', md.encode())
        receipt.put('reservation.json', q.pilot.canonical({**reservation, 'state': r['state']}))
    (output / 'report.json').write_bytes(q.pilot.canonical(r))
    return r


if __name__ == '__main__':
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--code-sha', required=True)
    p.add_argument('--group', type=int, choices=range(1, 7), required=True)
    p.add_argument('--output', type=Path, required=True)
    a = p.parse_args()
    try:
        original = json.loads((Path(__file__).parent / 'requests/qwen-bank-review-001.json').read_text())
        http = q.pilot.HTTP(github_token=os.getenv('GH_TOKEN', ''))
        if not http.github_token:
            raise q.pilot.PilotError('FALTA_CREDENCIAL_GITHUB')
        r = run(Receipt(http, a.code_sha, f'qwen-bank-group-{a.group:02}'), original, a.group, a.output)
        print(json.dumps({k: r.get(k) for k in ('task_id', 'state', 'generation_invocations_started', 'model_configured', 'effort_configured', 'usage', 'error')}))
        sys.exit(0 if r['state'] in ('REVISION_DOCUMENTAL_PENDIENTE_DE_ACEPTACION', 'YA_RESERVADO_SIN_NUEVA_GENERACION') else 1)
    except q.pilot.PilotError as err:
        print(str(err), file=sys.stderr); sys.exit(2)
