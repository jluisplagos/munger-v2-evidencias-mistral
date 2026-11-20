import json,subprocess
G=lambda *a: subprocess.check_output(['git','-C','<aux>',*a])
for D in ['qwen-bank-group-01','qwen-peer-group-01']:
    s=json.loads(G('show','953af02:automation/coordination/reviews/%s/sources.json'%D))
    for src in s['sources']:
        p=src['path']
        if p.startswith('reviews/'):
            print(D,p,'(informe Mistral; se coteja abajo)'); continue
        orig=G('show','4745f38:'+p).decode()
        if p.endswith('casos_aceptacion.jsonl'):
            ref='\n'.join(orig.splitlines()[:6])
            ok = src['text'].strip()==ref.strip()
        else:
            ok = src['text']==orig
        blob=G('rev-parse','4745f38:'+p).decode().strip()
        print(D,p,'texto_igual_a_4745f38=',ok,'blob_4745f38=',blob[:12],'blob_declarado=',src.get('original_git_blob','-')[:12])
# mistral_review en peer == review en report.json de Mistral?
s=json.loads(G('show','953af02:automation/coordination/reviews/qwen-peer-group-01/sources.json'))
mr=[x for x in s['sources'] if x['id']=='mistral_review'][0]['text']
rep=json.loads(G('show','953af02:automation/coordination/reviews/qwen-bank-group-01/postprocessed_report.json'))
rj=json.loads(G('show','953af02:automation/coordination/reviews/qwen-bank-group-01/report.json'))
print('report.json keys:',sorted(rj.keys()))
try:
    print('mistral_review == postprocessed.review :', json.loads(mr)==rep['review'])
except Exception as e: print('mistral_review no JSON:',e, mr[:200])
raw=json.loads(rj['raw_visible_model_output'])
print('raw_visible == postprocessed.review :', raw==rep['review'])
# cita recompuesta
plan=G('show','4745f38:resultados_qwen/q1_v2/banco_revisado/PLAN_DE_EJECUCION.md').decode()
adj=rep['citation_layout_adjustments'][0]
print('slice[source_start:source_end] (caracteres) == verbatim:', plan[adj['source_start']:adj['source_end']]==adj['verbatim_source_quote'])
import re
print('verbatim con espacios colapsados == cita del modelo:', re.sub(r'\s*\n\s*',' ',adj['verbatim_source_quote'])==adj['model_quote'])
print('cita modelo literal en plan:', adj['model_quote'] in plan)
