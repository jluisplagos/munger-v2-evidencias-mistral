#!/usr/bin/env python3
"""(revisor, ronda 2) Bloque «Qué concluye el análisis» + aptitud + salvedades que compondría la hoja v2, sin LibreOffice (la fila de la tasa
del análisis se toma de precio.json; solo para leer el veredicto)."""
import sys, os, json
SC = '/tmp/claude-0/revision_hoja_r2/limpia/munger_v2_r1/personaje_v2/scripts'
sys.path.insert(0, SC); sys.dont_write_bytecode = True
import hoja_resumen as H
ante = '--antecedente' in sys.argv
for exp in [a for a in sys.argv[1:] if not a.startswith('--')]:
    print('=' * 120); print(os.path.basename(os.path.dirname(os.path.abspath(exp))))
    try:
        d, libro, huellas = H.leer_expediente(exp, antecedente=ante)
    except H.ErrorExpediente as e:
        print('   PUERTA CERRADA:', str(e)[:300]); continue
    pr = d['precio.json']
    filas = [dict({k: pr.get(k) for k in ('precio_si', 'ponderado', 'zona', 'V', 'precio', 'g_impl_actual')}, r=0.09)] if 'precio_si' in pr else []
    md, t = H.componer(exp, d, libro, huellas, filas, 0.09, True, {})
    ini = md.index('## Qué concluye el análisis'); fin = md.index('## Por qué')
    cab = md[:ini].strip().splitlines()
    print('\n'.join(l for l in cab if l.startswith('>'))[:900])
    print(md[ini:fin].rstrip())
