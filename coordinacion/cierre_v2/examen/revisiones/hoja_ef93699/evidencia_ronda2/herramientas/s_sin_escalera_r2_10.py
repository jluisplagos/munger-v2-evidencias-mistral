"""(revisor, ronda 2 · R2-10) ¿Qué hace la hoja con un expediente cerrado y vigente SIN escalera de precios (precio.json con «sin_lectura»,
caso que la vía oficial contempla: pipeline.py l.595)? Simulación en la capa de lectura: la puerta real (Vidrala 4.14, copia) y, después,
precio.json sin escalera y ficha sin conclusión. No usa LibreOffice (sin escalera no hay recálculo). La hoja se escribiría fuera del
expediente. Ejecutar desde personaje_v2/scripts de una copia del paquete."""
import sys, os, copy, io, contextlib, shutil
sys.path.insert(0, '.')
import hoja_resumen as H
EXP = sys.argv[1] if len(sys.argv) > 1 else '/tmp/claude-0/revision_hoja_r2/exp/Vidrala_414/Vidrala'
SAL = sys.argv[2] if len(sys.argv) > 2 else '/tmp/claude-0/revision_hoja_r2/tmp/sin_escalera'
shutil.rmtree(SAL, ignore_errors=True); os.makedirs(SAL)
real = H.leer_expediente
def falso(exp, antecedente=False):
    d, libro, huellas = real(exp, antecedente=antecedente)
    d = copy.deepcopy(d)
    d['precio.json'] = {'sin_lectura': 'la hoja bloquea el valor (simulación del revisor)', 'precio': d['precio.json'].get('precio')}
    f = d['ficha.json']
    f['estado_analisis'] = 'modelo_no_aplicable'; f['cubo'] = 'Demasiado difícil'
    f['decision'] = {'accion': None, 'precio_objetivo': None, 'condicion': None}
    f.pop('objetivo', None); f.pop('escalera', None)
    f['causa_si_no_concluido'] = {'tipo': 'modelo_no_aplicable', 'detalle': 'el modelo no sirve para este negocio (simulación del revisor)'}
    return d, libro, huellas
H.leer_expediente = falso
b = io.StringIO()
with contextlib.redirect_stdout(b):
    try:
        rc = H.generar(EXP, SAL, None, H.LOCK_DEFECTO, H.TASAS)
    except Exception as e:
        rc = f'EXCEPCIÓN {type(e).__name__}: {e}'
print('cerrado y vigente, sin escalera de precios, estado modelo_no_aplicable → devuelve', rc)
print('   mensaje:', b.getvalue().strip()[:400])
print('   archivos escritos:', sorted(os.listdir(SAL)))
