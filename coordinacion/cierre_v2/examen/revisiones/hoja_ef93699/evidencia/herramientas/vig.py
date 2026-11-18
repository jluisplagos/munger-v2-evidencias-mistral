import sys, os
sys.path.insert(0, '/tmp/claude-0/revision_hoja/pkg/munger_v2_r1/personaje_v2/scripts'); sys.dont_write_bytecode = True
import cierre_v2 as CIE, pipeline as PIPE
c = sys.argv[1]
print('   vigencia oficial (cierre_v2.motivo_vigencia):', CIE.motivo_vigencia(c, PIPE.Pipeline.veredicto_auditoria))
if len(sys.argv) > 2 and sys.argv[2] == 'asegurar':
    m, arch = CIE.asegurar_vigencia(c, PIPE.Pipeline.veredicto_auditoria, None, None)
    print('   asegurar_vigencia →', (m or '')[:200], '| archivado en:', arch and os.path.relpath(arch, c))
