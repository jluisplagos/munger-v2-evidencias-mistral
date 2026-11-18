import sys, os, json
sys.path.insert(0, '/tmp/claude-0/revision_hoja_r2/limpia/munger_v2_r1/personaje_v2/scripts'); sys.dont_write_bytecode = True
import cierre_v2 as CIE, pipeline as PIPE
c = sys.argv[1]; e = os.path.basename(os.path.abspath(c))
print('   vigencia oficial (cierre_v2.motivo_vigencia):', CIE.motivo_vigencia(c, PIPE.Pipeline.veredicto_auditoria, e))
if len(sys.argv) > 2 and sys.argv[2] == 'asegurar':
    m, arch = CIE.asegurar_vigencia(c, PIPE.Pipeline.veredicto_auditoria, e, None)
    print('   asegurar_vigencia →', (m or '')[:160], '| archivado en:', arch and os.path.relpath(arch, c))
    if arch:
        print('   contenido del archivo:', sorted(os.listdir(arch)))
        r = json.load(open(os.path.join(arch, 'RETIRADA.json'), encoding='utf-8'))
        print('   RETIRADA.json → claves:', sorted(r), '· hoja_resumen_no_vigente:', r.get('hoja_resumen_no_vigente'))
        p = os.path.join(arch, 'HOJA_RESUMEN_NO_VIGENTE.json')
        if os.path.isfile(p): print('   HOJA_RESUMEN_NO_VIGENTE.json:', json.dumps(json.load(open(p, encoding='utf-8')), ensure_ascii=False)[:330])
