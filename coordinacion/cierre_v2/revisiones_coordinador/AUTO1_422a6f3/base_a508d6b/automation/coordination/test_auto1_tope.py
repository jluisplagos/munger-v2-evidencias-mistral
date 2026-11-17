"""AUTO1-M5: tope acumulado entre tareas, leído del registro de reservas."""
import base64
from decimal import Decimal
import json
import tempfile
import unittest
from unittest.mock import patch

import critical_review as cr
from test_auto1_transporte import FakeHTTP, GitHubStore, bundle, good_reply, pin_config

# Copia de los registros de reservation.json de la rama de registro, sin las pruebas
# de cero generaciones; los importes coinciden con los publicados.
LEDGER = {
    'automation/claude_review/results/munger-d-relevos-001': {'pilot_id': 'munger-d-relevos-001', 'state': 'RESULTADO_NO_ACEPTADO_NO_REINTENTAR', 'budget': {'reserved_usd': '0.115726'}},
    'automation/claude_review/results/munger-d-relevos-002': {'pilot_id': 'munger-d-relevos-002', 'state': 'RESULTADO_NO_ACEPTADO_NO_REINTENTAR', 'budget': {'reserved_usd': '0.156686', 'previous_estimated_cost_usd': '0.070368'}},
    'automation/coordination/reviews/audit-pilot-code-001': {'task_id': 'audit-pilot-code-001', 'state': 'RESULTADO_NO_ACEPTADO_NO_REINTENTAR', 'budget': {'reserved_usd': '1.912936'}},
    'automation/coordination/reviews/qwen-bank-group-01': {'task_id': 'qwen-bank-group-01', 'state': 'RESULTADO_NO_ACEPTADO_NO_REINTENTAR', 'maximum_generation_invocations': 1},
    'automation/coordination/reviews/qwen-bank-review-001': {'task_id': 'qwen-bank-review-001', 'state': 'RESULTADO_NO_ACEPTADO_NO_REINTENTAR', 'maximum_generation_invocations': 1},
    'automation/coordination/reviews/qwen-peer-group-01': {'task_id': 'qwen-peer-group-01', 'state': 'AUDITORIA_DOCUMENTAL_PENDIENTE_ACEPTACION', 'budget': {'reserved_usd': '0.25281'}},
    'automation/coordination/reviews/vibe-auth-001': {'task_id': 'vibe-auth-001', 'state': 'CONEXION_COMPROBADA', 'max_cli_invocations': 1},
}


def store_with(records):
    store = GitHubStore()
    for path, record in records.items():
        store.files[path + '/reservation.json'] = json.dumps(record).encode()
    return store


class CapTests(unittest.TestCase):
    def setUp(self):
        pin_config(self)
        self.tmp = tempfile.TemporaryDirectory(); self.addCleanup(self.tmp.cleanup)

    def run_task(self, http, task, cap):
        with patch.object(cr, 'TASK', task), patch.dict('os.environ', {cr.CAP_ENV: cap}):
            return cr.run(http, bundle(), self.tmp.name, cr.Receipt(http, 'a' * 40), execute=True)

    def test_m5_current_ledger_exposure_counts_bounds_and_skips_vibe(self):
        total, entries = cr.Register(FakeHTTP(store_with(LEDGER))).committed()
        self.assertEqual(total, Decimal('2.438158'))
        self.assertEqual(len(entries), 4)

    def test_m5_two_tasks_over_cap_second_stops_before_count_and_reserve(self):
        store = GitHubStore()
        first = FakeHTTP(store, reply=good_reply(), count=30000)
        r1 = self.run_task(first, 'tarea-a-001', '3')
        self.assertEqual(r1['state'], 'AUDITORIA_DOCUMENTAL_PENDIENTE_ACEPTACION')
        committed = Decimal(json.loads(store.files['automation/coordination/reviews/tarea-a-001/reservation.json'])['estimated_cost_usd'])
        self.assertGreater(committed, 0)
        # Una segunda tarea con TASK distinto: su reserva máxima no cabe bajo el mismo tope.
        second = FakeHTTP(store, reply=good_reply())
        with self.assertRaisesRegex(cr.pilot.PilotError, 'TOPE_ACUMULADO_SUPERADO'):
            self.run_task(second, 'tarea-b-001', str(committed + Decimal('1.5')))
        self.assertEqual((second.counted(), second.sent()), (0, 0))
        self.assertNotIn('automation/coordination/reviews/tarea-b-001/reservation.json', store.files)

    def test_m5_uncertain_attempt_counts_its_full_reserve(self):
        store = store_with({k: v for k, v in LEDGER.items() if 'audit-pilot' in k})
        h = FakeHTTP(store, reply=good_reply())
        with self.assertRaisesRegex(cr.pilot.PilotError, 'TOPE_ACUMULADO_SUPERADO'):
            self.run_task(h, 'audit-pilot-code-002', '3.9')
        self.assertEqual((h.counted(), h.sent()), (0, 0))

    def test_m5_missing_or_invalid_cap_blocks_before_anthropic(self):
        for cap in ('', 'ilimitado', '-1', '0', '1e3'):
            h = FakeHTTP(GitHubStore(), reply=good_reply())
            with self.subTest(cap=cap), self.assertRaisesRegex(cr.pilot.PilotError, 'TOPE_ACUMULADO_NO_FIJADO'):
                self.run_task(h, 'tarea-c-001', cap)
            self.assertFalse([c for c in h.calls if c[0] == 'anthropic'])

    def test_m5_exact_reserve_rechecked_inside_reserve(self):
        store = GitHubStore()
        h = FakeHTTP(store, reply=good_reply())
        receipt = cr.Receipt(h, 'a' * 40, cap='2.5')
        receipt.admit(Decimal('2'))
        # Otra reserva aparece entre la comprobación previa y el PUT create-only.
        store.files['automation/coordination/reviews/otra/reservation.json'] = json.dumps(
            {'budget': {'reserved_usd': '1'}}).encode()
        with self.assertRaisesRegex(cr.pilot.PilotError, 'TOPE_ACUMULADO_SUPERADO'):
            receipt.reserve({'budget': {'reserved_usd': '1.6'}})
        self.assertNotIn(receipt.base.split('contents/')[1] + '/reservation.json', store.files)

    def test_m5_unbounded_or_unreadable_record_blocks(self):
        for record, code in (({'budget': {'reserved_usd': '1'}, 'cost_status': 'INCIERTO_SIN_COTA'}, 'SIN_COTA_RECONCILIAR'),
                             ({'state': 'x'}, 'NO_VERIFICABLE'), ({'budget': {'reserved_usd': 1}}, 'NO_VERIFICABLE')):
            store = store_with({'automation/coordination/reviews/x': record})
            with self.subTest(code=code), self.assertRaisesRegex(cr.pilot.PilotError, code):
                cr.Register(FakeHTTP(store)).committed()
        store = GitHubStore(); store.files['automation/coordination/reviews/y/reservation.json'] = b'no json'
        with self.assertRaisesRegex(cr.pilot.PilotError, 'NO_VERIFICABLE'):
            cr.Register(FakeHTTP(store)).committed()

    def test_m5_final_reservation_records_cumulative_and_cost(self):
        store = GitHubStore()
        self.run_task(FakeHTTP(store, reply=good_reply()), 'tarea-d-001', '5')
        res = json.loads(store.files['automation/coordination/reviews/tarea-d-001/reservation.json'])
        self.assertEqual(res['cumulative']['cap_usd'], '5')
        self.assertEqual(res['cost_status'], 'CONOCIDO_ESTIMADO')
        self.assertEqual(res['provider'], 'anthropic')

    def test_audit_pilot_code_001_still_blocked_by_its_reservation(self):
        store = store_with(LEDGER)
        h = FakeHTTP(store, reply=good_reply())
        r = self.run_task(h, 'audit-pilot-code-001', '')
        self.assertEqual(r['state'], 'YA_RESERVADO_SIN_NUEVA_LLAMADA')
        self.assertFalse([c for c in h.calls if c[0] == 'anthropic'])
        self.assertFalse(store.puts)


if __name__ == '__main__':
    unittest.main(verbosity=2)
