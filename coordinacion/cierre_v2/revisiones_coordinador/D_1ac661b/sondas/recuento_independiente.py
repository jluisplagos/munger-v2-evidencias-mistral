"""Recuento independiente de la matriz de 36 desde la evidencia (revisor, no autor).
Uso: python3 -I recuento_independiente.py <dir ejecucion_d> <dir banco_revisado> <salida.json>
No ejecuta el producto: solo lee especificaciones, resultado_ejecucion.json, logs y banco."""
import json, os, sys, glob, csv, collections
D, B, OUT = sys.argv[1:4]
casos = [json.loads(l) for l in open(os.path.join(B, 'casos_aceptacion.jsonl'), encoding='utf-8') if l.strip()]
specs = {}
for f in glob.glob(os.path.join(D, 'scripts/especificaciones/*/*.json')):
    if f.endswith('adaptaciones.json'):
        continue
    s = json.load(open(f, encoding='utf-8')); specs[s['id']] = (f, s)
matriz = {r['id']: r for r in csv.DictReader(open(os.path.join(D, 'MATRIZ_EJECUCION.csv'), encoding='utf-8'))}
filas, cat = [], collections.Counter()
tot_crit = 0
incoherencias = []
for c in casos:
    cid = c['id']
    rp = os.path.join(D, 'evidencias', cid, 'resultado_ejecucion.json')
    res = json.load(open(rp, encoding='utf-8')) if os.path.isfile(rp) else None
    log = os.path.join(D, 'evidencias', cid, 'ejecucion.log')
    nlog = open(log, encoding='utf-8').read().count('\n# Caso ') + (1 if os.path.isfile(log) and open(log, encoding='utf-8').read().startswith('# Caso') else 0) if os.path.isfile(log) else 0
    fila = {'id': cid, 'naturaleza': c['naturaleza'], 'n_criterios_banco': len(c['criterios_observables']),
            'spec': bool(specs.get(cid)), 'resultado': bool(res), 'ejecuciones_en_log': nlog}
    if res:
        pasos = res['pasos']
        prod = [p for p in pasos if p.get('comando')]
        fila['comandos_producto'] = len(prod)
        fila['exits'] = [p['exit'] for p in prod]
        fila['estado_caso'] = res['estado_caso']
        crits = res.get('criterios', [])
        fila['criterios_arnes'] = [(x['id'], x['estado']) for x in crits]
        tot_crit += len(crits)
        s = specs[cid][1]
        fila['precond_simulada_verificada'] = any(p.get('comprobacion') == 'verificada' for p in s['pasos'])
        fila['sellar_con_revisor_arnes'] = any(p['op'] == 'sellar' for p in s['pasos'])
        # coherencia stdout guardado vs archivo
        for p in prod:
            g = p.get('guardado_en')
            if g:
                fp = os.path.join(D, 'evidencias', cid, g)
                if not os.path.isfile(fp):
                    incoherencias.append(f'{cid}: falta {g}')
                elif not open(fp, encoding='utf-8').read().endswith(p['stdout']):
                    incoherencias.append(f'{cid}: {g} no coincide con stdout registrado')
        sinprod = [p for p in s['pasos'] if p['op'] == 'preparar_cambio']
        if cid == 'Q1-026':
            k = 'ENTORNO (comando real con fallo esperado de entorno; ningún criterio del banco observado)'
        elif fila['precond_simulada_verificada'] or fila['sellar_con_revisor_arnes']:
            k = 'COMPONENTE_REAL_CON_PRECONDICION_SIMULADA (relevo de agente)'
        else:
            k = 'COMPONENTE_REAL_SIN_PRECONDICION_SIMULADA (relevo de agente)'
    else:
        obs = matriz[cid]['observacion_compartida']
        if c['naturaleza'] == 'DECISION_PENDIENTE':
            k = 'DECISION_PENDIENTE (sin ejecutar)'
        elif obs and obs != '-':
            k = 'OBSERVACION_COMPARTIDA (sin ejecución propia)'
        else:
            k = 'PENDIENTE (sin ejecución, relevo)'
    fila['categoria'] = k
    cat[k] += 1
    filas.append(fila)
out = {'casos': len(casos), 'categorias': dict(cat), 'criterios_arnes_total': tot_crit,
       'criterios_banco_total': sum(len(c['criterios_observables']) for c in casos),
       'casos_con_mas_de_una_ejecucion_en_log': [f['id'] for f in filas if f.get('ejecuciones_en_log', 0) > 1],
       'incoherencias_stdout_archivo': incoherencias,
       'ejecucion_real_del_personaje': 0,
       'filas': filas}
json.dump(out, open(OUT, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(json.dumps({k: v for k, v in out.items() if k != 'filas'}, ensure_ascii=False, indent=1))
