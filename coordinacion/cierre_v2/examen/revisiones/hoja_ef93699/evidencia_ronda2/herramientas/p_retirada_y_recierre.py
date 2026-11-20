#!/usr/bin/env python3
"""(revisor, ronda 2) Vía oficial con una hoja resumen dentro del expediente: RETIRADA por la llamada normal del pipeline (sin opciones)
cuando el material auditado cambió, con la hoja archivada junto al antecedente (decisión del coordinador: cierre_v2.archivar_salidas), y
CIERRE NUEVO después en el mismo expediente. Se compara con un control idéntico sin hoja. Empresa sintética del paquete («EmpresaX», V6.3,
cerrada concluido · esperar con el pipeline real y los agentes simulados). EJECUTAR BAJO flock DEL CERROJO COMÚN (el pipeline llama a
LibreOffice sin flock; la hoja se genera en este proceso con cerrojo_ya_tomado=True). Los textos sintéticos son «…»: la hoja se escribe con
la regla de contenido mínimo desactivada (solo para tener una hoja que archivar)."""
import contextlib, io, json, os, shutil, subprocess, sys
R = '/tmp/claude-0/revision_hoja_r2'; RAIZ = R + '/limpia/munger_v2_r1'; PV = RAIZ + '/personaje_v2'; SC = PV + '/scripts'
sys.path.insert(0, RAIZ + '/v6/v631_f1/scripts'); sys.path.insert(0, SC); sys.dont_write_bytecode = True
import prueba_pipeline_v631 as PP
import hoja_resumen as H, cierre_v2 as CIE, pipeline as PIPE
TS = PP.TS
dest = R + '/relanz_C'; shutil.rmtree(dest, ignore_errors=True); os.makedirs(dest)


def hoja(c):
    cm0 = H.contenido_minimo; H.contenido_minimo = lambda *a: []
    b = io.StringIO()
    try:
        with contextlib.redirect_stdout(b):
            rc = H.generar(c, c, R + '/tmp', H.LOCK_DEFECTO, [0.09], cerrojo_ya_tomado=True)
    finally:
        H.contenido_minimo = cm0
    return rc, b.getvalue().strip().splitlines()[-1][:170] if b.getvalue().strip() else ''


def comprobar(c):
    b = io.StringIO()
    with contextlib.redirect_stdout(b):
        rc = H.comprobar(c, c)
    return f'{rc} ({b.getvalue().strip()[:150]})'


N_AUD = [0]


def reaccion_nueva():
    base = TS.reaccion_normal()

    def r(c, nombre):
        base(c, nombre)
        if nombre == 'verificacion':
            N_AUD[0] += 1
            pa = c + '/auditoria.md'; txt = open(pa, encoding='utf-8').read()
            open(pa, 'w', encoding='utf-8').write(txt.replace('(sintético)', f'(sintético; auditoría hecha de nuevo, pasada {N_AUD[0]}: revisado otra vez el punto)'))
    return r


def pipe(c, *args, seguir=True):
    r = subprocess.run([TS.PY, TS.PIPE, c, *args], capture_output=True, text=True)
    rc = r.returncode
    if rc == 10 and seguir:
        rc, _ = TS.correr(c, reaccion_nueva())
    return r.returncode, rc, (r.stdout + r.stderr).strip()


def foto(c):
    st = TS.estado(c) if os.path.isfile(c + '/estado_pipeline.json') else {}
    f = json.load(open(c + '/ficha.json', encoding='utf-8')) if os.path.isfile(c + '/ficha.json') else {}
    hh = sorted(os.listdir(c + '/historial_hojas_resumen')) if os.path.isdir(c + '/historial_hojas_resumen') else []
    hc = sorted(os.listdir(c + '/historial_cierres')) if os.path.isdir(c + '/historial_cierres') else []
    ret = json.load(open(c + '/aprobaciones_retiradas.json', encoding='utf-8')) if os.path.isfile(c + '/aprobaciones_retiradas.json') else None
    n_ret = (len(ret.get('retiradas') or ret) if isinstance(ret, dict) else len(ret)) if ret is not None else 0
    return (f"estado {st.get('estado_analisis')} · paso {st.get('paso')} · fin {st.get('fin')} · fin_anterior {st.get('fin_anterior')} · auditoría {st.get('auditoria')} · "
            f"ficha {f.get('estado_analisis')}/{(f.get('decision') or {}).get('accion') if isinstance(f.get('decision'), dict) else None}/cierre {bool(f.get('cierre'))} · cierre_vigente {os.path.isfile(c + '/cierre_vigente.json')} · "
            f"hoja en el expediente {sorted(x for x in os.listdir(c) if x.startswith('hoja_resumen'))} · historial_hojas_resumen {hh} · historial_cierres {hc} · retiradas anotadas {n_ret} · "
            f"vigencia oficial: {CIE.motivo_vigencia(c, PIPE.Pipeline.veredicto_auditoria, os.path.basename(c)) or 'sin objeción'}")


def alterar(c):
    """Cambia el material auditado sin cambiar su contenido: un salto de línea al final de fase_c.json (la huella cambia)."""
    p = c + '/fase_c.json'
    with open(p, 'a', encoding='utf-8') as f:
        f.write('\n')


def archivo_retirada(c):
    base = c + '/historial_cierres'
    if not os.path.isdir(base):
        return 'sin historial_cierres'
    out = []
    for n in sorted(os.listdir(base)):
        d = os.path.join(base, n)
        ret = json.load(open(d + '/RETIRADA.json', encoding='utf-8')) if os.path.isfile(d + '/RETIRADA.json') else {}
        out.append(f"{n}: {sorted(os.listdir(d))} · RETIRADA.json → hoja_resumen_no_vigente = {ret.get('hoja_resumen_no_vigente')}")
        if os.path.isfile(d + '/HOJA_RESUMEN_NO_VIGENTE.json'):
            out.append('      HOJA_RESUMEN_NO_VIGENTE.json: ' + json.dumps(json.load(open(d + '/HOJA_RESUMEN_NO_VIGENTE.json', encoding='utf-8')), ensure_ascii=False)[:330])
    return '\n      '.join(out)


def n_auditorias(c):
    try:
        a = CIE.auditorias_del_expediente(c, PIPE.Pipeline.veredicto_auditoria)
        return len(a) if hasattr(a, '__len__') else a
    except Exception as e:  # noqa: BLE001
        return f'(no se pudo: {type(e).__name__}: {str(e)[:80]})'


print('######## C · retirada oficial por la llamada normal del pipeline (sin opciones) con la hoja dentro, y cierre nuevo después')
TS.BASE = dest + '/C'; os.makedirs(TS.BASE)
c = TS.preparar('EmpresaX'); rc, out = TS.correr(c, TS.reaccion_normal())
print('C0 cierre:', rc, '|', foto(c))
ctrl = dest + '/C_control/EmpresaX'; shutil.copytree(c, ctrl)
print('C1 hoja (contenido mínimo desactivado):', hoja(c), '| --comprobar:', comprobar(c))
print('   auditorías que reconoce la vía oficial en el expediente: con hoja', n_auditorias(c), '· control', n_auditorias(ctrl))
for x in (c, ctrl):
    alterar(x)
print('C2 material auditado cambiado (salto de línea al final de fase_c.json) en el expediente y en el control')
print('   con hoja:', foto(c)); print('   --comprobar antes de llamar al pipeline:', comprobar(c))
r = pipe(c, seguir=False)
print('C3 pipeline.py EXP (sin opciones) con la hoja dentro: código', r[0]); print('      ' + '\n      '.join(x[:230] for x in r[2].splitlines()[:6]))
print('   ', foto(c)); print('    archivo de la retirada:\n      ' + archivo_retirada(c))
print('    --comprobar:', comprobar(c))
b = io.StringIO()
with contextlib.redirect_stdout(b):
    rcg = H.generar(c, c, R + '/tmp', H.LOCK_DEFECTO, [0.09], cerrojo_ya_tomado=True)
print(f'    hoja_resumen.py (generar): código {rcg} · {b.getvalue().strip().splitlines()[0][:200]}')
rc_ = pipe(ctrl, seguir=False)
print('C3 control (sin hoja): código', rc_[0]); print('      ' + '\n      '.join(x[:230] for x in rc_[2].splitlines()[:6]))
print('   ', foto(ctrl)); print('    archivo de la retirada:\n      ' + archivo_retirada(ctrl))
print('   misma salida del pipeline salvo nombres de carpeta:', [x for x in r[2].splitlines() if 'HOJA' not in x][:6] == rc_[2].splitlines()[:6] or 'ver arriba')
r = pipe(c, '--desde', '13')
print('C4 «--desde 13» (auditoría nueva del material nuevo y cierre):', r[:2]); print('      ' + '\n      '.join(x[:200] for x in r[2].splitlines()[:4])); print('   ', foto(c))
rc_ = pipe(ctrl, '--desde', '13')
print('C4 control:', rc_[:2]); print('   ', foto(ctrl))
lee = lambda x: json.load(open(x + '/ficha.json', encoding='utf-8')) if os.path.isfile(x + '/ficha.json') else {}
quita = lambda f: {k: v for k, v in f.items() if k not in ('hashes', 'cierre', 'fecha', 'comprobacion_conjunta')}
f_a, f_b = lee(c), lee(ctrl)
print('   ficha con hoja = ficha del control (sin huellas, cierre ni fecha):', quita(f_a) == quita(f_b), '· estados:', f_a.get('estado_analisis'), f_b.get('estado_analisis'))
print('   auditorías que reconoce la vía oficial: con hoja', n_auditorias(c), '· control', n_auditorias(ctrl))
print('C5 hoja nueva tras el cierre nuevo:', hoja(c), '| --comprobar:', comprobar(c))
r = pipe(c, seguir=False); print('C6 pipeline sin opciones con el cierre nuevo y la hoja nueva: código', r[0], '·', (r[2].splitlines() or ['(sin salida)'])[-1][:160]); print('   ', foto(c))
print('    archivo de la retirada (sigue intacto):\n      ' + archivo_retirada(c))
