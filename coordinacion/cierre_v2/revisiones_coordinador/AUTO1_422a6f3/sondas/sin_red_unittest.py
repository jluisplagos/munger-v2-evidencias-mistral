#!/usr/bin/env python3
"""Ejecuta unittest con la red bloqueada en el proceso y registra el resultado por prueba.

Uso: python3 -I sin_red_unittest.py <directorio_de_pruebas> <patron> <salida.jsonl>
Cualquier intento de conexión o resolución DNS lanza un error y queda contado:
así una prueba ejecutada contra código antiguo no puede llamar a ningún proveedor.
"""
import json
import os
import socket
import sys
import unittest

ATTEMPTS = []


def _blocked(*args, **kwargs):
    ATTEMPTS.append(repr(args[:2])[:120])
    raise OSError('RED_BLOQUEADA_EN_LA_REVISION')


socket.socket.connect = _blocked
socket.socket.connect_ex = _blocked
socket.create_connection = _blocked
socket.getaddrinfo = _blocked

test_dir, pattern, out = sys.argv[1], sys.argv[2], sys.argv[3]
os.chdir(test_dir)
sys.path.insert(0, test_dir)


class Collect(unittest.TextTestResult):
    def __init__(self, *a, **k):
        super().__init__(*a, **k)
        self.rows = []

    def _row(self, test, outcome, err=None):
        detail = ''
        if err is not None:
            etype, value, _ = err
            detail = (etype.__name__ + ': ' + str(value)).splitlines()[0][:200]
        self.rows.append({'prueba': test.id(), 'resultado': outcome, 'detalle': detail})

    def addSuccess(self, test):
        super().addSuccess(test); self._row(test, 'OK')

    def addFailure(self, test, err):
        super().addFailure(test, err); self._row(test, 'FAIL', err)

    def addError(self, test, err):
        super().addError(test, err); self._row(test, 'ERROR', err)

    def addSkip(self, test, reason):
        super().addSkip(test, reason); self.rows.append({'prueba': test.id(), 'resultado': 'SKIP', 'detalle': reason})

    def addSubTest(self, test, subtest, err):
        super().addSubTest(test, subtest, err)
        if err is not None:
            self._row(subtest, 'FAIL_SUBTEST' if issubclass(err[0], test.failureException) else 'ERROR_SUBTEST', err)


suite = unittest.defaultTestLoader.discover(test_dir, pattern=pattern, top_level_dir=test_dir)
runner = unittest.TextTestRunner(resultclass=Collect, verbosity=0, stream=open(os.devnull, 'w'))
result = runner.run(suite)
with open(out, 'w') as fh:
    for row in result.rows:
        fh.write(json.dumps(row, ensure_ascii=False) + '\n')
    fh.write(json.dumps({'ejecutadas': result.testsRun, 'fallos': len(result.failures),
                         'errores': len(result.errors), 'omitidas': len(result.skipped),
                         'intentos_de_red': ATTEMPTS}, ensure_ascii=False) + '\n')
print(json.dumps({'ejecutadas': result.testsRun, 'fallos': len(result.failures), 'errores': len(result.errors),
                  'omitidas': len(result.skipped), 'intentos_de_red': len(ATTEMPTS)}))
