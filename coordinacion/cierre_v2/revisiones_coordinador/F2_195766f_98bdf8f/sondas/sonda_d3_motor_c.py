"""Sonda D3 (revisor): replica independiente del motor C desde las formulas de
referencia_V6.3.json (Motor!Q7, AA7, AK7, AU7, BE7, BF7, BG7, BH7, BJ7, BK7), no desde el
script del autor. Uso: python3 -I sonda_d3_motor_c.py <referencia_V6.3.json>
Comprueba: (1) que las formulas de REF son las que se replican (texto exacto);
(2) puente 1000 + 100 - 40 = 1060 y ROE de cierre 100/1060;
(3) el ejemplo del autor (B0=100, ROE0=10 %, g1=3 %, g_inf=2 %, ROE_lp=10 %, r=9 %): 115,06 y,
con B15 = 0,40, 278,45 (x2,42); (4) efecto de la quiebra (Palancas C22/C23) que el contrato del
autor omite; (5) contraejemplo de seleccion: Palancas C6 no entra en Diagnostico C5.
"""
import json, sys
from fractions import Fraction as F

ref = json.load(open(sys.argv[1], encoding='utf-8'))['formulas']
esperado = {
 'Motor!Q7': '=IF($BS7,IF(Q$3<=5,$E7,$E7-($E7-$H7)*(Q$3-5)/5),"")',
 'Motor!AA7': '=IF($BS7,$C7*(1+Q7),"")',
 'Motor!AK7': '=IF($BS7,$D7+($F7-$D7)*MIN(AK$3,5)/5,"")',
 'Motor!AU7': '=IF($BS7,IF($B7="C",$C7*AK7-(AA7-$C7),AA7*(AK7*(1-$K7)-$L7)-(AA7-$C7)/$G7),"")',
 'Motor!BE7': '=IF($BS7,SUMPRODUCT(AU7:BD7/(1+$J7)^$AU$3:$BD$3),"")',
 'Motor!BF7': '=IF($BS7,IF($B7="C",AJ7*($I7-$H7),AJ7*(1+$H7)*($F7*(1-$K7)*(1-$H7/$I7)-$L7)),"")',
 'Motor!BG7': '=IF($BS7,BF7/($J7-$H7),"")',
 'Motor!BH7': '=IF($BS7,BG7/(1+$J7)^10,"")',
 'Motor!BJ7': '=IF($BS7,(1-$N7)*BI7+$N7*$O7,"")',
 'Motor!BK7': '=IF(AND($BS7,N($P7)>0),BJ7/$P7,"")',
 'Motor!N7': '=N(Palancas!$C22)', 'Motor!O7': '=N(Palancas!$C23)',
 'Historia!L34': '=IF(AND(ISNUMBER(L9),ISNUMBER(L21),N(L21)>0),L9/L21,"")',
}
fallos = 0
for k, v in esperado.items():
    ok = ref.get(k) == v
    fallos += not ok
    print(('OK  ' if ok else 'FALLO ') + k)
c5 = ref["Diagnóstico V6!C5"]
print('Diagnostico V6!C5 =', c5)
print('  ¿C5 lee Palancas C6?', 'Palancas' in c5, '· ¿lee Analisis C62?', 'C$62' in c5)

def motor_c(B0, ROE0, g1, mT, ginf, roe_lp, r, p=F(0), rec=F(0), acciones=F(1)):
    L = [B0]; pv = F(0)
    for t in range(1, 11):
        g = g1 if t <= 5 else g1 - (g1 - ginf) * F(t - 5, 5)      # Q7
        L.append(L[-1] * (1 + g))                                  # AA7
        m = ROE0 + (mT - ROE0) * F(min(t, 5), 5)                   # AK7
        pv += (L[t - 1] * m - (L[t] - L[t - 1])) / (1 + r) ** t    # AU7, BE7
    bh = L[10] * (roe_lp - ginf) / (r - ginf) / (1 + r) ** 10      # BF7, BG7, BH7
    bi = pv + bh                                                   # BI7 (ajuste 0 en C)
    bj = (1 - p) * bi + p * rec                                    # BJ7
    return bj / acciones                                           # BK7

E0, BN, imp, div = F(1000), F(100), F(30), F(40)
E1 = E0 + BN - div
print(f'Puente: 1000 + 100 - 40 = {E1}; ROE cierre = {float(BN/E1):.6f}; ROE apertura = {float(BN/E0):.6f}')
print(f'Puente viejo (BAI + dividendos): {E0 + BN + imp + div}')
args = dict(B0=F(100), ROE0=F(1, 10), g1=F(3, 100), ginf=F(2, 100), roe_lp=F(1, 10), r=F(9, 100))
v1 = motor_c(mT=F(1, 10), **args); v2 = motor_c(mT=F(4, 10), **args)
print(f'Ejemplo del autor: B15=0,10 -> {float(v1):.4f}; B15=0,40 -> {float(v2):.4f}; x{float(v2/v1):.4f}')
v3 = motor_c(mT=F(1, 10), p=F(1, 10), rec=F(20), **args)
print(f'Con quiebra p=10 %, recuperacion 20 (omitida en el contrato del autor): {float(v3):.4f} '
      f'frente a {float(v1):.4f} sin ella')
ok_num = abs(float(v1) - 115.06) < 0.005 and abs(float(v2) - 278.45) < 0.005 and E1 == 1060
print('RESULTADO:', 'OK' if (fallos == 0 and ok_num) else f'FALLOS {fallos}, numeros {ok_num}')
sys.exit(0 if (fallos == 0 and ok_num) else 1)
