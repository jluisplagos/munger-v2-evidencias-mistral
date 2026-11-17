"""Verificacion numerica del contrato C corregido (F2-D3) contra las formulas del producto.

Replica en Python puro (sin ejecutar LibreOffice ni el pipeline) las formulas del motor C de
munger-v2 @ 957af65:
  - munger_v2_r1/v6/scripts/V6.1/test_fill.py:79  B0, ROE0 = Historia fila 21, fila 9 / fila 21
  - test_fill.py:84,93-98  flujo C = B(t-1)*ROE_t - (B(t)-B(t-1)); terminal = B10*(ROE_lp-g)/(r-g)
  - build_v6.py:933-942     g_t, L_t=prev*(1+g), m_t, flujo_t (motor C), VP y valor terminal
Comprueba: (1) puente de patrimonio correcto (los dividendos restan) con el ejemplo del revisor;
(2) ROE = beneficio neto atribuible / patrimonio de cierre (NO BAI / patrimonio medio);
(3) efecto de rellenar Palancas B15 con un payout (se lee como ROE objetivo).
Uso: python3 -I verificar_contrato_c.py   (sin argumentos; valores ilustrativos, no propuestos)
"""
import sys
from fractions import Fraction as F


def valor_c(B0, ROE0, g1, roe_obj, ginf, roe_lp, r):
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
    return pv + tv


def main():
    ok = True

    print('== 1. Puente de patrimonio: los dividendos RESTAN (contrato viejo los sumaba) ==')
    E0, BN, impuesto, div, OCI, recompras, ampl = F(1000), F(100), F(30), F(40), F(0), F(0), F(0)
    BAI = BN + impuesto
    e1_real = E0 + BN + OCI - div - recompras + ampl
    e1_viejo = E0 + BAI + OCI + div - recompras + ampl
    print(f'  E0=1000, beneficio neto=100, impuesto=30 (BAI=130), dividendos=40')
    print(f'  E1 real (B(t)=B(t-1)+BN+OCI-dividendos-recompras+ampliaciones+otros) = {e1_real}')
    print(f'  puente del contrato viejo (sumaba BAI y dividendos) = {e1_viejo}; '
          f'"otros movimientos" tendria que absorber {e1_real - e1_viejo}')
    ok &= (e1_real == 1060 and e1_viejo == 1170)

    print('== 2. ROE del producto: beneficio neto atribuible (Historia fila 9) / patrimonio de cierre (fila 21) ==')
    roe_prod = BN / e1_real
    roe_viejo = BAI / ((E0 + e1_real) / 2)
    print(f'  ROE producto (L9/L21) = {float(roe_prod):.6f}   ROE contrato viejo (BAI/patrimonio medio) = {float(roe_viejo):.6f}')
    ok &= abs(float(roe_prod) - 0.094340) < 5e-7 and abs(float(roe_viejo) - 0.126214) < 5e-7

    print('== 3. Identidad del motor C: flujo_t = B(t-1)*ROE_t - dB_t ; dividendo = BN - dB ==')
    B0, ROE0, g = F(1000), F(10, 100), F(3, 100)
    dB = B0 * g
    flujo = B0 * ROE0 - dB
    print(f'  B0=1000, ROE0=10%, g=3%: dB={dB}, flujo_t={flujo}, dividendo=BN-dB={B0 * ROE0 - dB}')
    ok &= (dB == 30 and flujo == 70)

    print('== 4. Palancas B15 se lee como ROE objetivo (NO como payout) ==')
    v_ok = valor_c(100, '0.10', '0.03', '0.10', '0.02', '0.10', '0.09')
    v_mal = valor_c(100, '0.10', '0.03', '0.40', '0.02', '0.10', '0.09')
    print(f'  B15 = ROE objetivo 10%: valor = {float(v_ok):.2f}')
    print(f'  B15 rellenado con payout 40% (se lee como ROE objetivo 40%): valor = {float(v_mal):.2f} '
          f'(x{float(v_mal / v_ok):.2f})')
    ok &= abs(float(v_ok) - 115.06) < 0.01 and abs(float(v_mal) - 278.45) < 0.01 and abs(float(v_mal / v_ok) - 2.42) < 0.01

    print()
    print('RESULTADO:', 'TODO CUADRA' if ok else 'HAY DIFERENCIAS')
    sys.exit(0 if ok else 1)


if __name__ == '__main__':
    main()
