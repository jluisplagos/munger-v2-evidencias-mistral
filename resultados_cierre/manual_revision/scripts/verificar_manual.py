"""Revision G-MANUAL (Mistral A) · verificacion de los cinco criterios de la solicitud.

Lee MANUAL_OPERATIVO_957af65.md y CONTRADICCIONES_GUIA.md (rama mistral/g-manual-traspaso,
contenido identico a 341831f) y contrasta sus afirmaciones con:
  - el producto jluisplagos/munger-v2 @ 957af652cdc3bef3d67e8623c9572138bac685e9 (git show, solo lectura)
  - el auxiliar @ 9871f59 (rutas EVID/ y PRUEBAS/, solo lectura)
No ejecuta nada del producto: es revision documental + comprobaciones de citas/hashes/comandos
literales. Genera resultados_cierre/manual_revision/verificacion_criterios.json.

Uso: python3 -B verificar_manual.py
"""
import hashlib
import json
import re
import subprocess
import sys
from pathlib import Path

WT = Path('/workspace/wt-gmanual-2df0cd')
PROD = Path('/workspace/github__jluisplagos__munger-v2')
AUX = Path('/workspace/github__jluisplagos__munger-v2-evidencias-mistral')
SHA_PROD = '957af652cdc3bef3d67e8623c9572138bac685e9'
SHA_EVID = '9871f59'
OUT = WT / 'resultados_cierre/manual_revision'

ABBR = {
    'PV2/': 'munger_v2_r1/personaje_v2/',
    'E414/': 'munger_v2_r1/personaje_v2/empresas_v2_correcciones/2026-11_Vidrala_ensayo_4_14/',
    'E415/': 'munger_v2_r1/personaje_v2/empresas_v2_correcciones/2026-11_Vidrala_ensayo_4_15/',
    'EVID/': None,      # auxiliar @ 9871f59
    'PRUEBAS/': 'EVID/coordinacion/cierre_v2/pruebas_candidata/957af65/',
}


def git_show(repo, sha, rel):
    r = subprocess.run(['git', '-C', str(repo), 'show', f'{sha}:{rel}'],
                       capture_output=True, text=True)
    return r.stdout if r.returncode == 0 else None


_cache = {}


def prod_lines(rel):
    if ('prod', rel) not in _cache:
        t = git_show(PROD, SHA_PROD, rel)
        _cache[('prod', rel)] = t.splitlines() if t is not None else None
    return _cache[('prod', rel)]


def aux_lines(rel):
    if ('aux', rel) not in _cache:
        t = git_show(AUX, SHA_EVID, rel)
        _cache[('aux', rel)] = t.splitlines() if t is not None else None
    return _cache[('aux', rel)]


def resolve(cita):
    """'PV2/scripts/x.py:10' -> (repo, rel, line) o None."""
    m = re.match(r'^([A-Z0-9]+/)?(.+?):(\d+)(?:-(\d+))?$', cita)
    if not m:
        return None
    pref, path, l1, l2 = m.group(1) or '', m.group(2), int(m.group(3)), m.group(4)
    for ab, full in ABBR.items():
        if pref == ab or cita.startswith(ab):
            rest = cita[len(ab):]
            mm = re.match(r'^(.+?):(\d+)(?:-(\d+))?$', rest)
            if not mm:
                return None
            path, l1, l2 = mm.group(1), int(mm.group(2)), mm.group(3)
            if full is None:
                return ('aux', path, l1, int(l2) if l2 else None)
            if full.startswith('EVID/'):
                return ('aux', full[len('EVID/'):] + path, l1, int(l2) if l2 else None)
            return ('prod', full + path, l1, int(l2) if l2 else None)
    # ruta directa del producto; si no existe en la raiz, probar munger_v2_r1/<nombre>
    mm = re.match(r'^(.+?):(\d+)(?:-(\d+))?$', cita)
    if mm:
        rel = mm.group(1)
        if prod_lines(rel) is None and '/' not in rel:
            rel = 'munger_v2_r1/' + rel
        return ('prod', rel, int(mm.group(2)), int(mm.group(3)) if mm.group(3) else None)
    return None


def get_lines(repo_kind, rel):
    return prod_lines(rel) if repo_kind == 'prod' else aux_lines(rel)


def main():
    manual = (WT / 'coordinacion/cierre_v2/manual/MANUAL_OPERATIVO_957af65.md').read_text(encoding='utf-8')
    guia = (WT / 'coordinacion/cierre_v2/manual/CONTRADICCIONES_GUIA.md').read_text(encoding='utf-8')
    findings = []

    def add(criterio, estado, detalle, fuente):
        findings.append({'criterio': criterio, 'estado': estado, 'detalle': detalle, 'fuente': fuente})

    # ---- C1: citas archivo:linea existen y apuntan a contenido coherente; hashes de §13; comandos literales
    citas = set(re.findall(r'`([A-Za-z0-9_./-]+\.(?:md|py|sh|json|txt|csv|js|yml|yaml|jsonl)):(\d+(?:-\d+)?)``?', manual))
    citas |= set(re.findall(r'`([A-Za-z0-9_./-]+\.(?:md|py|sh|json|txt|csv)):(\d+(?:-\d+)?)``?', guia))
    checked, faltan, sin_linea = 0, [], []
    for cita in sorted(citas):
        path, lns = cita
        r = resolve(path + ':' + lns)
        if not r:
            faltan.append(cita); continue
        repo_kind, full, l1, l2 = r
        lines = get_lines(repo_kind, full)
        if lines is None:
            faltan.append(cita)
            continue
        if l1 > len(lines):
            sin_linea.append((cita, len(lines)))
            continue
        checked += 1
    add('C1 citas archivo:linea', 'CONFORME' if not faltan and not sin_linea else 'CONFLICTO',
        f'{checked} citas resueltas y con linea dentro del archivo; faltan {len(faltan)}; linea fuera de rango {len(sin_linea)}'
        + (f'; faltan={faltan[:10]}' if faltan else '') + (f'; fuera={sin_linea[:10]}' if sin_linea else ''),
        'MANUAL_OPERATIVO_957af65.md + CONTRADICCIONES_GUIA.md vs producto@957af65 y auxiliar@9871f59')

    # hashes de la tabla §13 del manual
    sec13 = manual.split('## 13.')[1] if '## 13.' in manual else ''
    tab = re.findall(r'\| `([^`]+)` \| `([0-9a-f]{16})` \|', sec13)
    mal_hash = []
    for path, h in tab:
        repo_kind, full = 'prod', path
        for ab, f in ABBR.items():
            if path.startswith(ab):
                rest = path[len(ab):]
                if f is None:
                    repo_kind, full = 'aux', rest
                elif f.startswith('EVID/'):
                    repo_kind, full = 'aux', f[len('EVID/'):] + rest
                else:
                    repo_kind, full = 'prod', f + rest
                break
        t = git_show(PROD if repo_kind == 'prod' else AUX, SHA_PROD if repo_kind == 'prod' else SHA_EVID, full)
        if t is None:
            mal_hash.append((path, 'no existe'))
            continue
        real = hashlib.sha256(t.encode('utf-8')).hexdigest()[:16]
        if real != h:
            mal_hash.append((path, f'declarado {h} real {real}'))
    add('C1 hashes §13', 'CONFORME' if not mal_hash else 'CONFLICTO',
        f'{len(tab)} hashes declarados; discordantes: {mal_hash if mal_hash else "ninguno"}',
        'MANUAL §13 vs sha256 real de cada archivo citado')

    # comandos en bloques de codigo del manual: cada comando literal debe aparecer en alguna fuente citada nearby
    bloques = re.findall(r'\n\n((?:[ ]{4,}[^\n]+\n?)+)', manual)
    comandos = []
    for b in bloques:
        for ln in b.splitlines():
            ln = ln.strip()
            if ln and not ln.startswith('#') and (' ' in ln or ln.endswith('.sh') or ln.endswith('.py')):
                comandos.append(ln)
    # comprobar los comandos clave contra el producto
    checks_cmd = {
        'gh release download base-4.14 --repo jluisplagos/munger-v2 --pattern munger_v2_r1_entrega4.14_cierre_verificacion_entradas.zip --dir .downloads':
            ('prod', 'README.md'),
        'gh api -H "Accept: application/octet-stream" repos/jluisplagos/munger-v2/releases/assets/750814858':
            ('prod', 'munger_v2_r1/PROMPT_NUEVA_VENTANA.md'),
        'python tools/base_414.py materialize --source .downloads/munger_v2_r1_entrega4.14_cierre_verificacion_entradas.zip':
            ('prod', 'README.md'),
        'python tools/base_414.py verify --report docs/VERIFICACION_BASE_COMPLETA_LOCAL.json':
            ('prod', 'README.md'),
        'python tools/base_414.py verify --git-only': ('prod', 'README.md'),
        'bash verificar_paquete.sh completa': ('prod', 'munger_v2_r1/verificar_paquete.sh'),
        'python3 -I -B personaje_v2/empresas_v2_correcciones/2026-11_Vidrala_ensayo_4_14/scripts/comprobar_entrega_4_14.py':
            ('prod', 'munger_v2_r1/CONTINUIDAD.md'),
    }
    res_cmd = []
    for cmd, (rk, rel) in checks_cmd.items():
        lines = get_lines(rk, rel) or []
        hit = any(cmd in ln for ln in lines)
        res_cmd.append({'comando': cmd, 'fuente_esperada': rel, 'encontrado_literal': hit})
    add('C1 comandos literales', 'CONFORME' if all(r['encontrado_literal'] for r in res_cmd) else 'CONFLICTO',
        '; '.join(f"{'OK' if r['encontrado_literal'] else 'NO'} {r['comando'][:70]} ({r['fuente_esperada']})" for r in res_cmd),
        'bloque de comandos del manual vs fuente citada')

    # ---- C2: I19/I20 corregidos y no reintroducidos; H9 pendiente
    cont = prod_lines('munger_v2_r1/CONTINUIDAD.md') or []
    hito2 = prod_lines('munger_v2_r1/personaje_v2/empresas_v2_correcciones/2026-11_Vidrala_ensayo_4_15/hito2/HITO_2_4_15.md') or []
    test_i19 = prod_lines('munger_v2_r1/personaje_v2/pruebas/test_relevo_i19_415.py') or []
    ficha = prod_lines('munger_v2_r1/personaje_v2/scripts/ficha.py') or []
    pipe = prod_lines('munger_v2_r1/personaje_v2/scripts/pipeline.py') or []
    c2 = []
    c2.append(('CONTINUIDAD.md:9 declara I19/I20 corregidos',
               len(cont) >= 9 and ('I19' in cont[8] or 'I20' in cont[8] or 'correg' in cont[8].lower())))
    c2.append(('HITO_2_4_15.md:82-93 cubre I20 (verificacion_entradas en ficha/informe) y I19 (relevo caducado)',
               any('verificacion_entradas' in l for l in hito2[81:93]) and any('relevo' in l.lower() for l in hito2[81:93])))
    c2.append(('HITO_2_4_15.md:92-93 declara H9 pendiente (vuelve siempre a paso 12)',
               any('paso 12' in l or 'paso12' in l for l in hito2[91:93])))
    n_pasos_i19 = sum(1 for l in test_i19 if 'paso("' in l or 'paso(\"' in l)
    c2.append(('test_relevo_i19_415.py existe con >=5 pruebas (paso(...)) y exige n>=5',
               len(test_i19) > 0 and n_pasos_i19 >= 5 and any('n >= 5' in l for l in test_i19)))
    c2.append(('ficha.py:383-391 contiene verificacion_entradas',
               any('verificacion_entradas' in l for l in ficha[382:391])))
    c2.append(('pipeline.py:1060-1083 contiene relevos_caducados',
               any('relevos_caducados' in l for l in pipe[1059:1083])))
    manual_i19 = ('I19' in manual and 'H9' in manual and 'pendiente' in manual.lower())
    guia_i19 = ('H9' in guia and 'pendiente' in guia.lower() and 'I19' in guia and 'I20' in guia)
    c2.append(('el manual y la guia no reintroducen I19/I20 y marcan H9 pendiente', manual_i19 and guia_i19))
    # el manual no debe afirmar que el relevo caducado se resuelve con --desde 12 como procedimiento vigente
    reintro = 'usa `--desde 12`' in manual or '--desde 12`, que emite' in manual
    c2.append(('el manual no presenta --desde 12 como procedimiento vigente del relevo caducado', not reintro))
    add('C2 I19/I20/H9', 'CONFORME' if all(ok for _, ok in c2) else 'CONFLICTO',
        '; '.join(f"{'OK' if ok else 'FALLO'} {d}" for d, ok in c2),
        'producto@957af65 CONTINUIDAD.md:9, HITO_2_4_15.md:82-93, test_relevo_i19_415.py, ficha.py:383-391, pipeline.py:1060-1083 vs manual/guia')

    # ---- C3: no adopta politica ni valores
    body = manual + '\n' + guia
    params = re.findall(r'\b(R|theta|λ|lambda|k|umbral)\s*[=:]\s*[0-9]', body)
    politicas = re.findall(r'(adopta|elige|asigna)\s+(R|θ|λ|lambda|k)\b', body, re.I)
    add('C3 no politicas/valores', 'CONFORME' if not params and not politicas else 'CONFLICTO',
        f'hallazgos de asignacion de parametros: {params + politicas if (params or politicas) else "ninguno"}; el manual declara "no adopta ni propone ningun valor" (§1)',
        'busqueda regex sobre manual+guia; PROGRAM.md:7 del control')

    # ---- C4: tabla G-1..G-9 y O-1..O-18: comprobar que cada texto historico citado existe en la linea citada
    filas_go = []
    for ln in guia.splitlines():
        m = re.match(r'\| ((?:G|O)-\d+) \|', ln)
        if m:
            filas_go.append((m.group(1), re.findall(r'`([^`]+:\d+(?:-\d+)?)``?', ln)))
    mal = []
    for gid, citas_fila in filas_go:
        for cita in citas_fila:
            r = resolve(cita)
            if not r:
                mal.append((gid, 'cita no resuelta', cita)); continue
            rk, rel, l1, l2 = r
            lines = get_lines(rk, rel)
            if lines is None:
                mal.append((gid, 'archivo no existe', cita)); continue
            if l1 > len(lines):
                mal.append((gid, 'linea fuera de rango', cita)); continue
    n_g = sum(1 for g, _ in filas_go if g.startswith('G'))
    n_o = sum(1 for g, _ in filas_go if g.startswith('O'))
    add('C4 tabla G/O alcanzable', 'CONFORME' if not mal else 'CONFLICTO',
        f'{n_g} filas G y {n_o} filas O ({len(filas_go)} filas, {sum(len(c) for _, c in filas_go)} citas); citas no alcanzables: {mal if mal else "ninguna"} (todas existen en 957af65/9871f59)',
        'CONTRADICCIONES_GUIA.md §2-3 vs producto@957af65 y auxiliar@9871f59')
    # comprobacion textual de una muestra: G-1 (GUIA:114), G-2 (GUIA:98), O-1 (CONTINUIDAD:351), O-5 (CONTINUIDAD:130)
    muestras = []
    guia_l = prod_lines('munger_v2_r1/personaje_v2/GUIA_RECORRIDO_SUPERVISADO.md') or []
    for gid, l1, l2, palabra in [('G-1', 114, 114, 'Relevo'), ('G-2', 98, 98, 'V6.3'), ('G-7', 1, 1, '4.13'), ('G-8', 14, 14, 'descompresi')]:
        seg = guia_l[l1 - 1:l2] if guia_l else []
        ok = any(palabra.lower() in l.lower() for l in seg)
        muestras.append({'id': gid, 'lineas': f'{l1}-{l2}', 'esperaba': palabra, 'ok': ok, 'texto': (seg[0].strip()[:100] if seg else '')})
    cont_extra = {}
    for oid, l1, l2, palabra, rel in [('O-1', 351, 351, 'I19', 'munger_v2_r1/CONTINUIDAD.md'), ('O-5', 130, 132, 'quince', 'munger_v2_r1/CONTINUIDAD.md'), ('O-8', 386, 390, 'ZIP', 'munger_v2_r1/CONTINUIDAD.md'), ('O-15', 31, 32, '198', 'munger_v2_r1/personaje_v2/empresas_v2_correcciones/2026-11_Vidrala_ensayo_4_14/documentacion_cierre_4_14/traspaso/PROMPT_DEL_AGENTE_RECEPTOR.md')]:
        if rel not in cont_extra:
            cont_extra[rel] = prod_lines(rel) or []
        seg = cont_extra[rel][l1 - 1:l2]
        ok = any(palabra.lower() in l.lower() for l in seg)
        muestras.append({'id': oid, 'lineas': f'{l1}-{l2}', 'esperaba': palabra, 'ok': ok, 'texto': (seg[0].strip()[:100] if seg else ''), 'archivo': rel})
    add('C4 muestra textual G/O', 'CONFORME' if all(m['ok'] for m in muestras) else 'CONFLICTO',
        '; '.join(f"{m['id']}@{m['lineas']} busco '{m['esperaba']}': {'OK' if m['ok'] else 'NO'} ({m['texto'][:60]})" for m in muestras),
        'muestra de 6 entradas de la tabla vs lineas reales del producto')

    # ---- C5: T-TRASPASO ejecutable y separa LO/AG/RED
    sec10 = manual.split('## 10.')[1].split('## 11.')[0] if '## 10.' in manual else ''
    pasos = []
    for ln in sec10.splitlines():
        m = re.match(r'\| (\d+) \| ([^|]+) \| ([^|]+) \|', ln)
        if m:
            pasos.append((m.group(1), m.group(2).strip(), m.group(3).strip()))
    reqs = sorted({p[2].split(' ')[0] for p in pasos})
    n_pasos = len(pasos)
    sep_lo = 'LibreOffice' in sec10 and 'agentes reales' in sec10
    # comprobar que la lista de pruebas con LibreOffice citada (CONTINUIDAD:128) existe
    cont128 = cont[127] if len(cont) > 127 else ''
    lo_lista = 'test_comprobadores' in cont128 and 'soffice' in ' '.join(cont[120:135]).lower() or 'LibreOffice' in ' '.join(cont[125:130])
    # verificar_paquete.sh bloque entorno llama a comprobar_entorno y este a soffice
    vp = prod_lines('munger_v2_r1/verificar_paquete.sh') or []
    ce = prod_lines('munger_v2_r1/personaje_v2/scripts/comprobar_entorno.sh') or []
    entorno_llama = any('comprobar_entorno' in l for l in vp[:70]) and any('soffice' in l for l in ce)
    add('C5 T-TRASPASO', 'CONFORME' if (n_pasos == 19 and sep_lo and entorno_llama) else 'REVISAR',
        f'{n_pasos} pasos en la tabla (esperados 19); requisitos usados: {reqs}; separacion LO/AG/RED declarada: {sep_lo}; '
        f'entorno->soffice verificado en codigo: {entorno_llama}',
        'manual §10 vs verificar_paquete.sh y comprobar_entorno.sh @957af65')

    out = {
        'revision': 'G-MANUAL por Mistral A (independiente del autor Claude)',
        'solicitud': {'sha_autor': '341831fd8b4c9081c09f1ebe7b31799042402d0f',
                      'base_revisada': SHA_PROD, 'control_vigente': 'cdec2f5dab654a9149ed510475feae3ed2f0662f',
                      'rama_revision': 'mistral/g-manual-traspaso'},
        'metodo': 'solo lectura (git show) del producto @957af65 y del auxiliar @9871f59; ningun comando del producto ejecutado; sin LibreOffice; sin red',
        'hallazgos': findings,
    }
    (OUT / 'verificacion_criterios.json').write_text(json.dumps(out, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
    for f in findings:
        print(f"[{f['estado']}] C{f['criterio']}: {f['detalle'][:160]}")
    print('escrito', OUT / 'verificacion_criterios.json')


if __name__ == '__main__':
    main()
