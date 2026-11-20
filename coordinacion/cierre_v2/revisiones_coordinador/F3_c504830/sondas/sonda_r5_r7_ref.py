"""F3-R5/R7: lee las fórmulas reales de referencia_V6.3.json y evalúa el contraejemplo y la quiebra.
Uso: python3 -I sonda_r5_r7_ref.py <referencia_V6.3.json>"""
import json, sys
from fractions import Fraction as F
ref = json.load(open(sys.argv[1], encoding='utf-8'))
f = ref.get('formulas', ref)
def get(k):
    for cand in (f, ref):
        if isinstance(cand, dict) and k in cand:
            v = cand[k]
            return v if isinstance(v, str) else json.dumps(v, ensure_ascii=False)
    return None
for k in ['Diagnóstico V6!C5', 'Diagnóstico V6!C6', 'Motor!BJ7', 'Motor!N7', 'Motor!O7', 'Motor!Q7', 'Motor!BK7']:
    print(f'{k}: {get(k)}')
c5 = get('Diagnóstico V6!C5') or ''
print('C5 contiene "Palancas":', 'Palancas' in c5)
# Contraejemplo R5 evaluado con la lógica literal de C5/C6
def motor(c62):
    return {'Sí': 'A', 'No · financiación cambia mucho': 'B', 'No · banco o aseguradora': 'C',
            'No · banco, aseguradora o regulada': 'C', '': ''}.get(c62, '—')
m = motor('Sí'); print('C62=«Sí», C6=Financiera -> motor', m, '| C6 REVISAR:', m != 'C', '| V11 NOA:', m in ('A', 'B'))
# Quiebra R7 sobre el ejemplo de F (B0=100, ROE0=10 %, g1=3 %, ROE_obj=10 %, g∞=2 %, ROE_lp=10 %, r=9 %)
B0, R0, g1, Ro, gi, Rl, r = F(100), F(1, 10), F(3, 100), F(1, 10), F(2, 100), F(1, 10), F(9, 100)
L = [B0]; pv = 0
for t in range(1, 11):
    g = g1 if t <= 5 else g1 - (g1 - gi) * F(t - 5, 5)
    L.append(L[-1] * (1 + g)); m_ = R0 + (Ro - R0) * F(min(t, 5), 5)
    pv += (L[t-1] * m_ - (L[t] - L[t-1])) / (1 + r) ** t
BI = pv + L[10] * (Rl - gi) / (r - gi) / (1 + r) ** 10
p, rec = F(1, 10), F(20)
print(f'BI = {float(BI):.4f}; BJ = (1-p)·BI + p·rec = {float((1-p)*BI + p*rec):.4f}')
