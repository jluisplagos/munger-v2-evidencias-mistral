import json,subprocess
G=lambda *a: subprocess.check_output(['git','-C','<aux>',*a])
rep=json.loads(G('show','953af02:automation/coordination/reviews/qwen-bank-group-01/postprocessed_report.json'))
rj=json.loads(G('show','953af02:automation/coordination/reviews/qwen-bank-group-01/report.json'))
raw=json.loads(rj['raw_visible_model_output']); pp=rep['review']
def diff(a,b,p=''):
    if type(a)!=type(b): print('TIPO',p); return
    if isinstance(a,dict):
        for k in sorted(set(a)|set(b)): diff(a.get(k),b.get(k),p+'/'+k)
    elif isinstance(a,list):
        if len(a)!=len(b): print('LONG',p,len(a),len(b))
        for i,(x,y) in enumerate(zip(a,b)): diff(x,y,p+'[%d]'%i)
    elif a!=b: print('DIFIERE',p); print('  raw :',repr(a)); print('  post:',repr(b))
diff(raw,pp)
print('postprocessed.raw_visible_model_output == report.raw_visible:', rep.get('raw_visible_model_output')==rj['raw_visible_model_output'])
# todas las citas de Mistral: literales en su fuente?
for sec in ['cases','findings']:
    for x in pp[sec]:
        src=G('show','4745f38:'+x['source_path']).decode()
        print(sec, x.get('id',x.get('cases')), 'cita_literal=',x['quote'] in src)
