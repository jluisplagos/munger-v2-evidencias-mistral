"""AUTO1-M6, M7 y m9: inventario por job de disparadores, secretos, puertas e instalaciones."""
from pathlib import Path
import re
import unittest

try:
    import yaml
except ImportError:  # pragma: no cover - el runner de GitHub puede no tenerlo
    yaml = None

WORKFLOWS = Path(__file__).resolve().parents[2] / '.github/workflows'
INFERENCE_SECRETS = ('ANTHROPIC_API_KEY', 'MISTRAL_VIBE_CLI_KEY')
GATE = 'inferencia-aprobada'


def load():
    out = {}
    for path in sorted(WORKFLOWS.glob('*.yml')):
        doc = yaml.safe_load(path.read_text())
        triggers = doc.get('on', doc.get(True))
        triggers = [triggers] if isinstance(triggers, str) else list(triggers or [])
        out[path.name] = (doc, triggers)
    return out


def secrets(job):
    return set(re.findall(r'secrets\.([A-Z_]+)', yaml.safe_dump(job)))


def runs(job):
    return [s.get('run', '') for s in job.get('steps', [])]


@unittest.skipIf(yaml is None, 'PyYAML no disponible')
class WorkflowTests(unittest.TestCase):
    def setUp(self):
        self.workflows = load()

    def test_m6_inference_jobs_never_on_push_and_always_gated(self):
        gated = set()
        for name, (doc, triggers) in self.workflows.items():
            for job_name, job in doc['jobs'].items():
                if secrets(job) & set(INFERENCE_SECRETS):
                    gated.add((name, job_name))
                    with self.subTest(workflow=name, job=job_name):
                        self.assertEqual(triggers, ['workflow_dispatch'])
                        env = job.get('environment')
                        self.assertEqual(env['name'] if isinstance(env, dict) else env, GATE)
        # Inventario por nombre: cada alta de un job con secretos se revisa.
        self.assertEqual(gated, {
            ('analisis-directo.yml', 'analisis'), ('claude-critical-review.yml', 'review'),
            ('cribado-universo.yml', 'cribado'),
            ('piloto-claude-api.yml', 'pilot'), ('qwen-bank-mistral-groups.yml', 'mistral'),
            ('qwen-bank-mistral-groups.yml', 'claude'), ('qwen-bank-mistral-review.yml', 'review'),
            ('vibe-auth.yml', 'connection')})

    def test_m6_push_only_for_jobs_without_secrets(self):
        for name, (doc, triggers) in self.workflows.items():
            if 'push' in triggers or 'pull_request' in triggers:
                for job_name, job in doc['jobs'].items():
                    with self.subTest(workflow=name, job=job_name):
                        self.assertEqual(secrets(job), set())
            self.assertNotIn('pull_request_target', triggers)
            self.assertNotIn('workflow_run', triggers)
            self.assertNotIn('schedule', triggers)

    def test_m6_actions_pinned_and_credentials_not_persisted(self):
        for name, (doc, _) in self.workflows.items():
            for job in doc['jobs'].values():
                for step in job.get('steps', []):
                    if 'uses' in step:
                        self.assertRegex(step['uses'], r'^[^@]+@[0-9a-f]{40}$', name)
                    if step.get('uses', '').startswith('actions/checkout@'):
                        self.assertIs(step['with']['persist-credentials'], False, name)

    def test_m7_anthropic_jobs_install_nothing_and_never_share_with_mistral(self):
        for name, (doc, _) in self.workflows.items():
            for job_name, job in doc['jobs'].items():
                if 'ANTHROPIC_API_KEY' in secrets(job):
                    with self.subTest(workflow=name, job=job_name):
                        self.assertNotIn('MISTRAL_VIBE_CLI_KEY', secrets(job))
                        self.assertFalse(any('pip' in r or 'venv' in r for r in runs(job)))
                        self.assertFalse(any('setup-python' in s.get('uses', '') for s in job['steps']))

    def test_m7_third_party_install_isolated_wheels_only_without_secrets(self):
        installs = 0
        for name, (doc, _) in self.workflows.items():
            for job in doc['jobs'].values():
                for step in job.get('steps', []):
                    if 'pip install' in step.get('run', ''):
                        installs += 1
                        with self.subTest(workflow=name):
                            self.assertNotIn('env', step)
                            self.assertNotIn('secrets.', yaml.safe_dump(step))
                            self.assertIn('vibe-venv/bin/python" -m pip install', step['run'])
                            self.assertIn('--only-binary=:all:', step['run'])
                    if 'MISTRAL_VIBE_CLI_KEY' in yaml.safe_dump(step) and 'run' in step:
                        # El Python que orquesta (con GH_TOKEN) no es el del entorno virtual.
                        self.assertIn('PY="$(command -v python)"', step['run'], name)
        self.assertEqual(installs, 4)

    def test_m9_readiness_has_no_secret(self):
        doc, triggers = self.workflows['vibe-readiness.yml']
        self.assertEqual(secrets(doc['jobs']['readiness']), set())

    def test_m5_review_job_timeout_leaves_room_for_publication(self):
        for name in ('claude-critical-review.yml', 'qwen-bank-mistral-groups.yml', 'analisis-directo.yml',
                     'cribado-universo.yml'):
            doc, _ = self.workflows[name]
            for job in doc['jobs'].values():
                if 'ANTHROPIC_API_KEY' in secrets(job):
                    self.assertGreaterEqual(job['timeout-minutes'], 20, name)


if __name__ == '__main__':
    unittest.main(verbosity=2)
