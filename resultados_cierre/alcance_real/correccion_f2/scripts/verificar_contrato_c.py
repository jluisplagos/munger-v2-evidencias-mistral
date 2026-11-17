"""Verificacion numerica del contrato C corregido (F2-D3 / F3-R5..R8) contra el producto.

Replica en Python puro (sin LibreOffice ni pipeline) el motor C de munger-v2 @ 957af65:
  - build_v6.py: 927 L_t=L(t-1)*(1+g_t); 928 m_t=D+(F-D)*MIN(t,5)/5; 929-930 flujo C
    = L(t-1)*m_t - (L_t-L(t-1)); 926 g_t baja en linea recta de g1 a g_inf en los anos 6-10;
    931 BE=VP flujos; 932-934 BF/BG/BH terminal = L10*(ROE_lp-g_inf)/(r-g_inf)/(1+r)^10;
    935 BI; 936 BJ=(1-p)*BI+p*rec (quiebra, p=Palancas C22, rec=C23); 937 BK=BJ/acciones;
    960-962 tau=f=ajuste=0 en C; 963 r=Analisis C56 en C; 581-582 motor desde Analisis C62.
  - test_fill.py: 79 ROE0=L9/L21; 84,93 m_t; 86-88 tau/f/adj=0 en C; 94-95 flujo C; 99-100,103 terminal; 104.
Comprueba: (1) puente correcto (dividendos restan); (2) ROE = BN/patrimonio de cierre, no BAI/medio;
(3) identidad flujo = B(t-1)*ROE - dB solo con excedente limpio (variante con OCI); (4) ROE de cierre
vs apertura; (5) B15 como ROE objetivo (no payout); (6) quiebra BJ aplica en C.
Uso: python3 -I verificar_contrato_c.py   (sin argumentos; valores ilustrativos, no propuestos)
"""
import sys
from fractions import Fraction as F


def valor_c(B0, ROE0, g1, roe_obj, ginf, roe_lp, r, p=F(0), rec=F(0)):
    B0, ROE0, g1, roe_obj, ginf, roe_lp, r = (F(x) for x in (B0, ROE0, g1, roe_obj, ginf, roe_lp, r))
    L = [B0]
    flows = []
    for t in range(1, 11):
        g = g1 if t <= 5 else g1 - (g1 - ginf) * F(t - 5) / 5
        L.append(L[-1] * (1 + g))
        m = ROE0 + (roe_obj - ROE0) * F(min(t, 5)) / 5
        flows.append(L[t - 1] * m - (L[t] - L[t - 1]))
    pv = sum(x / (1 + r) ** t for t, x in enumerate(flows, 1))
    tv = L[10] * (roe_lp - ginf) / (r - ginf) / (1 + r) ** 10
    bi = pv + tv
    return (1 - p) * bi + p * rec, bi


def main():
    ok = True

    print('== 1. Puente de patrimonio: los dividendos RESTAN (el contrato viejo los sumaba) ==')
    E0, BN, impuesto, div, OCI, recompras, ampl = F(1000), F(100), F(30), F(40), F(0), F(0), F(0)
    BAI = BN + impuesto
    e1_real = E0 + BN + OCI - div - recompras + ampl
    e1_viejo = E0 + BAI + OCI + div - recompras + ampl
    print(f'  E0=1000, BN=100, impuesto=30 (BAI=130), dividendos=40, OCI=0')
    print(f'  E1 real = E0+BN+OCI-dividendos-recompras+ampliaciones+otros = {e1_real}')
    print(f'  puente viejo (sumaba BAI y dividendos) = {e1_viejo}; "otros" absorberia {e1_real - e1_viejo}')
    ok &= (e1_real == 1060 and e1_viejo == 1170)

    print('== 2. ROE del producto: BN (Historia fila 9) / patrimonio de CIERRE (fila 21) ==')
    roe_cierre = BN / e1_real
    roe_apertura = BN / E0
    roe_viejo = BAI / ((E0 + e1_real) / 2)
    print(f'  ROE cierre (L9/L21) = {float(roe_cierre):.6f} ({float(roe_cierre)*100:.3f} %)')
    print(f'  ROE sobre apertura = {float(roe_apertura):.6f}  <- el motor aplica m_t a la APERTURA (convencion del producto)')
    print(f'  ROE contrato viejo (BAI/patrimonio medio) = {float(roe_viejo):.6f}')
    ok &= abs(float(roe_cierre) - 0.094340) < 5e-7 and abs(float(roe_viejo) - 0.126214) < 5e-7

    print('== 3. Identidad flujo_t = B(t-1)*ROE_t - dB_t; dividendo = BN - dB SOLO con excedente limpio ==')
    B0, ROE0, g = F(1000), F(10, 100), F(3, 100)
    dB = B0 * g
    print(f'  Caso limpio (OCI=0): B0=1000, ROE0=10%, g=3% -> dB=30, flujo=70, dividendo=BN-dB=70 OK')
    ok &= (dB == 30 and B0 * ROE0 - dB == 70)
    E0v, BNv, OCIv, divv, recv = F(1000), F(100), F(-25), F(40), F(10)
    e1v = E0v + BNv + OCIv - divv - recv
    print(f'  Variante OCI=-25, recompras=10: E1 = {e1v}; BN-dB = {BNv - (e1v - E0v)} pero reparto real = {divv + recv}; diferencia = {BNv - (e1v - E0v) - (divv + recv)} = -OCI (el motor NO proyecta OCI)')
    ok &= (e1v == 1025 and BNv - (e1v - E0v) == 75 and divv + recv == 50)

    print('== 4. Palancas B15 se lee como ROE objetivo (NO como payout) ==')
    v_ok, _ = valor_c(100, '0.10', '0.03', '0.10', '0.02', '0.10', '0.09')
    v_mal, _ = valor_c(100, '0.10', '0.03', '0.40', '0.02', '0.10', '0.09')
    print(f'  B15 = ROE objetivo 10%: BI = {float(v_ok):.2f}')
    print(f'  B15 con payout 40% (leido como ROE objetivo 40%): BI = {float(v_mal):.2f} (x{float(v_mal / v_ok):.2f})')
    ok &= abs(float(v_ok) - 115.06) < 0.01 and abs(float(v_mal) - 278.45) < 0.01 and abs(float(v_mal / v_ok) - 2.42) < 0.01

    print('== 5. Quiebra BJ = (1-p)*BI + p*rec TAMBIEN aplica en el motor C (Palancas C22/C23; build_v6.py:936) ==')
    v_q, bi = valor_c(100, '0.10', '0.03', '0.10', '0.02', '0.10', '0.09', p=F(10, 100), rec=F(20))
    print(f'  p=10%, rec=20 sobre el ejemplo anterior: BI={float(bi):.2f} -> BJ={float(v_q):.2f} (antes de quiebra {float(bi):.2f})')
    ok &= abs(float(v_q) - 105.55) < 0.01

    print()
    print('RESULTADO:', 'TODO CUADRA' if ok else 'HAY DIFERENCIAS')
    sys.exit(0 if ok else 1)


if __name__ == '__main__':
    main()
