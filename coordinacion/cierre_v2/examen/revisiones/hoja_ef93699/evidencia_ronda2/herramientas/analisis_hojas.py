#!/usr/bin/env python3
"""(revisor, ronda 2) Sobre las hojas v2 generadas: (a) cifras frente a mis recálculos independientes de la ronda 1; (b) tesis y tesis inversa
enteras; (c) avisos de la tasa; (d) fecha del precio; (e) longitud, jerga y glosario."""
import sys, os, json, re, glob
SC = '/tmp/claude-0/revision_hoja_r2/limpia/munger_v2_r1/personaje_v2/scripts'
sys.path.insert(0, SC); sys.dont_write_bytecode = True
import hoja_resumen as H
R = '/tmp/claude-0/revision_hoja_r2'; EV1 = '/home/user/e_work/revision_hoja/evidencia/cifras'
nombres = ['Elis_414','Vidrala_414','Viscofan_414','Vidrala_413_bloqueo','Vidrala_413_cond','Viscofan_413','Vidrala_412_bloqueo','Vidrala_412_cond','Viscofan_412','Vidrala_411','Vidrala_4101','Vidrala_461']
print('(a) CIFRAS · filas de la hoja v2 frente a los recálculos independientes de la ronda 1 (indep_*.json)')
n_ok = n = 0; mx = 0.0
for nom in ('Vidrala_414','Viscofan_414','Elis_414'):
    exp = glob.glob(f'{R}/exp/{nom}/*/hoja_resumen.json')[0]
    t = json.load(open(exp, encoding='utf-8'))
    for p in sorted(glob.glob(f'{EV1}/indep_{nom}_r[0-9][0-9][0-9].json')):
        a = json.load(open(p))
        f = [x for x in t['sensibilidad']['filas'] if abs(x['r'] - a['C56']) < 1e-9]
        if not f: continue
        f = f[0]; d = abs(a['precio_si'] - f['precio_si']); dv = max(abs(x - y) for x, y in zip(a['V'], f['V']))
        n += 1; n_ok += (d < 1e-9 and dv < 1e-9 and a['zona'] == f['zona']); mx = max(mx, d, dv)
        rop = a['r_operativa_C15']
        cok = (isinstance(rop, str) and not H.es_num(f.get('r_operativa_C15'))) or (H.es_num(rop) and abs(rop - f['r_operativa_C15']) < 1e-12)
        print(f"   {nom} {a['C56']:.2f}: precio de Sí revisor {a['precio_si']:.6f} · hoja v2 {f['precio_si']:.6f} · dif {d:.1e} · zona {a['zona']}/{f['zona']} · tasa de descuento (C15) igual: {cok} · aviso r mínima igual: {a['r_vs_minima_C18'] == f.get('r_vs_minima_C18')}")
print(f'   {n_ok}/{n} filas coinciden · diferencia máxima {mx:.1e}')
print()
print('(b)–(e) por hoja')
JERGA = ['ROIC','ROCE','EBIT','EBITDA','FCF','NOPAT','S2C','capex','cst','orgánico','apalancamiento','foso','terminal','ponderado','MALO','NORMAL','BUENO','p\\(MALO\\)','k = 3','escalera','cubo','zona','heredada','motor','ancla','NIIF','PPA','SBC','BPA','DSO','CDI','OCEANE','mm\\b','variantes?','λ','reposición','marginal','PM1','D10','P-M1','comprobación conjunta','F1','precio de Sí','valor medio','tasa']
for nom in nombres:
    d0 = glob.glob(f'{R}/exp/{nom}/*/')[0]
    md = open(d0 + 'hoja_resumen.md', encoding='utf-8').read(); t = json.load(open(d0 + 'hoja_resumen.json', encoding='utf-8'))
    fc = json.load(open(d0 + 'fase_c.json', encoding='utf-8')); ficha = json.load(open(d0 + 'ficha.json', encoding='utf-8'))
    falt = []
    for campo in ('B101', 'B102'):
        fs = [H.limpiar(x) for x in H.frases(H.obtener_campo(fc, campo))]
        falt += [(campo, i + 1) for i, x in enumerate(fs) if x and x not in md]
    n101, n102 = len(H.frases(H.obtener_campo(fc, 'B101'))), len(H.frases(H.obtener_campo(fc, 'B102')))
    filas = t['sensibilidad']['filas']
    bajo = [H.tasa_txt(f['r']) for f in filas if isinstance(f.get('r_vs_minima_C18'), str) and 'REVISAR' in f['r_vs_minima_C18']]
    en_tabla = md.count('la tasa queda por debajo de la mínima')
    a2 = [a.get('detalle') for a in ficha.get('avisos') or [] if isinstance(a, dict) and a.get('id') == 'A2']
    a2_hoja = 'queda por debajo de su tasa mínima de referencia' in md
    v = t['veredicto']
    cuerpo = md.split('## Palabras que pueden no ser conocidas')[0]
    jer = sum(len(re.findall(r'(?<![\wáéíóú])' + j, cuerpo)) for j in JERGA)
    refs = sorted(set(r for r in re.findall(r'(?<![\wÁÉÍÓÚáéíóú])(?:[A-L]\d{1,3}(?::[A-L]\d{1,3})?)(?![\w%])', cuerpo) if not r.startswith(('F1',))))
    gl = re.findall(r'^- \*\*(.+?):\*\*', md.split('## Palabras que pueden no ser conocidas')[1].split('## Para comprobar')[0], re.M) if '## Palabras' in md else []
    larga = max(len(re.findall(r'\w+', x)) for x in H.frases(' '.join(e['texto'] for e in t['por_que']['tesis'] + t['por_que']['tesis_inversa'])))
    print(f"== {nom}: {len(re.findall(chr(92)+'w+', md))} palabras · tesis {n101} frases y tesis inversa {n102}, todas en la hoja: {not falt}{'' if not falt else ' FALTAN ' + str(falt)} · frase más larga {larga} palabras")
    print(f"     concluye {v['concluye']} · precio de compra {v['precio_compra']} · precio de Sí de la hoja de cálculo {v['precio_si_hoja_de_calculo']:.2f} · fecha del precio {v['fecha_precio']} ({v['dias_precio_antes_del_analisis']} días antes del análisis; «Ojo» en la hoja: {'**Ojo:**' in md})")
    print(f"     tasas con aviso «por debajo de la mínima»: {bajo} (en la tabla: {en_tabla}) · aviso A2 en la ficha: {bool(a2)} → nota en la hoja: {a2_hoja} · «descuenta al» (motor B): {md.count('descuenta al')} · notas fijas (no es la conclusión / no es un suelo / regla experimental): {('no es la conclusión' in md, 'no es un suelo' in md, 'regla experimental' in md)}")
    print(f"     jerga en el cuerpo: {jer} apariciones · referencias a celdas que quedan: {refs[:10]} · glosario: {len(gl)} términos")
