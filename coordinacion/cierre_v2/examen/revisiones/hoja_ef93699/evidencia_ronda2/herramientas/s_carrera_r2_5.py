"""(revisor, ronda 2 · R2-5) ¿Qué pasa si la aprobación se retira MIENTRAS la hoja se está generando (el recálculo tarda minutos)?
Simulación sin LibreOffice sobre una copia de Vidrala 4.14 (vigente, con su hoja): la puerta se pasa de verdad; en el lugar del recálculo
(a) cambia el material auditado y la vía oficial retira la aprobación (cierre_v2.asegurar_vigencia, como haría una llamada al pipeline) y
(b) se devuelven las filas ya calculadas de la hoja anterior. Después, generar() sigue con lo que leyó al principio.
Ejecutar desde personaje_v2/scripts de una copia del paquete; E es una COPIA del expediente (se modifica)."""
import sys, os, json, io, contextlib
sys.path.insert(0, '.'); sys.dont_write_bytecode = True
import hoja_resumen as H, cierre_v2 as CIE, pipeline as PIPE
E = sys.argv[1] if len(sys.argv) > 1 else '/tmp/claude-0/revision_hoja_r2/tmp/carrera/Vidrala'
filas0 = json.load(open(E + '/hoja_resumen.json', encoding='utf-8'))['sensibilidad']['filas']
def vig(): return CIE.motivo_vigencia(E, PIPE.Pipeline.veredicto_auditoria, 'Vidrala') or 'sin objeción'
print('antes: vigencia oficial:', vig(), '· hoja:', sorted(x for x in os.listdir(E) if x.startswith('hoja_resumen')))
def recalculo_simulado(libro, k, tasas, **kw):
    with open(E + '/fase_c.json', 'a', encoding='utf-8') as f: f.write('\n')          # el material auditado cambia
    m, arch = CIE.asegurar_vigencia(E, PIPE.Pipeline.veredicto_auditoria, 'Vidrala', None)  # la vía oficial retira la aprobación
    print('   (durante el recálculo) retirada oficial:', (m or '')[:110], '· archivado en', arch and os.path.relpath(arch, E), '·', sorted(os.listdir(arch)) if arch else None)
    return filas0
H.sensibilidad = recalculo_simulado
b = io.StringIO()
with contextlib.redirect_stdout(b):
    try: rc = H.generar(E, E, None, H.LOCK_DEFECTO, H.TASAS)
    except Exception as e: rc = f'EXCEPCIÓN {type(e).__name__}: {str(e)[:200]}'
print('\n'.join('   ' + x[:260] for x in b.getvalue().strip().splitlines()))
print('generar() devuelve', rc)
print('después: vigencia oficial:', vig())
print('   archivos en el expediente:', sorted(x for x in os.listdir(E) if x.startswith(('hoja_resumen', 'ficha', 'informe', 'cierre_vigente', 'aprobaciones'))))
if os.path.isfile(E + '/hoja_resumen.json'):
    t = json.load(open(E + '/hoja_resumen.json', encoding='utf-8'))
    print('   la hoja recién escrita dice de sí misma: vigencia =', t.get('vigencia'), '· generada', t.get('generada'))
b = io.StringIO()
with contextlib.redirect_stdout(b):
    rc = H.comprobar(E, E)
print('   --comprobar →', rc, '·', b.getvalue().strip()[:230])
