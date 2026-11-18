#!/usr/bin/env python3
"""(revisor, ronda 2) Para cada expediente: vigencia oficial (cierre_v2.motivo_vigencia), vigencia F1 y resultado de la puerta de hoja_resumen
(leer_expediente), sin LibreOffice."""
import sys, os, json
SC = '/tmp/claude-0/revision_hoja_r2/limpia/munger_v2_r1/personaje_v2/scripts'
sys.path.insert(0, SC); sys.dont_write_bytecode = True
import hoja_resumen as H, cierre_v2 as CIE, pipeline as PIPE, motor_a_f1 as F1
for exp in sys.argv[1:]:
    e = os.path.basename(os.path.abspath(exp))
    try:
        mv = CIE.motivo_vigencia(exp, PIPE.Pipeline.veredicto_auditoria, e)
    except Exception as ex:
        mv = f'EXCEPCIÓN {type(ex).__name__}: {ex}'
    try:
        f1 = F1.vigencia(exp)
    except Exception as ex:
        f1 = {'error': str(ex)}
    try:
        d, libro, huellas = H.leer_expediente(exp)
        puerta = 'ABIERTA'
    except H.ErrorExpediente as ex:
        puerta = 'CERRADA: ' + str(ex)[:230]
    try:
        f = json.load(open(os.path.join(exp, 'ficha.json'), encoding='utf-8'))
    except Exception:
        f = {}
    print(f"{os.path.basename(os.path.dirname(os.path.abspath(exp))):22} estado {str(f.get('estado_analisis')):24} cubo {str(f.get('cubo')):8} cv {str(os.path.isfile(os.path.join(exp,'cierre_vigente.json'))):5} "
          f"| vigencia oficial: {'vigente' if mv is None else 'NO: ' + str(mv)[:90]} | F1: motor {f1.get('motor')} exigido {f1.get('exigido')} exento {'sí' if f1.get('exento') else 'no'} | puerta de la hoja: {puerta}")
