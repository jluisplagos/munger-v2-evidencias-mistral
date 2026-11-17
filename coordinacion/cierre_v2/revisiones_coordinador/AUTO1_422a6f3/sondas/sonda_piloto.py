#!/usr/bin/env python3
"""pilot.py tras AUTO1: ¿aplica el tope acumulado (M5) y publica todo fallo posterior a la reserva (M1)?

Uso: python3 -I sonda_piloto.py <worktree_422a6f3>
Reutiliza los dobles de test_pilot.py (FakeHTTP, MemoryLedger); red bloqueada.
"""
import json
import os
from pathlib import Path
import socket
import sys
import tempfile
from unittest.mock import patch


def _blocked(*a, **k):
    raise OSError('RED_BLOQUEADA_EN_LA_REVISION')


socket.socket.connect = socket.socket.connect_ex = _blocked
socket.create_connection = socket.getaddrinfo = _blocked

ROOT = Path(sys.argv[1]).resolve()
sys.path.insert(0, str(ROOT / 'automation/claude_review'))
import pilot  # noqa: E402
import test_pilot as tp  # noqa: E402

out = []
# P1: sin MUNGER_TOPE_ACUMULADO_ANTHROPIC_USD, pilot.py reserva y llama igualmente.
env = {k: v for k, v in os.environ.items() if k != 'MUNGER_TOPE_ACUMULADO_ANTHROPIC_USD'}
with tempfile.TemporaryDirectory() as t, patch.dict(os.environ, env, clear=True):
    http, ledger = tp.FakeHTTP(), tp.MemoryLedger()
    r = pilot.run(http, tp.request('api'), t, tp.SHA, ledger)
out.append({'caso': 'P1 pilot.py sin variable de tope acumulado', 'esperado_si_M5_fuera_global': 'bloqueo antes de reservar',
            'observado': {'estado': r['state'], 'reservado': ledger.reserved, 'llamadas_pagadas': http.paid},
            'veredicto': 'HALLAZGO' if http.paid else 'CONFORME',
            'nota': 'pilot.py solo aplica su techo propio de 0,25 USD; sus reservas sí cuentan en el registro de critical_review'})

# P2: respuesta con un bloque de contenido que no es objeto, tras la reserva.
with tempfile.TemporaryDirectory() as t:
    http, ledger = tp.FakeHTTP(), tp.MemoryLedger()
    http.response = dict(tp.good_response(), content=['no-es-objeto'])
    try:
        r = pilot.run(http, tp.request('api'), t, tp.SHA, ledger)
        obs = {'estado': r['state']}
    except Exception as err:  # lo que escapa sin informe
        obs = {'escapa': type(err).__name__}
    obs.update(publicados=sorted(k for k in ledger.files if k != 'reservation.json'),
               reserva_final=ledger.files.get('reservation.json', {}).get('state') if isinstance(ledger.files.get('reservation.json'), dict) else 'actualizada',
               llamadas_pagadas=http.paid, informe_local=(Path(t) / 'report.json').exists())
out.append({'caso': 'P2 pilot.py con content no objeto tras la reserva', 'esperado': 'estado publicado (como M1 en critical_review)',
            'observado': obs, 'veredicto': 'HALLAZGO' if 'escapa' in obs else 'CONFORME',
            'nota': 'pilot.py:379 solo captura PilotError; la reserva queda RESERVADO_NO_REINTENTAR (bloquea, no repite)'})
for row in out:
    print(json.dumps(row, ensure_ascii=False))
