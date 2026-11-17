#!/usr/bin/env python3
"""Pruebas de mutación sobre una copia de 422a6f3: cada mutante reintroduce un defecto
concreto y se comprueba qué pruebas nuevas lo detectan. Sin red (sin_red_unittest.py).

Uso: python3 -I mutantes.py <worktree_422a6f3> <directorio_de_trabajo> <salida.jsonl>
"""
import json
from pathlib import Path
import shutil
import subprocess
import sys

SRC, WORK, OUT = Path(sys.argv[1]), Path(sys.argv[2]), Path(sys.argv[3])
HERE = Path(__file__).resolve().parent
CR = 'automation/coordination/critical_review.py'

MUTANTS = [
    ('M5_admit_sin_comparar', CR,
     "        if committed + Decimal(new_usd) > cap:\n            raise pilot.PilotError('TOPE_ACUMULADO_SUPERADO')\n",
     "        pass\n", 'test_auto1_tope.py'),
    ('M5_sin_comprobacion_previa', CR,
     "    if hasattr(receipt, 'admit'):\n        report['cumulative_precheck'] = receipt.admit(MAX_USD)\n",
     "", 'test_auto1_tope.py'),
    ('M5_tope_por_defecto_sin_variable', CR,
     "    if not isinstance(raw, str) or not re.fullmatch(r'[0-9]{1,6}(\\.[0-9]{1,6})?', raw.strip()):\n        raise pilot.PilotError('TOPE_ACUMULADO_NO_FIJADO_POR_RESPONSABLE')\n",
     "    if not raw:\n        raw = '1000'\n", 'test_auto1_tope.py'),
    ('M5_incierto_cuenta_cero', CR,
     "    return _usd(budget.get('reserved_usd'))\n",
     "    return Decimal('0') if record.get('state') == 'RESULTADO_NO_ACEPTADO_NO_REINTENTAR' else _usd(budget.get('reserved_usd'))\n",
     'test_auto1_tope.py'),
    ('M4_estado_unico', CR,
     "        report['state'] = REJECTED if report['cost_status'] == 'CONOCIDO_ESTIMADO' else UNCERTAIN\n",
     "        report['state'] = REJECTED\n", 'test_auto1_transporte.py'),
    ('M4_sin_uso_parcial', CR,
     "        raise TransportError(code, partial)\n",
     "        raise TransportError(code, {})\n", 'test_auto1_transporte.py'),
    ('m2_lectura_sin_cota_por_linea', CR,
     "    for raw in _lines(response, deadline, clock):\n",
     "    for raw in _iter_unbounded(response):\n", 'test_auto1_transporte.py'),
    ('m5_sin_plazo_total', CR,
     "        if deadline is not None and clock() > deadline:\n",
     "        if False:\n", 'test_auto1_transporte.py'),
    ('M3_sin_exigir_uso_final', CR,
     "            if not final_usage or type(message['usage'].get('input_tokens')) is not int:\n",
     "            if False:\n", 'test_auto1_transporte.py'),
    ('M1_sin_capturar_HTTPException', CR,
     "        except http.client.HTTPException:\n",
     "        except ZeroDivisionError:\n", 'test_auto1_transporte.py'),
]

# Para m2: lector antiguo (iteración por líneas, sin cota durante la lectura), con la
# misma comprobación de tamaño a posteriori que tenía a508d6b.
UNBOUNDED = '''
def _iter_unbounded(response):
    used = 0
    for raw in response:
        used += len(raw)
        if used > STREAM_LIMIT_BYTES:
            raise pilot.PilotError('STREAM_DEMASIADO_GRANDE')
        yield raw

'''

rows = []
for name, rel, old, new, pattern in MUTANTS:
    dest = WORK / name
    if dest.exists():
        shutil.rmtree(dest)
    shutil.copytree(SRC / 'automation', dest / 'automation')
    shutil.copytree(SRC / '.github', dest / '.github')
    path = dest / rel
    text = path.read_text()
    assert text.count(old) == 1, (name, text.count(old))
    text = text.replace(old, new)
    if name.startswith('m2_'):
        text = text.replace('\ndef read_stream(', UNBOUNDED + '\ndef read_stream(', 1)
    path.write_text(text)
    out = WORK / (name + '.jsonl')
    subprocess.run([sys.executable, '-I', str(HERE / 'sin_red_unittest.py'),
                    str(dest / 'automation/coordination'), pattern, str(out)], check=True,
                   capture_output=True, text=True)
    lines = [json.loads(x) for x in out.read_text().splitlines()]
    summary, tests = lines[-1], lines[:-1]
    failing = sorted({t['prueba'].split(' ')[0].rsplit('.', 1)[-1] for t in tests if t['resultado'] != 'OK'})
    rows.append({'mutante': name, 'archivo_pruebas': pattern, 'ejecutadas': summary['ejecutadas'],
                 'fallos': summary['fallos'], 'errores': summary['errores'],
                 'intentos_de_red': len(summary['intentos_de_red']),
                 'detectado': bool(failing), 'pruebas_que_lo_detectan': failing})

with OUT.open('w') as fh:
    for r in rows:
        fh.write(json.dumps(r, ensure_ascii=False) + '\n')
for r in rows:
    print(('DETECTADO ' if r['detectado'] else 'SOBREVIVE ') + r['mutante'], r['pruebas_que_lo_detectan'][:6],
          'red=%d' % r['intentos_de_red'])
