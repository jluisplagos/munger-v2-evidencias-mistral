#!/usr/bin/env python3
"""(revisor, ronda 2) Cómo presenta la hoja v2 los estados que no existen en expedientes reales: conclusión favorable (concluido · Sí ·
comprar), pendiente_de_investigacion y pendiente_de_datos con zona favorable. Empresa sintética del paquete, cerrada con el pipeline real y
los agentes simulados (como en la ronda 1). Los textos sintéticos son «…»: la hoja se compone con la regla de contenido mínimo desactivada.
EJECUTAR BAJO flock DEL CERROJO COMÚN."""
import contextlib, io, json, os, shutil, sys
R = '/tmp/claude-0/revision_hoja_r2'; RAIZ = R + '/limpia/munger_v2_r1'; PV = RAIZ + '/personaje_v2'
sys.path.insert(0, PV + '/pruebas'); sys.path.insert(0, PV + '/scripts'); sys.dont_write_bytecode = True
import test_pipeline_sintetico as TS
import hoja_resumen as H
dest = R + '/sint'; shutil.rmtree(dest, ignore_errors=True); os.makedirs(dest); TS.BASE = dest
casos = (('EmpresaX_sobrevive', dict(precio=8), None), ('EmpresaX_favorable', dict(precio=16), None), ('EmpresaX_sin_C34', dict(quitar_fase1=('C34',), quitar_etapa1=('C34',), precio=16), 'datos_ausentes'))
for nombre, kw, variante in casos:
    c = TS.preparar(nombre, **kw); rc, out = TS.correr(c, TS.reaccion_normal(variante))
    st = TS.estado(c); f = json.load(open(c + '/ficha.json', encoding='utf-8'))
    print('=' * 110); print(f"{nombre}: pipeline {rc} · estado {st.get('estado_analisis')} · cubo {f.get('cubo')} · decisión {json.dumps(f.get('decision'), ensure_ascii=False)[:140]} · cierre {f.get('cierre')}")
    print('   causa:', json.dumps(f.get('causa_si_no_concluido'), ensure_ascii=False)[:200])
    b = io.StringIO()
    with contextlib.redirect_stdout(b):
        rc0 = H.generar(c, c, R + '/tmp', H.LOCK_DEFECTO, [0.07, 0.08, 0.09, 0.10, 0.11], cerrojo_ya_tomado=True)
    print(f'   hoja_resumen.py tal cual: código {rc0} · {b.getvalue().strip().splitlines()[0][:200]}')
    cm0 = H.contenido_minimo; H.contenido_minimo = lambda *a: []
    b = io.StringIO()
    try:
        with contextlib.redirect_stdout(b):
            rc1 = H.generar(c, c, R + '/tmp', H.LOCK_DEFECTO, [0.07, 0.08, 0.09, 0.10, 0.11], cerrojo_ya_tomado=True)
    finally:
        H.contenido_minimo = cm0
    print(f'   con el contenido mínimo desactivado (solo para leer la página): código {rc1} · {b.getvalue().strip().splitlines()[-1][:200]}')
    if rc1 == 0:
        md = open(c + '/hoja_resumen.md', encoding='utf-8').read()
        print(md[md.index('## Qué concluye el análisis'):md.index('## Por qué')].rstrip())
        print(md[md.index('| Si se le pide'):md.index('## Predicciones')].rstrip())
        shutil.copy(c + '/hoja_resumen.md', f'{R}/evid/hoja_{nombre}.md')
