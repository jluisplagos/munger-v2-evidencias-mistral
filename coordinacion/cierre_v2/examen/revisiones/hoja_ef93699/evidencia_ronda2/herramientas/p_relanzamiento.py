#!/usr/bin/env python3
"""(revisor, ronda 2) Vía oficial con una hoja resumen dentro del expediente: relanzamientos del pipeline (decisión del coordinador).
Empresa sintética del paquete (V6.3, «EmpresaX», cerrada concluido · esperar con el pipeline real y los agentes simulados) y la V6.3.1 F1
(P6 → P8 «--desde 7» y P10 «--desde 12» con la declaración F1 cambiada). EJECUTAR BAJO flock DEL CERROJO COMÚN (el pipeline llama a
LibreOffice sin flock; la hoja se genera en este proceso con cerrojo_ya_tomado=True). Los textos sintéticos son «…»: la hoja se escribe con
la regla de contenido mínimo desactivada (solo para tener una hoja que archivar)."""
import contextlib, io, json, os, shutil, subprocess, sys
R = '/tmp/claude-0/revision_hoja_r2'; RAIZ = R + '/limpia/munger_v2_r1'; PV = RAIZ + '/personaje_v2'; SC = PV + '/scripts'
sys.path.insert(0, RAIZ + '/v6/v631_f1/scripts'); sys.path.insert(0, SC); sys.dont_write_bytecode = True
import prueba_pipeline_v631 as PP
import hoja_resumen as H, cierre_v2 as CIE, pipeline as PIPE, motor_a_f1 as F1
TS, PF = PP.TS, PP.PF
CFG63, CFG64 = PV + '/config_v2.json', PV + '/config_v2_v64_experimental.json'
dest = R + '/relanz'; shutil.rmtree(dest, ignore_errors=True); os.makedirs(dest)
def hoja(c):
    cm0 = H.contenido_minimo; H.contenido_minimo = lambda *a: []
    b = io.StringIO()
    try:
        with contextlib.redirect_stdout(b):
            rc = H.generar(c, c, R + '/tmp', H.LOCK_DEFECTO, [0.09], cerrojo_ya_tomado=True)
    finally:
        H.contenido_minimo = cm0
    return rc, b.getvalue().strip().splitlines()[-1][:150] if b.getvalue().strip() else ''
def comprobar(c):
    b = io.StringIO()
    with contextlib.redirect_stdout(b):
        rc = H.comprobar(c, c)
    return f'{rc} ({b.getvalue().strip()[:110]})'
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
def pipe(c, *args, cfg=None, seguir=True):
    env = dict(os.environ, MUNGER_CONFIG=cfg) if cfg else dict(os.environ)
    r = subprocess.run([TS.PY, TS.PIPE, c, *args], capture_output=True, text=True, env=env)
    rc = r.returncode
    if rc == 10 and seguir:
        if cfg: os.environ['MUNGER_CONFIG'] = cfg
        try: rc, _ = TS.correr(c, reaccion_nueva())
        finally: os.environ.pop('MUNGER_CONFIG', None)
    return r.returncode, rc, (r.stdout + r.stderr).strip()
def foto(c):
    st = TS.estado(c) if os.path.isfile(c + '/estado_pipeline.json') else {}
    f = json.load(open(c + '/ficha.json', encoding='utf-8')) if os.path.isfile(c + '/ficha.json') else {}
    hh = sorted(os.listdir(c + '/historial_hojas_resumen')) if os.path.isdir(c + '/historial_hojas_resumen') else []
    hc = sorted(os.listdir(c + '/historial_cierres')) if os.path.isdir(c + '/historial_cierres') else []
    return (f"estado {st.get('estado_analisis')} · paso {st.get('paso')} · fin {st.get('fin')} · fin_anterior {st.get('fin_anterior')} · auditoría {st.get('auditoria')} · "
            f"ficha {f.get('estado_analisis')}/{(f.get('decision') or {}).get('accion') if isinstance(f.get('decision'), dict) else None}/cierre {bool(f.get('cierre'))} · cierre_vigente {os.path.isfile(c + '/cierre_vigente.json')} · "
            f"hoja en el expediente {sorted(x for x in os.listdir(c) if x.startswith('hoja_resumen'))} · historial_hojas_resumen {hh} · historial_cierres {hc} · "
            f"vigencia oficial: {CIE.motivo_vigencia(c, PIPE.Pipeline.veredicto_auditoria, os.path.basename(c)) or 'vigente'}")
print('######## A · V6.3 sintética (EmpresaX): cierre concluido con el pipeline real')
TS.BASE = dest + '/A'; os.makedirs(TS.BASE)
c = TS.preparar('EmpresaX'); rc, out = TS.correr(c, TS.reaccion_normal())
print('A0 cierre:', rc, '|', foto(c))
ficha0 = json.load(open(c + '/ficha.json', encoding='utf-8'))
# control sin hoja: copia del expediente cerrado
ctrl = dest + '/A_control/EmpresaX'; shutil.copytree(c, ctrl)
print('A1 hoja (contenido mínimo desactivado):', hoja(c), '| --comprobar:', comprobar(c)); print('   ', foto(c))
print('A2 pipeline sin opciones:', pipe(c)[:2]); print('   ', foto(c))
r = pipe(c, '--reiniciar', '--desde', '13'); print('A3 «--reiniciar --desde 13»:', r[:2], '·', r[2].splitlines()[-1][:120]); print('   ', foto(c))
r = pipe(c, '--desde', '13', '--config', CFG64, seguir=False); print('A4 «--desde 13 --config V6.4» (plantilla equivocada):', r[:2], '·', r[2].splitlines()[-1][:140]); print('   ', foto(c))
fallo = dest + '/A_fallo/EmpresaX'; shutil.copytree(c, fallo); open(fallo + '/historial_hojas_resumen', 'w').write('no es una carpeta')
r = pipe(fallo, '--desde', '13', seguir=False); print('A9 «--desde 13» con un ARCHIVO llamado historial_hojas_resumen (no se puede archivar la hoja):', r[:2], '·', ' / '.join(x[:150] for x in r[2].splitlines()[-2:])); print('   ', foto(fallo))
r = pipe(c, '--desde', '13'); print('A5 «--desde 13»:', r[:2], '·', ' / '.join(x[:110] for x in r[2].splitlines()[:2])); print('   ', foto(c))
rc_ctrl = pipe(ctrl, '--desde', '13'); print('A5 control (mismo relanzamiento sin hoja):', rc_ctrl[:2]); print('   ', foto(ctrl))
lee = lambda x: json.load(open(x + '/ficha.json', encoding='utf-8')) if os.path.isfile(x + '/ficha.json') else {}
f_a, f_b = lee(c), lee(ctrl)
quita = lambda f: {k: v for k, v in f.items() if k not in ('hashes', 'cierre', 'fecha', 'comprobacion_conjunta')}
print('   ficha con hoja = ficha del control (sin huellas, cierre ni fecha):', quita(f_a) == quita(f_b), '· estados:', f_a.get('estado_analisis'), f_b.get('estado_analisis'))
print('A6 hoja nueva tras el cierre nuevo:', hoja(c), '| --comprobar:', comprobar(c))
r = pipe(c, '--reiniciar'); print('A7 «--reiniciar»:', r[:2], '·', r[2].splitlines()[0][:120]); print('   ', foto(c))
print('A8 hoja tras «--reiniciar» y cierre nuevo:', hoja(c), '| --comprobar:', comprobar(c))
print()
print('######## B · V6.3.1 F1 sintética (P6): cierre concluido; después, declaración F1 cambiada y relanzamiento')
TS.BASE = dest + '/P6'; os.makedirs(TS.BASE)
c6 = PF.preparar('EmpresaX_V631', PP.declaracion()); rc, out = PP.correr(c6, PP.CFG631)
print('B0 cierre P6:', rc, '|', foto(c6)); print('   F1:', {k: F1.vigencia(c6).get(k) for k in ('exigido', 'vigente', 'utilizable')})
print('B1 hoja:', hoja(c6), '| --comprobar:', comprobar(c6))
for nombre, desde in (('P8', '7'), ('P10', '12')):
    d_ = dest + f'/{nombre}/EmpresaX_V631'; shutil.copytree(c6, d_)
    decl = PP.declaracion(0.31); PF.escribir_fuente(d_, decl); json.dump(decl, open(d_ + '/motor_a_f1.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    print(f'{nombre} · declaración F1 cambiada; antes de relanzar --comprobar:', comprobar(d_))
    r = pipe(d_, '--desde', desde, cfg=PP.CFG631)
    print(f'{nombre} · «--desde {desde}»:', r[:2], '·', ' / '.join(x[:120] for x in r[2].splitlines()[:3])); print('   ', foto(d_))
    f = json.load(open(d_ + '/ficha.json', encoding='utf-8'))
    print('    ficha: F1 utilizable', (f.get('motor_a_f1') or {}).get('utilizable_para_conclusion'), '· aprobaciones_retiradas.json', os.path.isfile(d_ + '/aprobaciones_retiradas.json'))
    b = io.StringIO()
    with contextlib.redirect_stdout(b):
        rc = H.generar(d_, d_, R + '/tmp', H.LOCK_DEFECTO, [0.09], cerrojo_ya_tomado=True)
    print(f'    hoja_resumen.py (generar): código {rc} · {b.getvalue().strip().splitlines()[0][:170]} · --comprobar: {comprobar(d_)}')
    st_ = TS.estado(d_); st_['fin'] = st_.get('fin_anterior'); json.dump(st_, open(d_ + '/estado_pipeline.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    b = io.StringIO()
    with contextlib.redirect_stdout(b):
        rc = H.generar(d_, d_, R + '/tmp', H.LOCK_DEFECTO, [0.09], cerrojo_ya_tomado=True)
    print(f'    con «fin» antiguo repuesto (como lo dejaba el pipeline anterior): código {rc} · {b.getvalue().strip().splitlines()[0][:200]}')
    arch = d_ + '/historial_hojas_resumen'
    if os.path.isdir(arch):
        a0 = os.path.join(arch, sorted(os.listdir(arch))[0]); print('    archivo de la hoja:', sorted(os.listdir(a0)), '·', json.load(open(a0 + '/HOJA_RESUMEN_NO_VIGENTE.json', encoding='utf-8')).get('motivo'))
