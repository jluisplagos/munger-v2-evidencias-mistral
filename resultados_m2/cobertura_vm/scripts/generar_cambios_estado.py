"""Genera la lista de entradas que cambian de estado entre dos commits.

Uso: python3 -B scripts/generar_cambios_estado.py <sha_base> <sha_nuevo|HEAD-trabajo>
Compara resultados/verificacion_contexto.jsonl (nivel fuente) y COBERTURA_677.csv
(nivel fila, propaga estados de derivados) entre el commit base y el arbol de
trabajo actual, y escribe resultados/cambios_estado_<tag>.json con cada entrada
que cambia, su estado anterior y el nuevo, mas el resumen de transiciones.
No sustituye cifras: solo lista cambios de estado.
"""
import csv
import json
import subprocess
import sys
from collections import Counter
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import comun as C

REPO = Path(__file__).resolve().parents[3]
BASE = 'resultados_m2/cobertura_vm/'


def git_show(sha, rel):
    r = subprocess.run(['git', '-C', str(REPO), 'show', f'{sha}:{BASE}{rel}'],
                       capture_output=True, text=True)
    if r.returncode != 0:
        sys.exit(f'no se pudo leer {sha}:{BASE}{rel}: {r.stderr.strip()}')
    return r.stdout


def main():
    if len(sys.argv) < 3:
        sys.exit('uso: generar_cambios_estado.py <sha_base> <tag_salida> [sha_nuevo]')
    sha_base, tag = sys.argv[1], sys.argv[2]
    sha_nuevo = sys.argv[3] if len(sys.argv) > 3 else None

    def estados_ver(sha=None, texto=None):
        out = {}
        if texto is None:
            texto = git_show(sha, 'resultados/verificacion_contexto.jsonl')
        for line in texto.splitlines():
            if not line.strip():
                continue
            d = json.loads(line)
            out[(d['empresa'], d['celda'])] = d['estado_contextual']
        return out

    def estados_csv(sha=None, texto=None):
        if texto is None:
            texto = git_show(sha, 'COBERTURA_677.csv')
        out = {}
        for r in csv.DictReader(texto.splitlines()):
            out[(r['empresa'], r['celda'])] = r['estado_contextual']
        return out

    if sha_nuevo:
        old_ver = estados_ver(sha_base)
        new_ver = estados_ver(sha_nuevo)
        old_csv = estados_csv(sha_base)
        new_csv = estados_csv(sha_nuevo)
    else:
        old_ver = estados_ver(sha_base)
        new_ver = estados_ver(texto=(C.RESULTADOS / 'verificacion_contexto.jsonl').read_text(encoding='utf-8'))
        old_csv = estados_csv(sha_base)
        new_csv = estados_csv(texto=(C.OUT / 'COBERTURA_677.csv').read_text(encoding='utf-8'))

    cambios_ver = []
    for k in sorted(set(old_ver) | set(new_ver)):
        a, b = old_ver.get(k), new_ver.get(k)
        if a != b:
            cambios_ver.append({'empresa': k[0], 'celda': k[1], 'nivel': 'fuente', 'anterior': a, 'nuevo': b})
    cambios_csv = []
    for k in sorted(set(old_csv) | set(new_csv)):
        a, b = old_csv.get(k), new_csv.get(k)
        if a != b:
            cambios_csv.append({'empresa': k[0], 'celda': k[1], 'nivel': 'csv', 'anterior': a, 'nuevo': b})

    trans_ver = Counter((c['anterior'], c['nuevo']) for c in cambios_ver)
    trans_csv = Counter((c['anterior'], c['nuevo']) for c in cambios_csv)
    out = {
        'base': sha_base,
        'nuevo': sha_nuevo or 'arbol de trabajo',
        'n_cambios_fuente': len(cambios_ver),
        'n_cambios_csv': len(cambios_csv),
        'transiciones_fuente': {f'{a} -> {b}': n for (a, b), n in sorted(trans_ver.items(), key=lambda x: str(x[0]))},
        'transiciones_csv': {f'{a} -> {b}': n for (a, b), n in sorted(trans_csv.items(), key=lambda x: str(x[0]))},
        'cambios_fuente': cambios_ver,
        'cambios_csv': cambios_csv,
        'nota': 'Lista generada por diff de estados contextuales; no sustituye cifras ni fuentes. Una entrada que pierde acreditacion queda PENDIENTE (o CONFLICTO si hay contradiccion documentada).',
    }
    dest = C.RESULTADOS / f'cambios_estado_{tag}.json'
    dest.write_text(json.dumps(out, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
    print(json.dumps({k: v for k, v in out.items() if not k.startswith('cambios_')}, ensure_ascii=False, indent=1))
    print(f'escrito {dest}')


if __name__ == '__main__':
    main()
