"""Sonda D3: NORMAL del fixture C_orig con la replica independiente y con C15 = 0,40 (payout mal puesto).
Uso: python3 -I sonda_d3_fixture_c.py <Fixture_motorC_original.xlsx>   (solo lectura, openpyxl)"""
import sys, openpyxl
from fractions import Fraction as F
wb = openpyxl.load_workbook(sys.argv[1], data_only=False, read_only=True)
def v(h, c):
    x = wb[h][c].value
    return x
H, P, A = 'Historia', 'Palancas', 'Análisis'
B0, BN = v(H, 'L21'), v(H, 'L9')
print('Historia L9, L21 =', BN, B0)
for c in 'BCD':
    print(c, 'X14,X15,X16,X18 =', [v(P, f'{c}{r}') for r in (14, 15, 16, 18)], 'Análisis X68,X69 =', v(A, f'{c}68'), v(A, f'{c}69'))
print('Análisis C55, C56 =', v(A, 'C55'), v(A, 'C56'), '· Palancas C22, C23 =', v(P, 'C22'), v(P, 'C23'), '· C62 =', v(A, 'C62'))
def motor_c(B0, ROE0, g1, mT, ginf, roe_lp, r, p=0, rec=0, acc=1):
    B0, ROE0, g1, mT, ginf, roe_lp, r, p, rec, acc = (F(str(x)) for x in (B0, ROE0, g1, mT, ginf, roe_lp, r, p, rec, acc))
    L = [B0]; pv = F(0)
    for t in range(1, 11):
        g = g1 if t <= 5 else g1 - (g1 - ginf) * F(t - 5, 5)
        L.append(L[-1] * (1 + g)); m = ROE0 + (mT - ROE0) * F(min(t, 5), 5)
        pv += (L[t - 1] * m - (L[t] - L[t - 1])) / (1 + r) ** t
    bi = pv + L[10] * (roe_lp - ginf) / (r - ginf) / (1 + r) ** 10
    return ((1 - p) * bi + p * rec) / acc
ROE0 = F(str(BN)) / F(str(B0))
res = {}
for c in 'BCD':
    res[c] = motor_c(B0, ROE0, v(P, f'{c}14'), v(P, f'{c}15'), v(A, f'{c}68'), v(P, f'{c}18'), v(A, 'C56'),
                     v(P, 'C22') or 0, v(P, 'C23') or 0, v(A, 'C55'))
    print(f'{c}78 replica = {float(res[c]):.10f}')
mal = motor_c(B0, ROE0, v(P, 'C14'), 0.40, v(A, 'C68'), v(P, 'C18'), v(A, 'C56'), v(P, 'C22') or 0, v(P, 'C23') or 0, v(A, 'C55'))
print(f'NORMAL con C15 = 0,40: {float(mal):.4f} (x{float(mal / res["C"]):.4f})')
