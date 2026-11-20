import json,subprocess
G=lambda *a: subprocess.check_output(['git','-C','<aux>',*a])
rj=json.loads(G('show','953af02:automation/coordination/reviews/qwen-peer-group-01/report.json'))
for k,v in rj.items():
    if k not in ('review','audit','raw_visible_model_output'): print(k,json.dumps(v,ensure_ascii=False)[:400])
print('claves:',sorted(rj))
s=json.loads(G('show','953af02:automation/coordination/reviews/qwen-peer-group-01/sources.json'))
src={x['id']:x['text'] for x in s['sources']}
rev=None
for k in rj:
    if isinstance(rj[k],dict) and 'findings' in rj[k]: rev=rj[k]
    if isinstance(rj[k],str) and '"findings"' in rj[k]:
        try: rev=json.loads(rj[k])
        except: pass
print('--- citas de Claude API')
for f in rev['findings']:
    print(f['source_id'], 'cita_literal_en_fuente=', f['quote'] in src[f['source_id']], '|', f['quote'][:90])
cas=src['s00']; f4=src['s06']
for frag in ['no se presenta como apta para dinero real','no se presenta como apta.','no se presenta como apta mientras no se resuelva','Margen EBITDA estimado por el analista: 18%. Estimacion interna; no es cifra publicada','dinero real']:
    print(repr(frag),'apariciones casos=',cas.count(frag),'fixture f1_004=',f4.count(frag))
for i,l in enumerate(cas.splitlines(),1):
    if 'dinero real' in l: print(' linea',i,json.loads(l)['id'],'contiene "dinero real" en campos:',[k for k,v in json.loads(l).items() if 'dinero real' in json.dumps(v,ensure_ascii=False)])
