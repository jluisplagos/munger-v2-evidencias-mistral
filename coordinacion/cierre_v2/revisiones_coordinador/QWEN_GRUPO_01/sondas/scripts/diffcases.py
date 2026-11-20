import json,subprocess,sys
def load(p):
    t=subprocess.check_output(['git','-C','<aux>','show','4745f38:'+p]).decode()
    return {json.loads(l)['id']:json.loads(l) for l in t.splitlines() if l.strip()}
a=load('resultados_qwen/q1_v2/recibido/casos_aceptacion.jsonl'); b=load('resultados_qwen/q1_v2/banco_revisado/casos_aceptacion.jsonl')
for i in ['Q1-00%d'%k for k in range(1,7)]:
    ch=[k for k in sorted(set(a[i])|set(b[i])) if a[i].get(k)!=b[i].get(k)]
    print(i,'campos distintos recibido->revisado:',ch)
    for k in ch: print('  RECIBIDO',k,json.dumps(a[i].get(k),ensure_ascii=False)); print('  REVISADO',k,json.dumps(b[i].get(k),ensure_ascii=False))
