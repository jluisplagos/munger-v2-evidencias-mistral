#!/usr/bin/env python3
"""(revisor, ronda 2) Comprobaciones en proceso, sin LibreOffice: veredicto y aptitud con fichas de varios estados, códigos 4/5/6 sin hoja,
recálculo no forzado, entradas mal formadas."""
import sys, os, json, copy, shutil, io, contextlib
SC = '/tmp/claude-0/revision_hoja_r2/limpia/munger_v2_r1/personaje_v2/scripts'
sys.path.insert(0, SC); sys.dont_write_bytecode = True
import hoja_resumen as H
R = '/tmp/claude-0/revision_hoja_r2'
def cap(fn, *a, **k):
    b = io.StringIO()
    with contextlib.redirect_stdout(b):
        try: rc = fn(*a, **k)
        except Exception as e: rc = f'EXCEPCIÓN {type(e).__name__}: {e}'
    return rc, b.getvalue().strip()
print('### T3 · veredicto() con fichas de otros estados (ficha real de Vidrala 4.14 como base; solo cambian los campos indicados)')
ficha = json.load(open(f'{R}/exp/Vidrala_414/Vidrala/ficha.json', encoding='utf-8')); precio = json.load(open(f'{R}/exp/Vidrala_414/Vidrala/precio.json', encoding='utf-8'))
def caso(rot, cambios, pr=None, f1=None):
    f = copy.deepcopy(ficha)
    for k, v in cambios.items():
        if v is None: f.pop(k, None)
        else: f[k] = v
    v = H.veredicto(f, pr or precio, f1 or {})
    print(f'   {rot}:\n      Qué concluye: {v["conclusion"]}\n      A qué precio compraría: {v["linea_precio"]}')
caso('concluido · Sí · comprar · precio_objetivo nulo · sin bloque objetivo (como el sintético «sobrevive») · precio por debajo del precio de Sí',
     {'cubo': 'Sí', 'decision': {'accion': 'comprar', 'precio_objetivo': None, 'condicion': None}, 'objetivo': None}, dict(precio, precio=40.0, zona='bajo_malo'))
caso('concluido · Sí · comprar · precio_objetivo 56,00', {'cubo': 'Sí', 'decision': {'accion': 'comprar', 'precio_objetivo': 56.0, 'condicion': None}, 'objetivo': None}, dict(precio, precio=40.0, zona='bajo_malo'))
caso('concluido · No · descartar', {'cubo': 'No', 'decision': {'accion': 'descartar', 'precio_objetivo': None, 'condicion': None}, 'objetivo': None}, dict(precio, precio=40.0, zona='cumple_regla_k'))
caso('concluido · Demasiado difícil', {'cubo': 'Demasiado difícil', 'decision': {'accion': 'demasiado_dificil', 'precio_objetivo': None, 'condicion': None}, 'objetivo': None})
caso('pendiente_de_investigacion', {'estado_analisis': 'pendiente_de_investigacion', 'decision': {'accion': None, 'precio_objetivo': None}, 'objetivo': None, 'causa_si_no_concluido': {'tipo': 'incertidumbre_no_acotada', 'detalle': 'crecimiento_1_5·MALO'}}, dict(precio, precio=50.0, zona='cumple_regla_k'))
caso('concluido con ficha.motor_a_f1.utilizable_para_conclusion = false', {'motor_a_f1': {'utilizable_para_conclusion': False, 'rotulo': 'DIAGNÓSTICO F1 · …: F1-LIBRO', 'bloquean': [{'id': 'F1-LIBRO'}]}})
caso('concluido · acción desconocida', {'decision': {'accion': 'mantener', 'precio_objetivo': 56.0}, 'objetivo': None})
print()
print('### T2 · aptitud()')
for rot, f in (('V6.3/V6.3.1 de la 4.15: verificacion_entradas no apto + motor_a_f1 bloqueado', {'verificacion_entradas': {'apto_por_entradas': False, 'apto_para_dinero_real': False, 'resumen': {'universo': 288, 'comprobadas_universo': 0, 'motivo': 'no hay verificacion_entradas.json: ninguna entrada financiera está verificada'}}, 'motor_a_f1': {'utilizable_para_conclusion': False, 'rotulo': None, 'bloquean': [{'id': 'F1-LIBRO'}]}}),
               ('marcas apto_para_dinero_real = true en los tres bloques (A3)', {'aptitud_de_uso': {'caracter': 'validado', 'version': '9.9', 'apto_para_dinero_real': True}, 'verificacion_entradas': {'apto_por_entradas': True, 'apto_para_dinero_real': True, 'resumen': {}}, 'motor_a_f1': {'utilizable_para_conclusion': True, 'apto_para_dinero_real': True}}),
               ('V6.4 4.14 real (Vidrala): aptitud_de_uso con verificacion_entradas apto', {k: ficha[k] for k in ('aptitud_de_uso',)}),
               ('sin bloques', {})):
    L, d = H.aptitud(f, {})
    print(f'   {rot}:'); [print('      ' + l[:330]) for l in L]
print('   nota de la ficha real de Vidrala 4.14 que la hoja no copia:', ficha['aptitud_de_uso']['verificacion_entradas'].get('nota'))
print()
print('### T1 · H4: con un fallo no queda hoja y la anterior se aparta (copia de Vidrala 4.14 con su hoja vigente)')
def copia(n):
    d = f'{R}/rep/{n}'; shutil.rmtree(d, ignore_errors=True); os.makedirs(d); shutil.copytree(f'{R}/exp/Vidrala_414/Vidrala', d + '/Vidrala'); return d + '/Vidrala'
def estado(e): return sorted(x for x in os.listdir(e) if x.startswith('hoja_resumen'))
t0 = json.load(open(f'{R}/exp/Vidrala_414/Vidrala/hoja_resumen.json', encoding='utf-8')); filas0 = t0['sensibilidad']['filas']
real_sens = H.sensibilidad
# código 5: la fila de la tasa del análisis no reproduce precio.json
e = copia('T1_cod5')
H.sensibilidad = lambda *a, **k: [dict(f, precio_si=f['precio_si'] + (0.01 if abs(f['r'] - 0.09) < 1e-9 else 0)) for f in copy.deepcopy(filas0)]
rc, out = cap(H.generar, e, e, R + '/tmp', H.LOCK_DEFECTO, [0.07, 0.08, 0.09, 0.10, 0.11])
print(f'   código 5 (no reproduce): devuelve {rc} · {out.splitlines()[0][:120]} · archivos: {estado(e)} · --comprobar → {cap(H.comprobar, e, e)[0]}')
# código 6: recálculo que no recalcula (todas las filas iguales a la del 9 %)
e = copia('T1_cod6'); f9 = [f for f in filas0 if abs(f['r'] - 0.09) < 1e-9][0]
H.sensibilidad = lambda *a, **k: [dict(copy.deepcopy(f9), r=f['r'], C56_leida=f['r']) for f in filas0]
rc, out = cap(H.generar, e, e, R + '/tmp', H.LOCK_DEFECTO, [0.07, 0.08, 0.09, 0.10, 0.11])
print(f'   código 6 (recálculo que no recalcula): devuelve {rc} · {out.splitlines()[0][:170]} · archivos: {estado(e)}')
# código 4: contenido mínimo (a_no vacío) — hay que saltarse la puerta oficial porque tocar fase_c.json ya la cierra: se cambia en memoria
e = copia('T1_cod4'); H.sensibilidad = lambda *a, **k: copy.deepcopy(filas0)
real_leer = H.leer_expediente
def leer_mod(exp, antecedente=False):
    d, libro, h = real_leer(exp, antecedente); d['fase_c.json']['cambiaria_de_cubo']['a_no'] = '…'; return d, libro, h
H.leer_expediente = leer_mod
rc, out = cap(H.generar, e, e, R + '/tmp', H.LOCK_DEFECTO, [0.07, 0.08, 0.09, 0.10, 0.11])
print(f'   código 4 (contenido mínimo: «a No» = «…»): devuelve {rc} · {out.splitlines()[0][:170]} · archivos: {estado(e)}')
H.leer_expediente = real_leer
# control: con la sensibilidad buena se escribe
e = copia('T1_ok'); os.remove(e + '/hoja_resumen.md'); os.remove(e + '/hoja_resumen.json')
rc, out = cap(H.generar, e, e, R + '/tmp', H.LOCK_DEFECTO, [0.07, 0.08, 0.09, 0.10, 0.11])
print(f'   control (filas correctas): devuelve {rc} · archivos: {estado(e)} · --comprobar → {cap(H.comprobar, e, e)[0]}')
H.sensibilidad = real_sens
print()
print('### T6 · H13: entradas mal formadas (copia de Vidrala 4.14)')
for rot, fn in (('ficha.json truncada', lambda e: open(e + '/ficha.json', 'w').write(open(f'{R}/exp/Vidrala_414/Vidrala/ficha.json').read()[:500])),
                ('ficha.json es una lista', lambda e: open(e + '/ficha.json', 'w').write('[]')),
                ('estado_pipeline.json truncado', lambda e: open(e + '/estado_pipeline.json', 'w').write('{')),
                ('precio.json es una lista', lambda e: open(e + '/precio.json', 'w').write('[]')),
                ('fase1_metadatos.json roto', lambda e: open(e + '/fase1_metadatos.json', 'w').write('{')),
                ('fase_c.json = {}', lambda e: open(e + '/fase_c.json', 'w').write('{}')),
                ('cierre_vigente.json es un texto', lambda e: open(e + '/cierre_vigente.json', 'w').write('"x"')),
                ('ficha.provisional es un texto', lambda e: json.dump(dict(json.load(open(e + '/ficha.json')), provisional='si'), open(e + '/ficha.json', 'w')))):
    e = copia('T6'); os.remove(e + '/hoja_resumen.md'); os.remove(e + '/hoja_resumen.json'); fn(e)
    rc, out = cap(H.generar, e, e, R + '/tmp', H.LOCK_DEFECTO, [0.09])
    print(f'   {rot}: devuelve {rc} · {out.splitlines()[0][:150] if out else ""} · hoja: {estado(e)}')
print()
print('### T4/T5 · rótulos y recálculo')
print('   tasa_txt:', {r: H.tasa_txt(r) for r in (0.09, 0.085, 0.095, 0.075, 0.1, 0.12)})
print('   comprobar_recalculo con cinco filas idénticas →', H.comprobar_recalculo([dict(copy.deepcopy(f9), r=r) for r in (0.07, 0.08, 0.09, 0.10, 0.11)]))
print('   comprobar_recalculo con las filas reales →', H.comprobar_recalculo(filas0))
